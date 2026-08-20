"""Tests for the off-topic-discussion gate (#411).

The load-bearing test is `test_replaying_the_scan_flags_all_ten`: the gate exists
because ten off-topic gaps entered the corpus unopposed, so the thing to pin is
that it would have caught them -- not that it accepts what is there now.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit_discussion_relevance import (  # noqa: E402
    ERRORS,
    MIN_OVERLAP,
    relevance_rows,
    scored_text,
    tokens,
    trait_vocabulary,
)


def _doc(prompt: str, *, label="biofilm formation", nodes=(), definition="") -> dict:
    return {
        "label": label,
        "definition": definition,
        "causal_graphs": [{"nodes": [{"label": n} for n in nodes]}],
        "discussions": [{"discussion_id": "d1", "prompt": prompt}],
    }


def _rows(doc: dict):
    return relevance_rows([("f.yaml", doc)])[0]


def test_an_on_topic_question_passes():
    doc = _doc(
        "Is the nitric oxide effect on dispersal mediated by lowering c-di-GMP?",
        nodes=["nitric oxide", "biofilm dispersal", "c-di-GMP"],
    )
    assert _rows(doc) == []


def test_an_off_topic_sentence_is_flagged():
    doc = _doc(
        "MicroRNAs are small noncoding RNAs derived from edible plants.",
        nodes=["nitric oxide", "biofilm dispersal"],
    )
    rows = _rows(doc)
    assert [r[2] for r in rows] == ["OFF_TOPIC_DISCUSSION"]
    assert rows[0][2] in ERRORS


def test_contentless_boilerplate_is_flagged():
    """"It identifies gaps for future research" names no gap at all."""
    doc = _doc("Additionally, it identifies ongoing challenges and critical knowledge gaps.")
    assert [r[2] for r in _rows(doc)] == ["OFF_TOPIC_DISCUSSION"]


def test_an_empty_prompt_is_flagged():
    assert [r[2] for r in _rows(_doc("   "))] == ["EMPTY_PROMPT"]


def test_the_generated_prefix_earns_no_credit():
    """The scan's own prefix contains the trait label; scoring it hid 3 of 10."""
    assert scored_text("Knowledge gap for biofilm formation: xenomiRs cross kingdoms.") == (
        "xenomiRs cross kingdoms."
    )
    doc = _doc(
        "Knowledge gap for biofilm formation: MicroRNAs are small noncoding RNAs.",
        nodes=["nitric oxide"],
    )
    assert [r[2] for r in _rows(doc)] == ["OFF_TOPIC_DISCUSSION"]


def test_a_curator_written_prompt_is_not_stripped():
    text = "Does the extracellular matrix confer biofilm-defining properties?"
    assert scored_text(text) == text


def test_hedging_vocabulary_does_not_count_as_content():
    """The scan matched on exactly these words, so they must not score."""
    assert tokens("remains poorly understood however largely unclear") == set()


def test_node_labels_are_part_of_the_vocabulary():
    vocab = trait_vocabulary(_doc("x", nodes=["quorum sensing autoinducers"]))
    assert {"quorum", "sensing", "autoinducers"} <= vocab


def test_synonyms_count_toward_the_vocabulary():
    doc = _doc("x")
    doc["synonyms"] = [{"synonym_text": "thermophile"}]
    assert "thermophile" in trait_vocabulary(doc)


def test_threshold_is_the_calibrated_value():
    assert MIN_OVERLAP == 3, (
        "calibrated: off-topic scored 0-2 and on-topic 4-11, so 3 is the lowest "
        "value with perfect separation. Changing it needs a re-run of that "
        "measurement, not a guess."
    )


def test_replaying_the_scan_flags_all_ten():
    """The reason this gate exists: it must catch what actually got through."""
    import yaml
    from curate_knowledge_gaps import PLAN, SCAN_OUTPUT

    corpus = []
    for did, plan in PLAN.items():
        doc = yaml.safe_load((Path("data/traits") / plan["file"]).read_text())
        for disc in doc["discussions"]:
            if disc["discussion_id"] == did:
                disc["prompt"] = SCAN_OUTPUT[did][0]
        corpus.append((plan["file"], doc))
    rows, counts = relevance_rows(corpus)
    assert counts["discussions"] == 10
    assert len(rows) == 10, f"the gate must catch all ten, caught {len(rows)}"


def test_the_real_corpus_is_clean():
    rows, counts = relevance_rows()
    assert [r for r in rows if r[2] in ERRORS] == []
    assert counts["discussions"] == 10
