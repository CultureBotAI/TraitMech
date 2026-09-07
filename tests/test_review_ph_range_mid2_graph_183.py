"""Regression tests for the pH-range-mid2 environment review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_ph_range_mid2_graph_183 import (  # noqa: E402
    ACTION,
    EDGE_REPLACEMENTS,
    NODE_REMOVALS,
    NODE_REPLACEMENTS,
    SLUG,
    _edge_key,
    _node_key,
    transform,
)


def _current() -> dict:
    path = ROOT / "data" / "traits" / f"{SLUG}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before() -> dict:
    doc = _current()
    graph = doc["causal_graphs"][0]
    after_edge_by_key = {
        _edge_key(replacement["after"]): replacement["before"] for replacement in EDGE_REPLACEMENTS
    }
    after_node_by_key = {
        _node_key(replacement["after"]): replacement["before"] for replacement in NODE_REPLACEMENTS
    }
    removed_by_key = {_node_key(node): node for node in NODE_REMOVALS}

    graph["nodes"] = [
        copy.deepcopy(after_node_by_key.get(_node_key(node), node)) for node in graph["nodes"]
    ]
    graph["nodes"].extend(copy.deepcopy(node) for node in removed_by_key.values())
    graph["edges"] = [
        copy.deepcopy(after_edge_by_key.get(_edge_key(edge), edge)) for edge in graph["edges"]
    ]
    return doc


def _transform_from_before() -> dict:
    doc = _before()

    assert transform(SLUG, doc)
    return doc


def test_review_adds_snippets_grounds_edges_and_fixes_nodes():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    edge_by_key = {_edge_key(edge): edge for edge in graph["edges"]}
    node_by_key = {_node_key(node): node for node in graph["nodes"]}

    assert doc["curation_history"][-1]["action"] == ACTION
    assert "cytoplasm" not in node_by_key
    assert node_by_key["membrane_potential"]["node_type"] == "STATE"
    assert {
        ("external_ph_7_8", "permits maintenance of", "cytoplasmic_ph_homeostasis"),
        ("cytoplasmic_buffering", "stabilizes", "cytoplasmic_ph_homeostasis"),
        ("na_h_antiport_activity", "acidifies", "cytoplasm"),
        ("proton_motive_force", "remains relatively constant across", "external_ph_5_8"),
        ("dpsi_dph_rebalancing", "maintains", "proton_motive_force"),
        ("f0f1_atpase", "couples", "atp_synthesis"),
        ("proton_ion_antiporters", "maintain", "membrane_potential"),
    }.isdisjoint(edge_by_key)

    for replacement in EDGE_REPLACEMENTS:
        expected = replacement["after"]
        assert edge_by_key[_edge_key(expected)] == expected
        assert all(item.get("reference") and item.get("snippet") for item in expected["evidence"])


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

    with pytest.raises(ValueError, match="source edge drifted"):
        transform(SLUG, doc)


def test_refuses_source_node_drift_before_migration():
    doc = _before()
    graph = doc["causal_graphs"][0]
    key = _node_key(NODE_REPLACEMENTS[0]["before"])
    next(node for node in graph["nodes"] if _node_key(node) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="source node drifted"):
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
    replacement = EDGE_REPLACEMENTS[1]
    old_key = _edge_key(replacement["before"])
    graph["edges"] = [
        copy.deepcopy(replacement["after"]) if _edge_key(edge) == old_key else edge
        for edge in graph["edges"]
    ]

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)
