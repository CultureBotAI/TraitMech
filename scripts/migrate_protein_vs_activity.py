#!/usr/bin/env python3
"""#356 tranche 2: split protein from activity where one id meant both.

Six families carried both GENE_OR_PROTEIN and MOLECULAR_FUNCTION on one
``node_id``. #352 already settled the rule -- "a protein is not its activity",
which is why `catalase`/`urease` lost their GO ACTIVITY groundings and why
`catalase -enables-> catalase_function` is the shape the graphs use.

WHAT THE DESCRIPTIONS SAY DECIDES, and here they are unusually clean. In five of
the six, the GENE_OR_PROTEIN occurrences describe the ENZYME ("Enzyme that
degrades hydrogen peroxide", "Antiporter that expels sodium ions") and the lone
MOLECULAR_FUNCTION occurrence describes the ACTIVITY ("Enzyme activity that
detoxifies hydrogen peroxide", "Desaturase activity introducing double bonds").

So five of these are NOT a typing mistake. The id means two things, and the fix
that #366's own docstring names is TWO IDS, not one type -- retyping either way
would erase a distinction the curator drew correctly. Renaming the activity
occurrence is what makes one id mean one thing.

The sixth, `plasmid_methylase`, is the real retype: BOTH occurrences describe
the enzyme ("Methyltransferase encoded by a mobile element", "Plasmid-borne
methyltransferase shielding plasmid DNA"), neither an activity.

NAMING follows the corpus rather than inventing: `_activity` is used by 25
existing ids against 8 for `_function`, and four of the five targets ALREADY
EXIST corpus-wide as MOLECULAR_FUNCTION nodes, so these renames join an
established concept instead of minting a synonym. None collides with a node
already in its own graph.

Usage:
    python scripts/migrate_protein_vs_activity.py [--dry-run]
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
TIMESTAMP = "2026-08-15T06:00:00Z"

# (file, old_id) -> (new_id, why). The MOLECULAR_FUNCTION occurrence is renamed
# so the protein id stops meaning two things.
RENAME: dict[tuple[str, str], tuple[str, str]] = {
    ("environment/obligately_aerobic.yaml", "catalase"): (
        "catalase_activity",
        "Described as 'Enzyme ACTIVITY that detoxifies hydrogen peroxide', while the "
        "four GENE_OR_PROTEIN occurrences describe the enzyme itself ('Enzyme that "
        "degrades hydrogen peroxide to water and oxygen'). catalase_activity already "
        "exists corpus-wide as a MOLECULAR_FUNCTION node.",
    ),
    ("environment/obligately_aerobic.yaml", "superoxide_dismutase"): (
        "superoxide_dismutase_activity",
        "Described as 'Enzyme ACTIVITY that detoxifies superoxide' against 'Enzyme that "
        "dismutates superoxide' for the protein occurrences. It also carries GO:0004784, "
        "which IS 'superoxide dismutase activity' -- so the grounding was already "
        "describing a molecular function and only the id disagreed. The one new id in "
        "this migration, coined to the corpus's dominant _activity convention.",
    ),
    ("environment/ph_phenotype_with_numerical_limits.yaml", "na_h_antiporter"): (
        "na_h_antiport_activity",
        "Described as 'Cation/proton antiport ACTIVITY regulating internal pH and PMF', "
        "while the six GENE_OR_PROTEIN occurrences describe the transporter ('Membrane "
        "antiporter that exports sodium from the cytoplasm in exchange for protons'). "
        "na_h_antiport_activity already exists corpus-wide as MOLECULAR_FUNCTION.",
    ),
    ("environment/growth_range_phenotype_with_numerical_limits.yaml",
     "cation_proton_antiporter"): (
        "cation_proton_antiporter_activity",
        "Described as 'Ion/H+ antiporter ACTIVITY that exports K+ or Na+ in exchange for "
        "protons', against 'Antiporter exchanging cations for protons during pH stress' "
        "for the protein occurrences. cation_proton_antiporter_activity already exists "
        "corpus-wide as MOLECULAR_FUNCTION.",
    ),
    ("environment/temperature_optimum_very_low.yaml", "fatty_acid_desaturase"): (
        "fatty_acid_desaturase_activity",
        "Described as 'Desaturase ACTIVITY introducing double bonds into fatty acyl "
        "chains', against 'Desaturase enzyme (e.g., Des) that introduces double bonds' "
        "for the protein occurrences. fatty_acid_desaturase_activity already exists "
        "corpus-wide as MOLECULAR_FUNCTION.",
    ),
}

# The one genuine retype: both occurrences describe the enzyme.
RETYPE: dict[tuple[str, str], tuple[str, str]] = {
    ("genomics/plasmid_carriage.yaml", "plasmid_methylase"): (
        "GENE_OR_PROTEIN",
        "The exception in this tranche. Both occurrences describe the ENZYME -- "
        "'Methyltransferase encoded by a mobile element that pre-methylates its DNA' "
        "(GENE_OR_PROTEIN) and 'Plasmid-borne methyltransferase shielding plasmid DNA "
        "from restriction' (MOLECULAR_FUNCTION). Neither names an activity, so there is "
        "one concept here and it is a protein. A rename would have invented a "
        "distinction the corpus does not draw.",
    ),
}


def apply(dry_run: bool = False) -> int:
    touched = 0
    for path in sorted(TRAITS.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        rel = str(path.relative_to(TRAITS))
        notes: list[str] = []
        for graph in (doc.get("causal_graphs") or []):
            nodes = graph.get("nodes") or []
            ids = {n.get("node_id") for n in nodes}
            for node in nodes:
                nid = node.get("node_id")
                key = (rel, nid)
                if key in RENAME:
                    new_id, _why = RENAME[key]
                    if new_id in ids:
                        print(f"  COLLISION {rel} {new_id} already in graph", file=sys.stderr)
                        return 1
                    node["node_id"] = new_id
                    for e in (graph.get("edges") or []):
                        if e.get("subject") == nid:
                            e["subject"] = new_id
                        if e.get("object") == nid:
                            e["object"] = new_id
                    notes.append(f"renamed {nid} -> {new_id} (MOLECULAR_FUNCTION sense)")
                    print(f"  rename  {rel:56s} {nid} -> {new_id}")
                elif key in RETYPE:
                    target, _why = RETYPE[key]
                    was = node.get("node_type")
                    node["node_type"] = target
                    notes.append(f"retyped {nid}: {was} -> {target}")
                    print(f"  retype  {rel:56s} {nid} {was} -> {target}")
        if notes:
            rationale = " ".join(
                spec[1] for tbl in (RENAME, RETYPE)
                for (f, _n), spec in tbl.items() if f == rel
            )
            record_curation_event(
                doc, curator="claude", action="SPLIT_PROTEIN_FROM_ACTIVITY",
                llm_assisted=True, timestamp=TIMESTAMP,
                changes=("Separated the protein sense from the activity sense so one "
                         f"node_id means one thing (issue 356): {'; '.join(notes)}. "
                         f"{rationale}"),
            )
            touched += len(notes)
            if not dry_run:
                path.write_text(emit_trait_yaml(doc))
    print(f"\n{touched} node(s) changed{' (dry run)' if dry_run else ''}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    return apply(ap.parse_args().dry_run)


if __name__ == "__main__":
    sys.exit(main())
