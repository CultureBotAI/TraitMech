"""Tests for the discussion-anchor audit (#409).

The audit exists because `attaches_to` is free-form, so a migration that renames
a node can orphan an anchor with nothing complaining. These tests pin the three
defects and -- more importantly -- pin that an unknown SECTION stays a warning,
since the free-form design means this script will meet sections it has never
seen and must not fail them.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit_discussion_anchors import ERRORS, anchor_rows, causal_graph_anchors  # noqa: E402


def _doc(anchors: list[str], *, nodes: list[str] | None = None) -> dict:
    return {
        "causal_graphs": [
            {
                "graph_id": "g1",
                "nodes": [{"node_id": n} for n in (nodes if nodes is not None else ["real_node"])],
            }
        ],
        "discussions": [{"discussion_id": "d1", "prompt": "?", "attaches_to": anchors}],
    }


def test_resolving_anchor_is_clean():
    assert anchor_rows([("f.yaml", _doc(["causal_graphs#real_node"]))]) == []


def test_graph_id_is_a_valid_anchor():
    """A discussion about a whole mechanism anchors to the graph, not a node."""
    assert anchor_rows([("f.yaml", _doc(["causal_graphs#g1"]))]) == []


def test_unresolved_node_is_an_error():
    rows = anchor_rows([("f.yaml", _doc(["causal_graphs#renamed_away"]))])
    assert [r[2] for r in rows] == ["UNRESOLVED_ANCHOR"]
    assert rows[0][2] in ERRORS


def test_missing_hash_is_malformed():
    rows = anchor_rows([("f.yaml", _doc(["just_a_node_id"]))])
    assert [r[2] for r in rows] == ["MALFORMED_ANCHOR"]
    assert rows[0][2] in ERRORS


def test_unknown_section_warns_rather_than_fails():
    """Free-form by design: an unseen section is not the mistake we are catching."""
    rows = anchor_rows([("f.yaml", _doc(["composition#ingredient_x"]))])
    assert [r[2] for r in rows] == ["UNKNOWN_ANCHOR_SECTION"]
    assert rows[0][2] not in ERRORS


def test_record_without_graphs_cannot_resolve_a_graph_anchor():
    """Guards the empty-set case: no graphs must not mean every anchor passes."""
    doc = {"discussions": [{"discussion_id": "d1", "attaches_to": ["causal_graphs#anything"]}]}
    assert [r[2] for r in anchor_rows([("f.yaml", doc)])] == ["UNRESOLVED_ANCHOR"]


def test_causal_graph_anchors_collects_nodes_and_graph_ids():
    assert causal_graph_anchors(_doc([], nodes=["a", "b"])) == {"g1", "a", "b"}


def test_corpus_anchors_all_resolve():
    """The real corpus: every anchor the curation pass wrote must resolve."""
    errors = [r for r in anchor_rows() if r[2] in ERRORS]
    assert errors == [], f"unresolved discussion anchors: {errors}"
