"""Regression tests for the final canonical-example queue migration (#444)."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import backfill_canonical_examples_444 as migration  # noqa: E402


def _trait(slug: str) -> dict:
    return yaml.safe_load((ROOT / "data" / "traits" / f"{slug}.yaml").read_text())


def test_ledger_covers_the_exact_89_record_baseline() -> None:
    migration.validate_ledger()
    assert len(migration.TRANCHE) == 85
    assert len(migration.DEFERRED) == 4
    assert len(set(migration.TRANCHE) | set(migration.DEFERRED)) == 89


def test_all_populated_records_match_the_source_ledger() -> None:
    for slug, rows in migration.TRANCHE.items():
        expected = [
            {**migration.SOURCES[source_key], "note": note}
            for source_key, note in rows
        ]
        doc = _trait(slug)
        assert doc["canonical_examples"] == expected, slug
        assert any(
            event["action"] == migration.ADD_ACTION and "issue #444" in event["changes"]
            for event in doc["curation_history"]
        ), slug


def test_the_four_reviewed_evidence_gaps_leave_the_live_queue() -> None:
    assert migration.expected_queue() == set()
    for slug in migration.DEFERRED:
        doc = _trait(slug)
        assert not doc.get("canonical_examples"), slug
        assert any(
            event["action"] == migration.DEFER_ACTION
            and "No paid research was used" in event["changes"]
            for event in doc["curation_history"]
        ), slug


def test_migration_is_idempotent_after_application() -> None:
    assert migration.apply(write=False) == 0
