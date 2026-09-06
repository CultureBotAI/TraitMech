#!/usr/bin/env python3
"""Review NaCl-delta-mid2 graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_nacl_delta_mid2_graph_183.py
    python scripts/review_nacl_delta_mid2_graph_183.py --apply
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

SLUG = "environment/nacl_delta_mid2"
GRAPH_ID = "nacl_delta_mid2_broad_breadth"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T07:40:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "kdpfabc_complex",
            "label": "KdpFABC complex",
            "node_type": "GENE_OR_PROTEIN",
            "grounding_status": "REVIEWED_LABEL_ONLY",
            "grounding_notes": (
                "Reviewed as a contextual protein or protein-complex label within "
                "a quantitative measurement graph; no exact semantic family term "
                "was established for this aggregate use."
            ),
            "description": "High-affinity potassium uptake P-type ATPase complex.",
        },
        "after": {
            "node_id": "kdpfabc_expression",
            "label": "kdpFABC expression",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Expression of the kdpFABC high-affinity K+ uptake operon via "
                "KdpD under osmotic upshift."
            ),
        },
    },
    {
        "before": {
            "node_id": "compatible_solute_transport",
            "label": "compatible-solute accumulation/transport",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": "Biosynthesis and uptake of compatible solutes/osmolytes.",
        },
        "after": {
            "node_id": "compatible_solute_accumulation_transport",
            "label": "compatible-solute accumulation and transport",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": "Biosynthesis and uptake of compatible solutes/osmolytes.",
        },
    },
    {
        "before": {
            "node_id": "eps_matrix",
            "label": "exopolysaccharide matrix",
            "node_type": "CELLULAR_LOCALIZATION",
            "description": "Extracellular polymeric substance matrix surrounding cells.",
        },
        "after": {
            "node_id": "eps_matrix",
            "label": "exopolysaccharide matrix",
            "node_type": "CHEMICAL",
            "description": "Extracellular polymeric substance matrix surrounding cells.",
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "cyclic_di_amp",
            "predicate": "inhibits",
            "object": "potassium_uptake_systems",
            "description": "c-di-AMP binding to transporters/riboswitches inhibits K+ import.",
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00181-23",
                    "notes": (
                        "Binding of c-di-AMP to transporters and riboswitches "
                        "inhibits potassium import (KupA/KupB, KimA, kdp operon)."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
            "subject": "cyclic_di_amp",
            "predicate": "inhibits",
            "object": "potassium_uptake_systems",
            "description": "c-di-AMP binding to transporters/riboswitches inhibits K+ import.",
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.pgen.1007574",
                    "snippet": (
                        "A high level of c-di-AMP has been found to repress K+ and carnitine uptake"
                    ),
                    "notes": (
                        "Verified against the open Pham et al. introduction; "
                        "c-di-AMP is retained as a broad regulator of bacterial "
                        "K+ import rather than a direct determinant of this "
                        "NaCl-breadth bin."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
    {
        "before": {
            "subject": "cyclic_di_amp",
            "predicate": "modulates",
            "object": "cell_volume_regulation",
            "description": "c-di-AMP signaling acts as a master regulator of cell volume.",
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00181-23",
                    "notes": "Review argues cyclic di-AMP is a master regulator of cell volume.",
                }
            ],
            "predicate_id": "RO:0002211",
        },
        "after": {
            "subject": "cyclic_di_amp",
            "predicate": "modulates",
            "object": "cell_volume_regulation",
            "description": "c-di-AMP signaling acts as a master regulator of cell volume.",
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00181-23",
                    "snippet": "cyclic di-AMP is a master regulator of cell volume",
                    "notes": (
                        "Verified against public Foster et al. text; the edge is "
                        "kept at the level of broad second-messenger control over "
                        "cell-volume regulation."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "osmolality",
            "predicate": "upregulates",
            "object": "kdpfabc_complex",
            "description": "Elevated osmolality upregulates kdpFABC expression.",
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00181-23",
                    "notes": "Osmolality upregulates kdpFABC expression (review-level, broadly useful).",
                }
            ],
        },
        "after": {
            "subject": "osmolality",
            "predicate": "increases",
            "object": "kdpfabc_expression",
            "description": (
                "Ionic-strength changes can increase kdpFABC expression via "
                "KdpD during osmotic upshift."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1046/j.1365-2958.2002.02894.x",
                    "snippet": (
                        "increase the expression of kdpFABC under conditions of osmotic upshift"
                    ),
                    "notes": (
                        "Verified against the open Poolman et al. review; the "
                        "edge is moved from a protein-complex object to a "
                        "kdpFABC-expression process."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "compatible_solute_transport",
            "predicate": "causes",
            "object": "osmoprotection",
            "description": "Accumulation/transport of compatible solutes confers osmoprotection.",
            "evidence": [
                {
                    "reference": "DOI:10.1111/mec.16316",
                    "notes": (
                        "Compatible-solute biosynthesis/uptake and transporter "
                        "genes -> osmotic protection."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "compatible_solute_accumulation_transport",
            "predicate": "causes",
            "object": "osmoprotection",
            "description": "Accumulation/transport of compatible solutes confers osmoprotection.",
            "evidence": [
                {
                    "reference": "DOI:10.3389/fmicb.2018.00108",
                    "snippet": (
                        "accumulated by microorganisms under high salinity growth "
                        "conditions as stress protectants"
                    ),
                    "notes": (
                        "Verified against the open Leon et al. text; compatible "
                        "solute accumulation and uptake are retained as a broad "
                        "osmoprotective process."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "eps_matrix",
            "predicate": "binds",
            "object": "sodium_ion",
            "description": "The EPS matrix binds Na+ cations.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuaf020",
                    "notes": "The EPS matrix binds cations such as Na+ ions.",
                }
            ],
        },
        "after": {
            "subject": "eps_matrix",
            "predicate": "interacts with",
            "object": "sodium_ion",
            "description": "The EPS matrix physically interacts with Na+ cations.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuaf020",
                    "snippet": "the EPS matrix binds cations such as Na+ ions",
                    "notes": (
                        "Verified against the open Goszcz et al. review; "
                        "exopolysaccharide matrices are typed with the existing "
                        "CHEMICAL convention from the biofilm graph."
                    ),
                }
            ],
            "predicate_id": "biolink:interacts_with",
        },
    },
    {
        "before": {
            "subject": "eps_matrix",
            "predicate": "promotes",
            "object": "water_retention",
            "description": (
                "EPS matrix promotes water retention and reduces pericellular Na+ toxicity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuaf020",
                    "notes": "Lowering effective pericellular Na+ and retaining water.",
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "eps_matrix",
            "predicate": "promotes",
            "object": "water_retention",
            "description": (
                "EPS matrix promotes water retention and reduces pericellular Na+ toxicity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsre/fuaf020",
                    "snippet": (
                        "It also retains water, which helps in reducing the osmotic gradient"
                    ),
                    "notes": (
                        "Verified against the open Goszcz et al. review; this "
                        "EPS edge is kept as a contextual pericellular salt-stress "
                        "mitigation mechanism."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
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
            "Reviewed the nacl_delta_mid2_broad_breadth graph for issue #183: "
            "added exact snippets to 6 causal-edge evidence items, grounded "
            "2 residual predicates, and repaired 2 local node-type conflicts. "
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
