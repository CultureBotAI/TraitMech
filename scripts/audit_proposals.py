#!/usr/bin/env python3
"""Citation-bar audit for PROPOSED TraitRecords.

Candidate traits proposed from literature research (mapping_status: PROPOSED)
must each be backed by at least two *distinct* literature citations, counted
across `definition_source` and every `evidence[].reference`. LinkML/JSON-Schema
validation cannot express a count spread over two different slots, so this
cross-field rule lives here, alongside the other `qc` audit probes
(audit_schema.py, audit_writers.py).

A PROPOSED record FAILS if either:
  - it carries fewer than MIN_CITATIONS distinct, non-placeholder citations, or
  - any of its citations is not a recognizable reference (PMID:, DOI:, or URL).

SEEDED / REVIEWED / DEPRECATED records are not checked here — they inherit
provenance from METPO and are governed by the schema's own rules.

Usage:
    python scripts/audit_proposals.py [PATH ...]
    python scripts/audit_proposals.py --out reports/proposal_citation_audit.tsv

Paths may be files or directories; directories are walked for *.yaml.
Default scope when no paths given: data/traits/. Exits non-zero on any failure.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Iterable

import yaml

_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOTS = [_REPO_ROOT / "data" / "traits"]
DEFAULT_OUT = _REPO_ROOT / "reports" / "proposal_citation_audit.tsv"

#: Minimum number of distinct literature citations a PROPOSED record must carry.
MIN_CITATIONS = 2

#: A citation that has not actually been supplied yet.
_PLACEHOLDER = re.compile(r"^TODO\b", re.IGNORECASE)

#: A recognizable literature reference: PMID:, DOI:, or a bare URL.
_REFERENCE_SHAPE = re.compile(r"^(PMID:\d+|DOI:\S+|https?://\S+)$", re.IGNORECASE)


def is_placeholder(ref: str) -> bool:
    """True for empty / TODO-style citations that don't count toward the bar."""
    return not ref or not ref.strip() or bool(_PLACEHOLDER.match(ref.strip()))


def is_valid_reference(ref: str) -> bool:
    """True if `ref` looks like a PMID, DOI, or URL citation."""
    return bool(_REFERENCE_SHAPE.match(ref.strip())) if ref else False


def distinct_citations(record: dict) -> list[str]:
    """Distinct, non-placeholder citations across definition_source + evidence.

    Order-preserving (definition_source first, then evidence order) so the
    audit TSV is stable.
    """
    seen: set[str] = set()
    out: list[str] = []
    candidates: list[str] = []
    ds = record.get("definition_source")
    if isinstance(ds, str):
        candidates.append(ds)
    for item in record.get("evidence") or []:
        ref = (item or {}).get("reference")
        if isinstance(ref, str):
            candidates.append(ref)
    for ref in candidates:
        key = ref.strip()
        if is_placeholder(key) or key in seen:
            continue
        seen.add(key)
        out.append(key)
    return out


def audit_record(record: dict, path: str = "") -> dict | None:
    """Audit a single record. Returns a result row for PROPOSED records, else None.

    The row's `passes` is "yes" only when the record meets MIN_CITATIONS and
    every counted citation is a well-formed reference.
    """
    if (record.get("mapping_status") or "").upper() != "PROPOSED":
        return None
    cites = distinct_citations(record)
    malformed = [c for c in cites if not is_valid_reference(c)]
    passes = len(cites) >= MIN_CITATIONS and not malformed
    return {
        "path": path,
        "identifier": record.get("identifier", ""),
        "n_citations": len(cites),
        "citations": "; ".join(cites),
        "malformed": "; ".join(malformed),
        "passes": "yes" if passes else "no",
    }


def iter_yaml_files(roots: Iterable[Path]) -> Iterable[Path]:
    for root in roots:
        if root.is_file() and root.suffix == ".yaml":
            yield root
        elif root.is_dir():
            yield from sorted(root.rglob("*.yaml"))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", type=Path, help="files or dirs (default: data/traits/)")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help="TSV output path")
    args = ap.parse_args(argv)

    roots = args.paths or DEFAULT_ROOTS
    rows: list[dict] = []
    for path in iter_yaml_files(roots):
        try:
            record = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:  # malformed YAML is the strict validator's job
            print(f"WARN: skipping unparseable {path}: {exc}", file=sys.stderr)
            continue
        if not isinstance(record, dict):
            continue
        # Emit repository-relative paths so the TSV is reproducible across
        # contributors and CI (paths under DEFAULT_ROOTS are absolute).
        try:
            display_path = path.resolve().relative_to(_REPO_ROOT)
        except ValueError:
            display_path = path
        row = audit_record(record, str(display_path))
        if row is not None:
            rows.append(row)

    fields = ["path", "identifier", "n_citations", "citations", "malformed", "passes"]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow(row)

    failures = [r for r in rows if r["passes"] == "no"]
    print("", file=sys.stderr)
    print(f"=== proposal citation audit ({len(rows)} PROPOSED records) ===", file=sys.stderr)
    print(f"  minimum distinct citations: {MIN_CITATIONS}", file=sys.stderr)
    print(f"  passing:  {len(rows) - len(failures)} / {len(rows)}", file=sys.stderr)
    print(f"  failing:  {len(failures)}", file=sys.stderr)
    print(f"  TSV:      {args.out}", file=sys.stderr)
    for r in failures:
        reason = "malformed reference(s): " + r["malformed"] if r["malformed"] \
            else f"only {r['n_citations']} distinct citation(s)"
        print(f"  FAIL {r['identifier']} ({r['path']}): {reason}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
