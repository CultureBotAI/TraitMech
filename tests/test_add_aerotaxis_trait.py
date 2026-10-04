"""Protect aerotaxis scope, isolate qualifications and guarded creation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_aerotaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "aerotaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_directional_trait_not_positive_only_or_a_receptor():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000589"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "preferred oxygen conditions" in record["definition"]
    assert "active locomotion is directionally biased" in record["definition"]
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_three_primary_sources_and_observation_boundaries():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {
        writer.SHIOI, writer.ZHULIN, writer.BOUVARD,
    }
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
    repulsion, band, tracking = record["evidence"]
    assert "at high concentrations" in repulsion["snippet"]
    assert "not inspected" in repulsion["notes"]
    assert "3 to 5 microM" in band["snippet"]
    assert "hypothesis" in band["notes"]
    assert "not inspected" in band["notes"]
    for qualifier in ["published 2022-09-15", "2022_bouvard_pre.pdf",
                      "visually checked", "nonmotile cells", "6 micrometre",
                      "does not identify"]:
        assert qualifier in tracking["notes"]


def test_canonical_example_is_species_and_isolate_qualified():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:488447"
    assert example["taxon_label"] == "Burkholderia contaminans"
    assert example["reference"] == writer.BOUVARD
    for qualifier in ["unnamed environmental strain", "16S and recA", "selected",
                      "motile subpopulation", "species rank", "not a universal"]:
        assert qualifier in example["note"]


def test_mapping_and_molecular_gaps_remain_explicit():
    boundary, mechanism = writer.build_record()["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["need not be the highest", "speed changes alone",
                      "magnetoaerotaxis", "flagellar-specific"]:
        assert qualifier in boundary["rationale"]
    for qualifier in ["correlation", "taxon-paired", "NONMECHANISTIC", "accession"]:
        assert qualifier in mechanism["rationale"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1054300"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_idempotent_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    applied = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == applied


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_output_drift_refused_without_partial_writes(isolated, monkeypatch, target):
    if target == "record":
        record = writer.build_record()
        record["definition"] = "Unreviewed drift."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        writer.PROPOSAL.mkdir()
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Unreviewed drift")
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


def test_invalid_record_cannot_write_either_output(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert not snapshots(isolated)
