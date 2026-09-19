#!/usr/bin/env python3
"""Add the dCTPdeaminase system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dctpdeaminase_system.yaml"

BERNIER = "DOI:10.1101/2021.04.26.441389"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-19T09:25:18Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000274",
    "label": "dCTPdeaminase system",
    "definition": (
        "A phage defense system in which an organism possesses a dCTPdeaminase "
        "locus that converts dCTP into deoxy-uracil nucleotides during phage "
        "infection, depletes dCTP from the nucleotide pool, and halts phage "
        "replication by starving the phage of an essential DNA building block."
    ),
    "definition_source": BERNIER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "dCTPdeaminase",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": BERNIER,
            "snippet": (
                "bacteria employ a similar strategy to defend against phage "
                "infection"
            ),
            "notes": (
                "Bernier et al. support nucleotide depletion as a bacterial "
                "anti-phage strategy."
            ),
        },
        {
            "reference": BERNIER,
            "snippet": (
                "a family of defensive dCTP deaminase proteins that, in "
                "response to phage infection, convert dCTP into deoxy-uracil "
                "nucleotides"
            ),
            "notes": (
                "Bernier et al. support the dCTPdeaminase family as a phage-"
                "responsive dCTP-conversion defense."
            ),
        },
        {
            "reference": BERNIER,
            "snippet": (
                "starving the phage of an essential DNA building block and "
                "halting its replication"
            ),
            "notes": (
                "Bernier et al. connect dCTP depletion to phage DNA-building-"
                "block starvation and replication arrest."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "dCTPdeaminase | 10\\.1101/2021\\.04\\.26\\.441389 | "
                "Antiviral defense via nucleotide depletion in bacteria"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named "
                "dCTPdeaminase system to the Bernier et al. nucleotide-"
                "depletion preprint."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": "dCTPdeaminase__dCTPdeaminase",
            "notes": (
                "The DefenseFinder rules table models dCTPdeaminase as a "
                "single-profile system."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": "dCTPdeaminase__dCTPdeaminase",
            "notes": (
                "The DefenseFinder HMM inventory records the custom "
                "dCTPdeaminase profile."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "dctpdeaminase_dctp_depletion_defense",
            "title": "dCTPdeaminase loci deplete dCTP during phage infection",
            "description": (
                "Process sketch linking a dCTPdeaminase locus to phage-"
                "responsive dCTP conversion, dCTP depletion, phage DNA-building-"
                "block starvation, halted phage replication, and the "
                "dCTPdeaminase system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the DOI abstract's phage-responsive dCTP "
                "conversion and nucleotide-depletion output without asserting a "
                "universal phage sensor, activation route, strain-resolved "
                "enzyme accession, or complete substrate scope for every natural "
                "dCTPdeaminase system."
            ),
            "nodes": [
                {
                    "node_id": "dctpdeaminase_locus",
                    "label": "dCTPdeaminase locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A dCTPdeaminase anti-phage defense locus represented "
                        "by a custom DefenseFinder dCTPdeaminase profile."
                    ),
                },
                {
                    "node_id": "sensitive_phage_infection",
                    "label": "sensitive phage infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Infection by a phage whose propagation can be blocked "
                        "by a dCTPdeaminase defense system."
                    ),
                },
                {
                    "node_id": "dctp_conversion",
                    "label": "dCTP conversion into deoxy-uracil nucleotides",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Conversion of dCTP into deoxy-uracil nucleotides by "
                        "defensive dCTP deaminase proteins during phage "
                        "infection."
                    ),
                },
                {
                    "node_id": "dctp_depletion",
                    "label": "dCTP nucleotide-pool depletion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Elimination of dCTP from the nucleotide pool during "
                        "dCTPdeaminase-mediated defense."
                    ),
                },
                {
                    "node_id": "phage_dna_building_block_starvation",
                    "label": "phage DNA-building-block starvation",
                    "node_type": "STATE",
                    "description": (
                        "Deprivation of an essential deoxynucleotide needed for "
                        "phage DNA synthesis."
                    ),
                },
                {
                    "node_id": "halted_phage_replication",
                    "label": "halted phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Arrest of bacteriophage replication after dCTP "
                        "depletion."
                    ),
                },
                {
                    "node_id": "dctpdeaminase_system_trait",
                    "label": "dCTPdeaminase system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000274",
                    "description": (
                        "Possession of a genome-encoded dCTPdeaminase phage-"
                        "defense system."
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
                    "subject": "dctpdeaminase_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dctp_conversion",
                    "description": (
                        "The dCTPdeaminase locus encodes the dCTP deaminase "
                        "activity that converts dCTP into deoxy-uracil "
                        "nucleotides."
                    ),
                    "evidence": [
                        {
                            "reference": BERNIER,
                            "snippet": (
                                "defensive dCTP deaminase proteins that, in "
                                "response to phage infection, convert dCTP"
                            ),
                            "notes": (
                                "Bernier et al. identify defensive dCTP "
                                "deaminase proteins that convert dCTP during "
                                "phage infection."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_HMMS,
                            "snippet": "dCTPdeaminase__dCTPdeaminase",
                            "notes": (
                                "DefenseFinder models the dCTPdeaminase "
                                "protein profile used to identify the system."
                            ),
                        },
                    ],
                },
                {
                    "subject": "sensitive_phage_infection",
                    "predicate": "triggers",
                    "object": "dctp_conversion",
                    "description": (
                        "Phage infection induces dCTP conversion by defensive "
                        "dCTP deaminase proteins."
                    ),
                    "evidence": [
                        {
                            "reference": BERNIER,
                            "snippet": "in response to phage infection, convert dCTP",
                            "notes": (
                                "Bernier et al. place dCTP conversion in the "
                                "phage-infection response."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dctp_conversion",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dctp_depletion",
                    "description": (
                        "Conversion of dCTP into deoxy-uracil nucleotides "
                        "depletes the host dCTP nucleotide pool."
                    ),
                    "evidence": [
                        {
                            "reference": BERNIER,
                            "snippet": (
                                "completely eliminate the specific "
                                "deoxynucleotide (either dCTP or dGTP) from "
                                "the nucleotide pool during phage infection"
                            ),
                            "notes": (
                                "Bernier et al. connect defensive dCTP "
                                "conversion to loss of dCTP from the "
                                "nucleotide pool."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dctp_depletion",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_dna_building_block_starvation",
                    "description": (
                        "dCTP depletion starves the infecting phage of an "
                        "essential DNA building block."
                    ),
                    "evidence": [
                        {
                            "reference": BERNIER,
                            "snippet": (
                                "starving the phage of an essential DNA "
                                "building block"
                            ),
                            "notes": (
                                "Bernier et al. support phage DNA-building-"
                                "block starvation as the output of defensive "
                                "deoxynucleotide depletion."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_dna_building_block_starvation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "halted_phage_replication",
                    "description": (
                        "Starvation for dCTP halts phage DNA replication."
                    ),
                    "evidence": [
                        {
                            "reference": BERNIER,
                            "snippet": (
                                "starving the phage of an essential DNA "
                                "building block and halting its replication"
                            ),
                            "notes": (
                                "Bernier et al. place phage-replication arrest "
                                "downstream of defensive deoxynucleotide "
                                "depletion."
                            ),
                        }
                    ],
                },
                {
                    "subject": "halted_phage_replication",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "dctpdeaminase_system_trait",
                    "description": (
                        "dCTPdeaminase-mediated arrest of phage replication "
                        "realizes the dCTPdeaminase system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BERNIER,
                            "snippet": "bacteria employ a similar strategy to defend against phage infection",
                            "notes": (
                                "Bernier et al. support dCTP depletion as a "
                                "bacterial phage-defense strategy."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dctpdeaminase_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "dCTPdeaminase system possession is a phage-defense-"
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "dCTPdeaminase | "
                                "10\\.1101/2021\\.04\\.26\\.441389 | "
                                "Antiviral defense via nucleotide depletion in "
                                "bacteria"
                            ),
                            "notes": (
                                "DefenseFinder associates dCTPdeaminase with "
                                "the Bernier et al. bacterial antiviral "
                                "nucleotide-depletion preprint."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "dctpdeaminase-activation-profile-gap",
            "prompt": (
                "Resolve dCTPdeaminase activation, locus boundaries, and "
                "representative enzyme accessions before asserting narrower "
                "component or subtype traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Bernier et al. support dCTPdeaminase as a phage-responsive "
                "dCTP-depletion defense and DefenseFinder models the system "
                "with a custom dCTPdeaminase HMM profile, but this first "
                "system-level record does not resolve the universal phage "
                "sensor, activation route, strain-level accessions, or whether "
                "additional unmodeled components define some natural loci."
            ),
            "attaches_to": ["causal_graphs#dctpdeaminase_dctp_depletion_defense"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-19",
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
            "Minted dCTPdeaminase system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an ignored-and-"
            "hidden duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is reserved "
            "in proposals/metpo_traitmech_v151."
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
