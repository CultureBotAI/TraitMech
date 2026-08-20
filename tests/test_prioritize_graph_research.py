"""Tests for the deep-research prioritiser.

The tests that matter here are the exclusion tests. The score is a heuristic and
can be argued with; the exclusions are the part that is either right or wrong,
and the first version of this script got them wrong in a way nothing would have
caught -- a hand-written list of slug prefixes matched 47 of the 94 predicate
records and silently ranked the other 47 as research candidates.

So `test_no_object_property_survives_the_filter` runs against the real corpus
rather than a fixture: a fixture would have passed for the broken version too.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from prioritize_graph_research import (  # noqa: E402
    family_of,
    non_mechanism_reason,
    rank,
    researched_slugs,
    score,
    stale_fraction,
)


# --- exclusions: decided by schema fields, not by name ---


def test_object_property_is_excluded():
    assert non_mechanism_reason("metabolism", {"term_kind": "OBJECT_PROPERTY"}) == "object_property"


def test_datatype_property_is_excluded():
    assert (
        non_mechanism_reason("quantitative_property", {"term_kind": "DATATYPE_PROPERTY"})
        == "datatype_property"
    )


def test_deprecated_class_is_excluded():
    doc = {"term_kind": "CLASS", "mapping_status": "DEPRECATED"}
    assert non_mechanism_reason("observation", doc) == "deprecated"


def test_upper_ontology_is_excluded_even_when_it_has_a_graph():
    """`quality` and `material_entity` carry thin graphs and rank high regardless."""
    doc = {"term_kind": "CLASS", "mapping_status": "REVIEWED"}
    assert non_mechanism_reason("upper", doc) == "upper_ontology"


def test_a_real_trait_is_not_excluded():
    doc = {"term_kind": "CLASS", "mapping_status": "REVIEWED"}
    assert non_mechanism_reason("metabolism", doc) is None


def test_slug_shape_does_not_decide_it():
    """`uses_for_growth` was missed by prefix matching; term_kind catches it.

    And the converse: a CLASS whose name merely looks like a relation must not be
    excluded, which is exactly what a prefix list could not distinguish.
    """
    predicate = {"term_kind": "OBJECT_PROPERTY", "mapping_status": "REVIEWED"}
    trait = {"term_kind": "CLASS", "mapping_status": "REVIEWED"}
    assert non_mechanism_reason("metabolism", predicate) == "object_property"
    assert non_mechanism_reason("metabolism", trait) is None


def test_no_object_property_survives_the_filter_on_the_real_corpus():
    """The regression that motivated the rewrite. Runs on the corpus deliberately."""
    import yaml

    rows, counts = rank(collapse_families=False)
    ranked = {(r["category"], r["slug"]) for r in rows}
    leaked = []
    for path in Path("data/traits").rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text())
        key = (path.parent.name, path.stem)
        if key in ranked and non_mechanism_reason(path.parent.name, doc):
            leaked.append("/".join(key))
    assert not leaked, f"non-mechanism records ranked as research candidates: {leaked}"


# --- binned series: reported, not merged (#447) ---


def test_binned_slugs_belong_to_their_family():
    assert family_of("ph_delta_mid2") == "ph_delta"
    assert family_of("temperature_range_very_low") == "temperature_range"
    assert family_of("nacl_optimum_high") == "nacl_optimum"
    assert family_of("cell_length_small") == "cell_length"


def test_standalone_traits_have_no_family():
    for slug in ("biopolymer_degradation", "lithotrophic", "nitrogen_fixing_symbiosis", "ph"):
        assert family_of(slug) is None, slug


def _ph_delta_corpus():
    return [
        (
            f"data/traits/environment/ph_delta_{bin}.yaml",
            {"term_kind": "CLASS", "causal_graphs": []},
        )
        for bin in ("low", "mid2", "high")
    ]


def test_default_keeps_every_bin_and_reports_the_series():
    """The #447 fix: sibling bins share 5% of their content, so each is its own
    work item. Membership is information on the row, not a merge."""
    rows, counts = rank(
        _ph_delta_corpus(), connectivity=Path("/nonexistent"), completeness=Path("/nonexistent")
    )
    assert len(rows) == 3, "bins must not merge by default"
    assert all(r["family"] == "ph_delta" for r in rows)
    assert all(r["series_size"] == 3 for r in rows)
    assert counts["in_series"] == 3
    assert counts["families_collapsed"] == 0


def test_explicit_collapse_keeps_the_worst_member_and_counts_the_rest():
    rows, counts = rank(
        _ph_delta_corpus(),
        connectivity=Path("/nonexistent"),
        completeness=Path("/nonexistent"),
        collapse_families=True,
    )
    assert len(rows) == 1, "three bins of one family should collapse to one row"
    assert rows[0]["family"] == "ph_delta"
    assert rows[0]["family_members"] == 3
    assert counts["families_collapsed"] == 2


# --- completeness-audit staleness (#443) ---


def _graphed_doc(edges: int) -> dict:
    nodes = [{"node_id": f"n{i}"} for i in range(edges + 1)]
    return {
        "term_kind": "CLASS",
        "causal_graphs": [
            {
                "nodes": nodes,
                "edges": [
                    {"subject": f"n{i}", "predicate": "p", "object": f"n{i + 1}"}
                    for i in range(edges)
                ],
            }
        ],
    }


def _completeness_tsv(tmp_path, rows: list[tuple[str, str, int, int]]) -> Path:
    path = tmp_path / "completeness.tsv"
    lines = ["category\tslug\tverdict\tpriority\tgraph_edges\tmissing_modules"]
    for category, slug, graph_edges, missing in rows:
        lines.append(f"{category}\t{slug}\tshallow\tmedium\t{graph_edges}\t{missing}")
    path.write_text("\n".join(lines) + "\n")
    return path


def _connectivity_tsv(tmp_path, file: str, wired_nodes: int) -> Path:
    path = tmp_path / "connectivity.tsv"
    path.write_text(
        "file\tgraph_id\twired_nodes\tcomponents\tlargest_component\tcomponent_sizes\n"
        f"{file}\tg\t{wired_nodes}\t1\t{wired_nodes}\t{wired_nodes}\n"
    )
    return path


def test_fresh_completeness_row_contributes_to_the_score(tmp_path):
    rel = "data/traits/ecology/biofilm_formation.yaml"
    corpus = [(rel, _graphed_doc(edges=8))]
    conn = _connectivity_tsv(tmp_path, rel, wired_nodes=9)
    comp = _completeness_tsv(tmp_path, [("ecology", "biofilm_formation", 8, 3)])
    rows, counts = rank(corpus, connectivity=conn, completeness=comp)
    (row,) = rows
    assert not row["completeness_stale"]
    assert row["score"] == 6, "missing_modules*2 should be in the score"
    assert counts["completeness_rows_stale"] == 0


def test_stale_completeness_row_is_reported_but_not_scored(tmp_path):
    """The graph grew since the audit ran, so the audit's verdict describes a
    graph that no longer exists. The number stays visible; the score ignores it."""
    rel = "data/traits/ecology/biofilm_formation.yaml"
    corpus = [(rel, _graphed_doc(edges=8))]
    conn = _connectivity_tsv(tmp_path, rel, wired_nodes=9)
    comp = _completeness_tsv(tmp_path, [("ecology", "biofilm_formation", 2, 6)])
    rows, counts = rank(corpus, connectivity=conn, completeness=comp)
    (row,) = rows
    assert row["completeness_stale"]
    assert row["missing_modules"] == 6, "still reported for the reader"
    assert row["score"] == 0, "but excluded from the score"
    assert counts["completeness_rows_stale"] == 1
    assert counts["completeness_rows_matched"] == 1


def test_stale_fraction_is_zero_when_nothing_matched():
    assert stale_fraction({"completeness_rows_matched": 0, "completeness_rows_stale": 0}) == 0.0


def test_stale_fraction_on_the_real_corpus_reflects_443():
    """347 of 353 audit rows no longer matched the corpus when #443 was filed,
    and the corpus only grows. If this ever drops to 0 the audit was regenerated
    and the guard on --sort missing stops firing -- which is the goal, not a bug."""
    _, counts = rank()
    assert stale_fraction(counts) > 0.5


# --- score ---


def test_missing_modules_are_weighted_double():
    assert score(missing_modules=1, orphans=0, components=1, edges=8) == 2
    assert score(missing_modules=0, orphans=2, components=1, edges=8) == 2


def test_fragmentation_costs_two_per_extra_component():
    assert score(0, 0, 1, 8) == 0
    assert score(0, 0, 4, 8) == 6


def test_thin_graphs_hit_the_edge_floor():
    """edges-per-node cannot see this: 1 edge/2 nodes ties 20 edges/40 nodes."""
    assert score(0, 0, 1, 1) == 7
    assert score(0, 0, 1, 20) == 0


def test_score_never_goes_negative_on_a_large_graph():
    assert score(0, 0, 0, 100) == 0


# --- research-artifact detection ---


def test_provider_suffix_is_stripped_so_two_providers_are_one_trait(tmp_path):
    cat = tmp_path / "ecology"
    cat.mkdir()
    (cat / "biofilm_formation-deep-research-falcon.md").write_text("x")
    (cat / "biofilm_formation-deep-research-openscientist.md").write_text("x")
    (cat / "aerobic-edison-literature-meta.yaml").write_text("x")
    found = researched_slugs(tmp_path)
    assert ("ecology", "biofilm_formation") in found
    assert ("ecology", "aerobic") in found
    assert len(found) == 2, found


def test_missing_research_dir_is_empty_not_an_error():
    assert researched_slugs(Path("/nonexistent")) == set()


def test_every_ranked_candidate_on_the_real_corpus_is_already_researched():
    """The headline finding, pinned: no trait awaits a FIRST research pass.

    If this ever fails, a genuinely unresearched mechanism trait has appeared and
    it should go to the front of the queue -- so the failure is the useful signal,
    not a nuisance.
    """
    rows, _ = rank()
    unresearched = [f"{r['category']}/{r['slug']}" for r in rows if not r["researched"]]
    assert not unresearched, f"unresearched mechanism traits now exist: {unresearched}"


# --- the content-vs-connective distinction ---


def test_fragmentation_and_missing_modules_are_separable_signals():
    """The distinction that decides whether to spend money on research.

    A fragmented graph with nothing missing is a CONNECTIVE gap (curate it); a
    coherent graph with modules missing is a CONTENT gap (research it). The
    composite score cannot tell them apart -- it can rank the connective one
    higher, which is why `--sort missing` exists.
    """
    connective = score(missing_modules=0, orphans=0, components=6, edges=8)
    content = score(missing_modules=5, orphans=0, components=1, edges=10)
    assert connective == 10
    assert content == 10, "the composite score cannot separate these two cases"


def test_real_corpus_has_both_shapes_at_the_top():
    """Guards the worked example in the skill against corpus drift."""
    rows, _ = rank()
    by_slug = {r["slug"]: r for r in rows}
    connective = by_slug["biopolymer_degradation"]
    content = by_slug["nitrogen_fixing_symbiosis"]
    # The lower-scoring trait is the better research target.
    assert connective["score"] > content["score"]
    assert connective["components"] > content["components"]
    assert content["missing_modules"] > connective["missing_modules"]
    assert content["components"] == 1 and content["orphans"] == 0


# --- the numbers the skill states in prose ---

# .claude/skills/prioritize-graph-research/SKILL.md quotes each of these as fact.
# Prose that preserves a stale measurement is worse than prose that points at the
# command, and nothing else fails when the corpus moves -- so this test is the
# mechanism that keeps the skill honest, and its failure message has to say so
# (#429). Same defect class as the #410 history record that kept asserting a
# premise the review had already refuted.
SKILL_DOC = Path(".claude/skills/prioritize-graph-research/SKILL.md")
EXPECTED_COMPOSITION = {
    "object_property": 94,
    "datatype_property": 7,
    "deprecated": 20,
    "upper_ontology": 8,
    "non_mechanism": 129,
    # 55 rows across 11 binned series, none merged (#447). The old default
    # collapsed them to 11 rows and reported `families_collapsed: 44`.
    "in_series": 55,
    "families_collapsed": 0,
}


def test_corpus_composition_matches_what_the_skill_claims():
    _, counts = rank()
    # Totals are top-level keys; per-reason counts are prefixed `excluded_`.
    direct = {"non_mechanism", "families_collapsed", "in_series"}
    actual = {
        k: counts[k] if k in direct else counts.get(f"excluded_{k}", 0)
        for k in EXPECTED_COMPOSITION
    }
    drifted = {
        k: (EXPECTED_COMPOSITION[k], v) for k, v in actual.items() if v != EXPECTED_COMPOSITION[k]
    }
    assert not drifted, (
        f"corpus composition changed (expected, actual): {drifted}. "
        f"Update EXPECTED_COMPOSITION here AND the prose in {SKILL_DOC}, which "
        f"quotes these counts as fact -- the module docstring of "
        f"scripts/prioritize_graph_research.py quotes them too."
    )


def test_the_skill_doc_exists_and_names_the_recipe_it_documents():
    """A skill that cites a recipe name is only useful while the recipe exists."""
    assert SKILL_DOC.exists()
    text = SKILL_DOC.read_text()
    assert "just prioritize-research" in text
    assert "prioritize-research" in Path("justfile").read_text()
