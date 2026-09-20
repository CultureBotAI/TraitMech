#!/usr/bin/env python3
"""Add the BstA system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "bsta_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

OWEN = "DOI:10.1016/j.chom.2021.09.002"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T04:37:48Z"
PARENT_TIMESTAMP = "2026-09-20T04:37:49Z"
REVIEW_TIMESTAMP = "2026-09-20T05:13:00Z"
REVIEW_FOLLOWUP_TIMESTAMP = "2026-09-20T05:25:30Z"

IDENTIFIER = "traitmech:000301"
PROPOSAL = "proposals/metpo_traitmech_v178"
SYSTEM = "BstA"
SLUG = "bsta"
PROFILE = "BstA__BstA"
RULES_SNIPPET = "BstA\tBstA\t1\t1\tBstA__BstA"

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, and AbiV are split out as "
    "traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, and "
    "traitmech:000300, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "and Haaber et al. still support Abi as a genomically encoded phage "
    "defense strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape "
    "routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, and BstA are split out "
    "as traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, and traitmech:000301, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang "
    "et al., Bouchard et al., Haaber et al., and Owen et al. still "
    "support Abi as a genomically encoded phage defense strategy that "
    "spans mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, and other Abi "
    "families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "BstA | 10\\.1101/2020\\.07\\.13\\.199331 | "
            "Prophage-encoded phage defense proteins with cognate "
            "self-immunity"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named BstA "
            "system to the Owen et al. BstA preprint."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{PROFILE:<48} | {PROFILE:<48} | {SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records a BstA profile for "
            "BstA__BstA in the BstA model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models BstA as a one-component "
            "system requiring the BstA__BstA profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "BstA system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "BstA-family phage-defense locus whose encoded BstA protein can "
        "suppress lytic phage DNA replication and whose cognate anti-BstA "
        "aba element can self-immunize the encoding prophage from BstA "
        "activity."
    ),
    "definition_source": OWEN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "BstA",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": OWEN,
            "snippet": (
                "we identify BstA, a family of prophage-encoded "
                "phage-defense proteins in diverse Gram-negative bacteria"
            ),
            "notes": (
                "Owen et al. name BstA as a family of prophage-encoded "
                "phage-defense proteins."
            ),
        },
        {
            "reference": OWEN,
            "snippet": (
                "the BstA protein confers effective population-level "
                "defense against exogenous phage infection via abortive "
                "infection"
            ),
            "notes": (
                "Owen et al. support BstA as an abortive-infection "
                "phage-defense system."
            ),
        },
        {
            "reference": OWEN,
            "snippet": (
                "demonstrating that the BstA protein mediates defense "
                "against phage P22"
            ),
            "notes": (
                "Owen et al. show that phage resistance against P22 is "
                "BstA-protein dependent."
            ),
        },
        {
            "reference": OWEN,
            "snippet": (
                "BstA provides phage defense at the population level and "
                "prevents the spread of phage epidemics"
            ),
            "notes": (
                "Owen et al. connect BstA activity to suppression of phage "
                "epidemics at population level."
            ),
        },
        {
            "reference": OWEN,
            "snippet": (
                "phage DNA replication is strongly suppressed by BstA, but "
                "replication can be rescued by the aba element"
            ),
            "notes": (
                "Owen et al. support the direct phage-DNA-replication "
                "output of BstA and suppression by the cognate aba "
                "self-immunity element."
            ),
        },
        {
            "reference": OWEN,
            "snippet": (
                "each bstA locus contains a cognate aba element that is "
                "inactive against variant BstA proteins"
            ),
            "notes": (
                "Owen et al. show that aba self-immunity is cognate to its "
                "co-encoded BstA variant."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
        rules_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:568708",
            "taxon_label": (
                "Salmonella enterica subsp. enterica serovar "
                "Typhimurium str. D23580"
            ),
            "note": (
                "Owen et al. studied BstA in the BTP1 prophage of "
                "Salmonella enterica serovar Typhimurium ST313 strain "
                "D23580 and showed that BstA mediates defense against "
                "Salmonella phage P22."
            ),
            "reference": OWEN,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "bsta_locus_suppresses_phage_dna_replication",
            "title": (
                "BstA loci suppress lytic phage DNA replication through "
                "abortive infection"
            ),
            "description": (
                "Conservative system-level sketch linking possession of a "
                "BstA phage-defense locus to suppressed lytic phage DNA "
                "replication, cognate aba-mediated self-immunity, and the "
                "BstA system trait without asserting the unresolved direct "
                "phage trigger, BstA molecular target, or mechanism of "
                "aba-mediated self-immunity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures BstA as a named abortive-infection "
                "system with a DefenseFinder BstA profile while leaving "
                "the direct trigger of BstA localization, the direct DNA "
                "replication target, the physical form of the BstA-aba "
                "interaction, and the molecular basis for cognate aba "
                "specificity unresolved."
            ),
            "nodes": [
                {
                    "node_id": "bsta_locus",
                    "label": "BstA locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A BstA-family phage-defense locus carrying a "
                        "BstA coding sequence."
                    ),
                },
                {
                    "node_id": "aba_element",
                    "label": "aba self-immunity element",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A cognate anti-BstA aba element carried alongside "
                        "BstA in a BstA-encoding prophage."
                    ),
                },
                {
                    "node_id": "suppressed_encoding_prophage_dna_replication",
                    "label": "suppressed encoding-prophage DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "BstA-mediated suppression of DNA replication by the "
                        "BstA-encoding prophage in an aba-sensitive context."
                    ),
                },
                {
                    "node_id": "suppressed_lytic_phage_dna_replication",
                    "label": "suppressed lytic phage DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Strong suppression of infecting lytic-phage DNA "
                        "replication by BstA activity."
                    ),
                },
                {
                    "node_id": "bsta_system_trait",
                    "label": "BstA system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded BstA "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a bacteriophage abortive-infection "
                        "defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "bsta_locus",
                    "predicate": "includes",
                    "predicate_id": "biolink:has_part",
                    "object": "aba_element",
                    "description": (
                        "BstA loci contain a cognate anti-BstA aba "
                        "self-immunity element."
                    ),
                    "evidence": [
                        {
                            "reference": OWEN,
                            "snippet": (
                                "each bstA locus contains a cognate aba "
                                "element that is inactive against variant "
                                "BstA proteins"
                            ),
                            "notes": (
                                "Owen et al. show that BstA loci carry "
                                "cognate aba elements."
                            ),
                        }
                    ],
                },
                {
                    "subject": "bsta_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "suppressed_lytic_phage_dna_replication",
                    "description": (
                        "Owen et al. show that BstA can strongly suppress "
                        "lytic phage DNA replication, and DefenseFinder "
                        "catalogs a one-component BstA model."
                    ),
                    "evidence": [
                        {
                            "reference": OWEN,
                            "snippet": (
                                "phage DNA replication is strongly "
                                "suppressed by BstA"
                            ),
                            "notes": (
                                "Owen et al. link BstA to strong "
                                "suppression of phage DNA replication."
                            ),
                        },
                        hmm_inventory_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "aba_element",
                    "predicate": "prevents",
                    "predicate_id": "RO:0002212",
                    "object": "suppressed_encoding_prophage_dna_replication",
                    "description": (
                        "Owen et al. show that the cognate anti-BstA aba "
                        "element rescues its encoding prophage's DNA "
                        "replication from BstA-mediated suppression."
                    ),
                    "evidence": [
                        {
                            "reference": OWEN,
                            "snippet": (
                                "phage DNA replication is strongly suppressed "
                                "by BstA, but replication can be rescued by "
                                "the aba element"
                            ),
                            "notes": (
                                "Owen et al. show that aba counteracts "
                                "BstA-mediated suppression of phage DNA "
                                "replication."
                            ),
                        },
                        {
                            "reference": OWEN,
                            "snippet": (
                                "each bstA locus contains a cognate aba "
                                "element that is inactive against variant "
                                "BstA proteins"
                            ),
                            "notes": (
                                "Owen et al. show that aba self-immunity is "
                                "specific to its cognate co-encoded BstA "
                                "variant."
                            ),
                        },
                    ],
                },
                {
                    "subject": "suppressed_lytic_phage_dna_replication",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "bsta_system_trait",
                    "description": (
                        "BstA-mediated suppression of lytic-phage DNA "
                        "replication realizes BstA-system "
                        "abortive-infection defense."
                    ),
                    "evidence": [
                        {
                            "reference": OWEN,
                            "snippet": (
                                "We propose that BstA protein mediates "
                                "abortive infection by suppressing phage "
                                "DNA replication"
                            ),
                            "notes": (
                                "Owen et al. propose phage-DNA-replication "
                                "suppression as the mechanism by which "
                                "BstA mediates abortive infection."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "bsta_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system",
                    "description": (
                        "BstA system possession is an abortive-infection "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": OWEN,
                            "snippet": (
                                "we propose that BstA is an abortive "
                                "infection system"
                            ),
                            "notes": (
                                "Owen et al. classify BstA as an "
                                "abortive-infection system."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "bsta-mechanism-gap",
            "prompt": (
                "Resolve the direct phage trigger of BstA localization, "
                "the direct DNA-replication target, the physical "
                "BstA-aba interaction, and the basis of cognate aba "
                "specificity before minting narrower BstA-aba mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Owen et al. and DefenseFinder support BstA as a named "
                "abortive-infection system with a BstA HMM profile and a "
                "cognate aba self-immunity element, but the direct phage "
                "trigger that recruits BstA to phage DNA, the precise "
                "target by which BstA suppresses lytic phage DNA "
                "replication, the physical interaction between aba DNA and "
                "BstA, and the molecular basis of BstA-aba specificity "
                "remain unresolved."
            ),
            "attaches_to": ["causal_graphs#bsta_locus_suppresses_phage_dna_replication"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
        }
    ],
}


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted BstA system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_PR_REVIEW",
        changes=(
            "Added a Salmonella enterica serovar Typhimurium D23580 "
            "canonical example and represented the anti-BstA aba element "
            "as an explicit graph node with a supported rescue edge after "
            "the PR 1111 adversarial review filed issues 1112 and 1113."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_PR_REVIEW",
        changes=(
            "Separated aba self-immunity for the BstA-encoding prophage "
            "from BstA-mediated suppression of incoming lytic phage DNA "
            "replication after the PR 1111 adversarial review filed issue "
            "1114."
        ),
        llm_assisted=True,
        timestamp=REVIEW_FOLLOWUP_TIMESTAMP,
    )
    return record


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def update_abortive_parent(record: dict[str, Any]) -> dict[str, Any]:
    record = copy.deepcopy(record)
    [discussion] = [
        discussion
        for discussion in record["discussions"]
        if discussion["discussion_id"] == "abortive-infection-subfamily-split-gap"
    ]
    assert discussion["status"] == "OPEN"
    if discussion["rationale"] == NEW_PARENT_RATIONALE:
        return record
    assert discussion["rationale"] == OLD_PARENT_RATIONALE
    discussion["rationale"] = NEW_PARENT_RATIONALE
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=(
            "Documented BstA as split out in the open "
            "abortive-infection subfamily split-gap discussion after "
            f"minting {IDENTIFIER} for the BstA system; other "
            "abortive-infection families remain open."
        ),
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / ABORTIVE.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_abortive_parent(load_trait(ABORTIVE))
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "BstA system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
