"""Retain nuclear provenance without broadening autogamy to gamete fusion."""

import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qualify_autogamy_nuclear_origin as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "autogamy.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "template.tsv")
    before = writer.original.build_neighbor(writer.original.neighbor_preimage())
    writer.write_validated_trait(before, writer.TARGET)
    writer.PROPOSAL.write_text(writer.original.autogamy_writer.proposal_tsv(before))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {p.name: p.read_bytes() for p in root.iterdir()}


def test_same_cell_origin_and_fusion_exclusion_are_both_explicit():
    before = writer.original.build_neighbor(writer.original.neighbor_preimage())
    after = writer.build_record()
    assert after["definition"] == (
        "A sexual-reproduction phenotype in which two meiotically derived "
        "gametic nuclei formed within one unpaired, undivided cell fuse with "
        "each other, without fusion of separate gametes."
    )
    for key in before.keys() - {"definition", "curation_history"}:
        assert before[key] == after[key]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert "#1720" in after["curation_history"][-1]["changes"]


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after
    assert writer.PROPOSAL.read_text() == writer.original.autogamy_writer.proposal_tsv(writer.build_record())


@pytest.mark.parametrize("name", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("applied", [False, True])
def test_drift_cannot_be_overwritten(isolated, monkeypatch, name, applied):
    if applied:
        run(monkeypatch, True)
    path = getattr(writer, name)
    if name == "TARGET":
        record = yaml.safe_load(path.read_text())
        record["definition"] += " drift"
        writer.write_validated_trait(record, path)
    else:
        path.write_text("drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("name", ["TARGET", "PROPOSAL"])
def test_missing_preimage_is_refused(isolated, monkeypatch, name):
    getattr(writer, name).unlink()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Missing reviewed"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
