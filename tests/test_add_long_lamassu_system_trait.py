"""Protect long-Lamassu scope, parent provenance and guarded writes."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import add_long_lamassu_system_trait as writer  # noqa: E402


@pytest.fixture
def isolated_writer(tmp_path, monkeypatch):
    record = yaml.safe_load(writer.PARENT.read_text())
    discussion = next(
        d for d in record["discussions"] if d["discussion_id"] == "lamassu-subtype-and-effector-gap"
    )
    discussion["rationale"] = "Controlled parent discussion preimage."
    record["curation_history"] = []
    monkeypatch.setattr(
        writer, "PARENT_HASH", hashlib.sha256(discussion["rationale"].encode()).hexdigest()
    )
    monkeypatch.setattr(writer, "PARENT", tmp_path / "lamassu_system.yaml")
    monkeypatch.setattr(writer, "TARGET", tmp_path / "long_lamassu_system.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    writer.write_validated_trait(record, writer.PARENT)
    monkeypatch.setattr(sys, "argv", ["writer"])
    return record


def test_family_scope_and_source_qualified_example():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000571"
    assert record["parent_traits"] == ["traitmech:000232"]
    assert record["mapping_status"] == "PROPOSED"
    assert "long-LmuB family" in record["definition"]
    assert "coiled-coil" in record["definition"]
    assert "800" not in record["definition"]
    assert "causal_graphs" not in record
    assert "xrefs" not in record
    assert len(record["evidence"]) == 3
    assert len({e["reference"] for e in record["evidence"]}) == 2
    assert all(e["snippet"] and e["notes"] for e in record["evidence"])
    dataset = record["evidence"][2]
    rows = list(csv.reader(io.StringIO(dataset["snippet"]), delimiter="\t"))
    assert len(rows) == 3 and all(len(row) == 3 for row in rows)
    assert rows[0][2] == "Lamassu__LmuB_Long"
    assert "gene_name" in dataset["notes"] and "hit_gene_ref" in dataset["notes"]
    example = record["canonical_examples"][0]
    assert example["taxon_id"] == "NCBITaxon:1396"
    assert example["reference"] == writer.PAPER
    assert "B4077" in example["note"]
    assert "no genome assembly" in example["note"]
    record["synonyms"][0]["synonym_text"] = "mutated"
    assert writer.build_record()["synonyms"][0]["synonym_text"] == "long Lamassu"


def test_proposal_round_trip():
    record = writer.build_record()
    rows = list(csv.DictReader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 2
    row = rows[1]
    assert len(row) == 11
    assert row["proposed_id"] == "METPO:1052500"
    assert row["parent"] == "METPO:1018600"
    assert row["label"] == record["label"]
    assert row["definition"] == record["definition"]
    assert row["synonyms"] == record["synonyms"][0]["synonym_text"]
    assert row["traits_addressed"] == record["identifier"]
    assert row["xrefs"] == ""


def test_dry_run_and_idempotence_preserve_parent_fields(isolated_writer, monkeypatch):
    before = writer.PARENT.read_bytes()
    assert writer.main() == 0
    assert writer.PARENT.read_bytes() == before
    assert not writer.TARGET.exists()
    assert not writer.PROPOSAL.exists()
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    parent = yaml.safe_load(writer.PARENT.read_text())
    assert parent["curation_history"][-1]["action"] == "TRACK_NARROWER_RECORD"
    parent["curation_history"].pop()
    parent["discussions"][0]["rationale"] = parent["discussions"][0]["rationale"].removesuffix(
        writer.PARENT_ADDITION
    )
    assert parent == isolated_writer
    paths = [writer.TARGET, writer.PARENT, writer.PROPOSAL / "metpo_proposal_classes_robot.tsv"]
    first = [p.read_bytes() for p in paths]
    assert writer.main() == 0
    assert [p.read_bytes() for p in paths] == first


@pytest.mark.parametrize("drift", ["rationale", "status", "kind", "parent", "identifier"])
def test_parent_drift_refused(isolated_writer, drift):
    record = copy.deepcopy(isolated_writer)
    if drift == "rationale":
        record["discussions"][0]["rationale"] += " Later curation."
    elif drift == "status":
        record["discussions"][0]["status"] = "RESOLVED"
    elif drift == "kind":
        record["discussions"][0]["kind"] = "CURATION_TODO"
    elif drift == "parent":
        record["parent_traits"] = ["METPO:1000059"]
    else:
        record["identifier"] = "traitmech:999999"
    writer.write_validated_trait(record, writer.PARENT)
    before = writer.PARENT.read_bytes()
    with pytest.raises(SystemExit, match="changed"):
        writer.main()
    assert writer.PARENT.read_bytes() == before
    assert not writer.TARGET.exists()


@pytest.mark.parametrize("changed", ["target", "proposal"])
def test_output_drift_refused(isolated_writer, monkeypatch, changed):
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    if changed == "target":
        record = writer.build_record()
        record["definition"] += " Later independent curation."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("newer proposal\n")
    before = writer.PARENT.read_bytes()
    with pytest.raises(SystemExit, match=f"Existing {changed} differs"):
        writer.main()
    assert writer.PARENT.read_bytes() == before
