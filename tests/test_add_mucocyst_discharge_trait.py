"""Guard discharge scope, proposed-parent dependency and fail-closed writes."""

import csv
import io
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_mucocyst_discharge_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "trait.yaml")
    monkeypatch.setattr(writer, "PARENT_PATH", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal/template.tsv")
    monkeypatch.setattr(writer, "PARENT_PROPOSAL", tmp_path / "parent.tsv")
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    with writer.PARENT_PROPOSAL.open("w", newline="") as handle:
        csv.writer(handle, delimiter="\t", lineterminator="\n").writerows([
            ["proposed_id", "label", "definition", "parent", "traits_addressed"],
            ["ID", "LABEL", "A IAO:0000115", "SC %", ""],
            [writer.PARENT_METPO_ID, writer.PARENT["label"], writer.PARENT["definition"],
             writer.PARENT["parent_traits"][0], writer.PARENT["identifier"]],
        ])
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_scope_and_copy_isolation():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000684"
    assert record["label"] == "mucocyst discharge"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["traitmech:000637"]
    assert all(t in record["definition"] for t in [
        "exocytotic phenotype", "microbial cell", "releases mucocyst contents",
        "fusion of a mucocyst membrane", "plasma membrane",
    ])
    assert all(t not in record["definition"] for t in ["rapid", "calcium", "prey"])
    assert all(record.get(k) is None for k in [
        "causal_graphs", "canonical_examples", "xrefs", "synonyms",
    ])
    event, = record["curation_history"]
    assert event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_source_and_uncertainty_boundaries():
    record = writer.build_record()
    assert record["definition_source"] == writer.MDL1
    assert [e["reference"] for e in record["evidence"]] == [
        writer.MDL1, writer.DIBUCAINE, writer.CTH4,
    ]
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    mdl1, dibucaine, cth4 = record["evidence"]
    assert all(t in mdl1["notes"] for t in [
        "not a count of discharged organelles", "not the Author summary",
        "Figure 4 caption, not image", "not rendered", "phenotypes differ",
    ])
    assert all(t in dibucaine["notes"] for t in [
        "SRC:MED", "Abstract-only access", "not universal requirements",
        "thermophilia (B III)",
    ])
    assert all(t in cth4["notes"] for t in [
        "Abstract-only access", "not a positive mutant exemplar",
        "not imposed on all mucocysts", "no cargo is released",
    ])
    scope, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert all(t in scope["rationale"] for t in [
        "trichocyst discharge traitmech:000683", "mucocyst homologs",
        "fusion without cargo release", "organism-level disjointness",
    ])
    assert all(t in mechanism["rationale"] for t in [
        "Natural culture provenance", "deferred, not claimed absent",
        "sequence features alone", "wildtype designation alone",
    ])


def test_proposal_matches_record_and_parent_mapping():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1063700"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == writer.PARENT_METPO_ID == "METPO:1059000"
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        f"TraitMech:data/traits/physiology/{writer.SLUG}.yaml",
        *(e["reference"] for e in record["evidence"]),
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


@pytest.mark.parametrize("field", ["proposed_id", "label", "definition", "parent", "traits_addressed"])
def test_parent_proposal_drift_refused(isolated, monkeypatch, field):
    rows = list(csv.reader(io.StringIO(writer.PARENT_PROPOSAL.read_text()), delimiter="\t"))
    rows[2][rows[0].index(field)] = "unreviewed"
    with writer.PARENT_PROPOSAL.open("w", newline="") as handle:
        csv.writer(handle, delimiter="\t", lineterminator="\n").writerows(rows)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Parent proposal differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_duplicated_parent_mapping_refused(isolated, monkeypatch):
    lines = writer.PARENT_PROPOSAL.read_text().splitlines(keepends=True)
    writer.PARENT_PROPOSAL.write_text("".join(lines + [lines[2]]))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="Parent proposal differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PROPOSAL", "PARENT_PROPOSAL"])
def test_empty_preimage_refused(isolated, monkeypatch, target):
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("")
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
