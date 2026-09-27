#!/usr/bin/env python3
"""Add the Old exonuclease system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "old_exonuclease_system.yaml"

OLD_NUCLEASE = "DOI:10.1128/jb.177.3.497-501.1995"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/"
    "ee7647d8/content/3.defense-systems/old_exonuclease.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-27T01:44:29Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T01:44:30Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000399"
PROPOSAL = "proposals/metpo_traitmech_v276"
SLUG = "old_exonuclease"
PROFILE = "Old_exonuclease__Old_exonuclease"

OLD_ABSTRACT_SNIPPET = (
    "The Old protein of bacteriophage P2 is responsible for interference "
    "with the growth of phage lambda and for killing of recBC mutant "
    "Escherichia coli."
)
OLD_NUCLEASE_SNIPPET = (
    "The Old protein fused to maltose-binding protein has exonuclease "
    "activity on double-stranded DNA as well as nuclease activity on "
    "single-stranded DNA and RNA."
)
WIKI_DESCRIPTION_SNIPPET = (
    "It's been shown to protect against phage lambda "
    ":ref{doi=10.1128/jb.177.3.497-501.1995}, and when cloned with the "
    "P2 Tin accessory gene, it was shown to protect against other "
    "*E. coli* phages :ref{doi=10.1016/j.chom.2022.02.018}."
)
WIKI_MECHANISM_SNIPPET = (
    "The old_exonuclease is dsDNA exonuclease that digests in the 5' to "
    "3' direction :ref{doi=10.1128/jb.177.3.497-501.1995}. To our "
    "knowledge, other aspects of the molecular mechanisms remain unknown."
)
WIKI_STRUCTURE_SNIPPET = (
    "The Old_exonuclease is composed of 1 protein: Old_exonuclease."
)
WIKI_REFSEQ_SNIPPET = (
    "The Old_exonuclease system in *Shewanella xiamenensis* "
    "(GCF_022453805.1, NZ_CP092630) is composed of 1 protein: "
    "Old_exonuclease (WP_240293412.1)"
)
WIKI_VALIDATION_SNIPPET = (
    "Rousset_2022[<a href='https://doi.org/10.1016/"
    "j.chom.2022.02.018'>Rousset et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Enterobacteria phage P2 \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/NP_046798.1'>"
    "NP_046798.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> Lambda & T4 & LF82_P8 & "
    "Al505_P2"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        Lambda\n"
    "        T4\n"
    "        LF82_P8\n"
    "        Al505_P2"
)
ARTICLE_REGISTRY_SNIPPET = (
    "Old_exonuclease | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Old_exonuclease\tOld_exonuclease\t1\t1\t"
    "Old_exonuclease__Old_exonuclease\t\t\t"
)
HMM_ROW = (
    "| Old_exonuclease__Old_exonuclease                 | "
    "Old_exonuclease__Old_exonuclease                 | "
    "Old_exonuclease        | Custom                  | 200    |"
)


def old_lambda_evidence() -> dict[str, str]:
    return {
        "reference": OLD_NUCLEASE,
        "snippet": OLD_ABSTRACT_SNIPPET,
        "notes": (
            "The 1995 Old nuclease study identifies the P2 Old protein as "
            "responsible for phage-lambda interference."
        ),
    }


def old_nuclease_evidence() -> dict[str, str]:
    return {
        "reference": OLD_NUCLEASE,
        "snippet": OLD_NUCLEASE_SNIPPET,
        "notes": (
            "The 1995 biochemical study shows Old has nuclease activity on "
            "double-stranded DNA, single-stranded DNA, and RNA."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page links Old_exonuclease to "
            "lambda protection and to broader P2 Old plus Tin protection."
        ),
    }


def wiki_mechanism_gap_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_MECHANISM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page supports Old dsDNA "
            "exonuclease activity while leaving the remaining molecular "
            "mechanism unresolved."
        ),
    }


def wiki_structure_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_STRUCTURE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page describes Old_exonuclease "
            "as a one-protein system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page illustrates a predicted "
            "Old_exonuclease locus in RefSeq assembly GCF_022453805.1 on "
            "NZ_CP092630."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Rousset et al. to Enterobacteria phage P2 Old expressed in "
            "Escherichia coli against lambda, T4, LF82_P8, and Al505_P2."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            "lambda, T4, LF82_P8, and Al505_P2 in the Old_exonuclease "
            "protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named "
            "Old_exonuclease system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Old_exonuclease as a "
            "single-profile system requiring Old_exonuclease__Old_exonuclease."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records "
            "Old_exonuclease__Old_exonuclease under the Old_exonuclease "
            "system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Old exonuclease system",
    "definition": (
        "A phage defense system in which an organism possesses an Old "
        "exonuclease locus represented by DefenseFinder as a single-profile "
        "model, Old_exonuclease__Old_exonuclease, and experimentally linked "
        "to interference with phage lambda by the bacteriophage P2 Old "
        "protein."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Old_exonuclease",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": PROFILE,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        old_lambda_evidence(),
        old_nuclease_evidence(),
        wiki_description_evidence(),
        wiki_mechanism_gap_evidence(),
        wiki_structure_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "old_exonuclease_locus_interferes_with_lambda",
            "title": "Old exonuclease loci interfere with phage lambda",
            "description": (
                "Conservative system-level sketch linking a named "
                "Old_exonuclease one-profile model to phage-lambda "
                "interference."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Old_exonuclease as a named "
                "DefenseFinder single-profile phage-defense system while "
                "leaving natural host breadth, Tin accessory dependence, "
                "RecBCD-triggered activation, profile-to-protein mapping, "
                "and the lambda interference mechanism unresolved."
            ),
            "nodes": [
                {
                    "node_id": "old_exonuclease_locus",
                    "label": "Old exonuclease locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-profile Old-exonuclease phage-defense "
                        "locus represented by the custom DefenseFinder "
                        "Old_exonuclease profile."
                    ),
                },
                {
                    "node_id": "lambda_phage_interference",
                    "label": "lambda phage interference",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Interference with growth of phage lambda in a host "
                        "expressing bacteriophage P2 Old."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Old exonuclease system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Old exonuclease "
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
                    "subject": "old_exonuclease_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "lambda_phage_interference",
                    "description": (
                        "The P2 Old protein is linked to phage-lambda "
                        "interference, and DefenseFinder models "
                        "Old_exonuclease as a single-profile system."
                    ),
                    "evidence": [
                        old_lambda_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "lambda_phage_interference",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Old-mediated phage-lambda interference realizes "
                        "the Old exonuclease system trait."
                    ),
                    "evidence": [
                        old_lambda_evidence(),
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
                        "Old exonuclease system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        wiki_description_evidence(),
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "old-exonuclease-tin-trigger-mechanism-gap",
            "prompt": (
                "Resolve Old_exonuclease natural host breadth, Tin "
                "accessory dependence, RecBCD-triggered activation, "
                "profile-to-protein mapping, and lambda interference "
                "mechanism before minting narrower Old nuclease mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The 1995 P2 Old paper supports Old nuclease activity and "
                "phage-lambda interference, and DefenseFinder represents "
                "Old_exonuclease as a required single-profile model. This "
                "first system-level record leaves Tin dependence in the "
                "Rousset et al. assay, natural host breadth, RecBCD-linked "
                "activation, profile-to-protein mapping, and the exact "
                "phage-interference mechanism unresolved."
            ),
            "evidence": [
                old_lambda_evidence(),
                old_nuclease_evidence(),
                wiki_mechanism_gap_evidence(),
                wiki_structure_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#old_exonuclease_locus_interferes_with_lambda"
            ],
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
            "Minted Old exonuclease system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under phage defense "
            "system after an ignored-and-hidden duplicate review found no "
            "exact live TraitMech, METPO, history, or prior proposal record; "
            f"the replacement placeholder is reserved in {PROPOSAL}."
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
            "Reviewed Old exonuclease system during canonical-example "
            "issue 444 enforcement and left canonical_examples empty "
            "because the sources support a bacteriophage P2 Old protein, "
            "a heterologous Old plus Tin protection assay in Escherichia "
            "coli, and a DefenseFinder RefSeq model example, but not a "
            "direct native microbial isolate exemplar with experimentally "
            "verified Old_exonuclease activity. No paid research was used."
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
