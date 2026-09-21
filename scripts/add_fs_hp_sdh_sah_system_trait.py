#!/usr/bin/env python3
"""Add the FS-HP-SDH-sah system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "fs_hp_sdh_sah_system.yaml"

FILLOL_SALOM = "DOI:10.1016/j.cell.2022.07.014"
FILLOL_SALOM_PMID = "PMID:35985290"
PICI_DEFENSE_SNIPPET = (
    "the phage-inducible chromosomal islands (PICIs), carry an "
    "impressive arsenal of defense mechanisms"
)
PICI_IMMUNITY_SNIPPET = (
    "These defense systems provide broad immunity, blocking not only "
    "phage reproduction, but also plasmid and non-cognate PICI transfer."
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
TIMESTAMP = "2026-09-21T23:29:51Z"
IDENTIFIER = "traitmech:000349"
PROPOSAL = "proposals/metpo_traitmech_v226"
SLUG = "fs_hp_sdh_sah"

ARTICLE_REGISTRY_SNIPPET = (
    "FS_HP_SDH_sah | 10\\.1016/j\\.cell\\.2022\\.07\\.014 | "
    "Bacteriophages benefit from mobilizing pathogenicity islands "
    "encoding immune systems against competitors"
)
RULES_SNIPPET = (
    "FS_HP_SDH_sah\tFS_HP_SDH_sah\t2\t2\t"
    "FS_HP_SDH_sah__HP, FS_HP_SDH_sah__SDH_sah"
)
HP_HMM_ROW = (
    "| FS_HP_SDH_sah__HP                                | "
    "FS_HP_SDH_sah__HP                                | "
    "FS_HP_SDH_sah          | Custom                  | 20     |"
)
SDH_SAH_HMM_ROW = (
    "| FS_HP_SDH_sah__SDH_sah                           | "
    "FS_HP_SDH_sah__SDH_sah                           | "
    "FS_HP_SDH_sah          | Custom                  | 20     |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named FS_HP_SDH_sah "
            "system to the Fillol-Salom et al. PICI defense-system paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models FS_HP_SDH_sah as a "
            "two-profile system requiring the FS_HP_SDH_sah__HP and "
            "FS_HP_SDH_sah__SDH_sah profiles."
        ),
    }


def hp_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HP_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records FS_HP_SDH_sah__HP "
            "under FS_HP_SDH_sah."
        ),
    }


def sdh_sah_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": SDH_SAH_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records FS_HP_SDH_sah__SDH_sah "
            "under FS_HP_SDH_sah."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "FS-HP-SDH-sah system",
    "definition": (
        "A phage defense system in which an organism possesses an "
        "FS_HP_SDH_sah locus represented by DefenseFinder as a two-profile "
        "model requiring FS_HP_SDH_sah__HP and FS_HP_SDH_sah__SDH_sah."
    ),
    "definition_source": FILLOL_SALOM,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "FS_HP_SDH_sah",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "FS_HP_SDH_sah__HP",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "FS_HP_SDH_sah__SDH_sah",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": FILLOL_SALOM_PMID,
            "snippet": PICI_DEFENSE_SNIPPET,
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal "
                "islands as carriers of mobile-element defense mechanisms."
            ),
        },
        {
            "reference": FILLOL_SALOM_PMID,
            "snippet": PICI_IMMUNITY_SNIPPET,
            "notes": (
                "Fillol-Salom et al. support PICI-encoded defense systems "
                "as broad immunity determinants against phage reproduction "
                "and other mobile genetic element transfer."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hp_hmm_evidence(),
        sdh_sah_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "fs_hp_sdh_sah_locus_restricts_phage",
            "title": "FS-HP-SDH-sah loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "FS_HP_SDH_sah locus to broad mobile-element defense without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures FS-HP-SDH-sah as a named DefenseFinder "
                "two-profile system in the Fillol-Salom PICI defense family "
                "while leaving its natural host breadth, helper-phage trigger, "
                "HP component identity, SDH_sah partner function, and "
                "profile-to-activity mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "fs_hp_sdh_sah_locus",
                    "label": "FS_HP_SDH_sah locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder FS_HP_SDH_sah phage-defense locus "
                        "represented by custom FS_HP_SDH_sah__HP and "
                        "FS_HP_SDH_sah__SDH_sah profiles."
                    ),
                },
                {
                    "node_id": "pici_encoded_mobile_element_defense",
                    "label": "PICI-encoded mobile-element defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Defense by phage-inducible chromosomal island loci "
                        "against phage reproduction, plasmid transfer, or "
                        "non-cognate PICI transfer."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "FS-HP-SDH-sah system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded FS-HP-SDH-sah "
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
                    "subject": "fs_hp_sdh_sah_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pici_encoded_mobile_element_defense",
                    "description": (
                        "DefenseFinder maps FS_HP_SDH_sah to the Fillol-Salom "
                        "et al. PICI-encoded immunity study and models it as "
                        "a two-profile system requiring custom HP and SDH_sah "
                        "profiles."
                    ),
                    "evidence": [
                        {
                            "reference": FILLOL_SALOM_PMID,
                            "snippet": PICI_DEFENSE_SNIPPET,
                            "notes": (
                                "Fillol-Salom et al. support PICI loci as "
                                "carriers of phage and mobile-element "
                                "defense mechanisms."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        hp_hmm_evidence(),
                        sdh_sah_hmm_evidence(),
                    ],
                },
                {
                    "subject": "pici_encoded_mobile_element_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "FS_HP_SDH_sah-associated mobile-element defense "
                        "realizes the FS-HP-SDH-sah system trait."
                    ),
                    "evidence": [
                        {
                            "reference": FILLOL_SALOM_PMID,
                            "snippet": PICI_IMMUNITY_SNIPPET,
                            "notes": (
                                "Fillol-Salom et al. support PICI-encoded "
                                "defense systems as broad mobile-element "
                                "immunity determinants."
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
                        "FS-HP-SDH-sah system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [article_registry_evidence(), rules_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "fs-hp-sdh-sah-mechanism-gap",
            "prompt": (
                "Resolve FS_HP_SDH_sah natural hosts, helper-phage triggers, "
                "HP component identity, and SDH_sah partner activity before "
                "minting narrower FS_HP_SDH_sah mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Fillol-Salom et al. support phage-inducible chromosomal "
                "islands as carriers of defense systems that provide broad "
                "immunity, and DefenseFinder models FS_HP_SDH_sah as a "
                "two-profile system. Its exact natural host breadth, "
                "helper-phage trigger, HP component identity, SDH_sah "
                "partner activity, and profile-to-activity mapping remain "
                "unresolved."
            ),
            "attaches_to": ["causal_graphs#fs_hp_sdh_sah_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
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
            "Minted FS-HP-SDH-sah system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
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
