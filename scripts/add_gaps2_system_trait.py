#!/usr/bin/env python3
"""Add the GAPS2 system genomics trait and narrow the GAPS1 sibling gap."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gaps2_system.yaml"
GAPS1_TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gaps1_system.yaml"

MAHATA = "DOI:10.1038/s41564-024-01840-5"
MAHATA_PREPRINT = "DOI:10.1101/2023.03.28.534373"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/gaps2.md"
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
TIMESTAMP = "2026-09-26T11:26:41Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T11:26:42Z"
GAPS1_UPDATE_TIMESTAMP = "2026-09-26T11:26:43Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000380"
PROPOSAL = "proposals/metpo_traitmech_v257"
SLUG = "gaps2"

MAHATA_GMT_SYSTEMS_SNIPPET = (
    "We reveal four anti-phage defence systems encoded within GMT islands "
    "and further characterize one system, GAPS1, showing it is triggered "
    "by a phage capsid protein to induce cell dormancy"
)
WIKI_COMPOSITION_SNIPPET = (
    "The GAPS2 system is composed of a single protein. It was found in "
    "Gamma-Mobile-Trio (GMT) protein containing genomic island in Vibrio, "
    "and cloned into E. coli K-12 :ref{doi=10.1101/2023.03.28.534373}. "
    "The name GAPS derives from the \"GMT-encoded Anti-Phage System\" "
    "acronym."
)
WIKI_BRCT_SNIPPET = (
    "GAPS2 is composed of a single protein with a DNA BRCT domains "
    ":ref{doi=10.4161/cc.10.15.16312}."
)
WIKI_UNKNOWN_MECHANISM_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown."
)
WIKI_REFSEQ_SNIPPET = (
    "The GAPS2 system in *Mannheimia sp. USDA-ARS-USMARC-1261* "
    "(GCF_000521605.1, NZ_CP006942) is composed of 1 protein: GAPS2 "
    "(WP_025236539.1)"
)
WIKI_VALIDATION_GRAPH_SNIPPET = (
    "Mahata_2023[<a href='https://doi.org/10.1101/2023.03.28.534373'>"
    "Mahata et al., 2023</a>] --> Origin_0\n"
    "    Origin_0[Vibrio parahaemolyticus \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_174208646.1'>"
    "WP_174208646.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> P1-vir & Lambda-vir"
)
WIKI_PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        P1-vir\n"
    "        Lambda-vir"
)
ARTICLE_REGISTRY_SNIPPET = (
    "GAPS2 | 10\\.1101/2023\\.03\\.28\\.534373 | Gamma-Mobile-Trio systems "
    "define a new class of mobile elements rich in bacterial defensive and "
    "offensive tools"
)
RULES_SNIPPET = "GAPS2\tGAPS2\t1\t1\tGAPS2__GAPS2\t\t\t"
GAPS2_HMM_PROFILE = "GAPS2__GAPS2"
GAPS2_HMM_GA_CUT = "100"


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
            "The DefenseFinder wiki describes GAPS2 as a single-protein "
            "GMT-encoded system cloned from Vibrio into E. coli K-12."
        ),
    }


def wiki_brct_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_BRCT_SNIPPET,
        "notes": (
            "The DefenseFinder wiki reports a DNA BRCT domain in the "
            "single GAPS2 protein."
        ),
    }


def wiki_unknown_mechanism_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_UNKNOWN_MECHANISM_SNIPPET,
        "notes": "The DefenseFinder wiki records the GAPS2 mechanism as unknown.",
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted single-protein "
            "GAPS2 locus in RefSeq assembly GCF_000521605.1 on NZ_CP006942."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Mahata et al. to a Vibrio parahaemolyticus GAPS2 source locus "
            "expressed in E. coli against P1-vir and Lambda-vir."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            "P1-vir and Lambda-vir in the GAPS2 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named GAPS2 system "
            "to the Mahata et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models GAPS2 as a single-profile "
            "system requiring GAPS2__GAPS2."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            f"| {GAPS2_HMM_PROFILE:<49}| {GAPS2_HMM_PROFILE:<49}| "
            f"{'GAPS2':<23}| {'Custom':<24}| {GAPS2_HMM_GA_CUT:<7}|"
        ),
        "notes": (
            "The DefenseFinder HMM inventory records GAPS2__GAPS2 under the "
            "GAPS2 system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "GAPS2 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "GMT-encoded GAPS2 locus represented by DefenseFinder as a "
        "single-profile model, GAPS2__GAPS2, and experimentally linked to "
        "P1-vir and lambda-vir protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "GAPS2",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        {
            "synonym_text": GAPS2_HMM_PROFILE,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        mahata_gmt_systems_evidence(),
        wiki_composition_evidence(),
        wiki_brct_evidence(),
        wiki_unknown_mechanism_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "gaps2_locus_restricts_phages",
            "title": "GAPS2 loci protect against P1-vir and lambda-vir",
            "description": (
                "Conservative system-level sketch linking GAPS2 locus "
                "possession to protection against P1-vir and lambda-vir."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures GAPS2 as a named single-profile "
                "DefenseFinder phage-defense system while leaving natural "
                "host breadth, the molecular activity of the BRCT-domain "
                "GAPS2 component, the phage trigger, and exact "
                "GAPS2__GAPS2 profile-to-protein correspondence unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gaps2_locus",
                    "label": "GAPS2 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A GMT-encoded phage-defense locus represented by "
                        "the GAPS2__GAPS2 DefenseFinder profile."
                    ),
                },
                {
                    "node_id": "gaps2_listed_phage_protection",
                    "label": "P1-vir and lambda-vir protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Protection against P1-vir and lambda-vir by GAPS2.",
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "GAPS2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded GAPS2 phage-defense "
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
                    "subject": "gaps2_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gaps2_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a "
                        "Vibrio parahaemolyticus GAPS2 locus from Mahata "
                        "et al. to protection against P1-vir and lambda-vir, "
                        "and DefenseFinder models GAPS2 through the "
                        "GAPS2__GAPS2 profile."
                    ),
                    "evidence": [
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "gaps2_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against P1-vir and lambda-vir realizes "
                        "the GAPS2 system trait."
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
                        "GAPS2 system possession is a phage-defense-system "
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
            "discussion_id": "gaps2-mechanism-gap",
            "prompt": (
                "Resolve GAPS2 natural host breadth, BRCT-domain activity, "
                "phage trigger specificity, and exact GAPS2__GAPS2 "
                "profile-to-protein correspondence before minting narrower "
                "GAPS2 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mahata et al. support GAPS2 as a GMT-encoded anti-phage "
                "defense system that protects E. coli against P1-vir and "
                "lambda-vir when expressed from a Vibrio parahaemolyticus "
                "locus, and DefenseFinder represents GAPS2 as a "
                "single-profile system. Natural host breadth, BRCT-domain "
                "activity, the phage trigger, and exact profile-to-protein "
                "correspondence remain unresolved."
            ),
            "evidence": [
                wiki_composition_evidence(),
                wiki_brct_evidence(),
                wiki_unknown_mechanism_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#gaps2_locus_restricts_phages"],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        }
    ],
}


def write_gaps2_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted GAPS2 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed GAPS2 system canonical_examples and left them empty "
            "because the current sources support a Vibrio parahaemolyticus "
            "accession-level experimental validation graph, a DefenseFinder "
            "system model, and a RefSeq Mannheimia sp. example, but not a "
            "direct native microbial isolate exemplar with experimentally "
            "verified endogenous GAPS2 activity. No paid research was used."
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
    if "GAPS2/GAPS6 boundaries" not in record["discussions"][0]["prompt"]:
        raise ValueError("GAPS1 sibling prompt no longer mentions GAPS2/GAPS6")
    return record


def update_gaps1_record(*, apply: bool) -> None:
    record = load_gaps1_record()
    graph = record["causal_graphs"][0]
    discussion = record["discussions"][0]
    graph["scope_notes"] = graph["scope_notes"].replace(
        "sibling GAPS2 or GAPS6 systems unresolved",
        "sibling GAPS6 systems unresolved",
    )
    discussion["prompt"] = discussion["prompt"].replace(
        "GAPS2/GAPS6 boundaries",
        "GAPS6 boundaries",
    )
    discussion["rationale"] = discussion["rationale"].replace(
        "sibling GAPS2 or GAPS6 system boundaries",
        "sibling GAPS6 system boundaries",
    )
    record_curation_event(
        record,
        action="UPDATED_DISCUSSION",
        changes=(
            "Narrowed stale GAPS1 sibling-boundary references to GAPS6 "
            "after GAPS2 was split into its own TraitRecord."
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
    write_gaps2_record(apply=apply)
    update_gaps1_record(apply=apply)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
