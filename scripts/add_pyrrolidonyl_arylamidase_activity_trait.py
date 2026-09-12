#!/usr/bin/env python3
"""Add pyrrolidonyl arylamidase activity with URL/DOI-backed evidence."""
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
    "pyrrolidonyl_arylamidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T03:14:57Z"

RECORD = {
    "identifier": "traitmech:000155",
    "label": "pyrrolidonyl arylamidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active pyrrolidonyl arylamidase enzymes that release N-terminal "
        "pyroglutamyl groups from peptide substrates."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC3/4/19/3.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC3/4/19/3.html",
            "snippet": (
                "Reaction: Release of an N-terminal pyroglutamyl group from "
                "a polypeptide, the second amino acid generally not being Pro"
            ),
            "notes": (
                "The NC-IUBMB EC 3.4.19.3 entry defines "
                "pyroglutamyl-peptidase I by its accepted reaction, grounding "
                "the peptidase activity named by the organism-level "
                "pyrrolidonyl arylamidase phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/JCM.37.11.3443-3447.1999",
            "snippet": (
                "The strains displayed acid phosphatase, alkaline "
                "phosphatase, ester lipase C8 (weak reaction), esterase C4 "
                "(weak reaction), leucine arylamidase, phosphoamidase, and "
                "pyrrolidonyl arylamidase activity."
            ),
            "notes": (
                "Collins et al. characterized six Corynebacterium auriscanis "
                "isolates that displayed pyrrolidonyl arylamidase activity, "
                "supporting this as a directly assayed bacterial "
                "enzyme-activity phenotype."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:99807",
            "taxon_label": "Corynebacterium auriscanis",
            "note": (
                "Collins et al. detected pyrrolidonyl arylamidase activity "
                "in Corynebacterium auriscanis isolates from dogs."
            ),
            "reference": "DOI:10.1128/JCM.37.11.3443-3447.1999",
        }
    ],
    "discussions": [
        {
            "discussion_id": "pyrrolidonyl-arylamidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for pyrrolidonyl "
                "arylamidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0016920 denotes pyroglutamyl-peptidase molecular "
                "function rather than the organism-level pyrrolidonyl "
                "arylamidase production phenotype, so it is appropriate as a "
                "causal-node grounding rather than an equivalent TraitRecord "
                "xref."
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
            "Minted pyrrolidonyl arylamidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact pyrrolidonyl "
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
