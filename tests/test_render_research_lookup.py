"""Unit tests for the deep-research lookup in scripts/render_trait_pages.py.

The renderer looked for `research/traits/<cat>/<slug>.md` while the pipeline
writes `<slug>-deep-research-<provider>.md`, so the research block never
rendered for any trait (#233). These pin the two halves of the fix: finding the
file the pipeline actually writes, and previewing the answer rather than the
front matter and the twice-echoed prompt that precede it.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import render_trait_pages  # noqa: E402
from render_trait_pages import (  # noqa: E402
    RESEARCH_PROMPT_TAIL,
    research_answer,
    research_report,
)


@pytest.fixture()
def research_dir(tmp_path, monkeypatch):
    """Point the module's RESEARCH_DIR at a temp tree."""
    root = tmp_path / "research" / "traits"
    (root / "ecology").mkdir(parents=True)
    monkeypatch.setattr(render_trait_pages, "RESEARCH_DIR", root)
    return root / "ecology"


def test_finds_the_name_the_pipeline_writes(research_dir):
    written = research_dir / "mutualism-deep-research-falcon.md"
    written.write_text("body")
    assert research_report("ecology", "mutualism") == written


def test_the_name_the_renderer_used_to_expect_is_not_matched(research_dir):
    # The bug in reverse: a bare <slug>.md is not what the pipeline writes, so
    # matching it would resurrect the mismatch from the other side.
    (research_dir / "mutualism.md").write_text("body")
    assert research_report("ecology", "mutualism") is None


def test_no_report_is_not_an_error(research_dir):
    assert research_report("ecology", "mutualism") is None


def test_citation_sidecar_is_never_picked(research_dir):
    # `<slug>-deep-research-falcon.md.citations.md` matches the same glob and is
    # a reference list, not a report.
    (research_dir / "mutualism-deep-research-falcon.md.citations.md").write_text("refs")
    assert research_report("ecology", "mutualism") is None


def test_a_sidecar_does_not_shadow_its_report(research_dir):
    report = research_dir / "mutualism-deep-research-falcon.md"
    report.write_text("body")
    (research_dir / "mutualism-deep-research-falcon.md.citations.md").write_text("refs")
    assert research_report("ecology", "mutualism") == report


def test_known_provider_beats_alphabetical_order(research_dir):
    """The #245 tie-break: `codex` sorts first, `falcon` is the one to render."""
    (research_dir / "cellulolysis-deep-research-codex.md").write_text("codex")
    falcon = research_dir / "cellulolysis-deep-research-falcon.md"
    falcon.write_text("falcon")
    assert research_report("ecology", "cellulolysis") == falcon


def test_unknown_providers_fall_back_to_name_order(research_dir):
    # Deterministic rather than arbitrary — #228 made reproducible output a
    # requirement, and an unrecognised provider must not make the render depend
    # on directory iteration order.
    (research_dir / "x-deep-research-zeta.md").write_text("z")
    (research_dir / "x-deep-research-alpha.md").write_text("a")
    assert research_report("ecology", "x").name == "x-deep-research-alpha.md"


def test_a_longer_slug_does_not_capture_a_shorter_ones_report(research_dir):
    (research_dir / "biosafety_level_2-deep-research-falcon.md").write_text("two")
    assert research_report("ecology", "biosafety_level") is None


# --- preview extraction -------------------------------------------------

_REPORT = f"""---
provider: falcon
template_file: /Users/someone/TraitMech/templates/trait_causal_graph_research.md
---

## Question

# Microbial Trait Causal Graph Research Template
- {RESEARCH_PROMPT_TAIL}.

## Output

# Microbial Trait Causal Graph Research Template
- {RESEARCH_PROMPT_TAIL}.


# TraitMech curation report: mutualism

The answer starts here.
"""


def test_preview_starts_at_the_answer():
    assert research_answer(_REPORT)[0] == "# TraitMech curation report: mutualism"


def test_preview_drops_front_matter_and_both_prompt_copies():
    body = "\n".join(research_answer(_REPORT))
    assert "provider: falcon" not in body
    assert "/Users/someone/" not in body
    assert "Research Template" not in body
    assert RESEARCH_PROMPT_TAIL not in body


def test_report_without_the_marker_keeps_its_body(research_dir):
    """A different provider's layout still renders — just without the trim."""
    lines = research_answer("---\nprovider: codex\n---\n\n# A report\n\nBody.\n")
    assert lines == ["# A report", "", "Body."]


def test_no_front_matter_is_handled():
    assert research_answer("# Plain report\n\nBody.\n") == ["# Plain report", "", "Body."]


def test_every_tracked_report_yields_a_substantial_answer():
    """The trim must not silently empty a page for any real report."""
    reports = [
        p for p in sorted((REPO_ROOT / "research" / "traits").rglob("*-deep-research-*.md"))
        if not p.name.endswith(".citations.md")
    ]
    assert len(reports) >= 353, f"expected the tracked sweep corpus, found {len(reports)}"
    thin = [
        p.name for p in reports
        if len([line for line in research_answer(p.read_text()) if line.strip()]) < 20
    ]
    assert thin == [], f"reports whose answer did not survive the trim: {thin}"


def test_the_prompt_marker_appears_exactly_twice_in_every_sweep_report():
    """The trim anchors on the second marker; a layout change must be loud.

    If a future provider layout echoes the prompt a different number of times,
    or a report's answer quotes the instruction line, the preview boundary moves
    silently. Assert the shape the trim depends on rather than only asserting
    that something survived it (#255).
    """
    reports = sorted(
        (REPO_ROOT / "research" / "traits").rglob("*-deep-research-falcon.md")
    )
    assert len(reports) >= 353
    off = {
        p.name: p.read_text().count(RESEARCH_PROMPT_TAIL)
        for p in reports
        if p.read_text().count(RESEARCH_PROMPT_TAIL) != 2
    }
    assert off == {}, f"reports not echoing the prompt exactly twice: {off}"


def test_a_quoted_marker_in_the_answer_does_not_truncate_it():
    """The asymmetry #255 is about: boilerplate is survivable, lost findings are not."""
    text = (
        "---\np: f\n---\n"
        f"# Template\n- {RESEARCH_PROMPT_TAIL}.\n"
        f"# Template\n- {RESEARCH_PROMPT_TAIL}.\n"
        "\n# The answer\n\nFirst finding.\n"
        f"We note the instruction to log {RESEARCH_PROMPT_TAIL}.\n"
        "Last finding.\n"
    )
    body = research_answer(text)
    assert body[0] == "# The answer"
    assert "First finding." in body
    assert "Last finding." in body


@pytest.mark.parametrize("sidecar", [
    # The deep-research-client pipeline's form, and the only one in the tree today.
    "x-deep-research-zeta.md.citations.md",
    # _edison_capture's form. It sorts AHEAD of `x-deep-research-zeta.md`, since
    # '-' (0x2D) < '.' (0x2E), so a dot-only exclusion would render the
    # bibliography as the report for an unrecognised provider (#259).
    "x-deep-research-zeta-citations.md",
])
def test_neither_sidecar_convention_can_shadow_a_report(research_dir, sidecar):
    report = research_dir / "x-deep-research-zeta.md"
    report.write_text("the report")
    (research_dir / sidecar).write_text("references")
    assert research_report("ecology", "x") == report
