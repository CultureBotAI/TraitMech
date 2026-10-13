"""Guard fungal nutritional scope, evidence provenance and conservative writes."""

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
import add_nutritional_fungal_mycoparasitism_trait as writer  # noqa: E402


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


def test_identity_copy_and_history():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000717"
    assert record["label"] == "nutritional fungal mycoparasitism"
    assert record["trait_category"] == "ECOLOGY"
    assert record["mapping_status"] == "PROPOSED" and record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["METPO:1000059"]
    for text in ["a fungus obtains nutrients", "expense of another fungus", "living host", "after killing it"]:
        assert text in record["definition"]
    assert record["definition_source"] == "DOI:10.1139/b95-389"
    assert len(record["evidence"]) == len({e["reference"] for e in record["evidence"]}) == 3
    assert all(e["reference"].startswith("DOI:") for e in record["evidence"])
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert not any(record.get(k) for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs", "protein_examples"])
    assert len(record["curation_history"]) == 1
    event = record["curation_history"][0]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    record["discussions"][0]["rationale"] = "changed"
    assert len(writer.build_record()["evidence"]) == 3
    assert writer.build_record()["discussions"][0]["rationale"] != "changed"


def test_evidence_limits_and_hierarchy():
    record = writer.build_record()
    review, plate, soil = record["evidence"]
    for text in ["strict sense", "oomycetes", "UNRESOLVED", "not an independent experiment"]:
        assert text in review["notes"]
    for text in ["PMID:22302490", "SRC:MED", "29 days", "not by itself host killing", "full text was not retrieved"]:
        assert text in plate["notes"]
    for text in ["AGR:IND500606635, not PubMed", "sterile microcosm", "three-day culture-out", "separate broth assay", "Shares all six authors"]:
        assert text in soil["notes"]
    assert len(record["discussions"]) == 2 and all(d["status"] == "OPEN" for d in record["discussions"])
    scope, limits = [d["rationale"] for d in record["discussions"]]
    for text in ["persistent physical association", "not an exact synonym", "no organism-level disjointness", "deprecated", "historical IDs are not xrefs"]:
        assert text in scope
    for text in ["not experimental isolate deposits", "unresolved, not silently harmonized", "not proof none exists"]:
        assert text in limits


def test_source_receipt():
    doc = json.loads((writer.ROOT / f"research/traits/ecology/{writer.SLUG}-source-verification.json").read_text())
    assert doc["trait_id"] == writer.IDENTIFIER and doc["decision_timestamp"] == writer.TIMESTAMP
    assert doc["native_record_verification"]["exit"] == 0
    assert {r["reference"]: r["snippet"] for r in doc["rows"]} == {
        e["reference"]: e["snippet"] for e in writer.build_record()["evidence"]
    }
    assert [r["native_verdict"] for r in doc["rows"]] == ["UNRESOLVED", "VERIFIED", "VERIFIED"]
    for row in doc["rows"]:
        assert row["exact_contiguous_span"] and row["source_identity_verified"]
        assert row["words"] == len(row["snippet"].split()) <= 25
        assert len(row["source"]["sha256"]) == 64
        assert row["source"]["url"].startswith("https://")
        assert row["locator"] and row["inspection_limits"]
    assert doc["allocation"]["conflicting_reservations"] == []
    assert doc["novelty"]["ignored_hidden_included"]


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1067000"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1000059", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10" and rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        f"TraitMech:data/traits/ecology/{writer.SLUG}.yaml",
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
def test_drift_refused_without_partial_write(isolated, monkeypatch, target, after_apply):
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
