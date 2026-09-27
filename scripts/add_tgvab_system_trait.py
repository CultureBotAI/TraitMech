#!/usr/bin/env python3
"""Add the TgvAB system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "tgvab_system.yaml"

VIZZARRO = "DOI:10.1128/jb.00145-24"
GOMEZ = "DOI:10.1128/jb.00143-24"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T16:50:26Z"
IDENTIFIER = "traitmech:000412"
PROPOSAL = "proposals/metpo_traitmech_v289"

ARTICLE_ROW = (
    "| TgvAB | 10\\.1128/jb\\.00145-24 | Vibrio cholerae pathogenicity "
    "island 2 encodes two distinct types of restriction systems |"
)
HMM_ROWS = {
    "TgvAB__TgvA": (
        "| TgvAB__TgvA                                      | "
        "                                                  | TgvAB                  | "
        "Custom                  | 200    |"
    ),
    "TgvAB__TgvB": (
        "| TgvAB__TgvB                                      | "
        "                                                  | TgvAB                  | "
        "Custom                  | 400    |"
    ),
}
TGVAB_EMBEDDED_SNIPPET = (
    "the two genes embedded within the T1RM system encode a novel two-protein "
    "modification-dependent restriction system related to the GmrSD family of "
    "type IV restriction enzymes"
)
TEVENVIRINAE_SNIPPET = (
    "potent anti-phage activity against diverse members of the Tevenvirinae"
)
TYPE_IV_CYTOSINES_SNIPPET = (
    "novel modification-dependent type IV restriction system that recognizes "
    "hypermodified cytosines"
)
BOTH_COMPONENTS_SNIPPET = (
    "both TgvA and TgvB are required for defense against T2, T4, and T6"
)
GLUCOSYLATED_HMC_SNIPPET = (
    "TgvAB targets phage DNA with glucosylated 5-hydroxymethylcytosine "
    "(5hmC) bases"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the named TgvAB "
            "system to the Vizzarro et al. VPI-2 restriction-systems paper. "
            f"The pinned rules table ({DEFENSEFINDER_RULES}) does not list "
            "TgvAB, so the registry and HMM rows support a named "
            "system-possession trait rather than complete DefenseFinder "
            "detection criteria."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom TgvAB profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "TgvAB system",
    "definition": (
        "A restriction-modification system in which an organism possesses a "
        "two-gene TgvAB locus embedded in the Vibrio cholerae VPI-2 type I "
        "R-M cluster, encoding TgvA and TgvB modification-dependent "
        "restriction proteins related to GmrSD type IV restriction enzymes "
        "that restrict glucosylated hmC-containing T-even-like phage DNA."
    ),
    "definition_source": VIZZARRO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000095"],
    "synonyms": [
        {
            "synonym_text": "TgvAB",
            "synonym_type": "EXACT_SYNONYM",
            "source": VIZZARRO,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_ROWS
        ],
    ],
    "evidence": [
        {
            "reference": VIZZARRO,
            "snippet": TGVAB_EMBEDDED_SNIPPET,
            "notes": (
                "Vizzarro et al. define TgvAB as a modification-dependent "
                "restriction system related to GmrSD-family type IV "
                "restriction enzymes."
            ),
        },
        {
            "reference": VIZZARRO,
            "snippet": TEVENVIRINAE_SNIPPET,
            "notes": (
                "Vizzarro et al. support TgvAB anti-phage activity against "
                "phages with hypermodified genomes."
            ),
        },
        {
            "reference": GOMEZ,
            "snippet": BOTH_COMPONENTS_SNIPPET,
            "notes": (
                "Gomez and Waters independently report that both TgvA and "
                "TgvB are required for TgvAB-mediated anti-phage activity."
            ),
        },
        {
            "reference": GOMEZ,
            "snippet": GLUCOSYLATED_HMC_SNIPPET,
            "notes": (
                "Gomez and Waters support TgvAB as a type IV restriction "
                "system targeting glucosylated 5-hydroxymethylcytosine in "
                "T-even phage genomes."
            ),
        },
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "tgvab_type_iv_restriction",
            "title": "TgvAB restricts glucosylated T-even-like phage DNA",
            "description": (
                "Conservative system-level sketch linking a two-gene TgvAB "
                "locus to modification-dependent type IV restriction of "
                "glucosylated hmC-containing T-even-like phage DNA and TgvAB "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures TgvAB at VPI-2, T-even-like-phage, and "
                "type-IV-restriction level without asserting complete native "
                "host breadth, exact TgvA/TgvB subunit stoichiometry, or a "
                "DefenseFinder rule-level profile combination."
            ),
            "nodes": [
                {
                    "node_id": "tgvab_locus",
                    "label": "TgvAB locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene locus encoding TgvA and TgvB "
                        "GmrSD-related modification-dependent restriction "
                        "proteins."
                    ),
                },
                {
                    "node_id": "glucosylated_hmc_phage_dna",
                    "label": "glucosylated hmC phage DNA",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "T-even-like bacteriophage DNA carrying glucosylated "
                        "5-hydroxymethylcytosine modifications."
                    ),
                },
                {
                    "node_id": "tgvab_dependent_type_iv_restriction",
                    "label": "TgvAB-dependent type IV restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Modification-dependent restriction of "
                        "hypermodified phage DNA by TgvAB."
                    ),
                },
                {
                    "node_id": "t_even_like_phage_propagation",
                    "label": "T-even-like phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Productive propagation of T-even-like phages whose "
                        "genomes carry glucosylated hmC."
                    ),
                },
                {
                    "node_id": "tgvab_system_trait",
                    "label": "TgvAB system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded TgvAB "
                        "modification-dependent restriction system."
                    ),
                },
                {
                    "node_id": "restriction_modification_system",
                    "label": "restriction-modification system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000095",
                    "description": (
                        "Possession of a methyltransferase and restriction "
                        "endonuclease system for self/non-self DNA "
                        "discrimination."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "tgvab_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "tgvab_dependent_type_iv_restriction",
                    "description": (
                        "A TgvAB locus encodes both proteins required for "
                        "modification-dependent restriction of T-even phage "
                        "DNA."
                    ),
                    "evidence": [
                        {
                            "reference": VIZZARRO,
                            "snippet": TGVAB_EMBEDDED_SNIPPET,
                            "notes": (
                                "Vizzarro et al. define the embedded VPI-2 "
                                "TgvAB locus as a GmrSD-related type IV "
                                "restriction system."
                            ),
                        },
                        {
                            "reference": GOMEZ,
                            "snippet": BOTH_COMPONENTS_SNIPPET,
                            "notes": (
                                "Gomez and Waters show that anti-phage "
                                "activity requires both TgvA and TgvB."
                            ),
                        },
                        article_registry_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "tgvab_dependent_type_iv_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "glucosylated_hmc_phage_dna",
                    "description": (
                        "TgvAB-dependent type IV restriction targets "
                        "T-even-like phage DNA bearing glucosylated "
                        "5-hydroxymethylcytosine."
                    ),
                    "evidence": [
                        {
                            "reference": GOMEZ,
                            "snippet": GLUCOSYLATED_HMC_SNIPPET,
                            "notes": (
                                "Gomez and Waters directly connect the "
                                "TgvAB system to targeting glucosylated "
                                "5-hydroxymethylcytosine during phage "
                                "defense."
                            ),
                        },
                    ],
                },
                {
                    "subject": "tgvab_dependent_type_iv_restriction",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "t_even_like_phage_propagation",
                    "description": (
                        "Restriction of hypermodified T-even-like phage DNA "
                        "inhibits productive phage propagation."
                    ),
                    "evidence": [
                        {
                            "reference": VIZZARRO,
                            "snippet": TEVENVIRINAE_SNIPPET,
                            "notes": (
                                "Vizzarro et al. support TgvAB anti-phage "
                                "activity against hypermodified phages."
                            ),
                        },
                        {
                            "reference": GOMEZ,
                            "snippet": GLUCOSYLATED_HMC_SNIPPET,
                            "notes": (
                                "Gomez and Waters identify glucosylated "
                                "5-hydroxymethylcytosine as the phage-DNA "
                                "modification targeted by TgvAB."
                            ),
                        },
                    ],
                },
                {
                    "subject": "tgvab_dependent_type_iv_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "tgvab_system_trait",
                    "description": (
                        "TgvAB-dependent type IV restriction realizes the "
                        "TgvAB system trait."
                    ),
                    "evidence": [
                        {
                            "reference": VIZZARRO,
                            "snippet": TYPE_IV_CYTOSINES_SNIPPET,
                            "notes": (
                                "Vizzarro et al. frame TgvAB as a type IV "
                                "restriction system recognizing "
                                "hypermodified cytosines."
                            ),
                        },
                        {
                            "reference": GOMEZ,
                            "snippet": BOTH_COMPONENTS_SNIPPET,
                            "notes": (
                                "Gomez and Waters report that both encoded "
                                "TgvAB components are required for "
                                "anti-phage activity."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "tgvab_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "restriction_modification_system",
                    "description": (
                        "TgvAB is a GmrSD-related type IV restriction "
                        "system in the broader restriction-modification "
                        "family."
                    ),
                    "evidence": [
                        {
                            "reference": VIZZARRO,
                            "snippet": TGVAB_EMBEDDED_SNIPPET,
                            "notes": (
                                "Vizzarro et al. place TgvAB among "
                                "GmrSD-family type IV restriction enzymes."
                            ),
                        },
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "tgvab-defensefinder-rule-gap",
            "prompt": (
                "Resolve TgvAB native host breadth, TgvA/TgvB biochemical "
                "roles, phage substrate breadth, and DefenseFinder rule or "
                "model coverage before minting narrower TgvAB mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Vizzarro et al. and Gomez and Waters support TgvAB as a "
                "two-component VPI-2 type IV restriction system that "
                "restricts glucosylated hmC-containing T-even phage DNA, "
                "and the pinned DefenseFinder HMM inventory carries TgvA "
                "and TgvB custom profiles. The pinned DefenseFinder rules "
                "table has no TgvAB row, and the evidence does not yet "
                "resolve native host breadth, the individual TgvA versus "
                "TgvB biochemical roles, full phage substrate breadth, or "
                "a rule-level profile combination."
            ),
            "evidence": [
                {
                    "reference": VIZZARRO,
                    "snippet": TGVAB_EMBEDDED_SNIPPET,
                    "notes": (
                        "Vizzarro et al. name TgvAB as the GmrSD-related "
                        "modification-dependent restriction system."
                    ),
                },
                {
                    "reference": GOMEZ,
                    "snippet": GLUCOSYLATED_HMC_SNIPPET,
                    "notes": (
                        "Gomez and Waters support the glucosylated hmC "
                        "substrate class while leaving broader phage "
                        "substrate limits open."
                    ),
                },
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "a TgvAB row, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#tgvab_type_iv_restriction"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
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
            "Minted TgvAB system as a DOI-backed GENOMICS TraitRecord "
            "under restriction-modification system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, history, "
            "or prior proposal record; kept the graph at two-component "
            "TgvAB/type-IV-restriction level because the pinned "
            "DefenseFinder HMM rows are not backed by a pinned rules row; "
            f"the replacement placeholder is reserved in {PROPOSAL}."
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
