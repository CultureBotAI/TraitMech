"""Regression tests for the biosafety_level_5 review in issue #183."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from review_biosafety_level_5_graph_183 import (  # noqa: E402
    ACTION,
    AFTER_DEFINITION_SOURCE,
    AFTER_GRAPH,
    AFTER_RECORD_EVIDENCE,
    BEFORE_DEFINITION_SOURCE,
    BEFORE_GRAPH,
    BEFORE_RECORD_EVIDENCE,
    SLUG,
    transform,
)


def _current() -> dict:
    path = ROOT / "data" / "traits" / f"{SLUG}.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _before() -> dict:
    doc = _current()
    doc["definition_source"] = BEFORE_DEFINITION_SOURCE
    doc["evidence"] = copy.deepcopy(BEFORE_RECORD_EVIDENCE)
    doc["causal_graphs"] = [copy.deepcopy(BEFORE_GRAPH)]
    return doc


def _transform_from_before() -> dict:
    doc = _before()

    assert transform(SLUG, doc)
    return doc


def test_review_replaces_generalized_hazard_graph_with_ppl_alpha_context():
    doc = _transform_from_before()
    graph = doc["causal_graphs"][0]

    assert doc["curation_history"][-1]["action"] == ACTION
    assert doc["definition_source"] == AFTER_DEFINITION_SOURCE
    assert doc["evidence"] == AFTER_RECORD_EVIDENCE
    assert graph == AFTER_GRAPH
    assert graph["scope_status"] == "NONMECHANISTIC"

    edge_keys = {
        (edge["subject"], edge["predicate"], edge["object"])
        for edge in graph["edges"]
    }
    assert ("enhanced_pathogen_hazard", "motivates", "bsl5_trait") not in edge_keys
    assert (
        "planetary_protection_level_alpha",
        "was informally called",
        "bsl5_trait",
    ) in edge_keys

    assert len(graph["edges"]) == 8
    assert all(
        item.get("reference") and item.get("snippet")
        for edge in graph["edges"]
        for item in edge["evidence"]
    )


def test_repaired_record_is_exactly_idempotent():
    doc = _transform_from_before()
    before = copy.deepcopy(doc)

    assert not transform(SLUG, doc)
    assert doc == before


def test_refuses_source_record_evidence_drift_before_migration():
    doc = _before()
    doc["evidence"][0]["notes"] = "drift"

    with pytest.raises(ValueError, match="source record evidence drifted"):
        transform(SLUG, doc)


def test_refuses_source_definition_source_drift_before_migration():
    doc = _before()
    doc["definition_source"] = "DOI:10.1/drift"

    with pytest.raises(ValueError, match="source definition_source drifted"):
        transform(SLUG, doc)


def test_refuses_source_graph_drift_before_migration():
    doc = _before()
    doc["causal_graphs"][0]["nodes"][0]["label"] = "drift"

    with pytest.raises(ValueError, match="source graph drifted"):
        transform(SLUG, doc)


def test_refuses_migrated_graph_drift_after_migration():
    doc = _transform_from_before()
    doc["causal_graphs"][0]["edges"][0]["description"] = "drift"

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)


def test_refuses_partial_replay():
    doc = _before()
    doc["causal_graphs"] = [copy.deepcopy(AFTER_GRAPH)]

    with pytest.raises(ValueError, match="partial evidence replay"):
        transform(SLUG, doc)
