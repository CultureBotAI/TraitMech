#!/usr/bin/env python3
"""Add the Druantia system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "druantia_system.yaml"

DORON = "DOI:10.1126/science.aar4120"
WU = "DOI:10.64898/2026.05.12.724681"

CURATOR = "codex"
TIMESTAMP = "2026-09-16T00:36:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000234",
    "label": "Druantia system",
    "definition": (
        "A phage defense system in which an organism possesses a Druantia "
        "locus built around a conserved DruE-like helicase-nuclease core "
        "and subtype-specific partner proteins that activate or enable DNA "
        "processing to inhibit bacteriophage propagation."
    ),
    "definition_source": WU,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Druantia",
            "synonym_type": "EXACT_SYNONYM",
            "source": DORON,
        }
    ],
    "evidence": [
        {
            "reference": DORON,
            "snippet": (
                "Druantia DruABCDE (type I) DruMFGE (type II) DruHE "
                "(III) pfam14236, pfam00270, pfam00271, pfam09369, "
                "COG1205, pfam00145, COG0270 Helicase, methylase 1,342 "
                "1,321 (2.6%)"
            ),
            "notes": (
                "Doron et al. reported Druantia as a helicase- and "
                "methylase-associated system with Type I, Type II, and Type "
                "III locus architectures in their pangenome-scale antiphage "
                "system discovery screen."
            ),
        },
        {
            "reference": DORON,
            "snippet": (
                "A Type I system cloned from E. coli UMEA 4076-1 into E. "
                "coli MG1655 rendered the engineered strain resistant "
                "against 4 of the 6 phages tested"
            ),
            "notes": (
                "Doron et al. support Druantia as an experimentally "
                "validated phage-defense system rather than a source-only "
                "locus label."
            ),
        },
        {
            "reference": WU,
            "snippet": (
                "There are several subtypes of Druantia that all share the "
                "DruE protein but differ in their associated genes"
            ),
            "notes": (
                "Wu et al. support defining a broad Druantia family record "
                "around a common DruE component while keeping subtype "
                "partners separate."
            ),
        },
        {
            "reference": WU,
            "snippet": (
                "Druantia III is a late-acting defence where DruH is the "
                "likely infection sensor and DruE is a helicase-nuclease "
                "effector that engages ssDNA-containing replication "
                "intermediates"
            ),
            "notes": (
                "Wu et al. support the characterized Type III arrangement "
                "in which DruH likely senses infection and DruE acts as the "
                "helicase-nuclease effector."
            ),
        },
        {
            "reference": WU,
            "snippet": (
                "we identified 6,885 bacterial genomes encoding complete "
                "Druantia III systems, defined by the presence of both DruE "
                "and DruH"
            ),
            "notes": (
                "Wu et al. support Druantia III as a recurring bacterial "
                "DruE/DruH module rather than a single engineered "
                "construct."
            ),
        },
        {
            "reference": WU,
            "snippet": (
                "DruE is the only component shared across Druantia "
                "subtypes, suggesting that DNA processing by a DruE-like "
                "helicase-nuclease is the conserved core function of "
                "Druantia"
            ),
            "notes": (
                "Wu et al. support placing the broad Druantia trait at the "
                "DruE-core family level rather than making DruH universal "
                "across Type I, Type II, and Type III systems."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Doron et al. cloned a Druantia Type I system from E. coli "
                "UMEA 4076-1 into E. coli MG1655 and showed that the "
                "engineered strain resisted four of six tested phages."
            ),
            "reference": DORON,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "druantia_drue_dna_processing_phage_defense",
            "title": "Druantia cores direct infection-associated DNA processing",
            "description": (
                "Evidence-backed process sketch linking a Druantia locus to "
                "subtype-specific partner activation, DruE-family "
                "helicase-nuclease DNA processing, downstream phage DNA "
                "cleavage, and inhibition of phage growth."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph uses the conserved DruE-like core and the "
                "Druantia III DruH mechanism as a characterized example "
                "without asserting that DruH, RecBCD dependence, Zorya II "
                "synergy, late-phage-protein triggers, exact DNA substrates, "
                "or a single accessory-gene architecture are universal "
                "across Type I, Type II, and Type III Druantia loci."
            ),
            "nodes": [
                {
                    "node_id": "druantia_locus",
                    "label": "Druantia locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Druantia antiphage locus encoding a conserved "
                        "DruE-like helicase-nuclease and subtype-specific "
                        "partner proteins."
                    ),
                },
                {
                    "node_id": "druantia_partner_activation",
                    "label": "Druantia subtype-specific partner activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation or enabling of the DruE core by "
                        "subtype-specific Druantia partners, such as DruH "
                        "in Type III loci."
                    ),
                },
                {
                    "node_id": "drue_dna_processing",
                    "label": "DruE helicase-nuclease DNA processing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DNA processing by a DruE-like helicase-nuclease "
                        "that engages infection-associated DNA structures."
                    ),
                },
                {
                    "node_id": "downstream_phage_dna_cleavage",
                    "label": "downstream phage DNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cleavage of phage DNA downstream of DruE-family "
                        "DNA engagement and assembly."
                    ),
                },
                {
                    "node_id": "phage_growth",
                    "label": "phage growth",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Bacteriophage growth and amplification inside a "
                        "bacterial host population."
                    ),
                },
                {
                    "node_id": "druantia_system_trait",
                    "label": "Druantia system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000234",
                    "description": (
                        "Possession of a genome-encoded Druantia "
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
                    "subject": "druantia_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "druantia_partner_activation",
                    "description": (
                        "Druantia loci encode subtype-specific partner "
                        "proteins that activate or enable the DruE core."
                    ),
                    "evidence": [
                        {
                            "reference": WU,
                            "snippet": (
                                "the subtype-specific partner proteins "
                                "determine how that core is activated"
                            ),
                            "notes": (
                                "Wu et al. support subtype-specific "
                                "partners as the activation layer over the "
                                "conserved DruE core."
                            ),
                        }
                    ],
                },
                {
                    "subject": "druantia_partner_activation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "drue_dna_processing",
                    "description": (
                        "Subtype-specific partner activity activates or "
                        "enables DruE-family DNA processing."
                    ),
                    "evidence": [
                        {
                            "reference": WU,
                            "snippet": (
                                "DNA processing by a DruE-like "
                                "helicase-nuclease is the conserved core "
                                "function of Druantia"
                            ),
                            "notes": (
                                "Wu et al. support DruE-family DNA "
                                "processing as the conserved Druantia core "
                                "activated through subtype-specific "
                                "partners."
                            ),
                        }
                    ],
                },
                {
                    "subject": "drue_dna_processing",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "downstream_phage_dna_cleavage",
                    "description": (
                        "The DruE core engages ssDNA-containing "
                        "intermediates and promotes downstream DNA "
                        "cleavage."
                    ),
                    "evidence": [
                        {
                            "reference": WU,
                            "snippet": (
                                "DruE loads onto this intermediate through "
                                "its helicase core, assembles into a "
                                "higher-order state on extended ssDNA, and "
                                "promotes downstream DNA cleavage"
                            ),
                            "notes": (
                                "Wu et al. connect DruE helicase-core DNA "
                                "loading and assembly to downstream DNA "
                                "cleavage in their Druantia III model."
                            ),
                        }
                    ],
                },
                {
                    "subject": "downstream_phage_dna_cleavage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_growth",
                    "description": (
                        "Druantia-family DNA cleavage inhibits phage "
                        "growth."
                    ),
                    "evidence": [
                        {
                            "reference": WU,
                            "snippet": (
                                "DNA cleavage by DruE is required for "
                                "Druantia-mediated defence"
                            ),
                            "notes": (
                                "Wu et al. support DruE nuclease activity "
                                "as a required output for Druantia-mediated "
                                "defense."
                            ),
                        }
                    ],
                },
                {
                    "subject": "downstream_phage_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "druantia_system_trait",
                    "description": (
                        "Subtype-activated DruE-family DNA cleavage "
                        "realizes the Druantia system defense phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": WU,
                            "snippet": (
                                "DruE functions as the effector, providing "
                                "the helicase and nuclease activities "
                                "required for defence"
                            ),
                            "notes": (
                                "Wu et al. support DruE helicase and "
                                "nuclease activities as the Druantia III "
                                "defense output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "druantia_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Druantia system possession is a phage-defense-"
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DORON,
                            "snippet": (
                                "A Type I system cloned from E. coli UMEA "
                                "4076-1 into E. coli MG1655 rendered the "
                                "engineered strain resistant against 4 of "
                                "the 6 phages tested"
                            ),
                            "notes": (
                                "Doron et al. support experimentally "
                                "validated antiphage activity for a "
                                "Druantia Type I locus."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "druantia-subtype-mechanism-gap",
            "prompt": (
                "Resolve Druantia subtype composition and activation "
                "mechanisms before minting narrower Type I, Type II, or "
                "Type III Druantia-system children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Doron et al. separated Type I DruABCDE, Type II DruMFGE, "
                "and Type III DruHE architectures and validated one Type I "
                "locus, while Wu et al. define a Type III mechanism in "
                "which DruH likely senses infection and DruE engages "
                "ssDNA-containing intermediates. The first TraitRecord "
                "therefore stays at the DruE-core family level until "
                "separate review resolves Type I/II partner functions, "
                "Type III-specific DruH activation, exact phage triggers, "
                "and Zorya-coupled versus standalone outputs across "
                "Druantia loci."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        },
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the new TraitRecord YAML",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Druantia system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v111."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
