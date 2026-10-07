"""Test palmelloid enclosure, evidence qualifications and guarded curation."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_palmelloid_formation_trait as writer  # noqa: E402


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


def test_identity_scope_and_provenance():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000654"
    assert record["label"] == "palmelloid formation"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "retention within a mother-cell wall" in record["definition"]
    assert "adhesion through extracellular gelatinous material" in record["definition"]
    assert "nonmotile multicellular groups" in record["definition"]
    assert not any(s in record["definition"] for s in [
        "stress", "four", "sixteen", "flagella", "photoprotection", "cytokinesis",
    ])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_evidence_example_and_interpretation_limits():
    record = writer.build_record()
    light, cold, broad = record["evidence"]
    assert record["definition_source"] == broad["reference"] == writer.BROAD_USAGE
    assert light["reference"] == writer.HIGH_LIGHT
    assert cold["reference"] == writer.PSYCHROPHILE
    assert all(0 < len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "not an individual-cell count" in light["notes"]
    assert "stress is not a necessary condition" in cold["notes"]
    assert "terminology evidence" in broad["notes"]
    assert "selected evolved isolates" in broad["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:1653778", "Chlamydomonas priscui",
    )
    assert example["reference"] == writer.PSYCHROPHILE
    assert "8 C" in example["note"] and "0.7 M NaCl" in example["note"]
    assert "mixed population" in example["note"]
    assert "priscuii" in example["note"] and "synonym" in example["note"]
    scope, gap, provenance = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "normal transient pre-release sporangium" in scope["rationale"]
    assert "Gene possession alone does not establish" in gap["rationale"]
    assert "not proof of engineering" in provenance["rationale"]
    assert "omit CC-4414 from canonical examples" in provenance["rationale"]


def test_initial_draft_upgrade_retains_history(isolated, monkeypatch):
    initial = writer.build_initial_record()
    writer.write_validated_trait(initial, writer.TARGET)
    writer.PROPOSAL.parent.mkdir(parents=True)
    writer.PROPOSAL.write_text(writer.proposal_tsv(initial))
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    revised = yaml.safe_load(writer.TARGET.read_text())
    assert revised == writer.build_record()
    assert revised["curation_history"][:-1] == initial["curation_history"]
    assert revised["curation_history"][-1]["action"] == "CORRECTED_DEFINITION_SCOPE"
    assert revised["canonical_examples"] == initial["canonical_examples"]


@pytest.mark.parametrize("field", ["definition", "evidence", "curation_history"])
def test_initial_draft_drift_refused(isolated, monkeypatch, field):
    initial = writer.build_initial_record()
    del initial[field]
    writer.TARGET.write_text(yaml.safe_dump(initial))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1060700"
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
