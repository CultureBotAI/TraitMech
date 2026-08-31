"""Regression tests for the six metabolism pathway-spine repairs in #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from connect_metabolism_pathway_spines_183 import (  # noqa: E402
    ACTION,
    ADDITIONS,
    EXPECTED_COMPONENTS,
    _components,
    _edge_key,
    transform,
)


def _current(slug: str) -> dict:
    return yaml.safe_load((ROOT / "data" / "traits" / f"{slug}.yaml").read_text())


def _before(slug: str) -> dict:
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    keys = {_edge_key(edge) for edge in ADDITIONS[slug]}
    graph["edges"] = [edge for edge in graph["edges"] if _edge_key(edge) not in keys]
    return doc


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_reaches_one_component_with_exact_evidence(slug: str):
    doc = _before(slug)
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS[slug]
    assert transform(slug, doc)
    graph = doc["causal_graphs"][0]
    assert _components(graph) == 1
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}
    for edge in ADDITIONS[slug]:
        assert by_key[_edge_key(edge)] == edge
        assert all(item.get("reference") and item.get("snippet") for item in edge["evidence"])
    assert any(event["action"] == ACTION for event in doc["curation_history"])


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repaired_record_is_exactly_idempotent(slug: str):
    doc = _current(slug)
    before = copy.deepcopy(doc)
    assert not transform(slug, doc)
    assert doc == before


def test_refuses_connector_metadata_drift():
    slug = "metabolism/oxygenic_photosynthesis"
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    key = _edge_key(ADDITIONS[slug][0])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"
    with pytest.raises(ValueError, match="connector drifted"):
        transform(slug, doc)
