#!/usr/bin/env python3
"""Add valine arylamidase activity with DOI-backed evidence."""
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
    "valine_arylamidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-11T17:00:22Z"

RECORD = {
    "identifier": "traitmech:000144",
    "label": "valine arylamidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active valine arylamidase enzymes that hydrolyze valine arylamide "
        "substrates."
    ),
    "definition_source": "DOI:10.3389/fmicb.2022.1034816",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "DOI:10.3389/fmicb.2022.1034816",
            "snippet": (
                "Positive alkaline phosphatase, cystine arylamidase, "
                "esterase(C4), esterase lipase(C8), leucine arylamidase, "
                "naphthol-AS-B1-phosphohydrolase, valine arylamidase"
            ),
            "notes": (
                "Jiang et al. treated valine arylamidase as an assayed "
                "enzyme-activity phenotype in the Geminicoccus harenae type "
                "species description."
            ),
        },
        {
            "reference": "DOI:10.1099/ijsem.0.002327",
            "snippet": (
                "enzyme detection with an API zym kit was positive for "
                "alkaline phosphatase, esterase, leucine arylamidase, valine "
                "arylamidase, acid phosphatase"
            ),
            "notes": (
                "Jung et al. detected valine arylamidase in Lactobacillus "
                "allii strain WiKim39 with the API ZYM enzyme activity panel."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2498453",
            "taxon_label": "Geminicoccus harenae",
            "note": (
                "Jiang et al. reported Geminicoccus harenae as positive for "
                "valine arylamidase in the API ZYM enzyme activity panel."
            ),
            "reference": "DOI:10.3389/fmicb.2022.1034816",
        }
    ],
    "discussions": [
        {
            "discussion_id": "valine-arylamidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for valine "
                "arylamidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004177 covers aminopeptidase activity at molecular-"
                "function scope and no live GO class provides an exact "
                "residue-specific valine arylamidase production phenotype at "
                "organism-level scope."
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
            "Minted valine arylamidase activity as a DOI-backed TraitRecord "
            "after a repository-wide duplicate review covering ignored and "
            "hidden files; METPO has no exact valine arylamidase activity "
            "class yet."
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
