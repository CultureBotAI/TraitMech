"""Protect stiffness-directed migration scope and guarded trait creation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_durotaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "durotaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_boundaries_preserve_active_migration():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000596"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "migration is biased toward regions of greater substrate stiffness" in record["definition"]
    assert not any(k in record for k in ["canonical_examples", "causal_graphs", "xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"] is True
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["positive, stiff-side", "differential growth", "traitmech:000594",
                      "friction gradient", "Mechanotaxis", "not an exact synonym"]:
        assert qualifier in boundary["rationale"]
    for qualifier in ["does not uniquely", "Ax2-derived", "natural-strain", "mammalian",
                      "taxon-paired", "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_evidence_preserves_version_locators_and_source_limits():
    kang, filipinas = writer.build_record()["evidence"]
    assert {kang["reference"], filipinas["reference"]} == {writer.KANG, writer.FILIPINAS}
    for item in [kang, filipinas]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
    assert "Dictyostelium" in kang["snippet"]
    for qualifier in ["Version of Record (v4)", "2024-12-13", "96821.4",
                      "Figure 4", "not an abstract quote", "velocity difference",
                      "not direct microbial protein evidence"]:
        assert qualifier in kang["notes"]
    assert "stiffer substrates" in filipinas["snippet"]
    for qualifier in ["Crossref", "2025-02-27", "not inspected", "node migration and growth"]:
        assert qualifier in filipinas["notes"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055000"
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
