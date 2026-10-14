"""Guard hatch-stimulation identity, source roles and fail-closed writes."""

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
import add_nematode_egg_hatching_stimulatory_activity_trait as writer  # noqa: E402


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
    assert record["identifier"] == "traitmech:000724"
    assert record["label"] == "nematode egg-hatching stimulatory activity"
    assert "microorganism to increase nematode egg hatching" in record["definition"]
    assert "defined observation interval" in record["definition"]
    assert "comparable controls without that microbial influence" in record["definition"]
    assert record["trait_category"] == "PHYSIOLOGY" and record["term_kind"] == "CLASS"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition_source"] == writer.DEFINITION_SOURCE
    assert len({e["reference"] for e in record["evidence"]}) == 2
    assert all(e["reference"].startswith("DOI:") for e in record["evidence"])
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [17, 19]
    assert not any(record.get(k) for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs", "protein_examples"])
    event, = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert event["action"] == "MINTED_TRAITMECH_ID"
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 2


def test_source_and_assay_qualifiers():
    meyer, vejzagic = writer.build_record()["evidence"]
    for value in ["UNRESOLVED", "14 days", "motile and immotile", "PDB hatch", "Forty isolates", "splits controls"]:
        assert value in meyer["notes"]
    for value in ["VERIFIED", "own bacterial experiment", "bacteria-free controls", "20 h", "variability", "excludes near-zero controls"]:
        assert value in vejzagic["notes"]
    scope, limits = [d["rationale"] for d in writer.build_record()["discussions"]]
    for value in ["not merely lack of inhibition", "Embryogenesis without emergence", "No organism-level disjointness", "Neither host-generalism"]:
        assert value in scope
    for value in ["nutrient depletion", "culture age can reverse", "script shells", "not current-status verdicts"]:
        assert value in limits
    assert all(d["status"] == "OPEN" for d in writer.build_record()["discussions"])


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1067700"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1000059", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10" and rows[2][10] == writer.IDENTIFIER
    assert rows[2][3].split("|") == [f"TraitMech:data/traits/physiology/{writer.SLUG}.yaml", writer.DEFINITION_SOURCE]
    assert writer.SUPPORTING_SOURCE not in rows[2][3]


def test_source_receipt_and_narrative():
    receipt = json.loads((writer.ROOT / f"research/traits/physiology/{writer.SLUG}-source-verification.json").read_text())
    record = writer.build_record()
    assert receipt["trait_id"] == writer.IDENTIFIER and receipt["accepted_at"] == writer.TIMESTAMP
    assert receipt["native_record_verification"]["exit"] == 0
    assert receipt["native_record_verification"]["report_rows"] == 2
    assert receipt["allocation"]["reservation_adjudication"]["conflicting_reservations"] == []
    assert [r["native_verdict"] for r in receipt["rows"]] == ["UNRESOLVED", "VERIFIED"]
    for row, evidence in zip(receipt["rows"], record["evidence"], strict=True):
        assert row["reference"] == evidence["reference"] and row["snippet"] == evidence["snippet"]
        assert row["words"] == len(row["snippet"].split()) <= 25
        assert row["source_identity_verified"] and row["direct_source_match"]
        assert len(row["source"]["sha256"]) == 64
    assert receipt["rows"][0]["exact_normalized_text_layer_match"] is False
    narrative = (writer.PROPOSAL.parent / "proposal.md").read_text()
    assert "Only Meyer and the local record annotate the proposal definition" in narrative
    assert "not native `VERIFIED`" in narrative


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
