"""Regression tests for the ring_shaped review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_ring_shaped_graph_183 import (  # noqa: E402
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


def test_review_adds_snippets_and_grounds_ring_shaped_edges():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}
    changed_keys = {
        _edge_key(replacement["before"])
        for replacement in EDGE_REPLACEMENTS
        if _edge_key(replacement["before"]) != _edge_key(replacement["after"])
    }

    assert doc["curation_history"][-1]["action"] == ACTION
    assert nodes["bactofilin_lmdc_module"]["node_type"] == "PATHWAY"
    assert "grounding_status" not in nodes["bactofilin_lmdc_module"]
    assert "grounding_notes" not in nodes["bactofilin_lmdc_module"]
    assert changed_keys.isdisjoint(by_key)

    for replacement in EDGE_REPLACEMENTS:
        expected = replacement["after"]
        assert by_key[_edge_key(expected)] == expected
        assert all(item.get("reference") and item.get("snippet") for item in expected["evidence"])
        assert all("..." not in item["snippet"] for item in expected["evidence"])


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


def test_refuses_migrated_node_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    node_id = NODE_REPLACEMENTS[0]["after"]["node_id"]
    next(node for node in graph["nodes"] if node["node_id"] == node_id)["node_type"] = (
        "GENE_OR_PROTEIN"
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


def test_refuses_partial_replay():
    doc = _before()
    graph = doc["causal_graphs"][0]
    replacement = EDGE_REPLACEMENTS[0]
    old_key = _edge_key(replacement["before"])
    graph["edges"] = [
        copy.deepcopy(replacement["after"]) if _edge_key(edge) == old_key else edge
        for edge in graph["edges"]
    ]

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)
