#!/usr/bin/env python3
"""Restore five canonical-example citations the protein-taxon tranche replaced (#519).

The tranche rewrote 32 canonical-example citations from PMID to DOI and its
curation events describe this as an identifier upgrade. Twenty-seven are the
same paper. Five are a different paper under the same note (the PMID's own
registered DOI does not match the new DOI). A replacement labelled as a
normalisation is a provenance error, so this one-shot migration puts the
pre-tranche citation back and records the reversal. Replacing a citation
deliberately remains possible in a new event that says so.

The protein_examples evidence added by the tranche is untouched: it cites the
new DOIs as exemplar evidence in its own right, which is a separate claim.

Usage:
    python scripts/restore_substituted_citations.py           # dry run (default)
    python scripts/restore_substituted_citations.py --apply   # write
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TIMESTAMP = "2026-08-26T03:24:00Z"
ACTION = "RESTORE_CANONICAL_CITATION"

# (record, canonical taxon, citation the tranche wrote, citation it replaced)
RESTORATIONS = [
    ("metabolism/xylan_degradation", "NCBITaxon:44001",
     "DOI:10.1128/aem.56.4.1017-1024.1990", "PMID:18776029"),
    ("metabolism/homoacetogenesis", "NCBITaxon:33952",
     "DOI:10.1128/JB.00357-18", "PMID:22479398"),
    ("metabolism/biopolymer_degradation", "NCBITaxon:1708",
     "DOI:10.1016/0378-1119(86)90196-4", "PMID:23342046"),
    ("metabolism/chitinolysis", "NCBITaxon:615",
     "DOI:10.1002/j.1460-2075.1986.tb04235.x", "PMID:23398882"),
    ("metabolism/oxidative_phosphorylation", "NCBITaxon:266",
     "DOI:10.1016/S0005-2728(98)00092-9", "PMID:30428155"),
]


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true", help="write (default: dry run)")
    args = ap.parse_args()

    failures = 0
    for slug, taxon, wrong, original in RESTORATIONS:
        path = REPO_ROOT / "data" / "traits" / f"{slug}.yaml"
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        hits = 0
        for ex in doc.get("canonical_examples") or []:
            if (
                isinstance(ex, dict)
                and ex.get("taxon_id") == taxon
                and ex.get("reference") == wrong
            ):
                ex["reference"] = original
                hits += 1
        if hits != 1:
            print(
                f"  {path.name}: expected exactly one {taxon} example citing {wrong}, "
                f"found {hits}; not writing",
                file=sys.stderr,
            )
            failures += 1
            continue
        record_curation_event(
            doc,
            curator="claude",
            action=ACTION,
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
            changes=(
                f"Restored the canonical-example citation for {taxon} from {wrong} "
                f"back to {original} (review issue 519). The tranche event described "
                "the change as a PMID-to-DOI upgrade, but the DOI resolves to a "
                "different paper than the PMID, so this was a replacement rather than "
                "an identifier normalisation. The pre-tranche citation is restored; "
                "a deliberate replacement can be made in a new event that says so."
            ),
        )
        print(f"  {path.name}: {taxon} {wrong} -> {original}")
        if args.apply:
            write_validated_trait(doc, path)

    done = len(RESTORATIONS) - failures
    print(f"{done} citation(s) restored{'' if args.apply else ' (dry run)'}", file=sys.stderr)
    return int(failures > 0)


if __name__ == "__main__":
    sys.exit(main())
