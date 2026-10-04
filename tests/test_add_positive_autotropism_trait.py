"""Protect positive-autotropism scope, provenance and guarded outputs."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_positive_autotropism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "positive_autotropism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_definition_and_stage_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000604"
    assert record["label"] == "positive autotropism"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A phenotype in which germ-tube emergence or hyphal extension is "
        "directionally biased toward neighboring cells or hyphae of the same species."
    )
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs",
                                       "canonical_examples"])
    assert len(record["curation_history"]) == 2
    assert record["curation_history"][0]["llm_assisted"] is True
    assert record["curation_history"][0]["timestamp"] == "2026-10-04T21:04:32Z"
    assert record["curation_history"][1]["action"] == "REFINE_EVIDENCE_SNIPPET"
    assert "#1687" in record["curation_history"][1]["changes"]
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for text in ["not require both", "not an exact synonym or a prerequisite",
                 "genetic identity is not required", "chemotropism", "opposite direction"]:
        assert text in boundary["rationale"]
    for text in ["strain-provenance", "transformed chicory roots",
                 "does not establish engineering of the fungi", "protein accessions"]:
        assert text in mechanism["rationale"]


def test_direct_sources_and_limitations():
    record = writer.build_record()
    assert record["definition_source"] == writer.ROBINSON
    assert {e["reference"] for e in record["evidence"]} == {writer.ROBINSON, writer.RICHTER}
    emergence, extension = record["evidence"]
    for evidence in record["evidence"]:
        assert 8 <= len(evidence["snippet"].split()) <= 25
        assert "directly retrieved" in evidence["notes"]
    assert "beginning more nearly towards its neighbour" in emergence["snippet"]
    for text in ["Cellophane over agar", "neutrality on agar alone", "not later tip bending",
                 "sample sizes were not retrieved", "mixed-orientation spore-pair",
                 "Rhizopus stolonifer and Mucor plumbeus", "marked negative autotropism",
                 "does not establish a net positive response"]:
        assert text in emergence["notes"]
    assert "approach each other" in extension["snippet"]
    for text in ["MUCL 43194", "representative pair", "not a replication count",
                 "not an assertion", "movies were not retrieved"]:
        assert text in extension["notes"]


def test_proposal_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055800"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert writer.ROBINSON in rows[2][3] and writer.RICHTER in rows[2][3]
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
