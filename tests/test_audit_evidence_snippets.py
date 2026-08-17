"""Unit tests for scripts/audit_evidence_snippets.py.

The hard part of this audit is not detecting a bad snippet — it is deciding
which direction text travelled. A curated snippet appearing in a research report
proves nothing on its own, because the pipeline feeds the trait's EXISTING
evidence into the prompt. Both confounds cost real false positives while this
was being built (257 findings, then 41, then 7), so both are pinned here.
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import audit_evidence_snippets as aes  # noqa: E402
from audit_evidence_snippets import _prompt_evidence, audit, iter_evidence  # noqa: E402


def _write_trait(tmp_path, monkeypatch, body: str):
    traits = tmp_path / "data" / "traits" / "ecology"
    traits.mkdir(parents=True)
    (traits / "x.yaml").write_text(textwrap.dedent(body))
    monkeypatch.setattr(aes, "TRAITS_DIR", tmp_path / "data" / "traits")
    monkeypatch.setattr(aes, "RESEARCH_DIR", tmp_path / "research" / "traits")
    return traits


def _defects(findings):
    return sorted(f["defect"] for f in findings)


def test_ellipsis_is_flagged_as_non_contiguous(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        evidence:
          - reference: DOI:10.1/x
            snippet: obligate aerobe ... stops growing
        """)
    assert _defects(audit(check_reports=False)) == ["ELLIPTICAL_SNIPPET"]


def test_unicode_ellipsis_counts_too(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        evidence:
          - reference: DOI:10.1/x
            snippet: GH48, GH6 with CBM2 domains … release glucose
        """)
    assert _defects(audit(check_reports=False)) == ["ELLIPTICAL_SNIPPET"]


def test_a_single_word_snippet_supports_nothing(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        evidence:
          - reference: DOI:10.1/x
            snippet: toxins
        """)
    assert _defects(audit(check_reports=False)) == ["UNSUPPORTIVE_SNIPPET"]


def test_a_real_quote_is_clean(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        evidence:
          - reference: DOI:10.1/x
            snippet: aerobes require molecular oxygen as a terminal electron acceptor
        """)
    assert audit(check_reports=False) == []


def test_a_reference_with_no_quote_is_reported(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        evidence:
          - reference: DOI:10.1/x
        """)
    assert _defects(audit(check_reports=False)) == ["MISSING_SNIPPET"]


def test_reuse_across_edges_of_one_graph_is_flagged(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        causal_graphs:
          - graph_id: g1
            edges:
              - subject: a
                object: b
                evidence: [{reference: 'DOI:10.1/x', snippet: virulence factors present}]
              - subject: b
                object: c
                evidence: [{reference: 'DOI:10.1/x', snippet: virulence factors present}]
              - subject: c
                object: d
                evidence: [{reference: 'DOI:10.1/x', snippet: virulence factors present}]
        """)
    assert "REUSED_SNIPPET" in _defects(audit(check_reports=False))


def test_two_uses_are_not_yet_reuse(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        causal_graphs:
          - graph_id: g1
            edges:
              - subject: a
                object: b
                evidence: [{reference: 'DOI:10.1/x', snippet: a genuinely recurring key phrase}]
              - subject: b
                object: c
                evidence: [{reference: 'DOI:10.1/x', snippet: a genuinely recurring key phrase}]
        """)
    assert "REUSED_SNIPPET" not in _defects(audit(check_reports=False))


def test_record_and_edge_evidence_are_both_walked():
    doc = {
        "evidence": [{"reference": "DOI:10.1/x"}],
        "causal_graphs": [{"graph_id": "g1", "edges": [
            {"subject": "a", "object": "b", "evidence": [{"reference": "DOI:10.1/y"}]}]}],
    }
    locators = [loc for loc, _, _ in iter_evidence(doc)]
    assert locators == ["evidence[0]", "g1:a->b[0]"]


# --- direction: the part that produced real false positives -------------

def test_prompt_evidence_is_extracted_from_front_matter():
    raw = textwrap.dedent("""\
        ---
        provider: falcon
        template_variables:
          evidence_summary: 'DOI:10.1/x: ArsB extrudes arsenite (note)'
        ---

        # Answer
        """)
    assert "ArsB extrudes arsenite" in _prompt_evidence(raw)


@pytest.mark.parametrize("raw", [
    "no front matter at all\n",
    "---\n: : not yaml : :\n---\nbody\n",
    "---\njust_a_string\n---\nbody\n",
    "---\ntemplate_variables: not-a-mapping\n---\nbody\n",
])
def test_unreadable_front_matter_degrades_to_shown_nothing(raw):
    """Failing open only ever adds findings a human dismisses — never hides one."""
    assert _prompt_evidence(raw) == ""


