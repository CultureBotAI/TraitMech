#!/usr/bin/env python3
"""Move the measured NaCl-optimum exemplar to its most-specific bin (#478).

The source reports a 15--20% (w/v) optimum for *Wallemia ichthyophaga*.
That complete interval is above the ``NaCl optimum high`` threshold (>8% w/v),
so the #478 most-specific-placement policy puts the example on the bin rather
than duplicating it on the family parent.

Usage:
    python scripts/move_nacl_optimum_exemplar.py          # dry run
    python scripts/move_nacl_optimum_exemplar.py --apply  # write
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

PARENT_PATH = Path("data/traits/environment/nacl_optimum.yaml")
BIN_PATH = Path("data/traits/environment/nacl_optimum_high.yaml")
TIMESTAMP = "2026-08-30T20:02:00Z"
CURATOR = "codex"
ACTION = "MOVE_CANONICAL_EXAMPLE_TO_SPECIFIC_BIN"

SOURCE_EXAMPLE = {
    "taxon_id": "NCBITaxon:245174",
    "taxon_label": "Wallemia ichthyophaga",
    "reference": "DOI:10.1128/aem.02702-13",
    "note": (
        "Extremely halophilic fungus whose NaCl optimum was determined kinetically, "
        "from exponential-phase doubling times across a salinity series, giving an "
        "optimum of 15-20 percent NaCl. The artifact uses it as the worked example "
        "separating optimum from range, because the same organism still grows from "
        "10 percent to saturated (32 percent) NaCl."
    ),
}

BIN_EXAMPLE = {
    "taxon_id": "NCBITaxon:245174",
    "taxon_label": "Wallemia ichthyophaga",
    "reference": "DOI:10.1128/aem.02702-13",
    "note": (
        "Extremely halophilic fungus whose NaCl optimum was determined kinetically "
        "from exponential-phase doubling times across a salinity series. The "
        "reported 15-20% (w/v) optimum lies wholly above this bin's >8% (w/v) "
        "threshold. The same organism grows from 10% to saturated (~32%) NaCl; "
        "that wider interval is its growth range, not its optimum."
    ),
}


def _insert_examples(doc: dict[str, Any], examples: list[dict[str, str]]) -> None:
    """Insert after evidence, matching the corpus's dominant field order."""
    if "canonical_examples" in doc:
        doc["canonical_examples"] = examples
        return
    rebuilt: dict[str, Any] = {}
    for key, value in doc.items():
        rebuilt[key] = value
        if key == "evidence":
            rebuilt["canonical_examples"] = examples
    if "canonical_examples" not in rebuilt:
        rebuilt["canonical_examples"] = examples
    doc.clear()
    doc.update(rebuilt)


def transform(parent: dict[str, Any], bin_record: dict[str, Any]) -> bool:
    """Apply the exact move in memory; return false when already applied."""
    if parent.get("identifier") != "METPO:1000333":
        raise ValueError("parent identifier is not METPO:1000333")
    if bin_record.get("identifier") != "METPO:1000468":
        raise ValueError("bin identifier is not METPO:1000468")

    parent_examples = parent.get("canonical_examples") or []
    bin_examples = bin_record.get("canonical_examples") or []
    source_matches = [
        example
        for example in parent_examples
        if example.get("taxon_id") == SOURCE_EXAMPLE["taxon_id"]
    ]
    bin_matches = [
        example
        for example in bin_examples
        if example.get("taxon_id") == BIN_EXAMPLE["taxon_id"]
    ]

    if not source_matches and bin_matches == [BIN_EXAMPLE]:
        return False
    if source_matches != [SOURCE_EXAMPLE]:
        raise ValueError("parent does not contain the one exact source exemplar")
    if bin_matches:
        raise ValueError("target bin already contains this taxon; refusing duplication")

    remaining = [example for example in parent_examples if example is not source_matches[0]]
    if remaining:
        parent["canonical_examples"] = remaining
    else:
        parent.pop("canonical_examples", None)
    _insert_examples(bin_record, [*bin_examples, BIN_EXAMPLE])

    record_curation_event(
        parent,
        curator=CURATOR,
        action=ACTION,
        changes=(
            "Moved Wallemia ichthyophaga (NCBITaxon:245174; "
            "DOI:10.1128/aem.02702-13) off the NaCl-optimum parent under the "
            "#478 most-specific-placement policy. Its measured 15-20% (w/v) "
            "optimum belongs wholly in METPO:1000468; the same claim is not "
            "duplicated on parent and bin."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    record_curation_event(
        bin_record,
        curator=CURATOR,
        action=ACTION,
        changes=(
            "Added Wallemia ichthyophaga (NCBITaxon:245174; "
            "DOI:10.1128/aem.02702-13) from the NaCl-optimum parent under the "
            "#478 most-specific-placement policy. Its complete measured optimum "
            "interval, 15-20% (w/v), is above this bin's >8% (w/v) threshold."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def _validate_pair(parent: dict[str, Any], bin_record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        write_validated_trait(parent, tmpdir / PARENT_PATH.name)
        write_validated_trait(bin_record, tmpdir / BIN_PATH.name)


def apply(write: bool = False) -> int:
    parent_path = REPO_ROOT / PARENT_PATH
    bin_path = REPO_ROOT / BIN_PATH
    parent = yaml.safe_load(parent_path.read_text(encoding="utf-8")) or {}
    bin_record = yaml.safe_load(bin_path.read_text(encoding="utf-8")) or {}

    changed = transform(parent, bin_record)
    if not changed:
        print("Wallemia ichthyophaga is already on NaCl optimum high; no change")
        return 0

    _validate_pair(parent, bin_record)
    if write:
        write_validated_trait(parent, parent_path)
        write_validated_trait(bin_record, bin_path)

    mode = "applied" if write else "dry run"
    print(f"{mode}: moved NCBITaxon:245174 from {PARENT_PATH} to {BIN_PATH}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write; default is dry run")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    sys.exit(main())
