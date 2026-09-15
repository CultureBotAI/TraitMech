#!/usr/bin/env python3
"""Add the Zorya system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "zorya_system.yaml"

HU = "DOI:10.1038/s41586-024-08493-8"
MARIANO = "DOI:10.1038/s41467-025-57397-2"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T13:45:12Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000217",
    "label": "Zorya system",
    "definition": (
        "A genomics trait describing possession of a Zorya antiphage "
        "defense locus in which conserved ZorA/ZorB membrane-motor core "
        "proteins and subtype-specific effector proteins inhibit "
        "bacteriophage propagation."
    ),
    "definition_source": HU,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Zorya anti-phage defence system",
            "synonym_type": "EXACT_SYNONYM",
            "source": HU,
        },
        {
            "synonym_text": "Zorya phage defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": MARIANO,
        },
    ],
    "evidence": [
        {
            "reference": HU,
            "snippet": (
                "Zorya is a recently identified and widely distributed "
                "bacterial immune system that protects bacteria from viral "
                "(phage) infections"
            ),
            "notes": (
                "Hu et al. support Zorya as a bacterial antiviral immune "
                "system."
            ),
        },
        {
            "reference": MARIANO,
            "snippet": (
                "The Zorya phage defense system was first discovered in 2018"
            ),
            "notes": (
                "Mariano et al. support the standard US-English family name "
                "for the Zorya system."
            ),
        },
        {
            "reference": MARIANO,
            "snippet": (
                "all Zorya systems share two components, ZorA and ZorB, "
                "containing domains distantly related, respectively, to the "
                "MotA and MotB subunits of the bacterial flagellar motor"
            ),
            "notes": (
                "Mariano et al. support the conserved ZorA/ZorB motor-core "
                "architecture shared by Zorya systems."
            ),
        },
        {
            "reference": HU,
            "snippet": (
                "ZorAB transfers the phage invasion signal through the ZorA "
                "cytoplasmic tail to recruit and activate the soluble ZorC "
                "and ZorD effectors"
            ),
            "notes": (
                "Hu et al. support the Type I ZorAB-dependent effector "
                "recruitment and activation step."
            ),
        },
        {
            "reference": MARIANO,
            "snippet": (
                "For Zorya II, anti-phage activity requires the presence of "
                "the ZorE effector, which we show is recruited by ZorAB"
            ),
            "notes": (
                "Mariano et al. support Type II ZorE as a "
                "ZorAB-recruited effector."
            ),
        },
        {
            "reference": MARIANO,
            "snippet": (
                "We observed that homologs of Zorya I from Serratia "
                "marcescens ATCC 274 and Zorya II from E. coli ATCC 8739 "
                "provide protection against several phages from the Durham "
                "collection"
            ),
            "notes": (
                "Mariano et al. support experimentally validated Zorya "
                "phage protection from native Serratia marcescens and "
                "E. coli loci."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Mariano et al. report that a Zorya II locus from "
                "E. coli ATCC 8739 protected E. coli MT56 against several "
                "tested coliphages."
            ),
            "reference": MARIANO,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "zorya_zorab_effector_antiphage_defense",
            "title": "Zorya ZorAB motors recruit antiphage effectors",
            "description": (
                "Evidence-backed process sketch linking a Zorya locus to "
                "phage-triggered ZorAB ion-motor activation, effector "
                "recruitment, and inhibition of bacteriophage replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures characterized Type I ZorC/ZorD and "
                "Type II ZorE outputs without asserting one universal "
                "ZorAB-coupled effector, ion substrate, DNA target, "
                "cell-death pathway, Type III mechanism, or "
                "anti-Zorya-evasion mechanism across all Zorya loci."
            ),
            "nodes": [
                {
                    "node_id": "phage_invasion",
                    "label": "phage invasion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Entry of a bacteriophage and its nucleic acid into a "
                        "bacterial host cell."
                    ),
                },
                {
                    "node_id": "zorya_locus",
                    "label": "Zorya locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Zorya antiphage defense locus encoding conserved "
                        "ZorA/ZorB membrane core proteins and "
                        "subtype-specific effector proteins."
                    ),
                },
                {
                    "node_id": "zorab_ion_motor_activation",
                    "label": "ZorAB ion-motor activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of a membrane-anchored ZorA/ZorB "
                        "ion-driven motor after detection of phage invasion."
                    ),
                },
                {
                    "node_id": "zorya_effector_activity",
                    "label": "Zorya effector activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activity of ZorAB-coupled Zorya effector proteins "
                        "such as Type I ZorC/ZorD or Type II ZorE."
                    ),
                },
                {
                    "node_id": "phage_replication",
                    "label": "phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication of invading bacteriophage DNA after "
                        "host-cell entry."
                    ),
                },
                {
                    "node_id": "zorya_system_trait",
                    "label": "Zorya system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000217",
                    "description": (
                        "Possession of a genome-encoded Zorya antiphage "
                        "defense locus."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "zorya_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "zorab_ion_motor_activation",
                    "description": (
                        "Zorya loci encode the conserved ZorA and ZorB "
                        "membrane core proteins that form the ZorAB motor."
                    ),
                    "evidence": [
                        {
                            "reference": MARIANO,
                            "snippet": (
                                "all Zorya systems share two components, ZorA "
                                "and ZorB, containing domains distantly "
                                "related, respectively, to the MotA and MotB "
                                "subunits of the bacterial flagellar motor"
                            ),
                            "notes": (
                                "Mariano et al. support ZorA/ZorB as the "
                                "conserved Zorya core proteins."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_invasion",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "zorab_ion_motor_activation",
                    "description": (
                        "Phage invasion activates the ZorAB ion motor after "
                        "Zorya senses bacteriophage challenge."
                    ),
                    "evidence": [
                        {
                            "reference": HU,
                            "snippet": (
                                "ZorAB operates as a proton-driven motor that "
                                "becomes activated after sensing of phage "
                                "invasion"
                            ),
                            "notes": (
                                "Hu et al. support phage-invasion-dependent "
                                "ZorAB activation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "zorab_ion_motor_activation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "zorya_effector_activity",
                    "description": (
                        "ZorAB motor activation recruits and activates "
                        "subtype-specific Zorya effector proteins."
                    ),
                    "evidence": [
                        {
                            "reference": HU,
                            "snippet": (
                                "ZorAB transfers the phage invasion signal "
                                "through the ZorA cytoplasmic tail to recruit "
                                "and activate the soluble ZorC and ZorD "
                                "effectors"
                            ),
                            "notes": (
                                "Hu et al. support ZorAB-mediated Type I "
                                "ZorC/ZorD activation."
                            ),
                        },
                        {
                            "reference": MARIANO,
                            "snippet": (
                                "For Zorya II, anti-phage activity requires "
                                "the presence of the ZorE effector, which we "
                                "show is recruited by ZorAB"
                            ),
                            "notes": (
                                "Mariano et al. support ZorAB-mediated "
                                "recruitment of the Type II ZorE effector."
                            ),
                        },
                    ],
                },
                {
                    "subject": "zorya_effector_activity",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "Zorya effector activity helps inhibit invading "
                        "bacteriophages."
                    ),
                    "evidence": [
                        {
                            "reference": HU,
                            "snippet": (
                                "soluble ZorC and ZorD effectors, which "
                                "facilitate the degradation of the phage DNA"
                            ),
                            "notes": (
                                "Hu et al. support Type I ZorC/ZorD effectors "
                                "as phage-DNA-degradation outputs."
                            ),
                        }
                    ],
                },
                {
                    "subject": "zorya_effector_activity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "zorya_system_trait",
                    "description": (
                        "Zorya effector activity is the antiviral output that "
                        "realizes the Zorya system defense phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": MARIANO,
                            "snippet": (
                                "Our work reveals the molecular basis of the "
                                "activity of Zorya systems and highlights the "
                                "ZorE nickase as crucial for population-wide "
                                "immunity in the type II system"
                            ),
                            "notes": (
                                "Mariano et al. support ZorE nickase activity "
                                "as a Type II Zorya effector output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "zorya_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Zorya system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MARIANO,
                            "snippet": (
                                "The Zorya phage defense system was first "
                                "discovered in 2018"
                            ),
                            "notes": (
                                "Mariano et al. place Zorya in the "
                                "phage-defense-system family."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "zorya-subtype-effector-and-trigger-gap",
            "prompt": (
                "Resolve Zorya subtype effectors, ion usage, and phage "
                "triggers before minting narrower Zorya mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Hu et al. support Type I ZorAB activation and "
                "ZorC/ZorD-mediated phage-DNA degradation, and Mariano et "
                "al. support Type I/II ZorAB architecture plus a recruited "
                "Type II ZorE nickase, but Zorya variants need separate "
                "review before TraitMech asserts one universal ion "
                "substrate, effector composition, nuclease target, cell-death "
                "pathway, Type III mechanism, or anti-defense breadth."
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
            "Minted Zorya system as a DOI-backed GENOMICS TraitRecord under "
            "the phage defense system parent after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or prior "
            "proposal record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v94."
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