MARKER = "Warnings for claims that should not yet be curated into TraitMech"


def _write_report(tmp_path, evidence_summary: str, answer: str):
    """A report shaped like a real one: front matter, prompt echoed twice, answer."""
    research = tmp_path / "research" / "traits" / "ecology"
    research.mkdir(parents=True, exist_ok=True)
    (research / "x-deep-research-falcon.md").write_text(
        "---\n"
        "provider: falcon\n"
        "template_variables:\n"
        f"  evidence_summary: {evidence_summary!r}\n"
        "---\n\n"
        f"## Question\n\n- {MARKER}.\n\n"
        f"## Output\n\n- {MARKER}.\n\n"
        f"{answer}\n"
    )


def test_a_snippet_the_provider_was_given_is_not_an_echo(tmp_path, monkeypatch):
    """arsenic_tolerant's real shape: the prompt carried the quote, so the
    answer repeating it says nothing about where the YAML got it."""
    quote = "ArsB is an integral membrane protein able to extrude arsenite from the cell"
    _write_trait(tmp_path, monkeypatch, f"""
        evidence:
          - reference: DOI:10.1/x
            snippet: {quote}
        """)
    _write_report(tmp_path, f"DOI:10.1/x: {quote} (note)", f"# Report\n\n{quote}\n")
    assert "ECHOES_RESEARCH_REPORT" not in _defects(audit(check_reports=True))


def test_a_snippet_only_in_the_answer_is_an_echo(tmp_path, monkeypatch):
    quote = "cellobiohydrolases release cellobiose processively from cellulose chain ends"
    _write_trait(tmp_path, monkeypatch, f"""
        evidence:
          - reference: DOI:10.1/x
            snippet: {quote}
        """)
    _write_report(tmp_path, "DOI:10.1/z: something unrelated (note)", f"# Report\n\n{quote}\n")
    assert "ECHOES_RESEARCH_REPORT" in _defects(audit(check_reports=True))


def test_a_short_snippet_does_not_match_by_coincidence(tmp_path, monkeypatch):
    _write_trait(tmp_path, monkeypatch, """
        evidence:
          - reference: DOI:10.1/x
            snippet: cellulose degradation
        """)
    _write_report(tmp_path, "none", "# Report\n\ncellulose degradation happens here\n")
    assert "ECHOES_RESEARCH_REPORT" not in _defects(audit(check_reports=True))


def test_the_committed_baseline_matches_the_corpus():
    """The ratchet is only a ratchet if the frozen set is current."""
    from audit_evidence_snippets import DEFAULT_BASELINE, compare, load_baseline
    baseline = load_baseline(DEFAULT_BASELINE)
    assert baseline.counts, "baseline is empty — run `just audit-snippets --write-baseline`"
    # compare(), not key membership: `_key(r) not in baseline.counts` would
    # check presence only, ignoring both the occurrence count and the
    # REUSED_SNIPPET magnitude, so a third snippet-less reference or a graph
    # growing from 5 shared snippets to 50 would fail `just qc` while this test
    # passed. This is the only test comparing the committed baseline to the live
    # corpus, so it has to assert what qc enforces (#291).
    new = compare(audit(), baseline)
    assert new == [], f"{len(new)} findings are not baselined, e.g. {new[:2]}"


def test_fold_collapses_whitespace_left_by_stripped_punctuation():
    """An elliptical snippet must still match prose that lacks the ellipsis (#269).

    Stripping punctuation turns "…" into spaces; without a second collapse the
    snippet folds with a double space and the report's prose with one, so the
    substring test fails on exactly the snippets most worth verifying.
    """
    from audit_evidence_snippets import _fold
    snippet = _fold("GH48, GH6 with CBM2 domains … release glucose")
    prose = _fold("GH48 GH6 with CBM2 domains release glucose")
    assert "  " not in snippet
    assert snippet == prose


def test_the_audit_report_is_not_tracked(tmp_path):
    """It is rewritten mid-`qc`, so a committed copy is unobservably stale (#268)."""
    import subprocess
    out = subprocess.run(
        ["git", "ls-files", "reports/evidence_snippet_audit.tsv"],
        cwd=REPO_ROOT, capture_output=True, text=True).stdout.strip()
    assert out == "", (
        "reports/evidence_snippet_audit.tsv is tracked again; either untrack it "
        "or wire it into audit-derived-reports on a `git show HEAD:` basis")


