#!/usr/bin/env python3
"""Add gas-vesicle-mediated cellular buoyancy as a physiology trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "cellular_buoyancy.yaml"
GAS_VESICLE = REPO_ROOT / "data" / "traits" / "morphology" / "gas_vesicle.yaml"
INTRACELLULAR_INCLUSION = (
    REPO_ROOT / "data" / "traits" / "morphology" / "intracellular_inclusion.yaml"
)

FENG = "DOI:10.1186/s13036-024-00426-3"
PFEIFER_2022 = "DOI:10.3390/life12091455"
MLOUKA = "DOI:10.1128/JB.186.8.2355-2365.2004"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T22:49:00Z"
IDENTIFIER = "traitmech:000528"
PROPOSAL = "proposals/metpo_traitmech_v405"


def feng_physical_buoyancy_evidence() -> dict[str, str]:
    return {
        "reference": FENG,
        "snippet": (
            "can provide buoyancy for them to move up and down the water "
            "to obtain nutrients"
        ),
        "notes": (
            "Feng et al. review gas-vesicle physical properties that provide "
            "buoyancy for photosynthetic bacteria and halophilic archaea."
        ),
    }


def feng_photosynthetic_buoyancy_evidence() -> dict[str, str]:
    return {
        "reference": FENG,
        "snippet": (
            "give them the buoyancy to move upward so that they can get "
            "enough light for photosynthesis"
        ),
        "notes": (
            "Feng et al. describe gas vesicles giving photosynthetic bacteria "
            "buoyancy to move upward toward sufficient light."
        ),
    }


def feng_shell_evidence() -> dict[str, str]:
    return {
        "reference": FENG,
        "snippet": (
            "The gas vesicle (GV) is like a hollow nanoparticle consisting "
            "of an internal gas and a protein shell"
        ),
        "notes": (
            "Feng et al. describe the gas vesicle as an internal gas "
            "compartment bounded by a protein shell."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "cellular buoyancy",
    "definition": (
        "A physiology trait in which intracellular gas vesicles reduce a "
        "microbial cell's effective density enough to provide buoyancy and "
        "vertical positioning in the water column."
    ),
    "definition_source": FENG,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [
        {
            "synonym_text": "buoyancy",
            "synonym_type": "RELATED_SYNONYM",
            "source": FENG,
        }
    ],
    "evidence": [
        feng_physical_buoyancy_evidence(),
        feng_photosynthetic_buoyancy_evidence(),
        {
            "reference": PFEIFER_2022,
            "snippet": (
                "Approximately 3–10% of the cell volume must be occupied by "
                "gas vesicles to provide buoyancy"
            ),
            "notes": (
                "Pfeifer reviews gas-vesicle proteins and summarizes the "
                "fraction of cell volume that must contain gas vesicles to "
                "confer buoyancy."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1126",
            "taxon_label": "Microcystis aeruginosa",
            "note": (
                "Mlouka et al. mapped the M. aeruginosa gas-vesicle gene "
                "cluster and DNA rearrangements that lead to loss of cellular "
                "buoyancy."
            ),
            "reference": MLOUKA,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "gas_vesicles_confer_cellular_buoyancy",
            "title": "Gas vesicles confer cellular buoyancy",
            "description": (
                "Evidence-backed causal sketch linking a proteinaceous "
                "gas-filled organelle to cellular buoyancy."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph records the organelle-scale physical "
                "gas-vesicle branch and leaves taxon-specific Gvp protein "
                "assembly to the gas-vesicle morphology record. It does not "
                "assert that all planktonic depth regulation is gas-vesicle "
                "mediated."
            ),
            "nodes": [
                {
                    "node_id": "gas_vesicle_shell",
                    "label": "gas vesicle shell",
                    "node_type": "CELLULAR_LOCALIZATION",
                    "description": (
                        "Proteinaceous shell enclosing the gas-vesicle lumen."
                    ),
                    "grounding": "GO:0033172",
                },
                {
                    "node_id": "gas_vesicle",
                    "label": "gas vesicle",
                    "node_type": "ORGANELLE",
                    "description": (
                        "Hollow gas-filled protein nanocompartment that "
                        "displaces cytoplasmic volume."
                    ),
                    "grounding": "GO:0031411",
                },
                {
                    "node_id": "cellular_buoyancy_trait",
                    "label": "cellular buoyancy",
                    "node_type": "TRAIT",
                    "description": (
                        "Gas-vesicle-mediated capacity for upward flotation "
                        "or water-column positioning."
                    ),
                    "grounding": IDENTIFIER,
                },
            ],
            "edges": [
                {
                    "subject": "gas_vesicle_shell",
                    "predicate": "part of",
                    "predicate_id": "biolink:part_of",
                    "object": "gas_vesicle",
                    "description": (
                        "The protein shell encloses the internal gas volume "
                        "as part of the gas vesicle."
                    ),
                    "evidence": [feng_shell_evidence()],
                },
                {
                    "subject": "gas_vesicle",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "cellular_buoyancy_trait",
                    "description": (
                        "Gas-filled vesicles lower effective cellular "
                        "density and provide buoyancy."
                    ),
                    "evidence": [
                        feng_physical_buoyancy_evidence(),
                        feng_photosynthetic_buoyancy_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "cellular-buoyancy-xref-gap",
            "prompt": (
                "Resolve exact external ontology xrefs for gas-vesicle-mediated "
                "cellular buoyancy."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact active local METPO class was accepted for the "
                "organism-level cellular-buoyancy physiology trait. The only "
                "buoyancy hit in the local METPO snapshot is obsolete buoyancy "
                "structure, and GO:0031411 denotes the gas vesicle organelle "
                "rather than the gas-vesicle-conferred physiological "
                "disposition."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
        },
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def ground_existing_buoyancy_node(
    record: dict[str, Any],
    *,
    expected_identifier: str,
    expected_label: str,
    expected_node_label: str,
) -> None:
    assert record["identifier"] == expected_identifier
    assert record["label"] == expected_label
    assert record["mapping_status"] == "REVIEWED"

    graphs = record.get("causal_graphs") or []
    matching = [
        node
        for graph in graphs
        for node in graph.get("nodes", [])
        if node.get("node_id") == "buoyancy"
    ]
    assert len(matching) == 1

    node = matching[0]
    assert node["label"] == expected_node_label
    assert node["node_type"] == "TRAIT"
    assert node.get("grounding") in (None, "")
    node["grounding"] = IDENTIFIER

    record_curation_event(
        record,
        curator=CURATOR,
        action="GROUND_CAUSAL_NODE_TO_NEW_TRAIT",
        changes=(
            "Grounded the existing causal-graph buoyancy TRAIT node to newly "
            f"minted {IDENTIFIER} cellular buoyancy."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write YAML files")
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted cellular buoyancy as a DOI-backed PHYSIOLOGY TraitRecord "
            "after an ignored-and-hidden duplicate review found no exact "
            "same-scope TraitMech, METPO, history, or prior proposal record; "
            f"the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    gas_vesicle = load_trait(GAS_VESICLE)
    ground_existing_buoyancy_node(
        gas_vesicle,
        expected_identifier="traitmech:000070",
        expected_label="gas vesicle",
        expected_node_label="cellular buoyancy",
    )

    intracellular_inclusion = load_trait(INTRACELLULAR_INCLUSION)
    ground_existing_buoyancy_node(
        intracellular_inclusion,
        expected_identifier="traitmech:000066",
        expected_label="intracellular inclusion",
        expected_node_label="buoyancy",
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(gas_vesicle, GAS_VESICLE)
        write_validated_trait(intracellular_inclusion, INTRACELLULAR_INCLUSION)
        print(f"wrote {rel}")
        print(f"updated {GAS_VESICLE.relative_to(REPO_ROOT)}")
        print(f"updated {INTRACELLULAR_INCLUSION.relative_to(REPO_ROOT)}")
    else:
        print(f"would write {rel}")
        print(f"would update {GAS_VESICLE.relative_to(REPO_ROOT)}")
        print(f"would update {INTRACELLULAR_INCLUSION.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
