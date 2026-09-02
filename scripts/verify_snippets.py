#!/usr/bin/env python3
"""Check `EvidenceItem.snippet` strings against the sources they quote (#623).

WHY THIS EXISTS
---------------
`snippet` is the corpus's anti-hallucination control: a verbatim quote is what
stops a plausible claim entering the knowledge base unsourced. But
``audit_evidence_snippets.py`` only checks a snippet's SHAPE -- ellipsis marker,
length, reuse within a graph, whether it echoes the trait's own research report.
Nothing compares a snippet to the source, because nothing can offline.

That made retrieval the only real control, and it failed. Three defects shipped
into one PR (#618) and passed `audit-snippets` cleanly:

  #619  a PARAPHRASE presented as a verbatim quote -- the sentence did not exist
  #620  an unmarked interior elision, dropping "(P < 0.05)" from mid-quote
  #621  a note asserting a negative the source did not support

All three came from a summarising fetch layer. The same layer returned an
abstract with `Nos2`, `Escherichia` and `Salmonella` silently deleted. A tool
that can drop a gene name can drop a negation.

WHAT IT CATCHES, MEASURED -- AND WHAT IT DOES NOT
-------------------------------------------------
Tested against the three real defects that prompted it:

  #620 interior elision      CAUGHT.  similarity 0.97 -> LIKELY_PARAPHRASE
  #619 heavy paraphrase      NOT CAUGHT. similarity 0.18, token overlap 0.42,
                             so it lands in NOT_IN_ABSTRACT alongside every
                             legitimate full-text quote.

That second line is the honest limit and must not be papered over. Catching a
heavy paraphrase would need a threshold near 0.4, and at that level any
full-text quote about the same subject as the abstract trips it -- the check
would cry wolf until nobody read it. So this tool decisively VERIFIES
abstract-sourced snippets and decisively catches edits to them; it does NOT
replace opening the source, which is the only control that catches a rewrite.

WHAT THIS CAN AND CANNOT CONCLUDE
---------------------------------
Europe PMC serves ABSTRACTS, and many legitimate snippets are quoted from full
text. So the asymmetry is fundamental and is built into the verdicts:

  VERIFIED           the snippet is an exact substring of the abstract.
                     DECISIVE. A substring match cannot be a false positive.

  LIKELY_PARAPHRASE  not a substring, but some abstract sentence is >= the
                     similarity threshold. This is the #619/#620 signature and
                     the reason the tool is worth running. It is a PROMPT, not a
                     verdict: papers routinely restate abstract sentences in the
                     discussion, so a full-text quote can legitimately look like
                     a near-miss.

  NOT_IN_ABSTRACT    not a substring, nothing similar. Almost always a full-text
                     quote. INCONCLUSIVE -- absence of evidence only.

  UNRESOLVED         no record, or the record carries no abstract.

Nothing here is ever reported as proof of fabrication. `--fail-on paraphrase` is
opt-in precisely because the one actionable verdict is the one that can be wrong.

Network-dependent, so it is NOT part of `just qc` -- same placement as
`audit-uniprot`.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"

DEFAULT_THRESHOLD = 0.75
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")
SENT_RE = re.compile(r"(?<=[.!?])\s+")


def normalise(text: str) -> str:
    """Strip markup and collapse whitespace so YAML folding cannot cause a miss.

    Abstracts arrive with `<i>`/`<sub>` markup; snippets arrive folded across
    lines by the YAML writer. Neither difference is a real one.
    """
    return WS_RE.sub(" ", TAG_RE.sub("", text)).strip()


class LookupFailed(Exception):
    """The endpoint could not be reached or answered with an error.

    Kept distinct from "no record" on purpose. A 503 that silently became
    UNRESOLVED would let a fully rate-limited run print an all-UNRESOLVED report
    and exit 0 -- a check that cannot fail, which is the #522 shape and exactly
    what this script exists to argue against. Europe PMC does rate-limit: this
    was found by hammering it during development.
    """


def europepmc_abstract(ref: str, *, timeout: float = 30.0, retries: int = 3,
                       backoff: float = 2.0) -> str | None:
    """Return the abstract for a `PMID:`/`DOI:` reference, or None if unindexed.

    Raises LookupFailed when the endpoint itself could not answer, so a
    transport problem is never mistaken for an absent record.
    """
    if ref.startswith("PMID:"):
        query = f"EXT_ID:{ref[5:]}"
    elif ref.startswith("DOI:"):
        # Unquoted deliberately. Europe PMC's DOI field does NOT accept a quoted
        # value -- `DOI:"10.1073/pnas.1718635115"` returns a non-JSON error page
        # while the bare form returns the record. Caught by this script's own
        # canary against the #619 reference, which came back UNRESOLVED.
        query = f"DOI:{ref[4:]}"
    else:
        return None
    params = {"query": query, "resultType": "core", "format": "json"}
    url = f"{EPMC}?{urllib.parse.urlencode(params)}"
    last = ""
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as fh:
                payload = json.load(fh)
            break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
            last = str(exc)
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))
    else:
        raise LookupFailed(f"{ref}: {last}")
    results = (payload.get("resultList") or {}).get("result") or []
    if not results:
        return None
    return results[0].get("abstractText") or None


def best_sentence_ratio(snippet: str, abstract: str) -> tuple[float, str]:
    """Similarity of the closest abstract sentence, and that sentence.

    Compared per sentence rather than against the whole abstract: a short quote
    inside a long abstract scores near zero globally no matter how close it is
    to one sentence, which would hide exactly the near-miss this looks for.
    """
    best = (0.0, "")
    for sentence in SENT_RE.split(abstract):
        sentence = sentence.strip()
        if not sentence:
            continue
        ratio = SequenceMatcher(None, snippet.lower(), sentence.lower()).ratio()
        if ratio > best[0]:
            best = (ratio, sentence)
    return best


def classify(snippet: str, abstract: str | None, threshold: float) -> tuple[str, float, str]:
    if abstract is None:
        return "UNRESOLVED", 0.0, ""
    snippet_n, abstract_n = normalise(snippet), normalise(abstract)
    if snippet_n and snippet_n in abstract_n:
        return "VERIFIED", 1.0, ""
    ratio, sentence = best_sentence_ratio(snippet_n, abstract_n)
    if ratio >= threshold:
        return "LIKELY_PARAPHRASE", ratio, sentence
    return "NOT_IN_ABSTRACT", ratio, ""


def iter_evidence(doc: dict):
    """Yield (locator, evidence item) over every place evidence can live."""
    for index, item in enumerate(doc.get("evidence") or []):
        yield f"evidence[{index}]", item
    for graph in (doc.get("causal_graphs") or []):
        gid = graph.get("graph_id") or "?"
        for edge in (graph.get("edges") or []):
            tag = f"{gid}:{edge.get('subject')}->{edge.get('object')}"
            for index, item in enumerate(edge.get("evidence") or []):
                yield f"{tag}[{index}]", item
        for node in (graph.get("nodes") or []):
            for example in (node.get("protein_examples") or []):
                tag = f"{gid}:{node.get('node_id')}:{example.get('uniprot_id')}"
                for index, item in enumerate(example.get("evidence") or []):
                    yield f"{tag}[{index}]", item


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--record", action="append", default=[],
                    help="limit to one trait YAML (repeatable); default is the corpus")
    ap.add_argument("--out", type=Path, help="write a TSV report here")
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD,
                    help=f"paraphrase similarity threshold (default {DEFAULT_THRESHOLD})")
    ap.add_argument("--fail-on", choices=("none", "paraphrase"), default="none",
                    help="'paraphrase' exits 1 on any LIKELY_PARAPHRASE. Opt-in: that "
                         "verdict is a prompt, not proof (full text can resemble the abstract)")
    ap.add_argument("--delay", type=float, default=0.25, help="seconds between API calls")
    ap.add_argument("--limit", type=int, help="stop after N distinct references")
    args = ap.parse_args()

    paths = ([Path(r) for r in args.record] if args.record
             else sorted(TRAITS_DIR.rglob("*.yaml")))

    rows: list[dict[str, str]] = []
    cache: dict[str, str | None] = {}
    lookup_failures: list[str] = []
    for path in paths:
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            print(f"WARN: unparseable {path}: {exc}", file=sys.stderr)
            continue
        if not isinstance(doc, dict):
            continue
        rel = str(path.relative_to(REPO_ROOT)) if path.is_absolute() else str(path)
        for locator, item in iter_evidence(doc):
            snippet, ref = item.get("snippet"), item.get("reference") or ""
            if not snippet or not ref.startswith(("PMID:", "DOI:")):
                continue
            if ref not in cache:
                if args.limit is not None and len(cache) >= args.limit:
                    continue
                try:
                    cache[ref] = europepmc_abstract(ref)
                except LookupFailed as exc:
                    lookup_failures.append(str(exc))
                    cache[ref] = None
                time.sleep(args.delay)
            verdict, ratio, near = classify(snippet, cache[ref], args.threshold)
            rows.append({"file": rel, "locator": locator, "reference": ref,
                         "verdict": verdict, "similarity": f"{ratio:.2f}",
                         "snippet": normalise(snippet), "nearest_sentence": near})

    counts: dict[str, int] = {}
    for row in rows:
        counts[row["verdict"]] = counts.get(row["verdict"], 0) + 1

    print("=== snippet source verification (Europe PMC) ===")
    print(f"  checked: {len(rows)} snippet(s) over {len(cache)} distinct reference(s)")
    for verdict in ("VERIFIED", "LIKELY_PARAPHRASE", "NOT_IN_ABSTRACT", "UNRESOLVED"):
        if counts.get(verdict):
            print(f"    {verdict:<18} {counts[verdict]}")
    for row in rows:
        if row["verdict"] == "LIKELY_PARAPHRASE":
            print(f"\n  LIKELY_PARAPHRASE {row['file']} {row['locator']} ({row['reference']}, "
                  f"similarity {row['similarity']})")
            print(f"    snippet : {row['snippet'][:150]}")
            print(f"    abstract: {row['nearest_sentence'][:150]}")
    if counts.get("NOT_IN_ABSTRACT"):
        print("\n  NOT_IN_ABSTRACT is INCONCLUSIVE: Europe PMC serves abstracts, and a "
              "snippet quoted from full text cannot match one.")

    if args.out:
        cols = ["file", "locator", "reference", "verdict", "similarity", "snippet",
                "nearest_sentence"]
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", encoding="utf-8") as fh:
            fh.write("\t".join(cols) + "\n")
            for row in rows:
                fh.write("\t".join(row[c].replace("\t", " ") for c in cols) + "\n")
        print(f"  TSV: {args.out}")

    # A transport failure is ALWAYS fatal, regardless of --fail-on. Otherwise a
    # rate-limited run reports every snippet UNRESOLVED and exits 0, which reads
    # exactly like a clean run over unindexed references.
    if lookup_failures:
        print(f"\n  ERROR: {len(lookup_failures)} reference(s) could not be looked up. "
              f"This run proves NOTHING about them.", file=sys.stderr)
        for failure in lookup_failures[:5]:
            print(f"    {failure}", file=sys.stderr)
        if len(lookup_failures) > 5:
            print(f"    ... and {len(lookup_failures) - 5} more", file=sys.stderr)
        print("  Europe PMC rate-limits; retry with a larger --delay.", file=sys.stderr)
        return 2
    if args.fail_on == "paraphrase" and counts.get("LIKELY_PARAPHRASE"):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
