"""Regression tests for the temperature_delta_very_low review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_temperature_delta_very_low_graph_183 import (  # noqa: E402
    ACTION,
    EDGE_REMOVALS,
    EDGE_REPLACEMENTS,
    NODE_REPLACEMENTS,
    SLUG,
    TIMESTAMP,
    _edge_key,
    transform,
)


def _current() -> dict:
    path = ROOT / "data" / "traits" / f"{SLUG}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before() -> dict:
    doc = _current()
    graph = doc["causal_graphs"][0]
    after_nodes_by_id = {
        replacement["after"]["node_id"]: replacement["before"]
        for replacement in NODE_REPLACEMENTS
    }
    after_edges_by_key = {
        _edge_key(replacement["after"]): replacement["before"]
        for replacement in EDGE_REPLACEMENTS
    }

    graph["nodes"] = [
        copy.deepcopy(after_nodes_by_id.get(node["node_id"], node))
        for node in graph["nodes"]
    ]
    graph["edges"] = [
        copy.deepcopy(after_edges_by_key.get(_edge_key(edge), edge))
        for edge in graph["edges"]
    ]
    existing_edge_keys = {_edge_key(edge) for edge in graph["edges"]}
    graph["edges"].extend(
        copy.deepcopy(edge)
        for edge in EDGE_REMOVALS
        if _edge_key(edge) not in existing_edge_keys
    )
    return doc


def _transform_from_before() -> dict:
    doc = _before()

    assert transform(SLUG, doc)
    return doc


def _has_curation_event(doc: dict, action: str, timestamp: str) -> bool:
    return any(
        event.get("action") == action and event.get("timestamp") == timestamp
        for event in doc["curation_history"]
    )


def test_review_adds_snippets_and_removes_backwards_membrane_edge():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}

    assert _has_curation_event(doc, ACTION, TIMESTAMP)
    assert nodes["unsaturated_fatty_acid_content"]["node_type"] == "QUALITY"
    assert "translation_under_cold" not in nodes
    assert "large_ribosomal_subunit_biogenesis" in nodes
    assert all(_edge_key(edge) not in by_key for edge in EDGE_REMOVALS)

    for replacement in EDGE_REPLACEMENTS:
        expected = replacement["after"]
        assert by_key[_edge_key(expected)] == expected
        assert all(item.get("reference") and item.get("snippet") for item in expected["evidence"])


def test_repaired_record_is_exactly_idempotent():
    doc = _transform_from_before()
    before = copy.deepcopy(doc)

    assert not transform(SLUG, doc)
    assert doc == before


def test_refuses_source_node_drift_before_migration():
    doc = _before()
    graph = doc["causal_graphs"][0]
    node_id = NODE_REPLACEMENTS[0]["before"]["node_id"]
    next(node for node in graph["nodes"] if node["node_id"] == node_id)["label"] = "drift"

    with pytest.raises(ValueError, match="source node drifted"):
        transform(SLUG, doc)


def test_refuses_source_edge_drift_before_migration():
    doc = _before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(EDGE_REPLACEMENTS[0]["before"])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="source edge drifted"):
        transform(SLUG, doc)


def test_refuses_removed_edge_drift_before_migration():
    doc = _before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(EDGE_REMOVALS[0])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="source edge drifted"):
        transform(SLUG, doc)


def test_refuses_migrated_node_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    node_id = NODE_REPLACEMENTS[0]["after"]["node_id"]
    next(node for node in graph["nodes"] if node["node_id"] == node_id)["node_type"] = (
        "CHEMICAL"
    )

    with pytest.raises(ValueError, match="migrated node drifted"):
        transform(SLUG, doc)


def test_refuses_migrated_edge_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(EDGE_REPLACEMENTS[0]["after"])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="migrated edge drifted"):
        transform(SLUG, doc)


def test_refuses_migrated_removed_edge_after_migration():
    doc = _transform_from_before()
    doc["causal_graphs"][0]["edges"].extend(copy.deepcopy(edge) for edge in EDGE_REMOVALS)

    with pytest.raises(ValueError, match="removed edge"):
        transform(SLUG, doc)


def test_refuses_partial_replay():
    doc = _before()
    graph = doc["causal_graphs"][0]
    replacement = EDGE_REPLACEMENTS[1]
    old_key = _edge_key(replacement["before"])
    graph["edges"] = [
        copy.deepcopy(replacement["after"]) if _edge_key(edge) == old_key else edge
        for edge in graph["edges"]
    ]

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)
