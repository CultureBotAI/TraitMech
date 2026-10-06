"""Guard autophagy scope, evidence and fail-closed curation writes."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_autophagy_trait as writer  # noqa: E402


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


def test_identity_and_catabolic_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000638"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["trait_category"] == "PHYSIOLOGY"
    assert "degrades cytoplasmic material" in record["definition"]
    assert "own constituents or intracellular non-self cargo" in record["definition"]
    assert "lysosomal or vacuolar compartments" in record["definition"]
    assert not any(s in record["definition"] for s in ["starvation", "double-membrane", "ATG"])
    assert all(record.get(k) is None for k in [
        "canonical_examples", "causal_graphs", "xrefs", "synonyms",
    ])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 4


def test_evidence_and_access_limits():
    record = writer.build_record()
    yeast, routes, defense, flux = record["evidence"]
    assert record["definition_source"] == yeast["reference"] == writer.YEAST
    assert {e["reference"] for e in record["evidence"]} == {
        writer.YEAST, writer.ROUTES, writer.HOST_DEFENSE, writer.FLUX,
    }
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "not inhibited-body accumulation alone" in yeast["notes"]
    assert "full methods, actual figures" in yeast["notes"]
    assert "Publisher full text requires access" in routes["notes"]
    assert "not direct proof of completed cargo degradation" in defense["notes"]
    assert "nematode insulin-signaling results are not transferred" in defense["notes"]
    assert "block is partial" in flux["notes"]
    assert "Figure 6 and supplemental S6 Figure" in flux["notes"]
    scope, gap = record["discussions"]
    assert "Selective and bulk turnover" in scope["rationale"]
    assert "GO:0006914" in scope["rationale"]
    assert "biological process rather than an equivalent" in scope["rationale"]
    assert "Do not infer natural or engineered origin" in gap["rationale"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1059100"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        "TraitMech:data/traits/physiology/autophagy.yaml",
        writer.YEAST, writer.ROUTES, writer.HOST_DEFENSE, writer.FLUX,
    }


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


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_existing_drift_refused_without_partial_write(isolated, monkeypatch, target, after_apply):
    if after_apply:
        run(monkeypatch, True)
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("unreviewed drift\n")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", list(writer.PARENT))
def test_parent_projection_drift_refused(isolated, monkeypatch, field):
    parent = dict(writer.PARENT)
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH"])
def test_empty_record_refused(isolated, monkeypatch, target):
    getattr(writer, target).write_text("")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_prevalidation_failure_writes_nothing(isolated, monkeypatch):
    bad = writer.build_record()
    bad["unrecognized_field"] = "must not be written"
    monkeypatch.setattr(writer, "build_record", lambda: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
