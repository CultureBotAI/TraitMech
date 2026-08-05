#!/usr/bin/env python3
"""Triage report: do the CURIEs suggested in research reports mean what the
reports say they mean?

The deep-research sweep (#183, #241) produced 353 reports whose candidate-node
tables pair a human label with an ontology identifier. Nothing resolved those
identifiers, and a sample against OLS found the long tail materially wrong —
`CHEBI:10357` offered as "ectoine" is (-)-beta-caryophyllene, `ENVO:01000992`
as "cold stress" is *shower fixture*, `GO:0042599` as "magnetosome" is *lamellar
body* (#243). These tables are what a curator copies from when grounding causal
nodes, and since #233/#253 they are also rendered onto trait pages.

REPORT, NOT A GATE. It exits 0 whatever it finds, and is deliberately not in
`just qc`. Two reasons:

  * The reports are provider output. Nobody is going to hand-edit 353 of them,
    so failing a build on their contents would gate work on data no one intends
    to correct in place. The blocking gate belongs where curated data is —
    `mappings/node_grounding.tsv`, which `just validate-products` already
    covers.
  * Extraction from prose tables is heuristic (see `table_pairs`), so some
    findings are judgement calls rather than defects.

The value is a curator seeing "this suggestion does not resolve to what the
report claims" BEFORE lifting it into a grounding table.

Not built on scripts/validate_id_label_correspondence.py: that file is vendored
byte-identical across the Mech repos and drift-checked against CultureMech by
the `vendored-sync` CI job, so extending it here would fail CI. Its config
vocabulary is mirrored where it makes sense (adapters, canonical-or-synonym
policy) so the two read alike.

Usage:
    just audit-research-groundings
    python scripts/audit_research_groundings.py --limit 1     # canary
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = REPO_ROOT / "research" / "traits"
REPORT_TSV = REPO_ROOT / "reports" / "research_grounding_drift.tsv"

# Prefixes with an OAK sqlite adapter. Mirrors conf/id_label_targets.yaml, minus
# RO — the reports suggest node groundings, not predicates.
ADAPTERS = {
    "GO": "sqlite:obo:go",
    "CHEBI": "sqlite:obo:chebi",
    "ENVO": "sqlite:obo:envo",
    "PATO": "sqlite:obo:pato",
    "UBERON": "sqlite:obo:uberon",
    "CL": "sqlite:obo:cl",
}
# Real identifiers with no OAK sqlite to check them against. Named rather than
# ignored by omission, so a typoed prefix (CHBEI:) still shows up as unknown
# instead of being silently skipped — the same distinction
# conf/id_label_targets.yaml draws.
NO_ADAPTER = {"METPO", "traitmech", "NCBITaxon", "UniProtKB", "InterPro",
              "EC", "KEGG", "MetaCyc", "Rhea", "PMID", "DOI", "PDB", "Pfam"}

# Letters and underscores only in the prefix, deliberately. Allowing digits
# swept up fatty-acid shorthand — `C16:0`, `C18:1` — as 78 bogus UNKNOWN_PREFIX
# findings that drowned the real ones. No ontology prefix these reports use
# carries a digit.
CURIE_RE = re.compile(r"\b([A-Za-z][A-Za-z_]{1,15}):([0-9]{1,9})\b")


def normalize(text: str) -> str:
    """Lowercase, strip markdown emphasis and punctuation noise."""
    text = re.sub(r"[`*_]+", "", text or "")
    text = re.sub(r"\s+", " ", text)
    return text.strip().strip(".,;:").lower()


def table_pairs(text: str) -> list[tuple[int, str, str, str]]:
    """Yield (line_no, claimed_label, curie, whole_row) from markdown tables.

    The claimed label is the row's FIRST cell, which is how these tables are
    laid out — `| infection thread | \\`GO:0009860\\` where applicable | … |`.
    That is a heuristic: a row can mention an id in passing while naming a
    different node, which is why the whole row travels with the pair and why
    this script reports rather than fails.
    """
    out: list[tuple[int, str, str, str]] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        # Header separator rows (|---|---|) carry no content.
        if all(set(c) <= set("-: ") for c in cells):
            continue
        claimed = normalize(cells[0])
        if not claimed:
            continue
        seen: set[str] = set()
        for match in CURIE_RE.finditer(line):
            curie = f"{match.group(1)}:{match.group(2)}"
            if curie in seen:
                continue
            seen.add(curie)
            out.append((line_no, claimed, curie, line.strip()))
    return out


class Ontologies:
    """Lazily-opened OAK adapters, with a per-CURIE cache.

    Lazy because opening six semsql databases costs more than most runs need,
    and cached because the corpus repeats ids heavily — `CHEBI:15378` appears
    eight times.
    """

    def __init__(self) -> None:
        self._adapters: dict[str, object] = {}
        self._cache: dict[str, tuple[str, list[str], bool] | None] = {}

    def _adapter(self, prefix: str):
        if prefix not in self._adapters:
            from oaklib import get_adapter
            self._adapters[prefix] = get_adapter(ADAPTERS[prefix])
        return self._adapters[prefix]

    def lookup(self, curie: str) -> tuple[str, list[str], bool] | None:
        """Return (canonical_label, synonyms, obsolete), or None if unresolved."""
        if curie in self._cache:
            return self._cache[curie]
        prefix = curie.split(":", 1)[0]
        result: tuple[str, list[str], bool] | None = None
        try:
            adapter = self._adapter(prefix)
            label = adapter.label(curie)
            if label:
                synonyms = [s for s in (adapter.entity_aliases(curie) or []) if s]
                result = (label, synonyms, label.lower().startswith("obsolete"))
        except Exception:
            # A missing or broken adapter must not abort a 600-pair run; the
            # pair is reported as unresolved, which is the honest verdict.
            result = None
        self._cache[curie] = result
        return result


def _collapse(text: str) -> str:
    """Reduce to comparable characters: lowercase alphanumerics only."""
    return re.sub(r"[^a-z0-9]+", "", normalize(text))


def similarity(claimed: str, names: list[str]) -> float:
    """Best 0-1 resemblance between the claimed label and any ontology name.

    DRIFT mixes two populations that a single verdict cannot separate: genuine
    mis-groundings (`ectoine` for (-)-beta-caryophyllene, sharing nothing) and
    lexical variants of the right term (`fumarate` for *fumaric acid*,
    `10-formyl-tetrahydrofolate` for *10-formyltetrahydrofolic acid*). Scoring
    the distance lets the first sort to the top instead of being buried by the
    second. CHEBI in particular does not list `proton` as a synonym of *hydron*,
    so chemically-correct pairs do reach this bucket.
    """
    claimed_collapsed = _collapse(claimed)
    if not claimed_collapsed:
        return 0.0
    import difflib
    return max(
        (difflib.SequenceMatcher(None, claimed_collapsed, _collapse(n)).ratio()
         for n in names if _collapse(n)),
        default=0.0,
    )


def classify(claimed: str, row: str, resolved) -> tuple[str, str, float]:
    """Return (verdict, canonical_label, similarity)."""
    if resolved is None:
        return "UNRESOLVED", "", 0.0
    canonical, synonyms, obsolete = resolved
    raw_names = [n for n in [canonical, *synonyms] if n]
    names = [normalize(n) for n in raw_names]
    if obsolete:
        return "OBSOLETE", canonical, 1.0
    if any(n and (n == claimed or n in claimed or claimed in n) for n in names):
        return "OK_LABEL", canonical, 1.0
    # The report may name the term correctly while using it as a comparison —
    # `| symbiosome | GO:0043663 (host cell part) is too broad | …`. Saying what
    # the id means, anywhere in the row, is not a mis-grounding.
    row_norm = normalize(row)
    if any(n and n in row_norm for n in names):
        return "OK_IN_ROW", canonical, 1.0
    return "DRIFT", canonical, similarity(claimed, raw_names)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=0,
                    help="only scan the first N reports (0 = all); use 1 to canary")
    ap.add_argument("--report", default=str(REPORT_TSV),
                    help=f"output TSV (default: {REPORT_TSV.relative_to(REPO_ROOT)})")
    args = ap.parse_args()

    reports = [
        p for p in sorted(RESEARCH_DIR.rglob("*-deep-research-*.md"))
        if not re.search(r"[-.]citations\.md$", p.name)
    ]
    if args.limit:
        reports = reports[: args.limit]
    if not reports:
        print("no research reports found — is research/ tracked?", file=sys.stderr)
        return 0

    ontologies = Ontologies()
    rows: list[dict[str, str]] = []
    counts: dict[str, int] = {}
    skipped_prefixes: dict[str, int] = {}

    for path in reports:
        rel = path.relative_to(REPO_ROOT).as_posix()
        for line_no, claimed, curie, row in table_pairs(path.read_text()):
            prefix = curie.split(":", 1)[0]
            if prefix not in ADAPTERS:
                if prefix not in NO_ADAPTER:
                    # An unrecognised prefix is a typo or a new ontology, and
                    # either way wants a human — not silence.
                    counts["UNKNOWN_PREFIX"] = counts.get("UNKNOWN_PREFIX", 0) + 1
                    rows.append({
                        "file": rel, "line": str(line_no), "curie": curie,
                        "claimed_label": claimed, "ontology_label": "",
                        "verdict": "UNKNOWN_PREFIX", "similarity": "0.00",
                        "row": row,
                    })
                else:
                    skipped_prefixes[prefix] = skipped_prefixes.get(prefix, 0) + 1
                continue
            verdict, canonical, score = classify(
                claimed, row, ontologies.lookup(curie))
            counts[verdict] = counts.get(verdict, 0) + 1
            rows.append({
                "file": rel, "line": str(line_no), "curie": curie,
                "claimed_label": claimed, "ontology_label": canonical,
                "verdict": verdict, "similarity": f"{score:.2f}", "row": row,
            })

    actionable = [r for r in rows
                  if r["verdict"] in ("DRIFT", "OBSOLETE", "UNRESOLVED", "UNKNOWN_PREFIX")]
    # Sorted worst-first and deduplicated by (curie, claimed_label): the same
    # bad suggestion recurs across reports, and a curator fixes it once.
    # Least-similar first, so a wholesale mis-grounding leads and a lexical
    # variant of the right term trails. Deduplicated by (curie, claimed_label):
    # the same suggestion recurs across reports and is fixed once.
    distinct = sorted(
        {(r["curie"], r["claimed_label"], r["ontology_label"], r["verdict"],
          r["similarity"]) for r in actionable},
        key=lambda t: (float(t[4]), t[0], t[1]),
    )

    out_path = Path(args.report)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh, delimiter="\t", lineterminator="\n",
            fieldnames=["file", "line", "curie", "claimed_label",
                        "ontology_label", "verdict", "similarity", "row"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"=== research grounding drift ({len(reports)} reports) ===")
    print(f"  checkable (id, label) pairs: {sum(counts.values())}")
    for verdict in ("OK_LABEL", "OK_IN_ROW", "DRIFT", "OBSOLETE",
                    "UNRESOLVED", "UNKNOWN_PREFIX"):
        if counts.get(verdict):
            print(f"    {verdict:<15} {counts[verdict]:>5}")
    if skipped_prefixes:
        skipped = ", ".join(f"{p}={n}" for p, n in sorted(skipped_prefixes.items()))
        print(f"  no OAK adapter, not checked: {skipped}")
    print(f"  distinct actionable suggestions: {len(distinct)}")
    for curie, claimed, canonical, verdict, score in distinct[:15]:
        print(f"    {verdict:<13} {curie:<16} report says '{claimed}'"
              + (f" — ontology says '{canonical}'" if canonical else "")
              + (f"  [{score}]" if verdict == "DRIFT" else ""))
    if len(distinct) > 15:
        print(f"    ... and {len(distinct) - 15} more")
    print(f"  TSV: {out_path}")
    # Always 0: see the module docstring. The blocking gate is validate-products,
    # over the curated tables these suggestions feed into.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
