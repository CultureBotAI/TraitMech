"""Protect emitted child axioms, label scope and immutable historical inputs."""

import copy
import csv
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import refine_cellular_contraction_proposal as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal.tsv")
    sources = {}
    for identifier, (path, digest) in writer.CHILD_PROPOSALS.items():
        destination = tmp_path / (identifier.replace(":", "_") + ".tsv")
        destination.write_bytes(path.read_bytes())
        sources[identifier] = (destination, digest)
    monkeypatch.setattr(writer, "CHILD_PROPOSALS", sources)
    old = writer.original.build_record()
    writer.write_validated_trait(old, writer.TARGET)
    writer.PROPOSAL.write_text(writer.original.proposal_tsv(old))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {p.name: p.read_bytes() for p in root.iterdir() if p.is_file()}


def test_scope_history_and_three_rows(isolated):
    old = writer.original.build_record()
    record = writer.build_record()
    assert record["label"] == "cell body or cytoplasmic projection contraction"
    restored = copy.deepcopy(record)
    restored["label"] = old["label"]
    event = restored["curation_history"].pop()
    assert restored == old
    assert event["llm_assisted"] and event["timestamp"] == writer.TIMESTAMP
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 5 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][3].split("|") == ["TraitMech:data/traits/physiology/cellular_contraction.yaml", writer.original.KATOH]
    assert rows[2][4] == "METPO:1000059"
    for row, (identifier, (path, _)) in zip(rows[3:], writer.CHILD_PROPOSALS.items(), strict=True):
        historical = list(csv.reader(io.StringIO(path.read_text()), delimiter="\t"))[2]
        assert row[0] == identifier and row[4] == "METPO:1068200"
        assert all(row[i] == historical[i] for i in range(11) if i not in (4, 9))


def test_dry_apply_replay_preserves_history_cohorts(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    for path, _ in writer.CHILD_PROPOSALS.values():
        assert path.read_bytes() == before[path.name]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


@pytest.mark.parametrize("field", ["label", "definition", "mapping_status", "curation_history"])
def test_record_drift_refused(isolated, monkeypatch, field):
    doc = yaml.safe_load(writer.TARGET.read_text())
    doc[field] = [] if field == "curation_history" else "changed"
    writer.TARGET.write_text(yaml.safe_dump(doc))
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("which", ["proposal", "historical"])
def test_proposal_drift_refused(isolated, monkeypatch, which):
    path = writer.PROPOSAL if which == "proposal" else next(iter(writer.CHILD_PROPOSALS.values()))[0]
    path.write_text(path.read_text() + "drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_result_prevalidated(isolated, monkeypatch):
    record = writer.build_record()
    record["unknown_field"] = "invalid"
    monkeypatch.setattr(writer, "build_record", lambda: record)
    before = snapshot(isolated)
    with pytest.raises(Exception):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_refinement_is_not_creation_writer_replay(isolated, monkeypatch):
    run(monkeypatch, True)
    assert yaml.safe_load(writer.TARGET.read_text()) != writer.original.build_record()
    assert writer.PROPOSAL.read_text() != writer.original.proposal_tsv(writer.original.build_record())


def test_source_receipt_distinguishes_historical_label_and_plan():
    path = writer.ROOT / "research/traits/physiology/cellular_contraction-source-verification.json"
    receipt = json.loads(path.read_text())
    assert receipt["allocation"]["label"] == writer.original.build_record()["label"]
    refinement = receipt["review_refinements"]
    assert refinement["current_label"] == writer.LABEL
    assert refinement["issues"] == [1941, 1942]
    assert "pre-curation plan" in refinement["historical_plan_scope"]
