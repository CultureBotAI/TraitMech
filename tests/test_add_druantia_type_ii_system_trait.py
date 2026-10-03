"""Test Druantia II architecture, assay boundaries and guarded parent curation."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_druantia_type_ii_system_trait as writer  # noqa: E402


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
            "rationale": "Controlled parent discussion. " + spec["old_tail"],
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
    monkeypatch.setattr(writer, "PARENT", tmp_path / "druantia_system.yaml")
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
    assert record["identifier"] == "traitmech:000579"
    assert record["parent_traits"] == ["traitmech:000234"]
    assert record["mapping_status"] == "PROPOSED"
    assert "DruE together with DruM, DruF and DruG" in record["definition"]
    assert "DefenseFinder" not in record["definition"]
    assert "causal_graphs" not in record and "xrefs" not in record
    evidence = {e["reference"]: e for e in record["evidence"]}
    assert set(evidence) == {
        writer.ARCHITECTURE, writer.MECHANISM, writer.PADLOC, writer.DF,
    }
    assert all(e.get("snippet") and len(e["snippet"].split()) <= 25 for e in evidence.values())
    assert "requisite DruM and DruG" in evidence[writer.ARCHITECTURE]["snippet"]
    assert (
        "Results: Identification of new defence system variants"
        in evidence[writer.ARCHITECTURE]["notes"]
    )
    mechanism = evidence[writer.MECHANISM]
    assert "DruE alone" in mechanism["snippet"]
    assert "2026-07-08, not peer reviewed" in mechanism["notes"]
    assert "Insoluble DruF/G prevented full-system" in mechanism["notes"]
    assert "E. coli BL21" in mechanism["notes"]
    assert "not a demonstrated defense trigger" in mechanism["notes"]
    assert "both 4" in evidence[writer.PADLOC]["notes"]
    assert "DruK is secondary" in evidence[writer.PADLOC]["notes"]
    assert 'min_mandatory_genes_required="1"' in evidence[writer.DF]["snippet"]
    assert "One mandatory and three total" in evidence[writer.DF]["notes"]
    assert "Druantia_IV__DruF4" in evidence[writer.DF]["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:220664"
    assert example["taxon_label"] == "Pseudomonas protegens Pf-5"
    assert example["reference"] == writer.MECHANISM
    assert "GCF_000012265.1" in example["note"]
    assert "Not a native-host phage-resistance example" in example["note"]
    assert "Do not transfer type-III" in record["discussions"][0]["rationale"]


def test_proposal_matches_record_and_corrected_family_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    row = rows[2]
    assert row[0] == "METPO:1053300"
    assert row[1:3] == [record["label"], record["definition"]]
    assert row[4] == "METPO:1053100"
    assert row[5] == "Type II Druantia system" and row[6] == ""
    assert row[10] == record["identifier"]


def test_dry_run_apply_replay_and_preservation(isolated, monkeypatch):
    before = snapshots()
    assert run(monkeypatch) == 0 and snapshots() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()
    assert run(monkeypatch, True) == 0
    updated = yaml.safe_load(writer.PARENT.read_text())
    assert updated["curation_history"][:-1] == isolated["curation_history"]
    assert updated["curation_history"][-1]["action"] == "TRACK_NARROWER_RECORD"
    assert updated["discussions"][0]["rationale"] == (
        isolated["discussions"][0]["rationale"].removesuffix(writer.PREIMAGE["old_tail"])
        + writer.PREIMAGE["new_tail"]
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
        if record["identifier"] == "traitmech:000234":
            raise ValueError("Injected validation failure")
        return original(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", fail_parent)
    with pytest.raises(ValueError, match="Injected"):
        run(monkeypatch, True)
    assert snapshots() == before
