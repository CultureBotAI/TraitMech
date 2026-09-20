#!/usr/bin/env python3
"""Add the Butters gp57r system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "butters_gp57r_system.yaml"

MOHAMMED = "DOI:10.1101/2023.01.03.522681"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T02:22:02Z"

IDENTIFIER = "traitmech:000299"
SYSTEM = "Butters gp57r"
DEFENSEFINDER_SYSTEM = "Butters_gp57r"
SLUG = "butters_gp57r"
PROFILE = "Butters_gp57r__gp57r"
RULES_SNIPPET = "Butters_gp57r\tButters_gp57r\t1\t1\tButters_gp57r__gp57r"
PROPOSAL = "proposals/metpo_traitmech_v176"


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{PROFILE:<48} | {PROFILE:<48} | {DEFENSEFINDER_SYSTEM}",
        "notes": (
            "The DefenseFinder HMM inventory records a Butters gp57r "
            f"profile for {PROFILE} in the Butters_gp57r model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Butters_gp57r as a "
            "one-component system requiring the gp57r profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": f"{SYSTEM} system",
    "definition": (
        f"A phage defense system in which an organism possesses a {SYSTEM} "
        "locus that can protect bacteria from bacteriophage infection."
    ),
    "definition_source": MOHAMMED,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": DEFENSEFINDER_SYSTEM,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        {
            "reference": MOHAMMED,
            "snippet": (
                "Butters gp57r is both necessary and sufficient to inhibit "
                "infection by Island3 and other phages"
            ),
            "notes": (
                "Mohammed et al. report Butters gp57r as the Butters "
                "component that can block Island3 and additional heterotypic "
                "phages."
            ),
        },
        {
            "reference": MOHAMMED,
            "snippet": (
                "mc2155(gp57r) recapitulated defense against Island3 "
                "comparable to that mounted by mc2155(Butters)"
            ),
            "notes": (
                "Mohammed et al. show that expressing Butters gene 57r is "
                "sufficient to reproduce Butters-like defense against "
                "Island3."
            ),
        },
        {
            "reference": MOHAMMED,
            "snippet": (
                "Results show that Butters gp57r defends against several "
                "other phages (Fig. 3A)"
            ),
            "notes": (
                "Mohammed et al. test the breadth of the cloned gp57r "
                "defense and find protection against additional heterotypic "
                "phages."
            ),
        },
        {
            "reference": MOHAMMED,
            "snippet": (
                "the proposal that gp57r acts downstream of DNA injection"
            ),
            "notes": (
                "Mohammed et al. narrow the antiviral effect to a "
                "post-DNA-injection step without resolving gp57r's direct "
                "molecular substrate."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Butters_gp57r | 10\\.1101/2023\\.01\\.03\\.522681 | "
                "Identification of a new antiphage system "
                "inMycobacteriumphage Butters"
            ),
            "notes": (
                "The DefenseFinder model registry maps the named "
                "Butters_gp57r system to the Mohammed et al. Butters gp57r "
                "antiphage-system preprint."
            ),
        },
        hmm_inventory_evidence(),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Butters gp57r loci confer heterotypic phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Butters gp57r locus to restricted bacteriophage propagation "
                "without asserting the unresolved gp57r substrate, nuclease "
                "output, or phage-tail escape mechanism."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Butters gp57r as a named anti-phage "
                "system with a DefenseFinder gp57r profile while leaving "
                "the direct Island3 or PurpleHaze trigger, the role of the "
                "HEPN-associated RX4-6H motif, the primary gp57r molecular "
                "output, and homolog breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Butters gp57r locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Butters gp57r anti-phage defense locus cataloged "
                        "in DefenseFinder with a gp57r HMM profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Butters gp57r system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Butters gp57r system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Butters gp57r "
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
                        "Mohammed et al. show that Butters gp57r is "
                        "necessary and sufficient for Island3 inhibition, "
                        "and DefenseFinder catalogs a gp57r profile in the "
                        "Butters_gp57r model namespace."
                    ),
                    "evidence": [
                        {
                            "reference": MOHAMMED,
                            "snippet": (
                                "Butters gp57r is both necessary and "
                                "sufficient to inhibit infection by Island3 "
                                "and other phages"
                            ),
                            "notes": (
                                "Mohammed et al. support gp57r as the Butters "
                                "component that can restrict Island3 and "
                                "additional heterotypic phages."
                            ),
                        },
                        hmm_inventory_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Butters-gp57r-associated restriction of phage "
                        "propagation realizes the Butters gp57r system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MOHAMMED,
                            "snippet": (
                                "mc2155(gp57r) recapitulated defense against "
                                "Island3 comparable to that mounted by "
                                "mc2155(Butters)"
                            ),
                            "notes": (
                                "Mohammed et al. show that recombinant "
                                "expression of Butters gene 57r can reproduce "
                                "Butters-mediated Island3 defense."
                            ),
                        },
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Butters_gp57r | "
                                "10\\.1101/2023\\.01\\.03\\.522681 | "
                                "Identification of a new antiphage system "
                                "inMycobacteriumphage Butters"
                            ),
                            "notes": (
                                "DefenseFinder records Butters_gp57r as a "
                                "named system from the Mohammed et al. "
                                "Butters gp57r antiphage-system preprint."
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
                        "Butters gp57r system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "| Butters_gp57r | "
                                "10\\.1101/2023\\.01\\.03\\.522681 | "
                                "Identification of a new antiphage system "
                                "inMycobacteriumphage Butters |"
                            ),
                            "notes": (
                                "DefenseFinder associates Butters_gp57r with "
                                "the Mohammed et al. Butters gp57r "
                                "antiphage-system preprint."
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
                "Resolve the Butters gp57r direct phage trigger, primary "
                "molecular target, HEPN-associated RX4-6H motif requirement, "
                "DNA-amplification defect, PurpleHaze minor-tail escape "
                "route, and homolog breadth before minting narrower Butters "
                "gp57r mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mohammed et al. and DefenseFinder support Butters gp57r as "
                "a named anti-phage system with a gp57r profile, but the "
                "direct phage trigger, the biochemical role of its predicted "
                "HEPN domain and RX4-6H motif, the primary event leading to "
                "failed Island3 DNA amplification, and the defense scope of "
                "gp57r homologs in other mycobacteriophages or clinical "
                "Mycobacterium abscessus isolates are not resolved enough "
                "here to assert a narrower mechanistic child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
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
            "Minted Butters gp57r system as a DOI-backed GENOMICS "
            "TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
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
