"""Regression tests for the final ten metabolism graph repairs in #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from connect_final_metabolism_graphs_183 import (  # noqa: E402
    ACTION,
    ADDITIONS,
    EXPECTED_COMPONENTS,
    _components,
    _edge_key,
    transform,
)


def current(slug: str) -> dict:
    return yaml.safe_load((ROOT / "data" / "traits" / f"{slug}.yaml").read_text())


def before(slug: str) -> dict:
    doc = current(slug)
    keys = {_edge_key(item) for item in ADDITIONS[slug]}
    graph = doc["causal_graphs"][0]
    graph["edges"] = [item for item in graph["edges"] if _edge_key(item) not in keys]
    return doc


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_reaches_one_component(slug: str):
    doc = before(slug)
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS[slug]
    assert transform(slug, doc)
    assert _components(doc["causal_graphs"][0]) == 1
    assert doc["curation_history"][-1]["action"] == ACTION


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_is_idempotent(slug: str):
    doc = current(slug)
    snapshot = copy.deepcopy(doc)
    assert not transform(slug, doc)
    assert doc == snapshot


def test_refuses_partial_replay():
    slug = "metabolism/iron_oxidation"
    doc = before(slug)
    doc["causal_graphs"][0]["edges"].append(copy.deepcopy(ADDITIONS[slug][0]))
    with pytest.raises(ValueError, match="partial connector replay"):
        transform(slug, doc)
