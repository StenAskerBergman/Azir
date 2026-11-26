"""Build the Ixtal expedition crawlers and their native PDX animations."""

import argparse
from itertools import chain
from math import cos, pi, sin, sqrt, tau
from pathlib import Path
import random
import sys
import types
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw


BODY = "Body"
CUTTER_HEAD = "CutterHead"
DRUM = "Drum"
PIVOT = (0.0, 0.83, -1.20)
DRUM_CENTER = (0.0, .51, -1.94)
DRUM_OFFSET = tuple(center - root for center, root in zip(DRUM_CENTER, PIVOT))
TEETH = 8
MATERIALS = 16
IDENTITY = [0.0, 0.0, 0.0, 1.0]
LINKS = 32
RUN = 1.08
RADIUS = .417
TRACK_CENTER = .473
TRACK_X = 1.026
TRACK_HALF_WIDTH = .302
TRACK_LENGTH = 4 * RUN + tau * RADIUS
LINK_PITCH = TRACK_LENGTH / LINKS


def paint_polygon(mesh, points, normal, tangent, color):
    positions = mesh.get("p")
    for index in range(1, len(points) - 1):
        for corner in (0, index, index + 1):
            mesh.get("tri").append(len(positions) // 3)
            positions.extend(float(component) for component in points[corner])
            mesh.get("n").extend(normal)
            mesh.get("ta").extend([*tangent, 1.0])
            mesh.get("u0").extend([(color + 0.5) / MATERIALS, 0.5])


def contour_face(mesh, points, material):
    a, b, c = points[:3]
    u = [y - x for x, y in zip(a, b)]
    v = [y - x for x, y in zip(a, c)]
    cross = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])
    normal = tuple(x / sum(value*value for value in cross)**0.5 for x in cross)
    tangent = tuple(x / sum(value*value for value in u)**0.5 for x in u)
    paint_polygon(mesh, points, normal, tangent, material)


def bridge_rings(mesh, front, back, colors):
    contour_face(mesh, front, colors[0])
    contour_face(mesh, list(reversed(back)), colors[0])
    span(mesh, front, back, colors[1:])


def span(mesh, front, back, colors):
    for index in range(len(front)):
        next_index = (index + 1) % len(front)
        contour_face(mesh, [front[next_index], front[index], back[index], back[next_index]],
                     colors[index % len(colors)])


def section(x, z, width, bottom, top, bevel):
    """Clockwise cross section when looking toward the front of the machine."""
    return [(x+sx, y, z) for sx, y in (
        (-width+bevel,top),(width-bevel,top),(width,top-bevel),(width,bottom+bevel),
        (width-bevel,bottom),(-width+bevel,bottom),(-width,bottom+bevel),(-width,top-bevel),
    )]


def shell(mesh, x, cross_sections, cap, faces):
    rings = [section(x, *parameters) for parameters in cross_sections]
    contour_face(mesh, rings[0], cap)
    for front, rear in zip(rings,rings[1:]):
        span(mesh, front, rear, faces)
    contour_face(mesh, list(reversed(rings[-1])), cap)


def tube(mesh, start, end, radius, material, sides=10, end_material=None):
    axis = [b-a for a,b in zip(start,end)]
    length = sqrt(sum(v*v for v in axis))
    x,y,z = [v/length for v in axis]
    if abs(y) > .95:
        side = (1., 0., 0.)
    else:
        mag = sqrt(z*z+x*x)
        side = (z/mag, 0., -x/mag)
    normal = (y*side[2] - z*side[1], z*side[0] - x*side[2], x*side[1] - y*side[0])
    def ring(pos):
        return [tuple(p + radius*(cos(-tau*i/sides)*u + sin(-tau*i/sides)*v)
                      for p,u,v in zip(pos,side,normal)) for i in range(sides)]
    bridge_rings(mesh, ring(start), ring(end),
                 (material if end_material is None else end_material, material))


