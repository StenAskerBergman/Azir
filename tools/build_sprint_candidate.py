"""Build a standalone local test mod from integrated Runeterra and working Azir."""

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from tempfile import TemporaryDirectory

from validate_hoi4_mod import matching_brace, strip_comments

ROOTS = "common dlc events gfx history integrated_dlc interface localisation map music portraits sound tutorial".split()
EXTENSIONS = set(".txt .lua .csv .yml .gfx .gui .asset .dds .tga .bmp .mesh .anim .map .ogg .wav".split())
AUTHORING_DIRS = {"assets", "inspo", "inspo portaits", "old", "pdns", "pngs", "potential", "undone", "cursors files"}
FRELJORD_BRANCH_TAGS = {"DAV", "EBT", "FRT", "ICC", "NBC", "RSW", "STP", "SWF"}
LOC = re.compile(r"^\s*(?!l_[a-z_]+:)([^\s:#]+):(?:\d+)?[ \t]+")
TAG = re.compile(r"(?m)^\s*([A-Z0-9]{3})\s*=\s*\"([^\"]+)\"")
ABS_ASSET = re.compile(r'(?i)["\']((?:gfx|sound)[/\\][^"\'\n]+\.(?:png|bmp|dds|tga|wav|ogg))["\']')
NAME = "Runeterra - Shurima and Targon Sprint"


def read(path):
    return path.read_text(encoding="utf-8-sig")


def git_state(root):
    def run(*args):
        return subprocess.check_output(["git", "-C", str(root), *args]).decode("utf-8")
    return {"head": run("rev-parse", "HEAD").strip(), "status": run("status", "--short").splitlines()}


def inventory(root):
    files = {}
    for directory in ROOTS:
        for path in (root / directory).rglob("*"):
            if path.is_file():
                files[path.relative_to(root).as_posix().lower()] = path
    return files


def runtime_file(rel, path, references):
    parts = rel.split("/")
    if rel in references:
        return True
    if parts[:2] == ["history", "states"] and len(parts) > 3:
        return False  # Country-labelled alternatives for the flat 990 state histories.
    if parts[0] == "sound" and parts[1] in {"files", "hun"}:
        return False  # Voice audition/source collections. The two voice banks bind tar/ and shu_lor/.
    if parts[0] == "gfx":
        if set(parts[1:-1]) & AUTHORING_DIRS or rel == "gfx/if riot approves.bmp":
            return False
        if path.suffix.lower() == ".txt":
            return False
    if rel in {"localisation/_other_/__color.txt", "common/national_focus/xerath_notes.txt"}:
        return False
    return path.suffix.lower() in EXTENSIONS and not path.name.lower().startswith("_documentation")


def texture_references(files):
    references = set()
    for relative, path in files.items():
        if path.suffix.lower() not in {".gfx", ".gui", ".asset", ".txt"}:
            continue
        if not runtime_file(relative, path, set()):
            continue
        content = strip_comments(path.read_text(encoding="utf-8-sig", errors="replace"))
        references.update(x.replace("\\", "/").lower() for x in ABS_ASSET.findall(content))
        if path.suffix.lower() == ".asset" and "sound" in path.parts:
            for name in re.findall(r'(?i)\bfile\s*=\s*"([^"]+\.(?:wav|ogg))"', content):
                references.add("sound/" + name.replace("\\", "/").lower())
    return references


def localisation_keys(files):
    by_language = defaultdict(set)
    for rel, path in files.items():
        if rel.startswith("localisation/") and rel.endswith(".yml"):
            by_language[rel.split("/")[1]].update(
                match[1] for line in read(path).splitlines() if (match := LOC.match(line))
            )
    return by_language


def sprite_overlaps(files, local, game):
    # Offsets must match the unmodified text to leave every unrelated sprite intact.
    definitions = defaultdict(list)
    comments = re.compile(r'"(?:\\.|[^"\\])*"|#[^\n]*')
    sprites = re.compile(r'\b(?:\w*spriteType|progressbarType)\s*=\s*\{\s*name\s*=\s*"([^"]+)"', re.I)
    for key, path in files.items():
        if not (key.startswith("interface/") and key.endswith(".gfx")):
            continue
        text = read(path)
        script = comments.sub(lambda m: " " * len(m[0]) if m[0].startswith("#") else m[0], text)
        for match in sprites.finditer(script):
            end = matching_brace(script, script.index("{", match.start()))
            if end is None:
                raise ValueError(f"Unclosed sprite {match[1]} in {path}")
            textures = re.findall(r'\btexturefile\s*=\s*"([^"]+)"', script[match.start():end + 1], re.I)
            exists = bool(textures) and all(
                name.replace("\\", "/").lower() in files or (game / name).is_file() for name in textures
            )
            definitions[match[1]].append((key, match.start(), end + 1, key in local, exists))
    removed = defaultdict(list)
    owners = {}
    for name, entries in definitions.items():
        if len({local_layer for _, _, _, local_layer, _ in entries}) < 2:
            continue
        local_ok = any(local_layer and exists for _, _, _, local_layer, exists in entries)
        base_ok = any(not local_layer and exists for _, _, _, local_layer, exists in entries)
        prefer_local = local_ok or not base_ok
        owners[name] = "Azir" if prefer_local else "Runeterra (only resolvable textures)"
        for key, start, end, local_layer, _ in entries:
            if local_layer != prefer_local:
                removed[key].append((start, end))
    return removed, owners


