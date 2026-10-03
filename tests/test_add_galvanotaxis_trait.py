"""Test galvanotaxis scope, source boundaries and fail-closed writes."""

import copy
import csv
import io
import sys
from collections import Counter
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_galvanotaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "galvanotaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_is_active_motility_not_passive_drift():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000581"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "biases its active movement" in record["definition"]
    assert "electric field" in record["definition"]
    assert "xrefs" not in record
    assert "synonyms" not in record
    assert "full paywalled paper was not accessed" in record["evidence"][0]["notes"]
    assert "Only the abstract was accessed" in record["evidence"][1]["notes"]
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_examples_keep_strain_direction_and_mutant_context():
    ecoli, salmonella = writer.build_record()["canonical_examples"]
    assert ecoli["taxon_id"] == "NCBITaxon:83333"
    assert ecoli["reference"] == writer.SHI
    assert "anode-directed" in ecoli["note"]
    assert salmonella["taxon_id"] == "NCBITaxon:588858"
    assert salmonella["reference"] == writer.SUN
    assert "IR715" in salmonella["note"] and "pGFT/RalFc" in salmonella["note"]
    assert "cathode at 2 V/cm" in salmonella["note"]
    assert "Do not substitute the SW473" in salmonella["note"]


def test_graph_is_connected_and_does_not_claim_a_sensor_or_single_gene_necessity():
    graph, = writer.build_record()["causal_graphs"]
    assert graph["scope_status"] == "MECHANISTIC"
    assert "not a complete electrical sensing" in graph["scope_notes"]
    assert "not individual FliC necessity" in graph["scope_notes"]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert len(nodes) == 5 and len(graph["edges"]) == 4
    assert nodes["galvanotaxis_trait"]["grounding"] == writer.IDENTIFIER
    assert nodes["galvanotaxis_flagellar_motility"]["grounding"] == "GO:0071973"
    assert "grounding" not in nodes["galvanotaxis_process"]
    protein = nodes["galvanotaxis_flagellin"]
    assert protein["grounding"] == "InterPro:IPR001492"
    assert protein["gene_symbols"] == ["fliC", "fljB"]
    example, = protein["protein_examples"]
    assert example["uniprot_id"] == "UniProtKB:A0A0F6B2U2"
    assert example["taxon_id"] == "NCBITaxon:588858"
    assert example["entry_status"] == "UNREVIEWED"
    assert example["proteome_id"] == "UP000002695"
    assert (example["entry_version"], example["sequence_version"]) == (42, 1)
    assert "individual FliC necessity was not established" in example["role"]
    assert "EBI Proteins API" in example["evidence"][0]["notes"]
    reached = {"galvanotaxis_trait"}
    while True:
        next_reached = reached | {
            endpoint for edge in graph["edges"]
            if edge["subject"] in reached or edge["object"] in reached
            for endpoint in (edge["subject"], edge["object"])
        }
        if next_reached == reached:
            break
        reached = next_reached
    assert reached == set(nodes)
    assert graph["edges"][-1]["predicate_id"] == "METPO:2007700"


def test_open_questions_do_not_import_unreconciled_numeric_directions():
    questions = writer.build_record()["discussions"]
    assert [q["kind"] for q in questions] == ["KNOWLEDGE_GAP", "CURATION_TODO"]
    assert all(q["status"] == "OPEN" for q in questions)
    assert "fixed-cell drift alone is not this phenotype" in questions[0]["rationale"]
    assert "coordinate conventions need reconciliation" in questions[1]["rationale"]
    assert "No numerical directedness values are imported" in questions[1]["rationale"]
    assert writer.SOURCE_DATA in questions[1]["rationale"]


def test_all_evidence_is_cited_and_quotation_budget_is_source_bounded():
    record = writer.build_record()
    graph, = record["causal_graphs"]
    items = list(record["evidence"])
    items.extend(item for edge in graph["edges"] for item in edge["evidence"])
    items.extend(item for node in graph["nodes"] for example in node.get("protein_examples", [])
                 for item in example["evidence"])
    words = Counter()
    for item in items:
        assert item["reference"].startswith(("DOI:", "https://"))
        assert len(item["snippet"]) >= 24 and item["notes"]
        words[item["reference"]] += len(item["snippet"].split())
    assert len(items) == 7
    assert set(words) == {writer.ADLER, writer.SHI, writer.SUN, writer.INTERPRO}
    assert max(words.values()) <= 25


def test_proposal_matches_identity_and_parent():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1053500"
    assert rows[2][1:3] == [record["label"], record["definition"]]
    assert rows[2][4] == record["parent_traits"][0]
    assert rows[2][5:7] == ["", ""]
    assert rows[2][10] == writer.IDENTIFIER


def test_dry_run_apply_and_idempotent_replay(isolated, monkeypatch):
    assert run(monkeypatch) == 0
    assert not snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert yaml.safe_load(writer.TARGET.read_text()) == writer.build_record()
    applied = snapshots(isolated)
    assert run(monkeypatch, True) == 0
    assert snapshots(isolated) == applied


@pytest.mark.parametrize("target", ["record", "proposal"])
def test_output_drift_refused_without_partial_writes(isolated, monkeypatch, target):
    if target == "record":
        record = writer.build_record()
        record["definition"] = "Unreviewed drift."
        writer.write_validated_trait(record, writer.TARGET)
    else:
        writer.PROPOSAL.mkdir()
        (writer.PROPOSAL / "metpo_proposal_classes_robot.tsv").write_text("Unreviewed drift")
    before = snapshots(isolated)
    with pytest.raises(SystemExit, match="differs"):
        run(monkeypatch, True)
    assert snapshots(isolated) == before


def test_invalid_record_cannot_write_either_output(isolated, monkeypatch):
    record = copy.deepcopy(writer.RECORD)
    record["unknown_slot"] = "invalid"
    monkeypatch.setattr(writer, "RECORD", record)
    with pytest.raises(Exception, match="unknown_slot"):
        run(monkeypatch, True)
    assert not snapshots(isolated)
