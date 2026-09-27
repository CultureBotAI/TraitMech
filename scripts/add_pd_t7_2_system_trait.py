#!/usr/bin/env python3
"""Add the PD-T7-2 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_t7_2_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-t7-2.md"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-26T23:48:04Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T23:48:05Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000396"
PROPOSAL = "proposals/metpo_traitmech_v273"
SLUG = "pd_t7_2"
PHAGE_LIST = "T2, T4, T6, LambdaVir, T5, SECphi18, SECphi27, T3, and T7"
PROFILES = ("PD-T7-2__PD-T7-2_A", "PD-T7-2__PD-T7-2_B")
HMM_GA_CUTS = {
    "PD-T7-2__PD-T7-2_A": "50",
    "PD-T7-2__PD-T7-2_B": "100",
}

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_COMPOSITION_SNIPPET = (
    "The PD-T7-2 is composed of 2 proteins: PD-T7-2_A and PD-T7-2_B."
)
LEDERBERGIA_EXAMPLE_SNIPPET = (
    "The PD-T7-2 system in *Lederbergia lenta* "
    "(GCF_900478165.1, NZ_LS483476) is composed of 2 proteins "
    "PD-T7-2_A (WP_066145327.1) PD-T7-2_B (WP_066145329.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RRM73498.1'>"
    "RRM73498.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "RRM73410.1'>RRM73410.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T2 & T4 & T6 & "
    "LambdaVir & T5 & SECphi18 & SECphi27 & T3 & T7"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        T2\n"
    "        T4\n"
    "        T6\n"
    "        LambdaVir\n"
    "        T5\n"
    "        SECphi18\n"
    "        SECphi27\n"
    "        T3\n"
    "        T7"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-T7-2 | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the "
    "landscape of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = (
    "PD-T7-2\tPD-T7-2\t2\t2\t"
    "PD-T7-2__PD-T7-2_A, PD-T7-2__PD-T7-2_B\t\t\t"
)


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-T7-2 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names PD-T7-2 as a two-protein system "
            "with PD-T7-2_A and PD-T7-2_B."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": LEDERBERGIA_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "PD-T7-2 locus in RefSeq assembly GCF_900478165.1 on "
            "NZ_LS483476."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-T7-2 source locus expressed "
            f"in E. coli against {PHAGE_LIST}."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            f"{PHAGE_LIST} in the PD-T7-2 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PD-T7-2 "
            "system to the Vassallo et al. E. coli pangenome "
            "phage-defense preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-T7-2 as a two-profile "
            "system requiring PD-T7-2__PD-T7-2_A and "
            "PD-T7-2__PD-T7-2_B."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            f"| {profile:<49}| {profile:<49}| "
            f"{'PD-T7-2':<23}| {'Custom':<24}| "
            f"{HMM_GA_CUTS[profile]:<7}|"
        ),
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under the "
            "PD-T7-2 system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-T7-2 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "PD-T7-2 locus represented by DefenseFinder as a two-profile model, "
        "PD-T7-2__PD-T7-2_A and PD-T7-2__PD-T7-2_B, and experimentally "
        f"linked to {PHAGE_LIST} protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-T7-2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in PROFILES
        ],
    ],
    "evidence": [
        vassallo_screen_evidence(),
        wiki_composition_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        *[hmm_evidence(profile) for profile in PROFILES],
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_t7_2_locus_restricts_phages",
            "title": "PD-T7-2 loci restrict T2, T4, T6, LambdaVir, T5, "
            "SECphi18, SECphi27, T3, and T7",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PD-T7-2 locus to protection against T2, T4, T6, "
                "LambdaVir, T5, SECphi18, SECphi27, T3, and T7."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-T7-2 as a named DefenseFinder "
                "phage-defense system while leaving natural host breadth, "
                "the direct phage trigger, the effector mechanism, and "
                "exact profile-to-protein correspondence unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_t7_2_locus",
                    "label": "PD-T7-2 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the "
                        "PD-T7-2_A and PD-T7-2_B DefenseFinder profiles."
                    ),
                },
                {
                    "node_id": "pd_t7_2_listed_phage_protection",
                    "label": "T2, T4, T6, LambdaVir, T5, SECphi18, "
                    "SECphi27, T3, and T7 protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against T2, T4, T6, LambdaVir, T5, "
                        "SECphi18, SECphi27, T3, and T7 by PD-T7-2."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-T7-2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-T7-2 "
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
                    "subject": "pd_t7_2_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_t7_2_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-T7-2 locus "
                        "from Vassallo et al. to broad phage protection, "
                        "and DefenseFinder models PD-T7-2 through two "
                        "mandatory profiles."
                    ),
                    "evidence": [
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        *[hmm_evidence(profile) for profile in PROFILES],
                    ],
                },
                {
                    "subject": "pd_t7_2_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against the listed phages realizes "
                        "the PD-T7-2 system trait."
                    ),
                    "evidence": [
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "PD-T7-2 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        vassallo_screen_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pd-t7-2-mechanism-gap",
            "prompt": (
                "Resolve PD-T7-2 natural host breadth, direct phage trigger, "
                "effector mechanism, and profile-to-protein correspondence "
                "before minting narrower PD-T7-2 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-T7-2 as one of the conserved "
                "systems from an E. coli pangenome phage-defense selection, "
                "the DefenseFinder wiki maps the source locus to broad "
                "phage protection, and DefenseFinder represents the system "
                "with two profiles. Natural host breadth, the direct phage "
                "trigger, exact effector logic, and the exact correspondence "
                "between the two profiles and proteins remain unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_composition_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                *[hmm_evidence(profile) for profile in PROFILES],
            ],
            "attaches_to": ["causal_graphs#pd_t7_2_locus_restricts_phages"],
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
            "Minted PD-T7-2 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        curator=CURATOR,
        timestamp=TIMESTAMP,
        llm_assisted=True,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed PD-T7-2 system canonical_examples and left them empty "
            "because the current sources support an E. coli accession-level "
            "experimental validation graph, a DefenseFinder system model, "
            "and a RefSeq Lederbergia lenta example, but not a direct "
            "native microbial isolate exemplar with experimentally verified "
            "endogenous PD-T7-2 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
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
