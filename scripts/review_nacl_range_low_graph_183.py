#!/usr/bin/env python3
"""Review NaCl-range-low graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_nacl_range_low_graph_183.py
    python scripts/review_nacl_range_low_graph_183.py --apply
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

SLUG = "environment/nacl_range_low"
GRAPH_ID = "nacl_range_low_non_halophile"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T08:00:00Z"

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "hyperosmotic_stress",
            "label": "hyperosmotic stress",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": "Cellular stress from elevated external osmolarity (osmotic upshift).",
        },
        "after": {
            "node_id": "hyperosmotic_stress",
            "label": "hyperosmotic stress",
            "node_type": "ENVIRONMENTAL_FACTOR",
            "description": "External hypertonicity causing cell shrinkage and plasmolysis.",
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "nacl_concentration",
            "predicate": "causes",
            "object": "hyperosmotic_stress",
            "description": "Increased external NaCl concentration causes hyperosmotic stress.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsml/uqad020",
                    "notes": (
                        "Hyperosmotic upshift elicits rapid K+ import as an "
                        "emergency response; general bacterial osmotic-stress edge."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
        "after": {
            "subject": "nacl_concentration",
            "predicate": "causes",
            "object": "hyperosmotic_stress",
            "description": "Increased external NaCl concentration causes hyperosmotic stress.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsml/uqad020",
                    "snippet": (
                        "hyperosmotic stress by addition of either non-ionic "
                        "osmolyte sucrose or ionic solute NaCl"
                    ),
                    "notes": (
                        "Verified against the open Bhowmick et al. review; the "
                        "edge is retained as a broad NaCl-to-hyperosmotic-stress "
                        "step, not as a direct determinant of the <=1% range bin."
                    ),
                }
            ],
            "predicate_id": "biolink:causes",
        },
    },
    {
        "before": {
            "subject": "hyperosmotic_stress",
            "predicate": "induces",
            "object": "compatible_solute_accumulation",
            "description": "Hyperosmotic stress induces accumulation of compatible solutes.",
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsml/uqad020",
                    "notes": (
                        "After K+ import, cells synthesize or import compatible "
                        "solutes and export K+ to reduce cytoplasmic ionic strength."
                    ),
                }
            ],
        },
        "after": {
            "subject": "hyperosmotic_stress",
            "predicate": "increases",
            "object": "compatible_solute_accumulation",
            "description": (
                "Hyperosmotic stress increases compatible-solute accumulation "
                "as a later osmoadaptive response."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsml/uqad020",
                    "snippet": (
                        "external osmotic upshifts by increasing the cellular "
                        "concentration of cations"
                    ),
                    "notes": (
                        "Verified against the open Bhowmick et al. review; this "
                        "keeps compatible-solute accumulation as a broad "
                        "osmotic-upshift response."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
    },
    {
        "before": {
            "subject": "hypoosmotic_shock",
            "predicate": "opens",
            "object": "mechanosensitive_channels",
            "description": (
                "Hypoosmotic shock opens mechanosensitive channels MscL/MscS to prevent rupture."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsml/uqad020",
                    "notes": (
                        "Hypoosmotic shock triggers transient opening of "
                        "mechanosensitive channels (MscL/MscS) to prevent "
                        "turgor-driven cell rupture; broad across bacteria."
                    ),
                }
            ],
        },
        "after": {
            "subject": "mechanosensitive_channels",
            "predicate": "mitigates",
            "object": "hypoosmotic_shock",
            "description": (
                "Mechanosensitive channels mitigate turgor stress during sudden "
                "hypoosmotic shocks at the low-salinity end of the range."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/femsml/uqad020",
                    "snippet": "emergency reaction essential for preventing turgor increase",
                    "notes": (
                        "Verified against the open Bhowmick et al. review; the "
                        "edge is reversed from ungrounded shock-opens-channel "
                        "wording to a grounded mitigation predicate."
                    ),
                }
            ],
            "predicate_id": "METPO:2007407",
        },
    },
    {
        "before": {
            "subject": "c_di_amp",
            "predicate": "inhibits",
            "object": "opu_solute_importers",
            "description": "c-di-AMP binds and inhibits OpuA/OpuC compatible-solute importers.",
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00181-23",
                    "notes": (
                        "c-di-AMP binds CBS-containing importers (OpuA/OpuC) and "
                        "negatively regulates their transport activity."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
            "subject": "c_di_amp",
            "predicate": "inhibits",
            "object": "opu_solute_importers",
            "description": "c-di-AMP binds and inhibits OpuA/OpuC compatible-solute importers.",
            "evidence": [
                {
                    "reference": "DOI:10.1128/mmbr.00181-23",
                    "snippet": (
                        "Cyclic di-AMP binds to the CBS domains of compatible solute importers"
                    ),
                    "notes": (
                        "Verified against public Foster et al. text; OpuA/OpuC "
                        "are retained as representative CBS-domain osmolyte "
                        "importers."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
    },
    {
        "before": {
            "subject": "choline_uptake",
            "predicate": "enables",
            "object": "glycine_betaine_synthesis",
            "description": (
                "Choline uptake enables synthesis of glycine betaine, a key compatible solute."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1126/sciadv.ado6229",
                    "notes": (
                        "BetT mediates uptake of external choline used to "
                        "synthesize glycine betaine, a key compatible solute in "
                        "hyperosmotic environments."
                    ),
                }
            ],
            "predicate_id": "RO:0002327",
        },
        "after": {
            "subject": "choline_uptake",
            "predicate": "enables",
            "object": "glycine_betaine_synthesis",
            "description": (
                "Choline uptake enables synthesis of glycine betaine, a key compatible solute."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1126/sciadv.ado6229",
                    "snippet": (
                        "uptake of external choline for synthesizing the "
                        "osmoprotective glycine betaine"
                    ),
                    "notes": (
                        "Verified against public Yang et al. abstract text; "
                        "choline uptake is retained as the substrate-supply step "
                        "for glycine-betaine biosynthesis."
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
            "Reviewed the nacl_range_low_non_halophile graph for issue #183: "
            "added exact snippets to 5 causal-edge evidence items, grounded "
            "2 residual predicates, and repaired 1 local node-type conflict. "
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
