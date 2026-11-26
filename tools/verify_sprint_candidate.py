"""Read back a frozen standalone candidate and compare it with its inputs."""

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re

from validate_hoi4_mod import strip_comments, validate


def effective_files(game, mod, folder, replacements):
    paths = {}
    if not any(folder == r or folder.startswith(r + "/") for r in replacements):
        paths.update({p.name.lower(): p for p in (game / folder).glob("*.txt")})
    paths.update({p.name.lower(): p for p in (mod / folder).glob("*.txt")})
    return paths.values()


def script(path):
    return strip_comments(path.read_text(encoding="utf-8-sig", errors="replace"))


def diagnostic_id(line):
    if line.startswith("duplicate localization key "):
        return line.split(": ", 1)[0]
    return re.sub(r"(?<=\.txt):\d+:", ":", line)


def package_digest(hashes):
    digest = sha256()
    for name in sorted(hashes):
        digest.update(f"{name}\t{hashes[name]}\n".encode("utf-8"))
    return digest.hexdigest()


def compare_parent(parent, provenance, actual):
    parent = parent.resolve()
    if not isinstance(provenance, dict) or parent.name != provenance.get("candidate"):
        return ["The supplied parent does not match the candidate recorded in derived_from"]
    receipt_path = parent / "build-receipt.json"
    if not receipt_path.is_file():
        return [f"Missing parent receipt: {receipt_path}"]
    data = receipt_path.read_bytes()
    if sha256(data).hexdigest() != provenance.get("receipt_sha256"):
        return ["Parent receipt SHA-256 differs from derived_from"]
    previous = json.loads(data)["package_sha256"]
    if package_digest(previous) != provenance.get("package_digest_sha256"):
        return ["Parent package digest differs from derived_from"]
    overrides = provenance.get("overrides")
    if not isinstance(overrides, dict):
        return ["Missing parent override manifest"]
    # A null hash records deletion of an inherited file.
    changed = {name: actual.get(name) for name in previous.keys() | actual.keys()
               if previous.get(name) != actual.get(name)}
    return [f"Parent override mismatch: {name}" for name in sorted(changed.keys() | overrides.keys())
            if name not in changed or name not in overrides or changed[name] != overrides[name]]


