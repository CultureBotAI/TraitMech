#!/usr/bin/env python3
"""Resolve and verify every UniProt accession used by a causal graph.

Generic causal-node ``grounding`` values must never be UniProtKB instances,
regardless of node type. Organism-specific accessions belong in
``protein_examples``, where their declared taxon, entry status, proteome, and
version metadata can be checked against the UniProt REST API.

Output: ``reports/uniprot_grounding_audit.tsv``, one row per use. The command
fails on generic UniProt groundings, inactive/error responses, secondary rather
than primary accessions, taxon/status mismatches, or stale declared versions.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

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
    "usage",
    "accession",
    "declared_taxon_id",
    "declared_taxon_label",
    "declared_entry_status",
    "declared_entry_version",
    "declared_sequence_version",
    "status",
    "primary_accession",
    "primary_accession_match",
    "uniprot_name",
    "gene_symbol",
    "organism",
    "uniprot_taxon_id",
    "taxon_match",
    "entry_status_match",
    "entry_version",
    "entry_version_match",
    "sequence_version",
    "sequence_version_match",
    "proteome_ids",
    "replacement",
    "reused_in_n_files",
    "finding",
]


def iter_nodes(traits_dir: Path = TRAITS):
    """Yield ``(path, graph_id, node)`` for every causal node."""
    for path in sorted(traits_dir.glob("*/*.yaml")):
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            print(f"WARN: unparseable {path}: {exc}", file=sys.stderr)
            continue
        for graph in record.get("causal_graphs") or []:
            for node in graph.get("nodes") or []:
                if isinstance(node, dict):
                    yield path, graph.get("graph_id", ""), node


def iter_gene_nodes(traits_dir: Path = TRAITS):
    """Yield gene/protein nodes for callers that need the legacy subset."""
    yield from (
        item for item in iter_nodes(traits_dir) if item[2].get("node_type") == "GENE_OR_PROTEIN"
    )


def iter_uses(
    nodes: Iterable[tuple[Path, str, dict[str, Any]]],
) -> list[dict[str, Any]]:
    """Flatten prohibited generic groundings and valid exemplar locations."""
    uses: list[dict[str, Any]] = []
    for path, graph_id, node in nodes:
        grounding = str(node.get("grounding") or "")
        if grounding.startswith("UniProtKB:"):
            uses.append(
                {
                    "path": path,
                    "graph_id": graph_id,
                    "node": node,
                    "usage": "GENERIC_GROUNDING",
                    "accession": grounding.split(":", 1)[1],
                    "example": {},
                }
            )
        for example in node.get("protein_examples") or []:
            if not isinstance(example, dict):
                continue
            uniprot_id = str(example.get("uniprot_id") or "")
            if not uniprot_id.startswith("UniProtKB:"):
                continue
            uses.append(
                {
                    "path": path,
                    "graph_id": graph_id,
                    "node": node,
                    "usage": "PROTEIN_EXAMPLE",
                    "accession": uniprot_id.split(":", 1)[1],
                    "example": example,
                }
            )
    return uses


def _protein_name(data: dict[str, Any]) -> str:
    description = data.get("proteinDescription") or {}
    named = description.get("recommendedName") or next(
        iter(description.get("submissionNames") or []), {}
    )
    return str((named.get("fullName") or {}).get("value") or "")


def _gene_symbol(data: dict[str, Any]) -> str:
    first = next(iter(data.get("genes") or []), {})
    return str((first.get("geneName") or {}).get("value") or "")


def fetch(accession: str, delay: float = 0.1) -> dict[str, Any]:
    """Resolve one accession and normalize the fields the audit compares."""
    time.sleep(delay)
    try:
        with urllib.request.urlopen(API.format(acc=accession), timeout=30) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return {"status": "deleted"}
        return {"status": "error", "uniprot_name": f"HTTP {exc.code}"}
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        return {"status": "error", "uniprot_name": str(exc)[:120]}

    entry_type = str(data.get("entryType") or "")
    if entry_type == "Inactive":
        reason = data.get("inactiveReason") or {}
        kind = str(reason.get("inactiveReasonType") or "deleted").lower()
        return {
            "status": kind,
            "replacement": ",".join(reason.get("mergeDemergeTo") or []),
        }

    reviewed = "reviewed" in entry_type.lower() and "unreviewed" not in entry_type.lower()
    audit = data.get("entryAudit") or {}
    organism = data.get("organism") or {}
    proteomes = sorted(
        {
            str(xref.get("id"))
            for xref in data.get("uniProtKBCrossReferences") or []
            if xref.get("database") == "Proteomes" and xref.get("id")
        }
    )
    return {
        "status": "reviewed" if reviewed else "unreviewed",
        "entry_status": "REVIEWED" if reviewed else "UNREVIEWED",
        "primary_accession": str(data.get("primaryAccession") or ""),
        "uniprot_name": _protein_name(data),
        "gene_symbol": _gene_symbol(data),
        "organism": str(organism.get("scientificName") or ""),
        "taxon_id": str(organism.get("taxonId") or ""),
        "entry_version": audit.get("entryVersion", ""),
        "sequence_version": audit.get("sequenceVersion", ""),
        "proteome_ids": ",".join(proteomes),
    }


def _same(declared: Any, resolved: Any) -> str:
    """Return YES/NO, or SKIPPED when no declaration was made."""
    if declared in (None, ""):
        return "SKIPPED"
    return "YES" if str(declared) == str(resolved) else "NO"


def _contains(declared: Any, resolved_csv: Any) -> str:
    """Compare an optional declaration with a comma-separated resolved set."""
    if declared in (None, ""):
        return "SKIPPED"
    resolved = {item for item in str(resolved_csv or "").split(",") if item}
    return "YES" if str(declared) in resolved else "NO"


def result_row(use: dict[str, Any], resolved: dict[str, Any], reuse: int) -> dict[str, Any]:
    """Combine one declared use with a normalized UniProt response."""
    example = use["example"]
    accession = use["accession"]
    declared_taxon = str(example.get("taxon_id") or "").removeprefix("NCBITaxon:")
    primary_match = _same(accession, resolved.get("primary_accession"))
    taxon_match = _same(declared_taxon, resolved.get("taxon_id"))
    status_match = _same(example.get("entry_status"), resolved.get("entry_status"))
    entry_version_match = _same(example.get("entry_version"), resolved.get("entry_version"))
    sequence_version_match = _same(
        example.get("sequence_version"), resolved.get("sequence_version")
    )
    proteome_match = _contains(example.get("proteome_id"), resolved.get("proteome_ids"))

    findings: list[str] = []
    status = resolved.get("status", "error")
    if use["usage"] == "GENERIC_GROUNDING":
        findings.append("GENERIC_UNIPROT_GROUNDING")
    if status not in {"reviewed", "unreviewed"}:
        findings.append(f"UNIPROT_{str(status).upper()}")
    if primary_match == "NO":
        findings.append("NOT_PRIMARY_ACCESSION")
    if taxon_match == "NO":
        findings.append("TAXON_MISMATCH")
    if status_match == "NO":
        findings.append("ENTRY_STATUS_MISMATCH")
    if entry_version_match == "NO":
        findings.append("ENTRY_VERSION_MISMATCH")
    if sequence_version_match == "NO":
        findings.append("SEQUENCE_VERSION_MISMATCH")
    if proteome_match == "NO":
        findings.append("PROTEOME_MISMATCH")

    path: Path = use["path"]
    try:
        file_label = path.relative_to(REPO).as_posix()
    except ValueError:
        file_label = path.as_posix()
    node = use["node"]
    return {
        "file": file_label,
        "graph_id": use["graph_id"],
        "node_id": node.get("node_id", ""),
        "label": node.get("label", ""),
        "usage": use["usage"],
        "accession": accession,
        "declared_taxon_id": example.get("taxon_id", ""),
        "declared_taxon_label": example.get("taxon_label", ""),
        "declared_entry_status": example.get("entry_status", ""),
        "declared_entry_version": example.get("entry_version", ""),
        "declared_sequence_version": example.get("sequence_version", ""),
        "status": status,
        "primary_accession": resolved.get("primary_accession", ""),
        "primary_accession_match": primary_match,
        "uniprot_name": resolved.get("uniprot_name", ""),
        "gene_symbol": resolved.get("gene_symbol", ""),
        "organism": resolved.get("organism", ""),
        "uniprot_taxon_id": (
            f"NCBITaxon:{resolved['taxon_id']}" if resolved.get("taxon_id") else ""
        ),
        "taxon_match": taxon_match,
        "entry_status_match": status_match,
        "entry_version": resolved.get("entry_version", ""),
        "entry_version_match": entry_version_match,
        "sequence_version": resolved.get("sequence_version", ""),
        "sequence_version_match": sequence_version_match,
        "proteome_ids": resolved.get("proteome_ids", ""),
        "replacement": resolved.get("replacement", ""),
        "reused_in_n_files": reuse,
        "finding": "|".join(findings),
    }


def audit_uses(
    uses: list[dict[str, Any]],
    *,
    delay: float = 0.1,
    resolver=fetch,
) -> list[dict[str, Any]]:
    """Resolve unique accessions and return one comparison row per use."""
    accessions = sorted({use["accession"] for use in uses})
    resolved = {accession: resolver(accession, delay) for accession in accessions}
    files_per_accession: dict[str, set[str]] = defaultdict(set)
    for use in uses:
        files_per_accession[use["accession"]].add(use["path"].as_posix())
    return [
        result_row(
            use,
            resolved[use["accession"]],
            len(files_per_accession[use["accession"]]),
        )
        for use in uses
    ]


def write_report(rows: list[dict[str, Any]], out: Path = REPORT) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--traits-dir", type=Path, default=TRAITS)
    parser.add_argument("--out", type=Path, default=REPORT)
    parser.add_argument(
        "--delay",
        type=float,
        default=0.1,
        help="seconds to sleep between UniProt requests (default 0.1)",
    )
    args = parser.parse_args()

    nodes = list(iter_nodes(args.traits_dir))
    uses = iter_uses(nodes)
    rows = audit_uses(uses, delay=args.delay)
    write_report(rows, args.out)

    gene_nodes = [item for item in nodes if item[2].get("node_type") == "GENE_OR_PROTEIN"]
    by_prefix: Counter[str] = Counter()
    for _, _, node in gene_nodes:
        grounding = str(node.get("grounding") or "")
        by_prefix[grounding.split(":", 1)[0] if grounding else "(ungrounded)"] += 1
    print(f"GENE_OR_PROTEIN nodes: {len(gene_nodes)}")
    print(f"  ungrounded (label only): {by_prefix['(ungrounded)']}")
    for prefix in sorted(p for p in by_prefix if p != "(ungrounded)"):
        print(f"  {prefix + '-grounded:':24s} {by_prefix[prefix]}")
    print(f"  UniProtKB uses: {len(rows)}")
    print(f"  unique accessions: {len({row['accession'] for row in rows})}")
    print(f"  findings: {sum(bool(row['finding']) for row in rows)}")
    print(f"wrote {args.out}")
    return int(any(row["finding"] for row in rows))


if __name__ == "__main__":
    raise SystemExit(main())
