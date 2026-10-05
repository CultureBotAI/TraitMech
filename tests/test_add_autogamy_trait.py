"""Guard autogamy scope, source limits and fail-closed writes."""

import copy
import csv
import io
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_autogamy_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "autogamy.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_scope_and_provenance():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000622"
    assert record["label"] == "autogamy"
    assert record["definition"] == (
        "A sexual-reproduction phenotype in which two meiotically derived gametic "
        "nuclei formed within one unpaired cell fuse with each other."
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
    for text in ["fungal-scoped", "Cytogamy", "No universal genetic identity",
                 "filesystem category", "METPO:1000059"]:
        assert text in scope["rationale"]
    assert "not counted as evidence" in mechanism["rationale"]


def test_evidence_roles_and_limits():
    record = writer.build_record()
    assert record["definition_source"] == writer.NOBILI_1967
    historical, abstract, modern = record["evidence"]
    assert {e["reference"] for e in record["evidence"]} == {
        writer.NOBILI_1967, writer.BERGER_1986, writer.THIND_2020,
    }
    assert all(10 <= len(e["snippet"].split()) <= 25 for e in record["evidence"])
    for text in ["typeset", "serially fixed", "inferred", "not whole-genome"]:
        assert text in historical["notes"]
    assert "Full text, actual figures" in abstract["notes"]
    for text in ["macronuclear fragmentation", "stock d12", "not a canonical",
                 "remaining sections and supplements were not audited"]:
        assert text in modern["notes"]


def test_example_preserves_source_name_and_natural_strain():
    example, = writer.build_record()["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:74792"
    assert example["taxon_label"] == "Moneuplotes minuta"
    assert example["reference"] == writer.NOBILI_1967
    for text in ["A-25", "Euplotes minuta", "coastal sand", "5G/20",
                 "also conjugates", "no exact collection year", "id=74792",
                 "does not authenticate"]:
        assert text in example["note"]


def test_proposal_parity():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(r) for r in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1057500"
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
        record["parent_traits"] = ["traitmech:000609"]
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
