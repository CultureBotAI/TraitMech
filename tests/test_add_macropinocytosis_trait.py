"""Guard native uptake scope and fail-closed trait/proposal writing."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_macropinocytosis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    parent = {**writer.PARENT, "trait_category": "UPPER", "term_kind": "CLASS"}
    writer.write_validated_trait(parent, writer.PARENT_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000634"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "bulk extracellular fluid" in record["definition"]
    assert "closing actin-driven plasma-membrane ruffles" in record["definition"]
    assert not any(s in record["definition"] for s in ["axenic", "NF1", "nutrient", "enhanced"])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]


def test_sources_and_measurement_limits():
    record = writer.build_record()
    first, second = record["evidence"]
    assert record["definition_source"] == first["reference"] == writer.DEFINITION
    assert second["reference"] == writer.WILDTYPE
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "Scientific ABSTRACT quote" in first["notes"]
    assert "P=0.057" in first["notes"] and "do not call this significant" in first["notes"]
    assert "transgenic reporter" in first["notes"]
    assert "Contiguous Introduction quote" in second["notes"]
    assert "cannot quantify cumulative uptake" in second["notes"]


def test_canonical_provenance_is_strain_qualified():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:44689"
    assert example["taxon_label"] == "Dictyostelium discoideum"
    assert example["reference"] == writer.WILDTYPE
    assert writer.PROVENANCE in example["note"]
    assert "not Ax2, AX4, NF1 knockouts or reporter transformants" in example["note"]
    assert "laboratory-selected NC4 clone" in example["note"]
    assert "not an unchanged original wild isolate" in example["note"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][10] == writer.IDENTIFIER


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


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_refused_without_partial_writes(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    if target == "PARENT_PATH":
        parent = yaml.safe_load(path.read_text())
        parent["definition"] = "Unreviewed scope change"
        writer.write_validated_trait(parent, path)
    else:
        path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_empty_target_refused(isolated, monkeypatch):
    writer.TARGET.touch()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
