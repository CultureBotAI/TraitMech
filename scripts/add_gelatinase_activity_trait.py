#!/usr/bin/env python3
"""Add gelatinase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "gelatinase_activity.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T00:00:00Z"

RECORD = {
    "identifier": "traitmech:000136",
    "label": "gelatinase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active gelatinase protease."
    ),
    "definition_source": "DOI:10.1128/JB.01311-07",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "gelatinase-positive",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.1128/IAI.73.3.1606-1612.2005",
        },
        {
            "synonym_text": "gelatinase production",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.1128/IAI.73.3.1606-1612.2005",
        },
    ],
    "evidence": [
        {
            "reference": "DOI:10.1128/JB.01311-07",
            "snippet": (
                "One of the well-studied virulence factors of Enterococcus "
                "faecalis is a secreted bacterial protease, termed gelatinase"
            ),
            "notes": (
                "Del Papa et al. identify Enterococcus faecalis gelatinase as "
                "a secreted bacterial protease and experimentally test "
                "maturation steps needed for full protease activity."
            ),
        },
        {
            "reference": "DOI:10.1128/IAI.73.3.1606-1612.2005",
            "snippet": (
                "all gelatinase-positive isolates but little to no "
                "translocation for gelatinase nonproducers"
            ),
            "notes": (
                "Zeng, Teng and Murray score Enterococcus faecalis isolates by "
                "gelatinase production and distinguish gelatinase-positive "
                "from gelatinase-negative phenotypes."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1351",
            "taxon_label": "Enterococcus faecalis",
            "note": "Model gelatinase-producing bacterium used in gelE and fsr studies.",
            "reference": "DOI:10.1128/JB.01311-07",
        }
    ],
    "discussions": [
        {
            "discussion_id": "gelatinase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for gelatinase "
                "activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0008233 is the generic peptidase-activity class and "
                "MICRO:0000649 denotes a gelatinase assay, so both are too "
                "broad or assay-level for equivalent TraitRecord xrefs."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-11",
        }
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
            "Minted gelatinase activity as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden files; "
            "METPO has no exact gelatinase activity class yet."
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
