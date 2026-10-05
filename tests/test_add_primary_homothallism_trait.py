"""Protect functional primary-homothallism scope and guarded writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_primary_homothallism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "primary_homothallism.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000614"
    assert record["label"] == "primary homothallism"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["traitmech:000609"]
    assert "compatible mating-type determinants co-resident in one genome" in record["definition"]
    assert "without requiring mating-type switching" in record["definition"]
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs"])
    event, = record["curation_history"]
    assert event["llm_assisted"] is True and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["MAT inventory alone is insufficient", "not asserted disjoint",
                 "traitmech:000612", "traitmech:000611", "traitmech:000613",
                 "METPO:1056300"]:
        assert text in scope["rationale"]
    for text in ["not direct ligand-binding", "do not prove genetic unlinkage",
                 "NONMECHANISTIC", "not abstract-resolver VERIFIED"]:
        assert text in mechanism["rationale"]


def test_evidence_and_example_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.DAVID_PALMA
    david, review, paoletti, klix = record["evidence"]
    assert len({e["reference"] for e in record["evidence"]}) == 4
    for evidence in record["evidence"]:
        assert 8 <= len(evidence["snippet"].split()) <= 25
    for text in ["not an abstract quote", "6838", "vestigial sporulation",
                 "caption swaps C/D", "actual Figure 1 E/F", "not significantly reduced"]:
        assert text in david["notes"]
    assert "not experimental replication" in review["notes"]
    assert "scientific abstract" in paoletti["notes"]
    for text in ["subjects are the SmtA-1 and SmtA-3 deletion", "SWG at 24 C",
                 "not individually essential", "no known functional domain",
                 "front matter only"]:
        assert text in klix["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:264483"
    assert example["taxon_label"] == "Phaffia rhodozyma"
    assert example["reference"] == writer.DAVID_PALMA
    for text in ["CBS 6938", "not engineered", "PMC5103461", "UCD 77-61",
                 "32 of 41", "18 C for 10 days", "not independent trait replication"]:
        assert text in example["note"]


def test_proposal_parity_and_released_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1056800"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert all(e["reference"] in rows[2][3] for e in record["evidence"])
    assert rows[2][4] == "METPO:1000059"
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
        record["parent_traits"] = ["METPO:1000059"]
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
