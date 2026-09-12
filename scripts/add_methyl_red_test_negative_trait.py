#!/usr/bin/env python3
"""Add seeded METPO methyl-red-test-negative with ASM and DOI evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "other" / "methyl_red_test_negative.yaml"

ASM_MRVP = (
    "https://asm.org/getmedia/40946f85-9357-4563-aa8a-994427efa825/"
    "Methyl-Red-and-Voges-Proskauer-Test-Protocols.pdf"
)
HANSEN = "DOI:10.1128/JCM.42.8.3665-3669.2004"

CURATOR = "codex"
SEED_TIMESTAMP = "2026-09-12T18:34:21Z"
TIMESTAMP = "2026-09-12T18:38:59Z"

SEED_RECORD = {
    "identifier": "METPO:1005015",
    "label": "methyl red test negative",
    "definition": "A phenotype in which an organism tests negative in the methyl red test.",
    "trait_category": "OTHER",
    "term_kind": "CLASS",
    "mapping_status": "SEEDED",
    "parent_traits": ["METPO:1005013"],
    "curation_history": [
        {
            "timestamp": SEED_TIMESTAMP,
            "curator": "seed_from_metpo",
            "action": "SEEDED_FROM_METPO",
            "changes": "imported from data/raw/metpo.owl (CLASS)",
        }
    ],
}

UPDATES = {
    "parent_traits": ["METPO:1000059"],
    "definition_source": ASM_MRVP,
    "evidence": [
        {
            "reference": ASM_MRVP,
            "snippet": (
                "A negative MR test is indicated by a yellow color in the "
                "culture medium (Fig. 1B), which occurs when less acid is "
                "produced (pH is higher) from the fermentation of glucose."
            ),
            "notes": (
                "The ASM protocol PDF defines the negative methyl-red-test "
                "readout as a yellow culture after methyl red is added, "
                "reflecting less acidification during glucose fermentation."
            ),
        },
        {
            "reference": HANSEN,
            "snippet": (
                "In the ASM Manual of Clinical Microbiology, only 6 of the "
                "18 biochemical tests used in the present investigation are "
                "listed for Klebsiella species: indole, MR, VP, LDC, ODC, "
                "and malonate"
            ),
            "notes": (
                "Hansen et al. evaluated methyl red as a conventional "
                "Klebsiella biochemical test; their MR results varied enough "
                "by method that this first pass does not assert a canonical "
                "negative example."
            ),
        },
        {
            "reference": HANSEN,
            "snippet": (
                "Variable results were of two types: (i) those in which all "
                "three laboratories found a mixture of positive and negative "
                "results among the representatives of a species for a "
                "specific test (e.g., K. pneumoniae and l-sorbose), "
                "suggesting a truly variable reaction, and (ii) those in "
                "which one center found most strains to be negative while "
                "another found most positive (e.g., K. rhinoscleromatis and "
                "MR) or vice versa, suggesting that the results were method "
                "dependent."
            ),
            "notes": (
                "The same interlaboratory evaluation found that MR could be "
                "method dependent for some Klebsiella species/test "
                "combinations, so this first pass leaves canonical_examples "
                "empty rather than promoting a method-sensitive result."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "methyl-red-test-negative-assay-parent-gap",
            "prompt": (
                "Resolve a non-assay parent for negative methyl-red-test "
                "phenotypes before narrowing parent_traits below phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO:1005013 is the seeded superclass of METPO:1005015, "
                "but METPO:1005013 defines an assay rather than a broader "
                "microbial trait class, so this record is temporarily "
                "parented directly to METPO:1000059 phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-12",
        }
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(SEED_RECORD)
    record.update(copy.deepcopy(UPDATES))
    record_curation_event(
        record,
        curator=CURATOR,
        action="ENRICHED_FROM_LITERATURE",
        changes=(
            "Added the METPO methyl-red-test-negative phenotype with "
            "stable-URL and DOI-backed methyl-red-test evidence after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = build_record()
    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
