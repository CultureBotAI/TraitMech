#!/usr/bin/env python3
"""Add lysine decarboxylase activity with URL/DOI-backed evidence."""
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
    "lysine_decarboxylase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T01:35:50Z"

RECORD = {
    "identifier": "traitmech:000153",
    "label": "lysine decarboxylase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active lysine decarboxylase enzymes that decarboxylate L-lysine to "
        "cadaverine and carbon dioxide."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC4/1/1/18.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC4/1/1/18.html",
            "snippet": "Reaction: L-lysine = cadaverine + CO2",
            "notes": (
                "The NC-IUBMB EC 4.1.1.18 entry defines lysine "
                "decarboxylase by its accepted name and reaction from "
                "L-lysine to cadaverine and CO2, grounding the enzyme "
                "activity named by the organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/jb.01306-06",
            "snippet": (
                "Unexpectedly, the tolerance of P(i)-starved cells to "
                "fermentation acids was markedly increased as a result of "
                "the activity of the inducible CadBA lysine-dependent acid "
                "resistance system that consumes one proton and produces "
                "the diamine cadaverine."
            ),
            "notes": (
                "Moreau showed that the Escherichia coli inducible CadBA "
                "lysine-dependent acid resistance system produces "
                "cadaverine during phosphate starvation."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Moreau reported CadBA lysine-dependent acid resistance "
                "activity in phosphate-starved Escherichia coli."
            ),
            "reference": "DOI:10.1128/jb.01306-06",
        }
    ],
    "discussions": [
        {
            "discussion_id": "lysine-decarboxylase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for lysine "
                "decarboxylase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0008923 carries the same lysine decarboxylase activity "
                "label but denotes the enzyme molecular function rather than "
                "the organism-level lysine decarboxylase production "
                "phenotype, so it is appropriate as a causal-node grounding "
                "rather than an equivalent TraitRecord xref."
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
            "Minted lysine decarboxylase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact lysine "
            "decarboxylase activity class yet."
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
