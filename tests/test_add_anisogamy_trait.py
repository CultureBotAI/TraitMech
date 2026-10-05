"""Guard anisogamy scope, evidence roles and fail-closed curation writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_anisogamy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "anisogamy.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_and_scope():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000620"
    assert record["label"] == "anisogamy"
    assert record["definition"] == (
        "A sexual-reproduction phenotype in which the fusing gametes belong to "
        "two types that differ in size, with smaller male and larger female gametes."
    )
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["term_kind"] == "CLASS"
    assert record["parent_traits"] == ["METPO:1000059"]
    assert not any(k in record for k in ["synonyms", "xrefs", "causal_graphs"])
    event, = record["curation_history"]
    assert event["action"] == "MINTED_TRAITMECH_ID"
    assert event["llm_assisted"] and event["curator"] == "codex"
    scope, mechanism = record["discussions"]
    assert scope["status"] == mechanism["status"] == "OPEN"
    for text in ["including oogamy", "four-type classification", "not universal",
                 "No numerical threshold", "traitmech:000619", "filesystem category"]:
        assert text in scope["rationale"]
    for text in ["not a literal MID locus", "NONMECHANISTIC", "strain mismatch",
                 "blank mutation field", "abstract-resolver verdicts"]:
        assert text in mechanism["rationale"]


def test_evidence_roles_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.HAMAJI_2018
    definition, experiment, hierarchy = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.HAMAJI_2018, writer.NOZAKI_2014, writer.LINDSEY_2024,
    }
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    assert "\u2014anisogamy\u2014" in definition["snippet"]
    for text in ["scientific-abstract", "editorial summary", "NIES-4100/4018",
                 "NIES-3985/3984", "do not demonstrate", "remain unread"]:
        assert text in definition["notes"]
    for text in ["not C. angeleri", "male".capitalize(), "female diameter",
                 "volume ratio", "Table S1", "uninspected"]:
        assert text in experiment["notes"]
    assert "not a new gamete-fusion experiment" in hierarchy["notes"]
    assert "Background Sec1" in hierarchy["notes"]


def test_canonical_example_has_direct_support_and_qualified_provenance():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:51706"
    assert example["taxon_label"] == "Colemanosphaera charkowiensis"
    assert example["reference"] == writer.NOZAKI_2014
    for text in ["mixed 2013-0615-IC-3/4/7", "nitrogen-deficient", "natural water",
                 "NIES-3388", "NIES-3386", "NIES-3387", "dates conflict",
                 "not projected", "not independent", "id=51706"]:
        assert text in example["note"]


def test_proposal_parity_and_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1057400"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert all(e["reference"] in rows[2][3] for e in record["evidence"])
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    before = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == before


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_drift_refused_without_partial_writes(isolated, monkeypatch, target):
    if target == "record":
        record = writer.build_record()
        record["parent_traits"] = ["traitmech:000619"]
        writer.write_validated_trait(record, writer.TARGET)
    else:
        writer.PROPOSAL.mkdir()
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Unreviewed drift")
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


def test_invalid_record_cannot_write_outputs(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert not snapshots(isolated)
