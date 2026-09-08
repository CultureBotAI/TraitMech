"""Regression tests for the pH numerical-limits environment review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_ph_phenotype_graph_183 import (  # noqa: E402
    ACTION,
    EDGE_REPLACEMENTS,
    RECORD_EVIDENCE_AFTER,
    RECORD_EVIDENCE_BEFORE,
    SLUG,
    TIMESTAMP,
    _edge_key,
    transform,
)  # noqa: E402


def _current() -> dict:
    path = ROOT / "data" / "traits" / f"{SLUG}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before() -> dict:
    doc = _current()
    graph = doc["causal_graphs"][0]
    after_by_key = {
        _edge_key(replacement["after"]): replacement["before"] for replacement in EDGE_REPLACEMENTS
    }

    doc["evidence"] = copy.deepcopy(RECORD_EVIDENCE_BEFORE)
    graph["edges"] = [
        copy.deepcopy(after_by_key.get(_edge_key(edge), edge)) for edge in graph["edges"]
    ]
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


def test_review_adds_snippets_and_grounds_ph_axis_edges():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}

    assert doc["evidence"] == RECORD_EVIDENCE_AFTER
    assert _has_curation_event(doc, ACTION, TIMESTAMP)
    assert {
        ("external_ph_axis", "determines", "proton_motive_force"),
        ("phosphate_buffering", "stabilizes", "internal_ph"),
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

    with pytest.raises(ValueError, match="source record evidence drifted"):
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
