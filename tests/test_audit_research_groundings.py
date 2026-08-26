"""Unit tests for scripts/audit_research_groundings.py.

The ontology lookups need OAK semsql databases, so these exercise the parts that
decide WHAT gets looked up and HOW a result is judged — the extraction from
markdown tables and the verdict logic — with the adapter stubbed. Those are also
where the defects were: the first pass swept up fatty-acid shorthand (`C16:0`)
as 78 bogus findings, and lumped lexical variants in with real mis-groundings.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_research_groundings import (  # noqa: E402
    classify,
    similarity,
    table_pairs,
)


def _curies(text: str) -> list[str]:
    return [curie for _, _, curie, _ in table_pairs(text)]


def test_extracts_the_label_and_curie_from_a_table_row():
    rows = table_pairs("| infection thread | `GO:0009860` where applicable | note |")
    assert rows == [(1, "infection thread", "GO:0009860",
                     "| infection thread | `GO:0009860` where applicable | note |")]


@pytest.mark.parametrize("line", [
    # Fatty-acid shorthand. Allowing digits in the prefix made these 78 bogus
    # UNKNOWN_PREFIX findings that buried the real ones.
    "| membrane fluidity | C16:0 and C18:1 acyl-ACP | note |",
    "| growth | shifts at 37:13 ratio | note |",
])
def test_non_curie_colon_notation_is_not_extracted(line):
    assert _curies(line) == []


def test_header_separator_rows_are_skipped():
    assert _curies("|---|---|\n|:--|--:|") == []


def test_prose_outside_a_table_is_ignored():
    assert _curies("The node grounds to GO:0009860 in most taxa.") == []


def test_a_curie_repeated_in_one_row_is_counted_once():
    assert _curies("| x | `GO:0009860` — see GO:0009860 | note |") == ["GO:0009860"]


def test_multiple_distinct_curies_in_a_row_are_all_kept():
    assert _curies("| x | `GO:0009860` or CHEBI:15378 | note |") == [
        "GO:0009860", "CHEBI:15378"]


# --- verdicts -----------------------------------------------------------

def _resolved(label, synonyms=(), obsolete=False):
    return (label, list(synonyms), obsolete)


def test_matching_canonical_label_is_ok():
    verdict, canonical, _, _ = classify("pollen tube growth", "| row |",
                                        _resolved("pollen tube growth"))
    assert (verdict, canonical) == ("OK_LABEL", "pollen tube growth")


def test_matching_a_synonym_is_ok():
    verdict, _, _, _ = classify("calvin cycle", "| row |",
                                _resolved("reductive pentose-phosphate cycle",
                                          ["Calvin cycle"]))
    assert verdict == "OK_LABEL"


def test_naming_the_term_elsewhere_in_the_row_is_not_a_mis_grounding():
    """`| symbiosome | GO:0043663 (host cell part) is too broad |` is careful, not wrong."""
    verdict, _, _, _ = classify(
        "symbiosome",
        "| symbiosome | `GO:0043663` (host cell part) is too broad | note |",
        _resolved("host cell part"))
    assert verdict == "OK_IN_ROW"


def test_an_unrelated_label_is_drift():
    verdict, canonical, score, _ = classify(
        "ectoine", "| ectoine | CHEBI:10357 |",
        _resolved("(-)-beta-caryophyllene")
    )
    assert verdict == "DRIFT"
    assert canonical == "(-)-beta-caryophyllene"
    # No absolute threshold: character-level similarity between two unrelated
    # chemical names is not near zero (this pair scores 0.42), and the report
    # never compares the score to a cutoff. What it relies on is the ORDERING,
    # asserted in test_a_lexical_variant_scores_above_a_wholesale_mismatch.
    assert score == pytest.approx(similarity("ectoine", ["(-)-beta-caryophyllene"]))


def test_an_obsolete_term_is_flagged_even_when_the_label_matches():
    # GO:0009405 "pathogenesis" is obsolete; the label agrees, and that is
    # exactly why a label-only check would miss it.
    verdict, _, _, _ = classify("pathogenesis", "| row |",
                                _resolved("obsolete pathogenesis", obsolete=True))
    assert verdict == "OBSOLETE"


def test_an_unresolvable_id_is_not_silently_dropped():
    assert classify("ectoine", "| row |", None)[0] == "UNRESOLVED"


def test_a_merged_term_carries_its_successor_curie_and_label():
    from audit_research_groundings import MergedTerm

    resolved = MergedTerm((("GO:1902600", "proton transmembrane transport"),))
    assert classify("proton transport", "| row |", resolved) == (
        "MERGED", "proton transmembrane transport", 0.0, "GO:1902600"
    )


def test_a_lexical_variant_scores_above_a_wholesale_mismatch():
    """The ordering the report depends on: real errors must sort above variants."""
    variant = similarity("fumarate", ["fumaric acid"])
    wrong = similarity("ectoine", ["(-)-beta-caryophyllene"])
    assert variant > wrong
    assert similarity("10-formyl-tetrahydrofolate",
                      ["10-formyltetrahydrofolic acid"]) > wrong


# --- regressions from the #260 review -----------------------------------

def test_adapter_failure_is_not_reported_as_a_missing_id():
    """A broken toolchain must not read as a catastrophic corpus finding (#262)."""
    from audit_research_groundings import ADAPTER_ERROR
    assert classify("ectoine", "| row |", ADAPTER_ERROR)[0] == "ADAPTER_ERROR"
    assert classify("ectoine", "| row |", None)[0] == "UNRESOLVED"


def test_lowercase_prefixes_resolve_to_the_same_bucket_as_uppercase():
    """`doi:10...` sent 25 truncated citation fragments into the backlog (#261)."""
    from audit_research_groundings import _ADAPTERS_CF, _NO_ADAPTER_CF
    for prefix in ("doi", "DOI", "metpo", "METPO", "NCBITaxon", "ncbitaxon"):
        assert prefix.casefold() in _NO_ADAPTER_CF
    for prefix in ("go", "GO", "chebi", "CHEBI"):
        assert prefix.casefold() in _ADAPTERS_CF


def test_obsolete_outranks_drift_in_triage_order():
    """OBSOLETE scored 1.0 and an ascending sort buried all 39 of them (#264)."""
    from audit_research_groundings import VERDICT_RANK
    assert VERDICT_RANK["ADAPTER_ERROR"] < VERDICT_RANK["MERGED"]
    assert VERDICT_RANK["MERGED"] < VERDICT_RANK["UNRESOLVED"]
    assert VERDICT_RANK["UNRESOLVED"] < VERDICT_RANK["OBSOLETE"]
    assert VERDICT_RANK["OBSOLETE"] < VERDICT_RANK["DRIFT"]
    # The score must not re-bury it: an obsolete term's label often MATCHES.
    assert classify("pathogenesis", "| row |",
                    _resolved("obsolete pathogenesis", obsolete=True))[2] == 0.0


def test_the_backlog_artifact_exists_and_is_ranked():
    """The deliverable is the file, not the console summary (#263)."""
    backlog = REPO_ROOT / "reports" / "research_grounding_backlog.tsv"
    assert backlog.exists(), "run `just report-research-groundings`"
    lines = [ln for ln in backlog.read_text().splitlines() if ln and not ln.startswith("#")]
    header, rows = lines[0].split("\t"), [ln.split("\t") for ln in lines[1:]]
    assert header[:2] == ["verdict", "curie"]
    assert rows, "backlog is empty"
    from audit_research_groundings import VERDICT_RANK
    ranks = [VERDICT_RANK.get(r[0], 9) for r in rows]
    assert ranks == sorted(ranks), "backlog is not ranked by verdict"


def test_the_backlog_records_known_go_merges_with_successors():
    """The committed deliverable preserves the concrete #266 regressions."""
    backlog = REPO_ROOT / "reports" / "research_grounding_backlog.tsv"
    lines = [ln for ln in backlog.read_text().splitlines()
             if ln and not ln.startswith("#")]
    records = list(csv.DictReader(lines, delimiter="\t"))
    replacements = {
        (row["curie"], row["replacement_curie"])
        for row in records if row["verdict"] == "MERGED"
    }
    assert ("GO:0009878", "GO:0009877") in replacements
    assert ("GO:0015992", "GO:1902600") in replacements


def test_an_empty_adapter_is_an_error_not_1200_missing_ids():
    """A 0-byte semsql opens cleanly and labels nothing — the #265 case."""
    from audit_research_groundings import ADAPTER_ERROR, Ontologies

    class EmptyAdapter:
        def entities(self):
            return iter(())

        def label(self, curie):
            return None

    pool = Ontologies()
    pool._adapters["go"] = EmptyAdapter()
    assert pool.lookup("GO:0009860") is ADAPTER_ERROR


def test_a_probe_that_raises_is_not_treated_as_empty():
    """A partially-migrated live ontology must not be masked as a benign stub."""
    from audit_research_groundings import Ontologies

    class BrokenProbe:
        def entities(self):
            raise RuntimeError("no such table: node")

        def label(self, curie):
            return "pollen tube growth"

        def entity_aliases(self, curie):
            return []

        def entity_metadata_map(self, curie):
            return {}

    pool = Ontologies()
    pool._adapters["go"] = BrokenProbe()
    assert pool.lookup("GO:0009860")[0] == "pollen tube growth"


def test_absent_term_uses_oak_term_replaced_by_relationship():
    from audit_research_groundings import MergedTerm, Ontologies

    class MergedAdapter:
        def entities(self):
            return iter(["GO:1902600"])

        def label(self, curie):
            return {"GO:1902600": "proton transmembrane transport"}.get(curie)

        def obsoletes_migration_relationships(self, curies):
            assert list(curies) == ["GO:0015992"]
            return iter([("GO:0015992", "IAO:0100001", "GO:1902600")])

    pool = Ontologies()
    pool._adapters["go"] = MergedAdapter()
    assert pool.lookup("GO:0015992") == MergedTerm(
        (("GO:1902600", "proton transmembrane transport"),)
    )


def test_absent_term_does_not_treat_consider_as_a_replacement():
    from audit_research_groundings import Ontologies

    class ConsiderAdapter:
        def entities(self):
            return iter(["GO:1902600"])

        def label(self, curie):
            return None

        def obsoletes_migration_relationships(self, curies):
            return iter([("GO:0015992", "oboInOwl:consider", "GO:1902600")])

    pool = Ontologies()
    pool._adapters["go"] = ConsiderAdapter()
    assert pool.lookup("GO:0015992") is None
