"""Report unresolved literal art/audio bindings and the sound pools using them."""

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
from zipfile import ZipFile

from build_sprint_candidate import ABS_ASSET, inventory
from validate_hoi4_mod import matching_brace, strip_comments


def audit(output, game):
    mod = output / "RuneterraSprint"
    package = inventory(mod)
    required = defaultdict(set)
    sound_ids = defaultdict(set)
    pools = defaultdict(set)
    for relative, path in package.items():
        if path.suffix.lower() not in {".gfx", ".gui", ".txt", ".asset"}:
            continue
        text = strip_comments(path.read_text(encoding="utf-8-sig", errors="replace"))
        for match in ABS_ASSET.finditer(text):
            key = match[1].replace("\\", "/").lower()
            required[key].add(f"{relative}:{text.count(chr(10), 0, match.start()) + 1}")
        if not (relative.startswith("sound/") and relative.endswith(".asset")):
            continue
        for match in re.finditer(r'\b(sound|soundeffect)\s*=\s*\{\s*name\s*=\s*"([^"]+)"', text, re.I):
            end = matching_brace(text, text.index("{", match.start()))
            if end is None:
                raise ValueError(f"Unclosed {match[1]} {match[2]} in {path}")
            body = text[match.end():end]
            if match[1].lower() == "sound":
                binding = re.search(r'\bfile\s*=\s*"([^"]+\.(?:wav|ogg))"', body, re.I)
                if binding:
                    key = "sound/" + binding[1].replace("\\", "/").lower()
                    required[key].add(f"{relative}:{text.count(chr(10), 0, match.start()) + 1}")
                    sound_ids[key].add(match[2])
            else:
                for name in re.findall(r'\bsound\s*=\s*"?([\w.-]+)', body):
                    pools[name].add(match[2])
    dlcs = [folder for directory in ("dlc", "integrated_dlc")
            for folder in (game / directory).iterdir() if folder.is_dir()]
    archives = [path for directory in ("dlc", "integrated_dlc") for path in (game / directory).rglob("*.zip")]
    archived = set()
    for path in archives:
        with ZipFile(path) as archive:
            archived.update(s.replace("\\", "/").lower().lstrip("/") for s in archive.namelist())
    unresolved = {}
    dlc_only = []
    for key, locations in sorted(required.items()):
        if key in package or (game / key).is_file():
            continue
        if key in archived or any((folder / key).is_file() for folder in dlcs):
            dlc_only.append(key)
            continue
        unresolved[key] = {"bindings": sorted(locations)}
        if key in sound_ids:
            unresolved[key]["sound_ids"] = sorted(sound_ids[key])
            unresolved[key]["selecting_pools"] = sorted({p for name in sound_ids[key] for p in pools[name]})
    result = {
        "scope": "Literal gfx and audio paths in candidate script, GUI, sprites and sound assets. Includes declarations without gameplay consumers.",
        "distinct_literal_paths": len(required), "checked_unpacked_dlc_roots": len(dlcs),
        "checked_dlc_archives": len(archives), "resolved_only_in_dlc": dlc_only,
        "unresolved_graphics": sum(key.startswith("gfx/") for key in unresolved),
        "unresolved_audio": sum(key.startswith("sound/") for key in unresolved),
        "unresolved_audio_selected_by_pool": sum(bool(row.get("selecting_pools")) for row in unresolved.values()),
        "unresolved": unresolved,
    }
    out = output / "art-reference-check.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"{result['unresolved_graphics']} unresolved graphics, {result['unresolved_audio']} unresolved audio, "
          f"{result['unresolved_audio_selected_by_pool']} missing audio paths selected by pools. Details: {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--game", type=Path, default=Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV"))
    options = parser.parse_args()
    audit(options.output.resolve(), options.game.resolve())
