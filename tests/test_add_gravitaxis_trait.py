"""Protect gravitaxis evidence scope and guarded creation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_gravitaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "gravitaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_directional_swimming_without_a_universal_receptor_or_polarity():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000584"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "direction of active swimming" in record["definition"]
    assert "relative to gravity" in record["definition"]
    assert "receptor" not in record["definition"]
    assert "upward" not in record["definition"]
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_primary_sources_and_context_qualified_species_examples():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {writer.NASIR, writer.ROBERTS}
    for item in record["evidence"]:
        assert 24 <= len(item["snippet"])
        assert len(item["snippet"].split()) <= 25
        assert item["notes"]
    euglena, paramecium = record["canonical_examples"]
    assert (euglena["taxon_id"], euglena["taxon_label"]) == (
        "NCBITaxon:3039", "Euglena gracilis",
    )
    assert euglena["reference"] == writer.NASIR
    assert "buffer-only electroporation" in euglena["note"]
    assert "not the RNAi knockdowns" in euglena["note"]
    assert (paramecium["taxon_id"], paramecium["taxon_label"]) == (
        "NCBITaxon:5885", "Paramecium caudatum",
    )
    assert paramecium["reference"] == writer.ROBERTS
    assert "one-week-old" in paramecium["note"]
    assert all("species-level" in e["note"] for e in record["canonical_examples"])


def test_source_locators_and_graph_mapping_gaps_are_explicit():
    record = writer.build_record()
    nasir, roberts = record["evidence"]
    assert "Supplementary Figure 5e" in nasir["notes"]
    assert "not identical" in nasir["notes"]
    assert "not measured simultaneously" in roberts["notes"]
    boundary, graph = record["discussions"]
    assert boundary["status"] == graph["status"] == "OPEN"
    assert "biological process rather than" in boundary["rationale"]
    assert "not an exact synonym or a disjoint phenotype" in boundary["rationale"]
    assert "without a Proteomes cross-reference" in graph["rationale"]
    assert "does not establish sequence absence" in graph["rationale"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1053800"
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
