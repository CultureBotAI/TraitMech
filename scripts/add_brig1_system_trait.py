#!/usr/bin/env python3
"""Add the Brig1 system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brig1_system.yaml"

HALLINAN = "DOI:10.1038/s41586-024-07329-9"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T10:37:00Z"
IDENTIFIER = "traitmech:000307"
PROPOSAL = "proposals/metpo_traitmech_v184"

BRIG1_ADP_RIBOSYL_ROW = (
    "| Brig1__ADP_ribosyl                               | "
    "                                                 | Brig1                  | "
    "Custom                  | 20     |"
)
BRIG1_ROW = (
    "| Brig1__Brig1                                     | "
    "                                                 | Brig1                  | "
    "Custom                  | 20     |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Brig1 | 10\\.1038/s41586-024-07329-9 | DNA glycosylases "
            "provide antiviral defence in prokaryotes"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Brig1 model "
            "namespace to the Hallinan et al. Brig1 DNA-glycosylase paper."
        ),
    }


def brig1_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": BRIG1_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records Brig1__Brig1 under "
            "the Brig1 model namespace."
        ),
    }


def brig1_adp_ribosyl_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": BRIG1_ADP_RIBOSYL_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records Brig1__ADP_ribosyl "
            "under the Brig1 model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Brig1 system",
    "definition": (
        "A phage defense system in which an organism possesses a brig1-family "
        "locus whose encoded DNA glycosylase can excise "
        "alpha-glucosyl-hydroxymethylcytosine nucleobases from T-even "
        "bacteriophage DNA, generate abasic sites, and inhibit viral DNA "
        "replication."
    ),
    "definition_source": HALLINAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Brig1",
            "synonym_type": "RELATED_SYNONYM",
            "source": HALLINAN,
        },
        {
            "synonym_text": "bacteriophage replication inhibition DNA glycosylase 1",
            "synonym_type": "RELATED_SYNONYM",
            "source": HALLINAN,
        },
    ],
    "evidence": [
        {
            "reference": HALLINAN,
            "snippet": (
                "Following this approach, we identified Brig1, a DNA "
                "glycosylase that excises "
                "α-glucosyl-hydroxymethylcytosine nucleobases from "
                "the bacteriophage T4 genome to generate abasic sites and "
                "inhibit viral replication"
            ),
            "notes": (
                "Hallinan et al. identify Brig1 as a phage DNA-targeting "
                "DNA glycosylase."
            ),
        },
        {
            "reference": HALLINAN,
            "snippet": (
                "Brig1 homologues that provide immunity against T-even "
                "phages are present in multiple phage defence loci across "
                "distinct clades of bacteria"
            ),
            "notes": (
                "Hallinan et al. support modelling Brig1 as a bacterial "
                "phage-defence locus family rather than as one cloned "
                "environmental DNA insert."
            ),
        },
        {
            "reference": HALLINAN,
            "snippet": (
                "This result demonstrates that gene c not only inhibits "
                "T4 DNA replication but also causes a slight and gradual "
                "depletion of the phage DNA within the infected population"
            ),
            "notes": (
                "Hallinan et al. connect the gene later named brig1 to "
                "inhibited T4 DNA replication in infected cells."
            ),
        },
        {
            "reference": HALLINAN,
            "snippet": (
                "Together, these data demonstrate that Brig1 targets "
                "α-glucosylated hmC nucleobases in the viral DNA to "
                "provide defence against T4"
            ),
            "notes": (
                "Hallinan et al. show that Brig1 defense is specific to "
                "alpha-glucosylated hydroxymethylcytosine in phage DNA."
            ),
        },
        {
            "reference": HALLINAN,
            "snippet": (
                "Together, these results demonstrate that Brig1 is a DNA "
                "glycosylase that excises α-glucosyl-hmC nucleobases "
                "from ssDNA to generate abasic sites"
            ),
            "notes": (
                "Hallinan et al. directly verify that Brig1 DNA "
                "glycosylase activity creates abasic sites on "
                "alpha-glucosyl-hmC-containing substrates."
            ),
        },
        article_registry_evidence(),
        brig1_hmm_evidence(),
        brig1_adp_ribosyl_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "brig1_excises_modified_t_even_phage_dna",
            "title": "Brig1 excises modified T-even phage DNA",
            "description": (
                "Conservative system-level sketch linking a brig1-family "
                "locus to alpha-glucosyl-hmC base excision, abasic-site "
                "generation, inhibited T4-like phage DNA replication, "
                "restricted T-even phage propagation, and the Brig1 "
                "phage-defense trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Brig1 as a named DefenseFinder "
                "DNA-glycosylase phage-defense system whose prototype "
                "targets alpha-glucosyl-hmC nucleobases in T4 DNA and "
                "inhibits phage DNA replication while leaving the natural "
                "host, the source of the metagenomic prototype, whether all "
                "Brig1 homologues target exactly the same glucosylated "
                "nucleobase, and the relationship of the DefenseFinder "
                "Brig1__ADP_ribosyl profile to characterized Brig1 "
                "activity unresolved."
            ),
            "nodes": [
                {
                    "node_id": "brig1_locus",
                    "label": "brig1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A brig1-family phage-defense locus represented by "
                        "the DefenseFinder Brig1 model namespace."
                    ),
                },
                {
                    "node_id": "alpha_glucosyl_hmc_base_excision",
                    "label": "alpha-glucosyl-hmC base excision",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Brig1-mediated excision of alpha-glucosylated "
                        "hydroxymethylcytosine nucleobases from phage DNA."
                    ),
                },
                {
                    "node_id": "phage_dna_abasic_site_generation",
                    "label": "phage DNA abasic-site generation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Generation of abasic sites in glucosylated "
                        "T-even phage DNA after Brig1-mediated base excision."
                    ),
                },
                {
                    "node_id": "phage_dna_replication_inhibition",
                    "label": "phage DNA replication inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Inhibition and depletion of T4 phage DNA during "
                        "infection downstream of Brig1 activity."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of phage propagation in a "
                        "Brig1-containing infected host cell."
                    ),
                },
                {
                    "node_id": "brig1_system_trait",
                    "label": "Brig1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Brig1 "
                        "DNA-glycosylase phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system_trait",
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
                    "subject": "brig1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "alpha_glucosyl_hmc_base_excision",
                    "description": (
                        "The brig1 gene encodes a DNA glycosylase that "
                        "excises alpha-glucosyl-hmC nucleobases."
                    ),
                    "evidence": [
                        {
                            "reference": HALLINAN,
                            "snippet": (
                                "Brig1 is a DNA glycosylase that excises "
                                "α-glucosyl-hmC nucleobases from ssDNA "
                                "to generate abasic sites"
                            ),
                            "notes": (
                                "Hallinan et al. directly connect Brig1 "
                                "glycosylase activity to base excision."
                            ),
                        },
                        brig1_hmm_evidence(),
                    ],
                },
                {
                    "subject": "alpha_glucosyl_hmc_base_excision",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_dna_abasic_site_generation",
                    "description": (
                        "Brig1-mediated excision of alpha-glucosyl-hmC "
                        "generates abasic sites in modified DNA."
                    ),
                    "evidence": [
                        {
                            "reference": HALLINAN,
                            "snippet": (
                                "excises α-glucosyl-hmC nucleobases "
                                "from ssDNA to generate abasic sites"
                            ),
                            "notes": (
                                "Hallinan et al. show that the excision "
                                "reaction yields abasic sites."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_dna_abasic_site_generation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_dna_replication_inhibition",
                    "description": (
                        "Brig1-generated abasic sites on alpha-glucosylated "
                        "phage DNA are associated with inhibited T4 DNA "
                        "replication during infection."
                    ),
                    "evidence": [
                        {
                            "reference": HALLINAN,
                            "snippet": (
                                "Brig1 targets α-glucosylated hmC "
                                "nucleobases in the viral DNA to provide "
                                "defence against T4"
                            ),
                            "notes": (
                                "Hallinan et al. connect modified-base "
                                "targeting in viral DNA to T4 defense."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_dna_replication_inhibition",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Brig1-associated inhibition of T4 DNA replication "
                        "restricts phage propagation after infection."
                    ),
                    "evidence": [
                        {
                            "reference": HALLINAN,
                            "snippet": (
                                "gene c not only inhibits T4 DNA "
                                "replication but also causes a slight and "
                                "gradual depletion of the phage DNA within "
                                "the infected population"
                            ),
                            "notes": (
                                "Hallinan et al. measure T4 DNA replication "
                                "inhibition downstream of Brig1 expression."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brig1_system_trait",
                    "description": (
                        "Restriction of T-even phage propagation realizes "
                        "the Brig1 system trait."
                    ),
                    "evidence": [
                        {
                            "reference": HALLINAN,
                            "snippet": (
                                "Brig1 homologues that provide immunity "
                                "against T-even phages are present in "
                                "multiple phage defence loci across "
                                "distinct clades of bacteria"
                            ),
                            "notes": (
                                "Hallinan et al. frame Brig1 homologues as "
                                "a bacterial phage-defense locus family."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "brig1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system_trait",
                    "description": (
                        "Brig1 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": HALLINAN,
                            "snippet": (
                                "Brig1, a previously unknown anti-phage "
                                "defence system with homologues across "
                                "distinct clades of bacteria"
                            ),
                            "notes": (
                                "The Hallinan et al. editor summary "
                                "places Brig1 in the anti-phage defense "
                                "system class."
                            ),
                        },
                        brig1_adp_ribosyl_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brig1-natural-host-and-profile-gap",
            "prompt": (
                "Resolve natural Brig1 host taxa, broader Brig1-family "
                "specificity, and the Brig1__ADP_ribosyl DefenseFinder "
                "profile before minting narrower Brig1 children or adding "
                "canonical examples."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Hallinan et al. functionally isolated the first brig1 "
                "gene from a soil metagenomic fragment rather than a "
                "sequenced natural isolate, and they showed that "
                "experimentally tested Brig1 homologues can protect "
                "against T-even phages. The first TraitRecord therefore "
                "covers Brig1-family antiphage DNA-glycosylase-system "
                "possession while leaving natural host exemplars, the "
                "full sequence-level system architecture, and the "
                "relationship between the DefenseFinder Brig1__Brig1 and "
                "Brig1__ADP_ribosyl profiles to separate subtype review."
            ),
            "evidence": [
                {
                    "reference": HALLINAN,
                    "snippet": (
                        "To uncover novel anti-phage defence systems "
                        "present in unsequenced bacterial genomes, we "
                        "screened an eDNA library generated in an earlier "
                        "study"
                    ),
                    "notes": (
                        "Hallinan et al. functionally isolated the first "
                        "Brig1 source fragment from an environmental DNA "
                        "library rather than a named natural organism."
                    ),
                },
                brig1_adp_ribosyl_evidence(),
            ],
            "attaches_to": ["causal_graphs#brig1_excises_modified_t_even_phage_dna"],
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
            "Minted Brig1 system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_output(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    validate_output(record)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
    else:
        print(
            "Brig1 system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
