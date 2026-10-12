"""Keep the required environmental criterion distinct from its mechanism."""

import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import correct_bet_hedging_independence as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal.tsv")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    writer.write_validated_trait(writer.previous.original.PARENT, writer.PARENT_PATH)
    writer.write_validated_trait(writer.previous.build_record(), writer.TARGET)
    writer.PROPOSAL.write_text(writer.previous.original.proposal_tsv(writer.previous.build_record()))
    return tmp_path


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def test_implication_and_preserved_fields():
    before, after = writer.previous.build_record(), writer.build_record()
    rationale = after["discussions"][0]["rationale"]
    assert "must be independent of the prevailing environment" in rationale
    assert "environmental independence does not require a purely stochastic switching mechanism." in rationale
    assert "environmental independence is not a requirement" not in rationale
    assert rationale == before["discussions"][0]["rationale"].replace(writer.OLD_CLAUSE, writer.NEW_CLAUSE)
    assert {k: v for k, v in before.items() if k not in {"discussions", "curation_history"}} == {
        k: v for k, v in after.items() if k not in {"discussions", "curation_history"}}
    assert after["discussions"][1] == before["discussions"][1]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["action"] == "CORRECTED_SCOPE_WORDING"
    after["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    for name in ["parent.yaml", "proposal.tsv"]:
        assert (isolated / name).read_bytes() == before[name]
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
