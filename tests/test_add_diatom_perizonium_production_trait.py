"""Verify source boundaries and dry-run, replay, and preimage guards."""

import csv
import io
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_diatom_perizonium_production_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000693"
    assert record["label"] == "diatom perizonium production"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["traitmech:000690"]
    assert record["definition"] == (
        "A biomineralization phenotype in which a diatom produces the siliceous "
        "band system called the perizonium in an auxospore wall."
    )
    assert all(record.get(k) is None for k in [
        "causal_graphs", "canonical_examples", "xrefs", "synonyms",
    ])
    event, = record["curation_history"]
    assert event["llm_assisted"] and event["curator"] == "codex"
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_evidence_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.BIDDULPHIA
    assert [e["reference"] for e in record["evidence"]] == [
        writer.BIDDULPHIA, writer.PLAGIOGRAMMACEANS, writer.TABULARIA,
    ]
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    for pmid, item in zip(["36067191", "28813426", "23972513"], record["evidence"], strict=True):
        assert f"EXT_ID:{pmid} AND SRC:MED" in item["notes"]
        assert "unread" in item["notes"]
    first, second, third = record["evidence"]
    assert "not establish live kinetics" in first["notes"]
    assert "boundaries uncertain" in first["notes"]
    assert "not a live secretion time course" in second["notes"]
    assert "reinterpretation targets other papers" in second["notes"]
    assert "not absolute absence" in third["notes"]
    assert "not independent-laboratory replication" in third["notes"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    scope, mechanism = record["discussions"]
    assert all(t in scope["rationale"] for t in [
        "inherited band possession", "auxosporulation alone", "sexual origin",
        "No requirement for both", "not unresolved exact",
    ])
    assert all(t in mechanism["rationale"] for t in [
        "No canonical examples", "deferred, not claimed absent",
        "sequence features alone", "taxon-paired accessions",
    ])


def test_proposal_parent_is_released_ancestor_with_explicit_refinement():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1064600"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == writer.PARENT["parent_traits"][0] == "METPO:1000059"
    assert "METPO:1064300" in rows[2][9]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10"
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        f"TraitMech:data/traits/physiology/{writer.SLUG}.yaml",
        *(e["reference"] for e in record["evidence"]),
    }


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


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