# --- baseline identity (#270) -------------------------------------------

def _row(file, locator, defect, detail=""):
    return {"file": file, "locator": locator, "defect": defect,
            "severity": "WARN", "detail": detail}


def test_the_key_ignores_the_evidence_array_index():
    """evidence[1] renumbers to evidence[0] when item 0 is deleted — an
    improvement that used to fail qc as a new finding (#270)."""
    from audit_evidence_snippets import _key
    assert _key(_row("f.yaml", "evidence[1]", "MISSING_SNIPPET")) == \
           _key(_row("f.yaml", "evidence[0]", "MISSING_SNIPPET"))
    assert _key(_row("f.yaml", "g1:a->b[2]", "MISSING_SNIPPET")) == \
           _key(_row("f.yaml", "g1:a->b[0]", "MISSING_SNIPPET"))


def test_the_key_ignores_volatile_detail():
    """detail carries the full snippet and the DOI, so retyping a still-bad
    snippet flipped the key. audit_causal_graphs learned this first."""
    from audit_evidence_snippets import _key
    assert _key(_row("f.yaml", "evidence[0]", "ELLIPTICAL_SNIPPET", "a ... b")) == \
           _key(_row("f.yaml", "evidence[0]", "ELLIPTICAL_SNIPPET", "c ... d"))


def test_the_key_still_separates_files_locators_and_defects():
    from audit_evidence_snippets import _key
    base = _row("f.yaml", "evidence[0]", "MISSING_SNIPPET")
    assert _key(base) != _key(_row("g.yaml", "evidence[0]", "MISSING_SNIPPET"))
    assert _key(base) != _key(_row("f.yaml", "g1:a->b[0]", "MISSING_SNIPPET"))
    assert _key(base) != _key(_row("f.yaml", "evidence[0]", "ELLIPTICAL_SNIPPET"))


def test_fewer_occurrences_than_baselined_is_an_improvement():
    from audit_evidence_snippets import Baseline, compare
    rows = [_row("f.yaml", "evidence[0]", "MISSING_SNIPPET")]
    baseline = Baseline({("f.yaml", "evidence[]", "MISSING_SNIPPET"): 2}, {})
    assert compare(rows, baseline) == []


def test_one_more_occurrence_than_baselined_is_new():
    """The false negative a set-membership key would have introduced: a THIRD
    missing snippet matching a baselined pair and passing silently (#270)."""
    from audit_evidence_snippets import Baseline, compare
    rows = [_row("f.yaml", f"evidence[{i}]", "MISSING_SNIPPET") for i in range(3)]
    baseline = Baseline({("f.yaml", "evidence[]", "MISSING_SNIPPET"): 2}, {})
    new = compare(rows, baseline)
    assert len(new) == 1


def test_an_unbaselined_key_is_new():
    from audit_evidence_snippets import Baseline, compare
    rows = [_row("f.yaml", "evidence[0]", "ELLIPTICAL_SNIPPET")]
    assert len(compare(rows, Baseline({}, {}))) == 1


# --- magnitude ratchet for aggregate defects (#291) ----------------------

def _reused(n, graph="g1:*", file="f.yaml"):
    return _row(file, graph, "REUSED_SNIPPET",
                f"{n} evidence items share one snippet: 'virulence factors'")


def test_a_worse_reused_count_is_new_despite_the_same_key():
    """REUSED_SNIPPET has no index and carries its magnitude in detail, so
    dropping detail from the key let 3 -> 9 pass as one unchanged finding."""
    from audit_evidence_snippets import Baseline, _key, _magnitude_key, compare
    baseline = Baseline({_key(_reused(3)): 1}, {_magnitude_key(_reused(3)): 3})
    assert len(compare([_reused(9)], baseline)) == 1


def test_a_better_reused_count_still_passes():
    """The rot #270 fixed, from the other side: a count in the KEY would make
    3 -> 2 an unbaselined finding and fail on an improvement."""
    from audit_evidence_snippets import Baseline, _key, _magnitude_key, compare
    baseline = Baseline({_key(_reused(3)): 1}, {_magnitude_key(_reused(3)): 3})
    assert compare([_reused(2)], baseline) == []
    assert compare([_reused(3)], baseline) == []


def test_a_character_count_is_not_ratcheted():
    """UNSUPPORTIVE_SNIPPET's leading integer is a length, where larger is
    BETTER — ratcheting it would flag 6 chars growing to 10 as a regression."""
    from audit_evidence_snippets import _magnitude
    assert _magnitude(_row("f.yaml", "evidence[0]", "UNSUPPORTIVE_SNIPPET",
                           "6 chars, supports nothing specific: 'toxins'")) == 0
    assert _magnitude(_reused(7)) == 7


