#!/usr/bin/env python3
"""Review temperature_delta_very_low graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_temperature_delta_very_low_graph_183.py
    python scripts/review_temperature_delta_very_low_graph_183.py --apply
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

SLUG = "environment/temperature_delta_very_low"
GRAPH_ID = "temperature_delta_very_low_stenothermal"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T09:00:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "unsaturated_fatty_acid_content",
            "label": "unsaturated fatty acid content",
            "node_type": "CHEMICAL",
            "description": "Proportion of unsaturated fatty acids in membrane phospholipids.",
        },
        "after": {
            "node_id": "unsaturated_fatty_acid_content",
            "label": "unsaturated fatty acid content",
            "node_type": "QUALITY",
            "description": "Relative proportion of unsaturated fatty acids in membrane phospholipids.",
        },
    },
    {
        "before": {
            "node_id": "translation_under_cold",
            "label": "translation under cold shock",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": "Maintenance of protein synthesis at low temperature.",
        },
        "after": {
            "node_id": "large_ribosomal_subunit_biogenesis",
            "label": "50S ribosomal subunit biogenesis",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Biogenesis of the bacterial large ribosomal subunit at low temperature."
            ),
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "unsaturated_fatty_acid_content",
            "predicate": "increases",
            "object": "membrane_fluidity",
            "description": (
                "Higher unsaturated fatty acid proportion prevents excessive "
                "rigidification and maintains membrane fluidity at low temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "notes": (
                        "Proportionally more unsaturated fatty acids maintain "
                        "membrane fluidity within an optimal range; broad across microbes."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
            "subject": "unsaturated_fatty_acid_content",
            "predicate": "positively regulates",
            "object": "membrane_fluidity",
            "description": (
                "A higher unsaturated-fatty-acid proportion fluidizes bacterial "
                "cytoplasmic membranes and counteracts cold rigidification."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev-micro-091313-103612",
                    "snippet": "incorporation of proportionally more unsaturated fatty acids",
                    "notes": (
                        "Verified against the public Annual Review of Microbiology "
                        "abstract; de Mendoza reviews increased unsaturated fatty "
                        "acid incorporation as part of homeoviscous adaptation to "
                        "decreasing growth temperature."
                    ),
                },
                {
                    "reference": "DOI:10.1111/mmi.15323",
                    "snippet": (
                        "increases with temperature or an increase in the proportion "
                        "of unsaturated fatty acids and vice versa"
                    ),
                    "notes": (
                        "Verified against the open Molecular Microbiology full text; "
                        "Singh and Harinarayanan use E. coli unsaturated-fatty-acid "
                        "perturbations as a route to membrane-fluidity loss."
                    ),
                },
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "cold_shock",
            "predicate": "induces",
            "object": "cspa_protein",
            "description": (
                "Cold shock induces CspA, an RNA chaperone counteracting "
                "low-temperature RNA secondary structure."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1007/s12275-023-00031-x",
                    "notes": (
                        "Cold-shock proteins (notably CspA) bind RNA to promote "
                        "single-stranded states."
                    ),
                }
            ],
        },
        "after": {
            "subject": "cold_shock",
            "predicate": "positively regulates",
            "object": "cspa_protein",
            "description": (
                "Cold shock strongly increases CspA cold-shock protein synthesis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1046/j.1365-2958.1999.01284.x",
                    "snippet": "more than 10% of the total cellular protein synthesis",
                    "notes": (
                        "Verified against the open Molecular Microbiology full text; "
                        "CspA is the major E. coli cold-shock protein and its "
                        "synthesis rises sharply after temperature downshift."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "csda_helicase",
            "predicate": "maintains",
            "object": "translation_under_cold",
            "description": "CsdA binds ribosomes to maintain translation under cold shock.",
            "evidence": [
                {
                    "reference": "DOI:10.1007/s12275-023-00031-x",
                    "notes": "CsdA binds ribosomes to maintain translation under cold shock.",
                }
            ],
        },
        "after": {
            "subject": "csda_helicase",
            "predicate": "contributes to",
            "object": "large_ribosomal_subunit_biogenesis",
            "description": (
                "CsdA DEAD-box RNA helicase contributes to 50S ribosomal-subunit "
                "biogenesis at low temperature."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/nar/gkh603",
                    "snippet": (
                        "CsdA is involved in the biogenesis of the large rather "
                        "than the small ribosomal subunit"
                    ),
                    "notes": (
                        "Verified against the open Nucleic Acids Research abstract; "
                        "Charollais et al. place the E. coli CsdA helicase in 50S "
                        "ribosomal-subunit biogenesis at low temperatures."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
]

EDGE_REMOVALS: list[dict[str, Any]] = [
    {
        "subject": "membrane_fluidity",
        "predicate": "decreased by reduced unsaturated fatty acids",
        "object": "unsaturated_fatty_acid_content",
        "description": (
            "Reduced unsaturated fatty acid content decreases membrane fluidity, "
            "a direct physical consequence linking composition to cold stress."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1111/mmi.15323",
                "notes": (
                    "Decrease in membrane fluidity due to decrease in "
                    "unsaturated fatty acid content."
                ),
            }
        ],
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


def _assert_removed_edges_absent(graph: dict[str, Any]) -> None:
    removed = {_edge_key(edge) for edge in EDGE_REMOVALS}
    existing = {_edge_key(edge) for edge in graph.get("edges") or []}
    overlap = sorted(existing & removed)
    if overlap:
        raise ValueError(f"{SLUG}: removed edge(s) still present: {overlap}")


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
    removed_edges = {_edge_key(edge): edge for edge in EDGE_REMOVALS}

    migrated_edge_keys = set(after_edges) - set(before_edges)
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_edge_keys = existing_edge_keys & migrated_edge_keys

    has_after_nodes = _has_exact_nodes(graph, after_nodes)
    has_after_edges = _has_exact_edges(graph, after_edges)
    if has_after_nodes and has_after_edges:
        _assert_removed_edges_absent(graph)
        return False

    if present_migrated_edge_keys == migrated_edge_keys:
        _assert_exact_nodes(graph, after_nodes, "migrated")
        _assert_exact_edges(graph, after_edges, "migrated")
        _assert_removed_edges_absent(graph)
        return False

    if present_migrated_edge_keys:
        raise ValueError(f"{SLUG}: partial evidence replay: {sorted(present_migrated_edge_keys)}")

    _assert_exact_nodes(graph, before_nodes, "source")
    _assert_exact_edges(graph, before_edges | removed_edges, "source")

    after_by_before_node_id = {
        replacement["before"]["node_id"]: replacement["after"] for replacement in NODE_REPLACEMENTS
    }
    after_by_before_edge_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    removed_edge_keys = {_edge_key(edge) for edge in EDGE_REMOVALS}

    graph["nodes"] = [
        copy.deepcopy(after_by_before_node_id.get(node.get("node_id"), node))
        for node in graph.get("nodes") or []
    ]
    graph["edges"] = [
        copy.deepcopy(after_by_before_edge_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
        if _edge_key(edge) not in removed_edge_keys
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the temperature_delta_very_low_stenothermal graph for issue "
            "#183: added exact snippets to 4 membrane and cold-shock evidence "
            "items, grounded 3 residual predicates, collapsed 1 backwards "
            "membrane-fluidity edge into the supported unsaturated-fatty-acid "
            "edge, and retyped unsaturated fatty acid content as a QUALITY node. "
            "The record remains an explicitly reviewed nonmechanistic 1-5 degree "
            "C temperature-breadth bin. No paid research service was called."
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
