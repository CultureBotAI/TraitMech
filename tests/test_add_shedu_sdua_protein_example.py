"""Exercise the Shedu SduA protein-example writer offline and on temp copies.

The writer edits an existing record, so the base it is applied to is derived
from the committed record by removing exactly what the writer adds: the
``sdua_immune_nuclease`` node, its one edge, and its one curation event. Every
write goes to a temporary copy; the repository's record is only read.
"""

import copy
import socket
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_shedu_sdua_protein_example as writer  # noqa: E402

COMMITTED = writer.TARGET
ACTION = "ADD_SDUA_PROTEIN_EXAMPLE"


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    """Fail any network connection: the writer must never reach UniProt or Europe PMC."""

    def refuse(*_args, **_kwargs):
        raise AssertionError("network access attempted during an offline writer test")

    monkeypatch.setattr(socket.socket, "connect", refuse)
    monkeypatch.setattr(socket, "create_connection", refuse)


def committed_record():
    return yaml.safe_load(COMMITTED.read_text())


def graph_of(record):
    graphs = [g for g in record["causal_graphs"] if g["graph_id"] == writer.GRAPH_ID]
    assert len(graphs) == 1
    return graphs[0]


def strip_additions(record):
    """Return the record without the writer's node, edge and event, each removed exactly once."""
    base = copy.deepcopy(record)
    graph = graph_of(base)
    nodes = [n for n in graph["nodes"] if n["node_id"] != writer.NODE_ID]
    edges = [e for e in graph["edges"] if e["subject"] != writer.NODE_ID]
    events = [e for e in base["curation_history"] if e["action"] != ACTION]
    assert len(graph["nodes"]) - len(nodes) == 1
    assert len(graph["edges"]) - len(edges) == 1
    assert len(base["curation_history"]) - len(events) == 1
    graph["nodes"], graph["edges"], base["curation_history"] = nodes, edges, events
    return base


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    """Point the writer at a temp copy of the pre-change (base) record."""
    target = tmp_path / "data" / "traits" / "genomics" / "shedu_system.yaml"
    target.parent.mkdir(parents=True)
    monkeypatch.setattr(writer, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(writer, "TARGET", target)
    writer.write_validated_trait(strip_additions(committed_record()), target)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_dry_run_default_writes_nothing(isolated, monkeypatch):
    committed_before = COMMITTED.read_bytes()
    before = snapshot(isolated)
    run(monkeypatch)
    assert snapshot(isolated) == before
    assert COMMITTED.read_bytes() == committed_before


def test_apply_to_base_emits_exactly_the_committed_additions(isolated, monkeypatch):
    base = yaml.safe_load(writer.TARGET.read_text())
    committed_before = COMMITTED.read_bytes()
    run(monkeypatch, apply=True)
    out = yaml.safe_load(writer.TARGET.read_text())
    committed = committed_record()

    # Nothing outside the three additions changed.
    assert strip_additions(out) == base

    graph, committed_graph = graph_of(out), graph_of(committed)
    (node,) = [n for n in graph["nodes"] if n["node_id"] == writer.NODE_ID]
    assert node == writer.NODE
    assert node in committed_graph["nodes"]
    ids = [n["node_id"] for n in graph["nodes"]]
    assert ids.index(writer.NODE_ID) == ids.index(writer.ANCHOR_NODE) + 1

    assert node["node_type"] == "GENE_OR_PROTEIN"
    assert node["grounding_status"] == "REVIEWED_LABEL_ONLY"
    assert "grounding" not in node
    assert node["grounding_notes"]
    (example,) = node["protein_examples"]
    assert example["uniprot_id"] == "UniProtKB:B7HFR2"
    assert example["gene_symbol"] == "sduA"
    assert example["taxon_id"] == "NCBITaxon:405532"
    assert example["taxon_label"] == "Bacillus cereus (strain B4264)"
    assert example["entry_status"] == "REVIEWED"
    assert (example["entry_version"], example["sequence_version"]) == (58, 1)
    assert str(example["retrieved_on"]) == writer.RETRIEVED_ON
    assert len(example["evidence"]) == 2
    for item in example["evidence"]:
        assert item["reference"] == writer.GU
        assert item["notes"]
        assert "..." not in item["snippet"] and "…" not in item["snippet"]

    (edge,) = [e for e in graph["edges"] if e["subject"] == writer.NODE_ID]
    assert edge == writer.EDGE
    assert edge in committed_graph["edges"]
    assert (edge["predicate_id"], edge["object"]) == ("RO:0002326", "shedu_nuclease_activation")
    assert edge["object"] in ids

    new_events = [e for e in out["curation_history"] if e["action"] == ACTION]
    assert len(out["curation_history"]) == len(base["curation_history"]) + 1
    (event,) = new_events
    assert event == out["curation_history"][-1]
    assert event in committed["curation_history"]
    assert event["curator"] == "claude"
    assert event["llm_assisted"] is True
    assert event["timestamp"] == writer.TIMESTAMP

    assert out["identifier"] == writer.IDENTIFIER
    assert out["mapping_status"] == base["mapping_status"] == "PROPOSED"
    assert graph["scope_status"] == graph_of(base)["scope_status"]
    assert COMMITTED.read_bytes() == committed_before


def test_refuses_record_that_already_has_the_node(isolated, monkeypatch):
    run(monkeypatch, apply=True)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="already present"):
        run(monkeypatch, apply=True)
    assert snapshot(isolated) == before


def test_refuses_the_committed_record(isolated, monkeypatch):
    writer.TARGET.write_bytes(COMMITTED.read_bytes())
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="already present"):
        run(monkeypatch, apply=True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("apply", [False, True])
def test_refuses_a_different_trait(isolated, monkeypatch, apply):
    record = yaml.safe_load(writer.TARGET.read_text())
    record["identifier"] = "traitmech:000221"
    writer.TARGET.write_text(yaml.safe_dump(record, sort_keys=False))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="is not traitmech:000220"):
        run(monkeypatch, apply)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("change", ["renamed", "duplicated"])
def test_refuses_unless_exactly_one_target_graph(isolated, monkeypatch, change):
    record = yaml.safe_load(writer.TARGET.read_text())
    if change == "renamed":
        graph_of(record)["graph_id"] = "some_other_graph"
    else:
        record["causal_graphs"].append(copy.deepcopy(graph_of(record)))
    writer.TARGET.write_text(yaml.safe_dump(record, sort_keys=False))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match=f"exactly one {writer.GRAPH_ID}"):
        run(monkeypatch, apply=True)
    assert snapshot(isolated) == before


def test_refuses_when_edge_object_node_is_missing(isolated, monkeypatch):
    record = yaml.safe_load(writer.TARGET.read_text())
    graph = graph_of(record)
    graph["nodes"] = [n for n in graph["nodes"] if n["node_id"] != writer.EDGE["object"]]
    writer.TARGET.write_text(yaml.safe_dump(record, sort_keys=False))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="missing"):
        run(monkeypatch, apply=True)
    assert snapshot(isolated) == before


def test_validation_failure_writes_nothing(isolated, monkeypatch):
    bad = dict(writer.NODE, unrecognized_field="must not be written")
    monkeypatch.setattr(writer, "NODE", bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, apply=True)
    assert snapshot(isolated) == before
