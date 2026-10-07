"""Test broad fungal appressorium scope, evidence limits and guarded curation."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_appressorium_formation_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000659"
    assert record["label"] == "fungal appressorium formation"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "fungus forms specialized surface-associated penetration structures" in record["definition"]
    assert not any(s in record["definition"] for s in [
        "plant", "melanized", "single-celled", "germ tube", "Pmk1", "mitosis",
    ])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 4


def test_evidence_examples_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.SURVEY
    survey, guy11, cycle, boundary = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.SURVEY, writer.GUY11, writer.CELL_CYCLE, writer.EXPRESSORIUM,
    }
    assert all(0 < len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "actual Figures 2 and 6 and supplementary Table S1" in survey["notes"]
    assert "not an in-host assay or a universal fungal prevalence estimate" in survey["notes"]
    assert "previously called appressorium-like" in survey["notes"]
    assert "not the Author Summary" in guy11["notes"]
    assert "not inferred from RNA expression" in guy11["notes"]
    assert "Methods describe plastic coverslips" in guy11["notes"]
    assert "Results describing Figure 1A name a hydrophobic glass slide" in guy11["notes"]
    assert "surface discrepancy is unresolved" in guy11["notes"]
    assert "unrestricted post-penetration growth" in cycle["notes"]
    assert "not a canonical taxon assignment" in cycle["notes"]
    assert "not an asserted exact synonym" in boundary["notes"]
    assert "Figures, movies, supplements and strain provenance were not inspected" in boundary["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:318829", "Pyricularia oryzae",
    )
    assert example["reference"] == writer.GUY11
    assert "https://doi.org/10.5423/PPJ.NT.04.2013.0042" in example["note"]
    assert "French Guiana" in example["note"]
    assert "original 1988 isolation study was not retrieved" in example["note"]
    assert "not counted as an independent appressorium observation" in example["note"]
    assert "not its engineered deletion mutant, strain 70-15" in example["note"]
    hierarchy, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "GO:0075016 as a host-associated biological process" in hierarchy["rationale"]
    assert "compound infection cushions" in hierarchy["rationale"]
    assert "Whether to include that exit structure" in hierarchy["rationale"]
    assert "Formation does not guarantee successful penetration" in mechanism["rationale"]
    assert "possession of a candidate gene is not proof" in mechanism["rationale"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1061200"
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


def test_initial_record_migration_preserves_evidence_and_history(isolated, monkeypatch):
    initial = writer.build_initial_record()
    writer.write_validated_trait(initial, writer.TARGET)
    writer.PROPOSAL.parent.mkdir(parents=True)
    writer.PROPOSAL.write_text(writer.proposal_tsv(initial))
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    updated = yaml.safe_load(writer.TARGET.read_text())
    assert updated == writer.build_record()
    assert updated["curation_history"][:-1] == initial["curation_history"]
    assert updated["curation_history"][-1]["action"] == "EVIDENCE_CORRECTION"
    assert updated["canonical_examples"] == initial["canonical_examples"]
    assert updated["evidence"][1]["snippet"] == initial["evidence"][1]["snippet"]
    assert writer.PROPOSAL.read_bytes() == before["proposal/template.tsv"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


def test_altered_initial_evidence_refused(isolated, monkeypatch):
    initial = writer.build_initial_record()
    initial["evidence"][1]["notes"] += " Unreviewed surface claim."
    writer.write_validated_trait(initial, writer.TARGET)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Existing target differs"):
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
