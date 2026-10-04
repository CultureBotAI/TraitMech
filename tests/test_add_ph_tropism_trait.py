"""Protect pH-tropism scope, evidence qualifications and guarded output."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_ph_tropism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "ph_tropism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_growth_definition_and_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000602"
    assert record["label"] == "pH tropism"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["traitmech:000597"]
    assert record["definition"] == (
        "A phenotype in which polarized growth is directionally biased "
        "in response to a spatial gradient of external pH."
    )
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs",
                                       "canonical_examples"])
    assert len(record["curation_history"]) == 1
    assert record["curation_history"][0]["llm_assisted"] is True
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["lower or higher pH", "pH taxis", "extension rate alone",
                      "not a released term", "METPO:1000059", "mutant"]:
        assert qualifier in boundary["rationale"]
    for qualifier in ["FGSC 9935", "FGSC 4287", "engineered", "uniform pH",
                      "taxon-paired protein accessions", "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_direct_evidence_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.FERNANDES
    assert {e["reference"] for e in record["evidence"]} == {
        writer.FERNANDES, writer.YAMAMOTO,
    }
    gradient, interface = record["evidence"]
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
        assert "directly retrieved Europe PMC JATS" in item["notes"]
        assert "visually inspected" in item["notes"]
    assert "pH gradient" in gradient["snippet"]
    for qualifier in ["25 mM HCl/NaOH", "500 germ tubes", "Panel A",
                      "not necessarily wild-type magnitude", "engineered-mutant"]:
        assert qualifier in gradient["notes"]
    assert "pH 4" in interface["snippet"]
    for qualifier in ["n=1", "not independent", "Growth inhibition at pH 3",
                      "conflicts", "not a universal pH-4", "not inspected"]:
        assert qualifier in interface["notes"]


def test_proposal_record_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055600"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert writer.FERNANDES in rows[2][3] and writer.YAMAMOTO in rows[2][3]
    assert rows[2][4] == "METPO:1000059"
    assert rows[2][2].startswith("A phenotype in which")
    assert "v474 acceptance" in rows[2][9]
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
        record["parent_traits"] = ["METPO:1000702"]
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
