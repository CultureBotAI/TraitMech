#!/usr/bin/env python3
"""Add the Dpd system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dpd_system.yaml"

THIAVILLE = "DOI:10.1073/pnas.1518570113"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-19T18:31:00Z"


def hmm_inventory_evidence() -> dict[str, str]:
    hmm = "Dpd__DpdA"
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{hmm:<48} | {hmm:<48} | Dpd",
        "notes": (
            "The DefenseFinder HMM inventory records DpdA in the Dpd "
            "model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000278",
    "label": "Dpd system",
    "definition": (
        "A phage defense system in which an organism possesses a Dpd "
        "genomic island whose dpdA-K genes install 7-deazaguanine "
        "derivatives into DNA and are modeled by DefenseFinder as a "
        "multi-profile Dpd system."
    ),
    "definition_source": THIAVILLE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Dpd",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "dpdA-K",
            "synonym_type": "RELATED_SYNONYM",
            "source": THIAVILLE,
        },
    ],
    "evidence": [
        {
            "reference": THIAVILLE,
            "snippet": (
                "2'-deoxy-preQ0 and "
                "2'-deoxy-7-amido-7-deazaguanosine in enzymatic "
                "hydrolysates of DNA extracted from the pathogenic, "
                "Gram-negative bacteria Salmonella enterica serovar "
                "Montevideo"
            ),
            "notes": (
                "Thiaville et al. experimentally detected "
                "7-deazaguanine-derived DNA modifications in a bacterium "
                "carrying the Dpd island."
            ),
        },
        {
            "reference": THIAVILLE,
            "snippet": (
                "rename the genes of the S. Montevideo cluster as dpdA-K "
                "for 7-deazapurine in DNA"
            ),
            "notes": (
                "Thiaville et al. name the S. Montevideo 7-deazapurine "
                "DNA-modification cluster as dpdA-K."
            ),
        },
        {
            "reference": THIAVILLE,
            "snippet": (
                "the modifications were detected in DNA from other "
                "organisms containing these clusters, including Kineococcus "
                "radiotolerans, Comamonas testosteroni, and Sphingopyxis "
                "alaskensis"
            ),
            "notes": (
                "Thiaville et al. support treating Dpd as a recurrent "
                "bacterial system rather than a one-off S. Montevideo "
                "sequence feature."
            ),
        },
        {
            "reference": THIAVILLE,
            "snippet": (
                "strongly suggests a restriction-modification role for the "
                "cluster in Enterobacteriaceae"
            ),
            "notes": (
                "Thiaville et al. connect the Dpd cluster to a likely "
                "restriction-modification role based on transformation "
                "efficiencies of modified and unmodified plasmids."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "Dpd | 10\\.1073/pnas\\.1518570113 | Novel genomic island "
                "modifies DNA with 7-deazaguanine derivatives"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named Dpd "
                "system to the Thiaville et al. DNA-modification paper."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": (
                "Dpd\tDpd\t4\t4\tDpd__DpdA, Dpd__DpdB, Dpd__DpdC, "
                "Dpd__DpdD, Dpd__DpdE, Dpd__DpdF, Dpd__DpdG, "
                "Dpd__DpdH, Dpd__DpdI, Dpd__DpdJ, Dpd__DpdK"
            ),
            "notes": (
                "The DefenseFinder rules table models Dpd as a "
                "multi-profile defense system requiring a subset of DpdA-K "
                "profiles."
            ),
        },
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "dpd_dna_modification_defense",
            "title": (
                "Dpd islands install 7-deazaguanine DNA modifications"
            ),
            "description": (
                "Conservative system-level sketch linking a Dpd genomic "
                "island to 7-deazaguanine DNA modification, a likely "
                "restriction-modification output, and the Dpd system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Dpd as a DNA-modification system with "
                "a DefenseFinder model while leaving its exact restriction "
                "target, modified motif, phage substrate range, DpdA-K "
                "component functions, and optional FolE/QueC/QueD/QueE "
                "profile requirements unresolved."
            ),
            "nodes": [
                {
                    "node_id": "dpd_genomic_island",
                    "label": "Dpd genomic island",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A dpdA-K 7-deazapurine DNA-modification locus "
                        "represented by a multi-profile DefenseFinder Dpd "
                        "model."
                    ),
                },
                {
                    "node_id": "deazaguanine_dna_modification",
                    "label": "7-deazaguanine DNA modification",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Installation of 7-deazaguanine-derived "
                        "deoxynucleosides in bacterial DNA."
                    ),
                },
                {
                    "node_id": "restriction_modification_behavior",
                    "label": "restriction-modification behavior",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Self/non-self discrimination associated with a "
                        "bacterial DNA-modification island."
                    ),
                },
                {
                    "node_id": "dpd_system_trait",
                    "label": "Dpd system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000278",
                    "description": (
                        "Possession of a genome-encoded Dpd "
                        "7-deazaguanine DNA-modification defense system."
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
                    "subject": "dpd_genomic_island",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "deazaguanine_dna_modification",
                    "description": (
                        "The Dpd cluster installs 7-deazaguanine "
                        "derivatives in DNA."
                    ),
                    "evidence": [
                        {
                            "reference": THIAVILLE,
                            "snippet": (
                                "rename the genes of the S. Montevideo "
                                "cluster as dpdA-K for 7-deazapurine in DNA"
                            ),
                            "notes": (
                                "Thiaville et al. name the genes of the "
                                "7-deazapurine DNA-modification cluster as "
                                "dpdA-K."
                            ),
                        },
                        {
                            **hmm_inventory_evidence(),
                            "notes": (
                                "DefenseFinder includes DpdA in the custom "
                                "Dpd model profile inventory."
                            ),
                        },
                    ],
                },
                {
                    "subject": "deazaguanine_dna_modification",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restriction_modification_behavior",
                    "description": (
                        "Modified Dpd DNA is associated with "
                        "restriction-modification behavior in "
                        "Enterobacteriaceae."
                    ),
                    "evidence": [
                        {
                            "reference": THIAVILLE,
                            "snippet": (
                                "strongly suggests a "
                                "restriction-modification role for the "
                                "cluster in Enterobacteriaceae"
                            ),
                            "notes": (
                                "Thiaville et al. connect Dpd modification "
                                "to a likely restriction-modification role "
                                "without resolving the exact restriction "
                                "component or substrate."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restriction_modification_behavior",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "dpd_system_trait",
                    "description": (
                        "DefenseFinder models Dpd as a multi-profile "
                        "defense system rooted in DpdA-K DNA modification."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": (
                                "Dpd\tDpd\t4\t4\tDpd__DpdA, Dpd__DpdB, "
                                "Dpd__DpdC, Dpd__DpdD, Dpd__DpdE, "
                                "Dpd__DpdF, Dpd__DpdG, Dpd__DpdH, "
                                "Dpd__DpdI, Dpd__DpdJ, Dpd__DpdK"
                            ),
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "Dpd as a named defense-system model with "
                                "DpdA-K profiles."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dpd_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Dpd system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "Dpd | 10\\.1073/pnas\\.1518570113 | "
                                "Novel genomic island modifies DNA with "
                                "7-deazaguanine derivatives"
                            ),
                            "notes": (
                                "DefenseFinder associates Dpd with the "
                                "Thiaville et al. DNA-modification paper."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "dpd-restriction-mechanism-gap",
            "prompt": (
                "Resolve Dpd restriction targets, phage specificity, and "
                "DpdA-K component functions before minting narrower Dpd "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Thiaville et al. support dpdA-K-dependent installation of "
                "7-deazaguanine derivatives into DNA and a likely "
                "restriction-modification role, and DefenseFinder supports "
                "Dpd as a named multi-profile defense model. This first "
                "record does not yet resolve the universal restriction "
                "target, modified motif, antiphage substrate breadth, or "
                "the necessity of each profiled component across natural "
                "Dpd loci."
            ),
            "attaches_to": ["causal_graphs#dpd_dna_modification_defense"],
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
            "Minted Dpd system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v155."
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
