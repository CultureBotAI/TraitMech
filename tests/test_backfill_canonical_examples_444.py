"""Regression tests for the final canonical-example queue migration (#444)."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import backfill_canonical_examples_444 as migration  # noqa: E402
import repair_legacy_canonical_citations_1626 as citation_repair  # noqa: E402


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
        # Preserve the frozen migration ledger while requiring its exact reviewed successor.
        if slug == "environment/halophily_preference":
            spec = citation_repair.SPECS[slug]
            assert expected.count(spec["before"]) == 1
            review = citation_repair.REVIEW_SPECS[spec["identity"]["identifier"]]
            expected[expected.index(spec["before"])] = review["after_examples"][1]
            assert citation_repair.event(spec["changes"]) in doc["curation_history"]
            assert citation_repair.event(
                review["changes"], action=citation_repair.REVIEW_ACTION,
                timestamp=citation_repair.REVIEW_TIMESTAMP,
            ) in doc["curation_history"]
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


@pytest.mark.parametrize("drift", [None, "target", "other_example", "identity", "history"])
def test_reviewed_citation_successor_replay_is_exact(tmp_path, monkeypatch, drift):
    slug = "environment/halophily_preference"
    doc = _trait(slug)
    if drift == "target":
        doc["canonical_examples"][1]["note"] = "Unreviewed claim"
    elif drift == "other_example":
        doc["canonical_examples"][0]["reference"] = "PMID:1"
    elif drift == "identity":
        doc["definition"] = "Different scope"
    elif drift == "history":
        doc["curation_history"] = [
            row for row in doc["curation_history"] if row["action"] != citation_repair.REVIEW_ACTION
        ]
    path = tmp_path / "data/traits" / f"{slug}.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    before = path.read_bytes()
    monkeypatch.setattr(migration, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(migration, "TRANCHE", {slug: migration.TRANCHE[slug]})
    monkeypatch.setattr(migration, "DEFERRED", {})
    monkeypatch.setattr(migration, "validate_ledger", lambda: None)
    monkeypatch.setattr(migration, "expected_queue", set)

    def unexpected_write(*_args):
        pytest.fail("reviewed successor must never be rewritten by the old migration")

    monkeypatch.setattr(migration, "_write", unexpected_write)
    if drift:
        with pytest.raises(ValueError):
            migration.apply(write=True)
    else:
        assert migration.apply(write=True) == 0
    assert path.read_bytes() == before
