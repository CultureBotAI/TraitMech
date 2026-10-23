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
    COHORT_C_PATHS,
    COHORT_D_GAPS,
    _verify_graph_invariants,
    build_cohort_a_graphs,
    build_cohort_b_discussion,
    build_cohort_c_discussion,
    build_cohort_c_graphs,
    build_cohort_d_discussion,
    process_all,
)
from traitmech.validation.write_validated import validate_trait  # noqa: E402


def test_cohort_a_and_b_disjoint_and_cover_24_records() -> None:
    assert len(COHORT_A_PATHS) == 10
    assert len(COHORT_B_GAPS) == 14
    assert len(COHORT_C_PATHS) == 10
    assert len(COHORT_D_GAPS) == 54
    all_sets = [
        set(COHORT_A_PATHS),
        set(COHORT_B_GAPS),
        set(COHORT_C_PATHS),
        set(COHORT_D_GAPS),
    ]
    for idx, s1 in enumerate(all_sets):
        assert "data/traits/physiology/spore_germination.yaml" not in s1
        for s2 in all_sets[idx + 1 :]:
            assert s1.isdisjoint(s2)


def test_cohort_a_committed_records_have_valid_connected_causal_graphs() -> None:
    expected_mechanistic = {
        "data/traits/environment/capnophilic.yaml",
        "data/traits/metabolism/pectin_degradation.yaml",
        "data/traits/morphology/polar_flagellation.yaml",
        "data/traits/physiology/bacteriocin_production.yaml",
        "data/traits/physiology/coagulase_activity.yaml",
    }
    for rel_path in COHORT_A_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = doc.get("causal_graphs")
        assert graphs and len(graphs) == 1, f"{rel_path}: missing causal_graphs"
        _verify_graph_invariants(rel_path, doc, graphs)
        expected_scope = "MECHANISTIC" if rel_path in expected_mechanistic else "NONMECHANISTIC"
        assert graphs[0]["scope_status"] == expected_scope, (
            f"{rel_path}: expected {expected_scope}, got {graphs[0]['scope_status']}"
        )
        assert doc.get("canonical_examples"), f"{rel_path}: missing canonical_examples"

    polar_doc = yaml.safe_load(
        (REPO_ROOT / "data/traits/morphology/polar_flagellation.yaml").read_text(encoding="utf-8")
    )
    polar_nodes = {n["node_id"]: n for n in polar_doc["causal_graphs"][0]["nodes"]}
    assert "polar_flagellation_flhf" in polar_nodes
    assert "polar_flagellation_flhg" in polar_nodes
    assert polar_nodes["polar_flagellation_flhf"]["grounding"] == "InterPro:IPR020006"
    assert polar_nodes["polar_flagellation_flhg"]["grounding"] == "InterPro:IPR033875"


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


def test_cohort_c_committed_records_have_valid_connected_causal_graphs_and_todo() -> None:
    for rel_path in COHORT_C_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = doc.get("causal_graphs")
        assert graphs and len(graphs) == 1, f"{rel_path}: missing causal_graphs"
        _verify_graph_invariants(rel_path, doc, graphs)
        assert graphs[0]["scope_status"] in {"NONMECHANISTIC", "MECHANISTIC"}
        graph_id = graphs[0]["graph_id"]
        disc_id = f"{path.stem.replace('_', '-')}-protein-example-gap"
        discussions = doc.get("discussions") or []
        matching = [d for d in discussions if d.get("discussion_id") == disc_id]
        assert len(matching) == 1, f"{rel_path}: missing {disc_id}"
        disc = matching[0]
        assert disc["kind"] == "CURATION_TODO"
        if graphs[0]["scope_status"] == "MECHANISTIC":
            assert disc["status"] == "RESOLVED"
        else:
            assert disc["status"] == "OPEN"
        assert disc["attaches_to"] == [f"causal_graphs#{graph_id}"]


def test_cohort_d_committed_records_have_open_knowledge_gap_discussions() -> None:
    for rel_path in sorted(COHORT_D_GAPS):
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        disc_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        discussions = doc.get("discussions") or []
        matching = [d for d in discussions if d.get("discussion_id") == disc_id]
        assert len(matching) == 1, f"{rel_path}: missing {disc_id}"
        disc = matching[0]
        assert disc["kind"] == "KNOWLEDGE_GAP"
        assert disc["status"] == "OPEN"
        assert disc["attaches_to"] == ["causal_graphs"]
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

    rel_c = COHORT_C_PATHS[0]
    doc_c = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_c).read_text(encoding="utf-8")))
    graphs_c = build_cohort_c_graphs(rel_c, doc_c)
    doc_c["causal_graphs"] = graphs_c
    doc_c["discussions"] = [build_cohort_c_discussion(rel_c, doc_c, graphs_c[0]["graph_id"])]
    assert validate_trait(doc_c) == []

    rel_d = sorted(COHORT_D_GAPS)[0]
    doc_d = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_d).read_text(encoding="utf-8")))
    doc_d["discussions"] = [build_cohort_d_discussion(rel_d, doc_d)]
    assert validate_trait(doc_d) == []
