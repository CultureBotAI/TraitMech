#!/usr/bin/env python3
"""Add the dGTPase system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dgtpase_system.yaml"

TAL = "DOI:10.1101/2021.04.26.441389"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-19T10:46:26Z"

PROFILE = "dGTPase__Sp_dGTPase"


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{PROFILE:<48} | {PROFILE:<48} | dGTPase",
        "notes": (
            "The DefenseFinder HMM inventory records the custom Sp_dGTPase "
            "profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000276",
    "label": "dGTPase system",
    "definition": (
        "A phage defense system in which an organism possesses a dGTPase "
        "locus that degrades dGTP into phosphate-free deoxy-guanosine during "
        "phage infection, depletes dGTP from the nucleotide pool, and halts "
        "phage replication by starving the phage of an essential DNA building "
        "block."
    ),
    "definition_source": TAL,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "dGTPase",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": TAL,
            "snippet": (
                "bacteria employ a similar strategy to defend against phage "
                "infection"
            ),
            "notes": (
                "Tal et al. support nucleotide depletion as a bacterial "
                "anti-phage strategy."
            ),
        },
        {
            "reference": TAL,
            "snippet": (
                "A second family of phage resistance genes encode dGTPase "
                "enzymes, which degrade dGTP into phosphate-free "
                "deoxy-guanosine (dG)"
            ),
            "notes": (
                "Tal et al. support dGTPase genes as phage-resistance genes "
                "encoding enzymes that degrade dGTP."
            ),
        },
        {
            "reference": TAL,
            "snippet": (
                "completely eliminate the specific deoxynucleotide (either "
                "dCTP or dGTP) from the nucleotide pool during phage infection"
            ),
            "notes": (
                "Tal et al. connect dGTPase defense to dGTP nucleotide-pool "
                "elimination during phage infection."
            ),
        },
        {
            "reference": TAL,
            "snippet": (
                "starving the phage of an essential DNA building block and "
                "halting its replication"
            ),
            "notes": (
                "Tal et al. connect defensive deoxynucleotide depletion to "
                "phage DNA-building-block starvation and replication arrest."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "dGTPase | 10\\.1101/2021\\.04\\.26\\.441389 | Antiviral "
                "defense via nucleotide depletion in bacteria"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named dGTPase "
                "system to the Tal et al. nucleotide-depletion preprint."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": "dGTPase\tdGTPase\t1\t1\tdGTPase__Sp_dGTPase",
            "notes": (
                "The DefenseFinder rules table models dGTPase as a "
                "single-profile system."
            ),
        },
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "dgtpase_dgtp_depletion_defense",
            "title": "dGTPase loci deplete dGTP during phage infection",
            "description": (
                "Process sketch linking a dGTPase locus to dGTP degradation, "
                "dGTP depletion, phage DNA-building-block starvation, halted "
                "phage replication, and the dGTPase system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the DOI abstract's dGTPase-mediated dGTP "
                "degradation and nucleotide-depletion output without asserting "
                "a universal phage sensor, activation route, strain-resolved "
                "enzyme accession, or complete substrate scope for every "
                "natural dGTPase system."
            ),
            "nodes": [
                {
                    "node_id": "dgtpase_locus",
                    "label": "dGTPase locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A dGTPase anti-phage defense locus represented by a "
                        "custom DefenseFinder Sp_dGTPase profile."
                    ),
                },
                {
                    "node_id": "dgtp_degradation",
                    "label": "dGTP degradation into deoxy-guanosine",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Degradation of dGTP into phosphate-free "
                        "deoxy-guanosine by defensive dGTPase enzymes."
                    ),
                },
                {
                    "node_id": "dgtp_depletion",
                    "label": "dGTP nucleotide-pool depletion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Elimination of dGTP from the nucleotide pool during "
                        "dGTPase-mediated defense."
                    ),
                },
                {
                    "node_id": "phage_dna_building_block_starvation",
                    "label": "phage DNA-building-block starvation",
                    "node_type": "STATE",
                    "description": (
                        "Deprivation of an essential deoxynucleotide needed "
                        "for phage DNA synthesis."
                    ),
                },
                {
                    "node_id": "halted_phage_replication",
                    "label": "halted phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Arrest of bacteriophage replication after dGTP "
                        "depletion."
                    ),
                },
                {
                    "node_id": "dgtpase_system_trait",
                    "label": "dGTPase system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000276",
                    "description": (
                        "Possession of a genome-encoded dGTPase phage-defense "
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
                    "subject": "dgtpase_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dgtp_degradation",
                    "description": (
                        "The dGTPase locus encodes dGTPase activity that "
                        "degrades dGTP into phosphate-free deoxy-guanosine."
                    ),
                    "evidence": [
                        {
                            "reference": TAL,
                            "snippet": (
                                "dGTPase enzymes, which degrade dGTP into "
                                "phosphate-free deoxy-guanosine (dG)"
                            ),
                            "notes": (
                                "Tal et al. identify dGTPase enzymes that "
                                "degrade dGTP."
                            ),
                        },
                        {
                            **hmm_inventory_evidence(),
                            "notes": (
                                "DefenseFinder models the Sp_dGTPase protein "
                                "profile used to identify the dGTPase system."
                            ),
                        },
                    ],
                },
                {
                    "subject": "dgtp_degradation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dgtp_depletion",
                    "description": (
                        "Degradation of dGTP depletes the host dGTP nucleotide "
                        "pool during phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": TAL,
                            "snippet": (
                                "completely eliminate the specific "
                                "deoxynucleotide (either dCTP or dGTP) from "
                                "the nucleotide pool during phage infection"
                            ),
                            "notes": (
                                "Tal et al. connect defensive dGTPase activity "
                                "to loss of dGTP from the nucleotide pool."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dgtp_depletion",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_dna_building_block_starvation",
                    "description": (
                        "dGTP depletion starves the infecting phage of an "
                        "essential DNA building block."
                    ),
                    "evidence": [
                        {
                            "reference": TAL,
                            "snippet": (
                                "starving the phage of an essential DNA "
                                "building block"
                            ),
                            "notes": (
                                "Tal et al. support phage DNA-building-block "
                                "starvation as the output of defensive "
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
                        "Starvation for dGTP halts phage DNA replication."
                    ),
                    "evidence": [
                        {
                            "reference": TAL,
                            "snippet": (
                                "starving the phage of an essential DNA "
                                "building block and halting its replication"
                            ),
                            "notes": (
                                "Tal et al. place phage-replication arrest "
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
                    "object": "dgtpase_system_trait",
                    "description": (
                        "dGTPase-mediated arrest of phage replication realizes "
                        "the dGTPase system trait."
                    ),
                    "evidence": [
                        {
                            "reference": TAL,
                            "snippet": (
                                "bacteria employ a similar strategy to defend "
                                "against phage infection"
                            ),
                            "notes": (
                                "Tal et al. support dGTP depletion as a "
                                "bacterial phage-defense strategy."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dgtpase_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "dGTPase system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "dGTPase | 10\\.1101/2021\\.04\\.26\\.441389 "
                                "| Antiviral defense via nucleotide depletion "
                                "in bacteria"
                            ),
                            "notes": (
                                "DefenseFinder associates dGTPase with the Tal "
                                "et al. bacterial antiviral "
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
            "discussion_id": "dgtpase-activation-profile-gap",
            "prompt": (
                "Resolve dGTPase activation, locus boundaries, and "
                "representative enzyme accessions before asserting narrower "
                "component or subtype traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Tal et al. support dGTPase as a phage-responsive "
                "dGTP-depletion defense and DefenseFinder models the system "
                "with a custom Sp_dGTPase HMM profile, but this first "
                "system-level record does not resolve the universal phage "
                "sensor, activation route, strain-level accessions, or whether "
                "additional unmodeled components define some natural loci."
            ),
            "attaches_to": ["causal_graphs#dgtpase_dgtp_depletion_defense"],
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
            "Minted dGTPase system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v153."
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
