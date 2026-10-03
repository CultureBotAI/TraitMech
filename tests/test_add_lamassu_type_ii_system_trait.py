"""Protect component scope, orthogonal parents and atomic preflight checks."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import add_lamassu_type_ii_system_trait as writer  # noqa: E402


@pytest.fixture
def isolated_writer(tmp_path, monkeypatch):
    specs = copy.deepcopy(writer.PREIMAGES)
    records = {}
    for slug, spec in specs.items():
        record = yaml.safe_load((writer.TRAITS / f"{slug}.yaml").read_text())
        record["definition"] = f"A controlled LmuC-containing fixture for {slug}."
        record["parent_traits"] = list(spec["old_parents"])
        record["curation_history"] = []
        discussion = next(d for d in record["discussions"] if d["discussion_id"] == spec["discussion_id"])
        discussion["rationale"] = f"Controlled discussion preimage for {slug}."
        spec["definition_hash"] = hashlib.sha256(record["definition"].encode()).hexdigest()
        spec["rationale_hash"] = hashlib.sha256(discussion["rationale"].encode()).hexdigest()
        records[slug] = record
        writer.write_validated_trait(record, tmp_path / f"{slug}.yaml")
    monkeypatch.setattr(writer, "PREIMAGES", specs)
    monkeypatch.setattr(writer, "TRAITS", tmp_path)
    monkeypatch.setattr(writer, "TARGET", tmp_path / f"{writer.SLUG}.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    monkeypatch.setattr(sys, "argv", ["writer"])
    return records


def snapshots():
    return {p.name: p.read_bytes() for p in writer.TRAITS.glob("*.yaml")}


def test_component_scope_and_source_qualified_example():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000572"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000232"]
    assert "additional LmuC component" in record["definition"]
    assert "LmuA effector module" in record["definition"]
    assert "three" not in record["definition"]
    assert "dependent" not in record["definition"]
    assert "causal_graphs" not in record and "xrefs" not in record
    assert {e["reference"] for e in record["evidence"]} == {writer.CLASSIFICATION, writer.STRUCTURE}
    assert all(e["snippet"] and e["notes"] for e in record["evidence"])
    assert record["synonyms"][0]["synonym_text"] in record["evidence"][0]["snippet"]
    example = record["canonical_examples"][0]
    assert example["taxon_id"] == "NCBITaxon:1349767"
    assert "DSM 9628" in example["taxon_label"]
    assert "NZ_HG322949.1" in example["note"]
    assert "BL21-AI" in example["note"]
    assert "not native-host" in example["note"]
    record["evidence"].clear()
    assert len(writer.build_record()["evidence"]) == 2


def test_proposal_round_trip_and_header_width():
    record = writer.build_record()
    text = writer.proposal_tsv(record)
    raw = list(csv.reader(io.StringIO(text), delimiter="\t"))
    assert len(raw) == 3 and all(len(row) == 11 for row in raw)
    assert raw[1][-3:] == ["", "", ""]
    row = list(csv.DictReader(io.StringIO(text), delimiter="\t"))[1]
    assert row["proposed_id"] == "METPO:1052600"
    assert row["parent"] == "METPO:1018600"
    assert row["label"] == record["label"] and row["definition"] == record["definition"]
    assert row["traits_addressed"] == record["identifier"]
    assert row["synonyms"] == record["synonyms"][0]["synonym_text"]
    assert row["xrefs"] == ""


def test_dry_run_apply_idempotence_and_preservation(isolated_writer, monkeypatch):
    before = snapshots()
    assert writer.main() == 0
    assert snapshots() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    for slug, spec in writer.PREIMAGES.items():
        record = yaml.safe_load((writer.TRAITS / f"{slug}.yaml").read_text())
        assert record["parent_traits"] == spec["new_parents"]
        assert record["curation_history"][-1]["llm_assisted"] is True
        record["curation_history"].pop()
        record["parent_traits"] = spec["old_parents"]
        discussion = next(d for d in record["discussions"] if d["discussion_id"] == spec["discussion_id"])
        discussion["rationale"] = discussion["rationale"].removesuffix(spec["addition"])
        assert record == isolated_writer[slug]
    hnh = yaml.safe_load((writer.TRAITS / "lamassu_hnh_system.yaml").read_text())
    assert hnh["parent_traits"] == ["traitmech:000570", writer.IDENTIFIER]
    first = snapshots()
    tsv = (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").read_bytes()
    assert writer.main() == 0
    assert snapshots() == first
    assert (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").read_bytes() == tsv


@pytest.mark.parametrize("slug", list(writer.PREIMAGES))
@pytest.mark.parametrize("drift", ["identifier", "label", "definition", "parent", "rationale", "kind", "status"])
def test_any_existing_drift_refuses_all_writes(isolated_writer, monkeypatch, slug, drift):
    record = copy.deepcopy(isolated_writer[slug])
    spec = writer.PREIMAGES[slug]
    discussion = next(d for d in record["discussions"] if d["discussion_id"] == spec["discussion_id"])
    if drift == "identifier":
        record["identifier"] = "traitmech:999999"
    elif drift == "label":
        record["label"] += " revised"
    elif drift == "definition":
        record["definition"] += " Revised biological scope."
    elif drift == "parent":
        record["parent_traits"] = ["METPO:1000059"]
    elif drift == "rationale":
        discussion["rationale"] += " Later curation."
    elif drift == "kind":
        discussion["kind"] = "CURATION_TODO"
    else:
        discussion["status"] = "RESOLVED"
    writer.write_validated_trait(record, writer.TRAITS / f"{slug}.yaml")
    before = snapshots()
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    with pytest.raises(SystemExit, match="changed"):
        writer.main()
    assert snapshots() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()


@pytest.mark.parametrize("slug", [s for s in writer.PREIMAGES if s != "lamassu_system"])
def test_inconsistent_application_state_refused(isolated_writer, slug):
    record = copy.deepcopy(isolated_writer[slug])
    record["parent_traits"] = writer.PREIMAGES[slug]["new_parents"]
    writer.write_validated_trait(record, writer.TRAITS / f"{slug}.yaml")
    with pytest.raises(SystemExit, match="application state changed"):
        writer.main()


@pytest.mark.parametrize("changed", ["target", "proposal"])
def test_output_drift_refused(isolated_writer, monkeypatch, changed):
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    if changed == "target":
        record = writer.build_record()
        record["definition"] += " Later independent curation."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("later proposal\n")
    before = snapshots()
    with pytest.raises(SystemExit, match=f"Existing {changed} differs"):
        writer.main()
    assert snapshots() == before


def test_all_records_prevalidated_before_real_writes(isolated_writer, monkeypatch):
    before = snapshots()
    real_write = writer.write_validated_trait

    def fail_last(record, path):
        if record["identifier"] == "traitmech:000569":
            raise ValueError("simulated validation failure")
        return real_write(record, path)

    monkeypatch.setattr(writer, "write_validated_trait", fail_last)
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    with pytest.raises(ValueError, match="simulated validation failure"):
        writer.main()
    assert snapshots() == before
    assert not writer.TARGET.exists() and not writer.PROPOSAL.exists()
