#!/usr/bin/env python3
"""Structural audit of evidence snippets across the trait corpus.

``EvidenceItem.snippet`` is specified as a *verbatim quote from the source*
(``traitmech.yaml``), and ``docs/CURATION_PLAYBOOK.md`` sharpens that to
"verbatim, contiguous ... no ellipsis, no paraphrase", diversified across edges.
Until now nothing in this repo checked any of it — the enforcement was a human
PR reviewer, which is why the corpus already carries violations nobody logged.

This exists because of #183's backfill. Adding evidence-backed edges to 220
fragmented graphs means writing thousands of new snippets, and the obvious
shortcut is to paste the evidence cell out of a deep-research report. Those
cells are explicitly paraphrase — nine reports say so in as many words — so the
shortcut silently converts an anti-hallucination control into decoration. A
ratchet is the point: land green, then refuse to let the backfill make it worse.

Defects
-------
ELLIPTICAL_SNIPPET      contains "..." or "…", so it is stitched rather than
                        contiguous. An explicit playbook violation.
UNSUPPORTIVE_SNIPPET    too short to support any specific claim ("host",
                        "toxins"). Satisfies the field without doing its job.
REUSED_SNIPPET          the same snippet on several edges of one graph — the
                        playbook's "low snippet diversity". Each edge needs a
                        phrase supporting THAT edge.
MISSING_SNIPPET         a reference with no quote at all. Schema-legal, since
                        `snippet` is optional, and the largest category by far.
ECHOES_RESEARCH_REPORT  the snippet also appears in this trait's own research
                        report. Not proof of paraphrase — the report may quote
                        the same source — but it is the signature of the lift
                        this audit exists to catch, so it asks for a check
                        against the source rather than asserting a defect.

Baseline ratchet, same shape as audit_causal_graphs.py: pre-existing findings
are frozen in ``conf/evidence_snippet_baseline.tsv`` and never fail; anything
new exits 1.

Usage:
    just audit-snippets
    just audit-snippets --write-baseline     # freeze today's corpus
    just audit-snippets --fail-on any        # once burned down
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_trait_pages import research_answer  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
RESEARCH_DIR = REPO_ROOT / "research" / "traits"
DEFAULT_BASELINE = REPO_ROOT / "conf" / "evidence_snippet_baseline.tsv"
DEFAULT_REPORT = REPO_ROOT / "reports" / "evidence_snippet_audit.tsv"

FIELDNAMES = ["file", "locator", "defect", "severity", "detail"]

SEVERITY = {
    "ELLIPTICAL_SNIPPET": "ERROR",
    "UNSUPPORTIVE_SNIPPET": "WARN",
    "REUSED_SNIPPET": "WARN",
    "MISSING_SNIPPET": "WARN",
    "ECHOES_RESEARCH_REPORT": "WARN",
}

# A snippet shorter than this cannot identify what it supports. Calibrated to
# the corpus: the offenders are single words ("host", "growth", "export"), while
# the shortest legitimate quotes run to a clause. Deliberately not a word count —
# "pH homeostasis" is two words and does real work.
MIN_SNIPPET_CHARS = 12
# Below this a repeated snippet is more plausibly laziness than a genuinely
# recurring key phrase.
MAX_REUSE_PER_GRAPH = 2


def aes_traits_dir() -> Path:
    """Read the module global at call time, so tests can redirect it."""
    return TRAITS_DIR


def aes_research_dir() -> Path:
    return RESEARCH_DIR


def _safe_rel(path: Path) -> str:
    """Repo-relative where possible, absolute otherwise.

    relative_to() raises for a path outside the repo, which would make the audit
    un-runnable against a fixture tree. Mirrors _safe_rel in the vendored
    id-label validator.
    """
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "")).strip()


def _fold(text: str) -> str:
    """Casefold, drop punctuation, then re-collapse whitespace.

    The second collapse is load-bearing. Stripping punctuation turns a
    standalone "…" or " — " into a run of spaces, so the snippet folds with a
    double space where the report's prose folds with one and the substring test
    fails. That silently weakened the check on elliptical snippets — the ones
    most worth verifying against a source (#269).
    """
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", "", _norm(text).lower())).strip()


def research_text(category: str, slug: str) -> tuple[str, str]:
    """Return (folded answer text, folded text the provider was GIVEN).

    Direction is the whole difficulty. A curated snippet turning up in a report
    proves nothing on its own, because the pipeline feeds the trait's EXISTING
    evidence into the prompt as `evidence_summary` — so the report can be
    echoing the curator rather than the curator lifting from the report. Two
    layers of that confound are stripped here:

      * the front matter and the twice-echoed prompt, via research_answer() —
        the same trim the page renderer uses (#233). Without it, every
        curator-written snippet matched its own reflection: 257 findings.

      * the `evidence_summary` the provider was shown, which it frequently
        restates in its answer. `arsenic_tolerant` evidence[0] is the worked
        case: the snippet was in the prompt verbatim, so the answer repeating it
        says nothing about where the YAML got it.

    What survives is text in the answer that was NOT handed to the provider —
    which is the signal worth a curator's attention.
    """
    answers, given = [], []
    for path in sorted(aes_research_dir().glob(f"{category}/{slug}-deep-research-*.md")):
        if re.search(r"[-.]citations\.md$", path.name):
            continue
        raw = path.read_text()
        answers.append("\n".join(research_answer(raw)))
        given.append(_prompt_evidence(raw))
    return _fold(" ".join(answers)), _fold(" ".join(given))


def _prompt_evidence(raw: str) -> str:
    """The `evidence_summary` handed to the provider, or '' if unreadable.

    Parsed defensively: a malformed front matter must degrade to "we were shown
    nothing", which only ever adds findings for a human to dismiss, never
    suppresses one silently.
    """
    if not raw.startswith("---"):
        return ""
    try:
        front = yaml.safe_load(raw.split("---", 2)[1])
    except Exception:
        return ""
    if not isinstance(front, dict):
        return ""
    variables = front.get("template_variables")
    if not isinstance(variables, dict):
        return ""
    return str(variables.get("evidence_summary") or "")


def iter_evidence(doc: dict):
    """Yield (locator, evidence_item, graph_id) over a trait document.

    Record-level evidence and per-edge evidence are both checked: the schema
    describes the same field the same way in both places.
    """
    for i, item in enumerate(doc.get("evidence") or []):
        if isinstance(item, dict):
            yield f"evidence[{i}]", item, None
    for graph in doc.get("causal_graphs") or []:
        if not isinstance(graph, dict):
            continue
        graph_id = graph.get("graph_id", "?")
        for edge in graph.get("edges") or []:
            if not isinstance(edge, dict):
                continue
            subject = edge.get("subject", "?")
            obj = edge.get("object", "?")
            for j, item in enumerate(edge.get("evidence") or []):
                if isinstance(item, dict):
                    yield f"{graph_id}:{subject}->{obj}[{j}]", item, graph_id


def audit(check_reports: bool = True) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for path in sorted(aes_traits_dir().rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        if not isinstance(doc, dict):
            continue
        rel = _safe_rel(path)
        report_text, prompt_text = (
            research_text(path.parent.name, path.stem)
            if check_reports else ("", ""))
        # Reuse is counted per graph, not per file: two graphs in one trait are
        # separate arguments and may legitimately lean on the same key phrase.
        per_graph: dict[str, dict[str, int]] = {}

        for locator, item, graph_id in iter_evidence(doc):
            reference = _norm(str(item.get("reference") or ""))
            snippet = _norm(str(item.get("snippet") or ""))

            if not snippet:
                if reference:
                    findings.append({
                        "file": rel, "locator": locator,
                        "defect": "MISSING_SNIPPET",
                        "severity": SEVERITY["MISSING_SNIPPET"],
                        "detail": f"reference={reference} has no snippet",
                    })
                continue

            if "..." in snippet or "…" in snippet:
                findings.append({
                    "file": rel, "locator": locator,
                    "defect": "ELLIPTICAL_SNIPPET",
                    "severity": SEVERITY["ELLIPTICAL_SNIPPET"],
                    "detail": f"non-contiguous quote: {snippet[:120]!r}",
                })
            elif len(snippet) < MIN_SNIPPET_CHARS:
                findings.append({
                    "file": rel, "locator": locator,
                    "defect": "UNSUPPORTIVE_SNIPPET",
                    "severity": SEVERITY["UNSUPPORTIVE_SNIPPET"],
                    "detail": f"{len(snippet)} chars, supports nothing specific: "
                              f"{snippet!r}",
                })

            if report_text:
                folded = _fold(snippet)
                # Short strings match by coincidence; only a substantial span
                # appearing in the report is evidence of a lift.
                if (len(folded) >= 40 and folded in report_text
                        and folded not in prompt_text):
                    findings.append({
                        "file": rel, "locator": locator,
                        "defect": "ECHOES_RESEARCH_REPORT",
                        "severity": SEVERITY["ECHOES_RESEARCH_REPORT"],
                        "detail": "also appears in this trait's research report, "
                                  "whose evidence text may be paraphrase — verify "
                                  f"against {reference or 'the source'}",
                    })

            if graph_id:
                counts = per_graph.setdefault(graph_id, {})
                counts[snippet] = counts.get(snippet, 0) + 1

        for graph_id, counts in per_graph.items():
            for snippet, n in sorted(counts.items()):
                if n > MAX_REUSE_PER_GRAPH:
                    findings.append({
                        "file": rel, "locator": f"{graph_id}:*",
                        "defect": "REUSED_SNIPPET",
                        "severity": SEVERITY["REUSED_SNIPPET"],
                        # "evidence items", not "edges": an edge may carry more
                        # than one item, so the count is of items sharing the
                        # snippet, which is what was actually measured (#269).
                        "detail": f"{n} evidence items share one snippet: "
                                  f"{snippet[:100]!r}",
                    })
    return findings


def _key(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (row["file"], row["locator"], row["defect"], row["detail"])


def load_baseline(path: Path) -> set[tuple[str, str, str, str]]:
    if not path.exists():
        return set()
    with path.open() as fh:
        return {_key(row) for row in csv.DictReader(fh, delimiter="\t")}


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, delimiter="\t", lineterminator="\n",
                                fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(sorted(rows, key=_key))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--baseline", default=str(DEFAULT_BASELINE))
    ap.add_argument("--report", default=str(DEFAULT_REPORT))
    ap.add_argument("--write-baseline", action="store_true",
                    help="freeze the current findings as the accepted backlog")
    ap.add_argument("--fail-on", choices=("new", "error", "any"), default="new",
                    help="new (default) = any finding not in the baseline fails; "
                         "error = only new ERROR-severity findings fail; "
                         "any = every finding fails and the baseline is ignored")
    ap.add_argument("--no-report-check", action="store_true",
                    help="skip ECHOES_RESEARCH_REPORT (which reads research/)")
    args = ap.parse_args(argv)

    findings = audit(check_reports=not args.no_report_check)
    write_tsv(Path(args.report), findings)

    if args.write_baseline:
        write_tsv(Path(args.baseline), findings)
        print("=== evidence snippet audit: baseline written ===")
        print(f"  froze {len(findings)} findings -> {args.baseline}")
        return 0

    baseline = load_baseline(Path(args.baseline))
    new = [r for r in findings if _key(r) not in baseline]
    if args.fail_on == "any":
        blocking = findings
    elif args.fail_on == "error":
        blocking = [r for r in new if r["severity"] == "ERROR"]
    else:
        blocking = new

    counts: dict[str, int] = {}
    for row in findings:
        counts[row["defect"]] = counts.get(row["defect"], 0) + 1

    print("=== evidence snippet audit ===")
    print(f"  findings: {len(findings)}  (baselined: {len(findings) - len(new)}, "
          f"new: {len(new)}, blocking: {len(blocking)})")
    for defect in sorted(counts, key=lambda d: -counts[d]):
        print(f"    {defect:<24} {counts[defect]:>5}  [{SEVERITY[defect]}]")
    print(f"  TSV: {args.report}")

    for row in blocking[:20]:
        print(f"  ! {row['file']}  {row['locator']}  {row['defect']}: "
              f"{row['detail']}", file=sys.stderr)
    if len(blocking) > 20:
        print(f"  ... and {len(blocking) - 20} more", file=sys.stderr)
    return 1 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
