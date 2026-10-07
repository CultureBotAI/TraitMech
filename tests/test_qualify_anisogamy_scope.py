"""Check the scope repair and refuse drift before either output is changed."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import qualify_anisogamy_scope as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "anisogamy.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal.tsv")
    writer.write_validated_trait(writer.original.build_record(), writer.TARGET)
    writer.PROPOSAL.write_text(writer.original.proposal_tsv(writer.original.build_record()))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {p.name: p.read_bytes() for p in root.iterdir()}


def test_scope_repair_preserves_definition_and_example():
    before, after = writer.original.build_record(), writer.build_record()
    for key in ["identifier", "label", "definition", "definition_source",
                "parent_traits", "mapping_status", "canonical_examples"]:
        assert after[key] == before[key]
    assert after["evidence"][:-1] == before["evidence"]
    evidence = after["evidence"][-1]
    assert evidence["reference"] == writer.REFERENCE
    assert len(evidence["snippet"].split()) == 17
    assert "not evidence" in evidence["notes"]
    scope = after["discussions"][0]["rationale"]
    assert "not equivalent to the size-based sense" in scope
    assert "alone do not establish" in scope
    assert "exact synonym" in scope and "organism-level disjointness" in scope
    assert after["curation_history"][:-1] == before["curation_history"]
    assert "#1711" in after["curation_history"][-1]["changes"]
    assert after["curation_history"][-1]["llm_assisted"]
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv()), delimiter="\t"))
    assert {len(r) for r in rows} == {11}
    assert rows[2][1:3] == [after["label"], after["definition"]]
    assert all(e["reference"] in rows[2][3] for e in after["evidence"])


def test_dry_run_apply_replay(isolated, monkeypatch):
    before = snapshots(isolated)
    assert run(monkeypatch) == 0
    assert snapshots(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    after = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == after


@pytest.mark.parametrize("field", ["identifier", "label", "mapping_status", "parent_traits",
                                   "discussions", "proposal"])
def test_unreviewed_drift_is_refused(isolated, monkeypatch, field):
    if field == "proposal":
        writer.PROPOSAL.write_text("Unreviewed drift")
    else:
        record = writer.original.build_record()
        record[field] = {
            "identifier": "traitmech:999999", "label": "different label",
            "mapping_status": "REVIEWED", "parent_traits": ["traitmech:000619"],
            "discussions": [],
        }[field]
        writer.write_validated_trait(record, writer.TARGET)
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


def test_invalid_result_leaves_both_outputs_unchanged(isolated, monkeypatch):
    bad = writer.build_record()
    bad["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshots(isolated)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before
