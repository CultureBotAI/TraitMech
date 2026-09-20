#!/usr/bin/env python3
"""Add the JukAB system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "jukab_system.yaml"

LI_FINAL = "DOI:10.1016/j.cell.2025.02.016"
LI_PREPRINT = "DOI:10.1101/2022.09.17.508391"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T08:47:10Z"

JUKA_ROW = (
    "| JukAB__JukA                                      | "
    "JukAB__JukA                                      | JukAB                  | "
    "Custom                  | 20     |"
)
JUKB_ROW = (
    "| JukAB__JukB                                      | "
    "JukAB__JukB                                      | JukAB                  | "
    "Custom                  | 20     |"
)


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000305",
    "label": "JukAB system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "two-gene jukAB locus encoding a JukA sensor that binds a "
        "PhiKZ-like gp241 early phage protein at the EPI vesicle and "
        "directly recruits the pore-forming-toxin-like JukB effector to "
        "destabilize the vesicle, suppress early phage gene expression, and "
        "prevent phage DNA replication and nucleus assembly."
    ),
    "definition_source": LI_FINAL,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "JukAB",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "jumbo phage killer",
            "synonym_type": "RELATED_SYNONYM",
            "source": LI_FINAL,
        },
    ],
    "evidence": [
        {
            "reference": LI_FINAL,
            "snippet": (
                "a two-component immune system that terminates infection of "
                "φKZ-like phages"
            ),
            "notes": (
                "Li et al. define Juk as a two-component immune system "
                "that terminates PhiKZ-like jumbo-phage infection."
            ),
        },
        {
            "reference": LI_PREPRINT,
            "snippet": (
                "jukA and jukB together, but not either gene alone, "
                "conferred resistance against"
            ),
            "notes": (
                "Li et al. show that the JukA sensor and JukB effector are "
                "jointly required for heterologous PhiKZ resistance."
            ),
        },
        {
            "reference": LI_FINAL,
            "snippet": (
                "JukA (formerly YaaW) rapidly senses the EPI vesicle by "
                "binding to an early-expressed phage protein, gp241, and "
                "then directly recruits JukB"
            ),
            "notes": (
                "Li et al. identify JukA binding to the PhiKZ-like early "
                "phage protein gp241 at the EPI vesicle as the JukAB input "
                "that recruits JukB."
            ),
        },
        {
            "reference": LI_FINAL,
            "snippet": (
                "The JukB effector structurally resembles a pore-forming "
                "toxin and destabilizes the EPI vesicle"
            ),
            "notes": (
                "Li et al. connect the recruited JukB effector to "
                "destabilization of the early phage infection vesicle."
            ),
        },
        {
            "reference": LI_FINAL,
            "snippet": (
                "suppressing the expression of early phage genes and "
                "preventing phage DNA replication and phage nucleus assembly "
                "while saving the cell"
            ),
            "notes": (
                "Li et al. describe the downstream anti-phage outcome of "
                "two-component Juk immunity."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "JukAB | 10\\.1101/2022\\.09\\.17\\.508391 | A family of "
                "novel immune systems targets early infection of "
                "nucleus-forming jumbo phages"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named JukAB "
                "system to the Li et al. Juk immune-system preprint."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": "JukAB\tJukAB\t2\t2\tJukAB__JukA, JukAB__JukB",
            "notes": (
                "The DefenseFinder rules table models JukAB as a "
                "two-component system requiring JukAB__JukA and "
                "JukAB__JukB profiles."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": JUKA_ROW,
            "notes": (
                "The DefenseFinder HMM inventory records JukAB__JukA under "
                "the JukAB model namespace."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": JUKB_ROW,
            "notes": (
                "The DefenseFinder HMM inventory records JukAB__JukB under "
                "the JukAB model namespace."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "note": (
                "Li et al. discovered the native jukA-jukB operon in "
                "Pseudomonas aeruginosa PA14 and showed that the two-gene "
                "Juk locus provides immunity against PhiKZ-related "
                "nucleus-forming jumbo phages."
            ),
            "reference": LI_PREPRINT,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "jukab_recruits_effector_to_block_jumbo_phage",
            "title": "JukAB blocks early jumbo-phage infection",
            "description": (
                "Conservative system-level sketch linking a jukAB locus to "
                "gp241/EPI-vesicle sensing by JukA, JukB recruitment, "
                "JukB-mediated EPI-vesicle destabilization, suppression of "
                "early PhiKZ-like jumbo-phage development, and JukAB system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures JukAB as a named DefenseFinder "
                "two-profile system in which JukA binds the PhiKZ gp241 "
                "early phage protein at the EPI vesicle and recruits JukB "
                "to destabilize that vesicle. It summarizes the direct "
                "two-component system without minting separate sequence "
                "feature traits for jukA, jukB, gp241, or other "
                "JukA-associated effector families."
            ),
            "nodes": [
                {
                    "node_id": "jukab_locus",
                    "label": "jukAB locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene locus encoding JukA and JukB and "
                        "represented by the DefenseFinder JukAB rule."
                    ),
                },
                {
                    "node_id": "jukA_phage_ejected_factor_sensing",
                    "label": "JukA gp241 EPI-vesicle sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Binding of the JukA sensor to PhiKZ-like gp241 at "
                        "the early phage infection vesicle."
                    ),
                },
                {
                    "node_id": "jukB_effector_recruitment",
                    "label": "JukB effector recruitment",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "JukA-dependent recruitment of the JukB effector to "
                        "the phage infection site."
                    ),
                },
                {
                    "node_id": "early_jumbo_phage_progression",
                    "label": "early jumbo-phage progression",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Early phage transcription, DNA replication, and "
                        "nucleus assembly during infection by a "
                        "nucleus-forming jumbo phage."
                    ),
                },
                {
                    "node_id": "epi_vesicle_destabilization",
                    "label": "EPI vesicle destabilization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "JukB-associated destabilization of the lipid-based "
                        "early phage infection vesicle."
                    ),
                },
                {
                    "node_id": "jukab_system_trait",
                    "label": "JukAB system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000305",
                    "description": (
                        "Possession of a genome-encoded JukAB "
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
                    "subject": "jukab_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "jukA_phage_ejected_factor_sensing",
                    "description": (
                        "The JukAB locus encodes JukA, the sensor that "
                        "binds the early phage protein gp241 at the EPI "
                        "vesicle."
                    ),
                    "evidence": [
                        {
                            "reference": LI_FINAL,
                            "snippet": (
                                "JukA (formerly YaaW) rapidly senses the EPI "
                                "vesicle by binding to an early-expressed "
                                "phage protein, gp241"
                            ),
                            "notes": (
                                "Li et al. identify gp241/EPI-vesicle binding "
                                "by JukA as the characterized JukAB sensor "
                                "input."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": (
                                "JukAB\tJukAB\t2\t2\tJukAB__JukA, "
                                "JukAB__JukB"
                            ),
                            "notes": (
                                "DefenseFinder requires the JukA profile in "
                                "its JukAB system rule."
                            ),
                        },
                    ],
                },
                {
                    "subject": "jukA_phage_ejected_factor_sensing",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "jukB_effector_recruitment",
                    "description": (
                        "JukA sensing of gp241 at the EPI vesicle directly "
                        "recruits the JukB effector."
                    ),
                    "evidence": [
                        {
                            "reference": LI_FINAL,
                            "snippet": (
                                "JukA (formerly YaaW) rapidly senses the EPI "
                                "vesicle by binding to an early-expressed "
                                "phage protein, gp241, and then directly "
                                "recruits JukB"
                            ),
                            "notes": (
                                "Li et al. place direct JukB recruitment "
                                "downstream of JukA-gp241 binding at the EPI "
                                "vesicle."
                            ),
                        }
                    ],
                },
                {
                    "subject": "jukB_effector_recruitment",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "epi_vesicle_destabilization",
                    "description": (
                        "Recruited JukB is a pore-forming-toxin-like "
                        "effector that destabilizes the EPI vesicle."
                    ),
                    "evidence": [
                        {
                            "reference": LI_FINAL,
                            "snippet": (
                                "The JukB effector structurally resembles a "
                                "pore-forming toxin and destabilizes the EPI "
                                "vesicle"
                            ),
                            "notes": (
                                "Li et al. connect JukB to the vesicle "
                                "destabilization step of JukAB immunity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "epi_vesicle_destabilization",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "early_jumbo_phage_progression",
                    "description": (
                        "EPI-vesicle destabilization by the JukAB response "
                        "blocks early jumbo-phage gene expression, DNA "
                        "replication, and nucleus assembly."
                    ),
                    "evidence": [
                        {
                            "reference": LI_FINAL,
                            "snippet": (
                                "suppressing the expression of early phage "
                                "genes and preventing phage DNA replication "
                                "and phage nucleus assembly while saving the "
                                "cell"
                            ),
                            "notes": (
                                "Li et al. define the anti-phage output of "
                                "the two-component Juk system."
                            ),
                        },
                    ],
                },
                {
                    "subject": "epi_vesicle_destabilization",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "jukab_system_trait",
                    "description": (
                        "JukB-associated EPI-vesicle destabilization "
                        "realizes the JukAB defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": LI_FINAL,
                            "snippet": (
                                "a two-component immune system that "
                                "terminates infection of φKZ-like phages"
                            ),
                            "notes": (
                                "Li et al. frame two-component Juk as an "
                                "immune system that terminates PhiKZ-like "
                                "phage infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "jukab_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "JukAB system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "JukAB | 10\\.1101/2022\\.09\\.17\\.508391 "
                                "| A family of novel immune systems targets "
                                "early infection of nucleus-forming jumbo "
                                "phages"
                            ),
                            "notes": (
                                "DefenseFinder associates JukAB with the Li "
                                "et al. nucleus-forming-jumbo-phage immune "
                                "system paper."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "jukab-vesicle-effector-family-gap",
            "prompt": (
                "Resolve JukB vesicle-destabilization chemistry and the "
                "boundaries of other JukA-containing systems before minting "
                "narrower mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Li et al. resolve gp241/EPI-vesicle sensing by JukA and "
                "direct recruitment of JukB as a two-component JukAB "
                "strategy, but the exact chemistry of JukB-mediated vesicle "
                "destabilization and the relationship between canonical "
                "JukAB and JukA homologs paired with diverse other putative "
                "effectors still need narrower review."
            ),
            "attaches_to": ["causal_graphs#jukab_recruits_effector_to_block_jumbo_phage"],
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
            "Minted JukAB system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v182."
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
