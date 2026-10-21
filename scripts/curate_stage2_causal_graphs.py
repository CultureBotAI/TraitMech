#!/usr/bin/env python3
"""Curate Stage 2 causal_graphs and source-limited knowledge-gap discussions.

Addresses the 24 active CLASS records in environment/, metabolism/, morphology/,
and physiology/ that lacked both a causal_graphs block and an open deferral
discussion:

- Cohort A (10 multi-evidence records): adds a connected, schema-valid
  causal_graphs entry anchored on the trait's existing verbatim evidence
  snippets (one distinct evidence item per edge, zero clause-splitting, zero
  snippet reuse): 5 MECHANISTIC graphs with verified UniProtKB protein_examples
  (capnophilic, pectin_degradation, polar_flagellation, bacteriocin_production,
  coagulase_activity) and 5 NONMECHANISTIC morphological/organelle-behavior
  graphs (lateral_flagellation, polytrichous_flagellation,
  subpolar_flagellation, type_iv_pilus, magnetotaxis).
- Cohort B (14 single-snippet FAPROTAX metabolism records): adds a structured
  record-level OPEN Discussion (kind=KNOWLEDGE_GAP) documenting the
  source-limited mechanism gap and what multi-step pathway/enzyme/taxon
  evidence is required before constructing a causal graph.

Default is dry-run; pass --apply to write changes via the guarded writer
(`traitmech.validation.write_validated` + `record_curation_event`).

Usage:
    python scripts/curate_stage2_causal_graphs.py
    python scripts/curate_stage2_causal_graphs.py --apply
"""

from __future__ import annotations

import argparse
import sys
from collections import deque
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    validate_trait,
    write_validated_trait,
)

TRAITS_DIR = REPO_ROOT / "data" / "traits"
DO_NOT_WORK_PATH = REPO_ROOT / "DO_NOT_WORK.md"
CURATOR = "claude"
CURATION_ACTION_GRAPH = "CURATE_CAUSAL_GRAPH"
CURATION_ACTION_GAP = "RECORD_MECHANISM_KNOWLEDGE_GAP"
POSED_DATE = "2026-10-21"


def _ev_item(doc: dict[str, Any], index: int, notes: str) -> dict[str, str]:
    """Build an edge EvidenceItem from doc['evidence'][index] verbatim."""
    ev_list = doc.get("evidence") or []
    if index >= len(ev_list):
        raise ValueError(
            f"Record {doc.get('identifier')} has only {len(ev_list)} evidence items; "
            f"requested index {index}"
        )
    src = ev_list[index]
    ref = str(src.get("reference") or "").strip()
    snip = str(src.get("snippet") or "").strip()
    if not ref or not snip:
        raise ValueError(
            f"Record {doc.get('identifier')} evidence[{index}] missing reference or snippet"
        )
    return {
        "reference": ref,
        "snippet": snip,
        "notes": notes,
    }


