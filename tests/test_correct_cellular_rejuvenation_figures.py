"""Protect the distinct yeast endpoints and append-only correction provenance."""

import copy
import json
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import correct_cellular_rejuvenation_figures as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "SIDECAR", tmp_path / "source.json")
    writer.write_validated_trait(writer.initial.build_record(), writer.TARGET)
    source = {"sources": [{}, {}, {"source_read_scope": writer.initial.build_record()["evidence"][2]["notes"]}]}
    writer.SIDECAR.write_text(json.dumps(source))
    monkeypatch.setattr(writer, "EXPECTED_SOURCE_HASH", writer.digest(source))
    return tmp_path, source


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {p.name: p.read_bytes() for p in root.iterdir() if p.is_file()}


def test_only_attribution_and_new_event_change():
    before = writer.initial.build_record()
    after = writer.build_record()
    notes = after["evidence"][2]["notes"]
    assert writer.OLD not in notes and writer.NEW in notes
    assert "checksum" in notes and "separate result" in notes
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["llm_assisted"] and event["action"] == "CORRECTED_FIGURE_ATTRIBUTION"
    restored = copy.deepcopy(after)
    restored["evidence"][2]["notes"] = before["evidence"][2]["notes"]
    restored["curation_history"].pop()
    assert restored == before


def test_source_snapshot_retained_with_explicit_successor(isolated):
    _, source = isolated
    after = writer.corrected_sidecar(source)
    assert "assessment_corrections" not in source
    assert after["sources"] == source["sources"]
    correction, = after["assessment_corrections"]
    assert correction["supersedes_field"] == "sources[2].source_read_scope"
    assert correction["issue"].endswith("/1893")
    assert correction["corrected_source_read_scope"] == writer.build_record()["evidence"][2]["notes"]
    assert writer.corrected_sidecar(after) == after


def test_dry_run_apply_replay(isolated, monkeypatch):
    root, _ = isolated
    before = snapshot(root)
    assert run(monkeypatch) == 0 and snapshot(root) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(root)
    assert run(monkeypatch, True) == 0 and snapshot(root) == after


@pytest.mark.parametrize("field", ["definition", "label", "mapping_status", "parent_traits"])
def test_trait_drift_refused(isolated, monkeypatch, field):
    root, _ = isolated
    record = writer.initial.build_record()
    del record[field]
    writer.TARGET.write_text(yaml.safe_dump(record))
    before = snapshot(root)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(root) == before


@pytest.mark.parametrize("already_corrected", [False, True])
def test_sidecar_drift_refused_without_trait_write(isolated, monkeypatch, already_corrected):
    root, source = isolated
    if already_corrected:
        source = writer.corrected_sidecar(source)
        source["assessment_corrections"][0]["reason"] = "drift"
    else:
        source["sources"][2]["source_read_scope"] = "drift"
    writer.SIDECAR.write_text(json.dumps(source))
    before = snapshot(root)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(root) == before


def test_prevalidation_failure_writes_nothing(isolated, monkeypatch):
    root, _ = isolated
    record = writer.build_record()
    record["unknown_field"] = "invalid"
    monkeypatch.setattr(writer, "build_record", lambda: record)
    before = snapshot(root)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(root) == before
