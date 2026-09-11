#!/usr/bin/env python3
"""Add pectin degradation as a DOI-backed biopolymer degradation trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / "pectin_degradation.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-10T00:00:00Z"
GO_SOURCE = "http://purl.obolibrary.org/obo/go/releases/2026-07-26/go-basic.obo"

RECORD = {
    "identifier": "traitmech:000135",
    "label": "pectin degradation",
    "definition": (
        "A biopolymer-degradation metabolism in which an organism depolymerizes "
        "pectin into oligogalacturonides and catabolizes the released pectin "
        "breakdown products using pectinolytic enzymes."
    ),
    "definition_source": "DOI:10.1128/MMBR.00038-07",
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000110"],
    "synonyms": [
        {
            "synonym_text": "pectinolysis",
            "synonym_type": "EXACT_SYNONYM",
            "source": "DOI:10.1146/annurev.micro.50.1.213",
        },
        {
            "synonym_text": "pectin breakdown",
            "synonym_type": "EXACT_SYNONYM",
            "source": GO_SOURCE,
        },
        {
            "synonym_text": "pectin catabolism",
            "synonym_type": "EXACT_SYNONYM",
            "source": GO_SOURCE,
        },
        {
            "synonym_text": "pectinolytic",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.1128/MMBR.00038-07",
        },
    ],
    "xrefs": ["GO:0045490"],
    "evidence": [
        {
            "reference": "DOI:10.1128/MMBR.00038-07",
            "snippet": (
                "Catabolism of pectin and its breakdown products by pectinolytic "
                "bacteria occurs within distinct cellular environments"
            ),
            "notes": (
                "Abbott and Boraston review pectin breakdown by pectinolytic "
                "Enterobacteriaceae as a multicomponent microbial catabolic pathway."
            ),
        },
        {
            "reference": "DOI:10.1146/annurev.micro.50.1.213",
            "snippet": (
                "The extracellular degradation of the pectin leads to the formation "
                "of oligogalacturonides that are catabolized through an intracellular "
                "pathway"
            ),
            "notes": (
                "Hugouvieux-Cotte-Pattat et al. review the pectinase system and "
                "pectin-catabolite pathway of Erwinia chrysanthemi strain 3937."
            ),
        },
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="PROPOSED_FROM_RESEARCH",
        changes=(
            "Proposed DOI-backed pectin degradation after a repository-wide "
            "duplicate review covering ignored and hidden files."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
