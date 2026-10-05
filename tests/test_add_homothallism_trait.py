"""Protect mating-system scope, source sections and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_homothallism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "homothallism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_identity():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000609"
    assert record["label"] == "homothallism"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A fungal phenotype enabling a culture founded from a single spore to "
        "reproduce sexually in isolation from a mating partner."
    )
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs"])
    event, = record["curation_history"]
    assert event["llm_assisted"] is True and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["not a sequence feature", "uninucleate spore", "outcrossing",
                 "universal compatibility", "not is-a parents"]:
        assert text in scope["rationale"]
    for text in ["Separate wild-type sporulation", "NONMECHANISTIC", "editorial digest"]:
        assert text in mechanism["rationale"]


def test_evidence_sections_and_experimental_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.REVIEW
    assert {e["reference"] for e in record["evidence"]} == {
        writer.REVIEW, writer.YUN, writer.PASSER}
    review, yun, passer = record["evidence"]
    for e in record["evidence"]:
        assert 8 <= len(e["snippet"].split()) <= 25
    for text in ["Introduction", "not experimental replication", "not an abstract quote"]:
        assert text in review["notes"]
    for text in ["scientific abstract", "not sufficient", "nuclear level",
                 "provenance has not been verified", "remain uninspected"]:
        assert text in yun["notes"]
    for text in ["eLife digest", "not a VERIFIED resolver verdict", "Figures 5 and 8",
                 "version 2", "UV-induced and spontaneous", "universal compatibility",
                 "not a requirement for all"]:
        assert text in passer["notes"]


def test_natural_strain_qualified_separately_from_mutants():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:1295531"
    assert example["taxon_label"] == "Cryptococcus depauperatus CBS 7841"
    assert example["reference"] == writer.PASSER
    for text in ["wild-type CBS7841", "Supplementary file 1", "Figure 5A", "Figure 5B",
                 "not all measurements on wild type", "https://www.atcc.org/products/36983",
                 "provenance, not independent trait replication"]:
        assert text in example["note"]


def test_proposal_parity():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056300"
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
