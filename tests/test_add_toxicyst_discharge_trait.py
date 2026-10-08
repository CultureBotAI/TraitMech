"""Guard source-bounded toxicyst scope and fail-closed curated writes."""

import csv
import io
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_toxicyst_discharge_trait as writer  # noqa: E402


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


def test_scope_and_copy_isolation():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000685"
    assert record["label"] == "toxicyst discharge"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert all(t in record["definition"] for t in [
        "physiological phenotype", "microbial cell", "releases material",
        "toxicysts", "offensive extrusomes", "cell exterior",
    ])
    assert all(t not in record["definition"] for t in [
        "fusion", "calcium", "prey killing", "all", "rapid",
    ])
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
    assert record["definition_source"] == writer.COLEPS
    assert [e["reference"] for e in record["evidence"]] == [
        writer.COLEPS, writer.CALCIUM, writer.GENOMICS,
    ]
    assert all(5 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    coleps, calcium, genomics = record["evidence"]
    assert all(t in coleps["notes"] for t in [
        "SRC:MED", "Abstract-only access", "access-restricted", "living cells",
        "not a universal toxicyst cargo",
    ])
    assert all(t in calcium["notes"] for t in [
        "8/11", "1/11", "pressure injection", "caused damage",
        "Figures were not visually inspected", "No PMID was resolved",
    ])
    assert all(t in genomics["notes"] for t in [
        "A-C are drawings", "fixed Litonotus", "not direct imaging",
        "supplements were not inspected",
    ])
    scope, mechanism = record["discussions"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert all(t in scope["rationale"] for t in [
        "telescopic discharge and/or membrane fusion", "unresolved, not excluded",
        "traitmech:000637", "traitmech:000684", "traitmech:000683",
        "cell lysis", "organism-level disjointness",
    ])
    assert all(t in mechanism["rationale"] for t in [
        "Natural provenance", "no canonical examples", "deferred, not claimed absent",
        "predicted toxin annotations alone", "taxon-paired accessions",
    ])


def test_proposal_matches_record_and_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1063800"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0] == "METPO:1000059"
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


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PROPOSAL"])
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
