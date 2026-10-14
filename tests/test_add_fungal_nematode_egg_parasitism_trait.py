"""Guard egg-infection scope, source boundaries and fail-closed writes."""

import csv
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_nematode_egg_parasitism_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_evidence_and_history():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000726"
    assert record["label"] == "fungal nematode egg parasitism"
    assert "a fungus infects nematode eggs" in record["definition"]
    assert "penetrating their eggshells and colonizing their interiors" in record["definition"]
    assert record["trait_category"] == "ECOLOGY" and record["term_kind"] == "CLASS"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1004002"]
    assert record["definition_source"] == writer.DEFINITION_SOURCE
    assert {e["reference"] for e in record["evidence"]} == {writer.DEFINITION_SOURCE, writer.SUPPORTING_SOURCE}
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [9, 6, 14]
    assert sum(len(e["snippet"].split()) for e in record["evidence"] if e["reference"] == writer.DEFINITION_SOURCE) == 23
    assert not any(record.get(k) for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs", "protein_examples"])
    event, clarification = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert event["action"] == "MINTED_TRAITMECH_ID"
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    assert record["curation_history"][:-1] == writer.build_previous_record()["curation_history"]
    assert clarification["action"] == "CLARIFY_EVIDENCE" and "#1931" in clarification["changes"]
    assert event["timestamp"] < clarification["timestamp"]
    assert datetime.fromisoformat(clarification["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_source_and_scope_qualifiers():
    xu, xie, supplement = writer.build_record()["evidence"]
    for value in ["native VERIFIED", "JZD02", "individual egg", "30-hour", "no numerical infection rates", "6-hour", "42-hour", "not causal protein"]:
        assert value in xu["notes"]
    for value in ["Figure 5", "panel B", "NOT_IN_ABSTRACT", "its own", "36-1", "does not quantify nutrient", "pooled"]:
        assert value in xie["notes"]
    assert supplement["snippet"] == writer.SUPPLEMENT_SNIPPET
    for value in ["Supplementary Table 1 footnote", "NOT_IN_ABSTRACT", "operational scoring", "not another independent experiment", "23 words"]:
        assert value in supplement["notes"]
    scope, ontology, limits = [d["rationale"] for d in writer.build_record()["discussions"]]
    for value in ["Surface attachment", "not an asserted parent", "persistent symbiosis", "No organism-level disjointness", "not an exact synonym"]:
        assert value in scope
    for value in ["METPO:1000227", "deprecated", "no replacement", "not revived", "pin remains unchanged"]:
        assert value in ontology
    for value in ["34.7%", "not silently corrected", "No rates", "not tracer measurements", "No field efficacy", "Both counted primary experiments", "across fungal species"]:
        assert value in limits
    assert all(d["status"] == "OPEN" for d in writer.build_record()["discussions"])


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1067900"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1004002", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10" and rows[2][10] == writer.IDENTIFIER
    assert rows[2][3].split("|") == [f"TraitMech:data/traits/ecology/{writer.SLUG}.yaml", writer.DEFINITION_SOURCE]
    assert writer.SUPPORTING_SOURCE not in rows[2][3]


def test_source_receipt_and_narrative():
    receipt = json.loads((writer.ROOT / f"research/traits/ecology/{writer.SLUG}-source-verification.json").read_text())
    assert receipt["trait_id"] == writer.IDENTIFIER and receipt["accepted_at"] == writer.TIMESTAMP
    assert receipt["native_record_verification"]["exit"] == 0
    assert receipt["native_record_verification"]["report_rows"] == 3
    assert receipt["reservation_assessment"]["conflicting_reservations"] == []
    assert [r["native_verdict"] for r in receipt["rows"]] == ["VERIFIED", "NOT_IN_ABSTRACT", "NOT_IN_ABSTRACT"]
    assert receipt["evidence_clarification"]["combined_xu_words"] == 23
    assert receipt["evidence_clarification"]["distinct_primary_experiments"] == 2
    for row, evidence in zip(receipt["rows"], writer.build_record()["evidence"], strict=True):
        assert row["reference"] == evidence["reference"] and row["snippet"] == evidence["snippet"]
        assert row["words"] == len(row["snippet"].split()) <= 25
        assert row["source_identity_verified"] and row["direct_source_match"]
        assert len(row["source"]["sha256"]) == 64
    narrative = (writer.PROPOSAL.parent / "proposal.md").read_text()
    assert "Only Xu and the local record annotate the proposal definition" in narrative
    assert "`NOT_IN_ABSTRACT` is retained" in narrative


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


def test_reviewed_previous_record_migrates_without_rewriting_history(isolated, monkeypatch):
    previous = writer.build_previous_record()
    writer.write_validated_trait(previous, writer.TARGET)
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    result = yaml.safe_load(writer.TARGET.read_text())
    assert result == writer.build_record()
    assert result["curation_history"][:-1] == previous["curation_history"]
    assert result["evidence"][:2] == previous["evidence"]
    for field in ["identifier", "label", "definition", "definition_source", "parent_traits", "mapping_status"]:
        assert result[field] == previous[field]
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_refused_without_partial_write(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field,value", [("identifier", "METPO:9999999"), ("label", "other"),
    ("mapping_status", "PROPOSED"), ("parent_traits", []), ("definition", "changed")])
def test_parent_drift_refused(isolated, monkeypatch, field, value):
    writer.write_validated_trait(dict(writer.PARENT, **{field: value}), writer.PARENT_PATH)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Parent"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_record_rejected_before_write(isolated, monkeypatch):
    monkeypatch.setattr(writer, "build_record", lambda: dict(writer.RECORD, unexpected_field=True))
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
