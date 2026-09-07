#!/usr/bin/env python3
"""Review ring_shaped graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_ring_shaped_graph_183.py
    python scripts/review_ring_shaped_graph_183.py --apply
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

SLUG = "morphology/ring_shaped"
GRAPH_ID = "ring_shaped_curved_growth_closure"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T06:20:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "bactofilin_lmdc_module",
            "label": "bactofilin-M23 peptidase module",
            "node_type": "GENE_OR_PROTEIN",
            "description": (
                "Conserved bactofilin and M23 peptidase functional module "
                "remodeling the wall locally."
            ),
            "grounding_status": "REVIEWED_LABEL_ONLY",
            "grounding_notes": (
                "This is a multi-protein bactofilin/M23 module, not one protein "
                "family or accession."
            ),
        },
        "after": {
            "node_id": "bactofilin_lmdc_module",
            "label": "bactofilin-M23 peptidase module",
            "node_type": "PATHWAY",
            "description": (
                "Conserved bactofilin and M23 peptidase functional module "
                "remodeling the wall locally."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "mreb_filaments",
            "predicate": "correlates with",
            "object": "cell_wall_growth_rate",
            "description": ("MreB filament motion correlates with the rate of cell-wall growth."),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12071309",
                    "notes": (
                        "the motion of MreB filaments correlates with the rate of "
                        "cell wall growth; general shape-control edge."
                    ),
                }
            ],
        },
        "after": {
            "subject": "mreb_filaments",
            "predicate": "associated with",
            "object": "cell_wall_growth_rate",
            "description": (
                "MreB filament motion is associated with the rate of cell-wall growth."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.3390/microorganisms12071309",
                    "snippet": (
                        "motion of MreB filaments correlates with the rate of cell wall growth"
                    ),
                    "notes": (
                        "Verified against the open Dersch et al. text; the edge "
                        "remains associative and contextual rather than direct "
                        "ring-shape evidence."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
    },
    {
        "before": {
            "subject": "mreb_filaments",
            "predicate": "guides",
            "object": "pg_insertion_perpendicular",
            "description": (
                "MreB double filaments guide peptidoglycan insertion perpendicular "
                "to the long axis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-49785-x",
                    "notes": (
                        "These cytoskeletal structures guide peptidoglycan "
                        "insertion perpendicular to the long axis of the cell."
                    ),
                }
            ],
        },
        "after": {
            "subject": "mreb_filaments",
            "predicate": "regulates",
            "object": "pg_insertion_perpendicular",
            "description": (
                "MreB double filaments guide the orientation of peptidoglycan "
                "insertion perpendicular to the long axis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-49785-x",
                    "snippet": (
                        "guide peptidoglycan insertion perpendicular to the long axis of the cell"
                    ),
                    "notes": (
                        "Verified against the open Middlemiss et al. text; the "
                        "edge supports contextual MreB-guided peptidoglycan "
                        "insertion."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "bactofilin_polymers",
            "predicate": "spatially regulates",
            "object": "cell_wall_biosynthesis",
            "description": ("Bactofilin polymers spatially regulate cell-wall biosynthesis."),
            "evidence": [
                {
                    "reference": "DOI:10.7554/eLife.86577.2",
                    "notes": (
                        "bactofilin polymers... indicating a central role in the "
                        "spatial regulation of cell wall biosynthesis."
                    ),
                }
            ],
        },
        "after": {
            "subject": "bactofilin_polymers",
            "predicate": "regulates",
            "object": "cell_wall_biosynthesis",
            "description": "Bactofilin polymers regulate cell-wall biosynthesis.",
            "evidence": [
                {
                    "reference": "DOI:10.7554/eLife.86577.2",
                    "snippet": ("central role in the spatial regulation of cell wall biosynthesis"),
                    "notes": (
                        "Verified against the open Pohl et al. abstract; "
                        "bactofilin spatial wall-biosynthesis regulation is "
                        "retained as comparative Hyphomonas morphogenesis "
                        "evidence."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "bactofilin_lmdc_module",
            "predicate": "promotes",
            "object": "wall_biosynthesis_mode_change",
            "description": (
                "Conserved bactofilin and M23 peptidase module promotes local "
                "changes in cell-wall biosynthesis mode."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.7554/eLife.86577.2",
                    "notes": (
                        "bactofilins and M23 peptidases form a conserved "
                        "functional module that promotes local changes in the mode "
                        "of cell wall biosynthesis; cross-taxon."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "bactofilin_lmdc_module",
            "predicate": "promotes",
            "object": "wall_biosynthesis_mode_change",
            "description": (
                "Conserved bactofilin and M23 peptidase module promotes local "
                "changes in cell-wall biosynthesis mode."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.7554/eLife.86577.2",
                    "snippet": ("promotes local changes in the mode of cell wall biosynthesis"),
                    "notes": (
                        "Verified against the open Pohl et al. abstract; the "
                        "conserved bactofilin/M23 module is retained as "
                        "comparative cell-wall morphogenesis evidence."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "crva_polymer",
            "predicate": "skews",
            "object": "pg_synthesis_rate_skew",
            "description": (
                "CrvA polymer formation skews peptidoglycan synthesis rates to generate curvature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-45196-0",
                    "notes": (
                        "CrvA in Vibrio cholerae... skews peptidoglycan synthesis "
                        "rates; curvature-generating wall patterning."
                    ),
                }
            ],
        },
        "after": {
            "subject": "crva_polymer",
            "predicate": "regulates",
            "object": "pg_synthesis_rate_skew",
            "description": (
                "CrvA polymer formation regulates skewed peptidoglycan synthesis "
                "rates to generate curvature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-45196-0",
                    "snippet": (
                        "CrvA in Vibrio cholerae, which skews peptidoglycan synthesis rates"
                    ),
                    "notes": (
                        "Verified against the open Schiller et al. article text; "
                        "CrvA is retained as a comparative bacterial curvature "
                        "module."
                    ),
                }
            ],
            "predicate_id": "RO:0002211",
        },
    },
    {
        "before": {
            "subject": "crescentin",
            "predicate": "promotes",
            "object": "cell_curvature",
            "description": "Crescentin promotes cell curvature.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-45196-0",
                    "notes": (
                        "the intermediate filament-like protein crescentin in C. "
                        "crescentus generates curvature; canonical curvature "
                        "determinant."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "crescentin",
            "predicate": "promotes",
            "object": "cell_curvature",
            "description": "Crescentin promotes cell curvature.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-45196-0",
                    "snippet": "components that promote curvature",
                    "notes": (
                        "Verified against the open Schiller et al. article text; "
                        "Schiller et al. list crescentin in the same bacterial "
                        "curvature-component statement."
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
    existing_by_key = {_edge_key(edge) for edge in graph.get("edges") or []}
    return all(key in existing_by_key for key in edges)


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_nodes = _nodes_by_state("before")
    after_nodes = _nodes_by_state("after")
    before_edges = _edges_by_state("before")
    after_edges = _edges_by_state("after")

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys
    has_after_nodes = _has_exact_nodes(graph, after_nodes)
    has_after_edges = _has_exact_edges(graph, after_edges)

    if has_after_nodes and has_after_edges:
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_edge_keys == migrated_edge_keys and migrated_edge_keys:
        _assert_exact_nodes(graph, after_nodes, "migrated")
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_edge_keys or has_after_nodes:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"node={has_after_nodes} edges={sorted(present_migrated_edge_keys)}"
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
            "Reviewed the ring_shaped_curved_growth_closure graph for issue "
            "#183: added exact snippets to 6 comparative curvature and "
            "wall-patterning evidence entries, grounded 4 residual predicates, "
            "and retyped the bactofilin-M23 module as a pathway. No paid "
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
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write changes to data/traits/morphology/ring_shaped.yaml",
    )
    args = parser.parse_args()
    return apply(write=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