def visor(mesh):
    profile = [(0,.31),(.314,.154),(.314,-.154),(0,-.287),(-.314,-.154),(-.314,.154)]
    stack = []
    for scale, depth in ((1.24,0), (1.14,.045), (.96,.057), (.83,.078)):
        stack.append([(x*scale,1.67+y*scale,-.865+.49*y*scale-depth) for x,y in profile])
    for (outer,inner), color in zip(zip(stack,stack[1:]),(10,1,9),strict=True):
        span(mesh, inner, outer, (color,))
    rim = stack[-1]
    center = (-.019,1.69,-.953)
    for i,p in enumerate(rim):
        contour_face(mesh,(center,p,rim[(i+1)%6]), (4,4,4,9,4,4)[i])
    contour_face(mesh, [(-.19,1.73,-.95),(-.15,1.78,-.933),(-.03,1.823,-.915),
                        (-.083,1.783,-.929)], 8)


def add_hull(mesh, zaun):
    shell(mesh, 0, [(-1.40,.78,.36,.76,.13),(-.92,.94,.28,1.04,.16),
                    (.99,.97,.29,1.04,.17),(1.51,.78,.40,.89,.14)],
          11, (10,0,2,2,6,2,2,0))
    shell(mesh, 0, [(-.30,.52,.98,1.29,.13),(.70,.66,1.01,1.62,.13),
                    (1.49,.58,.91,1.39,.14)], 11, (2,10,11,2,2,2,11,10))
    # The armored cockpit is nested between the twin shoulder housings.
    outline = [(-.22,2.04),(.22,2.04),(.45,1.93),(.57,1.62),(.43,1.28),
               (-.43,1.28),(-.57,1.62),(-.45,1.93)]
    front = [(x,y,-.852+.49*(y-1.67)) for x,y in outline]
    crown = [(x*.89,y+(.38 if y>=1.90 else .13),.22) for x,y in outline]
    rear = [(x*.83,y+(.20 if y>=1.90 else .04),.90) for x,y in outline]
    contour_face(mesh, front, 11)
    span(mesh, front, crown, (0,1,10,9,11,9,10,1))
    span(mesh, crown, rear, (10,1,0,11,2,11,0,1))
    contour_face(mesh,rear[::-1],2)
    visor(mesh)
    shell(mesh,0,[(-1.09,.40,1.06,1.28,.06),(-.79,.53,1.07,1.32,.08)],
          11,(0,1,10,11))
    for idx in range(6):
        x=(idx-2.5)*.104
        shell(mesh,x,[(-1.128,.020,1.075,1.216,.008),(-1.085,.020,1.075,1.216,.008)],
              12,(2,))
    for side in (-1,1):
        x=side*.916
        shell(mesh,x,[(-1.52,.156,.72,1.05,.071),(-1.25,.251,.70,1.39,.088),
                      (-.59,.267,.76,1.64,.115),(.90,.268,.79,1.66,.115),
                      (1.31,.216,.80,1.46,.091)], 10,(0,1,10,11,2,11,10,1))
        for z in (-.22,.52):
            shell(mesh,x,[(z,.271,.797,1.52,.105),(z+.045,.271,.797,1.52,.105)],
                  10,(1,10,7,11))
        for i in range(3):
            z=-.48+i*.128
            face=[(side*1.189,.904,z),(side*1.189,.987,z+.026),
                  (side*1.189,.987,z+.096),(side*1.189,.904,z+.071)]
            contour_face(mesh,face if side>0 else face[::-1],8)
        tube(mesh,(side*.65,1.28,-.95),(side*.66,.85,-1.65),.096,2,end_material=1)
        tube(mesh,(side*.66,1.10,-1.28),(side*.66,.87,-1.62),.066,12,end_material=1)
        tube(mesh,(side*.65,1.27,-.96),(side*.65,1.21,-1.06),.115,1)
    shell(mesh,.0,[(.79,.28,1.42,1.81,.08),(1.36,.31,1.42,1.76,.08)],2,(2,11,2,11))
    for i in range(4):
        z=.84+i*.127
        shell(mesh,0,[(z,.305,1.70,1.802,.032),(z+.047,.305,1.70,1.802,.032)],10,(12,2))
    tube(mesh,(.56,1.37,1.07),(.56,1.94,1.07),.102,7 if zaun else 11,sides=8)
    tube(mesh,(.56,1.86,1.07),(.56,1.96,1.07),.133,1 if zaun else 2,sides=8)
    if zaun:
        add_zaun_refit(mesh)


