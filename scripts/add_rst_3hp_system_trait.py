#!/usr/bin/env python3
"""Add the Rst_3HP system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rst_3hp_system.yaml"

ROUSSET = "DOI:10.1016/j.chom.2022.02.018"

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
    "ee7647d8/content/3.defense-systems/rst_3hp.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-27T01:03:20Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T01:03:21Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000398"
PROPOSAL = "proposals/metpo_traitmech_v275"
SLUG = "rst_3hp"

ROUSSET_3HP_SNIPPET = (
    "The second system comprises three genes that have no clear predicted "
    "domain and protect against P1."
)
ROUSSET_FIGURE5_SNIPPET = (
    "Phage resistance heatmaps of the validated defense systems show the "
    "median fold resistance of three independent replicates against a "
    "panel of eight phages"
)
WIKI_DESCRIPTION_SNIPPET = (
    "The Rst_3HP system is composed of 3 proteins: Hp1, Hp2 and, Hp3. "
    "These proteins do not have clear predicted domains but they confer "
    "resistance against the phage P1 in *Escherichia coli* E1114 "
    ":ref{doi=10.1016/j.chom.2022.02.018}."
)
WIKI_MECHANISM_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown."
)
WIKI_STRUCTURE_SNIPPET = (
    "The Rst_3HP is composed of 3 proteins: Hp1, Hp2 and Hp3."
)
WIKI_REFSEQ_SNIPPET = (
    "The Rst_3HP system in *Aquitalea denitrificans* "
    "(GCF_009856625.1, NZ_CP047241) is composed of 3 proteins "
    "Hp1 (WP_159879082.1) Hp2 (WP_159879084.1) "
    "Hp3 (WP_159879086.1)"
)
WIKI_VALIDATION_SNIPPET = (
    "Rousset_2022[<a href='https://doi.org/10.1016/"
    "j.chom.2022.02.018'>Rousset et al., 2022</a>] --> Origin_0\n"
    "    Origin_0[Escherichia coli P2 loci \n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_000508501.1'>"
    "WP_000508501.1</a>, <a href='https://ncbi.nlm.nih.gov/protein/"
    "WP_112026686.1'>WP_112026686.1</a>,\n"
    "<a href='https://ncbi.nlm.nih.gov/protein/WP_000756244.1'>"
    "WP_000756244.1</a>] --> Expressed_0[Escherichia coli]\n"
    "    Expressed_0[Escherichia coli] ----> P1"
)
PROTECTS_SUBGRAPH_SNIPPET = "subgraph Title4[Protects against]\n        P1"
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_3HP | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_3HP\tRst_3HP\t3\t3\tRst_3HP__Hp1, Rst_3HP__Hp2, "
    "Rst_3HP__Hp3\t\t\t"
)
HMM_PROFILES = (
    ("Rst_3HP__Hp1", "67"),
    ("Rst_3HP__Hp2", "26"),
    ("Rst_3HP__Hp3", "20"),
)
HMM_SNIPPET = "\n".join(
    f"| {profile:<49}| {profile:<49}| {'Rst_3HP':<23}| "
    f"{'Custom':<24}| {ga_cut:<7}|"
    for profile, ga_cut in HMM_PROFILES
)


def rousset_3hp_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_3HP_SNIPPET,
        "notes": (
            "Rousset et al. experimentally describe the unnamed "
            "three-gene P2-hotspot system that DefenseFinder tracks as "
            "Rst_3HP."
        ),
    }


def rousset_figure5_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_FIGURE5_SNIPPET,
        "notes": (
            "The Figure 5 legend frames the cloned P2-hotspot hits, "
            "including the three-gene P1-restricting system, as validated "
            "defense systems in a replicated phage-resistance heatmap."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page names Rst_3HP as a "
            "three-protein system and links Hp1, Hp2, and Hp3 to P1 "
            "resistance in Escherichia coli E1114."
        ),
    }


def wiki_mechanism_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_MECHANISM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page leaves the Rst_3HP "
            "molecular mechanism unresolved."
        ),
    }


def wiki_structure_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_STRUCTURE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page describes Rst_3HP as a "
            "three-component Hp1/Hp2/Hp3 system."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted three-protein "
            "Rst_3HP locus in RefSeq assembly GCF_009856625.1 on NZ_CP047241."
        ),
    }


def wiki_validation_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_VALIDATION_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Rousset et al. to an Escherichia coli P2-locus source "
            "expressed in Escherichia coli against P1."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": PROTECTS_SUBGRAPH_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram lists P1 in "
            "the Rst_3HP protects-against subgraph."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Rst_3HP "
            "system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Rst_3HP as a "
            "three-profile system requiring Rst_3HP__Hp1, Rst_3HP__Hp2, "
            "and Rst_3HP__Hp3."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory records Hp1, Hp2, and Hp3 "
            "custom profiles under Rst_3HP."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst_3HP system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "three-protein Rst_3HP locus represented by DefenseFinder as a "
        "three-profile model requiring Rst_3HP__Hp1, Rst_3HP__Hp2, and "
        "Rst_3HP__Hp3 and experimentally linked to P1 protection when "
        "expressed in Escherichia coli."
    ),
    "definition_source": ROUSSET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Rst_3HP",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Rst_3HP__Hp1",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Rst_3HP__Hp2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Rst_3HP__Hp3",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        rousset_3hp_evidence(),
        rousset_figure5_evidence(),
        wiki_description_evidence(),
        wiki_mechanism_evidence(),
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
            "graph_id": "rst_3hp_locus_restricts_p1",
            "title": "Rst_3HP loci restrict P1 phage",
            "description": (
                "Conservative system-level sketch linking a named Rst_3HP "
                "three-gene locus model to P1 phage resistance."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Rst_3HP as a named DefenseFinder "
                "three-profile phage-defense system while leaving native "
                "host breadth, Hp1/Hp2/Hp3 molecular activities, "
                "profile-to-gene mapping, the direct phage trigger, and "
                "the P1 restriction mechanism unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_3hp_locus",
                    "label": "Rst_3HP locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A three-gene Hp1/Hp2/Hp3 phage-defense locus "
                        "represented by the custom DefenseFinder Rst_3HP "
                        "profiles."
                    ),
                },
                {
                    "node_id": "p1_phage_resistance",
                    "label": "P1 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Resistance against phage P1 in a host expressing "
                        "an Rst_3HP locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst_3HP system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Rst_3HP "
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
                    "subject": "rst_3hp_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "p1_phage_resistance",
                    "description": (
                        "Rousset et al. linked a cloned three-gene "
                        "P2-hotspot system to P1 protection, and "
                        "DefenseFinder models Rst_3HP as a three-profile "
                        "Hp1/Hp2/Hp3 system."
                    ),
                    "evidence": [
                        rousset_3hp_evidence(),
                        wiki_description_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "p1_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Rst_3HP-linked P1 resistance realizes the Rst_3HP "
                        "system trait."
                    ),
                    "evidence": [
                        rousset_3hp_evidence(),
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
                        "Rst_3HP system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        rousset_figure5_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "rst-3hp-host-mechanism-gap",
            "prompt": (
                "Resolve Rst_3HP native host breadth, Hp1/Hp2/Hp3 "
                "molecular activities, profile-to-gene mapping, and the "
                "mechanism of P1 restriction before minting narrower "
                "Rst_3HP mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support a three-gene P2-hotspot system "
                "with no clear predicted domains that protects against P1, "
                "and DefenseFinder represents Rst_3HP as a required "
                "Hp1/Hp2/Hp3 three-profile model. This first system-level "
                "record leaves native host breadth, profile-to-gene "
                "mapping, the molecular activities of Hp1, Hp2, and Hp3, "
                "and the P1 restriction mechanism unresolved."
            ),
            "evidence": [
                rousset_3hp_evidence(),
                wiki_mechanism_evidence(),
                wiki_structure_evidence(),
                rules_evidence(),
            ],
            "attaches_to": ["causal_graphs#rst_3hp_locus_restricts_p1"],
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
            "Minted Rst_3HP system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
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
            "Reviewed Rst_3HP during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support a cloned P2-hotspot Hp1/Hp2/Hp3 locus assayed "
            "in Escherichia coli and a DefenseFinder RefSeq model example, "
            "but not a direct native microbial isolate exemplar with "
            "experimentally verified Rst_3HP activity. No paid research was "
            "used."
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
