#!/usr/bin/env python3
"""Static checks for Azir focus trees and English localization.

The game remains the authoritative parser. This script catches the project-specific
mistakes that have repeatedly made focuses load without names, descriptions, or
rewards before a full HOI4 startup is necessary.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Focus:
    focus_id: str
    file: Path
    line: int
    body: str
    completion_reward: str | None
    relative_position_id: str | None


def strip_comments(text: str) -> str:
    """Remove Clausewitz # comments while preserving strings and line numbers."""
    output: list[str] = []
    for line in text.splitlines(keepends=True):
        quoted = False
        escaped = False
        cut = len(line)
        for index, char in enumerate(line):
            if char == '"' and not escaped:
                quoted = not quoted
            if char == "#" and not quoted:
                cut = index
                break
            escaped = char == "\\" and not escaped
            if char != "\\":
                escaped = False
        output.append(line[:cut])
        if cut < len(line) and not line[:cut].endswith("\n"):
            output.append("\n")
    return "".join(output)


def matching_brace(text: str, opening: int) -> int | None:
    depth = 0
    quoted = False
    escaped = False
    for index in range(opening, len(text)):
        char = text[index]
        if char == '"' and not escaped:
            quoted = not quoted
        if not quoted:
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    return index
        escaped = char == "\\" and not escaped
        if char != "\\":
            escaped = False
    return None


def nested_block(body: str, key: str) -> str | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}\s*=\s*\{{", body)
    if not match:
        return None
    opening = body.find("{", match.start())
    closing = matching_brace(body, opening)
    if closing is None:
        return None
    return body[opening + 1 : closing]


def parse_focuses(path: Path) -> list[Focus]:
    clean = strip_comments(path.read_text(encoding="utf-8-sig", errors="replace"))
    focuses: list[Focus] = []
    pattern = re.compile(r"(?m)^\s*(?:focus|shared_focus)\s*=\s*\{")
    for match in pattern.finditer(clean):
        opening = clean.find("{", match.start())
        closing = matching_brace(clean, opening)
        if closing is None:
            continue
        body = clean[opening + 1 : closing]
        id_match = re.search(r"(?m)^\s*id\s*=\s*([^\s#}]+)", body)
        if not id_match:
            continue
        relative_match = re.search(
            r"(?m)^\s*relative_position_id\s*=\s*([^\s#}]+)", body
        )
        focuses.append(
            Focus(
                focus_id=id_match.group(1).strip('"'),
                file=path,
                line=clean.count("\n", 0, match.start()) + 1,
                body=body,
                completion_reward=nested_block(body, "completion_reward"),
                relative_position_id=(
                    relative_match.group(1).strip('"') if relative_match else None
                ),
            )
        )
    return focuses


def load_localization(root: Path) -> tuple[dict[str, list[tuple[Path, int]]], list[str]]:
    keys: dict[str, list[tuple[Path, int]]] = defaultdict(list)
    errors: list[str] = []
    for path in sorted((root / "localisation" / "english").rglob("*.yml")):
        raw = path.read_bytes()
        relative = path.relative_to(root)
        if not raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"{relative}: English localization must be UTF-8 with BOM")
        text = raw.decode("utf-8-sig", errors="replace")
        first_content = next(
            (line.strip() for line in text.splitlines() if line.strip()), ""
        )
        if first_content != "l_english:":
            errors.append(f"{relative}: first content line must be 'l_english:'")
        for line_number, line in enumerate(text.splitlines(), start=1):
            match = re.match(r"^\s*([^\s:#]+):(?:\d+)?\s", line)
            if match and match.group(1) != "l_english":
                keys[match.group(1)].append((relative, line_number))
    return keys, errors


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    focus_files = sorted((root / "common" / "national_focus").glob("*.txt"))
    focuses = [focus for path in focus_files for focus in parse_focuses(path)]
    by_id: dict[str, list[Focus]] = defaultdict(list)
    for focus in focuses:
        by_id[focus.focus_id].append(focus)

    for focus_id, definitions in sorted(by_id.items()):
        if len(definitions) > 1:
            places = ", ".join(
                f"{item.file.relative_to(root)}:{item.line}" for item in definitions
            )
            errors.append(f"duplicate focus id {focus_id}: {places}")

    for focus in focuses:
        location = f"{focus.file.relative_to(root)}:{focus.line}"
        if focus.completion_reward is None:
            errors.append(f"{location}: {focus.focus_id} has no completion_reward")
        elif not re.sub(r"\s+", "", focus.completion_reward):
            errors.append(f"{location}: {focus.focus_id} has an empty completion_reward")

    # Within one file, HOI4 requires relative_position_id to refer to an earlier
    # definition. Cross-file anchors are intentionally left to the game parser.
    for path in focus_files:
        seen: set[str] = set()
        for focus in parse_focuses(path):
            same_file_definitions = [
                definition
                for definition in by_id.get(focus.relative_position_id or "", [])
                if definition.file == path
            ]
            if (
                focus.relative_position_id
                and same_file_definitions
                and focus.relative_position_id not in seen
            ):
                errors.append(
                    f"{path.relative_to(root)}:{focus.line}: {focus.focus_id} uses "
                    f"relative_position_id={focus.relative_position_id} before it is defined"
                )
            seen.add(focus.focus_id)

    localization, localization_errors = load_localization(root)
    errors.extend(localization_errors)
    for focus in focuses:
        location = f"{focus.file.relative_to(root)}:{focus.line}"
        if focus.focus_id not in localization:
            errors.append(f"{location}: missing localization {focus.focus_id}")
        description = f"{focus.focus_id}_desc"
        if description not in localization:
            errors.append(f"{location}: missing localization {description}")

    for key, definitions in sorted(localization.items()):
        if len(definitions) > 1:
            places = ", ".join(f"{path}:{line}" for path, line in definitions)
            errors.append(f"duplicate localization key {key}: {places}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="mod root (defaults to the parent of tools/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    errors = validate(root)
    if errors:
        print(f"FAIL: {len(errors)} validation issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: focus rewards, layout references, and English localization are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
