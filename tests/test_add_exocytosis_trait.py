"""Guard exocytosis scope, provenance and dry-run/replay mutation safety."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_exocytosis_trait as writer  # noqa: E402


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


def test_identity_and_secretion_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000637"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["trait_category"] == "PHYSIOLOGY"
    assert "releases material" in record["definition"]
    assert "intracellular membrane-bounded compartment" in record["definition"]
    assert "fusion pore" in record["definition"]
    assert "plasma membrane" in record["definition"]
    assert not any(s in record["definition"] for s in ["calcium", "stimulus", "SNARE"])
    assert all(record.get(k) is None for k in [
        "canonical_examples", "causal_graphs", "xrefs", "synonyms",
    ])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_evidence_and_access_limits():
    record = writer.build_record()
    fusion, secretion, boundary = record["evidence"]
    assert record["definition_source"] == fusion["reference"] == writer.FUSION
    assert {e["reference"] for e in record["evidence"]} == {
        writer.FUSION, writer.CONSTITUTIVE, writer.STEP_BOUNDARY,
    }
    assert [len(e["snippet"].split()) for e in record["evidence"]] == [15, 16, 20]
    assert "missing terminal punctuation" in fusion["notes"]
    assert "Fixation triggers some discharge" in fusion["notes"]
    assert "not inspected" in fusion["notes"]
    assert "temperature-sensitive sec mutants" in secretion["notes"]
    assert "Full methods, figures and strain provenance remain unread" in secretion["notes"]
    assert "Figure 9 shows untriggered mutant cells" in boundary["notes"]
    assert "not tnd1 as a positive example" in boundary["notes"]
    scope, gap = record["discussions"]
    assert "fusion alone does not demonstrate cargo release" in scope["rationale"]
    assert "GO:0006887" in scope["rationale"]
    assert "biological process rather than an equivalent" in scope["rationale"]
    assert "Do not infer natural or engineered provenance" in gap["rationale"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1059000"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        "TraitMech:data/traits/physiology/exocytosis.yaml",
        writer.FUSION, writer.CONSTITUTIVE, writer.STEP_BOUNDARY,
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
