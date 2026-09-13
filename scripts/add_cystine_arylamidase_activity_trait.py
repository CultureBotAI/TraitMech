#!/usr/bin/env python3
"""Add cystine arylamidase activity with DOI-backed evidence."""
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
    "cystine_arylamidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-11T19:19:57Z"

RECORD = {
    "identifier": "traitmech:000147",
    "label": "cystine arylamidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active cystine arylamidase enzymes that hydrolyze cystine arylamide "
        "substrates."
    ),
    "definition_source": "DOI:10.14202/vetworld.2024.143-149",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.14202/vetworld.2024.143-149",
            "snippet": (
                "Cystine arylamidase 7.5 L-cystyl-2-naphthylamide"
            ),
            "notes": (
                "Ludfiani et al. list L-cystyl-2-naphthylamide as the "
                "API ZYM cystine arylamidase substrate, grounding the "
                "organism-level phenotype as an arylamide-hydrolyzing enzyme "
                "activity."
            ),
        },
        {
            "reference": "DOI:10.3389/fmicb.2022.1034816",
            "snippet": (
                "Positive alkaline phosphatase, cystine arylamidase, "
                "esterase(C4), esterase lipase(C8), leucine arylamidase, "
                "naphthol-AS-B1-phosphohydrolase, valine arylamidase"
            ),
            "notes": (
                "Jiang et al. detected cystine arylamidase in the "
                "Geminicoccus harenae type strain with the API ZYM enzyme "
                "activity panel."
            ),
        },
        {
            "reference": "DOI:10.2323/jgam.60.59",
            "snippet": (
                "In API ZYM, activities are positive for alkaline "
                "phosphatase, esterase (C4), leucine arylamidase, valine "
                "arylamidase, cystine arylamidase"
            ),
            "notes": (
                "An et al. reported cystine arylamidase among positive "
                "API ZYM activities for the Flavobacterium panaciterrae "
                "DCY69T type strain."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2498453",
            "taxon_label": "Geminicoccus harenae",
            "note": (
                "Jiang et al. reported Geminicoccus harenae as positive for "
                "cystine arylamidase in the API ZYM enzyme activity panel."
            ),
            "reference": "DOI:10.3389/fmicb.2022.1034816",
        }
    ],
    "discussions": [
        {
            "discussion_id": "cystine-arylamidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for cystine "
                "arylamidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004177 covers aminopeptidase activity at "
                "molecular-function scope and no live GO class provides an "
                "exact residue-specific cystine arylamidase production "
                "phenotype at organism-level scope."
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
            "Minted cystine arylamidase activity as a DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact cystine "
            "arylamidase activity class yet."
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
