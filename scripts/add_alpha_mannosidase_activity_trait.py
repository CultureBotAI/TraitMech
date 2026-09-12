#!/usr/bin/env python3
"""Add alpha-mannosidase activity with URL/DOI-backed evidence."""
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
    "alpha_mannosidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T00:19:23Z"

RECORD = {
    "identifier": "traitmech:000150",
    "label": "alpha-mannosidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active alpha-mannosidase enzymes that hydrolyze terminal, "
        "non-reducing alpha-D-mannose residues in alpha-D-mannosides."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC3/2/1/24.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC3/2/1/24.html",
            "snippet": (
                "Reaction: Hydrolysis of terminal, non-reducing "
                "α-D-mannose residues in α-D-mannosides"
            ),
            "notes": (
                "The NC-IUBMB EC 3.2.1.24 entry defines alpha-mannosidase by "
                "its accepted name and hydrolytic reaction, grounding the "
                "enzyme activity named by the organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/jcm.32.3.854-855.1994",
            "snippet": (
                "Practically all A. haemolyticum strains (138 of 139) and "
                "the Listeria monocytogenes type strain were "
                "alpha-mannosidase positive"
            ),
            "notes": (
                "Carlson and Kontiainen detected alpha-mannosidase in nearly "
                "all tested Arcanobacterium haemolyticum strains with a 4-h "
                "alpha-mannosidase assay."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:28264",
            "taxon_label": "Arcanobacterium haemolyticum",
            "note": (
                "Carlson and Kontiainen reported 138 of 139 "
                "Arcanobacterium haemolyticum strains as alpha-mannosidase "
                "positive in a 4-h test."
            ),
            "reference": "DOI:10.1128/jcm.32.3.854-855.1994",
        }
    ],
    "discussions": [
        {
            "discussion_id": "alpha-mannosidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "alpha-mannosidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004559 carries the same alpha-mannosidase activity label "
                "but denotes the enzyme molecular function rather than the "
                "organism-level alpha-mannosidase production phenotype, so it "
                "is appropriate as a causal-node grounding rather than an "
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
            "Minted alpha-mannosidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact alpha-mannosidase "
            "activity class yet."
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
