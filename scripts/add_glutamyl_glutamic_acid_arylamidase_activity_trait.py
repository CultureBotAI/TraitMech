#!/usr/bin/env python3
"""Add glutamyl glutamic acid arylamidase activity with DOI-backed evidence."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / (
    "glutamyl_glutamic_acid_arylamidase_activity.yaml"
)
AMYGDALOBACTER = "DOI:10.1099/ijsem.0.006017"
OLLEYA = "DOI:10.1099/ijs.0.63642-0"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T14:23:58Z"

RECORD = {
    "identifier": "traitmech:000173",
    "label": "glutamyl glutamic acid arylamidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active glutamyl glutamic acid arylamidase enzymes that hydrolyze "
        "glutamyl-glutamic-acid arylamide substrates."
    ),
    "definition_source": AMYGDALOBACTER,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "glutamyl glutamic acid arylamidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": AMYGDALOBACTER,
        }
    ],
    "evidence": [
        {
            "reference": AMYGDALOBACTER,
            "snippet": (
                "enzymatic activities are present for: α-galactosidase, "
                "N-acetyl-β-glucosaminidase, arginine arylamidase, proline "
                "arylamidase, leucyl glycine arylamidase, phenylalanine "
                "arylamidase, leucine arylamidase, tyrosine arylamidase, "
                "alanine arylamidase, glycine arylamidase, histidine "
                "arylamidase, glutamyl glutamic acid arylamidase, serine "
                "arylamidase, valine arylamidase, cysteine arylamidase, "
                "esterase, esterase lipase, alpha-chymotrypsin"
            ),
            "notes": (
                "Srinivasan et al. listed glutamyl glutamic acid "
                "arylamidase among enzymatic activities present in the "
                "Amygdalobacter indicium species description, supporting the "
                "API arylamidase row as a directly assayed bacterial "
                "enzyme-activity phenotype."
            ),
        },
        {
            "reference": OLLEYA,
            "snippet": (
                "arginine arylamidase, leucyl glycine arylamidase, "
                "phenylalanine arylamidase, leucine arylamidase, tyrosine "
                "arylamidase, alanine arylamidase, glycine arylamidase, "
                "histidine arylamidase, glutamyl glutamic acid arylamidase "
                "and serine arylamidase are positive"
            ),
            "notes": (
                "Nichols et al. listed glutamyl glutamic acid arylamidase "
                "as positive in Olleya marilimosa strain CAM030T."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:3029272",
            "taxon_label": "Amygdalobacter indicium",
            "note": (
                "Srinivasan et al. reported Amygdalobacter indicium as "
                "positive for glutamyl glutamic acid arylamidase activity in "
                "an enzyme activity panel."
            ),
            "reference": AMYGDALOBACTER,
        }
    ],
    "discussions": [
        {
            "discussion_id": "glutamyl-glutamic-acid-arylamidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for glutamyl "
                "glutamic acid arylamidase activity before adding a "
                "TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0016805 covers broad dipeptidase activity at "
                "molecular-function scope, and no live GO class provides an "
                "exact glutamyl-glutamic-acid-specific arylamidase production "
                "phenotype at organism-level scope."
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
            "Minted glutamyl glutamic acid arylamidase activity as a "
            "DOI-backed TraitRecord after a repository-wide duplicate review "
            "covering ignored and hidden files; METPO has no exact glutamyl "
            "glutamic acid arylamidase activity class yet and the placeholder "
            "is reserved in proposals/metpo_traitmech_v50."
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
