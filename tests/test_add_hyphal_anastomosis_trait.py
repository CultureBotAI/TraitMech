"""Protect completed-fusion scope, source qualifiers and guarded outputs."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_hyphal_anastomosis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "hyphal_anastomosis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_definition_and_stage_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000605"
    assert record["label"] == "hyphal anastomosis"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A phenotype in which vegetative fungal hyphae fuse to establish cytoplasmic continuity."
    )
    assert record["synonyms"] == [{"synonym_text": "vegetative hyphal fusion",
                                   "synonym_type": "EXACT_SYNONYM", "source": writer.CHARLTON}]
    assert not any(k in record for k in ["xrefs", "causal_graphs", "canonical_examples"])
    assert len(record["curation_history"]) == 2
    assert record["curation_history"][0]["llm_assisted"] is True
    assert record["curation_history"][0]["timestamp"] == "2026-10-04T22:09:46Z"
    assert record["curation_history"][1]["action"] == "QUALIFIED_EVIDENCE_ENDPOINT"
    assert "#1690" in record["curation_history"][1]["changes"]
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for text in ["positive autotropism", "does not require genetic identity",
                 "persistent network viability", "Postfusion incompatibility"]:
        assert text in boundary["rationale"]
    for text in ["strain-provenance", "Transformed carrot roots",
                 "do not establish engineering of the fungi", "protein accessions"]:
        assert text in mechanism["rationale"]


def test_sources_support_identity_and_preserve_limitations():
    record = writer.build_record()
    assert record["definition_source"] == writer.GIOVANNETTI
    assert {e["reference"] for e in record["evidence"]} == {
        writer.GIOVANNETTI, writer.CHARLTON, writer.CROLL}
    fusion, perturbation, nonself = record["evidence"]
    for evidence in record["evidence"]:
        assert 8 <= len(evidence["snippet"].split()) <= 25
        assert "directly retrieved" in evidence["notes"]
    assert "complete fusion" in fusion["snippet"]
    for text in ["actual Figures 1 and 3", "not replication counts",
                 "Figure 2 was not visually inspected", "did not demonstrate genetic recombination"]:
        assert text in fusion["notes"]
    assert "or vegetative hyphal fusion" in perturbation["snippet"]
    for text in ["actual Figure 3", "not measured flow", "not a clean knockout",
                 "delta-so75 did not restore fusion", "Supplements were not inspected"]:
        assert text in perturbation["notes"]
    assert "genetically distinct" in nonself["snippet"]
    for text in ["nine of ten", "scored as perfect fusion",
                 "not a count of all fusion events", "Postfusion withdrawal",
                 "does not establish nuclear recombination",
                 "not visually inspected", "appear transposed"]:
        assert text in nonself["notes"]
    assert "nonself combinations fused" not in nonself["notes"]


def test_proposal_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055900"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert all(e["reference"] in rows[2][3] for e in record["evidence"])
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == [record["synonyms"][0]["synonym_text"], ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    applied = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == applied


def test_initial_record_upgrade_preserves_history_and_identity(isolated, monkeypatch):
    initial = writer.initial_record()
    writer.write_validated_trait(initial, writer.TARGET)
    before = snapshots(isolated)
    assert run(monkeypatch) == 0
    assert snapshots(isolated) == before
    assert run(monkeypatch, True) == 0
    result = yaml.safe_load(writer.TARGET.read_text())
    assert result == writer.build_record()
    assert result["curation_history"][:-1] == initial["curation_history"]
    assert result["definition"] == initial["definition"]
    assert [e["snippet"] for e in result["evidence"]] == [
        e["snippet"] for e in initial["evidence"]]


def test_initial_record_drift_is_not_an_upgrade_preimage(isolated, monkeypatch):
    initial = writer.initial_record()
    initial["evidence"][2]["notes"] += " Unreviewed evidence."
    writer.write_validated_trait(initial, writer.TARGET)
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


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
