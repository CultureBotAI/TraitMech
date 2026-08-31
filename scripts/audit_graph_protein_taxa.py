#!/usr/bin/env python3
"""Audit protein-node, canonical-taxon, and UniProt-example graph coverage.

The causal graph remains taxon-agnostic: a GENE_OR_PROTEIN node is grounded to
GO, InterPro, NCBIfam, or another semantic family/complex identifier. A
UniProtKB accession is an organism-specific example and belongs in the node's
``protein_examples`` list, paired with its source taxon and primary-source
evidence. Protein-source taxa are independent of ``canonical_examples``: the
former says where a mechanism was established, while the latter names an
organism that exemplifies the trait.

Output: ``reports/graph_protein_taxon_coverage.tsv``, one row per graph. The
default is report-only so the existing backlog can be curated incrementally.
Use ``--fail-on errors`` to enforce malformed or contradictory examples during
rollout and ``--fail-on gaps`` for the final coverage gate; ``gaps`` fails on
errors as well, so the final gate cannot pass a corpus with contradictory
examples just because its coverage is complete.

Records listed in ``DO_NOT_WORK.md`` are excluded from agentic curation and can
never be brought to coverage by the usual route, so their graphs report the
status ``PROTECTED`` (with the unmet requirements still listed) and do not count
toward the ``gaps`` gate. Editing that file is a user decision.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS = REPO_ROOT / "data" / "traits"
REPORT = REPO_ROOT / "reports" / "graph_protein_taxon_coverage.tsv"
DO_NOT_WORK = REPO_ROOT / "DO_NOT_WORK.md"

PROTECTED_PATH_RE = re.compile(r"`(data/traits/[^`]+\.yaml)`")

SEMANTIC_PROTEIN_PREFIXES = {"ComplexPortal", "GO", "InterPro", "NCBIfam"}
ERROR_CODES = {
    "TRAIT_RECORD_LOAD_ERROR",
    "GENERIC_UNIPROT_GROUNDING",
    "PROTEIN_EXAMPLE_ON_NONPROTEIN_NODE",
    "PROTEIN_EXAMPLE_MISSING_UNIPROT_ID",
    "PROTEIN_EXAMPLE_MISSING_TAXON_ID",
    "PROTEIN_EXAMPLE_MISSING_ROLE",
    "PROTEIN_EXAMPLE_MISSING_EVIDENCE",
    "PROTEIN_EXAMPLE_EVIDENCE_INCOMPLETE",
    "UNREVIEWED_EXAMPLE_MISSING_PROTEOME",
    "LABEL_ONLY_STATUS_WITH_GROUNDING",
}

LOAD_ERROR_KEY = "__audit_trait_record_load_error__"

NONPROTEIN_PRIMARY_RE = re.compile(
    r"(?:^|[\s/()-])(?:genes?|operons?|gene clusters?|loci|locus)(?:$|[\s/()-])",
    re.IGNORECASE,
)

NONPROTEIN_EXACT_LABEL_RE = re.compile(
    r"^(?:plasmid|prophage|phage[- /]plasmid|(?:cr|m|r|s|t)rna|"
    r"rna thermometer|shine-dalgarno sequence|promoter)$",
    re.IGNORECASE,
)


def _is_nonprotein_primary_label(label: object) -> bool:
    """Return whether a legacy GENE_OR_PROTEIN label is clearly not a protein."""
    normalized = " ".join(str(label or "").split())
    return bool(
        NONPROTEIN_PRIMARY_RE.search(normalized)
        or NONPROTEIN_EXACT_LABEL_RE.fullmatch(normalized)
    )

FIELDS = [
    "file",
    "trait_id",
    "trait_label",
    "graph_id",
    "scope_status",
    "protein_nodes",
    "semantic_grounded_nodes",
    "reviewed_label_only_nodes",
    "canonical_examples",
    "cited_canonical_examples",
    "protein_examples",
    "taxon_matched_examples",
    "status",
    "error_count",
    "gap_count",
    "unmet_requirements",
]


def load_records(traits_dir: Path = TRAITS) -> list[tuple[str, dict[str, Any]]]:
    """Load TraitRecords, retaining failures as gate-visible pseudo-records."""
    records: list[tuple[str, dict[str, Any]]] = []
    for path in sorted(traits_dir.glob("*/*.yaml")):
        try:
            label = path.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            label = path.as_posix()
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            print(f"WARN: unparseable {path}: {exc}", file=sys.stderr)
            records.append((label, {LOAD_ERROR_KEY: str(exc)}))
            continue
        if isinstance(doc, dict):
            records.append((label, doc))
        else:
            detail = f"expected a mapping, found {type(doc).__name__}"
            print(f"WARN: invalid trait record {path}: {detail}", file=sys.stderr)
            records.append((label, {LOAD_ERROR_KEY: detail}))
    return records


def load_protected(path: Path = DO_NOT_WORK) -> set[str]:
    """Return repo-relative trait paths that DO_NOT_WORK.md excludes from curation."""
    if not path.is_file():
        return set()
    return set(PROTECTED_PATH_RE.findall(path.read_text(encoding="utf-8")))


def _issue(issues: list[tuple[str, str]], code: str, detail: str = "") -> None:
    rendered = f"{code}:{detail}" if detail else code
    issues.append(("ERROR" if code in ERROR_CODES else "GAP", rendered))


def _evidence_is_complete(evidence: Any) -> bool:
    return bool(
        isinstance(evidence, dict)
        and evidence.get("reference")
        and evidence.get("snippet")
        and evidence.get("notes")
    )


def _load_error_row(file_label: str, detail: str) -> dict[str, Any]:
    """Return a report row that makes an unreadable record fail every gate."""
    compact_detail = " ".join(detail.split())[:240]
    return {
        "file": file_label,
        "trait_id": "",
        "trait_label": "",
        "graph_id": "",
        "scope_status": "",
        "protein_nodes": 0,
        "semantic_grounded_nodes": 0,
        "reviewed_label_only_nodes": 0,
        "canonical_examples": 0,
        "cited_canonical_examples": 0,
        "protein_examples": 0,
        "taxon_matched_examples": 0,
        "status": "ERROR",
        "error_count": 1,
        "gap_count": 0,
        "unmet_requirements": f"TRAIT_RECORD_LOAD_ERROR:{compact_detail}",
    }


def graph_row(
    file_label: str,
    record: dict[str, Any],
    graph: dict[str, Any],
    *,
    protected: bool = False,
) -> dict[str, Any]:
    """Return one deterministic coverage row for a causal graph.

    A ``protected`` graph keeps its findings and counts in the row but takes
    the status ``PROTECTED`` instead of ``GAP``, and its gaps are not counted
    toward the ``--fail-on gaps`` gate. Errors are never protected.
    """
    issues: list[tuple[str, str]] = []
    scope = str(graph.get("scope_status") or "")
    nodes = [node for node in graph.get("nodes") or [] if isinstance(node, dict)]
    declared_protein_nodes = [
        node for node in nodes if node.get("node_type") == "GENE_OR_PROTEIN"
    ]
    protein_nodes = [
        node
        for node in declared_protein_nodes
        if not _is_nonprotein_primary_label(node.get("label"))
    ]

    canonical = [
        ex for ex in record.get("canonical_examples") or [] if isinstance(ex, dict)
    ]
    canonical_taxa = {str(ex.get("taxon_id")) for ex in canonical if ex.get("taxon_id")}
    cited_canonical = [ex for ex in canonical if ex.get("taxon_id") and ex.get("reference")]

    semantic_grounded = 0
    reviewed_label_only = 0
    protein_example_count = 0
    taxon_matched_count = 0

    for node in nodes:
        node_id = str(node.get("node_id") or "?")
        node_type = node.get("node_type")
        nonprotein_label = _is_nonprotein_primary_label(node.get("label"))
        valid_protein_node = node_type == "GENE_OR_PROTEIN" and not nonprotein_label
        grounding = str(node.get("grounding") or "")
        examples = [
            ex for ex in node.get("protein_examples") or [] if isinstance(ex, dict)
        ]
        if grounding.startswith("UniProtKB:"):
            _issue(issues, "GENERIC_UNIPROT_GROUNDING", node_id)

        if examples and not valid_protein_node:
            _issue(
                issues,
                "PROTEIN_EXAMPLE_ON_NONPROTEIN_NODE",
                node_id,
            )

        # Validate every declared example even when the owning node is invalid;
        # otherwise putting examples on a gene/operon/RNA-shaped legacy node
        # bypasses every field-level check below (#523).
        for ex in examples:
            uniprot_id = str(ex.get("uniprot_id") or "")
            taxon_id = str(ex.get("taxon_id") or "")
            ex_label = uniprot_id or node_id

            if not uniprot_id.startswith("UniProtKB:"):
                _issue(issues, "PROTEIN_EXAMPLE_MISSING_UNIPROT_ID", ex_label)
            if not taxon_id.startswith("NCBITaxon:"):
                _issue(issues, "PROTEIN_EXAMPLE_MISSING_TAXON_ID", ex_label)
            if not ex.get("role"):
                _issue(issues, "PROTEIN_EXAMPLE_MISSING_ROLE", ex_label)

            evidence = ex.get("evidence")
            if not isinstance(evidence, list) or not evidence:
                _issue(issues, "PROTEIN_EXAMPLE_MISSING_EVIDENCE", ex_label)
            elif any(not _evidence_is_complete(item) for item in evidence):
                _issue(issues, "PROTEIN_EXAMPLE_EVIDENCE_INCOMPLETE", ex_label)

            if ex.get("entry_status") == "UNREVIEWED" and not ex.get("proteome_id"):
                _issue(issues, "UNREVIEWED_EXAMPLE_MISSING_PROTEOME", ex_label)

            if valid_protein_node:
                protein_example_count += 1
                if taxon_id in canonical_taxa:
                    taxon_matched_count += 1

        if node_type != "GENE_OR_PROTEIN":
            continue

        if nonprotein_label:
            _issue(
                issues,
                "GENE_OR_OPERON_PRIMARY_NODE",
                node_id,
            )
            continue

        prefix = grounding.split(":", 1)[0] if grounding else ""
        status = node.get("grounding_status")
        notes = node.get("grounding_notes")

        if grounding.startswith("UniProtKB:"):
            pass  # Already reported for every node type above.
        elif prefix in SEMANTIC_PROTEIN_PREFIXES:
            semantic_grounded += 1
        elif grounding:
            _issue(issues, "UNREVIEWED_PROTEIN_GROUNDING_PREFIX", f"{node_id}={prefix}")

        if grounding and status == "REVIEWED_LABEL_ONLY":
            _issue(issues, "LABEL_ONLY_STATUS_WITH_GROUNDING", node_id)
        elif not grounding:
            if status == "REVIEWED_LABEL_ONLY" and notes:
                reviewed_label_only += 1
            else:
                _issue(issues, "LABEL_ONLY_NODE_NOT_REVIEWED", node_id)

    if not scope or scope == "REVIEW_NEEDED":
        _issue(issues, "SCOPE_NOT_REVIEWED")
    elif scope == "NONMECHANISTIC" and not graph.get("scope_notes"):
        _issue(issues, "NONMECHANISTIC_SCOPE_MISSING_NOTES")

    if scope != "NONMECHANISTIC":
        if not protein_nodes:
            _issue(issues, "NO_PROTEIN_NODE")
        if not cited_canonical:
            _issue(issues, "NO_CITED_CANONICAL_TAXON")
        if not protein_example_count:
            _issue(issues, "NO_PROTEIN_EXAMPLE")

    error_count = sum(kind == "ERROR" for kind, _ in issues)
    gap_count = sum(kind == "GAP" for kind, _ in issues)
    if error_count:
        row_status = "ERROR"
    elif gap_count:
        row_status = "PROTECTED" if protected else "GAP"
    elif scope == "NONMECHANISTIC":
        row_status = "NONMECHANISTIC"
    else:
        row_status = "PASS"

    return {
        "file": file_label,
        "trait_id": record.get("identifier", ""),
        "trait_label": record.get("label", ""),
        "graph_id": graph.get("graph_id", ""),
        "scope_status": scope,
        "protein_nodes": len(protein_nodes),
        "semantic_grounded_nodes": semantic_grounded,
        "reviewed_label_only_nodes": reviewed_label_only,
        "canonical_examples": len(canonical),
        "cited_canonical_examples": len(cited_canonical),
        "protein_examples": protein_example_count,
        "taxon_matched_examples": taxon_matched_count,
        "status": row_status,
        "error_count": error_count,
        "gap_count": gap_count,
        "unmet_requirements": "|".join(detail for _, detail in issues),
    }


def coverage_rows(
    records: Iterable[tuple[str, dict[str, Any]]] | None = None,
    protected: set[str] | None = None,
) -> list[dict[str, Any]]:
    """Return one row per graph, plus one error row per unreadable record."""
    source = load_records() if records is None else records
    shielded = load_protected() if protected is None else protected
    rows: list[dict[str, Any]] = []
    for file_label, record in source:
        if LOAD_ERROR_KEY in record:
            rows.append(_load_error_row(file_label, str(record[LOAD_ERROR_KEY])))
            continue
        for graph in record.get("causal_graphs") or []:
            if isinstance(graph, dict):
                rows.append(
                    graph_row(
                        file_label, record, graph, protected=file_label in shielded
                    )
                )
    return rows


def write_report(rows: list[dict[str, Any]], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(
            {
                **row,
                "unmet_requirements": row.get("unmet_requirements") or "-",
            }
            for row in rows
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--traits-dir", type=Path, default=TRAITS)
    parser.add_argument("--out", type=Path, default=REPORT)
    parser.add_argument(
        "--fail-on",
        choices=("none", "errors", "gaps", "any"),
        default="none",
        help=(
            "exit non-zero for the selected finding class (default: none); "
            "'gaps' also fails on errors, 'any' additionally fails on protected gaps"
        ),
    )
    args = parser.parse_args()

    rows = coverage_rows(load_records(args.traits_dir))
    write_report(rows, args.out)
    statuses = Counter(row["status"] for row in rows)
    print(f"causal graphs: {len(rows)}")
    for status in ("PASS", "NONMECHANISTIC", "GAP", "PROTECTED", "ERROR"):
        print(f"  {status.lower():16s} {statuses[status]}")
    print(f"wrote {args.out}")

    return gate_exit_code(rows, args.fail_on)


def gate_exit_code(rows: list[dict[str, Any]], fail_on: str) -> int:
    """Map the coverage rows and a ``--fail-on`` class to a process exit code."""
    errors = sum(int(row["error_count"]) for row in rows)
    gaps = sum(int(row["gap_count"]) for row in rows if row["status"] != "PROTECTED")
    protected_gaps = sum(
        int(row["gap_count"]) for row in rows if row["status"] == "PROTECTED"
    )
    if fail_on == "errors":
        return int(errors > 0)
    if fail_on == "gaps":
        return int(errors > 0 or gaps > 0)
    if fail_on == "any":
        return int(errors > 0 or gaps > 0 or protected_gaps > 0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
