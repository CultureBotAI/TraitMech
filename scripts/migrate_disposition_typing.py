#!/usr/bin/env python3
"""Burn down the 11 baselined DISPOSITION_MISTYPED / DUPLICATE_GROUNDING findings (#352).

#353 shipped the detection and baselined what it found. This is the burn-down.

THE HEADLINE IS THAT ONLY HALF OF THEM WERE RETYPES. #352 framed the fix as
"sweep CAPACITY nodes matching the disposition pattern and retype them", and for
four nodes that is exactly right. For the other four, retyping would have been
wrong in a way that only shows up once you look for the grounding:

    every TRAIT node in the corpus is grounded, and the obvious grounding for
    each of those four is the term its OWN record already carries.

Grounding them that way trades a DISPOSITION_MISTYPED for a DUPLICATE_GROUNDING
and calls it progress. What it actually means is that the node RESTATES its
anchor, and in three of the four cases the node it restates is sitting in the
same graph already correctly typed and grounded. Those get merged, not retyped.

That is #352's own third bullet read strictly: "retype in one pass, GROUNDING
EACH -- an ungrounded new TRAIT node silently becomes a reachability anchor and
makes UNREACHABLE_FROM_TRAIT fall without the graph actually becoming more
connected." Requiring a grounding is what exposes the restatements.

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

from traitmech.validation.write_validated import emit_trait_yaml  # noqa: E402

TRAITS = REPO_ROOT / "data" / "traits"

# --- the four that really are mistyped dispositions --------------------------
# Retyped to TRAIT and grounded to a term that is NOT the record's own, which is
# what distinguishes these from the restatements below.
RETYPE: dict[tuple[str, str], dict] = {
    ("environment/slightly_halophilic.yaml", "salt_tolerance"): {
        "grounding": "METPO:1000622",  # halotolerant
        "why": "'Capacity to grow and survive under elevated salinity' is halotolerance. "
               "The record is METPO:1000625 (slightly halophilic), so this is a distinct "
               "term rather than a restatement of the anchor.",
    },
    ("environment/nacl_delta_low.yaml", "salt_tolerance_breadth"): {
        "grounding": "METPO:1000622",  # halotolerant
        "why": "'Capacity to grow across a range of ambient NaCl concentrations.' Already "
               "behaves as a trait -- it carries `is a -> nacl_delta` (METPO:1000335) -- "
               "and the record is METPO:1000479, so 1000622 collides with neither.",
    },
    ("environment/oxygen_preference.yaml", "oxygen_tolerance"): {
        "grounding": "METPO:1000609",  # aerotolerant
        "why": "'Capacity of a cell to survive exposure to molecular oxygen' is "
               "aerotolerance. Distinct from all five phenotype nodes in the graph "
               "(METPO:1000601/2/3/4/612). NOTE this is the organism-scoped sense; "
               "carboxydotrophic.yaml's same-named node reads 'Ability of an ENZYME to "
               "function in the presence of O2' and is correctly NOT a trait (#353).",
    },
    ("environment/ph_delta.yaml", "low_ph_tolerance"): {
        "grounding": "METPO:1003008",  # acidotolerant
        "why": "'Capacity to grow and survive under acidic external pH' is acidotolerance. "
               "The record is METPO:1000232 (pH delta), so no collision.",
    },
}

# --- the four restatements ---------------------------------------------------
# `into` repoints the node's edges onto an existing node and drops it; `drop`
# removes a leaf outright.
MERGE: dict[tuple[str, str], dict] = {
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
                node["node_type"] = "TRAIT"
                node["grounding"] = spec["grounding"]
                print(f"  retype  {rel} {node_id} -> TRAIT {spec['grounding']}")

            elif kind == "reground":
                if spec["grounding"] is None:
                    node.pop("grounding", None)
                    print(f"  unground {rel} {node_id}")
                else:
                    node["grounding"] = spec["grounding"]
                    print(f"  reground {rel} {node_id} -> {spec['grounding']}")

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
