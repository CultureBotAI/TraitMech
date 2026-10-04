"""Protect light-directed growth, natural provenance and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_phototropism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "phototropism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_growth_definition_and_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000598"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "growth" in record["definition"]
    assert "toward or away" in record["definition"]
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["phototaxis", "photokinesis", "phototrophy", "growth rate",
                      "without requiring both", "homolog alone"]:
        assert qualifier in boundary["rationale"]
    for qualifier in ["heterologous", "native", "taxon-paired protein accessions",
                      "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_evidence_and_natural_strain_are_qualified():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {
        writer.IDNURM, writer.SANZ, writer.SHAKYA,
    }
    for item in record["evidence"]:
        assert 24 <= len(item["snippet"])
        assert len(item["snippet"].split()) <= 25
    idnurm, sanz, provenance = record["evidence"]
    assert "away from far-UV" in idnurm["snippet"]
    assert "not measured in that panel" in idnurm["notes"]
    assert "not the native fungus" in sanz["notes"]
    assert "not inspected" in sanz["notes"]
    assert "not an independent phototropism experiment" in provenance["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:763407"
    assert example["taxon_label"] == "Phycomyces blakesleeanus NRRL 1555(-)"
    assert example["reference"] == writer.IDNURM
    assert writer.SHAKYA in example["note"]
    assert "not the madA mutants or backcrossed A56" in example["note"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055200"
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
        record["canonical_examples"][0]["taxon_id"] = "NCBITaxon:4837"
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
