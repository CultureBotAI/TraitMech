"""Protect shedding scope, citation roles and fail-closed first-pass writes."""

import copy
import csv
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_eukaryotic_flagellar_autotomy_trait as writer  # noqa: E402


def test_source_receipt_is_compact_and_preserves_evidence():
    path = writer.ROOT / "research/traits/physiology/eukaryotic_flagellar_autotomy-source-verification.json"
    raw = path.read_bytes()
    assert len(raw) < 25000
    receipt = json.loads(raw)
    ranges = receipt["allocation"]["full_range_check"]
    assert ranges["owners"] == 184357
    assert ranges["unique_contents"] == 2662
    assert len(ranges["complete_local_audit"]["sha256"]) == 64
    assert [r["snippet"] for r in receipt["rows"]] == [e["snippet"] for e in writer.RECORD["evidence"]]
    assert [r["native_verdict"] for r in receipt["rows"]] == ["VERIFIED", "NOT_IN_ABSTRACT"]
    assert receipt["mechanism_limitation"]["native_verdict"] == "NOT_IN_ABSTRACT"
    assert receipt["prepublication_remote_reassessment"]["nonremoved_files_checked"] == 88


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
    assert record["identifier"] == "traitmech:000731"
    assert record["label"] == "eukaryotic flagellar autotomy"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "microbial eukaryote" in record["definition"]
    assert "regulated severing of their axonemes near the base" in record["definition"]
    assert record["definition_source"] == "DOI:10.1186/1471-2121-4-11"
    assert [e["reference"] for e in record["evidence"]] == [
        "DOI:10.1186/1471-2121-4-11", "DOI:10.1534/g3.116.034264"]
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [10, 15]
    assert "native VERIFIED" in record["evidence"][0]["notes"]
    assert "calcium-containing medium, not reference strain WTB214" in record["evidence"][0]["notes"]
    assert "NOT_IN_ABSTRACT" in record["evidence"][1]["notes"]
    assert "biflagellate cells per 100 cells" in record["evidence"][1]["notes"]
    context = record["discussions"][2]["evidence"][0]
    assert context["reference"] == "DOI:10.1242/jcs.096941"
    assert context["supports"] == "SUPPORT"
    assert "not an additional definition citation" in context["explanation"]
    assert len(context["snippet"].split()) == 10
    assert "NOT_IN_ABSTRACT" in context["notes"]
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
        "TraitMech:data/traits/physiology/eukaryotic_flagellar_autotomy.yaml",
        record["definition_source"],
    ]
    assert "10.1242/jcs.096941" not in rows[2][3]


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
