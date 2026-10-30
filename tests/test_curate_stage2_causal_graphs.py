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
    COHORT_E_PATHS,
    COHORT_F_GAPS,
    COHORT_G_PATHS,
    COHORT_H_PATHS,
    COHORT_I_PATHS,
    COHORT_J_PATHS,
    _verify_graph_invariants,
    build_cohort_a_graphs,
    build_cohort_b_discussion,
    build_cohort_c_discussion,
    build_cohort_c_graphs,
    build_cohort_d_discussion,
    build_cohort_e_discussion,
    build_cohort_e_graphs,
    build_cohort_f_discussion,
    build_cohort_g_discussion,
    build_cohort_g_graphs,
    build_cohort_h_discussion,
    build_cohort_h_graphs,
    build_cohort_i_discussion,
    build_cohort_i_graphs,
    build_cohort_j_discussion,
    build_cohort_j_graphs,
    process_all,
)
from traitmech.validation.write_validated import validate_trait  # noqa: E402


def test_cohort_a_and_b_disjoint_and_cover_24_records() -> None:
    assert len(COHORT_A_PATHS) == 10
    assert len(COHORT_B_GAPS) == 14
    assert len(COHORT_C_PATHS) == 10
    assert len(COHORT_D_GAPS) == 41
    assert len(COHORT_E_PATHS) == 3
    assert len(COHORT_F_GAPS) == 30
    assert len(COHORT_G_PATHS) == 3
    assert len(COHORT_H_PATHS) == 3
    assert len(COHORT_I_PATHS) == 3
    assert len(COHORT_J_PATHS) == 3
    all_sets = [
        set(COHORT_A_PATHS),
        set(COHORT_B_GAPS),
        set(COHORT_C_PATHS),
        set(COHORT_D_GAPS),
        set(COHORT_E_PATHS),
        set(COHORT_F_GAPS),
        set(COHORT_G_PATHS),
        set(COHORT_H_PATHS),
        set(COHORT_I_PATHS),
        set(COHORT_J_PATHS),
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
        if rel_path in COHORT_E_PATHS:
            assert disc["status"] == "RESOLVED"
            assert "attaches_to" not in disc
        else:
            assert disc["status"] == "OPEN"
            assert disc["attaches_to"] == ["causal_graphs"]
        assert disc.get("prompt", "").strip()
        assert disc.get("rationale", "").strip()
        assert disc.get("evidence"), f"{rel_path}: missing discussion evidence"


def test_cohort_e_committed_records_have_valid_connected_causal_graphs_and_todo() -> None:
    for rel_path in COHORT_E_PATHS:
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


def test_cohort_f_committed_records_have_open_knowledge_gap_discussions() -> None:
    for rel_path in sorted(COHORT_F_GAPS):
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


def test_cohort_g_committed_records_have_valid_connected_causal_graphs_and_todo() -> None:
    for rel_path in COHORT_G_PATHS:
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


def test_cohort_h_committed_records_have_valid_connected_causal_graphs_and_todo() -> None:
    for rel_path in COHORT_H_PATHS:
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


def test_cohort_i_committed_records_have_valid_connected_causal_graphs_and_todo() -> None:
    for rel_path in COHORT_I_PATHS:
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


def test_cohort_j_committed_records_have_valid_connected_causal_graphs_and_todo() -> None:
    for rel_path in COHORT_J_PATHS:
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
        source_gap_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        source_gaps = [d for d in discussions if d.get("discussion_id") == source_gap_id]
        assert len(source_gaps) == 1, f"{rel_path}: missing {source_gap_id}"
        assert source_gaps[0]["status"] == "RESOLVED"
        assert source_gaps[0]["attaches_to"] == [f"causal_graphs#{graph_id}"]


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

    rel_e = COHORT_E_PATHS[0]
    doc_e = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_e).read_text(encoding="utf-8")))
    graphs_e = build_cohort_e_graphs(rel_e, doc_e)
    doc_e["causal_graphs"] = graphs_e
    doc_e["discussions"] = [build_cohort_e_discussion(rel_e, doc_e, graphs_e[0]["graph_id"])]
    assert validate_trait(doc_e) == []

    rel_f = sorted(COHORT_F_GAPS)[0]
    doc_f = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_f).read_text(encoding="utf-8")))
    doc_f["discussions"] = [build_cohort_f_discussion(rel_f, doc_f)]
    assert validate_trait(doc_f) == []

    rel_g = COHORT_G_PATHS[0]
    doc_g = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_g).read_text(encoding="utf-8")))
    graphs_g = build_cohort_g_graphs(rel_g, doc_g)
    doc_g["causal_graphs"] = graphs_g
    doc_g["discussions"] = [build_cohort_g_discussion(rel_g, doc_g, graphs_g[0]["graph_id"])]
    assert validate_trait(doc_g) == []

    rel_h = COHORT_H_PATHS[0]
    doc_h = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_h).read_text(encoding="utf-8")))
    graphs_h = build_cohort_h_graphs(rel_h, doc_h)
    doc_h["causal_graphs"] = graphs_h
    doc_h["discussions"] = [build_cohort_h_discussion(rel_h, doc_h, graphs_h[0]["graph_id"])]
    assert validate_trait(doc_h) == []

    rel_i = COHORT_I_PATHS[0]
    doc_i = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_i).read_text(encoding="utf-8")))
    graphs_i = build_cohort_i_graphs(rel_i, doc_i)
    doc_i["causal_graphs"] = graphs_i
    doc_i["discussions"] = [build_cohort_i_discussion(rel_i, doc_i, graphs_i[0]["graph_id"])]
    assert validate_trait(doc_i) == []

    rel_j = COHORT_J_PATHS[0]
    doc_j = copy.deepcopy(yaml.safe_load((REPO_ROOT / rel_j).read_text(encoding="utf-8")))
    graphs_j = build_cohort_j_graphs(rel_j, doc_j)
    doc_j["causal_graphs"] = graphs_j
    doc_j["discussions"] = [build_cohort_j_discussion(rel_j, doc_j, graphs_j[0]["graph_id"])]
    assert validate_trait(doc_j) == []
