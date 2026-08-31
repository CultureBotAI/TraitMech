"""Regression tests for quorum-sensing exemplar semantics (#521)."""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RECORD = REPO_ROOT / "data" / "traits" / "physiology" / "quorum_sensing.yaml"


def _record() -> dict:
    return yaml.safe_load(RECORD.read_text(encoding="utf-8"))


def test_quenching_protein_source_is_not_a_trait_exemplar():
    record = _record()
    canonical_taxa = {
        example["taxon_id"] for example in record["canonical_examples"]
    }
    protein_examples = {
        example["uniprot_id"]: example
        for node in record["causal_graphs"][0]["nodes"]
        for example in node.get("protein_examples", [])
    }

    assert protein_examples["UniProtKB:P12747"]["taxon_id"] in canonical_taxa
    assert protein_examples["UniProtKB:P0CJ63"]["taxon_id"] not in canonical_taxa


def test_positive_luxi_mechanism_anchors_the_canonical_exemplar():
    graph = _record()["causal_graphs"][0]
    nodes = {node["node_id"]: node for node in graph["nodes"]}
    edges = {
        (edge["subject"], edge["predicate"], edge["object"]): edge
        for edge in graph["edges"]
    }

    synthase = nodes["autoinducer_synthase"]
    assert synthase["grounding"] == "GO:0061579"
    assert synthase["protein_examples"][0]["uniprot_id"] == "UniProtKB:P12747"
    assert (
        edges[("autoinducer_synthase", "produces", "autoinducer")]["predicate_id"]
        == "METPO:2007800"
    )
    assert ("signal_receptor", "positively regulates", "autoinducer_synthase") in edges
