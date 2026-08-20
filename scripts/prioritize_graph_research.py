#!/usr/bin/env python3
"""Rank traits by causal-graph weakness, to pick the next deep-research target.

Deep research is paid and slow, so the choice of trait matters more than the
speed of running it. This ranks the corpus by how thin each trait's
`causal_graphs` are, and reports whether research has already been done -- so
"needs research" is never confused with "needs its existing research applied".

THREE WAYS A NAIVE RANKING GETS THIS WRONG, all measured rather than assumed.

1. NOT EVERY RECORD IS A MECHANISM. 124 of the 477 records carry no causal graph
   at all, so a ranking that treats "no graph" as the weakest graph puts all of
   them on top -- and not one is researchable. 94 are METPO object properties
   seeded into `data/traits` (`uses_for_growth`, `degrades`, `has_phenotype`,
   `exports`): relations, not traits. 7 are datatype properties (`has_value`,
   `is_negative_data`). 20 are DEPRECATED observation classes. 3 are
   upper-ontology classes (`microbe`, `enzyme`, `chemical_entity`). There is no
   mechanism to research in "does not assimilate".

2. UPPER-ONTOLOGY CLASSES THAT *DO* HAVE GRAPHS SCORE HIGH AND ARE STILL NOT
   TARGETS. `material_entity` and `quality` carry three-edge graphs, `phenotype`
   four -- thin enough to rank near the top on weakness alone. A thin graph on
   `quality` is not a research question; it is a sign the graph should probably
   not exist. The whole `upper` category is set aside for that reason, which is
   why the exclusion is by category and not by "has no graph".

3. BINNED SIBLINGS LOOK LIKE ONE QUESTION AND ARE NOT. `ph_delta_mid2`,
   `ph_delta_mid3`, `temperature_range_mid4`, `nacl_range_low` are METPO binning
   classes, and this script used to collapse each family into one row on the
   assumption that one research pass answers the whole family. Measured on the
   live corpus, that assumption is false (#447): mean node-label Jaccard between
   sibling bins is 5% (max 20%), child-vs-parent ~8%, and 18 of 3256 child edges
   are byte-identical to a parent edge. `temperature_range_high` and
   `temperature_range_mid4` share almost no mechanism content, so collapsing hid
   44 records that each need their own work. Series membership is therefore
   reported as INFORMATION (`[series ph_delta, 7 bins]`) and nothing merges by
   default; `--collapse-families` restores the old behaviour for reading the
   queue at family granularity. `scripts/trait_priority.py` (#448) carries the
   measured-overlap version of this rule: lump only above a configured overlap
   threshold, which nothing in the corpus reaches.

Exclusions are always counted and broken down in the output, never silent.
`--include-nonmechanism` shows them.

THE HEADLINE THIS PRODUCES, which is not what the framing "pick a trait for deep
research" expects: the 353 records that CAN carry a mechanism graph all already
DO, and they are exactly the 353 that already have a deep-research artifact. So
no trait is awaiting a first research pass. Every candidate here has been
researched and needs that research APPLIED -- or, if the ranking is being used
to choose a canary for a second provider, needs a deliberate second pass.

WEAKNESS SCORE, and why each term is in it:

  missing_modules * 2   From the Edison completeness audit: mechanism modules
                        the literature has and the graph does not. The only
                        term that reflects what is actually absent rather than
                        what the shape of the graph implies, so it is weighted
                        double. It is also the only input with NO FRESHNESS
                        GUARANTEE (#443): the audit is a point-in-time sweep,
                        the corpus keeps growing, and a verdict written against
                        a 2-edge graph says nothing about the 17-edge graph now
                        on disk. So each report row's `graph_edges` is compared
                        against the live count; a row that no longer matches is
                        marked stale, its missing_modules is REPORTED but
                        EXCLUDED from the score, and when most rows are stale
                        `--sort missing` refuses to run rather than rank on a
                        report describing a corpus that no longer exists
                        (override: --trust-stale-completeness).
  orphan_nodes          Nodes in no edge at all -- asserted and then unused.
  (components - 1) * 2  A graph in pieces cannot answer a question that crosses
                        the pieces; a trait whose own trait node is unreachable
                        from its mechanism is worse than a thin chain.
  max(0, 8 - edges)     A floor term. Below roughly eight edges a graph cannot
                        express a branch and a feedback arm at once, and
                        edges-per-node cannot see this: two nodes and one edge
                        scores 0.5, the same as forty nodes and twenty edges.

The score is a triage heuristic for ordering a queue, not a measurement of
quality. It says "look here first", and the reasons are printed alongside so a
curator can disagree with the ordering on the evidence rather than on faith.

A HIGH SCORE IS NOT THE SAME AS A GOOD RESEARCH TARGET, and the two columns that
separate them pull in opposite directions:

  many components, few missing modules -> a CONNECTIVE gap. The graph has the
      right pieces and never wired them together. `biopolymer_degradation`
      sits on six components, but its edges name endoglucanase, endochitinase
      and lignin oxidative enzymes without connecting any of them to the trait
      or to `assimilable_units`. Nothing in the literature is missing; the
      edges are. This is curation, not research.

  few components, many missing modules -> a CONTENT gap. The graph is coherent
      and incomplete. `nitrogen_fixing_symbiosis` has ONE component, no
      orphans, and the highest missing-module count in the corpus (11) -- though
      that count comes from a stale audit row, so today it is a lead to verify
      against the live graph, not a fact (#443).

So `--sort missing` exists, and it is the right sort when the question is "what
should we RESEARCH" -- provided the completeness audit still describes the
corpus. When most of its rows are stale the sort refuses to run instead of
ranking on it silently (#443). The default composite sort answers "which graph
is worst", which is a different question and usually resolves to curation work.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_causal_graphs import Corpus, _as_corpus  # noqa: E402

DEFAULT_TRAITS = Path("data/traits")
DEFAULT_CONNECTIVITY = Path("reports/causal_graph_connectivity.tsv")
DEFAULT_COMPLETENESS = Path("reports/graph_completeness_audit.tsv")
DEFAULT_RESEARCH = Path("research/traits")

# WHAT COUNTS AS A MECHANISM, decided by schema fields rather than by name.
#
# The first version of this script guessed with a hand-written list of slug
# prefixes ("does_not_", "builds_", "accumulates", ...). It matched 47 of the 94
# predicate records and silently ranked the other 47 -- `uses_for_growth`,
# `has_phenotype`, `exports`, `transports` -- as research candidates. The corpus
# already carries the answer as a declared field, so nothing needs guessing:
#
#   term_kind: OBJECT_PROPERTY   94 records, all graph-less. These are METPO
#                                object properties seeded into data/traits;
#                                `uses_for_growth` is a relation, not a trait.
#   term_kind: DATATYPE_PROPERTY  7 records (`has_value`, `is_negative_data`).
#   mapping_status: DEPRECATED   20 observation records, retired.
#   category `upper`              8 records. Three are graph-less (`microbe`,
#                                `enzyme`, `chemical_entity`); the other five
#                                DO have graphs, and three of those are thin
#                                enough to rank near the top (`material_entity`
#                                and `quality` at 3 edges, `phenotype` at 4).
#                                Excluded by category rather than by emptiness,
#                                because a thin graph on `quality` is not a
#                                research question.
#
# Together these account for every graph-less record in the corpus: 94 + 7 + 20
# + 3 = 124 of 477.
NON_MECHANISM_TERM_KINDS = frozenset({"OBJECT_PROPERTY", "DATATYPE_PROPERTY"})
NON_MECHANISM_CATEGORIES = frozenset({"upper"})


def non_mechanism_reason(category: str, doc: dict) -> str | None:
    """Why this record cannot carry a causal graph, or None if it can.

    Returns the reason rather than a bool so the caller can report the breakdown;
    a count of "82 set aside" invites the question this answers.
    """
    kind = doc.get("term_kind")
    if kind in NON_MECHANISM_TERM_KINDS:
        return kind.lower()
    if doc.get("mapping_status") == "DEPRECATED":
        return "deprecated"
    if category in NON_MECHANISM_CATEGORIES:
        return "upper_ontology"
    return None


# Binned/graded families: everything after the stem is a bin label. Membership
# is reported per row (and drives --collapse-families); it does NOT imply shared
# mechanism content -- measured sibling overlap is 5% (#447). Kept as explicit
# patterns rather than a generic "split on the last underscore", which would
# also group unrelated traits that merely share a prefix.
FAMILY_PATTERNS = (
    re.compile(r"^(temperature_(?:range|optimum|delta))_.+$"),
    re.compile(r"^(ph_(?:range|optimum|delta))_.+$"),
    re.compile(r"^(nacl_(?:range|optimum|delta))_.+$"),
    re.compile(r"^(cell_(?:length|width|diameter))_.+$"),
)


def family_of(slug: str) -> str | None:
    """The binning family a slug belongs to, or None if it stands alone."""
    for pattern in FAMILY_PATTERNS:
        m = pattern.match(slug)
        if m:
            return m.group(1)
    return None


def _read_tsv(path: Path, *keys: str) -> dict[tuple[str, ...], dict[str, str]]:
    """Index a TSV by a COMPOSITE key.

    Keying the completeness report by `slug` alone collapsed any two categories
    that name a trait the same way, losing one verdict silently -- and a lost
    verdict reads as `missing_modules = 0`, pushing that trait DOWN a weakness
    ranking, which is the wrong direction for a triage tool. The report carries a
    `category` column for exactly this reason (#428).
    """
    if not path.exists():
        return {}
    with path.open() as handle:
        return {tuple(row[k] for k in keys): row for row in csv.DictReader(handle, delimiter="\t")}


def researched_slugs(research_dir: Path = DEFAULT_RESEARCH) -> set[tuple[str, str]]:
    """(category, slug) pairs that already have a deep-research artifact.

    Matches on the filename stem before the provider suffix, so a second
    provider's report for the same trait does not read as a different trait.
    """
    found: set[tuple[str, str]] = set()
    if not research_dir.exists():
        return found
    for path in research_dir.rglob("*"):
        if not path.is_file():
            continue
        stem = re.split(r"-(?:deep-research|edison)-", path.name)[0]
        found.add((path.parent.name, stem))
    return found


def score(missing_modules: int, orphans: int, components: int, edges: int) -> int:
    """The weakness score. See the module docstring for why each term is here."""
    return (
        missing_modules * 2
        + orphans
        + max(0, components - 1) * 2
        + max(0, 8 - edges)
    )


def rank(
    source: Path | Corpus = DEFAULT_TRAITS,
    *,
    connectivity: Path = DEFAULT_CONNECTIVITY,
    completeness: Path = DEFAULT_COMPLETENESS,
    research_dir: Path = DEFAULT_RESEARCH,
    include_nonmechanism: bool = False,
    collapse_families: bool = False,
) -> tuple[list[dict], dict[str, int]]:
    """Return (ranked rows, counts of what was set aside and why)."""
    conn = _read_tsv(Path(connectivity), "file")
    comp = _read_tsv(Path(completeness), "category", "slug")
    researched = researched_slugs(Path(research_dir))

    rows: list[dict] = []
    counts = {
        "non_mechanism": 0,
        "no_graph_mechanism": 0,
        "families_collapsed": 0,
        "in_series": 0,
        "no_connectivity_row": 0,
        "completeness_rows_matched": 0,
        "completeness_rows_stale": 0,
    }

    for rel, doc in _as_corpus(source):
        path = Path(rel)
        category, slug = path.parent.name, path.stem
        reason = non_mechanism_reason(category, doc)
        mechanism = reason is None
        if reason:
            counts["non_mechanism"] += 1
            counts[f"excluded_{reason}"] = counts.get(f"excluded_{reason}", 0) + 1
            if not include_nonmechanism:
                continue

        graphs = doc.get("causal_graphs") or []
        nodes = sum(len(g.get("nodes") or []) for g in graphs)
        edges = sum(len(g.get("edges") or []) for g in graphs)
        if mechanism and not graphs:
            counts["no_graph_mechanism"] += 1

        c = conn.get((rel,), {})
        if c:
            components = int(c["components"])
        else:
            # Assuming "fully connected" is the OPTIMISTIC direction: it
            # understates fragmentation and pushes the trait down the ranking.
            # Counted so an incomplete join is visible rather than assumed
            # benign (#431).
            components = 1 if edges else 0
            if edges:
                counts["no_connectivity_row"] += 1
        wired = int(c.get("wired_nodes") or 0)
        v = comp.get((category, slug), {})
        missing = int(v.get("missing_modules") or 0)

        # STALENESS (#443): the completeness audit is a point-in-time sweep with
        # no freshness guarantee, and its verdicts were written against graphs
        # that have since grown (347 of 353 at the time of filing). A row whose
        # recorded edge count no longer matches the live graph is describing a
        # graph that no longer exists, so its missing_modules is reported in the
        # output but excluded from the score.
        stale = False
        if v:
            counts["completeness_rows_matched"] += 1
            reported_edges = int(v.get("graph_edges") or 0)
            if reported_edges != edges:
                stale = True
                counts["completeness_rows_stale"] += 1

        rows.append(
            {
                "category": category,
                "slug": slug,
                "mechanism": mechanism,
                "nodes": nodes,
                "edges": edges,
                "components": components,
                "orphans": max(0, nodes - wired),
                "missing_modules": missing,
                "completeness_stale": stale,
                "verdict": v.get("verdict", ""),
                "researched": (category, slug) in researched,
                "family": family_of(slug),
                # Overwritten below for series members; present on every row so
                # the JSON row schema does not depend on the slug (#472).
                "series_size": 0,
                "score": score(
                    0 if stale else missing, max(0, nodes - wired), components, edges
                ),
            }
        )

    # Series membership is information either way (#447): sibling bins carry
    # distinct mechanism content (measured overlap 5%), so nothing merges unless
    # explicitly asked to.
    series_size: dict[tuple[str, str], int] = {}
    for row in rows:
        if row["family"]:
            key = (row["category"], row["family"])
            series_size[key] = series_size.get(key, 0) + 1
    for row in rows:
        if row["family"]:
            row["series_size"] = series_size[(row["category"], row["family"])]
            counts["in_series"] += 1

    if collapse_families:
        rows, collapsed = _collapse(rows)
        counts["families_collapsed"] = collapsed

    rows.sort(key=lambda r: (-r["score"], r["category"], r["slug"]))
    return rows, counts


def stale_fraction(counts: dict[str, int]) -> float:
    """How much of the completeness audit no longer matches the live corpus."""
    matched = counts.get("completeness_rows_matched", 0)
    if not matched:
        return 0.0
    return counts.get("completeness_rows_stale", 0) / matched


def _collapse(rows: list[dict]) -> tuple[list[dict], int]:
    """Keep the worst member of each binning family, and say how many it stands for."""
    best: dict[tuple[str, str], dict] = {}
    standalone: list[dict] = []
    for row in rows:
        if not row["family"]:
            standalone.append(row)
            continue
        key = (row["category"], row["family"])
        incumbent = best.get(key)
        if incumbent is None or row["score"] > incumbent["score"]:
            row["family_members"] = (incumbent or {}).get("family_members", 0) + 1
            best[key] = row
        else:
            incumbent["family_members"] = incumbent.get("family_members", 1) + 1
    collapsed = sum(r.get("family_members", 1) - 1 for r in best.values())
    merged = standalone + list(best.values())
    for row in merged:
        row.setdefault("family_members", 1)  # uniform row schema (#472)
    return merged, collapsed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--traits-dir", type=Path, default=DEFAULT_TRAITS)
    ap.add_argument("--limit", type=int, default=15, help="rows to print (0 = all)")
    ap.add_argument(
        "--include-nonmechanism",
        action="store_true",
        help="include predicate/upper-ontology/observation records (not researchable)",
    )
    ap.add_argument(
        "--collapse-families",
        action="store_true",
        help="merge each binned series into its worst member. Off by default: "
        "measured sibling overlap is 5%%, so bins are distinct work items (#447)",
    )
    ap.add_argument(
        "--trust-stale-completeness",
        action="store_true",
        help="allow --sort missing even when the completeness audit no longer "
        "matches the live corpus (#443)",
    )
    ap.add_argument("--unresearched-only", action="store_true", help="only traits with no artifact")
    ap.add_argument(
        "--sort",
        choices=("score", "missing", "fragmentation"),
        default="score",
        help="score = worst graph overall; missing = biggest CONTENT gap, the right "
        "sort for choosing a research target; fragmentation = biggest CONNECTIVE gap, "
        "which is curation work rather than research",
    )
    ap.add_argument("--json", dest="as_json", action="store_true")
    args = ap.parse_args()

    connectivity_note = DEFAULT_CONNECTIVITY
    rows, counts = rank(
        args.traits_dir,
        include_nonmechanism=args.include_nonmechanism,
        collapse_families=args.collapse_families,
    )
    staleness = stale_fraction(counts)
    if args.unresearched_only:
        rows = [r for r in rows if not r["researched"]]
    if args.sort == "missing":
        # `--sort missing` ranks PURELY on the completeness audit. Zero matched
        # rows means there is nothing to sort on -- every missing_modules is 0
        # and the "ranking" would be the tie-breaker order wearing the sort's
        # name (#471). No override for this one: trusting zero rows is not a
        # meaningful choice.
        if counts["completeness_rows_matched"] == 0:
            print(
                f"ERROR: --sort missing ranks on {DEFAULT_COMPLETENESS}, but no "
                f"row of it matched the corpus -- every missing_modules is 0 and "
                f"there is nothing to sort on. Regenerate the audit first.",
                file=sys.stderr,
            )
            return 2
        # And when most of the audit no longer matches the corpus the sort is
        # not "somewhat degraded", it is an ordering of a corpus that no longer
        # exists (#443).
        if staleness > 0.5 and not args.trust_stale_completeness:
            print(
                f"ERROR: --sort missing ranks on {DEFAULT_COMPLETENESS}, but "
                f"{counts['completeness_rows_stale']} of "
                f"{counts['completeness_rows_matched']} of its rows no longer match "
                f"the live corpus (graph_edges has moved). Regenerate the audit, or "
                f"pass --trust-stale-completeness to rank on it anyway.",
                file=sys.stderr,
            )
            return 2
        rows.sort(key=lambda r: (-r["missing_modules"], r["components"], r["category"], r["slug"]))
    elif args.sort == "fragmentation":
        rows.sort(key=lambda r: (-r["components"], -r["orphans"], r["category"], r["slug"]))

    shown = rows if args.limit == 0 else rows[: args.limit]
    if args.as_json:
        print(json.dumps({"counts": counts, "rows": shown}, indent=2))
        return 0

    sort_meaning = {
        "score": "worst graph overall -- usually resolves to CURATION work",
        "missing": "biggest CONTENT gap -- the right sort for choosing what to RESEARCH",
        "fragmentation": "biggest CONNECTIVE gap -- curation, not research",
    }[args.sort]
    # Without this line a pasted ranking is ambiguous between two questions whose
    # answers differ, and reading it the wrong way is what spends money on a
    # report describing what is already on disk (#430).
    print(f"sorted by {args.sort}: {sort_meaning}\n")
    print(f"{'score':>5} {'edg':>3} {'nod':>3} {'cmp':>3} {'orph':>4} {'miss':>4} {'res':>3}  trait")
    for r in shown:
        if r.get("family_members", 1) > 1:
            fam = f"  [+{r['family_members'] - 1} sibling bins]"
        elif r.get("series_size", 0) > 1:
            fam = f"  [series {r['family']}, {r['series_size']} bins]"
        else:
            fam = ""
        # A stale completeness row's missing_modules is shown for reference but
        # did not contribute to the score; the marker keeps the two readable
        # side by side.
        miss = f"{r['missing_modules']:3d}*" if r["completeness_stale"] else f"{r['missing_modules']:4d}"
        print(
            f"{r['score']:5d} {r['edges']:3d} {r['nodes']:3d} {r['components']:3d} "
            f"{r['orphans']:4d} {miss} {'yes' if r['researched'] else 'NO ':>3}  "
            f"{r['category']}/{r['slug']}{fam}"
        )

    # Always say what was set aside. A ranking that silently drops a third of the
    # corpus reads as "these are the worst", not "these are the worst of what I
    # considered".
    breakdown = ", ".join(
        f"{v} {k.removeprefix('excluded_')}" for k, v in sorted(counts.items()) if k.startswith("excluded_")
    )
    if args.collapse_families:
        series_note = f"collapsed {counts['families_collapsed']} sibling bin(s) into their family"
    else:
        series_note = (
            f"{counts['in_series']} row(s) belong to a binned series "
            f"(reported, not merged -- measured sibling overlap is 5%, #447)"
        )
    print(
        f"\nranked {len(rows)} candidate(s); "
        f"set aside {counts['non_mechanism']} record(s) that cannot carry a "
        f"mechanism graph ({breakdown}); {series_note}"
    )
    if counts["completeness_rows_stale"]:
        print(
            f"WARNING: {counts['completeness_rows_stale']} of "
            f"{counts['completeness_rows_matched']} completeness-audit rows are STALE "
            f"(reported graph_edges no longer matches the live corpus). Their "
            f"missing_modules (marked *) were excluded from the score; regenerate "
            f"{DEFAULT_COMPLETENESS} to restore that signal (#443)."
        )
    if counts["no_connectivity_row"]:
        print(
            f"WARNING: {counts['no_connectivity_row']} graphed trait(s) are absent from "
            f"{connectivity_note} and were scored as fully connected, which understates "
            f"their weakness. Run `just audit-graphs` to refresh it."
        )
    unresearched = sum(1 for r in rows if not r["researched"])
    print(
        f"of the ranked candidates, {unresearched} have no deep-research artifact; "
        f"the rest already do -- those need their existing research APPLIED, "
        f"not re-run"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
