#!/usr/bin/env python3
"""Structural-integrity audit for TraitMech causal graphs.

LinkML/`validate-strict` check field *types*, but not graph *connectivity*.
This audit walks every ``data/traits/**/*.yaml`` causal graph and flags
structural defects the schema cannot catch:

  DANGLING_EDGE           an edge whose ``subject`` or ``object`` is not a
                          declared ``node_id`` in the same graph (a typo or a
                          deleted node).                            [ERROR]
  ORPHAN_NODE             a declared node that no edge references (a fully
                          disconnected node).                       [ERROR]
  NO_TRAIT_NODE           a graph with no ``node_type: TRAIT`` node, so there
                          is nothing to anchor reachability to.     [ERROR]
  FRAGMENTED_GRAPH        a MECHANISTIC graph that splits into several disconnected
                          components. Catches what UNREACHABLE_FROM_TRAIT cannot:
                          a split where each side happens to contain a node typed
                          TRAIT, so every node reaches *a* trait but not the one
                          the record is about (#220).
  DUPLICATE_GROUNDING     two nodes in one graph carrying the same ``grounding``.
                          The machine-readable signature of one concept modelled
                          twice — #351 grounded `growth_external_ph_5_5_9` to the
                          same METPO CURIE its own record's trait node already
                          had, which made the duplication legible but which
                          nothing detected (#352).            [WARN]
  DISPOSITION_MISTYPED    a CAPACITY or STATE node whose own description reads as
                          a disposition — "capacity to", "ability to",
                          "tolerance of". Those describe what an organism CAN do,
                          i.e. a TRAIT. Three separate defects this session were
                          a mis-typed node rather than a wrong predicate (#328,
                          #330, #331), and #334 retyped six on exactly this
                          evidence; the ones left behind survived only because
                          their in-edges happened not to violate a range, which
                          is an unrelated fact (#352).

                          QUALITY is deliberately NOT scanned, though it carries
                          the same phrasing in places: carboxydotrophic.yaml's
                          `oxygen_tolerance` is "Ability of an ENZYME to function
                          in the presence of O2", which is a property of a
                          protein rather than something an organism can do. The
                          same node_id typed CAPACITY in oxygen_preference.yaml
                          IS organism-scoped and is flagged. Widening to QUALITY
                          would need the organism/enzyme distinction, which this
                          heuristic does not make (#353 review).  [WARN]
  INCONSISTENT_NODE_TYPE  one ``node_id`` carrying different ``node_type``s in
                          different records. The only CROSS-RECORD check here —
                          neither record is wrong read alone, which is why
                          nothing caught it. `proton_motive_force` is typed four
                          ways across 35 records; 63 node_ids disagree with
                          themselves corpus-wide. #355 made it consequential by
                          minting `powers` (METPO:2007900) gated on
                          ``subject_types``, so two byte-identical assertions now
                          ground or not purely by how the subject is typed
                          (#356).

                          NOT EVERY HIT IS A DEFECT, and the baseline is where
                          that gets decided rather than here. `terminal
                          electron acceptor` is typed both CHEMICAL and
                          MOLECULAR_FUNCTION on purpose — mappings/node_grounding.tsv
                          carries a row for each, saying "same proposed METPO
                          class covers both senses; MOLECULAR_FUNCTION typing
                          surfaces the role-of interpretation". Same two-senses
                          shape as `reduces` (#330/#333) and the CAPACITY table
                          in the playbook. Where a family really does mean two
                          things, the fix is TWO node_ids, not one type: this
                          check asks whether one id means one thing, and a
                          curator answering "no, two" resolves it by splitting.
                                                                         [WARN]
  UNREACHABLE_FROM_TRAIT  a node in a MECHANISTIC graph that IS referenced by
                          some edge, but sits in
                          an island with no undirected path back to any TRAIT
                          node. The graph is several disjoint fragments rather
                          than one mechanism.                        [WARN]

Why UNREACHABLE_FROM_TRAIT is needed: ORPHAN_NODE catches a node with *zero*
edges, but says nothing about a well-connected cluster that never reaches the
trait. A graph can be four separate islands and still be "clean" under the
original two checks. That is the common failure mode of bulk enrichment
passes, which append a cluster of new nodes and edges without wiring them
into the existing cascade.

Reachability is deliberately **undirected**. Curated predicates mix directions
(``cellulase -enables-> trait`` but ``trait -produces-> glucose``), so a
directed walk would flag correctly-modelled graphs. The question here is
"is this one graph or several?", not "does causality flow one way?".

Connectivity is enforced only for ``scope_status: MECHANISTIC`` graphs. A
``NONMECHANISTIC`` graph explicitly collects several context or classification
branches that need not form one causal mechanism; treating its declared scope
as a connectivity defect contradicts the distinction. Dangling edges, orphan
nodes, missing trait anchors, duplicate groundings, and typing checks still run
for both scopes.

Because a large fraction of the corpus currently has at least one unreachable
node, a blocking check would be un-landable as-is. Use ``--write-baseline`` to
freeze the known set and ratchet: pre-existing fragmentation stays a warning,
while any *new* unreachable node fails the build.

Writes ``reports/causal_graph_audit.tsv``. Exit code is governed by
``--fail-on``:

  new    (default) any finding NOT in the baseline fails. Baselined findings
         never fail regardless of severity. This is the ratchet: the corpus
         cannot get more fragmented than it is today, but today's 499
         findings do not block.
  error  only new ERROR-severity findings fail. New fragmentation is still
         reported, but non-blocking — use if the ratchet proves too noisy.
  any    every finding fails and the baseline is ignored. Use once the
         backlog has been burned down.

Note that severity governs *reporting* and the ``error`` mode; under the
default ``new`` mode a WARN-severity regression blocks just like an ERROR,
because the point is to prevent backsliding.

Usage:
    python scripts/audit_causal_graphs.py
    python scripts/audit_causal_graphs.py --out reports/causal_graph_audit.tsv
    python scripts/audit_causal_graphs.py --write-baseline   # freeze today
    python scripts/audit_causal_graphs.py --fail-on any      # once burned down
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TRAITS_DIR = REPO_ROOT / "data" / "traits"
DEFAULT_OUT = REPO_ROOT / "reports" / "causal_graph_audit.tsv"
DEFAULT_CONNECTIVITY = REPO_ROOT / "reports" / "causal_graph_connectivity.tsv"
DEFAULT_BASELINE = REPO_ROOT / "conf" / "causal_graph_audit_baseline.tsv"
CONNECTIVITY_FIELDS = ("file", "graph_id", "wired_nodes", "components",
                       "largest_component", "component_sizes")

ERROR = "ERROR"
WARN = "WARN"

# Severity per defect. Promote UNREACHABLE_FROM_TRAIT to ERROR once the
# backlog is burned down (or just run with --fail-on any).
SEVERITY = {
    "DUPLICATE_GROUNDING": WARN,
    "DISPOSITION_MISTYPED": WARN,
    "INCONSISTENT_NODE_TYPE": WARN,
    "DANGLING_EDGE": ERROR,
    "ORPHAN_NODE": ERROR,
    "NO_TRAIT_NODE": ERROR,
    "UNREACHABLE_FROM_TRAIT": WARN,
    "FRAGMENTED_GRAPH": WARN,
}

FIELDNAMES = ["file", "graph_id", "defect", "severity", "detail"]


def _reachable(seeds: list[str], adjacency: dict[str, set[str]]) -> set[str]:
    """Undirected breadth-first closure from ``seeds``."""
    seen: set[str] = set()
    queue = deque(seeds)
    while queue:
        node = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        queue.extend(adjacency[node] - seen)
    return seen


def _components(node_set: set[str], adjacency: dict[str, set[str]]) -> list[set[str]]:
    """Undirected connected components, largest first.

    Anchor-free by design — it asks "is this one graph?" without needing to know
    which node the record is about, which is what makes it immune to the two
    ways UNREACHABLE_FROM_TRAIT can be fooled (several TRAIT nodes, or a trait
    node whose id does not follow the `<slug>_trait` convention).
    """
    seen: set[str] = set()
    out: list[set[str]] = []
    for node in sorted(n for n in node_set if n is not None):
        if node in seen:
            continue
        component = _reachable([node], adjacency)
        seen |= component
        out.append(component)
    return sorted(out, key=len, reverse=True)


def _topology(graph: dict) -> tuple[set, set, dict[str, set[str]]]:
    """``(declared node ids, edge-referenced ids, undirected adjacency)``.

    Shared by :func:`audit` and :func:`connectivity_rows` so the ratchet and
    the metric can never disagree about what "connected" means. Only edges
    whose BOTH ends are declared are wired, so a dangling edge cannot
    fabricate reachability through a phantom node — the audit reports that
    separately as DANGLING_EDGE.
    """
    node_set = {n.get("node_id") for n in (graph.get("nodes") or [])}
    referenced: set = set()
    adjacency: dict[str, set[str]] = defaultdict(set)
    for e in (graph.get("edges") or []):
        subj, obj = e.get("subject"), e.get("object")
        referenced.add(subj)
        referenced.add(obj)
        if subj in node_set and obj in node_set:
            adjacency[subj].add(obj)
            adjacency[obj].add(subj)
    return node_set, referenced, adjacency


Corpus = list[tuple[str, dict]]


def load_corpus(traits_dir: Path) -> Corpus:
    """Parse every trait YAML once, as ``[(repo-relative path, doc), ...]``.

    The three passes below each used to re-walk and re-parse the whole corpus
    for a different projection: **1431 ``yaml.safe_load`` calls for 477 records**,
    exactly three per file, doubled again because ``qc`` runs this script and
    then runs it a second time inside ``audit-derived-reports`` to diff against
    git. It is now 477 (#373).

    The parse count rather than a wall-clock figure on purpose. Timings taken
    while developing this ranged from 15.5s to 29.9s for identical code, and one
    measurement of the fix came out slower than the baseline it beats — quoting
    seconds here would hand the next person a number they cannot reproduce.

    Consolidating is not only about speed. Each pass carried its own copy of the
    rglob / safe_load / isinstance guard, so "which files does this audit see?"
    was answered in three places that could drift apart — the same argument
    ``_topology`` settled one level down for "what does connected mean" (#363).
    An unparseable YAML is skipped exactly once, here, and every projection now
    sees the identical file set by construction.
    """
    corpus: Corpus = []
    for path in sorted(traits_dir.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        try:
            rel = str(path.relative_to(REPO_ROOT))
        except ValueError:
            rel = str(path)
        corpus.append((rel, doc))
    return corpus


def _as_corpus(source: Path | Corpus) -> Corpus:
    """Accept a directory or an already-parsed corpus.

    ``main`` loads once and passes the list to all three passes; the tests call
    them with a ``tmp_path`` directory, which is the more readable fixture. Both
    stay supported rather than forcing every caller through a loader.
    """
    if isinstance(source, Path):
        return load_corpus(source)
    if isinstance(source, list):
        return source
    # A str path is the plausible wrong argument — every other path-taking
    # helper here accepts one. Without this it iterates the string and dies
    # unpacking a single character into (rel, doc), from inside a loop, with a
    # message naming neither the argument nor the type (#380).
    raise TypeError(
        f"expected a Path to a traits directory or an already-parsed corpus "
        f"(list of (path, doc) pairs), got {type(source).__name__}: {source!r}"
    )


def connectivity_rows(source: Path | Corpus) -> list[dict[str, str]]:
    """Per-graph connectivity, the metric #359 asked for.

    Neither headline count can tell a real connectivity gain from an anchor
    added inside an island. #352 is the worked example: `oxygen_tolerance`
    could be RETYPED to TRAIT (wrong -- the grounding contradicted the graph)
    or MERGED into `oxygen_preference_trait` (right), and
    UNREACHABLE_FROM_TRAIT lands on 1296 either way, because retyping simply
    added an anchor the island's nodes could already reach. FRAGMENTED_GRAPH's
    *count* is equally blind: it reports one finding per split graph however
    many pieces it is in, so 3 components -> 2 does not move it.

    What separates them is the component structure itself:

        retyped:  components=3 of 14  (sizes: 8, 4, 2)   <- island still an island
        merged:   components=2 of 13  (sizes: 11, 2)     <- island attached

    So this reports, per graph, the component count and the share of nodes in
    the largest one. Both are anchor-free, for the reason :func:`_components`
    documents: they ask "is this one graph?" without needing to know which
    node the record is about, so no amount of retyping or renaming moves them.
    Scoped to edge-referenced nodes, matching FRAGMENTED_GRAPH — an unwired
    node is ORPHAN_NODE's business and counting it here would let one defect
    depress two metrics.
    """
    rows: list[dict[str, str]] = []
    for rel, doc in _as_corpus(source):
        for graph in (doc.get("causal_graphs") or []):
            if graph.get("scope_status") == "NONMECHANISTIC":
                continue
            node_set, referenced, adjacency = _topology(graph)
            wired = node_set & referenced
            if not wired:
                continue
            components = _components(wired, adjacency)
            largest = len(components[0])
            rows.append({
                "file": rel,
                "graph_id": graph.get("graph_id", ""),
                "wired_nodes": str(len(wired)),
                "components": str(len(components)),
                "largest_component": str(largest),
                "component_sizes": ",".join(str(len(c)) for c in components),
            })
    return rows


# Matched against the DESCRIPTION only, never the label: the label is usually
# just the concept name ("buoyancy", "salt tolerance") while the description is
# where the curator says what it IS.
#
# The capacity/ability arm requires the capacity to be ORGANISM-scoped -- bare
# ("Capacity to grow...") or of a cell/organism. That is deliberate, not a
# tightening for its own sake: ph_optimum.yaml has "Capacity of cytoplasmic
# buffers (e.g. ...) to absorb pH fluctuations", which is a genuine reservoir
# CAPACITY and must not flag. A looser `capacity[^.]{0,30}?to` let it through
# only because the dots in "e.g." happened to stop the character class -- a
# correct verdict for an accidental reason, which an unrelated cleanup would
# silently reverse (#353 review).
_DISPOSITION_RE = re.compile(
    r"\b(?:"
    r"capacit(?:y|ies)(?:\s+of\s+(?:a|an|the)?\s*(?:cell|organism|bacteri\w+|archae\w+|microbe|strain|species|isolate)s?)?\s+to"
    r"|abilit(?:y|ies)(?:\s+of\s+(?:a|an|the)?\s*(?:cell|organism|bacteri\w+|archae\w+|microbe|strain|species|isolate)s?)?\s+to"
    r"|able\s+to"
    r"|tolerance\s+(?:of|to)"
    r")\b",
    re.IGNORECASE)


def node_type_index(source: Path | Corpus) -> dict[str, dict[str, int]]:
    """``node_id`` → ``{node_type: number of NODE OCCURRENCES}``, corpus-wide.

    Occurrences, not records, and the distinction is currently invisible: no
    ``node_id`` appears twice in one graph, and none appears in two graphs of
    one record, so the two counts are equal everywhere today. Nothing enforces
    that, though, and the count is quoted straight into the finding text
    ("STATE×18") whose whole job is to size the disagreement — so it says which
    it means rather than relying on the corpus staying shaped this way (#374).

    Every other check in this file is scoped to one graph. This one cannot be:
    the defect is that two RECORDS disagree, and neither record is wrong when
    read alone. #355 is what made it consequential — it minted `METPO:2007900`
    (`powers`) gated to ``subject_types = BIOLOGICAL_PROCESS|STATE``, so two
    byte-identical assertions now ground or not purely by how their subject is
    typed: `carboxydotrophic.yaml`'s `proton_motive_force` (STATE) grounds,
    `phototrophic.yaml`'s (CAPACITY) is `blocked_by_node_type` (#356).
    """
    index: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for _rel, doc in _as_corpus(source):
        for graph in (doc.get("causal_graphs") or []):
            for node in (graph.get("nodes") or []):
                nid, ntype = node.get("node_id"), node.get("node_type")
                if nid and ntype:
                    index[nid][ntype] += 1
    return {k: dict(v) for k, v in index.items()}


def audit(source: Path | Corpus) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    # Normalised once: INCONSISTENT_NODE_TYPE needs a corpus-wide pre-pass, and
    # handing it the already-parsed corpus keeps a Path caller (the tests) to a
    # single walk rather than one per projection.
    corpus = _as_corpus(source)
    type_index = node_type_index(corpus)
    for rel, doc in corpus:
        for graph in (doc.get("causal_graphs") or []):
            gid = graph.get("graph_id", "")
            nodes = graph.get("nodes") or []
            # Topology comes from the shared helper so this ratchet and
            # connectivity_rows() cannot drift apart on what "connected" means;
            # the DANGLING_EDGE pass below stays here because it is a finding,
            # not topology.
            node_set, referenced, adjacency = _topology(graph)

            for e in (graph.get("edges") or []):
                subj, obj = e.get("subject"), e.get("object")
                for end, ref in (("subject", subj), ("object", obj)):
                    if ref not in node_set:
                        findings.append({
                            "file": rel, "graph_id": gid, "defect": "DANGLING_EDGE",
                            "severity": SEVERITY["DANGLING_EDGE"],
                            "detail": f"{end}={ref!r} ({subj} -[{e.get('predicate')}]-> {obj})",
                        })

            for n in nodes:
                if n.get("node_id") not in referenced:
                    findings.append({
                        "file": rel, "graph_id": gid, "defect": "ORPHAN_NODE",
                        "severity": SEVERITY["ORPHAN_NODE"],
                        "detail": f"node_id={n.get('node_id')!r} label={n.get('label')!r} type={n.get('node_type')}",
                    })

            if not nodes:
                continue

            trait_nodes = [n.get("node_id") for n in nodes
                           if n.get("node_type") == "TRAIT"]
            if not trait_nodes:
                findings.append({
                    "file": rel, "graph_id": gid, "defect": "NO_TRAIT_NODE",
                    "severity": SEVERITY["NO_TRAIT_NODE"],
                    "detail": f"{len(nodes)} node(s), no node_type: TRAIT to anchor reachability",
                })
                continue

            enforce_connectivity = graph.get("scope_status") != "NONMECHANISTIC"
            if enforce_connectivity:
                reached = _reachable(trait_nodes, adjacency)
                for n in nodes:
                    nid = n.get("node_id")
                    # ORPHAN_NODE already covers zero-edge nodes; don't double-report.
                    if nid in reached or nid not in referenced:
                        continue
                    findings.append({
                        "file": rel, "graph_id": gid,
                        "defect": "UNREACHABLE_FROM_TRAIT",
                        "severity": SEVERITY["UNREACHABLE_FROM_TRAIT"],
                        "detail": (f"node_id={nid!r} label={n.get('label')!r} "
                                   f"type={n.get('node_type')} — in an island with no path to "
                                   f"{'/'.join(trait_nodes)}"),
                    })

            # One node_id, several node_types across the corpus (#356). Reported
            # on EVERY occurrence rather than on a presumed-wrong minority,
            # because nothing here knows which type is right — `proton_motive_force`
            # splits 18 STATE / 13 BIOLOGICAL_PROCESS and the gradient genuinely
            # is a state while generating it is a process, so the majority is an
            # observation, not a verdict. Per-occurrence rows also mean a family
            # clears together the moment it is normalised.
            #
            # The detail leads with node_id, so `_key` discriminates by node
            # within a graph. Deliberately NOT led with the type set: a family
            # part-way through a burn-down would re-key on every step and
            # un-suppress rows nobody has reached yet, which is the failure
            # FRAGMENTED_GRAPH's comment describes from the other direction.
            for n in nodes:
                nid = n.get("node_id")
                ntype = n.get("node_type")
                types = type_index.get(nid or "", {})
                if not nid or not ntype or len(types) < 2:
                    continue
                others = ", ".join(f"{t}×{c}" for t, c in sorted(types.items())
                                   if t != ntype)
                findings.append({
                    "file": rel, "graph_id": gid, "defect": "INCONSISTENT_NODE_TYPE",
                    "severity": SEVERITY["INCONSISTENT_NODE_TYPE"],
                    "detail": (f"node_id={nid!r} type={ntype} here — also {others} "
                               f"elsewhere in the corpus"),
                })

            # Two nodes with the same grounding are one concept modelled twice.
            by_grounding: dict[str, list[str]] = defaultdict(list)
            for n in nodes:
                g = (n.get("grounding") or "").strip()
                if g:
                    by_grounding[g].append(n.get("node_id"))
            for g, ids in sorted(by_grounding.items()):
                if len(ids) > 1:
                    findings.append({
                        "file": rel, "graph_id": gid, "defect": "DUPLICATE_GROUNDING",
                        "severity": SEVERITY["DUPLICATE_GROUNDING"],
                        # The leading whitespace-free token is _key's baseline
                        # discriminator, and it must carry BOTH the count and the
                        # CURIE. Leading with the CURIE alone kept the key stable
                        # when a THIRD node joined, so freezing two forgave three.
                        # Leading with the count alone opened the mirror of that:
                        # two DIFFERENT groundings each on 2 nodes in one graph
                        # would collide on `nodes=2` and freezing one would
                        # forgive the other (#353 review). Both vary here.
                        "detail": (f"nodes={len(ids)};grounding={g} "
                                   f"({', '.join(sorted(i for i in ids if i))})"),
                    })

            for n in nodes:
                if n.get("node_type") not in ("CAPACITY", "STATE"):
                    continue
                if _DISPOSITION_RE.search(n.get("description") or ""):
                    findings.append({
                        "file": rel, "graph_id": gid, "defect": "DISPOSITION_MISTYPED",
                        "severity": SEVERITY["DISPOSITION_MISTYPED"],
                        "detail": (f"node_id={n.get('node_id')!r} "
                                   f"type={n.get('node_type')} — description reads as a "
                                   f"disposition, which is a TRAIT"),
                    })

            # UNREACHABLE_FROM_TRAIT anchors on ANY node typed TRAIT, and that is
            # correct: 85 of 353 graphs legitimately carry more than one, because
            # a record links its parent and child traits as nodes
            # (`bsl1_trait` + `biosafety_level`, `nacl_delta_high_trait` +
            # `nacl_delta`). But it means a graph splitting into components that
            # EACH contain a TRAIT node reports clean — every node reaches *a*
            # trait, just not the one the record is about (#220).
            #
            # Anchoring on the record's own trait node instead was the obvious
            # alternative and does not work: `<slug>_trait` holds for 297 graphs
            # and not for the other 56, which use abbreviated ids
            # (`bsl1_trait` for biosafety_level_1, `predatory_trait` for
            # predatory_bacterium). Counting components needs no anchor at all,
            # so it cannot be fooled by either naming or typing.
            # Computed over edge-referenced nodes only. A zero-edge node is its
            # own component, but ORPHAN_NODE already reports it as an ERROR with
            # a clearer remedy — counting it here would raise a second finding
            # for one defect, which is the same reason UNREACHABLE_FROM_TRAIT
            # skips unreferenced nodes above.
            components = _components(node_set & referenced, adjacency)
            if enforce_connectivity and len(components) > 1:
                sizes = ", ".join(str(len(c)) for c in components)
                # Detail MUST lead with the component count, because `_key` takes
                # the leading whitespace-delimited token as the baseline
                # discriminator. Leading with the node count instead made the
                # ratchet fail open in both directions on the 220 graphs this
                # baselines: 3 components -> 4 keeps the node count, so real
                # backsliding stayed suppressed; while adding a node inside an
                # already-connected component changed the key and blocked a PR
                # whose fragmentation was unchanged — the ordinary shape of
                # #183's backfill. This is the first WARN-severity whole-graph
                # defect, so it is the first time the discriminator has had to be
                # anything but a node_id.
                findings.append({
                    "file": rel, "graph_id": gid, "defect": "FRAGMENTED_GRAPH",
                    "severity": SEVERITY["FRAGMENTED_GRAPH"],
                    "detail": (f"components={len(components)} of {len(nodes)} node(s) "
                               f"(sizes: {sizes}) — one record, several unrelated "
                               "mechanisms"),
                })
    return findings


def _key(row: dict[str, str]) -> tuple[str, str, str, str]:
    """Baseline identity: (file, graph, defect, discriminator).

    The discriminator is the leading fragment of ``detail`` — ``node_id=...``
    for node-shaped findings, ``subject=...``/``object=...`` for edge-shaped
    ones. Taking only the leading fragment means editing a still-broken node's
    *label* does not silently un-suppress it, while keeping distinct nodes and
    distinct dangling edges on distinct keys. Falling back to "" here would
    collapse every DANGLING_EDGE in a graph onto one key, so baselining one
    would suppress the rest.
    """
    detail = row.get("detail", "")
    node = detail.split(" ", 1)[0] if detail else ""
    return (row["file"], row["graph_id"], row["defect"], node)


def partition(
    findings: list[dict[str, str]],
    baseline: set[tuple[str, str, str, str]],
    fail_on: str,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    """Split ``findings`` into (not-in-baseline, blocking) for a ``--fail-on``.

    Kept separate from ``main`` so the exit-code contract is unit-testable: a
    regression here silently disarms the gate, which is exactly how the first
    cut of this check shipped without actually ratcheting.
    """
    new = [r for r in findings if _key(r) not in baseline]
    if fail_on == "any":
        # Strictest: ignore the baseline entirely. Use once the backlog is gone.
        blocking = list(findings)
    elif fail_on == "error":
        blocking = [r for r in new if r["severity"] == ERROR]
    else:  # "new" — the ratchet: never regress past the frozen baseline.
        blocking = list(new)
    return new, blocking


def load_baseline(path: Path) -> set[tuple[str, str, str, str]]:
    if not path.exists():
        return set()
    with path.open(newline="") as f:
        return {_key(r) for r in csv.DictReader(f, delimiter="\t")}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--connectivity-out", type=Path, default=None,
                    help="per-graph connectivity TSV (#359). Written on every run; "
                         "it is a measurement, not a verdict, and never affects the "
                         "exit code. Defaults NEXT TO --out rather than to a fixed "
                         "repo path, so redirecting the report redirects this too.")
    ap.add_argument("--traits-dir", type=Path, default=TRAITS_DIR)
    ap.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE,
                    help="TSV of known findings to suppress from the exit code.")
    ap.add_argument("--no-baseline", action="store_true",
                    help="Ignore the baseline file; report everything.")
    ap.add_argument("--write-baseline", action="store_true",
                    help="Freeze current WARN findings into --baseline and exit 0. "
                         "Refuses if any ERROR-severity finding exists.")
    ap.add_argument("--fail-on", choices=["new", "error", "any"], default="new",
                    help="new (default): any finding not in the baseline fails — a "
                         "true ratchet. error: only new ERROR-severity findings fail, "
                         "so new fragmentation is reported but non-blocking. "
                         "any: every finding fails, baseline ignored (post-burndown).")
    args = ap.parse_args()

    # Parsed once and shared by all three passes (#373). Every projection then
    # sees the same file set by construction, not by three guards agreeing.
    corpus = load_corpus(args.traits_dir)
    findings = audit(corpus)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(findings)

    # Derived from --out, not a fixed repo path. A caller that redirects the
    # report to a temp dir -- every test that runs this via subprocess, and the
    # staleness check in audit-derived-reports -- would otherwise still write
    # THIS file into the working tree. That is not hypothetical: it clobbered
    # the committed report with a single row naming a pytest tmpdir, and the
    # staleness gate is what caught it.
    if args.connectivity_out is None:
        args.connectivity_out = args.out.parent / DEFAULT_CONNECTIVITY.name

    conn = connectivity_rows(corpus)
    args.connectivity_out.parent.mkdir(parents=True, exist_ok=True)
    with args.connectivity_out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CONNECTIVITY_FIELDS, delimiter="\t",
                           lineterminator="\n")
        w.writeheader()
        w.writerows(conn)

    if args.write_baseline:
        # The baseline parks the known WARN backlog so the check can run
        # non-blocking. It is NOT a suppression channel for structural errors:
        # freezing an ERROR here would keep the gate green forever after.
        errors = [r for r in findings if r["severity"] == ERROR]
        if errors:
            print(f"Refusing to write baseline: {len(errors)} ERROR-severity "
                  f"finding(s) present. Fix these first — the baseline is for "
                  f"the WARN backlog only.", file=sys.stderr)
            for r in errors[:20]:
                print(f"  {r['defect']}  {r['file']} [{r['graph_id']}]  "
                      f"{r['detail']}", file=sys.stderr)
            return 1
        warns = [r for r in findings if r["severity"] != ERROR]
        args.baseline.parent.mkdir(parents=True, exist_ok=True)
        with args.baseline.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDNAMES, delimiter="\t",
                               lineterminator="\n")
            w.writeheader()
            w.writerows(warns)
        print(f"Wrote baseline: {args.baseline} ({len(warns)} finding(s))",
              file=sys.stderr)
        return 0

    baseline = set() if args.no_baseline else load_baseline(args.baseline)
    new, blocking = partition(findings, baseline, args.fail_on)

    by_defect: dict[str, int] = {}
    for r in findings:
        by_defect[r["defect"]] = by_defect.get(r["defect"], 0) + 1
    print("=== causal-graph structural audit ===", file=sys.stderr)
    print(f"  findings: {len(findings)}"
          f"  (baselined: {len(findings) - len(new)}, new: {len(new)},"
          f" blocking: {len(blocking)})", file=sys.stderr)
    for d, n in sorted(by_defect.items()):
        print(f"    {d:<22} {n:>5}  [{SEVERITY.get(d, WARN)}]", file=sys.stderr)
    print(f"  TSV: {args.out}", file=sys.stderr)

    # Reported alongside, never folded into the finding counts: this measures
    # the corpus, it does not judge it (#359). `attached` is the share of wired
    # nodes sitting in their graph's largest component -- the number that moves
    # when an island is genuinely joined and stays flat when a node is merely
    # retyped into an anchor.
    total_wired = sum(int(r["wired_nodes"]) for r in conn)
    total_components = sum(int(r["components"]) for r in conn)
    total_largest = sum(int(r["largest_component"]) for r in conn)
    if total_wired:
        pct = 100.0 * total_largest / total_wired
        print(f"  connectivity: {len(conn)} graph(s), {total_components} component(s) "
              f"over {total_wired} wired node(s); attached "
              f"{total_largest}/{total_wired} ({pct:.1f}%)", file=sys.stderr)
    else:
        print("  connectivity: no wired nodes", file=sys.stderr)
    print(f"  connectivity TSV: {args.connectivity_out}", file=sys.stderr)

    for r in (blocking or new)[:20]:
        print(f"  {r['severity']}  {r['defect']}  {r['file']} [{r['graph_id']}]"
              f"  {r['detail']}", file=sys.stderr)
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
