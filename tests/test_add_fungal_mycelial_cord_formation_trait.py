"""Check evidence boundaries and guarded two-record cord curation."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

from traitmech.validation.write_validated import ValidationFailedError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_fungal_mycelial_cord_formation_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for name, path in {
        "TARGET": "cord.yaml", "PARENT_PATH": "parent.yaml",
        "RHIZOMORPH_PATH": "rhizomorph.yaml", "PROPOSAL": "proposal/template.tsv",
    }.items():
        monkeypatch.setattr(writer, name, tmp_path / path)
    writer.write_validated_trait(writer.PARENT, writer.PARENT_PATH)
    fixture = {
        "identifier": "traitmech:000662", "label": "fungal rhizomorph formation",
        "trait_category": "MORPHOLOGY", "term_kind": "CLASS",
        "mapping_status": "PROPOSED", "parent_traits": ["METPO:1000059"],
        "discussions": [{"discussion_id": writer.DISCUSSION_ID,
                         "prompt": "Controlled scope fixture", "kind": "CURATION_TODO",
                         "status": "OPEN", "rationale": "Historical wording is not a test dependency."}],
        "curation_history": [{"timestamp": "2026-10-01T00:00:00Z", "curator": "codex",
                              "action": "TEST_FIXTURE", "changes": "Fixture", "llm_assisted": True}],
    }
    monkeypatch.setattr(writer, "RHIZOMORPH_PREIMAGE", writer.fingerprint(fixture))
    writer.write_validated_trait(fixture, writer.RHIZOMORPH_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_scope_and_evidence():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000669"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "MORPHOLOGY"
    assert "aggregation behind an extending margin of diffuse hyphae" in record["definition"]
    assert all(record.get(k) is None for k in ["causal_graphs", "xrefs", "synonyms"])
    definition, outgrowth, remodeling = record["evidence"]
    assert record["definition_source"] == definition["reference"] == writer.DEFINITION
    assert [e["reference"] for e in record["evidence"]] == [
        writer.DEFINITION, writer.OUTGROWTH, writer.REMODELING,
    ]
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "review supplies the operational terminology" in definition["notes"]
    assert "not independent experimental replication" in definition["notes"]
    assert "size and culture age are confounded" in outgrowth["notes"]
    assert "not microscopic proof" in outgrowth["notes"]
    assert "not a universal 99-day onset" in remodeling["notes"]
    example, = record["canonical_examples"]
    assert (example["taxon_id"], example["taxon_label"]) == (
        "NCBITaxon:194680", "Phanerochaete velutina",
    )
    assert example["reference"] == writer.OUTGROWTH
    assert "unnumbered isolate" in example["note"]
    assert "Farleigh Hungerford" in example["note"]
    assert "https://doi.org/10.1099/00221287-132-1-203" in example["note"]
    assert "8, 12 and 44 days" in example["note"]
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "not because mechanisms are absent" in record["discussions"][1]["rationale"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 3


def test_template_matches_record():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1062200"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_replay_and_old_record_scope(isolated, monkeypatch):
    before = snapshot(isolated)
    original = yaml.safe_load(writer.RHIZOMORPH_PATH.read_text())
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    changed = yaml.safe_load(writer.RHIZOMORPH_PATH.read_text())
    assert changed["discussions"][0]["status"] == "OPEN"
    assert changed["discussions"][0]["rationale"] == original["discussions"][0]["rationale"] + writer.SCOPE_APPEND
    assert changed["curation_history"][:-1] == original["curation_history"]
    restored = copy.deepcopy(changed)
    restored["discussions"][0]["rationale"] = original["discussions"][0]["rationale"]
    restored["curation_history"].pop()
    assert restored == original
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "RHIZOMORPH_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_drift_refused_before_any_write(isolated, monkeypatch, target, after_apply):
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
def test_parent_scope_drift_refused(isolated, monkeypatch, field):
    parent = dict(writer.PARENT)
    del parent[field]
    writer.PARENT_PATH.write_text(yaml.safe_dump(parent))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("field", ["identifier", "label", "mapping_status", "parent_traits", "discussions", "curation_history"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_old_record_semantic_drift_refused(isolated, monkeypatch, field, after_apply):
    if after_apply:
        run(monkeypatch, True)
    record = yaml.safe_load(writer.RHIZOMORPH_PATH.read_text())
    del record[field]
    writer.RHIZOMORPH_PATH.write_text(yaml.safe_dump(record))
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("target", ["TARGET", "PARENT_PATH", "RHIZOMORPH_PATH", "PROPOSAL"])
def test_empty_preimage_refused(isolated, monkeypatch, target):
    path = getattr(writer, target)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("")
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("invalid_record", ["new", "existing"])
def test_prevalidation_failure_writes_nothing(isolated, monkeypatch, invalid_record):
    if invalid_record == "new":
        bad = writer.build_record()
        bad["unrecognized_field"] = "must not be written"
        monkeypatch.setattr(writer, "build_record", lambda: bad)
    else:
        update = writer.update_rhizomorph

        def invalid(record):
            changed = update(record)
            changed["unrecognized_field"] = "must not be written"
            return changed

        monkeypatch.setattr(writer, "update_rhizomorph", invalid)
    before = snapshot(isolated)
    with pytest.raises(ValidationFailedError):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
