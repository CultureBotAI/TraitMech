#!/usr/bin/env python3
"""Verify a TraitMech METPO ROBOT-template proposal cohort.

Runs every pre-submission check the `metpo-proposal` skill specifies:

  1. Column-count sanity (classes=11 cols, properties=12 cols on every row).
  2. ROBOT header row 2 has the required directives.
  3. Parent integrity — every `SC %` parent resolves either in-file or to
     `METPO:<n>`.
  4. Subset tag consistency — every row in both TSVs carries the same
     `metpo_traitmech_<YYYY>_<MM>` value.
  5. Scope-A citations — every `traitmech:NNNNNN` ID a cohort CITES resolves to
     a real record. Whole-corpus coverage is reported but not asserted: it is a
     cross-cohort property that cohort v5 already satisfies, and demanding it of
     every cohort failed v1/v3/v7 permanently over work they never took on
     (#319). Skipped entirely for a cohort with no classes template (#318), or
     with `--skip-scope-a`.
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


def _corpus_traitmech_ids() -> set[str]:
    """Every traitmech id the corpus knows, from `identifier:` OR `synonyms:`."""
    ids: set[str] = set()
    for p in TRAITS_DIR.rglob("*.yaml"):
        ids |= set(re.findall(r"traitmech:\d+", p.read_text()))
    return ids


def cohort_coverage(proposals_dir: Path) -> tuple[set[str], set[str]]:
    """(all ids cited across every cohort, corpus ids none of them cite).

    The CROSS-cohort property #319's per-cohort rule was standing in for. No
    single cohort owns it — v5 lifts the synthetic traits, v1/v3/v7 lift other
    things — so it is asserted here, once, over the union (#349 review).
    """
    cited: set[str] = set()
    for tsv in sorted(proposals_dir.glob("*/metpo_proposal_classes_robot.tsv")):
        cited |= set(re.findall(r"traitmech:\d+", tsv.read_text()))
    return cited, _corpus_traitmech_ids() - cited


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
    # Anywhere a traitmech id can legitimately live in a record, not just
    # `identifier:`. The skill's Round-trip plan says that once upstream mints a
    # real METPO id the migration swaps `identifier:` to the METPO CURIE and
    # PRESERVES the old one in `synonyms:`. Reading only `identifier:` would make
    # a PARTIAL mint produce phantom failures against an already-submitted cohort
    # that still cites all of them — the same pathology #319 describes, pointed
    # the other way (#349 review).
    ids = _corpus_traitmech_ids()
    if not ids:
        print("  scope-A: no traitmech:NNNNNN ids in corpus (nothing to cover)", file=sys.stderr)
        return

    # Exact token match, not a substring scan: `i not in text` would treat
    # `traitmech:000001` as covered by a cell containing `traitmech:0000010`
    # (#321).
    cited = set(re.findall(r"traitmech:\d+", class_tsv_text))

    # WHAT THIS ASSERTS, AND WHY IT CHANGED (#319).
    #
    # It used to demand that EVERY corpus id appear in EVERY cohort carrying a
    # classes template. That is not a per-cohort property: v1 lifts causal-graph
    # scaffolding, v3 and v7 lift other things, and none of them undertook the
    # synthetic-trait lift. They failed permanently over a backlog they never
    # took on, which is how a check trains people to ignore it.
    #
    # The synthetic-trait lift IS done -- cohort v5 carries all 120 as class rows
    # and passes. So whole-corpus coverage is a CROSS-cohort property; it is
    # reported here and asserted by nobody, because no single cohort owns it.
    #
    # What IS a per-cohort property, and what this now checks: every id a cohort
    # CITES must resolve to a real record. That catches a typo or a citation left
    # behind after a record was renamed or removed -- a failure the old rule could
    # not see, because it only ever looked for absences in the other direction.
    phantom = sorted(c for c in cited if c not in ids)
    if phantom:
        _emit(failures,
              f"scope-A: {len(phantom)} cited traitmech id(s) do not exist in the "
              f"corpus: {phantom[:5]}{' ...' if len(phantom) > 5 else ''}")
    elif cited:
        print(f"  scope-A: all {len(cited)} cited traitmech ids resolve", file=sys.stderr)
    else:
        print("  scope-A: this cohort lifts no traitmech ids (not a Scope-A cohort)",
              file=sys.stderr)

    uncovered = len(ids - cited)
    if uncovered:
        print(f"  scope-A: FYI {uncovered} of {len(ids)} corpus ids are not in THIS "
              f"cohort (cross-cohort coverage is not a per-cohort gate; see v5)",
              file=sys.stderr)


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
    # Optional so --coverage, which is corpus-level, needs no cohort. main()
    # rejects an omitted cohort in every other mode.
    ap.add_argument("cohort_dir", type=Path, nargs="?",
                    help="proposals/metpo_traitmech_v<N>/ directory")
    ap.add_argument("--coverage", action="store_true",
                    help="Corpus-level: assert every traitmech id is lifted by SOME "
                         "cohort. Cross-cohort, so it takes no <cohort> argument.")
    ap.add_argument("--skip-scope-a", action="store_true", help="Don't check that a cohort's cited traitmech: ids resolve. "
                         "NOTE this now disables a CORRECTNESS check (a cited id that "
                         "no record has), not the old whole-corpus coverage rule it "
                         "used to suppress as expected noise (#319).")
    ap.add_argument("--skip-scope-c", action="store_true", help="Don't check that every CausalNodeTypeEnum value is lifted.")
    args = ap.parse_args()

    if args.coverage:
        cited, uncovered = cohort_coverage(REPO_ROOT / "proposals")
        print("=== cross-cohort Scope-A coverage ===", file=sys.stderr)
        print(f"  cited across all cohorts: {len(cited)}", file=sys.stderr)
        print(f"  corpus ids not lifted:    {len(uncovered)}", file=sys.stderr)
        for i in sorted(uncovered)[:20]:
            print(f"    {i}", file=sys.stderr)
        if uncovered:
            print("\nThese have no METPO home, so they cannot be cross-referenced from\n"
                  "kg-microbe. Add them to a Scope-A cohort (v5 is the existing one).",
                  file=sys.stderr)
            return 1
        print("  every traitmech id is lifted by some cohort", file=sys.stderr)
        return 0

    if args.cohort_dir is None:
        ap.error("a cohort directory is required unless --coverage is given")
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
