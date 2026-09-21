#!/usr/bin/env python3
"""Add the Ophion system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ophion_system.yaml"

KEESMAN = "DOI:10.1101/2025.09.30.679545"

KEESMAN_VALIDATION_SNIPPET = (
    "From over 500 candidate defense systems, we selected nine for "
    "experimental testing and validated three: Dionysus, a TerB-encoding "
    "system that disrupts early phage infection vesicle formation by Jumbo "
    "phages; Ophion, a Radical SAM-containing system that prevents the "
    "formation of the Jumbo phage nucleus; and Ambrosia, a tightly regulated "
    "RM-like system."
)
KEESMAN_COMPOSITION_SNIPPET = (
    "Ophion, named after a primordial serpent from Greek mythology, is a "
    "three gene system encoding a radical S-adenosyl-L-methionine (rSAM) "
    "enzyme (OpnA), a polymerase-and histidinol-phosphatase (PHP, OpnB), "
    "and a phosphoribosyl transferase (PRTase, OpnC)"
)
KEESMAN_PROTECTION_SNIPPET = (
    "Ophion shows strong protection against jumbo phages"
)
KEESMAN_REQUIREMENT_SNIPPET = (
    "Mutating conserved residues of the rSAM and PRTase domains revealed "
    "these to be essential for protection, with partial dependence on the PHP "
    "domain"
)
KEESMAN_STAGE_SNIPPET = (
    "Ophion provides potent and specific defense against jumbo phages by "
    "blocking progression from the EPI vesicle to the nucleus stage, "
    "possibly by halting the transcription of the nucleus forming genes"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T08:20:12Z"
REVIEW_TIMESTAMP = "2026-09-21T08:47:47Z"

IDENTIFIER = "traitmech:000331"
PROPOSAL = "proposals/metpo_traitmech_v208"
SYSTEM = "Ophion"
SLUG = "ophion"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Ophion | 10\\.1101/2025\\.09\\.30\\.679545 | Discovery of "
            "phage defense systems through component modularity networks"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Ophion "
            "system to the Keesman et al. modular phage-defense discovery "
            "preprint; the pinned DefenseFinder HMM inventory and rules "
            "table do not list Ophion, so this row is name-to-paper "
            "evidence rather than model-component evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Ophion system",
    "definition": (
        "A phage defense system in which an organism possesses a three-gene "
        "Ophion locus encoding OpnA, OpnB, and OpnC components that can "
        "block jumbo-phage infection before phage-nucleus formation."
    ),
    "definition_source": KEESMAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": SYSTEM,
            "synonym_type": "EXACT_SYNONYM",
            "source": KEESMAN,
        }
    ],
    "evidence": [
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_VALIDATION_SNIPPET,
            "notes": (
                "Keesman et al. named Ophion among three modular "
                "phage-defense candidates validated experimentally from an "
                "initial pool of more than 500 candidates."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_COMPOSITION_SNIPPET,
            "notes": (
                "Keesman et al. support Ophion as a three-gene system "
                "encoding OpnA, OpnB, and OpnC components with Radical SAM, "
                "PHP, and phosphoribosyl-transferase domains."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_PROTECTION_SNIPPET,
            "notes": (
                "Keesman et al. support Ophion as a system that strongly "
                "protects against jumbo phages."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_REQUIREMENT_SNIPPET,
            "notes": (
                "Keesman et al. support the OpnA Radical SAM and OpnC "
                "phosphoribosyl-transferase domains as essential in the "
                "tested Ophion system, with partial dependence on OpnB PHP."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_STAGE_SNIPPET,
            "notes": (
                "Keesman et al. connect Ophion-mediated defense to arrest of "
                "jumbo phages as they progress from the early phage "
                "infection vesicle stage to nucleus formation."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Ophion loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "Ophion locus to restricted jumbo-phage propagation without "
                "asserting the direct phage trigger, modified nucleotide "
                "product, or early-transcription target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Ophion as a named three-gene "
                "anti-jumbo-phage system while leaving its direct phage "
                "trigger, the OpnA/OpnB/OpnC interaction sequence, the "
                "nucleotide-modification product, the natural locus breadth, "
                "and the absence of pinned DefenseFinder HMM or rule rows "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Ophion locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A three-gene Ophion anti-jumbo-phage defense locus "
                        "encoding OpnA, OpnB, and OpnC components."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of jumbo bacteriophages in "
                        "cells carrying the Ophion system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Ophion system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Ophion "
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
                    "subject": f"{SLUG}_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The three-gene Ophion locus restricts infection by "
                        "jumbo phages."
                    ),
                    "evidence": [
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_PROTECTION_SNIPPET,
                            "notes": (
                                "Keesman et al. report that Ophion protects "
                                "against jumbo phages."
                            ),
                        },
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_REQUIREMENT_SNIPPET,
                            "notes": (
                                "Keesman et al. report that conserved-residue "
                                "mutations establish the OpnA Radical SAM "
                                "and OpnC phosphoribosyl-transferase "
                                "domains as essential, with partial "
                                "dependence on OpnB PHP."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Ophion-mediated phage restriction realizes the "
                        "Ophion system trait."
                    ),
                    "evidence": [
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_STAGE_SNIPPET,
                            "notes": (
                                "Keesman et al. connect Ophion activity to "
                                "blocking progression from the jumbo-phage "
                                "early phage infection vesicle stage to the "
                                "nucleus stage."
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
                    "description": "Ophion system possession is a phage-defense-system trait.",
                    "evidence": [
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_VALIDATION_SNIPPET,
                            "notes": (
                                "Keesman et al. list Ophion among "
                                "experimentally validated phage-defense "
                                "systems."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ophion-jumbo-phage-mechanism-gap",
            "prompt": (
                "Resolve Ophion phage triggers, nucleotide-modification "
                "products, and model coverage before minting narrower Ophion "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Keesman et al. support Ophion as a three-gene "
                "anti-jumbo-phage system that blocks progression from the "
                "early phage infection vesicle to the phage nucleus, but the "
                "direct phage trigger, exact OpnA/OpnB/OpnC interaction "
                "sequence, modified nucleotide product, natural locus "
                "breadth, and profile-to-component model are not resolved "
                "enough here to assert a narrower mechanistic child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
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
            "Minted Ophion system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement placeholder "
            f"is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_PR_REVIEW",
        changes=(
            "Tightened the Ophion conserved-residue evidence note after "
            "the PR 1183 adversarial review filed issue 1184, narrowing "
            "the claim to essential OpnA Radical SAM and OpnC "
            "phosphoribosyl-transferase domains plus partial OpnB PHP "
            "dependence."
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
