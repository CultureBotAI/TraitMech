#!/usr/bin/env python3
"""Add the FS-GIY-YIG system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "fs_giy_yig_system.yaml"

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
TIMESTAMP = "2026-09-21T21:36:57Z"
IDENTIFIER = "traitmech:000346"
PROPOSAL = "proposals/metpo_traitmech_v223"
SLUG = "fs_giy_yig"

ARTICLE_REGISTRY_SNIPPET = (
    "FS_GIY_YIG | 10\\.1016/j\\.cell\\.2022\\.07\\.014 | "
    "Bacteriophages benefit from mobilizing pathogenicity islands "
    "encoding immune systems against competitors"
)
RULES_SNIPPET = "FS_GIY_YIG\tFS_GIY_YIG\t1\t1\tFS_GIY_YIG__GIY_YIG"
GIY_YIG_HMM_ROW = (
    "| FS_GIY_YIG__GIY_YIG                              | "
    "FS_GIY_YIG__GIY_YIG                              | "
    "FS_GIY_YIG             | Custom                  | 100    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named FS_GIY_YIG "
            "system to the Fillol-Salom et al. PICI defense-system paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models FS_GIY_YIG as a "
            "single-profile system requiring the FS_GIY_YIG__GIY_YIG profile."
        ),
    }


def giy_yig_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": GIY_YIG_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records FS_GIY_YIG__GIY_YIG "
            "under FS_GIY_YIG."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "FS-GIY-YIG system",
    "definition": (
        "A phage defense system in which an organism possesses an "
        "FS_GIY_YIG locus represented by DefenseFinder as a single-profile "
        "model requiring FS_GIY_YIG__GIY_YIG."
    ),
    "definition_source": FILLOL_SALOM,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "FS_GIY_YIG",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "FS_GIY_YIG__GIY_YIG",
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
        giy_yig_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "fs_giy_yig_locus_restricts_phage",
            "title": "FS-GIY-YIG loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "FS_GIY_YIG locus to broad mobile-element defense without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures FS-GIY-YIG as a named DefenseFinder "
                "single-profile system in the Fillol-Salom PICI defense "
                "family while leaving its natural host breadth, helper-phage "
                "trigger, GIY-YIG substrate, and direct effector activity "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "fs_giy_yig_locus",
                    "label": "FS_GIY_YIG locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder FS_GIY_YIG phage-defense locus "
                        "represented by a GIY-YIG nuclease-like profile."
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
                    "label": "FS-GIY-YIG system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded FS-GIY-YIG "
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
                    "subject": "fs_giy_yig_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pici_encoded_mobile_element_defense",
                    "description": (
                        "DefenseFinder maps FS_GIY_YIG to the Fillol-Salom "
                        "et al. PICI-encoded immunity study and models it "
                        "as a single-profile system requiring a GIY-YIG "
                        "nuclease-like profile."
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
                        giy_yig_hmm_evidence(),
                    ],
                },
                {
                    "subject": "pici_encoded_mobile_element_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "FS_GIY_YIG-associated mobile-element defense "
                        "realizes the FS-GIY-YIG system trait."
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
                        "FS-GIY-YIG system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [article_registry_evidence(), rules_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "fs-giy-yig-mechanism-gap",
            "prompt": (
                "Resolve FS_GIY_YIG natural hosts, helper-phage triggers, "
                "GIY-YIG substrates, and effector activity before minting "
                "narrower FS_GIY_YIG mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Fillol-Salom et al. support phage-inducible chromosomal "
                "islands as carriers of defense systems that provide broad "
                "immunity, and DefenseFinder models FS_GIY_YIG as a "
                "single-profile system. Its exact natural host breadth, "
                "helper-phage trigger, nuclease substrate, and "
                "profile-to-activity mapping remain unresolved."
            ),
            "attaches_to": ["causal_graphs#fs_giy_yig_locus_restricts_phage"],
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
            "Minted FS-GIY-YIG system as a DOI-backed GENOMICS TraitRecord "
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
