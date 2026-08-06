#!/usr/bin/env python3
"""Verify a TraitMech METPO ROBOT-template proposal cohort.

Runs every pre-submission check the `metpo-proposal` skill specifies:

  1. Column-count sanity (classes=11 cols, properties=12 cols on every row).
  2. ROBOT header row 2 has the required directives.
  3. Parent integrity — every `SC %` parent resolves either in-file or to
     `METPO:<n>`.
  4. Subset tag consistency — every row in both TSVs carries the same
     `metpo_traitmech_<YYYY>_<MM>` value.
  5. Scope-A coverage — every `traitmech:NNNNNN` ID found in `data/traits/`
     appears in at least one `definition_source` cell, or the operator opts
     out with `--skip-scope-a`. Skipped entirely for a cohort that ships no
     classes template, since such a cohort proposes no classes and so is not
     doing Scope A at all (#318).
  6. Scope-C enum coverage — every `CausalNodeTypeEnum` permissible value
     appears as a leaf, or the operator opts out with `--skip-scope-c`.

Usage:
    python scripts/verify_metpo_proposal.py <cohort-dir>
    python scripts/verify_metpo_proposal.py proposals/metpo_traitmech_v1
    python scripts/verify_metpo_proposal.py <cohort> --skip-scope-a --skip-scope-c

Exits 0 on a clean verification, non-zero if any check fails. Prints a
summary to stderr regardless.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "src/traitmech/schema/traitmech.yaml"
TRAITS_DIR = REPO_ROOT / "data/traits"

CLASS_COLS = 11
PROP_COLS = 12

# Built-in CURIE prefixes accepted as external parents/ranges without
# requiring an in-file declaration.
EXTERNAL_PREFIX = re.compile(
    r"^(METPO|NCBITaxon|CHEBI|GO|PATO|RO|OBI|BFO|IAO|UBERON|ENVO|FOODON|ECO|PR|UO|UBPROP|CL):[A-Za-z0-9_]+$"
)

SUBSET_TAG = re.compile(r"^metpo_traitmech_\d{4}_\d{2}$")


def _read_tsv(path: Path) -> list[list[str]]:
    if not path.exists():
        return []
    return [line.rstrip("\n").split("\t") for line in path.read_text().splitlines()]


def _emit(failures: list[str], msg: str) -> None:
    failures.append(msg)
    print(f"  FAIL: {msg}", file=sys.stderr)


def check_columns(rows: list[list[str]], expected: int, label: str, failures: list[str]) -> None:
    for i, row in enumerate(rows, start=1):
        if len(row) != expected:
            _emit(failures, f"{label} row {i} has {len(row)} cols, expected {expected}")


def check_robot_header(rows: list[list[str]], required: list[str], label: str, failures: list[str]) -> None:
    if len(rows) < 2:
        _emit(failures, f"{label}: missing header rows (need 2)")
        return
    header2 = rows[1]
    for col_idx, directive in required:
        if col_idx >= len(header2):
            _emit(failures, f"{label} header row 2 too short — no col {col_idx}")
            continue
        actual = header2[col_idx].strip()
        if directive not in actual:
            _emit(failures, f"{label} header row 2 col {col_idx} = {actual!r}, expected to contain {directive!r}")


def check_parents(class_rows: list[list[str]], failures: list[str]) -> None:
    if len(class_rows) < 3:
        return
    ids_in_file = {r[0] for r in class_rows[2:] if len(r) > 0 and r[0]}
    for i, row in enumerate(class_rows[2:], start=3):
        if not row or len(row) < 5:
            continue
        parent = row[4].strip()
        if not parent:
            continue
        if parent in ids_in_file:
            continue
        if EXTERNAL_PREFIX.match(parent):
            continue
        _emit(failures, f"classes row {i} parent {parent!r} not in-file and not a recognized external CURIE")


def check_subset(rows: list[list[str]], col_idx: int, label: str, failures: list[str]) -> str | None:
    if len(rows) < 3:
        return None
    tags = set()
    for i, row in enumerate(rows[2:], start=3):
        if not row or len(row) <= col_idx:
            continue
        tag = row[col_idx].strip()
        if not tag:
            _emit(failures, f"{label} row {i} has empty subset tag")
            continue
        tags.add(tag)
        if not SUBSET_TAG.match(tag):
            _emit(failures, f"{label} row {i} subset {tag!r} does not match metpo_traitmech_YYYY_MM")
    if len(tags) > 1:
        _emit(failures, f"{label} has {len(tags)} distinct subset tags: {sorted(tags)}")
    return next(iter(tags), None) if len(tags) == 1 else None


def check_scope_a(class_tsv_text: str, failures: list[str]) -> None:
    if not TRAITS_DIR.exists():
        return
    # A cohort with no classes template proposes no classes, so it is not doing
    # Scope A and cannot be judged against it. Without this, class_tsv_text is ""
    # and EVERY traitmech: id in the corpus reads as uncited, so every
    # predicate-only cohort fails the moment the corpus gains its first synthetic
    # id — which is what v2, v4 and v6 all do today. main() already announces
    # "Scope C/A check will skip" for this case and check_scope_c already honours
    # it; only this check did not.
    #
    # Lifting the corpus's synthetic ids is a real obligation, but it belongs to
    # a Scope-A cohort, not to every cohort of any scope.
    if not class_tsv_text:
        print("  scope-A: no classes template in this cohort (skip)", file=sys.stderr)
        return
    ids: set[str] = set()
    for p in TRAITS_DIR.rglob("*.yaml"):
        for m in re.finditer(r"^identifier:\s*(traitmech:\d+)", p.read_text(), re.MULTILINE):
            ids.add(m.group(1))
    if not ids:
        print("  scope-A: no traitmech:NNNNNN ids in corpus (nothing to cover)", file=sys.stderr)
        return
    missing = sorted(i for i in ids if i not in class_tsv_text)
    if missing:
        _emit(failures, f"scope-A: {len(missing)} traitmech ids in corpus not cited in proposal: {missing[:5]}{' ...' if len(missing) > 5 else ''}")
    else:
        print(f"  scope-A: all {len(ids)} traitmech ids covered", file=sys.stderr)


def check_scope_c(class_tsv_text: str, failures: list[str]) -> None:
    if not SCHEMA_PATH.exists():
        _emit(failures, f"scope-C: schema not found at {SCHEMA_PATH}")
        return
    schema = yaml.safe_load(SCHEMA_PATH.read_text())
    enum = (schema.get("enums") or {}).get("CausalNodeTypeEnum") or {}
    values = list((enum.get("permissible_values") or {}).keys())
    if not values:
        return
    if "CausalNodeTypeEnum" not in class_tsv_text:
        print("  scope-C: CausalNodeTypeEnum not lifted in this cohort (skip)", file=sys.stderr)
        return
    missing = [v for v in values if f"CausalNodeTypeEnum.{v}" not in class_tsv_text]
    if missing:
        _emit(failures, f"scope-C: missing leaf rows for CausalNodeTypeEnum values: {missing}")
    else:
        print(f"  scope-C: all {len(values)} CausalNodeTypeEnum values lifted", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cohort_dir", type=Path, help="proposals/metpo_traitmech_v<N>/ directory")
    ap.add_argument("--skip-scope-a", action="store_true", help="Don't check that every traitmech: id is cited.")
    ap.add_argument("--skip-scope-c", action="store_true", help="Don't check that every CausalNodeTypeEnum value is lifted.")
    args = ap.parse_args()

    cohort_dir = args.cohort_dir
    if not cohort_dir.is_dir():
        print(f"error: not a directory: {cohort_dir}", file=sys.stderr)
        return 2

    classes_tsv = cohort_dir / "metpo_proposal_classes_robot.tsv"
    properties_tsv = cohort_dir / "metpo_proposal_properties_robot.tsv"
    if not classes_tsv.exists() and not properties_tsv.exists():
        print(f"error: no proposal TSVs found in {cohort_dir}", file=sys.stderr)
        return 2

    failures: list[str] = []

    print(f"Verifying {cohort_dir} ...", file=sys.stderr)

    class_rows = _read_tsv(classes_tsv)
    prop_rows = _read_tsv(properties_tsv)

    if class_rows:
        print(f"  classes TSV: {len(class_rows)} rows", file=sys.stderr)
        check_columns(class_rows, CLASS_COLS, "classes", failures)
        check_robot_header(
            class_rows,
            [(0, "ID"), (1, "LABEL"), (2, "A IAO:0000115"), (3, ">A IAO:0000119"), (4, "SC %"), (7, "A oboInOwl:inSubset")],
            "classes",
            failures,
        )
        check_parents(class_rows, failures)
        class_subset = check_subset(class_rows, 7, "classes", failures)
    else:
        print("  classes TSV: missing (Scope C/A check will skip)", file=sys.stderr)
        class_subset = None

    if prop_rows:
        print(f"  properties TSV: {len(prop_rows)} rows", file=sys.stderr)
        check_columns(prop_rows, PROP_COLS, "properties", failures)
        check_robot_header(
            prop_rows,
            [(0, "ID"), (1, "LABEL"), (2, "A IAO:0000115"), (3, ">A IAO:0000119"), (4, "TYPE"),
             (5, "DOMAIN"), (6, "RANGE"), (8, "A oboInOwl:inSubset")],
            "properties",
            failures,
        )
        prop_subset = check_subset(prop_rows, 8, "properties", failures)
        if class_subset and prop_subset and class_subset != prop_subset:
            _emit(failures, f"subset tag mismatch between classes ({class_subset!r}) and properties ({prop_subset!r})")
    else:
        print("  properties TSV: missing (skipped)", file=sys.stderr)

    class_tsv_text = classes_tsv.read_text() if classes_tsv.exists() else ""

    if not args.skip_scope_a:
        check_scope_a(class_tsv_text, failures)
    if not args.skip_scope_c:
        check_scope_c(class_tsv_text, failures)

    print("", file=sys.stderr)
    print("=== verify-proposal summary ===", file=sys.stderr)
    print(f"  cohort:   {cohort_dir}", file=sys.stderr)
    print(f"  failures: {len(failures)}", file=sys.stderr)
    if failures:
        return 1
    print("  status:   PASS", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
