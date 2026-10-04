"""Protect phototaxis evidence scope, canonical lineage and guarded creation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_phototaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "phototaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_directional_trait_not_a_receptor_or_positive_only():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000588"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "toward or away" in record["definition"]
    assert "active locomotion" in record["definition"]
    assert "speed" not in record["definition"]
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs", "replaces"])
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_three_primary_sources_and_version_boundaries():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {
        writer.SCHUERGERS, writer.BERTHOLD, writer.TRAUTMANN,
    }
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
    cyanobacterium, alga, provenance = record["evidence"]
    for qualifier in ["version 2", "2022-04-22", "-v2.xml", "immotile",
                      "PCC-M", "torA-gfp", "proposed PixJ1"]:
        assert qualifier in cyanobacterium["notes"]
    assert "not establish one universal" in cyanobacterium["notes"]
    assert "low CHR2 content" in alga["snippet"]
    assert "heterologous" in alga["notes"]
    assert "cell-wall-deficient CW2" in alga["notes"]
    assert "were not inspected" in alga["notes"]
    assert "laboratory microevolution" in provenance["notes"]
    assert "no blue-light phototaxis" in provenance["notes"]


def test_canonical_example_is_substrain_qualified():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:1148"
    assert example["taxon_label"] == "Synechocystis sp. PCC 6803"
    assert example["reference"] == writer.SCHUERGERS
    for qualifier in ["PCC-M", "not the torA-gfp", "species-level", "blue-light",
                      "DOI:10.1093/dnares/dss024", "No universal"]:
        assert qualifier in example["note"]


def test_source_discrepancies_and_mapping_gaps_remain_explicit():
    boundary, mechanism = writer.build_record()["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    assert "METPO:1000241 is obsolete" in boundary["rationale"]
    assert "biological-process" in boundary["rationale"]
    for qualifier in ["proposed model", "60x", "100x", "633 nm", "625 nm",
                      "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1054200"
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
