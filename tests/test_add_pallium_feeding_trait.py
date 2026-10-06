"""Guard feeding topology, evidence limits and fail-closed writing."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_pallium_feeding_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    parent = {**writer.PARENT, "trait_category": "UPPER", "term_kind": "CLASS"}
    writer.write_validated_trait(parent, writer.PARENT_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_evidence():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000632"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "all or part of particulate food" in record["definition"]
    assert "outside the main cell body" in record["definition"]
    assert "taking up released nutrients" in record["definition"]
    assert all(s not in record["definition"] for s in ["extracellular", "living", "diatom"])
    assert record["definition_source"] == writer.DEFINITION
    assert {e["reference"] for e in record["evidence"]} == {
        writer.DEFINITION, writer.ULTRASTRUCTURE, writer.GROWTH,
    }
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]


def test_source_and_topology_limits_remain_explicit():
    first, second, third = writer.build_record()["evidence"]
    assert "Direct scientific Abstract quote" in first["notes"]
    assert "Pages 253-255 and Figures 3-22 are missing" in first["notes"]
    assert "not an abstract quote" in second["notes"]
    assert "loss during fixation versus in vivo reorganization unresolved" in second["notes"]
    assert "Only the abstract was inspected" in third["notes"]
    discussion = writer.build_record()["discussions"][0]["rationale"]
    assert "complete enclosure intracellular" in discussion
    assert "partial enclosure extracellular" in discussion


def test_canonical_example_has_qualified_natural_provenance():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:402581"
    assert example["taxon_label"] == "Oblea rotunda"
    assert example["reference"] == writer.DEFINITION
    assert writer.PROVENANCE in example["note"]
    assert "naturally collected specimens" in example["note"]
    assert "No strain identifier or single collection site" in example["note"]


def test_proposal_matches_record_and_preserves_header_width():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_refused_without_partial_writes(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    if target == "PARENT_PATH":
        parent = yaml.safe_load(path.read_text())
        parent["definition"] = "Unreviewed scope change"
        writer.write_validated_trait(parent, path)
    else:
        path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_empty_target_refused(isolated, monkeypatch):
    writer.TARGET.touch()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
