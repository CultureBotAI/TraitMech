"""Unit tests for traitmech.curate.curation_event.

Focused on ``upsert`` (#395), which exists so a migration with a fixed timestamp
is idempotent for its OWN audit trail. Without it a migration appends only to
files it CHANGES, so once the data is correct a re-run writes nothing and a
corrected rationale never reaches the corpus. That divergence shipped twice
before anyone noticed, and recovering meant restoring 22 trait files and
re-running the migration.
"""

from __future__ import annotations

from traitmech.curate.curation_event import record_curation_event

# ---------------------------------------------------------------- upsert (#395)


def test_upsert_replaces_the_matching_entry_instead_of_appending():
    """A migration with a fixed timestamp must be idempotent for its own audit
    trail. Without this, it appends only to files it CHANGES, so once the data
    is correct a re-run writes nothing and a corrected rationale never reaches
    the corpus — a divergence that shipped twice before it was noticed."""
    doc = {"curation_history": []}
    record_curation_event(doc, curator="claude", action="MIGRATE",
                          timestamp="2026-01-01T00:00:00Z", changes="first")
    record_curation_event(doc, curator="claude", action="MIGRATE",
                          timestamp="2026-01-01T00:00:00Z", changes="corrected",
                          upsert=True)
    history = doc["curation_history"]
    assert len(history) == 1
    assert history[0]["changes"] == "corrected"


def test_upsert_keeps_the_entry_in_place():
    """Replaced in position, so a correction does not shuffle an append-only
    trail by jumping to the end."""
    doc = {"curation_history": []}
    record_curation_event(doc, curator="claude", action="A", timestamp="t1")
    record_curation_event(doc, curator="claude", action="MIGRATE", timestamp="t2",
                          changes="first")
    record_curation_event(doc, curator="claude", action="B", timestamp="t3")
    record_curation_event(doc, curator="claude", action="MIGRATE", timestamp="t2",
                          changes="corrected", upsert=True)
    actions = [e["action"] for e in doc["curation_history"]]
    assert actions == ["A", "MIGRATE", "B"]
    assert doc["curation_history"][1]["changes"] == "corrected"


def test_upsert_matches_on_all_three_of_curator_action_timestamp():
    """A different timestamp is a different event — two runs of the same
    migration on different days are two facts, not one."""
    doc = {"curation_history": []}
    record_curation_event(doc, curator="claude", action="MIGRATE", timestamp="t1",
                          changes="run one", upsert=True)
    record_curation_event(doc, curator="claude", action="MIGRATE", timestamp="t2",
                          changes="run two", upsert=True)
    record_curation_event(doc, curator="other", action="MIGRATE", timestamp="t1",
                          changes="someone else", upsert=True)
    assert len(doc["curation_history"]) == 3


def test_without_upsert_the_old_append_behaviour_is_unchanged():
    doc = {"curation_history": []}
    for _ in range(2):
        record_curation_event(doc, curator="claude", action="MIGRATE",
                              timestamp="t1", changes="x")
    assert len(doc["curation_history"]) == 2
