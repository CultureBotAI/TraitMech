#!/usr/bin/env python3
"""Add the Brc24 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "brc24_system.yaml"

KIEFFER = "DOI:10.1126/science.ads0915"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T13:34:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-10-01T13:34:01Z"
IDENTIFIER = "traitmech:000516"
PROPOSAL = "proposals/metpo_traitmech_v393"

GCU24_SCREEN_SNIPPET = "Identification of gcu24 and gcu142 through double spot screening"
GCU24_T4_RESISTANCE_SNIPPET = (
    "gcu24 and gcu142, which show growth despite the presence of the phage, "
    "indicating successful identification and resistance."
)
BRIC_PROFILE_SNIPPET = (
    "defense profiles of identified Bacteriophage Resistance integron "
    "Cassettes (BRiCs) against a panel of different phages"
)
GCU24_SCREENING_CONSTRUCT_SNIPPET = "C747\npMBA gcu24"
BRC24_ECOLI_CONSTRUCT_SNIPPET = "C806\npMBA brc24\nE. coli IJ1862"
BRC24_KPNEUMONIAE_CONSTRUCT_SNIPPET = "C816\npMBA brc24\nK. pneumoniae"
BRC24_PAERUGINOSA_CONSTRUCT_SNIPPET = "C971\npBTZ PcW brc24"
ARTICLE_ROW = (
    "| gcu24 | 10\\.1126/science\\.ads0915 | Mobile integrons "
    "encode phage defense systems | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the gcu24 source "
            "key to the Kieffer et al. mobile-integron BRiC paper."
        ),
    }


def screening_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": GCU24_SCREEN_SNIPPET,
        "notes": (
            "Kieffer et al. report initial identification of gcu24 in a "
            "double-spot phage-resistance screen."
        ),
    }


def t4_resistance_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": GCU24_T4_RESISTANCE_SNIPPET,
        "notes": (
            "Kieffer et al. support growth of the gcu24 clone during T4 "
            "phage challenge in the initial screen."
        ),
    }


def bric_panel_evidence() -> dict[str, str]:
    return {
        "reference": KIEFFER,
        "snippet": BRIC_PROFILE_SNIPPET,
        "notes": (
            "Kieffer et al. classify positive integron cassettes as BRiCs and "
            "compare their defense profiles across a phage panel."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Brc24 system",
    "definition": (
        "A phage defense system in which an organism possesses a gcu24/Brc24 "
        "bacteriophage-resistance integron cassette that supports growth "
        "during bacteriophage challenge."
    ),
    "definition_source": KIEFFER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "gcu24",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "brc24",
            "synonym_type": "RELATED_SYNONYM",
            "source": KIEFFER,
        },
    ],
    "evidence": [
        screening_evidence(),
        t4_resistance_evidence(),
        bric_panel_evidence(),
        {
            "reference": KIEFFER,
            "snippet": GCU24_SCREENING_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists the "
                "initial pMBA gcu24 screening plasmid."
            ),
        },
        {
            "reference": KIEFFER,
            "snippet": BRC24_ECOLI_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists pMBA "
                "brc24 in E. coli IJ1862 for high/low-MOI phage-panel "
                "testing."
            ),
        },
        {
            "reference": KIEFFER,
            "snippet": BRC24_KPNEUMONIAE_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists the "
                "pMBA brc24 plasmid introduced into Klebsiella pneumoniae "
                "KP5."
            ),
        },
        {
            "reference": KIEFFER,
            "snippet": BRC24_PAERUGINOSA_CONSTRUCT_SNIPPET,
            "notes": (
                "Kieffer et al.'s supplementary construct table lists a "
                "Pseudomonas aeruginosa brc24 expression construct."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "brc24_integron_cassette_confers_phage_resistance",
            "title": "Brc24 BRiCs confer phage resistance",
            "description": (
                "Conservative system-level sketch linking a gcu24/Brc24 "
                "bacteriophage-resistance integron cassette to phage "
                "resistance and Brc24 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Brc24 at the integron-cassette and "
                "phage-resistance-output level without asserting the native "
                "host range, exact sensitive-phage breadth outside the "
                "reported panels, direct molecular substrate, or a "
                "DefenseFinder HMM/rules profile absent from the pinned "
                "snapshot."
            ),
            "nodes": [
                {
                    "node_id": "brc24_integron_cassette",
                    "label": "Brc24 integron cassette",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A mobile integron gene cassette recovered in the "
                        "gcu24 screen and renamed as a Brc24 "
                        "bacteriophage-resistance integron cassette."
                    ),
                },
                {
                    "node_id": "brc24_phage_resistance",
                    "label": "Brc24 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage inhibition in cells carrying the "
                        "gcu24/Brc24 integron cassette."
                    ),
                },
                {
                    "node_id": "brc24_system_trait",
                    "label": "Brc24 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Brc24 "
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
                    "subject": "brc24_integron_cassette",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "brc24_phage_resistance",
                    "description": (
                        "The gcu24/Brc24 integron cassette contributes to "
                        "phage resistance during double-spot and phage-panel "
                        "assays."
                    ),
                    "evidence": [
                        screening_evidence(),
                        {
                            "reference": KIEFFER,
                            "snippet": BRC24_ECOLI_CONSTRUCT_SNIPPET,
                            "notes": (
                                "Kieffer et al. cloned brc24 for E. coli "
                                "IJ1862 phage-panel testing."
                            ),
                        },
                    ],
                },
                {
                    "subject": "brc24_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "brc24_system_trait",
                    "description": (
                        "Brc24-linked phage resistance realizes the "
                        "Brc24 system possession trait."
                    ),
                    "evidence": [
                        t4_resistance_evidence(),
                        bric_panel_evidence(),
                    ],
                },
                {
                    "subject": "brc24_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Brc24 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        bric_panel_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "brc24-defensefinder-model-gap",
            "prompt": (
                "Resolve Brc24 native host breadth, exact sensitive-phage "
                "breadth, molecular output, and DefenseFinder HMM/rules "
                "coverage before minting narrower Brc24 mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Kieffer et al. identify gcu24/Brc24 as a "
                "bacteriophage-resistance integron cassette, and the pinned "
                "DefenseFinder article registry maps the gcu24 source key "
                "to the same Science article. The pinned HMM inventory and "
                "rules table have no exact gcu24 or Brc24 row, so the "
                "first-pass record leaves native-host breadth, profile "
                "boundaries, exact phage target breadth, and direct "
                "molecular output unresolved."
            ),
            "evidence": [
                screening_evidence(),
                bric_panel_evidence(),
                {
                    "reference": KIEFFER,
                    "snippet": BRC24_KPNEUMONIAE_CONSTRUCT_SNIPPET,
                    "notes": (
                        "Kieffer et al. list brc24 in the heterologous "
                        "Klebsiella pneumoniae KP5 BRiC panel."
                    ),
                },
                {
                    "reference": KIEFFER,
                    "snippet": BRC24_PAERUGINOSA_CONSTRUCT_SNIPPET,
                    "notes": (
                        "Kieffer et al. list brc24 in the heterologous "
                        "Pseudomonas aeruginosa PAO1 BRiC panel."
                    ),
                },
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder HMM inventory found no exact gcu24, "
                        "brc24, or Brc24 row."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "A structured first-pass search of the pinned "
                        "DefenseFinder rules table found no exact gcu24, "
                        "brc24, or Brc24 system row."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#brc24_integron_cassette_confers_phage_resistance"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
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
            "Minted Brc24 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; kept the "
            "graph at BRiC integron-cassette level because the pinned "
            "DefenseFinder article registry names gcu24 but the pinned HMM "
            "inventory and rules table have no exact Brc24 row; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed Brc24 system during initial curation and left "
            "canonical_examples empty because the sources support "
            "heterologous gcu24/Brc24 phage-resistance assays and a "
            "DefenseFinder gcu24 article row, but not a direct named native "
            "microbial isolate exemplar with experimentally verified "
            "endogenous Brc24 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
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
