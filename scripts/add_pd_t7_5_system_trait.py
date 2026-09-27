#!/usr/bin/env python3
"""Add the PD-T7-5 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_t7_5_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-t7-5.md"
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
TIMESTAMP = "2026-09-27T00:29:55Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T00:29:56Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000397"
PROPOSAL = "proposals/metpo_traitmech_v274"
SLUG = "pd_t7_5"
PROFILE = "PD-T7-5__PD-T7-5"
PHAGE_LIST = "SECphi17, T3, and T7"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_DESCRIPTION_SNIPPET = (
    "PD-T7-5 is a defense system composed of a single protein which was "
    "discovered in :ref{doi=10.1038/s41564-022-01219-4}. Its antiphage "
    "activity was assessed by heterologous expression in *E. coli* against "
    "T7 and to reduce the size of lysis plaques of T3 "
    ":ref{doi=10.1038/s41564-022-01219-4}. PD-T7-5 contains a PD(D/E)XK "
    "nuclease domain like [PD-T7-1](/defense-systems/pd-t7-1)."
)
WIKI_MECHANISM_GAP_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown. However, "
    "the presence of a PD(D/E)XK domain in PD-T7-5 suggests a mechanism of "
    "action via DNA degradation :ref{doi=10.1038/s41564-022-01219-4}."
)
WIKI_COMPOSITION_SNIPPET = (
    "The PD-T7-5 system is composed of one protein: PD-T7-5."
)
SHEWANELLA_EXAMPLE_SNIPPET = (
    "The PD-T7-5 system in *Shewanella putrefaciens* "
    "(GCF_019599085.1, NZ_CP080633) is composed of 1 protein: "
    "PD-T7-5 (WP_220590848.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RRM82777.1'>"
    "RRM82777.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> SECphi17 & T3 & T7"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        SECphi17\n"
    "        T3\n"
    "        T7"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-T7-5 | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the "
    "landscape of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = "PD-T7-5\tPD-T7-5\t1\t1\tPD-T7-5__PD-T7-5\t\t\t"
HMM_ROW = (
    "| PD-T7-5__PD-T7-5                                 | "
    "PD-T7-5__PD-T7-5                                 | "
    "PD-T7-5                | Custom                  | 90     |"
)


def vassallo_screen_evidence() -> dict[str, str]:
    return {
        "reference": VASSALLO,
        "snippet": VASSALLO_ABSTRACT_SNIPPET,
        "notes": (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-T7-5 and related conserved "
            "phage-defense systems."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki describes PD-T7-5 as a single-protein "
            "defense system with heterologous E. coli antiphage activity "
            "against T7 and T3 plaque-size reduction."
        ),
    }


def wiki_mechanism_gap_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_MECHANISM_GAP_SNIPPET,
        "notes": (
            "The DefenseFinder wiki states that PD-T7-5 molecular mechanism "
            "is unresolved and leaves the PD(D/E)XK-mediated DNA degradation "
            "interpretation as a hypothesis."
        ),
    }


def wiki_composition_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names PD-T7-5 as a single-protein system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": SHEWANELLA_EXAMPLE_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted one-protein "
            "PD-T7-5 locus in RefSeq assembly GCF_019599085.1 on NZ_CP080633."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": EXPERIMENTAL_GRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-T7-5 source locus expressed "
            f"in E. coli against {PHAGE_LIST}."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists "
            f"{PHAGE_LIST} in the PD-T7-5 protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PD-T7-5 "
            "system to the Vassallo et al. E. coli pangenome "
            "phage-defense preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PD-T7-5 as a "
            "single-profile system requiring PD-T7-5__PD-T7-5."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records PD-T7-5__PD-T7-5 "
            "under the PD-T7-5 system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-T7-5 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "PD-T7-5 locus represented by DefenseFinder as a single-profile "
        "model, PD-T7-5__PD-T7-5, and experimentally linked to "
        f"{PHAGE_LIST} protection when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-T7-5",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        {
            "synonym_text": PROFILE,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        vassallo_screen_evidence(),
        wiki_description_evidence(),
        wiki_mechanism_gap_evidence(),
        wiki_composition_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_t7_5_locus_restricts_phages",
            "title": "PD-T7-5 loci restrict SECphi17, T3, and T7",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PD-T7-5 locus to protection against SECphi17, T3, and T7."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-T7-5 as a named DefenseFinder "
                "phage-defense system while leaving natural host breadth, "
                "the direct phage trigger, and the PD(D/E)XK effector "
                "mechanism unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_t7_5_locus",
                    "label": "PD-T7-5 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the "
                        "PD-T7-5 DefenseFinder profile."
                    ),
                },
                {
                    "node_id": "pd_t7_5_listed_phage_protection",
                    "label": "SECphi17, T3, and T7 protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against SECphi17, T3, and T7 by PD-T7-5."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-T7-5 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-T7-5 "
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
                    "subject": "pd_t7_5_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_t7_5_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-T7-5 locus "
                        "from Vassallo et al. to protection against "
                        "SECphi17, T3, and T7, and DefenseFinder models "
                        "PD-T7-5 through one mandatory profile."
                    ),
                    "evidence": [
                        wiki_description_evidence(),
                        wiki_mechanism_gap_evidence(),
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "pd_t7_5_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against SECphi17, T3, and T7 realizes "
                        "the PD-T7-5 system trait."
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
                        "PD-T7-5 system possession is a "
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
            "discussion_id": "pd-t7-5-mechanism-gap",
            "prompt": (
                "Resolve PD-T7-5 natural host breadth, direct phage "
                "trigger, and PD(D/E)XK effector mechanism before minting "
                "narrower PD-T7-5 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-T7-5 as one of the conserved "
                "systems from an E. coli pangenome phage-defense selection, "
                "the DefenseFinder wiki maps the source locus to protection "
                "against SECphi17, T3, and T7, and DefenseFinder represents "
                "the system with one profile. Natural host breadth, the "
                "direct phage trigger, and the PD(D/E)XK effector mechanism "
                "remain unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_description_evidence(),
                wiki_mechanism_gap_evidence(),
                wiki_composition_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#pd_t7_5_locus_restricts_phages"],
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
            "Minted PD-T7-5 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed PD-T7-5 system canonical_examples and left them empty "
            "because the current sources support an E. coli accession-level "
            "experimental validation graph, a DefenseFinder system model, "
            "and a RefSeq Shewanella putrefaciens example, but not a direct "
            "native microbial isolate exemplar with experimentally verified "
            "endogenous PD-T7-5 activity. No paid research was used."
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
