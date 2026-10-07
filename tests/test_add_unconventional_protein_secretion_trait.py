"""Guard secretion scope, proposal consistency and nonmutating writer checks."""

import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_unconventional_protein_secretion_trait as writer  # noqa: E402


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


def test_identity_and_route_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000648"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "eukaryotic microbial cell" in record["definition"]
    assert "plasma membrane or extracellular space" in record["definition"]
    assert "part or all" in record["definition"]
    assert "endoplasmic-reticulum-Golgi-plasma-membrane" in record["definition"]
    assert not any(s in record["definition"] for s in ["starvation", "leaderless", "autophagosome"])
    assert all(record.get(k) is None for k in [
        "canonical_examples", "causal_graphs", "xrefs", "synonyms",
    ])
    assert len(record["discussions"]) == 2
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert record["curation_history"][-1]["llm_assisted"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 4


def test_evidence_and_boundaries():
    record = writer.build_record()
    bypass, export, autophagosome, golgi = record["evidence"]
    assert record["definition_source"] == bypass["reference"] == writer.BYPASS
    assert {e["reference"] for e in record["evidence"]} == {
        writer.BYPASS, writer.EXPORT, writer.AUTOPHAGOSOME_BOUNDARY, writer.GOLGI_BOUNDARY,
    }
    assert all(12 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "COPII-dependent ER exit" in bypass["notes"]
    assert "not soluble extracellular release" in bypass["notes"]
    assert "not an abstract quote" in export["notes"]
    assert "not direct detection in culture medium" in export["notes"]
    assert "not specialized autophagosomes" in autophagosome["snippet"]
    assert "not the teaser" in golgi["notes"]
    assert "could not be assayed" in golgi["notes"]
    assert "remain a model" in golgi["notes"]
    scope, gap = record["discussions"]
    assert "not a broader parent" in scope["rationale"]
    assert "absent predicted signal peptide" in scope["rationale"]
    assert "not independent-laboratory replications" in gap["rationale"]


def test_proposal_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1060100"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER
    assert set(rows[2][3].split("|")) == {
        "TraitMech:data/traits/physiology/unconventional_protein_secretion.yaml",
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


def test_reviewed_initial_scope_can_be_corrected(isolated, monkeypatch):
    initial = writer.build_record(initial=True)
    writer.write_validated_trait(initial, writer.TARGET)
    writer.PROPOSAL.parent.mkdir(parents=True)
    writer.PROPOSAL.write_text(writer.proposal_tsv(initial))
    before = snapshot(isolated)
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    corrected = yaml.safe_load(writer.TARGET.read_text())
    assert corrected == writer.build_record()
    assert corrected["curation_history"][:-1] == initial["curation_history"]
    assert "#1760" in corrected["curation_history"][-1]["changes"]
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]


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
    monkeypatch.setattr(writer, "build_record", lambda **kwargs: bad)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
