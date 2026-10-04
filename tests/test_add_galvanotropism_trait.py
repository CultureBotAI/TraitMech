"""Protect electric-field growth scope, stage distinctions and guarded creation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_galvanotropism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "galvanotropism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_distinguishes_growth_from_taxis_and_fixed_polarity():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000595"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "growth is directionally oriented or reoriented" in record["definition"]
    assert "electric field" in record["definition"]
    assert not any(w in record["definition"] for w in ["cathode", "anode", "motile"])
    assert not any(k in record for k in ["canonical_examples", "xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["not whole-cell locomotion", "not motile", "traitmech:000581",
                      "traitmech:000594", "Passive displacement", "electron uptake"]:
        assert qualifier in boundary["rationale"]
    for qualifier in ["establishment", "maintenance", "engineered", "taxon-paired",
                      "actin-absence", "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_three_sources_preserve_controls_and_stage_boundaries():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {
        writer.RAJNICEK, writer.CROMBIE, writer.BRAND,
    }
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
    bacterial, fungal, calcium = record["evidence"]
    assert "(but not control)" in bacterial["snippet"]
    assert "toward the anode" in bacterial["snippet"]
    assert "passive bending" in bacterial["notes"]
    assert "not adopted as current biology" in bacterial["notes"]
    assert "towards the cathode" in fungal["snippet"]
    assert "not themselves directional growth" in fungal["notes"]
    assert "not an abstract quote" in calcium["notes"]
    for qualifier in ["low-calcium", "primarily reduced cathodal emergence",
                      "tip orientation could recover", "not thigmotropism",
                      "proposed model", "CAI4/CIp10", "NGY152"]:
        assert qualifier in calcium["notes"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1054900"
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
