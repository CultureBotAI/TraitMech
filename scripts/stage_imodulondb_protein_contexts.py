"""Stage iModulonDB component-gene matches for TraitMech review.

The input is JSONL exported from normalized
``kg_microbe_sources.imodulondb.ImodulonGene`` rows plus the dataset-local
``k`` and optional ``imodulon`` / ``imodulon_id`` metadata for each component.

Only exact UniProt joins against existing TraitMech ``protein_examples`` are
staged. iModulonDB membership is computational transcriptomics context: it can
tell a reviewer which source organism, dataset, and module to inspect, but it
does not replace the primary-source evidence required by ``ProteinExample``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections.abc import Iterable
from dataclasses import asdict, dataclass, fields
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
REPORT_DIR = REPO_ROOT / "reports" / "imodulondb"

UNIPROT_RE = re.compile(
    r"^(?:UniProtKB:)?"
    r"(?P<accession>[OPQ][0-9][A-Z0-9]{3}[0-9]|"
    r"[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})$"
)
EMPTY = {"", "-", ".", "na", "n/a", "none", "null", "nan"}
GUARDRAIL = (
    "iModulonDB membership is computational expression-module context; "
    "review the iModulonDB component, source organism, and primary literature "
    "before using it as TraitMech protein-example evidence."
)


class ImodulonStageError(RuntimeError):
    """Raised when source rows cannot be staged deterministically."""


@dataclass(frozen=True)
class ImodulonComponent:
    organism: str
    dataset: str
    k: int
    imodulon_id: str
    imodulon_name: str
    gene_id: str
    gene_locus: str
    gene_name: str
    gene_product: str
    weight: float
    in_imodulon: bool
    cog: str
    all_regulators: str
    string_id: str
    uniprot_id: str
    uniprot_protein_name: str
    uniprot_function: str


@dataclass(frozen=True)
class ProteinExampleMatch:
    trait_file: str
    trait_id: str
    trait_label: str
    trait_category: str
    graph_id: str
    graph_title: str
    node_id: str
    node_label: str
    node_grounding: str
    protein_label: str
    gene_symbol: str
    taxon_id: str
    taxon_label: str
    role: str


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    organism: str
    dataset: str
    k: int
    imodulon_id: str
    imodulon_name: str
    gene_id: str
    gene_name: str
    gene_product: str
    gene_locus: str
    weight: float
    all_regulators: str
    string_id: str
    uniprot_id: str
    uniprot_protein_name: str
    uniprot_function: str
    trait_file: str
    trait_id: str
    trait_label: str
    trait_category: str
    graph_id: str
    graph_title: str
    node_id: str
    node_label: str
    node_grounding: str
    existing_protein_label: str
    existing_gene_symbol: str
    existing_taxon_id: str
    existing_taxon_label: str
    existing_role: str
    evidence_guardrail: str


@dataclass(frozen=True)
class BlockedRow:
    block_reason: str
    block_detail: str
    organism: str
    dataset: str
    k: int | str
    imodulon_id: str
    gene_id: str
    gene_name: str
    uniprot_id: str


@dataclass(frozen=True)
class StageResult:
    candidates: list[Candidate]
    blocked: list[BlockedRow]


def _is_empty(value: str | None) -> bool:
    return value is None or value.strip().lower() in EMPTY


def normalize_uniprot(value: str | None) -> str | None:
    """Return a schema-canonical UniProtKB CURIE, or None when invalid."""
    if _is_empty(value):
        return None
    raw = str(value).strip()
    match = UNIPROT_RE.fullmatch(raw)
    if not match:
        return None
    return f"UniProtKB:{match.group('accession')}"


def _context(line_no: int, key: str) -> str:
    return f"line {line_no}: {key}"


def _required_string(raw: dict[str, Any], key: str, line_no: int) -> str:
    value = raw.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ImodulonStageError(f"{_context(line_no, key)} must be a non-empty string")
    return value.strip()


def _optional_string(raw: dict[str, Any], key: str, line_no: int) -> str:
    value = raw.get(key)
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ImodulonStageError(f"{_context(line_no, key)} must be a string or null")
    return "" if _is_empty(value) else value.strip()


def _required_float(raw: dict[str, Any], key: str, line_no: int) -> float:
    value = raw.get(key)
    if isinstance(value, bool) or not isinstance(value, int | float):
        raise ImodulonStageError(f"{_context(line_no, key)} must be a number")
    return float(value)


def _required_bool(raw: dict[str, Any], key: str, line_no: int) -> bool:
    value = raw.get(key)
    if not isinstance(value, bool):
        raise ImodulonStageError(f"{_context(line_no, key)} must be a boolean")
    return value


def _required_int(raw: dict[str, Any], key: str, line_no: int) -> int:
    value = raw.get(key)
    if isinstance(value, bool):
        raise ImodulonStageError(f"{_context(line_no, key)} must be an integer")
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    raise ImodulonStageError(f"{_context(line_no, key)} must be an integer")


def load_component(raw: Any, line_no: int) -> ImodulonComponent:
    """Load one normalized iModulonDB JSON object."""
    if not isinstance(raw, dict):
        raise ImodulonStageError(f"line {line_no}: expected a JSON object")
    k = _required_int(raw, "k", line_no)
    return ImodulonComponent(
        organism=_required_string(raw, "organism", line_no),
        dataset=_required_string(raw, "dataset", line_no),
        k=k,
        imodulon_id=_optional_string(raw, "imodulon_id", line_no) or str(k),
        imodulon_name=_optional_string(raw, "imodulon", line_no)
        or _optional_string(raw, "imodulon_name", line_no),
        gene_id=_required_string(raw, "gene_id", line_no),
        gene_locus=_optional_string(raw, "gene_locus", line_no),
        gene_name=_optional_string(raw, "gene_name", line_no),
        gene_product=_optional_string(raw, "gene_product", line_no),
        weight=_required_float(raw, "weight", line_no),
        in_imodulon=_required_bool(raw, "in_imodulon", line_no),
        cog=_optional_string(raw, "cog", line_no),
        all_regulators=_optional_string(raw, "all_regulators", line_no),
        string_id=_optional_string(raw, "string_id", line_no),
        uniprot_id=_optional_string(raw, "uniprot_id", line_no),
        uniprot_protein_name=_optional_string(raw, "uniprot_protein_name", line_no),
        uniprot_function=_optional_string(raw, "uniprot_function", line_no),
    )


def iter_jsonl(path: Path) -> Iterable[ImodulonComponent]:
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                raw = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ImodulonStageError(f"line {line_no}: malformed JSON: {exc.msg}") from exc
            yield load_component(raw, line_no)


def _relative(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def load_protein_examples(
    traits_dir: Path = TRAITS_DIR,
) -> dict[str, list[ProteinExampleMatch]]:
    """Index existing TraitMech protein examples by UniProtKB CURIE."""
    matches: dict[str, list[ProteinExampleMatch]] = {}
    for path in sorted(traits_dir.glob("*/*.yaml")):
        try:
            record = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as exc:
            raise ImodulonStageError(f"could not parse {path}: {exc}") from exc
        if not isinstance(record, dict):
            raise ImodulonStageError(f"{path} must contain a mapping")
        for graph in record.get("causal_graphs") or []:
            if not isinstance(graph, dict):
                continue
            for node in graph.get("nodes") or []:
                if not isinstance(node, dict) or node.get("node_type") != "GENE_OR_PROTEIN":
                    continue
                for example in node.get("protein_examples") or []:
                    if not isinstance(example, dict):
                        continue
                    uniprot_id = normalize_uniprot(str(example.get("uniprot_id") or ""))
                    if not uniprot_id:
                        continue
                    matches.setdefault(uniprot_id, []).append(
                        ProteinExampleMatch(
                            trait_file=_relative(path),
                            trait_id=str(record.get("identifier") or ""),
                            trait_label=str(record.get("label") or ""),
                            trait_category=str(record.get("trait_category") or ""),
                            graph_id=str(graph.get("graph_id") or ""),
                            graph_title=str(graph.get("title") or ""),
                            node_id=str(node.get("node_id") or ""),
                            node_label=str(node.get("label") or ""),
                            node_grounding=str(node.get("grounding") or ""),
                            protein_label=str(example.get("protein_label") or ""),
                            gene_symbol=str(example.get("gene_symbol") or ""),
                            taxon_id=str(example.get("taxon_id") or ""),
                            taxon_label=str(example.get("taxon_label") or ""),
                            role=str(example.get("role") or ""),
                        )
                    )
    return matches


def _candidate_id(component: ImodulonComponent, uniprot_id: str, match: ProteinExampleMatch) -> str:
    key = "|".join(
        [
            component.organism,
            component.dataset,
            str(component.k),
            uniprot_id,
            match.trait_id,
            match.graph_id,
            match.node_id,
        ]
    )
    digest = hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]
    return f"imodulondb-{digest}"


def _blocked(component: ImodulonComponent, reason: str, detail: str) -> BlockedRow:
    return BlockedRow(
        block_reason=reason,
        block_detail=detail,
        organism=component.organism,
        dataset=component.dataset,
        k=component.k,
        imodulon_id=component.imodulon_id,
        gene_id=component.gene_id,
        gene_name=component.gene_name,
        uniprot_id=component.uniprot_id,
    )


def stage_components(
    components: Iterable[ImodulonComponent],
    protein_examples: dict[str, list[ProteinExampleMatch]],
) -> StageResult:
    """Join components to TraitMech protein examples and return review rows."""
    candidates: list[Candidate] = []
    blocked: list[BlockedRow] = []
    seen_ids: set[str] = set()

    for component in components:
        normalized_uniprot = normalize_uniprot(component.uniprot_id)
        if not component.in_imodulon:
            blocked.append(
                _blocked(component, "OUTSIDE_IMODULON", "below the component threshold")
            )
            continue
        if _is_empty(component.uniprot_id):
            blocked.append(_blocked(component, "NO_UNIPROT", "no UniProt accession"))
            continue
        if not normalized_uniprot:
            blocked.append(_blocked(component, "INVALID_UNIPROT", "invalid UniProt accession"))
            continue

        matches = protein_examples.get(normalized_uniprot, [])
        if not matches:
            blocked.append(
                _blocked(
                    component,
                    "NO_TRAIT_PROTEIN_EXAMPLE",
                    "accession is absent from TraitMech protein_examples",
                )
            )
            continue

        for match in matches:
            candidate_id = _candidate_id(component, normalized_uniprot, match)
            if candidate_id in seen_ids:
                raise ImodulonStageError(
                    f"duplicate iModulonDB candidate key for {candidate_id}"
                )
            seen_ids.add(candidate_id)
            candidates.append(
                Candidate(
                    candidate_id=candidate_id,
                    organism=component.organism,
                    dataset=component.dataset,
                    k=component.k,
                    imodulon_id=component.imodulon_id,
                    imodulon_name=component.imodulon_name,
                    gene_id=component.gene_id,
                    gene_name=component.gene_name,
                    gene_product=component.gene_product,
                    gene_locus=component.gene_locus,
                    weight=component.weight,
                    all_regulators=component.all_regulators,
                    string_id=component.string_id,
                    uniprot_id=normalized_uniprot,
                    uniprot_protein_name=component.uniprot_protein_name,
                    uniprot_function=component.uniprot_function,
                    trait_file=match.trait_file,
                    trait_id=match.trait_id,
                    trait_label=match.trait_label,
                    trait_category=match.trait_category,
                    graph_id=match.graph_id,
                    graph_title=match.graph_title,
                    node_id=match.node_id,
                    node_label=match.node_label,
                    node_grounding=match.node_grounding,
                    existing_protein_label=match.protein_label,
                    existing_gene_symbol=match.gene_symbol,
                    existing_taxon_id=match.taxon_id,
                    existing_taxon_label=match.taxon_label,
                    existing_role=match.role,
                    evidence_guardrail=GUARDRAIL,
                )
            )

    candidates.sort(key=lambda row: row.candidate_id)
    blocked.sort(
        key=lambda row: (
            row.block_reason,
            row.organism,
            row.dataset,
            row.k,
            row.gene_id,
            row.uniprot_id,
        )
    )
    return StageResult(candidates=candidates, blocked=blocked)


def write_reports(result: StageResult, report_dir: Path = REPORT_DIR) -> None:
    """Write JSONL/TSV/Markdown staging reports."""
    report_dir.mkdir(parents=True, exist_ok=True)

    jsonl_path = report_dir / "candidates.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for candidate in result.candidates:
            handle.write(json.dumps(asdict(candidate), sort_keys=True) + "\n")

    candidate_tsv = report_dir / "candidates.tsv"
    with candidate_tsv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[field.name for field in fields(Candidate)],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(asdict(candidate) for candidate in result.candidates)

    blocked_tsv = report_dir / "blocked.tsv"
    with blocked_tsv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[field.name for field in fields(BlockedRow)],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(asdict(row) for row in result.blocked)

    by_reason: dict[str, int] = {}
    for row in result.blocked:
        by_reason[row.block_reason] = by_reason.get(row.block_reason, 0) + 1

    lines = [
        "# iModulonDB TraitMech staging summary",
        "",
        f"- Candidates: {len(result.candidates)}",
        f"- Blocked rows: {len(result.blocked)}",
    ]
    for reason in sorted(by_reason):
        lines.append(f"- {reason}: {by_reason[reason]}")
    lines.append("")
    lines.append(GUARDRAIL)
    lines.append("")
    (report_dir / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jsonl", type=Path, help="normalized iModulonDB component JSONL")
    parser.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    parser.add_argument("--report-dir", type=Path, default=REPORT_DIR)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write reports/imodulondb artifacts; dry-run only by default",
    )
    args = parser.parse_args(argv)

    try:
        protein_examples = load_protein_examples(args.traits_dir)
        result = stage_components(iter_jsonl(args.jsonl), protein_examples)
    except ImodulonStageError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"TraitMech UniProt accessions indexed: {len(protein_examples)}")
    print(f"iModulonDB candidates: {len(result.candidates)}")
    print(f"blocked rows: {len(result.blocked)}")
    if args.apply:
        write_reports(result, args.report_dir)
        print(f"reports written to {args.report_dir}")
    else:
        print("dry-run: pass --apply to write reports")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