def add_zaun_refit(mesh):
    # Visible external replacements differentiate captured vehicles at map scale.
    hose = [(.47,1.62,-.38),(.60,1.76,-.24),(.77,1.79,-.15),(.93,1.76,.04),
            (1.05,1.70,.29),(1.056,1.70,.63),(.93,1.72,.94),(.73,1.64,1.16)]
    for a,b in zip(hose,hose[1:]):
        tube(mesh,a,b,.069,7,sides=8,end_material=7)
    for a,b in ((hose[0],hose[1]),(hose[-1],hose[-2])):
        tube(mesh,a,tuple(x+(y-x)*.43 for x,y in zip(a,b)),.092,12,sides=8)
    shell(mesh,-.91,[(-.26,.269,1.52,1.69,.08),(.36,.266,1.53,1.70,.08)],7,(7,1,10,11))
    for x in (-1.06,-.76):
        for z in (-.20,.29):
            tube(mesh,(x,1.69,z),(x,1.717,z),.044,12,sides=6)


def add_running_gear(mesh):
    for side in (-1,1):
        x = side*TRACK_X
        outer = x + side*(TRACK_HALF_WIDTH-.038)
        inner = x - side*(TRACK_HALF_WIDTH-.025)
        for z,radius in ((-RUN,.365),(-.64,.21),(-.215,.21),
                         (.215,.21),(.64,.21),(RUN,.365)):
            y = TRACK_CENTER if radius>.3 else .289
            tube(mesh,(inner,y,z),(outer,y,z),radius,6,sides=14,end_material=2)
            tube(mesh,(outer,y,z),(outer+side*.036,y,z),radius*.72,11,sides=12,end_material=1)
            tube(mesh,(outer+side*.036,y,z),(outer+side*.071,y,z),radius*.53,2,sides=10,end_material=10)
            tube(mesh,(outer+side*.071,y,z),(outer+side*.104,y,z),radius*.17,1,sides=6)
        shell(mesh,x,[(-1.08,.22,.35,.64,.08),(1.10,.22,.35,.64,.08)],2,(2,6,2,11))


def add_cutter_head(mesh):
    # Leave the front and lower arc open so the toothed drum reads at map scale.
    shell(mesh,0,[(-2.20,.96,.88,1.04,.056),(-1.92,1.01,.84,1.14,.077),
                  (-1.54,.89,.74,1.05,.088)],10,(0,1,10,11,2,11,10,1))
    for side in (-1,1):
        shell(mesh,side*.925,[(-2.255,.095,.36,.99,.050),(-2.05,.161,.30,1.09,.074),
                               (-1.68,.150,.37,.94,.068)],10,(1,0,10,11,2,11,10,0))
        x=side*.965
        tube(mesh,(x-side*.15,.51,-1.94),(x+side*.128,.51,-1.94),.189,1,sides=12)
        tube(mesh,(x+side*.128,.51,-1.94),(x+side*.153,.51,-1.94),.134,8,sides=10)
        tube(mesh,(x+side*.153,.51,-1.94),(x+side*.181,.51,-1.94),.083,2,sides=8)
        for index in range(3):
            z=-2.109+index*.071
            panel=[(side*1.092,.759,z),(side*1.092,.852,z+.013),
                   (side*1.092,.852,z+.044),(side*1.092,.759,z+.031)]
            contour_face(mesh,panel if side>0 else panel[::-1],8)


