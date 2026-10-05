"""Protect switching scope, source discrepancies and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_mating_type_switching_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "mating_type_switching.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_identity():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000611"
    assert record["label"] == "mating-type switching"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A fungal phenotype enabling conversion from one mating type to "
        "another, either reversibly or irreversibly."
    )
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs", "canonical_examples"])
    event, = record["curation_history"]
    assert event["llm_assisted"] is True and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["not a literal MAT", "ordinary segregation", "not identical",
                 "not is-a parents", "Do not require reversibility"]:
        assert text in scope["rationale"]
    for text in ["natural strain provenance", "completed sexual reproduction", "NONMECHANISTIC"]:
        assert text in mechanism["rationale"]


def test_evidence_sections_and_experimental_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.REVIEW
    assert {e["reference"] for e in record["evidence"]} == {
        writer.REVIEW, writer.YAMADA, writer.YUN}
    review, yamada, yun = record["evidence"]
    for e in record["evidence"]:
        assert 8 <= len(e["snippet"].split()) <= 25
    for text in ["MATING TYPE SWITCHING (s3)",
                 "not experimental replication or an abstract quote", "irreversible"]:
        assert text in review["notes"]
    for text in ["scientific abstract", "engineered mutant", "not natural-isolate",
                 "exactly two mating types", "HTTP 500", "HTTP 403"]:
        assert text in yamada["notes"]
    for text in ["Conclusions (sec017)", "Actual Figures 3 and 4", "identify DR2",
                 "instead says DR1", "remains a model", "remain unverified"]:
        assert text in yun["notes"]


def test_proposal_parity():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056500"
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
