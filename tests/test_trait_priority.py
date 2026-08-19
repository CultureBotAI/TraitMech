"""Tests for the curation-priority queue ported from DisMech (#448).

The test that carries the most weight is `test_series_do_not_lump_at_measured_overlap`.
DisMech's prioritiser lumps a subtype series into its parent; importing that rule
unchanged would tell a curator to merge TraitMech's binned families, which
measurably hold distinct mechanism content (5% mean sibling overlap). So the
inverted rule needs a test that fails if someone "fixes" it back.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from trait_priority import (  # noqa: E402
    ACTIONS,
    build_queue,
    family_stem,
    is_grouping_term,
    jaccard,
    load_config,
    recommend,
    score,
    sibling_overlap,
    Record,
)

CFG = load_config()


def _rec(**kw) -> Record:
    base = dict(
        identifier="traitmech:000001",
        label="test trait",
        category="metabolism",
        slug="test_trait",
        term_kind="CLASS",
        mapping_status="REVIEWED",
        parents=[],
        edges=10,
        nodes=12,
        orphans=0,
        components=1,
        examples=2,
        edges_with_evidence=10,
        has_definition=True,
        has_definition_source=True,
        has_synonyms=True,
        has_evidence=True,
    )
    base.update(kw)
    return Record(**base)


def _act(rec: Record, *, children=0, series=None, series_size=0, overlap=0.0) -> str:
    return recommend(
        rec, CFG, children=children, series=series, series_size=series_size, overlap=overlap
    )


# --- the inverted lumping rule ----------------------------------------------


def test_series_do_not_lump_at_measured_overlap():
    """5% sibling overlap must NOT lump. This is the ported-and-inverted rule."""
    rec = _rec(label="temperature range mid4")
    assert _act(rec, series="temperature range", series_size=7, overlap=0.05) != "LUMP_INTO_PARENT"


def test_series_do_lump_when_siblings_genuinely_duplicate():
    """The rule is not disabled -- it is thresholded. Above the line it fires."""
    rec = _rec(label="temperature range mid4")
    assert _act(rec, series="temperature range", series_size=7, overlap=0.95) == "LUMP_INTO_PARENT"


def test_a_small_family_never_lumps_however_high_the_overlap():
    rec = _rec(label="temperature range mid4")
    assert _act(rec, series="temperature range", series_size=2, overlap=1.0) != "LUMP_INTO_PARENT"


def test_the_real_corpus_lumps_nothing_and_says_why():
    rows, meta = build_queue()
    assert meta["actions"]["LUMP_INTO_PARENT"] == 0
    assert meta["series_families"] >= 8, meta
    assert meta["mean_series_overlap"] < 0.2, (
        "sibling overlap rose sharply; the lumping decision needs re-examining, "
        f"not silently accepting: {meta['mean_series_overlap']}"
    )


# --- series detection --------------------------------------------------------


def test_family_stem_extracts_the_binned_stem():
    pats = CFG["heuristics"]["series_patterns"]
    assert family_stem("temperature range mid4", pats) == "temperature range"
    assert family_stem("pH delta very low", pats) == "pH delta"
    assert family_stem("NaCl optimum high", pats) == "NaCl optimum"


def test_family_stem_returns_none_for_a_standalone_trait():
    pats = CFG["heuristics"]["series_patterns"]
    for label in ("biopolymer degradation", "lithotrophic", "nitrogen-fixing symbiosis"):
        assert family_stem(label, pats) is None, label


def test_a_pattern_without_a_stem_group_cannot_group_silently():
    assert family_stem("temperature range mid4", [r"^temperature range mid\d$"]) is None


def test_sibling_overlap_is_mean_pairwise_jaccard():
    a = _rec(node_labels={"x", "y"})
    b = _rec(node_labels={"x", "y"})
    c = _rec(node_labels={"p", "q"})
    assert sibling_overlap([a, b]) == 1.0
    assert sibling_overlap([a, c]) == 0.0
    assert sibling_overlap([a]) == 0.0, "a single member has no pairs"


def test_jaccard_handles_empty_sets():
    assert jaccard(set(), {"a"}) == 0.0
    assert jaccard({"a"}, {"a"}) == 1.0


# --- the action ladder -------------------------------------------------------


def test_non_mechanism_records_drop_first():
    assert _act(_rec(term_kind="OBJECT_PROPERTY")) == "DROP_NON_MECHANISM"
    assert _act(_rec(term_kind="DATATYPE_PROPERTY")) == "DROP_NON_MECHANISM"
    assert _act(_rec(category="upper")) == "DROP_NON_MECHANISM"


def test_deprecated_drops_before_any_curation_advice():
    assert _act(_rec(mapping_status="DEPRECATED", edges=0, examples=0)) == "DROP_DEPRECATED"


def test_missing_graph_beats_missing_examples():
    """A record with neither needs the graph first."""
    assert _act(_rec(edges=0, examples=0)) == "BUILD_CAUSAL_GRAPH"


def test_a_graph_without_examples_asks_for_examples():
    assert _act(_rec(edges=10, examples=0)) == "ADD_CANONICAL_EXAMPLES"


def test_a_thin_or_fragmented_graph_asks_to_be_deepened():
    assert _act(_rec(edges=4, examples=1)) == "DEEPEN_CAUSAL_GRAPH"
    assert _act(_rec(edges=10, examples=1, components=3)) == "DEEPEN_CAUSAL_GRAPH"


def test_a_deep_record_is_marked_done():
    assert _act(_rec(edges=14, examples=3)) == "ALREADY_DEEP"


def test_grouping_labels_drop():
    assert _act(_rec(label="phenotype", category="metabolism")) == "DROP_GROUPING_TERM"


def test_is_grouping_term_matches_the_configured_patterns():
    pats = CFG["heuristics"]["grouping_term_patterns"]
    assert is_grouping_term("quality", pats)
    assert is_grouping_term("growth ph observation", pats)
    assert not is_grouping_term("biopolymer degradation", pats)


def test_every_emitted_action_is_declared():
    rows, _ = build_queue()
    assert {r["action"] for r in rows} <= set(ACTIONS)


# --- scoring -----------------------------------------------------------------


def test_missing_examples_outweighs_missing_synonyms():
    no_ex, _ = score(_rec(examples=0), CFG)
    no_syn, _ = score(_rec(has_synonyms=False), CFG)
    assert no_ex > no_syn


def test_non_mechanism_scores_to_the_floor_and_stops():
    s, why = score(_rec(term_kind="OBJECT_PROPERTY", edges=0, examples=0), CFG)
    assert s <= CFG["weights"]["non_mechanism"]
    assert len(why) == 1, "must short-circuit rather than accumulate curation debt"


def test_reasons_are_returned_so_the_score_is_arguable():
    _, why = score(_rec(edges=0, examples=0, has_synonyms=False), CFG)
    joined = " ".join(why)
    assert "no causal graph" in joined and "no canonical_examples" in joined


def test_components_and_orphans_are_capped():
    lots, _ = score(_rec(components=40, orphans=40), CFG)
    some, _ = score(_rec(components=6, orphans=6), CFG)
    assert lots == some, "uncapped, a pathological graph would dominate the queue"


def test_deep_records_are_deprioritised_not_hidden():
    deep, _ = score(_rec(edges=20, examples=5), CFG)
    thin, _ = score(_rec(edges=2, examples=0), CFG)
    assert deep < thin


# --- queue + meta ------------------------------------------------------------


def test_exclusions_are_counted_rather_than_dropped():
    """DisMech's sidecar lesson: an excluded row leaves no trace unless counted."""
    rows, meta = build_queue()
    assert meta["records"] == len(rows), "excluded records stay in the payload"
    assert meta["excluded_non_mechanism"] > 100
    assert meta["excluded_deprecated"] == 20


