#!/usr/bin/env python3
"""Audit YAML-writing scripts in TraitMech.

For every Python module under `scripts/` and `src/traitmech/` that writes a
YAML (looks for `yaml.dump`, `yaml.safe_dump`, or `.write_text(` on a `.yaml`
path), record:

  - appends to `curation_history`?
  - has a write-safeguard? (either `--dry-run` opt-out OR `--apply`/`--write`
    opt-in — opt-in is strictly safer because the default is to *not* write)
  - calls `linkml-validate` (in any form) before writing?
  - is mentioned in `justfile` (i.e. wired into a target)?

Output: TSV to stdout (and via --out to a file).
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

SEARCH_DIRS = [
    Path("scripts"),
    Path("src/traitmech"),
]

# Patterns
# Match `path.write_text(yaml.safe_dump(...))` and similar — must show
# yaml-serializer output flowing into write_text on the same line.
# Previously a weaker heuristic (.write_text + any .yaml token in the
# file) flagged scripts that READ trait YAMLs but write JSON/HTML/TSV
# as false positives.
_WRITE_TEXT_OF_YAML = re.compile(
    r"\.write_text\s*\(\s*yaml\.(?:safe_)?dump"
)
_CURATION_APPEND = re.compile(
    r"curation_history.*?(append|\+=|\.insert)"
    r"|['\"]curator['\"]\s*:"
    r"|append_curation_event"
    r"|record_curation"
)
# Match either the explicit `--dry-run` opt-out convention OR the
# `--apply`/`--write` opt-in convention. Either pattern indicates a
# safety-conscious writer (the latter is strictly stronger because the
# default action is *not* to write).
_WRITE_SAFEGUARD = re.compile(
    r"--dry[-_]run|dry_run\s*[:=]"
    r"|--apply\b|args\.apply\b"
    r"|--write\b|args\.write\b"
)
_VALIDATE_BEFORE_WRITE = re.compile(
    r"linkml[._-]?validate"
    r"|TraitValidator"
    r"|validate_trait\("
    r"|validator\.validate\("
    # write_validated_trait is the closed-schema gate from
    # src/traitmech/validation/write_validated.py — its callers
    # validate by virtue of calling it.
    r"|write_validated_trait\("
)


def script_paths() -> list[Path]:
    out: list[Path] = []
    for d in SEARCH_DIRS:
        if not d.exists():
            continue
        out.extend(sorted(p for p in d.rglob("*.py") if "__pycache__" not in str(p)))
    return out


def looks_like_yaml_writer(text: str) -> bool:
    if "yaml.safe_dump(" in text or "yaml.dump(" in text:
        return True
    # `.write_text(...)` only counts when the argument is a yaml.dump
    # / yaml.safe_dump result. The looser previous heuristic
    # (.write_text + any .yaml token in the file) flagged scripts that
    # only READ yamls but write something else (JSON, HTML, TSV).
    if _WRITE_TEXT_OF_YAML.search(text):
        return True
    # write_validated_trait is the closed-schema-gated wrapper that
    # callers route through instead of yaml.dump directly.
    if "write_validated_trait(" in text:
        return True
    return False


# Library helpers opt out of the CLI-writer audit by declaring
# `audit-writers: library-helper` as its own line (modulo leading
# whitespace from docstring indentation). The marker must:
#   1. Live under src/traitmech/ — CLI writers under scripts/ can't
#      silently suppress themselves, even if they include the
#      phrase in a docstring.
#   2. Appear as a standalone line (not embedded in narrative text)
#      so an incidental mention in prose can't trip it.
_LIBRARY_HELPER_MARKER_RE = re.compile(
    r"^\s*audit-writers:\s*library-helper\s*$",
    re.MULTILINE,
)
_LIBRARY_HELPER_PATH_SUBSTR = "src/traitmech/"


def _is_exempt_library_helper(path: Path, text: str) -> bool:
    """A YAML-writing module can opt out of the CLI-writer audit iff
    (a) its posix-style path contains ``src/traitmech/`` — CLI writers
    under ``scripts/`` can't silently suppress themselves — and
    (b) its source contains the literal-line marker
    ``audit-writers: library-helper`` (allowing leading whitespace
    for docstring indentation, but not arbitrary surrounding text)."""
    if _LIBRARY_HELPER_PATH_SUBSTR not in path.as_posix():
        return False
    return bool(_LIBRARY_HELPER_MARKER_RE.search(text))


def audit(path: Path, justfile_text: str) -> dict | None:
    # Suppress self-match: this module's regex source contains
    # `yaml.safe_dump` etc., so it would otherwise appear in its own
    # output. See G05 in reports/gap_fix_backlog.md.
    if path.resolve() == Path(__file__).resolve():
        return None
    try:
        text = path.read_text()
    except (UnicodeDecodeError, OSError):
        return None
    if not looks_like_yaml_writer(text):
        return None
    if _is_exempt_library_helper(path, text):
        return None
    return {
        "path": str(path),
        "writes_yaml": "yes",
        "appends_curation_history": "yes" if _CURATION_APPEND.search(text) else "no",
        "has_write_safeguard": "yes" if _WRITE_SAFEGUARD.search(text) else "no",
        "validates_before_write": "yes" if _VALIDATE_BEFORE_WRITE.search(text) else "no",
        "wired_into_just": "yes" if path.stem in justfile_text or path.name in justfile_text else "no",
    }


def _load_justfile_text() -> str:
    chunks = []
    for name in ("justfile", "project.justfile"):
        p = Path(name)
        if p.exists():
            chunks.append(p.read_text())
    return "\n".join(chunks)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=None, help="TSV output path (default stdout)")
    args = ap.parse_args()

    justfile_text = _load_justfile_text()

    rows: list[dict] = []
    for p in script_paths():
        row = audit(p, justfile_text)
        if row is not None:
            rows.append(row)

    fields = ["path", "writes_yaml", "appends_curation_history",
              "has_write_safeguard", "validates_before_write", "wired_into_just"]

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
            w.writeheader()
            for row in rows:
                w.writerow(row)
        print(f"Wrote {len(rows)} rows to {args.out}", file=sys.stderr)
    else:
        w = csv.DictWriter(sys.stdout, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for row in rows:
            w.writerow(row)

    # Print summary
    def count(field: str, val: str) -> int:
        return sum(1 for r in rows if r[field] == val)

    print("", file=sys.stderr)
    print(f"=== writers audit summary ({len(rows)} writers) ===", file=sys.stderr)
    print(f"  appends curation_history:   {count('appends_curation_history', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  has write safeguard:        {count('has_write_safeguard', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  validates before write:     {count('validates_before_write', 'yes')} / {len(rows)}",
          file=sys.stderr)
    print(f"  wired into justfile:        {count('wired_into_just', 'yes')} / {len(rows)}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
