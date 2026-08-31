"""Regression tests for the five trophic physiology repairs in #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from connect_trophic_physiology_graphs_183 import (  # noqa: E402
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
    keys = {_edge_key(edge) for edge in ADDITIONS[slug]}
    graph = doc["causal_graphs"][0]
    graph["edges"] = [edge for edge in graph["edges"] if _edge_key(edge) not in keys]
    return doc


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_reaches_one_component(slug: str):
    doc = _before(slug)
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS[slug]
    assert transform(slug, doc)
    assert _components(doc["causal_graphs"][0]) == 1
    assert doc["curation_history"][-1]["action"] == ACTION


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_is_exactly_idempotent(slug: str):
    doc = _current(slug)
    before = copy.deepcopy(doc)
    assert not transform(slug, doc)
    assert doc == before


def test_refuses_alternate_connected_state():
    slug = "physiology/autotrophic"
    doc = _before(slug)
    alternate = copy.deepcopy(ADDITIONS[slug][0])
    alternate["predicate"] = "supplies substrate to"
    doc["causal_graphs"][0]["edges"].append(alternate)
    with pytest.raises(ValueError, match="connected graph does not match exact migration state"):
        transform(slug, doc)


def test_refuses_connector_drift():
    slug = "physiology/oxidase_activity"
    doc = _current(slug)
    key = _edge_key(ADDITIONS[slug][0])
    next(edge for edge in doc["causal_graphs"][0]["edges"] if _edge_key(edge) == key)["description"] = "drift"
    with pytest.raises(ValueError, match="connector drifted"):
        transform(slug, doc)
