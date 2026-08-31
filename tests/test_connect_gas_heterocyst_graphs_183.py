"""Regression tests for the gas-vesicle/heterocyst issue #183 tranche."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from connect_gas_heterocyst_graphs_183 import (  # noqa: E402
    ACTION,
    ADDITIONS,
    EXPECTED_COMPONENTS,
    REMOVALS,
    _components,
    _edge_key,
    transform,
)


def _current(slug: str) -> dict:
    path = ROOT / "data" / "traits" / f"{slug}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before(slug: str) -> dict:
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    new_keys = {_edge_key(edge) for edge in ADDITIONS[slug]}
    graph["edges"] = [edge for edge in graph["edges"] if _edge_key(edge) not in new_keys]
    if slug == "morphology/heterocyst":
        graph["nodes"].extend([
            {
                "node_id": "furc_perr",
                "label": "FurC/PerR transcriptional regulator",
                "node_type": "GENE_OR_PROTEIN",
            },
            {
                "node_id": "hetr_promoter",
                "label": "hetR promoter",
                "node_type": "CELLULAR_LOCALIZATION",
            },
        ])
        graph["edges"].append({
            "subject": "furc_perr",
            "predicate": "binds promoter of",
            "object": "hetr_promoter",
            "evidence": [{"reference": "DOI:10.1371/journal.pone.0289761"}],
        })
    return doc


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_reaches_one_component_with_exact_snippet_backed_edges(slug: str):
    doc = _before(slug)
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS[slug]

    assert transform(slug, doc)

    graph = doc["causal_graphs"][0]
    assert _components(graph) == 1
    by_key = {_edge_key(edge): edge for edge in graph["edges"]}
    for expected in ADDITIONS[slug]:
        assert by_key[_edge_key(expected)] == expected
        assert all(
            item.get("reference") and item.get("snippet")
            for item in expected["evidence"]
        )
    assert doc["curation_history"][-1]["action"] == ACTION


def test_unresolved_furc_promoter_island_is_removed_without_a_bridge():
    slug = "morphology/heterocyst"
    doc = _before(slug)

    assert transform(slug, doc)

    graph = doc["causal_graphs"][0]
    node_ids = {node["node_id"] for node in graph["nodes"]}
    edge_keys = {_edge_key(edge) for edge in graph["edges"]}
    assert not (REMOVALS[slug]["nodes"] & node_ids)
    assert not (REMOVALS[slug]["edges"] & edge_keys)


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repaired_record_is_exactly_idempotent(slug: str):
    doc = _current(slug)
    before = copy.deepcopy(doc)

    assert not transform(slug, doc)
    assert doc == before


def test_refuses_connector_metadata_drift_after_migration():
    slug = "morphology/gas_vesicle"
    doc = _current(slug)
    graph = doc["causal_graphs"][0]
    key = _edge_key(ADDITIONS[slug][0])
    next(edge for edge in graph["edges"] if _edge_key(edge) == key)["description"] = "drift"

    with pytest.raises(ValueError, match="connector drifted"):
        transform(slug, doc)
