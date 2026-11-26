"""Report the 990 proposals and consolidate reviewed Azir technology files."""

import argparse
from collections import Counter
from pathlib import Path
import re
import shutil
import tempfile

from validate_hoi4_mod import matching_brace, strip_comments


ROOT = Path(__file__).resolve().parent.parent
DIRECTORY = ROOT / "common/technologies"
COLLECTION = DIRECTORY / "azir_runeterra_theme_replacements.txt"
CATALOG = ROOT / "documentation/Runeterra Theme Replacements.md"
TAG = re.compile(r"[A-Z][A-Z0-9]{2}")
ENTRY = re.compile(r"\s*([a-zA-Z0-9_]+)\s*=\s*\{")


def read_text(path):
    return path.read_text(encoding="utf-8-sig")


def split_technologies(text):
    clean = strip_comments(text)
    wrapper = ENTRY.match(clean)
    if not wrapper or wrapper[1] != "technologies":
        raise ValueError("expected a technologies block")
    closing = matching_brace(clean, wrapper.end()-1)
    if closing is None or clean[closing+1:].strip():
        raise ValueError("expected one balanced top-level technologies block")
    entries = {}
    cursor = wrapper.end()
    while clean[cursor:closing].strip():
        entry = ENTRY.match(clean, cursor)
        if not entry or entry[1] in entries:
            raise ValueError("invalid or duplicate technology entry")
        end = matching_brace(clean, entry.end()-1)
        if end is None or end >= closing:
            raise ValueError(f"unclosed technology {entry[1]}")
        entries[entry[1]] = clean[entry.end():end]
        cursor = end+1
    return entries


def existing_technologies():
    technologies = {}
    for path in sorted(DIRECTORY.glob("*.txt")):
        for key, body in split_technologies(read_text(path)).items():
            if key in technologies:
                raise ValueError(f"duplicate technology {key} in {path.name}")
            technologies[key] = (path, body)
    return technologies


def read_candidates():
    result = {}
    for line in read_text(CATALOG).splitlines():
        if not line.startswith("|"):
            continue
        columns = [column.strip() for column in line.split("|")[1:-1]]
        if len(columns) != 5 or not TAG.fullmatch(columns[0]):
            continue
        tag, *row = columns
        if tag in result:
            raise ValueError(f"multiple first candidates for {tag}")
        result[tag] = row
    return result


def owner(key):
    if key == "improved_dozer_blade_tech":
        return "Shared"
    words = key.split("_")
    return (words[1] if words[0] == "azir" else words[0]).upper().replace("PIL", "PLT")


def list_catalog(country, candidates, definitions):
    for tag, (country_name, name, gameplay, evidence) in candidates.items():
        if country and tag != country:
            continue
        print(f"{tag} {country_name} - {name}")
        if country:
            print(f"  {gameplay}\n  Evidence - {evidence}")
        for key, (path, body) in definitions.items():
            if owner(key) == tag:
                route = "researchable" if re.search(r"\bfolder\s*=", body) else "script-granted"
                print(f"  {key} ({route}, {path.name})")
    if not country:
        print(f"\n{len(candidates)} candidates, {len(definitions)} existing Azir technology IDs")
        print("Existing IDs by owner:", dict(sorted(Counter(map(owner,definitions)).items())))


def audit_roster(layer_paths, candidates):
    states = {}
    for layer in [*map(Path, layer_paths), ROOT]:
        folder = layer / "history/states"
        if not folder.is_dir():
            raise ValueError(f"state history missing under {layer}")
        owners = {}
        for path in sorted(folder.rglob("*.txt")):
            clean = strip_comments(read_text(path))
            state = re.search(r"\bid\s*=\s*(\d+)", clean)
            owner_tag = re.search(r"\bowner\s*=\s*([A-Z0-9]{3})", clean)
            if state and owner_tag:
                owners.setdefault(int(state[1]), set()).add(owner_tag[1])
        states.update(owners)
    bookmark = strip_comments(read_text(ROOT / "common/bookmarks/990.txt"))
    bookmark_tags = set(re.findall(r'(?m)^\s*"([A-Z0-9]{3})"\s*=\s*\{', bookmark))
    roster = bookmark_tags.union(*states.values()) - {"TST", "XYZ"}
    for state, owners in sorted(states.items()):
        if len(owners) > 1:
            print(f"State {state} has competing owners: {', '.join(sorted(owners))}")
    missing = roster - candidates.keys()
    print(f"{len(roster)} starting or possible starting tags, {len(candidates)} total candidates")
    if missing:
        raise ValueError(f"missing candidates: {', '.join(sorted(missing))}")


def merge_sources(names):
    sources = [(DIRECTORY / name).resolve() for name in names]
    if len(set(sources)) != len(sources) or any(
        path.parent != DIRECTORY.resolve() or path.suffix != ".txt"
        or path == COLLECTION or not path.is_file() for path in sources
    ):
        raise ValueError("supply distinct existing file names under common/technologies")

    before = existing_technologies()
    output = read_text(COLLECTION) if COLLECTION.exists() else "technologies = {\n}\n"
    chunks = []
    for path in sources:
        raw = read_text(path)
        split_technologies(raw)
        # The validated wrapper is the only top-level block. Keep every body line.
        chunks.append(f"    # From {path.name}\n"+raw[raw.index("{")+1:raw.rindex("}")].strip("\n"))
    output = output[:output.rindex("}")].rstrip()+"\n\n"+"\n\n".join(chunks)+"\n}\n"
    proposed = split_technologies(output)
    expected = {key: body for key, (path, body) in before.items()
                if path.resolve() in sources or path == COLLECTION}
    if proposed != expected:
        raise ValueError("technology IDs or definition bodies would change")

    backup = Path(tempfile.mkdtemp(prefix="azir-tech-consolidation-"))
    for path in sources:
        shutil.copy2(path, backup / path.name)
    original = COLLECTION.read_bytes() if COLLECTION.exists() else None
    try:
        COLLECTION.write_text(output, encoding="utf-8")
        for path in sources:
            path.unlink()
        after = existing_technologies()
        if {key: body for key, (_, body) in after.items()} != {key: body for key, (_, body) in before.items()}:
            raise ValueError("verification detected drift after consolidation")
    except (OSError, ValueError):
        for path in sources:
            shutil.copy2(backup / path.name, path)
        if original is None:
            COLLECTION.unlink(missing_ok=True)
        else:
            COLLECTION.write_bytes(original)
        raise
    print(f"Consolidated {len(expected)} definitions without changing their contents.")
    print(f"Source backup: {backup}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--country", type=str.upper, help="List the candidate and installed technologies for a tag")
    actions.add_argument("--consolidate", nargs="+", metavar="FILE", help="Move reviewed files into the common collection")
    actions.add_argument("--audit-roster", nargs=2, metavar=("RUNETERRA", "QUARIOR"),
                         help="Check candidate coverage of the layered 990 state history")
    args = parser.parse_args()
    try:
        candidates = read_candidates()
        if args.country and args.country not in candidates:
            raise ValueError(f"no candidate in the catalog for {args.country}")
        if args.consolidate:
            merge_sources(args.consolidate)
        elif args.audit_roster:
            audit_roster(args.audit_roster, candidates)
        else:
            list_catalog(args.country, candidates, existing_technologies())
    except (OSError, ValueError) as error:
        parser.exit(1,f"{error}\n")


if __name__ == "__main__":
    main()
