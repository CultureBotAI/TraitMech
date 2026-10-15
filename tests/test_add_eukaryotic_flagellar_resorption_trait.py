"""Protect resorption scope, source roles and fail-closed first-pass writes."""

import copy
import csv
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_eukaryotic_flagellar_resorption_trait as writer  # noqa: E402


def test_source_receipt_preserves_evidence_and_bounded_allocation():
    path = writer.ROOT / "research/traits/physiology/eukaryotic_flagellar_resorption-source-verification.json"
    raw = path.read_bytes()
    assert len(raw) < 25000
    receipt = json.loads(raw)
    assert [r["snippet"] for r in receipt["rows"]] == [r["snippet"] for r in writer.RECORD["evidence"]]
    assert [r["native_verdict"] for r in receipt["rows"]] == ["NOT_IN_ABSTRACT", "NOT_IN_ABSTRACT"]
    context = receipt["scope_limitation"]
    assert context["native_verdict"] == "VERIFIED"
    assert context["role"] == "scope_limit_context"
    assert "third sentence" in context["asset"]["locator"]
    allocation = receipt["allocation"]
    assert allocation["identifier"] == writer.IDENTIFIER
    assert allocation["cohort"] == "metpo_traitmech_v609"
    assert allocation["block"] == [1068600, 1068699]
    assert allocation["observed_at"] == writer.TIMESTAMP
    assert allocation["ignored_hidden_included"]
    assert allocation["full_range"]["full_pr_descriptions"] > 0
    assert len(allocation["assessment"]["sha256"]) == 64
    assert receipt["preallocation_guard"]["stable"]


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
    assert record["identifier"] == "traitmech:000733"
    assert record["label"] == "eukaryotic flagellar resorption"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "microbial eukaryote" in record["definition"]
    assert "previously assembled" in record["definition"]
    assert "disassembly of their axonemes" in record["definition"]
    assert record["definition_source"] == "DOI:10.1083/jcb.100.2.457"
    assert [r["reference"] for r in record["evidence"]] == [
        "DOI:10.1083/jcb.100.2.457", "DOI:10.1186/1471-2121-4-11"]
    assert [len(r["snippet"].split()) for r in record["evidence"]] == [8, 9]
    assert all("native NOT_IN_ABSTRACT" in r["notes"] for r in record["evidence"])
    assert "single OCR preformat block" in record["evidence"][0]["notes"]
    assert "short stubs" in record["evidence"][0]["notes"]
    assert "Figure 7 caption" in record["evidence"][1]["notes"]
    assert "not a resorption rate" in record["evidence"][1]["notes"]
    context = record["discussions"][0]["evidence"][0]
    assert context["reference"] == "DOI:10.1002/cm.20454"
    assert context["supports"] == "SUPPORT"
    assert "not an additional definition citation" in context["explanation"]
    assert len(context["snippet"].split()) == 12
    assert "third sentence" in context["notes"] and "native VERIFIED" in context["notes"]
    assert "not the actual figures" in context["notes"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert not any(record.get(k) for k in ("canonical_examples", "causal_graphs", "synonyms", "xrefs"))
    assert record["curation_history"][-1]["llm_assisted"]
    assert record["curation_history"][-1]["timestamp"] == writer.TIMESTAMP
    record["evidence"][0]["notes"] = "Mutated"
    assert writer.build_record()["evidence"][0]["notes"] != "Mutated"


def test_proposal_identity_parent_and_definition_citations(isolated):
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    old = list(csv.reader(io.StringIO(writer.SOURCE_PROPOSAL.read_text()), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[:2] == old[:2] and rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID and rows[2][-1] == writer.IDENTIFIER
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == "METPO:1000059" and rows[2][5:7] == ["", ""]
    assert rows[2][3].split("|") == [
        "TraitMech:data/traits/physiology/eukaryotic_flagellar_resorption.yaml",
        record["definition_source"],
    ]
    assert "10.1002/cm.20454" not in rows[2][3]


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
