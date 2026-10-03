"""Keep type-I scope and existing-record preimages independently testable."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_hachiman_type_i_system_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    specs = copy.deepcopy(writer.PREIMAGES)
    records = {}
    for slug, spec in specs.items():
        record = {
            "identifier": spec["identifier"], "label": spec["label"],
            "definition": f"Controlled definition for {slug}.",
            "trait_category": "GENOMICS", "term_kind": "CLASS",
            "mapping_status": "PROPOSED", "parent_traits": list(spec["parents"]),
            "evidence": [{"reference": writer.EXPERIMENTS, "notes": "Preserve me."}],
            "canonical_examples": [{"taxon_id": "NCBITaxon:511145",
                                    "taxon_label": "Escherichia coli str. K-12 substr. MG1655",
                                    "reference": writer.EXPERIMENTS}],
            "discussions": [{
                "discussion_id": spec["discussion_id"], "prompt": "Fixture question",
                "kind": "KNOWLEDGE_GAP", "status": "OPEN",
                "rationale": f"Controlled discussion for {slug}.",
            }],
            "curation_history": [{
                "timestamp": "2026-10-03T18:08:00Z", "curator": "codex",
                "action": "FIXTURE", "changes": "Preserve prior provenance.",
                "llm_assisted": True,
            }],
        }
        spec["definition_hash"] = hashlib.sha256(record["definition"].encode()).hexdigest()
        spec["rationale_hash"] = hashlib.sha256(record["discussions"][0]["rationale"].encode()).hexdigest()
        records[slug] = record
        writer.write_validated_trait(record, tmp_path / f"{slug}.yaml")
    monkeypatch.setattr(writer, "PREIMAGES", specs)
    monkeypatch.setattr(writer, "TRAITS", tmp_path)
    monkeypatch.setattr(writer, "TARGET", tmp_path / f"{writer.SLUG}.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return records


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots():
    return {str(p.relative_to(writer.TRAITS)): p.read_bytes()
            for p in writer.TRAITS.rglob("*") if p.is_file()}


def test_component_class_and_evidence_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000575"
    assert record["parent_traits"] == ["traitmech:000219"]
    assert record["mapping_status"] == "PROPOSED"
    assert "without a HamC component" in record["definition"]
    assert "cleavage" not in record["definition"]
    assert "causal_graphs" not in record and "xrefs" not in record
    assert {e["reference"] for e in record["evidence"]} == {
        writer.CLASSIFICATION, writer.EXPERIMENTS, writer.DF, writer.PADLOC,
    }
    assert all(e.get("snippet") and len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert 'prohibited_genes:\n  - HamC2' == record["evidence"][2]["snippet"]
    assert "no forbidden HamC" in record["evidence"][3]["notes"]
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:511145"
    assert example["taxon_label"] == "Escherichia coli str. K-12 substr. MG1655"
    assert example["reference"] == writer.EXPERIMENTS
    assert "U00096.3" in example["note"] and "2761204-2765368" in example["note"]
    assert "hamAB-deleted" in example["note"]
    assert "not an inference of HamC absence" in example["note"]


def test_proposal_round_trip_uses_replacement_family():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    row = rows[2]
    assert row[0] == "METPO:1052900"
    assert row[1:3] == [record["label"], record["definition"]]
    assert row[4] == "METPO:1052800" and row[4] != "METPO:1017300"
    assert row[5] == "Hachiman type I" and row[6] == ""
    assert row[10] == record["identifier"]


def test_dry_run_apply_replay_and_preservation(isolated, monkeypatch):
    before = snapshots()
    assert run(monkeypatch) == 0 and snapshots() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()
    assert run(monkeypatch, True) == 0
    for slug, original in isolated.items():
        updated = yaml.safe_load((writer.TRAITS / f"{slug}.yaml").read_text())
        assert updated["curation_history"][:-1] == original["curation_history"]
        assert updated["curation_history"][-1]["action"] == "TRACK_HACHIMAN_TYPE_I_CLASS"
        updated["curation_history"] = original["curation_history"]
        assert updated["discussions"][0]["rationale"] == (
            original["discussions"][0]["rationale"] + writer.PREIMAGES[slug]["addition"]
        )
        updated["discussions"][0]["rationale"] = original["discussions"][0]["rationale"]
        assert updated == original
    applied = snapshots()
    assert run(monkeypatch, True) == 0 and snapshots() == applied


@pytest.mark.parametrize("slug", tuple(writer.PREIMAGES))
@pytest.mark.parametrize("drift", [
    "identifier", "label", "mapping_status", "parent_traits", "definition",
    "discussion_id", "status", "kind", "rationale", "missing", "duplicate",
])
def test_existing_drift_refuses_all_writes(isolated, monkeypatch, slug, drift):
    record = copy.deepcopy(isolated[slug])
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
    writer.write_validated_trait(record, writer.TRAITS / f"{slug}.yaml")
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


def test_last_prevalidation_failure_prevents_all_live_writes(isolated, monkeypatch):
    original = writer.write_validated_trait
    before = snapshots()

    def fail_last(record, path):
        if record["identifier"] == "traitmech:000574":
            raise ValueError("Injected validation failure")
        return original(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", fail_last)
    with pytest.raises(ValueError, match="Injected"):
        run(monkeypatch, True)
    assert snapshots() == before
