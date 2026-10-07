"""Guard ribosome-turnover scope and immutable parent-proposal context."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_ribophagy_trait as writer  # noqa: E402


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


def test_identity_selectivity_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000641"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000638"]
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["definition"].startswith("An autophagy phenotype")
    assert "selectively degrades mature ribosomes or their subunits" in record["definition"]
    assert "macroautophagic delivery" in record["definition"]
    assert "lysosomal or vacuolar compartments" in record["definition"]
    assert not any(x in record["definition"] for x in ["starvation", "damaged", "Atg"])
    assert all(record.get(k) is None for k in [
        "canonical_examples", "causal_graphs", "xrefs", "synonyms",
    ])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 4


def test_evidence_source_sections_and_access_limits():
    record = writer.build_record()
    original, subunit, bulk, rsa1 = record["evidence"]
    assert record["definition_source"] == original["reference"] == writer.ORIGINAL
    assert {e["reference"] for e in record["evidence"]} == {
        writer.ORIGINAL, writer.SUBUNIT, writer.BULK, writer.RSA1,
    }
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert all("Scientific Abstract directly read" in e["notes"] for e in record["evidence"])
    assert "60S particles" in original["notes"]
    assert "do not transfer the same dependence to 40S" in original["notes"]
    assert "distinct from the precis" in subunit["notes"]
    assert "less dependent on Ubp3" in subunit["snippet"]
    assert "BY4741 with auxotrophic deletions" in subunit["notes"]
    assert "boundary evidence, not a positive selective-ribophagy" in bulk["notes"]
    assert "Full-text retrieval returned HTTP 500" in bulk["notes"]
    assert "mechanism differs" in rsa1["snippet"]
    assert "not an unqualified canonical ribophagy assignment" in rsa1["notes"]
    assert "Residual turnover" in rsa1["notes"]
    assert "not established" in rsa1["notes"]
    assert "modeled, not experimentally mapped" in rsa1["notes"]
    assert "actual figures, supplements" in rsa1["notes"]
    scope, gap = record["discussions"]
    assert all(curie in scope["rationale"] for curie in ["GO:0034517", "traitmech:000638"])
    assert "do not silently equate Rsa1-dependent turnover" in scope["rationale"]
    assert "natural strain provenance has not been independently verified" in gap["rationale"]


def test_proposal_preserves_parent_context_and_child_parity():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 4 and {len(r) for r in rows} == {11}
    assert rows[:2] == writer.HEADERS
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2] == writer.PARENT_ROW
    assert rows[2][0] == writer.PARENT_METPO_ID == "METPO:1059100"
    assert rows[3][0] == writer.METPO_ID == "METPO:1059400"
    assert rows[3][1:3] == [record["label"], record["definition"]]
    assert rows[3][4] == rows[2][0]
    assert rows[3][5:7] == ["", ""]
    assert rows[3][10] == writer.IDENTIFIER
    assert set(rows[3][3].split("|")) == {
        "TraitMech:data/traits/physiology/ribophagy.yaml",
        writer.ORIGINAL, writer.SUBUNIT, writer.BULK, writer.RSA1,
    }


def test_dry_run_apply_replay_preserves_parent_context(isolated, monkeypatch):
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


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "PARENT_PROPOSAL"])
def test_empty_record_or_context_refused(isolated, monkeypatch, target):
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