def build(base, azir, game, dest, install, candidate_number=None):
    if candidate_number is not None and candidate_number < 1:
        raise ValueError("The candidate number must be positive.")
    label = f"RC{candidate_number:02d}" if candidate_number is not None else ""
    name = f"{NAME} {label}" if label else NAME
    bundle = dest / "RuneterraSprint"
    launcher = azir.parent / f"RuneterraSprint{label}.mod"
    if dest.exists() or (install and launcher.exists()):
        raise ValueError("Choose a new output folder and an unused launcher descriptor.")
    if any(dest.is_relative_to(root) or root.is_relative_to(dest) for root in (base, azir, game)):
        raise ValueError("The output folder must be separate from input folders.")
    if not (base / "descriptor.mod").is_file() or not (azir / "descriptor.mod").is_file():
        raise ValueError("Expected Runeterra and Azir mod roots containing descriptor.mod.")
    settings = json.loads(read(game / "launcher-settings.json"))
    base_descriptor = read(base / "descriptor.mod")
    if 'name="Runeterra"' not in base_descriptor or 'replace_path="events"' not in base_descriptor:
        raise ValueError("Expected integrated Runeterra with Quarior replacements.")
    replacements = re.findall(r'(?m)^replace_path\s*=\s*"([^"]+)"', base_descriptor)
    target = ".".join(settings["rawVersion"].split(".")[:2]) + ".*"
    descriptor = f'name="{name}"\nversion="sprint-rc"\nsupported_version="{target}"\npicture="thumbnail.png"\n'
    descriptor += "".join(f'replace_path="{p}"\n' for p in replacements)
    external = descriptor + f'path="{bundle.as_posix()}"\n'
    layers = [inventory(base), inventory(azir)]
    sources = layers[0] | layers[1]
    references = texture_references(sources)
    sprite_ranges, sprite_owners = sprite_overlaps(sources, layers[1], game)
    azir_keys = localisation_keys(layers[1])
    shared = localisation_keys(layers[0])
    conflicts = defaultdict(dict)
    exclusions = {}
    hashes = {}
    emitted_paths = {}
    overlaps = {}
    omitted_base_keys = Counter()
    protected_tags = {}
    for path in (base / "common/country_tags").glob("*.txt"):
        protected_tags.update(TAG.findall(read(path)))
    vanilla_tags = game / "common/country_tags/00_countries.txt"
    vanilla_dupes = set(dict(TAG.findall(read(vanilla_tags)))) & protected_tags.keys()
    registered = set(protected_tags)
    for path in (game / "common/country_tags").glob("*.txt"):
        registered.update(dict(TAG.findall(read(path))))
    for key, path in sources.items():
        if key.startswith("common/country_tags/") and key.endswith(".txt"):
            registered.update(dict(TAG.findall(read(path))))
    inactive_freljord = FRELJORD_BRANCH_TAGS - registered
    for key, path in sources.items():
        if key.startswith("history/states/") and key.count("/") == 2 and key.endswith(".txt"):
            text = re.sub(r"(?m)#.*", "", read(path))
            occupied = set(re.findall(r"\b(?:owner|controller|add_core_of)\s*=\s*([A-Z0-9]{3})", text))
            if occupied & inactive_freljord:
                raise ValueError(f"{path} uses unregistered Freljord countries {occupied & inactive_freljord}")
    if vanilla_dupes != {"BLI", "BLZ", "HAR", "KUM"}:
        raise ValueError(f"Review the new vanilla/Runeterra tag overlap: {sorted(vanilla_dupes)}")
    local_tags = "common/country_tags/shurima_countries.txt"
    if dict(TAG.findall(read(sources[local_tags]))) != dict(TAG.findall(read(base / "common/country_tags/000_runeterra-shurima_countries.txt"))):
        raise ValueError("The two Shuriman tag registries have diverged. Reconcile their definitions.")
    authored_histories = {
        path.name[:3] for key, path in sources.items()
        if key.startswith("history/countries/") and path.read_bytes().strip()
    }

    dest.parent.mkdir(parents=True, exist_ok=True)
    with TemporaryDirectory(dir=dest.parent, prefix=".runeterra-sprint-") as work:
        out = Path(work) / "output"
        mod = out / bundle.name
        mod.mkdir(parents=True)

        def emit(relative, data):
            key = relative.as_posix().lower()
            if key in hashes:
                raise ValueError(f"Duplicate package path: {relative}")
            output = mod / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(data)
            hashes[key] = sha256(data).hexdigest()
            emitted_paths[key] = output

        for key, path in sorted(sources.items()):
            local = key in layers[1]
            rel = path.relative_to(azir if local else base)
            if not runtime_file(key, path, references):
                exclusions[key] = "development input or alternate state layout"
                continue
            if key == local_tags:
                exclusions[key] = "Runeterra already registers the same twelve tags"
                continue
            if key.startswith("history/countries/") and path.name[:3] in inactive_freljord:
                if local:
                    raise ValueError(f"Review the new Azir history for unregistered country {path.name[:3]}")
                exclusions[key] = "Freljord branch history without a registered country in the integrated 990 scenario"
                continue
            if key.startswith("history/countries/") and path.name[:3] in authored_histories and not path.read_bytes().strip():
                exclusions[key] = "empty placeholder beside authored country history"
                continue
            data = path.read_bytes()
            if local and key in layers[0] and data != layers[0][key].read_bytes():
                overlaps[key] = "Azir overrides integrated Runeterra"
            if key in sprite_ranges:
                content = read(path)
                for start, end in sorted(sprite_ranges[key], reverse=True):
                    content = content[:start] + content[end:]
                encoding = "utf-8-sig" if data.startswith(b"\xef\xbb\xbf") else "utf-8"
                data = content.encode(encoding)
            if key.startswith("localisation/") and key.endswith(".yml"):
                language = key.split("/")[1]
                kept = []
                for line in data.decode("utf-8-sig").splitlines(keepends=True):
                    match = LOC.match(line)
                    if match and not local and match[1] in azir_keys[language]:
                        omitted_base_keys[language] += 1
                    elif match and local and match[1] in shared[language]:
                        if match[1] in conflicts[language]:
                            raise ValueError(f"Duplicate Azir key {language}/{match[1]}")
                        conflicts[language][match[1]] = line.rstrip("\r\n")
                    else:
                        kept.append(line)
                data = "".join(kept).encode("utf-8-sig")
            emit(rel, data)
        for language, lines in conflicts.items():
            rel = Path("localisation", language, "replace", f"azir_sprint_merged_l_{language}.yml")
            emit(rel, (f"l_{language}:\n" + "\n".join(lines.values()) + "\n").encode("utf-8-sig"))
        country_data = read(vanilla_tags).splitlines(keepends=True)
        filtered = (line for line in country_data if not ((m := TAG.match(line)) and m[1] in vanilla_dupes))
        emit(Path("common/country_tags/00_countries.txt"), "".join(filtered).encode("utf-8"))
        emit(Path("descriptor.mod"), descriptor.encode())
        emit(Path("thumbnail.png"), (azir / "thumbnail.png").read_bytes())
        (out / launcher.name).write_text(external, encoding="utf-8")
        report = {"game": settings["version"], "runeterra": git_state(base), "azir": git_state(azir),
                  "launcher_descriptor": launcher.name,
                  "replace_paths": replacements, "base_registration_overrides": sorted(vanilla_dupes),
                  "base_localisation_rows_replaced": dict(omitted_base_keys),
                  "localised_keys_promoted": {lang: len(items) for lang, items in conflicts.items()},
                  "cross_layer_sprite_owners": sprite_owners,
                  "overlapping_runtime_paths_with_different_bytes": overlaps,
                  "omissions": exclusions, "package_sha256": hashes}
        for key, expected in hashes.items():
            if sha256(emitted_paths[key].read_bytes()).hexdigest() != expected:
                raise ValueError(f"Package readback failed: {key}")
        (out / "build-receipt.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        out.rename(dest)
    if install:
        with launcher.open("x", encoding="utf-8") as file:
            file.write(external)
    print(f"{len(hashes)} verified files in {bundle}\nBuild receipt: {dest / 'build-receipt.json'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="New destination folder outside both checkouts")
    parser.add_argument("--base", type=Path, default=Path("E:/Local Repo/Runeterra/Runeterra"))
    parser.add_argument("--azir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--game", type=Path, default=Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV"))
    parser.add_argument("--register", action="store_true", help="Add a local launcher descriptor without changing the playset")
    parser.add_argument("--candidate-number", type=int, help="Give a numbered candidate its own launcher entry (7 becomes RC07)")
    args = parser.parse_args()
    build(args.base.resolve(), args.azir.resolve(), args.game.resolve(), args.output.resolve(), args.register,
          args.candidate_number)
