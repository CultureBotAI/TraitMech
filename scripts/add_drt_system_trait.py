#!/usr/bin/env python3
"""Add the DRT system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "drt_system.yaml"

GAO = "DOI:10.1126/science.aba0372"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-19T12:30:14Z"

PROFILE = "DRT_1__drt1a"

DRT_RULES_SNIPPET = "DRT\tDRT_1\t2\t2\tDRT_1__drt1a, DRT_1__drt1b"


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": f"{PROFILE:<48} | {PROFILE:<48} | DRT_1",
        "notes": (
            "The DefenseFinder HMM inventory records the drt1a profile in "
            "the DRT_1 model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": "traitmech:000279",
    "label": "DRT system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "defense-associated reverse transcriptase locus whose RT-domain "
        "component or components can confer bacteriophage defense and are "
        "modeled by DefenseFinder as DRT subtypes."
    ),
    "definition_source": GAO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DRT",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "defense-associated RT",
            "synonym_type": "RELATED_SYNONYM",
            "source": GAO,
        },
        {
            "synonym_text": "defense-associated reverse transcriptase",
            "synonym_type": "RELATED_SYNONYM",
            "source": GAO,
        },
    ],
    "evidence": [
        {
            "reference": GAO,
            "snippet": (
                "We discovered that a family of uncharacterized reverse "
                "transcriptases (RTs) are active defense systems"
            ),
            "notes": (
                "Gao et al. experimentally support previously "
                "uncharacterized reverse transcriptases as active "
                "antiphage defense systems rather than mobile-element RT "
                "features alone."
            ),
        },
        {
            "reference": GAO,
            "snippet": (
                "six of these candidates (UG1, UG2, UG3, UG8, UG15, and "
                "UG16) provided robust protection against dsDNA phages"
            ),
            "notes": (
                "Gao et al. support DRT defense activity across several "
                "reverse-transcriptase candidate groups."
            ),
        },
        {
            "reference": GAO,
            "snippet": "We named these genes defense-associated RTs (DRTs)",
            "notes": (
                "Gao et al. coined the defense-associated RT naming that "
                "underlies the DRT system label."
            ),
        },
        {
            "reference": GAO,
            "snippet": (
                "In all cases, mutations in the RT active site [(Y/F)xDD "
                "to (Y/F)xAA, where x is any amino acid] abolished "
                "activity"
            ),
            "notes": (
                "Gao et al. connect DRT antiphage activity to conserved "
                "reverse-transcriptase active-site residues."
            ),
        },
        {
            "reference": GAO,
            "snippet": (
                "the UG3 (drt3a) and UG8 (drt3b) RTs are components of "
                "the same defense system (DRT type 3), with both RTs "
                "required for defense activity"
            ),
            "notes": (
                "Gao et al. support the multi-component DRT type 3 system "
                "while separating it from single-gene DRT subtypes."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "DRT | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
                "activities mediate antiviral immunity in prokaryotes"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named DRT "
                "system to the Gao et al. antiphage-system discovery "
                "paper."
            ),
        },
        {
            "reference": DEFENSEFINDER_RULES,
            "snippet": DRT_RULES_SNIPPET,
            "notes": (
                "The DefenseFinder rules table models DRT_1 as a "
                "two-profile DRT subtype."
            ),
        },
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "drt_reverse_transcriptase_antiphage_defense",
            "title": "DRT loci use reverse transcriptases for antiphage defense",
            "description": (
                "Conservative system-level sketch linking a DRT locus to "
                "reverse-transcriptase active-site dependence, "
                "subtype-specific bacteriophage resistance, and the DRT "
                "system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DRT systems at the family level while "
                "leaving the direct RT products, phage triggers, "
                "subtype-specific partner proteins or non-coding RNAs, "
                "additional subtype mechanisms, and exact phage targets "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "drt_locus",
                    "label": "DRT locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A defense-associated reverse transcriptase "
                        "antiphage locus represented by DRT subtype "
                        "profiles."
                    ),
                },
                {
                    "node_id": "defense_associated_rt_activity",
                    "label": "defense-associated RT activity",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "Reverse-transcriptase active-site-dependent "
                        "activity of DRT antiphage proteins."
                    ),
                },
                {
                    "node_id": "subtype_specific_phage_resistance",
                    "label": "subtype-specific phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against particular bacteriophages by "
                        "one of several DRT subtypes."
                    ),
                },
                {
                    "node_id": "drt_system_trait",
                    "label": "DRT system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000279",
                    "description": (
                        "Possession of a genome-encoded "
                        "defense-associated reverse transcriptase phage "
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
                    "subject": "drt_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "defense_associated_rt_activity",
                    "description": (
                        "DRT loci encode defense-associated RT-domain "
                        "proteins."
                    ),
                    "evidence": [
                        {
                            "reference": GAO,
                            "snippet": (
                                "We named these genes "
                                "defense-associated RTs (DRTs)"
                            ),
                            "notes": (
                                "Gao et al. connect the DRT name to "
                                "reverse-transcriptase defense genes."
                            ),
                        },
                        {
                            **hmm_inventory_evidence(),
                            "notes": (
                                "DefenseFinder includes drt1a in the "
                                "custom DRT_1 model profile inventory."
                            ),
                        },
                    ],
                },
                {
                    "subject": "defense_associated_rt_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "subtype_specific_phage_resistance",
                    "description": (
                        "Conserved reverse-transcriptase active-site "
                        "residues are required for DRT-mediated defense "
                        "activity."
                    ),
                    "evidence": [
                        {
                            "reference": GAO,
                            "snippet": (
                                "In all cases, mutations in the RT active "
                                "site [(Y/F)xDD to (Y/F)xAA, where x is "
                                "any amino acid] abolished activity"
                            ),
                            "notes": (
                                "Gao et al. show DRT antiphage activity "
                                "requires RT active-site residues."
                            ),
                        }
                    ],
                },
                {
                    "subject": "drt_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "subtype_specific_phage_resistance",
                    "description": (
                        "Experimentally reconstructed DRT candidate "
                        "systems provide protection against dsDNA phages."
                    ),
                    "evidence": [
                        {
                            "reference": GAO,
                            "snippet": (
                                "six of these candidates (UG1, UG2, UG3, "
                                "UG8, UG15, and UG16) provided robust "
                                "protection against dsDNA phages"
                            ),
                            "notes": (
                                "Gao et al. support DRT loci as defensive "
                                "against bacteriophages in heterologous "
                                "reconstruction assays."
                            ),
                        },
                        {
                            "reference": GAO,
                            "snippet": (
                                "the UG3 (drt3a) and UG8 (drt3b) RTs are "
                                "components of the same defense system "
                                "(DRT type 3), with both RTs required for "
                                "defense activity"
                            ),
                            "notes": (
                                "Gao et al. support multi-component DRT "
                                "type 3 as one DRT-system subtype."
                            ),
                        },
                    ],
                },
                {
                    "subject": "subtype_specific_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "drt_system_trait",
                    "description": (
                        "DefenseFinder models DRT as a phage-defense "
                        "system with subtype models such as DRT_1."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_RULES,
                            "snippet": DRT_RULES_SNIPPET,
                            "notes": (
                                "The DefenseFinder rules table supports "
                                "DRT_1 as a named defense-system subtype "
                                "model with drt1a and drt1b profiles."
                            ),
                        }
                    ],
                },
                {
                    "subject": "drt_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DRT system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "DRT | 10\\.1126/science\\.aba0372 | "
                                "Diverse enzymatic activities mediate "
                                "antiviral immunity in prokaryotes"
                            ),
                            "notes": (
                                "DefenseFinder associates DRT with the "
                                "Gao et al. prokaryotic antiviral-immunity "
                                "paper."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "drt-subtype-mechanism-gap",
            "prompt": (
                "Resolve DRT subtype products, partner RNAs or proteins, "
                "phage triggers, and antiphage substrates before minting "
                "narrower DRT subtype mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support several active "
                "reverse-transcriptase-containing antiphage systems, and "
                "DefenseFinder models DRT subtypes such as DRT_1. "
                "This first record stays at DRT-family level because "
                "the direct products of DRT RT activity, the exact phage "
                "triggers, the non-coding RNA role in DRT type 3, and "
                "the mechanisms for additional DRT subtypes are not "
                "resolved."
            ),
            "attaches_to": [
                "causal_graphs#drt_reverse_transcriptase_antiphage_defense"
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
            "Minted DRT system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v156."
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
