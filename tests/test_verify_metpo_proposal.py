"""Regression tests for scripts/verify_metpo_proposal.py's Scope-A check.

Locks in the #318 contract: a cohort that ships no classes template is not
doing Scope A, so the check must skip rather than treat every `traitmech:` id
in the corpus as uncited. Before the fix, `class_tsv_text` was `""` for such a
cohort and `i not in ""` was true for every id, so every predicate-only cohort
(v2, v4, v6) failed the skill's required verification step.

What the check asserts changed in #319: whole-corpus coverage was a
CROSS-cohort property that no single cohort owns, so demanding it of every
cohort failed v1/v3/v7 permanently over work they never took on. The
per-cohort property it asserts instead is that a cited id RESOLVES, which
also catches a typo the old rule could not see.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import verify_metpo_proposal as vmp  # noqa: E402


def property_rows(width):
    # Headers match kg-microbe 1408e7099d039026d7611c240938d8e177753406.
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "type", "domain",
         "range", "synonyms", "xrefs", "subset", "priority", "traits_addressed", "observations"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "TYPE", "DOMAIN", "RANGE",
         "A oboInOwl:hasRelatedSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        ["METPO:2007400", "test relation", "A test relation.", "DOI:10.1234/test",
         "owl:ObjectProperty", "METPO:1000525", "METPO:1000059", "alias one|alias two",
         "", "metpo_traitmech_2026_10", "", "test", "0"],
    ]
    if width == 12:
        for row in rows:
            del row[7]
    return rows


def write_template(path, rows):
    with path.open("w", newline="") as stream:
        csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)


@pytest.mark.parametrize("width", [12, 13])
@pytest.mark.parametrize("defect", [None, "short_row", "xref", "subset_header", "empty_subset"])
def test_property_layout_end_to_end(tmp_path, monkeypatch, capsys, width, defect):
    rows = property_rows(width)
    subset_column = width - 4
    if defect == "short_row":
        rows[2].pop()
    elif defect == "xref":
        rows[1][subset_column - 1] = ""
    elif defect == "subset_header":
        rows[1][subset_column] = ""
    elif defect == "empty_subset":
        rows[2][subset_column] = ""
    write_template(tmp_path / "metpo_proposal_properties_robot.tsv", rows)
    monkeypatch.setattr(sys, "argv", ["verify", str(tmp_path), "--skip-scope-a", "--skip-scope-c"])
    assert vmp.main() == (0 if defect is None else 1)
    errors = capsys.readouterr().err
    if defect == "empty_subset":
        assert "empty subset tag" in errors
    elif defect == "short_row":
        assert f"expected {width}" in errors


@pytest.mark.parametrize("directive", ["", "A oboInOwl:hasExactSynonym SPLIT=|",
                                      "A oboInOwl:hasRelatedSynonym"])
def test_property_related_synonyms_need_correct_split_directive(tmp_path, monkeypatch, directive):
    rows = property_rows(13)
    rows[1][7] = directive
    write_template(tmp_path / "metpo_proposal_properties_robot.tsv", rows)
    monkeypatch.setattr(sys, "argv", ["verify", str(tmp_path), "--skip-scope-a", "--skip-scope-c"])
    assert vmp.main() == 1


@pytest.mark.parametrize("width", [12, 13])
def test_property_class_subset_mismatch_is_rejected(tmp_path, monkeypatch, capsys, width):
    write_template(tmp_path / "metpo_proposal_properties_robot.tsv", property_rows(width))
    write_template(tmp_path / "metpo_proposal_classes_robot.tsv", [
        ["proposed_id", "label", "definition", "definition_source", "parent", "synonyms",
         "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        ["METPO:1007400", "test class", "A test class.", "DOI:10.1234/test",
         "METPO:1000059", "", "", "metpo_traitmech_2026_09", "", "", "test"],
    ])
    monkeypatch.setattr(sys, "argv", ["verify", str(tmp_path), "--skip-scope-a", "--skip-scope-c"])
    assert vmp.main() == 1
    assert "subset tag mismatch between classes" in capsys.readouterr().err


def test_class_width_is_fixed_by_header_row():
    rows = [
        [""] * 12,
        [""] * 12,
        [""] * 11,
    ]
    failures: list[str] = []

    width = vmp.check_columns(rows, vmp.CLASS_COLS, "classes", failures)

    assert width == 12
    assert failures == ["classes row 3 has 11 cols, expected 12"]


def test_twelve_column_class_header_checks_related_synonym_directive():
    rows = [
        [""] * 12,
        [
            "ID",
            "LABEL",
            "A IAO:0000115",
            ">A IAO:0000119",
            "SC %",
            "A oboInOwl:hasExactSynonym SPLIT=|",
            "A oboInOwl:hasDbXref SPLIT=|",
            "A oboInOwl:inSubset",
            "",
            "",
            "",
            "",
        ],
    ]
    failures: list[str] = []

    vmp.check_robot_header(
        rows,
        vmp.class_robot_header_requirements(12),
        "classes",
        failures,
    )

    assert failures == [
        "classes header row 2 col 11 = '', expected to contain "
        "'A oboInOwl:hasRelatedSynonym'",
    ]


def test_read_tsv_allows_missing_final_related_synonym_cell(tmp_path):
    path = tmp_path / "metpo_proposal_classes_robot.tsv"
    path.write_text(
        "\t".join(
            [
                "proposed_id",
                "label",
                "definition",
                "definition_source",
                "parent",
                "synonyms",
                "xrefs",
                "subset",
                "priority",
                "observations",
                "traits_addressed",
                "related_synonyms",
            ]
        )
        + "\n"
        + "\t".join(
            [
                "ID",
                "LABEL",
                "A IAO:0000115",
                ">A IAO:0000119",
                "SC %",
                "A oboInOwl:hasExactSynonym SPLIT=|",
                "A oboInOwl:hasDbXref SPLIT=|",
                "A oboInOwl:inSubset",
                "",
                "",
                "",
                "A oboInOwl:hasRelatedSynonym SPLIT=|",
            ]
        )
        + "\n"
        + "\t".join(
            [
                "METPO:1045200",
                "Toga system",
                "A phage defense system.",
                "DOI:10.1093/nar/gkag898",
                "METPO:1016300",
                "Toga",
                "",
                "metpo_traitmech_2026_09",
                "HIGH",
                "no related synonym cell",
                "traitmech:000498",
            ]
        )
        + "\n"
    )

    rows = vmp._read_tsv(path)
    failures: list[str] = []

    width = vmp.check_columns(rows, vmp.CLASS_COLS, "classes", failures)

    assert width == 12
    assert rows[2][-1] == ""
    assert failures == []


def _corpus(tmp_path: Path, *ids: str) -> Path:
    """A stand-in data/traits/ holding one YAML per synthetic id."""
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    for i, ident in enumerate(ids):
        (d / f"t{i}.yaml").write_text(f"identifier: {ident}\nlabel: t{i}\n")
    return d


def test_scope_a_skips_when_cohort_has_no_classes_template(tmp_path, monkeypatch):
    """#318: a predicate-only cohort must not be judged against Scope A."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a("", failures)
    assert failures == []


