#!/usr/bin/env python3
"""Add the Dsr system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dsr_system.yaml"

GAO = "DOI:10.1126/science.aba0372"
GARB = "DOI:10.1038/s41564-022-01207-8"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-19T13:00:46Z"

PROFILE_I = "Dsr_I__Dsr1"
PROFILE_II = "Dsr_II__Dsr2"

DSR_I_RULES_SNIPPET = "Dsr\tDsr_I\t1\t1\tDsr_I__Dsr1"
DSR_II_RULES_SNIPPET = "Dsr\tDsr_II\t1\t1\tDsr_II__Dsr2"


def hmm_inventory_evidence(profile: str, subtype: str, component: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{profile:<48} | {profile:<48} | {subtype}",
        "notes": (
            f"The DefenseFinder HMM inventory records the {component} profile in "
            f"the {subtype} model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000280",
    "label": "Dsr system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "defense-associated sirtuin locus whose SIR2-domain effector can "
        "deplete NAD+ during bacteriophage defense and is modeled by "
        "DefenseFinder as Dsr subtypes."
    ),
    "definition_source": GARB,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Dsr",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "defense-associated sirtuin",
            "synonym_type": "RELATED_SYNONYM",
            "source": GAO,
        },
    ],
    "evidence": [
        {
            "reference": GAO,
            "snippet": (
                "we selected 48 candidate systems to test experimentally "
                "for defense activity"
            ),
            "notes": (
                "Gao et al. used heterologous reconstitution and phage "
                "challenge as their experimental screen for "
                "computationally predicted antiphage systems."
            ),
        },
        {
            "reference": GAO,
            "snippet": "dsr, defense-associated sirtuin",
            "notes": (
                "Gao et al. introduced dsr as a defense-associated "
                "sirtuin name in the candidate-system activity figure."
            ),
        },
        {
            "reference": GAO,
            "snippet": (
                "Additional systems include proteins containing a SIR2 "
                "(sirtuin) deacetylase domain"
            ),
            "notes": (
                "Gao et al. place SIR2-domain proteins among additional "
                "antiphage defense-system candidates in their "
                "domain-architecture analysis."
            ),
        },
        {
            "reference": GARB,
            "snippet": (
                "DSR proteins degrade nicotinamide adenine dinucleotide "
                "(NAD+) during infection, depleting the cell of this "
                "essential molecule and aborting phage propagation"
            ),
            "notes": (
                "Garb et al. showed that DSR SIR2-domain proteins can "
                "defend through infection-coupled NAD+ depletion."
            ),
        },
        {
            "reference": GARB,
            "snippet": (
                "DSR2, directly identifies phage tail tube proteins and "
                "then becomes an active NADase in Bacillus subtilis"
            ),
            "notes": (
                "Garb et al. experimentally resolved the phage-derived "
                "activation cue for one Bacillus subtilis DSR2 system."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Dsr | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
                "activities mediate antiviral immunity in prokaryotes"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named Dsr "
                "system to the Gao et al. antiphage-system discovery "
                "paper."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": DSR_I_RULES_SNIPPET,
            "notes": (
                "The DefenseFinder rules table models Dsr_I as a "
                "single-profile Dsr subtype."
            ),
        },
        hmm_inventory_evidence(PROFILE_I, "Dsr_I", "Dsr1"),
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": DSR_II_RULES_SNIPPET,
            "notes": (
                "The DefenseFinder rules table models Dsr_II as a "
                "single-profile Dsr subtype."
            ),
        },
        hmm_inventory_evidence(PROFILE_II, "Dsr_II", "Dsr2"),
    ],
    "causal_graphs": [
        {
            "graph_id": "dsr_sirtuin_antiphage_defense",
            "title": "Dsr loci encode SIR2-domain antiphage proteins",
            "description": (
                "Conservative system-level sketch linking a Dsr locus to "
                "SIR2-domain NAD+ depletion, subtype-specific "
                "bacteriophage resistance, and the Dsr system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Dsr systems at the family level while "
                "leaving DefenseFinder Dsr_I/Dsr_II profile boundaries, "
                "subtype-specific triggers outside DSR2, host ranges, "
                "anti-defense proteins, and exact phage targets unresolved. "
                "This Dsr family is distinct from metabolic dissimilatory "
                "sulfite reductase DsrAB systems."
            ),
            "nodes": [
                {
                    "node_id": "dsr_locus",
                    "label": "Dsr locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A defense-associated sirtuin antiphage locus "
                        "represented by Dsr subtype profiles."
                    ),
                },
                {
                    "node_id": "sir2_domain_antiphage_activity",
                    "label": "SIR2-domain antiphage activity",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "NADase-associated molecular activity carried by a "
                        "Dsr SIR2-domain antiphage protein."
                    ),
                },
                {
                    "node_id": "subtype_specific_phage_resistance",
                    "label": "subtype-specific phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against particular bacteriophages by "
                        "a Dsr subtype."
                    ),
                },
                {
                    "node_id": "dsr_system_trait",
                    "label": "Dsr system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000280",
                    "description": (
                        "Possession of a genome-encoded "
                        "defense-associated sirtuin phage defense system."
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
                    "subject": "dsr_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "sir2_domain_antiphage_activity",
                    "description": (
                        "Dsr loci encode SIR2-domain defense-associated "
                        "sirtuin proteins."
                    ),
                    "evidence": [
                        {
                            "reference": GAO,
                            "snippet": "dsr, defense-associated sirtuin",
                            "notes": (
                                "Gao et al. connect the Dsr name to a "
                                "defense-associated sirtuin candidate."
                            ),
                        },
                        {
                            **hmm_inventory_evidence(PROFILE_I, "Dsr_I", "Dsr1"),
                            "notes": (
                                "DefenseFinder includes Dsr1 in the Dsr_I "
                                "custom model profile inventory."
                            ),
                        },
                    ],
                },
                {
                    "subject": "sir2_domain_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "subtype_specific_phage_resistance",
                    "description": (
                        "Garb et al. showed that DSR SIR2-domain effectors "
                        "can degrade NAD+ during infection and abort phage "
                        "propagation."
                    ),
                    "evidence": [
                        {
                            "reference": GARB,
                            "snippet": (
                                "DSR proteins degrade nicotinamide adenine "
                                "dinucleotide (NAD+) during infection, "
                                "depleting the cell of this essential "
                                "molecule and aborting phage propagation"
                            ),
                            "notes": (
                                "DSR SIR2-domain activity can deplete NAD+ "
                                "during infection in an abortive phage "
                                "defense outcome."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dsr_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "subtype_specific_phage_resistance",
                    "description": (
                        "Garb et al. support DSR NAD+ depletion as an "
                        "abortive phage-defense outcome, while "
                        "DefenseFinder models Dsr_I and Dsr_II as named "
                        "Dsr subtypes."
                    ),
                    "evidence": [
                        {
                            "reference": GARB,
                            "snippet": (
                                "DSR proteins degrade nicotinamide adenine "
                                "dinucleotide (NAD+) during infection, "
                                "depleting the cell of this essential "
                                "molecule and aborting phage propagation"
                            ),
                            "notes": (
                                "Garb et al. directly support "
                                "infection-coupled DSR NAD+ depletion as an "
                                "abortive antiphage output."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": DSR_I_RULES_SNIPPET,
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "Dsr_I as a named defense-system subtype "
                                "model with a Dsr1 profile."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": DSR_II_RULES_SNIPPET,
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "Dsr_II as a named defense-system subtype "
                                "model with a Dsr2 profile."
                            ),
                        },
                    ],
                },
                {
                    "subject": "subtype_specific_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "dsr_system_trait",
                    "description": (
                        "DefenseFinder represents Dsr as Dsr_I and Dsr_II "
                        "subtypes within its Dsr system models."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": DSR_I_RULES_SNIPPET,
                            "notes": (
                                "The Dsr_I rule links the Dsr system "
                                "namespace to the Dsr_I subtype and Dsr1 "
                                "profile."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": DSR_II_RULES_SNIPPET,
                            "notes": (
                                "The Dsr_II rule links the Dsr system "
                                "namespace to the Dsr_II subtype and Dsr2 "
                                "profile."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dsr_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Dsr system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Dsr | 10\\.1126/science\\.aba0372 | "
                                "Diverse enzymatic activities mediate "
                                "antiviral immunity in prokaryotes"
                            ),
                            "notes": (
                                "DefenseFinder associates Dsr with the "
                                "Gao et al. prokaryotic antiviral-immunity "
                                "paper."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "dsr-sirtuin-mechanism-gap",
            "prompt": (
                "Map DefenseFinder Dsr_I and Dsr_II profiles onto "
                "experimentally resolved DSR1 and DSR2 NADase triggers, "
                "host ranges, anti-defense proteins, and Dsr naming "
                "collisions before minting narrower Dsr mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support defense-associated sirtuin proteins "
                "as antiphage system components, Garb et al. resolved "
                "NAD+ depletion for multiple SIR2-dependent defense "
                "systems and tail tube-triggered NADase activation for "
                "B. subtilis DSR2, and DefenseFinder models Dsr_I and "
                "Dsr_II. This first record stays at Dsr-family level "
                "until the DefenseFinder subtype profiles can be aligned "
                "to specific experimental DSR1/DSR2 systems, trigger "
                "proteins, host ranges, and phage-encoded anti-DSR "
                "proteins. The DefenseFinder Dsr system is also lexically "
                "distinct from metabolic DsrAB dissimilatory sulfite "
                "reductase systems."
            ),
            "attaches_to": ["causal_graphs#dsr_sirtuin_antiphage_defense"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-19",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Dsr system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact phage-defense Dsr "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v157."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
