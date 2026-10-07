"""Guard fluid-uptake scope and the coupled macropinocytosis refinement."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_pinocytosis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    for attr, name in [("TARGET", "trait.yaml"), ("CHILD_PATH", "child.yaml"),
                       ("PARENT_PATH", "parent.yaml"), ("PROPOSAL", "proposal/template.tsv")]:
        monkeypatch.setattr(writer, attr, tmp_path / name)
    parent = {**writer.PARENT, "trait_category": "UPPER", "term_kind": "CLASS"}
    writer.write_validated_trait(parent, writer.PARENT_PATH)
    rationale = "Controlled historical hierarchy preimage."
    monkeypatch.setattr(writer, "CHILD_RATIONALE_SHA256",
                        hashlib.sha256(rationale.encode()).hexdigest())
    child = {
        **writer.CHILD, "parent_traits": [writer.PARENT["identifier"]],
        "evidence": [{"reference": writer.CHILD["definition_source"],
                      "notes": "Preserve existing experimental evidence."}],
        "canonical_examples": [{"taxon_id": "NCBITaxon:44689",
                                "taxon_label": "Dictyostelium discoideum",
                                "reference": writer.CHILD["definition_source"],
                                "note": "Controlled strain qualification."}],
        "discussions": [
            {"discussion_id": writer.CHILD_DISCUSSION, "kind": "CURATION_TODO",
             "status": "OPEN", "prompt": "Resolve the parent gap.",
             "rationale": rationale},
            {"discussion_id": "independent-gap", "kind": "KNOWLEDGE_GAP",
             "status": "OPEN", "prompt": "Preserve this independent gap.",
             "rationale": "Unrelated mechanism uncertainty."},
        ],
    }
    writer.event(child, "PRIOR_EVENT", "Preserve this earlier event.")
    writer.write_validated_trait(child, writer.CHILD_PATH)
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshot(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_scope_and_source_limits():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000635"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert "extracellular fluid" in record["definition"]
    assert "membrane-bound compartments" in record["definition"]
    assert not any(s in record["definition"] for s in ["ruffle", "nutrient", "nonconcentrative"])
    assert not any(record.get(k) for k in ["causal_graphs", "xrefs", "synonyms", "protein_examples"])
    first, second = record["evidence"]
    assert record["definition_source"] == first["reference"] == writer.FIRST
    assert second["reference"] == writer.SECOND
    assert all(8 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "PDF/figures were unavailable" in first["notes"]
    assert "Full text and figures were unavailable" in second["notes"]
    assert len(record["discussions"]) == 3
    assert all(d["status"] == "OPEN" for d in record["discussions"])
    assert "not establish independent taxon replication" in record["discussions"][2]["rationale"]
    original_notes = first["notes"]
    record["evidence"][0]["notes"] = "Mutation must not escape."
    assert writer.build_record()["evidence"][0]["notes"] == original_notes


def test_canonical_taxonomy_and_provenance_are_qualified():
    record = writer.build_record()
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:1257118"
    assert example["taxon_label"] == "Acanthamoeba castellanii str. Neff"
    assert example["reference"] == writer.FIRST
    for text in [writer.PROVENANCE, writer.TAXONOMY, "no collection accession",
                 "does not establish vial or genome identity", "not a species-wide assertion"]:
        assert text in example["note"]
    taxonomy = record["discussions"][1]
    evidence, = taxonomy["evidence"]
    assert evidence["reference"] == writer.TAXONOMY
    assert evidence["evidence_source"] == "abstract"
    assert len(evidence["snippet"].split()) <= 25
    assert "not another pinocytosis experiment" in evidence["notes"]


def test_proposal_matches_new_record_only():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == writer.METPO_ID == "METPO:1058800"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_replay_and_preserved_child_fields(isolated, monkeypatch):
    before = snapshot(isolated)
    old_child = yaml.safe_load(writer.CHILD_PATH.read_text())
    assert run(monkeypatch) == 0
    assert snapshot(isolated) == before
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    assert writer.PARENT_PATH.read_bytes() == before["parent.yaml"]
    child = yaml.safe_load(writer.CHILD_PATH.read_text())
    assert child["parent_traits"] == [writer.IDENTIFIER]
    assert child["curation_history"][:-1] == old_child["curation_history"]
    assert child["curation_history"][-1]["action"] == "REFINE_PINOCYTOSIS_PARENT"
    assert child["discussions"][1:] == old_child["discussions"][1:]
    discussion = child["discussions"][0]
    assert discussion.pop("resolved_date") == "2026-10-06"
    assert discussion.pop("resolution_note") == writer.CHILD_RESOLUTION
    assert discussion["status"] == "RESOLVED"
    discussion["status"] = "OPEN"
    child["parent_traits"] = old_child["parent_traits"]
    child["curation_history"].pop()
    assert child == old_child
    after = snapshot(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshot(isolated) == after


@pytest.mark.parametrize("target", ["TARGET", "PROPOSAL", "PARENT_PATH"])
@pytest.mark.parametrize("after_apply", [False, True])
def test_output_and_parent_drift_refused(isolated, monkeypatch, target, after_apply):
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


@pytest.mark.parametrize("field,value", [
    ("identifier", "traitmech:999999"), ("label", "other uptake"),
    ("definition", "Unreviewed scope change"), ("mapping_status", "REVIEWED"),
    ("parent_traits", ["METPO:1000188"]),
])
def test_child_identity_scope_and_parent_drift_refused(isolated, monkeypatch, field, value):
    child = yaml.safe_load(writer.CHILD_PATH.read_text())
    child[field] = value
    writer.write_validated_trait(child, writer.CHILD_PATH)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("drift", ["rationale", "status", "kind", "missing", "duplicate"])
def test_child_discussion_drift_refused(isolated, monkeypatch, drift):
    child = yaml.safe_load(writer.CHILD_PATH.read_text())
    discussion = child["discussions"][0]
    if drift == "missing":
        child["discussions"].pop(0)
    elif drift == "duplicate":
        child["discussions"].append(copy.deepcopy(discussion))
    else:
        discussion[drift] = {"rationale": "Independent curation", "status": "RESOLVED",
                             "kind": "KNOWLEDGE_GAP"}[drift]
    writer.write_validated_trait(child, writer.CHILD_PATH)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


@pytest.mark.parametrize("drift", ["status", "resolved_date", "resolution_note", "history"])
def test_child_replay_drift_refused(isolated, monkeypatch, drift):
    run(monkeypatch, True)
    child = yaml.safe_load(writer.CHILD_PATH.read_text())
    if drift == "history":
        child["curation_history"].pop()
    else:
        child["discussions"][0][drift] = {
            "status": "OPEN", "resolved_date": "2026-10-07",
            "resolution_note": "Independent resolution",
        }[drift]
    writer.write_validated_trait(child, writer.CHILD_PATH)
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="replay differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_empty_target_refused(isolated, monkeypatch):
    writer.TARGET.touch()
    before = snapshot(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before


def test_both_records_prevalidated_before_writing(isolated, monkeypatch):
    real_writer = writer.write_validated_trait

    def reject_child(record, path):
        if record["identifier"] == writer.CHILD["identifier"]:
            raise ValueError("Controlled child validation failure")
        return real_writer(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", reject_child)
    before = snapshot(isolated)
    with pytest.raises(ValueError, match="Controlled child"):
        run(monkeypatch, True)
    assert snapshot(isolated) == before
