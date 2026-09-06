#!/usr/bin/env python3
"""Connect the temperature-delta-high contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_temperature_delta_high_graph_183.py
    python scripts/connect_temperature_delta_high_graph_183.py --apply
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

SLUG = "environment/temperature_delta_high"
GRAPH_ID = "temperature_delta_high_eurythermal"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T19:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "Temperature-delta-high eurythermal breadth",
    "description": (
        "DOI-backed graph linking maximal thermal-adaptation flexibility to "
        "a temperature growth breadth above 30 \u00b0C."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Temperature-delta-high eurythermal context",
    "description": (
        "DOI-backed nonmechanistic graph connecting maximal "
        "thermal-adaptation flexibility, cold-side homoviscous membrane "
        "remodeling, high-temperature membrane-viscosity shifts, and "
        "thermostable-enzyme context to the above-30-degrees-C "
        "temperature-delta bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "decreased_growth_temperature",
        "predicate": "increases",
        "object": "unsaturated_fatty_acid_biosynthesis",
        "description": (
            "Lower growth temperature increases incorporation of unsaturated "
            "fatty acids (homoviscous adaptation)."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "incorporation of proportionally more unsaturated fatty acids",
                "notes": (
                    "Verified against the de Mendoza Annual Review abstract; "
                    "bacterial membranes remodel by incorporating proportionally "
                    "more unsaturated fatty acids as growth temperature decreases."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "homoviscous_adaptation",
        "predicate": "contributes to",
        "object": "membrane_fluidity_homeostasis",
        "description": (
            "Homoviscous adaptation contributes to membrane "
            "fluidity/permeability homeostasis across thermal shifts."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "remodel the fluidity of their membrane bilayer",
                "notes": (
                    "Verified against the de Mendoza Annual Review abstract; "
                    "homoviscous adaptation is the named membrane-fluidity "
                    "remodeling process used after growth temperature decreases."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "decreased_membrane_fluidity",
        "predicate": "positively regulates",
        "object": "unsaturated_fatty_acid_biosynthesis",
        "description": (
            "Reduced membrane fluidity is sensed and positively regulates "
            "unsaturated fatty acid biosynthesis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "upregulate the biosynthesis of unsaturated fatty acids",
                "notes": (
                    "Verified against the de Mendoza Annual Review abstract; "
                    "bacteria sense decreased membrane fluidity and initiate "
                    "responses that upregulate unsaturated fatty acid biosynthesis."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "lipid_desaturase_activity",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": (
            "Lipid desaturases introduce cis double bonds that loosen packing "
            "and increase fluidity."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/cells12101353",
                "snippet": "cis-double bonds, result in looser packing and increased fluidity",
                "notes": (
                    "Verified against the Wu et al. Cells review; lipid "
                    "desaturase-generated cis double bonds loosen acyl-chain "
                    "packing and increase membrane-bilayer fluidity."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "cis_trans_isomerase_activity",
        "predicate": "increases",
        "object": "membrane_viscosity_high_temperature",
        "description": (
            "Cis-trans isomerization of existing UFAs yields trans-UFAs "
            "resembling SFAs, raising membrane viscosity during warming."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/cells12101353",
                "snippet": "properties that resemble SFAs",
                "notes": (
                    "Verified against the Wu et al. Cells review; converting "
                    "cis-UFAs to trans-UFAs makes them more SFA-like and closer "
                    "packing at higher temperature."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "increased_fatty_acid_diversity",
        "predicate": "increases",
        "object": "membrane_fluidity",
        "description": (
            "Shifts in acyl chain length/branching and unsaturation jointly "
            "increase membrane fluidity at lower temperatures."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/cells12101353",
                "snippet": "increase the proportion of UFAs and short-chain fatty acids",
                "notes": (
                    "Verified against the Wu et al. Cells review; cold-adapted "
                    "membranes can increase unsaturated and short-chain fatty "
                    "acid proportions and modify branched-chain fatty-acid "
                    "content."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "thermostable_enzyme",
        "predicate": "prevents",
        "object": "irreversible_protein_inactivation",
        "description": (
            "Intrinsic enzyme thermostability prevents irreversible inactivation, "
            "extending upper growth limits."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/MMBR.65.1.1-43.2001",
                "snippet": "resistant to irreversible inactivation at high temperatures",
                "notes": (
                    "Verified against the open Vieille and Zeikus review; "
                    "hyperthermophilic enzymes are described as thermostable "
                    "and resistant to irreversible inactivation at high "
                    "temperatures."
                ),
            }
        ],
        "predicate_id": "RO:0002212",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "unsaturated_fatty_acid_biosynthesis",
        "predicate": "contributes to",
        "object": "homoviscous_adaptation",
        "description": (
            "Unsaturated-fatty-acid biosynthesis contributes to cold-side "
            "homoviscous membrane remodeling."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "termed homoviscous adaptation",
                "notes": (
                    "Verified against the de Mendoza Annual Review abstract; "
                    "this connector keeps unsaturated-fatty-acid biosynthesis as "
                    "one component of homoviscous adaptation rather than the "
                    "whole response."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "membrane_fluidity",
        "predicate": "associated with",
        "object": "membrane_fluidity_homeostasis",
        "description": (
            "Membrane fluidity is associated with the homoviscous homeostasis "
            "branch of broad thermal adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/cells12101353",
                "snippet": "cis-double bonds, result in looser packing and increased fluidity",
                "notes": (
                    "Verified against the Wu et al. Cells review; this connector "
                    "keeps desaturase-linked fluidity as a physical membrane "
                    "state associated with homeostasis."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "membrane_viscosity_high_temperature",
        "predicate": "associated with",
        "object": "membrane_fluidity_homeostasis",
        "description": (
            "High-temperature membrane viscosity is associated with the "
            "warming-side boundary of membrane-fluidity homeostasis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/cells12101353",
                "snippet": "properties that resemble SFAs",
                "notes": (
                    "Verified against the Wu et al. Cells review; this connector "
                    "keeps cis-trans isomerization as warming-side membrane "
                    "context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "membrane_fluidity_homeostasis",
        "predicate": "associated with",
        "object": "maximal_thermal_adaptation",
        "description": (
            "Membrane-fluidity homeostasis is associated with the broad "
            "thermal-adaptation context used to represent an extreme "
            "temperature-growth breadth."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1146/annurev-micro-091313-103612",
                "snippet": "remodel the fluidity of their membrane bilayer",
                "notes": (
                    "Verified against the de Mendoza Annual Review abstract; "
                    "this connector scopes homoviscous adaptation as membrane "
                    "context for the eurythermal bin."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "thermostable_enzyme",
        "predicate": "associated with",
        "object": "maximal_thermal_adaptation",
        "description": (
            "Thermostable-enzyme protection is associated with the high-temperature "
            "side of broad thermal adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/MMBR.65.1.1-43.2001",
                "snippet": "hyperthermophilic enzymes, are typically thermostable",
                "notes": (
                    "Verified against the open Vieille and Zeikus review; this "
                    "connector keeps thermostable enzymes as high-temperature "
                    "context rather than direct proof of an above-30-degrees-C "
                    "growth breadth."
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
            "by adding 5 source- and verbatim-snippet-backed association or "
            "contribution connectors among cold UFA synthesis, homoviscous "
            "adaptation, membrane-fluidity, high-temperature membrane-viscosity, "
            "and thermostable-enzyme branches. No paid research service was "
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
    print(f"{'applied' if write else 'dry run'}: repaired {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
