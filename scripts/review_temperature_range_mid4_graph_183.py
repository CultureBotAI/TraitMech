#!/usr/bin/env python3
"""Review temperature-range-mid4 graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_temperature_range_mid4_graph_183.py
    python scripts/review_temperature_range_mid4_graph_183.py --apply
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

SLUG = "environment/temperature_range_mid4"
GRAPH_ID = "temperature_range_mid4_warm_mesophile"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T04:20:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "membrane_lipid_composition",
            "label": "membrane lipid composition",
            "node_type": "QUALITY",
            "description": ("Saturated/unsaturated phospholipid makeup of the cell membrane."),
        },
        "after": {
            "node_id": "saturated_unsaturated_membrane_lipid_composition",
            "label": "saturated/unsaturated membrane lipid composition",
            "node_type": "QUALITY",
            "description": ("Saturated/unsaturated phospholipid makeup of the cell membrane."),
        },
    },
    {
        "before": {
            "node_id": "chaperone_systems",
            "label": "DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems",
            "node_type": "GENE_OR_PROTEIN",
            "grounding_status": "REVIEWED_LABEL_ONLY",
            "grounding_notes": (
                "Reviewed as a contextual protein or protein-complex label within "
                "a quantitative measurement graph; no exact semantic family term "
                "was established for this aggregate use."
            ),
            "description": (
                "Protective heat-shock chaperone systems that refold stress-damaged proteins."
            ),
        },
        "after": {
            "node_id": "heat_shock_chaperone_systems",
            "label": "DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems",
            "node_type": "GENE_OR_PROTEIN",
            "grounding_status": "REVIEWED_LABEL_ONLY",
            "grounding_notes": (
                "Reviewed as a contextual protein or protein-complex label within "
                "a quantitative measurement graph; no exact semantic family term "
                "was established for this aggregate use."
            ),
            "description": (
                "Protective heat-shock chaperone systems that refold stress-damaged proteins."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "fab_branchpoint_valve",
            "predicate": "enables",
            "object": "homeoviscous_adaptation",
            "description": (
                "The FabI/FabB branchpoint valve reallocates flux between "
                "saturated and unsaturated fatty acid synthesis, enabling "
                "homeoviscous adaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53677-5",
                    "notes": (
                        "A temperature-sensitive metabolic valve at the "
                        "fatty-acid branchpoint reallocates flux between saturated "
                        "and unsaturated fatty acid synthesis via FabI and FabB."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "fab_branchpoint_valve",
            "predicate": "enables",
            "object": "homeoviscous_adaptation",
            "description": (
                "The FabI/FabB branchpoint valve reallocates flux between "
                "saturated and unsaturated fatty acid synthesis, enabling "
                "homeoviscous adaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53677-5",
                    "snippet": "allocates flux between the saturated and unsaturated",
                    "notes": (
                        "Verified against the open Hoogerland et al. abstract; the "
                        "E. coli temperature-sensitive metabolic valve allocates "
                        "fatty-acid synthesis flux through FabI and FabB."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
    },
    {
        "before": {
            "subject": "fab_c10_competition",
            "predicate": "regulates",
            "object": "membrane_lipid_composition",
            "description": (
                "Competition of FabA/FabI/FabB for the common C10:1 pool shifts "
                "flux between saturated and unsaturated fatty acids, changing "
                "membrane lipid composition."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53677-5",
                    "notes": (
                        "FabA, FabI and FabB compete for a common C10:1 pool "
                        "forming a metabolic valve that shifts flux between "
                        "saturated and unsaturated fatty acids."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
        "after": {
            "subject": "fab_c10_competition",
            "predicate": "regulates",
            "object": "saturated_unsaturated_membrane_lipid_composition",
            "description": (
                "Competition of FabA/FabI/FabB for the common C10:1 pool shifts "
                "flux between saturated and unsaturated fatty acids, changing "
                "saturated/unsaturated membrane lipid composition."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53677-5",
                    "snippet": "compete for a common pool of substrates",
                    "notes": (
                        "Verified against the open Hoogerland et al. Figure 1 "
                        "legend; FabA interconverts the C10:1 acyl-ACP substrates "
                        "used by FabI and FabB, making the enzymes indirectly "
                        "compete for one pool."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "membrane_fluidity_restoration",
            "predicate": "enables",
            "object": "growth_after_temperature_shock",
            "description": (
                "Valve plus transcriptional feedback restores optimal membrane "
                "fluidity within a single generation, supporting growth after a "
                "temperature shock."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53677-5",
                    "notes": (
                        "Restores optimal membrane fluidity within a single "
                        "generation after a temperature shock."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "membrane_fluidity_restoration",
            "predicate": "contributes to",
            "object": "growth_after_temperature_shock",
            "description": (
                "Valve plus transcriptional feedback restores optimal membrane "
                "fluidity within a single generation, contributing to growth after "
                "a temperature shock."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53677-5",
                    "snippet": "restores optimal membrane fluidity within a single generation",
                    "notes": (
                        "Verified against the open Hoogerland et al. abstract; the "
                        "measured E. coli fatty-acid and phospholipid pathway "
                        "connects membrane-fluidity restoration to recovery from "
                        "temperature shock."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "heat_stress",
            "predicate": "causes",
            "object": "protein_unfolding_aggregation",
            "description": "High temperatures cause protein unfolding and aggregation.",
            "evidence": [
                {
                    "reference": "DOI:10.1186/s12864-023-09266-9",
                    "notes": (
                        "High temperatures cause a suite of problems for cells, "
                        "including protein unfolding and aggregation."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "heat_stress",
            "predicate": "causes",
            "object": "protein_unfolding_aggregation",
            "description": "High temperatures cause protein unfolding and aggregation.",
            "evidence": [
                {
                    "reference": "DOI:10.1186/s12864-023-09266-9",
                    "snippet": "unfold or misfold proteins",
                    "notes": (
                        "Verified against the open McGuire and Nano introduction; "
                        "the review context lists unfolding, misfolding, and "
                        "aggregation among the high-temperature cellular problems "
                        "near TMAX."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "protein_unfolding_aggregation",
            "predicate": "causes",
            "object": "mesophile_growth_impairment",
            "description": (
                "Protein unfolding and aggregation impairs mesophile growth unless compensated."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/s12864-023-09266-9",
                    "notes": (
                        "General mechanistic background applicable to the "
                        "warm-mesophile upper range; protein damage impairs growth "
                        "unless compensated."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "protein_unfolding_aggregation",
            "predicate": "contributes to",
            "object": "mesophile_growth_impairment",
            "description": (
                "Protein unfolding and aggregation contributes to mesophile growth "
                "impairment unless compensated."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/s12864-023-09266-9",
                    "snippet": "present many problems",
                    "notes": (
                        "Verified against the open McGuire and Nano introduction; "
                        "the paper frames high-temperature RNA, protein, lipid, "
                        "and DNA effects as cellular problems near the maximum "
                        "growth temperature."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "heat_stress",
            "predicate": "causes",
            "object": "membrane_fluidity",
            "description": (
                "High temperatures increase membrane fluidity, requiring compensatory adaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/s12864-023-09266-9",
                    "notes": (
                        "High temperatures cause a suite of problems for cells, "
                        "including increased membrane fluidity."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "heat_stress",
            "predicate": "positively regulates",
            "object": "membrane_fluidity",
            "description": (
                "High temperatures increase membrane fluidity, requiring compensatory adaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/s12864-023-09266-9",
                    "snippet": "cause increased membrane fluidity",
                    "notes": (
                        "Verified against the open McGuire and Nano introduction; "
                        "increased membrane fluidity is listed as a "
                        "high-temperature effect on cells."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "membrane_fluidity",
            "predicate": "requires",
            "object": "compensatory_adaptation",
            "description": (
                "Temperature-driven increase in membrane fluidity requires compensatory adaptation."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1186/s12864-023-09266-9",
                    "notes": (
                        "Increased membrane fluidity at high temperature requires "
                        "compensatory adaptation to maintain function."
                    ),
                }
            ],
        },
        "after": {
            "subject": "compensatory_adaptation",
            "predicate": "regulates",
            "object": "membrane_fluidity",
            "description": (
                "Compensatory membrane adaptation regulates temperature-driven "
                "membrane-fluidity changes."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53677-5",
                    "snippet": "maintains cell membranes at a fixed viscosity level",
                    "notes": (
                        "Verified against the open Hoogerland et al. introduction; "
                        "homeoviscous adaptation counteracts temperature by "
                        "varying unsaturated, branched-chain, or chain-length lipid "
                        "features to stabilize viscosity."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "rpoh_regulon",
            "predicate": "induces",
            "object": "chaperone_systems",
            "description": (
                "The sigma-32/RpoH regulon induces the DnaK/DnaJ/GrpE and "
                "GroES/GroEL chaperone systems."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03105-23",
                    "notes": (
                        "The alternative sigma factor sigma-32 (RpoH) drives "
                        "protective heat shock proteins including the "
                        "DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems."
                    ),
                }
            ],
        },
        "after": {
            "subject": "rpoh_regulon",
            "predicate": "positively regulates",
            "object": "heat_shock_chaperone_systems",
            "description": (
                "The sigma-32/RpoH regulon positively regulates the DnaK/DnaJ/GrpE "
                "and GroES/GroEL chaperone systems."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03105-23",
                    "snippet": "RpoH) that drives the expression",
                    "notes": (
                        "Verified against the open Berdejo et al. introduction; "
                        "RpoH is described as the main governor of the Salmonella "
                        "Typhimurium heat-shock response and as driving protective "
                        "heat-shock-protein expression."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "chaperone_systems",
            "predicate": "enables",
            "object": "heat_stress_protection",
            "description": (
                "The DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems protect against heat stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03105-23",
                    "notes": (
                        "Canonical heat-response: chaperone systems refold "
                        "stress-damaged proteins to protect against heat stress."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "heat_shock_chaperone_systems",
            "predicate": "enables",
            "object": "heat_stress_protection",
            "description": (
                "The DnaK/DnaJ/GrpE and GroES/GroEL chaperone systems protect against heat stress."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/mbio.03105-23",
                    "snippet": "protective heat shock proteins",
                    "notes": (
                        "Verified against the open Berdejo et al. introduction; "
                        "DnaK/DnaJ/GrpE and GroES/GroEL are named as molecular "
                        "chaperone systems in the protective heat-shock-protein "
                        "response."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
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
            "Reviewed the temperature_range_mid4_warm_mesophile graph for issue "
            "#183: added snippets to 9 edge-level evidence items, grounded the "
            "RpoH and compensatory-adaptation predicates, and narrowed 2 local "
            "node identifiers to avoid cross-record type collisions. No paid "
            "research service was called."
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
