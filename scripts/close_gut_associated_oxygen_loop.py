#!/usr/bin/env python3
"""Close the gut_associated oxygen/fermenter loop through colonocyte metabolism (#617).

The record's knowledge-gap discussion `x-gut-oxygen-causal-direction` asked whether the
one-way `luminal_oxygen_limitation -[contributes to]-> primary_fermenter_community` edge
should be a loop. Its `would_support` was "oxygen rises on depletion and falls again on
re-colonisation". Both arms are met, so the loop is real.

BUT the return arm is NOT `fermenters -> oxygen consumption`. Two bounds from the sources:

  1. HOST-MEDIATED. The supported route runs through butyrate and colonocyte oxidative
     metabolism; the epithelium is the oxygen sink, not the bacteria.
  2. NOT BULK ANOXIA. Friedman 2018 measured luminal pO2 directly and found germ-free and
     conventional mice nearly indistinguishable, so the community is not responsible for
     bulk centre-lumen anoxia. The Friedman evidence is attached to the closing edge
     precisely so the claim cannot drift into "the community creates the anaerobic gut".

The existing `luminal_oxygen_limitation` node already reads "Host functions that limit
oxygen diffusion into the colonic lumen during homeostasis" -- mucosal-to-luminal FLUX, not
bulk steady-state pO2 -- which is exactly the quantity the evidence supports. No rename.

DELIBERATELY OUT OF SCOPE
- No `abiotic_luminal_oxygen_consumption` node. The Friedman result is carried as bounding
  evidence on the closing edge instead; promoting it to its own node is a separate call.
- The oxygen pair is one of this graph's three disconnected components, and this change
  does NOT attach it to `gut_associated_trait`. Adding a connectivity-only edge without
  evidence is exactly what #183 warns against, so the island stays and is noted in #617.

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

TARGET = REPO_ROOT / "data" / "traits" / "ecology" / "gut_associated.yaml"
GRAPH_ID = "gut_associated_microbiota_metabolism"

RC = "DOI:10.1016/j.chom.2016.03.004"   # Rivera-Chavez 2016, Cell Host Microbe
BY = "DOI:10.1126/science.aam9949"      # Byndloss 2017, Science
KE = "DOI:10.1016/j.chom.2015.03.005"   # Kelly 2015, Cell Host Microbe
FR = "DOI:10.1073/pnas.1718635115"      # Friedman 2018, PNAS

NEW_NODES = [
    {
        "node_id": "butyrate",
        "label": "butyrate",
        "node_type": "CHEMICAL",
        "description": (
            "Short-chain fatty acid produced by anaerobic primary fermenters and consumed "
            "by colonocytes as their principal respiratory substrate."
        ),
        "grounding": "CHEBI:17968",
    },
    {
        "node_id": "colonocyte_oxidative_metabolism",
        "label": "colonocyte oxidative metabolism",
        "node_type": "BIOLOGICAL_PROCESS",
        "description": (
            "Beta-oxidation of butyrate by colonic epithelial cells, which consumes oxygen "
            "at the mucosal surface."
        ),
    },
]

NEW_EDGES = [
    {
        "subject": "primary_fermenter_community",
        "predicate": "produces",
        "object": "butyrate",
        "description": (
            "The anaerobic primary-fermenter community is the source of luminal butyrate; "
            "depleting it collapses butyrate and reconstituting it restores butyrate."
        ),
        "evidence": [
            {
                "reference": RC,
                "snippet": (
                    "inoculation with a community of 17 human Clostridia isolates "
                    "resulted in a significant increase in butyrate levels"
                ),
                "notes": (
                    "The recolonisation arm of the discussion's decision rule. The "
                    "converse was shown in the same study: streptomycin depletion of "
                    "butyrate-producing Clostridia lowered cecal butyrate."
                ),
            },
        ],
        "predicate_id": "biolink:produces",
    },
    {
        "subject": "butyrate",
        "predicate": "positively regulates",
        "object": "colonocyte_oxidative_metabolism",
        "description": (
            "Butyrate is sensed by epithelial PPAR-gamma and drives colonocyte energy "
            "metabolism toward beta-oxidation, raising epithelial oxygen consumption."
        ),
        "evidence": [
            {
                "reference": KE,
                "snippet": (
                    "Bacteria-derived butyrate affects epithelial O2 consumption and "
                    "results in stabilization of hypoxia-inducible factor (HIF), a "
                    "transcription factor coordinating barrier protection"
                ),
                "notes": (
                    "Cell-culture work in the same study shows the effect is direct: "
                    "epithelial metabolism of butyrate depletes local oxygen."
                ),
            },
            {
                "reference": BY,
                "snippet": (
                    "the depletion of butyrate-producing microbes by antibiotic treatment "
                    "reduced epithelial signaling through the intracellular butyrate "
                    "sensor peroxisome proliferator-activated receptor γ (PPAR-γ)"
                ),
                "notes": "Identifies PPAR-gamma as the epithelial butyrate sensor.",
            },
        ],
        "predicate_id": "RO:0002213",
    },
    {
        "subject": "colonocyte_oxidative_metabolism",
        "predicate": "contributes to",
        "object": "luminal_oxygen_limitation",
        "description": (
            "Colonocyte beta-oxidation consumes oxygen at the mucosa and so limits the "
            "oxygen reaching the lumen. SCOPE: this is a claim about mucosal-to-luminal "
            "oxygen flux and bioavailability, NOT about bulk centre-lumen anoxia."
        ),
        "evidence": [
            {
                "reference": BY,
                "snippet": (
                    "Microbiota-induced PPAR-γ signaling also limits the luminal "
                    "bioavailability of oxygen by driving the energy metabolism of colonic "
                    "epithelial cells (colonocytes) toward β-oxidation"
                ),
                "notes": (
                    "States the closing step directly, and in terms of BIOAVAILABILITY "
                    "rather than bulk concentration."
                ),
            },
            {
                "reference": RC,
                "snippet": (
                    "tributyrin supplementation restored epithelial hypoxia in "
                    "streptomycin-treated mice"
                ),
                "notes": (
                    "Metabolite rescue: the oxygen change tracks butyrate, not the "
                    "antibiotic, which is what makes the return arm causal rather than "
                    "correlational."
                ),
            },
            {
                "reference": FR,
                "snippet": (
                    "Remarkably, luminal oxygen levels were found to be nearly "
                    "indistinguishable between conventionally housed and germ-free mice, "
                    "being close to zero in the cecum in both cases"
                ),
                "notes": (
                    "BOUNDING EVIDENCE, attached deliberately. Direct phosphorescent-probe "
                    "measurement shows the microbiota is NOT responsible for bulk "
                    "centre-lumen anoxia -- germ-free cecal contents consume oxygen "
                    "chemically on their own. This edge therefore asserts only that "
                    "colonocyte metabolism limits oxygen FLUX toward the lumen, which is "
                    "how the target node is defined. Any future strengthening of this edge "
                    "into a claim about bulk anoxia would contradict this source."
                ),
            },
        ],
        "predicate_id": "RO:0002326",
    },
]

CURATION_CHANGES = (
    "Closed the oxygen/fermenter feedback loop in gut_associated_microbiota_metabolism "
    "(#617), resolving the record's x-gut-oxygen-causal-direction knowledge gap in favour "
    "of its would_support criterion. Added nodes butyrate (CHEBI:17968) and "
    "colonocyte_oxidative_metabolism, and three edges: primary_fermenter_community "
    "-[biolink:produces]-> butyrate -[RO:0002213]-> colonocyte_oxidative_metabolism "
    "-[RO:0002326]-> luminal_oxygen_limitation. The return arm is modelled as HOST-MEDIATED "
    "rather than as direct microbial oxygen consumption, because that is what the sources "
    "show. The closing edge carries DOI:10.1073/pnas.1718635115 as bounding evidence: bulk "
    "centre-lumen pO2 is near-identical in germ-free and conventional mice, so the claim is "
    "scoped to mucosal-to-luminal oxygen flux and must not drift into bulk anoxia. No "
    "connectivity-only edge was invented to attach this component to the trait node."
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

    nodes = graph.setdefault("nodes", [])
    edges = graph.setdefault("edges", [])
    existing_nodes = {n.get("node_id") for n in nodes}

    for anchor in ("primary_fermenter_community", "luminal_oxygen_limitation"):
        if anchor not in existing_nodes:
            print(f"ERROR: anchor node {anchor!r} is missing", file=sys.stderr)
            return 1

    add_nodes = [n for n in NEW_NODES if n["node_id"] not in existing_nodes]
    have = {(e.get("subject"), e.get("object")) for e in edges}
    add_edges = [e for e in NEW_EDGES if (e["subject"], e["object"]) not in have]

    if not add_nodes and not add_edges:
        print("Nothing to do: nodes and edges already present.")
        return 0

    print(f"{TARGET.relative_to(REPO_ROOT)} :: {GRAPH_ID}")
    for n in add_nodes:
        print(f"  WOULD ADD NODE {n['node_id']} [{n['node_type']}] {n.get('grounding','')}")
    for e in add_edges:
        print(f"  WOULD ADD EDGE {e['subject']} --{e['predicate_id']}--> {e['object']}"
              f"  ({len(e['evidence'])} evidence item(s))")
    if not args.apply:
        print("\nDry run. Re-run with --apply to write.")
        return 0

    nodes.extend(add_nodes)
    edges.extend(add_edges)
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
