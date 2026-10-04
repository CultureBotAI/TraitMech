"""Guard gyrotaxis semantics, source qualifiers and creation-only writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_gyrotaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "gyrotaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_torque_balance_not_a_rheotaxis_or_receptor_subtype():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000583"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "gravitational and viscous torques" in record["definition"]
    assert "swimming orientation" in record["definition"]
    assert "velocity gradient" not in record["definition"]
    assert "sensor" not in record["definition"]
    assert not any(key in record for key in ["xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_sources_example_context_and_explicit_graph_gap():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {writer.ZENG, writer.DURHAM}
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
        assert item["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:2829"
    assert example["taxon_label"] == "Heterosigma akashiwo"
    assert example["reference"] == writer.ZENG
    assert "GY-H24" in example["note"] and "3-9 hours" in example["note"]
    assert "species-level" in example["note"]
    question, = record["discussions"]
    assert question["status"] == "OPEN"
    assert "absence of mechanistic evidence" in question["rationale"]
    assert "audit requires a protein node" in question["rationale"]


def test_proposal_matches_record_without_shifted_equivalences():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1053700"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_idempotent_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    applied = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == applied


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_output_drift_refused_without_partial_writes(isolated, monkeypatch, target):
    if target == "record":
        record = writer.build_record()
        record["definition"] = "Unreviewed drift."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        writer.PROPOSAL.mkdir()
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Unreviewed drift")
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


def test_invalid_record_cannot_write_either_output(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert not snapshots(isolated)
