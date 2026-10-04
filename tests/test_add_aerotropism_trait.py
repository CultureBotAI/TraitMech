"""Protect aerotropism scope, evidence limits and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_aerotropism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "aerotropism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_growth_definition_and_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000601"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["traitmech:000597"]
    assert record["definition"] == (
        "A phenotype in which polarized growth is directionally "
        "biased in response to a spatial oxygen concentration gradient."
    )
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs",
                                       "canonical_examples"])
    assert record["curation_history"][-1]["llm_assisted"] is True
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["positive or negative", "Aerotaxis", "rheotropism",
                      "extension rate alone", "not released", "METPO:1000059"]:
        assert qualifier in boundary["rationale"]
    for qualifier in ["preferential growth", "natural strain", "NCBI identity",
                      "taxon-paired protein accessions", "NONMECHANISTIC"]:
        assert qualifier in mechanism["rationale"]


def test_evidence_access_and_mechanism_are_qualified():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {
        writer.DAMM, writer.BRAND,
    }
    assert record["definition_source"] == writer.DAMM
    tubes, review = record["evidence"]
    assert all(e.get("snippet") for e in record["evidence"])
    assert "not independent experimental replication" in review["notes"]
    assert "Creative Commons Attribution" in review["notes"]
    assert "describe galvanotropism, not aerotropism" in review["notes"]
    assert "aerotropism under hypoxic conditions" in review["snippet"]
    assert review["snippet"].endswith("[94, 97, 98].")
    leads = record["discussions"][1]["rationale"]
    for qualifier in (writer.AOKI, writer.CARLILE, "metadata only", "unverified",
                      "not definition authority or counted trait evidence"):
        assert qualifier in leads
    assert "negative response" in record["discussions"][0]["rationale"]
    assert 24 <= len(tubes["snippet"]) and len(tubes["snippet"].split()) <= 25
    assert len(record["curation_history"]) == 4
    assert "#1676" in record["curation_history"][1]["changes"]
    assert "#1678 and #1679" in record["curation_history"][2]["changes"]
    assert "now-withdrawn quotes" in record["curation_history"][2]["changes"]
    assert "#1680 and #1681" in record["curation_history"][-1]["changes"]
    assert "No new snippet-baseline exceptions" in record["curation_history"][-1]["changes"]
    assert "does not establish significance" in tubes["notes"]
    assert "germination, not orientation" in tubes["notes"]
    assert "not visually verified" in tubes["notes"]


def test_proposal_record_parity_and_pending_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1055500"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert writer.DAMM in rows[2][3] and writer.BRAND in rows[2][3]
    assert writer.AOKI not in rows[2][3] and writer.CARLILE not in rows[2][3]
    assert rows[2][4] == "METPO:1000059"
    assert rows[2][2].startswith("A phenotype in which")
    assert "v474 acceptance" in rows[2][9]
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
        record["parent_traits"] = ["METPO:1000702"]
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
