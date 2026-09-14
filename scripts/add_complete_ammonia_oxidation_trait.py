#!/usr/bin/env python3
"""Add complete ammonia oxidation with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "metabolism" / (
    "complete_ammonia_oxidation.yaml"
)
VAN_KESSEL = "DOI:10.1038/nature16459"
DAIMS = "DOI:10.1038/nature16461"
GHIMIRE_KAFLE = "DOI:10.1128/aem.01698-23"
CURATOR = "codex"
TIMESTAMP = "2026-09-14T19:03:57Z"

RECORD = {
    "identifier": "traitmech:000187",
    "label": "complete ammonia oxidation",
    "definition": (
        "A nitrification metabolism in which a single organism oxidizes ammonia "
        "via nitrite to nitrate."
    ),
    "definition_source": VAN_KESSEL,
    "trait_category": "METABOLISM",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1005001"],
    "synonyms": [
        {
            "synonym_text": "comammox",
            "synonym_type": "EXACT_SYNONYM",
            "source": VAN_KESSEL,
        },
    ],
    "evidence": [
        {
            "reference": VAN_KESSEL,
            "snippet": (
                "Complete oxidation of ammonia to nitrate in one organism "
                "(complete ammonia oxidation; comammox) is energetically "
                "feasible"
            ),
            "notes": (
                "van Kessel et al. define complete ammonia oxidation, or "
                "comammox, as oxidation of ammonia to nitrate in a single "
                "organism."
            ),
        },
        {
            "reference": DAIMS,
            "snippet": (
                "Here we report on the discovery and cultivation of a "
                "completely nitrifying bacterium from the genus Nitrospira, a "
                "globally distributed group of nitrite oxidizers."
            ),
            "notes": (
                "Daims et al. independently demonstrated complete nitrification "
                "in a single Nitrospira organism."
            ),
        },
        {
            "reference": GHIMIRE_KAFLE,
            "snippet": (
                "The dominance of Nitrospira sp. BO4 could be explained by the "
                "ability of comammox to generate more energy through the "
                "complete oxidation of ammonia to nitrate"
            ),
            "notes": (
                "Ghimire-Kafle et al. support the same ammonia-to-nitrate "
                "scope in a freshwater complete-ammonia-oxidizing Nitrospira "
                "enrichment."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1715989",
            "taxon_label": "Candidatus Nitrospira inopinata",
            "note": (
                "Daims et al. cultivated and physiologically characterized "
                "Candidatus Nitrospira inopinata as a complete nitrifier."
            ),
            "reference": DAIMS,
        },
    ],
    "discussions": [
        {
            "discussion_id": "complete-ammonia-oxidation-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for one-organism "
                "complete ammonia oxidation before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot contains only METPO:1000862 "
                "obsolete Complete ammonia oxidation. METPO:1005001 denotes "
                "nitrification without requiring both oxidation steps to occur "
                "in one organism, while GO:0019329 ammonia oxidation and "
                "GO:0019332 nitrite oxidation each cover only one component of "
                "the comammox phenotype."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-14",
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
            "Minted complete ammonia oxidation as a DOI-backed nitrification "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has only an obsolete Complete "
            "ammonia oxidation class in the local snapshot and the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v64."
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
