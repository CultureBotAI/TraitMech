"""Check rheotaxis scope, evidence provenance and guarded writer behavior."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_rheotaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "rheotaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_does_not_require_upstream_motion_or_sensing():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000582"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "fluid velocity gradients" in record["definition"]
    assert "self-propelled movement" in record["definition"]
    assert "upstream" not in record["definition"]
    assert "xrefs" not in record and "synonyms" not in record
    assert "causal_graphs" not in record
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_primary_evidence_and_strain_qualifiers():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {writer.KAYA, writer.MARCOS}
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
        assert item["notes"]
    assert "OI4139" in record["evidence"][0]["notes"]
    assert "passive advection alone is insufficient" in record["evidence"][0]["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:83333"
    assert example["taxon_label"] == "Escherichia coli K-12"
    assert example["reference"] == writer.KAYA
    assert "3-5 motility-selection" in example["note"]
    assert "moderate shear" in example["note"]
    question, = record["discussions"]
    assert question["status"] == "OPEN"
    assert "OI4139 must not be silently identified as strain 168" in question["rationale"]


def test_proposal_matches_identity_and_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1053600"
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
