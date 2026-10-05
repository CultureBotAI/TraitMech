"""Protect recombination-permitting mating scope and fail-closed writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_pseudobipolar_mating_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "pseudobipolar_mating_system.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000617"
    assert record["label"] == "pseudobipolar mating system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    for text in ["same chromosome", "can recombine during meiosis", "compatibility loci"]:
        assert text in record["definition"]
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs", "canonical_examples"])
    event, = record["curation_history"]
    assert event["action"] == "MINTED_TRAITMECH_ID"
    assert event["llm_assisted"] and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["2010", "2025", "fixed rate", "traitmech:000616",
                 "traitmech:000615", "disjointness", "traitmech:000610"]:
        assert text in scope["rationale"]
    for text in ["not an independently sampled natural", "gene conversion",
                 "eight-teliospore", "protein accessions", "NONMECHANISTIC"]:
        assert text in mechanism["rationale"]


def test_source_roles_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.COELHO_2010
    early, modern = record["evidence"]
    assert len({e["reference"] for e in record["evidence"]}) == 2
    for evidence in record["evidence"]:
        assert 8 <= len(evidence["snippet"].split()) <= 25
    assert early["snippet"].endswith("originate new mating types.")
    assert modern["snippet"].endswith("same chromosome but genetically unlinked")
    for text in ["not the author summary", "one parental cross", "mitotic clones",
                 "apparently diploid", "statistically significant linkage",
                 "assumes S. roseus synteny", "A2-15", "A2-6",
                 "results not shown", "unresolved"]:
        assert text in early["notes"]
    for text in ["not an independent functional replication", "likely heterothallic",
                 "sec017", "conditional", "does not exclude", "cannot be transferred",
                 "remain uninspected"]:
        assert text in modern["notes"]


def test_proposal_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1057100"
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
    before = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == before


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_drift_refused_without_partial_writes(isolated, monkeypatch, target):
    if target == "record":
        record = writer.build_record()
        record["parent_traits"] = ["traitmech:000616"]
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
