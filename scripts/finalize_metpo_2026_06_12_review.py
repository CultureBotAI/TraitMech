#!/usr/bin/env python3
"""Finalize review dispositions for active METPO 2026-06-12 drift (#534).

The release-delta inventory created by #515 deliberately left active additions
and non-target field changes pending. This dry-run-by-default command classifies
all 153 pending rows without creating TraitRecords or overwriting reviewed local
content. ``--apply`` updates the inventory and writes a compact companion table
containing rationale and related TraitRecord CURIEs.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

from seed_from_metpo import OWL_PATH, parse_owl

ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "reports" / "metpo_2026_06_12_release_delta.tsv"
REVIEW_REPORT = ROOT / "reports" / "metpo_2026_06_12_active_review.tsv"
BASE_FIELDS = [
    "curie", "corpus_record", "source_status", "change_type", "field",
    "old_value", "new_value", "disposition",
]
REVIEW_FIELDS = [
    "curie", "change_type", "field", "disposition", "related_trait", "rationale",
]
PENDING_ADDITION = "NOT_SEEDED_REVIEW_REQUIRED"
PENDING_FIELD = "MEASURED_NO_AUTOMATIC_OVERWRITE"

# A new upstream CURIE does not authorize a second primary record. These terms
# are exact or close lexical/semantic matches to existing reviewed records; a
# future explicit identifier migration can reconsider them without duplicating
# the catalog now.
DUPLICATE_OF = {
    "METPO:1005031": "traitmech:000060",  # peritrichous
    "METPO:1005033": "traitmech:000059",  # amphitrichous
    "METPO:1005034": "traitmech:000058",  # lophotrichous
    "METPO:1005035": "traitmech:000057",  # monotrichous
    "METPO:1005038": "traitmech:000104",  # denitrification
    "METPO:1005039": "traitmech:000103",  # nitrogen fixation
    "METPO:1007005": "traitmech:000056",  # flagellar arrangement
    "METPO:1007070": "traitmech:000003",  # piezotolerant
    "METPO:1007071": "traitmech:000001",  # piezophilic
    "METPO:1007072": "traitmech:000007",  # radiotolerant
    "METPO:1007074": "traitmech:000012",  # metal tolerant
    "METPO:1007076": "traitmech:000063",  # capsule
    "METPO:1007077": "traitmech:000053",  # biofilm formation
    "METPO:1007083": "traitmech:000075",  # catalase activity
    "METPO:1007085": "traitmech:000076",  # oxidase activity
    "METPO:1007087": "traitmech:000077",  # urease activity
    "METPO:1007092": "traitmech:000011",  # xerophilic
}

# These definition changes are semantic rewrites paired with source hierarchy
# changes. Local records are REVIEWED and cite their own definition sources, so
# the review decision is to retain them rather than treat upstream text as a
# mechanical patch.
SEMANTIC_DEFINITION_CHANGES = {
    "METPO:1000606",
    "METPO:1000607",
    "METPO:1000623",
    "METPO:1000625",
    "METPO:1000628",
    "METPO:1000721",
    "METPO:1002005",
    "METPO:1003006",
}

ADDITION_DISPOSITIONS = {
    "SUPPORTING_FIELD_VOCABULARY",
    "OUT_OF_SCOPE_NON_TRAIT_ENTITY",
    "DUPLICATE_NO_NEW_PRIMARY",
    "NO_CORPUS_DEMAND_NO_PRIMARY",
}
FIELD_DISPOSITIONS = {
    "RETAIN_CURATED_LOCAL_SYNONYMS",
    "RETAIN_CURATED_LOCAL_HIERARCHY",
    "RETAIN_CURATED_LOCAL_DEFINITION",
    "RETAIN_LOCAL_TYPOGRAPHY_OR_GRAMMAR",
}


def classify_pending(
    row: dict[str, str], source: dict[str, dict[str, Any]]
) -> tuple[str, str, str]:
    """Return final disposition, rationale, and related TraitRecord CURIE."""
    curie = row["curie"]
    pending = row["disposition"]
    if pending == PENDING_ADDITION or pending in ADDITION_DISPOSITIONS:
        term = source[curie]
        kind = term["term_kind"]
        if kind in {"DATATYPE_PROPERTY", "OBJECT_PROPERTY"}:
            return (
                "SUPPORTING_FIELD_VOCABULARY",
                f"{kind} may describe supporting YAML values or relations; it is not a primary trait entry",
                "",
            )
        if curie == "METPO:1004005":
            return (
                "OUT_OF_SCOPE_NON_TRAIT_ENTITY",
                "growth medium is a material entity, not a microbial trait",
                "",
            )
        if curie in DUPLICATE_OF:
            return (
                "DUPLICATE_NO_NEW_PRIMARY",
                "new source CURIE overlaps an existing reviewed TraitRecord; do not create a duplicate",
                DUPLICATE_OF[curie],
            )
        if kind == "CLASS":
            return (
                "NO_CORPUS_DEMAND_NO_PRIMARY",
                "ontology membership alone is insufficient; no evidence-backed corpus need was supplied",
                "",
            )
        raise ValueError(f"{curie}: unhandled active addition kind {kind!r}")

    if pending == PENDING_FIELD or pending in FIELD_DISPOSITIONS:
        field = row["field"]
        if field == "synonyms":
            return (
                "RETAIN_CURATED_LOCAL_SYNONYMS",
                "source additions are redundant, overly broad, rotated bin aliases, or typography-only changes",
                curie,
            )
        if field == "parents":
            return (
                "RETAIN_CURATED_LOCAL_HIERARCHY",
                "changing a reviewed local hierarchy is an inference change, not a mechanical source refresh",
                curie,
            )
        if field == "definition" and curie in SEMANTIC_DEFINITION_CHANGES:
            return (
                "RETAIN_CURATED_LOCAL_DEFINITION",
                "local reviewed definition retains its evidence scope; upstream semantic rewrite is not auto-authoritative",
                curie,
            )
        if field == "definition":
            return (
                "RETAIN_LOCAL_TYPOGRAPHY_OR_GRAMMAR",
                "source change removes scientific typography or introduces no semantic improvement",
                curie,
            )
        raise ValueError(f"{curie}: unhandled pending field {field!r}")
    raise ValueError(f"{curie}: row is not pending review: {pending!r}")


def finalize(
    rows: list[dict[str, str]], source: dict[str, dict[str, Any]]
) -> tuple[Counter[str], list[dict[str, str]], int]:
    counts: Counter[str] = Counter()
    review_rows: list[dict[str, str]] = []
    pending_count = 0
    for row in rows:
        current = row["disposition"]
        if current not in {
            PENDING_ADDITION,
            PENDING_FIELD,
            *ADDITION_DISPOSITIONS,
            *FIELD_DISPOSITIONS,
        }:
            continue
        disposition, rationale, related = classify_pending(row, source)
        if current in {PENDING_ADDITION, PENDING_FIELD}:
            pending_count += 1
        elif current != disposition:
            raise ValueError(
                f"{row['curie']} {row['field']}: recorded {current!r}, expected {disposition!r}"
            )
        row["disposition"] = disposition
        counts[disposition] += 1
        review_rows.append({
            "curie": row["curie"],
            "change_type": row["change_type"],
            "field": row["field"],
            "disposition": disposition,
            "related_trait": related,
            "rationale": rationale,
        })
    return counts, review_rows, pending_count


def write_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="", prefix=f".{path.name}.",
            suffix=".part", dir=path.parent, delete=False,
        ) as stream:
            temporary = Path(stream.name)
            writer = csv.DictWriter(
                stream,
                delimiter="\t",
                fieldnames=fieldnames,
                lineterminator="\n",
                extrasaction="ignore",
            )
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="rewrite the release inventory")
    parser.add_argument("--report", type=Path, default=REPORT)
    parser.add_argument("--review-report", type=Path, default=REVIEW_REPORT)
    args = parser.parse_args(argv)
    try:
        with args.report.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            rows = list(reader)
        if not set(BASE_FIELDS).issubset(reader.fieldnames or []):
            raise ValueError(f"{args.report}: missing expected release-delta columns")
        counts, review_rows, pending_before = finalize(rows, parse_owl(OWL_PATH))
        if pending_before not in {0, 153}:
            raise ValueError(f"expected 153 pending rows or an idempotent rerun; found {pending_before}")
        if len(review_rows) not in {0, 153}:
            raise ValueError(f"expected 153 reviewed rows; found {len(review_rows)}")
        if args.apply:
            write_rows(args.report, rows, BASE_FIELDS)
            write_rows(args.review_report, review_rows, REVIEW_FIELDS)
        verb = "FINALIZED" if args.apply else "WOULD_FINALIZE"
        if not pending_before:
            verb = "VERIFIED_CURRENT"
        print(f"{verb}\t{pending_before} row(s)\t{args.report}")
        for disposition, count in sorted(counts.items()):
            print(f"  {disposition:<40} {count:>3}")
        if not args.apply and pending_before:
            print("Re-run with --apply to write final dispositions")
        return 0
    except (KeyError, OSError, ValueError, csv.Error) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
