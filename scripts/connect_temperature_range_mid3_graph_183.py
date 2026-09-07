#!/usr/bin/env python3
"""Connect the temperature-range-mid3 contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_temperature_range_mid3_graph_183.py
    python scripts/connect_temperature_range_mid3_graph_183.py --apply
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

SLUG = "environment/temperature_range_mid3"
GRAPH_ID = "temperature_range_mid3_upper_mesophile"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T22:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "Temperature-range-mid3 upper-mesophile range",
    "description": (
        "DOI-backed graph linking upper-mesophile adaptation to a temperature "
        "growth range of approximately 30\u201334 \u00b0C."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "Temperature-range-mid3 upper-mesophile context",
    "description": (
        "DOI-backed nonmechanistic graph connecting upper-mesophile "
        "growth-range context, the DesK/DesR membrane-order sensor, des "
        "expression, cooling-induced membrane rigidification, and "
        "homeoviscous liquid-crystalline membrane maintenance."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "membrane_order",
        "predicate": "positively regulates",
        "object": "desk_kinase_state",
        "description": (
            "Increased membrane order (reduced fluidity) promotes the DesK "
            "kinase-dominant state; membrane physical state is the proximate "
            "signal."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "kinase-dominant state of DesK",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "the current Des model links temperature-decrease-driven "
                    "membrane rigidification/thickening to the active "
                    "kinase-dominant state."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "desk",
        "predicate": "positively regulates",
        "object": "desr",
        "description": (
            "DesK controls DesR phosphorylation in the core two-component "
            "signaling step linking membrane physical state to transcriptional "
            "response."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "phosphorylating or dephosphorylating DesR",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "DesK is described as a membrane-associated histidine "
                    "kinase that phosphorylates or dephosphorylates DesR "
                    "in a temperature-dependent manner."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "phospho_desr",
        "predicate": "positively regulates",
        "object": "des_gene",
        "description": (
            "DesR-P tetramerizes, binds the des promoter, and positively "
            "regulates des expression for lipid desaturation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "activating expression of the des gene",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "phosphorylated DesR tetramers bind Pdes and activate "
                    "des transcription."
                ),
            }
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "des_gene",
        "predicate": "regulates",
        "object": "membrane_fatty_acyl_chains",
        "description": (
            "Des-mediated unsaturation regulates membrane fatty acyl chains, "
            "fluidizing the membrane and reducing bilayer thickness."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "desaturates the fatty acyl chains",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "Des desaturates membrane-lipid fatty acyl chains as the "
                    "effector of the DesK/DesR temperature-sensing system."
                ),
            }
        ],
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "temperature_decrease",
        "predicate": "causes",
        "object": "membrane_rigidity",
        "description": (
            "A temperature decrease causes membrane rigidification and increased "
            "thickness, a physical trigger for homeoviscous adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "rigidification and concomitant thickening",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "temperature decrease is described as causing cell-membrane "
                    "rigidification and thickening."
                ),
            }
        ],
        "predicate_id": "biolink:causes",
    },
    {
        "subject": "homeoviscous_adaptation",
        "predicate": "contributes to",
        "object": "liquid_crystalline_membrane",
        "description": (
            "Homeoviscous adaptation contributes to a functional "
            "liquid-crystalline membrane state at low temperature."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1007/s42770-023-01057-4",
                "snippet": "maintain the liquid crystalline phase",
                "notes": (
                    "Verified against the open Ram\u00f3n et al. review; organisms "
                    "in cold environments are described as adapting their "
                    "membrane composition to maintain a liquid-crystalline "
                    "state."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "membrane_rigidity",
        "predicate": "associated with",
        "object": "membrane_order",
        "description": (
            "Cooling-induced membrane rigidification is associated with the "
            "ordered membrane state sensed by DesK."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "membrane rigidifies and increases in thickness",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "this connector joins the cooling membrane signal to the "
                    "DesK kinase-state branch."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "desk_kinase_state",
        "predicate": "associated with",
        "object": "desk",
        "description": (
            "The DesK kinase-dominant state is associated with the DesK/DesR "
            "temperature-sensing step."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "DesK is a molecular sensor that directly detects membrane thickness",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "this connector keeps DesK kinase activity as two-component "
                    "signaling context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "desr",
        "predicate": "associated with",
        "object": "phospho_desr",
        "description": (
            "DesR regulation is associated with phosphorylated DesR promoter "
            "activation in the DesK/DesR branch."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": "DesR is a DNA-binding response regulator (transcriptional activator)",
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "this connector joins DesR to its phosphorylated "
                    "transcription-activation context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "membrane_fatty_acyl_chains",
        "predicate": "associated with",
        "object": "homeoviscous_adaptation",
        "description": (
            "Des-mediated fatty-acyl-chain unsaturation is associated with "
            "homeoviscous membrane adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1128/spectrum.03925-23",
                "snippet": (
                    "resulting in membrane fluidization and concomitant decrease "
                    "of bilayer thickness"
                ),
                "notes": (
                    "Verified against the open Sidarta et al. introduction; "
                    "this connector keeps des expression as membrane-fatty-acyl "
                    "remodeling context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "liquid_crystalline_membrane",
        "predicate": "associated with",
        "object": "upper_mesophile_adaptation",
        "description": (
            "Maintenance of a liquid-crystalline membrane state is associated "
            "with upper-mesophile range adaptation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/s41467-024-53677-5",
                "snippet": (
                    "homeostatically maintain the fluidity of their membranes by "
                    "adapting lipid composition"
                ),
                "notes": (
                    "Verified against the open Hoogerland et al. abstract; this "
                    "connector keeps lipid-composition adaptation as range-bin "
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
            "by adding 5 source- and verbatim-snippet-backed association "
            "connectors among DesK/DesR membrane-order sensing, des expression, "
            "cooling-induced membrane rigidification, and homeoviscous "
            "liquid-crystalline membrane branches. No paid research service was "
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
