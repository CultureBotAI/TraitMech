"""Protect postfusion scope, evidence limits and guarded writer behavior."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_heterokaryon_incompatibility_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "heterokaryon_incompatibility.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_definition_and_scope_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000606"
    assert record["label"] == "heterokaryon incompatibility"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A fungal phenotype in which postfusion nonself recognition restricts "
        "the establishment or growth of viable vegetative heterokaryons."
    )
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs", "canonical_examples"])
    assert len(record["curation_history"]) == 1
    assert record["curation_history"][0]["llm_assisted"] is True
    assert record["curation_history"][0]["timestamp"] == "2026-10-04T23:02:57Z"
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for text in ["not a het/vic locus", "prefusion avoidance", "not an is-a parent",
                 "death of the whole colony", "vic4", "exact synonym"]:
        assert text in boundary["rationale"]
    for text in ["remain unread", "strain provenance", "protein mechanisms",
                 "not proof of ROS necessity"]:
        assert text in mechanism["rationale"]


def test_primary_evidence_and_access_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.HUTCHISON
    assert {e["reference"] for e in record["evidence"]} == {
        writer.HUTCHISON, writer.MAREK, writer.SMITH}
    identity, microscopy, boundary = record["evidence"]
    for evidence in record["evidence"]:
        assert 8 <= len(evidence["snippet"].split()) <= 25
        assert "directly retrieved" in evidence["notes"]
        assert "Full text, figures" in evidence["notes"]
    assert "slow growth" in identity["snippet"]
    assert "do not establish causal edges" in identity["notes"]
    assert "compatible self-pairings" in microscopy["snippet"]
    assert "rarely" in microscopy["snippet"]
    assert "Death also occurred in older hyphae" in microscopy["notes"]
    assert "stable heterokaryons" in boundary["snippet"]
    assert "not asserted as an exact synonym" in boundary["notes"]
    assert "one study, not independent replications" in boundary["notes"]


def test_proposal_parity_and_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056000"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert all(e["reference"] in rows[2][3] for e in record["evidence"])
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    applied = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == applied


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_drift_refused_without_partial_writes(isolated, monkeypatch, target):
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


def test_invalid_record_cannot_write_outputs(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert not snapshots(isolated)
