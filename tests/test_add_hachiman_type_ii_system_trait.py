"""Regression checks for the Hachiman architecture addition and scope repair."""

import copy
import csv
import hashlib
import importlib.util
import io
from pathlib import Path

import pytest
import yaml

SPEC = importlib.util.spec_from_file_location(
    "hachiman_type_ii_writer",
    Path(__file__).resolve().parents[1] / "scripts/add_hachiman_type_ii_system_trait.py",
)
writer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(writer)


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    parent = {
        "identifier": "traitmech:000219", "label": "Hachiman system",
        "definition": writer.OLD_DEFINITION,
        "definition_source": "DOI:10.1016/j.cell.2024.09.020",
        "trait_category": "GENOMICS", "term_kind": "CLASS",
        "mapping_status": "PROPOSED", "parent_traits": ["traitmech:000209"],
        "synonyms": [{"synonym_text": "Hachiman defense system",
                      "synonym_type": "EXACT_SYNONYM"}],
        "evidence": [{"reference": writer.CORROBORATION, "notes": "Preserve evidence."}],
        "discussions": [{
            "discussion_id": "hachiman-subtype-and-trigger-gap",
            "prompt": "Fixture question", "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": "Controlled fixture, independent of later parent curation.",
        }],
        "causal_graphs": [{
            "graph_id": "hachiman_hamab_dna_cleavage", "title": "Fixture graph",
            "scope_status": "NONMECHANISTIC", "scope_notes": "Only type I.",
            "nodes": [{"node_id": "hachiman_locus", "label": "Hachiman locus",
                       "node_type": "GENETIC_ELEMENT", "description": writer.OLD_LOCUS},
                      {"node_id": "trait", "label": "Hachiman system", "node_type": "TRAIT",
                       "grounding": "traitmech:000219"}],
            "edges": [{"subject": "hachiman_locus", "predicate": "contributes to",
                       "object": "trait", "description": "Fixture edge.",
                       "evidence": [{"reference": writer.CORROBORATION}]}],
        }],
        "curation_history": [{"timestamp": "2026-09-15T14:47:54Z", "curator": "codex",
                              "action": "FIXTURE", "changes": "Keep prior provenance.",
                              "llm_assisted": True}],
    }
    monkeypatch.setattr(writer, "TARGET", tmp_path / "child.yaml")
    monkeypatch.setattr(writer, "PARENT", tmp_path / "parent.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    monkeypatch.setattr(writer, "RATIONALE_HASH", hashlib.sha256(
        parent["discussions"][0]["rationale"].encode()).hexdigest())
    writer.write_validated_trait(parent, writer.PARENT)
    return parent


def run(monkeypatch, apply=False):
    monkeypatch.setattr(writer.sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def test_architecture_evidence_and_source_host():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000574"
    assert record["parent_traits"] == ["traitmech:000219"]
    assert "HamA and HamB" in record["definition"]
    assert "HamC (DUF3223)" in record["definition"]
    assert "cleavage" not in record["definition"]
    assert record["mapping_status"] == "PROPOSED"
    assert "causal_graphs" not in record and "xrefs" not in record
    assert {e["reference"] for e in record["evidence"]} == {
        writer.CLASSIFICATION, writer.CORROBORATION, writer.DF, writer.PADLOC,
    }
    assert all(e.get("snippet") for e in record["evidence"])
    assert all(len(e["snippet"].split()) <= 25 for e in record["evidence"])
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:173675"
    assert example["taxon_label"] == "Sphingopyxis witflariensis"
    assert example["reference"] == writer.CLASSIFICATION
    assert "DSM 14551" in example["note"] and "NZ_NISJ01000011.1" in example["note"]
    assert "engineered E. coli BL21-AI" in example["note"]
    assert "not an independent type-II experiment" in record["evidence"][1]["notes"]
    assert 'minimum gene counts are 2' in record["evidence"][2]["notes"]
    assert 'minimum_core: 3' in record["evidence"][3]["snippet"]


def test_proposal_replaces_family_without_duplicate_child_parent(isolated):
    parent, child = writer.build_parent(), writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(child, parent)), delimiter="\t"))
    assert len(rows) == 4 and {len(row) for row in rows} == {11}
    assert rows[2][0] == "METPO:1052800" and rows[2][4] == "METPO:1016300"
    assert rows[3][0] == "METPO:1052801" and rows[3][4] == rows[2][0]
    assert rows[2][2] == parent["definition"] == writer.NEW_DEFINITION
    assert rows[3][2] == child["definition"]
    assert rows[2][10] == "traitmech:000219" and rows[3][10] == child["identifier"]
    assert "METPO:1017300" in rows[2][9]
    assert rows[2][7] == rows[3][7] == "metpo_traitmech_2026_10"