def test_not_citing_every_corpus_id_is_not_a_failure(tmp_path, monkeypatch):
    """#319: whole-corpus coverage is a CROSS-cohort property.

    v1/v3/v7 lift causal-graph scaffolding, not synthetic traits, and failed
    permanently over a backlog they never took on. Cohort v5 carries all 120,
    so the coverage exists -- just not in every cohort.
    """
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tsome class\t...\n", failures)
    assert failures == []


def test_a_phantom_citation_fails(tmp_path, monkeypatch):
    """The property that IS per-cohort: a cited id must resolve.

    Catches a typo, or a citation left behind after a record was renamed or
    removed -- which the old whole-corpus rule could not see, since it only
    looked for absences in the other direction.
    """
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tc\tdef\tTraitMech:traitmech:999999\n", failures)
    assert len(failures) == 1
    assert "traitmech:999999" in failures[0]


def test_scope_a_passes_when_the_id_is_cited(tmp_path, monkeypatch):
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    vmp.check_scope_a(
        "METPO:1007400\tc\tdef\tTraitMech:traitmech:000001\n", failures)
    assert failures == []


def test_a_longer_cited_id_is_not_confused_with_a_shorter_real_one(tmp_path, monkeypatch):
    """#321: the coverage test must match whole ids, not substrings.

    `traitmech:000001 not in "...traitmech:0000010..."` is False, so the shorter
    id read as covered and the check could report full Scope-A coverage while
    that term was genuinely un-lifted. A coverage gate that passes when it should
    fail is worse than no gate.
    """
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path, "traitmech:000001"))
    failures: list[str] = []
    # traitmech:0000010 is cited but does not exist; a substring scan would have
    # matched it against the real traitmech:000001 and reported nothing (#321).
    vmp.check_scope_a("METPO:1007400\tc\tdef\tTraitMech:traitmech:0000010\n", failures)
    assert len(failures) == 1
    assert "traitmech:0000010" in failures[0]


