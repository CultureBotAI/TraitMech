#!/usr/bin/env python3
"""#356 tranche 4 + #384: one id per SENSE for oxygen, and drop a wrong CURIE.

The CHEMICAL/ENVIRONMENTAL_FACTOR families are the first tranche whose answer is
TWO IDS rather than one type, and the corpus already says so: the two senses are
grounded in different ontologies.

    the molecule          CHEBI:15379      dioxygen
    the ambient condition ENVO:...         an environmental oxygen term

#384 reported two ids for one molecule. There are FOUR:

    molecular_oxygen  21   CHEMICAL x20 (CHEBI:15379 x19) + ENVIRONMENTAL_FACTOR x1
    oxygen            13   CHEMICAL x11 (CHEBI:15379 x5)  + ENVIRONMENTAL_FACTOR x2
    dioxygen           1   CHEMICAL      (CHEBI:15379)
    ambient_oxygen     1   ENVIRONMENTAL_FACTOR

So this normalises on SENSE, not on type: every chemical occurrence becomes
`molecular_oxygen`, every ambient one becomes `ambient_oxygen`. No node is
retyped for oxygen at all -- the curators' types were right; the ids were not.

oxygen_preference.yaml is the model rather than a collision: it already carries
`ambient_oxygen` AND `molecular_oxygen` in one graph, which is exactly the shape
the rest of the corpus is being brought to.

AND A WRONG CURIE GOES WITH IT. The two ENVIRONMENTAL_FACTOR `oxygen` nodes are
grounded ENVO:01001495, whose label is "DIOXYGEN DISSOLVED IN MARINE WATER"
(mappings/node_grounding.tsv:170, matched by "exact name match via kg-microbe
index"). Neither record is about marine water -- pink_pigmented.yaml is
carotenoid gene expression, chemoorganotrophic.yaml is aerobic respiration. The
grounding is dropped rather than replaced: no generic ENVO term has been
verified here, and inventing one would repeat the mistake that produced this.
The mapping row that would re-apply it is filed separately.

root_exudates rides along as the third family in the same tranche. Both
occurrences describe the SUBSTANCE ("Plant-derived carbon compounds",
"Host-derived metabolites"), so both are CHEMICAL. rhizosphere_association.yaml
already models the condition as its own node -- `root_exudates` (CHEMICAL)
-causes-> `rhizosphere_habitat` (ENVIRONMENTAL_FACTOR) -- which is the same
two-ids shape and settles it.

Usage:
    python scripts/migrate_oxygen_senses.py [--dry-run]
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
TIMESTAMP = "2026-08-17T02:00:00Z"
ACTION = "NORMALISE_NODE_SENSE"

CHEMICAL_ID = "molecular_oxygen"
AMBIENT_ID = "ambient_oxygen"
# The grounder keys on (label, node_type), NOT node_id, so normalising ids alone
# leaves the field that actually matches untouched — which is half of why the
# retracted CURIE could come back (#403 review). Also a correctness fix in its
# own right: `molecular oxygen` on an ENVIRONMENTAL_FACTOR node reads as the
# molecule sitting on the condition node, which is the distinction this tranche
# exists to draw. `ambient molecular oxygen` is oxygen_preference.yaml's wording,
# the record this tranche treats as the model.
AMBIENT_LABEL = "ambient molecular oxygen"

# Keyed by (node_id, node_type) — by SENSE, which is the actual rule and cannot
# under-apply. A first version hardcoded a per-file list and missed NINE of the
# thirteen `oxygen` occurrences; enumerating files by hand is exactly the shape
# that silently under-applies.
#
# No rationale here quotes a record's description, so the file-keyed form the
# playbook prefers (#395/#401) is not needed: the reason is about the sense, and
# it is equally true in every record carrying it.
#
# spec: (new_id or None, new_type or None, drop_grounding, why)
PLAN: dict[tuple[str, str], tuple[str | None, str | None, bool, str]] = {
    ("oxygen", "CHEMICAL"): (
        CHEMICAL_ID, None, False,
        "The molecule, not the condition — the dioxygen participating in the reaction "
        "the graph describes. Normalised onto molecular_oxygen, the id 20 other "
        "chemical occurrences already use, so one id means one sense corpus-wide "
        "(issues 356, 384).",
    ),
    ("dioxygen", "CHEMICAL"): (
        CHEMICAL_ID, None, False,
        "A third id for the same molecule, grounded CHEBI:15379 like the rest. Folded "
        "into molecular_oxygen: #384 reported two ids for oxygen, and there were four.",
    ),
    ("molecular_oxygen", "ENVIRONMENTAL_FACTOR"): (
        AMBIENT_ID, None, False,
        "The condition, not the molecule — ambient O2 acting on the cell, which is why "
        "it is typed ENVIRONMENTAL_FACTOR. The type was right and the id was not, so "
        "the chemical id stops carrying both senses.",
    ),
    ("oxygen", "ENVIRONMENTAL_FACTOR"): (
        AMBIENT_ID, None, True,
        "The condition, not the molecule, and typed ENVIRONMENTAL_FACTOR accordingly — "
        "moved to ambient_oxygen. ITS GROUNDING IS ALSO WRONG AND IS DROPPED: "
        "ENVO:01001495 is 'dioxygen dissolved in marine water' "
        "(mappings/node_grounding.tsv, matched by an exact NAME match via the "
        "kg-microbe index), and neither record carrying it is about marine water — one "
        "is carotenoid gene expression, the other aerobic respiration. Dropped rather "
        "than replaced, because no generic environmental-oxygen term has been verified "
        "here and guessing one would repeat the mistake that produced this.",
    ),
    # Already-normalised, so the migration is idempotent from its OWN output and
    # not only from the pre-migration state: after a rename the node's key is the
    # NEW id, which the entries above no longer match (#395's lesson applied to
    # the plan itself).
    ("ambient_oxygen", "ENVIRONMENTAL_FACTOR"): (
        None, None, True,
        "Already the ambient sense. Listed so a re-run still normalises the label and "
        "still retracts ENVO:01001495 if it has been re-applied — the grounder keys on "
        "(label, node_type), so an un-normalised label is what lets the retracted CURIE "
        "come back.",
    ),
    ("root_exudates", "ENVIRONMENTAL_FACTOR"): (
        None, "CHEMICAL", False,
        "The substance, not the condition: root exudates are a set of compounds, which "
        "is what CHEMICAL is for. rhizosphere_association.yaml settles it by modelling "
        "both — root_exudates (CHEMICAL) -causes-> rhizosphere_habitat "
        "(ENVIRONMENTAL_FACTOR) — the same two-ids shape this tranche applies to oxygen.",
    ),
}


def apply(dry_run: bool = False) -> int:
    changed = 0
    for path in sorted(TRAITS.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        rel = str(path.relative_to(TRAITS))
        in_scope, notes = [], []
        for graph in (doc.get("causal_graphs") or []):
            nodes = graph.get("nodes") or []
            ids = {n.get("node_id") for n in nodes}
            for node in nodes:
                key = (node.get("node_id"), node.get("node_type"))
                if key not in PLAN:
                    continue
                new_id, new_type, drop_g, _why = PLAN[key]
                in_scope.append(key)
                old_id = node["node_id"]
                if new_id and new_id != old_id:
                    if new_id in ids:
                        print(f"  COLLISION {rel} {new_id}", file=sys.stderr)
                        return 1
                    node["node_id"] = new_id
                    for e in (graph.get("edges") or []):
                        if e.get("subject") == old_id:
                            e["subject"] = new_id
                        if e.get("object") == old_id:
                            e["object"] = new_id
                    notes.append(f"{old_id} -> {new_id}")
                    print(f"  rename  {rel:50s} {old_id} -> {new_id}")
                if new_type and node.get("node_type") != new_type:
                    node["node_type"] = new_type
                    notes.append(f"{old_id} typed {new_type}")
                    print(f"  retype  {rel:50s} {old_id} -> {new_type}")
                if (new_id or node.get("node_id")) == AMBIENT_ID \
                        and node.get("label") != AMBIENT_LABEL:
                    was_label = node.get("label")
                    node["label"] = AMBIENT_LABEL
                    notes.append(f"label {was_label!r} -> {AMBIENT_LABEL!r}")
                    print(f"  relabel {rel:50s} {was_label!r} -> {AMBIENT_LABEL!r}")
                if drop_g and node.get("grounding"):
                    gone = node.pop("grounding")
                    notes.append(f"dropped grounding {gone}")
                    print(f"  unground {rel:49s} {old_id} ({gone})")
        if in_scope:
            settled = "; ".join(
                f"{PLAN[k][0] or k[0]} is the "
                f"{'ambient' if PLAN[k][0] == AMBIENT_ID else 'chemical'} sense here"
                for k in dict.fromkeys(in_scope))
            why = " ".join(PLAN[k][3] for k in dict.fromkeys(in_scope))
            record_curation_event(
                doc, curator="claude", action=ACTION, llm_assisted=True,
                timestamp=TIMESTAMP, upsert=True,
                changes=f"One node_id per SENSE (issues 356, 384): {settled}. {why}",
            )
            changed += len(notes)
            if not dry_run:
                path.write_text(emit_trait_yaml(doc))
    print(f"\n{changed} change(s){' (dry run)' if dry_run else ''}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    return apply(ap.parse_args().dry_run)


if __name__ == "__main__":
    sys.exit(main())
