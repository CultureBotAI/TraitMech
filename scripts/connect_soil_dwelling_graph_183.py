#!/usr/bin/env python3
"""Connect the soil_dwelling contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_soil_dwelling_graph_183.py
    python scripts/connect_soil_dwelling_graph_183.py --apply
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
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from connect_morphology_graphs_183 import _components, _edge_key  # noqa: E402
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "ecology/soil_dwelling"
GRAPH_ID = "soil_dwelling_biogeochemistry"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T12:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "Soil-dwelling microbes drive terrestrial biogeochemical cycling",
    "description": (
        "Evidence-backed causal sketch linking soil habitat to participation "
        "in biogeochemical cycling."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Soil-dwelling microbes in soil life-history contexts",
    "description": (
        "Evidence-backed nonmechanistic sketch connecting soil habitat, "
        "biogeochemical cycling, and community-level oligotrophy, growth, "
        "motility, dormancy, and genomic life-history axes."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "soil_habitat",
        "predicate": "confers",
        "object": "soil_dwelling_trait",
        "description": "The terrestrial soil environment hosts soil-resident microbes.",
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro.2017.87",
                "snippet": "a broad diversity of microbial taxa",
                "notes": (
                    "Verified against the Fierer review; the claim is "
                    "habitat-level and does not assert a universal molecular "
                    "mechanism for all soil microbes."
                ),
            }
        ],
        "predicate_id": "METPO:2007700",
    },
    {
        "subject": "low_organic_carbon",
        "predicate": "associated with",
        "object": "oligotrophic_lifestyle",
        "description": (
            "Low-carbon soil gradients are associated with oligotrophic taxa "
            "carrying small genomes, lower potential growth rates, and fewer "
            "chemotaxis/motility genes."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/ismeco/ycae081",
                "snippet": "chemotaxis and motility were under-represented",
                "notes": (
                    "Verified against the open ISME Communications full text; "
                    "the edge is retained as an ecological association rather "
                    "than a deterministic carbon-to-genome mechanism."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "soil_resource_availability",
        "predicate": "associated with",
        "object": "potential_growth_rate",
        "description": (
            "Resource-rich, humid, acid-neutral soils are associated with "
            "higher microbiome potential growth."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53753-w",
                "snippet": "exhibit high potential growth rates",
                "notes": (
                    "Verified against the open Nature Communications abstract; "
                    "the global pattern is observational, so the edge no longer "
                    "uses a direct positive-regulation predicate."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "aridity",
        "predicate": "associated with",
        "object": "potential_growth_rate",
        "description": (
            "Dry and resource-poor soils are associated with lower soil "
            "microbiome potential growth rates."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53753-w",
                "snippet": "display lower potential growth rates",
                "notes": (
                    "Verified against the open Nature Communications abstract; "
                    "the study reports a macroscale association across soil "
                    "microbiomes."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "soil_carbon_availability",
        "predicate": "associated with",
        "object": "flagellar_motility",
        "description": (
            "High soil carbon availability is associated with greater "
            "community-level prevalence of flagellar motility genes."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/ismejo/wrae067",
                "snippet": (
                    "prevalence of flagellar motility is positively associated "
                    "with soil C availability"
                ),
                "notes": (
                    "Verified against the open ISME Journal full text; glucose "
                    "amendment and four field gradients support the association."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "climate_extreme_event",
        "predicate": "increases",
        "object": "dormancy_sporulation",
        "description": (
            "Experimental heat treatment increased soil dormancy and "
            "sporulation gene abundance."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41586-024-08185-3",
                "snippet": "enhancing dormancy and sporulation genes",
                "notes": (
                    "Verified against the open Nature abstract; the curated "
                    "edge is narrowed to heat because the abstract identifies "
                    "heat, not all imposed extremes, as the treatment enhancing "
                    "dormancy and sporulation genes."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "soil_pH_precip_cn",
        "predicate": "associated with",
        "object": "life_history_axes",
        "description": (
            "Soil pH, precipitation and C:N are associated with soil bacterial "
            "life-history genomic axes in random-forest models."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41564-023-01465-0",
                "snippet": "Random forest analyses show that soil pH",
                "notes": (
                    "Verified against the PubMed abstract for the Nature "
                    "Microbiology article; the edge is scoped as "
                    "community-level statistical association."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
]

ADDED_NODES: list[dict[str, Any]] = [
    {
        "node_id": "soil_life_history_activity_context",
        "label": "soil life-history and activity context",
        "node_type": "STATE",
        "description": (
            "Community-level soil microbial context spanning oligotrophy, "
            "growth potential, motility, dormancy/sporulation, and genomic "
            "life-history axes."
        ),
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "soil_habitat",
        "predicate": "associated with",
        "object": "soil_life_history_activity_context",
        "description": (
            "Soil habitat provides the heterogeneous ecological context in "
            "which resident microbes partition across multiple activity and "
            "life-history strategies."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro.2017.87",
                "snippet": (
                    "categorize soil microorganisms on the basis of their "
                    "ecological strategies"
                ),
                "notes": (
                    "Verified against the Fierer review; the connector groups "
                    "soil-associated community branches without asserting a "
                    "single universal soil-dwelling mechanism."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "oligotrophic_lifestyle",
        "predicate": "associated with",
        "object": "soil_life_history_activity_context",
        "description": (
            "Oligotrophic taxa in low-carbon soils are one branch of the "
            "community-level soil life-history context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/ismeco/ycae081",
                "snippet": (
                    "diverse array of ecological strategies used by soil "
                    "bacteria"
                ),
                "notes": (
                    "Verified against the open ISME Communications full text; "
                    "oligotroph-enriched taxa are treated as a carbon-gradient "
                    "association within soils."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "potential_growth_rate",
        "predicate": "associated with",
        "object": "soil_life_history_activity_context",
        "description": (
            "Potential community growth rate is an activity axis associated "
            "with moisture and resource gradients across soils."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53753-w",
                "snippet": "spatial variation of microbial potential growth rates",
                "notes": (
                    "Verified against the open Nature Communications abstract; "
                    "the Zhou et al. global survey models soil microbiome "
                    "potential growth as a community-level ecological axis."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "flagellar_motility",
        "predicate": "associated with",
        "object": "soil_life_history_activity_context",
        "description": (
            "Flagellar-motility gene prevalence is a carbon-associated "
            "mobility branch in soil communities."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/ismejo/wrae067",
                "snippet": (
                    "prevalence of flagellar motility in bacterial "
                    "communities and soil C availability"
                ),
                "notes": (
                    "Verified against the open ISME Journal full text; "
                    "Ramoneda et al. connect flagellar prevalence with soil "
                    "carbon availability across community datasets."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "dormancy_sporulation",
        "predicate": "associated with",
        "object": "soil_life_history_activity_context",
        "description": (
            "Dormancy and sporulation gene programs are stress-response "
            "branches in disturbed soil communities."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41586-024-08185-3",
                "snippet": (
                    "soil microbiomes from different climates share unified "
                    "responses to extreme climatic events"
                ),
                "notes": (
                    "Verified against the open Nature abstract; heat-enhanced "
                    "dormancy/sporulation abundance is retained as a soil "
                    "disturbance context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "life_history_axes",
        "predicate": "associated with",
        "object": "soil_life_history_activity_context",
        "description": (
            "The soil bacterial MCOA axes summarize genomic life-history "
            "strategies associated with pH, C:N, and precipitation gradients."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41564-023-01465-0",
                "snippet": (
                    "drive the dominant life history strategy of soil "
                    "bacterial communities"
                ),
                "notes": (
                    "Verified against the Nature Microbiology abstract; "
                    "Piton et al. place soil pH, C:N ratio, and precipitation "
                    "as predictors of community-level genomic strategy axes."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
]


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


def _nodes_by_id(nodes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {node["node_id"]: node for node in nodes}


def _edges_by_key(edges: list[dict[str, Any]]) -> dict[
    tuple[str | None, str | None, str | None], dict[str, Any]
]:
    return {_edge_key(edge): edge for edge in edges}


def _assert_graph_metadata(graph: dict[str, Any], expected: dict[str, str], state: str) -> None:
    actual = {field: graph.get(field) for field in expected}
    if actual != expected:
        raise ValueError(f"{SLUG}: {state} graph metadata drifted: {actual!r}")


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


def _assert_endpoints(
    graph: dict[str, Any],
    added_nodes: dict[str, dict[str, Any]],
    added_edges: list[dict[str, Any]],
) -> None:
    node_ids = {node["node_id"] for node in graph.get("nodes") or []} | set(added_nodes)
    for edge in added_edges:
        key = _edge_key(edge)
        if edge["subject"] not in node_ids or edge["object"] not in node_ids:
            raise ValueError(f"{SLUG}: connector endpoint missing for {key}")
        evidence = edge.get("evidence") or []
        if not evidence or any(
            not item.get("reference") or not item.get("snippet") for item in evidence
        ):
            raise ValueError(f"{SLUG}: connector lacks source/snippet evidence: {key}")


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    added_nodes = _nodes_by_id(ADDED_NODES)
    added_edges = _edges_by_key(ADDED_EDGES)
    source_connector_edges = _edges_by_key(SOURCE_CONNECTOR_EDGES)

    existing_node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    existing_edge_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    added_node_ids = set(added_nodes)
    added_edge_keys = set(added_edges)
    present_added_node_ids = existing_node_ids & added_node_ids
    present_added_edge_keys = existing_edge_keys & added_edge_keys

    before = _components(graph)
    if before == 1 and (
        present_added_node_ids == added_node_ids
        and present_added_edge_keys == added_edge_keys
    ):
        _assert_graph_metadata(graph, GRAPH_METADATA_AFTER, "migrated")
        _assert_exact_nodes(graph, added_nodes, "migrated")
        _assert_exact_edges(graph, added_edges, "migrated")
        return False

    _assert_graph_metadata(graph, GRAPH_METADATA_BEFORE, "source")
    if before != EXPECTED_COMPONENTS:
        raise ValueError(f"{SLUG}: expected {EXPECTED_COMPONENTS} components, found {before}")
    if present_added_node_ids or present_added_edge_keys:
        partial = sorted(present_added_node_ids) + sorted(present_added_edge_keys)
        raise ValueError(f"{SLUG}: partial connector replay: {partial}")

    _assert_exact_edges(graph, source_connector_edges, "source")
    _assert_endpoints(graph, added_nodes, ADDED_EDGES)

    graph.update(GRAPH_METADATA_AFTER)
    graph.setdefault("nodes", []).extend(copy.deepcopy(ADDED_NODES))
    graph.setdefault("edges", []).extend(copy.deepcopy(ADDED_EDGES))

    after = _components(graph)
    if after != 1:
        raise ValueError(f"{SLUG}: expected one component after repair, found {after}")
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            f"Resolved issue #183 graph fragmentation ({before} components to 1) "
            "by adding a soil life-history/activity context node and 6 "
            "source- and exact-snippet-backed association connectors. "
            "The connectors join broad soil community branches while preserving "
            "soil_dwelling_biogeochemistry as a nonmechanistic habitat graph. "
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
    print(f"{'applied' if write else 'dry run'}: repaired {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
