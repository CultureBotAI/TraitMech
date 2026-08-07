"""Regression tests for scripts/verify_metpo_proposal.py's Scope-A check.

Locks in the #318 contract: a cohort that ships no classes template is not
doing Scope A, so the check must skip rather than treat every `traitmech:` id
in the corpus as uncited. Before the fix, `class_tsv_text` was `""` for such a
cohort and `i not in ""` was true for every id, so every predicate-only cohort
(v2, v4, v6) failed the skill's required verification step.

The check still has to fire for cohorts that DO carry a classes template,
otherwise the fix would disarm it — that is the second test here.
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import verify_metpo_proposal as vmp  # noqa: E402


def _corpus(tmp_path: Path, *ids: str) -> Path:
    """A stand-in data/traits/ holding one YAML per synthetic id."""
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    for i, ident in enumerate(ids):
        (d / f"t{i}.yaml").write_text(f"identifier: {ident}\nlabel: t{i}\n")
    return d


def test_scope_a_skips_when_cohort_has_no_classes_template(tmp_path, monkeypatch):
    """#318: a predicate-only cohort must not be judged against Scope A."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a("", failures)
    assert failures == []


def test_not_citing_every_corpus_id_is_not_a_failure(tmp_path, monkeypatch):
    """#319: whole-corpus coverage is a CROSS-cohort property.

    v1/v3/v7 lift causal-graph scaffolding, not synthetic traits, and failed
    permanently over a backlog they never took on. Cohort v5 carries all 120,
    so the coverage exists -- just not in every cohort.
    """
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tsome class\t...\n", failures)
    assert failures == []


def test_a_phantom_citation_fails(tmp_path, monkeypatch):
    """The property that IS per-cohort: a cited id must resolve.

    Catches a typo, or a citation left behind after a record was renamed or
    removed -- which the old whole-corpus rule could not see, since it only
    looked for absences in the other direction.
    """
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tc\tdef\tTraitMech:traitmech:999999\n", failures)
    assert len(failures) == 1
    assert "traitmech:999999" in failures[0]


def test_scope_a_passes_when_the_id_is_cited(tmp_path, monkeypatch):
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a(
        "METPO:1007400\tc\tdef\tTraitMech:traitmech:000001\n", failures)
    assert failures == []


def test_a_longer_cited_id_is_not_confused_with_a_shorter_real_one(tmp_path, monkeypatch):
    """#321: the coverage test must match whole ids, not substrings.

    `traitmech:000001 not in "...traitmech:0000010..."` is False, so the shorter
    id read as covered and the check could report full Scope-A coverage while
    that term was genuinely un-lifted. A coverage gate that passes when it should
    fail is worse than no gate.
    """
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    # traitmech:0000010 is cited but does not exist; a substring scan would have
    # matched it against the real traitmech:000001 and reported nothing (#321).
    vmp.check_scope_a("METPO:1007400\tc\tdef\tTraitMech:traitmech:0000010\n", failures)
    assert len(failures) == 1
    assert "traitmech:0000010" in failures[0]


def test_scope_a_is_silent_on_an_empty_corpus(tmp_path, monkeypatch):
    """No synthetic ids at all — nothing to cover, whatever the cohort ships."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tc\n", failures)
    assert failures == []
