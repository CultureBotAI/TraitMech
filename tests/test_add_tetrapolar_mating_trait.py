"""Protect functional tetrapolar-mating scope and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_tetrapolar_mating_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "tetrapolar_mating_system.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000615"
    assert record["label"] == "tetrapolar mating system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "two independently segregating mating-type factors" in record["definition"]
    assert "different specificities at both factors" in record["definition"]
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs"])
    event, = record["curation_history"]
    assert event["llm_assisted"] is True and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["not possession", "not a guarantee", "traitmech:000610",
                 "universal self-sterility", "bifactorial"]:
        assert text in scope["rationale"]
    for text in ["unsuccessful cross", "protein accessions", "NONMECHANISTIC",
                 "actual verdict"]:
        assert text in mechanism["rationale"]


def test_evidence_and_example_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.FINDLEY
    findley, maia = record["evidence"]
    assert len({e["reference"] for e in record["evidence"]}) == 2
    for evidence in record["evidence"]:
        assert 8 <= len(evidence["snippet"].split()) <= 25
    for text in ["not an abstract quote", "complementary recombinants",
                 "not an observed equal-ratio", "not page-rendered",
                 "include blastospores", "F1S2 #16", "remain uninspected"]:
        assert text in findley["notes"]
    for text in ["scientific abstract", "linkage disequilibrium", "two thirds nonhaploid",
                 "HTTP 500/403", "no canonical example"]:
        assert text in maia["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:104669"
    assert example["taxon_label"] == "Cryptococcus amylolentus"
    assert example["reference"] == writer.FINDLEY
    for text in ["CBS6039 x CBS6273", "Natural provenance", "insect frass",
                 "V8 pH 5", "24 C", "two-week", "not hyphae alone"]:
        assert text in example["note"]


def test_proposal_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056900"
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
        record["parent_traits"] = ["traitmech:000610"]
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
