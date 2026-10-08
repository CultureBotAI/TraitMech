"""Guard constricting-ring scope, evidence qualifiers and fail-closed writes."""

import csv
import io
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_constricting_ring_trait as writer  # noqa: E402


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


def test_scope_and_copy_isolation():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000677"
    assert record["label"] == "fungal constricting-ring trap formation"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert all(t in record["definition"] for t in [
        "fungus", "three-celled hyphal", "mature ring cells", "inflate inward",
    ])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    initial, correction = record["curation_history"]
    assert initial == writer.build_initial_record()["curation_history"][0]
    assert "#1823" in correction["changes"]
    for event in (initial, correction):
        assert event["llm_assisted"]
        assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_source_and_example_boundaries():
    record = writer.build_record()
    assert record["definition_source"] == writer.DEVELOPMENT
    assert [e["reference"] for e in record["evidence"]] == [
        writer.DEVELOPMENT, writer.TAXONOMY, writer.CYTOKINESIS,
    ]
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "Figure 1" in record["evidence"][0]["notes"]
    assert "not universal requirements" in record["evidence"][0]["notes"]
    assert "2022; published 16 December" in record["evidence"][1]["notes"]
    assert "not time-resolved inflation" in record["evidence"][1]["notes"]
    assert "not another positive nematode-trap observation" in record["evidence"][2]["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:2743661", "Drechslerella daliensis (nom. inval.)",
    )
    assert example["reference"] == writer.TAXONOMY
    assert all(t in example["note"] for t in [
        "CGMCC3.20131", "burned forest soil", "25 July 2017", "rank species",
        "not a claim", "validly published", "not every isolate",
    ])
    scope, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "morphologically complete immature rings" in scope["rationale"]
    assert "individual cell geometry" in scope["rationale"]
    assert "intracellular actomyosin rings" in scope["rationale"]
    assert "mechanism is deferred, not claimed absent" in mechanism["rationale"]
    assert "Native provenance of laboratory strain 29" in mechanism["rationale"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1063000"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        f"TraitMech:data/traits/morphology/{writer.SLUG}.yaml",
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


def test_initial_migration_preserves_original_event(isolated, monkeypatch):
    initial = writer.build_initial_record()
    writer.write_validated_trait(initial, writer.TARGET)
    writer.PROPOSAL.parent.mkdir(parents=True)
    writer.PROPOSAL.write_text(writer.proposal_tsv(initial))
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    record = yaml.safe_load(writer.TARGET.read_text())
    assert record == writer.build_record()
    assert record["curation_history"][:-1] == initial["curation_history"]
    assert record["canonical_examples"] == initial["canonical_examples"]
    assert record["definition"] == initial["definition"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


def test_initial_preimage_drift_is_refused(isolated, monkeypatch):
    initial = writer.build_initial_record()
    initial["definition"] = "Unreviewed definition."
    writer.write_validated_trait(initial, writer.TARGET)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


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
