"""Tests for Stage 3 UniProt protein_examples curation and entry_version refresh."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from curate_stage3_protein_examples import (  # noqa: E402
    C2S3_COHORT_C_BLOCKERS,
    C2S3_COHORT_C_PROMOTIONS,
    C2S3_RETRIEVED_ON,
    C3S3_COHORT_E_BLOCKERS,
    C3S3_COHORT_E_PROMOTIONS,
    C3S3_RETRIEVED_ON,
    C4S3_COHORT_G_PROMOTIONS,
    C4S3_RETRIEVED_ON,
    C5S3_COHORT_H_PROMOTIONS,
    C5S3_RETRIEVED_ON,
    C6S3_COHORT_I_PROMOTIONS,
    C6S3_RETRIEVED_ON,
    ENTRY_VERSION_REFRESHES,
    NEW_PROTEIN_EXAMPLES,
    RETRIEVED_ON,
    process_all,
)
from traitmech.validation.write_validated import validate_trait  # noqa: E402


def test_stage3_scope_excludes_do_not_work_and_matches_counts() -> None:
    assert len(NEW_PROTEIN_EXAMPLES) == 5
    total_new_examples = sum(
        len(exs) for spec in NEW_PROTEIN_EXAMPLES.values() for exs in spec["nodes"].values()
    )
    assert total_new_examples == 11
    assert len(ENTRY_VERSION_REFRESHES) == 112
    assert len(C2S3_COHORT_C_PROMOTIONS) == 8
    total_c2s3_examples = sum(
        len(spec["new_node"]["protein_examples"]) for spec in C2S3_COHORT_C_PROMOTIONS.values()
    )
    assert total_c2s3_examples == 16
    assert len(C2S3_COHORT_C_BLOCKERS) == 2
    assert len(C3S3_COHORT_E_PROMOTIONS) == 2
    total_c3s3_examples = sum(
        len(spec["new_node"]["protein_examples"]) for spec in C3S3_COHORT_E_PROMOTIONS.values()
    )
    assert total_c3s3_examples == 2
    assert len(C3S3_COHORT_E_BLOCKERS) == 1
    assert len(C4S3_COHORT_G_PROMOTIONS) == 3
    total_c4s3_examples = sum(
        len(spec["new_node"]["protein_examples"]) for spec in C4S3_COHORT_G_PROMOTIONS.values()
    )
    assert total_c4s3_examples == 4
    assert len(C5S3_COHORT_H_PROMOTIONS) == 3
    total_c5s3_examples = sum(
        len(spec["new_node"]["protein_examples"]) for spec in C5S3_COHORT_H_PROMOTIONS.values()
    )
    assert total_c5s3_examples == 3
    assert len(C6S3_COHORT_I_PROMOTIONS) == 3
    total_c6s3_examples = sum(
        len(spec["new_node"]["protein_examples"]) for spec in C6S3_COHORT_I_PROMOTIONS.values()
    )
    assert total_c6s3_examples == 3
    all_files = (
        {r[0] for r in ENTRY_VERSION_REFRESHES}
        | set(NEW_PROTEIN_EXAMPLES)
        | set(C2S3_COHORT_C_PROMOTIONS)
        | set(C2S3_COHORT_C_BLOCKERS)
        | set(C3S3_COHORT_E_PROMOTIONS)
        | set(C3S3_COHORT_E_BLOCKERS)
        | set(C4S3_COHORT_G_PROMOTIONS)
        | set(C5S3_COHORT_H_PROMOTIONS)
        | set(C6S3_COHORT_I_PROMOTIONS)
    )
    assert len(all_files) == 128
    assert "data/traits/physiology/spore_germination.yaml" not in all_files


def test_new_protein_examples_committed_and_schema_valid() -> None:
    for rel_path, spec in NEW_PROTEIN_EXAMPLES.items():
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["identifier"] == spec["identifier"]
        assert validate_trait(doc) == []
        assert any(h.get("changes") == spec["changes_summary"] for h in doc["curation_history"])
        graphs = [g for g in doc.get("causal_graphs", []) if g.get("graph_id") == spec["graph_id"]]
        assert len(graphs) == 1
        graph = graphs[0]
        assert graph["scope_notes"] == spec["scope_notes"]
        nodes_by_id = {n["node_id"]: n for n in graph["nodes"]}
        for node_id, expected_examples in spec["nodes"].items():
            assert node_id in nodes_by_id
            node = nodes_by_id[node_id]
            assert node["node_type"] == "GENE_OR_PROTEIN"
            assert not str(node.get("grounding") or "").startswith("UniProtKB:")
            assert node.get("protein_examples") == expected_examples
            for pe in node["protein_examples"]:
                assert pe["uniprot_id"].startswith("UniProtKB:")
                assert pe["taxon_id"].startswith("NCBITaxon:")
                assert pe["retrieved_on"] == RETRIEVED_ON
                assert pe["entry_version"] >= 1
                assert pe["sequence_version"] >= 1
                assert pe.get("evidence"), f"{rel_path}/{node_id}: missing evidence"


def test_c2s3_and_c3s3_promotions_and_blockers_committed() -> None:
    promotions = [
        (C2S3_COHORT_C_PROMOTIONS, C2S3_RETRIEVED_ON),
        (C3S3_COHORT_E_PROMOTIONS, C3S3_RETRIEVED_ON),
        (C4S3_COHORT_G_PROMOTIONS, C4S3_RETRIEVED_ON),
        (C5S3_COHORT_H_PROMOTIONS, C5S3_RETRIEVED_ON),
        (C6S3_COHORT_I_PROMOTIONS, C6S3_RETRIEVED_ON),
    ]
    for promo_dict, expected_date in promotions:
        for rel_path, spec in promo_dict.items():
            path = REPO_ROOT / rel_path
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
            assert doc["identifier"] == spec["identifier"]
            assert validate_trait(doc) == []
            assert any(h.get("changes") == spec["changes_summary"] for h in doc["curation_history"])
            graphs = [
                g for g in doc.get("causal_graphs", []) if g.get("graph_id") == spec["graph_id"]
            ]
            assert len(graphs) == 1
            graph = graphs[0]
            assert graph["scope_status"] == "MECHANISTIC"
            assert graph["scope_notes"] == spec["scope_notes"]
            expected_node = spec["new_node"]
            nodes_by_id = {n["node_id"]: n for n in graph["nodes"]}
            assert expected_node["node_id"] in nodes_by_id
            node = nodes_by_id[expected_node["node_id"]]
            assert node == expected_node
            for pe in node["protein_examples"]:
                assert pe["uniprot_id"].startswith("UniProtKB:")
                assert pe["taxon_id"].startswith("NCBITaxon:")
                assert pe["retrieved_on"] == expected_date
                assert pe["entry_version"] >= 1
                assert pe["sequence_version"] >= 1
                assert pe.get("evidence")
            discussions = [
                d
                for d in doc.get("discussions", [])
                if d.get("discussion_id") == spec["discussion_id"]
            ]
            assert len(discussions) == 1
            assert discussions[0]["status"] == "RESOLVED"
            assert discussions[0]["resolved_date"] == expected_date
            assert discussions[0]["resolution_note"] == spec["resolution_message"]["body"]

    blockers = {**C2S3_COHORT_C_BLOCKERS, **C3S3_COHORT_E_BLOCKERS}
    for rel_path, spec in blockers.items():
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["identifier"] == spec["identifier"]
        assert validate_trait(doc) == []
        assert any(h.get("changes") == spec["changes_summary"] for h in doc["curation_history"])
        discussions = [
            d for d in doc.get("discussions", []) if d.get("discussion_id") == spec["discussion_id"]
        ]
        assert len(discussions) == 1
        assert discussions[0]["status"] == "OPEN"
        assert discussions[0]["notes"] == spec["blocker_message"]["body"]


def test_entry_version_refreshes_committed() -> None:
    for rel_path, graph_id, node_id, curie, _old_v, new_v in ENTRY_VERSION_REFRESHES:
        doc = yaml.safe_load((REPO_ROOT / rel_path).read_text(encoding="utf-8"))
        found = False
        for g in doc.get("causal_graphs", []):
            if g.get("graph_id") == graph_id:
                for n in g.get("nodes", []):
                    if n.get("node_id") == node_id:
                        for pe in n.get("protein_examples", []):
                            if pe.get("uniprot_id") == curie:
                                assert pe["entry_version"] == new_v
                                assert pe["retrieved_on"] == RETRIEVED_ON
                                found = True
        assert found, f"Missing {curie} in {rel_path} ({graph_id}/{node_id})"


def test_process_all_is_idempotent_on_committed_corpus() -> None:
    assert process_all(apply=False) == (0, 0, 0)


def test_protected_record_guard_raises(tmp_path: Path) -> None:
    all_rels = (
        {r[0] for r in ENTRY_VERSION_REFRESHES}
        | set(NEW_PROTEIN_EXAMPLES)
        | set(C2S3_COHORT_C_PROMOTIONS)
        | set(C2S3_COHORT_C_BLOCKERS)
        | set(C3S3_COHORT_E_PROMOTIONS)
        | set(C3S3_COHORT_E_BLOCKERS)
        | set(C4S3_COHORT_G_PROMOTIONS)
        | set(C5S3_COHORT_H_PROMOTIONS)
        | set(C6S3_COHORT_I_PROMOTIONS)
    )
    for rel_path in all_rels:
        src = REPO_ROOT / rel_path
        dst = tmp_path / rel_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    first_rel = sorted(NEW_PROTEIN_EXAMPLES)[0]
    (tmp_path / "DO_NOT_WORK.md").write_text(f"- `{first_rel}`\n", encoding="utf-8")
    with pytest.raises(ValueError, match="DO_NOT_WORK protected trait"):
        process_all(apply=False, repo_root=tmp_path)
