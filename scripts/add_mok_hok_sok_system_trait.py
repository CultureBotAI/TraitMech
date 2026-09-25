#!/usr/bin/env python3
"""Add the Mok-Hok-Sok system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mok_hok_sok_system.yaml"

PECOTA_DOI = "DOI:10.1128/jb.178.7.2044-2050.1996"
PECOTA_PMID = "PMID:8606182"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-25T05:02:42Z"
IDENTIFIER = "traitmech:000372"
PROPOSAL = "proposals/metpo_traitmech_v249"
SLUG = "mok_hok_sok"

ARTICLE_REGISTRY_SNIPPET = (
    "Mok_Hok_Sok | 10\\.1128/jb\\.178\\.7\\.2044-2050\\.1996 | "
    "Exclusion of T4 phage by the hok/sok killer locus from plasmid R1"
)
RULES_SNIPPET = (
    "Mok_Hok_Sok\tMok_Hok_Sok\t1\t1\t"
    "Mok_Hok_Sok__Hok, Mok_Hok_Sok__Mok\t\t\t"
)
HMM_ROWS = {
    "Mok_Hok_Sok__Hok": (
        "| Mok_Hok_Sok__Hok                                 | "
        "Mok_Hok_Sok__Hok                                 | "
        "Mok_Hok_Sok            | Custom                  | 90     |"
    ),
    "Mok_Hok_Sok__Mok": (
        "| Mok_Hok_Sok__Mok                                 | "
        "Mok_Hok_Sok__Mok                                 | "
        "Mok_Hok_Sok            | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Mok_Hok_Sok "
            "system to the Pecota and Wood plasmid R1 hok/sok phage-exclusion "
            "paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Mok_Hok_Sok as a single "
            "system listing Hok and Mok profiles with 1/1 thresholds."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under "
            "Mok_Hok_Sok."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Mok-Hok-Sok system",
    "definition": (
        "A phage defense system in which an organism possesses a hok/sok "
        "toxin-antitoxin locus represented by DefenseFinder as the "
        "two-profile Mok_Hok_Sok model and experimentally linked to "
        "bacteriophage T4 exclusion by the plasmid R1 hok/sok locus."
    ),
    "definition_source": PECOTA_DOI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Mok_Hok_Sok",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "hok/sok",
            "synonym_type": "RELATED_SYNONYM",
            "source": PECOTA_PMID,
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
            "reference": PECOTA_PMID,
            "snippet": (
                "To investigate whether the hok/sok locus evolved as a "
                "phage-exclusion mechanism, Escherichia coli cells that "
                "contain hok/sok on a pBR322-based plasmid were challenged "
                "with T1, T4, T5, T7, and lambda phage."
            ),
            "notes": (
                "Pecota and Wood tested whether a plasmid-carried hok/sok "
                "locus can act as a phage-exclusion mechanism."
            ),
        },
        {
            "reference": PECOTA_PMID,
            "snippet": (
                "The presence of hok/sok reduced the efficiency of plating "
                "of T4 by 42% and decreased the plaque size by approximately "
                "85%."
            ),
            "notes": (
                "Pecota and Wood show that hok/sok reduced bacteriophage T4 "
                "plating efficiency and plaque size."
            ),
        },
        {
            "reference": PECOTA_PMID,
            "snippet": (
                "Single-step growth experiments demonstrated that hok/sok "
                "decreased the T4 burst size by 40%, increased the time to "
                "form mature phage (eclipse time) from 22 to 30 min, and "
                "increased the time to cell lysis (latent period) from 30 "
                "to 60 min."
            ),
            "notes": (
                "Pecota and Wood support delayed T4 development and a lower "
                "T4 burst size in the presence of hok/sok."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "mok_hok_sok_locus_restricts_t4_phage",
            "title": "Mok-Hok-Sok loci exclude T4 phage",
            "description": (
                "Conservative system-level sketch linking a DefenseFinder "
                "Mok_Hok_Sok locus to bacteriophage T4 exclusion and the "
                "Mok-Hok-Sok system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Mok_Hok_Sok as a named DefenseFinder "
                "two-profile model tied to plasmid R1 hok/sok T4 exclusion "
                "while leaving natural host breadth, Sok antisense-RNA "
                "representation, Hok toxin activation, and the exact "
                "DefenseFinder Hok/Mok profile-to-activity mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "mok_hok_sok_locus",
                    "label": "Mok_Hok_Sok locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A hok/sok toxin-antitoxin phage-defense locus "
                        "represented by the DefenseFinder Mok_Hok_Sok Hok "
                        "and Mok profiles."
                    ),
                },
                {
                    "node_id": "t4_phage_exclusion",
                    "label": "T4 phage exclusion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of bacteriophage T4 plaque formation, "
                        "burst size, and lysis timing in a host carrying "
                        "hok/sok."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Mok-Hok-Sok system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Mok-Hok-Sok "
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
                    "subject": "mok_hok_sok_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t4_phage_exclusion",
                    "description": (
                        "The plasmid R1 hok/sok locus can mediate T4 phage "
                        "exclusion, and DefenseFinder models Mok_Hok_Sok as "
                        "a Hok/Mok two-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": PECOTA_PMID,
                            "snippet": (
                                "The presence of hok/sok reduced the "
                                "efficiency of plating of T4 by 42% and "
                                "decreased the plaque size by approximately "
                                "85%."
                            ),
                            "notes": (
                                "Pecota and Wood connect hok/sok possession "
                                "to bacteriophage T4 restriction."
                            ),
                        },
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "t4_phage_exclusion",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "T4 phage exclusion realizes the Mok-Hok-Sok system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": PECOTA_PMID,
                            "snippet": (
                                "Single-step growth experiments demonstrated "
                                "that hok/sok decreased the T4 burst size by "
                                "40%, increased the time to form mature phage "
                                "(eclipse time) from 22 to 30 min, and "
                                "increased the time to cell lysis (latent "
                                "period) from 30 to 60 min."
                            ),
                            "notes": (
                                "Pecota and Wood show lower burst size and "
                                "delayed T4 development when hok/sok is "
                                "present."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Mok-Hok-Sok system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "mok-hok-sok-natural-context-gap",
            "prompt": (
                "Resolve the natural host range, Sok antisense-RNA "
                "representation, Hok toxin activation, and Hok/Mok "
                "profile-to-activity mapping before minting narrower "
                "Mok-Hok-Sok mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Pecota and Wood support T4 exclusion by the plasmid R1 "
                "hok/sok locus carried on a pBR322-based plasmid, and "
                "DefenseFinder models Mok_Hok_Sok with Hok and Mok protein "
                "profiles. This first record leaves the native biological "
                "breadth, RNA antitoxin representation, Hok triggering, and "
                "profile-to-activity mapping unresolved."
            ),
            "attaches_to": ["causal_graphs#mok_hok_sok_locus_restricts_t4_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-25",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Mok-Hok-Sok system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
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
