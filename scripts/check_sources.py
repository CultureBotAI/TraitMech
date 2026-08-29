#!/usr/bin/env python3
"""Validate download.yaml, TraitMech's source catalogue.

Adopted from ProteinTraitsMech's `check_sources.py` so the two repos can be
read side by side, with two deliberate differences.

FIRST, THE REQUIRED FIELDS ARE ACTUALLY ENFORCED. The sibling's docstring says
a source block "also carries name, source, license, status", but only `url` is
checked, so a block can omit its licence and pass. Licence provenance is the
main thing this catalogue exists to carry — several TraitMech sources are
collaborator projects over public data whose upstream terms a consumer has to
carry forward — so omitting it must fail rather than pass quietly.

SECOND, IT RUNS IN CI. The sibling defines `sources-check` but never wired it
into a workflow (a comment there records this as a follow-up), which makes it a
recipe nobody runs. This one is a `just qc` dependency.

Checks:
  - every block carries url, name, source, license, status;
  - `status` is in the allowed set;
  - `source` values are unique — two blocks claiming one id would make the
    seeded/seeder cross-check ambiguous;
  - a block with status `seeded` names a `seeder:` whose script exists;
  - every scripts/seed_*.py is referenced by some block (orphan → warning);
  - restrictive or unresolved licences are surfaced as warnings, not hidden.

Exit non-zero on error; warnings do not fail. Stdlib + PyYAML.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "download.yaml"
SCRIPTS = REPO_ROOT / "scripts"

REQUIRED = ("url", "name", "source", "license", "status")

# `candidate` and `rejected` carry real weight here: both external sources were
# characterised in full and deliberately not seeded, and the reason belongs in
# the catalogue rather than in a commit message nobody will find.
STATUSES = {"seeded", "candidate", "deferred", "rejected", "superseded", "enrichment"}

RESTRICTIVE = ("noncommercial", "non-commercial", "-nc", "byncnd", "by-nc",
               "noderiv", "-nd", "login", "registration", "flagged")
UNRESOLVED = ("unknown", "unclear", "tbd", "see upstream_licenses")


def main() -> int:
    if not MANIFEST.exists():
        print(f"ERROR: {MANIFEST.name} not found", file=sys.stderr)
        return 2
    try:
        blocks = yaml.safe_load(MANIFEST.read_text(encoding="utf-8")) or []
    except yaml.YAMLError as exc:
        # A syntax error must read as a diagnostic, not a raw parser traceback:
        # the operator needs to know which file failed and roughly where.
        print(f"ERROR: {MANIFEST.name} is not valid YAML: {exc}", file=sys.stderr)
        return 2
    if not isinstance(blocks, list):
        print("ERROR: download.yaml must be a YAML list", file=sys.stderr)
        return 2
    if not blocks:
        # An empty catalogue used to pass green, so deleting every source
        # satisfied the gate. A catalogue with no sources is a broken file.
        print("ERROR: download.yaml lists no sources", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    referenced: set[str] = set()
    seen_sources: dict[str, str] = {}

    for i, block in enumerate(blocks):
        # A bare `-` with a mis-indented body parses to None, and this file's
        # own style makes that a one-keystroke mistake. Report it rather than
        # raising AttributeError on the next line.
        if not isinstance(block, dict):
            errors.append(
                f"block[{i}] is {type(block).__name__}, not a mapping — check "
                "the indentation under its `-`"
            )
            continue

        tag = block.get("name") or block.get("source") or f"block[{i}]"
        for field in REQUIRED:
            if not block.get(field):
                errors.append(f"[{tag}] missing required field: {field}")

        status = block.get("status")
        if status is not None and not isinstance(status, str):
            errors.append(f"[{tag}] status must be a string, got {type(status).__name__}")
            status = None
        if status is not None and status not in STATUSES:
            errors.append(
                f"[{tag}] invalid status {status!r}; expected one of "
                f"{', '.join(sorted(STATUSES))}"
            )

        source = block.get("source")
        if source:
            if source in seen_sources:
                errors.append(
                    f"[{tag}] duplicate source id {source!r}, already used by "
                    f"{seen_sources[source]!r}"
                )
            else:
                seen_sources[source] = tag

        seeder = block.get("seeder")
        if seeder:
            parts = str(seeder).split()
            if not parts:
                errors.append(f"[{tag}] seeder is blank")
            else:
                script = parts[0]
                referenced.add(script)
                # Constrain the shape: without this, `seeder: ../download.yaml`
                # resolves to a real file and passes, which also lets a source
                # dodge the orphan-seeder warning.
                if not re.fullmatch(r"seed_[A-Za-z0-9_]+\.py", script):
                    errors.append(
                        f"[{tag}] seeder must be a scripts/seed_*.py file, got {script!r}"
                    )
                elif not (SCRIPTS / script).exists():
                    errors.append(f"[{tag}] seeder script not found: scripts/{script}")
        elif status == "seeded":
            errors.append(f"[{tag}] status is 'seeded' but no seeder is named")

        licence = str(block.get("license", "")).lower()
        if any(token in licence for token in RESTRICTIVE):
            warnings.append(f"[{tag}] restrictive licence: {block.get('license')}")
        elif any(token in licence for token in UNRESOLVED):
            warnings.append(f"[{tag}] licence unresolved: {block.get('license')}")
        if block.get("upstream_licenses") and status in {"seeded", "enrichment"}:
            warnings.append(
                f"[{tag}] is in use and carries upstream_licenses; anything "
                "published from it must carry those terms forward"
            )

    for script in sorted(SCRIPTS.glob("seed_*.py")):
        if script.name not in referenced:
            warnings.append(
                f"seeder scripts/{script.name} is not referenced in download.yaml"
            )

    # Re-reads every block, so it must tolerate the same malformed input the
    # main loop reports on — a non-mapping block, or a non-scalar status. This
    # summary crashing was what turned three reported errors into tracebacks.
    by_status: dict[str, int] = {}
    for block in blocks:
        if not isinstance(block, dict):
            continue
        status = block.get("status")
        if isinstance(status, str) and status:
            by_status[status] = by_status.get(status, 0) + 1

    summary = ", ".join(f"{n} {s}" for s, n in sorted(by_status.items()))
    print(f"download.yaml: {len(blocks)} source(s) ({summary})")
    for warning in warnings:
        print(f"  WARN: {warning}")
    for error in errors:
        print(f"  ERROR: {error}")
    if errors:
        print(f"\n{len(errors)} error(s).")
        return 1
    print(f"\nOK ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
