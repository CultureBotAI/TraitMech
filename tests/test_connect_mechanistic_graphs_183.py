"""Regression tests for the first post-scope #183 content tranche."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from connect_mechanistic_graphs_183 import (  # noqa: E402
    ACTION,
    ADDITIONS,
    REMOVALS,
    _components,
    _edge_key,
    transform,
)


def _current(slug: str) -> dict:
    path = ROOT / "data" / "traits" / f"{slug}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before_additions(slug: str) -> dict:
    doc = _current(slug)
    keys = {_edge_key(edge) for edge in ADDITIONS[slug]}
    graph = doc["causal_graphs"][0]
    graph["edges"] = [edge for edge in graph["edges"] if _edge_key(edge) not in keys]
    return doc


def _before_restriction_removal() -> dict:
    slug = "genomics/restriction_modification_system"
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    graph["nodes"].extend([
        {
            "node_id": "type_iv_restriction_enzyme",
            "label": "type IV restriction enzyme",
            "node_type": "GENE_OR_PROTEIN",
        },
        {
            "node_id": "methylated_dna_motif",
            "label": "methylated DNA motif",
            "node_type": "CHEMICAL",
        },
    ])
    graph["edges"].append({
        "subject": "type_iv_restriction_enzyme",
        "predicate": "cleaves",
        "object": "methylated_dna_motif",
        "evidence": [{"reference": "DOI:10.3390/microorganisms11122962"}],
    })
    return doc


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_adds_only_snippet_backed_connectors_and_connects_graph(slug: str):
    doc = _before_additions(slug)
    assert _components(doc["causal_graphs"][0]) > 1

    assert transform(slug, doc)

    graph = doc["causal_graphs"][0]
    assert _components(graph) == 1
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}
    for expected in ADDITIONS[slug]:
        actual = by_key[_edge_key(expected)]
        assert actual == expected
        assert all(item.get("reference") and item.get("snippet") for item in actual["evidence"])
    assert doc["curation_history"][-1]["action"] == ACTION


def test_removes_only_the_out_of_scope_type_iv_island():
    slug = "genomics/restriction_modification_system"
    doc = _before_restriction_removal()
    assert _components(doc["causal_graphs"][0]) == 2

    assert transform(slug, doc)

    graph = doc["causal_graphs"][0]
    assert _components(graph) == 1
    assert not (REMOVALS[slug]["nodes"] & {node["node_id"] for node in graph["nodes"]})
    assert not (REMOVALS[slug]["edges"] & {_edge_key(edge) for edge in graph["edges"]})


@pytest.mark.parametrize("slug", sorted(set(ADDITIONS) | set(REMOVALS)))
def test_is_idempotent_on_the_repaired_record(slug: str):
    doc = _current(slug)
    before = copy.deepcopy(doc)

    assert not transform(slug, doc)
    assert doc == before


def test_refuses_partial_connector_replay():
    slug = "ecology/biofilm_formation"
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    graph["edges"] = [
        edge for edge in graph["edges"]
        if _edge_key(edge) != _edge_key(ADDITIONS[slug][0])
    ]

    with pytest.raises(ValueError, match="partial replay"):
        transform(slug, doc)
