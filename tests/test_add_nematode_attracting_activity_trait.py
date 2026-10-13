"""Guard attraction scope, citation roles and fail-closed curation."""

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
import add_nematode_attracting_activity_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000721"
    assert record["label"] == "nematode-attracting activity"
    assert "microorganism to elicit directed movement of nematodes" in record["definition"]
    assert record["trait_category"] == "PHYSIOLOGY" and record["term_kind"] == "CLASS"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition_source"] == writer.DEFINITION_SOURCE
    assert len({e["reference"] for e in record["evidence"]}) == 2
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [14, 16]
    assert not any(record.get(k) for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs", "protein_examples"])
    event, = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert event["action"] == "MINTED_TRAITMECH_ID"
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 2


def test_source_and_assay_qualifiers():
    fungal, bacterial = writer.build_record()["evidence"]
    for value in ["scientific abstract", "VERIFIED", "CBS 115.81", "L1/dauer", "not the capture image", "Sodium azide"]:
        assert value in fungal["notes"]
    for value in ["NOT_IN_ABSTRACT", "Discussion", "YSM0385", "glucose plus citrate", "1 h", "Y091"]:
        assert value in bacterial["notes"]
    scope, limits = [d["rationale"] for d in writer.build_record()["discussions"]]
    for value in ["not its own chemotaxis", "Passive retention", "killing or consumption", "No exact synonyms"]:
        assert value in scope
    for value in ["medium-control signal", "ky32", "ky10", "S2 diacetyl", "unchecked", "No shared microbial mechanism"]:
        assert value in limits
    assert all(d["status"] == "OPEN" for d in writer.build_record()["discussions"])


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1067400"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1000059", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10" and rows[2][10] == writer.IDENTIFIER
    assert rows[2][3].split("|") == [f"TraitMech:data/traits/physiology/{writer.SLUG}.yaml", writer.DEFINITION_SOURCE]


def test_source_receipt_and_narrative():
    receipt = json.loads((writer.ROOT / f"research/traits/physiology/{writer.SLUG}-source-verification.json").read_text())
    record = writer.build_record()
    assert receipt["trait_id"] == writer.IDENTIFIER and receipt["accepted_at"] == writer.TIMESTAMP
    assert [r["reference"] for r in receipt["rows"]] == [e["reference"] for e in record["evidence"]]
    assert [r["native_verdict"] for r in receipt["rows"]] == ["VERIFIED", "NOT_IN_ABSTRACT"]
    assert receipt["native_record_verification"]["exit"] == 0
    assert receipt["allocation"]["reservation_adjudication"]["conflicting_reservations"] == []
    for row, evidence in zip(receipt["rows"], record["evidence"], strict=True):
        assert row["snippet"] == evidence["snippet"]
        assert row["words"] == len(row["snippet"].split()) <= 25
        assert row["exact_contiguous_span"] and row["source_identity_verified"]
        assert len(row["source"]["sha256"]) == 64
    narrative = (writer.PROPOSAL.parent / "proposal.md").read_text()
    assert "14-word scientific-abstract" in narrative and "16-word Discussion" in narrative
    assert "Only Hsueh and the local record annotate the proposal definition" in narrative
    assert "not microbial chemotaxis" in narrative and "S2 calibration" in narrative


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


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
    parent = dict(writer.PARENT, **{field: value})
    writer.write_validated_trait(parent, writer.PARENT_PATH)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Parent"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_invalid_record_rejected_before_write(isolated, monkeypatch):
    invalid = dict(writer.build_record(), unexpected_field=True)
    monkeypatch.setattr(writer, "build_record", lambda: invalid)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
