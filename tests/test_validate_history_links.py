from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from validate_history_links import main  # noqa: E402


def test_validator_rejects_bare_link(tmp_path, capsys):
    path = tmp_path / "record.yaml"
    path.write_text("links:\n  issues:\n  - '423'\n", encoding="utf-8")

    assert main([str(path)]) == 1
    assert "links.issues[0]" in capsys.readouterr().err


def test_validator_accepts_absolute_urls(tmp_path):
    path = tmp_path / "record.yaml"
    path.write_text(
        "links:\n"
        "  issues:\n"
        "  - https://github.com/CultureBotAI/TraitMech/issues/423\n"
        "  prs:\n"
        "  - https://github.com/CultureBotAI/TraitMech/pull/529\n",
        encoding="utf-8",
    )

    assert main([str(path)]) == 0
