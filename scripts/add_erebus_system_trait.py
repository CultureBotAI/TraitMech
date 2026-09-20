#!/usr/bin/env python3
"""Add the Erebus system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "erebus_system.yaml"

VAN_DEN_BERG = "DOI:10.1016/j.chom.2024.07.007"
VAN_DEN_BERG_VALIDATED_SYSTEMS_SNIPPET = (
    "We validated six of these phage defense systems, including factors "
    "preventing viral attachment, R-loop-acting enzymes, the inflammasome, "
    "ubiquitin pathway, and pathogen recognition signaling."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)
DEFENSEFINDER_HMMS = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/Liste_hmm_system.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-20T11:49:00Z"
REVIEW_TIMESTAMP = "2026-09-20T12:25:08Z"

IDENTIFIER = "traitmech:000308"
PROPOSAL = "proposals/metpo_traitmech_v185"
SYSTEM = "Erebus"
SLUG = "erebus"
HMM = "Erebus__EruA"
EMPTY_HMM_NAME = ""


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Erebus | 10\\.1016/j\\.chom\\.2024\\.07\\.007 | Bacterial "
            "homologs of innate eukaryotic antiviral defenses with anti-phage "
            "activity highlight shared evolutionary roots of viral defenses"
        ),
        "notes": (
            "The DefenseFinder model registry maps the named Erebus system "
            "to the van den Berg et al. antiphage-system discovery paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{HMM:<48} | {EMPTY_HMM_NAME:<48} | {SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records Erebus__EruA in the "
            "Erebus model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Erebus system",
    "definition": (
        "A phage defense system in which an organism possesses an Erebus "
        "locus that can protect bacteria from bacteriophage infection."
    ),
    "definition_source": VAN_DEN_BERG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Erebus",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "EruA",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        }
    ],
    "evidence": [
        {
            "reference": VAN_DEN_BERG,
            "snippet": VAN_DEN_BERG_VALIDATED_SYSTEMS_SNIPPET,
            "notes": (
                "van den Berg et al. validated six phage defense systems "
                "related to eukaryotic innate antiviral responses."
            ),
        },
        {
            "reference": VAN_DEN_BERG,
            "snippet": (
                "Searching for phage defense systems related to innate antiviral "
                "genes from vertebrates and plants, we uncovered over 450 "
                "candidates."
            ),
            "notes": (
                "van den Berg et al. motivate a conservative system-level record "
                "that does not assert a resolved Erebus trigger, effector "
                "output, or universal pathway."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "erebus_locus_restricts_phage",
            "title": "Erebus loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of an Erebus "
                "locus to restricted bacteriophage propagation without asserting "
                "the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Erebus as a named anti-phage system with an "
                "Erebus__EruA DefenseFinder HMM profile entry while leaving its "
                "phage trigger, molecular substrate, antiviral effector output, "
                "and subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "erebus_locus",
                    "label": "Erebus locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An Erebus anti-phage defense locus cataloged in "
                        "DefenseFinder with an Erebus__EruA HMM profile entry."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells carrying "
                        "the Erebus system."
                    ),
                },
                {
                    "node_id": "erebus_system_trait",
                    "label": "Erebus system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Erebus phage-defense "
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
                    "subject": "erebus_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps Erebus to a eukaryotic-antiviral-"
                        "homolog antiphage-system discovery paper and catalogs "
                        "an Erebus__EruA HMM profile entry in the Erebus "
                        "model namespace."
                    ),
                    "evidence": [
                        {
                            "reference": VAN_DEN_BERG,
                            "snippet": VAN_DEN_BERG_VALIDATED_SYSTEMS_SNIPPET,
                            "notes": (
                                "van den Berg et al. validated six phage defense "
                                "systems related to eukaryotic innate antiviral "
                                "responses."
                            ),
                        },
                        article_registry_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "erebus_system_trait",
                    "description": (
                        "Erebus-mediated phage restriction realizes the Erebus "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": VAN_DEN_BERG,
                            "snippet": VAN_DEN_BERG_VALIDATED_SYSTEMS_SNIPPET,
                            "notes": (
                                "van den Berg et al. validated six phage defense "
                                "systems related to eukaryotic antiviral responses."
                            ),
                        },
                    ],
                },
                {
                    "subject": "erebus_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Erebus system possession is a phage-defense-system trait."
                    ),
                    "evidence": [article_registry_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "erebus-mechanism-gap",
            "prompt": (
                "Resolve Erebus phage triggers and effector outputs before "
                "minting narrower Erebus mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "van den Berg et al. and DefenseFinder support Erebus as a "
                "named anti-phage system with an Erebus__EruA HMM profile "
                "entry, but the trigger, molecular substrate, antiviral "
                "effector output, and subtype-specific mechanism are not "
                "resolved enough here to assert a narrower mechanistic child "
                "trait."
            ),
            "attaches_to": ["causal_graphs#erebus_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
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
            "Minted Erebus system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            f"record; the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CURATION_REVIEW_REVISION",
        changes=(
            "Resolved PR 1136 review issue 1137 by mirroring the "
            "proposal-only EruA label as a RELATED_SYNONYM sourced to the "
            "pinned DefenseFinder HMM inventory."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
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
