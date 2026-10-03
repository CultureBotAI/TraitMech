"""Test biological architecture and fail-closed Zorya type-III curation."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_zorya_type_iii_system_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    spec = copy.deepcopy(writer.PREIMAGE)
    record = {
        "identifier": spec["identifier"], "label": spec["label"],
        "definition": "Controlled parent definition.",
        "trait_category": "GENOMICS", "term_kind": "CLASS",
        "mapping_status": "PROPOSED", "parent_traits": list(spec["parents"]),
        "evidence": [{"reference": writer.ARCHITECTURE, "notes": "Preserve me."}],
        "canonical_examples": [{"taxon_id": "NCBITaxon:562",
                                "taxon_label": "Escherichia coli",
                                "reference": writer.ARCHITECTURE}],
        "discussions": [{
            "discussion_id": spec["discussion_id"], "prompt": "Fixture question",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": "Controlled parent discussion.",
        }],
        "curation_history": [{
            "timestamp": "2026-10-02T18:08:00Z", "curator": "codex",
            "action": "FIXTURE", "changes": "Preserve prior provenance.",
            "llm_assisted": True,
        }],
    }
    spec["definition_hash"] = hashlib.sha256(record["definition"].encode()).hexdigest()
    spec["rationale_hash"] = hashlib.sha256(record["discussions"][0]["rationale"].encode()).hexdigest()
    monkeypatch.setattr(writer, "PREIMAGE", spec)
    monkeypatch.setattr(writer, "TRAITS", tmp_path)
    monkeypatch.setattr(writer, "TARGET", tmp_path / f"{writer.SLUG}.yaml")
    monkeypatch.setattr(writer, "PARENT", tmp_path / "zorya_system.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    writer.write_validated_trait(record, writer.PARENT)
    return record


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots():
    return {str(p.relative_to(writer.TRAITS)): p.read_bytes()
            for p in writer.TRAITS.rglob("*") if p.is_file()}


def test_biological_definition_and_evidence_boundaries():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000576"
    assert record["parent_traits"] == ["traitmech:000217"]
    assert record["mapping_status"] == "PROPOSED"
    assert "ZorA and ZorB together with ZorF and ZorG" in record["definition"]
    assert "DefenseFinder" not in record["definition"]
    assert "causal_graphs" not in record and "xrefs" not in record
    evidence = record["evidence"]
    assert {e["reference"] for e in evidence} == {
        writer.DISCOVERY, writer.ARCHITECTURE, writer.PADLOC, writer.DF,
    }
    assert all(e.get("snippet") and len(e["snippet"].split()) <= 25 for e in evidence)
    assert "zorBC" in evidence[0]["notes"] and "hypotheses" in evidence[0]["notes"]
    assert "both 4" in evidence[2]["notes"]
    assert 'min_mandatory_genes_required="3"' in evidence[3]["snippet"]
    assert "four mandatory slots" in evidence[3]["notes"]
    assert "minimum counts are only 3" in evidence[3]["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:83617"
    assert example["taxon_label"] == "Stenotrophomonas nitritireducens"
    assert example["reference"] == writer.DISCOVERY
    assert "NZ_LDJG01000021.1" in example["note"]
    assert "DSM 12575" in example["note"] and "not species-wide" in example["note"]
    assert "plasmid-borne" in example["note"] and "BL21-AI" in example["note"]


def test_proposal_matches_record_and_family_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    row = rows[2]
    assert row[0] == "METPO:1053000"
    assert row[1:3] == [record["label"], record["definition"]]
    assert row[4] == "METPO:1017100"
    assert row[5] == "Zorya type III" and row[6] == ""
    assert row[10] == record["identifier"]


def test_dry_run_apply_replay_and_preservation(isolated, monkeypatch):
    before = snapshots()
    assert run(monkeypatch) == 0 and snapshots() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()
    assert run(monkeypatch, True) == 0
    updated = yaml.safe_load(writer.PARENT.read_text())
    assert updated["curation_history"][:-1] == isolated["curation_history"]
    assert updated["curation_history"][-1]["action"] == "TRACK_ZORYA_TYPE_III_CLASS"
    assert updated["discussions"][0]["rationale"] == (
        isolated["discussions"][0]["rationale"] + writer.PREIMAGE["addition"]
    )
    updated["curation_history"] = isolated["curation_history"]
    updated["discussions"][0]["rationale"] = isolated["discussions"][0]["rationale"]
    assert updated == isolated
    applied = snapshots()
    assert run(monkeypatch, True) == 0 and snapshots() == applied


@pytest.mark.parametrize("drift", [
    "identifier", "label", "mapping_status", "parent_traits", "definition",
    "discussion_id", "status", "kind", "rationale", "missing", "duplicate",
])
def test_parent_drift_refuses_all_writes(isolated, monkeypatch, drift):
    record = copy.deepcopy(isolated)
    if drift in {"identifier", "label", "mapping_status", "parent_traits", "definition"}:
        record[drift] = {
            "identifier": "traitmech:000999", "label": "Changed", "mapping_status": "REVIEWED",
            "parent_traits": ["METPO:1000000"], "definition": "Changed definition.",
        }[drift]
    elif drift == "missing":
        record["discussions"] = []
    elif drift == "duplicate":
        record["discussions"] *= 2
    else:
        record["discussions"][0][drift] = {
            "discussion_id": "changed-id", "status": "RESOLVED", "kind": "CURATION_TODO",
            "rationale": "Unreviewed change.",
        }[drift]
    writer.write_validated_trait(record, writer.PARENT)
    before = snapshots()
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshots() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()


@pytest.mark.parametrize("target", ["child", "proposal"])
def test_output_drift_refused(isolated, monkeypatch, target):
    run(monkeypatch, True)
    if target == "child":
        record = yaml.safe_load(writer.TARGET.read_text())
        record["definition"] = "Changed definition."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Changed")
    before = snapshots()
    with pytest.raises(SystemExit):
        run(monkeypatch, True)
    assert snapshots() == before


def test_parent_prevalidation_failure_prevents_live_writes(isolated, monkeypatch):
    original = writer.write_validated_trait
    before = snapshots()

    def fail_parent(record, path):
        if record["identifier"] == "traitmech:000217":
            raise ValueError("Injected validation failure")
        return original(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", fail_parent)
    with pytest.raises(ValueError, match="Injected"):
        run(monkeypatch, True)
    assert snapshots() == before
