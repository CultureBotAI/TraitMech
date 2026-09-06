"""Regression tests for the genomic_island review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_genomic_island_graph_183 import (  # noqa: E402
    ACTION,
    EDGE_REPLACEMENTS,
    NODE_REPLACEMENTS,
    RECORD_EVIDENCE_REPLACEMENTS,
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
    after_record_evidence = {
        tuple(sorted(replacement["after"].items())): replacement["before"]
        for replacement in RECORD_EVIDENCE_REPLACEMENTS
    }
    after_nodes_by_id = {
        replacement["after"]["node_id"]: replacement["before"] for replacement in NODE_REPLACEMENTS
    }
    after_edges_by_key = {
        _edge_key(replacement["after"]): replacement["before"] for replacement in EDGE_REPLACEMENTS
    }

    doc["evidence"] = [
        copy.deepcopy(after_record_evidence.get(tuple(sorted(item.items())), item))
        for item in doc["evidence"]
    ]
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


def test_review_adds_snippets_and_grounds_genomic_island_edges():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}

    assert doc["curation_history"][-1]["action"] == ACTION
    assert all("snippet" in evidence for evidence in doc["evidence"])
    assert nodes["integrative_conjugative_element"]["node_type"] == "GENETIC_ELEMENT"
    assert nodes["integrative_mobilizable_element"]["node_type"] == "GENETIC_ELEMENT"
    assert nodes["conjugation"]["grounding"] == "GO:0009291"
    assert {
        ("gi_trait", "carries", "mobility_module"),
        ("integrative_conjugative_element", "disseminates by", "conjugation"),
        ("integrative_conjugative_element", "requires", "type_iv_secretion_system"),
        ("integrative_mobilizable_element", "uses", "conjugation"),
    }.isdisjoint(by_key)

    for replacement in EDGE_REPLACEMENTS:
        expected = replacement["after"]
        assert by_key[_edge_key(expected)] == expected
        assert all(item.get("reference") and item.get("snippet") for item in expected["evidence"])


def test_repaired_record_is_exactly_idempotent():
    doc = _transform_from_before()
    before = copy.deepcopy(doc)

    assert not transform(SLUG, doc)
    assert doc == before


def test_refuses_source_record_evidence_drift_before_migration():
    doc = _before()
    doc["evidence"][0]["notes"] = "drift"

    with pytest.raises(ValueError, match="missing source record evidence"):
        transform(SLUG, doc)


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


def test_refuses_migrated_edge_drift_after_migration():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    key = _edge_key(EDGE_REPLACEMENTS[2]["after"])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="migrated edge drifted"):
        transform(SLUG, doc)


def test_refuses_partial_replay():
    doc = _before()
    graph = doc["causal_graphs"][0]
    replacement = EDGE_REPLACEMENTS[2]
    old_key = _edge_key(replacement["before"])
    graph["edges"] = [
        copy.deepcopy(replacement["after"]) if _edge_key(edge) == old_key else edge
        for edge in graph["edges"]
    ]

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)
