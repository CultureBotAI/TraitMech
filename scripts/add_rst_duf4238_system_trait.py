#!/usr/bin/env python3
"""Add the Rst_DUF4238 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rst_duf4238_system.yaml"

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
    "ee7647d8/content/3.defense-systems/rst_duf4238.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-26T07:22:10Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-26T07:32:10Z"
POSED_DATE = "2026-09-26"
IDENTIFIER = "traitmech:000374"
PROPOSAL = "proposals/metpo_traitmech_v251"
SLUG = "rst_duf4238"

DUF4238_VALIDATION_SNIPPET = (
    "The first system consists of a single protein with a DUF4238 domain "
    "(whose molecular function is currently unknown) that provides strong "
    "resistance against T7."
)
FIGURE5_SNIPPET = (
    "Phage resistance heatmaps of the validated defense systems show the "
    "median fold resistance of three independent replicates against a "
    "panel of eight phages"
)
WIKI_DESCRIPTION_SNIPPET = (
    "Rst_DUF4238 is a single gene system found in a screen of phage and "
    "phage-satellites antiviral hotspots :ref{doi=10.1016/j.chom.2022.02.018}. "
    "It was shown to provide *E.coli* with a strong resistance against phage T7."
)
WIKI_MECHANISM_SNIPPET = (
    "As far as we are aware, the molecular mechanism is unknown."
)
WIKI_STRUCTURE_SNIPPET = "The Rst_DUF4238 is composed of 1 protein: DUF4238."
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_DUF4238 | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_DUF4238\tRst_DUF4238\t1\t1\t"
    "Rst_DUF4238__DUF4238_Pers\t\t\t"
)
HMM_PROFILE = "Rst_DUF4238__DUF4238_Pers"
HMM_SYSTEM = "Rst_DUF4238"
HMM_GA_CUT = "100"


def rousset_validation_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": DUF4238_VALIDATION_SNIPPET,
        "notes": (
            "Rousset et al. describe the one-protein DUF4238 candidate from "
            "the P2-encoded hotspot and connect it to strong T7 resistance."
        ),
    }


def rousset_figure5_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": FIGURE5_SNIPPET,
        "notes": (
            "The Figure 5 legend frames the cloned P2-hotspot hits, "
            "including the DUF4238 system, as validated defense systems in "
            "a replicated phage-resistance heatmap."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page names Rst_DUF4238 as a "
            "single-gene system and links it to strong T7 resistance."
        ),
    }


def wiki_mechanism_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_MECHANISM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page leaves the Rst_DUF4238 "
            "molecular mechanism unresolved."
        ),
    }


def wiki_structure_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_STRUCTURE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page describes Rst_DUF4238 as a "
            "one-component DUF4238 system."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Rst_DUF4238 "
            "system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Rst_DUF4238 as a "
            "single-profile system requiring Rst_DUF4238__DUF4238_Pers."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            f"| {HMM_PROFILE:<49}| {HMM_PROFILE:<49}| "
            f"{HMM_SYSTEM:<23}| {'Custom':<24}| {HMM_GA_CUT:<7}|"
        ),
        "notes": (
            "The DefenseFinder HMM inventory records "
            "Rst_DUF4238__DUF4238_Pers under Rst_DUF4238."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst_DUF4238 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "single-gene Rst_DUF4238 locus represented by DefenseFinder as an "
        "Rst_DUF4238__DUF4238_Pers single-profile model and "
        "experimentally linked to strong resistance against phage T7."
    ),
    "definition_source": ROUSSET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Rst_DUF4238",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": HMM_PROFILE,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DUF4238_Pers",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
    ],
    "evidence": [
        rousset_validation_evidence(),
        rousset_figure5_evidence(),
        wiki_description_evidence(),
        wiki_mechanism_evidence(),
        wiki_structure_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rst_duf4238_locus_restricts_t7",
            "title": "Rst_DUF4238 loci restrict T7 phage",
            "description": (
                "Conservative system-level sketch linking the named "
                "Rst_DUF4238 single-gene locus model to strong T7 phage "
                "resistance."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Rst_DUF4238 as a named DefenseFinder "
                "single-profile phage-defense system while leaving native "
                "host breadth, the molecular activity of the DUF4238 "
                "component, exact DUF4238_Pers profile grounding, and the "
                "mechanism of T7 restriction unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_duf4238_locus",
                    "label": "Rst_DUF4238 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene DUF4238 phage-defense locus "
                        "represented by the custom DefenseFinder "
                        "Rst_DUF4238__DUF4238_Pers profile."
                    ),
                },
                {
                    "node_id": "t7_phage_resistance",
                    "label": "T7 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Strong resistance against phage T7 in a host "
                        "expressing an Rst_DUF4238 locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst_DUF4238 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Rst_DUF4238 "
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
                    "subject": "rst_duf4238_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t7_phage_resistance",
                    "description": (
                        "Rousset et al. linked a cloned one-protein "
                        "DUF4238 locus to strong T7 resistance, and "
                        "DefenseFinder models Rst_DUF4238 as a "
                        "single-profile DUF4238_Pers system."
                    ),
                    "evidence": [
                        rousset_validation_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "t7_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Strong T7 resistance realizes the Rst_DUF4238 "
                        "system trait."
                    ),
                    "evidence": [
                        rousset_validation_evidence(),
                        wiki_description_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Rst_DUF4238 system possession is a "
                        "phage-defense-system trait."
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
            "discussion_id": "rst-duf4238-host-mechanism-gap",
            "prompt": (
                "Resolve Rst_DUF4238 native host breadth, accession-level "
                "DUF4238 proteins, and the molecular mechanism of T7 "
                "restriction before minting narrower Rst_DUF4238 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support a one-protein DUF4238 P2-hotspot "
                "system that provides strong T7 resistance when expressed "
                "in Escherichia coli, and DefenseFinder represents "
                "Rst_DUF4238 as a single-profile Rst_DUF4238__DUF4238_Pers "
                "model. This first system-level record leaves native host "
                "breadth, accession-level component grounding, the "
                "profile-to-activity mapping, and the T7 restriction "
                "mechanism unresolved."
            ),
            "evidence": [
                rousset_validation_evidence(),
                wiki_mechanism_evidence(),
                wiki_structure_evidence(),
                rules_evidence(),
            ],
            "attaches_to": ["causal_graphs#rst_duf4238_locus_restricts_t7"],
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
            "Minted Rst_DUF4238 system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an "
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
            "Reviewed Rst_DUF4238 during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support a cloned P2-hotspot DUF4238 locus assayed in "
            "Escherichia coli and a DefenseFinder RefSeq model example, "
            "but not a direct native host exemplar with experimental "
            "Rst_DUF4238 activity. No paid research was used."
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
