#!/usr/bin/env python3
"""Add the Prometheus system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "prometheus_system.yaml"

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
TIMESTAMP = "2026-09-19T20:12:30Z"

IDENTIFIER = "traitmech:000291"
SYSTEM = "Prometheus"
SLUG = "prometheus"
HMM = "Prometheus__ProA"
PROPOSAL = "proposals/metpo_traitmech_v168"
EMPTY_HMM_NAME = ""


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{HMM:<48} | {EMPTY_HMM_NAME:<48} | {SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records "
            f"{HMM} in the {SYSTEM} model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": f"{SYSTEM} system",
    "definition": (
        f"A phage defense system in which an organism possesses a {SYSTEM} "
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
            "source": DEFENSEFINDER_ARTICLES,
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
                f"that does not assert a resolved {SYSTEM} trigger, effector "
                "output, or universal pathway."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                f"{SYSTEM} | 10\\.1016/j\\.chom\\.2024\\.07\\.007 | Bacterial "
                "homologs of innate eukaryotic antiviral defenses with "
                "anti-phage activity highlight shared evolutionary roots of "
                "viral defenses"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named "
                f"{SYSTEM} system to the van den Berg et al. antiphage-system "
                "discovery paper."
            ),
        },
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": f"{SYSTEM} loci confer bacterial phage defense",
            "description": (
                f"Conservative system-level sketch linking possession of a {SYSTEM} "
                "locus to restricted bacteriophage propagation without asserting "
                "the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                f"The graph captures {SYSTEM} as a named anti-phage system with a "
                f"{HMM} DefenseFinder HMM profile entry while leaving its phage "
                "trigger, molecular substrate, antiviral effector output, and "
                "subtype breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": f"{SYSTEM} locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        f"A {SYSTEM} anti-phage defense locus cataloged in "
                        f"DefenseFinder with a {HMM} HMM profile entry."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        f"carrying the {SYSTEM} system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": f"{SYSTEM} system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        f"Possession of a genome-encoded {SYSTEM} "
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
                        f"DefenseFinder maps {SYSTEM} to a eukaryotic-antiviral-"
                        "homolog antiphage-system discovery paper and catalogs "
                        f"a {HMM} HMM profile entry in the {SYSTEM} model "
                        "namespace."
                    ),
                    "evidence": [
                        {
                            "reference": VAN_DEN_BERG,
                            "snippet": VAN_DEN_BERG_VALIDATED_SYSTEMS_SNIPPET,
                            "notes": (
                                "van den Berg et al. place Prometheus in a "
                                "discovery cohort of validated phage defense "
                                "systems related to eukaryotic innate immunity."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Prometheus | 10\\.1016/j\\.chom\\.2024\\.07"
                                "\\.007 | Bacterial homologs of innate "
                                "eukaryotic antiviral defenses with anti-phage "
                                "activity highlight shared evolutionary roots "
                                "of viral defenses"
                            ),
                            "notes": (
                                "The DefenseFinder registry maps Prometheus "
                                "itself to the van den Berg et al. bacterial "
                                "antiphage-system discovery paper."
                            ),
                        },
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        f"{SYSTEM}-mediated phage restriction realizes the "
                        f"{SYSTEM} system trait."
                    ),
                    "evidence": [
                        {
                            "reference": VAN_DEN_BERG,
                            "snippet": VAN_DEN_BERG_VALIDATED_SYSTEMS_SNIPPET,
                            "notes": (
                                "van den Berg et al. validated six phage defense "
                                "systems related to eukaryotic antiviral "
                                "responses."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Prometheus | 10\\.1016/j\\.chom\\.2024\\.07"
                                "\\.007 | Bacterial homologs of innate "
                                "eukaryotic antiviral defenses with anti-phage "
                                "activity highlight shared evolutionary roots "
                                "of viral defenses"
                            ),
                            "notes": (
                                "DefenseFinder records Prometheus as a named "
                                "system from the van den Berg et al. antiphage "
                                "discovery paper."
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
                        f"{SYSTEM} system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "| Prometheus | 10\\.1016/j\\.chom\\.2024\\.07"
                                "\\.007 | Bacterial homologs of innate "
                                "eukaryotic antiviral defenses with anti-phage "
                                "activity highlight shared evolutionary roots "
                                "of viral defenses |"
                            ),
                            "notes": (
                                "DefenseFinder associates Prometheus with the "
                                "van den Berg et al. bacterial antiphage-system "
                                "discovery paper."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": f"{SLUG}-mechanism-gap",
            "prompt": (
                f"Resolve {SYSTEM} phage triggers and effector outputs before "
                f"minting narrower {SYSTEM} mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                f"van den Berg et al. and DefenseFinder support {SYSTEM} as a "
                f"named anti-phage system with a {HMM} HMM profile entry, but "
                "the trigger, molecular substrate, antiviral effector output, "
                "and subtype-specific mechanism are not resolved enough here "
                "to assert a narrower mechanistic child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
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
            f"Minted {SYSTEM} system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
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
