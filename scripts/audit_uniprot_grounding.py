#!/usr/bin/env python3
"""Audit UniProtKB groundings on GENE_OR_PROTEIN causal-graph nodes.

Every `grounding: UniProtKB:<acc>` in `data/traits/*/*.yaml` is resolved
against the UniProt REST API and classified as one of:

  reviewed    — UniProtKB/Swiss-Prot entry (curated; stable; preferred)
  unreviewed  — UniProtKB/TrEMBL entry (automatic annotation)
  deleted     — accession no longer active in UniProtKB
  merged      — accession folded into another entry (follow `replacement`)
  error       — network/parse failure

It also flags *reuse*: one accession attached to nodes in more than one
trait file. A single organism's protein standing in for a taxon-agnostic
family node is a grounding smell, not a fact about the mechanism.

Output: `reports/uniprot_grounding_audit.tsv`, one row per node.
Read-only with respect to the trait corpus — this script never edits YAML.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
TRAITS = REPO / "data" / "traits"
REPORT = REPO / "reports" / "uniprot_grounding_audit.tsv"
API = "https://rest.uniprot.org/uniprotkb/{acc}.json"

FIELDS = [
    "file",
    "graph_id",
    "node_id",
    "label",
    "accession",
    "status",
    "uniprot_name",
    "organism",
    "replacement",
    "reused_in_n_files",
]


def iter_gene_nodes(traits_dir: Path):
    """Yield (path, graph_id, node) for every GENE_OR_PROTEIN causal node."""
    for path in sorted(traits_dir.glob("*/*.yaml")):
        try:
            record = yaml.safe_load(path.read_text()) or {}
        except yaml.YAMLError as exc:
            print(f"WARN: unparseable {path}: {exc}", file=sys.stderr)
            continue
        for graph in record.get("causal_graphs") or []:
            for node in graph.get("nodes") or []:
                if node.get("node_type") == "GENE_OR_PROTEIN":
                    yield path, graph.get("graph_id", ""), node


def fetch(accession: str, delay: float) -> dict:
    """Resolve one accession. Deleted entries return entryType 'Inactive'."""
    time.sleep(delay)
    try:
        with urllib.request.urlopen(API.format(acc=accession), timeout=30) as resp:
            data = json.load(resp)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return {"status": "error", "uniprot_name": str(exc)[:80]}

    entry_type = data.get("entryType", "")
    if entry_type == "Inactive":
        reason = data.get("inactiveReason", {}) or {}
        kind = (reason.get("inactiveReasonType") or "").lower()
        return {
            "status": kind or "deleted",
            "replacement": ",".join(reason.get("mergeDemergeTo", []) or []),
        }

    description = data.get("proteinDescription", {})
    named = description.get("recommendedName") or next(
        iter(description.get("submissionNames") or []), {}
    )
    return {
        "status": "reviewed" if "reviewed" in entry_type and "unreviewed" not in entry_type else "unreviewed",
        "uniprot_name": (named.get("fullName") or {}).get("value", ""),
        "organism": data.get("organism", {}).get("scientificName", ""),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--delay",
        type=float,
        default=0.1,
        help="seconds to sleep between UniProt requests (default 0.1)",
    )
    args = parser.parse_args()

    nodes = list(iter_gene_nodes(TRAITS))
    grounded = [
        (path, graph_id, node)
        for path, graph_id, node in nodes
        if (node.get("grounding") or "").startswith("UniProtKB:")
    ]

    files_per_accession: dict[str, set[str]] = defaultdict(set)
    for path, _, node in grounded:
        files_per_accession[node["grounding"].split(":", 1)[1]].add(path.name)

    cache: dict[str, dict] = {}
    for accession in sorted(files_per_accession):
        cache[accession] = fetch(accession, args.delay)

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    tally: dict[str, int] = defaultdict(int)
    with REPORT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        for path, graph_id, node in grounded:
            accession = node["grounding"].split(":", 1)[1]
            resolved = cache[accession]
            tally[resolved["status"]] += 1
            writer.writerow(
                {
                    "file": path.relative_to(REPO).as_posix(),
                    "graph_id": graph_id,
                    "node_id": node.get("node_id", ""),
                    "label": node.get("label", ""),
                    "accession": accession,
                    "status": resolved["status"],
                    "uniprot_name": resolved.get("uniprot_name", ""),
                    "organism": resolved.get("organism", ""),
                    "replacement": resolved.get("replacement", ""),
                    "reused_in_n_files": len(files_per_accession[accession]),
                }
            )

    ungrounded = len(nodes) - len(grounded)
    print(f"GENE_OR_PROTEIN nodes: {len(nodes)}")
    print(f"  ungrounded (label only): {ungrounded}")
    print(f"  UniProtKB-grounded:      {len(grounded)}  ({len(files_per_accession)} unique accessions)")
    for status in sorted(tally):
        print(f"    {status:12s} {tally[status]}")
    reused = sum(1 for files in files_per_accession.values() if len(files) > 1)
    print(f"  accessions reused across >1 trait file: {reused}")
    print(f"\nwrote {REPORT.relative_to(REPO)}")
    return 1 if tally.get("deleted") or tally.get("error") else 0


if __name__ == "__main__":
    raise SystemExit(main())
