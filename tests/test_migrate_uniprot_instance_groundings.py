"""Tests for the curated UniProt instance-grounding migration."""

from pathlib import Path
import csv
import sys

import yaml

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from migrate_uniprot_instance_groundings import (  # noqa: E402
    migrate_doc,
    reconcile_candidate_rows,
    unhandled_labels,
)


def _doc(label: str, grounding: str, node_type: str = "GENE_OR_PROTEIN") -> dict:
    return {
        "causal_graphs": [{
            "nodes": [{
                "node_id": "n1",
                "label": label,
                "node_type": node_type,
                "grounding": grounding,
            }]
        }]
    }


def test_replaces_instance_with_family_grounding():
    doc = _doc("FtsZ", "UniProtKB:C0LUM8")
    assert migrate_doc(doc) == [("n1", "UniProtKB:C0LUM8", "InterPro:IPR000158")]
    assert doc["causal_graphs"][0]["nodes"][0]["grounding"] == "InterPro:IPR000158"


def test_replaces_oxidase_instance_with_complex_not_activity():
    doc = _doc("cytochrome c oxidase", "UniProtKB:P98055")
    assert migrate_doc(doc) == [("n1", "UniProtKB:P98055", "GO:0045277")]
    assert doc["causal_graphs"][0]["nodes"][0]["grounding"] != "GO:0004129"


def test_retracts_unresolved_generic_label():
    doc = _doc("terminal oxidase", "UniProtKB:A0A2U9ILE5")
    assert migrate_doc(doc) == [("n1", "UniProtKB:A0A2U9ILE5", None)]
    assert "grounding" not in doc["causal_graphs"][0]["nodes"][0]


def test_ignores_non_uniprot_and_non_gene_nodes():
    go_doc = _doc("FtsZ", "InterPro:IPR000158")
    chemical_doc = _doc("FtsZ", "UniProtKB:C0LUM8", node_type="CHEMICAL")
    assert migrate_doc(go_doc) == []
    assert migrate_doc(chemical_doc) == []


def test_preflight_reports_unreviewed_labels():
    docs = {Path("x.yaml"): _doc("new protein", "UniProtKB:P12345")}
    assert unhandled_labels(docs) == {"new protein"}


def test_reconciles_candidate_inventory_with_curator_decisions():
    rows = [
        {"label": "FtsZ", "current_grounding": "UniProtKB:C0LUM8"},
        {"label": "terminal oxidase", "current_grounding": "UniProtKB:X"},
        {"label": "unrelated", "current_grounding": ""},
    ]
    assert reconcile_candidate_rows(rows, {"ftsz": 6, "terminal oxidase": 2}) == 2
    assert rows[0]["current_grounding"] == "InterPro:IPR000158"
    assert rows[0]["curator_decision"] == "APPLIED"
    assert rows[1]["current_grounding"] == ""
    assert rows[1]["curator_decision"] == "RETRACTED"
    assert rows[2] == {"label": "unrelated", "current_grounding": ""}


def test_corpus_and_mapping_have_no_unpaired_uniprot_instances():
    repo = Path(__file__).resolve().parents[1]
    offenders = []
    for path in (repo / "data/traits").glob("*/*.yaml"):
        doc = yaml.safe_load(path.read_text()) or {}
        for graph in doc.get("causal_graphs") or []:
            for node in graph.get("nodes") or []:
                if str(node.get("grounding", "")).startswith("UniProtKB:"):
                    offenders.append(f"{path.name}:{node.get('node_id')}")
    assert offenders == []

    with (repo / "mappings/node_grounding.tsv").open(newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        mapped = [
            row["label"]
            for row in rows
            if row["target_curie"].startswith("UniProtKB:")
        ]
    assert mapped == []
