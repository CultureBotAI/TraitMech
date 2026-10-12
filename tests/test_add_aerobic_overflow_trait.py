"""Protect oxygen-sufficient phenotype scope and guarded writer behavior."""

import csv
import io
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_aerobic_overflow_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_evidence_and_copy_isolation():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000705"
    assert record["label"] == "aerobic overflow metabolism"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["term_kind"] == "CLASS" and record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "incompletely oxidized products" in record["definition"]
    assert "lower ATP yield per substrate" in record["definition"]
    assert "respiratory capacity and sufficient oxygen" in record["definition"]
    assert record["definition_source"] == writer.IDENTITY
    assert [e["reference"] for e in record["evidence"]] == [
        writer.IDENTITY, writer.BACTERIAL, writer.YEAST,
    ]
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all(not record.get(k) for k in ["synonyms", "causal_graphs", "xrefs", "canonical_examples"])
    event, correction = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    assert "#1881" in correction["changes"] and correction["llm_assisted"]
    assert datetime.fromisoformat(correction["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    record["discussions"][0]["rationale"] = "mutated"
    assert len(writer.build_record()["evidence"]) == 3
    assert writer.build_record()["discussions"][0]["rationale"] != "mutated"


def test_scope_and_inference_limits():
    record = writer.build_record()
    identity, bacterial, yeast = record["evidence"]
    assert "not the abstract" in identity["notes"]
    assert "original modeling, not new experimental replication" in identity["notes"]
    assert "threshold is not universal" in bacterial["notes"]
    assert "does not exclude acetate reuptake" in bacterial["notes"]
    assert "above 30% air saturation" in yeast["notes"]
    assert "authors report no first-hour repression" in yeast["notes"]
    assert "does not establish monotonic or unchanged" in yeast["notes"]
    assert writer.ORIGINAL_RESPIRATION_NOTE not in yeast["notes"]
    scope, gaps = record["discussions"]
    assert "oxygen limitation must be excluded" in scope["rationale"]
    assert "not asserted as exact synonyms" in scope["rationale"]
    assert "excludes external electron acceptors" in scope["rationale"]
    assert "Gene presence and predicted flux alone" in gaps["rationale"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1065800"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1000059", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10"
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        f"TraitMech:data/traits/physiology/{writer.SLUG}.yaml",
        *(e["reference"] for e in record["evidence"]),
    }


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


def test_upgrade_original_draft_preserves_earlier_event(isolated, monkeypatch):
    original = writer.build_initial_record()
    writer.write_validated_trait(original, writer.TARGET)
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    revised = yaml.safe_load(writer.TARGET.read_text())
    assert revised == writer.build_record()
    assert revised["curation_history"][:-1] == original["curation_history"]


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_existing_drift_refused_without_partial_write(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", list(writer.PARENT))
def test_parent_projection_drift_refused(isolated, monkeypatch, field):
    parent = dict(writer.PARENT)
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PROPOSAL"])
def test_empty_preimage_refused(isolated, monkeypatch, target):
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_prevalidation_failure_writes_nothing(isolated, monkeypatch):
    bad = writer.build_record()
    bad["unrecognized_field"] = "must not be written"
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
