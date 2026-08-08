#!/usr/bin/env python3
"""Burn down the 11 baselined DISPOSITION_MISTYPED / DUPLICATE_GROUNDING findings (#352).

#353 shipped the detection and baselined what it found. This is the burn-down.

THE HEADLINE IS THAT NONE OF THEM WERE RETYPES. #352 framed the fix as "sweep
CAPACITY nodes matching the disposition pattern and retype them". Not one of the
eight survived the attempt, and the thing that killed each one is the grounding:

    every TRAIT node in the corpus is grounded, so retyping a node forces you to
    name the term it IS -- and for all eight, the only available term restates
    the record, contradicts it, or is narrower than the node it labels.

Grounding them anyway trades a DISPOSITION_MISTYPED for a DUPLICATE_GROUNDING,
or for a false claim, and calls it progress. Requiring a grounding is what
exposes that, which is #352's own third bullet read strictly.

It took three rounds to get here, and the count went 4 -> 2 -> 0:

  round 1  called four retypes and four restatements.
  round 2  (#360 review) salt_tolerance_breadth was grounded METPO:1000622 while
           keeping `is a -> nacl_delta`, asserting halotolerant sub NaCl-delta;
           oxygen_tolerance was grounded METPO:1000609, sub the record's own
           METPO:1000601 and false of the obligate aerobes it covers.
  round 3  (#360 review) salt_tolerance was grounded METPO:1000622, a DIRECT
           SIBLING of the record's METPO:1000625 asserting the negation of it
           ("does not require salt" vs "requires salt"); low_ph_tolerance was
           grounded METPO:1003008, whose definition excludes the acidophiles
           the generic pH-delta record covers.

The lesson worth keeping: "is this term distinct from the record's own?" is the
WRONG test, and it passed all four of the nodes that later failed. The right
test is whether the term is COMPATIBLE with the record and no NARROWER than the
node -- a sibling term is maximally distinct and still wrong.

MEASURED, NOT ASSERTED: retyping changed the component structure of ZERO of the
eight graphs -- it only ever added an anchor inside what was already there.
Merging improves three of them (oxygen_preference 3 components -> 2, ph_delta
3 -> 2, ph_delta_low 5 -> 4); the other five are pure deduplication and leave
the component count where it was. Both facts are invisible in
UNREACHABLE_FROM_TRAIT, which reads 1296 either way, and that is why #359
exists. Saying "eight merges, three of them structural" is the honest claim;
saying "merging attaches the islands" would be this migration making exactly
the kind of overclaim it was written to catch.

#352's third bullet is what made this findable: "retype in one pass, GROUNDING
EACH -- an ungrounded new TRAIT node silently becomes a reachability anchor and
makes UNREACHABLE_FROM_TRAIT fall without the graph actually becoming more
connected." It warns about the anchor effect and suggests requiring a grounding
as the remedy. Requiring one did something better than prevent the anchor: it
made every retype in the sweep fail out loud.

CAPACITY IS NOT VESTIGIAL, which the issue left open. 24 nodes carry it; these 8
leave 16, and the survivors are a different sense entirely -- `reducing_power`
(a pool of reductants), `cytoplasmic_buffering_capacity` (a reservoir),
`swimming_velocity` (a rate), `metabolic_versatility` (a breadth). Reservoir and
quantity capacities are not organism dispositions and must stay. That two-senses
split is the same shape `reduces` recorded in mappings/predicate_grounding.tsv,
and it is why #353's heuristic is organism-scoped rather than matching bare
"capacity to".

Usage:
    python scripts/migrate_disposition_typing.py [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import emit_trait_yaml  # noqa: E402

TRAITS = REPO_ROOT / "data" / "traits"

# Fixed rather than wall-clock, because pages/ derives its "Corpus as of" stamp
# from the latest curation_history entry (#228) and a clock would make every
# re-run of this migration produce a different 477-page diff.
TIMESTAMP = "2026-08-08T05:00:00Z"

# The first pass logged all eleven events as RETYPE_CAUSAL_NODE, including the
# seven that were not retypes at all. An audit trail that calls a merge a retype
# cannot answer the question it exists to answer, so each kind gets its own
# label. RETYPE_CAUSAL_NODE now goes unused, which is the honest outcome.
ACTIONS = {
    "retype": "RETYPE_CAUSAL_NODE",
    "merge": "MERGE_CAUSAL_NODE",
    "drop": "DROP_CAUSAL_NODE",
    "reground": "REGROUND_CAUSAL_NODE",
    "unground": "UNGROUND_CAUSAL_NODE",
}

# --- no retypes -------------------------------------------------------------
# THIS TABLE IS EMPTY, AND THAT IS THE FINDING. #352 framed the whole issue as
# a retype sweep; three rounds of review took the retype count 4 -> 2 -> 0. Each
# round failed the same test: the grounding a node needs in order to BE a trait
# turned out to restate, contradict, or narrow the record it sits in. Kept as an
# empty table rather than deleted, because "we looked and there were none" and
# "we never modelled retypes" are different claims and only one is true.
RETYPE: dict[tuple[str, str], dict] = {
}

# --- the eight restatements --------------------------------------------------
# `into` repoints the node's edges onto an existing node and drops it; `drop`
# removes a leaf outright.
MERGE: dict[tuple[str, str], dict] = {
    ("environment/slightly_halophilic.yaml", "salt_tolerance"): {
        "into": "slightly_halophilic_trait",
        "why": "A SEVENTH restatement, caught in the third review round (#360). I had "
               "grounded it METPO:1000622 (halotolerant), reasoning that the record is "
               "METPO:1000625 (slightly halophilic) so the term is 'distinct'. It is "
               "distinct in the worst way: 1000622 and 1000625 are DIRECT SIBLINGS under "
               "1000629 (halophily preference), and 1000622 means 'tolerates high salt "
               "but DOES NOT REQUIRE it for growth' while 1000625 means the organism "
               "'REQUIRES low to moderate salt for optimal growth'. So the node asserted "
               "of this record the negation of what the record's own term says. Distinct "
               "is not the test; compatible is. NO CONNECTIVITY CLAIM HERE: the node was "
               "already in the trait's component via osmoprotectant_transport -> "
               "compatible_solutes -> osmotic_stress, so merging leaves the graph at 2 "
               "components and is a correctness fix, not a structural one. METPO has no "
               "generic salt-tolerance disposition to reground to -- filed as a proposal.",
    },
    ("environment/ph_delta.yaml", "low_ph_tolerance"): {
        "into": "ph_delta_trait",
        "why": "An EIGHTH restatement (#360). I had grounded it METPO:1003008 "
               "(acidotolerant) and claimed 'no collision' with the record's "
               "METPO:1000232 (pH delta). No collision, but the wrong SCOPE: 1003008 is "
               "defined as tolerating acid 'WHILE MAINTAINING OPTIMAL GROWTH NEAR NEUTRAL "
               "pH', which excludes the acidophiles this generic pH-delta record covers. "
               "A grounding narrower than the node it labels is a false claim about every "
               "organism in the excluded part. Also a pure sink. Merging repoints "
               "amino_acid_decarboxylase_acid_resistance onto ph_delta_trait, which reads "
               "correctly: an acid-resistance system widens the growth-supporting pH "
               "range, and a pH delta IS that range.",
    },
    ("environment/nacl_delta_low.yaml", "salt_tolerance_breadth"): {
        "into": "nacl_delta",
        "why": "A FIFTH restatement, caught in review (#360). 'Capacity to grow across a "
               "range of ambient NaCl concentrations' against nacl_delta's 'Breadth of the "
               "growth-supporting NaCl range' -- the same claim, and nacl_delta is in the "
               "same graph already TRAIT and already grounded METPO:1000335. I had "
               "retyped it and grounded it METPO:1000622 (halotolerant), which is a "
               "DEGREE of tolerance, not a breadth: 1000622 is a halophily preference "
               "(sub 1000629) while 1000335 is a delta (sub 1000532/1000534), so the "
               "node's existing `is a -> nacl_delta` edge asserted halotolerant sub NaCl "
               "delta, a subsumption METPO does not have. The absolute-vs-breadth "
               "distinction this migration insists on for pH, missed for salt.",
    },
    ("environment/oxygen_preference.yaml", "oxygen_tolerance"): {
        "into": "oxygen_preference_trait",
        "why": "A SIXTH restatement (#360). METPO:1000601's own definition is 'an "
               "organism's oxygen requirements OR TOLERANCE for growth', so 'capacity of "
               "a cell to survive exposure to molecular oxygen' is part of what the "
               "anchor already says. I had grounded it METPO:1000609 (aerotolerant), "
               "which METPO defines as 'does NOT USE O2 for growth but tolerates its "
               "presence' -- the aerotolerant-anaerobe phenotype, false of the obligate "
               "aerobes this node also covers -- and which is itself sub METPO:1000601, "
               "making it a sixth child phenotype in a graph that wires the other four "
               "in with `is a` and left this one unlinked. aerotolerant.yaml, the record "
               "FOR 1000609, has no such node at all: it models the same biology as "
               "detoxification processes. Merging attaches the ROS-defence island to the "
               "trait, which unlike a retype is a real connectivity gain.",
    },
    ("environment/ph_delta_low.yaml", "ph_homeostasis_capacity"): {
        "into": "cytoplasmic_ph_homeostasis",
        "why": "'Capacity to balance and maintain cytoplasmic pH under pH stress' is "
               "cytoplasmic_ph_homeostasis, which is IN THE SAME GRAPH already typed "
               "BIOLOGICAL_PROCESS and grounded GO:0051453. Grounding the capacity node "
               "to GO:0051453 would have produced a DUPLICATE_GROUNDING against it.",
    },
    ("morphology/sphere_shaped.yaml", "elongation_capacity"): {
        "into": "lateral_elongation",
        "why": "'Capacity of a cell to elongate into a rod via sidewall growth' against "
               "lateral_elongation's 'Sidewall growth mode that lengthens rods' -- the "
               "same claim twice, and both already carried `reduced in -> "
               "sphere_shaped_trait`.",
    },
    ("morphology/non_spore_forming.yaml", "loss_sporulation_capacity"): {
        "into": "non_spore_forming_trait",
        "why": "'Loss of the capacity to undergo sporulation' IS the record's own trait "
               "(METPO:1000872, non-spore forming), so the only correct grounding "
               "duplicates the anchor. Collapsing leaves low_spo0a_activity -causes-> "
               "non_spore_forming_trait, which is the shape loss_sporulation_genes "
               "already uses in this graph.",
    },
    ("environment/psychrotolerant.yaml", "growth_at_4c"): {
        "drop": True,
        "why": "'Ability to grow at refrigeration-range low temperature (4 C)' IS "
               "METPO:1000618 (psychrotolerant), the record's own term and the grounding "
               "of psychrotolerant_trait, which is the node it hangs off. A leaf "
               "restating its own parent. The parent keeps two other in-edges "
               "(cold_shock_response confers, facultative_lipid_remodeling manifests as), "
               "so nothing is stranded.",
    },
}

# --- duplicate groundings ----------------------------------------------------
REGROUND: dict[tuple[str, str], dict] = {
    ("environment/ph_delta_high.yaml", "growth_external_ph_5_5_9"): {
        "grounding": "METPO:1000332",  # pH range
        "why": "Shared METPO:1000478 with ph_delta_high_trait, but the two say different "
               "things: this node is an ABSOLUTE external range ('~5.5-9.0'), while "
               "ph_delta_high_trait is a BREADTH ('approximately 5-9 pH units'), which is "
               "what a pH DELTA is. 1000478 belongs to the delta; this is a pH range "
               "(METPO:1000332).",
    },
    ("physiology/catalase_activity.yaml", "catalase"): {
        "grounding": None,
        "why": "GO:0004096 is 'catalase ACTIVITY' -- a molecular function, which is what "
               "catalase_function is. A protein is not its activity, and the graph already "
               "says so correctly: catalase -enables-> catalase_function. Dropped from the "
               "protein, kept on the function.",
    },
    ("physiology/urease_activity.yaml", "urease"): {
        "grounding": None,
        "why": "GO:0009039 is 'urease ACTIVITY'. Same as catalase: kept on urease_function, "
               "dropped from the protein that enables it.",
    },
}


def apply(dry_run: bool = False) -> int:
    files: dict[str, list] = {}
    for kind, table in (("retype", RETYPE), ("merge", MERGE), ("reground", REGROUND)):
        for (rel, node_id), spec in table.items():
            files.setdefault(rel, []).append((kind, node_id, spec))

    for rel, actions in sorted(files.items()):
        path = TRAITS / rel
        doc = yaml.safe_load(path.read_text())
        events: list[tuple[str, str]] = []
        for kind, node_id, spec in actions:
            graph = next((g for g in doc.get("causal_graphs") or []
                          if any(n.get("node_id") == node_id for n in g.get("nodes") or [])),
                         None)
            if graph is None:
                print(f"  MISSING NODE {rel} {node_id}", file=sys.stderr)
                return 1
            nodes = graph["nodes"]
            node = next(n for n in nodes if n["node_id"] == node_id)

            if kind == "retype":
                was = node.get("node_type")
                node["node_type"] = "TRAIT"
                node["grounding"] = spec["grounding"]
                print(f"  retype  {rel} {node_id} -> TRAIT {spec['grounding']}")
                events.append(("retype", f"Retyped node {node_id} from {was} to TRAIT and "
                                         f"grounded it {spec['grounding']}. Issue 352. "
                                         f"{spec['why']}"))

            elif kind == "reground":
                if spec["grounding"] is None:
                    was_grounding = node.pop("grounding", None)
                    print(f"  unground {rel} {node_id}")
                    events.append(("unground", f"Dropped the grounding {was_grounding} from node "
                                               f"{node_id}. Issue 352. {spec['why']}"))
                else:
                    was_grounding = node.get("grounding")
                    node["grounding"] = spec["grounding"]
                    print(f"  reground {rel} {node_id} -> {spec['grounding']}")
                    events.append(("reground", f"Regrounded node {node_id} from {was_grounding} to "
                                               f"{spec['grounding']}. Issue 352. {spec['why']}"))

            else:  # merge
                target = spec.get("into")
                if target and not any(n["node_id"] == target for n in nodes):
                    print(f"  MISSING TARGET {rel} {target}", file=sys.stderr)
                    return 1
                kept = []
                for e in graph.get("edges") or []:
                    if node_id not in (e["subject"], e["object"]):
                        kept.append(e)
                        continue
                    if not target:
                        continue  # drop the leaf's edge outright
                    e["subject"] = target if e["subject"] == node_id else e["subject"]
                    e["object"] = target if e["object"] == node_id else e["object"]
                    if e["subject"] == e["object"]:
                        continue  # collapsed onto itself
                    # An edge identical to one already present is a restatement too.
                    if any(k["subject"] == e["subject"] and k["object"] == e["object"]
                           and k.get("predicate") == e.get("predicate") for k in kept):
                        continue
                    kept.append(e)
                graph["edges"] = kept
                graph["nodes"] = [n for n in nodes if n["node_id"] != node_id]
                print(f"  merge   {rel} {node_id} -> {target or '(dropped)'}")
                if target:
                    events.append(("merge", f"Merged node {node_id} into {target} and repointed its "
                                            f"edges. Issue 352. {spec['why']}"))
                else:
                    events.append(("drop", f"Dropped node {node_id} and its edges. Issue 352. "
                                           f"{spec['why']}"))

        for key, changes in events:
            record_curation_event(doc, curator="claude", action=ACTIONS[key],
                                  changes=changes, llm_assisted=True, timestamp=TIMESTAMP)

        if not dry_run:
            path.write_text(emit_trait_yaml(doc))
    print(f"\n{sum(len(v) for v in files.values())} finding(s) resolved across "
          f"{len(files)} file(s){' (dry run)' if dry_run else ''}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    return apply(ap.parse_args().dry_run)


if __name__ == "__main__":
    sys.exit(main())
