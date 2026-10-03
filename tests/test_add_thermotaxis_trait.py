"""Test thermotaxis scope, graph semantics and fail-closed writer behavior."""

import copy
import csv
import io
import sys
from collections import Counter
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import add_thermotaxis_trait as writer  # noqa: E402


@pytest.fixture
def isolated(tmp_path, monkeypatch):
    monkeypatch.setattr(writer, "TARGET", tmp_path / "thermotaxis.yaml")
    monkeypatch.setattr(writer, "PROPOSAL", tmp_path / "proposal")
    return tmp_path


def run(monkeypatch, apply=False):
    monkeypatch.setattr(sys, "argv", ["writer"] + (["--apply"] if apply else []))
    return writer.main()


def snapshots(root):
    return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_identity_is_temperature_guided_motility_not_growth_or_chemotaxis():
    record = writer.build_record()
    assert record["identifier"] == "traitmech:000580"
    assert record["mapping_status"] == "PROPOSED"
    assert record["trait_category"] == "PHYSIOLOGY"
    assert record["parent_traits"] == ["METPO:1000702"]
    assert "biases its active movement" in record["definition"]
    assert "temperature gradient" in record["definition"]
    assert "growth" not in record["definition"]
    assert "xrefs" not in record
    assert "universal trait thresholds" in record["evidence"][1]["notes"]
    assert "passive thermophoresis" in record["discussions"][0]["rationale"]
    assert record["curation_history"][-1]["llm_assisted"] is True


def test_canonical_example_does_not_conflate_behavior_reporters_and_growth():
    record = writer.build_record()
    example, = record["canonical_examples"]
    assert example["taxon_id"] == "NCBITaxon:83333"
    assert example["taxon_label"] == "Escherichia coli K-12"
    assert example["reference"] == writer.PAULICK
    assert "AW405" in example["note"] and "GFP marker" in example["note"]
    assert "not the engineered VS223 FRET reporter" in example["note"]
    assert "MG1655 growth assay" in example["note"]
    assert "2017-08-31" in record["evidence"][0]["notes"]
    assert "elife-26607-v2.pdf" in record["evidence"][0]["notes"]


def test_tar_graph_is_connected_scoped_and_separates_instance_from_process():
    graph, = writer.build_record()["causal_graphs"]
    assert graph["scope_status"] == "MECHANISTIC"
    assert "not a universal microbial mechanism" in graph["scope_notes"]
    assert "complete Tar/Tsr accumulation model" in graph["scope_notes"]
    nodes = {n["node_id"]: n for n in graph["nodes"]}
    assert len(nodes) == 6
    assert len(graph["edges"]) == 5
    trait = nodes["thermotaxis_trait"]
    process = nodes["thermotaxis_migration_process"]
    assert (trait["node_type"], trait["grounding"]) == ("TRAIT", writer.IDENTIFIER)
    assert (process["node_type"], process["grounding"]) == ("BIOLOGICAL_PROCESS", "GO:0043052")
    protein = nodes["thermotaxis_tar_receptor"]
    assert protein["grounding_status"] == "REVIEWED_LABEL_ONLY"
    assert "grounding" not in protein
    assert "domain, not the full receptor" in protein["grounding_notes"]
    example, = protein["protein_examples"]
    assert example["uniprot_id"] == "UniProtKB:P07017"
    assert example["gene_symbol"] == "tar"
    assert example["taxon_id"] == "NCBITaxon:83333"
    assert example["entry_status"] == "REVIEWED"
    assert (example["entry_version"], example["sequence_version"]) == (208, 2)
    assert "not the entire receptor array" in example["role"]
    reached = {"thermotaxis_trait"}
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
    assert all(e["subject"] in nodes and e["object"] in nodes for e in graph["edges"])


def test_all_evidence_is_cited_and_quotation_budget_is_source_bounded():
    record = writer.build_record()
    graph, = record["causal_graphs"]
    items = list(record["evidence"])
    items.extend(item for edge in graph["edges"] for item in edge["evidence"])
    items.extend(item for node in graph["nodes"] for example in node.get("protein_examples", [])
                 for item in example["evidence"])
    words = Counter()
    for item in items:
        assert item["reference"].startswith("DOI:")
        assert len(item["snippet"]) >= 24 and item["notes"]
        words[item["reference"]] += len(item["snippet"].split())
    assert set(words) == {writer.PAULICK, writer.PASTER, writer.NARA, writer.NISHIYAMA}
    assert max(words.values()) <= 25


def test_proposal_matches_identity_parent_and_mapping_scope():
    record = writer.build_record()
    rows = list(csv.reader(io.StringIO(writer.proposal_tsv(record)), delimiter="\t"))
    assert len(rows) == 3 and {len(row) for row in rows} == {11}
    assert rows[1][-3:] == ["", "", ""]
    assert rows[2][0] == "METPO:1053400"
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