def build_cohort_a_graphs(rel_path: str, doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Construct the connected causal_graphs list for a Cohort A record."""
    if rel_path == "data/traits/environment/capnophilic.yaml":
        return [
            {
                "graph_id": "capnophilic_co2_canb_sketch",
                "title": "Capnophilic elevated-CO2 requirement and CanB contribution",
                "description": (
                    "Evidence-backed causal mechanism linking the capnophilic growth "
                    "phenotype to elevated environmental carbon dioxide and beta-class "
                    "carbonic anhydrase CanB."
                ),
                "scope_status": "MECHANISTIC",
                "scope_notes": (
                    "The taxon-matched protein example anchors the Campylobacter jejuni "
                    "NCTC 11168 CanB (Cj0237/CynT) beta-carbonic anhydrase branch; it "
                    "is not presented as a universal mechanism for every capnophilic organism."
                ),
                "nodes": [
                    {
                        "node_id": "capnophilic_trait",
                        "label": "capnophilic",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1005021",
                        "description": "Requirement for elevated carbon dioxide concentrations for optimal microbial growth.",
                    },
                    {
                        "node_id": "capnophilic_carbon_dioxide",
                        "label": "carbon dioxide",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:16526",
                        "description": "Elevated environmental carbon dioxide required for optimal capnophilic growth.",
                    },
                    {
                        "node_id": "capnophilic_canb_carbonic_anhydrase",
                        "label": "beta-carbonic anhydrase CanB",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "InterPro:IPR001765",
                        "description": "Beta-class carbonic anhydrase (CanB/Cj0237) contributing to capnophilic growth in Campylobacter jejuni.",
                        "protein_examples": [
                            {
                                "uniprot_id": "UniProtKB:Q0PBR7",
                                "protein_label": "Carbonic anhydrase",
                                "gene_symbol": "cynT",
                                "taxon_id": "NCBITaxon:192222",
                                "taxon_label": "Campylobacter jejuni subsp. jejuni serotype O:2 (strain ATCC 700819 / NCTC 11168)",
                                "entry_status": "UNREVIEWED",
                                "entry_version": 98,
                                "sequence_version": 1,
                                "proteome_id": "UP000000799",
                                "retrieved_on": POSED_DATE,
                                "role": "Cytoplasmic beta-carbonic anhydrase CanB (Cj0237/CynT) that is a major contributor to the capnophilic growth phenotype of Campylobacter jejuni NCTC 11168.",
                                "evidence": [
                                    _ev_item(
                                        doc,
                                        1,
                                        "Al-Haideri et al. establish that CanB (Cj0237, UniProtKB:Q0PBR7) is a major contributor to the capnophilic growth phenotype of C. jejuni NCTC 11168.",
                                    )
                                ],
                            }
                        ],
                    },
                ],
                "edges": [
                    {
                        "subject": "capnophilic_trait",
                        "predicate": "depends on",
                        "predicate_id": "RO:0002502",
                        "object": "capnophilic_carbon_dioxide",
                        "description": "Capnophilic growth depends on elevated environmental carbon dioxide concentrations.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Al-Haideri et al. establish that capnophilic Campylobacter jejuni requires high environmental carbon dioxide for optimum growth.",
                            )
                        ],
                    },
                    {
                        "subject": "capnophilic_canb_carbonic_anhydrase",
                        "predicate": "contributes to",
                        "predicate_id": "RO:0002326",
                        "object": "capnophilic_trait",
                        "description": "Beta-carbonic anhydrase CanB contributes to the capnophilic growth phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Al-Haideri et al. show that CanB is a major contributor to the capnophilic growth phenotype of C. jejuni.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/metabolism/pectin_degradation.yaml":
        return [
            {
                "graph_id": "pectin_degradation_catabolic_sketch",
                "title": "Compartmentalized pectin depolymerization and oligogalacturonide catabolism",
                "description": (
                    "Evidence-backed pathway linking secreted pectate lyase "
                    "depolymerization of pectin and compartmentalized oligogalacturonide "
                    "catabolism to the pectin degradation phenotype."
                ),
                "scope_status": "MECHANISTIC",
                "scope_notes": (
                    "The taxon-matched protein example anchors the Dickeya dadantii 3937 "
                    "(Erwinia chrysanthemi 3937) secreted pectate lyase PelA branch of "
                    "extracellular pectin depolymerization."
                ),
                "nodes": [
                    {
                        "node_id": "pectin_degradation_trait",
                        "label": "pectin degradation",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000135",
                        "description": "Biopolymer-degradation metabolism that depolymerizes pectin and catabolizes its breakdown products.",
                    },
                    {
                        "node_id": "pectin_degradation_catabolic_process",
                        "label": "pectin catabolic process",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0045490",
                        "description": "Compartmentalized extracellular depolymerization of pectin to oligogalacturonides and intracellular catabolism of breakdown products.",
                    },
                    {
                        "node_id": "pectin_degradation_pectate_lyase",
                        "label": "pectate lyase",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "InterPro:IPR002022",
                        "description": "Secreted pectate lyase (Pel) that cleaves extracellular pectin to oligogalacturonide intermediates.",
                        "protein_examples": [
                            {
                                "uniprot_id": "UniProtKB:P0C1A3",
                                "protein_label": "Pectate lyase A",
                                "gene_symbol": "pelA",
                                "taxon_id": "NCBITaxon:198628",
                                "taxon_label": "Dickeya dadantii (strain 3937)",
                                "entry_status": "REVIEWED",
                                "entry_version": 88,
                                "sequence_version": 1,
                                "proteome_id": "UP000006859",
                                "retrieved_on": POSED_DATE,
                                "role": "Secreted pectate lyase A (PelA) in Dickeya dadantii 3937 (Erwinia chrysanthemi 3937) that cleaves extracellular pectin to oligogalacturonides during pectin catabolism.",
                                "evidence": [
                                    _ev_item(
                                        doc,
                                        1,
                                        "Hugouvieux-Cotte-Pattat et al. review extracellular pectin degradation to oligogalacturonides in E. chrysanthemi 3937 (Dickeya dadantii 3937), exemplified by reviewed pectate lyase PelA (UniProtKB:P0C1A3).",
                                    )
                                ],
                            }
                        ],
                    },
                ],
                "edges": [
                    {
                        "subject": "pectin_degradation_catabolic_process",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "pectin_degradation_trait",
                        "description": "Compartmentalized catabolism of pectin and its breakdown products confers the pectin degradation trait.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Abbott and Boraston review compartmentalized catabolism of pectin and its breakdown products by pectinolytic bacteria.",
                            )
                        ],
                    },
                    {
                        "subject": "pectin_degradation_pectate_lyase",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "pectin_degradation_catabolic_process",
                        "description": "Secreted pectate lyase mediates extracellular pectin depolymerization to oligogalacturonides during pectin catabolism.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Hugouvieux-Cotte-Pattat et al. describe extracellular pectin degradation forming oligogalacturonides for intracellular catabolism.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/morphology/lateral_flagellation.yaml":
        return [
            {
                "graph_id": "lateral_flagellation_swarming_sketch",
                "title": "Inducible proton-driven lateral flagella and surface swarming",
                "description": (
                    "Evidence-backed causal sketch linking proton-driven lateral "
                    "flagella to the lateral flagellation morphology and surface "
                    "swarming motility."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Morphological arrangement descriptor spanning multiple bacterial "
                    "lineages (DOI:10.1111/j.1574-6968.2006.00403.x, "
                    "DOI:10.1128/jb.167.1.210-218.1986, DOI:10.1128/jb.185.15.4508-4518.2003); "
                    "the record's verbatim evidence quotes characterize organelle-level "
                    "lateral flagellation and proton-driven swarming without naming "
                    "individual protein subunits."
                ),
                "nodes": [
                    {
                        "node_id": "lateral_flagellation_trait",
                        "label": "lateral flagellation",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1005036",
                        "description": "Motility morphology in which flagella emerge from the lateral side of the cell.",
                    },
                    {
                        "node_id": "lateral_flagellation_lateral_flagella",
                        "label": "bacterial-type flagellum",
                        "node_type": "ORGANELLE",
                        "grounding": "GO:0009288",
                        "description": "Inducible lateral flagellar organelles expressed on surfaces or in viscous media.",
                    },
                    {
                        "node_id": "lateral_flagellation_swarming_motility",
                        "label": "swarming motility",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0071973",
                        "description": "Surface translocation enabled by lateral flagella.",
                    },
                    {
                        "node_id": "lateral_flagellation_proton_motive_force",
                        "label": "proton motive force",
                        "node_type": "STATE",
                        "grounding": "METPO:1007500",
                        "description": "Transmembrane proton gradient that powers lateral flagellar rotation during swarming.",
                    },
                ],
                "edges": [
                    {
                        "subject": "lateral_flagellation_lateral_flagella",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "lateral_flagellation_trait",
                        "description": "Expression of an inducible lateral flagella system confers the lateral flagellation morphology.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Merino et al. describe the separate inducible lateral flagella system expressed in viscous media or on surfaces.",
                            )
                        ],
                    },
                    {
                        "subject": "lateral_flagellation_lateral_flagella",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "lateral_flagellation_swarming_motility",
                        "description": "Lateral flagella enable bacterial swarming motility across surfaces.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Belas et al. show that lateral flagella enable bacteria to move over surfaces (swarming).",
                            )
                        ],
                    },
                    {
                        "subject": "lateral_flagellation_proton_motive_force",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "lateral_flagellation_swarming_motility",
                        "description": "Proton-driven lateral flagellar motors power translocation over surfaces during swarming.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Stewart and McCarter report that multiple proton-driven lateral flagella enable surface swarming.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/morphology/polar_flagellation.yaml":
        return [
            {
                "graph_id": "polar_flagellation_flhf_flhg_sketch",
                "title": "FlhF and FlhG polar flagellar placement regulation",
                "description": (
                    "Evidence-backed causal mechanism linking antagonistic FlhF "
                    "GTPase and FlhG ATPase regulation and polar flagellum placement "
                    "to polar flagellation."
                ),
                "scope_status": "MECHANISTIC",
                "scope_notes": (
                    "The taxon-matched protein examples anchor the Vibrio alginolyticus "
                    "FlhF GTPase and FlhG ATPase polar-flagellum placement regulators; "
                    "they are not presented as a universal mechanism for every "
                    "polar-flagellated lineage."
                ),
                "nodes": [
                    {
                        "node_id": "polar_flagellation_trait",
                        "label": "polar flagellation",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1005032",
                        "description": "Motility morphology in which one or more flagella are positioned at one or both cell poles.",
                    },
                    {
                        "node_id": "polar_flagellation_polar_flagellum",
                        "label": "bacterial-type flagellum",
                        "node_type": "ORGANELLE",
                        "grounding": "GO:0009288",
                        "description": "Flagellar organelle positioned at the bacterial cell pole.",
                    },
                    {
                        "node_id": "polar_flagellation_flhf",
                        "label": "FlhF polar flagellar placement GTPase",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "InterPro:IPR020006",
                        "description": "Signal-recognition-particle-like GTPase FlhF that promotes flagellar assembly at the cell pole.",
                        "protein_examples": [
                            {
                                "uniprot_id": "UniProtKB:A0AA36UPE1",
                                "protein_label": "Flagellar biosynthesis protein FlhF",
                                "gene_symbol": "flhF",
                                "taxon_id": "NCBITaxon:663",
                                "taxon_label": "Vibrio alginolyticus",
                                "entry_status": "UNREVIEWED",
                                "entry_version": 12,
                                "sequence_version": 1,
                                "proteome_id": "UP000054316",
                                "retrieved_on": POSED_DATE,
                                "role": "Signal-recognition-particle-like GTPase FlhF that promotes single polar flagellum placement at the cell pole in Vibrio alginolyticus.",
                                "evidence": [
                                    _ev_item(
                                        doc,
                                        2,
                                        "Kojima et al. report that FlhF (UniProtKB:A0AA36UPE1) and FlhG function antagonistically to generate a single flagellum at the cell pole in Vibrio alginolyticus.",
                                    )
                                ],
                            }
                        ],
                    },
                    {
                        "node_id": "polar_flagellation_flhg",
                        "label": "FlhG polar flagellar number regulator ATPase",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "InterPro:IPR033875",
                        "description": "MinD/ParA-family ATPase FlhG (FleN) that antagonizes FlhF to restrict flagellar number at the cell pole.",
                        "protein_examples": [
                            {
                                "uniprot_id": "UniProtKB:Q588V8",
                                "protein_label": "MinD/ParA family protein",
                                "gene_symbol": "flhG",
                                "taxon_id": "NCBITaxon:663",
                                "taxon_label": "Vibrio alginolyticus",
                                "entry_status": "UNREVIEWED",
                                "entry_version": 85,
                                "sequence_version": 1,
                                "proteome_id": "UP000054316",
                                "retrieved_on": POSED_DATE,
                                "role": "MinD/ParA-family ATPase FlhG (FleN) that functions antagonistically with FlhF to restrict Vibrio alginolyticus to a single polar flagellum.",
                                "evidence": [
                                    _ev_item(
                                        doc,
                                        2,
                                        "Kojima et al. report that FlhG (UniProtKB:Q588V8) and FlhF function antagonistically to generate a single flagellum at the cell pole in Vibrio alginolyticus.",
                                    )
                                ],
                            }
                        ],
                    },
                ],
                "edges": [
                    {
                        "subject": "polar_flagellation_polar_flagellum",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "polar_flagellation_trait",
                        "description": "Regular positioning of flagella at the cell pole defines the polar flagellation pattern.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Schuhmacher et al. define regular cell-surface flagellar number and location as the bacterial flagellation pattern.",
                            )
                        ],
                    },
                    {
                        "subject": "polar_flagellation_flhf",
                        "predicate": "contributes to",
                        "predicate_id": "RO:0002326",
                        "object": "polar_flagellation_trait",
                        "description": "FlhF promotes single polar flagellum placement at the cell pole in Vibrio alginolyticus.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Kojima et al. describe the single polar flagellum synthesized at the cell pole in Vibrio alginolyticus.",
                            )
                        ],
                    },
                    {
                        "subject": "polar_flagellation_flhg",
                        "predicate": "regulates",
                        "predicate_id": "RO:0002211",
                        "object": "polar_flagellation_flhf",
                        "description": "FlhG and FlhF function antagonistically to generate a single flagellum at the cell pole.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Kojima et al. report that FlhF and FlhG function antagonistically to generate a single flagellum at the cell pole.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/morphology/polytrichous_flagellation.yaml":
        return [
            {
                "graph_id": "polytrichous_flagellation_tuft_sketch",
                "title": "Polytrichous multi-flagellar tuft arrangement and swimming motility",
                "description": (
                    "Evidence-backed morphology sketch linking monopolar or bipolar "
                    "multi-flagellar tufts to polytrichous flagellation and swimming locomotion."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Morphological arrangement sketch backed by "
                    "DOI:10.1128/AEM.64.10.3576-3583.1998 and "
                    "DOI:10.1128/AEM.68.12.6310-6320.2002; specific flagellar "
                    "structural or placement proteins in Thermocrinis ruber are not "
                    "identified in the cited electron-microscopy and motility sources."
                ),
                "nodes": [
                    {
                        "node_id": "polytrichous_flagellation_trait",
                        "label": "polytrichous flagellation",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1007006",
                        "description": "Flagellar arrangement in which multiple flagella (a tuft) are present per cell.",
                    },
                    {
                        "node_id": "polytrichous_flagellation_flagellar_tuft",
                        "label": "bacterial-type flagellum",
                        "node_type": "ORGANELLE",
                        "grounding": "GO:0009288",
                        "description": "Monopolar or bipolar tuft of multiple bacterial flagella per cell.",
                    },
                    {
                        "node_id": "polytrichous_flagellation_swimming_motility",
                        "label": "locomotion",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0040011",
                        "description": "Swimming pattern driven by polytrichous flagellar tufts.",
                    },
                ],
                "edges": [
                    {
                        "subject": "polytrichous_flagellation_flagellar_tuft",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "polytrichous_flagellation_trait",
                        "description": "Presence of multiple polar flagella per cell confers the polytrichous flagellation phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Huber et al. directly observe monopolar polytrichous flagellation with up to three flagella per cell in Thermocrinis ruber OC 1/4.",
                            )
                        ],
                    },
                    {
                        "subject": "polytrichous_flagellation_flagellar_tuft",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "polytrichous_flagellation_swimming_motility",
                        "description": "Bipolar polytrichous flagella enable rotational and translational swimming locomotion.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Thar and Kuhl connect bipolar polytrichous flagella to a distinct swimming pattern.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/morphology/subpolar_flagellation.yaml":
        return [
            {
                "graph_id": "subpolar_flagellation_surface_assembly_sketch",
                "title": "Subpolar flagellar assembly and cell-surface placement",
                "description": (
                    "Evidence-backed morphology sketch linking cell-surface assembly "
                    "of subpolar flagella to the subpolar flagellation phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Morphological placement sketch backed by DOI:10.1128/JB.01405-06 "
                    "and DOI:10.3390/biom10050774; strain-matched UniProtKB protein "
                    "examples for the Bradyrhizobium diazoefficiens USDA 110 subpolar "
                    "flagellin or placement factors remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "subpolar_flagellation_trait",
                        "label": "subpolar flagellation",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1005037",
                        "description": "Motility morphology in which flagella emerge from subpolar positions near the cell pole.",
                    },
                    {
                        "node_id": "subpolar_flagellation_subpolar_flagellum",
                        "label": "bacterial-type flagellum",
                        "node_type": "ORGANELLE",
                        "grounding": "GO:0009288",
                        "description": "Flagellar organelle emerging at a subpolar position on the bacterial cell surface.",
                    },
                    {
                        "node_id": "subpolar_flagellation_flagellum_assembly",
                        "label": "bacterial-type flagellum assembly",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0044780",
                        "description": "Assembly of a membrane-traversing subpolar flagellum on the cell surface.",
                    },
                ],
                "edges": [
                    {
                        "subject": "subpolar_flagellation_subpolar_flagellum",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "subpolar_flagellation_trait",
                        "description": "Flagellar systems growing at subpolar positions confer the subpolar flagellation morphology.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Kanbe et al. describe thick and thin flagellar systems uniquely growing at subpolar positions in Bradyrhizobium.",
                            )
                        ],
                    },
                    {
                        "subject": "subpolar_flagellation_flagellum_assembly",
                        "predicate": "contributes to",
                        "predicate_id": "RO:0002326",
                        "object": "subpolar_flagellation_subpolar_flagellum",
                        "description": "Cell-surface flagellar assembly forms the membrane-traversing subpolar flagellum.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Camarena and Dreyfus describe assembly of a single membrane-traversing subpolar flagellum on the cell surface.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/morphology/type_iv_pilus.yaml":
        return [
            {
                "graph_id": "type_iv_pilus_extension_retraction_sketch",
                "title": "Type IV pilus cell-surface appendage and dynamic extension-retraction",
                "description": (
                    "Evidence-backed morphology sketch linking cell-surface type IV "
                    "pili fibers and their dynamic extension and retraction to the "
                    "type IV pilus trait."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Appendage-and-dynamics sketch backed by DOI:10.1093/femsre/fuab053 "
                    "and DOI:10.1042/BST20160221; PilA/PilB/PilT protein nodes with "
                    "strain-matched UniProtKB accessions for Pseudomonas aeruginosa "
                    "PAO1 remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "type_iv_pilus_trait",
                        "label": "type IV pilus",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000175",
                        "description": "Morphology trait in which a cell produces extracellular type IV pilus filaments that dynamically extend and retract.",
                    },
                    {
                        "node_id": "type_iv_pilus_appendage",
                        "label": "type IV pilus complex",
                        "node_type": "CELLULAR_LOCALIZATION",
                        "grounding": "GO:0044096",
                        "description": "Hair-like prokaryotic surface appendage composed of type IV pilin subunits.",
                    },
                    {
                        "node_id": "type_iv_pilus_extension_retraction",
                        "label": "pilus-dependent motility",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0071972",
                        "description": "Dynamic extension and retraction of type IV pilus fibers.",
                    },
                    {
                        "node_id": "type_iv_pilus_cell_surface",
                        "label": "cell surface",
                        "node_type": "CELLULAR_LOCALIZATION",
                        "grounding": "GO:0009986",
                        "description": "Bacterial or archaeal cell surface from which type IV pili extend.",
                    },
                ],
                "edges": [
                    {
                        "subject": "type_iv_pilus_appendage",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "type_iv_pilus_trait",
                        "description": "Production of type IV pili appendages confers the type IV pilus morphology trait.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Ellison et al. review type IV pili (T4P) as prokaryotic appendages across bacteria and archaea.",
                            )
                        ],
                    },
                    {
                        "subject": "type_iv_pilus_appendage",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "type_iv_pilus_extension_retraction",
                        "description": "Type IV pilus fibers dynamically extend and retract.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Ellison et al. describe T4P as broadly distributed fibers that dynamically extend and retract.",
                            )
                        ],
                    },
                    {
                        "subject": "type_iv_pilus_appendage",
                        "predicate": "located in",
                        "predicate_id": "biolink:located_in",
                        "object": "type_iv_pilus_cell_surface",
                        "description": "Type IV pili are hair-like appendages localized on the bacterial cell surface.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Piepenbrink and Sundberg characterize type IV pili as hair-like bacterial surface appendages.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/bacteriocin_production.yaml":
        return [
            {
                "graph_id": "bacteriocin_production_defense_mechanism",
                "title": "Ribosomal bacteriocin peptide production and antibacterial defense",
                "description": (
                    "Evidence-backed physiological mechanism linking ribosomally "
                    "synthesized bacteriocin peptides to the bacteriocin production "
                    "trait and microbial defense against competing bacteria."
                ),
                "scope_status": "MECHANISTIC",
                "scope_notes": (
                    "Peptide-anchored mechanism backed by "
                    "DOI:10.3389/fmicb.2016.00461 and "
                    "DOI:10.1146/annurev.micro.56.012302.161024, with reviewed "
                    "Lactococcus lactis subsp. lactis lantibiotic nisin-A "
                    "(UniProtKB:P13068) curated on the InterPro:IPR006079 "
                    "bacteriocin peptide node."
                ),
                "nodes": [
                    {
                        "node_id": "bacteriocin_production_trait",
                        "label": "bacteriocin production",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000183",
                        "description": "Physiological trait in which bacteria synthesize antimicrobial bacteriocin peptides or proteins.",
                    },
                    {
                        "node_id": "bacteriocin_production_lantibiotic",
                        "label": "Lantibiotic type-A",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "InterPro:IPR006079",
                        "description": "Ribosomally synthesized antimicrobial bacteriocin peptide family exemplified by Lactococcus lactis nisin-A.",
                        "protein_examples": [
                            {
                                "uniprot_id": "UniProtKB:P13068",
                                "entry_status": "REVIEWED",
                                "entry_version": 93,
                                "sequence_version": 1,
                                "retrieved_on": POSED_DATE,
                                "gene_symbol": "spaN",
                                "protein_label": "Lantibiotic nisin-A",
                                "taxon_id": "NCBITaxon:1360",
                                "taxon_label": "Lactococcus lactis subsp. lactis",
                                "role": "Ribosomally synthesized class I lantibiotic bacteriocin peptide produced by Lactococcus lactis subsp. lactis.",
                                "evidence": [
                                    _ev_item(
                                        doc,
                                        0,
                                        "Rea et al. define bacteriocins as ribosomally synthesized antimicrobial peptides produced by bacteria, exemplified by Lactococcus lactis nisin-A (UniProtKB:P13068).",
                                    )
                                ],
                            }
                        ],
                    },
                    {
                        "node_id": "bacteriocin_production_antibacterial_defense",
                        "label": "defense response to bacterium",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0042742",
                        "description": "Microbial defense function killing or inhibiting competing bacteria.",
                    },
                ],
                "edges": [
                    {
                        "subject": "bacteriocin_production_lantibiotic",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "bacteriocin_production_trait",
                        "description": "Ribosomally synthesized antimicrobial bacteriocin peptides confer the bacteriocin production trait.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Rea et al. define bacteriocins as ribosomally synthesized antimicrobial peptides produced by bacteria.",
                            )
                        ],
                    },
                    {
                        "subject": "bacteriocin_production_lantibiotic",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "bacteriocin_production_antibacterial_defense",
                        "description": "Bacteriocin peptides function as microbial defense systems against competing bacteria.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Riley and Wertz characterize bacteriocins as an abundant and diverse family of microbial defense systems.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/coagulase_activity.yaml":
        return [
            {
                "graph_id": "coagulase_activity_prothrombin_mechanism",
                "title": "Staphylococcal coagulase prothrombin activation and fibrinogen cleavage",
                "description": (
                    "Evidence-backed physiological mechanism linking secreted "
                    "staphylocoagulases (Coa and vWbp) to non-proteolytic "
                    "prothrombin activation and fibrinogen cleavage."
                ),
                "scope_status": "MECHANISTIC",
                "scope_notes": (
                    "Protein-anchored mechanism backed by DOI:10.1159/000333447 "
                    "and DOI:10.1371/journal.ppat.1001036, with reviewed "
                    "Staphylococcus aureus staphylocoagulase Coa "
                    "(UniProtKB:P07767) curated on the InterPro:IPR019553 "
                    "coagulase node."
                ),
                "nodes": [
                    {
                        "node_id": "coagulase_activity_trait",
                        "label": "coagulase activity",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1007089",
                        "description": "Physiological enzyme-activity phenotype in which secreted coagulase factors activate prothrombin and clot plasma.",
                    },
                    {
                        "node_id": "coagulase_activity_staphylocoagulase",
                        "label": "staphylocoagulase family protein",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": "InterPro:IPR019553",
                        "description": "Secreted staphylococcal coagulase polypeptides (Coa and vWbp) that bind and non-proteolytically activate prothrombin.",
                        "protein_examples": [
                            {
                                "uniprot_id": "UniProtKB:P07767",
                                "entry_status": "REVIEWED",
                                "entry_version": 82,
                                "sequence_version": 2,
                                "retrieved_on": POSED_DATE,
                                "gene_symbol": "coa",
                                "protein_label": "Staphylocoagulase",
                                "taxon_id": "NCBITaxon:1280",
                                "taxon_label": "Staphylococcus aureus",
                                "role": "Secreted Staphylococcus aureus coagulase (Coa) that binds and non-proteolytically activates host prothrombin to cleave fibrinogen.",
                                "evidence": [
                                    _ev_item(
                                        doc,
                                        1,
                                        "Cheng et al. demonstrate that Staphylococcus aureus Coa (UniProtKB:P07767) promotes non-proteolytic activation of prothrombin and cleavage of fibrinogen.",
                                    )
                                ],
                            }
                        ],
                    },
                    {
                        "node_id": "coagulase_activity_prothrombin_activation",
                        "label": "zymogen activation",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0031638",
                        "description": "Non-proteolytic activation of host prothrombin and downstream conversion of fibrinogen to fibrin.",
                    },
                ],
                "edges": [
                    {
                        "subject": "coagulase_activity_staphylocoagulase",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "coagulase_activity_trait",
                        "description": "Secreted staphylococcal coagulase polypeptides confer the coagulase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "McAdow, Missiakas, and Schneewind describe secreted Staphylococcus aureus coagulases that bind to and activate prothrombin.",
                            )
                        ],
                    },
                    {
                        "subject": "coagulase_activity_staphylocoagulase",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "coagulase_activity_prothrombin_activation",
                        "description": "Coa and vWbp promote non-proteolytic activation of prothrombin and cleavage of fibrinogen.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Cheng et al. demonstrate that Coa and vWbp promote non-proteolytic activation of prothrombin and cleavage of fibrinogen.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/magnetotaxis.yaml":
        return [
            {
                "graph_id": "magnetotaxis_magnetosome_navigation_sketch",
                "title": "Magnetosome chain alignment and geomagnetic navigation",
                "description": (
                    "Evidence-backed physiological sketch linking magnetosome "
                    "chain alignment to magnetoreception and directed motility "
                    "along geomagnetic field lines."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Organelle-to-behavior sketch backed by DOI:10.1128/JB.00398-20, "
                    "DOI:10.1038/s41396-018-0098-9, and DOI:10.1128/mbio.01649-23; "
                    "MamK/MamJ magnetoskeleton protein examples are curated on the "
                    "companion `data/traits/morphology/magnetosome.yaml` organelle "
                    "record rather than duplicated here without a protein node."
                ),
                "nodes": [
                    {
                        "node_id": "magnetotaxis_trait",
                        "label": "magnetotaxis",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000176",
                        "description": "Behavioral physiology in which magnetosome-bearing motile cells align and navigate along geomagnetic field lines.",
                    },
                    {
                        "node_id": "magnetotaxis_magnetosome_organelle",
                        "label": "magnetosome",
                        "node_type": "ORGANELLE",
                        "grounding": "GO:0110143",
                        "description": "Membrane-bounded magnetic-mineral organelle aligned into intracellular chains in magnetotactic bacteria.",
                    },
                    {
                        "node_id": "magnetotaxis_magnetoreception",
                        "label": "magnetoreception",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0050958",
                        "description": "Detection and alignment with Earth's geomagnetic field for cellular orientation and navigation.",
                    },
                    {
                        "node_id": "magnetotaxis_directed_motility",
                        "label": "taxis",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0042330",
                        "description": "Directed microbial motility along geomagnetic field lines.",
                    },
                ],
                "edges": [
                    {
                        "subject": "magnetotaxis_magnetosome_organelle",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "magnetotaxis_magnetoreception",
                        "description": "Alignment of magnetosome organelles into chains enables geomagnetic field navigation.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Awal et al. state that magnetotactic bacteria align their magnetosome organelles into chains to navigate within the geomagnetic field.",
                            )
                        ],
                    },
                    {
                        "subject": "magnetotaxis_magnetoreception",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "magnetotaxis_directed_motility",
                        "description": "Prokaryotic magnetoreception enables detection of Earth's magnetic field for orientation and directed navigation.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Lin et al. describe magnetotaxis as prokaryotic magnetoreception enabling detection of Earth's magnetic field for orientation and navigation.",
                            )
                        ],
                    },
                    {
                        "subject": "magnetotaxis_directed_motility",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "magnetotaxis_trait",
                        "description": "Directed motility guided by Earth's magnetic field confers the magnetotaxis phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Muller et al. define magnetotactic bacteria by their ability to use Earth's magnetic field for directed motility.",
                            )
                        ],
                    },
                ],
            }
        ]

    raise KeyError(f"Unexpected Cohort A path: {rel_path}")


COHORT_A_PATHS: tuple[str, ...] = (
    "data/traits/environment/capnophilic.yaml",
    "data/traits/metabolism/pectin_degradation.yaml",
    "data/traits/morphology/lateral_flagellation.yaml",
    "data/traits/morphology/polar_flagellation.yaml",
    "data/traits/morphology/polytrichous_flagellation.yaml",
    "data/traits/morphology/subpolar_flagellation.yaml",
    "data/traits/morphology/type_iv_pilus.yaml",
    "data/traits/physiology/bacteriocin_production.yaml",
    "data/traits/physiology/coagulase_activity.yaml",
    "data/traits/physiology/magnetotaxis.yaml",
)


COHORT_B_GAPS: dict[str, tuple[str, str]] = {
    "data/traits/metabolism/aromatic_compound_degradation.yaml": (
        "Add multi-step ring-cleavage pathway evidence (e.g. catechol or protocatechuate dioxygenase enzymes, substrates, and products) and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single broad FAPROTAX review snippet (DOI:10.3390/ijerph6010278) naming bacterial degradation pathways of aromatic compounds without specific enzyme or intermediate claims; constructing a multi-edge causal graph from that single 60-character phrase would require clause-splitting or unsupported edges.",
    ),
    "data/traits/metabolism/aromatic_hydrocarbon_degradation.yaml": (
        "Add primary literature evidence for aromatic-ring hydroxylation and cleavage enzymes (e.g. benzene/biphenyl dioxygenase) and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single substrate-list snippet (DOI:10.1007/BF00058836) enumerating benzene, arenes, biphenyl, and fused aromatic hydrocarbons without catalytic or pathway-step assertions.",
    ),
    "data/traits/metabolism/dark_hydrogen_oxidation.yaml": (
        "Add primary literature evidence for uptake [NiFe]-hydrogenase catalysis, terminal electron-acceptor coupling, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single ecological review snippet (DOI:10.3389/fmicb.2018.02873) describing hydrothermal-vent biomass production by hydrogen-oxidizing organisms without enzyme-level or electron-transport claims.",
    ),
    "data/traits/metabolism/dark_oxidation_of_sulfur_compounds.yaml": (
        "Add primary literature evidence for sulfur-oxidizing enzyme complexes (e.g. Sox, Sqr, or Dsr pathways) and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single physiological rate snippet (DOI:10.1111/1462-2920.14543) coupling dark sulfide oxidation to oxygen consumption without enzyme or intermediate assertions.",
    ),
    "data/traits/metabolism/hydrocarbon_degradation.yaml": (
        "Add primary literature evidence for alkane monooxygenase or anaerobic hydrocarbon-activating enzymes and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single high-level review snippet (DOI:10.1128/MR.54.3.305-315.1990) stating that hydrocarbons are degraded primarily by bacteria and fungi, which is insufficient to ground a multi-edge mechanism graph without inventing unsupported edges.",
    ),
    "data/traits/metabolism/hydrogenotrophic_methanogenesis.yaml": (
        "Add primary literature evidence for the H2/CO2 methanogenesis pathway steps (e.g. Fmd/Fwd, Mch, Mtd, Mer, Mtr, Mcr, and energy-converting hydrogenases) and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single 26-character phrase ('from CO2 and H2 to methane' in DOI:10.1146/annurev-micro-011720-122807); building a multi-edge graph from one short phrase would violate the snippet-diversity and anti-clause-splitting rules.",
    ),
    "data/traits/metabolism/methanol_oxidation.yaml": (
        "Add primary literature evidence for PQQ- or NAD-dependent methanol dehydrogenase (MxaFI/XoxF/Mdh), formaldehyde oxidation, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single 37-character phrase ('methanol utilization in methylotrophy' in DOI:10.3389/fbioe.2021.787791) without verbatim catalytic or electron-transfer quotes in the evidence block.",
    ),
    "data/traits/metabolism/nitrate_reduction.yaml": (
        "Add primary literature evidence distinguishing assimilatory (Nas), respiratory (Nar), and dissimilatory/periplasmic (Nap) nitrate reductase reactions and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single overview snippet (DOI:10.1128/JB.181.21.6573-6584.1999) noting that nitrate reduction serves three purposes, without verbatim quotes for the individual reductase branches.",
    ),
    "data/traits/metabolism/nitrate_respiration.yaml": (
        "Add primary literature evidence for respiratory nitrate reductase (NarGHI/NapAB), electron-transport phosphorylation, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single snippet (DOI:10.1126/science.1254070) contrasting denitrification and ammonification endpoints without enzyme-level nitrate-to-nitrite respiratory mechanism quotes.",
    ),
    "data/traits/metabolism/nitrite_respiration.yaml": (
        "Add a second independent evidence snippet covering electron donation or proton-motive-force coupling alongside NrfA/NirS/NirK nitrite reduction and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single evidence item (DOI:10.1074/jbc.M709090200) on Escherichia coli NrfA reduction of nitrite to ammonium; a connected multi-edge graph requires at least two independent verbatim snippets so no single quote is reused or clause-split across edges.",
    ),
    "data/traits/metabolism/nitrogen_respiration.yaml": (
        "Add primary literature evidence for nitrogen-oxide respiratory reductases, electron-transport chains, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single 38-character snippet ('N oxides as terminal electron acceptors' in DOI:10.1128/mmbr.61.4.533-616.1997), which supports the upper-level class definition but not a multi-edge mechanism graph.",
    ),
    "data/traits/metabolism/respiration_of_sulfur_compounds.yaml": (
        "Add primary literature evidence for dissimilatory sulfur/sulfate/thiosulfate reductases (e.g. DsrAB, PsrABC, PhsABC) and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single 42-character snippet ('sulfate, sulfur, or thiosulfate respiration' in DOI:10.3389/fmicb.2023.1108245) enumerating the respiratory subclasses without enzymatic mechanism quotes.",
    ),
    "data/traits/metabolism/sulfur_respiration.yaml": (
        "Add primary literature evidence for polysulfide/elemental-sulfur reductase (PsrABC or SreABC), sulfide production, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single 48-character snippet ('using sulfur as an alternative electron acceptor' in DOI:10.3389/fmicb.2023.1108245) without a second independent mechanistic quote to support a connected multi-edge graph.",
    ),
    "data/traits/metabolism/thiosulfate_respiration.yaml": (
        "Add primary literature evidence for thiosulfate reductase (PhsABC), sulfite/sulfide products, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single 45-character snippet ('sulfur- and thiosulfate reducing type strain' in DOI:10.3389/fmicb.2023.1108245) without enzymatic or product-level quotes needed for a multi-edge causal graph.",
    ),
}


def _verify_graph_invariants(rel_path: str, doc: dict[str, Any], graphs: list[dict[str, Any]]) -> None:
    """Verify structural, grounding, and snippet invariants before writing."""
    trait_id = str(doc.get("identifier") or "")
    for graph in graphs:
        nodes = graph.get("nodes") or []
        edges = graph.get("edges") or []
        if len(nodes) < 3 or len(edges) < 2:
            raise ValueError(f"{rel_path}: graph must have >=3 nodes and >=2 edges")
        node_ids = [str(n.get("node_id") or "") for n in nodes]
        if len(node_ids) != len(set(node_ids)):
            raise ValueError(f"{rel_path}: duplicate node_id in {node_ids}")
        groundings = [str(n.get("grounding") or "") for n in nodes]
        if any(not g for g in groundings):
            raise ValueError(f"{rel_path}: ungrounded node in {nodes}")
        if len(groundings) != len(set(groundings)):
            raise ValueError(f"{rel_path}: duplicate node grounding in {groundings}")
        trait_nodes = [
            n for n in nodes
            if n.get("node_type") == "TRAIT" and n.get("grounding") == trait_id
        ]
        if not trait_nodes:
            raise ValueError(f"{rel_path}: missing TRAIT anchor node grounded to {trait_id}")

        adj: dict[str, set[str]] = {nid: set() for nid in node_ids}
        snippets: list[str] = []
        for edge in edges:
            s = str(edge.get("subject") or "")
            o = str(edge.get("object") or "")
            if s not in adj or o not in adj:
                raise ValueError(f"{rel_path}: dangling edge {s}->{o}")
            if s == o:
                raise ValueError(f"{rel_path}: self-loop on {s}")
            if not edge.get("predicate") or not edge.get("predicate_id"):
                raise ValueError(f"{rel_path}: missing predicate/predicate_id on {s}->{o}")
            adj[s].add(o)
            adj[o].add(s)
            ev_list = edge.get("evidence") or []
            if not ev_list:
                raise ValueError(f"{rel_path}: missing evidence on {s}->{o}")
            for ev in ev_list:
                snip = str(ev.get("snippet") or "").strip()
                if len(snip) < 12 or "..." in snip or "…" in snip:
                    raise ValueError(f"{rel_path}: invalid snippet on {s}->{o}: {snip!r}")
                snippets.append(snip)

        if len(snippets) != len(set(snippets)):
            raise ValueError(f"{rel_path}: reused snippet across edges: {snippets}")

        # Connected component check
        visited: set[str] = set()
        queue: deque[str] = deque([node_ids[0]])
        visited.add(node_ids[0])
        while queue:
            curr = queue.popleft()
            for nb in adj[curr]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        if len(visited) != len(node_ids):
            raise ValueError(f"{rel_path}: disconnected graph ({len(visited)}/{len(node_ids)} reached)")

        if graph.get("scope_status") == "MECHANISTIC":
            protein_nodes_with_examples = [
                n for n in nodes
                if n.get("node_type") == "GENE_OR_PROTEIN" and (n.get("protein_examples") or [])
            ]
            if not protein_nodes_with_examples:
                raise ValueError(f"{rel_path}: MECHANISTIC graph must have >=1 GENE_OR_PROTEIN node with protein_examples")
            if not (doc.get("canonical_examples") or []):
                raise ValueError(f"{rel_path}: MECHANISTIC graph requires cited canonical_examples on record")


PECTIN_CANONICAL_EXAMPLES: list[dict[str, str]] = [
    {
        "taxon_id": "NCBITaxon:198628",
        "taxon_label": "Dickeya dadantii 3937",
        "note": (
            "Hugouvieux-Cotte-Pattat et al. review extracellular pectin "
            "depolymerization and intracellular oligogalacturonide catabolism "
            "in Erwinia chrysanthemi strain 3937 (now Dickeya dadantii 3937)."
        ),
        "reference": "DOI:10.1146/annurev.micro.50.1.213",
    }
]


def build_cohort_b_discussion(rel_path: str, doc: dict[str, Any]) -> dict[str, Any]:
    """Construct the KNOWLEDGE_GAP DiscussionItem for a Cohort B record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale = COHORT_B_GAPS[rel_path]
    ev_list = doc.get("evidence") or []
    supporting_ev: list[dict[str, str]] = []
    if ev_list and isinstance(ev_list[0], dict):
        src = ev_list[0]
        ref = str(src.get("reference") or "").strip()
        snip = str(src.get("snippet") or "").strip()
        if ref and snip:
            supporting_ev.append(
                {
                    "reference": ref,
                    "supports": "PARTIAL",
                    "snippet": snip,
                    "explanation": (
                        "Existing record-level evidence supports the high-level "
                        "metabolic trait definition but does not provide multi-step "
                        "enzymatic mechanism quotes for a connected causal graph."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-causal-graph-source-gap",
        "prompt": prompt,
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


def process_all(apply: bool = False) -> tuple[int, int]:
    """Process Cohort A and Cohort B records. Returns (graphs_added, gaps_added)."""
    graphs_added = 0
    gaps_added = 0

    for rel_path in COHORT_A_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = build_cohort_a_graphs(rel_path, doc)
        needs_pectin_canon = (
            rel_path == "data/traits/metabolism/pectin_degradation.yaml"
            and doc.get("canonical_examples") != PECTIN_CANONICAL_EXAMPLES
        )
        if doc.get("causal_graphs") == graphs and not needs_pectin_canon:
            continue
        if needs_pectin_canon:
            doc["canonical_examples"] = [dict(item) for item in PECTIN_CANONICAL_EXAMPLES]
            record_curation_event(
                doc,
                action="ADD_CANONICAL_EXAMPLES",
                curator=CURATOR,
                changes=(
                    "Added source-backed canonical example Dickeya dadantii 3937 "
                    "(NCBITaxon:198628; DOI:10.1146/annurev.micro.50.1.213) from "
                    "existing record evidence on Erwinia chrysanthemi strain 3937."
                ),
                llm_assisted=True,
            )
        _verify_graph_invariants(rel_path, doc, graphs)
        doc["causal_graphs"] = graphs
        scope_status = graphs[0]["scope_status"]
        record_curation_event(
            doc,
            action=CURATION_ACTION_GRAPH,
            curator=CURATOR,
            changes=(
                f"Added {scope_status} causal_graphs entry ({graphs[0]['graph_id']}) "
                "anchored on existing verbatim record evidence snippets."
            ),
            llm_assisted=True,
        )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        graphs_added += 1

    for rel_path in sorted(COHORT_B_GAPS):
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        existing_disc = doc.get("discussions") or []
        disc_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        disc = build_cohort_b_discussion(rel_path, doc)
        matched = [d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id]
        if matched:
            if matched[0] == disc:
                continue
            for idx, d in enumerate(existing_disc):
                if isinstance(d, dict) and d.get("discussion_id") == disc_id:
                    existing_disc[idx] = disc
            doc["discussions"] = existing_disc
        else:
            existing_disc.append(disc)
            doc["discussions"] = existing_disc
            record_curation_event(
                doc,
                action=CURATION_ACTION_GAP,
                curator=CURATOR,
                changes=(
                    f"Recorded OPEN KNOWLEDGE_GAP discussion ({disc_id}) documenting "
                    "the source-limited mechanism gap for causal_graphs."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        gaps_added += 1

    return graphs_added, gaps_added


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to data/traits/ via write_validated (default: dry-run).",
    )
    args = parser.parse_args(argv)
    graphs_added, gaps_added = process_all(apply=args.apply)
    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(
        f"[{mode}] Cohort A causal_graphs added: {graphs_added}; "
        f"Cohort B KNOWLEDGE_GAP discussions added: {gaps_added}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
