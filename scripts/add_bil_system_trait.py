#!/usr/bin/env python3
"""Add the Bil system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "bil_system.yaml"

HOR = "DOI:10.1038/s41586-024-07616-5"
MILLMAN = "DOI:10.1016/j.chom.2022.09.017"
MILLMAN_PREPRINT = "DOI:10.1101/2022.05.11.491447"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-25T03:02:00Z"
POSED_DATE = "2026-09-24"
IDENTIFIER = "traitmech:000369"
PROPOSAL = "proposals/metpo_traitmech_v246"

BIL_FIGURE_SNIPPET = "Bil antiphage defence system"
BIL_CTF_SNIPPET = (
    "phage central tail fibre is obstructed by the covalently attached "
    "ubiquitin-like protein"
)
BIL_INFECTIVITY_SNIPPET = "These phages show severely impaired infectivity"
MILLMAN_TITLE_SNIPPET = (
    "An expanded arsenal of immune systems that protect bacteria from phages"
)
MILLMAN_PREPRINT_TITLE_SNIPPET = (
    "An expanding arsenal of immune systems that protect bacteria from phages"
)
ARTICLE_REGISTRY_SNIPPET = (
    "Bil | 10\\.1101/2022\\.05\\.11\\.491447 | An expanding arsenal "
    "of immune systems that protect bacteria from phages"
)


def hor_figure_evidence() -> dict[str, str]:
    return {
        "reference": HOR,
        "snippet": BIL_FIGURE_SNIPPET,
        "notes": (
            "Hor et al. identify Bil as a ubiquitin-like conjugation "
            "antiphage defense system."
        ),
    }


def hor_central_tail_fibre_evidence() -> dict[str, str]:
    return {
        "reference": HOR,
        "snippet": BIL_CTF_SNIPPET,
        "notes": (
            "Hor et al. show that the Bil system obstructs the phage central "
            "tail fibre with a covalently attached ubiquitin-like protein."
        ),
    }


def hor_infectivity_evidence() -> dict[str, str]:
    return {
        "reference": HOR,
        "snippet": BIL_INFECTIVITY_SNIPPET,
        "notes": (
            "Hor et al. connect Bil-dependent particle production to reduced "
            "phage infectivity."
        ),
    }


def millman_evidence() -> dict[str, str]:
    return {
        "reference": MILLMAN,
        "snippet": MILLMAN_TITLE_SNIPPET,
        "notes": (
            "Millman et al. published the discovery cohort that DefenseFinder "
            "maps to its Bil article-registry row."
        ),
    }


def millman_preprint_evidence() -> dict[str, str]:
    return {
        "reference": MILLMAN_PREPRINT,
        "snippet": MILLMAN_PREPRINT_TITLE_SNIPPET,
        "notes": (
            "The bioRxiv version of Millman et al. is the DOI cited in "
            "DefenseFinder's Bil article-registry row."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Bil system to "
            "the Millman et al. antiphage-system discovery preprint."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Bil system",
    "definition": (
        "A phage defense system in which an organism possesses a Bil bacterial "
        "ubiquitin-like conjugation locus that can covalently attach a "
        "ubiquitin-like protein to the bacteriophage central tail fibre and "
        "impair phage infectivity."
    ),
    "definition_source": HOR,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Bil",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Bil antiphage defence system",
            "synonym_type": "EXACT_SYNONYM",
            "source": HOR,
        },
    ],
    "evidence": [
        hor_figure_evidence(),
        hor_central_tail_fibre_evidence(),
        hor_infectivity_evidence(),
        millman_evidence(),
        millman_preprint_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "bil_locus_impairs_phage_assembly",
            "title": "Bil loci impair bacteriophage infectivity",
            "description": (
                "Conservative system-level sketch linking possession of a Bil "
                "ubiquitin-like conjugation locus to central-tail-fibre "
                "obstruction and impaired phage infectivity without asserting "
                "the exact DefenseFinder profile or rule set for Bil."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Bil as a named phage-defense system whose "
                "ubiquitin-like protein is covalently attached to the phage "
                "central tail fibre while leaving the exact Bil component "
                "composition, target-phage breadth, receptor-recognition "
                "consequences, and DefenseFinder model profiles unresolved."
            ),
            "nodes": [
                {
                    "node_id": "bil_locus",
                    "label": "Bil locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A bacterial Bil ubiquitin-like conjugation locus "
                        "that encodes an antiphage defense system."
                    ),
                },
                {
                    "node_id": "bil_ubiquitin_like_conjugation",
                    "label": "Bil ubiquitin-like conjugation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Covalent attachment of a Bil ubiquitin-like protein "
                        "during phage infection."
                    ),
                },
                {
                    "node_id": "central_tail_fibre_obstruction",
                    "label": "central tail fibre obstruction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Obstruction of a bacteriophage central tail fibre by "
                        "a covalently attached ubiquitin-like protein."
                    ),
                },
                {
                    "node_id": "impaired_phage_infectivity",
                    "label": "impaired phage infectivity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced infectivity of phage particles released "
                        "from cells encoding the Bil defense system."
                    ),
                },
                {
                    "node_id": "bil_system_trait",
                    "label": "Bil system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Bil phage-defense "
                        "system."
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
                    "subject": "bil_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "bil_ubiquitin_like_conjugation",
                    "description": (
                        "Bil loci encode a bacterial antiphage system based "
                        "on ubiquitin-like conjugation, and DefenseFinder "
                        "links Bil to an antiphage-system discovery preprint."
                    ),
                    "evidence": [
                        hor_figure_evidence(),
                        millman_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "bil_ubiquitin_like_conjugation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "central_tail_fibre_obstruction",
                    "description": (
                        "The Bil system can obstruct the phage central tail "
                        "fibre by covalently attaching a ubiquitin-like "
                        "protein."
                    ),
                    "evidence": [hor_central_tail_fibre_evidence()],
                },
                {
                    "subject": "central_tail_fibre_obstruction",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "impaired_phage_infectivity",
                    "description": (
                        "Central-tail-fibre obstruction by the Bil system "
                        "impairs phage-particle infectivity."
                    ),
                    "evidence": [
                        hor_central_tail_fibre_evidence(),
                        hor_infectivity_evidence(),
                    ],
                },
                {
                    "subject": "impaired_phage_infectivity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "bil_system_trait",
                    "description": (
                        "Bil-mediated impairment of phage infectivity "
                        "realizes the Bil system trait."
                    ),
                    "evidence": [
                        hor_infectivity_evidence(),
                    ],
                },
                {
                    "subject": "bil_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Bil system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        hor_figure_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "bil-defensefinder-profile-gap",
            "prompt": (
                "Resolve Bil HMM profiles and rule rows before minting "
                "component-specific Bil mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Hor et al. support Bil as a bacterial ubiquitin-like "
                "conjugation antiphage system that modifies the phage "
                "central tail fibre, and the pinned DefenseFinder article "
                "registry maps Bil to the Millman et al. discovery preprint. "
                "The same pinned HMM inventory and rules table do not include "
                "exact Bil rows, so the exact DefenseFinder profile set, "
                "component rule, and model coverage remain unresolved."
            ),
            "evidence": [article_registry_evidence()],
            "attaches_to": ["causal_graphs#bil_locus_impairs_phage_assembly"],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
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
            "Minted Bil system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            f"proposal record; the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_DEFENSEFINDER_PROFILE_GAP",
        changes=(
            "Reviewed the DefenseFinder Bil article-registry row at commit "
            f"{DEFENSEFINDER_COMMIT} and left narrower Bil HMM/profile "
            "semantics unresolved because the pinned HMM inventory and rules "
            "table have no exact Bil rows."
        ),
        llm_assisted=True,
        timestamp="2026-09-25T03:03:00Z",
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
