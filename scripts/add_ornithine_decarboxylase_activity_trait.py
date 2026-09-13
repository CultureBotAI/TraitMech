#!/usr/bin/env python3
"""Add ornithine decarboxylase activity with URL/DOI-backed evidence."""
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
    "ornithine_decarboxylase_activity.yaml"
)
CURATOR = "codex"
TIMESTAMP = "2026-09-12T02:38:18Z"

RECORD = {
    "identifier": "traitmech:000154",
    "label": "ornithine decarboxylase activity",
    "definition": (
        "A physiological enzyme-activity phenotype in which a cell produces "
        "active ornithine decarboxylase enzymes that decarboxylate "
        "L-ornithine to putrescine and carbon dioxide."
    ),
    "definition_source": "https://iubmb.qmul.ac.uk/enzyme/EC4/1/1/17.html",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": "https://iubmb.qmul.ac.uk/enzyme/EC4/1/1/17.html",
            "snippet": "Reaction: L-ornithine = putrescine + CO2",
            "notes": (
                "The NC-IUBMB EC 4.1.1.17 entry defines ornithine "
                "decarboxylase by its accepted name and reaction from "
                "L-ornithine to putrescine and CO2, grounding the enzyme "
                "activity named by the organism-level phenotype."
            ),
        },
        {
            "reference": "DOI:10.1128/jb.124.2.791-799.1975",
            "snippet": (
                "Several Escherichia coli K-12 mutants blocked in the "
                "synthesis of ornithine decarboxylase (OD) were isolated "
                "after transduction for serA+ in a strain (MA197) blocked in "
                "agmatine ureohydrolase (AUH) with a mutagenized phage lysate "
                "of P1. The new double-polyamine mutants were characterized "
                "by an unconditional polyamine dependence; either putrescine "
                "or spermidine was required for normal growth. The mutational "
                "block was varified by the demonstration of a virtual absence "
                "of OD activity in cellular extracts."
            ),
            "notes": (
                "Cunningham-Rundles and Maas isolated Escherichia coli K-12 "
                "mutants blocked in ornithine decarboxylase synthesis and "
                "verified the loss of OD activity, supporting E. coli K-12 "
                "as a direct organismal example for the activity."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:83333",
            "taxon_label": "Escherichia coli K-12",
            "note": (
                "Cunningham-Rundles and Maas isolated E. coli K-12 speC "
                "mutants with a virtual absence of ornithine decarboxylase "
                "activity in cellular extracts."
            ),
            "reference": "DOI:10.1128/jb.124.2.791-799.1975",
        }
    ],
    "discussions": [
        {
            "discussion_id": "ornithine-decarboxylase-activity-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for ornithine "
                "decarboxylase activity before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "GO:0004586 carries the same ornithine decarboxylase "
                "activity label but denotes the enzyme molecular function "
                "rather than the organism-level ornithine decarboxylase "
                "production phenotype, so it is appropriate as a causal-node "
                "grounding rather than an equivalent TraitRecord xref."
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
            "Minted ornithine decarboxylase activity as a URL/DOI-backed "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; METPO has no exact ornithine "
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
