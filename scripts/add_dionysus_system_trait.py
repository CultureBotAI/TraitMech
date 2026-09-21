#!/usr/bin/env python3
"""Add the Dionysus system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dionysus_system.yaml"

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
    "Dionysus is named after the god associated with winemaking and the "
    "celebration of life. This defense system consists of three genes "
    "encoding: DinA, featuring a merozoite adhesive erythrocyte binding "
    "protein (MAEBL) and a transmembrane (TM) domain; DinB, a TerB-like "
    "protein; and DinC, a pore-forming toxin (PFT) with four TM domains"
)
KEESMAN_JUMBO_SPECIFIC_SNIPPET = (
    "Both Dionysus and Ophion specifically block infection by jumbo phages, "
    "which have evolved specialized compartments to protect their DNA from "
    "DNA-targeting host defenses"
)
KEESMAN_EPI_SNIPPET = (
    "Specifically, we show that Dionysus forms pores in the EPI vesicle of "
    "the jumbo phage to disrupt the infection cycle of the phage at an early "
    "stage, similar to the mechanism described for the Juk phage defense "
    "system"
)
KEESMAN_REQUIREMENT_SNIPPET = (
    "All three proteins of Dionysus are essential for its protective "
    "capacity, as mutating a conserved amino acid within the MAEBL-like "
    "domain of DinA (H326A), and deletion of DinB or DinC, resulted in the "
    "partial (DinA H326A) or complete loss of anti-phage activity"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T07:22:15Z"

IDENTIFIER = "traitmech:000330"
PROPOSAL = "proposals/metpo_traitmech_v207"
SYSTEM = "Dionysus"
SLUG = "dionysus"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Dionysus | 10\\.1101/2025\\.09\\.30\\.679545 | Discovery of "
            "phage defense systems through component modularity networks"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Dionysus "
            "system to the Keesman et al. modular phage-defense discovery "
            "preprint; the pinned DefenseFinder HMM inventory and rules "
            "table do not list Dionysus, so this row is name-to-paper "
            "evidence rather than model-component evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Dionysus system",
    "definition": (
        "A phage defense system in which an organism possesses a three-gene "
        "Dionysus locus encoding DinA, DinB, and DinC components that can "
        "block jumbo-phage infection."
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
                "Keesman et al. named Dionysus among three modular "
                "phage-defense candidates validated experimentally from an "
                "initial pool of more than 500 candidates."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_COMPOSITION_SNIPPET,
            "notes": (
                "Keesman et al. support Dionysus as a three-gene defense "
                "system encoding DinA, DinB, and DinC components."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_JUMBO_SPECIFIC_SNIPPET,
            "notes": (
                "Keesman et al. support Dionysus as a system that blocks "
                "infection by jumbo phages with early phage infection "
                "vesicles."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_EPI_SNIPPET,
            "notes": (
                "Keesman et al. connect Dionysus to disruption of the jumbo "
                "phage early phage infection vesicle and therefore to "
                "interruption of the phage infection cycle."
            ),
        },
        {
            "reference": KEESMAN,
            "snippet": KEESMAN_REQUIREMENT_SNIPPET,
            "notes": (
                "Keesman et al. support all three Dionysus proteins as "
                "required for full anti-phage protection in the tested "
                "system."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Dionysus loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Dionysus locus to restricted jumbo-phage propagation "
                "without asserting the direct phage trigger or "
                "protein-resolved pore-forming sequence."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Dionysus as a named three-gene "
                "anti-jumbo-phage system while leaving its direct phage "
                "trigger, the DinA/DinB/DinC interaction sequence, the "
                "natural locus breadth, and the absence of pinned "
                "DefenseFinder HMM or rule rows unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Dionysus locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A three-gene Dionysus anti-phage defense locus "
                        "encoding DinA, DinB, and DinC components."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Dionysus system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Dionysus system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Dionysus "
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
                        "The three-gene Dionysus locus restricts infection "
                        "by jumbo phages."
                    ),
                    "evidence": [
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_JUMBO_SPECIFIC_SNIPPET,
                            "notes": (
                                "Keesman et al. report that Dionysus blocks "
                                "infection by jumbo phages."
                            ),
                        },
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_REQUIREMENT_SNIPPET,
                            "notes": (
                                "Keesman et al. report that DinA, DinB, and "
                                "DinC perturbations reduce or abolish "
                                "Dionysus anti-phage activity."
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
                        "Dionysus-mediated phage restriction realizes the "
                        "Dionysus system trait."
                    ),
                    "evidence": [
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_EPI_SNIPPET,
                            "notes": (
                                "Keesman et al. connect Dionysus activity to "
                                "disruption of the jumbo-phage infection "
                                "cycle at an early vesicle stage."
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
                        "Dionysus system possession is a phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": KEESMAN,
                            "snippet": KEESMAN_VALIDATION_SNIPPET,
                            "notes": (
                                "Keesman et al. list Dionysus among "
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
            "discussion_id": "dionysus-jumbo-phage-mechanism-gap",
            "prompt": (
                "Resolve Dionysus phage triggers, EPI-vesicle pore "
                "formation, and model coverage before minting narrower "
                "Dionysus mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Keesman et al. support Dionysus as a three-gene "
                "anti-jumbo-phage system that disrupts the jumbo-phage EPI "
                "vesicle stage, but the direct phage trigger, exact "
                "DinA/DinB/DinC interaction sequence, natural locus breadth, "
                "and profile-to-component model are not resolved enough here "
                "to assert a narrower mechanistic child trait."
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
            "Minted Dionysus system as a DOI-backed GENOMICS TraitRecord "
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
