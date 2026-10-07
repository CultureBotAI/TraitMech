"""Test fungal scope, source limits and guarded conidiation curation."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_conidiation_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000657"
    assert record["label"] == "fungal conidiation"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "fungus produces nonmotile asexual propagules" in record["definition"]
    assert "outgrowth from conidiogenous cells" in record["definition"]
    assert "conversion of pre-existing hyphal cells" in record["definition"]
    assert not any(s in record["definition"] for s in [
        "BrlA", "aerial", "stalk", "uninucleate", "endospore", "starvation",
    ])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 4


def test_evidence_examples_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.TERMINOLOGY
    terminology, development, morphology, boundary = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.TERMINOLOGY, writer.DEVELOPMENT, writer.MORPHOLOGY, writer.BOUNDARY,
    }
    assert all(0 < len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "supports terminology, not independent experimental replication" in terminology["notes"]
    assert "no Europe PMC records" in terminology["notes"]
    assert "dessication" in development["snippet"]
    assert "not personally inspected figures" in development["notes"]
    assert "Figure 7 caption" in morphology["notes"]
    assert "not time-lapse proof" in morphology["notes"]
    assert "not a fungal observation" in boundary["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:2041050", "Cephalotrichum lignatile",
    )
    assert example["reference"] == writer.MORPHOLOGY
    assert "CBS 209.63" in example["note"]
    assert "https://pmc.ncbi.nlm.nih.gov/articles/PMC5679026/" in example["note"]
    assert "1959 isolate from timber in a cave" in example["note"]
    assert "not an inferred wild-type or GMO status" in example["note"]
    hierarchy, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "fungal qualifier is intentional" in hierarchy["rationale"]
    assert "neither trait is imposed as the other's is-a parent" in hierarchy["rationale"]
    assert "rather than only one Aspergillus-like" in mechanism["rationale"]
    assert "no universal BrlA, WetA or autophagy dependence" in mechanism["rationale"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1061000"
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
