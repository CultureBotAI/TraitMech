"""Protect nuclear-state scope, qualified provenance and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_heterokaryosis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "heterokaryosis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_definition_and_readout_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000608"
    assert record["label"] == "heterokaryosis"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "GENOMICS"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition"] == (
        "A fungal phenotype characterized by the coexistence of genetically "
        "distinct nuclei within a shared cytoplasm."
    )
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs"])
    assert len(record["curation_history"]) == 1
    assert record["curation_history"][0]["llm_assisted"] is True
    assert record["curation_history"][0]["timestamp"] == "2026-10-05T00:29:53Z"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["not a locus", "not an ontology parent", "not is-a parents",
                 "exactly two nuclei", "fungal scope"]:
        assert text in scope["rationale"]
    for text in ["different readouts", "label exchange", "NONMECHANISTIC",
                 "natural P581", "engineered 2018"]:
        assert text in mechanism["rationale"]


def test_primary_evidence_and_access_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.EXPRESSION
    assert {e["reference"] for e in record["evidence"]} == {
        writer.EXPRESSION, writer.SAMILS, writer.KESSLER}
    for e in record["evidence"]:
        assert 8 <= len(e["snippet"].split()) <= 25
        assert "directly retrieved Europe PMC abstract" in e["notes"]
    expression, natural, fungicide = record["evidence"]
    assert "genetically distinct nuclei" in expression["snippet"]
    assert "not inspected" in expression["notes"]
    assert "largely sterile" in expression["notes"]
    assert "Bulk DNA ratios and RNA expression are different readouts" in natural["notes"]
    assert "not visually inspected" in natural["notes"]
    for text in ["engineered derivatives", "dual fluorescence alone", "detection-limit",
                 "not demonstrated", "Figures 5-6", "remain uninspected"]:
        assert text in fungicide["notes"]


def test_natural_example_does_not_promote_component_stocks():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:40127"
    assert example["taxon_label"] == "Neurospora tetrasperma"
    assert example["reference"] == writer.SAMILS
    for text in ["P581 (lineage L6)", "Methods 2a and Table 1", "homokaryotic components",
                 "not identifiers for the heterokaryon", "not assert that all isolates",
                 "https://pmc.ncbi.nlm.nih.gov/articles/PMC4046401/"]:
        assert text in example["note"]


def test_proposal_parity_and_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056200"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert all(e["reference"] in rows[2][3] for e in record["evidence"])
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    applied = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == applied


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_drift_refused_without_partial_writes(isolated, monkeypatch, target):
    if target == "record":
        record = writer.build_record()
        record["parent_traits"] = ["METPO:1000702"]
        writer.write_validated_trait(record, writer.TARGET)
    else:
        writer.PROPOSAL.mkdir()
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Unreviewed drift")
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


def test_invalid_record_cannot_write_outputs(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert not snapshots(isolated)
