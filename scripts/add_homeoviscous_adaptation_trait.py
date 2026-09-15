#!/usr/bin/env python3
"""Add the homeoviscous adaptation physiology trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "physiology" / "homeoviscous_adaptation.yaml"
DE_MENDOZA = "DOI:10.1146/annurev-micro-091313-103612"
MAITI = "DOI:10.1039/d4cc03114h"
HOOGERLAND = "DOI:10.1038/s41467-024-53677-5"
SIDARTA = "DOI:10.1128/spectrum.03925-23"
FABI_UNIPROT = "https://rest.uniprot.org/uniprotkb/P0AEK4.json"
FABB_UNIPROT = "https://rest.uniprot.org/uniprotkb/P0A953.json"
CURATOR = "codex"
TIMESTAMP = "2026-09-15T07:02:39Z"

RECORD = {
    "identifier": "traitmech:000208",
    "label": "homeoviscous adaptation",
    "definition": (
        "A stress response in which an organism remodels membrane lipid "
        "composition to maintain a functional membrane viscosity and fluidity "
        "when temperature changes perturb lipid packing."
    ),
    "definition_source": MAITI,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000078"],
    "synonyms": [
        {
            "synonym_text": "homoviscous adaptation",
            "synonym_type": "EXACT_SYNONYM",
            "source": DE_MENDOZA,
        },
        {
            "synonym_text": "HVA",
            "synonym_type": "RELATED_SYNONYM",
            "source": MAITI,
        },
    ],
    "evidence": [
        {
            "reference": DE_MENDOZA,
            "snippet": "termed homeoviscous adaptation",
            "notes": (
                "de Mendoza reviews the temperature-driven bacterial membrane "
                "remodeling response and names it homeoviscous adaptation."
            ),
        },
        {
            "reference": SIDARTA,
            "snippet": (
                "Upon temperature decrease, the membrane rigidifies and increases "
                "in thickness, resulting in activation of the kinase-dominant "
                "state of DesK"
            ),
            "notes": (
                "Sidarta et al. support membrane rigidification and thickening as "
                "proximal physical triggers in the Bacillus subtilis DesK/DesR "
                "homeoviscous-adaptation model."
            ),
        },
        {
            "reference": HOOGERLAND,
            "snippet": (
                "hard-wired parameters calibrate the system to generate membrane "
                "compositions that maintain constant fluidity"
            ),
            "notes": (
                "Hoogerland et al. directly support E. coli temperature adaptation "
                "through a fatty-acid synthesis control system that maintains "
                "membrane fluidity."
            ),
        },
        {
            "reference": HOOGERLAND,
            "snippet": "restores optimal membrane fluidity within a single generation",
            "notes": (
                "Hoogerland et al. directly connect the E. coli fatty-acid "
                "branchpoint valve and transcriptional feedback to rapid "
                "membrane-fluidity restoration after temperature shock."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "E. coli rapidly restores membrane fluidity after temperature "
                "shock through a FabI/FabB branchpoint valve coupled to "
                "transcriptional feedback."
            ),
            "reference": HOOGERLAND,
        },
        {
            "taxon_id": "NCBITaxon:1423",
            "taxon_label": "Bacillus subtilis",
            "note": (
                "B. subtilis is the model organism for DesK/DesR membrane "
                "thickness sensing and Des-mediated fatty-acyl-chain "
                "desaturation during cold-induced homeoviscous adaptation."
            ),
            "reference": SIDARTA,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "homeoviscous_adaptation_membrane_fluidity",
            "title": "Membrane-fluidity homeostasis by lipid remodeling",
            "description": (
                "Evidence-backed causal sketch linking temperature-driven "
                "membrane rigidification to homeoviscous lipid remodeling and "
                "restored membrane fluidity."
            ),
            "scope_status": "MECHANISTIC",
            "scope_notes": (
                "This graph captures the conserved membrane-fluidity output of "
                "homeoviscous adaptation without making the Bacillus DesK/DesR "
                "two-component branch, E. coli FabI/FabB metabolic valve, or any "
                "single lipid species universal across microbes."
            ),
            "nodes": [
                {
                    "node_id": "homeoviscous_adaptation_trait",
                    "label": "homeoviscous adaptation",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000208",
                    "description": (
                        "Capacity to remodel membrane lipid composition to "
                        "preserve functional membrane viscosity and fluidity."
                    ),
                },
                {
                    "node_id": "temperature_downshift",
                    "label": "temperature downshift",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "A decrease in ambient temperature that orders the lipid "
                        "bilayer."
                    ),
                },
                {
                    "node_id": "membrane_rigidification",
                    "label": "membrane rigidification",
                    "node_type": "QUALITY",
                    "description": (
                        "Reduced membrane fluidity and increased bilayer "
                        "thickness after cooling."
                    ),
                },
                {
                    "node_id": "homeoviscous_adaptation_process",
                    "label": "homeoviscous adaptation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "grounding": "METPO:1016200",
                    "description": (
                        "Temperature-responsive lipid remodeling that restores "
                        "the membrane to a fluidity setpoint."
                    ),
                },
                {
                    "node_id": "fab_fatty_acid_branchpoint_enzymes",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                    "grounding_notes": (
                        "Reviewed E. coli branchpoint protein set; no single "
                        "taxon-agnostic family, activity, or complex term captures "
                        "the FabI enoyl-ACP reductase and FabB "
                        "beta-ketoacyl-ACP synthase pair without also adding "
                        "unrelated fatty-acid synthesis components."
                    ),
                    "label": "FabI/FabB branchpoint enzymes",
                    "node_type": "GENE_OR_PROTEIN",
                    "description": (
                        "E. coli fatty-acid synthesis enzymes at the "
                        "saturated/unsaturated branchpoint that route acyl-ACP "
                        "flux during temperature adaptation."
                    ),
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P0AEK4",
                            "protein_label": (
                                "Enoyl-[acyl-carrier-protein] reductase [NADH] "
                                "FabI"
                            ),
                            "gene_symbol": "fabI",
                            "taxon_id": "NCBITaxon:83333",
                            "taxon_label": "Escherichia coli K-12",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 161,
                            "sequence_version": 2,
                            "role": (
                                "E. coli K-12 FabI catalyzes enoyl-ACP reduction "
                                "in fatty-acid elongation and participates in the "
                                "FabI/FabB metabolic valve that allocates flux "
                                "between saturated and unsaturated fatty-acid "
                                "synthesis during homeoviscous adaptation."
                            ),
                            "evidence": [
                                {
                                    "reference": FABI_UNIPROT,
                                    "snippet": (
                                        "Involved in the elongation cycle of "
                                        "fatty acid which are used in the lipid "
                                        "metabolism"
                                    ),
                                    "notes": (
                                        "Verified FabI identity and fatty-acid "
                                        "elongation role against the live UniProt "
                                        "REST entry for P0AEK4 retrieved on "
                                        "2026-09-15."
                                    ),
                                },
                                {
                                    "reference": HOOGERLAND,
                                    "snippet": (
                                        "via the branchpoint enzymes FabI and "
                                        "FabB"
                                    ),
                                    "notes": (
                                        "Hoogerland et al. place FabI in the "
                                        "temperature-sensitive E. coli fatty-acid "
                                        "branchpoint valve."
                                    ),
                                },
                            ],
                        },
                        {
                            "uniprot_id": "UniProtKB:P0A953",
                            "protein_label": (
                                "3-oxoacyl-[acyl-carrier-protein] synthase 1"
                            ),
                            "gene_symbol": "fabB",
                            "taxon_id": "NCBITaxon:83333",
                            "taxon_label": "Escherichia coli K-12",
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 155,
                            "sequence_version": 1,
                            "role": (
                                "E. coli K-12 FabB elongates acyl-ACP substrates "
                                "in fatty-acid biosynthesis and participates in "
                                "the FabI/FabB metabolic valve that allocates flux "
                                "between saturated and unsaturated fatty-acid "
                                "synthesis during homeoviscous adaptation."
                            ),
                            "evidence": [
                                {
                                    "reference": FABB_UNIPROT,
                                    "snippet": (
                                        "Catalyzes a key reaction in unsaturated "
                                        "fatty acid (UFA) synthesis"
                                    ),
                                    "notes": (
                                        "Verified FabB identity and unsaturated "
                                        "fatty-acid synthesis role against the "
                                        "live UniProt REST entry for P0A953 "
                                        "retrieved on 2026-09-15."
                                    ),
                                },
                                {
                                    "reference": HOOGERLAND,
                                    "snippet": (
                                        "via the branchpoint enzymes FabI and "
                                        "FabB"
                                    ),
                                    "notes": (
                                        "Hoogerland et al. place FabB in the "
                                        "temperature-sensitive E. coli fatty-acid "
                                        "branchpoint valve."
                                    ),
                                },
                            ],
                        },
                    ],
                },
                {
                    "node_id": "membrane_lipid_remodeling",
                    "label": "membrane lipid remodeling",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Changes in membrane lipid unsaturation, branching, or "
                        "chain length that alter lipid packing."
                    ),
                },
                {
                    "node_id": "membrane_fluidity",
                    "label": "membrane fluidity",
                    "node_type": "QUALITY",
                    "grounding": "METPO:1007505",
                    "description": (
                        "Dynamic lipid-bilayer state maintained near a "
                        "functional setpoint by homeoviscous remodeling."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "temperature_downshift",
                    "predicate": "causes",
                    "object": "membrane_rigidification",
                    "description": (
                        "A temperature decrease causes the bacterial membrane to "
                        "rigidify and thicken."
                    ),
                    "evidence": [
                        {
                            "reference": SIDARTA,
                            "snippet": (
                                "Upon temperature decrease, the membrane "
                                "rigidifies and increases in thickness"
                            ),
                            "notes": (
                                "Sidarta et al. describe rigidification and "
                                "thickening as the immediate membrane response "
                                "to temperature decrease."
                            ),
                        },
                    ],
                    "predicate_id": "biolink:causes",
                },
                {
                    "subject": "membrane_rigidification",
                    "predicate": "positively regulates",
                    "object": "homeoviscous_adaptation_process",
                    "description": (
                        "Membrane rigidification is sensed as the physical "
                        "input that activates homeoviscous lipid remodeling."
                    ),
                    "evidence": [
                        {
                            "reference": SIDARTA,
                            "snippet": (
                                "Upon temperature decrease, the membrane "
                                "rigidifies and increases in thickness, "
                                "resulting in activation of the kinase-dominant "
                                "state of DesK"
                            ),
                            "notes": (
                                "Sidarta et al. support the physical "
                                "membrane-state trigger through the B. subtilis "
                                "DesK sensor model."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002213",
                },
                {
                    "subject": "homeoviscous_adaptation_process",
                    "predicate": "positively regulates",
                    "object": "membrane_lipid_remodeling",
                    "description": (
                        "Homeoviscous adaptation increases lipid remodeling "
                        "routes, including fatty-acyl desaturation, that "
                        "counteract bilayer ordering."
                    ),
                    "evidence": [
                        {
                            "reference": SIDARTA,
                            "snippet": (
                                "desaturates the fatty acyl chains, resulting "
                                "in membrane fluidization and concomitant "
                                "decrease of bilayer thickness"
                            ),
                            "notes": (
                                "Sidarta et al. support Des-mediated fatty-acyl "
                                "desaturation as a concrete B. subtilis "
                                "homeoviscous remodeling branch."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002213",
                },
                {
                    "subject": "fab_fatty_acid_branchpoint_enzymes",
                    "predicate": "regulates",
                    "object": "membrane_lipid_remodeling",
                    "description": (
                        "The E. coli FabI/FabB branchpoint valve allocates "
                        "fatty-acid synthesis flux between saturated and "
                        "unsaturated membrane-lipid routes."
                    ),
                    "evidence": [
                        {
                            "reference": HOOGERLAND,
                            "snippet": (
                                "A first element of this regulatory system is a "
                                "temperature-sensitive metabolic valve that "
                                "allocates flux between the saturated and "
                                "unsaturated fatty acid synthesis pathways via "
                                "the branchpoint enzymes FabI and FabB"
                            ),
                            "notes": (
                                "Hoogerland et al. support the E. coli FabI/FabB "
                                "branchpoint valve as a regulator of flux between "
                                "saturated and unsaturated fatty-acid synthesis."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002211",
                },
                {
                    "subject": "membrane_lipid_remodeling",
                    "predicate": "regulates",
                    "object": "membrane_fluidity",
                    "description": (
                        "Temperature-dependent membrane lipid remodeling "
                        "maintains membrane fluidity near a functional setpoint."
                    ),
                    "evidence": [
                        {
                            "reference": HOOGERLAND,
                            "snippet": (
                                "hard-wired parameters calibrate the system to "
                                "generate membrane compositions that maintain "
                                "constant fluidity"
                            ),
                            "notes": (
                                "Hoogerland et al. show that the E. coli "
                                "fatty-acid synthesis system generates "
                                "temperature-specific membrane compositions "
                                "that maintain fluidity."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002211",
                },
                {
                    "subject": "membrane_fluidity",
                    "predicate": "contributes to",
                    "object": "homeoviscous_adaptation_trait",
                    "description": (
                        "Restoration of optimal membrane fluidity is the "
                        "physiological output of homeoviscous adaptation."
                    ),
                    "evidence": [
                        {
                            "reference": HOOGERLAND,
                            "snippet": (
                                "restores optimal membrane fluidity within a "
                                "single generation"
                            ),
                            "notes": (
                                "Hoogerland et al. directly connect the "
                                "homeoviscous fatty-acid control system to "
                                "rapid fluidity restoration."
                            ),
                        },
                    ],
                    "predicate_id": "RO:0002326",
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "homeoviscous-adaptation-xref-gap",
            "prompt": (
                "Resolve an exact external ontology class for organism-level "
                "homeoviscous adaptation before adding a TraitRecord xref."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact GO, PATO, or METPO class is present in the pinned "
                "local snapshot for homeoviscous adaptation. Related lipid "
                "metabolism, fatty-acid desaturation, membrane-fluidity, and "
                "cold-response terms are narrower, broader, or shifted from "
                "the whole-organism membrane-acclimation trait."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        },
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted homeoviscous adaptation as a DOI-backed stress-response "
            "TraitRecord after a repository-wide duplicate review covering "
            "ignored and hidden files; the local METPO snapshot has no exact "
            "homeoviscous-adaptation class and the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v85."
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
