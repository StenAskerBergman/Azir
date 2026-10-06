"""Check the final Git index against the current explicit commit scope."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT).decode("utf-8")


def main():
    scope = json.loads((ROOT / "commit-scope.json").read_text(encoding="utf-8"))
    errors = []
    if scope["base_commit"] != git("rev-parse", "HEAD").strip():
        errors.append("Scope is stale: base_commit must match current HEAD.")
    groups = {}
    for label in ("include", "hold", "never"):
        paths = scope[label]
        if not isinstance(paths, list) or any(not isinstance(p, str) for p in paths):
            raise ValueError(f"{label} must be a list of paths")
        for path in paths:
            if (not path or path.startswith("/") or "\\" in path
                    or any(c in path for c in "*?[:")
                    or any(part in ("", ".", "..") for part in path.split("/"))):
                errors.append(f"Invalid exact relative path: {path!r}")
            if path in groups:
                errors.append(f"Repeated or conflicting classification: {path}")
            groups[path] = label
    staged = set(filter(None, git("diff", "--cached", "--name-only", "--no-renames", "-z").split("\0")))
    included = set(scope["include"])
    if not included:
        errors.append("No paths included for this batch.")
    for path in sorted(staged - included):
        errors.append(f"Blocked staged path ({groups.get(path, 'UNCLASSIFIED')}): {path}")
    for path in sorted(included - staged):
        errors.append(f"Included path is not staged: {path}")
    if git("ls-files", "-u", "-z"):
        errors.append("Unresolved index conflicts.")
    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        return 1
    print(f"PASS: all {len(staged)} staged paths match the current commit scope")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"FAIL: cannot validate commit scope: {error}")
        sys.exit(1)
