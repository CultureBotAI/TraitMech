#!/usr/bin/env python3
"""Add pyrazinamidase activity with URL/DOI-backed evidence."""
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
    "pyrazinamidase_activity.yaml"
)
IUBMB = "https://iubmb.qmul.ac.uk/enzyme/EC3/5/1/19.html"
ZHANG = "DOI:10.1111/j.1742-4658.2007.06241.x"
PETRELLA = "DOI:10.1371/journal.pone.0015785"
CURATOR = "codex"
TIMESTAMP = "2026-09-12T09:07:58Z"

RECORD = {
    "identifier": "traitmech:000163",
    "label": "pyrazinamidase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active nicotinamidase/pyrazinamidase enzymes that hydrolyze "
        "nicotinamide and can convert pyrazinamide to pyrazinoic acid."
    ),
    "definition_source": ZHANG,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "nicotinamidase activity",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "nicotinamidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "nicotinamide amidohydrolase",
            "synonym_type": "RELATED_SYNONYM",
            "source": IUBMB,
        },
        {
            "synonym_text": "nicotinamidase/pyrazinamidase",
            "synonym_type": "RELATED_SYNONYM",
            "source": ZHANG,
        },
    ],
    "evidence": [
        {
            "reference": IUBMB,
            "snippet": (
                "<b>Reaction:</b> nicotinamide + "
                "H<small><sub>2</sub></small>O = nicotinate + "
                "NH<small><sub>3</sub></small>"
            ),
            "notes": (
                "The NC-IUBMB EC 3.5.1.19 entry grounds the "
                "nicotinamide-deamidating side of the PncA activity with "
                "the accepted nicotinamidase reaction."
            ),
        },
        {
            "reference": ZHANG,
            "snippet": (
                "The nicotinamidase/pyrazinamidase (PncA) of "
                "Mycobacterium tuberculosis is involved in the activation "
                "of the important front-line antituberculosis drug "
                "pyrazinamide by converting it into the active form, "
                "pyrazinoic acid."
            ),
            "notes": (
                "Zhang et al. characterized the Mycobacterium tuberculosis "
                "PncA enzyme, linking nicotinamidase/pyrazinamidase activity "
                "to cellular conversion of pyrazinamide into pyrazinoic acid."
            ),
        },
        {
            "reference": PETRELLA,
            "snippet": (
                "Pyrazinamidase (PncA) activates the first-line "
                "antituberculous drug pyrazinamide into pyrazinoic acid."
            ),
            "notes": (
                "Petrella et al. independently describe PncA as the "
                "pyrazinamidase that activates pyrazinamide, supporting the "
                "pyrazinamidase label for the organism-level activity."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1773",
            "taxon_label": "Mycobacterium tuberculosis",
            "note": (
                "Zhang et al. characterized active "
                "nicotinamidase/pyrazinamidase PncA from Mycobacterium "
                "tuberculosis."
            ),
            "reference": ZHANG,
        }
    ],
    "discussions": [
        {
            "discussion_id": "pyrazinamidase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for "
                "pyrazinamidase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0008936 nicotinamidase activity denotes the catalytic "
                "molecular function rather than the organism-level "
                "pyrazinamidase/nicotinamidase phenotype, so it is "
                "appropriate as a causal-node grounding for the source label "
                "and not as an equivalent TraitRecord xref."
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
            "Minted pyrazinamidase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact pyrazinamidase "
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
