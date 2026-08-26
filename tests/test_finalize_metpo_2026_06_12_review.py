from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from finalize_metpo_2026_06_12_review import (  # noqa: E402
    DUPLICATE_OF,
    REPORT,
    classify_pending,
    finalize,
    main,
    write_rows,
)
from seed_from_metpo import OWL_PATH, parse_owl  # noqa: E402


def _row(disposition: str, *, curie: str = "METPO:1", field: str = "entity"):
    return {
        "curie": curie,
        "change_type": "ADDED" if field == "entity" else "CHANGED",
        "field": field,
        "disposition": disposition,
    }


def test_active_properties_are_supporting_vocabulary_not_primary_records():
    row = _row("NOT_SEEDED_REVIEW_REQUIRED")
    disposition, rationale, related = classify_pending(
        row, {"METPO:1": {"term_kind": "DATATYPE_PROPERTY"}}
    )
    assert disposition == "SUPPORTING_FIELD_VOCABULARY"
    assert "supporting YAML" in rationale
    assert related == ""


def test_known_duplicate_points_to_the_existing_trait():
    row = _row("NOT_SEEDED_REVIEW_REQUIRED", curie="METPO:1005038")
    disposition, _, related = classify_pending(
        row, {"METPO:1005038": {"term_kind": "CLASS"}}
    )
    assert disposition == "DUPLICATE_NO_NEW_PRIMARY"
    assert related == "traitmech:000104"


def test_reviewed_local_fields_are_not_overwritten_by_source_drift():
    source = {"METPO:1000606": {"term_kind": "CLASS"}}
    definition = _row(
        "MEASURED_NO_AUTOMATIC_OVERWRITE",
        curie="METPO:1000606",
        field="definition",
    )
    parent = {**definition, "field": "parents"}
    assert classify_pending(definition, source)[0] == "RETAIN_CURATED_LOCAL_DEFINITION"
    assert classify_pending(parent, source)[0] == "RETAIN_CURATED_LOCAL_HIERARCHY"


def test_finalize_is_idempotent():
    rows = [_row("NOT_SEEDED_REVIEW_REQUIRED")]
    source = {"METPO:1": {"term_kind": "OBJECT_PROPERTY"}}
    counts, review, pending = finalize(rows, source)
    assert sum(counts.values()) == 1
    assert len(review) == 1
    assert pending == 1
    once = [dict(row) for row in rows]
    counts, review, pending = finalize(rows, source)
    assert sum(counts.values()) == 1
    assert len(review) == 1
    assert pending == 0
    assert rows == once


def test_cli_dry_run_does_not_rewrite_report(tmp_path):
    report = tmp_path / "delta.tsv"
    fieldnames = [
        "curie", "corpus_record", "source_status", "change_type", "field",
        "old_value", "new_value", "disposition",
    ]
    with report.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, delimiter="\t", fieldnames=fieldnames)
        writer.writeheader()
    before = report.read_bytes()
    assert main([
        "--report", str(report), "--review-report", str(tmp_path / "review.tsv")
    ]) == 0
    assert report.read_bytes() == before


def test_atomic_writer_removes_staging_file_on_install_failure(tmp_path, monkeypatch):
    destination = tmp_path / "review.tsv"

    def fail_replace(source, target):
        raise OSError("injected install failure")

    monkeypatch.setattr("finalize_metpo_2026_06_12_review.os.replace", fail_replace)
    with pytest.raises(OSError, match="injected install failure"):
        write_rows(destination, [{"column": "value"}], ["column"])
    assert list(tmp_path.iterdir()) == []


def test_live_inventory_is_fully_classified_and_primary_scope_is_respected():
    with REPORT.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    source = parse_owl(OWL_PATH)
    counts, review, pending = finalize(rows, source)
    assert pending == 0
    assert len(review) == 153
    assert counts == {
        "DUPLICATE_NO_NEW_PRIMARY": 17,
        "NO_CORPUS_DEMAND_NO_PRIMARY": 38,
        "OUT_OF_SCOPE_NON_TRAIT_ENTITY": 1,
        "RETAIN_CURATED_LOCAL_DEFINITION": 8,
        "RETAIN_CURATED_LOCAL_HIERARCHY": 8,
        "RETAIN_CURATED_LOCAL_SYNONYMS": 31,
        "RETAIN_LOCAL_TYPOGRAPHY_OR_GRAMMAR": 12,
        "SUPPORTING_FIELD_VOCABULARY": 38,
    }
    active_additions = [
        source[row["curie"]]
        for row in rows
        if row["change_type"] == "ADDED" and row["source_status"] == "ACTIVE"
    ]
    assert not [
        term["label"]
        for term in active_additions
        if term["term_kind"] == "CLASS"
        and {"gene", "operon"} & set(re.findall(r"[a-z]+", (term["label"] or "").casefold()))
    ]
    gene_count_terms = [
        term for term in active_additions if "gene count" in (term["label"] or "")
    ]
    assert len(gene_count_terms) == 2
    assert {term["term_kind"] for term in gene_count_terms} == {"DATATYPE_PROPERTY"}


def test_every_duplicate_target_exists_in_the_corpus():
    identifiers = set()
    for path in (REPO_ROOT / "data" / "traits").rglob("*.yaml"):
        for line in path.read_text().splitlines():
            if line.startswith("identifier: "):
                identifiers.add(line.removeprefix("identifier: "))
                break
    assert set(DUPLICATE_OF.values()) <= identifiers
