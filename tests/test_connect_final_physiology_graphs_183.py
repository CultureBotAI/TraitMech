"""Regression tests for the final five physiology graph repairs in #183."""

from __future__ import annotations
import copy
import sys
from pathlib import Path
import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from connect_final_physiology_graphs_183 import (  # noqa: E402
    ACTION,
    ADDITIONS,
    EXPECTED_COMPONENTS,
    REMOVALS,
    _components,
    _edge_key,
    transform,
)


def current(slug: str) -> dict:
    return yaml.safe_load((ROOT / "data" / "traits" / f"{slug}.yaml").read_text())


def before(slug: str) -> dict:
    doc = current(slug)
    graph = doc["causal_graphs"][0]
    keys = {_edge_key(e) for e in ADDITIONS[slug]}
    graph["edges"] = [e for e in graph["edges"] if _edge_key(e) not in keys]
    removal = REMOVALS.get(slug)
    if removal:
        graph["nodes"].extend(
            [
                {
                    "node_id": "conductive_pili_cytochromes",
                    "label": "conductive pili and cytochromes",
                    "node_type": "GENE_OR_PROTEIN",
                    "description": "Conductive structures associated with direct interspecies electron transfer.",
                },
                {
                    "node_id": "diet",
                    "label": "direct interspecies electron transfer",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Electron exchange between syntrophic partners.",
                },
            ]
        )
        graph["edges"].append(
            {
                "subject": "conductive_pili_cytochromes",
                "predicate": "enables",
                "object": "diet",
                "description": "Conductive structures enable DIET.",
                "evidence": [{"reference": "DOI:10.3390/life14050591"}],
            }
        )
    return doc


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_reaches_one_component(slug: str):
    doc = before(slug)
    assert _components(doc["causal_graphs"][0]) == EXPECTED_COMPONENTS[slug]
    assert transform(slug, doc)
    assert _components(doc["causal_graphs"][0]) == 1
    assert doc["curation_history"][-1]["action"] == ACTION


@pytest.mark.parametrize("slug", sorted(ADDITIONS))
def test_repair_is_idempotent(slug: str):
    doc = current(slug)
    snapshot = copy.deepcopy(doc)
    assert not transform(slug, doc)
    assert doc == snapshot


def test_refuses_partial_replay():
    slug = "physiology/chemolithotrophic"
    doc = before(slug)
    doc["causal_graphs"][0]["edges"].append(copy.deepcopy(ADDITIONS[slug][0]))
    with pytest.raises(ValueError, match="partial connector replay"):
        transform(slug, doc)


def test_refuses_removal_drift():
    slug = "physiology/lithoheterotrophic"
    doc = before(slug)
    doc["causal_graphs"][0]["nodes"] = [
        n for n in doc["causal_graphs"][0]["nodes"] if n["node_id"] != "diet"
    ]
    with pytest.raises(ValueError, match="connected graph does not match exact migration state"):
        transform(slug, doc)
