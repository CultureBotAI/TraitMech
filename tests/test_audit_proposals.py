"""Unit tests for scripts/audit_proposals.py.

Locks in the >=2-distinct-citation rule for PROPOSED TraitRecords:
- only PROPOSED records are checked (SEEDED/REVIEWED/DEPRECATED return None);
- citations are counted across definition_source + evidence[].reference;
- duplicates and TODO placeholders don't count;
- malformed references (not PMID/DOI/URL) fail the record.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_proposals import (  # noqa: E402
    MIN_CITATIONS,
    audit_record,
    distinct_citations,
    is_placeholder,
    is_valid_reference,
)


def _proposed(definition_source=None, refs=()):
    rec = {"identifier": "traitmech:000999", "mapping_status": "PROPOSED"}
    if definition_source is not None:
        rec["definition_source"] = definition_source
    rec["evidence"] = [{"reference": r} for r in refs]
    return rec


# ---------------------------------------------------------------- helpers


def test_is_placeholder():
    assert is_placeholder("TODO:add_citation")
    assert is_placeholder("")
    assert is_placeholder("   ")
    assert not is_placeholder("PMID:12345678")


def test_is_valid_reference():
    assert is_valid_reference("PMID:12829275")
    assert is_valid_reference("DOI:10.1099/ijsem.0.001671")
    assert is_valid_reference("https://example.org/paper")
    assert not is_valid_reference("just some text")
    assert not is_valid_reference("PMID:")


def test_distinct_citations_dedupes_and_drops_placeholders():
    rec = _proposed(
        definition_source="DOI:10.1/x",
        refs=["DOI:10.1/x", "PMID:111", "TODO:add_citation", ""],
    )
    # DOI:10.1/x appears twice (def_source + evidence) -> counted once;
    # placeholder + empty dropped.
    assert distinct_citations(rec) == ["DOI:10.1/x", "PMID:111"]


# ---------------------------------------------------------------- audit_record


def test_audit_skips_non_proposed():
    for status in ("SEEDED", "REVIEWED", "DEPRECATED"):
        rec = _proposed(definition_source="DOI:10.1/x", refs=["PMID:1"])
        rec["mapping_status"] = status
        assert audit_record(rec) is None


def test_audit_passes_with_two_distinct_citations():
    rec = _proposed(definition_source="DOI:10.1/x", refs=["PMID:222"])
    row = audit_record(rec)
    assert row is not None
    assert row["n_citations"] == 2
    assert row["passes"] == "yes"


def test_audit_fails_with_single_citation():
    rec = _proposed(definition_source="DOI:10.1/x", refs=["DOI:10.1/x"])
    row = audit_record(rec)
    assert row["n_citations"] == 1
    assert row["passes"] == "no"


def test_audit_fails_when_only_placeholders():
    rec = _proposed(definition_source="TODO:add_citation", refs=["TODO:later"])
    row = audit_record(rec)
    assert row["n_citations"] == 0
    assert row["passes"] == "no"


def test_audit_fails_on_malformed_reference():
    rec = _proposed(definition_source="DOI:10.1/x", refs=["not a real ref"])
    row = audit_record(rec)
    assert row["malformed"] == "not a real ref"
    assert row["passes"] == "no"


def test_min_citations_is_two():
    assert MIN_CITATIONS == 2
