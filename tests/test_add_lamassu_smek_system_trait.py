"""Guard SMEK-system scope and the curation writer's mutation contract."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import add_lamassu_smek_system_trait as writer  # noqa: E402


@pytest.fixture
def isolated_writer(tmp_path, monkeypatch):
    parent = yaml.safe_load(writer.PARENT.read_text())
    discussion = next(
        d for d in parent["discussions"] if d["discussion_id"] == "lamassu-subtype-and-effector-gap"
    )
    # Exercise guard behavior independently of later curation of the shared parent.
    discussion["rationale"] = "Original parent subtype discussion."
    monkeypatch.setattr(
        writer, "OLD_PARENT_HASH", hashlib.sha256(discussion["rationale"].encode()).hexdigest()
    )
    parent["curation_history"] = []
    path = tmp_path / "lamassu_system.yaml"
    writer.write_validated_trait(parent, path)
    monkeypatch.setattr(writer, "PARENT", path)
    monkeypatch.setattr(writer, "TARGET", tmp_path / "lamassu_smek_system.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    monkeypatch.setattr(sys, "argv", ["writer"])
    return parent


def test_record_preserves_architecture_and_example_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000569"
    assert record["parent_traits"] == ["traitmech:000232"]
    assert record["mapping_status"] == "PROPOSED"
    assert "short" not in record["definition"]
    assert all(name in record["definition"] for name in ("SMEK", "LmuA", "LmuB", "LmuC"))
    assert "causal_graphs" not in record
    assert "xrefs" not in record
    assert all(s["synonym_type"] == "RELATED_SYNONYM" for s in record["synonyms"])
    assert "SMEK" not in [s["synonym_text"] for s in record["synonyms"]]
    assert len({e["reference"] for e in record["evidence"]}) == 4
    assert len(record["evidence"]) == 9
    assert all(e["snippet"] and e["notes"] for e in record["evidence"])
    example = record["canonical_examples"][0]
    assert example["taxon_id"] == "NCBITaxon:40215"
    assert "Computational genomic example" in example["note"]
    assert "GCF_021491935.1" in example["note"]
    assert example["reference"] == writer.DATASET
    rationale = record["discussions"][0]["rationale"]
    assert "124 short-profile calls and one long-profile" in rationale
    assert "DS-27" in rationale
    record["label"] = "mutated"
    assert writer.build_record()["label"] == "Lamassu-SMEK system"


def test_proposal_round_trip():
    record = writer.build_record()
    rows = list(csv.DictReader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 2
    row = rows[1]
    assert row["proposed_id"] == "METPO:1052300"
    assert row["traits_addressed"] == record["identifier"]
    assert row["label"] == record["label"]
    assert row["definition"] == record["definition"]
    assert row["parent"] == "METPO:1018600"
    assert row["exact_synonyms"] == row["xrefs"] == ""
    assert row["related_synonyms"].split("|") == [s["synonym_text"] for s in record["synonyms"]]


def test_dry_run_then_apply_is_idempotent(isolated_writer, monkeypatch):
    before = writer.PARENT.read_bytes()
    assert writer.main() == 0
    assert writer.PARENT.read_bytes() == before
    assert not writer.TARGET.exists()
    assert not writer.PROPOSAL.exists()
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    proposal = writer.PROPOSAL / "metpo_proposal_classes_robot.tsv"
    first = [p.read_bytes() for p in (writer.TARGET, writer.PARENT, proposal)]
    assert writer.main() == 0
    assert [p.read_bytes() for p in (writer.TARGET, writer.PARENT, proposal)] == first


def test_parent_drift_refused(isolated_writer):
    parent = copy.deepcopy(isolated_writer)
    discussion = next(
        d for d in parent["discussions"] if d["discussion_id"] == "lamassu-subtype-and-effector-gap"
    )
    discussion["rationale"] += " Unrelated newer curation."
    writer.write_validated_trait(parent, writer.PARENT)
    with pytest.raises(SystemExit, match="parent discussion changed"):
        writer.main()
    assert not writer.TARGET.exists()


@pytest.mark.parametrize("changed", ["target", "proposal"])
def test_existing_output_drift_refused(isolated_writer, monkeypatch, changed):
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    if changed == "target":
        record = writer.build_record()
        record["definition"] += " Newer independent curation."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("newer proposal\n")
    before = writer.PARENT.read_bytes()
    with pytest.raises(SystemExit, match=f"Existing {changed} differs"):
        writer.main()
    assert writer.PARENT.read_bytes() == before
