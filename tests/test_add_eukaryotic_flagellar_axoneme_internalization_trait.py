"""Protect intact-withdrawal scope, source roles and fail-closed first-pass writes."""

import copy
import csv
import io
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_eukaryotic_flagellar_axoneme_internalization_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000734"
    assert record["label"] == "eukaryotic flagellar axoneme internalization"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "microbial eukaryote internalizes the intact axoneme" in record["definition"]
    assert "of its own cilium or flagellum into its cell body" in record["definition"]
    assert record["definition_source"] == "DOI:10.1002/cm.21637"
    assert [e["reference"] for e in record["evidence"]] == [
        "DOI:10.1002/cm.21637", "DOI:10.1083/jcb.201701074"]
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [5, 14]
    assert all("native NOT_IN_ABSTRACT" in e["notes"] for e in record["evidence"])
    assert "not biological-culture counts" in record["evidence"][0]["notes"]
    assert "16 sampled frames" in record["evidence"][1]["notes"]
    assert "not continuous playback" in record["evidence"][1]["notes"]
    assert "no retraction rate or replicate count" in record["evidence"][1]["notes"]
    context = record["discussions"][0]["evidence"][0]
    assert context["reference"] == "DOI:10.1091/mbc.E24-12-0577"
    assert context["supports"] == "SUPPORT"
    assert "not an additional definition citation" in context["explanation"]
    assert len(context["snippet"].split()) == 9
    assert "Long et al. 2025" in context["notes"]
    assert "native NOT_IN_ABSTRACT" in context["notes"]
    assert "S3F-H" in context["notes"] and "4.5-fold" in context["notes"]
    assert "5.5 +/- 0.2" in context["notes"]
    assert "no organism-level disjointness" in record["discussions"][0]["rationale"]
    assert "broader cilium-disassembly program" in record["discussions"][0]["rationale"]
    assert "complete retractions" in record["discussions"][2]["rationale"]
    assert "excluded cells retaining cilia" in record["discussions"][2]["rationale"]
    assert "content remains unread" in record["discussions"][3]["rationale"]
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
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[:2] == old[:2] and rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID and rows[2][-1] == writer.IDENTIFIER
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == "METPO:1000059" and rows[2][5:7] == ["", ""]
    assert rows[2][3].split("|") == [
        "TraitMech:data/traits/physiology/eukaryotic_flagellar_axoneme_internalization.yaml",
        record["definition_source"],
    ]
    assert "10.1091/mbc.E24-12-0577" not in rows[2][3]
    assert "10.1080/15384101.2017.1360655" not in rows[2][3]


def test_source_receipt_matches_curated_excerpts():
    path = writer.ROOT / f"research/traits/physiology/{writer.SLUG}-source-verification.json"
    receipt = json.loads(path.read_text())
    record = writer.build_record()
    expected = {item["reference"]: item["snippet"] for item in record["evidence"]}
    assert {row["reference"]: row["snippet"] for row in receipt["rows"]} == expected
    assert all(row["role"] == "definition_support" for row in receipt["rows"])
    assert all(row["native_verdict"] == "NOT_IN_ABSTRACT" for row in receipt["rows"])
    context = receipt["scope_context"]
    assert context["reference"] == record["discussions"][0]["evidence"][0]["reference"]
    assert context["snippet"] == record["discussions"][0]["evidence"][0]["snippet"]
    assert context["native_verdict"] == "NOT_IN_ABSTRACT"
    assert context["direct_full_text_match"]
    assert all("native_abstract" not in row for row in receipt["rows"] + [context])
    assert len(receipt["metadata"]) == 6
    assert all(len(row["sha256"]) == 64 for row in receipt["source_assets"])
    assert receipt["manual_html_check"]["later_access_limit"]


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
