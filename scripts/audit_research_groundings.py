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
`just qc` (nor in audit-derived-reports, which must stay offline-runnable).
Two reasons:

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
    just report-research-groundings
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
BACKLOG_TSV = REPO_ROOT / "reports" / "research_grounding_backlog.tsv"

# Sentinel distinguishing "the lookup could not run" from "the id is absent".
ADAPTER_ERROR = object()

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

# Both lookups are casefolded. The reports spell prefixes inconsistently —
# `metpo:1000650` and `doi:10.1371/...` both occur — and a case-sensitive test
# sent 25 truncated `doi:10` fragments into UNKNOWN_PREFIX, inflating the
# backlog with evidence citations that are not groundings at all (#261).
_ADAPTERS_CF = {k.casefold(): v for k, v in ADAPTERS.items()}
_NO_ADAPTER_CF = {p.casefold() for p in NO_ADAPTER}

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
        self._empty: dict[str, bool] = {}

    def _adapter(self, prefix: str):
        if prefix not in self._adapters:
            from oaklib import get_adapter
            self._adapters[prefix] = get_adapter(_ADAPTERS_CF[prefix.casefold()])
        return self._adapters[prefix]

    def lookup(self, curie: str):
        """Return (canonical_label, synonyms, obsolete), None, or ADAPTER_ERROR.

        None means the adapter opened and the id is genuinely absent.
        ADAPTER_ERROR means the lookup could not be performed at all — a failed
        semsql download, an empty sqlite stub, an OAK change. Conflating them
        would let a broken toolchain rewrite the committed TSV to ~1200
        "not in the ontology" rows and exit 0, which reads as a catastrophic
        finding about the corpus rather than a broken tool (#262). The vendored
        validator draws the same distinction for the same reason.
        """
        if curie in self._cache:
            return self._cache[curie]
        prefix = curie.split(":", 1)[0].casefold()
        result = None
        try:
            adapter = self._adapter(prefix)
        except Exception:
            self._cache[curie] = ADAPTER_ERROR
            return ADAPTER_ERROR
        if self._is_empty(prefix, adapter):
            self._cache[curie] = ADAPTER_ERROR
            return ADAPTER_ERROR
        try:
            label = adapter.label(curie)
            if label:
                synonyms = [s for s in (adapter.entity_aliases(curie) or []) if s]
                result = (label, synonyms, self._deprecated(adapter, curie, label))
        except Exception:
            result = ADAPTER_ERROR
        self._cache[curie] = result
        return result

    def _is_empty(self, prefix: str, adapter) -> bool:
        """True if the adapter opened but holds no terms — a 0-byte sqlite.

        This is the case an exception handler alone misses, and the one that
        matters most: a stub opens cleanly and returns None for every label, so
        every pair would fall through to UNRESOLVED and the committed backlog
        would silently become ~1200 "not in the ontology" rows (#265).

        Peeks one entity rather than counting, and caches per prefix. A probe
        that RAISES is not treated as empty — a partially-migrated live ontology
        fails the same way, and calling that empty would hide real findings.
        Same reasoning as AdapterPool._is_empty in the vendored validator.
        """
        if prefix in self._empty:
            return self._empty[prefix]
        try:
            empty = next(iter(adapter.entities()), None) is None
        except Exception as exc:
            print(f"  ! emptiness probe failed for {prefix}: {exc}",
                  file=sys.stderr)
            empty = False
        if empty:
            print(f"  ! {prefix}: adapter opened but holds no terms — every "
                  "lookup for this prefix is ADAPTER_ERROR, not a finding",
                  file=sys.stderr)
        self._empty[prefix] = empty
        return empty

    @staticmethod
    def _deprecated(adapter, curie: str, label: str) -> bool:
        """Prefer OAK's deprecation flag over the label-prefix convention.

        `obsolete ...` is a GO/OBO labelling habit, not a guarantee — CHEBI
        deprecates without relabelling, so a label-only test scores an obsolete
        CHEBI id as OK_LABEL (#264). The string check stays as a fallback for
        adapters that do not expose the flag.
        """
        try:
            meta = adapter.entity_metadata_map(curie) or {}
            flag = meta.get("deprecated") or meta.get("owl:deprecated")
            if isinstance(flag, list):
                flag = flag[0] if flag else None
            if flag is not None:
                return str(flag).lower() in ("true", "1")
        except Exception:
            pass
        return label.lower().startswith("obsolete")


