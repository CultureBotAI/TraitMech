"""Pins what write_validated_trait actually does to formatting (#322).

Its comment claimed a byte-identical round-trip. That is false for most of the
corpus, and believing it is how a bulk script ends up rewriting every long
string in every file it touches. These tests record the real behaviour so the
claim cannot quietly come back.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

DUMP_OPTS = {"default_flow_style": False, "sort_keys": False, "allow_unicode": True}


def test_long_strings_are_rewrapped():
    """The dominant cause: safe_dump wraps at its own width, not the file's."""
    text = (
        "label: t\n"
        "note: this is a deliberately long single-line value that safe_dump will"
        " re-wrap because it exceeds the default width it emits at\n"
    )
    assert yaml.safe_dump(yaml.safe_load(text), **DUMP_OPTS) != text


def test_hand_written_quoting_is_dropped():
    """The second cause: a quoted scalar comes back unquoted."""
    text = 'label: t\nnote: "Textbook Fe(III)-reducer."\n'
    assert yaml.safe_dump(yaml.safe_load(text), **DUMP_OPTS) != text


def test_already_normalised_content_does_round_trip():
    """The claim is not wrong in general -- it is wrong for hand-edited files.

    Content that safe_dump itself produced comes back unchanged, which is why
    the helper is safe for a record it already owns.
    """
    normalised = yaml.safe_dump({"label": "t", "note": "short"}, **DUMP_OPTS)
    assert yaml.safe_dump(yaml.safe_load(normalised), **DUMP_OPTS) == normalised
