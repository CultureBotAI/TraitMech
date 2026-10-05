from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from render_discussions_shell import render_shell  # noqa: E402
from render_trait_pages import (  # noqa: E402
    load_record_sessions,
    record_timestamp,
    synonym_search_text,
    template_environment,
)


def test_search_indexes_names_not_synonym_metadata():
    text = synonym_search_text({"synonyms": [
        {"synonym_text": "ferrous iron phototrophy", "synonym_type": "EXACT",
         "source": "DOI:10.123/example"}, "legacy synonym",
    ]})
    assert text == "ferrous iron phototrophy legacy synonym"
    for key in ("synonym_type", "source", "EXACT", "DOI:"):
        assert key not in text


def test_record_session_association_is_exact_and_preserves_attribution(tmp_path):
    folder = tmp_path / "history/records/example"
    folder.mkdir(parents=True)
    (folder / "one.yaml").write_text(
        "target: {path: data/traits/metabolism/example.yaml}\n"
        "session: {timestamp: '2026-09-14T22:08:51Z', actors: [{name: codex}]}\n"
        "events: [{type: CREATE, summary: Original curation}]\n"
    )
    sessions = load_record_sessions(tmp_path)
    assert list(sessions) == ["data/traits/metabolism/example.yaml"]
    events = sessions["data/traits/metabolism/example.yaml"]
    assert record_timestamp({}, events) == "2026-09-14 22:08 UTC"
    assert events[0]["session"]["actors"][0]["name"] == "codex"
    assert events[0]["source_url"].endswith("/history/records/example/one.yaml")
    assert record_timestamp({}) == ""


def test_actual_photoferrotrophy_session_is_retained_as_source_provenance():
    sessions = load_record_sessions()["data/traits/metabolism/photoferrotrophy.yaml"]
    assert sessions[0]["events"][0]["type"] == "CREATE"
    assert record_timestamp({}, sessions) == "2026-09-14 22:08 UTC"


def test_discussions_shell_is_idempotent_and_preserves_browser_payload():
    raw = ('<html><head></head><body><nav aria-label="Project navigation">'
           '<a href="https://culturebotai.github.io/mechs/">All Mech projects</a>'
           '</nav><main id="main-content">Content</main><script src="data.js"></script>'
           '</body></html>')
    result = render_shell(raw)
    assert render_shell(result) == result
    assert '<main id="main-content">Content</main><script src="data.js"></script>' in result
    assert result.count('../../pages/index.html') == 1
    assert result.count('../../pages/browse.html') == 1
    assert '../../pages/theme-toggle.js' in result
    assert 'https://culturebotai.github.io/mechs/' in result
    with pytest.raises(ValueError, match="template changed"):
        render_shell('<html><head></head><body>Unexpected layout</body></html>')


def test_category_title_is_readable_words():
    result = template_environment().get_template("category.html").render(
        category="QUANTITATIVE_PROPERTY", traits=[], root="../",
    )
    assert '<h1>Quantitative Property ' in result
