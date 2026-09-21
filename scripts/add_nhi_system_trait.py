#!/usr/bin/env python3
"""Add the Nhi system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "nhi_system.yaml"

BARI = "DOI:10.1016/j.chom.2022.03.001"
DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

NHI_IMMUNITY_SNIPPET = (
    "Here, we describe a unique mode of nucleic acid immunity mediated by a "
    "single enzyme with nuclease and helicase activities, herein referred to "
    "as Nhi (nuclease-helicase immunity)"
)
NHI_PROTECTION_SNIPPET = (
    "This enzyme provides robust protection against diverse staphylococcal "
    "phages and prevents phage DNA accumulation in cells stripped of all "
    "other known defenses"
)
NHI_INTERMEDIATE_SNIPPET = (
    "Our observations support a model in which Nhi targets and degrades "
    "phage-specific replication intermediates"
)
NHI_CONSERVATION_SNIPPET = (
    "Nhi homologs are distributed in diverse bacteria and exhibit functional "
    "conservation"
)

HMM_ROW = (
    "| Nhi__Nhi                                         | "
    "Nhi__Nhi                                         | Nhi                    | "
    "Custom                  | 100    |"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T16:05:11Z"

IDENTIFIER = "traitmech:000332"
PROPOSAL = "proposals/metpo_traitmech_v209"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Nhi | 10\\.1101/776245 | A unique mode of nucleic acid immunity "
            "performed by a single multifunctional enzyme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Nhi model "
            "namespace to the Bari et al. nuclease-helicase immunity preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "Nhi\tNhi\t1\t1\tNhi__Nhi",
        "notes": (
            "The DefenseFinder rules table models Nhi as a one-component "
            "system requiring the Nhi__Nhi profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records Nhi__Nhi under the "
            "Nhi model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Nhi system",
    "definition": (
        "A phage defense system in which an organism possesses an "
        "Nhi-family locus represented by the DefenseFinder Nhi__Nhi "
        "profile and exemplified by a single enzyme with nuclease and "
        "helicase activities that protects against diverse staphylococcal "
        "phages, prevents phage DNA accumulation, and is inferred to target "
        "and degrade phage-specific replication intermediates."
    ),
    "definition_source": BARI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Nhi",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": BARI,
            "snippet": NHI_IMMUNITY_SNIPPET,
            "notes": (
                "Bari et al. define Nhi as nuclease-helicase immunity "
                "mediated by one enzyme with nuclease and helicase "
                "activities."
            ),
        },
        {
            "reference": BARI,
            "snippet": NHI_PROTECTION_SNIPPET,
            "notes": (
                "Bari et al. support Nhi as a system that protects against "
                "diverse staphylococcal phages and prevents phage DNA "
                "accumulation even without other known defenses."
            ),
        },
        {
            "reference": BARI,
            "snippet": NHI_INTERMEDIATE_SNIPPET,
            "notes": (
                "Bari et al. infer that Nhi targets and degrades "
                "phage-specific replication intermediates."
            ),
        },
        {
            "reference": BARI,
            "snippet": NHI_CONSERVATION_SNIPPET,
            "notes": (
                "Bari et al. support functional conservation of Nhi homologs "
                "across diverse bacteria."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1282",
            "taxon_label": "Staphylococcus epidermidis",
            "note": (
                "Bari et al. characterized Nhi from the Staphylococcus "
                "epidermidis RP62a locus and showed that this single "
                "nuclease-helicase enzyme protects against diverse "
                "staphylococcal phages."
            ),
            "reference": BARI,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "nhi_locus_restricts_staphylococcal_phages",
            "title": "Nhi loci provide nuclease-helicase phage defense",
            "description": (
                "Conservative system-level sketch linking an Nhi locus to "
                "nuclease-helicase immunity, phage-replication-intermediate "
                "degradation, prevention of phage DNA accumulation, and the "
                "Nhi system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Nhi as a named single-profile phage "
                "defense system without asserting the direct phage trigger, "
                "the exact nuclease-helicase substrate, an accession-level "
                "natural host protein, or the full taxonomic breadth of "
                "functional homologs."
            ),
            "nodes": [
                {
                    "node_id": "nhi_locus",
                    "label": "Nhi locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An Nhi-family anti-phage defense locus represented "
                        "by the DefenseFinder Nhi__Nhi profile."
                    ),
                },
                {
                    "node_id": "nhi_nuclease_helicase_immunity",
                    "label": "Nhi nuclease-helicase immunity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Nucleic acid immunity mediated by one enzyme with "
                        "nuclease and helicase activities."
                    ),
                },
                {
                    "node_id": "phage_specific_replication_intermediate_degradation",
                    "label": "phage-specific replication intermediate degradation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Targeting and degradation of phage-specific "
                        "replication intermediates by Nhi."
                    ),
                },
                {
                    "node_id": "phage_dna_accumulation_prevention",
                    "label": "phage DNA accumulation prevention",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Prevention of phage DNA accumulation during Nhi "
                        "anti-phage activity."
                    ),
                },
                {
                    "node_id": "nhi_system_trait",
                    "label": "Nhi system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Nhi "
                        "nuclease-helicase phage-defense system."
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
                    "subject": "nhi_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "nhi_nuclease_helicase_immunity",
                    "description": (
                        "The Nhi locus encodes a single-enzyme "
                        "nuclease-helicase immunity system, and DefenseFinder "
                        "models Nhi as a one-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": BARI,
                            "snippet": NHI_IMMUNITY_SNIPPET,
                            "notes": (
                                "Bari et al. describe Nhi as immunity "
                                "mediated by one enzyme with nuclease and "
                                "helicase activities."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "nhi_nuclease_helicase_immunity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_specific_replication_intermediate_degradation",
                    "description": (
                        "Nhi nuclease-helicase immunity is inferred to "
                        "target and degrade phage-specific replication "
                        "intermediates."
                    ),
                    "evidence": [
                        {
                            "reference": BARI,
                            "snippet": NHI_INTERMEDIATE_SNIPPET,
                            "notes": (
                                "Bari et al. support this as a model for Nhi "
                                "rather than as a completely resolved "
                                "direct-substrate assignment."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_specific_replication_intermediate_degradation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_dna_accumulation_prevention",
                    "description": (
                        "Degradation of phage-specific replication "
                        "intermediates explains Nhi-dependent prevention of "
                        "phage DNA accumulation."
                    ),
                    "evidence": [
                        {
                            "reference": BARI,
                            "snippet": NHI_PROTECTION_SNIPPET,
                            "notes": (
                                "Bari et al. directly observed prevention of "
                                "phage DNA accumulation in Nhi-containing "
                                "cells; the replication-intermediate target "
                                "is recorded as the authors' model."
                            ),
                        },
                        {
                            "reference": BARI,
                            "snippet": NHI_INTERMEDIATE_SNIPPET,
                            "notes": (
                                "Bari et al. model Nhi as targeting and "
                                "degrading phage-specific replication "
                                "intermediates."
                            ),
                        },
                    ],
                },
                {
                    "subject": "phage_dna_accumulation_prevention",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "nhi_system_trait",
                    "description": (
                        "Preventing phage DNA accumulation realizes the Nhi "
                        "phage-defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": BARI,
                            "snippet": NHI_PROTECTION_SNIPPET,
                            "notes": (
                                "Bari et al. connect Nhi to protection "
                                "against staphylococcal phages and to "
                                "prevention of phage DNA accumulation."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "nhi_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Nhi system possession is a bacterial phage-defense "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": BARI,
                            "snippet": (
                                "highlighting the versatility of such compact "
                                "weapons as major players in antiphage defense"
                            ),
                            "notes": (
                                "Bari et al. place Nhi among compact "
                                "anti-phage defense systems."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "nhi-trigger-and-substrate-gap",
            "prompt": (
                "Resolve the Nhi phage trigger, exact "
                "replication-intermediate substrate, accession-level natural "
                "host protein, and homolog breadth before minting narrower "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Bari et al. support Nhi as a compact single-enzyme "
                "nuclease-helicase immunity system that prevents phage DNA "
                "accumulation and is inferred to target and degrade "
                "phage-specific replication intermediates. DefenseFinder "
                "models Nhi with a one-profile rule, but this first "
                "system-level record leaves the direct phage trigger, exact "
                "substrate, natural-host accession, and full taxonomic "
                "breadth of functional homologs unresolved."
            ),
            "attaches_to": ["causal_graphs#nhi_locus_restricts_staphylococcal_phages"],
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
            "Minted Nhi system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
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
