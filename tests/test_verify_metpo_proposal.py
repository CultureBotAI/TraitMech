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


def test_scope_a_still_fires_for_a_classes_cohort(tmp_path, monkeypatch):
    """The fix must not disarm the check where it genuinely applies."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    # Non-empty classes text that does NOT cite the corpus id.
    vmp.check_scope_a("METPO:1007400\tsome class\t...\n", failures)
    assert len(failures) == 1
    assert "traitmech:000001" in failures[0]


def test_scope_a_passes_when_the_id_is_cited(tmp_path, monkeypatch):
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a(
        "METPO:1007400\tc\tdef\tTraitMech:traitmech:000001\n", failures)
    assert failures == []


def test_scope_a_is_silent_on_an_empty_corpus(tmp_path, monkeypatch):
    """No synthetic ids at all — nothing to cover, whatever the cohort ships."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tc\n", failures)
    assert failures == []
