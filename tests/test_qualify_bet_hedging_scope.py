"""Protect the source-defined distinction between pre-stress and independent states."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qualify_bet_hedging_scope as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal.tsv")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    writer.write_validated_trait(writer.original.PARENT, writer.PARENT_PATH)
    writer.write_validated_trait(writer.original.build_record(), writer.TARGET)
    writer.PROPOSAL.write_text(writer.original.proposal_tsv(writer.original.build_record()))
    return tmp_path


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def test_source_criteria_and_preserved_evidence():
    before, after = writer.original.build_record(), writer.build_record()
    assert "interconverts" in after["definition"]
    assert "independently of the prevailing environment" in after["definition"]
    assert "before environmental change" in after["definition"]
    assert "trade-offs" in after["definition"]
    assert "temporal precedence alone" in after["discussions"][0]["rationale"]
    assert "Deterministic age-related variation can qualify" in after["discussions"][0]["rationale"]
    for key in ["identifier", "evidence", "parent_traits", "mapping_status", "definition_source"]:
        assert before[key] == after[key]
    assert after["discussions"][1] == before["discussions"][1]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["action"] == "QUALIFIED_TRAIT_SCOPE"
    rows = list(csv.reader(io.StringIO(writer.original.proposal_tsv(after)), delimiter="\t"))
    assert rows[2][2] == after["definition"]
    after["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("value", ["", "unreviewed drift\n"])
def test_drift_refused_without_partial_write(isolated, monkeypatch, target, value):
    getattr(writer, target).write_text(value)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
def test_missing_preimage_refused(isolated, monkeypatch, target):
    getattr(writer, target).unlink()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Missing"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_prevalidation_failure_writes_nothing(isolated, monkeypatch):
    bad = writer.build_record()
    bad["unrecognized_field"] = "must fail before writing"
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
