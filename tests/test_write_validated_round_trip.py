"""Pins what write_validated_trait actually does to formatting (#322).

Its comment claimed a byte-identical round-trip. That is false for most of the
corpus, and believing it is how a bulk script ends up rewriting every long
string in every file it touches.

These tests bind to the helper itself, not to a re-declared copy of its options.
The first cut asserted on ``yaml.safe_dump`` with a duplicated ``DUMP_OPTS``
dict, which meant adding e.g. ``width=4096`` to the real options would have
stopped the re-wrapping, falsified the comment's stated cause and its counts,
and left the tests passing against PyYAML's defaults (#322 review) -- the exact
failure mode this file exists to prevent, one level up.
"""

from __future__ import annotations

import functools
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.validation.write_validated import (  # noqa: E402
    EMIT_OPTS,
    write_validated_trait,
)

TRAITS = sorted((REPO_ROOT / "data" / "traits").rglob("*.yaml"))


@functools.lru_cache(maxsize=1)
def _split() -> tuple[tuple[Path, ...], tuple[Path, ...]]:
    """Corpus files that survive a round trip, and those reformatted.

    Cached: three tests need it and each walk parses all 477 records.
    """
    same: list[Path] = []
    changed: list[Path] = []
    for path in TRAITS:
        before = path.read_text()
        try:
            doc = yaml.safe_load(before)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        (same if yaml.safe_dump(doc, **EMIT_OPTS) == before else changed).append(path)
    return tuple(same), tuple(changed)


def test_a_hand_edited_corpus_file_is_reformatted_by_the_helper(tmp_path):
    """End to end through write_validated_trait, not through safe_dump.

    This is the assertion that binds to the real options: change them so the
    reformatting stops and this fails.
    """
    _same, changed = _split()
    assert changed, "expected some corpus files to be reformatted"
    source = changed[0]
    doc = yaml.safe_load(source.read_text())
    out = tmp_path / source.name
    write_validated_trait(doc, out)
    assert out.read_bytes() != source.read_bytes()


def test_the_helpers_own_output_round_trips(tmp_path):
    """The claim is wrong for HAND-EDITED files, not in general.

    A file the helper already owns comes back byte-identical, which is why it is
    safe for a single record and unsafe for a bulk rewrite.
    """
    same, _changed = _split()
    doc = yaml.safe_load((same or TRAITS)[0].read_text())
    first = tmp_path / "a.yaml"
    write_validated_trait(doc, first)
    second = tmp_path / "b.yaml"
    write_validated_trait(yaml.safe_load(first.read_text()), second)
    assert first.read_bytes() == second.read_bytes()


def test_the_documented_corpus_split_is_still_true():
    """Keeps the numbers in write_validated.py honest rather than a snapshot.

    The original claim misled precisely because it was frozen prose nobody
    rechecked. This fails loudly on the day #322's normalisation lands, which is
    the correct time to update the comment.
    """
    same, changed = _split()
    assert (len(same), len(changed)) == (127, 350), (
        f"round-trip split moved to {len(same)} identical / {len(changed)} "
        f"reformatted; update the counts in write_validated.py's comment"
    )
