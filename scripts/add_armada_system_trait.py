#!/usr/bin/env python3
"""Add the ARMADA system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import (  # noqa: E402
    emit_trait_yaml,
    write_validated_trait,
)

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "armada_system.yaml"

BELL = "DOI:10.1016/j.chom.2026.05.015"
BELL_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12458937/"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T00:00:29Z"
IDENTIFIER = "traitmech:000477"
PROPOSAL = "proposals/metpo_traitmech_v354"

FINAL_CLASS_SNIPPET = (
    "Through comprehensive phylogenetic and structural analyses of YprA-like "
    "helicases, we identify several major clades, which define distinct "
    "defense systems including a broad class we call ARMADA "
    "(disARM-related antiviral defense array)."
)
FINAL_PROTECTION_SNIPPET = (
    "We show experimentally that ARMADA protects bacteria against a broad range "
    "of phages via a direct, non-abortive mechanism."
)
OPERON_CONTEXT_SNIPPET = (
    "The two largest uncharacterized YprA-like clades encompass a distinct set "
    "of related operons that, in addition to the YprA homologs, share two "
    "other genes with DISARM Class I systems"
)
TYPE_SPLIT_SNIPPET = (
    "The ARMADA clade splits into two well-separated, strongly supported "
    "subclades which we denote Type I and Type II."
)
NCTC_PROTECTION_SNIPPET = (
    "Log-protection (reduction in phage titer) conferred by ARMADA, expressed "
    "from plasmid pBeloBAC11 in BL21-AI, against a panel of 80 phages"
)
ATCC_8739_NATIVE_SNIPPET = (
    "Screening 66 phages that could form plaques on the double-deletion strain "
    "showed that the strain carrying only Druantia III exhibited at least "
    "modest protection (<0.01 EOP or <0.5 SFC) against 3 phages, whereas the "
    "strain carrying ARMADA Type II exhibited a much broader range of "
    "immunity, with at least modest protection observed against 30 phages."
)
ARMADA_DRUANTIA_SYNERGY_SNIPPET = (
    "Druantia Type III and ARMADA Type II systems showed clear evidence of "
    "synergizing to confer phage defense in their native host"
)
ARTICLE_REGISTRY_SNIPPET = (
    "Armada | 10\\.1101/2025\\.09\\.15\\.676423 | YprA family helicases "
    "provide the missing link between diverse prokaryotic immune systems"
)


def pmc_evidence(snippet: str, notes: str) -> dict[str, str]:
    return {
        "reference": BELL_PMC,
        "snippet": snippet,
        "notes": notes,
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder article registry maps the named Armada "
            "system to the Bell et al. YprA-family helicase preprint. The "
            "pinned HMM inventory and rules table do not list Armada, so this "
            "row is name-to-paper evidence rather than model-component "
            "evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "ARMADA system",
    "definition": (
        "A phage defense system in which an organism possesses an ARMADA "
        "YprA-like-helicase locus whose Type I and Type II operons share "
        "BrxHII-like and PglX-like components with DISARM Class I systems and "
        "whose experimentally tested Type II forms protect against a broad "
        "range of phages."
    ),
    "definition_source": BELL,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "ARMADA",
            "synonym_type": "EXACT_SYNONYM",
            "source": BELL,
        },
        {
            "synonym_text": "Armada",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "disARM-related antiviral defense array",
            "synonym_type": "EXACT_SYNONYM",
            "source": BELL,
        },
    ],
    "evidence": [
        {
            "reference": BELL,
            "snippet": FINAL_CLASS_SNIPPET,
            "notes": (
                "Bell et al. define ARMADA as a broad YprA-like helicase "
                "defense-system class."
            ),
        },
        {
            "reference": BELL,
            "snippet": FINAL_PROTECTION_SNIPPET,
            "notes": (
                "Bell et al. summarize experimental support that ARMADA "
                "protects bacteria against a broad range of phages."
            ),
        },
        pmc_evidence(
            OPERON_CONTEXT_SNIPPET,
            (
                "The preprint full text describes ARMADA operons as carrying "
                "YprA homologs plus BrxHII-like and PglX-like components "
                "shared with DISARM Class I systems."
            ),
        ),
        pmc_evidence(
            TYPE_SPLIT_SNIPPET,
            (
                "The preprint full text separates the broad ARMADA clade into "
                "Type I and Type II subclades."
            ),
        ),
        pmc_evidence(
            NCTC_PROTECTION_SNIPPET,
            (
                "A cloned E. coli NCTC 12900 ARMADA Type II cluster "
                "was tested for protection against a broad phage panel in a "
                "heterologous BL21-AI assay."
            ),
        ),
        pmc_evidence(
            ATCC_8739_NATIVE_SNIPPET,
            (
                "Precise system deletions in E. coli ATCC 8739 supported "
                "native ARMADA Type II protection across a broader tested "
                "phage set than the co-located Druantia Type III system."
            ),
        ),
        article_registry_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Bell et al. generated precise armABCD deletions in E. coli "
                "strain ATCC 8739 and showed that its native ARMADA Type II "
                "system provided broader phage protection than the co-located "
                "Druantia Type III system."
            ),
            "reference": BELL_PMC,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "armada_locus_phage_protection",
            "title": "ARMADA loci protect against broad phage panels",
            "description": (
                "Conservative system-level sketch linking an ARMADA "
                "YprA-like-helicase locus to experimentally measured "
                "anti-phage protection and ARMADA system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures ARMADA as a named YprA-like-helicase "
                "phage-defense system with Type I and Type II subclades "
                "while leaving direct phage triggers or effectors, native "
                "host breadth, exact Type I and Type II boundaries, "
                "profile-to-component mapping, and DefenseFinder HMM/rules "
                "detection criteria unresolved."
            ),
            "nodes": [
                {
                    "node_id": "armada_locus",
                    "label": "ARMADA locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A YprA-like-helicase ARMADA antiphage locus from a "
                        "Type I or Type II ARMADA clade."
                    ),
                },
                {
                    "node_id": "armada_broad_phage_protection",
                    "label": "ARMADA broad phage protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Experimentally measured reduction in bacteriophage "
                        "growth or plaque formation by tested ARMADA Type II "
                        "systems."
                    ),
                },
                {
                    "node_id": "armada_system_trait",
                    "label": "ARMADA system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded ARMADA phage-defense "
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
                    "subject": "armada_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "armada_broad_phage_protection",
                    "description": (
                        "ARMADA Type II loci from E. coli NCTC 12900 and "
                        "ATCC 8739 provided experimentally measured "
                        "anti-phage protection."
                    ),
                    "evidence": [
                        {
                            "reference": BELL,
                            "snippet": FINAL_PROTECTION_SNIPPET,
                            "notes": (
                                "Bell et al. summarize broad, direct, "
                                "non-abortive ARMADA anti-phage protection."
                            ),
                        },
                        pmc_evidence(
                            ATCC_8739_NATIVE_SNIPPET,
                            (
                                "Precise ARMADA and Druantia deletions in "
                                "E. coli ATCC 8739 resolved native "
                                "ARMADA-associated phage immunity."
                            ),
                        ),
                    ],
                },
                {
                    "subject": "armada_broad_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "armada_system_trait",
                    "description": (
                        "Broad phage protection realizes the ARMADA system "
                        "possession trait."
                    ),
                    "evidence": [
                        pmc_evidence(
                            NCTC_PROTECTION_SNIPPET,
                            (
                                "The cloned NCTC 12900 ARMADA Type II locus "
                                "was tested in BL21-AI against a broad "
                                "phage panel."
                            ),
                        ),
                        pmc_evidence(
                            ATCC_8739_NATIVE_SNIPPET,
                            (
                                "The native ATCC 8739 ARMADA Type II system "
                                "protected against a broader tested phage "
                                "panel than its co-located Druantia Type III "
                                "system."
                            ),
                        ),
                    ],
                },
                {
                    "subject": "armada_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "ARMADA system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": BELL,
                            "snippet": FINAL_CLASS_SNIPPET,
                            "notes": (
                                "Bell et al. define ARMADA among "
                                "YprA-family prokaryotic immune systems."
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
            "discussion_id": "armada-subtype-model-and-mechanism-gap",
            "prompt": (
                "Resolve exact ARMADA Type I and Type II boundaries, "
                "DefenseFinder HMM/rules coverage, profile-to-component "
                "mapping, direct phage triggers or outputs, and native host "
                "breadth before minting narrower ARMADA mechanism, subtype, "
                "or protein-component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Bell et al. support ARMADA as a broad YprA-like-helicase "
                "system family that shares BrxHII-like and PglX-like "
                "components with DISARM Class I systems and splits into "
                "Type I and Type II subclades, and the article "
                "experimentally validates Type II protection from E. coli "
                "NCTC 12900 and ATCC 8739 loci. The pinned DefenseFinder "
                "article registry names Armada and maps it to the Bell et "
                "al. preprint, but the pinned HMM inventory and rules table "
                "do not contain Armada rows, leaving profile coverage and "
                "detection criteria unresolved."
            ),
            "evidence": [
                {
                    "reference": BELL,
                    "snippet": FINAL_CLASS_SNIPPET,
                    "notes": (
                        "Bell et al. define ARMADA as a broad YprA-like "
                        "helicase defense-system class."
                    ),
                },
                pmc_evidence(
                    TYPE_SPLIT_SNIPPET,
                    (
                        "The broad ARMADA clade is split into Type I and "
                        "Type II subclades."
                    ),
                ),
                pmc_evidence(
                    ARMADA_DRUANTIA_SYNERGY_SNIPPET,
                    (
                        "The ATCC 8739 native-host experiments support "
                        "ARMADA Type II and Druantia Type III interaction "
                        "while leaving their coupling mechanism unresolved."
                    ),
                ),
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "No Armada or ARMADA HMM inventory row was present "
                        "in the pinned DefenseFinder model file."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "No Armada or ARMADA rule row was present in the "
                        "pinned DefenseFinder rules table."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#armada_locus_phage_protection"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-30",
        }
    ],
}


def validate_output(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


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
            "Minted ARMADA system as a final-DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under phage defense "
            "system after an ignored-and-hidden duplicate review found no "
            "exact live TraitMech, METPO, history, or prior proposal "
            "record; kept the graph at broad YprA-like-helicase system "
            "level because the pinned DefenseFinder article row is not "
            "backed by pinned HMM or rules rows; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    validate_output(record)

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"Wrote {rel}")
    else:
        sys.stdout.write(emit_trait_yaml(record))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
