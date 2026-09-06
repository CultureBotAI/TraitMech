#!/usr/bin/env python3
"""Connect the pH-delta-mid2 contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_ph_delta_mid2_graph_183.py
    python scripts/connect_ph_delta_mid2_graph_183.py --apply
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

SLUG = "environment/ph_delta_mid2"
GRAPH_ID = "ph_delta_mid2_broad_breadth"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T15:00:00Z"
EXPECTED_COMPONENTS = 7

GRAPH_METADATA_BEFORE = {
    "title": "pH-delta-mid2 broad-breadth pH homeostasis",
    "description": (
        "DOI-backed graph linking broad pH-homeostasis flexibility to a pH "
        "growth breadth of approximately 3–4 pH units."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "pH-delta-mid2 contextual pH-homeostasis breadth",
    "description": (
        "DOI-backed nonmechanistic graph connecting broad pH-homeostasis "
        "flexibility, PMF component balancing, respiratory proton pumping, "
        "ATPase-mediated proton translocation, alkaline antiport, acid-side "
        "decarboxylation, and passive cytoplasmic buffering to the 3-4 pH-unit "
        "breadth bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "external_ph_stress",
        "predicate": "regulates",
        "object": "pmf_component_balance",
        "description": (
            "External pH stress modulates the relative balance of proton-motive "
            "force components."
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
        "predicate_id": "RO:0002211",
    },
    {
        "subject": "respiratory_proton_pumps",
        "predicate": "generates",
        "object": "pmf_generation",
        "description": "Primary respiratory-chain proton pumps generate proton motive force.",
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "Primary proton pumps generate the PMF",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; respiratory-chain complexes are listed "
                    "among the proton pumps that establish bacterial PMF."
                ),
            }
        ],
        "predicate_id": "biolink:produces",
    },
    {
        "subject": "f1fo_atpase",
        "predicate": "contributes to",
        "object": "proton_translocation_homeostasis",
        "description": (
            "F1Fo-ATPase contributes to pH homeostasis by coupling ATP turnover "
            "to proton translocation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "ATP-dependent H+ extrusion under acidic conditions",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; F1Fo-ATPase can drive proton efflux in "
                    "acid-stressed non-respiratory neutralophiles."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "na_h_antiporter_activity",
        "predicate": "contributes to",
        "object": "alkaline_ph_homeostasis",
        "description": (
            "Na+/H+ antiporter activity imports H+ and extrudes Na+ as part of "
            "alkaline pH homeostasis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "proton entry driven by the transmembrane potential",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; electrogenic cation/proton antiport "
                    "supports proton entry during alkaline stress."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "glutamate_decarboxylase_system",
        "predicate": "consumes",
        "object": "intracellular_proton",
        "description": (
            "The glutamate decarboxylase system consumes intracellular protons "
            "during acid-stress decarboxylation."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "consumes a proton during decarboxylation",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; GadB consumes a cytoplasmic proton when it "
                    "decarboxylates glutamate in the E. coli acid-resistance "
                    "cycle."
                ),
            }
        ],
        "predicate_id": "biolink:consumes",
    },
    {
        "subject": "cytoplasmic_buffers",
        "predicate": "contributes to",
        "object": "cytoplasmic_ph_buffering",
        "description": (
            "Small molecules, including polyamines, amino acids, and phosphate, "
            "contribute to passive cytoplasmic pH buffering."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/antibiotics12091474",
                "snippet": "Cytoplasmic pH is buffered by small molecules",
                "notes": (
                    "Verified against the open Rebelo et al. review; small "
                    "molecules contribute passive cytoplasmic buffering in pH "
                    "homeostasis."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "pmf_component_balance",
        "predicate": "associated with",
        "object": "broad_ph_homeostasis",
        "description": (
            "Proton-motive-force component balancing is associated with broad "
            "pH homeostasis across external pH stress."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "relative magnitudes of the two PMF components",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; the connector keeps PMF balancing as one "
                    "contextual arm of broad pH homeostasis."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "pmf_generation",
        "predicate": "associated with",
        "object": "broad_ph_homeostasis",
        "description": (
            "Respiratory proton pumping is associated with the PMF generation "
            "that supports pH-homeostasis flexibility."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "Primary proton pumps generate the PMF",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; respiratory-chain proton pumps establish "
                    "the PMF used by bacterial pH-homeostasis systems."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "proton_translocation_homeostasis",
        "predicate": "associated with",
        "object": "broad_ph_homeostasis",
        "description": (
            "ATPase-mediated proton translocation is associated with "
            "acid-stress pH-homeostasis flexibility."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "ATP-dependent H+ extrusion under acidic conditions",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; F1Fo-ATPase proton efflux is one acid-side "
                    "branch of pH homeostasis."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "alkaline_ph_homeostasis",
        "predicate": "associated with",
        "object": "broad_ph_homeostasis",
        "description": (
            "Na+/H+ antiporter-dependent alkaline pH homeostasis is one branch "
            "of broader pH-homeostasis flexibility."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "proton entry driven by the transmembrane potential",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; electrogenic antiport is retained as an "
                    "alkaline-side branch, not a universal breadth determinant."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "glutamate_decarboxylase_system",
        "predicate": "associated with",
        "object": "broad_ph_homeostasis",
        "description": (
            "The Gad proton-consuming acid-resistance system is associated with "
            "acid-side support for broad pH homeostasis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "consumes a proton during decarboxylation",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; the Gad branch supports acid-side "
                    "cytoplasmic proton consumption rather than directly "
                    "defining a 3-4 pH-unit growth breadth."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "cytoplasmic_ph_buffering",
        "predicate": "associated with",
        "object": "broad_ph_homeostasis",
        "description": (
            "Passive cytoplasmic buffering is associated with broad "
            "pH-homeostasis flexibility."
        ),
        "evidence": [
            {
                "reference": "DOI:10.3390/antibiotics12091474",
                "snippet": "Cytoplasmic pH is buffered by small molecules",
                "notes": (
                    "Verified against the open Rebelo et al. review; small "
                    "molecule buffering is retained as passive pH-homeostasis "
                    "support."
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
            "connectors among PMF balancing, respiratory proton pumping, "
            "ATPase-mediated proton translocation, alkaline antiport, Gad "
            "acid-side support, and cytoplasmic buffering. No paid research "
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
