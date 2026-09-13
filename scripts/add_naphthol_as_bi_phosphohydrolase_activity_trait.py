#!/usr/bin/env python3
"""Add naphthol-AS-BI-phosphohydrolase activity with DOI-backed evidence."""
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
    "naphthol_as_bi_phosphohydrolase_activity.yaml"
)
LUDFIANI = "DOI:10.14202/vetworld.2024.143-149"
OTSUKA = "DOI:10.1128/JCM.43.8.3713-3717.2005"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T15:09:52Z"

RECORD = {
    "identifier": "traitmech:000174",
    "label": "naphthol-AS-BI-phosphohydrolase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active phosphohydrolases that hydrolyze naphthol-AS-BI-phosphate "
        "substrates."
    ),
    "definition_source": LUDFIANI,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "naphthol-AS-BI-phosphohydrolase",
            "synonym_type": "RELATED_SYNONYM",
            "source": LUDFIANI,
        }
    ],
    "evidence": [
        {
            "reference": LUDFIANI,
            "snippet": (
                "Naphthol-AS-BI-phosphohydrolase 5.4 "
                "Naphthol-AS-BI-phosphate"
            ),
            "notes": (
                "Ludfiani et al. list Naphthol-AS-BI-phosphate as the API "
                "ZYM naphthol-AS-BI-phosphohydrolase substrate, grounding "
                "the organism-level phenotype as hydrolysis of the "
                "naphthol-AS-BI phosphate chromogenic substrate."
            ),
        },
        {
            "reference": OTSUKA,
            "snippet": (
                "Alkaline phosphatase, esterase (C4), esterase lipase "
                "(C8), leucine arylamidase, acid phosphatase, and "
                "naphthol-AS-BI-phosphohydrolase were clearly positive"
            ),
            "notes": (
                "Otsuka et al. detected clear naphthol-AS-BI-"
                "phosphohydrolase API ZYM reactions in the five "
                "Corynebacterium resistens isolates they characterized."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:258224",
            "taxon_label": "Corynebacterium resistens",
            "note": (
                "Otsuka et al. detected clear naphthol-AS-BI-"
                "phosphohydrolase API ZYM reactions in Corynebacterium "
                "resistens isolates."
            ),
            "reference": OTSUKA,
        }
    ],
    "discussions": [
        {
            "discussion_id": (
                "naphthol-as-bi-phosphohydrolase-activity-xref-gap"
            ),
            "prompt": (
                "Resolve an exact external ontology class for "
                "naphthol-AS-BI-phosphohydrolase activity before adding a "
                "TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0016791 covers broad phosphatase activity at "
                "molecular-function scope, and no live GO class provides an "
                "exact naphthol-AS-BI-phosphate-specific phosphohydrolase "
                "production phenotype at organism-level scope."
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
            "Minted naphthol-AS-BI-phosphohydrolase activity as a "
            "DOI-backed TraitRecord after a repository-wide duplicate "
            "review covering ignored and hidden files; METPO has no exact "
            "naphthol-AS-BI-phosphohydrolase activity class yet and the "
            "placeholder is reserved in proposals/metpo_traitmech_v51."
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
