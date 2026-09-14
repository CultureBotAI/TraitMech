#!/usr/bin/env python3
"""Add bacteriocin production with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "bacteriocin_production.yaml"
REA = "DOI:10.3389/fmicb.2016.00461"
RILEY = "DOI:10.1146/annurev.micro.56.012302.161024"
ZHANG = "DOI:10.1038/srep27973"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T05:04:06Z"
REVIEW_TIMESTAMP = "2026-09-14T05:16:59Z"

RECORD = {
    "identifier": "traitmech:000183",
    "label": "bacteriocin production",
    "definition": (
        "A physiological trait in which bacteria produce bacteriocins, "
        "ribosomally synthesized antimicrobial peptides or proteins that "
        "kill or inhibit other bacteria."
    ),
    "definition_source": REA,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "xrefs": ["GO:0030152"],
    "evidence": [
        {
            "reference": REA,
            "snippet": (
                "Bacteriocins are ribosomally synthesized antimicrobial "
                "peptides produced by bacteria, which have the ability to "
                "kill or inhibit other bacteria."
            ),
            "notes": (
                "Rea et al. review bacteriocins as bacterially produced "
                "ribosomal antimicrobial peptides."
            ),
        },
        {
            "reference": RILEY,
            "snippet": (
                "the most abundant and diverse family of microbial defense "
                "systems: the bacteriocins."
            ),
            "notes": (
                "Riley and Wertz support bacteriocins as a widespread, "
                "diverse microbial defense-system family."
            ),
        },
        {
            "reference": ZHANG,
            "snippet": (
                "Traditionally, nisin was produced industrially by using "
                "Lactococcus lactis in the neutral fermentation process."
            ),
            "notes": (
                "Zhang et al. support Lactococcus lactis as an industrial "
                "nisin-producing bacterium."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Lactococcus lactis is used as a canonical nisin-producing "
                "bacterium in neutral fermentation."
            ),
            "reference": ZHANG,
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
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted bacteriocin production as a DOI-backed TraitRecord "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files; METPO has no exact bacteriocin production class "
            "yet and the placeholder is reserved in "
            "proposals/metpo_traitmech_v60."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADVERSARIAL_REVIEW_REPAIR",
        changes=(
            "Resolved PR #899 review issue #900 by grounding bacteriocin "
            "production to GO:0030152 and removing the obsolete xref-gap TODO."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
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
