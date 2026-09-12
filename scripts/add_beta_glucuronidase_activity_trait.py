#!/usr/bin/env python3
"""Add beta-glucuronidase activity with URL/DOI-backed evidence."""
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
    "beta_glucuronidase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T00:37:27Z"

RECORD = {
    "identifier": "traitmech:000151",
    "label": "beta-glucuronidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active beta-glucuronidase enzymes that hydrolyze beta-D-glucuronosides "
        "to D-glucuronate and an alcohol."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC3/2/1/31.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC3/2/1/31.html",
            "snippet": (
                "Reaction: a β-D-glucuronoside + H2O = D-glucuronate + "
                "an alcohol"
            ),
            "notes": (
                "The NC-IUBMB EC 3.2.1.31 entry defines beta-glucuronidase by "
                "its accepted name and hydrolytic reaction, grounding the "
                "enzyme activity named by the organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/aem.50.6.1383-1387.1985",
            "snippet": (
                "The beta-glucuronidase produced by E. coli cleaves the MUG "
                "substrate to yield a fluorescent end product."
            ),
            "notes": (
                "Moberg used beta-glucuronidase cleavage of MUG to detect "
                "Escherichia coli in food samples."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Moberg reported beta-glucuronidase-mediated cleavage of MUG "
                "by Escherichia coli in a fluorogenic detection assay."
            ),
            "reference": "DOI:10.1128/aem.50.6.1383-1387.1985",
        }
    ],
    "discussions": [
        {
            "discussion_id": "beta-glucuronidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "beta-glucuronidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004566 carries the same beta-glucuronidase activity label "
                "but denotes the enzyme molecular function rather than the "
                "organism-level beta-glucuronidase production phenotype, so it "
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
            "Minted beta-glucuronidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact beta-glucuronidase "
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
