"""Protect the no-exchange differentia and history-preserving correction."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qualify_cytogamy_scope as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "cytogamy.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "template.tsv")
    writer.write_validated_trait(writer.original.build_record(), writer.TARGET)
    writer.PROPOSAL.write_text(writer.original.proposal_tsv(writer.original.build_record()))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {p.name: p.read_bytes() for p in root.iterdir() if p.is_file()}


def test_definition_and_proposal_exclude_one_way_exchange():
    before = writer.original.build_record()
    after = writer.build_record()
    assert after["definition"] == (
        "A sexual-reproduction phenotype in which a paired cell self-fertilizes "
        "by fusion of its own gametic nuclei without exchanging gametic nuclei "
        "with its partner."
    )
    for key in before.keys() - {"definition", "discussions", "curation_history"}:
        assert before[key] == after[key]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert "#1717" in after["curation_history"][-1]["changes"]
    assert "no gametic-nuclear exchange" in after["discussions"][0]["rationale"]
    assert after["discussions"][1:] == before["discussions"][1:]
    old = list(csv.reader(io.StringIO(writer.original.proposal_tsv(before)), delimiter="\t"))
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv()), delimiter="\t"))
    assert rows[:2] == old[:2] and {len(r) for r in rows} == {11}
    assert rows[2][2] == after["definition"]
    assert "without gametic-nuclear exchange" in rows[2][9]
    assert all(rows[2][i] == old[2][i] for i in range(11) if i not in [2, 9])


def test_dry_run_apply_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_refused_before_writes(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    if target == "TARGET":
        record = yaml.safe_load(path.read_text())
        record["label"] = "unreviewed drift"
        writer.write_validated_trait(record, path)
    else:
        path.write_text(path.read_text() + "unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
def test_missing_preimage_refused(isolated, monkeypatch, target):
    getattr(writer, target).unlink()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Missing reviewed"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_result_cannot_write(isolated, monkeypatch):
    invalid = copy.deepcopy(writer.build_record())
    invalid["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "build_record", lambda: invalid)
    before = snapshot(isolated)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
