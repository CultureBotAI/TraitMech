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
    from audit_evidence_snippets import DEFAULT_BASELINE, _key, load_baseline
    baseline = load_baseline(DEFAULT_BASELINE)
    assert baseline, "baseline is empty — run `just audit-snippets --write-baseline`"
    new = [r for r in audit() if _key(r) not in baseline]
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