# Triage order. A verdict is a kind of finding, not a degree of one, so ranking
# by verdict first stops the 39 OBSOLETE findings — including GO:0009405, the
# case a label check cannot see — from sorting below every DRIFT (#264).
VERDICT_RANK = {
    "ADAPTER_ERROR": 0,   # the tool is broken; nothing below is trustworthy
    "UNRESOLVED": 1,      # the id does not exist
    "OBSOLETE": 2,        # the id is deprecated
    "DRIFT": 3,           # the id exists and means something else
    "UNKNOWN_PREFIX": 4,  # outside the grounding policy
}


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
    if resolved is ADAPTER_ERROR:
        return "ADAPTER_ERROR", "", 0.0
    if resolved is None:
        return "UNRESOLVED", "", 0.0
    canonical, synonyms, obsolete = resolved
    raw_names = [n for n in [canonical, *synonyms] if n]
    names = [normalize(n) for n in raw_names]
    if obsolete:
        # Similarity is meaningless here — the label often MATCHES, which is
        # exactly why a label-only check misses it. Ordering is by verdict
        # first (see VERDICT_RANK), so this value never buries the finding.
        return "OBSOLETE", canonical, 0.0
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
                    help=f"per-occurrence TSV (default: {REPORT_TSV.relative_to(REPO_ROOT)})")
    ap.add_argument("--backlog", default=str(BACKLOG_TSV),
                    help=f"ranked, deduplicated backlog TSV "
                         f"(default: {BACKLOG_TSV.relative_to(REPO_ROOT)})")
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
            prefix = curie.split(":", 1)[0].casefold()
            if prefix not in _ADAPTERS_CF:
                if prefix not in _NO_ADAPTER_CF:
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

    actionable = [r for r in rows if r["verdict"] in VERDICT_RANK]
    # Ranked by verdict, then least-similar first within a verdict, so a
    # wholesale mis-grounding leads and a lexical variant of the right term
    # trails. Deduplicated: the same suggestion recurs across reports and a
    # curator decides it once, so the backlog carries an occurrence count
    # rather than one line per site.
    distinct = sorted(
        {(r["curie"], r["claimed_label"], r["ontology_label"], r["verdict"],
          r["similarity"]) for r in actionable},
        key=lambda t: (VERDICT_RANK.get(t[3], 9), float(t[4]), t[0], t[1]),
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

    checked = sum(n for v, n in counts.items() if v != "UNKNOWN_PREFIX")

    # The backlog is the deliverable: ranked, deduplicated, one line per thing a
    # curator has to decide. Writing it only to stdout left the 490-item list
    # nowhere on disk, and nobody triages from a console scrollback (#263). The
    # full per-occurrence dump stays in the other file, for locating every site
    # of a suggestion once it has been judged.
    backlog_path = Path(args.backlog)
    backlog_path.parent.mkdir(parents=True, exist_ok=True)
    occurrences: dict[tuple[str, str], int] = {}
    for r in actionable:
        key = (r["curie"], r["claimed_label"])
        occurrences[key] = occurrences.get(key, 0) + 1
    with backlog_path.open("w", newline="") as fh:
        # A vintage line, because this report is not wired into
        # audit-derived-reports and so nothing else will notice it going stale.
        # Corpus counts rather than a wall-clock timestamp: a date would change
        # on every regeneration and make the file churn, whereas these move only
        # when the inputs or the findings actually do.
        fh.write(f"# generated by scripts/audit_research_groundings.py from "
                 f"{len(reports)} reports; {checked} pairs checked; "
                 f"{len(distinct)} distinct findings\n")
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(["verdict", "curie", "claimed_label", "ontology_label",
                         "similarity", "occurrences"])
        for curie, claimed, canonical, verdict, score in distinct:
            writer.writerow([verdict, curie, claimed, canonical, score,
                             occurrences.get((curie, claimed), 1)])

    print(f"=== research grounding drift ({len(reports)} reports) ===")
    print(f"  (id, label) pairs checked against an ontology: {checked}")
    for verdict in ("OK_LABEL", "OK_IN_ROW", "DRIFT", "OBSOLETE",
                    "UNRESOLVED", "ADAPTER_ERROR", "UNKNOWN_PREFIX"):
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
    if counts.get("ADAPTER_ERROR"):
        print("  WARNING: ontology lookups failed for "
              f"{counts['ADAPTER_ERROR']} pairs — treat every verdict below as "
              "provisional and check the OAK semsql downloads.", file=sys.stderr)
    print(f"  backlog TSV:     {backlog_path}")
    print(f"  all occurrences: {out_path}")
    # Always 0: see the module docstring. The blocking gate is validate-products,
    # over the curated tables these suggestions feed into.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
