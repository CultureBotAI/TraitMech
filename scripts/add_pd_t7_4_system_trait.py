#!/usr/bin/env python3
"""Add the PD-T7-4 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_t7_4_system.yaml"

VASSALLO = "DOI:10.1038/s41564-022-01219-4"

DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/ee7647d8/"
    "content/3.defense-systems/pd-t7-4.md"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T08:45:27Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T08:45:28Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000406"
PROPOSAL = "proposals/metpo_traitmech_v283"
SLUG = "pd_t7_4"
PROFILE = "PD-T7-4__PD-T7-4"
PHAGE_LIST = "SECphi18, SECphi27, T3, and T7"

VASSALLO_ABSTRACT_SNIPPET = (
    "Here we developed an experimental selection scheme agnostic to genomic "
    "context to identify defence systems in 71 diverse E. coli strains. Our "
    "results unveil 21 conserved defence systems, none of which were "
    "previously detected as enriched in defence islands."
)
WIKI_UNKNOWN_ANNOTATION_SNIPPET = (
    "Sensor: Unknown\n"
    "    Activator: Unknown\n"
    "    Effector: Unknown\n"
    "    PFAM: PF13643"
)
WIKI_COMPOSITION_SNIPPET = "The PD-T7-4 is composed of 1 protein: PD-T7-4."
SALINIBACTERIUM_EXAMPLE_SNIPPET = (
    "The PD-T7-4 system in *Salinibacterium hongtaonis* "
    "(GCF_003065485.1, NZ_CP026951) is composed of 1 protein: "
    "PD-T7-4 (WP_108515598.1)"
)
EXPERIMENTAL_GRAPH_SNIPPET = (
    "Vassallo_2022[<a href='https://doi.org/10.1038/"
    "s41564-022-01219-4'>Vassallo et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/RRL46918.1'>"
    "RRL46918.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> SECphi18 & SECphi27 & T3 & T7"
)
PROTECTS_SUBGRAPH_SNIPPET = (
    "subgraph Title4[Protects against]\n"
    "        SECphi18\n"
    "        SECphi27\n"
    "        T3\n"
    "        T7"
)
RULES_SNIPPET = "PD-T7-4\tPD-T7-4\t1\t1\tPD-T7-4__PD-T7-4\t\t\t"
HMM_ROW = (
    "| PD-T7-4__PD-T7-4                                 | "
    "PD-T7-4__PD-T7-4                                 | "
    "PD-T7-4                | Custom                  | 100    |"
)


def evidence(reference: str, snippet: str, notes: str) -> dict[str, str]:
    return {
        "reference": reference,
        "snippet": snippet,
        "notes": notes,
    }


def vassallo_screen_evidence() -> dict[str, str]:
    return evidence(
        VASSALLO,
        VASSALLO_ABSTRACT_SNIPPET,
        (
            "Vassallo et al. developed the agnostic E. coli pangenome "
            "selection that uncovered PD-T7-4 and related conserved "
            "phage-defense systems."
        ),
    )


def wiki_unknown_annotation_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_WIKI,
        WIKI_UNKNOWN_ANNOTATION_SNIPPET,
        (
            "The pinned DefenseFinder PD-T7-4 page has no sensor, "
            "activator, or effector annotation for PD-T7-4 and lists "
            "PF13643 as the associated Pfam profile."
        ),
    )


def wiki_composition_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_WIKI,
        WIKI_COMPOSITION_SNIPPET,
        "The DefenseFinder wiki names PD-T7-4 as a single-protein system.",
    )


def wiki_refseq_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_WIKI,
        SALINIBACTERIUM_EXAMPLE_SNIPPET,
        (
            "The DefenseFinder wiki illustrates a predicted one-protein "
            "PD-T7-4 locus in RefSeq assembly GCF_003065485.1 on "
            "NZ_CP026951."
        ),
    )


def wiki_validation_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_WIKI,
        EXPERIMENTAL_GRAPH_SNIPPET,
        (
            "The DefenseFinder experimental-validation diagram links "
            "Vassallo et al. to an E. coli PD-T7-4 source locus expressed "
            f"in E. coli against {PHAGE_LIST}."
        ),
    )


def wiki_protects_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_WIKI,
        PROTECTS_SUBGRAPH_SNIPPET,
        (
            "The DefenseFinder experimental-validation diagram lists "
            f"{PHAGE_LIST} in the PD-T7-4 protects-against subgraph."
        ),
    )


def rules_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_RULES,
        RULES_SNIPPET,
        (
            "The DefenseFinder rules table models PD-T7-4 as a "
            "single-profile system requiring PD-T7-4__PD-T7-4."
        ),
    )


def hmm_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_HMMS,
        HMM_ROW,
        (
            "The DefenseFinder HMM inventory records PD-T7-4__PD-T7-4 "
            "under the PD-T7-4 system namespace."
        ),
    )


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-T7-4 system",
    "definition": (
        "A phage defense system in which an organism possesses a PD-T7-4 "
        "locus represented by DefenseFinder as a single-profile model, "
        "PD-T7-4__PD-T7-4, and experimentally linked to protection "
        f"against {PHAGE_LIST} when expressed in E. coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-T7-4",
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
        wiki_unknown_annotation_evidence(),
        wiki_composition_evidence(),
        wiki_refseq_evidence(),
        wiki_validation_evidence(),
        wiki_protects_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_t7_4_locus_restricts_phages",
            "title": "PD-T7-4 loci restrict SECphi18, SECphi27, T3, and T7",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PD-T7-4 locus to protection against SECphi18, SECphi27, "
                "T3, and T7."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-T7-4 as a named DefenseFinder "
                "phage-defense system while leaving natural host breadth, "
                "the direct phage trigger, and the PF13643-associated "
                "effector mechanism unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_t7_4_locus",
                    "label": "PD-T7-4 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A phage-defense locus represented by the PD-T7-4 "
                        "DefenseFinder profile."
                    ),
                },
                {
                    "node_id": "pd_t7_4_listed_phage_protection",
                    "label": "SECphi18, SECphi27, T3, and T7 protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against SECphi18, SECphi27, T3, and "
                        "T7 by PD-T7-4."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PD-T7-4 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-T7-4 "
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
                    "subject": "pd_t7_4_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_t7_4_listed_phage_protection",
                    "description": (
                        "The DefenseFinder wiki links a PD-T7-4 locus from "
                        "Vassallo et al. to protection against SECphi18, "
                        "SECphi27, T3, and T7, and DefenseFinder models "
                        "PD-T7-4 through one mandatory profile."
                    ),
                    "evidence": [
                        wiki_unknown_annotation_evidence(),
                        wiki_composition_evidence(),
                        wiki_validation_evidence(),
                        wiki_protects_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "pd_t7_4_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Protection against SECphi18, SECphi27, T3, and "
                        "T7 realizes the PD-T7-4 system trait."
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
                        "PD-T7-4 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        vassallo_screen_evidence(),
                        wiki_composition_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pd-t7-4-mechanism-gap",
            "prompt": (
                "Resolve PD-T7-4 natural host breadth, direct phage trigger, "
                "and PF13643-associated effector mechanism before minting "
                "narrower PD-T7-4 mechanism traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vassallo et al. support PD-T7-4 as one of the conserved "
                "systems from an E. coli pangenome phage-defense selection, "
                "the DefenseFinder wiki maps the source locus to protection "
                f"against {PHAGE_LIST}, and DefenseFinder represents the "
                "system with one profile. Natural host breadth, the direct "
                "phage trigger, and effector logic remain unresolved."
            ),
            "evidence": [
                vassallo_screen_evidence(),
                wiki_unknown_annotation_evidence(),
                wiki_validation_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#pd_t7_4_locus_restricts_phages"],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        },
        {
            "discussion_id": "pd-t7-4-defensefinder-article-registry-gap",
            "prompt": (
                "Recheck whether DefenseFinder adds a PD-T7-4 "
                "List_system_article.md row before using the article "
                "registry as direct PD-T7-4 model-to-paper evidence."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned DefenseFinder wiki, rules table, and HMM "
                "inventory all represent PD-T7-4, but the pinned "
                "List_system_article.md registry omits a PD-T7-4 row. The "
                "PD-T7-4 record therefore cites the pinned wiki plus the "
                "DOI-backed Vassallo et al. screen instead of inventing a "
                "missing article-registry entry."
            ),
            "evidence": [
                wiki_composition_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        },
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted PD-T7-4 system as a DOI- and DefenseFinder-backed "
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
            "Reviewed PD-T7-4 system canonical_examples and left them empty "
            "because the current sources support an E. coli accession-level "
            "experimental validation graph, a DefenseFinder system model, "
            "and a RefSeq Salinibacterium hongtaonis example, but not a "
            "direct native microbial isolate exemplar with experimentally "
            "verified endogenous PD-T7-4 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    if apply:
        if TARGET.exists():
            raise FileExistsError(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        return

    with tempfile.TemporaryDirectory() as tmp:
        check_path = Path(tmp) / TARGET.name
        write_validated_trait(record, check_path)
        if TARGET.exists():
            if check_path.read_bytes() != TARGET.read_bytes():
                raise SystemExit(
                    f"{TARGET.relative_to(REPO_ROOT)} differs from generated output"
                )
            print(f"{TARGET.relative_to(REPO_ROOT)} matches generated output")
        else:
            print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
