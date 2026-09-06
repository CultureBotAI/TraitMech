"""Regression tests for the temperature-optimum-very-low review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_temperature_optimum_very_low_graph_183 import (  # noqa: E402
    ACTION,
    EDGE_REPLACEMENTS,
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
    after_by_key = {
        _edge_key(replacement["after"]): replacement["before"] for replacement in EDGE_REPLACEMENTS
    }

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


def test_review_adds_snippets_and_grounds_psychrophile_edges():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}

    assert _has_curation_event(doc, ACTION, TIMESTAMP)
    assert {
        ("fatty_acid_desaturase_activity", "increases abundance of", "unsaturated_fatty_acids"),
        ("unsaturated_fatty_acids", "maintains", "membrane_fluidity"),
        ("membrane_fluidity", "supports", "psychrophile_machinery"),
        ("cold_shock_proteins", "supports", "translation_low_temperature"),
        ("glycine_betaine", "stabilizes", "protein_membrane_stabilization"),
        ("trehalose", "acts as", "cryoprotection"),
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
    key = _edge_key(EDGE_REPLACEMENTS[1]["after"])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="migrated edge drifted"):
        transform(SLUG, doc)


def test_refuses_partial_replay():
    doc = _before()
    graph = doc["causal_graphs"][0]
    replacement = EDGE_REPLACEMENTS[5]
    old_key = _edge_key(replacement["before"])
    graph["edges"] = [
        copy.deepcopy(replacement["after"]) if _edge_key(edge) == old_key else edge
        for edge in graph["edges"]
    ]

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)
