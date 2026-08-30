"""Tests for the #183 lithotrophic graph repair."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from connect_lithotrophic_graph import (  # noqa: E402
    ACTION,
    NEW_EDGES,
    TARGET_GRAPH,
    TARGET_IDENTIFIER,
    transform,
)


def _doc() -> dict:
    node_ids = sorted(
        {
            endpoint
            for edge in NEW_EDGES
            for endpoint in (edge["subject"], edge["object"])
        }
    )
    return {
        "identifier": TARGET_IDENTIFIER,
        "causal_graphs": [
            {
                "graph_id": TARGET_GRAPH,
                "nodes": [{"node_id": node_id} for node_id in node_ids],
                "edges": [],
            }
        ],
    }


def test_adds_six_grounded_snippet_backed_edges():
    doc = _doc()

    assert transform(doc)

    edges = doc["causal_graphs"][0]["edges"]
    assert edges == list(NEW_EDGES)
    assert all(edge["predicate_id"] for edge in edges)
    assert all(edge["evidence"][0]["snippet"] for edge in edges)
    assert doc["curation_history"][-1]["action"] == ACTION


def test_is_idempotent_after_exact_replay():
    doc = _doc()
    assert transform(doc)

    assert not transform(doc)


def test_refuses_partial_replay():
    doc = _doc()
    doc["causal_graphs"][0]["edges"].append(copy.deepcopy(NEW_EDGES[0]))

    with pytest.raises(ValueError, match="only some connecting edges"):
        transform(doc)


def test_refuses_to_overwrite_changed_edge():
    doc = _doc()
    changed = copy.deepcopy(NEW_EDGES[0])
    changed["description"] = "changed"
    doc["causal_graphs"][0]["edges"].append(changed)

    with pytest.raises(ValueError, match="refusing to overwrite"):
        transform(doc)
