#!/usr/bin/env python3
"""Flag a discussion whose prompt is not about the trait it is filed under (#411).

The `kg-microbe-kgscan` pass filed ten `KNOWLEDGE_GAP` discussions whose prompts
were gap-SHAPED sentences lifted from retrieved papers but not gaps about the
traits they landed on: `commensalism` and `gut_associated` both got a sentence
about plant-derived xenomiRs, `animal_pathogen` got marine plastisphere
prokaryotes, and two records got the same contentless review boilerplate. The
scan matched the hedging vocabulary of a gap statement ("remain poorly
understood") without checking the sentence was about the trait.

Nothing in this repo stopped that. The scan lives upstream in
`kg_microbe_kgscan`, so the precision bug cannot be fixed here (#411) -- but the
recurrence can be gated here, which is what this does.

THE RULE. Tokenise the prompt and the trait's own vocabulary -- label,
definition, and every causal-graph node label -- and require at least
`MIN_OVERLAP` shared content words.

THE THRESHOLD IS CALIBRATED, NOT GUESSED. Scored against both the ten original
scraped sentences and the ten curated replacements authored from each record's
own graph:

    scraped / off-topic overlap counts:  0 0 0 0 0 0 0 1 1 2
    curated / on-topic  overlap counts:  4 4 5 5 6 6 8 8 10 11

    min_overlap=1  flags  7/10 off-topic, 0/10 on-topic wrongly
    min_overlap=2  flags  9/10 off-topic, 0/10 on-topic wrongly
    min_overlap=3  flags 10/10 off-topic, 0/10 on-topic wrongly

Three is the lowest value with perfect separation, and it sits inside a two-token
gap between the worst on-topic prompt and the best off-topic one. A false
positive here is a signal to re-run that calibration, not to nudge the number.

ERROR rather than WARN, and wired into `qc`: ten bad records entered the corpus
and nothing objected. A heuristic that only warns would not have stopped them.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_causal_graphs import Corpus, _as_corpus  # noqa: E402

DEFAULT_TRAITS = Path("data/traits")
MIN_OVERLAP = 3

# Function words and hedging vocabulary. The hedges matter: "however", "remain",
# "poorly", "understood" are exactly what the scan matched on, so counting them
# as content would let the failure mode score against itself.
STOPWORDS = frozenset(
    """the a an of in and or to for with on at is are was were be been being that this
    these those which by from as it its their there has have had not no all such other
    more most however also than then both each many some very often between during
    within into onto over under while when where what whether remain remains remained
    poorly understood unknown unclear largely central question questions research
    future challenges critical identifies additionally finally background study
    studies review reviews report reports show shows shown suggest suggests using
    used use based however""".split()
)

WORD = re.compile(r"[a-z]{4,}")

# The scan writes "Knowledge gap for <trait label>: <sentence>". That prefix is
# machine-generated boilerplate containing the trait's own label, so scoring it
# hands every scan-written prompt free relevance credit for words it did not
# choose -- replaying the ten original prompts flagged only 7 of 10 until this
# was stripped, against 10 of 10 in the calibration, which scored the sentence
# alone. Authored content is unaffected: no curator writes this prefix.
GENERATED_PREFIX = re.compile(r"^\s*knowledge gap for\b[^:]*:\s*", re.IGNORECASE)


def scored_text(prompt: str) -> str:
    """The part of a prompt whose wording was actually chosen."""
    return GENERATED_PREFIX.sub("", prompt, count=1)


def tokens(text: str | None) -> set[str]:
    if not text:
        return set()
    return {w for w in WORD.findall(text.lower()) if w not in STOPWORDS}


def trait_vocabulary(doc: dict) -> set[str]:
    """Every content word the record itself uses to describe its subject.

    Node labels are included because they are where a mechanism question's
    vocabulary actually lives -- a question about c-di-GMP shares nothing with a
    trait label reading "biofilm formation" but everything with its graph.
    """
    vocab = tokens(doc.get("label")) | tokens(doc.get("definition"))
    for syn in doc.get("synonyms") or []:
        vocab |= tokens(syn.get("synonym_text") if isinstance(syn, dict) else syn)
    for graph in doc.get("causal_graphs") or []:
        for node in graph.get("nodes") or []:
            vocab |= tokens(node.get("label"))
    return vocab


def relevance_rows(
    source: Path | Corpus = DEFAULT_TRAITS, min_overlap: int = MIN_OVERLAP
) -> tuple[list[tuple[str, str, str, str]], dict[str, int]]:
    """Return (rows, counts); each row is (file, discussion_id, defect, detail)."""
    rows: list[tuple[str, str, str, str]] = []
    counts = {"discussions": 0, "records": 0}
    for rel, doc in _as_corpus(source):
        discussions = doc.get("discussions") or []
        if discussions:
            counts["records"] += 1
        vocab = trait_vocabulary(doc)
        for disc in discussions:
            counts["discussions"] += 1
            did = disc.get("discussion_id", "?")
            prompt = disc.get("prompt") or ""
            if not prompt.strip():
                rows.append((rel, did, "EMPTY_PROMPT", "no prompt text"))
                continue
            shared = tokens(scored_text(prompt)) & vocab
            if len(shared) < min_overlap:
                rows.append(
                    (
                        rel,
                        did,
                        "OFF_TOPIC_DISCUSSION",
                        f"{len(shared)} shared content word(s) with the trait "
                        f"(need {min_overlap}): {sorted(shared) or 'none'}",
                    )
                )
    return rows, counts


ERRORS = {"OFF_TOPIC_DISCUSSION", "EMPTY_PROMPT"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--traits-dir", type=Path, default=DEFAULT_TRAITS)
    ap.add_argument("--min-overlap", type=int, default=MIN_OVERLAP)
    args = ap.parse_args()

    rows, counts = relevance_rows(args.traits_dir, args.min_overlap)
    for rel, did, defect, detail in rows:
        print(f"{defect}\t{rel}\t{did}\t{detail}")
    errors = [r for r in rows if r[2] in ERRORS]
    print(
        f"\ndiscussion relevance: {counts['discussions']} discussion(s) across "
        f"{counts['records']} record(s); {len(errors)} error(s) "
        f"(min_overlap={args.min_overlap})"
    )
    if errors:
        print(
            "  A flagged prompt is either filed under the wrong trait -- the #411 "
            "failure -- or worded without using any of the trait's own vocabulary. "
            "Re-anchor it or reword it; do not lower the threshold, which was "
            "calibrated with a two-token margin."
        )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
