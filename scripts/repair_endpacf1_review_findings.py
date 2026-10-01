#!/usr/bin/env python3
"""Apply the ENDPaCF1 Copilot review fixes to the existing record."""

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

from add_endpacf1_system_trait import (  # noqa: E402
    COPILOT_REVIEW_FIX_TIMESTAMP,
    IDENTIFIER,
    PHAGE_DEFENSE_SYSTEM,
    RECORD,
    TARGET,
    yee_native_deletion_evidence,
)
from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

CURATOR = "codex"
ACTION = "ADDRESS_ENDPACF1_REVIEW_FINDINGS"

CANONICAL_EXAMPLE = copy.deepcopy(RECORD["canonical_examples"][0])
NATIVE_DELETION_EVIDENCE = yee_native_deletion_evidence()

UNSUPPORTED_EDGE = {
    "subject": "hypermodified_phage_dna_sensing",
    "predicate": "contributes to",
    "predicate_id": "RO:0002326",
    "object": "modification_dependent_phage_dna_cleavage",
    "description": (
        "ENDPaCF1-family iEndoIII-linked sensing is coupled to "
        "endonuclease cleavage of modified phage DNA."
    ),
}


def _insert_after_evidence(
    record: dict[str, Any], field: str, value: list[dict[str, str]]
) -> None:
    """Insert a top-level field after evidence, matching the local record order."""
    if field in record:
        record[field] = value
        return

    rebuilt: dict[str, Any] = {}
    for key, existing in record.items():
        rebuilt[key] = existing
        if key == "evidence":
            rebuilt[field] = value
    if field not in rebuilt:
        rebuilt[field] = value
    record.clear()
    record.update(rebuilt)


def transform(record: dict[str, Any]) -> bool:
    if record.get("identifier") != IDENTIFIER:
        raise ValueError(f"expected identifier {IDENTIFIER}")
    if record.get("label") != "ENDPaCF1 system":
        raise ValueError("expected ENDPaCF1 system label")
    if record.get("mapping_status") != "PROPOSED":
        raise ValueError("expected PROPOSED mapping_status")
    if record.get("parent_traits") != [PHAGE_DEFENSE_SYSTEM]:
        raise ValueError(f"expected only {PHAGE_DEFENSE_SYSTEM} as parent")

    examples = record.get("canonical_examples") or []
    evidence = record.get("evidence") or []
    graph = record["causal_graphs"][0]
    edges = graph["edges"]
    unsupported_edges = [
        edge for edge in edges if edge.get("subject") == UNSUPPORTED_EDGE["subject"]
    ]
    review_events = [
        event
        for event in record.get("curation_history", [])
        if event.get("action") == ACTION
    ]

    already_applied = (
        examples == [CANONICAL_EXAMPLE]
        and NATIVE_DELETION_EVIDENCE in evidence
        and not unsupported_edges
        and len(review_events) == 1
    )
    if already_applied:
        return False

    if examples:
        raise ValueError("canonical_examples unexpectedly populated")
    if NATIVE_DELETION_EVIDENCE in evidence:
        raise ValueError("native deletion evidence already present without exemplar")
    if len(unsupported_edges) != 1:
        raise ValueError("expected exactly one unsupported sensing-to-cleavage edge")

    unsupported_edge = unsupported_edges[0]
    for key, value in UNSUPPORTED_EDGE.items():
        if unsupported_edge.get(key) != value:
            raise ValueError(f"unexpected unsupported edge {key}")

    hypermodified_idx = next(
        idx
        for idx, item in enumerate(evidence)
        if item.get("snippet", "").startswith("ENDPaCF1 protects bacteria")
    )
    evidence.insert(hypermodified_idx + 1, NATIVE_DELETION_EVIDENCE)
    _insert_after_evidence(record, "canonical_examples", [CANONICAL_EXAMPLE])
    graph["edges"] = [edge for edge in edges if edge is not unsupported_edge]

    record_curation_event(
        record,
        curator=CURATOR,
        action=ACTION,
        changes=(
            "Addressed Copilot review issues #1501, #1502, and #1503: "
            "added Pseudomonas aeruginosa (NCBITaxon:287) as a DOI-backed "
            "native ENDPaCF1 canonical example, removed the unsupported "
            "direct hypermodified-phage-DNA-sensing to modification-"
            "dependent-phage-DNA-cleavage causal edge, and included the "
            "discussions block in the repository CREATE history sections."
        ),
        llm_assisted=True,
        timestamp=COPILOT_REVIEW_FIX_TIMESTAMP,
    )
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record: dict[str, Any] = yaml.safe_load(TARGET.read_text(encoding="utf-8")) or {}
    changed = transform(record)

    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"{'updated' if changed else 'unchanged'} {TARGET.relative_to(REPO_ROOT)}")
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        check_path = Path(tmp) / TARGET.name
        write_validated_trait(record, check_path)
    print(f"{'would update' if changed else 'would leave'} {TARGET.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
