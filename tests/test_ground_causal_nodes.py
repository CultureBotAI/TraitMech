"""Unit tests for scripts/ground_causal_nodes.py.

Locks in:
- (label, node_type) keying — same label, different types map to
  different CURIEs without aliasing.
- Header validation in load_mapping (G06 from PR #66 review).
- The grounded_keys-on-validation-failure behavior (the residual
  TSV must include nodes that were just grounded but then rolled
  back when the file failed validation).
- Idempotency: existing grounding never overwritten.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from ground_causal_nodes import (  # noqa: E402
    ground_nodes_in_doc,
    load_mapping,
)


# ---------------------------------------------------------------- load_mapping


def _write_tsv(path: Path, rows: list[str]) -> None:
    path.write_text("\n".join(rows) + "\n")


HDR = "label\tnode_type\ttarget_curie\ttarget_label\tsource\tconfidence\tnotes"


def test_load_mapping_basic(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        HDR,
        "molecular oxygen\tCHEMICAL\tCHEBI:15379\tdioxygen\tCHEBI\thigh\t",
        "photosynthesis\tBIOLOGICAL_PROCESS\tGO:0015979\tphotosynthesis\tGO\thigh\t",
    ])
    m = load_mapping(p)
    assert m == {
        ("molecular oxygen", "CHEMICAL"): ("CHEBI:15379", "CHEBI"),
        ("photosynthesis", "BIOLOGICAL_PROCESS"): ("GO:0015979", "GO"),
    }


def test_load_mapping_same_label_different_node_types(tmp_path):
    """The (label, node_type) key disambiguates context-dependent terms."""
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        HDR,
        "terminal electron acceptor\tCHEMICAL\tMETPO:1007504\tterminal electron acceptor\tMETPO\thigh\t",
        "terminal electron acceptor\tMOLECULAR_FUNCTION\tMETPO:1007504\tterminal electron acceptor\tMETPO\thigh\t",
    ])
    m = load_mapping(p)
    assert ("terminal electron acceptor", "CHEMICAL") in m
    assert ("terminal electron acceptor", "MOLECULAR_FUNCTION") in m
    assert len(m) == 2


def test_load_mapping_missing_required_header(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        "label\tnodetype\ttargetcurie\tsource",  # typo'd headers
        "x\tCHEMICAL\tCHEBI:1\tfoo",
    ])
    with pytest.raises(ValueError, match="missing required column"):
        load_mapping(p)


def test_load_mapping_conflict_raises(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        HDR,
        "molecular oxygen\tCHEMICAL\tCHEBI:15379\tdioxygen\tCHEBI\thigh\t",
        "molecular oxygen\tCHEMICAL\tCHEBI:99999\tbogus\tBOGUS\thigh\t",
    ])
    with pytest.raises(ValueError, match="mapping conflict"):
        load_mapping(p)


def test_load_mapping_skips_incomplete_rows(tmp_path):
    p = tmp_path / "m.tsv"
    _write_tsv(p, [
        HDR,
        "\tCHEMICAL\tCHEBI:1\tfoo\tCHEBI\thigh\t",  # missing label
        "x\t\tCHEBI:2\tfoo\tCHEBI\thigh\t",          # missing node_type
        "x\tCHEMICAL\t\tfoo\tCHEBI\thigh\t",         # missing curie
        "y\tCHEMICAL\tCHEBI:3\tfoo\tCHEBI\thigh\t",
    ])
    m = load_mapping(p)
    assert m == {("y", "CHEMICAL"): ("CHEBI:3", "CHEBI")}


def test_load_mapping_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_mapping(tmp_path / "nope.tsv")


# ---------------------------------------------------------------- ground_nodes_in_doc


def _doc_with_nodes(nodes: list[dict]) -> dict:
    return {"causal_graphs": [{"nodes": nodes}]}


def test_ground_nodes_basic():
    doc = _doc_with_nodes([
        {"node_id": "a", "label": "molecular oxygen", "node_type": "CHEMICAL"},
        {"node_id": "b", "label": "photosynthesis", "node_type": "BIOLOGICAL_PROCESS"},
    ])
    mapping = {
        ("molecular oxygen", "CHEMICAL"): ("CHEBI:15379", "CHEBI"),
        ("photosynthesis", "BIOLOGICAL_PROCESS"): ("GO:0015979", "GO"),
    }
    grounded, per_curie, residual, grounded_keys, _ = ground_nodes_in_doc(doc, mapping)
    assert grounded == 2
    assert per_curie == Counter({"CHEBI:15379": 1, "GO:0015979": 1})
    assert residual == Counter()
    assert grounded_keys == Counter({
        ("molecular oxygen", "CHEMICAL"): 1,
        ("photosynthesis", "BIOLOGICAL_PROCESS"): 1,
    })
    nodes = doc["causal_graphs"][0]["nodes"]
    assert nodes[0]["grounding"] == "CHEBI:15379"
    assert nodes[1]["grounding"] == "GO:0015979"


def test_ground_nodes_skips_existing_grounding():
    """Idempotency: existing grounding must never be overwritten."""
    doc = _doc_with_nodes([
        {"node_id": "a", "label": "molecular oxygen", "node_type": "CHEMICAL",
         "grounding": "CHEBI:99999"},
        {"node_id": "b", "label": "molecular oxygen", "node_type": "CHEMICAL"},
    ])
    mapping = {("molecular oxygen", "CHEMICAL"): ("CHEBI:15379", "CHEBI")}
    grounded, _, _, _, _ = ground_nodes_in_doc(doc, mapping)
    assert grounded == 1
    nodes = doc["causal_graphs"][0]["nodes"]
    assert nodes[0]["grounding"] == "CHEBI:99999"
    assert nodes[1]["grounding"] == "CHEBI:15379"


def test_ground_nodes_node_type_keyed_lookup():
    """A label without its node_type in the mapping stays ungrounded."""
    doc = _doc_with_nodes([
        {"node_id": "a", "label": "terminal electron acceptor",
         "node_type": "CHEMICAL"},
        {"node_id": "b", "label": "terminal electron acceptor",
         "node_type": "PATHWAY"},  # different node_type, not in mapping
    ])
    mapping = {
        ("terminal electron acceptor", "CHEMICAL"): ("METPO:1007504", "METPO"),
    }
    grounded, _, residual, _, _ = ground_nodes_in_doc(doc, mapping)
    assert grounded == 1
    assert residual == Counter({("terminal electron acceptor", "PATHWAY"): 1})


def test_ground_nodes_idempotent_second_pass():
    doc = _doc_with_nodes([
        {"node_id": "a", "label": "photosynthesis", "node_type": "BIOLOGICAL_PROCESS"},
    ])
    mapping = {("photosynthesis", "BIOLOGICAL_PROCESS"): ("GO:0015979", "GO")}
    ground_nodes_in_doc(doc, mapping)
    grounded2, _, residual2, grounded_keys2, _ = ground_nodes_in_doc(doc, mapping)
    assert grounded2 == 0
    assert residual2 == Counter()
    assert grounded_keys2 == Counter()


def test_ground_nodes_skips_nodes_without_label_or_type():
    doc = _doc_with_nodes([
        {"node_id": "a", "node_type": "CHEMICAL"},                  # no label
        {"node_id": "b", "label": "x"},                              # no node_type
        {"node_id": "c", "label": "", "node_type": "CHEMICAL"},      # empty label
    ])
    grounded, _, residual, _, _ = ground_nodes_in_doc(doc, {("x", "CHEMICAL"): ("X:1", "X")})
    assert grounded == 0
    assert residual == Counter()


def test_ground_nodes_grounded_keys_separable_from_residual():
    """grounded_keys is needed so a caller can re-classify just-grounded
    nodes back into residual if a downstream validation step rejects
    the file (Copilot fix from PR #66)."""
    doc = _doc_with_nodes([
        {"node_id": "a", "label": "molecular oxygen", "node_type": "CHEMICAL"},
        {"node_id": "b", "label": "unmapped thing", "node_type": "CHEMICAL"},
    ])
    mapping = {("molecular oxygen", "CHEMICAL"): ("CHEBI:15379", "CHEBI")}
    grounded, _, residual, grounded_keys, _ = ground_nodes_in_doc(doc, mapping)
    assert grounded == 1
    assert residual == Counter({("unmapped thing", "CHEMICAL"): 1})
    assert grounded_keys == Counter({("molecular oxygen", "CHEMICAL"): 1})
    # Caller can union residual + grounded_keys if rolling back a write.
    rolled_back_residual = residual + grounded_keys
    assert rolled_back_residual == Counter({
        ("molecular oxygen", "CHEMICAL"): 1,
        ("unmapped thing", "CHEMICAL"): 1,
    })


# ------------------------------------------------- duplicate-grounding guard (#361)


def test_ground_nodes_declines_curie_already_in_graph():
    """The exact shape #352 burned down by hand: a protein node and the
    function node it enables, where the mapping table sends the protein to
    the function's GO ACTIVITY term. Writing it would re-create the
    DUPLICATE_GROUNDING that audit-graphs reports."""
    doc = _doc_with_nodes([
        {"node_id": "catalase_function", "label": "catalase activity",
         "node_type": "MOLECULAR_FUNCTION", "grounding": "GO:0004096"},
        {"node_id": "catalase", "label": "catalase", "node_type": "GENE_OR_PROTEIN"},
    ])
    mapping = {("catalase", "GENE_OR_PROTEIN"): ("GO:0004096", "GO")}
    grounded, per_curie, residual, grounded_keys, declined = ground_nodes_in_doc(doc, mapping)

    assert grounded == 0
    assert per_curie == Counter()
    assert grounded_keys == Counter()
    assert declined == Counter({("catalase", "GENE_OR_PROTEIN", "GO:0004096"): 1})
    # Still ungrounded on disk, so it belongs in the residual report.
    assert residual == Counter({("catalase", "GENE_OR_PROTEIN"): 1})
    assert "grounding" not in doc["causal_graphs"][0]["nodes"][1]


def test_ground_nodes_declines_second_node_mapping_to_same_curie():
    """`taken` is updated as we go, not just seeded once -- otherwise two
    ungrounded nodes sharing a mapped CURIE would both take it and produce
    the duplicate this guard exists to prevent."""
    doc = _doc_with_nodes([
        {"node_id": "a", "label": "catalase", "node_type": "GENE_OR_PROTEIN"},
        {"node_id": "b", "label": "catalase (KatA)", "node_type": "GENE_OR_PROTEIN"},
    ])
    mapping = {
        ("catalase", "GENE_OR_PROTEIN"): ("GO:0004096", "GO"),
        ("catalase (kata)", "GENE_OR_PROTEIN"): ("GO:0004096", "GO"),
    }
    grounded, _, _, _, declined = ground_nodes_in_doc(doc, mapping)

    assert grounded == 1
    assert declined == Counter({("catalase (kata)", "GENE_OR_PROTEIN", "GO:0004096"): 1})
    nodes = doc["causal_graphs"][0]["nodes"]
    assert nodes[0]["grounding"] == "GO:0004096"
    assert "grounding" not in nodes[1]


def test_ground_nodes_guard_is_per_graph_not_per_record():
    """DUPLICATE_GROUNDING is scoped to one graph, so the same CURIE in a
    DIFFERENT graph of the same record is not a duplicate and must still be
    written -- otherwise the guard would suppress legitimate groundings."""
    doc = {"causal_graphs": [
        {"nodes": [{"node_id": "a", "label": "catalase activity",
                    "node_type": "MOLECULAR_FUNCTION", "grounding": "GO:0004096"}]},
        {"nodes": [{"node_id": "b", "label": "catalase",
                    "node_type": "GENE_OR_PROTEIN"}]},
    ]}
    mapping = {("catalase", "GENE_OR_PROTEIN"): ("GO:0004096", "GO")}
    grounded, _, _, _, declined = ground_nodes_in_doc(doc, mapping)

    assert grounded == 1
    assert declined == Counter()
    assert doc["causal_graphs"][1]["nodes"][0]["grounding"] == "GO:0004096"


def test_ground_nodes_guard_leaves_the_72_protein_shorthand_alone():
    """The mapping rows are NOT the defect: where a graph models the protein
    but not its function, protein -> GO activity is the corpus's accepted
    shorthand and must still be written (#361)."""
    doc = _doc_with_nodes([
        {"node_id": "catalase", "label": "catalase", "node_type": "GENE_OR_PROTEIN"},
        {"node_id": "h2o2", "label": "hydrogen peroxide", "node_type": "CHEMICAL",
         "grounding": "CHEBI:16240"},
    ])
    mapping = {("catalase", "GENE_OR_PROTEIN"): ("GO:0004096", "GO")}
    grounded, per_curie, _, _, declined = ground_nodes_in_doc(doc, mapping)

    assert grounded == 1
    assert declined == Counter()
    assert per_curie == Counter({"GO:0004096": 1})
    assert doc["causal_graphs"][0]["nodes"][0]["grounding"] == "GO:0004096"
