"""Every intra-repo `file.md#anchor` cross-reference must resolve (#632).

`CLAUDE.md` is loaded every session and is the main route into the playbook's
longer sections, so a link that silently degrades to a page-top jump costs a
reader real time on an 880-line document. Nothing checked these until now, and
the first one was added by #629.

Offline, and it generalises: any cross-reference added later is covered without
touching this file.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\]\(([^)\s]+\.md)#([^)\s]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)


def slugify(heading: str) -> str:
    """GitHub's anchor rule: lowercase, drop punctuation, spaces to hyphens."""
    text = heading.strip().lower()
    text = re.sub(r"[^a-z0-9 _-]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def markdown_sources() -> list[Path]:
    paths = [REPO_ROOT / "CLAUDE.md"]
    paths += sorted((REPO_ROOT / "docs").glob("*.md"))
    paths += sorted((REPO_ROOT / "history").glob("*.md"))
    return [p for p in paths if p.exists()]


def anchor_links() -> list[tuple[Path, str, str]]:
    found = []
    for path in markdown_sources():
        for target, anchor in LINK_RE.findall(path.read_text(encoding="utf-8")):
            found.append((path, target, anchor))
    return found


def test_the_scan_is_not_vacuous():
    """If the pattern ever stops matching, this test would pass while checking nothing."""
    assert anchor_links(), (
        "no `file.md#anchor` links were found — either they were all removed, or "
        "LINK_RE no longer matches the way they are written"
    )


@pytest.mark.parametrize(
    "source,target,anchor",
    anchor_links(),
    ids=[f"{s.name}->{t}#{a}" for s, t, a in anchor_links()],
)
def test_anchor_link_resolves(source: Path, target: str, anchor: str):
    resolved = (source.parent / target).resolve()
    assert resolved.is_file(), f"{source.name} links to a missing file: {target}"
    slugs = {slugify(h) for h in HEADING_RE.findall(resolved.read_text(encoding="utf-8"))}
    assert anchor in slugs, (
        f"{source.name} links to {target}#{anchor}, but no heading there slugifies to it. "
        f"Renaming a heading breaks the link silently — update both."
    )


@pytest.mark.parametrize("heading,expected", [
    ("## Merging when another curation PR lands first (#622)",
     "merging-when-another-curation-pr-lands-first-622"),
    ("# Curation history", "curation-history"),
    ("### A deep-research report is not a snippet source (#247)",
     "a-deep-research-report-is-not-a-snippet-source-247"),
    ("## `paths:` filters", "paths-filters"),
])
def test_slugify_matches_github(heading, expected):
    assert slugify(heading.lstrip("# ")) == expected
