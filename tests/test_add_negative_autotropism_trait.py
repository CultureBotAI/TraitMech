"""Protect negative-autotropism evidence, boundaries and guarded output."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_negative_autotropism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "negative_autotropism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_directional_definition_and_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000603"
    assert record["label"] == "negative autotropism"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A phenotype in which germ-tube emergence or hyphal extension is "
        "directionally biased away from neighboring cells or hyphae of the same species."
    )
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs",
                                       "canonical_examples"])
    assert len(record["curation_history"]) == 2
    assert record["curation_history"][0]["llm_assisted"] is True
    assert record["curation_history"][0]["timestamp"] == "2026-10-04T20:13:46Z"
    assert record["curation_history"][1]["action"] == "QUALIFY_STRAIN_PROVENANCE"
    assert "#1684" in record["curation_history"][1]["changes"]
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["without requiring both", "genetic identity", "hyphal fusion",
                      "cytoplasm retreat alone", "chemotropism or aerotropism"]:
        assert qualifier in boundary["rationale"]
    assert "engineered ro-1" not in mechanism["rationale"]
    for qualifier in ["strain sources", "1968 full paper", "origin has not been verified",
                      "Mutation alone does not establish genetic engineering or natural provenance",
                      "protein accessions", "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_direct_evidence_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.MONTIEL_RUBIES
    assert {e["reference"] for e in record["evidence"]} == {
        writer.MONTIEL_RUBIES, writer.ROBINSON,
    }
    extension, emergence = record["evidence"]
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
        assert "directly retrieved" in item["notes"]
    assert "away from each other" in extension["snippet"]
    for qualifier in ["retrospective", "not a new independent replication",
                      "Figure 5B", "Table 2", "not counts", "not inspected"]:
        assert qualifier in extension["notes"]
    assert "negative autotropism" in emergence["snippet"]
    for qualifier in ["Rhizopus stolonifer", "Mucor plumbeus", "Trichoderma viride",
                      "not demonstrated subsequent", "not a negative exemplar",
                      "sample sizes were not retrieved"]:
        assert qualifier in emergence["notes"]


def test_proposal_record_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055700"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert writer.MONTIEL_RUBIES in rows[2][3] and writer.ROBINSON in rows[2][3]
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
