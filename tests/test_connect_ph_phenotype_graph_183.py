"""Regression tests for the pH numerical-limits component repair in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from connect_ph_phenotype_graph_183 import (  # noqa: E402
    ACTION,
    ADDED_EDGES,
    EXPECTED_COMPONENTS,
    GRAPH_METADATA_AFTER,
    GRAPH_METADATA_BEFORE,
    SLUG,
    SOURCE_CONNECTOR_EDGES,
    TIMESTAMP,
    _components,
    _edge_key,
    transform,
)


def _current() -> dict:
    path = ROOT / "data" / "traits" / f"{SLUG}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before() -> dict:
    doc = _current()
    graph = doc["causal_graphs"][0]

    addition_keys = {_edge_key(edge) for edge in ADDED_EDGES}

    graph.update(GRAPH_METADATA_BEFORE)
    graph["edges"] = [
        copy.deepcopy(edge)
        for edge in graph["edges"]
        if _edge_key(edge) not in addition_keys
    ]
    return doc


def _transform_from_before() -> dict:
    doc = _before()
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS

    assert transform(SLUG, doc)
    return doc


def _has_curation_event(doc: dict, action: str, timestamp: str) -> bool:
    return any(
        event.get("action") == action and event.get("timestamp") == timestamp
        for event in doc["curation_history"]
    )


def test_repair_reaches_one_component_with_exact_snippet_backed_edges():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]

    assert _components(graph) == 1
    assert {field: graph[field] for field in GRAPH_METADATA_AFTER} == GRAPH_METADATA_AFTER

    by_key = {_edge_key(edge): edge for edge in graph["edges"]}

    for expected in ADDED_EDGES:
        assert by_key[_edge_key(expected)] == expected
        assert all(item.get("reference") and item.get("snippet") for item in expected["evidence"])
    assert _has_curation_event(doc, ACTION, TIMESTAMP)


def test_repaired_record_is_exactly_idempotent():
    doc = _transform_from_before()
    before = copy.deepcopy(doc)

    assert not transform(SLUG, doc)
    assert doc == before


def test_refuses_source_metadata_drift_before_migration():
    doc = _before()
    doc["causal_graphs"][0]["title"] = "drift"

    with pytest.raises(ValueError, match="source graph metadata drifted"):
        transform(SLUG, doc)


def test_refuses_source_connector_drift_before_migration():
    doc = _before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(SOURCE_CONNECTOR_EDGES[0])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="source edge drifted"):
        transform(SLUG, doc)


def test_refuses_added_edge_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(ADDED_EDGES[0])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="migrated edge drifted"):
        transform(SLUG, doc)


def test_refuses_missing_endpoint():
    doc = _before()
    doc["causal_graphs"][0]["nodes"] = [
        node
        for node in doc["causal_graphs"][0]["nodes"]
        if node["node_id"] != "proton_motive_force"
    ]

    with pytest.raises(ValueError, match="connector endpoint missing"):
        transform(SLUG, doc)


def test_refuses_partial_replay():
    doc = _before()
    doc["causal_graphs"][0]["edges"].append(copy.deepcopy(ADDED_EDGES[0]))

    with pytest.raises(ValueError, match="partial connector replay"):
        transform(SLUG, doc)
