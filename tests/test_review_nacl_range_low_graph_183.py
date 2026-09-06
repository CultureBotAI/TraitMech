"""Regression tests for the NaCl-range-low review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_nacl_range_low_graph_183 import (  # noqa: E402
    ACTION,
    EDGE_REPLACEMENTS,
    NODE_REPLACEMENTS,
    SLUG,
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
        replacement["after"]["node_id"]: replacement["before"] for replacement in NODE_REPLACEMENTS
    }
    after_edges_by_key = {
        _edge_key(replacement["after"]): replacement["before"] for replacement in EDGE_REPLACEMENTS
    }

    graph["nodes"] = [
        copy.deepcopy(after_nodes_by_id.get(node["node_id"], node)) for node in graph["nodes"]
    ]
    graph["edges"] = [
        copy.deepcopy(after_edges_by_key.get(_edge_key(edge), edge)) for edge in graph["edges"]
    ]
    return doc


def _transform_from_before() -> dict:
    doc = _before()

    assert transform(SLUG, doc)
    return doc


def _has_curation_event(doc: dict, action: str) -> bool:
    return any(event.get("action") == action for event in doc["curation_history"])


def test_review_adds_snippets_and_repairs_nacl_range_low_graph():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    by_id = {node["node_id"]: node for node in graph["nodes"]}
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}

    assert graph["scope_status"] == "NONMECHANISTIC"
    assert _has_curation_event(doc, ACTION)

    for replacement in NODE_REPLACEMENTS:
        expected = replacement["after"]
        assert by_id[expected["node_id"]] == expected

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
    next(
        node
        for node in graph["nodes"]
        if node["node_id"] == NODE_REPLACEMENTS[0]["before"]["node_id"]
    )["description"] = "drift"

    with pytest.raises(ValueError, match="source node drifted"):
        transform(SLUG, doc)


def test_refuses_source_edge_drift_before_migration():
    doc = _before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(EDGE_REPLACEMENTS[0]["before"])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="source edge drifted"):
        transform(SLUG, doc)


def test_refuses_migrated_node_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    node_id = NODE_REPLACEMENTS[0]["after"]["node_id"]
    next(node for node in graph["nodes"] if node["node_id"] == node_id)["description"] = "drift"

    with pytest.raises(ValueError, match="migrated node drifted"):
        transform(SLUG, doc)


def test_refuses_migrated_edge_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(EDGE_REPLACEMENTS[0]["after"])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="migrated edge drifted"):
        transform(SLUG, doc)


def test_refuses_partial_replay():
    doc = _before()
    graph = doc["causal_graphs"][0]
    replacement = EDGE_REPLACEMENTS[2]
    graph["edges"] = [
        copy.deepcopy(replacement["after"]) if edge == replacement["before"] else edge
        for edge in graph["edges"]
    ]

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)
