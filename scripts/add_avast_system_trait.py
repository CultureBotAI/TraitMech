#!/usr/bin/env python3
"""Add the AVAST system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "avast_system.yaml"

GAO_2020 = "DOI:10.1126/science.aba0372"
GAO_2022 = "DOI:10.1126/science.abm4096"
MURALIDHARAN = "DOI:10.1016/j.molcel.2026.01.004"
CURATOR = "codex"
TIMESTAMP = "2026-09-18T10:44:12Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000239",
    "label": "AVAST system",
    "definition": (
        "A phage defense system in which an organism possesses a locus "
        "encoding a STAND-superfamily antiviral ATPase/NTPase that "
        "functions as a modular Avs receptor-effector, recognizes "
        "conserved bacteriophage proteins, and activates "
        "subtype-specific antiphage outputs to inhibit bacteriophage "
        "replication."
    ),
    "definition_source": GAO_2020,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": (
                "antiviral ATPase/NTPase of the STAND superfamily system"
            ),
            "synonym_type": "EXACT_SYNONYM",
            "source": GAO_2020,
        },
        {
            "synonym_text": "antiviral STAND system",
            "synonym_type": "EXACT_SYNONYM",
            "source": GAO_2020,
        },
    ],
    "evidence": [
        {
            "reference": GAO_2020,
            "snippet": (
                "AVAST, antiviral ATPase/NTPase of the STAND "
                "superfamily"
            ),
            "notes": (
                "Gao et al. coined AVAST as a recurring antiviral "
                "STAND ATPase/NTPase defense-system family in their "
                "pangenome-scale antiphage-system discovery screen."
            ),
        },
        {
            "reference": GAO_2022,
            "snippet": (
                "Avs1 to Avs3 recognize the large terminase subunit, "
                "and Avs4 recognizes the portal"
            ),
            "notes": (
                "Gao et al. characterized Avs1 through Avs4 as "
                "prokaryotic STAND-family innate immune receptors that "
                "detect conserved phage proteins and trigger "
                "subtype-specific antiviral effector outputs."
            ),
        },
        {
            "reference": MURALIDHARAN,
            "snippet": (
                "AVAST type 5 (Avs5) systems, part of the signal "
                "transduction ATPases of numerous domains (STAND) "
                "superfamily, confer conserved immunity against jumbo "
                "phages"
            ),
            "notes": (
                "Muralidharan et al. extend the named AVAST family with "
                "Avs5 systems that defend against nucleus-forming jumbo "
                "phages."
            ),
        },
        {
            "reference": MURALIDHARAN,
            "snippet": (
                "Recognition of phage infection triggers the Sir2-like "
                "effector domain of Avs5 across three Avs5 clades"
            ),
            "notes": (
                "Muralidharan et al. support a subtype-specific Avs5 "
                "effector activation mechanism downstream of phage "
                "infection sensing."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "note": (
                "Muralidharan et al. characterized the Pseudomonas "
                "aeruginosa Avs5-1 system and showed that its Sir2-like "
                "effector domain is activated during jumbo-phage "
                "infection."
            ),
            "reference": MURALIDHARAN,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "avast_stand_pattern_recognition_defense",
            "title": (
                "AVAST STAND receptors detect phage proteins during "
                "antiphage defense"
            ),
            "description": (
                "Evidence-backed process sketch linking an AVAST locus "
                "to Avs STAND receptor activation, subtype-specific "
                "antiviral effector activity, and inhibition of "
                "bacteriophage replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph stays at the AVAST-family level and does "
                "not assert that all Avs subtypes detect the same "
                "phage protein, carry the same nuclease or Sir2-like "
                "effector domain, act on the same molecular substrate, "
                "or inhibit the same class of phages."
            ),
            "nodes": [
                {
                    "node_id": "avast_locus",
                    "label": "AVAST locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus encoding a "
                        "STAND-superfamily antiviral ATPase/NTPase that "
                        "functions as a modular Avs receptor-effector."
                    ),
                },
                {
                    "node_id": "avs_stand_receptor_activation",
                    "label": "Avs STAND receptor activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of an Avs STAND-family receptor "
                        "after detection of a conserved phage protein "
                        "during bacteriophage infection."
                    ),
                },
                {
                    "node_id": "avast_effector_output",
                    "label": "AVAST antiviral effector output",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Subtype-specific nuclease, NADase, or "
                        "membrane-associated antiviral activity "
                        "triggered by an activated AVAST receptor."
                    ),
                },
                {
                    "node_id": "phage_replication",
                    "label": "phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Bacteriophage genome replication and "
                        "production inside an infected bacterial host."
                    ),
                },
                {
                    "node_id": "avast_system_trait",
                    "label": "AVAST system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000239",
                    "description": (
                        "Possession of a genome-encoded AVAST "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded "
                        "immune systems that inhibit bacteriophage "
                        "infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "avast_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "avs_stand_receptor_activation",
                    "description": (
                        "AVAST loci encode Avs STAND-family "
                        "receptors that are activated when their "
                        "cognate conserved phage protein is present."
                    ),
                    "evidence": [
                        {
                            "reference": GAO_2022,
                            "snippet": (
                                "Avs1 to Avs3 recognize the large "
                                "terminase subunit, and Avs4 recognizes "
                                "the portal"
                            ),
                            "notes": (
                                "Gao et al. support Avs1 through Avs4 "
                                "as phage-protein-sensing AVAST "
                                "receptors."
                            ),
                        },
                        {
                            "reference": MURALIDHARAN,
                            "snippet": (
                                "Avs5 localizes to early infection "
                                "vesicles, where it senses an essential, "
                                "early-expressed phage protein named "
                                "JADA"
                            ),
                            "notes": (
                                "Muralidharan et al. support "
                                "phage-infection recognition by Avs5 "
                                "receptors."
                            ),
                        },
                    ],
                },
                {
                    "subject": "avs_stand_receptor_activation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "avast_effector_output",
                    "description": (
                        "Detection of a phage cue activates the "
                        "effector domain coupled to the cognate Avs "
                        "STAND receptor."
                    ),
                    "evidence": [
                        {
                            "reference": MURALIDHARAN,
                            "snippet": (
                                "Recognition of phage infection "
                                "triggers the Sir2-like effector domain "
                                "of Avs5 across three Avs5 clades"
                            ),
                            "notes": (
                                "Muralidharan et al. connect phage "
                                "recognition to subtype-specific Avs5 "
                                "Sir2-like effector activation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "avast_effector_output",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "Subtype-specific AVAST effector activities "
                        "restrict bacteriophage replication or "
                        "propagation after recognition of a phage cue."
                    ),
                    "evidence": [
                        {
                            "reference": GAO_2022,
                            "snippet": (
                                "In all four cases, target recognition "
                                "led to Avs protein activation and "
                                "antiviral activity"
                            ),
                            "notes": (
                                "Gao et al. support Avs effector "
                                "outputs as downstream antiviral "
                                "activities in Avs1 through Avs4 "
                                "systems."
                            ),
                        },
                        {
                            "reference": MURALIDHARAN,
                            "snippet": (
                                "Upon sensing Jumbo J phage, Avs5-1 "
                                "underwent oligomerization, which "
                                "activated the enzymatic activity of "
                                "its Sir2 effector, resulting in rapid "
                                "NAD + hydrolysis, disruption of phage "
                                "nucleus formation, and arrest of "
                                "infection"
                            ),
                            "notes": (
                                "Muralidharan et al. support Avs5 "
                                "Sir2-like effector activity as a "
                                "jumbo-phage-restricting AVAST output."
                            ),
                        },
                    ],
                },
                {
                    "subject": "avast_effector_output",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "avast_system_trait",
                    "description": (
                        "Activated AVAST effector outputs realize the "
                        "AVAST phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MURALIDHARAN,
                            "snippet": (
                                "AVAST type 5 (Avs5) systems, part of "
                                "the signal transduction ATPases of "
                                "numerous domains (STAND) superfamily, "
                                "confer conserved immunity against "
                                "jumbo phages"
                            ),
                            "notes": (
                                "Muralidharan et al. connect a "
                                "characterized AVAST subtype to "
                                "conserved antiphage immunity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "avast_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "AVAST system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": GAO_2020,
                            "snippet": (
                                "AVAST, antiviral ATPase/NTPase of the "
                                "STAND superfamily"
                            ),
                            "notes": (
                                "Gao et al. identified AVAST among "
                                "candidate phage-defense systems."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "avast-subtype-effector-gap",
            "prompt": (
                "Resolve AVAST subtype sensors, phage triggers, and "
                "effector outputs before minting narrower Avs1-Avs5 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support phage-protein pattern recognition "
                "by Avs1 through Avs4, while Muralidharan et al. "
                "support Avs5 immunity against nucleus-forming jumbo "
                "phages through phage-triggered Sir2-like effector "
                "activation. The first TraitRecord therefore stays at "
                "the AVAST-system level until separate review resolves "
                "which phage cues, effector domains, and antiviral "
                "substrates generalize across AVAST loci."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-18",
        }
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
            "Minted AVAST system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the "
            "replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v116."
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
