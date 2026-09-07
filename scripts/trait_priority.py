#!/usr/bin/env python3
"""Build a TraitMech curation queue with a recommended action per record (#448).

Ported from DisMech's MONDO prioritiser (`monarch-initiative/dismech`,
`src/dismech/compare/mondo_priority.py` + `src/dismech/priority_dashboard.py`).
What is taken is the DESIGN:

  * a weighted score whose every component is inspectable and retunable in YAML,
    rather than a hard-coded ranking;
  * explicit specificity heuristics that resolve to a recommended ACTION --
    curate this as a root, lump it into its parent, drop it -- so the output is a
    decision rather than a number;
  * a static dashboard generated from the same scoring code as the CLI, so the
    page and the terminal can never disagree.

ONE RULE IS DELIBERATELY INVERTED, and it is the reason this is a port rather
than a copy. DisMech penalises a subtype series hard (`subtype_series_penalty:
-18`) and recommends `LUMP_INTO_PARENT`, because in MONDO an over-split series is
usually redundant term proliferation. TraitMech's binned families --
`temperature_range_{low,mid1..4,high,very_low}`, `ph_delta_*`, `nacl_*` -- look
identical in shape but are not redundant. The live sibling, child/parent, and
structural-edge overlap measurements are emitted in the CLI and dashboard
rather than frozen in this docstring (#481). They show that the bins carry
distinct mechanism content, and lumping them would discard real curation.
Series membership is therefore reported as INFORMATION, and
`LUMP_INTO_PARENT` fires only when measured sibling overlap exceeds
`series_lump_min_sibling_overlap`. Nothing in the corpus currently reaches that
threshold, which is the correct outcome and not a bug.

This also replaces the retired completeness-audit prioritizer. That tool mixed
live graph topology with a paid point-in-time `missing_modules` snapshot that
has no local regeneration path (#443, #480); this queue reads live corpus state
only.

THREE RULES IN THE LADDER CURRENTLY NEVER FIRE, and that is the corpus rather
than a bug. Checked, not assumed:

  BUILD_CAUSAL_GRAPH        0 mechanism records have zero edges.
  CURATE_ROOT_WITH_SUBTYPES 9 records have >=4 children and a thin graph, and
                            all 9 are predicates or upper-ontology classes
                            (`has_ph_observation`, `upper/quality`), so an
                            earlier DROP rule claims them first.
  DROP_GROUPING_TERM        46 labels match a grouping pattern and all 46 are
                            already dropped as non-mechanism or deprecated, so
                            the pattern list is inert as configured.

They are kept because each becomes reachable the moment the corpus changes -- a
newly seeded trait with no graph, or a thin non-`upper` grouping label -- and a
ladder that silently lacks a rung is worse than one with an unused rung. The
counts are printed so an unreachable rule cannot masquerade as a passing check.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_causal_graphs import Corpus, _as_corpus  # noqa: E402

DEFAULT_TRAITS = Path("data/traits")
DEFAULT_CONFIG = Path("conf/trait_priority.yaml")
DEFAULT_RESEARCH = Path("research/traits")
# app/, not pages/: `pages/` must byte-match what render_trait_pages.py produces
# and `audit-derived-reports` enforces that, so a second generator writing there
# reads as staleness. app/ is where TraitMech already keeps generated standalone
# apps (app/discussions/), which is also where DisMech keeps its dashboard.
DEFAULT_HTML = Path("app/dashboard/priority.html")
DEFAULT_JSON = Path("app/dashboard/priority.json")
REVIEWED_EMPTY_CANONICAL_EXAMPLES_ACTION = "REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP"

# Ordered most- to least-specific: the first matching rule wins, exactly as in
# DisMech's `_recommend_action` ladder.
ACTIONS = (
    "DROP_NON_MECHANISM",
    "DROP_DEPRECATED",
    "DROP_GROUPING_TERM",
    "LUMP_INTO_PARENT",
    "CURATE_ROOT_WITH_SUBTYPES",
    "ADD_CANONICAL_EXAMPLES",
    "BUILD_CAUSAL_GRAPH",
    "DEEPEN_CAUSAL_GRAPH",
    "ALREADY_DEEP",
    "CURATE_ROOT",
)


@dataclass
class Record:
    identifier: str
    label: str
    category: str
    slug: str
    term_kind: str
    mapping_status: str
    parents: list[str]
    edges: int
    nodes: int
    orphans: int
    components: int
    examples: int
    node_labels: set[str] = field(default_factory=set)
    edge_signatures: set[tuple[str, str, str]] = field(default_factory=set)
    edges_with_evidence: int = 0
    has_definition: bool = False
    has_definition_source: bool = False
    has_synonyms: bool = False
    has_evidence: bool = False
    canonical_examples_reviewed_empty: bool = False
    researched: bool = False


def researched_slugs(research_dir: Path = DEFAULT_RESEARCH) -> set[tuple[str, str]]:
    """Return (category, slug) pairs with an existing research artifact."""
    found: set[tuple[str, str]] = set()
    if not research_dir.exists():
        return found
    for path in research_dir.rglob("*"):
        if path.is_file():
            stem = re.split(r"-(?:deep-research|edison)-", path.name)[0]
            found.add((path.parent.name, stem))
    return found


def load_config(path: Path = DEFAULT_CONFIG) -> dict[str, Any]:
    cfg = yaml.safe_load(Path(path).read_text())
    for key in ("weights", "caps", "thresholds", "heuristics"):
        if not isinstance(cfg.get(key), dict):
            raise ValueError(f"{path}: missing or malformed '{key}' mapping")
    return cfg


def read_records(
    source: Path | Corpus = DEFAULT_TRAITS, research_dir: Path = DEFAULT_RESEARCH
) -> dict[str, Record]:
    out: dict[str, Record] = {}
    researched = researched_slugs(research_dir)
    for rel, doc in _as_corpus(source):
        p = Path(rel)
        graphs = doc.get("causal_graphs") or []
        examples = doc.get("canonical_examples") or []
        events = doc.get("curation_history") or []
        nodes = [n for g in graphs for n in (g.get("nodes") or [])]
        edges = [e for g in graphs for e in (g.get("edges") or [])]
        wired = {e.get("subject") for e in edges} | {e.get("object") for e in edges}
        rec = Record(
            identifier=doc.get("identifier", rel),
            label=doc.get("label", p.stem),
            category=p.parent.name,
            slug=p.stem,
            term_kind=doc.get("term_kind", ""),
            mapping_status=doc.get("mapping_status", ""),
            parents=list(doc.get("parent_traits") or []),
            edges=len(edges),
            nodes=len(nodes),
            orphans=sum(1 for n in nodes if n.get("node_id") not in wired),
            components=_components(nodes, edges),
            examples=len(examples),
            node_labels={(n.get("label") or "").lower() for n in nodes} - {""},
            edge_signatures={
                (
                    str(edge.get("subject") or ""),
                    str(edge.get("predicate_id") or edge.get("predicate") or ""),
                    str(edge.get("object") or ""),
                )
                for edge in edges
                if edge.get("subject") and edge.get("object")
            },
            edges_with_evidence=sum(1 for e in edges if e.get("evidence")),
            has_definition=bool(doc.get("definition")),
            has_definition_source=bool(doc.get("definition_source")),
            has_synonyms=bool(doc.get("synonyms")),
            has_evidence=bool(doc.get("evidence")),
            canonical_examples_reviewed_empty=(
                not examples
                and any(
                    event.get("action") == REVIEWED_EMPTY_CANONICAL_EXAMPLES_ACTION
                    for event in events
                )
            ),
            researched=(p.parent.name, p.stem) in researched,
        )
        out[rec.identifier] = rec
    return out


def _components(nodes: list[dict], edges: list[dict]) -> int:
    """Connected components over the wired subgraph (orphans counted separately)."""
    adj: dict[str, set[str]] = defaultdict(set)
    for e in edges:
        s, o = e.get("subject"), e.get("object")
        if s and o:
            adj[s].add(o)
            adj[o].add(s)
    seen: set[str] = set()
    count = 0
    for start in adj:
        if start in seen:
            continue
        count += 1
        stack = [start]
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            stack.extend(adj[cur] - seen)
    return count


# --- lumping / splitting -----------------------------------------------------


def family_stem(label: str, patterns: list[str]) -> str | None:
    """The series stem a label belongs to, or None.

    Mirrors DisMech's `_extract_family_stem`: the pattern must expose a named
    `stem` group, so adding a pattern cannot silently change what gets grouped.
    """
    for pattern in patterns:
        m = re.match(pattern, label, flags=re.IGNORECASE)
        if m:
            stem = (m.groupdict().get("stem") or "").strip(" ,")
            if stem:
                return stem
    return None


def is_grouping_term(label: str, patterns: list[str]) -> bool:
    return any(re.search(p, label, flags=re.IGNORECASE) for p in patterns)


def is_non_mechanism(rec: Record, heur: dict[str, Any]) -> bool:
    if rec.term_kind in set(heur.get("non_mechanism_term_kinds") or ()):
        return True
    return rec.category in set(heur.get("non_mechanism_categories") or ())


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def sibling_overlap(members: list[Record]) -> float:
    """Mean pairwise node-label Jaccard across a series.

    This is the measurement that decides whether lumping is defensible, rather
    than the assumption that a shared label prefix implies shared content. The
    current value is emitted in the generated metadata, so corpus drift cannot
    make this explanation disagree with the measurement (#481).
    """
    pairs = [
        jaccard(members[i].node_labels, members[j].node_labels)
        for i in range(len(members))
        for j in range(i + 1, len(members))
    ]
    return sum(pairs) / len(pairs) if pairs else 0.0


def overlap_measurements(
    records: dict[str, Record], families: dict[str, list[Record]]
) -> dict[str, int | float | None]:
    """Return reproducible corpus-level measurements behind the lumping rule.

    Sibling statistics are pair-weighted across all detected series. Parent
    statistics cover direct parent links from a series member to another corpus
    record. A shared structural edge means the same subject node id, grounded
    predicate id (or predicate label when ungrounded), and object node id; it is
    deliberately named precisely rather than described as "byte-identical".
    """
    sibling_values = [
        jaccard(members[i].node_labels, members[j].node_labels)
        for members in families.values()
        for i in range(len(members))
        for j in range(i + 1, len(members))
    ]
    family_members = {
        record.identifier for members in families.values() for record in members
    }
    child_parent_pairs: list[tuple[Record, Record]] = []
    for identifier in sorted(family_members):
        child = records[identifier]
        child_parent_pairs.extend(
            (child, records[parent]) for parent in child.parents if parent in records
        )
    parent_values = [
        jaccard(child.node_labels, parent.node_labels)
        for child, parent in child_parent_pairs
    ]
    return {
        "sibling_pairs": len(sibling_values),
        "mean_sibling_overlap": (
            round(sum(sibling_values) / len(sibling_values), 3)
            if sibling_values
            else None
        ),
        "max_sibling_overlap": round(max(sibling_values), 3) if sibling_values else None,
        "child_parent_pairs": len(child_parent_pairs),
        "mean_child_parent_overlap": (
            round(sum(parent_values) / len(parent_values), 3) if parent_values else None
        ),
        "max_child_parent_overlap": round(max(parent_values), 3) if parent_values else None,
        "child_edges_compared": sum(child.edges for child, _ in child_parent_pairs),
        "shared_structural_edges": sum(
            len(child.edge_signatures & parent.edge_signatures)
            for child, parent in child_parent_pairs
        ),
    }


# --- scoring -----------------------------------------------------------------


def canonical_examples_satisfied(rec: Record, cfg: dict[str, Any]) -> bool:
    """True once exemplars exist or were explicitly reviewed as unfillable."""
    return (
        rec.examples >= cfg["thresholds"]["deep_graph_min_examples"]
        or rec.canonical_examples_reviewed_empty
    )


def score(rec: Record, cfg: dict[str, Any]) -> tuple[float, list[str]]:
    """Return (score, reasons). Reasons are printed so the score is arguable."""
    w, caps, th = cfg["weights"], cfg["caps"], cfg["thresholds"]
    total = 0.0
    why: list[str] = []

    def add(amount: float, reason: str) -> None:
        nonlocal total
        if amount:
            total += amount
            why.append(f"{reason} {amount:+g}")

    if is_non_mechanism(rec, cfg["heuristics"]):
        add(w["non_mechanism"], "not a mechanism record")
        return total, why
    if rec.mapping_status == "DEPRECATED":
        add(w["deprecated"], "deprecated")
        return total, why

    if not rec.edges:
        add(w["missing_causal_graph"], "no causal graph")
    elif rec.edges <= th["thin_graph_max_edges"]:
        add(w["thin_causal_graph"], f"thin graph ({rec.edges} edges)")
    if not rec.examples and not rec.canonical_examples_reviewed_empty:
        add(w["missing_canonical_examples"], "no canonical_examples")
    elif rec.canonical_examples_reviewed_empty:
        why.append("canonical_examples reviewed empty +0")
    if rec.edges and not rec.edges_with_evidence:
        add(w["edges_without_evidence"], "no edge carries evidence")

    extra = min(max(rec.components - 1, 0), caps["per_extra_component"])
    add(extra * w["per_extra_component"], f"{rec.components} components")
    orphans = min(rec.orphans, caps["per_orphan_node"])
    add(orphans * w["per_orphan_node"], f"{rec.orphans} orphan nodes")

    if not rec.has_definition:
        add(w["missing_definition"], "no definition")
    if not rec.has_definition_source:
        add(w["missing_definition_source"], "no definition_source")
    if not rec.has_synonyms:
        add(w["missing_synonyms"], "no synonyms")
    if not rec.has_evidence:
        add(w["missing_evidence"], "no record-level evidence")

    if rec.edges >= th["deep_graph_min_edges"] and canonical_examples_satisfied(rec, cfg):
        add(w["already_deep"], "already deep")
    return total, why


def recommend(
    rec: Record,
    cfg: dict[str, Any],
    *,
    children: int,
    series: str | None,
    series_size: int,
    overlap: float,
) -> str:
    """First matching rule wins, as in DisMech's `_recommend_action`."""
    heur, th = cfg["heuristics"], cfg["thresholds"]
    if is_non_mechanism(rec, heur):
        return "DROP_NON_MECHANISM"
    if rec.mapping_status == "DEPRECATED":
        return "DROP_DEPRECATED"
    if is_grouping_term(rec.label, heur.get("grouping_term_patterns") or []):
        return "DROP_GROUPING_TERM"
    # The inverted rule: only lump when the siblings measurably duplicate.
    if (
        series
        and series_size >= th["series_min_family_size"]
        and overlap >= th["series_lump_min_sibling_overlap"]
    ):
        return "LUMP_INTO_PARENT"
    if children >= th["broad_parent_min_children"] and rec.edges <= th["thin_graph_max_edges"]:
        return "CURATE_ROOT_WITH_SUBTYPES"
    if not rec.edges:
        return "BUILD_CAUSAL_GRAPH"
    if not rec.examples and not rec.canonical_examples_reviewed_empty:
        return "ADD_CANONICAL_EXAMPLES"
    if rec.edges <= th["thin_graph_max_edges"] or rec.components > 1:
        return "DEEPEN_CAUSAL_GRAPH"
    if rec.edges >= th["deep_graph_min_edges"] and canonical_examples_satisfied(rec, cfg):
        return "ALREADY_DEEP"
    return "CURATE_ROOT"


def build_queue(
    source: Path | Corpus = DEFAULT_TRAITS,
    cfg: dict[str, Any] | None = None,
    research_dir: Path = DEFAULT_RESEARCH,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    cfg = cfg or load_config()
    recs = read_records(source, research_dir)
    child_count: dict[str, int] = defaultdict(int)
    for r in recs.values():
        for p in r.parents:
            child_count[p] += 1

    patterns = cfg["heuristics"].get("series_patterns") or []
    families: dict[str, list[Record]] = defaultdict(list)
    stems: dict[str, str | None] = {}
    for r in recs.values():
        stem = family_stem(r.label, patterns)
        stems[r.identifier] = stem
        if stem:
            families[stem.lower()].append(r)
    overlaps = {k: sibling_overlap(v) for k, v in families.items()}

    rows = []
    for r in recs.values():
        stem = stems[r.identifier]
        fam = families.get((stem or "").lower(), [])
        ov = overlaps.get((stem or "").lower(), 0.0)
        s, why = score(r, cfg)
        rows.append(
            {
                "identifier": r.identifier,
                "label": r.label,
                "category": r.category,
                "slug": r.slug,
                "score": round(s, 2),
                "action": recommend(
                    r, cfg, children=child_count[r.identifier], series=stem,
                    series_size=len(fam), overlap=ov,
                ),
                "edges": r.edges,
                "nodes": r.nodes,
                "components": r.components,
                "orphans": r.orphans,
                "examples": r.examples,
                "canonical_examples_reviewed_empty": r.canonical_examples_reviewed_empty,
                "children": child_count[r.identifier],
                "series": stem,
                "series_size": len(fam) if stem else 0,
                "series_overlap": round(ov, 3) if stem else None,
                "researched": r.researched,
                "reasons": why,
            }
        )
    rows.sort(key=lambda x: (-x["score"], x["category"], x["slug"]))

    measured_overlap = overlap_measurements(recs, families)
    meta = {
        "records": len(rows),
        "series_families": len(families),
        # Recorded, not dropped: DisMech's sidecar lesson -- a row excluded from
        # the queue leaves no trace in the file unless the count is written down.
        "excluded_non_mechanism": sum(1 for x in rows if x["action"] == "DROP_NON_MECHANISM"),
        "excluded_deprecated": sum(1 for x in rows if x["action"] == "DROP_DEPRECATED"),
        # Retained for compatibility with existing dashboard consumers: this is
        # the unweighted mean of family means used by the decision rule. The
        # explicitly named pair-weighted measurements below are the review
        # statistics introduced in #481.
        "mean_series_overlap": (
            round(sum(overlaps.values()) / len(overlaps), 3) if overlaps else None
        ),
        **measured_overlap,
        "lump_threshold": cfg["thresholds"]["series_lump_min_sibling_overlap"],
        "unresearched_mechanism_records": sum(
            1 for x in rows if not x["researched"] and not x["action"].startswith("DROP")
        ),
        "actions": {a: sum(1 for x in rows if x["action"] == a) for a in ACTIONS},
    }
    return rows, meta


# --- output ------------------------------------------------------------------


def render_html(rows: list[dict[str, Any]], meta: dict[str, Any], top: int) -> str:
    head = (
        "<!doctype html><meta charset=utf-8>"
        "<title>TraitMech curation priority</title>"
        "<style>body{font:14px/1.5 system-ui,sans-serif;margin:2rem;max-width:1200px}"
        "table{border-collapse:collapse;width:100%}th,td{padding:.35rem .5rem;"
        "border-bottom:1px solid #ddd;text-align:left;vertical-align:top}"
        "th{background:#f4f4f4}code{font-size:.9em}.a{font-weight:600}"
        "tr:hover{background:#fafafa}.n{text-align:right}"
        "figure{margin:0 0 1.5rem}figcaption{color:#555}</style>"
    )
    counts = "".join(
        f"<li><code>{html.escape(a)}</code> &mdash; {n}</li>"
        for a, n in meta["actions"].items()
        if n
    )
    lumped = meta["actions"].get("LUMP_INTO_PARENT", 0)
    lumping_outcome = (
        "Nothing lumps, because the bins carry distinct mechanism content"
        if lumped == 0
        else f"{lumped} record(s) cross the configured redundancy threshold"
    )
    lump = (
        f"<p><strong>Lumping.</strong> {meta['series_families']} binned series detected; "
        f"{meta['sibling_pairs']} sibling pairs have mean node-label overlap "
        f"<strong>{meta['mean_sibling_overlap']}</strong> "
        f"(max {meta['max_sibling_overlap']}); {meta['child_parent_pairs']} direct "
        f"child/parent pairs have mean overlap {meta['mean_child_parent_overlap']} "
        f"(max {meta['max_child_parent_overlap']}). "
        f"Only {meta['shared_structural_edges']} of {meta['child_edges_compared']} child "
        f"edges share the same subject/predicate/object structure with a parent. "
        f"The unweighted mean of family means is {meta['mean_series_overlap']} "
        f"against a lump threshold of {meta['lump_threshold']}. {lumping_outcome} &mdash; "
        f"the rule DisMech applies to MONDO "
        f"subtype series does not transfer unretuned.</p>"
    )
    body = [
        head,
        "<h1>TraitMech curation priority</h1>",
        f"<figure><figcaption>{meta['records']} records; "
        f"{meta['excluded_non_mechanism']} not mechanism records, "
        f"{meta['excluded_deprecated']} deprecated &mdash; both scored to the floor "
        f"rather than dropped silently.</figcaption></figure>",
        f"<p><strong>Research.</strong> {meta['unresearched_mechanism_records']} "
        "mechanism record(s) have no artifact; the rest need existing research "
        "applied, not re-run.</p>",
        f"<ul>{counts}</ul>",
        lump,
        f"<h2>Top {min(top, len(rows))}</h2>",
        "<table><tr><th class=n>score</th><th>action</th><th>trait</th>"
        "<th class=n>edges</th><th class=n>cmp</th><th class=n>orph</th>"
        "<th class=n>ex</th><th>series</th><th>why</th></tr>",
    ]
    for r in rows[:top]:
        series = (
            f"{html.escape(r['series'])} ({r['series_size']}, ov {r['series_overlap']})"
            if r["series"]
            else ""
        )
        body.append(
            f"<tr><td class=n>{r['score']:g}</td>"
            f"<td class=a><code>{html.escape(r['action'])}</code></td>"
            f"<td>{html.escape(r['category'])}/{html.escape(r['slug'])}</td>"
            f"<td class=n>{r['edges']}</td><td class=n>{r['components']}</td>"
            f"<td class=n>{r['orphans']}</td><td class=n>{r['examples']}</td>"
            f"<td>{series}</td><td>{html.escape('; '.join(r['reasons']))}</td></tr>"
        )
    body.append("</table>")
    return "\n".join(body)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--traits-dir", type=Path, default=DEFAULT_TRAITS)
    ap.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    # 0 = all. Previously `--top 0` sliced to nothing while the footer still
    # claimed every row was shown, so the output contradicted itself (#452).
    ap.add_argument("--top", type=int, default=25, help="rows to show (0 = all)")
    ap.add_argument("--action", help="only rows with this recommended action")
    ap.add_argument(
        "--unresearched-only",
        action="store_true",
        help="only mechanism records with no deep-research artifact",
    )
    ap.add_argument("--format", choices=("table", "tsv", "json"), default="table")
    ap.add_argument("--dashboard", action="store_true", help="write the static dashboard")
    ap.add_argument("--html-out", type=Path, default=DEFAULT_HTML)
    ap.add_argument("--json-out", type=Path, default=DEFAULT_JSON)
    args = ap.parse_args()

    rows, meta = build_queue(args.traits_dir, load_config(args.config))
    matched = [r for r in rows if not args.action or r["action"] == args.action]
    if args.unresearched_only:
        matched = [
            r
            for r in matched
            if not r["researched"] and not r["action"].startswith("DROP")
        ]
    shown = matched if args.top == 0 else matched[: args.top]

    if args.dashboard:
        args.html_out.parent.mkdir(parents=True, exist_ok=True)
        args.html_out.write_text(render_html(rows, meta, args.top))
        args.json_out.write_text(json.dumps({"meta": meta, "rows": rows}, indent=2))
        print(f"wrote {args.html_out} and {args.json_out}")

    if args.format == "json":
        print(json.dumps({"meta": meta, "rows": shown}, indent=2))
    elif args.format == "tsv":
        print("score\taction\tcategory\tslug\tedges\tcomponents\torphans\texamples")
        for r in shown:
            print(
                f"{r['score']:g}\t{r['action']}\t{r['category']}\t{r['slug']}\t"
                f"{r['edges']}\t{r['components']}\t{r['orphans']}\t{r['examples']}"
            )
    else:
        print(f"{'score':>6} {'action':<26} {'edg':>3} {'ex':>3}  trait")
        for r in shown:
            print(
                f"{r['score']:6g} {r['action']:<26} {r['edges']:3d} {r['examples']:3d}  "
                f"{r['category']}/{r['slug']}"
            )
        # Derived from what was actually printed, not from the pre-slice list.
        print(
            f"\n{len(shown)} row(s) shown of {len(matched)} matching, "
            f"{meta['records']} total; "
            f"{meta['excluded_non_mechanism']} non-mechanism and "
            f"{meta['excluded_deprecated']} deprecated scored to the floor, not dropped"
        )
        print(
            f"research: {meta['unresearched_mechanism_records']} mechanism record(s) "
            f"have no artifact -- the rest need theirs APPLIED, not re-run"
        )
        print(
            f"lumping: {meta['series_families']} series / {meta['sibling_pairs']} sibling "
            f"pairs, mean overlap {meta['mean_sibling_overlap']} "
            f"(max {meta['max_sibling_overlap']}); child/parent mean "
            f"{meta['mean_child_parent_overlap']}; structural parent-edge overlap "
            f"{meta['shared_structural_edges']}/{meta['child_edges_compared']}; "
            f"threshold {meta['lump_threshold']} "
            f"-> {meta['actions'].get('LUMP_INTO_PARENT', 0)} lumped"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
