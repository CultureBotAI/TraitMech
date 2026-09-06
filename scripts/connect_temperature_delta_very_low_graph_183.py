#!/usr/bin/env python3
"""Connect the temperature_delta_very_low cold-stress graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_temperature_delta_very_low_graph_183.py
    python scripts/connect_temperature_delta_very_low_graph_183.py --apply
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

SLUG = "environment/temperature_delta_very_low"
GRAPH_ID = "temperature_delta_very_low_stenothermal"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T11:00:00Z"
EXPECTED_COMPONENTS = 4

GRAPH_METADATA_BEFORE = {
    "title": "Temperature-delta-very-low stenothermal breadth",
    "description": (
        "DOI-backed graph linking very limited thermal-adaptation flexibility "
        "to a 1–5 °C temperature growth breadth."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Very-low temperature-delta contextual cold-stress branches",
    "description": (
        "DOI-backed contextual graph connecting cold-induced membrane "
        "rigidification, unsaturated-fatty-acid membrane remodeling, CspA/CsdA "
        "RNA support, and very limited thermal-adaptation flexibility to the "
        "1–5 °C temperature-delta bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
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
    {
        "subject": "cold_shock",
        "predicate": "positively regulates",
        "object": "cspa_protein",
        "description": "Cold shock strongly increases CspA cold-shock protein synthesis.",
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
    {
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
                    "CsdA is involved in the biogenesis of the large rather than "
                    "the small ribosomal subunit"
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
]

ADDED_NODES: list[dict[str, Any]] = [
    {
        "node_id": "membrane_phase_transition_temperature",
        "label": "membrane phase-transition temperature",
        "node_type": "QUALITY",
        "description": (
            "Temperature at which membrane lipids shift between "
            "liquid-crystalline and ordered gel phases."
        ),
    },
    {
        "node_id": "low_temperature_membrane_transport",
        "label": "membrane transport at low temperature",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": (
            "Maintenance of membrane permeability, diffusion, and "
            "membrane-protein function under low-temperature stress."
        ),
    },
    {
        "node_id": "cold_rna_metabolism",
        "label": "RNA metabolism at low temperature",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": (
            "RNA chaperone and helicase activity that preserves translation and "
            "ribosomal-subunit biogenesis during cold stress."
        ),
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "cold_shock",
        "predicate": "negatively regulates",
        "object": "membrane_fluidity",
        "description": (
            "Cold exposure drives membrane lipids toward ordered gel states and "
            "thereby decreases functional membrane fluidity."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s00792-017-0939-x",
                "snippet": "liquid crystalline phase into the rigid gel phase",
                "notes": (
                    "Verified against the public Springer page; Siliakus et al. "
                    "review low-temperature shifts from liquid-crystalline to "
                    "rigid gel membrane phases."
                ),
            }
        ],
        "predicate_id": "RO:0002212",
    },
    {
        "subject": "unsaturated_fatty_acid_content",
        "predicate": "negatively regulates",
        "object": "membrane_phase_transition_temperature",
        "description": (
            "A higher cis-unsaturated-fatty-acid fraction lowers membrane "
            "phase-transition temperature and helps keep membranes fluid in "
            "the cold."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "incorporation of proportionally more unsaturated fatty acids",
                "notes": (
                    "Verified against the public Annual Review of Microbiology "
                    "abstract; de Mendoza reviews increased unsaturated fatty "
                    "acid incorporation as growth temperature decreases."
                ),
            },
            {
                "reference": "DOI:10.1007/s00792-017-0939-x",
                "snippet": "liquid crystalline phase into the rigid gel phase",
                "notes": (
                    "Verified against the public Springer page; membrane lipids "
                    "below their transition temperature shift away from the "
                    "liquid-crystalline state."
                ),
            },
        ],
        "predicate_id": "RO:0002212",
    },
    {
        "subject": "membrane_fluidity",
        "predicate": "contributes to",
        "object": "low_temperature_membrane_transport",
        "description": (
            "Liquid-crystalline membrane fluidity supports permeability, "
            "diffusion, and membrane-protein function at low temperature."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s00792-017-0939-x",
                "snippet": "many membrane proteins only function in the liquid crystalline phase",
                "notes": (
                    "Verified against the public Springer page; Siliakus et al. "
                    "link low-temperature membrane phase to membrane-protein "
                    "function."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "low_temperature_membrane_transport",
        "predicate": "contributes to",
        "object": "very_limited_thermal_adaptation",
        "description": (
            "Cold preservation of membrane transport is one contextual branch "
            "of the thermal-acclimation flexibility represented in this "
            "nonmechanistic temperature-breadth graph."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s00792-017-0939-x",
                "snippet": "many membrane proteins only function in the liquid crystalline phase",
                "notes": (
                    "Verified against the public Springer page; this supports "
                    "the membrane-function branch without asserting a direct "
                    "universal cause of the 1-5 degree C temperature-delta bin."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "cspa_protein",
        "predicate": "contributes to",
        "object": "cold_rna_metabolism",
        "description": (
            "CspA RNA chaperone activity supports translation by reducing "
            "low-temperature RNA secondary structure."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1046/j.1365-2958.1999.01284.x",
                "snippet": (
                    "facilitates translation by destabilizing mRNA secondary "
                    "structures formed at low temperature"
                ),
                "notes": (
                    "Verified against the open Molecular Microbiology full text; "
                    "the source assigns CspA RNA-chaperone activity a role in "
                    "low-temperature translation."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "csda_helicase",
        "predicate": "contributes to",
        "object": "cold_rna_metabolism",
        "description": (
            "CsdA DEAD-box helicase activity supports RNA handling and large "
            "ribosomal-subunit maturation in the cold."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/nar/gkh603",
                "snippet": (
                    "CsdA is involved in the biogenesis of the large rather than "
                    "the small ribosomal subunit"
                ),
                "notes": (
                    "Verified against the open Nucleic Acids Research abstract; "
                    "CsdA supports an RNA helicase-dependent low-temperature "
                    "ribosome-biogenesis branch."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "large_ribosomal_subunit_biogenesis",
        "predicate": "contributes to",
        "object": "cold_rna_metabolism",
        "description": (
            "50S ribosomal-subunit biogenesis is part of the RNA-processing and "
            "translation-support module required during cold stress."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/nar/gkh603",
                "snippet": "deficit in free 50S subunits at low temperatures",
                "notes": (
                    "Verified against the open Nucleic Acids Research abstract; "
                    "CsdA defects in the cold appear as impaired 50S subunit "
                    "accumulation."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "cold_rna_metabolism",
        "predicate": "contributes to",
        "object": "very_limited_thermal_adaptation",
        "description": (
            "Cold-supportive RNA chaperone and ribosome-biogenesis functions "
            "are a second contextual branch of the thermal-acclimation "
            "flexibility represented in this nonmechanistic temperature-breadth "
            "graph."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1046/j.1365-2958.1999.01284.x",
                "snippet": (
                    "facilitates translation by destabilizing mRNA secondary "
                    "structures formed at low temperature"
                ),
                "notes": (
                    "Verified against the open Molecular Microbiology full text; "
                    "this supports the RNA-function branch without asserting "
                    "CspA as a universal determinant of the 1-5 degree C "
                    "temperature-delta bin."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
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
            "by adding 3 contextual cold membrane and RNA nodes plus 8 "
            "source- and verbatim-snippet-backed connectors. The connectors "
            "join supported cold-stress branches without asserting a direct "
            "universal unsaturated-fatty-acid cause of the 1-5 degree C "
            "temperature-delta bin. No paid research service was called."
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
