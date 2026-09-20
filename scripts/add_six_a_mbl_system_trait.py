#!/usr/bin/env python3
"""Add the 6A-MBL system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "six_a_mbl_system.yaml"

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
VAN_DEN_BERG_ZENODO = "https://zenodo.org/records/11209165"
VAN_DEN_BERG_6A_MBL_SNIPPET = (
    "In addition, a fused ubiquitin-like E1-E2-JAB protein combined with a "
    "putative MBL nuclease (6A-MBL) was found"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-20T16:42:08Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-20T16:43:08Z"
REVIEW_REVISION_TIMESTAMP = "2026-09-20T17:16:31Z"

IDENTIFIER = "traitmech:000314"
PROPOSAL = "proposals/metpo_traitmech_v191"
SYSTEM = "6A-MBL"
DEFENSEFINDER_SYSTEM = "6A_MBL"
SLUG = "six_a_mbl"
CAP23_HMM = "6A_MBL__cap2_3"
MBLB_HMM = "6A_MBL__MblB"
EMPTY_HMM_NAME = ""


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "6A_MBL | 10\\.1016/j\\.chom\\.2024\\.07\\.007 | Bacterial "
            "homologs of innate eukaryotic antiviral defenses with anti-phage "
            "activity highlight shared evolutionary roots of viral defenses"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named 6A-MBL system "
            "to the van den Berg et al. antiphage-system discovery paper."
        ),
    }


def hmm_inventory_evidence(gene_name: str, profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{gene_name:<48} | {EMPTY_HMM_NAME:<48} | {DEFENSEFINDER_SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{gene_name} as a {profile} profile in the 6A_MBL model namespace."
        ),
    }


def zenodo_naming_evidence() -> dict[str, str]:
    return {
        "reference": VAN_DEN_BERG_ZENODO,
        "snippet": VAN_DEN_BERG_6A_MBL_SNIPPET,
        "notes": (
            "The Zenodo manuscript/supplementary-data record from van den Berg "
            "et al. names 6A-MBL as a putative MBL-nuclease system candidate."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "6A-MBL system",
    "definition": (
        "A phage defense system in which an organism possesses a 6A-MBL "
        "locus that can protect bacteria from bacteriophage infection."
    ),
    "definition_source": VAN_DEN_BERG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": SYSTEM,
            "synonym_type": "EXACT_SYNONYM",
            "source": VAN_DEN_BERG_ZENODO,
        },
        {
            "synonym_text": DEFENSEFINDER_SYSTEM,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "cap2_3",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "MblB",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
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
                "that does not assert a resolved 6A-MBL trigger, effector output, "
                "or universal pathway."
            ),
        },
        zenodo_naming_evidence(),
        article_registry_evidence(),
        hmm_inventory_evidence(CAP23_HMM, "cap2_3"),
        hmm_inventory_evidence(MBLB_HMM, "MblB"),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "6A-MBL loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a 6A-MBL "
                "locus to restricted bacteriophage propagation without asserting "
                "the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures 6A-MBL as a named anti-phage system with "
                "6A_MBL__cap2_3 and 6A_MBL__MblB DefenseFinder HMM profile "
                "entries while leaving its phage trigger, molecular substrate, "
                "antiviral effector output, and subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "6A-MBL locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A 6A-MBL anti-phage defense locus cataloged in "
                        "DefenseFinder with cap2_3 and MblB HMM profile entries."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells carrying "
                        "the 6A-MBL system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "6A-MBL system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded 6A-MBL phage-defense "
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
                    "subject": f"{SLUG}_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder maps 6A_MBL to a eukaryotic-antiviral-"
                        "homolog antiphage-system discovery paper and catalogs "
                        "cap2_3 and MblB HMM profile entries in the 6A_MBL "
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
                        hmm_inventory_evidence(CAP23_HMM, "cap2_3"),
                        hmm_inventory_evidence(MBLB_HMM, "MblB"),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "6A-MBL-mediated phage restriction realizes the 6A-MBL "
                        "system trait."
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
                        }
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "6A-MBL system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [article_registry_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "six-a-mbl-mechanism-gap",
            "prompt": (
                "Resolve 6A-MBL phage triggers and effector outputs before "
                "minting narrower 6A-MBL mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "van den Berg et al. and DefenseFinder support 6A-MBL as a "
                "named anti-phage system with 6A_MBL__cap2_3 and 6A_MBL__MblB "
                "HMM profile entries, but the trigger, molecular substrate, "
                "antiviral effector output, and subtype-specific mechanism are "
                "not resolved enough here to assert a narrower mechanistic "
                "child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}")
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted 6A-MBL system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior proposal "
            f"record; the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed the 6A-MBL canonical_examples gap and left "
            "canonical_examples empty: the current evidence supports a named "
            "phage-defense system and DefenseFinder profiles, but the curated "
            "record does not yet cite a source-backed bacterial taxon with a "
            "directly observed 6A-MBL locus. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="CURATION_REVIEW_REVISION",
        changes=(
            "Resolved issue #1148 by sourcing the exact 6A-MBL synonym from "
            "the stable van den Berg Zenodo record that names 6A-MBL "
            "verbatim, leaving DefenseFinder model and component labels as "
            "related synonyms."
        ),
        llm_assisted=True,
        timestamp=REVIEW_REVISION_TIMESTAMP,
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
