"""Guard oogamy scope, append-only proposal ancestry and preimage protection."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_oogamy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "oogamy.yaml")
    monkeypatch.setattr(writer, "PARENT", tmp_path / "anisogamy.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal.tsv")
    writer.write_validated_trait(writer.parent_writer.build_record(), writer.PARENT)
    writer.PROPOSAL.write_text(writer.parent_writer.proposal_tsv())
    monkeypatch.setattr(writer, "PARENT_SHA", hashlib.sha256(writer.PARENT.read_bytes()).hexdigest())
    monkeypatch.setattr(writer, "PROPOSAL_SHA", hashlib.sha256(writer.PROPOSAL.read_bytes()).hexdigest())
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {p.name: p.read_bytes() for p in root.iterdir() if p.is_file()}


def test_record_scope_and_evidence():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000621"
    assert record["label"] == "oogamy"
    assert record["definition"] == (
        "A sexual-reproduction phenotype in which large nonmotile female gametes "
        "fuse with smaller male gametes."
    )
    assert record["parent_traits"] == ["traitmech:000620"]
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY" and record["term_kind"] == "CLASS"
    assert record["definition_source"] == writer.VRANKEN_2023
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs"])
    scope, hierarchy, native, engineered = record["evidence"]
    assert len({e["reference"] for e in record["evidence"]}) == 4
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "except for red algae" in scope["snippet"]
    assert "also non-motile." in scope["snippet"]
    assert "not a universal rule" in hierarchy["notes"]
    for text in ["possible fertilization", "not 33 independent", "primer polymorphism",
                 "packet size", "uninspected"]:
        assert text in native["notes"]
    for text in ["scientific-abstract", "E15 and A18", "engineered", "not visually rendered",
                 "not a universal oogamy mechanism"]:
        assert text in engineered["notes"]
    event, = record["curation_history"]
    assert event["action"] == "MINTED_TRAITMECH_ID" and event["llm_assisted"]


def test_natural_example_and_open_gaps():
    record = writer.build_record()
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:3068"
    assert example["taxon_label"] == "Volvox carteri f. nagariensis"
    assert example["reference"] == writer.NOZAKI_2018
    for text in ["NIES-4206", "NIES-4208", "LC376032/LC376034", "2016-05-25",
                 "2016-06-09", "2016-06-10", "conflict remains unresolved",
                 "not projected", "not every strain", "id=3068"]:
        assert text in example["note"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "not a MID/MAT sequence feature" in record["discussions"][1]["rationale"]


def test_parent_change_is_scoped():
    before = writer.parent_writer.build_record()
    frozen = copy.deepcopy(before)
    after = writer.build_parent(before)
    assert before == frozen
    assert after["discussions"][0]["status"] == "OPEN"
    assert writer.OLD_SCOPE not in after["discussions"][0]["rationale"]
    assert writer.NEW_SCOPE in after["discussions"][0]["rationale"]
    assert after["curation_history"][:-1] == before["curation_history"]
    for key in before.keys() - {"discussions", "curation_history"}:
        assert before[key] == after[key]
    assert after["discussions"][1:] == before["discussions"][1:]


def test_proposal_is_append_only_with_exact_parent_and_scope():
    record = writer.build_record()
    original = writer.parent_writer.proposal_tsv()
    proposal = writer.proposal_tsv(record)
    assert proposal.startswith(original)
    rows = list(csv.reader(io.StringIO(proposal), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[-1][0] == "METPO:1057410"
    assert rows[-1][1:3] == [record["label"], record["definition"]]
    assert rows[-1][4] == rows[2][0] == "METPO:1057400"
    assert rows[-1][5:7] == ["", ""]
    assert rows[-1][7] == rows[2][7]
    assert rows[-1][-1] == writer.IDENTIFIER
    assert all(e["reference"] in rows[-1][3] for e in record["evidence"])


def test_dry_run_apply_and_idempotent_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["PARENT", "PROPOSAL", "TARGET"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_fails_closed(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    if target == "PROPOSAL":
        path.write_text(path.read_text() + "unreviewed drift\n")
    else:
        record = yaml.safe_load(path.read_text()) if path.exists() else writer.build_record()
        record["label"] = "unreviewed drift"
        writer.write_validated_trait(record, path)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["PARENT", "PROPOSAL"])
def test_missing_preimage_fails_closed(isolated, monkeypatch, target):
    getattr(writer, target).unlink()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Missing reviewed"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_record_cannot_mutate_other_outputs(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    before = snapshot(isolated)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
