"""Protect own-periplasmic withdrawal scope and fail-closed creation."""

import copy
import csv
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_bacterial_flagellar_filament_internalization_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    source = writer.SOURCE_PROPOSAL.read_bytes()
    for name, relative in [("TARGET", "trait.yaml"), ("PROPOSAL", "proposal/classes.tsv"),
                           ("SOURCE_PROPOSAL", "historical.tsv")]:
        monkeypatch.setattr(writer, name, tmp_path / relative)
    writer.SOURCE_PROPOSAL.write_bytes(source)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_source_roles_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000735"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "assembled portion of its own flagellar filament" in record["definition"]
    assert "from outside its cell body into its cell-body periplasm" in record["definition"]
    assert record["definition_source"] == "DOI:10.1038/s41564-023-01401-2"
    assert [e["reference"] for e in record["evidence"]] == [
        "DOI:10.1038/s41564-023-01401-2", "DOI:10.1063/pt.nkma.bqid"]
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [11, 13]
    assert "native NOT_IN_ABSTRACT" in record["evidence"][0]["notes"]
    assert "no same-cell temporal information" in record["evidence"][0]["notes"]
    assert "100 nm, versus 50 nm" in record["evidence"][0]["notes"]
    assert "Native UNRESOLVED" in record["evidence"][1]["notes"]
    assert "not independent experimental replication" in record["evidence"][1]["notes"]
    context = record["discussions"][0]["evidence"][0]
    assert context["reference"] == "DOI:10.1111/j.1365-2958.2006.05081.x"
    assert context["supports"] == "NO_EVIDENCE" and len(context["snippet"].split()) == 14
    assert "not an internalization frequency" in context["notes"]
    assert "native NOT_IN_ABSTRACT" in context["notes"]
    assert "Partial withdrawal counts" in record["discussions"][0]["rationale"]
    assert "static endoflagella" in record["discussions"][0]["rationale"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert not any(record.get(k) for k in ("canonical_examples", "causal_graphs", "synonyms", "xrefs"))
    assert record["curation_history"][-1]["timestamp"] == writer.TIMESTAMP
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"][0]["notes"] = "Mutated"
    assert writer.build_record()["evidence"][0]["notes"] != "Mutated"


def test_proposal_identity_and_citation_roles(isolated):
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    old = list(csv.reader(io.StringIO(writer.SOURCE_PROPOSAL.read_text()), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[:2] == old[:2] and rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID and rows[2][-1] == writer.IDENTIFIER
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == "METPO:1000059" and rows[2][5:7] == ["", ""]
    assert rows[2][3].split("|") == [
        "TraitMech:data/traits/physiology/bacterial_flagellar_filament_internalization.yaml",
        record["definition_source"],
    ]
    assert "05081.x" not in rows[2][3]


def test_source_receipt_matches_curated_excerpts():
    receipt = json.loads((writer.ROOT / f"research/traits/physiology/{writer.SLUG}-source-verification.json").read_text())
    record = writer.build_record()
    assert {r["reference"]: r["snippet"] for r in receipt["rows"]} == {
        r["reference"]: r["snippet"] for r in record["evidence"]}
    assert [r["native_verdict"] for r in receipt["rows"]] == ["NOT_IN_ABSTRACT", "UNRESOLVED"]
    assert all(r["direct_full_text_match"] for r in receipt["rows"])
    context = record["discussions"][0]["evidence"][0]
    assert receipt["scope_context"]["snippet"] == context["snippet"]
    assert receipt["scope_context"]["supports"] == "NO_EVIDENCE"
    assert receipt["scope_context"]["native_verdict"] == "NOT_IN_ABSTRACT"
    assert len(receipt["metadata"]) == 5
    assert all(len(r["sha256"]) == 64 for r in receipt["source_assets"])


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.SOURCE_PROPOSAL.read_bytes() == before["historical.tsv"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("name", ["TARGET", "PROPOSAL", "SOURCE_PROPOSAL"])
def test_conflicting_output_or_dependency_refused(isolated, monkeypatch, name):
    path = getattr(writer, name)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("conflicting: content\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", ["evidence", "definition", "curation_history", "discussions"])
def test_later_curation_preserved(isolated, monkeypatch, field):
    run(monkeypatch, True)
    record = yaml.safe_load(writer.TARGET.read_text())
    record[field] = [] if isinstance(record[field], list) else "Later curation"
    writer.TARGET.write_text(yaml.safe_dump(record))
    before = snapshot(isolated)
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_result_prevalidated_before_any_write(isolated, monkeypatch):
    record = copy.deepcopy(writer.build_record())
    record["unknown_field"] = "invalid"
    monkeypatch.setattr(writer, "build_record", lambda: record)
    before = snapshot(isolated)
    with pytest.raises(Exception):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
