"""Protect the evidence correction, historical provenance and guarded writes."""

import copy
import json
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qualify_aggregate_inheritance_reporter as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    base = json.loads(writer.SIDECAR.read_text())
    base.pop("assessment_corrections", None)
    for name, filename in [("TARGET", "trait.yaml"), ("SIDECAR", "source.json"),
                           ("PROPOSAL", "proposal.tsv")]:
        monkeypatch.setattr(writer, name, tmp_path / filename)
    writer.write_validated_trait(writer.initial.build_record(), writer.TARGET)
    writer.SIDECAR.write_text(json.dumps(base))
    writer.PROPOSAL.write_text(writer.initial.proposal_tsv(writer.initial.build_record()))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {p.name: p.read_bytes() for p in root.iterdir() if p.is_file()}


def test_scoped_change_and_unchanged_original():
    original = writer.initial.build_record()
    corrected = writer.build_record()
    assert corrected["curation_history"][:-1] == original["curation_history"]
    assert corrected["curation_history"][-1]["timestamp"] == writer.TIMESTAMP
    assert "#1896" in corrected["curation_history"][-1]["changes"]
    assert corrected["evidence"][0]["snippet"] == original["evidence"][0]["snippet"]
    assert writer.NEW in corrected["evidence"][0]["notes"]
    assert "not independent proof of endogenous unstressed aggregation" in writer.NEW
    assert corrected["evidence"][1:3] == original["evidence"][1:]
    assert corrected["evidence"][3]["reference"] == writer.SOURCE
    assert len(corrected["evidence"][3]["snippet"].split()) <= 25
    assert "Figure 3 separately" in corrected["evidence"][3]["notes"]
    assert "47 C for 15 minutes" in corrected["evidence"][3]["notes"]
    assert "no reporter is declared universally artifact-free" in corrected["discussions"][1]["rationale"]
    for field in set(original) - {"evidence", "discussions", "curation_history"}:
        assert corrected[field] == original[field]
    assert corrected["discussions"][0] == original["discussions"][0]
    assert corrected["discussions"][2] == original["discussions"][2]
    corrected["evidence"][3]["notes"] = "mutated"
    assert writer.build_record()["evidence"][3] == writer.ADDED_EVIDENCE
    assert len(writer.initial.build_record()["evidence"]) == 3


def test_historical_sidecar_preserved_and_correction_replay():
    document = json.loads(writer.SIDECAR.read_text())
    original = copy.deepcopy(document)
    original.pop("assessment_corrections", None)
    corrected = writer.corrected_sidecar(original)
    assert writer.corrected_sidecar(corrected) == corrected
    correction, = corrected.pop("assessment_corrections")
    assert corrected == original
    assert correction["issue"] == writer.ISSUE
    assert correction["added_evidence"] == writer.ADDED_EVIDENCE
    assert correction["source_sha256"] == writer.SOURCE_HASH
    assert correction["exact_contiguous_span"] and correction["source_identity_verified"]


def test_dry_run_apply_and_idempotence(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PROPOSAL.read_text() == writer.initial.proposal_tsv(writer.build_record())
    applied = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == applied


@pytest.mark.parametrize("field", ["TARGET", "SIDECAR", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_refused_without_partial_write(isolated, monkeypatch, field, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, field)
    if field == "SIDECAR":
        value = json.loads(path.read_text())
        value["unreviewed"] = True
        path.write_text(json.dumps(value))
    else:
        path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_corrupted_successor_refused(isolated, monkeypatch):
    run(monkeypatch, True)
    sidecar = json.loads(writer.SIDECAR.read_text())
    sidecar["assessment_corrections"][0]["issue"] = "unreviewed"
    writer.SIDECAR.write_text(json.dumps(sidecar))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_prevalidation_failure_writes_nothing(isolated, monkeypatch):
    bad = writer.build_record()
    bad["invalid_field"] = "rejected"
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
