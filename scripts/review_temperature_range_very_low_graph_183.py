#!/usr/bin/env python3
"""Review temperature-range-very-low graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_temperature_range_very_low_graph_183.py
    python scripts/review_temperature_range_very_low_graph_183.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "environment/temperature_range_very_low"
GRAPH_ID = "temperature_range_very_low_psychrophile"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T04:40:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "rna_secondary_structure",
            "label": "mRNA/RNA secondary structure",
            "node_type": "CHEMICAL",
            "description": "Cold-stabilized RNA secondary structures impeding translation.",
        },
        "after": {
            "node_id": "cold_stabilized_rna_secondary_structure",
            "label": "cold-stabilized mRNA/RNA secondary structure",
            "node_type": "QUALITY",
            "description": "Cold-stabilized RNA secondary structures impeding translation.",
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "membrane_fatty_acid_desaturation",
            "predicate": "increases",
            "object": "membrane_fluidity",
            "description": (
                "Homeoviscous adaptation via lipid desaturation maintains membrane "
                "fluidity in the cold."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "notes": (
                        "Cells adapt membrane composition (increasing double bonds "
                        "in lipids) to maintain fluidity and function."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "membrane_fatty_acid_desaturation",
            "predicate": "increases",
            "object": "membrane_fluidity",
            "description": (
                "Homeoviscous adaptation via lipid desaturation maintains membrane "
                "fluidity in the cold."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "snippet": "production of double bonds in lipids",
                    "notes": (
                        "Verified against the open Ramón et al. PubMed abstract; "
                        "the multifactorial cold-adaptation model lists membrane "
                        "composition adaptation by producing lipid double bonds."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "low_temperature",
            "predicate": "activates",
            "object": "two_component_cold_signaling",
            "description": (
                "Cold-induced membrane state changes activate two-component cold signaling."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "notes": (
                        "Cold sensing occurs via changes in the liquid-crystalline "
                        "state of membranes that activate two-component signaling "
                        "systems."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "low_temperature",
            "predicate": "activates",
            "object": "two_component_cold_signaling",
            "description": (
                "Cold-induced membrane state changes activate two-component cold signaling."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "snippet": "activation of a two-component system",
                    "notes": (
                        "Verified against the open Ramón et al. PubMed abstract; "
                        "cold sensing is described as occurring mainly through "
                        "liquid-crystalline membrane-state changes that activate a "
                        "two-component signal-transduction system."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "cold_shock_proteins",
            "predicate": "acts on",
            "object": "rna_secondary_structure",
            "description": (
                "CspA-family RNA chaperones resolve cold-stabilized RNA structures "
                "to sustain translation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s42770-023-01057-4",
                    "notes": (
                        "Cold-shock proteins (CSPs) act on mRNAs; increased levels "
                        "of nucleic-acid-binding CspA-related proteins."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cold_shock_proteins",
            "predicate": "regulates",
            "object": "cold_stabilized_rna_secondary_structure",
            "description": (
                "CspA-family RNA chaperones regulate cold-stabilized RNA structures "
                "to sustain translation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.4161/rna.7.6.13482",
                    "snippet": "through their RNA chaperoning function",
                    "notes": (
                        "Verified against the open Phadtare and Severinov PubMed "
                        "abstract; CspA-family cold-shock proteins are described "
                        "as RNA-modulating proteins affecting low-temperature "
                        "transcription and possibly translation through RNA "
                        "chaperoning."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "molecular_chaperones",
            "predicate": "preserves",
            "object": "proteostasis_cold",
            "description": (
                "Chaperone/protease systems counter cold-slowed folding and misfolding risk."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1197797",
                    "notes": (
                        "Psychrophiles constitutively synthesize molecular "
                        "chaperones; Clp/GroEL/DnaK/GroES/TF upregulated during "
                        "cold shock."
                    ),
                }
            ],
        },
        "after": {
            "subject": "molecular_chaperones",
            "predicate": "contributes to",
            "object": "proteostasis_cold",
            "description": (
                "Chaperone/protease systems contribute to proteostasis by "
                "countering cold-slowed folding and misfolding risk."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1197797",
                    "snippet": "heat shock proteins associated to folding",
                    "notes": (
                        "Verified against the open Ramasamy et al. PMC text; the "
                        "Antarctic psychrophile review discusses heat-shock "
                        "proteins associated with protein folding in 4 °C versus "
                        "18 °C Pseudoalteromonas haloplanktis TAC125."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "compatible_solutes",
            "predicate": "stabilizes",
            "object": "protein_membrane_stabilization",
            "description": (
                "Osmolytes lower freezing damage and stabilize proteins and membranes."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1197797",
                    "notes": (
                        "Accumulation of compatible osmolytes prevents cell "
                        "shrinkage, lowers cytoplasmic freezing point, and "
                        "stabilizes proteins and membranes."
                    ),
                }
            ],
        },
        "after": {
            "subject": "compatible_solutes",
            "predicate": "contributes to",
            "object": "protein_membrane_stabilization",
            "description": (
                "Osmolytes contribute to protein and membrane stabilization while "
                "lowering freezing damage."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1197797",
                    "snippet": ("stabilizing membranes and proteins at chilling temperatures"),
                    "notes": (
                        "Verified against the open Ramasamy et al. PMC text; "
                        "Antarctic compatible osmolytes are described as restoring "
                        "osmotic balance, scavenging free radicals, counteracting "
                        "protein aggregation, improving protein folding, and "
                        "stabilizing membranes and proteins."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "ice_binding_proteins",
            "predicate": "inhibits",
            "object": "ice_crystal_growth",
            "description": (
                "AFPs/IBPs bind ice and inhibit ice-crystal growth and recrystallization."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1197797",
                    "notes": (
                        "AFPs bind ice, inhibit ice-crystal growth, produce thermal "
                        "hysteresis, and show IRI activity."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
            "subject": "ice_binding_proteins",
            "predicate": "inhibits",
            "object": "ice_crystal_growth",
            "description": (
                "AFPs/IBPs bind ice and inhibit ice-crystal growth and recrystallization."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2023.1197797",
                    "snippet": "inhibits the growth of ice crystals",
                    "notes": (
                        "Verified against the open Ramasamy et al. PMC text; ice "
                        "binding proteins are described as antifreeze proteins that "
                        "bind ice, inhibit ice-crystal growth, lower freezing "
                        "temperature, create a thermal hysteresis gap, and display "
                        "ice-recrystallization inhibition activity."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
]


def _edge_key(edge: dict[str, Any]) -> tuple[str | None, str | None, str | None]:
    return edge.get("subject"), edge.get("predicate"), edge.get("object")


def _find_graph(doc: dict[str, Any]) -> dict[str, Any]:
    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1:
        raise ValueError(f"{SLUG}: expected exactly one graph, found {len(graphs)}")
    graph = graphs[0]
    if graph.get("graph_id") != GRAPH_ID:
        raise ValueError(f"{SLUG}: expected graph_id {GRAPH_ID!r}")
    if graph.get("scope_status") != "NONMECHANISTIC":
        raise ValueError(f"{SLUG}: expected a NONMECHANISTIC graph")
    return graph


def _nodes_by_state(state: str) -> dict[str, dict[str, Any]]:
    return {replacement[state]["node_id"]: replacement[state] for replacement in NODE_REPLACEMENTS}


def _edges_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _assert_exact_nodes(
    graph: dict[str, Any], expected_by_id: dict[str, dict[str, Any]], state: str
) -> None:
    existing_by_id = {node.get("node_id"): node for node in graph.get("nodes") or []}
    missing = set(expected_by_id) - set(existing_by_id)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} node(s): {sorted(missing)}")
    for node_id, expected in expected_by_id.items():
        if existing_by_id[node_id] != expected:
            raise ValueError(f"{SLUG}: {state} node drifted: {node_id}")


def _assert_exact_edges(
    graph: dict[str, Any],
    expected_by_key: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
    state: str,
) -> None:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    missing = set(expected_by_key) - set(existing_by_key)
    if missing:
        raise ValueError(f"{SLUG}: missing {state} edge(s): {sorted(missing)}")
    for key, expected in expected_by_key.items():
        if existing_by_key[key] != expected:
            raise ValueError(f"{SLUG}: {state} edge drifted: {key}")


def _has_exact_nodes(graph: dict[str, Any], nodes: dict[str, dict[str, Any]]) -> bool:
    existing_by_id = {node.get("node_id"): node for node in graph.get("nodes") or []}
    return all(existing_by_id.get(node_id) == node for node_id, node in nodes.items())


def _has_exact_edges(
    graph: dict[str, Any],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_by_key = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    return all(existing_by_key.get(key) == edge for key, edge in edges.items())


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_nodes = _nodes_by_state("before")
    after_nodes = _nodes_by_state("after")
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")

    migrated_node_ids = set(after_nodes) - set(before_nodes)
    existing_node_ids = {node.get("node_id") for node in graph.get("nodes") or []}
    present_migrated_node_ids = existing_node_ids & migrated_node_ids

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    if _has_exact_nodes(graph, after_nodes) and _has_exact_edges(graph, after_edges):
        return False

    if (
        present_migrated_node_ids == migrated_node_ids
        and present_migrated_edge_keys == migrated_edge_keys
    ):
        _assert_exact_nodes(graph, after_nodes, "migrated")
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_node_ids or present_migrated_edge_keys:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"nodes={sorted(present_migrated_node_ids)} "
            f"edges={sorted(present_migrated_edge_keys)}"
        )

    _assert_exact_nodes(graph, before_nodes, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_node_id = {
        replacement["before"]["node_id"]: replacement["after"] for replacement in NODE_REPLACEMENTS
    }
    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    graph["nodes"] = [
        copy.deepcopy(after_by_before_node_id.get(node.get("node_id"), node))
        for node in graph.get("nodes") or []
    ]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the temperature_range_very_low_psychrophile graph for "
            "issue #183: added snippets to 6 edge-level evidence items, "
            "grounded 3 residual predicates, and narrowed 1 local node "
            "identifier and type for cold-stabilized RNA secondary structure. "
            "No paid research service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    path = REPO_ROOT / "data" / "traits" / f"{SLUG}.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if transform(SLUG, doc):
        changed = 1
        if write:
            write_validated_trait(doc, path)
        else:
            with tempfile.TemporaryDirectory() as tmp:
                write_validated_trait(doc, Path(tmp) / path.name)
    print(f"{'applied' if write else 'dry run'}: reviewed {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
