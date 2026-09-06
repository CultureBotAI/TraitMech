#!/usr/bin/env python3
"""Connect the pH-delta-very-low contextual graph for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/connect_ph_delta_very_low_graph_183.py
    python scripts/connect_ph_delta_very_low_graph_183.py --apply
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

SLUG = "environment/ph_delta_very_low"
GRAPH_ID = "ph_delta_very_low_stenotopic"
ACTION = "CONNECT_CAUSAL_GRAPH_COMPONENTS"
TIMESTAMP = "2026-09-04T17:00:00Z"
EXPECTED_COMPONENTS = 6

GRAPH_METADATA_BEFORE = {
    "title": "pH-delta-very-low stenotopic breadth",
    "description": (
        "DOI-backed graph linking very limited pH-homeostasis flexibility to a "
        "pH growth breadth of at most ~1 pH unit."
    ),
}

GRAPH_METADATA_AFTER = {
    "title": "pH-delta-very-low stenotopic pH-homeostasis context",
    "description": (
        "DOI-backed nonmechanistic graph connecting very limited "
        "pH-homeostasis flexibility, PMF partitioning, constitutive "
        "pH-homeostatic expression cost, alkaline antiport, F1Fo acid-side "
        "pumping, and Gad proton-consumption branches to the at-most-1 "
        "pH-unit breadth bin."
    ),
}

SOURCE_CONNECTOR_EDGES: list[dict[str, Any]] = [
    {
        "subject": "external_ph_stress",
        "predicate": "regulates",
        "object": "pmf_partitioning",
        "description": (
            "External pH stress modulates partitioning of the proton motive "
            "force between Delta-pH and Delta-psi."
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
        "subject": "constitutive_ph_homeostasis_expression",
        "predicate": "causes",
        "object": "energetic_cost",
        "description": (
            "Constitutive expression of pH-homeostatic machinery can impose a "
            "growth cost near neutral pH."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "energetic cost of expressing proteins",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; constitutive pH-homeostatic preparedness in "
                    "extremophiles can negatively affect growth near neutral pH."
                ),
            }
        ],
        "predicate_id": "biolink:causes",
    },
    {
        "subject": "na_h_antiporter_activity",
        "predicate": "contributes to",
        "object": "alkaline_ph_homeostasis",
        "description": "Na+/H+ antiporter activity contributes to alkaline pH homeostasis.",
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "proton entry driven by the transmembrane potential",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; electrogenic cation/proton antiport supports "
                    "proton entry during alkaline stress."
                ),
            }
        ],
        "predicate_id": "RO:0002326",
    },
    {
        "subject": "f1fo_atpase_proton_pumping",
        "predicate": "contributes to",
        "object": "acid_stress_survival",
        "description": "Hydrolytic F1Fo-ATPase proton pumping contributes to acid-stress survival.",
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
        "subject": "glutamate_decarboxylase_system",
        "predicate": "contributes to",
        "object": "cytoplasmic_proton_consumption",
        "description": (
            "Glutamate decarboxylase GadB coupled with a GABA/glutamate "
            "antiporter contributes to cytoplasmic proton consumption."
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
        "predicate_id": "RO:0002326",
    },
]

ADDED_EDGES: list[dict[str, Any]] = [
    {
        "subject": "pmf_partitioning",
        "predicate": "associated with",
        "object": "very_limited_ph_homeostasis",
        "description": (
            "PMF partitioning is associated with the pH-homeostasis flexibility "
            "that bounds a very narrow external-pH growth interval."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": (
                    "demands of pH homeostasis for particular bacteria determine "
                    "the relative magnitudes"
                ),
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; the connector keeps PMF partitioning as "
                    "pH-homeostasis context rather than direct proof of the "
                    "at-most-1-unit breadth."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "energetic_cost",
        "predicate": "associated with",
        "object": "very_limited_ph_homeostasis",
        "description": (
            "The energetic cost of constitutive extremophile "
            "pH-homeostatic machinery is associated with boundary constraints "
            "on very narrow pH breadth."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "preparedness often negatively impacts growth at near neutral pH",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; the connector represents a "
                    "cost-of-preparedness branch, not a universal cause of "
                    "stenotopic pH breadth."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "alkaline_ph_homeostasis",
        "predicate": "associated with",
        "object": "very_limited_ph_homeostasis",
        "description": (
            "Na+/H+ antiporter-linked alkaline pH homeostasis is a contextual "
            "branch of limited pH-homeostasis flexibility."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "active transport of protons inward is a crucial adaptation",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; alkaline proton import support is retained "
                    "as one boundary branch."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "acid_stress_survival",
        "predicate": "associated with",
        "object": "very_limited_ph_homeostasis",
        "description": (
            "F1Fo-ATPase acid-stress survival support is associated with the "
            "acid-side boundary of limited pH homeostasis."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "promotes ATP-dependent H+ extrusion under acidic conditions",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; ATP-dependent proton pumping is kept as "
                    "acid-side support rather than a direct breadth mechanism."
                ),
            }
        ],
        "predicate_id": "biolink:associated_with",
    },
    {
        "subject": "cytoplasmic_proton_consumption",
        "predicate": "associated with",
        "object": "very_limited_ph_homeostasis",
        "description": (
            "Gad-linked cytoplasmic proton consumption is associated with "
            "acid-side pH-homeostasis support."
        ),
        "evidence": [
            {
                "reference": "DOI:10.1038/nrmicro2549",
                "snippet": "The consumption of the proton supports acid pH homeostasis",
                "notes": (
                    "Verified against the open PMC manuscript of the Krulwich "
                    "et al. review; Gad-mediated proton consumption is scoped "
                    "as an acid-side support branch."
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
            "connectors among PMF partitioning, constitutive cost, alkaline "
            "antiport, F1Fo acid-survival support, and Gad proton-consumption "
            "branches. No paid research service was called."
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
