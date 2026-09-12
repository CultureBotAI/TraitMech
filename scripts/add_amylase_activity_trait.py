#!/usr/bin/env python3
"""Add amylase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "amylase_activity.yaml"
SIDAR = "DOI:10.3389/fbioe.2020.00871"
BROWN = "DOI:10.1007/s00018-023-04812-w"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T08:08:43Z"

RECORD = {
    "identifier": "traitmech:000162",
    "label": "amylase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active amylolytic enzymes that hydrolyze starch."
    ),
    "definition_source": SIDAR,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "amylolytic enzymes",
            "synonym_type": "RELATED_SYNONYM",
            "source": SIDAR,
        }
    ],
    "evidence": [
        {
            "reference": SIDAR,
            "snippet": (
                "All enzymes capable of degrading starch are collectively "
                "indicated as amylolytic enzymes."
            ),
            "notes": (
                "Sidar et al. frame amylolytic enzymes as starch-degrading "
                "enzymes, grounding the organism-level phenotype as active "
                "amylase production rather than starch catabolism itself."
            ),
        },
        {
            "reference": BROWN,
            "snippet": (
                "the Bacteroides ovatus (Bo) extracellular α-amylase, "
                "BoGH13ASus"
            ),
            "notes": (
                "Brown et al. characterized BoGH13A_Sus as a Bacteroides "
                "ovatus extracellular alpha-amylase in a starch utilization "
                "system, supporting B. ovatus as a source-backed amylase "
                "activity example."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:28116",
            "taxon_label": "Bacteroides ovatus",
            "note": (
                "Brown et al. characterized the extracellular alpha-amylase "
                "BoGH13A_Sus from the Bacteroides ovatus starch utilization "
                "system."
            ),
            "reference": BROWN,
        }
    ],
    "discussions": [
        {
            "discussion_id": "amylase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for amylase "
                "activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0016160 carries the same amylase activity label but "
                "denotes the enzyme molecular function rather than the "
                "organism-level amylolytic enzyme production phenotype, so "
                "it is appropriate as a causal-node grounding rather than an "
                "equivalent TraitRecord xref."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-12",
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
            "Minted amylase activity as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden "
            "files; METPO has no exact amylase activity class yet."
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
