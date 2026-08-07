#!/usr/bin/env python3
"""Repair the 16 `enables` edges whose object cannot satisfy RO:0002327's range (#334).

biolink gives `enables` the range 'biological process or activity', which of
CausalNodeTypeEnum's members only BIOLOGICAL_PROCESS, PATHWAY and
MOLECULAR_FUNCTION satisfy. #315 widened the audit from its original TRAIT-only
test to that full range and surfaced 33 edges; #351 took 17, and these are the
remaining 16.

THERE IS NO SINGLE SWEEP HERE. Six distinct idioms are mixed together, and the
right repair differs per idiom. Each is spelled out in DECISIONS below with the
sentence from the record that justifies it, because the object type alone was
never enough to classify them -- the same lesson `reduces` recorded in
mappings/predicate_grounding.tsv when its two senses turned out not to be
separable by object type.

The edits are STRUCTURAL, not textual. Every one of the 15 affected files
round-trips byte-identically through emit_trait_yaml, so the file is parsed,
modified and re-emitted. Earlier migrations spliced raw lines with regexes and
broke YAML three times over (an unquoted ": " in a scalar, an unwrapped append
to a wrapped block, an insertion mid-line) and once mangled prose -- "proper
polar growth" became "proper powth". A regex editing a structure it does not
parse is the wrong tool, and here it is not needed.

Usage:
    python scripts/migrate_enables_range_edges.py [--dry-run]
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

# (file, graph_id, subject, object) -> what to do and why.
#
# `predicate`/`predicate_id` replace the grounding; `object`/`subject` repoint
# the edge; `retype` changes a node's node_type; `description` rewrites the edge
# note when the repair changes what the edge asserts.
DECISIONS: dict[tuple[str, str, str, str], dict] = {

    # --- idiom 1: the object was the machine, but the graph already held the
    # process the subject actually feeds. Repointing keeps `enables` and needs
    # no new term.
    ("environment/ph_range_high.yaml", "ph_range_high_extreme_alkaliphile",
     "cytoplasmic_na", "mrp_antiporter_complex"): {
        "object": "extreme_alkaliphile_antiport",
        "why": "The record already says it: 'Cytoplasmic Na+ is the substrate that "
               "sustains high levels of alkaliphile antiport activity.' The ANTIPORT "
               "is what the Na+ pool sustains, and that node is in the same graph.",
    },

    # --- idiom 2: the edge was simply backwards. The oxidase's own description
    # states the correct direction, and the object it needs is already present.
    ("environment/facultative_oxygen_preference.yaml",
     "facultative_oxygen_preference_switching",
     "molecular_oxygen", "terminal_oxidase_cytochrome_bd"): {
        "subject": "terminal_oxidase_cytochrome_bd",
        "object": "aerobic_respiration",
        "description": "Cytochrome bd is a high-affinity terminal oxidase, sustaining "
                       "aerobic respiration at the low O2 tensions where low-affinity "
                       "oxidases cannot operate.",
        "why": "The node description already reads 'High-affinity terminal oxidase "
               "ENABLING oxygen respiration at low O2 tensions' -- protein enables "
               "process, which is both domain- and range-correct. Written the other "
               "way round it claimed O2 enables a protein. The graph's existing "
               "molecular_oxygen -enables-> aerobic_respiration edge already carries "
               "the O2-availability link, so nothing is lost.",
    },

    # --- idiom 3: an energetic driver powering a molecular machine (5 edges).
    # RO has no relation for this: it models energetics at the process level and
    # these objects are protein complexes -- the same gap `exports`/`imports`
    # recorded ("RO models transport at the process level, so no RO relation
    # admits the GENE_OR_PROTEIN subject these edges use"). Minted as
    # METPO:2007900 `powers`, whose label is the verb every one of these five
    # edge descriptions already uses.
    ("morphology/motile.yaml", "motile_energy_dependent_locomotion",
     "ion_motive_force", "flagellar_motor"): {
        "predicate": "powers", "predicate_id": "METPO:2007900",
        "why": "'Ion motive force POWERS rotation of the flagellar motor.'",
    },
    ("morphology/motile.yaml", "motile_energy_dependent_locomotion",
     "motor_torque", "flagellar_motor"): {
        "predicate": "powers", "predicate_id": "METPO:2007900",
        "why": "'Torque generation drives rotation of the flagellar motor.'",
    },
    ("morphology/motility.yaml", "motility_locomotion_machinery",
     "ion_motive_force", "flagellar_motor"): {
        "predicate": "powers", "predicate_id": "METPO:2007900",
        "why": "'Ion motive force POWERS rotation of many bacterial flagellar motors.'",
    },
    ("morphology/flagellated.yaml", "flagellated_flagellar_motor",
     "ion_motive_force", "stator_complex"): {
        "predicate": "powers", "predicate_id": "METPO:2007900",
        "why": "'Ion flux through stator complexes POWERS torque generation.'",
    },
    ("morphology/gliding.yaml", "gliding_surface_motility",
     "proton_motive_force", "gliding_motility_machinery"): {
        "predicate": "powers", "predicate_id": "METPO:2007900",
        "why": "'Proton motive force can POWER gliding motility motors.'",
    },

    # --- idiom 4: the subject makes or moves the object. Three different
    # relations, split by what the subject IS -- the split predicate_grounding
    # already documents between `produces` and `has output`.
    ("environment/piezophilic.yaml", "piezophilic_hhp_membrane_adaptation",
     "pfa_operon", "omega3_pufa"): {
        "predicate": "produces", "predicate_id": "METPO:2007800",
        "why": "A GENE_OR_PROTEIN subject bringing a CHEMICAL into existence, which "
               "is exactly `produces`' declared gate. NOT `encodes`: the operon "
               "encodes a SYNTHASE, and the synthase makes the PUFA -- `encodes` "
               "does not admit a CHEMICAL object, correctly.",
    },
    ("physiology/chemolithoheterotrophic.yaml",
     "chemolithoheterotrophic_inorganic_energy_organic_carbon",
     "sox_pathway", "sulfate"): {
        "predicate": "has output", "predicate_id": "RO:0002234",
        "why": "The subject IS an activity (PATHWAY), which is the documented "
               "dividing line: activity subjects take RO:0002234, whose domain "
               "'biological process or activity' they satisfy, rather than the "
               "METPO term minted for the subjects RO cannot cover.",
    },
    ("morphology/sphere_shaped.yaml", "sphere_shaped_septal_peptidoglycan",
     "ftsW_flippase", "lipid_ii"): {
        "predicate": "transports", "predicate_id": "METPO:2007812",
        "why": "'FtsW FLIPS lipid II to the outer septal face' -- a flippase moves "
               "its substrate across the membrane, which is transport, not "
               "enablement. Needs GENE_OR_PROTEIN added to `transports`' "
               "subject_types, which is a deliberate widening recorded there.",
    },

    # --- idiom 5: the object was never a process at all.
    ("morphology/filament_shaped.yaml", "filament_shaped_streptomyces_polar_growth",
     "scy", "apical_polarisome"): {
        "predicate": "part of", "predicate_id": "biolink:part_of",
        "why": "'Scy is a COMPONENT of the tip-organizing center.' Mereology, not "
               "causation. The corpus already uses `part of` this way "
               "(flii_atpase_complex part of ft3ss_export_system).",
    },
    ("physiology/stress_response.yaml", "stress_response_induction",
     "hfq", "rpos"): {
        "predicate": "promotes", "predicate_id": "RO:0002213",
        "why": "'Hfq enables sRNA-dependent TRANSLATION of RpoS' -- the object is "
               "the sigma factor, not the translation, so what the edge actually "
               "asserts about RpoS is that Hfq increases it. The graph already "
               "reads ppgpp -positively regulates-> rpos alongside it.",
    },

    # --- idiom 6: a QUALITY object that is really a disposition or a process.
    # Retyping the node is the fix; the predicate follows from the new type.
    ("ecology/human_pathogen.yaml", "human_pathogen_anthropoid_adaptation",
     "biofilm_formation", "treatment_resistance_persistence"): {
        "predicate": "confers", "predicate_id": "METPO:2007700",
        "retype": {"treatment_resistance_persistence": "TRAIT"},
        "why": "'Tolerance to antimicrobial treatment and persistent infection' is a "
               "DISPOSITION -- what the organism would do under treatment -- not a "
               "quality it displays. Retyped to TRAIT, which makes this the same "
               "shape #302 solved for 164 edges, and `confers` already admits a "
               "BIOLOGICAL_PROCESS subject.",
    },
    ("morphology/gas_vesicle.yaml", "gas_vesicle_buoyancy",
     "gas_vesicle_trait", "buoyancy"): {
        "predicate": "confers", "predicate_id": "METPO:2007700",
        "retype": {"buoyancy": "TRAIT"},
        "why": "The corpus already types this concept BOTH ways: buoyancy is TRAIT in "
               "intracellular_inclusion.yaml, where gas_vesicle -confers-> buoyancy, "
               "and QUALITY here. That is a typing inconsistency (#352's shape), and "
               "the TRAIT reading is the right one -- 'reduced effective cell density "
               "permitting vertical positioning' is a disposition. Needs TRAIT added "
               "to `confers`' subject_types, recorded there as a decision.",
    },
    ("morphology/cell_width_large.yaml", "cell_width_large_setpoint_increase",
     "rod_complex_rotation", "even_pg_distribution"): {
        "retype": {"even_pg_distribution": "BIOLOGICAL_PROCESS"},
        "why": "The label reads like a quality but the description does not: "
               "'Evenly distributed INSERTION of peptidoglycan in the cell-surface "
               "layer.' Insertion is a process, so `enables` is already the right "
               "relation and only the node type was wrong.",
    },
    ("morphology/intracellular_inclusion.yaml", "inclusion_compartmentalization",
     "inclusion_trait", "cytoplasmic_compartmentalization"): {
        "predicate": "manifests as", "predicate_id": "METPO:2007400",
        "why": "Unlike buoyancy, compartmentalization is not a disposition the "
               "inclusion confers -- it is how the inclusion PRESENTS: 'spatial "
               "segregation of material or activity within the cytoplasm'. That is "
               "what `manifests as` is for, and its gate is already open.",
    },
}


def apply(dry_run: bool = False) -> int:
    by_file: dict[str, list[tuple]] = {}
    for key in DECISIONS:
        by_file.setdefault(key[0], []).append(key)

    changed = 0
    for rel, keys in sorted(by_file.items()):
        path = TRAITS / rel
        original = path.read_text()
        doc = yaml.safe_load(original)
        for key in keys:
            _, gid, subj, obj = key
            spec = DECISIONS[key]
            graph = next((g for g in doc.get("causal_graphs") or []
                          if g.get("graph_id") == gid), None)
            if graph is None:
                print(f"  MISSING GRAPH {rel} [{gid}]", file=sys.stderr)
                return 1
            edge = next((e for e in graph.get("edges") or []
                         if e.get("subject") == subj and e.get("object") == obj
                         and e.get("predicate_id") == "RO:0002327"), None)
            if edge is None:
                print(f"  MISSING EDGE {rel} [{gid}] {subj}->{obj}", file=sys.stderr)
                return 1
            for field in ("subject", "object", "predicate", "predicate_id",
                          "description"):
                if field in spec:
                    edge[field] = spec[field]
            nodes = {n["node_id"]: n for n in graph.get("nodes") or []}
            for node_id, node_type in (spec.get("retype") or {}).items():
                if node_id not in nodes:
                    print(f"  MISSING NODE {rel} [{gid}] {node_id}", file=sys.stderr)
                    return 1
                nodes[node_id]["node_type"] = node_type
            changed += 1
            print(f"  {rel} [{gid}] {subj} -> {obj}")
        rendered = emit_trait_yaml(doc)
        if not dry_run:
            path.write_text(rendered)
    print(f"\n{changed} edge(s) repaired across {len(by_file)} file(s)"
          f"{' (dry run)' if dry_run else ''}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    return apply(ap.parse_args().dry_run)


if __name__ == "__main__":
    sys.exit(main())