def verify(output, game, base, parent=None):
    receipt = json.loads((output / "build-receipt.json").read_text(encoding="utf-8"))
    mod = output / "RuneterraSprint"
    expected = receipt["package_sha256"]
    actual = {p.relative_to(mod).as_posix().lower(): sha256(p.read_bytes()).hexdigest()
              for p in mod.rglob("*") if p.is_file()}
    failures = []
    for name in sorted(expected.keys() | actual.keys()):
        if expected.get(name) != actual.get(name):
            failures.append(f"Content or file list mismatch: {name}")
    if parent is not None:
        failures.extend(compare_parent(parent, receipt.get("derived_from"), actual))
    launcher_name = receipt.get("launcher_descriptor", "RuneterraSprint.mod")
    launchers = list(output.glob("*.mod"))
    if len(launchers) != 1 or launchers[0].name != launcher_name:
        failures.append(f"Expected exactly one launcher descriptor named {launcher_name}")
    elif not (mod / "descriptor.mod").is_file():
        failures.append("Missing internal package descriptor")
    else:
        descriptor = (mod / "descriptor.mod").read_text(encoding="utf-8")
        external = launchers[0].read_text(encoding="utf-8")
        if external != descriptor + f'path="{mod.as_posix()}"\n':
            failures.append("The launcher descriptor differs from the package descriptor or its target")
    replacements = receipt["replace_paths"]
    def files(folder):
        return effective_files(game, mod, folder, replacements)

    tags = {}
    for path in files("common/country_tags"):
        for tag, target in re.findall(r'(?m)^\s*([A-Z0-9]{3})\s*=\s*"([^"]+)"', script(path)):
            if tag in tags:
                failures.append(f"Tag {tag} is registered by both {tags[tag]} and {path.name}")
            tags[tag] = path.name
            if not any((root / "common" / target).is_file() for root in (mod, game)):
                failures.append(f"{tag} has no country definition at {target}")
    states = {}
    owners = {}
    province_states = {}
    for path in files("history/states"):
        text = script(path)
        state = re.search(r"\bid\s*=\s*(\d+)", text)
        if not state:
            failures.append(f"{path.name} has no state id")
            continue
        if state[1] in states:
            failures.append(f"State {state[1]} is duplicated in {path.name} and {states[state[1]]}")
        states[state[1]] = path.name
        owner = re.search(r"\bowner\s*=\s*([A-Z0-9]{3})", text)
        if owner:
            owners[state[1]] = owner[1]
        provinces = re.search(r"\bprovinces\s*=\s*\{([^}]*)\}", text)
        if not provinces:
            failures.append(f"{path.name} has no province list")
        else:
            for province in provinces[1].split():
                if province in province_states:
                    failures.append(f"Province {province} assigned twice in {province_states[province]} and {path.name}")
                province_states[province] = path.name
        for tag in re.findall(r"\b(?:owner|controller|add_core_of)\s*=\s*([A-Z0-9]{3})", text):
            if tag not in tags:
                failures.append(f"{path.name} uses unregistered tag {tag}")
    defined = {}
    for line in (mod / "map/definition.csv").read_text(encoding="utf-8-sig").splitlines():
        fields = line.split(";")
        if len(fields) > 4 and fields[0].isdigit():
            defined[fields[0]] = fields[4]
    for province in province_states.keys() - defined.keys():
        failures.append(f"{province_states[province]} assigns unknown province {province}")
    for province, terrain in defined.items():
        if province != "0" and terrain == "land" and province not in province_states:
            failures.append(f"Land province {province} has no state")
    units = {p.stem.lower() for p in files("history/units")}
    characters = set()
    for path in files("common/characters"):
        # Find direct children of characters, ignoring strings containing braces.
        depth = 0
        for m in re.finditer(r'"(?:\\.|[^"\\])*"|([\w.-]+)\s*=\s*\{|[{}]', script(path)):
            if m[0].startswith('"'):
                continue
            if m[1] and depth == 1:
                characters.add(m[1])
            depth += -1 if m[0] == "}" else 1
    histories = {}
    for path in files("history/countries"):
        tag = path.name[:3]
        if tag in histories:
            failures.append(f"Country {tag} has two history files: {path.name} and {histories[tag]}")
        histories[tag] = path.name
        text = script(path)
        if not text.strip():
            continue
        if path.name[:3] not in tags:
            failures.append(f"History {path.name} has no registered country")
        for oob in re.findall(r'(?m)^\s*oob\s*=\s*"?([^"\s}#]+)', text):
            if oob.lower() not in units:
                failures.append(f"{path.name} references missing OOB {oob}")
        for capital in re.findall(r"(?m)^\s*capital\s*=\s*(\d+)", text):
            if capital not in states:
                failures.append(f"{path.name} references missing capital {capital}")
            elif path.name[:3] in owners.values() and owners.get(capital) != path.name[:3]:
                failures.append(f"{path.name} places its capital {capital} in {owners.get(capital)}")
        for character in re.findall(r'(?m)^\s*recruit_character\s*=\s*"?([\w.-]+)', text):
            if character not in characters:
                failures.append(f"{path.name} recruits missing character {character}")
    candidate_diagnostics = validate(mod)
    baseline = Counter(map(diagnostic_id, validate(base)))
    introduced = list((Counter(map(diagnostic_id, candidate_diagnostics)) - baseline).elements())
    result = {"package_digest_sha256": package_digest(actual), "verified_files": len(actual),
              "registered_tags_including_dynamic": len(tags), "state_ids": len(states),
              "assigned_provinces": len(province_states), "country_history_tags": len(histories),
              "structural_or_manifest_failures": failures, "base_validator_count": baseline.total(),
              "candidate_validator_count": len(candidate_diagnostics), "introduced_diagnostics": introduced,
              "candidate_validator_diagnostics": candidate_diagnostics}
    if parent is not None:
        result["compared_parent"] = parent.resolve().name
    (output / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "candidate_validator_diagnostics"}, indent=2))
    return bool(failures or introduced)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Build folder containing build-receipt.json and RuneterraSprint/")
    parser.add_argument("--base", type=Path, default=Path("E:/Local Repo/Runeterra/Runeterra"))
    parser.add_argument("--game", type=Path, default=Path("E:/SteamLibrary/steamapps/common/Hearts of Iron IV"))
    parser.add_argument("--parent", type=Path, help="Compare payload changes with the recorded parent receipt and overrides")
    args = parser.parse_args()
    raise SystemExit(verify(args.output.resolve(), args.game.resolve(), args.base.resolve(), args.parent))
