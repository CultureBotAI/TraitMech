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
    assert counts["non_mechanism"] == 129, counts


# --- family collapsing ---


def test_binned_slugs_collapse_to_their_family():
    assert family_of("ph_delta_mid2") == "ph_delta"
    assert family_of("temperature_range_very_low") == "temperature_range"
    assert family_of("nacl_optimum_high") == "nacl_optimum"
    assert family_of("cell_length_small") == "cell_length"


def test_standalone_traits_have_no_family():
    for slug in ("biopolymer_degradation", "lithotrophic", "nitrogen_fixing_symbiosis", "ph"):
        assert family_of(slug) is None, slug


def test_collapsing_keeps_the_worst_member_and_counts_the_rest():
    corpus = [
        (f"data/traits/environment/ph_delta_{bin}.yaml", {"term_kind": "CLASS", "causal_graphs": []})
        for bin in ("low", "mid2", "high")
    ]
    rows, counts = rank(corpus, connectivity=Path("/nonexistent"), completeness=Path("/nonexistent"))
    assert len(rows) == 1, "three bins of one family should collapse to one row"
    assert rows[0]["family"] == "ph_delta"
    assert rows[0]["family_members"] == 3
    assert counts["families_collapsed"] == 2


def test_no_collapse_keeps_every_bin():
    corpus = [
        (f"data/traits/environment/ph_delta_{bin}.yaml", {"term_kind": "CLASS", "causal_graphs": []})
        for bin in ("low", "mid2", "high")
    ]
    rows, _ = rank(
        corpus,
        connectivity=Path("/nonexistent"),
        completeness=Path("/nonexistent"),
        collapse_families=False,
    )
    assert len(rows) == 3


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
