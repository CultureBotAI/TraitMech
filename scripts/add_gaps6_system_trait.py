#!/usr/bin/env python3
"""Add the GAPS6 system genomics trait and finish the GAPS1 sibling gap."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gaps6_system.yaml"
GAPS1_TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gaps1_system.yaml"

MAHATA = "DOI:10.1038/s41564-024-01840-5"
MAHATA_PREPRINT = "DOI:10.1101/2023.03.28.534373"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/gaps6.md"
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
TIMESTAMP = "2026-09-26T11:58:13Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T11:58:14Z"
GAPS1_UPDATE_TIMESTAMP = "2026-09-26T11:58:15Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000381"
PROPOSAL = "proposals/metpo_traitmech_v258"
SLUG = "gaps6"

MAHATA_GMT_SYSTEMS_SNIPPET = (
    "We reveal four anti-phage defence systems encoded within GMT islands "
    "and further characterize one system, GAPS1, showing it is triggered "
    "by a phage capsid protein to induce cell dormancy"
)
WIKI_COMPOSITION_SNIPPET = (
    "GAPS6 is composed of two proteins, "
    "[GAPS6a](https://www.ncbi.nlm.nih.gov/protein/WP_248387294.1/) "
    "and [GAPS6b](https://www.ncbi.nlm.nih.gov/protein/WP_248387295.1/). "
    "These two proteins are encoded together in diverse Gram-negative bacteria."
)
WIKI_GAPS6B_ESSENTIAL_SNIPPET = (
    "GAPS6b is essential for the defense phenotype, however it is not "
    "known whether GAPS6b could be sufficient."
)
WIKI_PINC_SNIPPET = (
    "GAPS6b is composed of TPR repeats at the N-terminus, possibly allowing "
    "ligand binding and a predicted RNAse domain (PINc, PF08745.14) at the "
    "C-terminus. PINc domains have been implicated as toxins in bacterial "
    "toxin-antitoxin modules :ref{doi=10.1093/protein/gzq081}. The PINc "
    "domain is required for the anti-phage defense activity of GAPS6."
)
WIKI_REFSEQ_SNIPPET = (
    "The GAPS6 system in *Escherichia coli* (GCF_013372365.1, "
    "NZ_CP054227) is composed of 2 proteins GAPS6b (WP_096985931.1) "
    "GAPS6a (WP_000346990.1)"
)
WIKI_VALIDATION_GRAPH_SNIPPET = (
    "Mahata_2023[<a href='https://doi.org/10.1101/2023.03.28.534373'>"
    "Mahata et al., 2023</a>] --> Origin_0\n"
    "    Origin_0[Vibrio parahaemolyticus \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_248387294.1'>"
    "WP_248387294.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "WP_248387295.1'>WP_248387295.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> T7 & T4 & P1-vir & Lambda-vir"
)
ARTICLE_REGISTRY_SNIPPET = (
    "GAPS6 | 10\\.1101/2023\\.03\\.28\\.534373 | Gamma-Mobile-Trio systems "
    "define a new class of mobile elements rich in bacterial defensive and "
    "offensive tools"
)
RULES_SNIPPET = "GAPS6\tGAPS6\t2\t2\tGAPS6__GAPS6a, GAPS6__GAPS6b\t\t\t"
GAPS6_HMM_PROFILES = ("GAPS6__GAPS6a", "GAPS6__GAPS6b")
GAPS6_HMM_GA_CUT = "20"


def mahata_gmt_systems_evidence() -> dict[str, str]:
    return {
        "reference": MAHATA,
        "snippet": MAHATA_GMT_SYSTEMS_SNIPPET,
        "notes": (
            "Mahata et al. identify four anti-phage defense systems in "
            "Gamma-Mobile-Trio islands."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki describes GAPS6 as a two-protein "
            "system with GAPS6a and GAPS6b encoded together."
        ),
    }


def wiki_gaps6b_essential_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_GAPS6B_ESSENTIAL_SNIPPET,
        "notes": (
            "The DefenseFinder wiki reports that GAPS6b is essential for "
            "GAPS6 defense but leaves GAPS6b sufficiency unresolved."
        ),
    }


def wiki_pinc_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_PINC_SNIPPET,
        "notes": (
            "The DefenseFinder wiki reports that GAPS6b carries TPR repeats "
            "and a PINc domain required for GAPS6 anti-phage activity."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "GAPS6 locus in RefSeq assembly GCF_013372365.1 on NZ_CP054227."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links Mahata "
            "et al. to a Vibrio parahaemolyticus GAPS6 source locus "
            "expressed in E. coli against T7, T4, P1-vir, and Lambda-vir."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named GAPS6 system "
            "to the Mahata et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models GAPS6 as a two-profile "
            "system requiring GAPS6__GAPS6a and GAPS6__GAPS6b."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            f"| {profile:<49}| {profile:<49}| "
            f"{'GAPS6':<23}| {'Custom':<24}| {GAPS6_HMM_GA_CUT:<7}|"
        ),
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under the "
            "GAPS6 system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "GAPS6 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "GMT-encoded GAPS6 locus represented by DefenseFinder as a "
        "two-profile model, GAPS6__GAPS6a and GAPS6__GAPS6b, and "
        "experimentally linked to T7, T4, P1-vir, and lambda-vir "
        "protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "GAPS6",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in GAPS6_HMM_PROFILES
        ],
    ],
    "evidence": [
        mahata_gmt_systems_evidence(),
        wiki_composition_evidence(),
        wiki_gaps6b_essential_evidence(),
        wiki_pinc_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        *[hmm_evidence(profile) for profile in GAPS6_HMM_PROFILES],
    ],
    "causal_graphs": [
        {
            "graph_id": "gaps6_locus_restricts_phages",
            "title": "GAPS6 loci protect against T7, T4, P1-vir, and lambda-vir",
            "description": (
                "Conservative system-level sketch linking GAPS6 locus "
                "possession to protection against T7, T4, P1-vir, and "
                "lambda-vir."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures GAPS6 as a named two-profile "
                "DefenseFinder phage-defense system while leaving natural "
                "host breadth, the activity of GAPS6a, GAPS6b sufficiency "
                "and trigger specificity, and exact GAPS6a/GAPS6b "
                "profile-to-protein correspondence unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gaps6_locus",
                    "label": "GAPS6 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A GMT-encoded phage-defense locus represented by "
                        "the GAPS6__GAPS6a and GAPS6__GAPS6b DefenseFinder "
                        "profiles."
                    ),
                },
                {
                    "node_id": "gaps6_listed_phage_protection",
                    "label": "T7, T4, P1-vir, and lambda-vir protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against T7, T4, P1-vir, and lambda-vir "
                        "by GAPS6."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "GAPS6 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded GAPS6 phage-defense "
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
                    "subject": "gaps6_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gaps6_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a Vibrio "
                        "parahaemolyticus GAPS6 locus from Mahata et al. to "
                        "protection against T7, T4, P1-vir, and lambda-vir, "
                        "and DefenseFinder models GAPS6 through two "
                        "mandatory profiles."
                    ),
                    "evidence": [
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        rules_evidence(),
                        *[
                            hmm_evidence(profile)
                            for profile in GAPS6_HMM_PROFILES
                        ],
                    ],
                },
                {
                    "subject": "gaps6_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against T7, T4, P1-vir, and lambda-vir "
                        "realizes the GAPS6 system trait."
                    ),
                    "evidence": [wiki_validation_evidence()],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "GAPS6 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        mahata_gmt_systems_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "gaps6-mechanism-gap",
            "prompt": (
                "Resolve GAPS6 natural host breadth, GAPS6a activity, "
                "GAPS6b sufficiency and trigger specificity, and exact "
                "GAPS6a/GAPS6b profile-to-protein correspondence before "
                "minting narrower GAPS6 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mahata et al. support GAPS6 as a GMT-encoded anti-phage "
                "defense system that protects E. coli against T7, T4, "
                "P1-vir, and lambda-vir when expressed from a Vibrio "
                "parahaemolyticus locus, and DefenseFinder represents GAPS6 "
                "as a two-profile system. Natural host breadth, GAPS6a "
                "activity, GAPS6b sufficiency, the phage trigger, and exact "
                "profile-to-protein correspondence remain unresolved."
            ),
            "evidence": [
                wiki_composition_evidence(),
                wiki_gaps6b_essential_evidence(),
                wiki_pinc_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                *[hmm_evidence(profile) for profile in GAPS6_HMM_PROFILES],
            ],
            "attaches_to": ["causal_graphs#gaps6_locus_restricts_phages"],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        }
    ],
}


def write_gaps6_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted GAPS6 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed GAPS6 system canonical_examples and left them empty "
            "because the current sources support a Vibrio parahaemolyticus "
            "accession-level experimental validation graph, a DefenseFinder "
            "system model, and a RefSeq Escherichia coli example, but not a "
            "direct native microbial isolate exemplar with experimentally "
            "verified endogenous GAPS6 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def load_gaps1_record() -> dict[str, Any]:
    record = yaml.safe_load(GAPS1_TARGET.read_text())
    if not isinstance(record, dict):
        raise TypeError(f"{GAPS1_TARGET} did not parse to a mapping")
    if record.get("identifier") != "traitmech:000371":
        raise ValueError("GAPS1 record identifier changed")
    if record.get("label") != "GAPS1 system":
        raise ValueError("GAPS1 record label changed")
    if record.get("mapping_status") != "PROPOSED":
        raise ValueError("GAPS1 record mapping_status changed")
    if record["discussions"][0]["discussion_id"] != "gaps1-trigger-sibling-gap":
        raise ValueError("GAPS1 sibling discussion is not the first discussion")
    if record["discussions"][0]["status"] != "OPEN":
        raise ValueError("GAPS1 sibling discussion is no longer open")
    if "GAPS6 boundaries" not in record["discussions"][0]["prompt"]:
        raise ValueError("GAPS1 sibling prompt no longer mentions GAPS6")
    return record


def update_gaps1_record(*, apply: bool) -> None:
    record = load_gaps1_record()
    graph = record["causal_graphs"][0]
    discussion = record["discussions"][0]
    graph["scope_notes"] = graph["scope_notes"].replace(
        (
            "the molecular activity of the GAPS1 component, the exact "
            "capsid-protein trigger, and sibling GAPS6 systems unresolved"
        ),
        (
            "the molecular activity of the GAPS1 component, and the exact "
            "capsid-protein trigger unresolved"
        ),
    )
    discussion["prompt"] = discussion["prompt"].replace(
        "GAPS1 component activity, natural-host exemplars, and GAPS6 boundaries",
        "GAPS1 component activity and natural-host exemplars",
    )
    discussion["rationale"] = discussion["rationale"].replace(
        "a universal GAPS1 host range, or sibling GAPS6 system boundaries",
        "or a universal GAPS1 host range",
    )
    record_curation_event(
        record,
        action="UPDATED_DISCUSSION",
        changes=(
            "Resolved the remaining stale GAPS1 sibling-boundary reference "
            "after GAPS6 was split into its own TraitRecord."
        ),
        curator=CURATOR,
        timestamp=GAPS1_UPDATE_TIMESTAMP,
        llm_assisted=True,
    )
    if apply:
        write_validated_trait(record, GAPS1_TARGET)
    else:
        print(f"Would update {GAPS1_TARGET.relative_to(REPO_ROOT)}")


def write_record(*, apply: bool) -> None:
    write_gaps6_record(apply=apply)
    update_gaps1_record(apply=apply)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
