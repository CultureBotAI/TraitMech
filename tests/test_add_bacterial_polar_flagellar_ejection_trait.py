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
import add_bacterial_polar_flagellar_ejection_trait as writer  # noqa: E402


def test_source_receipt_is_compact_and_preserves_evidence():
    path = writer.ROOT / "research/traits/physiology/bacterial_polar_flagellar_ejection-source-verification.json"
    raw = path.read_bytes()
    assert len(raw) < 25000
    receipt = json.loads(raw)
    ranges = receipt["allocation"]["full_range_check"]
    assert ranges["owners"] == 189221
    assert ranges["unique_contents"] == 2636
    assert len(ranges["complete_local_audit"]["sha256"]) == 64
    assert [r["snippet"] for r in receipt["rows"]] == [e["snippet"] for e in writer.RECORD["evidence"]]
    assert [r["native_verdict"] for r in receipt["rows"]] == [
        "NOT_IN_ABSTRACT", "VERIFIED", "NOT_IN_ABSTRACT"]
    assert receipt["allocation"]["remote"]["pending_files"] == 812
    assert receipt["allocation"]["drift"]["stable"]


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
    assert record["identifier"] == "traitmech:000732"
    assert record["label"] == "bacterial polar flagellar ejection"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "actively ejects previously assembled axial structures" in record["definition"]
    assert "polar flagellum by separation at its base" in record["definition"]
    assert record["definition_source"] == "DOI:10.1371/journal.pbio.3000165"
    assert [e["reference"] for e in record["evidence"]] == [
        "DOI:10.1371/journal.pbio.3000165", "DOI:10.1111/mmi.14511",
        "DOI:10.1038/s41467-026-75593-6"]
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [12, 9, 15]
    assert "native NOT_IN_ABSTRACT" in record["evidence"][0]["notes"]
    assert writer.SOURCE_LOCATOR in record["evidence"][0]["notes"]
    assert "native VERIFIED" in record["evidence"][1]["notes"]
    assert "not the actual figures or supplement" in record["evidence"][1]["notes"]
    assert "native NOT_IN_ABSTRACT" in record["evidence"][2]["notes"]
    assert "not biological replicates or ejection rates" in record["evidence"][2]["notes"]
    assert "not complete carbon starvation" in record["evidence"][0]["notes"]
    assert "not a directly imaged cut" in record["evidence"][1]["notes"]
    assert len(record["discussions"]) == 4
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
        "TraitMech:data/traits/physiology/bacterial_polar_flagellar_ejection.yaml",
        record["definition_source"],
    ]
    assert "10.1111/mmi.14511" not in rows[2][3]
    assert "10.1038/s41467-026-75593-6" not in rows[2][3]


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


def test_locator_agrees_across_maintained_owners():
    receipt = json.loads((writer.ROOT / "research/traits/physiology/bacterial_polar_flagellar_ejection-source-verification.json").read_text())
    assert writer.SOURCE_LOCATOR in receipt["rows"][0]["locator"]
    assert receipt["rows"][0]["assessment"] == writer.RECORD["evidence"][0]["notes"]
    proposal = (writer.ROOT / "proposals/metpo_traitmech_v608/proposal.md").read_text()
    assert "article1.body1.sec2.sec4.p1" in proposal
    assert "third paragraph" not in proposal


def test_locator_repair_is_narrow_dry_run_and_idempotent(isolated, monkeypatch):
    original = writer.build_record()
    original["evidence"][0]["notes"] = original["evidence"][0]["notes"].replace(
        writer.SOURCE_LOCATOR, writer.OLD_LOCATOR
    )
    writer.TARGET.write_text(yaml.safe_dump(original))
    before = snapshot(isolated)
    monkeypatch.setattr(sys, "argv", ["writer", "--correct-source-locator"])
    assert writer.main() == 0
    assert snapshot(isolated) == before
    monkeypatch.setattr(sys, "argv", ["writer", "--correct-source-locator", "--apply"])
    assert writer.main() == 0
    corrected = yaml.safe_load(writer.TARGET.read_text())
    assert corrected["curation_history"][:-1] == original["curation_history"]
    assert corrected["curation_history"][-1]["action"] == "CORRECT_EVIDENCE_LOCATOR"
    assert corrected["curation_history"][-1]["timestamp"] == writer.LOCATOR_CORRECTION_TIMESTAMP
    assert corrected["evidence"][0]["notes"] == writer.RECORD["evidence"][0]["notes"]
    restored = copy.deepcopy(corrected)
    restored["curation_history"].pop()
    restored["evidence"][0]["notes"] = original["evidence"][0]["notes"]
    assert restored == original
    after = snapshot(isolated)
    assert writer.main() == 0
    assert snapshot(isolated) == after
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshot(isolated) == after


@pytest.mark.parametrize("field", ["identifier", "definition", "evidence", "curation_history"])
def test_locator_repair_preserves_unreviewed_changes(isolated, monkeypatch, field):
    current = writer.build_record()
    current[field] = [] if isinstance(current[field], list) else "Unreviewed change"
    writer.TARGET.write_text(yaml.safe_dump(current))
    before = snapshot(isolated)
    monkeypatch.setattr(sys, "argv", ["writer", "--correct-source-locator", "--apply"])
    with pytest.raises(SystemExit):
        writer.main()
    assert snapshot(isolated) == before


def test_locator_repair_requires_existing_record(isolated, monkeypatch):
    before = snapshot(isolated)
    monkeypatch.setattr(sys, "argv", ["writer", "--correct-source-locator", "--apply"])
    with pytest.raises(SystemExit):
        writer.main()
    assert snapshot(isolated) == before