def test_the_real_baseline_records_reused_magnitudes():
    """Guards the wiring: a baseline read without magnitudes silently disarms."""
    from audit_evidence_snippets import DEFAULT_BASELINE, load_baseline
    magnitudes = [v for v in load_baseline(DEFAULT_BASELINE).magnitudes.values() if v]
    assert magnitudes, "no REUSED_SNIPPET magnitudes captured from the baseline"
    assert max(magnitudes) >= 3


def test_two_reused_snippets_in_one_graph_get_separate_magnitudes():
    """`{graph_id}:*` means every reused snippet in a graph shares a _key(), so
    a per-key max would let the smaller of an uneven pair grow to the larger
    unnoticed — trophic_type_classification_axes already carries two (#291)."""
    from audit_evidence_snippets import Baseline, _key, _magnitude_key, compare
    a = _row("f.yaml", "g1:*", "REUSED_SNIPPET",
             "3 evidence items share one snippet: 'carbon source'")
    b = _row("f.yaml", "g1:*", "REUSED_SNIPPET",
             "8 evidence items share one snippet: 'energy source'")
    assert _key(a) == _key(b)
    assert _magnitude_key(a) != _magnitude_key(b)
    baseline = Baseline({_key(a): 2},
                        {_magnitude_key(a): 3, _magnitude_key(b): 8})
    worse_a = dict(a, detail="7 evidence items share one snippet: 'carbon source'")
    assert len(compare([worse_a, b], baseline)) == 1, \
        "the smaller snippet grew to below the larger's magnitude and passed"


# ------------------------------------------------- reworded shared snippet (#292)
#
# The magnitude key folds the snippet TEXT in, because two reuse groups in one
# graph share a _key() and keying on the graph alone lets the smaller grow up to
# the larger unnoticed (#291). The cost was that REWORDING a shared snippet
# produced an unseen key, its baselined magnitude read as 0, and a curator was
# told something got worse when nothing had — pushing them at --write-baseline,
# which is the rot #270 was about.


def _reworded(n, graph="g1:*", file="f.yaml"):
    """Same group, same count — only the quoted text differs."""
    return _row(file, graph, "REUSED_SNIPPET",
                f"{n} evidence items share one snippet: 'virulence factors of the pathogen'")


def test_rewording_the_only_shared_snippet_is_not_new():
    """One baselined magnitude under this key means there is nothing smaller to
    grow into something larger, so comparing against it is safe by construction."""
    from audit_evidence_snippets import (
        Baseline, _key, _magnitude_key, compare)
    baseline = Baseline({_key(_reused(3)): 1}, {_magnitude_key(_reused(3)): 3})
    assert compare([_reworded(3)], baseline) == []


def test_rewording_does_not_let_the_count_grow():
    """The fallback must still ratchet: same group, reworded, but WORSE."""
    from audit_evidence_snippets import (
        Baseline, _key, _magnitude_key, compare)
    baseline = Baseline({_key(_reused(3)): 1}, {_magnitude_key(_reused(3)): 3})
    assert len(compare([_reworded(9)], baseline)) == 1


def test_a_graph_with_two_reuse_groups_still_fails_closed():
    """#292 rejected a per-key MAX fallback because with groups of 4 and 2 the
    2 could be reworded and grown to 4 while the max sheltered it. With more
    than one baselined magnitude the fallback declines, so that cannot happen."""
    from audit_evidence_snippets import (
        Baseline, _key, _magnitude_key, compare)
    baseline = Baseline(
        {_key(_reused(4)): 2},
        {_magnitude_key(_reused(4)): 4,
         _magnitude_key(_row("f.yaml", "g1:*", "REUSED_SNIPPET",
                             "2 evidence items share one snippet: 'energy source'")): 2},
    )
    # the smaller group, reworded and grown to the larger's magnitude
    grown = _row("f.yaml", "g1:*", "REUSED_SNIPPET",
                 "4 evidence items share one snippet: 'energy source used'")
    assert len(compare([grown], baseline)) == 1


def test_an_unrelated_graph_is_not_borrowed_from():
    """The fallback is scoped by _key(), so a different graph's magnitude cannot
    shelter this one."""
    from audit_evidence_snippets import (
        Baseline, _key, _magnitude_key, compare)
    baseline = Baseline({_key(_reused(3)): 1},
                        {_magnitude_key(_reused(9, graph="other:*")): 9})
    assert len(compare([_reworded(3)], baseline)) == 1
