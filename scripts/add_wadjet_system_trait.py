#!/usr/bin/env python3
"""Add the Wadjet system genomics trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "wadjet_system.yaml"

DEEP = "DOI:10.1016/j.molcel.2022.09.008"
LIU = "DOI:10.1016/j.molcel.2022.11.015"
WEISS = "DOI:10.1093/nar/gkad130"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T14:19:20Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000218",
    "label": "Wadjet system",
    "definition": (
        "A genomics trait describing possession of a Wadjet anti-plasmid "
        "defense locus encoding a derivative SMC complex such as JetABCD, "
        "MksBEFG, or EptABCD that restricts circular plasmids by "
        "ATPase-dependent DNA cleavage."
    ),
    "definition_source": LIU,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000188"],
    "synonyms": [
        {
            "synonym_text": "Wadjet defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEEP,
        }
    ],
    "evidence": [
        {
            "reference": LIU,
            "snippet": (
                "Wadjet systems (JetABCD/MksBEFG/EptABCD) are derivative "
                "SMC complexes with roles in bacterial immunity against "
                "selfish DNA"
            ),
            "notes": (
                "Liu et al. support defining Wadjet as a recurring "
                "SMC-derived bacterial immune system spanning JetABCD, "
                "MksBEFG, and EptABCD subfamilies."
            ),
        },
        {
            "reference": DEEP,
            "snippet": (
                "the Wadjet defense system recognizes DNA topology to "
                "protect its host against plasmid transformation"
            ),
            "notes": (
                "Deep et al. support the standard Wadjet defense system "
                "name and connect the system to anti-plasmid immunity."
            ),
        },
        {
            "reference": DEEP,
            "snippet": (
                "Wadjet forms a complex similar to the bacterial condensin "
                "complex MukBEF, with a novel nuclease subunit similar to a "
                "type II DNA topoisomerase"
            ),
            "notes": (
                "Deep et al. support the SMC-family complex architecture "
                "and JetD-like nuclease component."
            ),
        },
        {
            "reference": LIU,
            "snippet": (
                "Purified JetABCD complexes cleave circular DNA molecules, "
                "regardless of the DNA helical topology; cleavage is DNA "
                "sequence nonspecific and depends on the SMC ATPase"
            ),
            "notes": (
                "Liu et al. connect JetABCD SMC ATPase activity to "
                "sequence-independent cleavage of circular plasmid DNA."
            ),
        },
        {
            "reference": WEISS,
            "snippet": "MksG is a nuclease that degrades plasmid DNA",
            "notes": (
                "Weiss et al. support the MksG nuclease as the executing "
                "plasmid-DNA-degradation component of MksBEFG."
            ),
        },
        {
            "reference": WEISS,
            "snippet": (
                "Introduction of plasmids results in an increase in DNA "
                "bound MksG, indicating an activation of the system in vivo"
            ),
            "notes": (
                "Weiss et al. support plasmid-responsive activation of the "
                "Corynebacterium glutamicum MksBEFG system in vivo."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1718",
            "taxon_label": "Corynebacterium glutamicum",
            "note": (
                "Weiss et al. investigated the Corynebacterium glutamicum "
                "MksBEFG complex and showed that plasmid introduction "
                "increased DNA-bound MksG in vivo."
            ),
            "reference": WEISS,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "wadjet_smc_plasmid_restriction",
            "title": "Wadjet SMC complexes cleave circular plasmid DNA",
            "description": (
                "Evidence-backed process sketch linking a Wadjet locus to "
                "SMC ATPase cycling, Wadjet nuclease-mediated circular "
                "plasmid cleavage, and restriction of plasmid transformation."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures JetABCD and MksBEFG family-level "
                "anti-plasmid outputs without asserting one universal "
                "subfamily architecture, plasmid size threshold, linear "
                "plasmid escape rule, polar scaffold, DNA-loop-extrusion "
                "state, or activation cue across all Wadjet loci."
            ),
            "nodes": [
                {
                    "node_id": "wadjet_locus",
                    "label": "Wadjet locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Wadjet anti-plasmid defense locus encoding "
                        "JetABCD, MksBEFG, EptABCD, or related SMC-family "
                        "components."
                    ),
                },
                {
                    "node_id": "wadjet_smc_atpase_cycle",
                    "label": "Wadjet SMC ATPase cycle",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "ATPase cycling by the Wadjet SMC core complex "
                        "during circular DNA restriction."
                    ),
                },
                {
                    "node_id": "wadjet_plasmid_dna_cleavage",
                    "label": "Wadjet plasmid DNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cleavage or processive degradation of circular "
                        "plasmid DNA by a Wadjet-associated nuclease."
                    ),
                },
                {
                    "node_id": "plasmid_transformation",
                    "label": "plasmid transformation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Introduction and establishment of exogenous "
                        "plasmid DNA in a bacterial cell."
                    ),
                },
                {
                    "node_id": "wadjet_system_trait",
                    "label": "Wadjet system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000218",
                    "description": (
                        "Possession of a genome-encoded Wadjet "
                        "anti-plasmid defense locus."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "wadjet_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "wadjet_smc_atpase_cycle",
                    "description": (
                        "Wadjet loci encode derivative SMC complexes with "
                        "Jet, Mks, or Ept ATPase cores."
                    ),
                    "evidence": [
                        {
                            "reference": LIU,
                            "snippet": (
                                "Wadjet systems (JetABCD/MksBEFG/EptABCD) "
                                "are derivative SMC complexes with roles in "
                                "bacterial immunity against selfish DNA"
                            ),
                            "notes": (
                                "Liu et al. support JetABCD, MksBEFG, and "
                                "EptABCD as Wadjet-family SMC complexes."
                            ),
                        }
                    ],
                },
                {
                    "subject": "wadjet_smc_atpase_cycle",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "wadjet_plasmid_dna_cleavage",
                    "description": (
                        "The Wadjet SMC ATPase cycle enables nuclease-driven "
                        "cleavage of circular plasmid DNA."
                    ),
                    "evidence": [
                        {
                            "reference": LIU,
                            "snippet": (
                                "Purified JetABCD complexes cleave circular "
                                "DNA molecules, regardless of the DNA helical "
                                "topology; cleavage is DNA sequence "
                                "nonspecific and depends on the SMC ATPase"
                            ),
                            "notes": (
                                "Liu et al. support SMC-ATPase-dependent "
                                "cleavage by purified JetABCD."
                            ),
                        },
                        {
                            "reference": WEISS,
                            "snippet": (
                                "The MksBEF subunits exhibit an ATPase cycle "
                                "in vitro"
                            ),
                            "notes": (
                                "Weiss et al. support ATPase cycling by the "
                                "C. glutamicum MksBEF core."
                            ),
                        },
                    ],
                },
                {
                    "subject": "wadjet_plasmid_dna_cleavage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "plasmid_transformation",
                    "description": (
                        "Wadjet-mediated plasmid DNA cleavage restricts "
                        "incoming circular plasmids."
                    ),
                    "evidence": [
                        {
                            "reference": DEEP,
                            "snippet": (
                                "the Wadjet defense system recognizes DNA "
                                "topology to protect its host against "
                                "plasmid transformation"
                            ),
                            "notes": (
                                "Deep et al. support Wadjet-mediated "
                                "protection against plasmid transformation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "wadjet_plasmid_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "wadjet_system_trait",
                    "description": (
                        "Wadjet nuclease-mediated plasmid DNA cleavage is "
                        "the anti-plasmid output that realizes the Wadjet "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": WEISS,
                            "snippet": (
                                "MksG is a nuclease that degrades plasmid DNA"
                            ),
                            "notes": (
                                "Weiss et al. support MksG nuclease activity "
                                "as a Wadjet/MksBEFG plasmid-degradation "
                                "output."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "wadjet-subfamily-and-substrate-gap",
            "prompt": (
                "Resolve Wadjet subfamily architecture, plasmid substrate "
                "specificity, and activation cues before minting narrower "
                "Wadjet mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Deep et al. and Liu et al. support JetABCD-mediated "
                "topology- or shape-biased circular plasmid cleavage, and "
                "Weiss et al. support MksG-mediated plasmid degradation in "
                "the MksBEFG subfamily, but Wadjet variants need separate "
                "review before TraitMech asserts one exact target size "
                "threshold, linear-plasmid escape rule, loop-extrusion "
                "endpoint, polar localization pattern, or nuclease "
                "activation model."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        },
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the new TraitRecord YAML",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Wadjet system as a DOI-backed GENOMICS TraitRecord "
            "after an ignored-and-hidden duplicate review found no exact "
            "live TraitMech, METPO, or prior proposal record; the "
            "replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v95."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
