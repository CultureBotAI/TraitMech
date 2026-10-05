"""Protect mating-type scope, evidence limits and fail-closed trait writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_unisexual_reproduction_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "unisexual_reproduction.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_identity():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000613"
    assert record["label"] == "unisexual reproduction"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A fungal phenotype enabling sexual or parasexual reproduction with "
        "genetic contribution from only one mating type."
    )
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs", "canonical_examples"])
    event, = record["curation_history"]
    assert event["llm_assisted"] is True and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["not mean one strain", "not a subclass of parasexuality",
                 "helper cells", "MAT sequence content", "absence of outcrossing"]:
        assert text in scope["rationale"]
    for text in ["laboratory-cross derivative", "different readouts", "natural strains",
                 "Manual full-text matching"]:
        assert text in mechanism["rationale"]


def test_evidence_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.FERETZAKI
    feretzaki, lin, alby, ni = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.FERETZAKI, writer.LIN, writer.ALBY, writer.NI}
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [13, 13, 17, 18]
    for text in ["scientific abstract", "not the separate Author Summary", "precise role"]:
        assert text in feretzaki["notes"]
    for text in ["scientific abstract", "API uses the word alpha", "not obligatory clonal"]:
        assert text in lin["notes"]
    for text in ["not an abstract quote", "NCBI PMC efetch", "near-diploid and intermediate",
                 "not uniform restoration of euploidy", "helpers need not contribute genomes"]:
        assert text in alby["notes"]
    for text in ["not an abstract quote", "laboratory F1", "do not make XL280 a natural exemplar",
                 "not defining requirements"]:
        assert text in ni["notes"]


def test_proposal_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056700"
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
        record["parent_traits"] = ["traitmech:000609"]
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
