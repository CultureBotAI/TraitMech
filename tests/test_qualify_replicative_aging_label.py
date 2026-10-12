"""Protect the label correction and append-only preimage guards."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qualify_replicative_aging_label as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal.tsv")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    writer.write_validated_trait(writer.original.build_record(), writer.TARGET)
    writer.write_validated_trait(writer.original.PARENT, writer.PARENT_PATH)
    writer.PROPOSAL.write_text(writer.original.proposal_tsv(writer.original.build_record()))
    return tmp_path


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def test_corrected_scope_preserves_evidence_and_history():
    before, after = writer.original.build_record(), writer.build_record()
    assert after["label"] == "replicative aging with functional decline"
    assert after["curation_history"][:-1] == before["curation_history"]
    assert len(after["curation_history"]) == len(before["curation_history"]) + 1
    for key in before:
        if key not in {"label", "curation_history", "discussions"}:
            assert before[key] == after[key]
    assert after["discussions"][1] == before["discussions"][1]
    assert "not asserted as an exact synonym" in after["discussions"][0]["rationale"]
    assert all(d["status"] == "OPEN" for d in after["discussions"])
    rows = list(csv.reader(io.StringIO(writer.original.proposal_tsv(after)), delimiter="\t"))
    assert rows[2][1:3] == [after["label"], after["definition"]]


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert after["parent.yaml"] == before["parent.yaml"]
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("content", ["", "unreviewed drift\n"])
def test_drift_refused_without_writes(isolated, monkeypatch, target, content):
    getattr(writer, target).write_text(content)
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


def test_invalid_result_refused_before_writes(isolated, monkeypatch):
    bad = writer.build_record()
    bad["unknown_slot"] = True
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
