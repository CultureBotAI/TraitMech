from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from migrate_process_quality_consistency import DECISIONS, normalize_document


def graph_doc(node_id: str, node_type: str) -> dict:
    return {
        "causal_graphs": [
            {
                "nodes": [{"node_id": node_id, "label": node_id, "node_type": node_type}],
                "edges": [
                    {
                        "subject": "driver",
                        "predicate": "causes",
                        "object": node_id,
                    }
                ],
            }
        ]
    }


@pytest.mark.parametrize(
    ("old_id", "old_type", "new_id", "new_type"),
    [
        ("inside_positive_membrane_potential", "QUALITY", "reversed_membrane_potential", "STATE"),
        ("membrane_proton_permeability", "BIOLOGICAL_PROCESS", "proton_permeability", "QUALITY"),
        ("membrane_rigidification", "BIOLOGICAL_PROCESS", "membrane_rigidity", "QUALITY"),
        ("positive_dna_supercoiling", "QUALITY", "dna_positive_supercoiling", "BIOLOGICAL_PROCESS"),
    ],
)
def test_aliases_rename_nodes_and_edges(old_id, old_type, new_id, new_type):
    doc = graph_doc(old_id, old_type)
    in_scope, changes = normalize_document(doc)
    node = doc["causal_graphs"][0]["nodes"][0]
    edge = doc["causal_graphs"][0]["edges"][0]
    assert node["node_id"] == new_id
    assert node["node_type"] == new_type
    assert edge["object"] == new_id
    assert in_scope == [new_id]
    assert changes


def test_an_existing_canonical_node_is_in_scope_without_a_change():
    doc = graph_doc("proton_permeability", "QUALITY")
    doc["causal_graphs"][0]["nodes"][0]["label"] = "membrane proton permeability"
    assert normalize_document(doc) == (["proton_permeability"], [])


def test_enables_is_replaced_when_the_object_becomes_a_quality():
    doc = graph_doc("maximal_growth_rate", "BIOLOGICAL_PROCESS")
    edge = doc["causal_graphs"][0]["edges"][0]
    edge["predicate"] = "enables"
    edge["description"] = "Balanced conditions enable peak growth."
    normalize_document(doc)
    assert edge["predicate"] == "promotes"
    assert edge["predicate_id"] == "RO:0002213"
    assert edge["description"] == "Balanced conditions promote peak growth."


def test_rename_refuses_to_collide_with_an_existing_node():
    doc = graph_doc("membrane_rigidification", "QUALITY")
    doc["causal_graphs"][0]["nodes"].append(
        {"node_id": "membrane_rigidity", "label": "rigidity", "node_type": "QUALITY"}
    )
    with pytest.raises(ValueError, match="already in graph"):
        normalize_document(doc)


def test_every_decision_has_a_permanent_rationale():
    assert all(decision.rationale and "->" not in decision.rationale for decision in DECISIONS.values())


def test_live_corpus_has_only_canonical_ids_and_types_after_migration():
    import yaml

    seen: dict[str, set[str]] = {}
    aliases = {
        old_id
        for old_id, decision in DECISIONS.items()
        if old_id != decision.canonical_id
    }
    for path in Path("data/traits").rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text())
        for graph in doc.get("causal_graphs") or []:
            for node in graph.get("nodes") or []:
                node_id = node.get("node_id")
                assert node_id not in aliases
                if node_id in DECISIONS:
                    seen.setdefault(node_id, set()).add(node.get("node_type"))
    expected = {
        decision.canonical_id: {decision.node_type}
        for decision in DECISIONS.values()
    }
    assert seen == expected