def test_scope_a_is_silent_on_an_empty_corpus(tmp_path, monkeypatch):
    """No synthetic ids at all — nothing to cover, whatever the cohort ships."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus(tmp_path))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tc\n", failures)
    assert failures == []


# --- the two behaviours added in #319, which shipped canaried but untested ----
#
# Both were verified by hand and neither had a test, which is the same gap the
# #337 review named: a manual canary proves it worked once; a test is what fails
# when someone changes it later.


def _corpus_files(tmp_path, **files):
    d = tmp_path / "traits"
    d.mkdir(exist_ok=True)
    for name, body in files.items():
        (d / f"{name}.yaml").write_text(body)
    return d


def test_an_id_parked_in_synonyms_still_resolves(tmp_path, monkeypatch):
    """The partial-mint case (#349 review).

    The skill's round-trip plan swaps `identifier:` to the minted METPO CURIE and
    PRESERVES the old id in `synonyms:`. Reading only `identifier:` made a
    half-finished mint produce phantom failures against an already-submitted
    cohort that still cites all of them.
    """
    # A PARTIAL mint, which is the case that actually breaks. With every record
    # minted, `ids` empties and check_scope_a returns early, so an
    # identifier-only reader would pass for the wrong reason -- the first cut of
    # this test did exactly that and survived the canary.
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus_files(
        tmp_path,
        minted="identifier: METPO:9999999\nsynonyms:\n- synonym_text: traitmech:000001\n",
        unminted="identifier: traitmech:000002\n"))
    failures: list[str] = []
    vmp.check_scope_a(
        "METPO:1007400\tc\tdef\tTraitMech:traitmech:000001|traitmech:000002\n",
        failures)
    assert failures == []


def test_an_id_in_no_record_at_all_still_fails(tmp_path, monkeypatch):
    """Widening where ids are read must not make the check unfalsifiable."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus_files(
        tmp_path, t="identifier: traitmech:000001\n"))
    failures: list[str] = []
    vmp.check_scope_a("METPO:1007400\tc\tdef\tTraitMech:traitmech:000002\n", failures)
    assert len(failures) == 1 and "traitmech:000002" in failures[0]


def test_cohort_coverage_unions_across_cohorts(tmp_path, monkeypatch):
    """The cross-cohort property: one cohort covering an id is enough."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus_files(
        tmp_path, t="identifier: traitmech:000001\nx: traitmech:000002\n"))
    props = tmp_path / "proposals"
    (props / "v1").mkdir(parents=True)
    (props / "v2").mkdir(parents=True)
    (props / "v1" / "metpo_proposal_classes_robot.tsv").write_text("x\ttraitmech:000001\n")
    (props / "v2" / "metpo_proposal_classes_robot.tsv").write_text("x\ttraitmech:000002\n")
    cited, uncovered = vmp.cohort_coverage(props)
    assert cited == {"traitmech:000001", "traitmech:000002"}
    assert uncovered == set()


def test_cohort_coverage_reports_an_id_no_cohort_lifts(tmp_path, monkeypatch):
    """The obligation #319 would otherwise have closed with nothing tracking it:
    mint a new synthetic id and something must notice."""
    monkeypatch.setattr(vmp, "TRAITS_DIR", _corpus_files(
        tmp_path, t="identifier: traitmech:000121\n"))
    props = tmp_path / "proposals"
    (props / "v5").mkdir(parents=True)
    (props / "v5" / "metpo_proposal_classes_robot.tsv").write_text("x\ttraitmech:000001\n")
    _cited, uncovered = vmp.cohort_coverage(props)
    assert uncovered == {"traitmech:000121"}
