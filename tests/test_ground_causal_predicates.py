"""Unit tests for scripts/ground_causal_predicates.py.

Locks in the idempotency contract (existing predicate_id never
overwritten), conflict detection (same label → different CURIEs
raises), and the residual-counting behavior.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from ground_causal_predicates import (  # noqa: E402
    ground_edges_in_doc,
    load_mapping,
)


# ---------------------------------------------------------------- load_mapping


def _write_tsv(path: Path, rows: list[str]) -> None:
    path.write_text("\n".join(rows) + "\n")


def test_load_mapping_basic(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\ttarget_curie\ttarget_label\tsource\tconfidence\tnotes",
        "enables\tRO:0002327\tenables\tRO\thigh\t",
        "causes\tbiolink:causes\tcauses\tbiolink\thigh\t",
    ])
    m = load_mapping(p)
    assert m == {
        "enables": ("RO:0002327", "RO"),
        "causes": ("biolink:causes", "biolink"),
    }


def test_load_mapping_skips_incomplete_rows(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\ttarget_curie\ttarget_label\tsource\tconfidence\tnotes",
        "\tRO:0002327\tenables\tRO\thigh\t",      # missing label
        "enables\t\tenables\tRO\thigh\t",          # missing curie
        "causes\tbiolink:causes\tcauses\tbiolink\thigh\t",
    ])
    m = load_mapping(p)
    assert m == {"causes": ("biolink:causes", "biolink")}


def test_load_mapping_conflict_raises(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\ttarget_curie\ttarget_label\tsource\tconfidence\tnotes",
        "regulates\tRO:0002211\tregulates\tRO\thigh\t",
        "regulates\tbiolink:regulates\tregulates\tbiolink\thigh\t",
    ])
    with pytest.raises(ValueError, match="mapping conflict"):
        load_mapping(p)


def test_load_mapping_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_mapping(tmp_path / "does_not_exist.tsv")


# ---------------------------------------------------------------- ground_edges_in_doc


def _doc_with_edges(edges: list[dict]) -> dict:
    return {"causal_graphs": [{"edges": edges}]}


def test_ground_edges_basic():
    doc = _doc_with_edges([
        {"subject": "a", "predicate": "enables", "object": "b"},
        {"subject": "c", "predicate": "causes", "object": "d"},
    ])
    grounded, per_curie, residual = ground_edges_in_doc(
        doc, {"enables": ("RO:0002327", "RO"), "causes": ("biolink:causes", "biolink")}
    )
    assert grounded == 2
    assert per_curie == Counter({"RO:0002327": 1, "biolink:causes": 1})
    assert residual == Counter()
    edges = doc["causal_graphs"][0]["edges"]
    assert edges[0]["predicate_id"] == "RO:0002327"
    assert edges[1]["predicate_id"] == "biolink:causes"


def test_ground_edges_skips_existing_predicate_id():
    """Idempotency: a non-empty predicate_id must never be overwritten."""
    doc = _doc_with_edges([
        {"subject": "a", "predicate": "enables", "object": "b",
         "predicate_id": "RO:9999999"},
        {"subject": "c", "predicate": "enables", "object": "d"},  # ungrounded
    ])
    grounded, per_curie, _ = ground_edges_in_doc(doc, {"enables": ("RO:0002327", "RO")})
    assert grounded == 1, "only the empty predicate_id should be filled"
    edges = doc["causal_graphs"][0]["edges"]
    assert edges[0]["predicate_id"] == "RO:9999999", "existing CURIE not overwritten"
    assert edges[1]["predicate_id"] == "RO:0002327"


def test_ground_edges_idempotent_second_pass():
    doc = _doc_with_edges([{"subject": "a", "predicate": "enables", "object": "b"}])
    mapping = {"enables": ("RO:0002327", "RO")}
    ground_edges_in_doc(doc, mapping)
    grounded2, per2, residual2 = ground_edges_in_doc(doc, mapping)
    assert grounded2 == 0
    assert per2 == Counter()
    assert residual2 == Counter()


def test_ground_edges_residual_unmapped():
    doc = _doc_with_edges([
        {"subject": "a", "predicate": "supports", "object": "b"},
        {"subject": "c", "predicate": "manifests as", "object": "d"},
    ])
    grounded, _, residual = ground_edges_in_doc(doc, {})
    assert grounded == 0
    assert residual == Counter({"supports": 1, "manifests as": 1})


def test_ground_edges_skips_edges_without_predicate():
    doc = _doc_with_edges([
        {"subject": "a", "object": "b"},  # no predicate at all
        {"subject": "c", "predicate": "", "object": "d"},  # empty
    ])
    grounded, _, residual = ground_edges_in_doc(doc, {"enables": ("RO:0002327", "RO")})
    assert grounded == 0
    assert residual == Counter()
