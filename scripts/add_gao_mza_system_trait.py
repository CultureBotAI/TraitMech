#!/usr/bin/env python3
"""Add the Gao-Mza system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gao_mza_system.yaml"

GAO = "DOI:10.1126/science.aba0372"
GAO_PMID = "PMID:32855333"
GAO_CASSETTES_SNIPPET = (
    "By systematic defense gene prediction and heterologous reconstitution, "
    "here we discover 29 widespread antiviral gene cassettes, collectively "
    "present in 32% of all sequenced bacterial and archaeal genomes, that "
    "mediate protection against specific bacteriophages."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-22T04:08:35Z"
IDENTIFIER = "traitmech:000355"
PROPOSAL = "proposals/metpo_traitmech_v232"
SLUG = "gao_mza"

ARTICLE_REGISTRY_SNIPPET = (
    "Gao_Mza | 10\\.1126/science\\.aba0372 | Diverse enzymatic activities "
    "mediate antiviral immunity in prokaryotes"
)
RULES_SNIPPET = (
    "Gao_Mza\tGao_Mza\t5\t5\tGao_Mza__MzaA, Gao_Mza__MzaB, "
    "Gao_Mza__MzaC, Gao_Mza__MzaD, Gao_Mza__MzaE"
)
HMM_ROWS = {
    "Gao_Mza__MzaA": (
        "| Gao_Mza__MzaA                                    | "
        "Gao_Mza__MzaA                                    | "
        "Gao_Mza                | Custom                  | 100    |"
    ),
    "Gao_Mza__MzaB": (
        "| Gao_Mza__MzaB                                    | "
        "Gao_Mza__MzaB                                    | "
        "Gao_Mza                | Custom                  | 400    |"
    ),
    "Gao_Mza__MzaC": (
        "| Gao_Mza__MzaC                                    | "
        "Gao_Mza__MzaC                                    | "
        "Gao_Mza                | Custom                  | 650    |"
    ),
    "Gao_Mza__MzaD": (
        "| Gao_Mza__MzaD                                    | "
        "Gao_Mza__MzaD                                    | "
        "Gao_Mza                | Custom                  | 100    |"
    ),
    "Gao_Mza__MzaE": (
        "| Gao_Mza__MzaE                                    | "
        "Gao_Mza__MzaE                                    | "
        "Gao_Mza                | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Gao_Mza "
            "system to the Gao et al. prokaryotic antiviral-immunity paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Gao_Mza as a five-profile "
            "system requiring the Gao_Mza__MzaA through Gao_Mza__MzaE "
            "profiles."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under Gao_Mza."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Gao-Mza system",
    "definition": (
        "A phage defense system in which an organism possesses a Gao_Mza "
        "locus represented by DefenseFinder as a five-profile model requiring "
        "Gao_Mza__MzaA, Gao_Mza__MzaB, Gao_Mza__MzaC, Gao_Mza__MzaD, and "
        "Gao_Mza__MzaE."
    ),
    "definition_source": GAO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Gao_Mza",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
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
            "reference": GAO_PMID,
            "snippet": GAO_CASSETTES_SNIPPET,
            "notes": (
                "Gao et al. support a systematic defense-gene prediction "
                "and heterologous reconstitution campaign that discovered "
                "widespread antiviral gene cassettes."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "gao_mza_locus_restricts_phage",
            "title": "Gao-Mza loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Gao_Mza locus to Gao et al. antiviral cassette defense "
                "without asserting the unresolved MzaA, MzaB, MzaC, MzaD, "
                "or MzaE component activities."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Gao-Mza as a named DefenseFinder "
                "five-profile Gao-family system while leaving natural hosts, "
                "MzaA/MzaB/MzaC/MzaD/MzaE protein functions, phage triggers, "
                "and direct effector activity unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gao_mza_locus",
                    "label": "Gao_Mza locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder Gao_Mza phage-defense locus "
                        "represented by custom MzaA through MzaE profiles."
                    ),
                },
                {
                    "node_id": "gao_2020_antiviral_cassette_defense",
                    "label": "Gao 2020 antiviral cassette defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Bacteriophage protection by one of the antiviral "
                        "gene cassettes described in the Gao et al. "
                        "systematic defense-gene discovery campaign."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Gao-Mza system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Gao-Mza "
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
                    "subject": "gao_mza_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gao_2020_antiviral_cassette_defense",
                    "description": (
                        "DefenseFinder maps Gao_Mza to the Gao et al. "
                        "systematic antiphage-system discovery paper and "
                        "models it as a five-profile system requiring MzaA "
                        "through MzaE."
                    ),
                    "evidence": [
                        {
                            "reference": GAO_PMID,
                            "snippet": GAO_CASSETTES_SNIPPET,
                            "notes": (
                                "Gao et al. support bacteriophage protection "
                                "by widespread antiviral gene cassettes."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "gao_2020_antiviral_cassette_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Gao_Mza-associated antiviral cassette defense "
                        "realizes the Gao-Mza system trait."
                    ),
                    "evidence": [
                        {
                            "reference": GAO_PMID,
                            "snippet": GAO_CASSETTES_SNIPPET,
                            "notes": (
                                "Gao et al. support bacteriophage protection "
                                "by widespread antiviral gene cassettes."
                            ),
                        }
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Gao-Mza system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [article_registry_evidence(), rules_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "gao-mza-mechanism-gap",
            "prompt": (
                "Resolve Gao_Mza natural hosts, MzaA/MzaB/MzaC/MzaD/MzaE "
                "component functions, phage triggers, and effector activity "
                "before minting narrower Gao_Mza mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support widespread antiviral gene cassettes that "
                "mediate protection against specific bacteriophages, and "
                "DefenseFinder models Gao_Mza as a five-profile system. The "
                "exact natural host breadth, Mza component identities, phage "
                "trigger, and profile-to-activity mapping remain unresolved."
            ),
            "attaches_to": ["causal_graphs#gao_mza_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-22",
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
            "Minted Gao-Mza system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement placeholder "
            f"is reserved in {PROPOSAL}."
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
