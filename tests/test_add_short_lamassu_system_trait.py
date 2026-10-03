"""Keep the short-Lamassu family distinct from effector and length bins."""

import copy
import csv
import hashlib
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import add_short_lamassu_system_trait as writer  # noqa: E402


@pytest.fixture
def isolated_writer(tmp_path, monkeypatch):
    originals = {}
    for attr, discussion_id, hash_attr in [
        ("PARENT", "lamassu-subtype-and-effector-gap", "PARENT_HASH"),
        ("HNH", "lamassu-hnh-function-and-model-scope", "HNH_HASH"),
    ]:
        path = getattr(writer, attr)
        record = yaml.safe_load(path.read_text())
        discussion = next(d for d in record["discussions"] if d["discussion_id"] == discussion_id)
        discussion["rationale"] = f"Controlled {attr} discussion preimage."
        monkeypatch.setattr(
            writer, hash_attr, hashlib.sha256(discussion["rationale"].encode()).hexdigest()
        )
        record["curation_history"] = []
        if attr == "HNH":
            record["parent_traits"] = ["traitmech:000232"]
        destination = tmp_path / path.name
        writer.write_validated_trait(record, destination)
        monkeypatch.setattr(writer, attr, destination)
        originals[attr] = record
    monkeypatch.setattr(writer, "TARGET", tmp_path / "short_lamassu_system.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    monkeypatch.setattr(sys, "argv", ["writer"])
    return originals


def test_family_scope_and_qualified_source_organism():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000570"
    assert record["parent_traits"] == ["traitmech:000232"]
    assert record["mapping_status"] == "PROPOSED"
    assert "short-LmuB family" in record["definition"]
    assert "coiled-coil" in record["definition"]
    assert "600" not in record["definition"]
    assert "causal_graphs" not in record
    assert "xrefs" not in record
    assert len(record["evidence"]) == 5
    assert len({e["reference"] for e in record["evidence"]}) == 2
    assert all(e["snippet"] and e["notes"] for e in record["evidence"])
    assert all(e["reference"] in (writer.PAPER, writer.STRUCTURE) for e in record["evidence"])
    example = record["canonical_examples"][0]
    assert example["taxon_id"] == "NCBITaxon:666"
    assert example["reference"] == writer.PAPER
    assert "heterologous E. coli host" in example["note"]
    assert "species-wide possession" in example["note"]
    assert "cutoff" in record["discussions"][0]["rationale"]
    record["synonyms"][0]["synonym_text"] = "mutated"
    assert writer.build_record()["synonyms"][0]["synonym_text"] == "short Lamassu"


def test_proposal_round_trip_and_existing_child_request():
    record = writer.build_record()
    rows = list(csv.DictReader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 2
    row = rows[1]
    assert len(row) == 11
    assert row["proposed_id"] == "METPO:1052400"
    assert row["parent"] == "METPO:1018600"
    assert row["label"] == record["label"]
    assert row["definition"] == record["definition"]
    assert row["traits_addressed"] == record["identifier"]
    assert row["synonyms"] == record["synonyms"][0]["synonym_text"]
    assert row["xrefs"] == ""
    assert "METPO:1052200" in row["observations"]


def test_dry_run_apply_and_reapply_preserve_evidence(isolated_writer, monkeypatch):
    before = {p: p.read_bytes() for p in (writer.PARENT, writer.HNH)}
    assert writer.main() == 0
    assert {p: p.read_bytes() for p in before} == before
    assert not writer.TARGET.exists()
    assert not writer.PROPOSAL.exists()
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    hnh = yaml.safe_load(writer.HNH.read_text())
    assert hnh["parent_traits"] == [writer.IDENTIFIER]
    for key in ("definition", "evidence", "canonical_examples", "synonyms"):
        assert hnh[key] == isolated_writer["HNH"][key]
    paths = [
        writer.TARGET,
        writer.PARENT,
        writer.HNH,
        writer.PROPOSAL / "metpo_proposal_classes_robot.tsv",
    ]
    first = [p.read_bytes() for p in paths]
    assert writer.main() == 0
    assert [p.read_bytes() for p in paths] == first


@pytest.mark.parametrize("attr", ["PARENT", "HNH"])
@pytest.mark.parametrize("drift", ["rationale", "status", "parent"])
def test_existing_record_drift_refused(isolated_writer, attr, drift):
    record = copy.deepcopy(isolated_writer[attr])
    if drift == "rationale":
        record["discussions"][0]["rationale"] += " Later independent curation."
    elif drift == "status":
        record["discussions"][0]["status"] = "RESOLVED"
    else:
        record["parent_traits"] = ["METPO:1000059"]
    writer.write_validated_trait(record, getattr(writer, attr))
    before = [p.read_bytes() for p in (writer.PARENT, writer.HNH)]
    with pytest.raises(SystemExit, match="changed"):
        writer.main()
    assert [p.read_bytes() for p in (writer.PARENT, writer.HNH)] == before
    assert not writer.TARGET.exists()


@pytest.mark.parametrize("drift", [False, True])
def test_review_accepts_only_exact_legacy_preimage(isolated_writer, monkeypatch, drift):
    legacy = writer.build_record()
    legacy["evidence"].append(
        {
            "reference": "https://example.org/legacy-taxonomy",
            "snippet": "Controlled legacy identity snippet.",
            "notes": "Controlled legacy identity evidence.",
        }
    )
    legacy["curation_history"].pop()
    writer.write_validated_trait(legacy, writer.TARGET)
    monkeypatch.setattr(
        writer, "LEGACY_TARGET_SHA256S", {hashlib.sha256(writer.TARGET.read_bytes()).hexdigest()}
    )
    if drift:
        legacy["evidence"][5]["notes"] += " Later independent curation."
        writer.write_validated_trait(legacy, writer.TARGET)
    paths = [writer.TARGET, writer.PARENT, writer.HNH]
    before = [p.read_bytes() for p in paths]
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    if drift:
        with pytest.raises(SystemExit, match="Existing target differs"):
            writer.main()
        assert [p.read_bytes() for p in paths] == before
    else:
        assert writer.main() == 0
        current = yaml.safe_load(writer.TARGET.read_text())
        assert len(current["evidence"]) == 5
        assert current["synonyms"][0]["synonym_text"] == "short Lamassu"
        assert current["curation_history"][:-1] == legacy["curation_history"]
        assert current["curation_history"][-1]["action"] == "REFINE_SYNONYM_AND_EVIDENCE_SCOPE"
        first = [p.read_bytes() for p in paths]
        assert writer.main() == 0
        assert [p.read_bytes() for p in paths] == first


def test_hnh_definition_drift_refused(isolated_writer):
    record = copy.deepcopy(isolated_writer["HNH"])
    record["definition"] += " Independently expanded scope."
    writer.write_validated_trait(record, writer.HNH)
    with pytest.raises(SystemExit, match="biological scope changed"):
        writer.main()
    assert not writer.TARGET.exists()


@pytest.mark.parametrize("changed", ["target", "proposal"])
def test_output_drift_refused(isolated_writer, monkeypatch, changed):
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    assert writer.main() == 0
    if changed == "target":
        record = writer.build_record()
        record["definition"] += " Newer curation."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("newer proposal\n")
    before = [p.read_bytes() for p in (writer.PARENT, writer.HNH)]
    with pytest.raises(SystemExit, match=f"Existing {changed} differs"):
        writer.main()
    assert [p.read_bytes() for p in (writer.PARENT, writer.HNH)] == before


@pytest.mark.parametrize("drift", [False, True])
def test_proposal_review_accepts_only_exact_preimage(isolated_writer, monkeypatch, drift):
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(writer.build_record())), delimiter="\t"))
    rows[2][5] = "Controlled legacy synonym"
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    writer.PROPOSAL.mkdir()
    path = writer.PROPOSAL / "metpo_proposal_classes_robot.tsv"
    path.write_text(stream.getvalue())
    monkeypatch.setattr(
        writer, "LEGACY_PROPOSAL_SHA256", hashlib.sha256(path.read_bytes()).hexdigest()
    )
    if drift:
        path.write_text(stream.getvalue() + "Later independent proposal edit.\n")
    paths = [writer.PARENT, writer.HNH, path]
    before = [p.read_bytes() for p in paths]
    monkeypatch.setattr(sys, "argv", ["writer", "--apply"])
    if drift:
        with pytest.raises(SystemExit, match="Existing proposal differs"):
            writer.main()
        assert [p.read_bytes() for p in paths] == before
        assert not writer.TARGET.exists()
    else:
        assert writer.main() == 0
        assert path.read_text() == writer.proposal_tsv(writer.build_record())
        first = [p.read_bytes() for p in paths]
        assert writer.main() == 0
        assert [p.read_bytes() for p in paths] == first
