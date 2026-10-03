"""Exercise scientific boundaries, guarded preimages and replay safety."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_druantia_type_iv_system_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    record = {
        "identifier": "traitmech:000234", "label": "Druantia system",
        "definition": "Controlled old parent definition.",
        "definition_source": writer.FAMILY,
        "trait_category": "GENOMICS", "term_kind": "CLASS",
        "mapping_status": "PROPOSED", "parent_traits": ["traitmech:000209"],
        "synonyms": [{"synonym_text": "Druantia", "synonym_type": "EXACT_SYNONYM"}],
        "evidence": [
            {"reference": writer.FAMILY, "snippet": "suggesting a shared function",
             "notes": "Controlled hypothesis note."},
            {"reference": writer.FAMILY, "snippet": "A type III observation",
             "notes": "Controlled type-III note."},
            {"reference": "DOI:10.1126/science.aar4120", "notes": "Preserve me."},
        ],
        "canonical_examples": [{"taxon_id": "NCBITaxon:562",
                                "taxon_label": "Escherichia coli"}],
        "causal_graphs": [{
            "graph_id": "controlled_graph", "title": "Controlled graph",
            "description": "Controlled obsolete family mechanism.",
            "scope_status": "NONMECHANISTIC",
            "nodes": [{"node_id": "family", "label": "Druantia system",
                       "node_type": "TRAIT", "grounding": "traitmech:000234"}],
            "edges": [],
        }],
        "discussions": [{
            "discussion_id": "druantia-subtype-mechanism-gap",
            "prompt": "Controlled old question.", "kind": "KNOWLEDGE_GAP",
            "status": "OPEN", "rationale": "Controlled old rationale.",
        }],
        "curation_history": [{
            "timestamp": "2026-10-02T18:08:00Z", "curator": "codex",
            "action": "FIXTURE", "changes": "Preserve prior provenance.",
            "llm_assisted": True,
        }],
    }
    monkeypatch.setattr(writer, "TRAITS", tmp_path)
    monkeypatch.setattr(writer, "TARGET", tmp_path / f"{writer.SLUG}.yaml")
    monkeypatch.setattr(writer, "PARENT", tmp_path / "druantia_system.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    writer.write_validated_trait(record, writer.PARENT)
    record = yaml.safe_load(writer.PARENT.read_text())
    monkeypatch.setattr(writer, "PREIMAGE_HASH", writer.fingerprint(record))
    monkeypatch.setattr(writer, "POSTIMAGE_HASH", writer.fingerprint(writer.repair_parent(record)))
    return record


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots():
    return {str(p.relative_to(writer.TRAITS)): p.read_bytes()
            for p in writer.TRAITS.rglob("*") if p.is_file()}


def test_architecture_and_evidence_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000577"
    assert record["parent_traits"] == ["traitmech:000234"]
    assert record["mapping_status"] == "PROPOSED"
    assert "DruE and DruF together with DruL" in record["definition"]
    assert "without the type-II DruM and DruG" in record["definition"]
    assert "DefenseFinder" not in record["definition"]
    assert not {"causal_graphs", "xrefs", "canonical_examples"} & record.keys()
    assert {e["reference"] for e in record["evidence"]} == {
        writer.DISCOVERY, writer.DF, writer.PADLOC,
    }
    assert all(e.get("snippet") and len(e["snippet"].split()) <= 25
               for e in record["evidence"])
    notes = " ".join(e["notes"] for e in record["evidence"])
    for constraint in ["not Druantia IV", "three mandatory slots", "both minimum counts 3",
                       "exchangeables", "no forbidden genes", "DruK is secondary",
                       "prohibited list is NA", "incomplete assembly"]:
        assert constraint in notes


def test_proposal_identity_and_parent_replacement(isolated):
    child, parent = writer.build_record(), writer.build_parent()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(child, parent)), delimiter="\t"))
    assert len(rows) == 4 and {len(row) for row in rows} == {11}
    assert rows[2][0] == "METPO:1053100" and rows[2][4] == "METPO:1016300"
    assert rows[3][0] == "METPO:1053101" and rows[3][4] == "METPO:1053100"
    for row, record in zip(rows[2:], [parent, child], strict=True):
        assert row[1:3] == [record["label"], record["definition"]]
        assert row[10] == record["identifier"] and row[6] == ""
    assert "v111 METPO:1018800" in rows[2][9]


def test_dry_run_apply_replay_and_parent_scope(isolated, monkeypatch):
    before = snapshots()
    assert run(monkeypatch) == 0 and snapshots() == before
    assert run(monkeypatch, True) == 0
    parent = yaml.safe_load(writer.PARENT.read_text())
    assert "causal_graphs" not in parent
    assert parent["definition"] == writer.NEW_DEFINITION
    assert parent["canonical_examples"] == isolated["canonical_examples"]
    assert parent["curation_history"][:-1] == isolated["curation_history"]
    assert parent["discussions"][0]["status"] == "OPEN"
    assert parent["discussions"][0]["rationale"] == (
        isolated["discussions"][0]["rationale"] + writer.ADDITION
    )
    assert "hypothesis" in parent["evidence"][0]["notes"]
    assert parent["evidence"][1]["notes"].startswith("Preprint v1")
    assert parent["evidence"][2] == isolated["evidence"][2]
    assert parent["evidence"][-1] == writer.DISCOVERY_EVIDENCE
    for key in set(isolated) - {"definition", "causal_graphs", "curation_history",
                                "discussions", "evidence"}:
        assert parent[key] == isolated[key]
    applied = snapshots()
    assert run(monkeypatch, True) == 0 and snapshots() == applied


@pytest.mark.parametrize("drift", [
    "identifier", "label", "mapping_status", "parent_traits", "definition",
    "definition_source", "evidence", "causal_graphs", "curation_history",
    "discussion_id", "status", "kind", "rationale", "missing", "duplicate",
])
def test_parent_drift_prevents_all_writes(isolated, monkeypatch, drift):
    record = copy.deepcopy(isolated)
    if drift in {"identifier", "label", "mapping_status", "definition", "definition_source"}:
        record[drift] = "Changed"
    elif drift in {"parent_traits", "evidence", "causal_graphs", "curation_history"}:
        record[drift] = []
    elif drift == "missing":
        record["discussions"] = []
    elif drift == "duplicate":
        record["discussions"] *= 2
    else:
        record["discussions"][0][drift] = "Changed"
    # Deliberately serialize invalid preimages to exercise refusal before validation.
    writer.PARENT.write_text(yaml.safe_dump(record))
    before = snapshots()
    with pytest.raises(SystemExit, match="preimage"):
        run(monkeypatch, True)
    assert snapshots() == before


@pytest.mark.parametrize("target", ["child", "proposal", "applied_parent"])
def test_output_drift_refused(isolated, monkeypatch, target):
    run(monkeypatch, True)
    if target == "proposal":
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Changed")
    else:
        path = writer.TARGET if target == "child" else writer.PARENT
        record = yaml.safe_load(path.read_text())
        record["definition"] = "Changed definition."
        writer.write_validated_trait(record, path)
    before = snapshots()
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshots() == before


def test_prevalidation_failure_prevents_live_writes(isolated, monkeypatch):
    original = writer.write_validated_trait
    before = snapshots()

    def fail_parent(record, path):
        if record["identifier"] == "traitmech:000234":
            raise ValueError("Injected validation failure")
        return original(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", fail_parent)
    with pytest.raises(ValueError, match="Injected"):
        run(monkeypatch, True)
    assert snapshots() == before
