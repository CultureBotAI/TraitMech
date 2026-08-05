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
        "enables": ("RO:0002327", "RO", None, None),
        "causes": ("biolink:causes", "biolink", None, None),
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
    assert m == {"causes": ("biolink:causes", "biolink", None, None)}


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
    grounded, per_curie, residual, _blocked = ground_edges_in_doc(
        doc, {"enables": ("RO:0002327", "RO", None, None), "causes": ("biolink:causes", "biolink", None, None)}
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
    grounded, per_curie, _, _blocked = ground_edges_in_doc(doc, {"enables": ("RO:0002327", "RO", None, None)})
    assert grounded == 1, "only the empty predicate_id should be filled"
    edges = doc["causal_graphs"][0]["edges"]
    assert edges[0]["predicate_id"] == "RO:9999999", "existing CURIE not overwritten"
    assert edges[1]["predicate_id"] == "RO:0002327"


def test_ground_edges_idempotent_second_pass():
    doc = _doc_with_edges([{"subject": "a", "predicate": "enables", "object": "b"}])
    mapping = {"enables": ("RO:0002327", "RO", None, None)}
    ground_edges_in_doc(doc, mapping)
    grounded2, per2, residual2, _blocked2 = ground_edges_in_doc(doc, mapping)
    assert grounded2 == 0
    assert per2 == Counter()
    assert residual2 == Counter()


def test_ground_edges_residual_unmapped():
    doc = _doc_with_edges([
        {"subject": "a", "predicate": "supports", "object": "b"},
        {"subject": "c", "predicate": "manifests as", "object": "d"},
    ])
    grounded, _, residual, _blocked = ground_edges_in_doc(doc, {})
    assert grounded == 0
    assert residual == Counter({"supports": 1, "manifests as": 1})


def test_ground_edges_skips_edges_without_predicate():
    doc = _doc_with_edges([
        {"subject": "a", "object": "b"},  # no predicate at all
        {"subject": "c", "predicate": "", "object": "d"},  # empty
    ])
    grounded, _, residual, _blocked = ground_edges_in_doc(doc, {"enables": ("RO:0002327", "RO", None, None)})
    assert grounded == 0
    assert residual == Counter()


# ---------------------------------------------------- node-type constraints (#236)
#
# An exact label match is not sufficient to ground a predicate. `causally
# upstream of` IS the label of RO:0002411, and every corpus edge carrying it
# connects material entities — which RO's definition over occurrents forbids.
# The id↔label gate cannot see that: it compares a CURIE to its label and never
# looks at the edge. So the constraint lives beside the mapping and is enforced
# here (#235 is the mistake this exists to prevent).

PROC = frozenset({"BIOLOGICAL_PROCESS", "PATHWAY", "MOLECULAR_FUNCTION"})


def _typed_doc(s_type: str, o_type: str, predicate: str = "causally upstream of") -> dict:
    return {"causal_graphs": [{
        "nodes": [{"node_id": "a", "node_type": s_type},
                  {"node_id": "b", "node_type": o_type}],
        "edges": [{"subject": "a", "predicate": predicate, "object": "b"}],
    }]}


def test_edge_outside_the_declared_types_is_not_grounded():
    doc = _typed_doc("CHEMICAL", "CHEMICAL")
    grounded, _per, residual, blocked = ground_edges_in_doc(
        doc, {"causally upstream of": ("RO:0002411", "RO", PROC, PROC)})
    assert grounded == 0
    assert "predicate_id" not in doc["causal_graphs"][0]["edges"][0]
    assert blocked == Counter({("causally upstream of", "CHEMICAL->CHEMICAL"): 1})
    # Stays in the residual: a wrong grounding is worse than a missing one.
    assert residual == Counter({"causally upstream of": 1})


def test_edge_inside_the_declared_types_is_grounded():
    doc = _typed_doc("BIOLOGICAL_PROCESS", "PATHWAY")
    grounded, per_curie, residual, blocked = ground_edges_in_doc(
        doc, {"causally upstream of": ("RO:0002411", "RO", PROC, PROC)})
    assert grounded == 1
    assert per_curie == Counter({"RO:0002411": 1})
    assert residual == Counter() and blocked == Counter()


def test_blocked_key_survives_a_label_containing_a_parenthesis():
    """`positively influences (saturating)` is a real corpus label.

    Recovering the label by splitting the display string on " (" would truncate
    it to `positively influences`, so the residual TSV would mark the WRONG row
    blocked and leave the real one reading `unmapped`.
    """
    doc = _typed_doc("CHEMICAL", "CHEMICAL", predicate="positively influences (saturating)")
    _g, _p, _r, blocked = ground_edges_in_doc(
        doc, {"positively influences (saturating)": ("RO:9", "RO", PROC, PROC)})
    assert next(iter(blocked))[0] == "positively influences (saturating)"


def test_object_type_alone_can_block():
    doc = _typed_doc("BIOLOGICAL_PROCESS", "CHEMICAL")
    grounded, _per, _res, blocked = ground_edges_in_doc(
        doc, {"causally upstream of": ("RO:0002411", "RO", PROC, PROC)})
    assert grounded == 0
    assert next(iter(blocked)) == ("causally upstream of", "BIOLOGICAL_PROCESS->CHEMICAL")


def test_unconstrained_mapping_still_grounds_anything():
    """`*`/None must stay permissive — 99 existing rows rely on it."""
    doc = _typed_doc("CHEMICAL", "CAPACITY", predicate="enables")
    grounded, _per, _res, blocked = ground_edges_in_doc(
        doc, {"enables": ("RO:0002327", "RO", None, None)})
    assert grounded == 1 and blocked == Counter()


def test_missing_node_type_is_blocked_by_a_constraint():
    """A node with no declared type cannot be shown to satisfy the domain."""
    doc = {"causal_graphs": [{
        "nodes": [{"node_id": "a"}, {"node_id": "b"}],
        "edges": [{"subject": "a", "predicate": "causally upstream of", "object": "b"}],
    }]}
    grounded, _per, _res, blocked = ground_edges_in_doc(
        doc, {"causally upstream of": ("RO:0002411", "RO", PROC, PROC)})
    assert grounded == 0 and sum(blocked.values()) == 1


def test_load_mapping_parses_type_columns(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\ttarget_curie\ttarget_label\tsource\tconfidence\tsubject_types\tobject_types\tnotes",
        "upstream\tRO:0002411\tcausally upstream of\tRO\thigh\tBIOLOGICAL_PROCESS|PATHWAY\tPATHWAY\t",
        "loose\tRO:0002327\tenables\tRO\thigh\t*\t\t",
    ])
    m = load_mapping(p)
    assert m["upstream"] == ("RO:0002411", "RO",
                            frozenset({"BIOLOGICAL_PROCESS", "PATHWAY"}),
                            frozenset({"PATHWAY"}))
    # `*` and empty both mean "any", so old rows keep working unchanged.
    assert m["loose"] == ("RO:0002327", "RO", None, None)


