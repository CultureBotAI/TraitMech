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

3. BINNED SIBLINGS CROWD THE LIST. `ph_delta_mid2`, `ph_delta_mid3`,
   `temperature_range_mid4`, `nacl_range_low` are METPO binning classes over one
   underlying mechanism. Ranked individually they fill the top of the list with
   the same research question at different cut points. They collapse into one
   family row carrying the family's worst score, because one research pass
   answers the whole family -- which makes a family MORE efficient per call, not
   less, but only if you run it once.

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
                        double.
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
      scores 28 on six components, but its edges name endoglucanase,
      endochitinase and lignin oxidative enzymes without connecting any of them
      to the trait or to `assimilable_units`. Nothing in the literature is
      missing; the edges are. This is curation, not research.

  few components, many missing modules -> a CONTENT gap. The graph is coherent
      and incomplete. `nitrogen_fixing_symbiosis` scores 22 with ONE component
      and no orphans, on the highest missing-module count in the corpus (11).
      Only literature can supply what is absent.

So `--sort missing` exists, and it is the right sort when the question is "what
should we RESEARCH". The default composite sort answers "which graph is worst",
which is a different question and usually resolves to curation work.
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


# Binned/graded families: everything after the stem is a bin label, so one
# research pass covers the family. Kept as explicit patterns rather than a
# generic "split on the last underscore", which would also collapse unrelated
# traits that merely share a prefix.
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
    collapse_families: bool = True,
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
        "no_connectivity_row": 0,
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
                "verdict": v.get("verdict", ""),
                "researched": (category, slug) in researched,
                "family": family_of(slug),
                "score": score(missing, max(0, nodes - wired), components, edges),
            }
        )

    if collapse_families:
        rows, collapsed = _collapse(rows)
        counts["families_collapsed"] = collapsed

    rows.sort(key=lambda r: (-r["score"], r["category"], r["slug"]))
    return rows, counts


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
    return standalone + list(best.values()), collapsed


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--traits-dir", type=Path, default=DEFAULT_TRAITS)
    ap.add_argument("--limit", type=int, default=15, help="rows to print (0 = all)")
    ap.add_argument(
        "--include-nonmechanism",
        action="store_true",
        help="include predicate/upper-ontology/observation records (not researchable)",
    )
    ap.add_argument("--no-collapse-families", action="store_true", help="rank each bin separately")
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
        collapse_families=not args.no_collapse_families,
    )
    if args.unresearched_only:
        rows = [r for r in rows if not r["researched"]]
    if args.sort == "missing":
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
        fam = f"  [+{r['family_members'] - 1} sibling bins]" if r.get("family_members", 1) > 1 else ""
        print(
            f"{r['score']:5d} {r['edges']:3d} {r['nodes']:3d} {r['components']:3d} "
            f"{r['orphans']:4d} {r['missing_modules']:4d} {'yes' if r['researched'] else 'NO ':>3}  "
            f"{r['category']}/{r['slug']}{fam}"
        )

    # Always say what was set aside. A ranking that silently drops a third of the
    # corpus reads as "these are the worst", not "these are the worst of what I
    # considered".
    breakdown = ", ".join(
        f"{v} {k.removeprefix('excluded_')}" for k, v in sorted(counts.items()) if k.startswith("excluded_")
    )
    print(
        f"\nranked {len(rows)} candidate(s); "
        f"set aside {counts['non_mechanism']} record(s) that cannot carry a "
        f"mechanism graph ({breakdown}); "
        f"collapsed {counts['families_collapsed']} sibling bin(s) into their family"
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
