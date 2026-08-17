"""Guards on the frozen scan provenance in the knowledge-gap curation (#409).

SCAN_OUTPUT holds the ten sentences the kg-microbe-kgscan pass produced, as
literals, because building them from the record's live state was correct exactly
once -- a second run quoted the authored question back as the scraped one. The
literals are the only surviving copy in the working tree, so they get tests.

The wrapping that produced them also silently corrupted one string
("post-infectious" -> "post- infectious"), which is the specific failure
`test_no_hyphen_space_artefacts` exists to catch: a verbatim quote that is not
verbatim is worse than no quote, because it reads as evidence.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from curate_knowledge_gaps import PLAN, SCAN_OUTPUT, scan_note  # noqa: E402


def test_every_planned_discussion_has_frozen_scan_output():
    assert set(PLAN) == set(SCAN_OUTPUT)


def test_no_hyphen_space_artefacts():
    """A hyphen followed by a space is how the line-wrapping corrupted a quote."""
    for did, (prompt, _) in SCAN_OUTPUT.items():
        assert "- " not in prompt, f"{did}: wrapping artefact in a verbatim quote"


def test_no_double_spaces_from_joined_fragments():
    for did, (prompt, _) in SCAN_OUTPUT.items():
        assert "  " not in prompt, f"{did}: double space from joined fragments"


def test_prompts_are_the_scan_format_not_the_authored_question():
    """The regression that motivated freezing these: notes quoting the rewrite.

    Every scan prompt starts with its generated prefix. An authored question
    never does, so this fails loudly if the literals are ever refreshed from
    already-curated records.
    """
    for did, (prompt, _) in SCAN_OUTPUT.items():
        assert prompt.startswith("Knowledge gap for "), f"{did}: not the scan's format"


def test_every_entry_kept_its_references():
    for did, (_, refs) in SCAN_OUTPUT.items():
        assert refs, f"{did}: lost its PMIDs"
        assert all(re.fullmatch(r"PMID:\d+", r) for r in refs), f"{did}: malformed reference"


def test_note_quotes_the_scraped_sentence_and_all_its_pmids():
    did = "kgscan-30bcdf4a32b0"
    prompt, refs = SCAN_OUTPUT[did]
    note = scan_note(did, PLAN[did]["scan_topic"])
    assert prompt in note
    for ref in refs:
        assert ref in note
    assert "retrieved from ." not in note, "empty reference list rendered into the note"


def test_note_does_not_depend_on_record_state():
    """scan_note takes an id, not a record -- so a rerun cannot corrupt it."""
    did = "kgscan-4fc1a06fa1e3"
    assert scan_note(did, "x") == scan_note(did, "x")
    assert SCAN_OUTPUT[did][0] in scan_note(did, "x")


def test_corpus_notes_still_hold_the_scan_sentences():
    """The committed records, not just the table: provenance survived the write."""
    import yaml

    for did, plan in PLAN.items():
        doc = yaml.safe_load((Path("data/traits") / plan["file"]).read_text())
        disc = next(d for d in doc["discussions"] if d["discussion_id"] == did)
        prompt, refs = SCAN_OUTPUT[did]
        assert prompt in disc["notes"], f"{did}: scraped sentence missing from the record"
        for ref in refs:
            assert ref in disc["notes"], f"{did}: {ref} missing from the record"
        assert "evidence" not in disc, f"{did}: scan PMIDs re-pointed at the authored question"
