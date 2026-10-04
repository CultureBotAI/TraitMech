"""Protect osmotaxis evidence scope and guarded record/proposal creation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_osmotaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "osmotaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_migration_trait_not_uniform_shock_or_universal_chemotaxis():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000592"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "active locomotion produces net migration" in record["definition"]
    assert "spatial gradient in external osmotic conditions" in record["definition"]
    assert not any(k in record for k in ["canonical_examples", "xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True
    boundary, mechanism = record["discussions"]
    assert boundary["status"] == mechanism["status"] == "OPEN"
    for qualifier in ["uniform shock", "passive transport", "not an exact synonym",
                      "can coexist", "does not negate it universally"]:
        assert qualifier in boundary["rationale"]
    assert "life-stage restriction" in mechanism["rationale"]
    assert "taxon-paired protein accessions" in mechanism["rationale"]


def test_three_primary_sources_with_bounded_verbatim_snippets():
    record = writer.build_record()
    assert {e["reference"] for e in record["evidence"]} == {
        writer.LESLIE, writer.BARROS, writer.ROSKO,
    }
    for item in record["evidence"]:
        assert len(item["snippet"]) >= 24
        assert len(item["snippet"].split()) <= 25
        assert "Europe PMC" in item["notes"]
    migration, distinction, model = record["evidence"]
    assert "all substances tested" in migration["snippet"]
    assert "under the tested conditions" in migration["notes"]
    assert "not evidence that all" in migration["notes"]
    assert "antecedent" in distinction["notes"]
    assert "distinguishing chemical from osmotic" in distinction["notes"]
    assert "can lead" in model["snippet"]
    assert "not a direct spatial-gradient migration result" in model["notes"]
    assert "not systematically inspected" in model["notes"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1054600"
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
