#!/usr/bin/env python3
"""Review broad soil-dwelling graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_soil_dwelling_graph_183.py
    python scripts/review_soil_dwelling_graph_183.py --apply
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

SLUG = "ecology/soil_dwelling"
GRAPH_ID = "soil_dwelling_biogeochemistry"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T00:20:00Z"

RECORD_EVIDENCE_BEFORE: list[dict[str, Any]] = [
    {
        "reference": "DOI:10.1038/nrmicro.2017.87",
        "notes": (
            'Fierer, "Embracing the unknown", characterizes the soil microbiome '
            "as a distinct, complex microbial habitat."
        ),
    },
    {
        "reference": "DOI:10.1038/nrmicro1341",
        "notes": (
            "Martiny et al. support soil communities as biogeographically "
            "structured microbial habitats."
        ),
    },
]

RECORD_EVIDENCE_AFTER: list[dict[str, Any]] = [
    {
        "reference": "DOI:10.1038/nrmicro.2017.87",
        "snippet": "a gram of soil can contain thousands of individual microbial taxa",
        "notes": (
            "Verified against the Fierer review; it frames soil as a diverse, "
            "complex microbial habitat rather than a single uniform niche."
        ),
    },
    {
        "reference": "DOI:10.1038/nrmicro1341",
        "snippet": "free-living microbial taxa exhibit biogeographic patterns",
        "notes": (
            "Verified against the Martiny et al. abstract; environmental selection "
            "and spatial structure support treating soil association as habitat "
            "ecology, not simple taxonomic membership."
        ),
    },
]

NODE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "node_id": "climate_extreme_event",
            "label": "extreme climatic event",
            "node_type": "ENVIRONMENTAL_FACTOR",
            "description": "Heat, flood, or freeze disturbance events in soil.",
        },
        "after": {
            "node_id": "climate_extreme_event",
            "label": "extreme heat event",
            "node_type": "ENVIRONMENTAL_FACTOR",
            "description": "Experimental heat disturbance in soil.",
        },
    },
]

EDGE_REPLACEMENTS: list[dict[str, dict[str, Any]]] = [
    {
        "before": {
            "subject": "soil_habitat",
            "predicate": "confers",
            "object": "soil_dwelling_trait",
            "description": "Soil substrate and pore-water chemistry sustain soil-resident microbes.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro.2017.87",
                    "notes": (
                        "Fierer characterizes the soil microbiome as a distinct microbial habitat."
                    ),
                }
            ],
            "predicate_id": "METPO:2007700",
        },
        "after": {
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
    },
    {
        "before": {
            "subject": "soil_dwelling_trait",
            "predicate": "contributes to",
            "object": "biogeochemical_cycling",
            "description": "Soil microbes drive terrestrial biogeochemical cycling.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro1341",
                    "notes": (
                        "Martiny et al. show soil communities are biogeographically "
                        "structured habitats central to ecosystem function."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
        "after": {
            "subject": "soil_dwelling_trait",
            "predicate": "contributes to",
            "object": "biogeochemical_cycling",
            "description": "Soil microbes contribute to terrestrial biogeochemical cycling.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/nrmicro.2017.87",
                    "snippet": "specific microbial controls on soil processes",
                    "notes": (
                        "Verified against the Fierer review; soil microbial "
                        "processes include nutrient transformations and organic "
                        "carbon-pool dynamics."
                    ),
                }
            ],
            "predicate_id": "RO:0002326",
        },
    },
    {
        "before": {
            "subject": "low_organic_carbon",
            "predicate": "enriches for",
            "object": "oligotrophic_lifestyle",
            "description": (
                "Carbon-limited soils enrich oligotrophic taxa with small genomes "
                "and reduced motility/chemotaxis."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/ismeco/ycae081",
                    "notes": (
                        "Dragone et al.: oligotroph-enriched taxa in "
                        "carbon-limited soils had smaller genomes, slower growth, "
                        "carbon-storage pathways, and under-represented "
                        "chemotaxis/motility genes."
                    ),
                }
            ],
        },
        "after": {
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
    },
    {
        "before": {
            "subject": "soil_resource_availability",
            "predicate": "increases",
            "object": "potential_growth_rate",
            "description": (
                "Resource-rich, humid, acid-neutral soils support higher "
                "microbiome potential growth."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53753-w",
                    "notes": (
                        "Zhou et al.: high potential growth in resource-rich, "
                        "acid-neutral soils of cold, humid regions (18O-H2O DNA "
                        "incorporation)."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
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
    },
    {
        "before": {
            "subject": "aridity",
            "predicate": "decreases",
            "object": "potential_growth_rate",
            "description": "Aridity lowers soil microbiome potential growth rate.",
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41467-024-53753-w",
                    "notes": (
                        "Zhou et al.: aridity was a stronger predictor of community "
                        "growth than temperature; dry soils had lower potential "
                        "growth."
                    ),
                }
            ],
            "predicate_id": "RO:0002212",
        },
        "after": {
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
    },
    {
        "before": {
            "subject": "soil_carbon_availability",
            "predicate": "increases prevalence of",
            "object": "flagellar_motility",
            "description": (
                "High soil carbon availability raises prevalence of flagellar motility."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1093/ismejo/wrae067",
                    "notes": (
                        "Ramoneda et al.: rhizosphere ~11.5% higher flagellar "
                        "prevalence (P=0.012); glucose amendment increased "
                        "prevalence (P=0.017)."
                    ),
                }
            ],
        },
        "after": {
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
                        "prevalence of flagellar motility is positively "
                        "associated with soil C availability"
                    ),
                    "notes": (
                        "Verified against the open ISME Journal full text; glucose "
                        "amendment and four field gradients support the association."
                    ),
                }
            ],
            "predicate_id": "biolink:associated_with",
        },
    },
    {
        "before": {
            "subject": "climate_extreme_event",
            "predicate": "increases",
            "object": "dormancy_sporulation",
            "description": (
                "Heat, flood and freeze extremes increase dormancy and sporulation gene abundance."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41586-024-08185-3",
                    "notes": (
                        "Knight et al.: dormancy and sporulation genes increased "
                        "across flood, freeze and heat; 46% of annotated genes "
                        "shifted at disturbance end."
                    ),
                }
            ],
            "predicate_id": "RO:0002213",
        },
        "after": {
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
    },
    {
        "before": {
            "subject": "soil_pH_precip_cn",
            "predicate": "predicts",
            "object": "life_history_axes",
            "description": (
                "Soil pH, precipitation and C:N predict soil bacterial life-history genomic axes."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1038/s41564-023-01465-0",
                    "notes": (
                        "Piton et al.: random-forest models using pH, precipitation "
                        "and C:N predicted MCOA1/MCOA2 (R2=0.80, 0.58); pH and "
                        "precipitation top predictors."
                    ),
                }
            ],
        },
        "after": {
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


def _assert_record_evidence(
    doc: dict[str, Any], expected: list[dict[str, Any]], state: str
) -> None:
    if doc.get("evidence") != expected:
        raise ValueError(f"{SLUG}: {state} record evidence drifted")


def _assert_exact_nodes(
    graph: dict[str, Any],
    expected_by_id: dict[str | None, dict[str, Any]],
    state: str,
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


def _replacements_by_state(
    state: str,
) -> dict[tuple[str | None, str | None, str | None], dict[str, Any]]:
    return {_edge_key(replacement[state]): replacement[state] for replacement in EDGE_REPLACEMENTS}


def _nodes_by_state(state: str) -> dict[str | None, dict[str, Any]]:
    return {
        replacement[state].get("node_id"): replacement[state] for replacement in NODE_REPLACEMENTS
    }


def _has_exact_state(
    doc: dict[str, Any],
    graph: dict[str, Any],
    evidence: list[dict[str, Any]],
    nodes: dict[str | None, dict[str, Any]],
    edges: dict[tuple[str | None, str | None, str | None], dict[str, Any]],
) -> bool:
    existing_edges = {_edge_key(edge): edge for edge in graph.get("edges") or []}
    existing_nodes = {node.get("node_id"): node for node in graph.get("nodes") or []}
    return (
        doc.get("evidence") == evidence
        and all(existing_nodes.get(node_id) == node for node_id, node in nodes.items())
        and all(existing_edges.get(key) == edge for key, edge in edges.items())
    )


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    graph = _find_graph(doc)
    before_edges = _replacements_by_state("before")
    after_edges = _replacements_by_state("after")
    before_nodes = _nodes_by_state("before")
    after_nodes = _nodes_by_state("after")
    migrated_keys = set(after_edges) - set(before_edges)
    existing_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    present_migrated_keys = existing_keys & migrated_keys

    if _has_exact_state(doc, graph, RECORD_EVIDENCE_AFTER, after_nodes, after_edges):
        return False

    if present_migrated_keys == migrated_keys:
        _assert_record_evidence(doc, RECORD_EVIDENCE_AFTER, "migrated")
        _assert_exact_nodes(graph, after_nodes, "migrated")
        _assert_exact_edges(graph, after_edges, "migrated")
        return False

    if present_migrated_keys:
        raise ValueError(f"{SLUG}: partial evidence replay: {sorted(present_migrated_keys)}")

    _assert_record_evidence(doc, RECORD_EVIDENCE_BEFORE, "source")
    _assert_exact_nodes(graph, before_nodes, "source")
    _assert_exact_edges(graph, before_edges, "source")

    after_by_before_key = {
        _edge_key(replacement["before"]): replacement["after"] for replacement in EDGE_REPLACEMENTS
    }
    after_node_by_before_id = {
        replacement["before"]["node_id"]: replacement["after"] for replacement in NODE_REPLACEMENTS
    }

    doc["evidence"] = copy.deepcopy(RECORD_EVIDENCE_AFTER)
    graph["nodes"] = [
        copy.deepcopy(after_node_by_before_id.get(node.get("node_id"), node))
        for node in graph.get("nodes") or []
    ]
    graph["edges"] = [
        copy.deepcopy(after_by_before_key.get(_edge_key(edge), edge))
        for edge in graph.get("edges") or []
    ]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the broad soil_dwelling_biogeochemistry graph for issue "
            "#183: added verbatim snippets to 2 record-level and 8 edge-level "
            "evidence items, regrounded 5 broad ecological association edges to "
            "biolink:associated_with, and narrowed the extreme-climate statement "
            "to heat-induced dormancy/sporulation. No paid research service was "
            "called."
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
