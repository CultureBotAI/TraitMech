"""Protect inheritance scope, source qualification and fail-closed writes."""

import csv
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_unequal_protein_aggregate_inheritance_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000711"
    assert record["label"] == "unequal protein aggregate inheritance at cell division"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["term_kind"] == "CLASS" and record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "recurrently yields sibling cells" in record["definition"]
    assert "unequal numbers or amounts of inherited protein aggregates" in record["definition"]
    assert record["definition_source"] == writer.DEFINITION_SOURCE
    assert [e["reference"] for e in record["evidence"]] == [
        writer.BACTERIAL_RETENTION, writer.DEFINITION_SOURCE, writer.SHARED_INHERITANCE,
    ]
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all(not record.get(k) for k in ["synonyms", "causal_graphs", "xrefs", "canonical_examples"])
    event, = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    record["discussions"][0]["rationale"] = "mutated"
    assert len(writer.build_record()["evidence"]) == 3
    assert writer.build_record()["discussions"][0]["rationale"] != "mutated"


def test_scope_and_source_limits():
    record = writer.build_record()
    retention, fusion, shared = record["evidence"]
    assert "lineage schematic, not another experiment" in retention["notes"]
    assert "engineered MG1655 reporter" in retention["notes"]
    assert "Figure 4B is fusion and 4C is nucleation" in fusion["notes"]
    assert "caption reverses them" in fusion["notes"]
    assert "continuous 40 C" in fusion["notes"] and "followed by 37 C" in fusion["notes"]
    assert "not concentration" in fusion["notes"]
    assert "not the fraction of all sibling pairs" in shared["notes"]
    assert "projected cell area, not volume" in shared["notes"]
    assert "Unequal shared inheritance is compatible" in shared["notes"]
    assert "NOT_IN_ABSTRACT" in retention["notes"] and "NOT_IN_ABSTRACT" in shared["notes"]
    scope, gaps, obsolete = record["discussions"]
    for text in ["not a single unequal sibling pair", "Amount is not concentration",
                 "complete aggregate exclusion", "need not favor a fixed pole",
                 "not asserted as an exact synonym", "without reparenting"]:
        assert text in scope["rationale"]
    assert "does not imply active transport" in gaps["rationale"]
    assert "METPO:1000011" in obsolete["rationale"]
    assert "no definition, replacement or consider annotation" in obsolete["rationale"]
    assert "Do not reactivate" in obsolete["rationale"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])


def test_primary_source_sidecar_matches_snippets():
    path = writer.ROOT / f"research/traits/physiology/{writer.SLUG}-source-verification.json"
    rows = json.loads(path.read_text())["evidence_assessment"]["rows"]
    assert {"DOI:" + row["doi"]: row["snippet"] for row in rows} == {
        e["reference"]: e["snippet"] for e in writer.build_record()["evidence"]
    }
    assert [row["native_verdict"] for row in rows] == [
        "NOT_IN_ABSTRACT", "VERIFIED", "NOT_IN_ABSTRACT",
    ]
    assert all(row["exact_contiguous_span"] and row["source_identity_verified"] for row in rows)


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1066400"
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
