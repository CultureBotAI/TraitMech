"""Pins what write_validated_trait actually does to formatting (#322).

The helper's comment claims a byte-identical round-trip. Before #322 that was
false for 350 of 477 records, and believing it is how a bulk script ends up
rewriting every long string in every file it touches. #322 normalised the corpus
so the claim holds, and these tests ENFORCE it rather than merely describing it.

They bind to the helper itself, not to a re-declared copy of its options.
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
    emit_trait_yaml,
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
        (same if emit_trait_yaml(doc) == before else changed).append(path)
    return tuple(same), tuple(changed)


def test_a_corpus_file_round_trips_byte_identically(tmp_path):
    """End to end through write_validated_trait, not through safe_dump.

    Since #322's normalisation the claim in write_validated.py is TRUE, so this
    asserts it directly rather than demonstrating its failure. Change EMIT_OPTS
    or how they are composed and this breaks on a real record.
    """
    source = TRAITS[0]
    doc = yaml.safe_load(source.read_text())
    out = tmp_path / source.name
    write_validated_trait(doc, out)
    assert out.read_bytes() == source.read_bytes()


def test_the_helpers_own_output_round_trips(tmp_path):
    """Idempotence: writing the helper's own output again changes nothing.

    Distinct from the corpus test above, which asserts the CORPUS is in that
    form. This asserts the property of the emitter itself, so it still holds if
    a record is ever legitimately excluded.
    """
    same, _changed = _split()
    doc = yaml.safe_load((same or TRAITS)[0].read_text())
    first = tmp_path / "a.yaml"
    write_validated_trait(doc, first)
    second = tmp_path / "b.yaml"
    write_validated_trait(yaml.safe_load(first.read_text()), second)
    assert first.read_bytes() == second.read_bytes()


def test_the_whole_corpus_round_trips():
    """The claim is now ENFORCED, not merely corrected (#322).

    Before normalisation this asserted a 127/350 split, i.e. it documented how
    false the claim was. The corpus was normalised so the claim became true, and
    this is what keeps it true: any record hand-edited back into a form
    safe_dump would not emit fails here, and so does any change to EMIT_OPTS or
    to how they are composed.
    """
    same, changed = _split()
    assert not changed, (
        f"{len(changed)} record(s) no longer round-trip through "
        f"write_validated_trait; first few: "
        f"{[str(p.relative_to(REPO_ROOT)) for p in changed[:5]]}"
    )
    # _split() skips anything that will not parse. The old assertion pinned the
    # total at 127+350=477, so a skipped record failed it; `not changed` alone
    # passes vacuously for one. Pin the total too, or a record edited into
    # invalid YAML silently drops out of the guard (#344 review).
    assert len(same) == len(TRAITS), (
        f"{len(TRAITS) - len(same)} record(s) did not parse and were skipped, "
        f"so they are not covered by the round-trip guard"
    )
