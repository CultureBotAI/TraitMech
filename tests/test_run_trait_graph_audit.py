"""Unit tests for the malformed-CURIE scan in scripts/run_trait_graph_audit.py.

The scan exists because the sweep produced double-prefixed CURIEs twice, and the
second time the manual grep for them raced a report still being generated. It is
wired into `--verify` and therefore into `just qc`, where it currently reports
zero hits across all 707 tracked artifacts.

A gate whose corpus is already clean is exactly the kind that can be silently
broken — a mistyped pattern would keep reporting zero forever. These tests are
what distinguishes "found nothing" from "cannot find anything".
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from run_trait_graph_audit import scan_malformed_curies  # noqa: E402


def _scan(tmp_path: Path, text: str):
    path = tmp_path / "report.md"
    path.write_text(text)
    return scan_malformed_curies([path])


@pytest.mark.parametrize("line,expected", [
    # The shape that actually shipped: the template hands the provider an
    # already-prefixed identifier and asks it to quote it verbatim; it prefixed
    # it again. Seen for METPO, and reachable for any ontology.
    ("| phenotype | `METPO:METPO:1000059` |", "double prefix"),
    ("grounded to GO:GO:0009860 where applicable", "double prefix"),
    ("see chebi:chebi:15378 for the proton", "double prefix"),
    # CURIE prefixes are case-sensitive; nothing downstream normalises them.
    ("candidate grounding go:0009860", "lowercase prefix"),
    ("candidate grounding Chebi:15378", "lowercase prefix"),
    # The OBO underscore form used where a CURIE was expected.
    ("candidate grounding GO_0009860", "underscore form"),
])
def test_malformed_shapes_are_caught(tmp_path, line, expected):
    hits = _scan(tmp_path, line)
    # A string can be wrong in more than one way at once — `chebi:chebi:15378`
    # is both double-prefixed and lowercased — so this asserts the shape is
    # named, not that it is named exactly once.
    assert expected in [name for _, _, name, _ in hits], hits
    assert all(line_no == 1 for _, line_no, _, _ in hits)


@pytest.mark.parametrize("line", [
    # Correctly-cased CURIEs, which the case-insensitive lowercase pattern must
    # match internally and then discard.
    "| infection thread | `GO:0009860` | canonical entry route |",
    "CHEBI:15378 is the proton; ENVO:01000992 the environment",
    "METPO:1000059 and NCBITaxon:562 and PATO:0000384",
    # The underscore form is legitimate inside a real PURL — the pattern's
    # negative lookbehind has to spare this one.
    "http://purl.obolibrary.org/obo/GO_0009860",
    "see <http://purl.obolibrary.org/obo/CHEBI_15378>",
    # Prose colons that are not CURIEs at all.
    "Note: note: this is a repeated word, not a prefix, and has no id",
    # A short numeric suffix is a section number or a time, not an identifier.
    "GO:12 and step 3_2024 are not identifiers",
])
def test_well_formed_content_is_not_flagged(tmp_path, line):
    assert _scan(tmp_path, line) == []


def test_reports_path_and_line_number(tmp_path):
    hits = _scan(tmp_path, "clean line\nanother clean line\nbad METPO:METPO:1000059 here\n")
    assert len(hits) == 1
    path, line_no, name, text = hits[0]
    assert path == tmp_path / "report.md"
    assert line_no == 3
    assert name == "double prefix"
    assert text.startswith("METPO:METPO:")


def test_the_tracked_corpus_is_clean():
    """The invariant #241 asserted in prose, asserted from the tree instead."""
    artifacts = sorted((REPO_ROOT / "research" / "traits").rglob("*.md"))
    assert artifacts, "no research artifacts found — research/ should be tracked"
    hits = scan_malformed_curies(artifacts)
    assert hits == [], f"malformed CURIEs in tracked artifacts: {hits[:5]}"
