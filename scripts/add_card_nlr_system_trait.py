#!/usr/bin/env python3
"""Add the CARD-NLR system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "card_nlr_system.yaml"

WEIN = "DOI:10.1101/2023.05.28.542683"
WEIN_EPMC = "https://europepmc.org/article/PPR/PPR668921"

CARD_DEFENSE_SNIPPET = (
    "Here we show that CARD-like domains are present in defense systems "
    "that protect bacteria against phage."
)
BGSDM_CARD_SNIPPET = (
    "The bacterial CARD is essential for protease-mediated activation of "
    "certain bacterial gasdermins, which promote cell death once phage "
    "infection is recognized."
)
CARD_EFFECTOR_SNIPPET = (
    "We further show that multiple anti-phage defense systems utilize "
    "CARD-like domains to activate a variety of cell death effectors."
)
CARD_TRIGGER_SNIPPET = (
    "We find that these systems are triggered by a conserved immune evasion "
    "protein that phages use to overcome the bacterial defense system RexAB, "
    "demonstrating that phage proteins inhibiting one defense system can "
    "activate another."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

ARTICLE_ROW = (
    "CARD_NLR | 10\\.1101/2023\\.05\\.28\\.542683 | CARD-like domains "
    "mediate anti-phage defense in bacterial gasdermin systems"
)
CARD_PROTEASE_HMM_ROW = (
    "| CARD_NLR__CARD_Protease                          | "
    "CARD_NLR__CARD_Protease                          | CARD_NLR               | "
    "Custom                  | 300    |"
)
NLR_HMM_ROW = (
    "| CARD_NLR__NLR_new                                | "
    "CARD_NLR__NLR_new                                | CARD_NLR               | "
    "Custom                  | 100    |"
)
PHOSPHO_HMM_ROW = (
    "| CARD_NLR__Trypsin_Phospho                        | "
    "CARD_NLR__Trypsin_Phospho                        | CARD_NLR               | "
    "Custom                  | 400    |"
)
ENDONUCLEASE_RULE_ROW = (
    "CARD_NLR\tCARD_NLR_Endonuclease\t1\t3\t"
    "CARD_NLR__Endonuclease\tCARD_NLR__CARD_Protease, "
    "CARD_NLR__NLR_new, CARD_NLR__Trypsin\tCARD_NLR__Phospho, "
    "CARD_NLR__Phospho_Trypsin, CARD_NLR__Subtilase, "
    "CARD_NLR__Subtilase_long_new, CARD_NLR__Subtilase_small_new, "
    "CARD_NLR__Trypsin_Phospho, GasderMIN__bGSDM\t"
)
GASDERMIN_RULE_ROW = (
    "CARD_NLR\tCARD_NLR_GasderMIN\t1\t3\tGasderMIN__bGSDM\t"
    "CARD_NLR__CARD_Protease, CARD_NLR__NLR_new, CARD_NLR__Trypsin\t"
    "CARD_NLR__Endonuclease, CARD_NLR__Endonuclease_new, "
    "CARD_NLR__Phospho, CARD_NLR__Phospho_Trypsin, "
    "CARD_NLR__Subtilase, CARD_NLR__Subtilase_long_new, "
    "CARD_NLR__Subtilase_small_new, CARD_NLR__Trypsin_Phospho, "
    "CARD_NLR__Trypsine_Endonuclease_new\t"
)
PHOSPHO_RULE_ROW = (
    "CARD_NLR\tCARD_NLR_Phospho\t1\t3\t"
    "CARD_NLR__Trypsin_Phospho\tCARD_NLR__CARD_Protease, "
    "CARD_NLR__NLR_new, CARD_NLR__Trypsin\tCARD_NLR__Endonuclease, "
    "CARD_NLR__Endonuclease_new, CARD_NLR__Subtilase, "
    "CARD_NLR__Subtilase_long_new, CARD_NLR__Subtilase_small_new, "
    "CARD_NLR__Trypsine_Endonuclease_new, GasderMIN__bGSDM\t"
)
SUBTILASE_RULE_ROW = (
    "CARD_NLR\tCARD_NLR_Subtilase\t1\t3\t"
    "CARD_NLR__Subtilase_long_new\tCARD_NLR__CARD_Protease, "
    "CARD_NLR__NLR_new, CARD_NLR__Trypsin\tCARD_NLR__Endonuclease, "
    "CARD_NLR__Endonuclease_new, CARD_NLR__Phospho, "
    "CARD_NLR__Phospho_Trypsin, CARD_NLR__Trypsin_Phospho, "
    "CARD_NLR__Trypsine_Endonuclease_new, GasderMIN__bGSDM\t"
)
LIKE_RULE_ROW = (
    "CARD_NLR\tCARD_NLR_like\t2\t4\tCARD_NLR__Endonuclease, "
    "CARD_NLR__Phospho_Trypsin, CARD_NLR__Subtilase_long_new, "
    "CARD_NLR__Trypsin_Phospho\tCARD_NLR__CARD_Protease, "
    "CARD_NLR__NLR_new, CARD_NLR__Trypsin\t\t"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T13:47:08Z"

IDENTIFIER = "traitmech:000337"
PROPOSAL = "proposals/metpo_traitmech_v214"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The DefenseFinder article registry maps the CARD_NLR model "
            "namespace to the Wein et al. bacterial CARD-like domain "
            "anti-phage defense preprint."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": CARD_PROTEASE_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records a CARD-like protease "
            "profile under the CARD_NLR model namespace."
        ),
    }


def nlr_hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": NLR_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records an NLR profile under "
            "the CARD_NLR model namespace."
        ),
    }


def phospho_hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": PHOSPHO_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records a "
            "Trypsin_Phospho-profiled effector under the CARD_NLR model "
            "namespace."
        ),
    }


def endonuclease_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": ENDONUCLEASE_RULE_ROW,
        "notes": (
            "The DefenseFinder rules table models a CARD_NLR endonuclease "
            "subtype with CARD-like and NLR-like accessory profiles."
        ),
    }


def gasdermin_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": GASDERMIN_RULE_ROW,
        "notes": (
            "The DefenseFinder rules table models a CARD_NLR_GasderMIN "
            "subtype with GasderMIN__bGSDM as its mandatory effector "
            "profile."
        ),
    }


def phospho_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": PHOSPHO_RULE_ROW,
        "notes": (
            "The DefenseFinder rules table models a CARD_NLR_Phospho "
            "subtype with CARD-like and NLR-like accessory profiles."
        ),
    }


def subtilase_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": SUBTILASE_RULE_ROW,
        "notes": (
            "The DefenseFinder rules table models a CARD_NLR subtilase "
            "subtype with CARD-like and NLR-like accessory profiles."
        ),
    }


def like_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": LIKE_RULE_ROW,
        "notes": (
            "The DefenseFinder rules table also models a CARD_NLR_like "
            "subtype that requires two of several candidate effector "
            "profiles."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "CARD-NLR system",
    "definition": (
        "A phage defense system in which an organism possesses a CARD-NLR "
        "locus represented by the DefenseFinder CARD_NLR model namespace, "
        "coupling bacterial CARD-like detector components and NLR-like "
        "profiles to subtype-specific GasderMIN, endonuclease, "
        "Trypsin_Phospho, or Subtilase effector profiles that can promote "
        "cell death after phage recognition."
    ),
    "definition_source": WEIN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "CARD_NLR",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "CARD_NLR__CARD_Protease",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "CARD_NLR__NLR_new",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": WEIN_EPMC,
            "snippet": CARD_DEFENSE_SNIPPET,
            "notes": (
                "The Wein et al. abstract supports CARD-like-domain "
                "systems as bacterial phage-defense systems."
            ),
        },
        {
            "reference": WEIN_EPMC,
            "snippet": BGSDM_CARD_SNIPPET,
            "notes": (
                "The Wein et al. abstract supports bacterial CARD-mediated "
                "protease activation of some bacterial gasdermins after "
                "phage recognition."
            ),
        },
        {
            "reference": WEIN_EPMC,
            "snippet": CARD_EFFECTOR_SNIPPET,
            "notes": (
                "The Wein et al. abstract states that multiple anti-phage "
                "systems use CARD-like domains to activate varied "
                "cell-death effectors."
            ),
        },
        {
            "reference": WEIN_EPMC,
            "snippet": CARD_TRIGGER_SNIPPET,
            "notes": (
                "The Wein et al. abstract reports that these systems can be "
                "triggered by a phage immune-evasion protein."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
        nlr_hmm_inventory_evidence(),
        phospho_hmm_inventory_evidence(),
        endonuclease_rules_evidence(),
        gasdermin_rules_evidence(),
        phospho_rules_evidence(),
        subtilase_rules_evidence(),
        like_rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "card_nlr_loci_activate_cell_death_effectors",
            "title": "CARD-NLR loci activate antiphage cell-death effectors",
            "description": (
                "System-level sketch linking a CARD-NLR locus to "
                "CARD-like detector activation, subtype-specific "
                "cell-death effector activation, and the CARD-NLR "
                "system trait without asserting the molecular mechanism of "
                "any one DefenseFinder subtype."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures CARD-NLR as a named DefenseFinder "
                "model namespace supported by Wein et al. CARD-like domain "
                "anti-phage defense evidence while leaving subtype-specific "
                "phage triggers, the effector activation sequence, "
                "GasderMIN-associated subtype boundaries, and "
                "endonuclease, Trypsin_Phospho, or Subtilase outputs "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "card_nlr_locus",
                    "label": "CARD-NLR locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A bacterial anti-phage defense locus cataloged in "
                        "DefenseFinder with CARD_NLR profiles."
                    ),
                },
                {
                    "node_id": "card_like_detector_activation",
                    "label": "CARD-like detector activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of a bacterial CARD-like detector "
                        "within a CARD-NLR system."
                    ),
                },
                {
                    "node_id": "cell_death_effector_activation",
                    "label": "cell-death effector activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of a gasdermin or other "
                        "subtype-specific cell-death effector by a "
                        "CARD-like anti-phage defense system."
                    ),
                },
                {
                    "node_id": "phage_triggered_cell_death",
                    "label": "phage-triggered cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Host cell death promoted by a CARD-like "
                        "bacterial anti-phage defense system."
                    ),
                },
                {
                    "node_id": "card_nlr_system_trait",
                    "label": "CARD-NLR system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded CARD-NLR "
                        "phage-defense system."
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
                    "subject": "card_nlr_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "card_like_detector_activation",
                    "description": (
                        "CARD-NLR loci couple CARD-like and NLR-like "
                        "DefenseFinder profiles to subtype-specific "
                        "effector profiles."
                    ),
                    "evidence": [
                        {
                            "reference": WEIN_EPMC,
                            "snippet": CARD_DEFENSE_SNIPPET,
                            "notes": (
                                "Wein et al. support bacterial CARD-like "
                                "domains as parts of anti-phage defense "
                                "systems."
                            ),
                        },
                        hmm_inventory_evidence(),
                        nlr_hmm_inventory_evidence(),
                        endonuclease_rules_evidence(),
                    ],
                },
                {
                    "subject": "card_like_detector_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "cell_death_effector_activation",
                    "description": (
                        "Bacterial CARD-like domains activate "
                        "subtype-specific cell-death effectors."
                    ),
                    "evidence": [
                        {
                            "reference": WEIN_EPMC,
                            "snippet": CARD_EFFECTOR_SNIPPET,
                            "notes": (
                                "Wein et al. report multiple "
                                "CARD-like-domain anti-phage systems that "
                                "activate cell-death effectors."
                            ),
                        },
                        gasdermin_rules_evidence(),
                        phospho_rules_evidence(),
                        subtilase_rules_evidence(),
                    ],
                },
                {
                    "subject": "cell_death_effector_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_triggered_cell_death",
                    "description": (
                        "Activated gasdermin and non-gasdermin CARD-NLR "
                        "effectors can promote defense-associated cell "
                        "death."
                    ),
                    "evidence": [
                        {
                            "reference": WEIN_EPMC,
                            "snippet": BGSDM_CARD_SNIPPET,
                            "notes": (
                                "Wein et al. support CARD-dependent "
                                "gasdermin activation and cell death after "
                                "phage recognition."
                            ),
                        },
                        {
                            "reference": WEIN_EPMC,
                            "snippet": CARD_EFFECTOR_SNIPPET,
                            "notes": (
                                "Wein et al. generalize CARD-like-domain "
                                "activation to multiple cell-death effector "
                                "classes."
                            ),
                        },
                    ],
                },
                {
                    "subject": "phage_triggered_cell_death",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "card_nlr_system_trait",
                    "description": (
                        "CARD-like effector-associated cell death realizes "
                        "the CARD-NLR phage-defense-system output."
                    ),
                    "evidence": [
                        {
                            "reference": WEIN_EPMC,
                            "snippet": CARD_TRIGGER_SNIPPET,
                            "notes": (
                                "Wein et al. support CARD-like-domain "
                                "system triggering by a bacteriophage "
                                "immune-evasion protein."
                            ),
                        },
                        like_rules_evidence(),
                    ],
                },
                {
                    "subject": "card_nlr_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "CARD-NLR system possession is a phage-defense "
                        "system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        endonuclease_rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "card-nlr-subtype-mechanism-gap",
            "prompt": (
                "Resolve CARD-NLR subtype effectors, phage triggers, "
                "natural-host examples, and GasderMIN subtype boundaries "
                "before minting narrower CARD-NLR mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wein et al. support CARD-like domains in multiple "
                "anti-phage defense systems that activate cell-death "
                "effectors, and DefenseFinder models CARD_NLR subtypes "
                "with gasdermin, endonuclease, CARD_NLR_Phospho, and Subtilase "
                "effector profiles. This first system-level record leaves "
                "the exact phage triggers, CARD-to-effector activation "
                "sequence, accession-level natural-host components, and "
                "boundaries between standalone GasderMIN and "
                "CARD_NLR_GasderMIN contexts unresolved."
            ),
            "attaches_to": [
                "causal_graphs#card_nlr_loci_activate_cell_death_effectors"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}"
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted CARD-NLR system as a DOI- and stable-URL-backed "
            "GENOMICS TraitRecord under the phage defense system parent "
            "after an ignored-and-hidden duplicate review found no exact "
            "live TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
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
