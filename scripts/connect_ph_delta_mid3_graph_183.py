#!/usr/bin/env python3
"""Connect the pH-delta-mid3 contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_ph_delta_mid3_graph_183.py
    python scripts/connect_ph_delta_mid3_graph_183.py --apply
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

SLUG = "environment/ph_delta_mid3"
GRAPH_ID = "ph_delta_mid3_wide_breadth"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T16:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "pH-delta-mid3 wide-breadth pH homeostasis",
    "description": (
        "DOI-backed graph linking wide pH-homeostasis flexibility to a pH "
        "growth breadth of approximately 4–5 pH units."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "pH-delta-mid3 wide pH-homeostasis context",
    "description": (
        "DOI-backed nonmechanistic graph connecting wide pH-homeostasis "
        "flexibility, PMF regulation and generation, alkaline Na+/H+ antiport, "
        "ATPase support, phosphate buffering, amino-acid decarboxylation, and "
        "membrane proton-permeability branches to the 4-5 pH-unit breadth bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "external_alkaline_ph",
        "predicate": "regulates",
        "object": "na_h_antiport",
        "description": (
            "High external pH modulates the contribution of electrogenic Na+/H+ "
            "antiport to cytoplasmic pH homeostasis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "energize active proton uptake",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; cation/proton antiporters use PMF from "
                    "respiration or ATPases to drive proton uptake under "
                    "alkaline stress."
                ),
            }
        ],
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "pmf_regulation",
        "predicate": "contributes to",
        "object": "cytoplasmic_ph_maintenance",
        "description": (
            "Regulation of Delta-psi and Delta-pH contributes to maintenance of "
            "cytoplasmic pH across external pH changes."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "relative magnitudes of the two PMF components",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; bacterial pH-homeostasis demands determine "
                    "how delta-psi and delta-pH contribute to the PMF."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "proton_pumping_respiratory_complexes",
        "predicate": "generates",
        "object": "proton_motive_force",
        "description": "Proton-pumping respiratory complexes generate proton motive force.",
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "Primary proton pumps generate the PMF",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; respiratory-chain complexes are listed among "
                    "the proton pumps that establish bacterial PMF."
                ),
            }
        ],
        "predicate_id": "biolink:produces",
    },
    {
        "subject": "f0f1_atpase",
        "predicate": "contributes to",
        "object": "cytoplasmic_ph_maintenance",
        "description": "F0F1-ATPase proton pumping contributes to bacterial pH homeostasis.",
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "Key regulators of bacterial pH homeostasis",
                "notes": (
                    "Verified against the open Poolman review; proton-pumping "
                    "enzymes, including F0F1-ATPase in lactic acid bacteria, are "
                    "listed as bacterial pH-homeostasis regulators."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "phosphate_buffering",
        "predicate": "contributes to",
        "object": "intracellular_ph_stability",
        "description": "Cytoplasmic phosphate buffering contributes to intracellular pH stability.",
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "buffering capacity of the cytoplasm",
                "notes": (
                    "Verified against the open Poolman review; cytoplasmic "
                    "buffering is described as important for absorbing pH "
                    "fluctuations."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "aa_decarboxylation",
        "predicate": "contributes to",
        "object": "proton_motive_force",
        "description": (
            "Amino-acid decarboxylation pathways consume protons and contribute "
            "to PMF and intracellular pH control."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "Proton motive force generation by substrate decarboxylation",
                "notes": (
                    "Verified against the open Poolman review; substrate "
                    "decarboxylation is linked to bacterial PMF generation in "
                    "pH homeostasis."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "membrane_lipid_remodeling",
        "predicate": "decreases",
        "object": "proton_permeability",
        "description": "Membrane lipid composition shifts reduce proton permeability.",
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2022.1034164",
                "snippet": "higher content of saturated fatty acids",
                "notes": (
                    "Verified against the open Frontiers methanotroph review; "
                    "saturated bacterial membranes are described as lowering "
                    "proton permeability under acid stress."
                ),
            }
        ],
        "predicate_id": "RO:0002212",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "proton_motive_force",
        "predicate": "associated with",
        "object": "wide_ph_homeostasis",
        "description": (
            "PMF generation and amino-acid decarboxylation are associated with "
            "wide pH-homeostasis flexibility."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": "utilization of the PMF for nutrient uptake",
                "notes": (
                    "Verified against the open Poolman review; the connector "
                    "joins the decarboxylation and PMF branch as pH-homeostasis "
                    "support without asserting direct causation of a 4-5 "
                    "pH-unit growth breadth."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "cytoplasmic_ph_maintenance",
        "predicate": "associated with",
        "object": "wide_ph_homeostasis",
        "description": (
            "Cytoplasmic pH maintenance is associated with wide "
            "pH-homeostasis flexibility across external pH changes."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": (
                    "Bacterial pH homeostasis is important for physiology, "
                    "ecology and pathogenesis"
                ),
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; PMF regulation is retained as one energetic "
                    "arm of the wide pH-breadth context."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "na_h_antiport",
        "predicate": "associated with",
        "object": "wide_ph_homeostasis",
        "description": (
            "Electrogenic Na+/H+ antiport is associated with alkaline-side "
            "support for wide pH homeostasis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "active transport of protons inward is a crucial adaptation",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; the connector keeps antiport as "
                    "alkaline-side support rather than a universal breadth "
                    "cause."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "intracellular_ph_stability",
        "predicate": "associated with",
        "object": "wide_ph_homeostasis",
        "description": (
            "Cytoplasmic phosphate buffering is associated with stable "
            "intracellular pH during pH-homeostasis challenges."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1093/femsre/fuad033",
                "snippet": (
                    "large impact on the internal pH if there would not be "
                    "sufficient buffering capacity"
                ),
                "notes": (
                    "Verified against the open Poolman review; phosphate "
                    "buffering remains one passive branch of pH-homeostasis "
                    "support."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "proton_permeability",
        "predicate": "associated with",
        "object": "wide_ph_homeostasis",
        "description": (
            "Membrane proton permeability is associated with acid-side envelope "
            "support for wide pH homeostasis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3389/fmicb.2022.1034164",
                "snippet": "saturated membrane to minimize proton permeability",
                "notes": (
                    "Verified against the open Frontiers methanotroph review; "
                    "lipid remodeling is retained as an acid-side "
                    "proton-permeability branch."
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
            "connectors among the PMF generation, PMF regulation, alkaline "
            "Na+/H+ antiport, ATPase, phosphate-buffering, amino-acid "
            "decarboxylation, and membrane proton-permeability branches. No "
            "paid research service was called."
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
