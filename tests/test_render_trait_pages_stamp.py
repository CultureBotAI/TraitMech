"""Regression tests for the per-record page stamp (#304).

A trait page must carry ITS OWN latest curation timestamp, not the corpus-wide
maximum. Storing 477 copies of a global value meant every data PR rewrote every
page: PR #300 changed 14 trait files and produced a 508-file diff, of which 477
were nothing but a footer timestamp. That buries the real change in review and
makes pages/ conflict spuriously between concurrent PRs.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from render_trait_pages import corpus_timestamp, record_timestamp  # noqa: E402

_A = {"curation_history": [{"timestamp": "2026-01-01T00:00:00Z"}]}
_B = {"curation_history": [
    {"timestamp": "2026-05-05T09:00:00Z"},
    {"timestamp": "2026-06-06T10:00:00Z"},
]}


def test_record_timestamp_is_that_records_latest():
    assert record_timestamp(_B) == "2026-06-06 10:00 UTC"


def test_record_timestamp_is_not_the_corpus_maximum():
    """The whole point: editing record B must not restamp record A."""
    traits = [(Path("a.yaml"), _A), (Path("b.yaml"), _B)]
    assert corpus_timestamp(traits) == "2026-06-06 10:00 UTC"
    assert record_timestamp(_A) == "2026-01-01 00:00 UTC"
    assert record_timestamp(_A) != corpus_timestamp(traits)


def test_record_timestamp_is_empty_without_history():
    """Falls back to '' rather than the clock, as corpus_timestamp does --
    the template then renders 'Built from' instead of inventing currency."""
    assert record_timestamp({}) == ""
    assert record_timestamp({"curation_history": []}) == ""
