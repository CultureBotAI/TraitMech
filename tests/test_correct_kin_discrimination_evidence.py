"""Keep the reviewed evidence repair precise and preserve initial provenance."""

import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_kin_discrimination_trait as initial  # noqa: E402
import correct_kin_discrimination_evidence as repair  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for name, relative in [("TARGET", "trait.yaml"), ("PARENT_PATH", "parent.yaml"), ("PROPOSAL", "proposal.tsv")]:
        monkeypatch.setattr(repair, name, tmp_path / relative)
    initial.write_validated_trait(initial.PARENT, repair.PARENT_PATH)
    initial.write_validated_trait(initial.build_record(), repair.TARGET)
    repair.PROPOSAL.write_text(initial.proposal_tsv(initial.build_record()))
    return tmp_path


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["repair"] + (["--apply"] if apply else []))
    return repair.main()


def test_precise_scope_and_history():
    before, after = initial.build_record(), repair.build_record()
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["timestamp"] == repair.TIMESTAMP
    for key in before:
        if key not in {"definition_source", "evidence", "discussions", "curation_history"}:
            assert before[key] == after[key]
    assert after["definition_source"] == "DOI:10.1128/mBio.00723-17"
    assert after["evidence"][0] == before["evidence"][0]
    assert after["evidence"][1]["reference"] == "DOI:10.1073/pnas.1512671112"
    assert after["evidence"][1]["notes"] == before["evidence"][1]["notes"]
    assert "swarms did merge" in after["evidence"][1]["snippet"]
    assert "same antagonism as nonkin" in after["evidence"][2]["snippet"]
    assert "scientific abstract" in after["evidence"][2]["notes"]
    assert "NOT_IN_ABSTRACT" not in after["evidence"][2]["notes"]
    assert after["discussions"][0] == before["discussions"][0]
    assert "corrected excerpt is from the scientific abstract" in after["discussions"][1]["rationale"]
    assert all(len(e["snippet"].split()) <= 25 for e in after["evidence"])
    assert initial.proposal_tsv(before) == initial.proposal_tsv(after)


def test_dry_run_apply_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(repair.TARGET.read_text()) == repair.build_record()
    assert repair.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("name", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("mode", ["missing", "empty", "drift"])
def test_bad_preimages_refused_without_writes(isolated, monkeypatch, name, mode):
    path = getattr(repair, name)
    if mode == "missing":
        path.unlink()
    else:
        path.write_text("" if mode == "empty" else "unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises((SystemExit, FileNotFoundError)):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
