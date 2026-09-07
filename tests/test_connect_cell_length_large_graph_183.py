"""Regression tests for the cell_length_large morphology repair in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from connect_cell_length_large_graph_183 import (  # noqa: E402
    ACTION,
    ADDITIONS,
    EDGE_REPLACEMENTS,
    EXPECTED_COMPONENTS,
    GRAPH_METADATA_AFTER,
    GRAPH_METADATA_BEFORE,
    SLUG,
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
    graph.update(GRAPH_METADATA_BEFORE)

    before_by_after_key = {
        _edge_key(replacement["after"]): replacement["before"] for replacement in EDGE_REPLACEMENTS
    }
    addition_keys = {_edge_key(edge) for edge in ADDITIONS}

    graph["edges"] = [
        copy.deepcopy(before_by_after_key.get(_edge_key(edge), edge))
        for edge in graph["edges"]
        if _edge_key(edge) not in addition_keys
    ]
    return doc


def _transform_from_before() -> dict:
    doc = _before()
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS

    assert transform(SLUG, doc)
    return doc


def test_repair_reaches_one_component_with_exact_snippet_backed_edges():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]

    assert _components(graph) == 1
    assert {field: graph[field] for field in GRAPH_METADATA_AFTER} == GRAPH_METADATA_AFTER

    by_key = {_edge_key(edge): edge for edge in graph["edges"]}
    old_keys = {_edge_key(replacement["before"]) for replacement in EDGE_REPLACEMENTS}
    assert not (set(by_key) & old_keys)

    for replacement in EDGE_REPLACEMENTS:
        expected = replacement["after"]
        assert by_key[_edge_key(expected)] == expected
        assert all(item.get("reference") and item.get("snippet") for item in expected["evidence"])
    for expected in ADDITIONS:
        assert by_key[_edge_key(expected)] == expected
        assert all(item.get("reference") and item.get("snippet") for item in expected["evidence"])
    assert doc["curation_history"][-1]["action"] == ACTION


def test_repaired_record_is_exactly_idempotent():
    doc = _transform_from_before()
    before = copy.deepcopy(doc)

    assert not transform(SLUG, doc)
    assert doc == before


def test_refuses_source_edge_drift_before_migration():
    doc = _before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(EDGE_REPLACEMENTS[0]["before"])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="source connector drifted"):
        transform(SLUG, doc)


def test_refuses_connector_metadata_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(ADDITIONS[0])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="migrated connector drifted"):
        transform(SLUG, doc)


def test_refuses_graph_metadata_drift_after_migration():
    doc = _transform_from_before()
    doc["causal_graphs"][0]["title"] = "drift"

    with pytest.raises(ValueError, match="migrated graph metadata drifted"):
        transform(SLUG, doc)


def test_refuses_partial_replay():
    doc = _before()
    graph = doc["causal_graphs"][0]
    new_edge = EDGE_REPLACEMENTS[0]["after"]
    old_key = _edge_key(EDGE_REPLACEMENTS[0]["before"])
    graph["edges"] = [
        copy.deepcopy(new_edge) if _edge_key(edge) == old_key else edge for edge in graph["edges"]
    ]

    with pytest.raises(ValueError, match="partial connector replay"):
        transform(SLUG, doc)
