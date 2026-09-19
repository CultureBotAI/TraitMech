#!/usr/bin/env python3
"""Add the Viperin system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "viperin_system.yaml"

BERNHEIM = "DOI:10.1038/s41586-020-2762-2"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)
DEFENSEFINDER_RULES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/DefenseFinder_rules.tsv"
)
DEFENSEFINDER_HMMS = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/Liste_hmm_system.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-19T03:43:00Z"

PROFILES = ("pVip",)


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    hmm = f"Viperin__{profile}"
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{hmm:<48} | {hmm:<48} | Viperin",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{profile} in the Viperin model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000263",
    "label": "Viperin system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "prokaryotic viperin locus represented by a pVip profile that can "
        "produce antiviral modified ribonucleotides and protect against "
        "phage infection."
    ),
    "definition_source": BERNHEIM,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Viperin",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "pVip",
            "synonym_type": "RELATED_SYNONYM",
            "source": BERNHEIM,
        },
    ],
    "evidence": [
        {
            "reference": BERNHEIM,
            "snippet": (
                "Here we show that eukaryotic viperin originated from a "
                "clade of bacterial and archaeal proteins that protect "
                "against phage infection"
            ),
            "notes": (
                "Bernheim et al. support treating prokaryotic viperins as "
                "bacterial and archaeal phage-protective proteins rather "
                "than only as an animal antiviral factor."
            ),
        },
        {
            "reference": BERNHEIM,
            "snippet": (
                "Prokaryotic viperins produce a set of modified "
                "ribonucleotides"
            ),
            "notes": (
                "Bernheim et al. support modified ribonucleotide synthesis "
                "as a recurring output of prokaryotic viperin proteins."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Viperin | 10\\.1038/s41586-020-2762-2 | Prokaryotic "
                "viperins produce diverse antiviral molecules"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named Viperin "
                "system to the Bernheim et al. prokaryotic viperin paper."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": "Viperin\tViperin\t1\t1\tViperin__pVip",
            "notes": (
                "The DefenseFinder rules table models Viperin with a pVip "
                "profile."
            ),
        },
        *(hmm_inventory_evidence(profile) for profile in PROFILES),
    ],
    "causal_graphs": [
        {
            "graph_id": "viperin_modified_ribonucleotides_restrict_phage",
            "title": "Prokaryotic viperins produce antiviral ribonucleotides",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "prokaryotic viperin locus to modified ribonucleotide "
                "production and inhibited phage transcription."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures characterized pVip-mediated modified "
                "ribonucleotide production and T7 transcription inhibition "
                "without asserting one universal nucleotide product, viral "
                "polymerase target, accessory-gene architecture, or phage "
                "range across all Viperin loci."
            ),
            "nodes": [
                {
                    "node_id": "viperin_locus",
                    "label": "Viperin locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A prokaryotic viperin phage-defense locus "
                        "satisfying a DefenseFinder rule over the pVip "
                        "profile."
                    ),
                },
                {
                    "node_id": "modified_ribonucleotide_production",
                    "label": "modified ribonucleotide production",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Production of modified ribonucleotides by "
                        "prokaryotic viperin enzymes."
                    ),
                },
                {
                    "node_id": "t7_phage_transcription_inhibition",
                    "label": "T7 phage transcription inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Inhibition of T7 phage "
                        "polymerase-dependent transcription."
                    ),
                },
                {
                    "node_id": "viperin_system_trait",
                    "label": "Viperin system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000263",
                    "description": (
                        "Possession of a genome-encoded prokaryotic viperin "
                        "phage-defense locus."
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
                    "subject": "viperin_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "modified_ribonucleotide_production",
                    "description": (
                        "The Viperin locus encodes a pVip-class radical-SAM "
                        "enzyme that produces modified ribonucleotides."
                    ),
                    "evidence": [
                        {
                            "reference": BERNHEIM,
                            "snippet": (
                                "Prokaryotic viperins produce a set of "
                                "modified ribonucleotides"
                            ),
                            "notes": (
                                "Bernheim et al. support modified "
                                "ribonucleotide production as a pVip output."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": "Viperin\tViperin\t1\t1\tViperin__pVip",
                            "notes": (
                                "The DefenseFinder rules table supports pVip "
                                "as the required Viperin system profile."
                            ),
                        },
                    ],
                },
                {
                    "subject": "modified_ribonucleotide_production",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "t7_phage_transcription_inhibition",
                    "description": (
                        "Prokaryotic viperin products can inhibit "
                        "T7 phage polymerase-dependent transcription."
                    ),
                    "evidence": [
                        {
                            "reference": BERNHEIM,
                            "snippet": (
                                "prokaryotic viperins protect against T7 "
                                "phage infection by inhibiting viral "
                                "polymerase-dependent transcription"
                            ),
                            "notes": (
                                "Bernheim et al. connect prokaryotic "
                                "viperin activity to inhibition of T7 "
                                "transcription."
                            ),
                        }
                    ],
                },
                {
                    "subject": "t7_phage_transcription_inhibition",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "viperin_system_trait",
                    "description": (
                        "Inhibition of phage transcription is a source-backed "
                        "antiviral output that realizes the Viperin system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": BERNHEIM,
                            "snippet": (
                                "prokaryotic viperins protect against T7 "
                                "phage infection by inhibiting viral "
                                "polymerase-dependent transcription"
                            ),
                            "notes": (
                                "Bernheim et al. support pVip-mediated "
                                "protection from T7 phage infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "viperin_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Viperin system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BERNHEIM,
                            "snippet": (
                                "Here we show that eukaryotic viperin "
                                "originated from a clade of bacterial and "
                                "archaeal proteins that protect against "
                                "phage infection"
                            ),
                            "notes": (
                                "Bernheim et al. support Viperin as a "
                                "prokaryotic phage-defense system."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "viperin-product-and-subtype-gap",
            "prompt": (
                "Resolve Viperin nucleotide products, accessory genes, and "
                "phage-target breadth before minting narrower Viperin "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Bernheim et al. support prokaryotic viperins as "
                "phage-protective producers of modified ribonucleotides, "
                "and DefenseFinder models Viperin through the pVip profile, "
                "but Viperin-family loci need separate review before "
                "TraitMech asserts one universal antiviral nucleotide, "
                "polymerase target, or accessory-gene architecture."
            ),
            "attaches_to": [
                "causal_graphs#viperin_modified_ribonucleotides_restrict_phage"
            ],
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
            "Minted Viperin system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v140."
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
