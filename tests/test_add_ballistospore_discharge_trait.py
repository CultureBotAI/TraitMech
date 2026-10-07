"""Test the discharge/formation distinction and guarded trait writer."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_ballistospore_discharge_trait as writer  # noqa: E402


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


def test_identity_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000661"
    assert record["label"] == "ballistospore discharge"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "coalescence of Buller's drop" in record["definition"]
    assert "forcibly discharges spores" in record["definition"]
    assert all(s not in record["definition"] for s in ["asexual", "endospore", "PHS1"])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_evidence_examples_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.BALLISTICS
    ballistics, development, mechanics = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.BALLISTICS, writer.DEVELOPMENT, writer.MECHANICS,
    }
    assert all(0 < len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "calculated, not a directly measured range" in ballistics["notes"]
    assert "six launches" in ballistics["notes"]
    assert "image retrieval failed" in ballistics["notes"]
    assert ballistics["snippet"] == (
        "At the moment of fusion, Buller's drop snaps from the hilar appendix "
        "onto the adjacent spore surface."
    )
    assert "Introduction, first paragraph" in ballistics["notes"]
    assert "asexually (ballistoconidia) or sexually (basidiospores)" in development["snippet"]
    assert "GI277" in development["notes"]
    assert "does not distinguish formation from discharge" in development["notes"]
    assert "delayed formation" in development["notes"]
    assert "scientific abstract" in mechanics["notes"]
    assert "artificial validation system is not a fungal exemplar" in mechanics["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:5005", "Sporobolomyces salmonicolor",
    )
    assert example["reference"] == writer.BALLISTICS
    assert "Strain NPM01" in example["note"]
    assert "contaminated manufacturing facility" in example["note"]
    assert "modeled, not directly measured" in example["note"]
    assert "not every strain or life stage" in example["note"]
    hierarchy, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "formation can persist without release" in hierarchy["rationale"]
    assert "pressure-driven" in hierarchy["rationale"]
    assert "not an unknown-mechanism claim" in mechanism["rationale"]
    assert "not counted as verified evidence" in mechanism["rationale"]
    assert "Do not invent a protein motor" in mechanism["rationale"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1061400"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
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


def test_correction_preserves_initial_event_and_other_evidence():
    initial, corrected = writer.build_initial_record(), writer.build_record()
    assert corrected["curation_history"][:-1] == initial["curation_history"]
    assert corrected["curation_history"][-1]["action"] == "CORRECTED_EVIDENCE_SNIPPET"
    assert corrected["evidence"][1:] == initial["evidence"][1:]
    assert all(corrected[k] == v for k, v in initial.items()
               if k not in {"evidence", "curation_history"})


def test_reviewed_initial_preimage_migrates_and_replays(isolated, monkeypatch):
    writer.write_validated_trait(writer.build_initial_record(), writer.TARGET)
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


def test_unreviewed_initial_preimage_is_refused(isolated, monkeypatch):
    initial = writer.build_initial_record()
    initial["evidence"][0]["notes"] += " Unreviewed drift."
    writer.write_validated_trait(initial, writer.TARGET)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
