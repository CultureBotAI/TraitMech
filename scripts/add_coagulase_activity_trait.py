#!/usr/bin/env python3
"""Add METPO coagulase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "coagulase_activity.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T00:00:00Z"

RECORD = {
    "identifier": "METPO:1007089",
    "label": "coagulase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "coagulase factors that activate prothrombin and convert fibrinogen to "
        "fibrin, clotting blood plasma."
    ),
    "definition_source": "DOI:10.1159/000333447",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "SEEDED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "coagulase test",
            "synonym_type": "EXACT_SYNONYM",
            "source": "metpo.owl",
        },
        {
            "synonym_text": "coagulase-positive",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.1159/000333447",
        },
    ],
    "created_by": "Marcin Joachimiak",
    "evidence": [
        {
            "reference": "DOI:10.1159/000333447",
            "snippet": (
                "Clinical isolates of Staphylococcus aureus secrete coagulases, "
                "polypeptides that bind to and activate prothrombin"
            ),
            "notes": (
                "McAdow, Missiakas and Schneewind review how staphylococcal "
                "coagulases activate prothrombin, convert fibrinogen to fibrin, "
                "and clot plasma or blood."
            ),
        },
        {
            "reference": "DOI:10.1371/journal.ppat.1001036",
            "snippet": (
                "Coa and vWbp promote the non-proteolytic activation of prothrombin "
                "and cleavage of fibrinogen"
            ),
            "notes": (
                "Cheng et al. experimentally show that the two S. aureus "
                "coagulases, Coa and von Willebrand factor binding protein, "
                "mediate prothrombin and fibrinogen reactions relevant to "
                "staphylococcal clot formation."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1280",
            "taxon_label": "Staphylococcus aureus",
            "note": "Canonical coagulase-positive bacterium that secretes Coa and vWbp.",
            "reference": "DOI:10.1371/journal.ppat.1001036",
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
        action="SEEDED_FROM_METPO",
        changes=(
            "Added the active METPO coagulase activity class as a DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files."
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
