"""Guard lethal endpoints, source limitations and fail-closed writes."""

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
import add_lethal_nematicidal_activity_trait as writer  # noqa: E402


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


def test_identity_scope_and_history():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000720"
    assert record["label"] == "lethal nematicidal activity"
    assert record["definition"] == "A physiological capability of a microorganism to kill nematodes."
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["mapping_status"] == "PROPOSED" and record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["definition_source"] == "DOI:10.1128/spectrum.02577-21"
    assert len({e["reference"] for e in record["evidence"]}) == 2
    assert all(e["reference"].startswith("DOI:") and 10 <= len(e["snippet"].split()) <= 25
               for e in record["evidence"])
    assert not any(record.get(k) for k in ["canonical_examples", "causal_graphs", "synonyms", "xrefs", "protein_examples"])
    event, correction = record["curation_history"]
    assert event["curator"] == "codex" and event["llm_assisted"]
    assert datetime.fromisoformat(event["timestamp"]) <= datetime.now(timezone.utc)
    assert correction["action"] == "CORRECTED_EVIDENCE_ROLE"
    assert datetime.fromisoformat(correction["timestamp"]) <= datetime.now(timezone.utc)
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 2


def test_evidence_and_endpoint_limits():
    record = writer.build_record()
    bacterial, fungal = record["evidence"]
    for text in ["VERIFIED", "scientific Abstract", "synthetic standards", "not t-CA/PPA", "No live-culture"]:
        assert text in bacterial["notes"]
    for text in ["NOT_IN_ABSTRACT", "culture filtrate", "water/PDB", "72 h", "without its duration"]:
        assert text in fungal["notes"]
    scope, limits = [d["rationale"] for d in record["discussions"]]
    for text in [writer.CONTEXT_REFERENCE, "UNRESOLVED", "not microbial killing", "zero results"]:
        assert text in scope
    for text in ["reversible paralysis", "requires feeding", "CHEBI:25491", "not an xref", "no exact", "infection"]:
        assert text in scope
    for text in ["MT529846.1", "SF_570", "MT529837.1", "SF_561", "FbMi-4", "No corrected accession", "without canonical examples"]:
        assert text in limits


def test_source_receipt():
    receipt = json.loads((writer.ROOT / f"research/traits/physiology/{writer.SLUG}-source-verification.json").read_text())
    assert receipt["trait_id"] == writer.IDENTIFIER
    assert receipt["decision_timestamp"] == writer.TIMESTAMP
    assert receipt["native_record_verification"]["exit"] == 0
    assert [(r["reference"], r["snippet"]) for r in receipt["rows"]] == [
        (e["reference"], e["snippet"]) for e in writer.build_record()["evidence"]
    ]
    assert [r["native_verdict"] for r in receipt["rows"]] == ["VERIFIED", "NOT_IN_ABSTRACT"]
    context, = receipt["context_only_sources"]
    assert context["reference"] == writer.CONTEXT_REFERENCE and context["native_verdict"] == "UNRESOLVED"
    assert context["role"] == "discussion_only"
    assert context["snippet"] in writer.build_record()["discussions"][0]["rationale"]
    for row in [*receipt["rows"], context]:
        assert row["exact_contiguous_span"] and row["source_identity_verified"]
        assert row["words"] == len(row["snippet"].split()) <= 25
        assert len(row["source"]["sha256"]) == 64 and row["source"]["url"].startswith("https://")
        assert row["locator"] and row["inspection_limits"]
    assert receipt["allocation"]["conflicting_reservations"] == []
    assert receipt["novelty"]["ignored_hidden_included"]


def test_proposal_contract():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1067300"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4:7] == ["METPO:1000059", "", ""]
    assert rows[2][7] == "metpo_traitmech_2026_10" and rows[2][10] == writer.IDENTIFIER
    citations = rows[2][3].split("|")
    assert len(citations) == len(set(citations)) == 3
    assert set(citations) == {f"TraitMech:data/traits/physiology/{writer.SLUG}.yaml", *(e["reference"] for e in record["evidence"])}
    assert writer.CONTEXT_REFERENCE not in citations


def test_known_preimage_migration_retains_context_and_history(isolated, monkeypatch):
    previous = writer.build_initial_record()
    writer.write_validated_trait(previous, writer.TARGET)
    writer.PROPOSAL.parent.mkdir()
    writer.PROPOSAL.write_text(writer.proposal_tsv(previous))
    before = snapshot(isolated)
    assert run(monkeypatch) == 0 and snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    current = yaml.safe_load(writer.TARGET.read_text())
    assert current == writer.build_record()
    assert current["curation_history"][:-1] == previous["curation_history"]
    assert current["evidence"] == previous["evidence"][:2]
    context = previous["evidence"][2]
    assert context["snippet"] in current["discussions"][0]["rationale"]
    assert context["reference"] not in writer.PROPOSAL.read_text()
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0 and snapshot(isolated) == after


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
