#!/usr/bin/env python3
"""Add alpha-fucosidase activity with URL/DOI-backed evidence."""
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
    "alpha_fucosidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T01:09:57Z"

RECORD = {
    "identifier": "traitmech:000152",
    "label": "alpha-fucosidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active alpha-fucosidase enzymes that hydrolyze alpha-L-fucosides to "
        "L-fucose and an alcohol."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC3/2/1/51.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC3/2/1/51.html",
            "snippet": (
                "Reaction: an α-L-fucoside + H2O = L-fucose + an alcohol"
            ),
            "notes": (
                "The NC-IUBMB EC 3.2.1.51 entry defines alpha-L-fucosidase by "
                "its accepted name and hydrolytic reaction, grounding the "
                "enzyme activity named by the organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/jcm.22.3.333-335.1985",
            "snippet": (
                "Positive reactions for alpha-glucosidase, beta-glucosidase, "
                'alpha-fucosidase, and alpha-glucuronidase suggest that "B. '
                'forsythus" may be saccharolytic.'
            ),
            "notes": (
                "Tanner et al. detected alpha-fucosidase in the then-proposed "
                "oral species Bacteroides forsythus with the API ZYM enzyme "
                "activity panel."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:28112",
            "taxon_label": "Tannerella forsythia",
            "note": (
                "Tanner et al. reported alpha-fucosidase-positive reactions "
                'for "Bacteroides forsythus", the basonym of Tannerella '
                "forsythia, in API ZYM profiles."
            ),
            "reference": "DOI:10.1128/jcm.22.3.333-335.1985",
        }
    ],
    "discussions": [
        {
            "discussion_id": "alpha-fucosidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "alpha-fucosidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004560 carries the alpha-L-fucosidase activity label but "
                "denotes the enzyme molecular function rather than the "
                "organism-level alpha-fucosidase production phenotype, so it "
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
            "Minted alpha-fucosidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact alpha-fucosidase "
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
