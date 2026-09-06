#!/usr/bin/env python3
"""Connect the temperature-optimum-very-low contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_temperature_optimum_very_low_graph_183.py
    python scripts/connect_temperature_optimum_very_low_graph_183.py --apply
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

SLUG = "environment/temperature_optimum_very_low"
GRAPH_ID = "temperature_optimum_very_low_psychrophile_setpoint"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T21:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "Temperature-optimum-very-low psychrophile setpoint",
    "description": (
        "DOI-backed graph linking cold-adapted membrane and enzyme machinery "
        "to a temperature optimum at or below ~10 \u00b0C."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Temperature-optimum-very-low psychrophile context",
    "description": (
        "DOI-backed nonmechanistic graph connecting cold-adapted membranes, "
        "cold-shock RNA chaperones, compatible-solute cryoprotection, "
        "antifreeze-protein ice binding, and flexible enzyme branches to the "
        "at-or-below-10-degrees-C optimum bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "fatty_acid_desaturase_activity",
        "predicate": "increases",
        "object": "unsaturated_fatty_acids",
        "description": "Fatty acid desaturase activity increases unsaturated acyl chains.",
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "increase in the proportion of unsaturated acyl chains",
                "notes": (
                    "Verified against the open Hamdan review; lower growth "
                    "temperatures are described as activating desaturases "
                    "that convert saturated acyl fatty acids to unsaturated "
                    "ones."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "unsaturated_fatty_acids",
        "predicate": "contributes to",
        "object": "membrane_fluidity",
        "description": (
            "Increased unsaturated fatty acids contribute to membrane fluidity "
            "at low temperature."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/AEM.01928-22",
                "snippet": "proportion of unsaturated fatty acids was higher",
                "notes": (
                    "Verified against the open Yang et al. abstract; "
                    "Bacillus simplex H-b cultured at low temperature "
                    "carried a higher unsaturated-fatty-acid proportion."
                ),
            },
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "maintain optimum membrane fluidity",
                "notes": (
                    "Verified against the open Hamdan review; fatty-acyl-chain "
                    "modifications are described as preserving membrane "
                    "fluidity in freezing environments."
                ),
            },
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "membrane_fluidity",
        "predicate": "contributes to",
        "object": "psychrophile_machinery",
        "description": (
            "Maintained membrane fluidity contributes to cold-adapted cellular "
            "machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/AEM.01928-22",
                "snippet": "contribute to the survival of the strain under cold conditions",
                "notes": (
                    "Verified against the open Yang et al. abstract; the cold "
                    "adaptation model includes membrane transport adjustment "
                    "among mechanisms supporting Bacillus simplex H-b survival "
                    "under cold conditions."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "cold_shock_proteins",
        "predicate": "contributes to",
        "object": "translation_low_temperature",
        "description": (
            "Cold shock proteins / RNA chaperones contribute to transcription "
            "and translation in the cold."
        ),
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "regulation of cellular protein synthesis",
                "notes": (
                    "Verified against the open Hamdan review; cold-shock "
                    "proteins are linked to cellular protein-synthesis "
                    "regulation, including transcription and translation "
                    "initiation."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "glycine_betaine",
        "predicate": "contributes to",
        "object": "protein_membrane_stabilization",
        "description": (
            "Glycine betaine contributes to protein and membrane stabilization "
            "during cold stress."
        ),
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "growth-enhancing effect of glycine betaine",
                "notes": (
                    "Verified against the open Hamdan review; the glycine "
                    "betaine paragraph cites low-temperature growth enhancement "
                    "and discusses compatible solutes as cold cryoprotectants."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "trehalose",
        "predicate": "contributes to",
        "object": "cryoprotection",
        "description": "Trehalose contributes to cryoprotection.",
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "preventing protein denaturation and aggregation",
                "notes": (
                    "Verified against the open Hamdan review; trehalose is "
                    "reported as preventing protein denaturation and aggregation "
                    "in psychrophilic bacteria."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "antifreeze_proteins",
        "predicate": "causes",
        "object": "thermal_hysteresis",
        "description": "Antifreeze proteins lower the freezing point via thermal hysteresis.",
        "evidence": [
            {
                "reference": "DOI:10.1007/s42770-023-01057-4",
                "snippet": "lower the water freezing point",
                "notes": (
                    "Verified against the open Ram\u00f3n et al. abstract and "
                    "review text; anti-freeze proteins are described as "
                    "lowering the water freezing point via thermal hysteresis "
                    "or ice-recrystallization inhibition."
                ),
            }
        ],
        "predicate_id": "biolink:causes",
    },
    {
        "subject": "enzyme_structural_flexibility",
        "predicate": "increases",
        "object": "catalytic_activity_low_temperature",
        "description": (
            "Increased enzyme structural flexibility increases catalytic "
            "activity at low temperature."
        ),
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "up to 10-fold higher specific activity",
                "notes": (
                    "Verified against the open Hamdan review; psychrophiles "
                    "are described as producing structurally flexible enzymes "
                    "with higher low-temperature specific activity than "
                    "mesophilic homologues."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "translation_low_temperature",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "Cold-shock protein support for translation is associated with "
            "psychrophile cold-adapted machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.4161/rna.7.6.13482",
                "snippet": "facilitating transcription and translation at low temperature",
                "notes": (
                    "Verified against the open Hamdan review; this connector "
                    "keeps cold-shock RNA chaperones as protein-synthesis "
                    "context for psychrophile physiology."
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
            "Compatible-solute protein and membrane stabilization is "
            "associated with psychrophile cold-adapted machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "compatible solutes such as trehalose and glycine-betaine",
                "notes": (
                    "Verified against the open Hamdan review; this connector "
                    "keeps glycine-betaine compatible-solute effects as broad "
                    "cold-stress context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "cryoprotection",
        "predicate": "associated with",
        "object": "protein_membrane_stabilization",
        "description": (
            "Trehalose-linked cryoprotection is associated with protein and "
            "membrane stabilization during cold stress."
        ),
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": (
                    "counteracting protein aggregation, improving protein "
                    "folding and stabilizing membranes and proteins at "
                    "chilling temperatures"
                ),
                "notes": (
                    "Verified against the open Hamdan review; this connector "
                    "keeps trehalose as a compatible-solute cryoprotection "
                    "branch."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "thermal_hysteresis",
        "predicate": "associated with",
        "object": "cryoprotection",
        "description": (
            "Antifreeze-protein thermal hysteresis is associated with "
            "cryoprotection near freezing."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s42770-023-01057-4",
                "snippet": (
                    "AFPs lower the water freezing point, avoiding frostbite "
                    "due to their thermal hysteresis"
                ),
                "notes": (
                    "Verified against the open Ram\u00f3n et al. abstract and "
                    "review text; this connector keeps antifreeze proteins as "
                    "ice-binding cryoprotection context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "catalytic_activity_low_temperature",
        "predicate": "associated with",
        "object": "psychrophile_machinery",
        "description": (
            "Flexible-enzyme catalytic activity is associated with "
            "psychrophile cold-adapted machinery."
        ),
        "evidence": [
            {
                "reference": "DOI:10.17159/sajs.2018/20170254",
                "snippet": "adapted to function at low temperatures, with high catalytic constants",
                "notes": (
                    "Verified against the open Hamdan review; this connector "
                    "keeps low-temperature enzyme flexibility as contextual "
                    "psychrophile machinery."
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
            "by adding 5 source- and verbatim-snippet-backed association "
            "connectors among cold-shock RNA support, compatible-solute "
            "cryoprotection, antifreeze protein ice-binding, and "
            "low-temperature flexible-enzyme branches. No paid research "
            "service was called."
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
