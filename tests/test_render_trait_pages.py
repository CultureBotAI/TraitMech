"""Unit tests for the page stamp in scripts/render_trait_pages.py.

The stamp is what makes `pages/` verifiable by regenerate-and-diff (#228). Its
whole job is normalisation — mixed offsets, the 'Z' suffix, both YAML shapes —
so these assert that every shape a curation_history entry can legitimately take
is actually counted, and that nothing reintroduces wall-clock nondeterminism.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from render_trait_pages import corpus_timestamp  # noqa: E402


def _doc(*timestamps):
    return [(None, {"curation_history": [{"timestamp": t} for t in timestamps]})]


def test_picks_the_latest_timestamp():
    assert corpus_timestamp(_doc(
        "2026-05-05T01:35:46+00:00",
        "2026-08-03T22:40:00Z",
        "2026-06-24T17:21:13Z",
    )) == "2026-08-03 22:40 UTC"


def test_z_suffix_and_explicit_offset_compare_correctly():
    """'2026-01-01T00:00:00Z' is EARLIER than '2026-01-01T01:00:00+00:00'.

    Comparing the raw strings would get this right by luck; comparing a naive
    parse of a '-07:00' value would not, which is why everything is normalised
    to UTC first.
    """
    assert corpus_timestamp(_doc(
        "2026-01-01T00:00:00Z",
        "2026-01-01T01:00:00+00:00",
    )) == "2026-01-01 01:00 UTC"


def test_offsets_are_normalised_not_string_compared():
    """18:00-07:00 is 01:00Z the NEXT day, so it must win over 12:00Z."""
    assert corpus_timestamp(_doc(
        "2026-03-01T12:00:00Z",
        "2026-03-01T18:00:00-07:00",
    )) == "2026-03-02 01:00 UTC"


def test_datetime_typed_timestamps_are_counted():
    """PyYAML resolves an UNQUOTED ISO timestamp to a datetime, not a str.

    Accepting only str silently dropped those, so a single unquoted entry would
    make the stamp go stale or backwards with no signal — the silent-zero
    failure this whole gate family exists to prevent.
    """
    aware = datetime(2026, 9, 1, 12, 0, tzinfo=timezone.utc)
    assert corpus_timestamp(_doc(aware)) == "2026-09-01 12:00 UTC"
    assert corpus_timestamp(_doc("2026-01-01T00:00:00Z", aware)) == "2026-09-01 12:00 UTC"


def test_naive_datetimes_are_assumed_utc_not_discarded():
    assert corpus_timestamp(_doc(datetime(2026, 9, 1, 12, 0))) == "2026-09-01 12:00 UTC"


def test_unparsable_and_missing_entries_are_skipped_not_fatal():
    assert corpus_timestamp(_doc("not a date", None, 42, "2026-04-01T00:00:00Z")) \
        == "2026-04-01 00:00 UTC"


def test_no_usable_timestamp_returns_empty_never_the_clock():
    """Falling back to now() would restore the nondeterminism #228 removed."""
    assert corpus_timestamp(_doc("not a date")) == ""
    assert corpus_timestamp([(None, {})]) == ""
    assert corpus_timestamp([]) == ""


def test_is_a_pure_function_of_the_data():
    """Same input twice — the property that makes regenerate-and-diff work."""
    docs = _doc("2026-05-05T01:35:46+00:00")
    assert corpus_timestamp(docs) == corpus_timestamp(docs)


def test_real_corpus_yields_a_stamp():
    """Guards the live tree: if every timestamp stopped parsing, the footer
    would silently fall back to 'Built from' and nobody would notice."""
    import yaml
    traits = []
    for p in sorted((REPO_ROOT / "data" / "traits").rglob("*.yaml")):
        doc = yaml.safe_load(p.read_text())
        if isinstance(doc, dict):
            traits.append((p, doc))
    assert corpus_timestamp(traits), "no parsable curation_history timestamp in the corpus"