def test_dry_run_apply_replay_and_preservation(isolated, monkeypatch):
    before = writer.PARENT.read_bytes()
    assert run(monkeypatch) == 0
    assert writer.PARENT.read_bytes() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()
    assert run(monkeypatch, True) == 0
    applied = yaml.safe_load(writer.PARENT.read_text())
    expected = copy.deepcopy(isolated)
    expected["definition"] = writer.NEW_DEFINITION
    expected["causal_graphs"][0]["nodes"][0]["description"] = writer.NEW_LOCUS
    expected["discussions"][0]["rationale"] += writer.ADDITION
    assert applied["curation_history"][:-1] == expected.pop("curation_history")
    event = applied.pop("curation_history")[-1]
    assert event["action"] == "SCOPE_HACHIMAN_FAMILY_AND_TYPE_II"
    assert applied == expected
    paths = [writer.PARENT, writer.TARGET, writer.PROPOSAL / "metpo_proposal_classes_robot.tsv"]
    snapshots = [p.read_bytes() for p in paths]
    assert run(monkeypatch, True) == 0
    assert [p.read_bytes() for p in paths] == snapshots


@pytest.mark.parametrize("field,value", [
    ("identifier", "traitmech:000220"), ("label", "Changed"),
    ("mapping_status", "REVIEWED"), ("parent_traits", ["METPO:1000000"]),
    ("definition", "Drift"), ("discussions", []), ("causal_graphs", []),
])
def test_identity_drift_refused_without_writes(isolated, monkeypatch, field, value):
    record = copy.deepcopy(isolated)
    record[field] = value
    writer.write_validated_trait(record, writer.PARENT)
    before = writer.PARENT.read_bytes()
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert writer.PARENT.read_bytes() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()


@pytest.mark.parametrize("drift", ["rationale", "status", "kind", "node", "partial", "duplicate"])
def test_nested_preimage_drift_refused(isolated, monkeypatch, drift):
    record = copy.deepcopy(isolated)
    if drift in {"rationale", "status", "kind"}:
        record["discussions"][0][drift] = {
            "rationale": "Unreviewed text", "status": "RESOLVED", "kind": "CURATION_TODO",
        }[drift]
    elif drift == "node":
        record["causal_graphs"][0]["nodes"][0]["description"] = "Changed"
    elif drift == "duplicate":
        record["discussions"] *= 2
    else:
        record["definition"] = writer.NEW_DEFINITION
    writer.write_validated_trait(record, writer.PARENT)
    before = writer.PARENT.read_bytes()
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert writer.PARENT.read_bytes() == before and not writer.TARGET.exists()


@pytest.mark.parametrize("target", ["child", "proposal"])
def test_output_drift_refused(isolated, monkeypatch, target):
    run(monkeypatch, True)
    path = writer.TARGET if target == "child" else writer.PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if target == "child":
        record = yaml.safe_load(path.read_text())
        record["definition"] = "Changed"
        writer.write_validated_trait(record, path)
    else:
        path.write_text("Changed")
    before = writer.PARENT.read_bytes(), path.read_bytes()
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert before == (writer.PARENT.read_bytes(), path.read_bytes())


def test_final_prevalidation_failure_prevents_live_writes(isolated, monkeypatch):
    original = writer.write_validated_trait
    before = writer.PARENT.read_bytes()

    def fail_parent(record, path):
        if record["identifier"] == "traitmech:000219":
            raise ValueError("Injected last-record validation failure")
        return original(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", fail_parent)
    with pytest.raises(ValueError, match="Injected"):
        run(monkeypatch, True)
    assert writer.PARENT.read_bytes() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()
