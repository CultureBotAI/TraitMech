#!/usr/bin/env python3
"""Add the Gao-Qat system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gao_qat_system.yaml"

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
TIMESTAMP = "2026-09-22T08:09:38Z"
IDENTIFIER = "traitmech:000359"
PROPOSAL = "proposals/metpo_traitmech_v236"
SLUG = "gao_qat"

ARTICLE_REGISTRY_SNIPPET = (
    "Gao_Qat | 10\\.1126/science\\.aba0372 | Diverse enzymatic activities "
    "mediate antiviral immunity in prokaryotes"
)
RULES_SNIPPET = (
    "Gao_Qat\tGao_Qat\t4\t4\tGao_Qat__QatA, Gao_Qat__QatB, "
    "Gao_Qat__QatC, Gao_Qat__QatD"
)
HMM_ROWS = {
    "Gao_Qat__QatA": (
        "| Gao_Qat__QatA                                    | "
        "Gao_Qat__QatA                                    | "
        "Gao_Qat                | Custom                  | 20     |"
    ),
    "Gao_Qat__QatB": (
        "| Gao_Qat__QatB                                    | "
        "Gao_Qat__QatB                                    | "
        "Gao_Qat                | Custom                  | 20     |"
    ),
    "Gao_Qat__QatC": (
        "| Gao_Qat__QatC                                    | "
        "Gao_Qat__QatC                                    | "
        "Gao_Qat                | Custom                  | 20     |"
    ),
    "Gao_Qat__QatD": (
        "| Gao_Qat__QatD                                    | "
        "Gao_Qat__QatD                                    | "
        "Gao_Qat                | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Gao_Qat "
            "system to the Gao et al. prokaryotic antiviral-immunity paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Gao_Qat as a four-profile "
            "system requiring the Gao_Qat__QatA through Gao_Qat__QatD "
            "profiles."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under Gao_Qat."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Gao-Qat system",
    "definition": (
        "A phage defense system in which an organism possesses a Gao_Qat "
        "locus represented by DefenseFinder as a four-profile model "
        "requiring Gao_Qat__QatA, Gao_Qat__QatB, Gao_Qat__QatC, and "
        "Gao_Qat__QatD."
    ),
    "definition_source": GAO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Gao_Qat",
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
            "graph_id": "gao_qat_locus_restricts_phage",
            "title": "Gao-Qat loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Gao_Qat locus to Gao et al. antiviral cassette defense "
                "without asserting the unresolved Qat component activities."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Gao-Qat as a named DefenseFinder "
                "four-profile Gao-family system while leaving natural hosts, "
                "QatA/QatB/QatC/QatD protein functions, phage triggers, and "
                "direct effector activity unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gao_qat_locus",
                    "label": "Gao_Qat locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder Gao_Qat phage-defense locus "
                        "represented by custom QatA through QatD profiles."
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
                    "label": "Gao-Qat system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Gao-Qat "
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
                    "subject": "gao_qat_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gao_2020_antiviral_cassette_defense",
                    "description": (
                        "DefenseFinder maps Gao_Qat to the Gao et al. "
                        "systematic antiphage-system discovery paper and "
                        "models it as a four-profile system requiring QatA "
                        "through QatD."
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
                        "Gao_Qat-associated antiviral cassette defense "
                        "realizes the Gao-Qat system trait."
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
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Gao-Qat system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [article_registry_evidence(), rules_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "gao-qat-mechanism-gap",
            "prompt": (
                "Resolve Gao_Qat natural hosts, Qat component functions, "
                "phage triggers, and effector activity before minting "
                "narrower Gao_Qat mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support widespread antiviral gene cassettes that "
                "mediate protection against specific bacteriophages, and "
                "DefenseFinder models Gao_Qat as a four-profile system. The "
                "exact natural host breadth, QatA/QatB/QatC/QatD component "
                "identities, phage trigger, and profile-to-activity mapping "
                "remain unresolved."
            ),
            "attaches_to": ["causal_graphs#gao_qat_locus_restricts_phage"],
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
            "Minted Gao-Qat system as a DOI-backed GENOMICS TraitRecord "
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
