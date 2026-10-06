"""Guard selective ER degradation and unchanged parent-proposal context."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_er_phagy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PARENT_PROPOSAL", tmp_path / "parent.tsv")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    writer.PARENT_PROPOSAL.write_text(writer.tsv([*writer.HEADERS, writer.PARENT_ROW]))
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_selectivity_and_route_inclusive_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000642"
    assert record["label"] == "ER-phagy"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000638"]
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["definition"].startswith("An autophagy phenotype")
    assert "selectively degrades portions of its endoplasmic reticulum" in record["definition"]
    assert "lysosomal or vacuolar compartments" in record["definition"]
    assert not any(s in record["definition"] for s in ["starvation", "stress", "Atg", "macro"])
    assert all(record.get(k) is None for k in [
        "canonical_examples", "causal_graphs", "xrefs", "synonyms",
    ])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_evidence_selectivity_flux_and_access_limits():
    record = writer.build_record()
    micro, macro, routes = record["evidence"]
    assert record["definition_source"] == routes["reference"] == writer.ROUTES
    assert {e["reference"] for e in record["evidence"]} == {
        writer.MICRO, writer.MACRO, writer.ROUTES,
    }
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all("Scientific Abstract directly read" in e["notes"] for e in record["evidence"])
    assert "ER-phagy degrades excess ER membrane" in micro["snippet"]
    assert "DTT and tunicamycin interfere with vacuolar proteolysis" in micro["notes"]
    assert "not completed degradation" in micro["notes"]
    assert "partly disintegrated" in micro["notes"]
    assert "derive from W303" in micro["notes"]
    assert "not make ER-phagy and nucleophagy synonyms" in macro["notes"]
    assert "qualified as probable" in macro["notes"]
    assert "Full text, actual figures" in macro["notes"]
    assert "distinct molecular requirements" in routes["snippet"]
    assert "not micro-ER-phagy-specific absence tests" in routes["notes"]
    assert "Atg40 is dispensable" in routes["notes"]
    assert "background correction" in routes["notes"]
    scope, gap = record["discussions"]
    assert all(curie in scope["rationale"] for curie in ["GO:0061709", "traitmech:000638"])
    assert "process-to-phenotype shift" in scope["rationale"]
    assert "route-inclusive phenotype" in scope["rationale"]
    assert "natural strain provenance has not been independently verified" in gap["rationale"]


def test_proposal_preserves_parent_and_child_parity():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[:2] == writer.HEADERS
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2] == writer.PARENT_ROW
    assert rows[2][0] == writer.PARENT_METPO_ID == "METPO:1059100"
    assert rows[3][0] == writer.METPO_ID == "METPO:1059500"
    assert rows[3][1:3] == [record["label"], record["definition"]]
    assert rows[3][4] == rows[2][0]
    assert rows[3][5:7] == ["", ""]
    assert rows[3][10] == writer.IDENTIFIER
    assert set(rows[3][3].split("|")) == {
        "TraitMech:data/traits/physiology/er_phagy.yaml",
        writer.MICRO, writer.MACRO, writer.ROUTES,
    }


def test_dry_run_apply_replay_preserves_parent(isolated, monkeypatch):
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    assert writer.PARENT_PROPOSAL.read_bytes() == before["parent.tsv"]
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PROPOSAL"])
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


@pytest.mark.parametrize("field", list(writer.PARENT))
def test_parent_projection_drift_refused(isolated, monkeypatch, field):
    parent = dict(writer.PARENT)
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PARENT_PROPOSAL"])
def test_empty_context_refused(isolated, monkeypatch, target):
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