def test_queue_is_sorted_by_descending_score():
    rows, _ = build_queue()
    assert rows == sorted(rows, key=lambda x: (-x["score"], x["category"], x["slug"]))


def test_config_must_declare_all_four_sections(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text("weights: {}\n")
    try:
        load_config(bad)
    except ValueError as exc:
        assert "caps" in str(exc)
    else:
        raise AssertionError("a config missing 'caps' must be rejected")


# --- CLI row accounting (#452) ---


def _run(args: list[str]) -> str:
    import contextlib
    import io
    import sys as _sys

    from trait_priority import main

    argv = _sys.argv
    _sys.argv = ["trait_priority", *args]
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            main()
    finally:
        _sys.argv = argv
    return buf.getvalue()


def _row_count(out: str) -> int:
    import re as _re

    return len([ln for ln in out.splitlines() if _re.match(r"^ *-?[0-9]+ [A-Z_]+", ln)])


def test_top_zero_means_all_matching_the_sibling_tool():
    """`prioritize_graph_research.py --limit 0` means all; these must agree."""
    out = _run(["--top", "0"])
    assert _row_count(out) == 477


def test_the_footer_count_equals_the_rows_actually_printed():
    """The footer used to report the pre-slice list, so it claimed 477 and showed 0."""
    for top in ("3", "10", "0"):
        out = _run(["--top", top])
        printed = _row_count(out)
        stated = int(out.split("row(s) shown")[0].strip().split("\n")[-1])
        assert stated == printed, f"--top {top}: footer says {stated}, printed {printed}"


def test_action_filter_narrows_both_rows_and_the_stated_count():
    out = _run(["--action", "ALREADY_DEEP", "--top", "0"])
    printed = _row_count(out)
    assert printed == 9, printed
    assert f"{printed} row(s) shown of {printed} matching" in out
