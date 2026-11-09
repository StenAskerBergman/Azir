# Void Gate model handoff

The gate is a single landmark at the Void Rupture in state 91, province 2883. The existing open gate is the shape and scale reference for both new meshes. Use the actual mesh in `gfx/models/void_gate/void_gate_open.mesh` to establish the front, ground plane, footprint and center of the opening. Image 7 is a silhouette reference. Its camera angle is oblique.

## Shared geometry

- Block out both meshes over the final gate at the same scale, origin, ground contact and facing. Match the root contact points, the large rear rib, the smaller forward rib and the path through the mouth. This keeps the structure planted as the models swap.
- Use dark, layered chitin with weathered gray edges and traces of Shuriman sandstone at the feet. Keep enough contrast between the ribs and the opening to read at campaign-map zoom. Preserve the finished model's asymmetric outline.
- Supply separate mesh objects for the ribs, base rubble and emissive fissure insert so the importer can simplify the footprint or adjust the glow. Keep the glowing fissure within the landmark footprint. Give it a shallow, dark bottom so it reads as a cut in the ground on HOI4's flat terrain.

## Stage 1 — Construction, image 1

> An unfinished black chitin gate taking root in shattered Shuriman sandstone. Two broad roots climb into an asymmetric ribbed arch over an open ravine. A few short hooks project inward, with daylight between them. Thin violet seams run from the fissure into the roots. Keep the opening empty and expose the broken footing. This is the skeleton of the finished gate in the supplied model, seen from the same front.

Use the same two anchor feet and the same bend in the large rib as the final model. Leave space for the nested forward rib and the thick shell around the mouth to develop. The low violet glow comes from the ground and hairline seams.

## Stage 2 — First Rift, image 2

> The same gate after its first firing. The large rib has thickened and a smaller forward rib now curls toward it. The roots have pulled apart the sandstone and exposed the broken walls of the fissure. Use layered black plates, ochre fractures and narrow luminous veins. Keep the middle clear enough to see through. The gate has the outline of its final form, with room for the finished mouth and its sustained purple interior.

Keep both anchor feet and the opening aligned to stage 1. Carry the smaller rib forward toward its position on the finished mesh. Put the stronger glow in the fissure insert and inner seams. The pink mushroom cloud and the later violet storm belong to the event art.

## Import and event art

Export each mesh with its textures and a front and three-quarter preview. Verify against the current model in the HOI4 mesh exporter before converting to `.mesh` and DDS. Use `void_gate_construction` and `void_gate_first_rift` as asset stems. Add their `pdxmesh` registrations in `gfx/entities/void_gate.gfx` and bind them to `building_landmark_void_gate_construction` and `building_landmark_void_gate_first_rift` in `gfx/entities/void_gate.asset`. The construction placeholder's scale of 0.8 can be removed once the replacement matches the shared footprint.

| Event | Art brief | Picture binding |
| --- | --- | --- |
| Construction of the Void Gate Begins | Image 1, dormant arch and purple ground seams | `GFX_news_event_azir_gate_construction` |
| The First Rift Fires | Pink-white flash, rising column and a broad pink mushroom cloud over the arch | `GFX_news_event_azir_first_rift` |
| A Storm Over Icathia | Image 3, a sustained violet vortex three days later | `GFX_news_event_azir_rift_aftermath` |
| Kai'Sa Returns | Image 5, Kai'Sa silhouetted across a fissure | `GFX_news_event_azir_kaisa_returns` |
| The Sun Disc Shatters | Image 6, split imperial disc above the fallen capital | `GFX_news_event_azir_broken_sun_disc` |
| A Second Sun Over Nerimazeth | An intact, smaller bronze disc over old stonework, with Xerath's blue arcane light and gathered followers | `GFX_news_event_xerath_sundisc` |

The first five picture bindings are in `interface/azir_landmark_events.gfx`. Xerath's binding is in `interface/_news_eventpictures.gfx`. The current bindings use installed static textures. Convert the supplied animations to the event presentation format verified by the mod and retain a static frame for the standard news window.

## In-game checks

1. Start Rift Rapture. Confirm the world sees the warning once and the unfinished gate appears. Lose the Rupture mid-focus and verify that construction stalls and resuming does not send another warning.
2. Finish Rift Rapture. Confirm the first-rift model and flash event appear together, followed three days later by the aftermath. Finish Open Void Gate and confirm the current open gate replaces the staged landmark after the existing opening animation.
3. Start fresh as Icathia and finish The Void's Influence. The Remnants of a Void World should offer Resist the Void's Corruption and Succumb to the Void's Influence. Choose Resistance. Complete Invite Settlers and Void Containment while Kassadin is present, Icathia holds the Rupture and the civil war is over. Finish Talk to a Daughter and verify that Icathia can invite Kai'Sa or let her keep her own watch. On an existing save that already chose Hybrid, verify that Kai'Sa joins once when the focus completes.
4. Raise Xerath's disc before the capital falls. In a separate run lose Nerimazeth during construction and verify that the decision cancels. Conquer state 144 from Shurima in wartime and verify that The Sun Disc Shatters goes out once, regardless of whether Xerath built his disc.