def add_drum(mesh):
    _,y,z = DRUM_CENTER
    tube(mesh,(-.91,y,z),(.91,y,z),.343,2,sides=16,end_material=1)
    for ring,x in enumerate((-.76,-.51,-.255,0,.255,.51,.76)):
        tube(mesh,(x-.070,y,z),(x+.070,y,z),.386,11,sides=16,end_material=10)
        for index in range(TEETH):
            angle = tau*(index/TEETH + (.04 if ring%2 else 0.0))
            def wedge_point(dx,distance,along):
                return (x+dx, y+distance*cos(angle)-along*sin(angle),
                        z+distance*sin(angle)+along*cos(angle))
            tooth = [wedge_point(*dimensions) for dimensions in (
                (-.084,.341,-.089),(.084,.341,-.089),(.085,.377,.088),(-.085,.377,.088),
                (-.047,.503,.005),(.047,.503,.005),(.077,.429,.105),(-.077,.429,.105),
            )]
            for face, color in zip(((0,1,2,3),(4,7,6,5),(0,4,5,1),(1,5,6,2),
                                    (2,6,7,3),(3,7,4,0)),(2,12,10,11,5,11),strict=True):
                contour_face(mesh,[tooth[k] for k in face],color)


def track_pose(distance):
    """Return a link position and tangent frame on a closed stadium path."""
    travel = distance % TRACK_LENGTH
    center = TRACK_CENTER
    straight = 2 * RUN
    arc = pi * RADIUS
    if travel < straight:
        return (0.0, center + RADIUS, RUN - travel), 0.0
    travel -= straight
    if travel < arc:
        angle = -travel / RADIUS
        return (0.0, center + RADIUS*cos(angle), -RUN + RADIUS*sin(angle)), angle
    travel -= arc
    if travel < straight:
        return (0.0, center - RADIUS, -RUN + travel), -pi
    angle = -pi - (travel-straight) / RADIUS
    return (0.0, center + RADIUS*cos(angle), RUN + RADIUS*sin(angle)), angle


