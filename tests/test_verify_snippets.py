"""Offline tests for the snippet source verifier (#623).

Every test here stubs the network. The script's value rests entirely on what its
verdicts are allowed to mean, so that is what is pinned: a substring match is
decisive, a near-miss is a prompt, and a non-match proves nothing.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import verify_snippets as vs  # noqa: E402

FRIEDMAN = (
    "The succession from aerobic and facultative anaerobic bacteria to obligate anaerobes "
    "in the infant gut suggests that the gut microbes consume oxygen. Remarkably, "
    "measurements of luminal oxygen levels show nearly identical pO<sub>2</sub> (partial "
    "pressure of oxygen) profiles in conventional and germ-free mice, pointing to the "
    "existence of oxygen consumption mechanisms other than microbial respiration."
)


def test_exact_substring_is_verified():
    snippet = ("measurements of luminal oxygen levels show nearly identical pO2 (partial "
               "pressure of oxygen) profiles in conventional and germ-free mice")
    verdict, ratio, _ = vs.classify(snippet, FRIEDMAN, vs.DEFAULT_THRESHOLD)
    assert verdict == "VERIFIED"
    assert ratio == 1.0


def test_markup_and_yaml_folding_do_not_cause_a_false_miss():
    """`<sub>` in the abstract and newlines from YAML folding are not real differences."""
    snippet = "nearly identical pO2 (partial pressure\n    of oxygen) profiles"
    assert vs.classify(snippet, FRIEDMAN, vs.DEFAULT_THRESHOLD)[0] == "VERIFIED"


def test_interior_elision_is_flagged_as_a_near_miss():
    """The #620 defect: words removed from mid-quote, with no ellipsis marker.

    audit_evidence_snippets.py cannot see this -- it only flags a literal '...'.
    """
    snippet = ("Remarkably, measurements of luminal oxygen levels show nearly identical "
               "profiles in conventional and germ-free mice, pointing to the existence of "
               "oxygen consumption mechanisms other than microbial respiration")
    verdict, ratio, nearest = vs.classify(snippet, FRIEDMAN, vs.DEFAULT_THRESHOLD)
    assert verdict == "LIKELY_PARAPHRASE"
    assert ratio >= vs.DEFAULT_THRESHOLD
    assert "pO2" in nearest


def test_a_heavy_rewrite_is_NOT_caught_and_that_is_documented():
    """The #619 defect, pinned as a KNOWN LIMIT rather than a passing check.

    The fabricated sentence scores far below threshold, so it is indistinguishable
    from a legitimate full-text quote. Lowering the threshold to catch it would
    flag every full-text quote on the same subject. This test exists so the limit
    cannot be quietly forgotten or the docstring quietly oversold.
    """
    fabricated = ("Remarkably, luminal oxygen levels were found to be nearly "
                  "indistinguishable between conventionally housed and germ-free mice, "
                  "being close to zero in the cecum in both cases")
    verdict, ratio, _ = vs.classify(fabricated, FRIEDMAN, vs.DEFAULT_THRESHOLD)
    assert verdict == "NOT_IN_ABSTRACT"
    assert ratio < vs.DEFAULT_THRESHOLD


def test_absent_abstract_is_unresolved_not_a_defect():
    assert vs.classify("anything", None, vs.DEFAULT_THRESHOLD)[0] == "UNRESOLVED"


def test_doi_query_is_unquoted():
    """Europe PMC returns a non-JSON error page for a quoted DOI value.

    Regression guard: the first version quoted it and every DOI came back
    UNRESOLVED, which looked like 'not indexed' rather than 'the query is wrong'.
    """
    captured = {}

    def fake_urlopen(url, timeout=None):  # noqa: ARG001
        captured["url"] = url
        # URLError so the script's own retry path runs and ends in LookupFailed;
        # a bare AssertionError would escape the handler and test nothing.
        raise vs.urllib.error.URLError("stop before the network")

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(vs.urllib.request, "urlopen", fake_urlopen)
        with pytest.raises(vs.LookupFailed):
            vs.europepmc_abstract("DOI:10.1073/pnas.1718635115", retries=1)
    assert "DOI%3A10.1073%2Fpnas.1718635115" in captured["url"]
    assert "%22" not in captured["url"], "the DOI value must not be quoted"


def test_transport_failure_raises_rather_than_reporting_no_record():
    """A 503 must not be reportable as UNRESOLVED.

    Otherwise a fully rate-limited run prints an all-UNRESOLVED report and exits
    0, which is indistinguishable from a clean run over unindexed references --
    a check that cannot fail.
    """
    def always_fail(url, timeout=None):  # noqa: ARG001
        raise vs.urllib.error.URLError("503")

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(vs.urllib.request, "urlopen", always_fail)
        mp.setattr(vs.time, "sleep", lambda _s: None)
        with pytest.raises(vs.LookupFailed):
            vs.europepmc_abstract("PMID:29610310", retries=2)


def test_an_unindexed_reference_is_not_a_transport_failure():
    """An empty result set is a real answer: the reference is simply not there."""
    class FakeResponse:
        def read(self):
            return b'{"resultList": {"result": []}}'

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(vs.json, "load", lambda _fh: {"resultList": {"result": []}})
        mp.setattr(vs.urllib.request, "urlopen", lambda url, timeout=None: FakeResponse())
        assert vs.europepmc_abstract("PMID:1") is None


def test_non_literature_references_are_skipped():
    """CHEBI/GO/METPO references have no abstract and are not literature claims."""
    assert vs.europepmc_abstract("CHEBI:17968") is None
    assert vs.europepmc_abstract("GO:0006635") is None
