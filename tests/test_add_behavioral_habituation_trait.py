"""Protect habituation scope, quote provenance and fail-closed curation."""

import csv
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml
from lxml import html

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_behavioral_habituation_trait as writer  # noqa: E402


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


def test_identity_and_copy_isolation():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000714"
    assert record["label"] == "behavioral habituation"
    assert record["mapping_status"] == "PROPOSED" and record["term_kind"] == "CLASS"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition_source"] == writer.DEFINITION_SOURCE
    for text in ["repeated stimulation", "experience-dependent", "behavioral response",
                 "not attributable solely", "sensory adaptation", "motor fatigue"]:
        assert text in record["definition"]
    assert len(record["evidence"]) == 4
    assert all(e["reference"].startswith("DOI:") for e in record["evidence"])
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all(not record.get(k) for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs", "protein_examples"])
    assert len(record["curation_history"]) == 1
    event = record["curation_history"][0]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    record["discussions"][0]["rationale"] = "changed"
    assert len(writer.build_record()["evidence"]) == 4
    assert writer.build_record()["discussions"][0]["rationale"] != "changed"


def test_experimental_and_terminology_scope():
    record = writer.build_record()
    physarum, stentor, drugs, review = record["evidence"]
    for text in ["Q and CAF denote", "recovery was incomplete", "Residual aversiveness",
                 "not verified as the current corrected VoR", "crosses PDF columns"]:
        assert text in physarum["notes"]
    assert "low force stimuli" in stentor["snippet"] and "alternating high force" in stentor["snippet"]
    for text in ["Figure 4F", "not the adjacent model", "cadence equivalence remains unresolved",
                 "not a stimulus-free rest", "modeled, not an identified molecular"]:
        assert text in stentor["notes"]
    for text in ["12-hour cycloheximide", "not interchangeable", "not prove universally",
                 "not retention after withdrawal", "not an independent replication"]:
        assert text in drugs["notes"]
    assert "not a microbial experiment" in review["notes"]
    assert "not itself dishabituation" in review["notes"]
    scope, gaps, historical = record["discussions"]
    assert "not itself dishabituation" in scope["rationale"]
    assert "no species-wide assignment" in gaps["rationale"]
    for curie in ["METPO:1000004", "METPO:1000005", "METPO:0000248", "METPO:000249"]:
        assert curie in historical["rationale"]
    assert "Original historical scopes remain unresolved" in historical["rationale"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])


def test_source_receipt_and_caption_provenance():
    path = writer.ROOT / f"research/traits/physiology/{writer.SLUG}-source-verification.json"
    doc = json.loads(path.read_text())
    assert doc["trait_id"] == writer.IDENTIFIER and doc["decision_timestamp"] == writer.TIMESTAMP
    rows = doc["rows"]
    assert not doc["native_record_verification_pending"]
    assert doc["native_record_verification"]["exit"] == 0
    assert all(r["native_verdict"] == "NOT_IN_ABSTRACT" for r in rows)
    assert {r["reference"]: r["snippet"] for r in rows} == {
        e["reference"]: e["snippet"] for e in writer.build_record()["evidence"]
    }
    for row in rows:
        assert row["exact_contiguous_span"] and row["source_identity_verified"]
        assert row["words"] == len(row["snippet"].split()) <= 25
        assert len(row["source"]["sha256"]) == 64
        assert row["source"]["url"].startswith("https://")
        assert row["locator"] and row["version"]
    assert rows[3]["section_type"] == "Review definition"
    assert rows[1]["caption_locator"] == "//figure[@id='F4']"
    text = html.fragment_fromstring(rows[1]["raw_quote_html"], create_parent="p").text_content()
    assert text == rows[1]["snippet"]
    assert len(rows[1]["caption_text_sha256"]) == 64
    assert doc["allocation"]["conflicting_reservations"] == []
    assert len(doc["allocation"]["dispositions"]) == 12
    assert doc["novelty"]["ignored_hidden_included"]


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1066700"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1000059", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10" and rows[2][10] == writer.IDENTIFIER
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
