#!/usr/bin/env python3
"""Re-emit trait records that drifted off the write_validated_trait form (#554).

#322/#344 normalised the whole corpus so that
`test_the_whole_corpus_round_trips` could ENFORCE the round-trip claim rather
than merely document how false it was. Thirteen records edited by the
2026-08-26 tranches drifted back: their content is correct, but their line
wrapping is not what `safe_dump` under the helper's EMIT_OPTS produces, so the
invariant fails on main.

This rewrites drifted records through the helper's own emission path. **No data
changes; only formatting.** For that reason, and following the #344 precedent
exactly, it adds no `curation_history` event: there is no curation claim to
record, and thirteen "reflowed a line" events would be provenance noise.

Two-pass, per #324's lesson: every file is computed and semantically checked
before anything is written, and the run aborts on the first mismatch rather
than leaving the corpus half-normalised.

Usage:
    python scripts/normalize_trait_emission.py           # dry run (default)
    python scripts/normalize_trait_emission.py --apply   # write
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TRAITS = REPO_ROOT / "data" / "traits"


def rendered(doc: dict[str, Any], name: str) -> bytes:
    """Return what write_validated_trait would emit for ``doc``."""
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / name
        write_validated_trait(doc, out)
        return out.read_bytes()


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true", help="write (default is a dry run)")
    args = ap.parse_args()

    planned: list[tuple[Path, bytes]] = []
    for path in sorted(TRAITS.glob("*/*.yaml")):
        raw = path.read_bytes()
        try:
            doc = yaml.safe_load(raw.decode("utf-8"))
        except yaml.YAMLError as exc:
            print(f"ABORT: {path} does not parse: {exc}", file=sys.stderr)
            return 1
        if not isinstance(doc, dict):
            continue
        try:
            want = rendered(doc, path.name)
        except Exception as exc:  # validation failure is a real defect, not drift
            print(f"ABORT: {path} does not validate: {exc}", file=sys.stderr)
            return 1
        if want == raw:
            continue
        # Pass one: prove the rewrite is semantically identical BEFORE any write.
        if yaml.safe_load(want.decode("utf-8")) != doc:
            print(f"ABORT: re-emitting {path} would change its data", file=sys.stderr)
            return 1
        planned.append((path, want))

    for path, _ in planned:
        print(f"  normalise {path.relative_to(REPO_ROOT)}")
    print(
        f"{len(planned)} record(s) drifted from the emitter's form"
        f"{'' if args.apply else ' (dry run)'}",
        file=sys.stderr,
    )

    if not args.apply:
        return 0

    # Pass two: every file already checked, so writing cannot strand the corpus.
    for path, want in planned:
        path.write_bytes(want)
    for path, _ in planned:
        if rendered(yaml.safe_load(path.read_text(encoding="utf-8")), path.name) != path.read_bytes():
            print(f"ABORT: {path} still does not round-trip after writing", file=sys.stderr)
            return 1
    print(f"{len(planned)} record(s) normalised and re-verified", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
