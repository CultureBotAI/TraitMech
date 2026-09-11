#!/usr/bin/env python3
"""Add caseinase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "caseinase_activity.yaml"
CURATOR = "codex"
TIMESTAMP = "2026-09-11T00:00:00Z"

RECORD = {
    "identifier": "traitmech:000137",
    "label": "caseinase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active caseinase proteases that hydrolyze casein."
    ),
    "definition_source": "DOI:10.3389/fmicb.2018.01148",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "caseinase production",
            "synonym_type": "RELATED_SYNONYM",
            "source": "DOI:10.2174/1874285801408010025",
        }
    ],
    "evidence": [
        {
            "reference": "DOI:10.3389/fmicb.2018.01148",
            "snippet": (
                "two enzymes secreted by a B. cereus RC6 strain that permits "
                "the degradation of casein"
            ),
            "notes": (
                "Ouertani et al. identify secreted Bacillus cereus RC6 "
                "proteases that degrade casein in a dairy-product context."
            ),
        },
        {
            "reference": "DOI:10.2174/1874285801408010025",
            "snippet": (
                "screened for enzyme production (caseinase, gelatinase, "
                "amylase, carboxymethyl cellulase, and esterase)"
            ),
            "notes": (
                "Alves et al. use caseinase as a reusable extracellular "
                "hydrolytic-enzyme phenotype while screening environmental "
                "microbial isolates."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1396",
            "taxon_label": "Bacillus cereus",
            "note": (
                "Bacillus cereus RC6 secreted casein-degrading proteases in "
                "milk-matrix experiments."
            ),
            "reference": "DOI:10.3389/fmicb.2018.01148",
        }
    ],
    "discussions": [
        {
            "discussion_id": "caseinase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for caseinase "
                "activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0008233 is a generic peptidase-activity class and is too "
                "broad for caseinase activity as an equivalent TraitRecord xref."
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
            "Minted caseinase activity as a DOI-backed TraitRecord after a "
            "repository-wide duplicate review covering ignored and hidden files; "
            "METPO has no exact caseinase activity class yet."
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
