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
    ENTRY_VERSION_REFRESHES,
    NEW_PROTEIN_EXAMPLES,
    RETRIEVED_ON,
    process_all,
)
from traitmech.validation.write_validated import validate_trait  # noqa: E402


def test_stage3_scope_excludes_do_not_work_and_matches_counts() -> None:
    assert len(NEW_PROTEIN_EXAMPLES) == 5
    total_new_examples = sum(
        len(exs)
        for spec in NEW_PROTEIN_EXAMPLES.values()
        for exs in spec["nodes"].values()
    )
    assert total_new_examples == 11
    assert len(ENTRY_VERSION_REFRESHES) == 110
    all_files = {r[0] for r in ENTRY_VERSION_REFRESHES} | set(NEW_PROTEIN_EXAMPLES)
    assert len(all_files) == 104
    assert "data/traits/physiology/spore_germination.yaml" not in all_files


def test_new_protein_examples_committed_and_schema_valid() -> None:
    for rel_path, spec in NEW_PROTEIN_EXAMPLES.items():
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["identifier"] == spec["identifier"]
        assert validate_trait(doc) == []
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
    for rel_path in ({r[0] for r in ENTRY_VERSION_REFRESHES} | set(NEW_PROTEIN_EXAMPLES)):
        src = REPO_ROOT / rel_path
        dst = tmp_path / rel_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    first_rel = sorted(NEW_PROTEIN_EXAMPLES)[0]
    (tmp_path / "DO_NOT_WORK.md").write_text(f"- `{first_rel}`\n", encoding="utf-8")
    with pytest.raises(ValueError, match="DO_NOT_WORK protected trait"):
        process_all(apply=False, repo_root=tmp_path)
