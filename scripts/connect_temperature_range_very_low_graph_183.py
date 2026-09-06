#!/usr/bin/env python3
"""Connect the temperature-range-very-low contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_temperature_range_very_low_graph_183.py
    python scripts/connect_temperature_range_very_low_graph_183.py --apply
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

SLUG = "environment/temperature_range_very_low"
GRAPH_ID = "temperature_range_very_low_psychrophile"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T23:20:00Z"
EXPECTED_COMPONENTS = 7

GRAPH_METADATA_BEFORE = {
    "title": "Temperature-range-very-low psychrophile range",
    "description": (
        "DOI-backed graph linking psychrophile cold-adapted machinery to a "
        "temperature growth range reaching \u2264 ~10 \u00b0C."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Temperature-range-very-low psychrophile context",
    "description": (
        "DOI-backed nonmechanistic graph connecting membrane desaturation, "
        "two-component cold signaling, CspA-family RNA chaperones, cold "
        "proteostasis, compatible-solute stabilization, and ice-binding "
        "protein branches to the at-or-below-10-degrees-C growth-range bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
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
                    "Verified against the open Ram\u00f3n et al. PubMed abstract; "
                    "the multifactorial cold-adaptation model lists membrane "
                    "composition adaptation by producing lipid double bonds."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "low_temperature",
        "predicate": "activates",
        "object": "two_component_cold_signaling",
        "description": "Cold-induced membrane state changes activate two-component cold signaling.",
        "evidence": [
            {
                "reference": "DOI:10.1007/s42770-023-01057-4",
                "snippet": "activation of a two-component system",
                "notes": (
                    "Verified against the open Ram\u00f3n et al. PubMed abstract; "
                    "cold sensing is described as occurring mainly through "
                    "liquid-crystalline membrane-state changes that activate a "
                    "two-component signal-transduction system."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
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
    {
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
                    "Antarctic psychrophile review discusses heat-shock proteins "
                    "associated with protein folding in 4 \u00b0C versus "
                    "18 \u00b0C Pseudoalteromonas haloplanktis TAC125."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
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
                "snippet": "stabilizing membranes and proteins at chilling temperatures",
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
    {
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
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "membrane_fluidity",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "Membrane fatty-acid desaturation is associated with the "
            "cold-adapted machinery supporting psychrophile growth ranges."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s42770-023-01057-4",
                "snippet": "production of double bonds in lipids",
                "notes": (
                    "Verified against the open Ram\u00f3n et al. PubMed abstract; "
                    "this connector keeps membrane desaturation as cold "
                    "membrane-adaptation context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "two_component_cold_signaling",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "Two-component cold signaling is associated with psychrophile "
            "cold-adapted machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s42770-023-01057-4",
                "snippet": "activation of a two-component system",
                "notes": (
                    "Verified against the open Ram\u00f3n et al. PubMed abstract; "
                    "this connector keeps low-temperature membrane sensing as "
                    "cold-acclimation context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "cold_stabilized_rna_secondary_structure",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "CspA-family regulation of cold-stabilized RNA structure is "
            "associated with psychrophile cold-adapted machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.4161/rna.7.6.13482",
                "snippet": "through their RNA chaperoning function",
                "notes": (
                    "Verified against the open Phadtare and Severinov PubMed "
                    "abstract; this connector keeps CspA-family RNA chaperones "
                    "as low-temperature transcript context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "proteostasis_cold",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "Cold proteostasis support is associated with the psychrophile "
            "machinery context."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2023.1197797",
                "snippet": "heat shock proteins associated to folding",
                "notes": (
                    "Verified against the open Ramasamy et al. PMC text; this "
                    "connector keeps chaperone/protease systems as protein-folding "
                    "context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "protein_membrane_stabilization",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "Compatible-solute stabilization is associated with psychrophile "
            "cold-adapted machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2023.1197797",
                "snippet": "stabilizing membranes and proteins at chilling temperatures",
                "notes": (
                    "Verified against the open Ramasamy et al. PMC text; this "
                    "connector keeps compatible osmolytes as stabilization "
                    "context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "ice_crystal_growth",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "Ice-binding protein inhibition of ice-crystal growth is associated "
            "with psychrophile cold-adapted machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2023.1197797",
                "snippet": "inhibits the growth of ice crystals",
                "notes": (
                    "Verified against the open Ramasamy et al. PMC text; this "
                    "connector keeps ice-binding proteins as freezing-protection "
                    "context."
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


def _edges_by_key(edges: list[dict[str, Any]]) -> dict[
    tuple[str | None, str | None, str | None], dict[str, Any]
]:
    return {_edge_key(edge): edge for edge in edges}


def _assert_graph_metadata(graph: dict[str, Any], expected: dict[str, str], state: str) -> None:
    actual = {field: graph.get(field) for field in expected}
    if actual != expected:
        raise ValueError(f"{SLUG}: {state} graph metadata drifted: {actual!r}")


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


def _assert_endpoints(graph: dict[str, Any], edges: list[dict[str, Any]]) -> None:
    node_ids = {node["node_id"] for node in graph.get("nodes") or []}
    for edge in edges:
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
    additions = _edges_by_key(ADDED_EDGES)
    source_connectors = _edges_by_key(SOURCE_CONNECTOR_EDGES)

    existing_keys = {_edge_key(edge) for edge in graph.get("edges") or []}
    addition_keys = set(additions)
    present = existing_keys & addition_keys

    before = _components(graph)
    if before == 1 and present == addition_keys:
        _assert_graph_metadata(graph, GRAPH_METADATA_AFTER, "migrated")
        _assert_exact_edges(graph, additions, "migrated")
        return False

    _assert_graph_metadata(graph, GRAPH_METADATA_BEFORE, "source")
    if present:
        raise ValueError(f"{SLUG}: partial connector replay: {sorted(present)}")

    _assert_exact_edges(graph, source_connectors, "source")
    _assert_endpoints(graph, ADDED_EDGES)
    if before != EXPECTED_COMPONENTS:
        raise ValueError(f"{SLUG}: expected {EXPECTED_COMPONENTS} components, found {before}")

    graph.update(GRAPH_METADATA_AFTER)
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
            "by adding 6 source- and verbatim-snippet-backed association "
            "connectors among membrane desaturation, two-component cold "
            "signaling, CspA-family RNA chaperone, cold proteostasis, "
            "compatible-solute, and ice-binding protein branches. No paid "
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
    print(f"{'applied' if write else 'dry run'}: repaired {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
