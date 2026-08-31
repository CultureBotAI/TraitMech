"""Regression tests for the eight two-component metabolism graphs in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from connect_metabolism_two_component_graphs_183 import (  # noqa: E402
    ACTION,
    ADDITIONS,
    EXPECTED_COMPONENTS,
    _components,
    _edge_key,
    transform,
)


def _current(slug: str) -> dict:
    path = ROOT / "data" / "traits" / f"{slug}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before(slug: str) -> dict:
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    new_keys = {_edge_key(edge) for edge in ADDITIONS[slug]}
    graph["edges"] = [
        edge for edge in graph["edges"] if _edge_key(edge) not in new_keys
    ]
    return doc


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_reaches_one_component_with_exact_snippet_backed_edge(slug: str):
    doc = _before(slug)
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS[slug]

    assert transform(slug, doc)

    graph = doc["causal_graphs"][0]
    assert _components(graph) == 1
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}
    for expected in ADDITIONS[slug]:
        assert by_key[_edge_key(expected)] == expected
        assert all(
            item.get("reference") and item.get("snippet")
            for item in expected["evidence"]
        )
    assert doc["curation_history"][-1]["action"] == ACTION


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repaired_record_is_exactly_idempotent(slug: str):
    doc = _current(slug)
    before = copy.deepcopy(doc)

    assert not transform(slug, doc)
    assert doc == before


def test_refuses_connector_metadata_drift_after_migration():
    slug = "metabolism/respiration"
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    key = _edge_key(ADDITIONS[slug][0])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)[
        "description"
    ] = "drift"

    with pytest.raises(ValueError, match="connector drifted"):
        transform(slug, doc)
