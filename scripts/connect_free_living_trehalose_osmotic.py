#!/usr/bin/env python3
"""Wire trehalose biosynthesis to osmotic stress tolerance in `ecology/free_living`.

Resolves the record's own knowledge-gap discussion `x-compatible-solute-partitioning`
(#614), which asked whether trehalose's placement under a terminal
`environmental_stress_tolerance` node is a real distinction from the ectoine and
glycine-betaine routes to `osmotic_stress_tolerance`. Its stated `would_refute` was
"the trehalose knockout is osmotically impaired". It is, so the split is refuted.

The graph currently splits into two components, and the smaller is exactly
`{trehalose_biosynthesis, environmental_stress_tolerance}`. Adding the osmotic edge
merges it. That fragmentation is invisible to `audit-graphs` because the graph is
NONMECHANISTIC (#613).

WHAT THIS DELIBERATELY DOES NOT DO
- It does not remove `trehalose_biosynthesis -> environmental_stress_tolerance`.
  That edge's evidence is a comparative-genomics gene-presence observation, which is
  weaker than what is added here, but removing a cited edge is a semantic decision and
  evidence removal without provenance is the #520 failure. The desiccation and
  alkaline/oxidative results below argue trehalose's role is specifically osmotic, so
  that edge is flagged for review in #614 rather than deleted here.
- It does not add the "ectoine functionally substitutes for trehalose" relation, nor
  touch `glycine_betaine_system`. Both are noted in #614.
- It does not set the discussion to RESOLVED. That is a separate call once the edit lands.

Dry run by default; pass --apply to write.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "ecology" / "free_living.yaml"
GRAPH_ID = "free_living_environmental_habitat"
SUBJECT = "trehalose_biosynthesis"
OBJECT = "osmotic_stress_tolerance"

NEW_EDGE = {
    "subject": SUBJECT,
    "predicate": "enables",
    "object": OBJECT,
    "description": (
        "Trehalose accumulation through the OtsAB pathway is required for free-living "
        "osmotic stress tolerance: losing the pathway reduces viability under both "
        "nonionic and ionic hyperosmotic challenge, and supplying trehalose restores it."
    ),
    "evidence": [
        {
            "reference": "DOI:10.1128/mBio.00390-21",
            "snippet": (
                "the Δ(otsCB-otsA) mutant showed reduced viability under these "
                "stress conditions similar to the ΔecfG mutant"
            ),
            "notes": (
                "Free-living hyperosmotic challenge in Bradyrhizobium diazoefficiens "
                "USDA 110: 400 mM sorbitol, 27 mM NaCl, 50 mM MgCl2, 75 mM MgSO4. The "
                "nonionic sorbitol condition is what separates osmotic pressure from "
                "salt-specific ion toxicity. Causality is pinned by two further controls: "
                "expressing a cytoplasmic trehalase (strain TreF-1) phenocopies the "
                "deletion, and exogenous trehalose rescues the otsA deletion but not the "
                "transporter-deficient otsCB-otsA or otsCB deletions, so the phenotype "
                "tracks intracellular trehalose rather than the locus."
            ),
        },
        {
            "reference": "DOI:10.1128/AEM.02483-09",
            "snippet": (
                "the single, double, and triple mutant strains lacking the OtsAB pathway "
                "(the ΔotsA, ΔotsA ΔtreS or ΔotsA ΔtreY, and "
                "ΔotsA ΔtreS ΔtreY mutants) were inhibited for growth on "
                "60 mM NaCl"
            ),
            "notes": (
                "Independently constructed mutants in the same strain background "
                "(published as B. japonicum), so the phenotype does not depend on one "
                "construct. Mutants lacking both the OtsAB and TreYZ routes failed to "
                "grow on salt-containing medium. The same study found the low-trehalose "
                "otsA and otsA treY mutants were NOT worse than wild type under "
                "desiccation at 50% relative humidity, which is why this edge is scoped "
                "to osmotic tolerance rather than to environmental stress generally."
            ),
        },
    ],
    "predicate_id": "RO:0002327",
}

CURATION_CHANGES = (
    "Added trehalose_biosynthesis -[RO:0002327 enables]-> osmotic_stress_tolerance to "
    "free_living_environmental_habitat, resolving the record's x-compatible-solute-"
    "partitioning knowledge gap (#614) against its own stated would_refute criterion. "
    "Loss-of-function, trehalase-depletion and metabolite-rescue evidence from "
    "DOI:10.1128/mBio.00390-21, replicated by independent mutants in "
    "DOI:10.1128/AEM.02483-09, show the trehalose knockout is osmotically impaired, so "
    "the trehalose/ectoine split the graph asserted is not a real distinction. This also "
    "merges the graph's stranded {trehalose_biosynthesis, environmental_stress_tolerance} "
    "component into the main one. The pre-existing edge to environmental_stress_tolerance "
    "is retained rather than deleted: its comparative-genomics evidence is weaker but "
    "removing a cited edge is a semantic decision, tracked in #614."
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the change (default: dry run)")
    args = ap.parse_args()

    doc = yaml.safe_load(TARGET.read_text(encoding="utf-8"))
    graphs = [g for g in (doc.get("causal_graphs") or []) if g.get("graph_id") == GRAPH_ID]
    if len(graphs) != 1:
        print(f"ERROR: expected exactly one graph {GRAPH_ID!r}, found {len(graphs)}", file=sys.stderr)
        return 1
    graph = graphs[0]

    node_ids = {n.get("node_id") for n in (graph.get("nodes") or [])}
    for required in (SUBJECT, OBJECT):
        if required not in node_ids:
            print(f"ERROR: node {required!r} is not in the graph", file=sys.stderr)
            return 1

    edges = graph.setdefault("edges", [])
    if any(e.get("subject") == SUBJECT and e.get("object") == OBJECT for e in edges):
        print("Nothing to do: the edge already exists.")
        return 0

    print(f"WOULD ADD to {TARGET.relative_to(REPO_ROOT)} :: {GRAPH_ID}")
    print(f"  {SUBJECT} --{NEW_EDGE['predicate_id']} ({NEW_EDGE['predicate']})--> {OBJECT}")
    for item in NEW_EDGE["evidence"]:
        print(f"    evidence: {item['reference']}")
        print(f"      snippet: {item['snippet'][:88]}...")
    if not args.apply:
        print("\nDry run. Re-run with --apply to write.")
        return 0

    edges.append(NEW_EDGE)
    record_curation_event(
        doc,
        curator="claude",
        action="CONNECT_CAUSAL_GRAPH",
        changes=CURATION_CHANGES,
        llm_assisted=True,
    )
    write_validated_trait(doc, TARGET)
    print(f"\nWROTE {TARGET.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
