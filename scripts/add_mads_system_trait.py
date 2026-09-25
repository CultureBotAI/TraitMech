#!/usr/bin/env python3
"""Add the MADS system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mads_system.yaml"

MAESTRI = "DOI:10.1016/j.chom.2024.07.005"
MAESTRI_PREPRINT = "DOI:10.1101/2023.03.30.534895"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-25T03:36:00Z"
POSED_DATE = "2026-09-24"
IDENTIFIER = "traitmech:000370"
PROPOSAL = "proposals/metpo_traitmech_v247"

DISCOVERY_SNIPPET = "coined methylation-associated defense system (MADS)"
RESISTANCE_SNIPPET = (
    "MADS interacts with a CRISPR-Cas system in its native host to provide "
    "robust and durable resistance against phages"
)
DNA_PHAGE_SNIPPET = (
    "MADS encodes a defense system that is active against at least 4 "
    "different DNA phages"
)
METHYLATION_SNIPPET = (
    "MADS uses a methylation-based self/non-self discrimination mechanism"
)
PREPRINT_TITLE_SNIPPET = (
    "Bacterial defences interact synergistically by disrupting phage cooperation"
)
ARTICLE_REGISTRY_SNIPPET = (
    "MADS | 10\\.1101/2023\\.03\\.30\\.534895 | Bacterial defences "
    "interact synergistically by disrupting phage cooperation"
)
RULES_SNIPPET = (
    "MADS\tMADS\t3\t3\tMADS__mad1, MADS__mad2, MADS__mad3, "
    "MADS__mad4, MADS__mad5, MADS__mad6, MADS__mad7, MADS__mad8\t\t\t"
)

HMM_GA_CUTS = {
    "MADS__mad1": "20",
    "MADS__mad2": "150",
    "MADS__mad3": "200",
    "MADS__mad4": "50",
    "MADS__mad5": "50",
    "MADS__mad6": "150",
    "MADS__mad7": "100",
    "MADS__mad8": "100",
}


def maestri_discovery_evidence() -> dict[str, str]:
    return {
        "reference": MAESTRI,
        "snippet": DISCOVERY_SNIPPET,
        "notes": (
            "Maestri et al. coin methylation-associated defense system (MADS) "
            "for the newly discovered phage-defense locus."
        ),
    }


def maestri_resistance_evidence() -> dict[str, str]:
    return {
        "reference": MAESTRI,
        "snippet": RESISTANCE_SNIPPET,
        "notes": (
            "Maestri et al. show that native-host MADS and CRISPR-Cas "
            "cooperate to provide robust phage resistance."
        ),
    }


def maestri_dna_phage_evidence() -> dict[str, str]:
    return {
        "reference": MAESTRI,
        "snippet": DNA_PHAGE_SNIPPET,
        "notes": (
            "Maestri et al. support MADS activity against DMS3vir and three "
            "additional DNA phages."
        ),
    }


def maestri_methylation_evidence() -> dict[str, str]:
    return {
        "reference": MAESTRI,
        "snippet": METHYLATION_SNIPPET,
        "notes": (
            "Maestri et al. connect MADS to methylation-based self/non-self "
            "discrimination."
        ),
    }


def maestri_preprint_evidence() -> dict[str, str]:
    return {
        "reference": MAESTRI_PREPRINT,
        "snippet": PREPRINT_TITLE_SNIPPET,
        "notes": (
            "The bioRxiv version of Maestri et al. is the DOI cited in "
            "DefenseFinder's MADS article-registry row."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named MADS system to "
            "the Maestri et al. preprint."
        ),
    }


def defensefinder_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models MADS with MADS__mad1 "
            "through MADS__mad8 profiles and a minimum of three mandatory "
            "matches."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    ga_cut = HMM_GA_CUTS[profile]
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            f"| {profile:<49}| {profile:<49}| "
            f"{'MADS':<23}| {'Custom':<24}| {ga_cut:<7}|"
        ),
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under the "
            "MADS model namespace."
        ),
    }


def mads_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_GA_CUTS]

RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "MADS system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "methylation-associated defense system locus whose canonical "
        "architecture has mad1 through mad8 genes and whose "
        "methylation-coupled self/non-self discrimination can restrict "
        "bacteriophage infection."
    ),
    "definition_source": MAESTRI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "MADS",
            "synonym_type": "EXACT_SYNONYM",
            "source": MAESTRI,
        },
        {
            "synonym_text": "methylation-associated defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": MAESTRI,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_GA_CUTS
        ],
    ],
    "evidence": [
        maestri_discovery_evidence(),
        maestri_resistance_evidence(),
        maestri_dna_phage_evidence(),
        maestri_methylation_evidence(),
        maestri_preprint_evidence(),
        article_registry_evidence(),
        defensefinder_rules_evidence(),
        *mads_hmm_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "note": (
                "Maestri et al. discovered MADS in the native Pseudomonas "
                "aeruginosa SMC4386 locus and showed that deleting the locus "
                "reduced resistance to phage DMS3vir."
            ),
            "reference": MAESTRI,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "mads_methylation_restricts_phage",
            "title": "MADS loci confer methylation-associated phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "MADS locus to methylation-based self/non-self "
                "discrimination, restriction of DNA phages, and the MADS "
                "system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures MADS as a named eight-gene DefenseFinder "
                "profile set whose activity is associated with methylation "
                "and DNA restriction while leaving the exact mapping from the "
                "MADS__mad profiles to nuclease, ATPase, kinase, specificity, "
                "and methyltransferase activities unresolved."
            ),
            "nodes": [
                {
                    "node_id": "mads_locus",
                    "label": "MADS locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A methylation-associated phage-defense locus in the "
                        "MADS family."
                    ),
                },
                {
                    "node_id": "mads_self_nonself_discrimination",
                    "label": "MADS self/non-self discrimination",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Methylation-based discrimination between host DNA "
                        "and unmethylated mobile genetic element DNA by MADS."
                    ),
                },
                {
                    "node_id": "dna_phage_restriction",
                    "label": "DNA phage restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of infecting DNA bacteriophages by the "
                        "MADS locus."
                    ),
                },
                {
                    "node_id": "mads_system_trait",
                    "label": "MADS system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded MADS phage-defense "
                        "system."
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
                    "subject": "mads_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "mads_self_nonself_discrimination",
                    "description": (
                        "MADS loci encode an eight-gene methylation-associated "
                        "defense system, and DefenseFinder models MADS as an "
                        "eight-profile rule with at least three mandatory "
                        "matches."
                    ),
                    "evidence": [
                        maestri_discovery_evidence(),
                        maestri_methylation_evidence(),
                        article_registry_evidence(),
                        defensefinder_rules_evidence(),
                        *mads_hmm_evidence(),
                    ],
                },
                {
                    "subject": "mads_self_nonself_discrimination",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dna_phage_restriction",
                    "description": (
                        "MADS-associated methylation-based self/non-self "
                        "discrimination contributes to DNA-phage restriction."
                    ),
                    "evidence": [
                        maestri_methylation_evidence(),
                        maestri_dna_phage_evidence(),
                    ],
                },
                {
                    "subject": "dna_phage_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "mads_system_trait",
                    "description": (
                        "MADS-mediated DNA-phage restriction realizes the MADS "
                        "system trait."
                    ),
                    "evidence": [maestri_dna_phage_evidence()],
                },
                {
                    "subject": "mads_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "MADS system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        maestri_discovery_evidence(),
                        maestri_resistance_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "mads-profile-activity-gap",
            "prompt": (
                "Resolve MADS subtype boundaries, MADS3-4 relationships, "
                "and Mad1-Mad8 profile-to-activity mappings before minting "
                "narrower MADS mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Maestri et al. support MADS as a methylation-associated "
                "defense system active against DNA phages, and DefenseFinder "
                "models MADS as an eight-profile rule. The pinned model "
                "does not resolve which combinations of MADS__mad profiles "
                "correspond to methylation, specificity, nuclease, ATPase, "
                "or kinase activities, so this first record stays at system "
                "level."
            ),
            "evidence": [
                maestri_dna_phage_evidence(),
                defensefinder_rules_evidence(),
            ],
            "attaches_to": ["causal_graphs#mads_methylation_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        }
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted MADS system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            f"proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        curator=CURATOR,
        timestamp=TIMESTAMP,
        llm_assisted=True,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
