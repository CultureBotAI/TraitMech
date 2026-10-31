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
REUSED_SNIPPET          the same snippet on several evidence items of one graph
                        — the playbook's "low snippet diversity". Each edge
                        needs a phrase supporting THAT edge. Counted per item
                        rather than per edge, since one edge may carry several.
MISSING_SNIPPET         a reference with no quote at all. Schema-legal, since
                        `snippet` is optional, and the largest category by far.
ECHOES_RESEARCH_REPORT  the snippet also appears in this trait's own research
                        report. Not proof of paraphrase — the report may quote
                        the same source — but it is the signature of the lift
                        this audit exists to catch, so it asks for a check
                        against the source rather than asserting a defect.
UNQUOTED_DEFINITION_SOURCE
                        the record's `definition_source` (`PMID:` or `DOI:`) is
                        absent from record-level `evidence[].reference` while
                        already carrying a verbatim snippet on `causal_graphs`
                        edges or another record in the corpus (#1981).

Baseline ratchet: pre-existing findings are frozen in
``conf/evidence_snippet_baseline.tsv`` and never fail; anything new exits 1.

NOT the same shape as audit_causal_graphs.py, which is set membership on a
4-tuple carrying the locator index and a detail fragment. That shape rotted here
(#270): the index renumbers when an evidence item is deleted, so an improvement
read as a new finding. This keys without the index and compares OCCURRENCE
COUNTS, plus a magnitude ratchet for REUSED_SNIPPET, whose locator has no index
and whose severity lives in its detail (#291).

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
from typing import NamedTuple

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_trait_pages import research_answer  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
RESEARCH_DIR = REPO_ROOT / "research" / "traits"
DEFENSE_FINDER_ARTICLES_MD = (
    REPO_ROOT / "data" / "raw" / "defense_finder" / "wiki" / "List_system_article.md"
)
DEFAULT_BASELINE = REPO_ROOT / "conf" / "evidence_snippet_baseline.tsv"
DEFAULT_REPORT = REPO_ROOT / "reports" / "evidence_snippet_audit.tsv"

FIELDNAMES = ["file", "locator", "defect", "severity", "detail"]

SEVERITY = {
    "ELLIPTICAL_SNIPPET": "ERROR",
    "UNSUPPORTIVE_SNIPPET": "WARN",
    "REUSED_SNIPPET": "WARN",
    "MISSING_SNIPPET": "WARN",
    "ECHOES_RESEARCH_REPORT": "WARN",
    "UNQUOTED_DEFINITION_SOURCE": "WARN",
}

# A snippet shorter than this cannot identify what it supports. Calibrated to
# the corpus: the offenders are single words ("host", "growth", "export"), while
# the shortest legitimate quotes run to a clause. Deliberately not a word count —
# "pH homeostasis" is two words and does real work.
MIN_SNIPPET_CHARS = 12
# Minimum length for a corpus-wide non-elliptical quote on a non-OBJECT_PROPERTY
# record to trigger UNQUOTED_DEFINITION_SOURCE when a CLASS record already cites
# definition_source in evidence[].reference without a snippet (#2002).
MIN_CORPUS_QUOTE_CHARS = 16
# Below this a repeated snippet is more plausibly laziness than a genuinely
# recurring key phrase.
MAX_REUSE_PER_GRAPH = 2


def aes_traits_dir() -> Path:
    """Read the module global at call time, so tests can redirect it."""
    return TRAITS_DIR


def aes_research_dir() -> Path:
    return RESEARCH_DIR


def aes_defense_finder_articles_md() -> Path:
    return DEFENSE_FINDER_ARTICLES_MD


_DOI_TOKEN_RE = re.compile(r"(?:DOI:\s*)?(10\.\d{4,9}/[^\s|,\];\"'>]+)", re.IGNORECASE)
_PMID_TOKEN_RE = re.compile(
    r"(?:PMID:\s*|pubmed\.ncbi\.nlm\.nih\.gov/|ncbi\.nlm\.nih\.gov/pubmed/)(\d{4,10})",
    re.IGNORECASE,
)


def _extract_wiki_dois(text: str) -> set[str]:
    unescaped = (text or "").replace(r"\.", ".")
    dois: set[str] = set()
    for match in _DOI_TOKEN_RE.finditer(unescaped):
        doi_val = match.group(1).rstrip(".,;)")
        if doi_val:
            dois.add(f"DOI:{doi_val}")
    return dois


def _load_defense_finder_ref_aliases(path: Path | None = None) -> dict[str, set[str]]:
    """Load optional DOI:↔PMID: equivalence pairs from List_system_article.md (#2002)."""
    target = path if path is not None else aes_defense_finder_articles_md()
    aliases: dict[str, set[str]] = {}
    if not target.exists():
        return aliases
    for raw_line in target.read_text(encoding="utf-8", errors="replace").splitlines():
        dois = _extract_wiki_dois(raw_line)
        if not dois:
            continue
        pmids = {f"PMID:{m.group(1)}" for m in _PMID_TOKEN_RE.finditer(raw_line)}
        if not pmids and "|" in raw_line:
            for cell in raw_line.split("|"):
                token = cell.strip()
                if re.fullmatch(r"\d{6,10}", token):
                    pmids.add(f"PMID:{token}")
        for doi_ref in dois:
            for pmid_ref in pmids:
                aliases.setdefault(doi_ref, set()).add(pmid_ref)
                aliases.setdefault(f"DOI:{doi_ref[4:].lower()}", set()).add(pmid_ref)
                aliases.setdefault(pmid_ref, set()).add(doi_ref)
    return aliases


_PRIMARY_REF_PREFIXES = (
    "PMID:",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC",
    "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC",
    "https://europepmc.org/article/PPR/",
)


def _record_repeats_def_source(doc: dict, def_source: str) -> bool:
    """Return True if canonical_examples[].reference, synonyms[].source, or causal_graphs[].edges[].evidence[].reference repeats def_source."""
    target = def_source.lower()
    for ex in doc.get("canonical_examples") or []:
        if isinstance(ex, dict):
            ref = _norm(str(ex.get("reference") or "")).lower()
            if ref and ref == target:
                return True
    for syn in doc.get("synonyms") or []:
        if isinstance(syn, dict):
            src = _norm(str(syn.get("source") or "")).lower()
            if src and src == target:
                return True
    for cg in doc.get("causal_graphs") or []:
        if not isinstance(cg, dict):
            continue
        for edge in cg.get("edges") or []:
            if not isinstance(edge, dict):
                continue
            for ev in edge.get("evidence") or []:
                if isinstance(ev, dict):
                    ref = _norm(str(ev.get("reference") or "")).lower()
                    if ref and ref == target:
                        return True
    return False


def _record_wiki_doi_aliases(doc: dict, record_refs: set[str]) -> dict[str, set[str]]:
    """Map DOIs in a record's List_system_article.md rows or confirmed definition_source to quoted primary refs."""
    quoted_primary = {r for r in record_refs if r.startswith(_PRIMARY_REF_PREFIXES)}
    if not quoted_primary:
        return {}
    wiki_dois: set[str] = set()
    has_wiki_ref = False
    for item in doc.get("evidence") or []:
        if not isinstance(item, dict):
            continue
        ref = _norm(str(item.get("reference") or ""))
        if "List_system_article.md" not in ref:
            continue
        has_wiki_ref = True
        snip = _norm(str(item.get("snippet") or ""))
        for doi_ref in _extract_wiki_dois(snip):
            wiki_dois.add(doi_ref)
            wiki_dois.add(f"DOI:{doi_ref[4:].lower()}")
    def_source = _norm(str(doc.get("definition_source") or ""))
    if (
        len(quoted_primary) == 1
        and def_source.startswith("DOI:")
        and def_source not in record_refs
        and (has_wiki_ref or _record_repeats_def_source(doc, def_source))
    ):
        wiki_dois.add(def_source)
        wiki_dois.add(f"DOI:{def_source[4:].lower()}")
    if not wiki_dois:
        return {}
    aliases: dict[str, set[str]] = {}
    for doi_ref in wiki_dois:
        aliases.setdefault(doi_ref, set()).update(quoted_primary)
    for primary_ref in quoted_primary:
        aliases.setdefault(primary_ref, set()).update(wiki_dois)
    return aliases


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


def audit(
    check_reports: bool = True,
    check_definition_sources: bool = False,
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    docs: list[tuple[Path, dict]] = []
    refs_by_record_id: dict[str, set[str]] = {}
    refs_by_parent_id: dict[str, set[str]] = {}
    corpus_quoted_refs_16: set[str] = set()
    ref_aliases = _load_defense_finder_ref_aliases() if check_definition_sources else {}
    for path in sorted(aes_traits_dir().rglob("*.yaml")):
        doc = yaml.safe_load(path.read_text())
        if not isinstance(doc, dict):
            continue
        docs.append((path, doc))
        if check_definition_sources:
            is_object_property = (
                _norm(str(doc.get("term_kind") or "")) == "OBJECT_PROPERTY"
            )
            rec_id = _norm(str(doc.get("identifier") or doc.get("id") or path.stem))
            rec_keys = {
                k
                for k in (
                    _norm(str(doc.get("identifier") or "")),
                    _norm(str(doc.get("id") or "")),
                    _norm(path.stem),
                )
                if k
            }
            parents = [
                _norm(str(p)) for p in (doc.get("parent_traits") or []) if _norm(str(p))
            ]
            quoted: set[str] = set()
            if not is_object_property:
                for _loc, item, _gid in iter_evidence(doc):
                    ref = _norm(str(item.get("reference") or ""))
                    snip = _norm(str(item.get("snippet") or ""))
                    if (ref and len(snip) >= MIN_SNIPPET_CHARS
                            and "..." not in snip and "…" not in snip):
                        quoted.add(ref)
                        if len(snip) >= MIN_CORPUS_QUOTE_CHARS:
                            corpus_quoted_refs_16.add(ref)
            for key in rec_keys or {rec_id}:
                refs_by_record_id.setdefault(key, set()).update(quoted)
            for parent_id in parents:
                refs_by_parent_id.setdefault(parent_id, set()).update(quoted)

    for path, doc in docs:
        rel = _safe_rel(path)
        report_text, prompt_text = (
            research_text(path.parent.name, path.stem)
            if check_reports else ("", ""))
        # Reuse is counted per graph, not per file: two graphs in one trait are
        # separate arguments and may legitimately lean on the same key phrase.
        per_graph: dict[str, dict[str, int]] = {}
        if check_definition_sources:
            is_object_property = (
                _norm(str(doc.get("term_kind") or "")) == "OBJECT_PROPERTY"
            )
            min_snip_chars = 1 if is_object_property else MIN_SNIPPET_CHARS
            record_refs: set[str] = set()
            record_any_refs: set[str] = set()
            for item in doc.get("evidence") or []:
                if not isinstance(item, dict):
                    continue
                ref = _norm(str(item.get("reference") or ""))
                snip = _norm(str(item.get("snippet") or ""))
                if ref:
                    record_any_refs.add(ref)
                if (ref and len(snip) >= min_snip_chars
                        and "..." not in snip and "…" not in snip):
                    record_refs.add(ref)
            def_source = _norm(str(doc.get("definition_source") or ""))
            def_source_in_ev = def_source in record_any_refs
            rec_id = _norm(str(doc.get("identifier") or doc.get("id") or path.stem))
            parents = [
                _norm(str(p)) for p in (doc.get("parent_traits") or []) if _norm(str(p))
            ]
            family_quoted = (
                set(refs_by_record_id.get(rec_id, set()))
                | set(refs_by_parent_id.get(rec_id, set()))
            )
            for parent_id in parents:
                family_quoted.update(refs_by_record_id.get(parent_id, set()))
                family_quoted.update(refs_by_parent_id.get(parent_id, set()))
            def_aliases = set(ref_aliases.get(def_source, set()))
            if def_source.startswith("DOI:"):
                def_aliases.update(
                    ref_aliases.get(f"DOI:{def_source[4:].lower()}", set())
                )
            in_rec_aliases = _record_wiki_doi_aliases(doc, record_refs)
            def_aliases.update(in_rec_aliases.get(def_source, set()))
            if def_source.startswith("DOI:"):
                def_aliases.update(
                    in_rec_aliases.get(f"DOI:{def_source[4:].lower()}", set())
                )
            has_corpus_16_quote = (
                not is_object_property
                and (def_source_in_ev or _record_repeats_def_source(doc, def_source))
                and def_source in corpus_quoted_refs_16
            )
            has_alias_quote = (
                not is_object_property
                and bool(
                    def_aliases & (record_refs | family_quoted | corpus_quoted_refs_16)
                )
            )
            if (def_source.startswith(("PMID:", "DOI:"))
                    and (
                        def_source in family_quoted
                        or has_corpus_16_quote
                        or has_alias_quote
                    )
                    and def_source not in record_refs):
                reason = (
                    "lacks a non-elliptical verbatim snippet in record-level evidence[]"
                    if def_source_in_ev
                    else "is absent from record-level evidence[].reference"
                )
                findings.append({
                    "file": rel,
                    "locator": "definition_source",
                    "defect": "UNQUOTED_DEFINITION_SOURCE",
                    "severity": SEVERITY["UNQUOTED_DEFINITION_SOURCE"],
                    "detail": (
                        f"definition_source={def_source} {reason} despite carrying a "
                        "verbatim snippet on causal_graphs or parent/sibling/child records"
                    ),
                })

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


_INDEX_RE = re.compile(r"\[\d+\]$")


def _key(row: dict[str, str]) -> tuple[str, str, str]:
    """Baseline identity: file, locator WITHOUT its array index, and defect.

    The index has to go. `evidence[1]` renumbers to `evidence[0]` when item 0 is
    deleted, so an unchanged finding became a new one and `just qc` failed on a
    change that strictly improved the corpus — 114 baselined findings sat at
    index >= 1. The remedy a curator reaches for is `--write-baseline`, which
    re-freezes anything genuinely new in the same PR. That is how a ratchet rots
    (#270).

    `detail` goes too, for the same reason at a different granularity: it
    carries the full snippet for ELLIPTICAL/UNSUPPORTIVE and the DOI for
    MISSING, so retyping a still-elliptical snippet or correcting the DOI on a
    still-snippet-less reference flipped the key. audit_causal_graphs.py learned
    this first and keys on only the leading fragment of its detail.

    Dropping both collapses several findings onto one key, which is why the
    baseline carries a COUNT rather than a set of keys — see compare().
    """
    return (row["file"], _INDEX_RE.sub("[]", row["locator"]), row["defect"])


# Defects whose detail leads with a magnitude that can get WORSE without the
# finding count changing. REUSED_SNIPPET is the only aggregate this audit emits:
# one finding per (graph, snippet) whatever the number of items sharing it, with
# the number in the detail. Everything else is per-item, so more of it means
# more findings and the occurrence count already catches it.
#
# UNSUPPORTIVE_SNIPPET is deliberately NOT here even though its detail also leads
# with an integer: that integer is a character count, where larger is BETTER, so
# ratcheting it would flag a snippet growing from 6 chars to 10 as a regression.
MAGNITUDE_DEFECTS = {"REUSED_SNIPPET"}

def _magnitude_key(row: dict[str, str]) -> tuple[str, str, str, str] | None:
    """Identity for a magnitude, or None where magnitude is not ratcheted.

    REUSED_SNIPPET's locator is `{graph_id}:*`, so every reused snippet in one
    graph shares a _key(). Keying the magnitude on the graph alone would let the
    smaller of an uneven pair grow up to the larger unnoticed —
    `trophic_type_classification_axes:*` already carries two rows. The snippet
    itself is the discriminator (#291).

    Cost of that choice, tracked in #292: editing the shared snippet's TEXT
    produces an unseen key here. That is no longer the end of the story —
    :func:`_baselined_magnitude` resolves an unseen key against the graph's ONLY
    baselined magnitude where there is exactly one, which is safe because there
    is then nothing smaller to grow into something larger. Read that function
    before concluding this key is unmitigated.

    It still fails closed where the graph carries MORE than one baselined
    magnitude — `trophic_type_classification_axes:*` is the only such graph
    today, and the case this key was written for: falling back to a per-key max
    there would let the smaller group be reworded and grown to the larger's
    magnitude, restoring exactly the sheltering this key removes.
    """
    if row.get("defect") not in MAGNITUDE_DEFECTS:
        return None
    match = re.search(r"share one snippet: (.+)$", row.get("detail", ""))
    return (*_key(row), match.group(1) if match else "")


def _magnitude(row: dict[str, str]) -> int:
    """The leading integer of `detail`, for defects where more is worse.

    Ratcheted as a VALUE, not folded into the key. Putting it in the key would
    reintroduce the rot #270 fixed from the other side: 3 -> 2 is an
    improvement, and a key carrying the count would make it an unbaselined
    finding and fail. audit_causal_graphs.py keys on the leading token for the
    same information and accepts that cost; a value comparison does not have to.
    """
    if row.get("defect") not in MAGNITUDE_DEFECTS:
        return 0
    match = re.match(r"\s*(\d+)", row.get("detail", ""))
    return int(match.group(1)) if match else 0


class Baseline(NamedTuple):
    """What the frozen backlog accepted: how many, and how bad.

    Both maps travel together rather than one being a module global, so
    compare() is a pure function of its arguments and the tests exercise the
    magnitude branch by constructing a Baseline instead of poking a global.
    """

    counts: dict[tuple[str, str, str], int]
    magnitudes: dict[tuple[str, str, str, str], int]


def load_baseline(path: Path) -> Baseline:
    """Baselined occurrences per key.

    A count, not a set. Keying without the index means `evidence[0]` and
    `evidence[1]` share a key, so set membership would let a THIRD missing
    snippet at `evidence[2]` match a baselined key and pass silently — trading a
    false positive for a false negative inside the integrity mechanism. The
    count says "two of these were accepted"; a third is new.
    """
    counts: dict[tuple[str, str, str], int] = {}
    magnitudes: dict[tuple[str, str, str, str], int] = {}
    if not path.exists():
        return Baseline(counts, magnitudes)
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            key = _key(row)
            counts[key] = counts.get(key, 0) + 1
            mkey = _magnitude_key(row)
            if mkey is not None:
                magnitudes[mkey] = max(magnitudes.get(mkey, 0), _magnitude(row))
    return Baseline(counts, magnitudes)


def compare(findings: list[dict[str, str]],
            baseline: Baseline) -> list[dict[str, str]]:
    """Findings in excess of what the baseline accepted.

    Two ways to exceed it: more occurrences at a key than were frozen, or an
    aggregate finding whose magnitude is worse than the frozen one. Fewer
    occurrences, or a smaller magnitude, is an improvement and passes.

    Note which ROW is reported for a count excess: findings are walked in audit
    order and the ones PAST the baselined count are marked, so the row named is
    the last at that key rather than the one that is new. Adding a snippet-less
    reference at evidence[0] points a curator at evidence[2]. The exit code is
    right and a count-based key cannot do better — the occurrences are
    interchangeable by construction.
    """
    seen: dict[tuple[str, str, str], int] = {}
    new: list[dict[str, str]] = []
    for row in findings:
        key = _key(row)
        seen[key] = seen.get(key, 0) + 1
        if seen[key] > baseline.counts.get(key, 0):
            new.append(row)
        elif _magnitude(row) > _baselined_magnitude(row, baseline):
            # Same key, same occurrence count, but worse — a graph going from 3
            # shared snippets to 9 is one REUSED_SNIPPET finding either way
            # (#291).
            new.append(row)
    return new


def _baselined_magnitude(row: dict[str, str], baseline: "Baseline") -> int:
    """The magnitude this row is ratcheted against, tolerating a reworded snippet.

    The exact magnitude key folds the snippet TEXT in, because two reuse groups
    in one graph share a ``_key()`` and keying on the graph alone would let the
    smaller grow up to the larger unnoticed (#291). The cost was that EDITING a
    shared snippet — rewording it, not diversifying it — produced an unseen key,
    so its baselined magnitude read as 0, any count beat it, and a curator was
    told something got worse when nothing had. The remedy they reach for is
    ``--write-baseline``, which is the rot #270 was about (#292).

    #292 rejected falling back to the graph's per-key MAX, correctly: with two
    baselined groups of 4 and 2, the 2 could be reworded and grown to 4 while
    the max sheltered it.

    That objection needs two groups. When the graph has exactly ONE baselined
    magnitude under this key there is nothing smaller to grow into something
    larger, so the fallback is safe by construction rather than by luck —
    a reworded snippet is compared against the only magnitude it could be.

    NOT ONLY A REWORDING, and that is deliberate rather than a hole. Without
    content matching, a reworded snippet is indistinguishable from a REPLACEMENT
    — the baselined group diversified away and a genuinely different snippet
    reused at or below the same magnitude. Both are accepted, and both satisfy
    the ratchet's contract: nothing got worse. Growth is still caught, because
    the comparison is on magnitude, and a NEW group in the graph is caught
    earlier by the occurrence count in :func:`compare`.
    Measured on the current baseline: 13 REUSED_SNIPPET rows across 12 graphs,
    and one graph (trophic_type, the case #291 was written about) carries two.
    So this covers eleven of twelve and leaves the twelfth failing closed
    exactly as today.
    """
    mkey = _magnitude_key(row)
    if mkey is None:
        return 0
    if mkey in baseline.magnitudes:
        return baseline.magnitudes[mkey]
    key = _key(row)
    siblings = [m for k, m in baseline.magnitudes.items() if k[:len(key)] == key]
    return siblings[0] if len(siblings) == 1 else 0


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
    ap.add_argument("--check-definition-sources", action="store_true",
                    help="also warn when definition_source (PMID:/DOI:) is quoted on "
                         "causal_graphs or parent/sibling records but omitted from "
                         "record-level evidence[].reference (#1981)")
    args = ap.parse_args(argv)

    findings = audit(
        check_reports=not args.no_report_check,
        check_definition_sources=args.check_definition_sources,
    )
    write_tsv(Path(args.report), findings)

    if args.write_baseline:
        write_tsv(Path(args.baseline), findings)
        print("=== evidence snippet audit: baseline written ===")
        print(f"  froze {len(findings)} findings -> {args.baseline}")
        return 0

    baseline = load_baseline(Path(args.baseline))
    new = compare(findings, baseline)
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