def test_none_sentinel_parses_to_the_empty_set(tmp_path):
    """`NONE` is distinct from `*`/empty — no node type satisfies the domain."""
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\ttarget_curie\ttarget_label\tsource\tconfidence\tsubject_types\tobject_types\tnotes",
        "uses electron donor\tMETPO:2000009\tuses as electron donor\tMETPO\thigh\tNONE\t*\t",
    ])
    m = load_mapping(p)
    assert m["uses electron donor"] == ("METPO:2000009", "METPO", frozenset(), None)


@pytest.mark.parametrize("node_type", ["TRAIT", "CHEMICAL", "BIOLOGICAL_PROCESS"])
def test_none_sentinel_blocks_every_subject_type(node_type):
    """METPO:2000009 needs an organism subject and no such node type exists (#295)."""
    doc = _typed_doc(node_type, "CHEMICAL", predicate="uses electron donor")
    grounded, _per, _res, blocked = ground_edges_in_doc(
        doc, {"uses electron donor": ("METPO:2000009", "METPO", frozenset(), None)})
    assert grounded == 0 and sum(blocked.values()) == 1


def test_sentinel_colliding_with_a_real_node_type_is_fatal(tmp_path, monkeypatch):
    """A schema gaining a NONE member would let the sentinel shadow it silently."""
    import ground_causal_predicates as gcp

    schema = tmp_path / "schema.yaml"
    schema.write_text(
        "enums:\n"
        "  CausalNodeTypeEnum:\n"
        "    permissible_values:\n"
        "      TRAIT:\n"
        "      NONE:\n"
    )
    monkeypatch.setattr(gcp, "SCHEMA_PATH", schema)
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\ttarget_curie\ttarget_label\tsource\tconfidence\tsubject_types\tobject_types\tnotes",
        "x\tRO:1\tx\tRO\thigh\tTRAIT\t*\t",
    ])
    with pytest.raises(ValueError, match="collides with the sentinel"):
        gcp.load_mapping(p)


def test_unknown_node_type_name_is_fatal(tmp_path):
    """A typo in the constraint would silently block everything or nothing.

    A constraint nobody can see is worse than no constraint, so an unknown
    CausalNodeTypeEnum value raises rather than warning.
    """
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\ttarget_curie\ttarget_label\tsource\tconfidence\tsubject_types\tobject_types\tnotes",
        "x\tRO:1\tx\tRO\thigh\tBIOLOGICAL_PROCES\t*\t",
    ])
    with pytest.raises(ValueError, match="BIOLOGICAL_PROCES"):
        load_mapping(p)
