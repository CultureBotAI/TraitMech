#!/usr/bin/env python3
"""Check `canonical_examples` taxon ids against NCBITaxon (#445).

`canonical_examples` is the slot that ties a trait to real organisms, which is
what makes this catalog usable from KG-Microbe. 226 records carry 315 of them and
nothing checked any of it: not that the CURIE is well formed, not that the id
exists, and not that the stored `taxon_label` still matches the ontology.

Label drift is the interesting case, because it is invisible and it is already
here: `morphology/heterocyst` stores `NCBITaxon:103690` as "Nostoc sp. PCC 7120"
while NCBITaxon now labels that node "Nostoc sp. PCC 7120 = FACHB-418". Neither
is wrong; they have simply diverged, and a curator comparing a record against
NCBI has no way to know which of the two they are looking at.

Defects:

  MALFORMED_TAXON_CURIE (ERROR)   Not `PREFIX:id`, or a non-numeric NCBITaxon id.
  MISSING_TAXON_ID (ERROR)        An example with no `taxon_id` at all.
  UNRESOLVED_TAXON (ERROR)        An NCBITaxon id the ontology does not know.
  TAXON_LABEL_DRIFT (WARN)        Stored label differs from the ontology label.
                                  WARN, not ERROR: NCBI relabels nodes for its
                                  own reasons (adding strain synonyms, as above),
                                  and a curator-chosen display label is not
                                  automatically wrong because upstream expanded
                                  it. Failing these would make every upstream
                                  rename a build break.

Deliberately NOT in `qc`, following `validate-products`: resolution needs the
OAK NCBITaxon build, which is a large download that a bare CI runner may not
have. Without an adapter the id checks still run and resolution is reported as
skipped, so the recipe is useful offline rather than merely silent.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_causal_graphs import Corpus, _as_corpus  # noqa: E402

DEFAULT_TRAITS = Path("data/traits")
CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*:[A-Za-z0-9_.\-]+$")
NCBITAXON = re.compile(r"^NCBITaxon:\d+$")

ERRORS = {"MALFORMED_TAXON_CURIE", "MISSING_TAXON_ID", "UNRESOLVED_TAXON"}


def _adapter():
    """Return an NCBITaxon adapter, or None if it cannot be built.

    Returning None rather than raising keeps the id-shape checks useful on a
    machine with no ontology build, which is the common case in CI.
    """
    try:
        from oaklib import get_adapter

        adapter = get_adapter("sqlite:obo:ncbitaxon")
        adapter.label("NCBITaxon:2261")  # cheap probe; a partial build fails here
        return adapter
    except Exception:
        return None


def example_rows(
    source: Path | Corpus = DEFAULT_TRAITS, *, adapter=None, resolve: bool = True
) -> tuple[list[tuple[str, str, str]], dict[str, int]]:
    """Return (rows, counts) where each row is (file, defect, detail)."""
    if resolve and adapter is None:
        adapter = _adapter()
    rows: list[tuple[str, str, str]] = []
    counts = {"examples": 0, "records": 0, "resolved": 0, "resolution": 0}
    counts["resolution"] = 1 if adapter is not None else 0

    for rel, doc in _as_corpus(source):
        examples = doc.get("canonical_examples") or []
        if examples:
            counts["records"] += 1
        for ex in examples:
            counts["examples"] += 1
            tid = ex.get("taxon_id")
            label = ex.get("taxon_label")
            if not tid:
                rows.append((rel, "MISSING_TAXON_ID", f"{label or '<no label>'}"))
                continue
            if not CURIE.match(str(tid)):
                rows.append((rel, "MALFORMED_TAXON_CURIE", f"{tid} is not PREFIX:id"))
                continue
            if str(tid).startswith("NCBITaxon:") and not NCBITAXON.match(str(tid)):
                rows.append((rel, "MALFORMED_TAXON_CURIE", f"{tid} has a non-numeric id"))
                continue
            if adapter is None or not str(tid).startswith("NCBITaxon:"):
                continue
            actual = adapter.label(tid)
            if actual is None:
                rows.append((rel, "UNRESOLVED_TAXON", f"{tid} not found in NCBITaxon"))
                continue
            counts["resolved"] += 1
            if label and actual != label:
                rows.append(
                    (rel, "TAXON_LABEL_DRIFT", f"{tid} record={label!r} ncbitaxon={actual!r}")
                )
    return rows, counts


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--traits-dir", type=Path, default=DEFAULT_TRAITS)
    ap.add_argument("--no-resolve", action="store_true", help="skip ontology lookups")
    args = ap.parse_args()

    rows, counts = example_rows(args.traits_dir, resolve=not args.no_resolve)
    for rel, defect, detail in rows:
        print(f"{defect}\t{rel}\t{detail}")

    errors = [r for r in rows if r[1] in ERRORS]
    warns = len(rows) - len(errors)
    print(
        f"\ncanonical_examples: {counts['examples']} example(s) across "
        f"{counts['records']} record(s); {len(errors)} error(s), {warns} warning(s)"
    )
    if counts["resolution"]:
        print(f"  resolved against NCBITaxon: {counts['resolved']}")
    else:
        # Say it, rather than reporting a clean run that checked half of what it
        # claims to check.
        print(
            "  NCBITaxon resolution SKIPPED (no usable ontology build) -- id shape "
            "was checked, existence and labels were not"
        )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
