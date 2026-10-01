#!/usr/bin/env python3
"""Apply AbiF adversarial review fixes to the existing record."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from add_abif_system_trait import (  # noqa: E402
    ABIF_REVIEW_FIX_TIMESTAMP,
    ABORTIVE,
    IDENTIFIER,
    TARGET,
)
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

CURATOR = "codex"
ACTION = "ADDRESS_ABIF_REVIEW_FINDING"

REPLACEMENTS = {
    "plasmid pCG1-derived abiF locus": "pNP40-derived abiF locus",
    "pCG1-derived EcoRV-XbaI fragment": (
        "EcoRV-XbaI fragment carried by recombinant plasmid pCG1"
    ),
    "pCG1-derived fragment": "pNP40-derived EcoRV-XbaI fragment",
    "pNP40 pCG1 AbiF determinant": "pNP40 AbiF determinant into pCG1",
    "pCG1-encoded region": "cloned pNP40 region",
    "pCG1-derived abiF locus": "pNP40-derived abiF locus",
    "pNP40 pCG1-derived abortive-infection locus": (
        "pNP40-derived abortive-infection locus cloned on pCG1"
    ),
    "pCG1-derived abortive-infection locus": (
        "pNP40-derived abortive-infection locus"
    ),
    "pCG1 AbiF open reading frame": "pNP40 AbiF open reading frame",
    "pCG1-encoded pNP40 phage-insensitivity determinant": (
        "pNP40 phage-insensitivity determinant cloned on pCG1"
    ),
    "pCG1-encoded pNP40 determinant": "pNP40 determinant cloned on pCG1",
    "pCG1-derived lactococcal AbiF": "pNP40-derived lactococcal AbiF",
}


def replace_strings(value: Any) -> Any:
    if isinstance(value, str):
        for old, new in REPLACEMENTS.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_strings(item) for item in value]
    if isinstance(value, dict):
        return {key: replace_strings(item) for key, item in value.items()}
    return value


def transform(record: dict[str, Any]) -> bool:
    if record.get("identifier") not in {IDENTIFIER, "traitmech:000214"}:
        raise ValueError(f"unexpected identifier {record.get('identifier')}")
    if record.get("mapping_status") != "PROPOSED":
        raise ValueError("expected PROPOSED mapping_status")

    existing_event = any(
        event.get("action") == ACTION
        for event in record.get("curation_history", [])
    )

    before = copy.deepcopy(record)
    updated = replace_strings(record)
    record.clear()
    record.update(updated)
    if before == record and not existing_event:
        raise ValueError("no AbiF pCG1 wording was updated")

    if not existing_event:
        record_curation_event(
            record,
            curator=CURATOR,
            action=ACTION,
            changes=(
                "Addressed adversarial review issue #1505 by clarifying "
                "that pNP40 is the AbiF determinant source context and "
                "that pCG1 is the recombinant plasmid clone used in the "
                "Garvey et al. subcloning experiment."
            ),
            llm_assisted=True,
            timestamp=ABIF_REVIEW_FIX_TIMESTAMP,
        )
    return before != record or not existing_event


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record: dict[str, Any] = yaml.safe_load(TARGET.read_text(encoding="utf-8")) or {}
    parent: dict[str, Any] = yaml.safe_load(ABORTIVE.read_text(encoding="utf-8")) or {}
    record_changed = transform(record)
    parent_changed = transform(parent)
    changed = record_changed or parent_changed

    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
        print(
            f"{'updated' if changed else 'unchanged'} "
            f"{TARGET.relative_to(REPO_ROOT)} and {ABORTIVE.relative_to(REPO_ROOT)}"
        )
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / ABORTIVE.name)
    print(
        f"{'would update' if changed else 'would leave'} "
        f"{TARGET.relative_to(REPO_ROOT)} and {ABORTIVE.relative_to(REPO_ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
