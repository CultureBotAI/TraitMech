"""Test qualified chlamydospore evidence and guarded one-record curation."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_chlamydospore_formation_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000658"
    assert record["label"] == "fungal chlamydospore formation"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "fungus forms enlarged, thick-walled cells" in record["definition"]
    assert "within hyphae" not in record["definition"]
    assert "at their tips" not in record["definition"]
    assert not any(s in record["definition"] for s in [
        "dormant", "resistant", "endospore", "Rme1", "starvation", "uninucleate",
    ])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 6


def test_evidence_examples_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.MORPHOLOGY
    morphology, isolates, induction, viability, boundary, conidial = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.MORPHOLOGY, writer.ORIGINAL_ISOLATES, writer.INDUCTION,
        writer.VIABILITY, writer.BOUNDARY, writer.CONIDIAL_ROUTE,
    }
    assert all(0 < len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "not independent experimental replication across all fungi" in morphology["notes"]
    assert "Full Methods and strain tables were not inspected" in isolates["notes"]
    assert "not evidence that chlamydospores were observed in patient tissue" in isolates["notes"]
    assert "Actual Figure 1 micrographs" in induction["notes"]
    assert "ordinal 0-3 score, not a cell percentage" in induction["notes"]
    assert "not against survival roles in every fungus" in viability["notes"]
    assert "blastic conidiogenesis" in viability["notes"]
    assert "not a fungal observation" in boundary["notes"]
    assert "Informally Refereed" in boundary["notes"]
    assert "inside the conidia" in conidial["snippet"]
    assert "sub-MIC FA17" in conidial["notes"]
    assert "chlamydospore-like; those are not promoted" in conidial["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:42374", "Candida dubliniensis",
    )
    assert example["reference"] == writer.ORIGINAL_ISOLATES
    assert "naturally recovered oral clinical isolates" in example["note"]
    assert "https://doi.org/10.1099/13500872-141-7-1507" in example["note"]
    assert "cohort-level isolate provenance" in example["note"]
    assert "not assigned to CD36" in example["note"]
    hierarchy, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "traitmech:000657" in hierarchy["rationale"]
    assert "https://github.com/berkeleybop/metpo/issues/67" in hierarchy["rationale"]
    assert "GO:0001410 was resolved through QuickGO" in hierarchy["rationale"]
    assert "not support that as a universal function" in hierarchy["rationale"]
    assert "Gene possession alone is not a chlamydospore phenotype" in mechanism["rationale"]
    assert "Issue #1772 corrected the initial hypha-only restriction" in mechanism["rationale"]


def test_initial_draft_migration_preserves_provenance(isolated, monkeypatch):
    initial = writer.build_initial_record()
    writer.write_validated_trait(initial, writer.TARGET)
    writer.PROPOSAL.parent.mkdir(parents=True)
    writer.PROPOSAL.write_text(writer.proposal_tsv(initial))
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    corrected = yaml.safe_load(writer.TARGET.read_text())
    assert corrected == writer.build_record()
    assert corrected["curation_history"][:-1] == initial["curation_history"]
    assert corrected["curation_history"][-1]["action"] == "REVISED_DEFINITION"
    assert "#1772" in corrected["curation_history"][-1]["changes"]
    assert corrected["canonical_examples"] == initial["canonical_examples"]
    assert len(initial["evidence"]) == 5 and len(corrected["evidence"]) == 6
    assert corrected["definition"] != initial["definition"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1061100"
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