def add_tread_links(mesh, assignment):
    faces = ((0,1,2,3),(7,6,5,4),(1,0,4,5),(2,1,5,6),(3,2,6,7),(0,3,7,4))
    for link in range(LINKS):
        position, angle = track_pose(link * LINK_PITCH)
        count = len(mesh.get("p")) // 3
        for x_center in (-TRACK_X,TRACK_X):
            half = LINK_PITCH*.43
            corners = [
                (x_center+x, position[1]+y*cos(angle)-z*sin(angle),
                 position[2]+y*sin(angle)+z*cos(angle))
                for y in (.048,-.023)
                for x,z in [(-TRACK_HALF_WIDTH,-half),(-TRACK_HALF_WIDTH,half),
                            (TRACK_HALF_WIDTH,half),(TRACK_HALF_WIDTH,-half)]
            ]
            for index, face in enumerate(faces):
                color = (2 if link%2 else 13) if index==0 else 3
                contour_face(mesh,[corners[i] for i in face],color)
        assignment.extend([link+3] * (len(mesh.get("p"))//3 - count))


def surface_uvs(mesh, points):
    uv = mesh.get("u0")
    normals = mesh.get("n")
    for index, (x, y, z) in enumerate(points):
        nx, ny, nz = map(abs, normals[3*index:3*index+3])
        horizontal, vertical = (z, y) if nx >= max(ny, nz) else (x, z) if ny >= nz else (x, y)
        slot = int(uv[2*index] * MATERIALS)
        uv[2*index] = (slot + 0.075 + (horizontal + 2.65) * .161) / MATERIALS
        uv[2*index+1] = 0.075 + (vertical + 2.65) * .161


def finish_atlas(target, colors, weathering):
    output = Image.new("RGBA",(MATERIALS*128,256))
    rng = random.Random(990)
    for slot, color in enumerate(colors):
        mottles = Image.new("L", (16,32))
        mottles.putdata([rng.randrange(256) for _ in range(16*32)])
        broad = mottles.resize((128,256), Image.Resampling.BICUBIC).tobytes()
        strength = weathering * .25 if slot in (4,8,9) else weathering
        pixels = []
        for mottled in broad:
            tint = (mottled-127)/127 * strength + rng.randint(-4,4)
            pixels.append(tuple(max(0,min(255,int(channel+tint))) for channel in color)+(255,))
        finish = Image.new("RGBA", (128,256))
        finish.putdata(pixels)
        draw = ImageDraw.Draw(finish)
        if slot not in (4,6,8,9):
            scratch = tuple(min(255, channel + 27) for channel in color)+(255,)
            for _ in range(55):
                x, y = rng.randrange(124), rng.randrange(248)
                draw.line((x,y,x+rng.randint(1,3),y+rng.randint(2,7)), fill=scratch)
        output.paste(finish,(slot*128,0))
    output.save(target, pixel_format="DXT1")


def inverse_bind(position):
    return [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0,
            *(-component for component in position)]


def make_clips(model, write_animfile, read_meshfile):
    clips = (
        ("idle", 1, .005, .002, .04, .0, 0, 0),
        ("move", 3, .015, .008, .12, .025, 6, 0),
        ("work", 2, .012, .010, .0, .05, 2, 1),
    )
    frames = 32
    bind_poses = [track_pose(link * LINK_PITCH) for link in range(LINKS)]
    for clip, cycles, bounce, pitch, cutter_lift, cutter_travel, links_per_loop, turns in clips:
        animation = ET.Element("File", pdxasset=[1, 0])
        info = ET.SubElement(animation, "info", fps=[24.0], sa=[frames], j=[3+LINKS])
        ET.SubElement(info, BODY, sa=["tq"], t=[0.0]*3, q=IDENTITY, s=[1.0])
        lift_rotation = [sin(cutter_lift/2),0.0,0.0,cos(cutter_lift/2)]
        ET.SubElement(info, CUTTER_HEAD, sa=["q"], t=list(PIVOT), q=lift_rotation, s=[1.0])
        ET.SubElement(info, DRUM, sa=["q"], t=list(DRUM_OFFSET), q=IDENTITY, s=[1.0])
        for link, (position, _) in enumerate(bind_poses):
            ET.SubElement(info, f"Tread_{link:02}", sa=["tq"], t=list(position), q=IDENTITY, s=[1.0])
        translations, rotations = [], []
        for frame in range(frames):
            phase = tau * cycles * frame / (frames - 1)
            pulse = (1 - cos(phase)) / 2
            translations.extend([0.0, bounce * pulse, 0.0])
            for angle in (pitch*sin(phase), cutter_lift+cutter_travel*pulse, -tau*turns*frame/(frames-1)):
                rotations.extend([sin(angle/2), 0.0, 0.0, cos(angle/2)])
            progress = links_per_loop * frame / (frames - 1)
            for link, (_, base_angle) in enumerate(bind_poses):
                position, orientation = track_pose((link+progress) * LINK_PITCH)
                angle = (orientation - base_angle + pi) % tau - pi
                translations.extend(position)
                rotations.extend([sin(angle/2), 0.0, 0.0, cos(angle/2)])
        ET.SubElement(animation, "samples", t=translations, q=rotations)
        path = model / f"bramble_crawler_{clip}.anim"
        write_animfile(str(path), animation)
        result = read_meshfile(str(path))
        assert result.find("info").get("j") == [LINKS+3]
        assert len(result.find("samples").get("q")) == frames * 4 * (LINKS+3)


def build_model(zaun):
    scene = ET.Element("File", pdxasset=[1, 0])
    shape = ET.SubElement(ET.SubElement(scene,"object"),"BrambleCrawler")
    mesh = ET.SubElement(shape,"mesh",p=[],n=[],ta=[],u0=[],tri=[])
    add_hull(mesh,zaun)
    add_running_gear(mesh)
    assignment = [0] * (len(mesh.get("p"))//3)
    for bone, build in enumerate((add_cutter_head,add_drum),start=1):
        build(mesh)
        assignment.extend([bone] * (len(mesh.get("p"))//3 - len(assignment)))
    add_tread_links(mesh,assignment)
    indices = list(chain.from_iterable((bone,-1,-1,-1) for bone in assignment))
    coordinates = iter(mesh.get("p"))
    points = list(zip(coordinates,coordinates,coordinates,strict=True))
    surface_uvs(mesh,points)
    axes = list(zip(*points))
    ET.SubElement(mesh,"aabb",min=[min(axis) for axis in axes],max=[max(axis) for axis in axes])
    ET.SubElement(mesh,"material",shader=["PdxMeshStandard"],
                  diff=["bramble_crawler_zaun_finish.dds" if zaun else "bramble_crawler_piltover_finish.dds"],
                  n=["bramble_crawler_normal.dds"],spec=["bramble_crawler_spec.dds"])
    ET.SubElement(mesh,"skin",bones=[4],ix=indices,w=[1.0,0.0,0.0,0.0]*len(assignment))
    skeleton = ET.SubElement(shape,"skeleton")
    ET.SubElement(skeleton,BODY,ix=[0],tx=inverse_bind((0.0,0.0,0.0)))
    ET.SubElement(skeleton,CUTTER_HEAD,ix=[1],pa=[0],tx=inverse_bind(PIVOT))
    ET.SubElement(skeleton,DRUM,ix=[2],pa=[1],tx=inverse_bind(DRUM_CENTER))
    for link in range(LINKS):
        position,_ = track_pose(link*LINK_PITCH)
        ET.SubElement(skeleton,f"Tread_{link:02}",ix=[link+3],pa=[0],tx=inverse_bind(position))
    locators = ET.SubElement(scene,"locator")
    for name,pos in {
        "crawler_exhaust": [.56,1.96,1.07],
        "crawler_left_track": [-1.025,.16,.94],
        "crawler_right_track": [1.025,.16,.94],
    }.items():
        ET.SubElement(locators,name,p=pos,q=IDENTITY,pa=[BODY])
    for side,x in (("left",-.66),("right",.66)):
        ET.SubElement(locators,f"crawler_blade_{side}",p=[x,-.46,-1.14],
                      q=IDENTITY,pa=[CUTTER_HEAD])
    return scene


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdx_module", type=Path, help="Directory containing pdx_data.py")
    parser.add_argument("--model-dir", type=Path,
                        default=Path("gfx/models/units/pil_bramble_crawler"))
    args = parser.parse_args()
    module = types.ModuleType("io_pdx_mesh")
    module.__path__ = [str(args.pdx_module.resolve())]
    sys.modules[module.__name__] = module
    from io_pdx_mesh.pdx_data import read_meshfile, write_animfile, write_meshfile

    model = args.model_dir
    for suffix, zaun, weathering, colors in (
        ("animated",False,18,((113,80,65),(211,163,85),(58,58,64),(39,41,48),
                             (25,144,171),(169,124,72),(29,30,33),(134,97,69),
                             (93,229,247),(21,57,67),(142,108,84),(75,52,45),
                             (128,128,130),(76,73,75),(0,0,0),(0,0,0))),
        ("zaun",True,25,((62,95,70),(160,131,76),(62,64,62),(40,43,42),
                         (38,149,103),(159,125,72),(31,33,31),(194,107,54),
                         (134,242,143),(29,65,52),(84,111,77),(51,66,49),
                         (132,137,128),(88,89,74),(0,0,0),(0,0,0))),
    ):
        variant = build_model(zaun)
        texture = variant.find(".//material").get("diff")[0]
        finish_atlas(model/texture,colors,weathering)
        output = model / f"bramble_crawler_{suffix}.mesh"
        write_meshfile(str(output), variant)
        result = read_meshfile(str(output))
        assert result.find(".//mesh/skin").get("ix") == variant.find(".//mesh/skin").get("ix")
        assert len(result.find("locator")) == 5
    make_clips(model, write_animfile, read_meshfile)
    print(f"Exported two mesh variants, three clips and {LINKS} paired tread joints")


if __name__ == "__main__":
    main()
