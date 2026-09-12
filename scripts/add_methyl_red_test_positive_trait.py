#!/usr/bin/env python3
"""Add seeded METPO methyl-red-test-positive with ASM and DOI evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "other" / "methyl_red_test_positive.yaml"

ASM_MRVP = (
    "https://asm.org/getmedia/40946f85-9357-4563-aa8a-994427efa825/"
    "Methyl-Red-and-Voges-Proskauer-Test-Protocols.pdf"
)
HANSEN = "DOI:10.1128/JCM.42.8.3665-3669.2004"

CURATOR = "codex"
SEED_TIMESTAMP = "2026-09-12T19:14:16Z"
TIMESTAMP = "2026-09-12T19:16:03Z"

SEED_RECORD = {
    "identifier": "METPO:1005014",
    "label": "methyl red test positive",
    "definition": (
        "A phenotype in which an organism tests positive in the methyl red "
        "test, indicating mixed acid fermentation."
    ),
    "trait_category": "OTHER",
    "term_kind": "CLASS",
    "mapping_status": "SEEDED",
    "parent_traits": ["METPO:1005013"],
    "synonyms": [
        {
            "synonym_text": "methyl red test",
            "synonym_type": "RELATED_SYNONYM",
            "source": "metpo.owl",
        }
    ],
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
                "When the culture medium turns red after addition of methyl "
                "red, because of a pH at or below 4.4 from the fermentation "
                "of glucose, the culture has a positive result for the MR "
                "test (Fig.1A)."
            ),
            "notes": (
                "The ASM protocol PDF defines a positive methyl-red-test "
                "readout as red culture medium after methyl red is added, "
                "reflecting glucose fermentation that acidifies the medium "
                "to pH 4.4 or lower."
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
                "Klebsiella biochemical test; their Table 3 reports "
                "K. ornithinolytica methyl-red result percentages across "
                "CPHL, NRL, and SSI."
            ),
        },
        {
            "reference": HANSEN,
            "snippet": (
                "Methyl red 93.5 100.0 100.0 100.0 100.0 100.0 0.0 "
                "0.0 10.0 36.7m 46.7 90.0"
            ),
            "notes": (
                "Hansen et al. Table 3 reports the Methyl red row as 100.0% "
                "positive for K. ornithinolytica in all three reference "
                "laboratories, directly supporting the canonical example."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:54291",
            "taxon_label": "Klebsiella ornithinolytica",
            "note": (
                "Hansen et al. Table 3 reported 100.0% methyl-red-positive "
                "results for K. ornithinolytica across the CPHL, NRL, and "
                "SSI reference laboratories."
            ),
            "reference": HANSEN,
        }
    ],
    "discussions": [
        {
            "discussion_id": "methyl-red-test-positive-assay-parent-gap",
            "prompt": (
                "Resolve a non-assay parent for positive methyl-red-test "
                "phenotypes before narrowing parent_traits below phenotype."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "METPO:1005013 is the seeded superclass of METPO:1005014, "
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
            "Added the METPO methyl-red-test-positive phenotype with "
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
