"""Protect chemokinesis identity, evidence qualifications and guarded writes."""

import copy
import csv
import hashlib
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_chemokinesis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "chemokinesis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_speed_response_does_not_require_or_exclude_taxis():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000586"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "swimming speed changes" in record["definition"]
    assert "without requiring directional bias" in record["definition"]
    assert not any(k in record for k in ["xrefs", "synonyms", "causal_graphs"])
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_sources_and_uniform_stimulus_are_qualified_not_canonical():
    record = writer.build_record()
    assert record["definition_source"] == writer.GARREN
    assert {e["reference"] for e in record["evidence"]} == {
        writer.GARREN, writer.SON, writer.GAO, writer.STRAIN,
    }
    for item in record["evidence"]:
        assert 24 <= len(item["snippet"])
        assert len(item["snippet"].split()) <= 25
        assert item["notes"]
    assert not record.get("canonical_examples")
    observed = record["evidence"][1]
    for qualifier in ["YM4", "late exponential", "pH 7.5", "uniform",
                      "5 micromolar serine", "600 mM sodium", "laboratory mutant"]:
        assert qualifier in observed["notes"]
    assert "#1653" in record["curation_history"][-1]["changes"]


def test_hypotheses_are_not_promoted_to_causal_edges():
    record = writer.build_record()
    assert "we hypothesize" in record["evidence"][2]["snippet"]
    boundary, graph = record["discussions"]
    assert boundary["status"] == graph["status"] == "OPEN"
    assert "No equivalence, disjointness" in boundary["rationale"]
    assert "turning-only" in boundary["rationale"]
    assert "not a gene-knockout experiment" in graph["rationale"]
    assert "NONMECHANISTIC" in graph["rationale"]


def test_proposal_record_parity_and_header_padding():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1054000"
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


def test_known_draft_migration_uses_exact_preimage(isolated, monkeypatch):
    draft = writer.build_record()
    draft["definition"] = "Controlled draft fixture."
    digest = hashlib.sha256(json.dumps(draft, sort_keys=True).encode()).hexdigest()
    monkeypatch.setattr(writer, "INITIAL_DRAFT_SHA256", digest)
    writer.write_validated_trait(draft, writer.TARGET)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    draft["label"] = "Unexpected drift"
    writer.write_validated_trait(draft, writer.TARGET)
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before
