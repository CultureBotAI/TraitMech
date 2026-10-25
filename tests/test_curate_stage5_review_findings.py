"""Tests for Stage 5 grouped review remediation (Cycle 1 #1981, Cycle 2 #1995, Cycle 3–4 #2002)."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

import audit_evidence_snippets as aes  # noqa: E402
from curate_stage5_review_findings import (  # noqa: E402
    ACTION,
    CURATOR,
    CYCLE2_TIMESTAMP,
    CYCLE3_TIMESTAMP,
    CYCLE4_TIMESTAMP,
    REMEDIATION_SPECS,
    TIMESTAMP,
    process_all,
)
from traitmech.validation.write_validated import validate_trait  # noqa: E402


def test_stage5_scope_excludes_do_not_work_and_matches_counts() -> None:
    assert len(REMEDIATION_SPECS) == 45
    assert "data/traits/physiology/spore_germination.yaml" not in REMEDIATION_SPECS
    finding_ids = {spec["finding_id"] for spec in REMEDIATION_SPECS.values()}
    assert finding_ids == {
        "F-DEF-SRC-CYANOPHYCIN-001",
        "F-DEF-SRC-CADMIUM-002",
        "F-DEF-SRC-COBALT-003",
        "F-DEF-SRC-ZINC-004",
        "F-DEF-SRC-CARBON-FIXATION-010",
        "F-DEF-SRC-WOOD-LJUNGDAHL-011",
        "F-DEF-SRC-PROPIONIC-FERM-012",
        "F-DEF-SRC-MANGANESE-OX-013",
        "F-DEF-SRC-CELLULOLYSIS-014",
        "F-DEF-SRC-CHITINOLYSIS-015",
        "F-C3S4-DEF-SRC-001",
        "F-C3S4-DEF-SRC-002",
        "F-C3S4-DEF-SRC-003",
        "F-C3S4-DEF-SRC-004",
        "F-C3S4-DEF-SRC-005",
        "F-C3S4-DEF-SRC-006",
        "F-C3S4-DEF-SRC-007",
        "F-C3S4-DEF-SRC-008",
        "F-C3S4-DEF-SRC-009",
        "F-C3S4-DEF-SRC-010",
        "F-C3S4-DEF-SRC-011",
        "F-C3S4-DEF-SRC-012",
        "F-C3S4-DEF-SRC-013",
        "F-C3S4-DEF-SRC-014",
        "F-C3S4-DEF-SRC-015",
        "F-C3S4-DEF-SRC-016",
        "F-C3S4-DEF-SRC-017",
        "F-C4S4-DEF-SRC-001",
        "F-C4S4-DEF-SRC-002",
        "F-C4S4-DEF-SRC-003",
        "F-C4S4-DEF-SRC-004",
        "F-C4S4-DEF-SRC-005",
        "F-C4S4-DEF-SRC-006",
        "F-C4S4-DEF-SRC-007",
        "F-C4S4-DEF-SRC-008",
        "F-C4S4-DEF-SRC-009",
        "F-C4S4-DEF-SRC-010",
        "F-C4S4-DEF-SRC-011",
        "F-C4S4-DEF-SRC-012",
        "F-C4S4-DEF-SRC-013",
        "F-C4S4-DEF-SRC-014",
        "F-C4S4-DEF-SRC-015",
        "F-C4S4-DEF-SRC-016",
        "F-C4S4-DEF-SRC-017",
        "F-C4S4-DEF-SRC-018",
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
        assert last_event["timestamp"] == spec.get("timestamp", TIMESTAMP)
        assert last_event["timestamp"] in {
            TIMESTAMP,
            CYCLE2_TIMESTAMP,
            CYCLE3_TIMESTAMP,
            CYCLE4_TIMESTAMP,
        }
        assert last_event["changes"] == spec["changes"]


def test_process_all_is_idempotent_on_committed_corpus() -> None:
    assert process_all(apply=False) == (45, 0)


def test_zero_unquoted_definition_sources_on_remediated_records() -> None:
    rows = aes.audit(check_reports=False, check_definition_sources=True)
    unquoted_files = {row["file"] for row in rows if row["defect"] == "UNQUOTED_DEFINITION_SOURCE"}
    assert unquoted_files.isdisjoint(REMEDIATION_SPECS)


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
