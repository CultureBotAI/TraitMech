"""Tests for Stage 5 grouped review remediation (G-STAGE4-RECORD-LEVEL-DEFINITION-SOURCE)."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

from curate_stage5_review_findings import (  # noqa: E402
    ACTION,
    CURATOR,
    REMEDIATION_SPECS,
    TIMESTAMP,
    process_all,
)
from traitmech.validation.write_validated import validate_trait  # noqa: E402


def test_stage5_scope_excludes_do_not_work_and_matches_counts() -> None:
    assert len(REMEDIATION_SPECS) == 4
    assert "data/traits/physiology/spore_germination.yaml" not in REMEDIATION_SPECS
    finding_ids = {spec["finding_id"] for spec in REMEDIATION_SPECS.values()}
    assert finding_ids == {
        "F-DEF-SRC-CYANOPHYCIN-001",
        "F-DEF-SRC-CADMIUM-002",
        "F-DEF-SRC-COBALT-003",
        "F-DEF-SRC-ZINC-004",
    }


def test_stage5_remediations_committed_and_schema_valid() -> None:
    for rel_path, spec in REMEDIATION_SPECS.items():
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert doc["identifier"] == spec["identifier"]
        assert doc["definition_source"] == spec["definition_source"]
        assert validate_trait(doc) == []
        refs = {ev.get("reference"): ev for ev in doc.get("evidence", [])}
        assert spec["definition_source"] in refs
        assert refs[spec["definition_source"]] == spec["evidence_entry"]
        last_event = doc["curation_history"][-1]
        assert last_event["curator"] == CURATOR
        assert last_event["action"] == ACTION
        assert last_event["timestamp"] == TIMESTAMP
        assert last_event["changes"] == spec["changes"]


def test_process_all_is_idempotent_on_committed_corpus() -> None:
    assert process_all(apply=False) == (4, 0)


def test_protected_record_guard_raises(tmp_path: Path) -> None:
    for rel_path in REMEDIATION_SPECS:
        src = REPO_ROOT / rel_path
        dst = tmp_path / rel_path
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    first_rel = sorted(REMEDIATION_SPECS)[0]
    (tmp_path / "DO_NOT_WORK.md").write_text(f"- `{first_rel}`\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Refusing to touch DO_NOT_WORK.md excluded file"):
        process_all(apply=False, repo_root=tmp_path)
