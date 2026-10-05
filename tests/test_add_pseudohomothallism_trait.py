"""Protect pseudohomothallism scope, qualified examples and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_pseudohomothallism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "pseudohomothallism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_identity():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000612"
    assert record["label"] == "pseudohomothallism"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["traitmech:000609"]
    assert record["definition"] == (
        "A fungal phenotype enabling a sexual spore carrying separate nuclei "
        "of compatible mating types to establish a self-fertile heterokaryotic culture."
    )
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs"])
    event, = record["curation_history"]
    assert event["llm_assisted"] is True and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["not heterothallism", "exactly two nuclei", "absence of outcrossing",
                 "MAT sequences", "METPO:1056300"]:
        assert text in scope["rationale"]
    for text in ["no one meiotic program", "natural P581", "NONMECHANISTIC"]:
        assert text in mechanism["rationale"]


def test_evidence_and_natural_example_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.REVIEW
    review, merino, raju, menkis = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.REVIEW, writer.MERINO, writer.RAJU, writer.MENKIS}
    for evidence in record["evidence"]:
        assert 8 <= len(evidence["snippet"].split()) <= 25
    for text in ["section s2b", "not experimental replication or an abstract quote"]:
        assert text in review["notes"]
    assert "scientific abstract" in merino["notes"]
    for text in ["truncated at 400 words", "three functional nuclei", "but inferred",
                 "Do not require exactly two nuclei"]:
        assert text in raju["notes"]
    for text in ["Methods s4d", "not an abstract quote", "selected assay denominator",
                 "83-progeny", "not the native P581 selfing assay"]:
        assert text in menkis["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:40127"
    assert example["taxon_label"] == "Neurospora tetrasperma"
    assert example["reference"] == writer.MENKIS
    for text in ["P581", "Table 1", "152 heterokaryotic", "selected assay set",
                 "not the example", "25 C"]:
        assert text in example["note"]


def test_proposal_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056600"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert all(e["reference"] in rows[2][3] for e in record["evidence"])
    assert rows[2][4] == "METPO:1000059"
    assert "standalone METPO proposal" in record["discussions"][0]["rationale"]
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
        record["parent_traits"] = ["METPO:1000059"]
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
