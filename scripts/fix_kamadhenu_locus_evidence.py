#!/usr/bin/env python3
"""Add direct phage-restriction evidence to the Kamadhenu locus edge."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "kamadhenu_system.yaml"

IDENTIFIER = "traitmech:000310"
MOSTERD = "DOI:10.1073/pnas.2426508122"
MOSTERD_ESCAPE_SNIPPET = (
    "we isolated 66 phage escape mutants which had become insensitive to 13 "
    "distinct, plasmid-encoded lactococcal phage resistance systems (i.e. "
    "Rhea, Kamadhenu, Rugutis, Audmula, PARIS, type II CBASS, Septu, AbiA, "
    "AbiB, AbiD/F, AbiG, AbiJ, AbiP)"
)


def mosterd_escape_evidence() -> dict[str, str]:
    return {
        "reference": MOSTERD,
        "snippet": MOSTERD_ESCAPE_SNIPPET,
        "notes": (
            "Mosterd et al. treat Kamadhenu as a plasmid-encoded lactococcal "
            "phage-resistance system in their escape-mutant screen."
        ),
    }


def load_record(path: Path) -> dict[str, Any]:
    record = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(record, dict):
        raise AssertionError(f"{path} did not contain a TraitRecord mapping")
    return record


def select_locus_edge(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == IDENTIFIER
    assert record["label"] == "Kamadhenu system"
    assert record["mapping_status"] == "PROPOSED"

    graphs = record["causal_graphs"]
    assert [graph["graph_id"] for graph in graphs] == ["kamadhenu_locus_restricts_phage"]

    matches = [
        edge
        for edge in graphs[0]["edges"]
        if edge.get("subject") == "kamadhenu_locus"
        and edge.get("predicate_id") == "RO:0002326"
        and edge.get("object") == "restricted_phage_propagation"
    ]
    assert len(matches) == 1
    edge = matches[0]
    assert [e["reference"] for e in edge["evidence"]] == [
        "DOI:10.1093/nar/gkae671",
        (
            "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
            "afb0e5a8b466be53586b13266f5d38d98c3ac268/List_system_article.md"
        ),
    ]
    return edge


def update_record(record: dict[str, Any]) -> None:
    edge = select_locus_edge(record)
    edge["evidence"].insert(1, mosterd_escape_evidence())
    record_curation_event(
        record,
        curator="codex",
        action="UPDATED_EVIDENCE",
        changes=(
            "Added direct Mosterd et al. phage-resistance evidence to the "
            "Kamadhenu locus edge in response to PR #1140 review issue #1141."
        ),
        llm_assisted=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}")
    args = parser.parse_args()

    record = load_record(TARGET)
    update_record(record)

    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"updated {TARGET.relative_to(REPO_ROOT)}")
    else:
        with tempfile.TemporaryDirectory() as tmp:
            write_validated_trait(record, Path(tmp) / TARGET.name)
        print(f"would update {TARGET.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
