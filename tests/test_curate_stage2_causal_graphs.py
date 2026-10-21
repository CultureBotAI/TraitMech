"""Tests for Stage 2 causal_graphs and source-limited knowledge-gap curation."""

from __future__ import annotations

import copy
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from curate_stage2_causal_graphs import (  # noqa: E402
    COHORT_A_PATHS,
    COHORT_B_GAPS,
    _verify_graph_invariants,
    build_cohort_a_graphs,
    build_cohort_b_discussion,
    process_all,
)
from traitmech.validation.write_validated import validate_trait  # noqa: E402


def test_cohort_a_and_b_disjoint_and_cover_24_records() -> None:
    assert len(COHORT_A_PATHS) == 10
    assert len(COHORT_B_GAPS) == 14
    assert set(COHORT_A_PATHS).isdisjoint(set(COHORT_B_GAPS))
    assert "data/traits/physiology/spore_germination.yaml" not in set(COHORT_A_PATHS)
    assert "data/traits/physiology/spore_germination.yaml" not in set(COHORT_B_GAPS)


def test_cohort_a_committed_records_have_valid_connected_causal_graphs() -> None:
    for rel_path in COHORT_A_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = doc.get("causal_graphs")
        assert graphs and len(graphs) == 1, f"{rel_path}: missing causal_graphs"
        _verify_graph_invariants(rel_path, doc, graphs)


def test_cohort_b_committed_records_have_open_knowledge_gap_discussions() -> None:
    for rel_path in sorted(COHORT_B_GAPS):
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        disc_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        discussions = doc.get("discussions") or []
        matching = [d for d in discussions if d.get("discussion_id") == disc_id]
        assert len(matching) == 1, f"{rel_path}: missing {disc_id}"
        disc = matching[0]
        assert disc["kind"] == "KNOWLEDGE_GAP"
        assert disc["status"] == "OPEN"
        assert "attaches_to" not in disc
        assert disc.get("prompt", "").strip()
        assert disc.get("rationale", "").strip()
        assert disc.get("evidence"), f"{rel_path}: missing discussion evidence"


def test_process_all_is_idempotent_on_committed_corpus() -> None:
    assert process_all(apply=False) == (0, 0)


def test_builders_produce_closed_schema_valid_records() -> None:
    rel_a = COHORT_A_PATHS[0]
    doc_a = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_a).read_text(encoding="utf-8")))
    doc_a["causal_graphs"] = build_cohort_a_graphs(rel_a, doc_a)
    assert validate_trait(doc_a) == []

    rel_b = sorted(COHORT_B_GAPS)[0]
    doc_b = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_b).read_text(encoding="utf-8")))
    doc_b["discussions"] = [build_cohort_b_discussion(rel_b, doc_b)]
    assert validate_trait(doc_b) == []
