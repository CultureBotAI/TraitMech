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
POSED_DATE_C2 = "2026-10-23"
POSED_DATE_C4 = "2026-10-25"
POSED_DATE_C5 = "2026-10-25"
POSED_DATE_C6 = "2026-10-26"


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

COHORT_C_PATHS: tuple[str, ...] = (
    "data/traits/metabolism/arsenate_respiration.yaml",
    "data/traits/metabolism/chlorate_respiration.yaml",
    "data/traits/metabolism/dimethyl_sulfoxide_respiration.yaml",
    "data/traits/metabolism/fumarate_respiration.yaml",
    "data/traits/metabolism/perchlorate_respiration.yaml",
    "data/traits/metabolism/tetrathionate_respiration.yaml",
    "data/traits/metabolism/trimethylamine_n_oxide_respiration.yaml",
    "data/traits/physiology/arginine_dihydrolase_activity.yaml",
    "data/traits/physiology/lysine_decarboxylase_activity.yaml",
    "data/traits/physiology/siderophore_production.yaml",
)

COHORT_C_PROTEIN_GAPS: dict[str, tuple[str, str, int]] = {
    "data/traits/metabolism/arsenate_respiration.yaml": (
        "Add strain-matched UniProtKB protein_examples for Shewanella sp. ANA-3 respiratory arsenate reductase subunits (ArrA/ArrB) so arsenate_respiration_arr_pathway_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1073/pnas.1834303100, DOI:10.1128/AEM.69.5.2800-2809.2003, DOI:10.1128/JB.01110-07) supports respiratory arsenate reduction to arsenite via arsenate respiratory reductase (ARR) in Shewanella sp. ANA-3 (NCBITaxon:94122), but verified UniProtKB accessions and proteome metadata must be added to a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        0,
    ),
    "data/traits/metabolism/chlorate_respiration.yaml": (
        "Add strain-matched UniProtKB protein_examples for Ideonella dechloratans chlorate reductase (ClrABC) and chlorite dismutase (Cld) so chlorate_respiration_pathway_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1128/AEM.69.9.5585-5592.2003, DOI:10.1128/AEM.07303-11) supports the two-step dissimilatory chlorate reduction pathway (chlorate reduction followed by chlorite decomposition) in Ideonella dechloratans (NCBITaxon:36863), but verified UniProtKB accessions must be added to a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/metabolism/dimethyl_sulfoxide_respiration.yaml": (
        "Add strain-matched UniProtKB protein_examples for the Shewanella oneidensis MR-1 SO1427-SO1432 (DmsEFABGH) extracellular DMSO reductase complex so dmso_respiration_reductase_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1073/pnas.0505959103, DOI:10.1111/1462-2920.15971) establishes the SO1427-SO1432 gene cluster required for extracellular DMSO respiration in Shewanella oneidensis MR-1 (NCBITaxon:211586), but verified UniProtKB accessions must be curated on a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        0,
    ),
    "data/traits/metabolism/fumarate_respiration.yaml": (
        "Add strain-matched UniProtKB protein_examples for Bacteroides fragilis fumarate reductase subunits (FrdCAB) so fumarate_respiration_frd_pathway_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1128/mBio.03238-19, DOI:10.1128/JB.00389-22) establishes fumarate reductase (FRD) catalysis and NADH-to-fumarate respiratory electron transfer in Bacteroides fragilis (NCBITaxon:817), but verified UniProtKB accessions must be curated on a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        0,
    ),
    "data/traits/metabolism/perchlorate_respiration.yaml": (
        "Add a strain-matched canonical_examples entry and UniProtKB protein_examples for perchlorate reductase (PcrABCD) and chlorite dismutase (Cld) (e.g., in candidate exemplar Dechloromonas aromatica RCB) so perchlorate_respiration_reduction_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature by Melnyk et al. (DOI:10.1186/s12864-015-2011-5, DOI:10.1128/AEM.05758-11) supports periplasmic reduction of perchlorate to chlorite by perchlorate reductase (PcrABCD) and chlorite dismutation to chloride and O2 by chlorite dismutase (Cld), but canonical_examples and verified strain-matched UniProtKB accessions must be curated before marking the graph MECHANISTIC.",
        0,
    ),
    "data/traits/metabolism/tetrathionate_respiration.yaml": (
        "Add strain-matched UniProtKB protein_examples for Salmonella enterica serovar Typhimurium LT2 tetrathionate reductase subunits (TtrA/TtrB/TtrC) so tetrathionate_respiration_ttr_pathway_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1046/j.1365-2958.1999.01345.x, DOI:10.1128/JB.183.8.2463-2475.2001) identifies the ttrABC structural genes and tetrathionate-to-thiosulfate reduction in Salmonella enterica serovar Typhimurium LT2 (NCBITaxon:99287), but verified UniProtKB accessions must be curated on a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/metabolism/trimethylamine_n_oxide_respiration.yaml": (
        "Add strain-matched UniProtKB protein_examples for Escherichia coli K-12 TMAO reductase (TorA/TorC) encoded by the torCAD operon so tmao_respiration_tor_pathway_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1111/1462-2920.12726, DOI:10.3389/fmicb.2024.1467153) establishes anaerobic respiratory growth on TMAO and reduction of TMAO to trimethylamine by torCAD-encoded TMAO reductase in Escherichia coli K-12 (NCBITaxon:83333), but verified UniProtKB accessions must be curated on a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        0,
    ),
    "data/traits/physiology/arginine_dihydrolase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Latilactobacillus sakei arc-operon arginine deiminase pathway enzymes (ArcA, ArcB, ArcC) so arginine_dihydrolase_adi_pathway_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1016/j.fm.2010.11.016, DOI:10.1128/aem.07724-11, DOI:10.1016/j.resmic.2012.11.004) establishes arc-operon ADI pathway conversion of arginine to citrulline and ornithine in Latilactobacillus sakei (NCBITaxon:1599), but verified UniProtKB accessions must be curated on a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        3,
    ),
    "data/traits/physiology/lysine_decarboxylase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Escherichia coli inducible lysine decarboxylase (CadA) and lysine-cadaverine antiporter (CadB) so lysine_decarboxylase_cadba_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 4.1.1.18, DOI:10.1128/jb.01306-06) establishes the CadBA lysine-dependent acid-resistance decarboxylation of L-lysine to cadaverine and CO2 in Escherichia coli (NCBITaxon:562), but verified UniProtKB accessions must be curated on a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/physiology/siderophore_production.yaml": (
        "Add strain-matched UniProtKB protein_examples for Pseudomonas aeruginosa pyoverdine synthetase/transport proteins (e.g. PvdD, PvdL, FpvA) so siderophore_production_iron_scavenging_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1111/1462-2920.14937, DOI:10.15698/mic2018.10.649, DOI:10.1073/pnas.0908760106) establishes pyoverdine siderophore biosynthesis and extracellular iron scavenging in Pseudomonas aeruginosa (NCBITaxon:287), but verified UniProtKB accessions must be curated on a GENE_OR_PROTEIN node before marking the graph MECHANISTIC.",
        2,
    ),
}


def build_cohort_c_graphs(rel_path: str, doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Construct the connected NONMECHANISTIC causal_graphs list for a Cohort C record."""
    if rel_path == "data/traits/metabolism/arsenate_respiration.yaml":
        return [
            {
                "graph_id": "arsenate_respiration_arr_pathway_sketch",
                "title": "Respiratory arsenate reduction to arsenite and terminal electron acceptor pathway",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking dissimilatory "
                    "arsenate respiratory reductase (ARR) activity, arsenite "
                    "production, and arsenate terminal electron acceptance to "
                    "arsenate respiration."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway-and-activity sketch backed by DOI:10.1073/pnas.1834303100, "
                    "DOI:10.1128/AEM.69.5.2800-2809.2003, and DOI:10.1128/JB.01110-07; "
                    "strain-matched UniProtKB protein examples for the Shewanella sp. "
                    "ANA-3 respiratory arsenate reductase subunits ArrA/ArrB remain "
                    "to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "arsenate_respiration_trait",
                        "label": "arsenate respiration",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000195",
                        "description": "Anaerobic respiration using arsenate As(V) as a terminal electron acceptor.",
                    },
                    {
                        "node_id": "arsenate_respiration_arsenate",
                        "label": "arsenate",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:18231",
                        "description": "Arsenate As(V) oxyanion serving as the terminal respiratory electron acceptor.",
                    },
                    {
                        "node_id": "arsenate_respiration_reductase_activity",
                        "label": "arsenate reductase (donor) activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0030631",
                        "description": "Arsenate respiratory reductase (ARR) activity catalyzing respiratory As(V) reduction.",
                    },
                    {
                        "node_id": "arsenate_respiration_arsenite",
                        "label": "arsenite",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:29866",
                        "description": "Arsenite produced by respiratory reduction of arsenate As(V).",
                    },
                ],
                "edges": [
                    {
                        "subject": "arsenate_respiration_trait",
                        "predicate": "has electron acceptor",
                        "predicate_id": "METPO:2007702",
                        "object": "arsenate_respiration_arsenate",
                        "description": "Arsenate As(V) serves as a terminal electron acceptor in microbial anaerobic respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Saltikov and Newman state that arsenate can be used by microorganisms as a terminal electron acceptor in anaerobic respiration.",
                            )
                        ],
                    },
                    {
                        "subject": "arsenate_respiration_reductase_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "arsenate_respiration_arsenite",
                        "description": "Respiratory arsenate reduction couples electron donor oxidation with reduction of As(V) to arsenite.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Saltikov et al. show that Shewanella sp. strain ANA-3 couples lactate oxidation with the reduction of As(V) to arsenite.",
                            )
                        ],
                    },
                    {
                        "subject": "arsenate_respiration_reductase_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "arsenate_respiration_trait",
                        "description": "Arsenate respiratory reductase (ARR) is the key enzyme conferring arsenate respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Malasarn et al. characterize arsenate respiratory reductase (ARR) as the key enzyme involved in Shewanella sp. strain ANA-3 arsenate respiration.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/metabolism/fumarate_respiration.yaml":
        return [
            {
                "graph_id": "fumarate_respiration_frd_pathway_sketch",
                "title": "NADH dehydrogenase to fumarate reductase anaerobic respiratory chain",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking NADH "
                    "dehydrogenase activity, fumarate reductase (FRD) catalysis, "
                    "and succinate production to fumarate respiration."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway-and-activity sketch backed by DOI:10.1128/mBio.03238-19 "
                    "and DOI:10.1128/JB.00389-22; strain-matched UniProtKB protein "
                    "examples for Bacteroides fragilis fumarate reductase subunits "
                    "(FrdCAB) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "fumarate_respiration_trait",
                        "label": "fumarate respiration",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000196",
                        "description": "Anaerobic respiration using fumarate as a terminal electron acceptor.",
                    },
                    {
                        "node_id": "fumarate_respiration_frd_activity",
                        "label": "succinate dehydrogenase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0000104",
                        "description": "Fumarate reductase (FRD) catalytic activity transferring electrons from reduced quinone to fumarate under anaerobic and nanaerobic conditions.",
                    },
                    {
                        "node_id": "fumarate_respiration_succinate",
                        "label": "succinate",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:30031",
                        "description": "Succinate produced by fumarate reductase reduction of fumarate.",
                    },
                    {
                        "node_id": "fumarate_respiration_nadh_dehydrogenase_activity",
                        "label": "NADH dehydrogenase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0003954",
                        "description": "NADH dehydrogenase activity initiating electron transfer in the NADH-to-fumarate anaerobic respiratory chain.",
                    },
                ],
                "edges": [
                    {
                        "subject": "fumarate_respiration_frd_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "fumarate_respiration_succinate",
                        "description": "Fumarate reductase transfers electrons from reduced quinone to fumarate and produces succinate.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Ito et al. state that under anaerobic conditions fumarate serves as a terminal electron acceptor with fumarate reductase (FRD) transferring electrons from reduced quinone and producing succinate.",
                            )
                        ],
                    },
                    {
                        "subject": "fumarate_respiration_nadh_dehydrogenase_activity",
                        "predicate": "causally upstream of",
                        "predicate_id": "RO:0002411",
                        "object": "fumarate_respiration_frd_activity",
                        "description": "NADH dehydrogenases supply electrons in the NADH-to-fumarate anaerobic respiratory chain.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Butler et al. show that the anaerobic respiratory chain from NADH to fumarate involves two NADH dehydrogenases.",
                            )
                        ],
                    },
                    {
                        "subject": "fumarate_respiration_frd_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "fumarate_respiration_trait",
                        "description": "Synthesis and catalytic activity of fumarate reductase under anaerobic and nanaerobic conditions confers fumarate respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Butler et al. show that fumarate reductase is synthesized and active under anaerobic and nanaerobic respiratory conditions.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/metabolism/perchlorate_respiration.yaml":
        return [
            {
                "graph_id": "perchlorate_respiration_reduction_sketch",
                "title": "Anaerobic respiratory perchlorate reduction to chloride",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking anaerobic "
                    "respiratory perchlorate reduction and chloride formation to "
                    "perchlorate respiration."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway sketch backed by Melnyk et al. (DOI:10.1186/s12864-015-2011-5 "
                    "and DOI:10.1128/AEM.05758-11); canonical_examples and strain-matched "
                    "UniProtKB protein examples for perchlorate reductase (PcrABCD) and "
                    "chlorite dismutase (Cld) (e.g., in candidate exemplar Dechloromonas "
                    "aromatica RCB) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "perchlorate_respiration_trait",
                        "label": "perchlorate respiration",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000197",
                        "description": "Anaerobic respiration using perchlorate as a terminal electron acceptor.",
                    },
                    {
                        "node_id": "perchlorate_respiration_perchlorate_reduction",
                        "label": "anaerobic respiration",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0019645",
                        "description": "Anaerobic respiratory reduction of perchlorate by perchlorate reductase (PcrABCD) and chlorite dismutase (Cld).",
                    },
                    {
                        "node_id": "perchlorate_respiration_chloride",
                        "label": "chloride",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:17996",
                        "description": "Chloride anion produced as the terminal product of respiratory perchlorate reduction and chlorite dismutation.",
                    },
                ],
                "edges": [
                    {
                        "subject": "perchlorate_respiration_perchlorate_reduction",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "perchlorate_respiration_trait",
                        "description": "Perchlorate reductase and chlorite dismutase encoded by pcrABCD and cld confer perchlorate respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Melnyk et al. identify perchlorate reductase and chlorite dismutase, encoded by the pcrABCD and cld genes, as the core enzymes of perchlorate respiration.",
                            )
                        ],
                    },
                    {
                        "subject": "perchlorate_respiration_perchlorate_reduction",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "perchlorate_respiration_chloride",
                        "description": "Periplasmic reduction of perchlorate to chlorite followed by chlorite dismutation yields chloride and molecular oxygen.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Melnyk et al. describe periplasmic reduction of perchlorate to chlorite by perchlorate reductase followed by dismutation of chlorite to chloride and molecular oxygen.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/metabolism/chlorate_respiration.yaml":
        return [
            {
                "graph_id": "chlorate_respiration_pathway_sketch",
                "title": "Two-step dissimilatory chlorate reduction pathway via chlorite",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking chlorate "
                    "terminal electron acceptance and two-step dissimilatory "
                    "chlorate reduction via chlorite to chlorate respiration."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway sketch backed by DOI:10.1128/AEM.69.9.5585-5592.2003 "
                    "and DOI:10.1128/AEM.07303-11; strain-matched UniProtKB protein "
                    "examples for Ideonella dechloratans chlorate reductase (ClrABC) "
                    "and chlorite dismutase (Cld) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "chlorate_respiration_trait",
                        "label": "chlorate respiration",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000198",
                        "description": "Anaerobic respiration using chlorate as a terminal electron acceptor.",
                    },
                    {
                        "node_id": "chlorate_respiration_chlorate",
                        "label": "chlorate",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:17891",
                        "description": "Chlorate oxyanion serving as the terminal electron acceptor.",
                    },
                    {
                        "node_id": "chlorate_respiration_dissimilatory_pathway",
                        "label": "anaerobic respiration",
                        "node_type": "PATHWAY",
                        "grounding": "GO:0019645",
                        "description": "Two-step dissimilatory chlorate reduction respiratory pathway consisting of chlorate reduction followed by chlorite decomposition.",
                    },
                    {
                        "node_id": "chlorate_respiration_chlorite",
                        "label": "chlorite",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:17444",
                        "description": "Chlorite intermediate produced by chlorate reduction and decomposed in the second step of the chlorate respiration pathway.",
                    },
                ],
                "edges": [
                    {
                        "subject": "chlorate_respiration_trait",
                        "predicate": "has electron acceptor",
                        "predicate_id": "METPO:2007702",
                        "object": "chlorate_respiration_chlorate",
                        "description": "Chlorate ion serves as the sole electron acceptor for oxidation of organic matter in chlorate respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Danielsson Thorell et al. show that chlorate ion serves as the sole electron acceptor for oxidation of organic matter in anaerobic respiration.",
                            )
                        ],
                    },
                    {
                        "subject": "chlorate_respiration_dissimilatory_pathway",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "chlorate_respiration_trait",
                        "description": "Chlorate-respiring bacteria use dissimilatory chlorate reduction as an anaerobic respiratory pathway.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Hellberg Lindqvist et al. characterize chlorate-respiring bacteria (CRB) that use chlorate as a terminal electron acceptor.",
                            )
                        ],
                    },
                    {
                        "subject": "chlorate_respiration_dissimilatory_pathway",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "chlorate_respiration_chlorite",
                        "description": "Reduction of chlorate occurs in a two-step reaction producing chlorite followed by chlorite decomposition.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Danielsson Thorell et al. report that reduction of chlorate occurs in a two-step reaction: chlorate reduction followed by chlorite decomposition.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/metabolism/trimethylamine_n_oxide_respiration.yaml":
        return [
            {
                "graph_id": "tmao_respiration_tor_pathway_sketch",
                "title": "torCAD-encoded TMAO reductase anaerobic respiratory pathway",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking TMAO "
                    "terminal electron acceptance, torCAD-encoded TMAO reductase "
                    "catalysis, and trimethylamine formation to TMAO respiration."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway-and-activity sketch backed by DOI:10.1111/1462-2920.12726 "
                    "and DOI:10.3389/fmicb.2024.1467153; strain-matched UniProtKB "
                    "protein examples for Escherichia coli K-12 TMAO reductase "
                    "TorA/TorC encoded by the torCAD operon remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "tmao_respiration_trait",
                        "label": "trimethylamine N-oxide respiration",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000199",
                        "description": "Anaerobic respiration using trimethylamine N-oxide (TMAO) as a terminal electron acceptor.",
                    },
                    {
                        "node_id": "tmao_respiration_tmao",
                        "label": "trimethylamine N-oxide",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:15724",
                        "description": "Trimethylamine N-oxide (TMAO) serving as the terminal electron acceptor in anaerobic respiratory growth.",
                    },
                    {
                        "node_id": "tmao_respiration_reductase_activity",
                        "label": "trimethylamine-N-oxide reductase (cytochrome c) activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0008810",
                        "description": "Respiratory TMAO reductase activity encoded by the torCAD operon reducing TMAO to trimethylamine.",
                    },
                    {
                        "node_id": "tmao_respiration_trimethylamine",
                        "label": "trimethylamine",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:18139",
                        "description": "Trimethylamine (TMA) produced by respiratory reduction of TMAO.",
                    },
                ],
                "edges": [
                    {
                        "subject": "tmao_respiration_trait",
                        "predicate": "has electron acceptor",
                        "predicate_id": "METPO:2007702",
                        "object": "tmao_respiration_tmao",
                        "description": "Trimethylamine N-oxide (TMAO) serves as the terminal electron acceptor in anaerobic respiratory growth.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Denby et al. describe anaerobic respiratory growth with trimethylamine-N-oxide (TMAO) as the terminal electron acceptor.",
                            )
                        ],
                    },
                    {
                        "subject": "tmao_respiration_reductase_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "tmao_respiration_trimethylamine",
                        "description": "TMAO reductase encoded by the torCAD operon reduces TMAO to trimethylamine (TMA).",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Denby et al. state that TMAO is reduced to TMA by the enzyme TMAO reductase, encoded by the torCAD operon.",
                            )
                        ],
                    },
                    {
                        "subject": "tmao_respiration_reductase_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "tmao_respiration_trait",
                        "description": "Respiratory TMAO reduction confers the trimethylamine N-oxide respiration energy-metabolism mode.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Qiu and Tang describe switching from aerobic intracellular energy metabolism to trimethylamine N-oxide respiration.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/metabolism/tetrathionate_respiration.yaml":
        return [
            {
                "graph_id": "tetrathionate_respiration_ttr_pathway_sketch",
                "title": "Tetrathionate reductase catalysis and anaerobic reduction to thiosulfate",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking tetrathionate "
                    "terminal electron acceptance, TtrABC tetrathionate reductase "
                    "activity, and thiosulfate production to tetrathionate respiration."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway-and-activity sketch backed by DOI:10.1046/j.1365-2958.1999.01345.x "
                    "and DOI:10.1128/JB.183.8.2463-2475.2001; strain-matched UniProtKB "
                    "protein examples for Salmonella enterica serovar Typhimurium LT2 "
                    "tetrathionate reductase subunits TtrA/TtrB/TtrC remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "tetrathionate_respiration_trait",
                        "label": "tetrathionate respiration",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000200",
                        "description": "Anaerobic respiration using tetrathionate as a terminal electron acceptor.",
                    },
                    {
                        "node_id": "tetrathionate_respiration_tetrathionate",
                        "label": "tetrathionate",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:29892",
                        "description": "Tetrathionate oxyanion serving as the terminal respiratory electron acceptor.",
                    },
                    {
                        "node_id": "tetrathionate_respiration_ttr_activity",
                        "label": "tetrathionate reductase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0018523",
                        "description": "Respiratory tetrathionate reductase catalytic activity encoded by ttrA, ttrB, and ttrC.",
                    },
                    {
                        "node_id": "tetrathionate_respiration_thiosulfate",
                        "label": "thiosulfate",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:26977",
                        "description": "Thiosulfate produced by respiratory reduction of tetrathionate.",
                    },
                ],
                "edges": [
                    {
                        "subject": "tetrathionate_respiration_trait",
                        "predicate": "has electron acceptor",
                        "predicate_id": "METPO:2007702",
                        "object": "tetrathionate_respiration_tetrathionate",
                        "description": "Tetrathionate serves as the terminal respiratory electron acceptor.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Hensel et al. state that bacteria use tetrathionate as a terminal respiratory electron acceptor.",
                            )
                        ],
                    },
                    {
                        "subject": "tetrathionate_respiration_ttr_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "tetrathionate_respiration_trait",
                        "description": "Tetrathionate reductase encoded by ttrA, ttrB, and ttrC confers tetrathionate respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Hensel et al. identify ttrA, ttrB, and ttrC as the tetrathionate reductase structural genes.",
                            )
                        ],
                    },
                    {
                        "subject": "tetrathionate_respiration_ttr_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "tetrathionate_respiration_thiosulfate",
                        "description": "Respiratory reduction of tetrathionate produces thiosulfate.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Price-Carter et al. report that Salmonella reduces tetrathionate to thiosulfate.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/metabolism/dimethyl_sulfoxide_respiration.yaml":
        return [
            {
                "graph_id": "dmso_respiration_reductase_sketch",
                "title": "Membrane and extracellular DMSO reductase respiratory pathway",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking dimethyl "
                    "sulfoxide terminal electron acceptance and DMSO reductase "
                    "activity to dimethyl sulfoxide respiration."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway-and-activity sketch backed by DOI:10.1073/pnas.0505959103 "
                    "and DOI:10.1111/1462-2920.15971; strain-matched UniProtKB "
                    "protein examples for the Shewanella oneidensis MR-1 SO1427-SO1432 "
                    "(DmsEFABGH) extracellular DMSO reductase subunits remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "dmso_respiration_trait",
                        "label": "dimethyl sulfoxide respiration",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000201",
                        "description": "Anaerobic respiration using dimethyl sulfoxide (DMSO) as a terminal electron acceptor.",
                    },
                    {
                        "node_id": "dmso_respiration_dmso",
                        "label": "dimethyl sulfoxide",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:28262",
                        "description": "Dimethyl sulfoxide serving as a terminal respiratory electron acceptor.",
                    },
                    {
                        "node_id": "dmso_respiration_reductase_activity",
                        "label": "dimethyl-sulfoxide reductase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0009388",
                        "description": "Membrane-associated or cell-surface DMSO reductase activity catalyzing respiratory DMSO reduction.",
                    },
                    {
                        "node_id": "dmso_respiration_extracellular_process",
                        "label": "anaerobic respiration",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0019645",
                        "description": "Extracellular anaerobic respiratory process encoded by the SO1427-SO1432 gene cluster.",
                    },
                ],
                "edges": [
                    {
                        "subject": "dmso_respiration_trait",
                        "predicate": "has electron acceptor",
                        "predicate_id": "METPO:2007702",
                        "object": "dmso_respiration_dmso",
                        "description": "Dimethyl sulfoxide serves as a terminal electron acceptor in anaerobic respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Rosenbaum et al. demonstrate that Moorella thermoacetica uses dimethyl sulfoxide as a terminal electron acceptor.",
                            )
                        ],
                    },
                    {
                        "subject": "dmso_respiration_reductase_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "dmso_respiration_trait",
                        "description": "Membrane-associated DMSO reductase activity confers dimethyl sulfoxide respiration.",
                        "evidence": [
                            _ev_item(
                                doc,
                                3,
                                "Rosenbaum et al. demonstrate membrane-associated DMSO reductase activity during anaerobic growth on DMSO.",
                            )
                        ],
                    },
                    {
                        "subject": "dmso_respiration_extracellular_process",
                        "predicate": "contributes to",
                        "predicate_id": "RO:0002326",
                        "object": "dmso_respiration_trait",
                        "description": "The SO1427-SO1432 gene cluster mediates extracellular anaerobic respiration of DMSO.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Gralnick et al. show that the SO1427-SO1432 gene cluster is required for anaerobic respiration of DMSO in Shewanella oneidensis.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/arginine_dihydrolase_activity.yaml":
        return [
            {
                "graph_id": "arginine_dihydrolase_adi_pathway_sketch",
                "title": "Arginine deiminase (ADI) pathway conversion of L-arginine to citrulline and ornithine",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "arginine deiminase catalysis, L-citrulline and L-ornithine "
                    "formation, and ADI pathway ATP generation to arginine "
                    "dihydrolase activity."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway-and-activity sketch backed by EC 3.5.3.6, "
                    "DOI:10.1016/j.fm.2010.11.016, DOI:10.1128/aem.07724-11, and "
                    "DOI:10.1016/j.resmic.2012.11.004; strain-matched UniProtKB "
                    "protein examples for Latilactobacillus sakei arc operon enzymes "
                    "(ArcA, ArcB, ArcC) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "arginine_dihydrolase_activity_trait",
                        "label": "arginine dihydrolase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000164",
                        "description": "Physiological enzyme-activity phenotype mediated by the microbial arginine deiminase (ADI) pathway.",
                    },
                    {
                        "node_id": "arginine_dihydrolase_adi_pathway",
                        "label": "arginine catabolic process to ornithine",
                        "node_type": "PATHWAY",
                        "grounding": "GO:0019546",
                        "description": "Arginine deiminase (ADI) pathway encoded by the arc operon that converts arginine to citrulline and ornithine with ATP generation.",
                    },
                    {
                        "node_id": "arginine_dihydrolase_deiminase_activity",
                        "label": "arginine deiminase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0008792",
                        "description": "Catalytic hydrolysis of L-arginine and water to L-citrulline and ammonia (EC 3.5.3.6).",
                    },
                    {
                        "node_id": "arginine_dihydrolase_citrulline",
                        "label": "L-citrulline",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:16349",
                        "description": "L-citrulline intermediate produced from L-arginine by arginine deiminase.",
                    },
                ],
                "edges": [
                    {
                        "subject": "arginine_dihydrolase_adi_pathway",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "arginine_dihydrolase_activity_trait",
                        "description": "Arginine conversion through the arc-operon ADI pathway confers the arginine dihydrolase activity trait.",
                        "evidence": [
                            _ev_item(
                                doc,
                                3,
                                "Rimaux et al. describe arginine conversion through the arc-operon-encoded arginine deiminase (ADI) pathway as a common metabolic trait of Lactobacillus sakei.",
                            )
                        ],
                    },
                    {
                        "subject": "arginine_dihydrolase_deiminase_activity",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "arginine_dihydrolase_adi_pathway",
                        "description": "Arginine deiminase hydrolyzes L-arginine and water to L-citrulline and ammonia in the first step of the ADI pathway.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 3.5.3.6 defines the arginine deiminase reaction converting L-arginine and water to L-citrulline and ammonia.",
                            )
                        ],
                    },
                    {
                        "subject": "arginine_dihydrolase_adi_pathway",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "arginine_dihydrolase_citrulline",
                        "description": "Arginine conversion through the ADI pathway produces citrulline and ornithine.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Rimaux et al. show that arginine conversion through the ADI pathway produces both citrulline and ornithine.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/lysine_decarboxylase_activity.yaml":
        return [
            {
                "graph_id": "lysine_decarboxylase_cadba_sketch",
                "title": "Lysine decarboxylation to cadaverine and CadBA proton-consuming acid resistance",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking lysine "
                    "decarboxylase catalytic activity and cadaverine production to "
                    "the lysine decarboxylase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 4.1.1.18 and "
                    "DOI:10.1128/jb.01306-06; strain-matched UniProtKB protein "
                    "examples for Escherichia coli CadA inducible lysine decarboxylase "
                    "and CadB lysine-cadaverine antiporter remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "lysine_decarboxylase_activity_trait",
                        "label": "lysine decarboxylase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000153",
                        "description": "Physiological enzyme-activity phenotype in which L-lysine is decarboxylated to cadaverine and carbon dioxide.",
                    },
                    {
                        "node_id": "lysine_decarboxylase_catalytic_activity",
                        "label": "lysine decarboxylase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0008923",
                        "description": "Catalytic decarboxylation of L-lysine consuming a cytoplasmic proton and producing cadaverine and CO2 (EC 4.1.1.18).",
                    },
                    {
                        "node_id": "lysine_decarboxylase_cadaverine",
                        "label": "cadaverine",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:18127",
                        "description": "Diamine cadaverine produced by decarboxylation of L-lysine.",
                    },
                ],
                "edges": [
                    {
                        "subject": "lysine_decarboxylase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "lysine_decarboxylase_activity_trait",
                        "description": "Inducible CadBA lysine decarboxylase activity consumes a proton and produces cadaverine.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Moreau shows that inducible CadBA lysine-dependent acid resistance activity consumes one proton and produces the diamine cadaverine.",
                            )
                        ],
                    },
                    {
                        "subject": "lysine_decarboxylase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "lysine_decarboxylase_cadaverine",
                        "description": "Lysine decarboxylase converts L-lysine into cadaverine and CO2.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 4.1.1.18 defines the lysine decarboxylase reaction converting L-lysine into cadaverine and CO2.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/siderophore_production.yaml":
        return [
            {
                "graph_id": "siderophore_production_iron_scavenging_sketch",
                "title": "Siderophore biosynthesis, extracellular secretion, and iron scavenging",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "siderophore biosynthesis, extracellular siderophore secretion, "
                    "and high-affinity iron scavenging to siderophore production."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Biosynthesis-and-transport sketch backed by DOI:10.1111/1462-2920.14937, "
                    "DOI:10.15698/mic2018.10.649, and DOI:10.1073/pnas.0908760106; "
                    "strain-matched UniProtKB protein examples for Pseudomonas aeruginosa "
                    "pyoverdine synthetases (PvdL/PvdI/PvdJ/PvdD) and TonB-dependent "
                    "receptor FpvA remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "siderophore_production_trait",
                        "label": "siderophore production",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000186",
                        "description": "Physiological trait in which microorganisms synthesize and secrete iron-chelating siderophores.",
                    },
                    {
                        "node_id": "siderophore_production_biosynthesis",
                        "label": "siderophore biosynthetic process",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0019290",
                        "description": "Cellular biosynthesis of iron-chelating siderophore molecules such as pyoverdine under iron-limiting conditions.",
                    },
                    {
                        "node_id": "siderophore_production_siderophore",
                        "label": "siderophore",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:26672",
                        "description": "Secreted high-affinity iron-chelating molecule released into the extracellular environment.",
                    },
                    {
                        "node_id": "siderophore_production_iron_import",
                        "label": "siderophore transport",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0015891",
                        "description": "Extracellular scavenging and cellular uptake of siderophore-chelated iron.",
                    },
                ],
                "edges": [
                    {
                        "subject": "siderophore_production_biosynthesis",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "siderophore_production_trait",
                        "description": "Biosynthesis of iron-chelating siderophores such as pyoverdine under iron-limiting conditions confers the siderophore production trait.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Ringel and Bruser review fluorescent pyoverdine siderophores produced by pseudomonads for growth under iron-limiting conditions.",
                            )
                        ],
                    },
                    {
                        "subject": "siderophore_production_biosynthesis",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "siderophore_production_siderophore",
                        "description": "Bacteria synthesize iron-chelating siderophore molecules to access iron.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Schalk et al. define siderophores as iron-chelating molecules produced by bacteria to access iron.",
                            )
                        ],
                    },
                    {
                        "subject": "siderophore_production_siderophore",
                        "predicate": "enables",
                        "predicate_id": "RO:0002327",
                        "object": "siderophore_production_iron_import",
                        "description": "Secreted siderophores scavenge environmental iron and mediate its uptake into the cell.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Schalk et al. state that secreted siderophores scavenge environmental iron and bring it back into the cells.",
                            )
                        ],
                    },
                ],
            }
        ]

    raise KeyError(f"Unexpected Cohort C path: {rel_path}")


COHORT_D_GAPS: dict[str, tuple[str, str]] = {
    "data/traits/metabolism/acetoclastic_methanogenesis.yaml": (
        "Add primary literature evidence for acetate activation (AckA-Pta or Acs), acetyl-CoA decarbonylase/synthase (CdhCDE), and methyl-CoM reductase (McrABG) plus a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries two broad overview snippets (DOI:10.1007/s00253-023-12700-3, DOI:10.3389/fmicb.2017.01198) stating that acetoclastic methanogens split acetate to CH4 and CO2, without enzymatic step quotes or a cited canonical example.",
    ),
    "data/traits/metabolism/acetone_butanol_ethanol_fermentation.yaml": (
        "Add primary literature evidence for the acidogenic-to-solventogenic pathway enzymes (e.g. CoA-transferase CtfAB, acetoacetate decarboxylase Adc, and aldehyde/alcohol dehydrogenase AdhE) and strain-matched UniProtKB protein accessions before constructing causal_graphs.",
        "The current record carries one overview snippet on Clostridium acetobutylicum acid reassimilation (DOI:10.1073/pnas.1423143112) and one historical industrial fermentation snippet (DOI:10.1002/bit.22003), which cannot ground a multi-edge enzymatic mechanism graph without inventing unsupported edges.",
    ),
    "data/traits/metabolism/anaerobic_ammonium_oxidation.yaml": (
        "Add primary literature evidence for nitrite reduction to nitric oxide (NirS), hydrazine synthase (HzsABC), and hydrazine dehydrogenase (Hdh) plus a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries overall stoichiometry and substrate-affinity snippets (DOI:10.1038/22749, DOI:10.1128/AEM.65.7.3248-3250.1999, DOI:10.1038/nature10453) without intermediate hydrazine-pathway enzyme quotes or a cited canonical example.",
    ),
    "data/traits/metabolism/arsenite_oxidation.yaml": (
        "Add primary literature evidence for periplasmic arsenite oxidase (AioAB or ArxAB), electron transfer to c-type cytochrome/azurin, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries general detoxification/energy and strain-isolation snippets (DOI:10.3389/fmicb.2020.569282, DOI:10.1128/AEM.66.1.92-97.2000, DOI:10.1186/s12866-024-03676-9) without enzyme-level catalytic quotes or a cited canonical example.",
    ),
    "data/traits/metabolism/butyric_acid_fermentation.yaml": (
        "Add primary literature evidence for thiolase, 3-hydroxybutyryl-CoA dehydrogenase, crotonase, butyryl-CoA dehydrogenase/EtfAB, and phosphotransbutyrylase/butyrate kinase or butyryl-CoA:acetate CoA-transferase in Clostridium tyrobutyricum before constructing causal_graphs.",
        "The current record summarizes anaerobe energy-conservation history, gene-cluster arrangements, and strain yield (DOI:10.3389/fmicb.2021.703525, DOI:10.1111/j.1574-6968.2009.01514.x, DOI:10.1111/1751-7915.12304) without distinct step-by-step enzymatic reaction quotes.",
    ),
    "data/traits/metabolism/citrate_fermentation.yaml": (
        "Add primary literature evidence for citrate uptake (CitH/CitS), citrate lyase (CitDEF), and membrane-bound oxaloacetate decarboxylase Na+ pump (OadGAB) before constructing causal_graphs.",
        "The current record carries two growth-and-prevalence snippets in Klebsiella pneumoniae (DOI:10.1128/JB.183.18.5248-5256.2001, DOI:10.1186/1471-2180-9-168) without enzymatic step or intermediate quotes.",
    ),
    "data/traits/metabolism/complete_ammonia_oxidation.yaml": (
        "Add primary literature evidence for ammonia monooxygenase (AmoCAB), hydroxylamine dehydrogenase (Hao), and nitrite oxidoreductase (NxrAB) catalysis in comammox Nitrospira before constructing causal_graphs.",
        "The current record carries three discovery and ecological-dominance snippets on comammox Nitrospira (DOI:10.1038/nature16459, DOI:10.1038/nature16461, DOI:10.1128/aem.01698-23) without distinct intermediate nitrite-step or enzyme quotes.",
    ),
    "data/traits/metabolism/iodate_respiration.yaml": (
        "Add primary literature evidence for the periplasmic iodate reductase complex (IdrABP1P2) and electron-transport coupling plus strain-matched UniProtKB protein accessions before constructing causal_graphs.",
        "The current record carries growth and whole-cell IO3- to I- reduction snippets across three taxa (DOI:10.1128/AEM.00241-07, DOI:10.1038/s41396-021-01034-5, DOI:10.3389/fmicb.2021.804181) without enzyme-complex or electron-transfer quotes.",
    ),
    "data/traits/metabolism/lipolysis.yaml": (
        "Add primary literature evidence for extracellular triacylglycerol lipase secretion, fatty-acid/glycerol uptake, and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries two general definition snippets for microbial lipases EC 3.1.1.3 (DOI:10.1186/s12934-020-01428-8, DOI:10.1007/s00253-004-1568-8) without a cited canonical example or multi-step catabolic mechanism quotes.",
    ),
    "data/traits/metabolism/methyl_based_methanogenesis.yaml": (
        "Add primary literature evidence for substrate-specific methyltransferases (MtaABC/MtmBC/MtbA/MttBC), methyl-CoM reductase (McrABG), and a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries two pathway-classification snippets (DOI:10.1128/mmbr.00024-22, DOI:10.3389/fmicb.2017.01198) without enzymatic step quotes or a cited canonical example.",
    ),
    "data/traits/metabolism/nitrification.yaml": (
        "Add a second independent evidence snippet covering ammonia monooxygenase / hydroxylamine oxidoreductase and nitrite oxidoreductase steps plus a strain-matched canonical example before constructing causal_graphs.",
        "The current record carries a single overview snippet (DOI:10.3389/fmicb.2020.01900) describing two-step oxidation of ammonia to nitrite and nitrate; a connected multi-edge graph requires at least two independent verbatim snippets without clause-splitting.",
    ),
    "data/traits/metabolism/organohalide_respiration.yaml": (
        "Add primary literature evidence for corrinoid-dependent reductive dehalogenase catalysis (e.g. PceA, TceA, RdhA) and menaquinone/hydrogenase electron transport before constructing causal_graphs.",
        "The current record carries definition, phylogenetic-distribution, and mixed-culture cofactor snippets (DOI:10.1098/rstb.2012.0322, DOI:10.1126/science.276.5318.1568) without reductive dehalogenase enzyme or dechlorination-product quotes.",
    ),
    "data/traits/metabolism/selenate_respiration.yaml": (
        "Add primary literature evidence for periplasmic respiratory selenate reductase (SerABC or SrdBCA) and selenate-to-selenite reduction stoichiometry before constructing causal_graphs.",
        "The current record carries strain-isolation and terminal-electron-acceptor snippets (DOI:10.1128/aem.60.8.3011-3019.1994, DOI:10.1128/AEM.02737-06, DOI:10.1016/j.syapm.2005.12.011) without enzymatic reductase or selenite-product quotes.",
    ),
    "data/traits/morphology/akinete.yaml": (
        "Add primary literature evidence for cyanobacterial akinete differentiation regulators (e.g. AvaK, HepA) and envelope glycolipid/polysaccharide biosynthesis before constructing causal_graphs.",
        "The current record carries morphological and ecological-survival snippets in Nostocales (DOI:10.1159/000517443, DOI:10.3389/fmicb.2025.1677844) without developmental gene or biosynthetic pathway quotes.",
    ),
    "data/traits/morphology/holdfast.yaml": (
        "Add primary literature evidence for holdfast polysaccharide biosynthesis/export proteins (HfsDABCHG) and outer-membrane anchoring proteins (HfaABD) before constructing causal_graphs.",
        "The current record carries polar adhesin function and monosaccharide-composition snippets in Caulobacterales (DOI:10.1128/jb.00276-19, DOI:10.1128/jb.00273-22) without biosynthetic or anchoring protein quotes.",
    ),
    "data/traits/physiology/acid_phosphatase_activity.yaml": (
        "Add primary microbial literature evidence for secreted or periplasmic acid phosphatase catalysis (EC 3.1.3.2, e.g. SapM, AphA, PhoN) and substrate dephosphorylation products before constructing causal_graphs.",
        "The current record carries one culture-filtrate detection snippet and one API ZYM profile snippet (DOI:10.1128/JB.182.23.6850-6853.2000, DOI:10.1155/2021/8888641) without distinct catalytic substrate/product quotes for a multi-edge graph.",
    ),
    "data/traits/physiology/alanine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for alanine aminopeptidase/arylamidase catalysis and physiological peptide cleavage in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.4.11.2 reaction snippet with a multi-enzyme API ZYM species-description list (DOI:10.1099/ijsem.0.006017), leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/alkaline_phosphatase_activity.yaml": (
        "Add primary microbial literature evidence for PhoA/PhoX alkaline phosphatase catalysis (EC 3.1.3.1), phosphate-ester hydrolysis products, and PhoBR regulation before constructing causal_graphs.",
        "The current record carries one constitutive-expression snippet and one API ZYM profile list (DOI:10.1128/JB.185.16.4983-4991.2003, DOI:10.1155/2021/8888641) without distinct catalytic reaction/product quotes for a multi-edge graph.",
    ),
    "data/traits/physiology/alpha_chymotrypsin_activity.yaml": (
        "Add primary microbial literature evidence for bacterial chymotrypsin-like serine endopeptidase catalysis and substrate cleavage before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.4.21.1 cleavage-specificity snippet with a multi-enzyme API ZYM species-description list (DOI:10.1099/ijsem.0.006017), leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/alpha_galactosidase_activity.yaml": (
        "Add primary microbial literature evidence for MelA/Aga alpha-galactosidase catalysis and melibiose/raffinose catabolism in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one EC 3.2.1.22 catalytic definition snippet (DOI:10.3109/07388551.2013.794124) with a diagnostic assay-panel list (DOI:10.1128/jcm.22.3.333-335.1985), leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/alpha_glucosidase_activity.yaml": (
        "Add primary microbial literature evidence for alpha-glucosidase (EC 3.2.1.20) catalysis of terminal alpha-D-glucosidic linkages and maltose/oligosaccharide utilization before constructing causal_graphs.",
        "The current record carries two API ZYM enzyme-panel survey snippets (DOI:10.1371/journal.pone.0322500, DOI:10.3390/microorganisms13092005) without verbatim catalytic reaction or pathway quotes.",
    ),
    "data/traits/physiology/alpha_mannosidase_activity.yaml": (
        "Add primary microbial literature evidence for GH38/GH92 alpha-mannosidase catalysis and mannoside utilization in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.2.1.24 reaction snippet with a diagnostic strain-discrimination snippet (DOI:10.1128/jcm.32.3.854-855.1994), leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/arginine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for aminopeptidase B (EC 3.4.11.6) catalysis and physiological peptide cleavage in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.4.11.6 reaction snippet with two multi-enzyme diagnostic profile lists (DOI:10.3389/fgene.2023.1240581, DOI:10.1099/ijsem.0.006017), leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/beta_glucosidase_activity.yaml": (
        "Add primary microbial literature evidence for BglA/BglX beta-glucosidase cellobiose/beta-D-glucoside hydrolysis and glucose release before constructing causal_graphs.",
        "The current record pairs one EC 3.2.1.21 definition snippet (DOI:10.1007/s13205-015-0328-z) with two API ZYM diagnostic survey snippets (DOI:10.2323/jgam.60.59, DOI:10.3390/microorganisms12040776), leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/carboxylesterase_activity.yaml": (
        "Add primary microbial literature evidence for microbial carboxylesterase (EC 3.1.1.1) substrate hydrolysis and alcohol/carboxylate release in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.1.1.1 reaction snippet with a diagnostic strain-characterization snippet, leaving only one catalytic reaction quote.",
    ),
    "data/traits/physiology/caseinase_activity.yaml": (
        "Add primary microbial literature evidence for secreted extracellular caseinolytic protease identification, peptide release, and strain-matched UniProtKB protein accessions before constructing causal_graphs.",
        "The current record carries two general casein-hydrolysis screening snippets (DOI:10.3389/fmicb.2018.01148, DOI:10.2174/1874285801408010025) without specific protease gene/enzyme or multi-step mechanism quotes.",
    ),
    "data/traits/physiology/cystine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for cystinyl aminopeptidase/arylamidase (EC 3.4.11.3) catalysis in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.4.11.3 reaction snippet with two multi-enzyme API ZYM diagnostic lists, leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/dnase_activity.yaml": (
        "Add primary microbial literature evidence for secreted extracellular deoxyribonuclease (e.g. Nuc, EndA) phosphodiester cleavage and oligonucleotide products before constructing causal_graphs.",
        "The current record carries two general DNase agar-screening snippets (DOI:10.3389/fmicb.2019.00969, DOI:10.22207/JPAM.14.1.44) without specific nuclease enzyme or catalytic product quotes.",
    ),
    "data/traits/physiology/gamma_glutamyltransferase_activity.yaml": (
        "Add primary microbial literature evidence for Ggt gamma-glutamyltransferase glutathione cleavage and gamma-glutamyl amino-acid transfer in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.4.19.13 reaction snippet with two diagnostic strain-phenotyping snippets (DOI:10.3389/fgene.2023.1240581), leaving only one catalytic reaction quote.",
    ),
    "data/traits/physiology/gelatinase_activity.yaml": (
        "Add primary microbial literature evidence for secreted GelE/metalloprotease gelatin cleavage, peptide products, and quorum-sensing regulation before constructing causal_graphs.",
        "The current record carries two diagnostic gelatin-liquefaction assay snippets without specific protease identity or multi-step catalytic quotes.",
    ),
    "data/traits/physiology/glutamyl_glutamic_acid_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for glutamyl aminopeptidase (EC 3.4.11.7) catalysis and N-terminal dicarboxylic amino-acid cleavage before constructing causal_graphs.",
        "The current record carries two diagnostic enzyme-panel survey snippets (DOI:10.1099/ijsem.0.006017, DOI:10.1099/ijs.0.63642-0) without verbatim catalytic reaction or enzyme-mechanism quotes.",
    ),
    "data/traits/physiology/glycine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for glycyl aminopeptidase/arylamidase catalysis and substrate cleavage before constructing causal_graphs.",
        "The current record carries diagnostic enzyme-panel survey snippets without verbatim catalytic reaction or multi-step mechanism quotes.",
    ),
    "data/traits/physiology/histidine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for histidyl aminopeptidase/arylamidase catalysis and substrate cleavage before constructing causal_graphs.",
        "The current record carries diagnostic enzyme-panel survey snippets without verbatim catalytic reaction or multi-step mechanism quotes.",
    ),
    "data/traits/physiology/lecithinase_activity.yaml": (
        "Add primary microbial literature evidence for phospholipase C (Plc, EC 3.1.4.3) phosphatidylcholine cleavage to 1,2-diacylglycerol and phosphocholine before constructing causal_graphs.",
        "The current record carries two egg-yolk/lecithinase diagnostic assay snippets (DOI:10.2147/IDR.S365254, DOI:10.1128/jb.81.6.939-945.1961) without distinct phospholipid cleavage product quotes.",
    ),
    "data/traits/physiology/leucine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for leucyl aminopeptidase (PepA/Lap, EC 3.4.11.1) catalysis and peptide turnover in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.4.11.1 reaction snippet with a diagnostic API ZYM panel snippet, leaving only one catalytic reaction quote.",
    ),
    "data/traits/physiology/leucyl_glycine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for aminopeptidase cleavage of leucyl-glycine arylamide substrates and enzyme identity before constructing causal_graphs.",
        "The current record carries two diagnostic API rapid ID32A / species-description snippets (DOI:10.1099/ijsem.0.006017, DOI:10.1128/JCM.40.9.3427-3431.2002) without verbatim catalytic reaction quotes.",
    ),
    "data/traits/physiology/lipase_activity.yaml": (
        "Add primary microbial literature evidence for extracellular triacylglycerol lipase (EC 3.1.1.3) ester hydrolysis to diacylglycerol/fatty acids and enzyme identity before constructing causal_graphs.",
        "The current record carries two tributyrin/screening assay snippets (DOI:10.22207/JPAM.16.4.27, DOI:10.1016/j.mex.2018.01.004) without verbatim catalytic reaction or enzyme-mechanism quotes.",
    ),
    "data/traits/physiology/naphthol_as_bi_phosphohydrolase_activity.yaml": (
        "Add primary microbial literature evidence for the phosphohydrolase enzyme catalyzing naphthol-AS-BI-phosphate hydrolysis and its physiological substrate before constructing causal_graphs.",
        "The current record carries two API ZYM diagnostic substrate/panel snippets (DOI:10.14202/vetworld.2024.143-149, DOI:10.1128/JCM.43.8.3713-3717.2005) without catalytic product or enzyme-identity quotes.",
    ),
    "data/traits/physiology/phenylalanine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for phenylalanyl aminopeptidase/arylamidase catalysis and substrate cleavage before constructing causal_graphs.",
        "The current record carries two diagnostic enzyme-panel survey snippets (DOI:10.1099/ijsem.0.006017, DOI:10.1128/JCM.40.9.3427-3431.2002) without verbatim catalytic reaction quotes.",
    ),
    "data/traits/physiology/pyrrolidonyl_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for pyroglutamyl-peptidase I (PyrA, EC 3.4.19.3) catalysis and physiological peptide turnover in the exemplar taxon before constructing causal_graphs.",
        "The current record pairs one IUBMB EC 3.4.19.3 reaction snippet with a diagnostic strain-phenotyping list (DOI:10.1128/JCM.37.11.3443-3447.1999), leaving only one mechanistic quote.",
    ),
    "data/traits/physiology/serine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for seryl aminopeptidase/arylamidase catalysis and substrate cleavage before constructing causal_graphs.",
        "The current record carries two diagnostic enzyme-panel survey snippets (DOI:10.1099/ijsem.0.006017, DOI:10.1128/JCM.40.9.3427-3431.2002) without verbatim catalytic reaction quotes.",
    ),
    "data/traits/physiology/trypsin_activity.yaml": (
        "Add primary microbial literature evidence for microbial trypsin-like serine protease catalysis and physiological substrate cleavage before constructing causal_graphs.",
        "The current record pairs IUBMB EC 3.4.21.4 cleavage/vertebrate-pancreas snippets with an API ZYM diagnostic survey list (DOI:10.1371/journal.pone.0322500), lacking a second microbial mechanistic quote.",
    ),
    "data/traits/physiology/tyrosine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for tyrosyl aminopeptidase/arylamidase catalysis and substrate cleavage before constructing causal_graphs.",
        "The current record carries two diagnostic enzyme-panel survey snippets (DOI:10.1099/ijsem.0.006017, DOI:10.1128/JCM.40.9.3427-3431.2002) without verbatim catalytic reaction quotes.",
    ),
    "data/traits/physiology/valine_arylamidase_activity.yaml": (
        "Add primary microbial literature evidence for valyl aminopeptidase/arylamidase catalysis and substrate cleavage before constructing causal_graphs.",
        "The current record carries two API ZYM diagnostic survey snippets (DOI:10.3389/fmicb.2022.1034816, DOI:10.1099/ijsem.0.002327) without verbatim catalytic reaction quotes.",
    ),
}


def _verify_graph_invariants(
    rel_path: str, doc: dict[str, Any], graphs: list[dict[str, Any]]
) -> None:
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
            n for n in nodes if n.get("node_type") == "TRAIT" and n.get("grounding") == trait_id
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
            raise ValueError(
                f"{rel_path}: disconnected graph ({len(visited)}/{len(node_ids)} reached)"
            )

        if graph.get("scope_status") == "MECHANISTIC":
            protein_nodes_with_examples = [
                n
                for n in nodes
                if n.get("node_type") == "GENE_OR_PROTEIN" and (n.get("protein_examples") or [])
            ]
            if not protein_nodes_with_examples:
                raise ValueError(
                    f"{rel_path}: MECHANISTIC graph must have >=1 GENE_OR_PROTEIN node with protein_examples"
                )
            if not (doc.get("canonical_examples") or []):
                raise ValueError(
                    f"{rel_path}: MECHANISTIC graph requires cited canonical_examples on record"
                )


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


def build_cohort_c_discussion(rel_path: str, doc: dict[str, Any], graph_id: str) -> dict[str, Any]:
    """Construct the CURATION_TODO DiscussionItem for a Cohort C record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale, ev_index = COHORT_C_PROTEIN_GAPS[rel_path]
    ev_list = doc.get("evidence") or []
    supporting_ev: list[dict[str, str]] = []
    if len(ev_list) > ev_index and isinstance(ev_list[ev_index], dict):
        src = ev_list[ev_index]
        ref = str(src.get("reference") or "").strip()
        snip = str(src.get("snippet") or "").strip()
        if ref and snip:
            supporting_ev.append(
                {
                    "reference": ref,
                    "supports": "PARTIAL",
                    "snippet": snip,
                    "explanation": (
                        "Existing record-level evidence supports the connected "
                        "NONMECHANISTIC pathway/function graph but does not provide "
                        "strain-matched UniProtKB protein accessions for protein_examples."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-protein-example-gap",
        "prompt": prompt,
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "attaches_to": [f"causal_graphs#{graph_id}"],
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE_C2,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


def build_cohort_d_discussion(rel_path: str, doc: dict[str, Any]) -> dict[str, Any]:
    """Construct the KNOWLEDGE_GAP DiscussionItem for a Cohort D record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale = COHORT_D_GAPS[rel_path]
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
                        "Existing record-level evidence supports the trait definition "
                        "and diagnostic or organismal occurrence, but lacks multiple "
                        "distinct pathway/enzyme quotes and strain-matched UniProtKB "
                        "protein accessions needed for a connected causal graph."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-causal-graph-source-gap",
        "prompt": prompt,
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "attaches_to": ["causal_graphs"],
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE_C2,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


COHORT_E_PATHS: tuple[str, ...] = (
    "data/traits/other/coagulase_positive.yaml",
    "data/traits/other/indole_test_positive.yaml",
    "data/traits/physiology/pyrazinamidase_activity.yaml",
)

COHORT_E_PROTEIN_GAPS: dict[str, tuple[str, str, int]] = {
    "data/traits/other/coagulase_positive.yaml": (
        "Add strain-matched UniProtKB protein_examples for Staphylococcus aureus secreted coagulase (Coa, UniProtKB:P07767) so coagulase_positive_prothrombin_clotting_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1099/mic.0.000019, DOI:10.1371/journal.ppat.1001036) establishes prothrombin activation by secreted coagulase (Coa) and plasma clotting in Staphylococcus aureus (NCBITaxon:1280), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/other/indole_test_positive.yaml": (
        "Add strain-matched UniProtKB protein_examples for Escherichia coli tryptophanase (TnaA) so indole_test_positive_tryptophan_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1128/AEM.02787-15) establishes L-tryptophan degradation to indole in enterotoxigenic Escherichia coli strain H10407 (NCBITaxon:316401), but a verified UniProtKB accession for tryptophanase (TnaA) on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/physiology/pyrazinamidase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Mycobacterium tuberculosis nicotinamidase/pyrazinamidase PncA (UniProtKB:I6Y493) so pyrazinamidase_activity_pnca_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 3.5.1.19, DOI:10.1111/j.1742-4658.2007.06241.x, DOI:10.1371/journal.pone.0015785) establishes nicotinamide hydrolysis to nicotinate and pyrazinamide activation to pyrazinoic acid by PncA in Mycobacterium tuberculosis (NCBITaxon:1773), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
}


def build_cohort_e_graphs(rel_path: str, doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Construct the connected NONMECHANISTIC causal_graphs list for a Cohort E record."""
    if rel_path == "data/traits/other/coagulase_positive.yaml":
        return [
            {
                "graph_id": "coagulase_positive_prothrombin_clotting_sketch",
                "title": "Coagulase-mediated prothrombin activation and plasma clotting",
                "description": (
                    "Evidence-backed mechanism sketch linking bacterial prothrombin "
                    "activation and plasma clotting to the coagulase positive "
                    "test-outcome phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Biological-process sketch backed by DOI:10.1099/mic.0.000019 "
                    "and DOI:10.1371/journal.ppat.1001036; strain-matched UniProtKB "
                    "protein examples for secreted Staphylococcus aureus coagulase "
                    "(Coa, UniProtKB:P07767) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "coagulase_positive_trait",
                        "label": "coagulase positive",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1007090",
                        "description": "Test-outcome phenotype in which bacterial coagulase activity promotes clotting of plasma.",
                    },
                    {
                        "node_id": "coagulase_positive_prothrombin_activation",
                        "label": "zymogen activation",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0031638",
                        "description": "Binding and activation of host prothrombin by secreted staphylococcal coagulase (Coa).",
                    },
                    {
                        "node_id": "coagulase_positive_blood_coagulation",
                        "label": "blood coagulation",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0007596",
                        "description": "Coagulase-dependent clotting of blood plasma detected by the coagulase test.",
                    },
                ],
                "edges": [
                    {
                        "subject": "coagulase_positive_prothrombin_activation",
                        "predicate": "causally upstream of",
                        "predicate_id": "RO:0002411",
                        "object": "coagulase_positive_blood_coagulation",
                        "description": "Secreted Staphylococcus aureus coagulase (Coa) binds to and activates prothrombin to initiate plasma clotting.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Cheng et al. show that clinical isolates of Staphylococcus aureus secrete coagulase (Coa), a polypeptide that binds to and activates prothrombin.",
                            )
                        ],
                    },
                    {
                        "subject": "coagulase_positive_blood_coagulation",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "coagulase_positive_trait",
                        "description": "Coagulase-dependent clotting of plasma confers the coagulase positive test-outcome phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Loof et al. show that coagulase-positive Staphylococcus aureus bacteria promote clotting of plasma, which is abolished in a coagulase-deficient mutant strain.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/other/indole_test_positive.yaml":
        return [
            {
                "graph_id": "indole_test_positive_tryptophan_sketch",
                "title": "Bacterial L-tryptophan catabolism to indole",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking bacterial "
                    "tryptophan catabolism and indole formation to the indole test "
                    "positive phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Pathway-and-metabolite sketch backed by DOI:10.1128/AEM.02787-15; "
                    "strain-matched UniProtKB protein examples for Escherichia coli "
                    "tryptophanase (TnaA) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "indole_test_positive_trait",
                        "label": "indole test positive",
                        "node_type": "TRAIT",
                        "grounding": "METPO:1005011",
                        "description": "Test-outcome phenotype in which an organism degrades tryptophan to produce indole.",
                    },
                    {
                        "node_id": "indole_test_positive_tryptophan_catabolism",
                        "label": "L-tryptophan catabolic process",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0006569",
                        "description": "Bacterial catabolic degradation of L-tryptophan yielding extracellular indole.",
                    },
                    {
                        "node_id": "indole_test_positive_indole",
                        "label": "indole",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:35581",
                        "description": "Indole metabolite produced from bacterial tryptophan degradation and detected by the indole test.",
                    },
                ],
                "edges": [
                    {
                        "subject": "indole_test_positive_tryptophan_catabolism",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "indole_test_positive_indole",
                        "description": "Bacterial tryptophan degradation produces indole as a catabolic product.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Darkoh et al. characterize indole as a bacterial product of tryptophan degradation.",
                            )
                        ],
                    },
                    {
                        "subject": "indole_test_positive_tryptophan_catabolism",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "indole_test_positive_trait",
                        "description": "Catabolic conversion of supplemented tryptophan into millimolar indole confers the indole test positive phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Darkoh et al. show that enterotoxigenic Escherichia coli strain H10407 produces 3.3 +/- 0.22 mM indole in the presence of 5 mM tryptophan.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/pyrazinamidase_activity.yaml":
        return [
            {
                "graph_id": "pyrazinamidase_activity_pnca_sketch",
                "title": "Nicotinamidase/pyrazinamidase (PncA) hydrolysis of nicotinamide and pyrazinamide",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "nicotinamidase/pyrazinamidase catalytic activity, nicotinamide "
                    "hydrolysis to nicotinate, and pyrazinamide conversion to "
                    "pyrazinoic acid to the pyrazinamidase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 3.5.1.19, "
                    "DOI:10.1111/j.1742-4658.2007.06241.x, and "
                    "DOI:10.1371/journal.pone.0015785; strain-matched UniProtKB "
                    "protein examples for Mycobacterium tuberculosis PncA "
                    "(UniProtKB:I6Y493) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "pyrazinamidase_activity_trait",
                        "label": "pyrazinamidase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000163",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active nicotinamidase/pyrazinamidase enzymes.",
                    },
                    {
                        "node_id": "pyrazinamidase_catalytic_activity",
                        "label": "nicotinamidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0008936",
                        "description": "Catalytic hydrolysis of nicotinamide to nicotinate and ammonia (EC 3.5.1.19) and conversion of pyrazinamide to pyrazinoic acid by PncA.",
                    },
                    {
                        "node_id": "pyrazinamidase_nicotinate",
                        "label": "nicotinate",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:32544",
                        "description": "Nicotinate produced by nicotinamidase-catalyzed hydrolysis of nicotinamide and water.",
                    },
                ],
                "edges": [
                    {
                        "subject": "pyrazinamidase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "pyrazinamidase_activity_trait",
                        "description": "Nicotinamidase/pyrazinamidase (PncA) catalytic activity converts pyrazinamide into pyrazinoic acid and confers the pyrazinamidase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Zhang et al. show that the nicotinamidase/pyrazinamidase (PncA) of Mycobacterium tuberculosis converts pyrazinamide into pyrazinoic acid.",
                            )
                        ],
                    },
                    {
                        "subject": "pyrazinamidase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "pyrazinamidase_nicotinate",
                        "description": "Nicotinamidase hydrolyzes nicotinamide and water to produce nicotinate and ammonia.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 3.5.1.19 defines the nicotinamidase reaction converting nicotinamide and water into nicotinate and ammonia.",
                            )
                        ],
                    },
                ],
            }
        ]

    raise KeyError(f"Unexpected Cohort E path: {rel_path}")


def build_cohort_e_discussion(rel_path: str, doc: dict[str, Any], graph_id: str) -> dict[str, Any]:
    """Construct the CURATION_TODO DiscussionItem for a Cohort E record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale, ev_index = COHORT_E_PROTEIN_GAPS[rel_path]
    ev_list = doc.get("evidence") or []
    supporting_ev: list[dict[str, str]] = []
    if len(ev_list) > ev_index and isinstance(ev_list[ev_index], dict):
        src = ev_list[ev_index]
        ref = str(src.get("reference") or "").strip()
        snip = str(src.get("snippet") or "").strip()
        if ref and snip:
            supporting_ev.append(
                {
                    "reference": ref,
                    "supports": "PARTIAL",
                    "snippet": snip,
                    "explanation": (
                        "Existing record-level evidence supports the connected "
                        "NONMECHANISTIC pathway/function graph but does not provide "
                        "strain-matched UniProtKB protein accessions for protein_examples."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-protein-example-gap",
        "prompt": prompt,
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "attaches_to": [f"causal_graphs#{graph_id}"],
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE_C2,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


COHORT_F_GAPS: dict[str, tuple[str, str]] = {
    "data/traits/other/catalase_negative.yaml": (
        "Add primary literature evidence for the genetic or biochemical basis of catalase absence and alternative H2O2 scavenging (e.g. NADH peroxidase Npx) before constructing causal_graphs.",
        "This record represents a negative catalase-test outcome phenotype; its evidence pairs an assay-foam snippet (DOI:10.1038/srep03081) with a single sentence noting that Enterococcus faecium is catalase negative (DOI:10.1128/iai.72.8.4512-4520.2004), which does not ground a multi-edge causal graph for the negative test state.",
    ),
    "data/traits/other/catalase_test.yaml": (
        "Add multi-step mechanistic evidence or keep causal mechanism curation on the corresponding enzyme-activity record (catalase_positive / catalase activity) rather than the diagnostic assay class.",
        "METPO:1007080 represents a diagnostic biochemical test protocol (ASM catalase test protocol; DOI:10.1038/srep03081) rather than a cellular physiological pathway; the underlying H2O2 disproportionation mechanism is curated on catalase_positive.yaml.",
    ),
    "data/traits/other/circular_colony.yaml": (
        "Add primary literature evidence for the cellular growth, surface-motility, and extracellular-matrix determinants of circular colony morphology before constructing causal_graphs.",
        "The current record carries descriptive ASM colony-morphology protocol snippets defining macroscopic circular colony form without genetic, regulatory, or biophysical mechanism quotes.",
    ),
    "data/traits/other/coagulase_negative.yaml": (
        "Add primary literature evidence for the absence of coagulase genes (coa/vwb) in coagulase-negative staphylococci before considering any mechanism representation.",
        "This record represents a negative diagnostic test-outcome phenotype uniting coagulase-negative staphylococci (DOI:10.3390/microorganisms9040830; NBK563240) by the absence of plasma clotting rather than an active multi-step biochemical pathway.",
    ),
    "data/traits/other/colony_morphology.yaml": (
        "Add primary literature evidence for extracellular matrix, cell-surface appendage, and multicellular morphogenesis pathways before constructing causal_graphs on this upper colony-morphology class.",
        "The current record carries descriptive ASM protocol snippets enumerating macroscopic colony form, elevation, and margin categories without molecular or cellular mechanism quotes.",
    ),
    "data/traits/other/colony_shape.yaml": (
        "Add primary literature evidence for the biophysical and genetic determinants of macroscopic colony outline before constructing causal_graphs on this grouping class.",
        "The current record carries descriptive ASM protocol snippets illustrating colony form diagrams without molecular, regulatory, or biomechanical mechanism quotes.",
    ),
    "data/traits/other/epibiont_phenotype.yaml": (
        "Add primary literature evidence for surface attachment adhesins, biofilm formation, and host-epibiont interactions in Epibacterium ulvae before constructing causal_graphs.",
        "The current record carries two strain-isolation habitat snippets from the surface of the marine alga Ulva australis (DOI:10.1099/ijs.0.042838-0; BacDive 24523) without molecular colonization or attachment mechanism quotes.",
    ),
    "data/traits/other/filamentous_colony.yaml": (
        "Add primary literature evidence for filamentous cell-chain growth, extracellular matrix, and swarming/sliding determinants of filamentous colony outline before constructing causal_graphs.",
        "The current record carries a single general colony-morphology overview snippet (DOI:10.7759/cureus.374) without specific genetic or cellular morphogenesis quotes.",
    ),
    "data/traits/other/fried_egg_shaped_colony.yaml": (
        "Add primary literature evidence for central agar penetration versus peripheral surface growth determinants of fried-egg colony morphology before constructing causal_graphs.",
        "The current record carries a single morphological description snippet (DOI:10.1371/journal.pone.0068373) describing the opaque center and translucent peripheral zone without molecular or cellular mechanism quotes.",
    ),
    "data/traits/other/generalist.yaml": (
        "Add primary literature evidence for metabolic versatility, regulatory network plasticity, and broad resource-utilization pathways in a cited exemplar taxon before constructing causal_graphs.",
        "The current record carries two high-level ecological classification snippets (DOI:10.1093/femsec/fiaa240; DOI:10.1038/s41559-023-02027-7) contrasting niche breadth in generalists vs specialists without molecular mechanism quotes or a canonical example.",
    ),
    "data/traits/other/hemolysis.yaml": (
        "Add a second independent primary literature snippet covering cytolytic pore formation or membrane phospholipid cleavage by secreted Staphylococcus aureus hemolysins (e.g. Hla, Hlb) before constructing causal_graphs.",
        "The current record carries a single 54-character phrase ('hemolysis to toxigenic substances secreted by S. aureus' in DOI:10.3390/toxins5061140); constructing a multi-edge graph from one short phrase would violate the snippet-diversity and anti-clause-splitting rules.",
    ),
    "data/traits/other/hemolytic.yaml": (
        "Add a second independent primary literature snippet covering erythrocyte membrane lysis by secreted Staphylococcus aureus hemolysins (e.g. alpha-hemolysin Hla) before constructing causal_graphs.",
        "The current record carries a single 54-character phrase ('hemolysis to toxigenic substances secreted by S. aureus' in DOI:10.3390/toxins5061140); constructing a multi-edge graph from one short phrase would violate the snippet-diversity and anti-clause-splitting rules.",
    ),
    "data/traits/other/indole_test.yaml": (
        "Keep causal mechanism curation on the positive phenotype record (indole_test_positive) or add primary literature evidence for tryptophanase (TnaA) catalysis alongside Kovac's/Ehrlich's reagent detection.",
        "METPO:1005010 represents the diagnostic indole test assay protocol (ASM indole test protocol) rather than the organismal tryptophan-to-indole catabolic phenotype curated on indole_test_positive.yaml.",
    ),
    "data/traits/other/indole_test_negative.yaml": (
        "Add primary literature evidence for the absence or inactivation of tryptophanase (tnaA) in indole-negative Klebsiella pneumoniae isolates before considering a mechanism representation.",
        "This record represents a negative diagnostic test-outcome phenotype (DOI:10.1128/AEM.02787-15; DOI:10.1128/JCM.00940-06) defined by the absence of indole production from tryptophan.",
    ),
    "data/traits/other/irregular_colony.yaml": (
        "Add primary literature evidence for asymmetric edge expansion, nutrient-diffusion limitation, or extracellular matrix determinants of irregular colony outline before constructing causal_graphs.",
        "The current record carries a single general colony-morphology overview snippet (DOI:10.7759/cureus.374) without specific genetic or biophysical morphogenesis quotes.",
    ),
    "data/traits/other/methyl_red_test.yaml": (
        "Keep causal mechanism curation on mixed_acid_fermentation.yaml or add organism-level enzymatic evidence for mixed-acid pyruvate catabolism alongside the pH-indicator protocol.",
        "METPO:1005013 represents the diagnostic methyl red pH-indicator assay protocol (ASM Methyl Red and Voges-Proskauer protocol), whereas the underlying metabolic pathway is curated on mixed_acid_fermentation.yaml.",
    ),
    "data/traits/other/methyl_red_test_negative.yaml": (
        "Add primary literature evidence for neutral fermentation end-product routing (acetoin/2,3-butanediol conversion) in methyl-red-negative Klebsiella pneumoniae before constructing causal_graphs.",
        "This record represents a negative diagnostic test-outcome phenotype supported by ASM protocol color-threshold and clinical panel reproducibility snippets (DOI:10.1128/JCM.42.8.3665-3669.2004) without enzymatic pathway quotes.",
    ),
    "data/traits/other/methyl_red_test_positive.yaml": (
        "Add primary literature evidence for mixed-acid fermentation enzymes (e.g. PflB, LdhA, AckA-Pta) producing stable organic acids in Klebsiella ornithinolytica before constructing causal_graphs.",
        "The current record pairs an ASM pH-indicator color-change snippet with a clinical identification panel count snippet (DOI:10.1128/JCM.42.8.3665-3669.2004), lacking enzymatic or metabolic pathway quotes for the exemplar taxon.",
    ),
    "data/traits/other/non_hemolytic.yaml": (
        "Add primary literature evidence for the genetic absence of hemolysin/cytolysin operons in gamma-hemolytic strains before considering a mechanism representation.",
        "This record represents a negative diagnostic phenotype (gamma-hemolysis / absence of red-blood-cell lysis in DOI:10.14202/vetworld.2025.3622-3630) supported by a single screening snippet without a canonical example.",
    ),
    "data/traits/other/osmotic_tolerance.yaml": (
        "Add a second independent primary literature snippet covering compatible-solute uptake/synthesis (e.g. glycine betaine, trehalose, proline) and osmosensory regulation plus a canonical example before constructing causal_graphs.",
        "The current record carries a single 49-character snippet ('tolerance against hyperosmotic conditions (400 mM sorbitol)' in DOI:10.1128/mBio.00390-21) without a second mechanistic quote or canonical example.",
    ),
    "data/traits/other/oxidase_negative.yaml": (
        "Add primary literature evidence for cytochrome c oxidase absence and alternative terminal oxidases (e.g. cytochrome bd or bo3 quinol oxidases) in oxidase-negative taxa before considering a mechanism representation.",
        "This record represents a negative diagnostic test-outcome phenotype (ASM oxidase test protocol; DOI:10.5812/chbs-160199) defined by the absence of cytochrome c oxidase indicator oxidation.",
    ),
    "data/traits/other/oxidase_test.yaml": (
        "Keep causal mechanism curation on the positive enzyme-activity record (oxidase_positive) rather than the diagnostic redox-indicator assay class.",
        "METPO:1007081 represents the diagnostic oxidase test protocol (ASM oxidase test protocol; DOI:10.5812/chbs-160199), whereas the cytochrome c oxidase respiratory mechanism is curated on oxidase_positive.yaml.",
    ),
    "data/traits/other/punctiform_colony.yaml": (
        "Add primary literature evidence for slow growth rate, microcolony confinement, or metabolic constraints underlying pinpoint (<1 mm) punctiform colonies before constructing causal_graphs.",
        "The current record carries a single general colony-morphology overview snippet (DOI:10.7759/cureus.374) without specific genetic or physiological mechanism quotes.",
    ),
    "data/traits/other/rhizoid_colony.yaml": (
        "Add primary literature evidence for branching multicellular filamentation, surfactant production, or sliding motility underlying rhizoid colony morphology before constructing causal_graphs.",
        "The current record carries a single general colony-morphology overview snippet (DOI:10.7759/cureus.374) without specific genetic or cellular morphogenesis quotes.",
    ),
    "data/traits/other/specialist.yaml": (
        "Add primary literature evidence for genome reduction, narrow substrate-transport specificity, or strict host/habitat adaptation in a cited exemplar taxon before constructing causal_graphs.",
        "The current record carries two high-level ecological classification snippets (DOI:10.1093/femsec/fiaa240; DOI:10.1038/s41559-023-02027-7) contrasting niche breadth in generalists vs specialists without molecular mechanism quotes or a canonical example.",
    ),
    "data/traits/other/urease_negative.yaml": (
        "Add primary literature evidence for the absence of urease structural/accessory genes (ureABC/ureDEFG) in urease-negative taxa before considering a mechanism representation.",
        "This record represents a negative diagnostic test-outcome phenotype supported by phenol-red urease medium indicator snippets (DOI:10.5812/chbs-160199) without a canonical example or active enzymatic pathway.",
    ),
    "data/traits/other/urease_test.yaml": (
        "Keep causal mechanism curation on the positive enzyme-activity record (urease_positive) rather than the diagnostic urea-broth/agar assay class.",
        "METPO:1007082 represents the diagnostic urease test protocol (DOI:10.5812/chbs-160199), whereas the nickel-metalloenzyme urea hydrolysis mechanism is curated on urease_positive.yaml.",
    ),
    "data/traits/other/voges_proskauer_test.yaml": (
        "Keep causal mechanism curation on the metabolic pathway record (butanediol_fermentation) or add enzymatic evidence for alpha-acetolactate synthase (BudB) and decarboxylase (BudA) alongside the KOH/alpha-naphthol assay protocol.",
        "METPO:1005016 represents the diagnostic Voges-Proskauer assay protocol (ASM Methyl Red and Voges-Proskauer protocol) detecting acetoin oxidation to diacetyl in KOH rather than a standalone organismal gene-to-trait mechanism.",
    ),
    "data/traits/other/voges_proskauer_test_negative.yaml": (
        "Add primary literature evidence for the absence of the alpha-acetolactate-to-acetoin pathway in Voges-Proskauer-negative Escherichia coli before considering a mechanism representation.",
        "This record represents a negative diagnostic test-outcome phenotype supported by a single ASM protocol color-comparison snippet without enzymatic pathway quotes.",
    ),
    "data/traits/other/voges_proskauer_test_positive.yaml": (
        "Add primary literature evidence for alpha-acetolactate synthase (BudB) and alpha-acetolactate decarboxylase (BudA) acetoin biosynthesis in Klebsiella oxytoca before constructing causal_graphs.",
        "The current record pairs an ASM KOH-oxidation reagent chemistry snippet with a clinical identification panel count snippet (DOI:10.1128/JCM.42.8.3665-3669.2004), lacking organismal enzymatic catalysis quotes for acetoin biosynthesis.",
    ),
}


def build_cohort_f_discussion(rel_path: str, doc: dict[str, Any]) -> dict[str, Any]:
    """Construct the KNOWLEDGE_GAP DiscussionItem for a Cohort F record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale = COHORT_F_GAPS[rel_path]
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
                        "Existing record-level evidence supports the diagnostic assay, "
                        "test-outcome, colony-shape, or ecological-scope definition, "
                        "but does not provide multi-step molecular mechanism quotes "
                        "for a connected causal graph."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-causal-graph-source-gap",
        "prompt": prompt,
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "attaches_to": ["causal_graphs"],
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE_C2,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


COHORT_G_PATHS: tuple[str, ...] = (
    "data/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.yaml",
    "data/traits/physiology/ornithine_decarboxylase_activity.yaml",
    "data/traits/physiology/prolyl_aminopeptidase_activity.yaml",
)

COHORT_G_PROTEIN_GAPS: dict[str, tuple[str, str, int]] = {
    "data/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Zymomonas mobilis alcohol dehydrogenase II AdhB (UniProtKB:P0DTE6) so nad_dependent_alcohol_dehydrogenase_adh_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 1.1.1.1, DOI:10.1111/j.1432-1033.1986.tb09366.x, DOI:10.1128/jb.169.6.2591-2597.1987) establishes NAD-dependent alcohol dehydrogenase catalysis and adhB cloning/purification in Zymomonas mobilis (NCBITaxon:542), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/physiology/ornithine_decarboxylase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Escherichia coli K-12 biosynthetic ornithine decarboxylase SpeC (UniProtKB:P21169) so ornithine_decarboxylase_spec_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 4.1.1.17, DOI:10.1128/jb.124.2.791-799.1975) establishes L-ornithine decarboxylation to putrescine and CO2 and speC mutant loss of activity in Escherichia coli K-12 (NCBITaxon:83333), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/physiology/prolyl_aminopeptidase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Neisseria gonorrhoeae proline iminopeptidase Pip (UniProtKB:P40051) so prolyl_aminopeptidase_pip_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 3.4.11.5, DOI:10.1111/j.1365-2958.1993.tb01249.x) establishes N-terminal proline release from peptides by proline iminopeptidase (Pip) in Neisseria gonorrhoeae (NCBITaxon:485), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
}


def build_cohort_g_graphs(rel_path: str, doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Construct the connected NONMECHANISTIC causal_graphs list for a Cohort G record."""
    if rel_path == "data/traits/physiology/nad_dependent_alcohol_dehydrogenase_activity.yaml":
        return [
            {
                "graph_id": "nad_dependent_alcohol_dehydrogenase_adh_sketch",
                "title": "NAD-dependent alcohol dehydrogenase catalysis and NADH generation",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "NAD-dependent alcohol dehydrogenase catalytic activity and "
                    "NADH generation to the NAD-dependent alcohol dehydrogenase "
                    "activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 1.1.1.1, "
                    "DOI:10.1111/j.1432-1033.1986.tb09366.x, and "
                    "DOI:10.1128/jb.169.6.2591-2597.1987; strain-matched UniProtKB "
                    "protein examples for Zymomonas mobilis alcohol dehydrogenase II "
                    "(AdhB, UniProtKB:P0DTE6) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "nad_dependent_alcohol_dehydrogenase_activity_trait",
                        "label": "NAD-dependent alcohol dehydrogenase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000165",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active NAD-dependent alcohol dehydrogenases.",
                    },
                    {
                        "node_id": "nad_dependent_alcohol_dehydrogenase_catalytic_activity",
                        "label": "alcohol dehydrogenase (NAD+) activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004022",
                        "description": "NAD-dependent oxidoreductase activity interconverting primary or secondary alcohols with aldehydes or ketones and generating NADH (EC 1.1.1.1).",
                    },
                    {
                        "node_id": "nad_dependent_alcohol_dehydrogenase_nadh",
                        "label": "NADH",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:16908",
                        "description": "Reduced nicotinamide adenine dinucleotide cofactor produced during NAD+-dependent alcohol oxidation.",
                    },
                ],
                "edges": [
                    {
                        "subject": "nad_dependent_alcohol_dehydrogenase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "nad_dependent_alcohol_dehydrogenase_activity_trait",
                        "description": "Purified NAD-dependent alcohol dehydrogenase isoenzymes confer the organismal alcohol dehydrogenase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Neale et al. purified and characterized the two native NAD-dependent alcohol dehydrogenase isoenzymes found in Zymomonas mobilis.",
                            )
                        ],
                    },
                    {
                        "subject": "nad_dependent_alcohol_dehydrogenase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "nad_dependent_alcohol_dehydrogenase_nadh",
                        "description": "NAD-dependent alcohol dehydrogenase oxidizes primary or secondary alcohols with NAD+ to yield an aldehyde or ketone, NADH, and H+.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 1.1.1.1 defines the NAD-dependent alcohol dehydrogenase reaction producing an aldehyde or ketone, NADH, and H+.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/ornithine_decarboxylase_activity.yaml":
        return [
            {
                "graph_id": "ornithine_decarboxylase_spec_sketch",
                "title": "Ornithine decarboxylase conversion of L-ornithine to putrescine",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "ornithine decarboxylase catalytic activity and putrescine "
                    "biosynthesis to the ornithine decarboxylase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 4.1.1.17 and "
                    "DOI:10.1128/jb.124.2.791-799.1975; strain-matched UniProtKB "
                    "protein examples for Escherichia coli K-12 biosynthetic "
                    "ornithine decarboxylase (SpeC, UniProtKB:P21169) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "ornithine_decarboxylase_activity_trait",
                        "label": "ornithine decarboxylase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000154",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active ornithine decarboxylases that decarboxylate L-ornithine to putrescine and CO2.",
                    },
                    {
                        "node_id": "ornithine_decarboxylase_catalytic_activity",
                        "label": "ornithine decarboxylase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004586",
                        "description": "Catalytic decarboxylation of L-ornithine to putrescine and carbon dioxide (EC 4.1.1.17).",
                    },
                    {
                        "node_id": "ornithine_decarboxylase_putrescine",
                        "label": "putrescine",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:17148",
                        "description": "Diamine putrescine produced by decarboxylation of L-ornithine.",
                    },
                ],
                "edges": [
                    {
                        "subject": "ornithine_decarboxylase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "ornithine_decarboxylase_activity_trait",
                        "description": "Cellular synthesis of active ornithine decarboxylase confers the ornithine decarboxylase activity phenotype, which is abolished in E. coli K-12 OD mutants.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Cunningham-Rundles and Maas show that Escherichia coli K-12 mutants blocked in ornithine decarboxylase synthesis exhibit a virtual absence of OD activity in cellular extracts.",
                            )
                        ],
                    },
                    {
                        "subject": "ornithine_decarboxylase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "ornithine_decarboxylase_putrescine",
                        "description": "Ornithine decarboxylase converts L-ornithine into putrescine and carbon dioxide.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 4.1.1.17 defines the ornithine decarboxylase reaction converting L-ornithine into putrescine and CO2.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/prolyl_aminopeptidase_activity.yaml":
        return [
            {
                "graph_id": "prolyl_aminopeptidase_pip_sketch",
                "title": "Prolyl aminopeptidase (Pip) hydrolytic release of N-terminal L-proline",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "prolyl aminopeptidase catalytic activity and N-terminal "
                    "L-proline release from peptides to the prolyl aminopeptidase "
                    "activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 3.4.11.5 and "
                    "DOI:10.1111/j.1365-2958.1993.tb01249.x; strain-matched UniProtKB "
                    "protein examples for Neisseria gonorrhoeae proline iminopeptidase "
                    "(Pip, UniProtKB:P40051) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "prolyl_aminopeptidase_activity_trait",
                        "label": "prolyl aminopeptidase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000166",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active prolyl aminopeptidases that release N-terminal proline residues from peptides.",
                    },
                    {
                        "node_id": "prolyl_aminopeptidase_catalytic_activity",
                        "label": "aminopeptidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004177",
                        "description": "Prolyl aminopeptidase / proline iminopeptidase catalytic activity selectively cleaving N-terminal proline residues from peptides (EC 3.4.11.5).",
                    },
                    {
                        "node_id": "prolyl_aminopeptidase_proline",
                        "label": "L-proline",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:17203",
                        "description": "Free L-proline released from the N-terminus of peptides by prolyl aminopeptidase hydrolysis.",
                    },
                ],
                "edges": [
                    {
                        "subject": "prolyl_aminopeptidase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "prolyl_aminopeptidase_activity_trait",
                        "description": "Elaboration of proline iminopeptidase (Pip) hydrolase activity selectively removing N-terminal proline residues from peptides confers the prolyl aminopeptidase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Albertson and Koomey show that proline iminopeptidase (Pip) is a hydrolase elaborated by Neisseria gonorrhoeae that selectively removes N-terminal proline residues from peptides.",
                            )
                        ],
                    },
                    {
                        "subject": "prolyl_aminopeptidase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "prolyl_aminopeptidase_proline",
                        "description": "Prolyl aminopeptidase catalyzes the hydrolytic release of N-terminal proline from a peptide.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 3.4.11.5 defines the prolyl aminopeptidase reaction as the release of N-terminal proline from a peptide.",
                            )
                        ],
                    },
                ],
            }
        ]

    raise KeyError(f"Unexpected Cohort G path: {rel_path}")


def build_cohort_g_discussion(rel_path: str, doc: dict[str, Any], graph_id: str) -> dict[str, Any]:
    """Construct the CURATION_TODO DiscussionItem for a Cohort G record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale, ev_index = COHORT_G_PROTEIN_GAPS[rel_path]
    ev_list = doc.get("evidence") or []
    supporting_ev: list[dict[str, str]] = []
    if len(ev_list) > ev_index and isinstance(ev_list[ev_index], dict):
        src = ev_list[ev_index]
        ref = str(src.get("reference") or "").strip()
        snip = str(src.get("snippet") or "").strip()
        if ref and snip:
            supporting_ev.append(
                {
                    "reference": ref,
                    "supports": "PARTIAL",
                    "snippet": snip,
                    "explanation": (
                        "Existing record-level evidence supports the connected "
                        "NONMECHANISTIC pathway/function graph but does not provide "
                        "strain-matched UniProtKB protein accessions for protein_examples."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-protein-example-gap",
        "prompt": prompt,
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "attaches_to": [f"causal_graphs#{graph_id}"],
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE_C4,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


COHORT_H_PATHS: tuple[str, ...] = (
    "data/traits/metabolism/butanediol_fermentation.yaml",
    "data/traits/physiology/beta_glucuronidase_activity.yaml",
    "data/traits/physiology/beta_n_acetylhexosaminidase_activity.yaml",
)

COHORT_H_PROTEIN_GAPS: dict[str, tuple[str, str, int]] = {
    "data/traits/metabolism/butanediol_fermentation.yaml": (
        "Add strain-matched UniProtKB protein_examples for Klebsiella pneumoniae meso-2,3-butanediol dehydrogenase BudC (UniProtKB:Q48436) so butanediol_fermentation_acetoin_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.1186/s12934-023-02163-6, ASM Methyl Red / Voges-Proskauer protocol, DOI:10.1007/s00253-014-5526-9) establishes acetoin intermediate reduction to 2,3-butanediol and stereoisomer production in Klebsiella pneumoniae (NCBITaxon:573), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        2,
    ),
    "data/traits/physiology/beta_glucuronidase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Escherichia coli K-12 beta-glucuronidase UidA (UniProtKB:P05804) so beta_glucuronidase_uida_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 3.2.1.31, DOI:10.1128/aem.50.6.1383-1387.1985) establishes beta-D-glucuronoside hydrolysis to D-glucuronate and alcohol and MUG substrate cleavage in Escherichia coli (NCBITaxon:562), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/physiology/beta_n_acetylhexosaminidase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Serratia marcescens chitobiase Chb (UniProtKB:Q54468) so beta_n_acetylhexosaminidase_chb_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 3.2.1.52, DOI:10.1021/jf020965x) establishes hydrolytic release of terminal non-reducing N-acetyl-D-hexosamine residues and N-acetylhexosaminidase production in Serratia marcescens (NCBITaxon:615), but a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
}


def build_cohort_h_graphs(rel_path: str, doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Construct the connected NONMECHANISTIC causal_graphs list for a Cohort H record."""
    if rel_path == "data/traits/metabolism/butanediol_fermentation.yaml":
        return [
            {
                "graph_id": "butanediol_fermentation_acetoin_sketch",
                "title": "Acetoin intermediate formation and reduction to 2,3-butanediol",
                "description": (
                    "Evidence-backed metabolic pathway sketch linking acetoin "
                    "(3-hydroxybutanone) intermediate reduction and 2,3-butanediol "
                    "production to the 2,3-butanediol fermentation phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Metabolic-intermediate sketch backed by the ASM Methyl Red / "
                    "Voges-Proskauer protocol and DOI:10.1007/s00253-014-5526-9; "
                    "strain-matched UniProtKB protein examples for Klebsiella "
                    "pneumoniae meso-2,3-butanediol dehydrogenase (BudC, "
                    "UniProtKB:Q48436) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "butanediol_fermentation_trait",
                        "label": "2,3-butanediol fermentation",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000181",
                        "description": "Fermentation phenotype in which microorganisms convert sugars via acetoin into 2,3-butanediol neutral end products.",
                    },
                    {
                        "node_id": "butanediol_fermentation_acetoin",
                        "label": "acetoin",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:15688",
                        "description": "Acetoin (3-hydroxybutanone), the four-carbon ketone intermediate formed during sugar fermentation via the butanediol pathway.",
                    },
                    {
                        "node_id": "butanediol_fermentation_2_3_butanediol",
                        "label": "butane-2,3-diol",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:16982",
                        "description": "Neutral four-carbon diol product (2,3-butanediol) formed by enzymatic reduction of acetoin during butanediol fermentation.",
                    },
                ],
                "edges": [
                    {
                        "subject": "butanediol_fermentation_acetoin",
                        "predicate": "derives into",
                        "predicate_id": "RO:0001001",
                        "object": "butanediol_fermentation_2_3_butanediol",
                        "description": "Bacteria fermenting sugars via the butanediol pathway produce acetoin as an intermediate that is further reduced to 2,3-butanediol.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "The ASM Methyl Red / Voges-Proskauer protocol states that bacteria fermenting sugars via the butanediol pathway produce acetoin (3-hydroxybutanone) as an intermediate that can be further reduced to 2,3-butanediol.",
                            )
                        ],
                    },
                    {
                        "subject": "butanediol_fermentation_2_3_butanediol",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "butanediol_fermentation_trait",
                        "description": "Production of meso-2,3-butanediol, (2S,3S)-butanediol, and (2R,3R)-butanediol stereoisomers in culture broth confers the 2,3-butanediol fermentation phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                2,
                                "Chen et al. show that Klebsiella pneumoniae produces meso-2,3-butanediol, 2S,3S-butanediol, and 2R,3R-butanediol in culture broth.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/beta_glucuronidase_activity.yaml":
        return [
            {
                "graph_id": "beta_glucuronidase_uida_sketch",
                "title": "Beta-glucuronidase hydrolysis of beta-D-glucuronosides to D-glucuronate",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "beta-glucuronidase catalytic activity and D-glucuronate "
                    "release to the beta-glucuronidase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 3.2.1.31 and "
                    "DOI:10.1128/aem.50.6.1383-1387.1985; strain-matched UniProtKB "
                    "protein examples for Escherichia coli K-12 beta-glucuronidase "
                    "(UidA, UniProtKB:P05804) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "beta_glucuronidase_activity_trait",
                        "label": "beta-glucuronidase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000151",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active beta-glucuronidase enzymes that hydrolyze beta-D-glucuronosides.",
                    },
                    {
                        "node_id": "beta_glucuronidase_catalytic_activity",
                        "label": "beta-glucuronidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004566",
                        "description": "Glycosidase catalytic activity hydrolyzing a beta-D-glucuronoside with H2O to yield D-glucuronate and an alcohol (EC 3.2.1.31).",
                    },
                    {
                        "node_id": "beta_glucuronidase_d_glucuronate",
                        "label": "D-glucuronate",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:15748",
                        "description": "Free D-glucuronate released by beta-glucuronidase hydrolysis of beta-D-glucuronosides.",
                    },
                ],
                "edges": [
                    {
                        "subject": "beta_glucuronidase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "beta_glucuronidase_activity_trait",
                        "description": "Cellular production of active beta-glucuronidase that cleaves beta-D-glucuronide substrates such as MUG confers the beta-glucuronidase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Moberg shows that the beta-glucuronidase produced by Escherichia coli cleaves the MUG substrate to yield a fluorescent end product.",
                            )
                        ],
                    },
                    {
                        "subject": "beta_glucuronidase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "beta_glucuronidase_d_glucuronate",
                        "description": "Beta-glucuronidase hydrolyzes a beta-D-glucuronoside with H2O to produce D-glucuronate and an alcohol.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 3.2.1.31 defines the beta-glucuronidase reaction hydrolyzing a beta-D-glucuronoside with H2O to D-glucuronate and an alcohol.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/beta_n_acetylhexosaminidase_activity.yaml":
        return [
            {
                "graph_id": "beta_n_acetylhexosaminidase_chb_sketch",
                "title": "Beta-N-acetylhexosaminidase hydrolytic release of N-acetyl-D-hexosamine residues",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "beta-N-acetylhexosaminidase catalytic activity and "
                    "N-acetyl-D-glucosamine release to the "
                    "beta-N-acetylhexosaminidase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 3.2.1.52 and "
                    "DOI:10.1021/jf020965x; strain-matched UniProtKB protein "
                    "examples for Serratia marcescens chitobiase (Chb, "
                    "UniProtKB:Q54468) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "beta_n_acetylhexosaminidase_activity_trait",
                        "label": "beta-N-acetylhexosaminidase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000157",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active beta-N-acetylhexosaminidase enzymes.",
                    },
                    {
                        "node_id": "beta_n_acetylhexosaminidase_catalytic_activity",
                        "label": "beta-N-acetylhexosaminidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004563",
                        "description": "Glycosidase catalytic activity hydrolyzing terminal non-reducing N-acetyl-D-hexosamine residues in N-acetyl-beta-D-hexosaminides (EC 3.2.1.52).",
                    },
                    {
                        "node_id": "beta_n_acetylhexosaminidase_hexosamine",
                        "label": "N-acetyl-D-glucosamine",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:59640",
                        "description": "Terminal N-acetyl-D-hexosamine (N-acetyl-D-glucosamine) monomer released by beta-N-acetylhexosaminidase hydrolysis of chitooligosaccharides and N-acetyl-beta-D-hexosaminides.",
                    },
                ],
                "edges": [
                    {
                        "subject": "beta_n_acetylhexosaminidase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "beta_n_acetylhexosaminidase_activity_trait",
                        "description": "Production of active beta-N-acetylhexosaminidase by chitin-degrading bacteria confers the beta-N-acetylhexosaminidase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Kurakake et al. show that Serratia marcescens YS-1, a chitin-degrading microorganism, produced mainly N-acetylhexosaminidase.",
                            )
                        ],
                    },
                    {
                        "subject": "beta_n_acetylhexosaminidase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "beta_n_acetylhexosaminidase_hexosamine",
                        "description": "Beta-N-acetylhexosaminidase catalyzes the hydrolysis of terminal non-reducing N-acetyl-D-hexosamine residues in N-acetyl-beta-D-hexosaminides.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 3.2.1.52 defines beta-N-acetylhexosaminidase catalysis as the hydrolysis of terminal non-reducing N-acetyl-D-hexosamine residues in N-acetyl-beta-D-hexosaminides.",
                            )
                        ],
                    },
                ],
            }
        ]

    raise KeyError(f"Unexpected Cohort H path: {rel_path}")


def build_cohort_h_discussion(rel_path: str, doc: dict[str, Any], graph_id: str) -> dict[str, Any]:
    """Construct the CURATION_TODO DiscussionItem for a Cohort H record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale, ev_index = COHORT_H_PROTEIN_GAPS[rel_path]
    ev_list = doc.get("evidence") or []
    supporting_ev: list[dict[str, str]] = []
    if len(ev_list) > ev_index and isinstance(ev_list[ev_index], dict):
        src = ev_list[ev_index]
        ref = str(src.get("reference") or "").strip()
        snip = str(src.get("snippet") or "").strip()
        if ref and snip:
            supporting_ev.append(
                {
                    "reference": ref,
                    "supports": "PARTIAL",
                    "snippet": snip,
                    "explanation": (
                        "Existing record-level evidence supports the connected "
                        "NONMECHANISTIC pathway/function graph but does not provide "
                        "strain-matched UniProtKB protein accessions for protein_examples."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-protein-example-gap",
        "prompt": prompt,
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "attaches_to": [f"causal_graphs#{graph_id}"],
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE_C5,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


COHORT_I_PATHS: tuple[str, ...] = (
    "data/traits/physiology/alpha_fucosidase_activity.yaml",
    "data/traits/physiology/amylase_activity.yaml",
    "data/traits/physiology/beta_galactosidase_activity.yaml",
)

COHORT_I_PROTEIN_GAPS: dict[str, tuple[str, str, int]] = {
    "data/traits/physiology/alpha_fucosidase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Bacteroides thetaiotaomicron VPI-5482 alpha-L-fucosidase BT_2970 (UniProtKB:Q8A3I4) so alpha_fucosidase_hydrolysis_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 3.2.1.51, DOI:10.1128/jcm.22.3.333-335.1985) establishes hydrolytic cleavage of alpha-L-fucosides with H2O to L-fucose and an alcohol and positive alpha-fucosidase activity in Tannerella forsythia (NCBITaxon:28112), while Bacteroides thetaiotaomicron VPI-5482 (NCBITaxon:226186, DOI:10.1073/pnas.251226098) is a cited canonical example; a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/physiology/amylase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Bacillus licheniformis alpha-amylase AmyS (UniProtKB:P06278) so amylase_starch_hydrolysis_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (DOI:10.3389/fbioe.2020.00871, DOI:10.1007/s00018-023-04812-w) establishes amylolytic enzyme degradation of starch and extracellular alpha-amylase activity in Bacteroides ovatus, while Bacillus licheniformis (NCBITaxon:1402, DOI:10.1007/s002530200001) is a cited canonical example; a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
    "data/traits/physiology/beta_galactosidase_activity.yaml": (
        "Add strain-matched UniProtKB protein_examples for Escherichia coli K-12 beta-galactosidase LacZ (UniProtKB:P00722) so beta_galactosidase_lacz_sketch can be promoted from NONMECHANISTIC to MECHANISTIC.",
        "The record's primary literature (EC 3.2.1.23, DOI:10.3389/fmicb.2021.742300, DOI:10.1128/jcm.22.3.333-335.1985) establishes beta-galactosidase hydrolysis of lactose O-glycosidic bonds to glucose and galactose and positive beta-galactosidase activity in Selenomonas sputigena (NCBITaxon:69823), while Escherichia coli K-12 (NCBITaxon:83333, DOI:10.1038/369761a0) is a cited canonical example; a verified UniProtKB accession on a GENE_OR_PROTEIN node must be curated before marking the graph MECHANISTIC.",
        1,
    ),
}


def build_cohort_i_graphs(rel_path: str, doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Construct the connected NONMECHANISTIC causal_graphs list for a Cohort I record."""
    if rel_path == "data/traits/physiology/alpha_fucosidase_activity.yaml":
        return [
            {
                "graph_id": "alpha_fucosidase_hydrolysis_sketch",
                "title": "Alpha-L-fucosidase hydrolytic cleavage of alpha-L-fucosides",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "alpha-L-fucosidase catalytic activity and hydrolytic water "
                    "consumption to the alpha-fucosidase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by EC 3.2.1.51 and "
                    "DOI:10.1128/jcm.22.3.333-335.1985; strain-matched UniProtKB "
                    "protein examples for Bacteroides thetaiotaomicron VPI-5482 "
                    "alpha-L-fucosidase (BT_2970, UniProtKB:Q8A3I4) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "alpha_fucosidase_activity_trait",
                        "label": "alpha-fucosidase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000152",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active alpha-fucosidase enzymes that hydrolyze alpha-L-fucosides to L-fucose and an alcohol.",
                    },
                    {
                        "node_id": "alpha_fucosidase_catalytic_activity",
                        "label": "alpha-L-fucosidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004560",
                        "description": "Glycosidase catalytic activity hydrolyzing an alpha-L-fucoside with H2O to yield L-fucose and an alcohol (EC 3.2.1.51).",
                    },
                    {
                        "node_id": "alpha_fucosidase_water",
                        "label": "water",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:15377",
                        "description": "Water molecule consumed as a hydrolytic co-substrate during cleavage of alpha-L-fucoside linkages.",
                    },
                ],
                "edges": [
                    {
                        "subject": "alpha_fucosidase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "alpha_fucosidase_activity_trait",
                        "description": "Cellular production of active alpha-L-fucosidase detected by alpha-fucoside substrate hydrolysis confers the alpha-fucosidase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Tanner et al. report positive alpha-fucosidase reactions in API ZYM enzyme activity panels for Tannerella forsythia ('B. forsythus').",
                            )
                        ],
                    },
                    {
                        "subject": "alpha_fucosidase_catalytic_activity",
                        "predicate": "has input",
                        "predicate_id": "RO:0002233",
                        "object": "alpha_fucosidase_water",
                        "description": "Alpha-L-fucosidase hydrolyzes an alpha-L-fucoside with H2O to produce L-fucose and an alcohol.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "IUBMB EC 3.2.1.51 defines the alpha-L-fucosidase reaction hydrolyzing an alpha-L-fucoside with H2O to L-fucose and an alcohol.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/amylase_activity.yaml":
        return [
            {
                "graph_id": "amylase_starch_hydrolysis_sketch",
                "title": "Extracellular amylase catalysis and starch catabolism",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "extracellular amylase catalytic activity and starch "
                    "catabolism to the amylase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-pathway sketch backed by DOI:10.3389/fbioe.2020.00871 "
                    "and DOI:10.1007/s00018-023-04812-w; strain-matched UniProtKB "
                    "protein examples for Bacillus licheniformis alpha-amylase "
                    "(AmyS, UniProtKB:P06278) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "amylase_activity_trait",
                        "label": "amylase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000162",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active amylolytic enzymes that hydrolyze starch.",
                    },
                    {
                        "node_id": "amylase_catalytic_activity",
                        "label": "amylase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0016160",
                        "description": "Amylolytic glycoside hydrolase activity catalyzing the endohydrolysis or exohydrolysis of starch polysaccharides.",
                    },
                    {
                        "node_id": "amylase_starch_catabolism",
                        "label": "starch catabolic process",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0005983",
                        "description": "Enzymatic breakdown and degradation of starch polysaccharides by amylolytic enzymes.",
                    },
                ],
                "edges": [
                    {
                        "subject": "amylase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "amylase_activity_trait",
                        "description": "Production of extracellular alpha-amylase enzymes such as BoGH13ASus confers the amylase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Brown et al. characterize the Bacteroides ovatus extracellular alpha-amylase BoGH13ASus in starch utilization.",
                            )
                        ],
                    },
                    {
                        "subject": "amylase_catalytic_activity",
                        "predicate": "causally upstream of",
                        "predicate_id": "RO:0002411",
                        "object": "amylase_starch_catabolism",
                        "description": "Amylolytic enzymes catalyze the degradation of starch polysaccharides.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Sidar et al. define all enzymes capable of degrading starch collectively as amylolytic enzymes.",
                            )
                        ],
                    },
                ],
            }
        ]

    if rel_path == "data/traits/physiology/beta_galactosidase_activity.yaml":
        return [
            {
                "graph_id": "beta_galactosidase_lacz_sketch",
                "title": "Beta-galactosidase hydrolysis of lactose O-glycosidic bonds to glucose and galactose",
                "description": (
                    "Evidence-backed physiological mechanism sketch linking "
                    "beta-galactosidase catalytic activity and glucose release "
                    "from lactose hydrolysis to the beta-galactosidase activity phenotype."
                ),
                "scope_status": "NONMECHANISTIC",
                "scope_notes": (
                    "Activity-and-reaction sketch backed by DOI:10.3389/fmicb.2021.742300 "
                    "and DOI:10.1128/jcm.22.3.333-335.1985; strain-matched UniProtKB "
                    "protein examples for Escherichia coli K-12 beta-galactosidase "
                    "(LacZ, UniProtKB:P00722) remain to be curated."
                ),
                "nodes": [
                    {
                        "node_id": "beta_galactosidase_activity_trait",
                        "label": "beta-galactosidase activity",
                        "node_type": "TRAIT",
                        "grounding": "traitmech:000148",
                        "description": "Physiological enzyme-activity phenotype in which a cell produces active beta-galactosidase enzymes that hydrolyze lactose into glucose and galactose.",
                    },
                    {
                        "node_id": "beta_galactosidase_catalytic_activity",
                        "label": "beta-galactosidase activity",
                        "node_type": "MOLECULAR_FUNCTION",
                        "grounding": "GO:0004565",
                        "description": "Glycosyl hydrolase catalytic activity hydrolyzing O-glycosidic bonds of lactose to produce glucose and galactose (EC 3.2.1.23).",
                    },
                    {
                        "node_id": "beta_galactosidase_glucose",
                        "label": "glucose",
                        "node_type": "CHEMICAL",
                        "grounding": "CHEBI:17234",
                        "description": "Free D-glucose monomer released alongside galactose by beta-galactosidase hydrolysis of lactose.",
                    },
                ],
                "edges": [
                    {
                        "subject": "beta_galactosidase_catalytic_activity",
                        "predicate": "confers",
                        "predicate_id": "METPO:2007700",
                        "object": "beta_galactosidase_activity_trait",
                        "description": "Cellular production of active beta-galactosidase detected in chromogenic substrate panels confers the beta-galactosidase activity phenotype.",
                        "evidence": [
                            _ev_item(
                                doc,
                                1,
                                "Tanner et al. report Selenomonas sputigena as positive for beta-galactosidase in API ZYM enzyme activity strips.",
                            )
                        ],
                    },
                    {
                        "subject": "beta_galactosidase_catalytic_activity",
                        "predicate": "has output",
                        "predicate_id": "RO:0002234",
                        "object": "beta_galactosidase_glucose",
                        "description": "Beta-galactosidase hydrolyzes the O-glycosidic bonds of lactose to produce glucose and galactose.",
                        "evidence": [
                            _ev_item(
                                doc,
                                0,
                                "Zhou et al. state that beta-galactosidase (EC 3.2.1.23) hydrolyzes O-glycosidic bonds of lactose resulting in the production of glucose and galactose.",
                            )
                        ],
                    },
                ],
            }
        ]

    raise KeyError(f"Unexpected Cohort I path: {rel_path}")


def build_cohort_i_discussion(rel_path: str, doc: dict[str, Any], graph_id: str) -> dict[str, Any]:
    """Construct the CURATION_TODO DiscussionItem for a Cohort I record."""
    slug = Path(rel_path).stem.replace("_", "-")
    prompt, rationale, ev_index = COHORT_I_PROTEIN_GAPS[rel_path]
    ev_list = doc.get("evidence") or []
    supporting_ev: list[dict[str, str]] = []
    if len(ev_list) > ev_index and isinstance(ev_list[ev_index], dict):
        src = ev_list[ev_index]
        ref = str(src.get("reference") or "").strip()
        snip = str(src.get("snippet") or "").strip()
        if ref and snip:
            supporting_ev.append(
                {
                    "reference": ref,
                    "supports": "PARTIAL",
                    "snippet": snip,
                    "explanation": (
                        "Existing record-level evidence supports the connected "
                        "NONMECHANISTIC pathway/function graph but does not provide "
                        "strain-matched UniProtKB protein accessions for protein_examples."
                    ),
                }
            )
    discussion: dict[str, Any] = {
        "discussion_id": f"{slug}-protein-example-gap",
        "prompt": prompt,
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "attaches_to": [f"causal_graphs#{graph_id}"],
        "rationale": rationale,
        "posed_by": CURATOR,
        "posed_date": POSED_DATE_C6,
    }
    if supporting_ev:
        discussion["evidence"] = supporting_ev
    return discussion


def process_all(apply: bool = False) -> tuple[int, int]:
    """Process Cohort A, B, C, D, E, F, G, H, and I records. Returns (graphs_added, gaps_added)."""
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
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
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

    for rel_path in COHORT_C_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = build_cohort_c_graphs(rel_path, doc)
        graph_id = graphs[0]["graph_id"]
        disc = build_cohort_c_discussion(rel_path, doc, graph_id)
        disc_id = disc["discussion_id"]
        existing_disc = doc.get("discussions") or []
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
        existing_graphs = doc.get("causal_graphs") or []
        if existing_graphs == graphs and matched and matched[0] == disc:
            continue
        if (
            len(existing_graphs) == 1
            and existing_graphs[0].get("graph_id") == graph_id
            and matched
            and matched[0].get("kind") == "CURATION_TODO"
            and matched[0].get("attaches_to") == [f"causal_graphs#{graph_id}"]
            and (
                (
                    existing_graphs[0].get("scope_status") == "MECHANISTIC"
                    and matched[0].get("status") == "RESOLVED"
                    and matched[0].get("resolution_note")
                )
                or (
                    existing_graphs == graphs
                    and matched[0].get("status") == "OPEN"
                    and matched[0].get("notes")
                )
            )
        ):
            _verify_graph_invariants(rel_path, doc, existing_graphs)
            continue
        _verify_graph_invariants(rel_path, doc, graphs)
        doc["causal_graphs"] = graphs
        if matched:
            for idx, d in enumerate(existing_disc):
                if isinstance(d, dict) and d.get("discussion_id") == disc_id:
                    existing_disc[idx] = disc
            doc["discussions"] = existing_disc
        else:
            existing_disc.append(disc)
            doc["discussions"] = existing_disc
            scope_status = graphs[0]["scope_status"]
            record_curation_event(
                doc,
                action=CURATION_ACTION_GRAPH,
                curator=CURATOR,
                changes=(
                    f"Added {scope_status} causal_graphs entry ({graph_id}) "
                    f"and OPEN CURATION_TODO discussion ({disc_id}) anchored on "
                    "existing verbatim record evidence snippets."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        graphs_added += 1

    for rel_path in sorted(COHORT_D_GAPS):
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        existing_disc = doc.get("discussions") or []
        disc = build_cohort_d_discussion(rel_path, doc)
        disc_id = disc["discussion_id"]
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
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
                    f"Recorded OPEN KNOWLEDGE_GAP discussion ({disc_id}) attached to "
                    "causal_graphs documenting the source-limited mechanism gap."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        gaps_added += 1

    for rel_path in COHORT_E_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = build_cohort_e_graphs(rel_path, doc)
        graph_id = graphs[0]["graph_id"]
        disc = build_cohort_e_discussion(rel_path, doc, graph_id)
        disc_id = disc["discussion_id"]
        existing_disc = doc.get("discussions") or []
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
        existing_graphs = doc.get("causal_graphs") or []
        source_gap_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        open_source_gaps = [
            d
            for d in existing_disc
            if isinstance(d, dict)
            and d.get("discussion_id") == source_gap_id
            and (d.get("status") == "OPEN" or d.get("attaches_to") != [f"causal_graphs#{graph_id}"])
        ]
        if existing_graphs == graphs and matched and matched[0] == disc and not open_source_gaps:
            continue
        if (
            len(existing_graphs) == 1
            and existing_graphs[0].get("graph_id") == graph_id
            and matched
            and matched[0].get("kind") == "CURATION_TODO"
            and matched[0].get("attaches_to") == [f"causal_graphs#{graph_id}"]
            and not open_source_gaps
            and (
                (
                    existing_graphs[0].get("scope_status") == "MECHANISTIC"
                    and matched[0].get("status") == "RESOLVED"
                    and matched[0].get("resolution_note")
                )
                or (
                    existing_graphs == graphs
                    and matched[0].get("status") == "OPEN"
                    and matched[0].get("notes")
                )
            )
        ):
            _verify_graph_invariants(rel_path, doc, existing_graphs)
            continue
        _verify_graph_invariants(rel_path, doc, graphs)
        doc["causal_graphs"] = graphs
        for d in existing_disc:
            if isinstance(d, dict) and d.get("discussion_id") == source_gap_id:
                d["status"] = "RESOLVED"
                d["resolved_date"] = POSED_DATE_C2
                d["attaches_to"] = [f"causal_graphs#{graph_id}"]
                d["resolution_note"] = (
                    f"Added connected NONMECHANISTIC causal_graphs entry ({graph_id}) "
                    "anchored on existing verbatim record evidence snippets, and "
                    "tracked the remaining strain-matched UniProtKB protein-example "
                    f"requirement in {disc_id}."
                )
        if matched:
            for idx, d in enumerate(existing_disc):
                if isinstance(d, dict) and d.get("discussion_id") == disc_id:
                    existing_disc[idx] = disc
            doc["discussions"] = existing_disc
        else:
            existing_disc.append(disc)
            doc["discussions"] = existing_disc
            scope_status = graphs[0]["scope_status"]
            record_curation_event(
                doc,
                action=CURATION_ACTION_GRAPH,
                curator=CURATOR,
                changes=(
                    f"Added {scope_status} causal_graphs entry ({graph_id}) "
                    f"and OPEN CURATION_TODO discussion ({disc_id}) anchored on "
                    "existing verbatim record evidence snippets."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        graphs_added += 1

    for rel_path in sorted(COHORT_F_GAPS):
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        existing_disc = doc.get("discussions") or []
        disc = build_cohort_f_discussion(rel_path, doc)
        disc_id = disc["discussion_id"]
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
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
                    f"Recorded OPEN KNOWLEDGE_GAP discussion ({disc_id}) attached to "
                    "causal_graphs documenting the source-limited mechanism gap."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        gaps_added += 1

    for rel_path in COHORT_G_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = build_cohort_g_graphs(rel_path, doc)
        graph_id = graphs[0]["graph_id"]
        disc = build_cohort_g_discussion(rel_path, doc, graph_id)
        disc_id = disc["discussion_id"]
        existing_disc = doc.get("discussions") or []
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
        existing_graphs = doc.get("causal_graphs") or []
        source_gap_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        open_source_gaps = [
            d
            for d in existing_disc
            if isinstance(d, dict)
            and d.get("discussion_id") == source_gap_id
            and (d.get("status") == "OPEN" or d.get("attaches_to") != [f"causal_graphs#{graph_id}"])
        ]
        if existing_graphs == graphs and matched and matched[0] == disc and not open_source_gaps:
            continue
        if (
            len(existing_graphs) == 1
            and existing_graphs[0].get("graph_id") == graph_id
            and matched
            and matched[0].get("kind") == "CURATION_TODO"
            and matched[0].get("attaches_to") == [f"causal_graphs#{graph_id}"]
            and not open_source_gaps
            and (
                (
                    existing_graphs[0].get("scope_status") == "MECHANISTIC"
                    and matched[0].get("status") == "RESOLVED"
                    and matched[0].get("resolution_note")
                )
                or (
                    existing_graphs == graphs
                    and matched[0].get("status") == "OPEN"
                    and matched[0].get("notes")
                )
            )
        ):
            _verify_graph_invariants(rel_path, doc, existing_graphs)
            continue
        _verify_graph_invariants(rel_path, doc, graphs)
        doc["causal_graphs"] = graphs
        for d in existing_disc:
            if isinstance(d, dict) and d.get("discussion_id") == source_gap_id:
                d["status"] = "RESOLVED"
                d["resolved_date"] = POSED_DATE_C4
                d["attaches_to"] = [f"causal_graphs#{graph_id}"]
                d["resolution_note"] = (
                    f"Added connected NONMECHANISTIC causal_graphs entry ({graph_id}) "
                    "anchored on existing verbatim record evidence snippets, and "
                    "tracked the remaining strain-matched UniProtKB protein-example "
                    f"requirement in {disc_id}."
                )
        if matched:
            for idx, d in enumerate(existing_disc):
                if isinstance(d, dict) and d.get("discussion_id") == disc_id:
                    existing_disc[idx] = disc
            doc["discussions"] = existing_disc
        else:
            existing_disc.append(disc)
            doc["discussions"] = existing_disc
            scope_status = graphs[0]["scope_status"]
            record_curation_event(
                doc,
                action=CURATION_ACTION_GRAPH,
                curator=CURATOR,
                changes=(
                    f"Added {scope_status} causal_graphs entry ({graph_id}) "
                    f"and OPEN CURATION_TODO discussion ({disc_id}) anchored on "
                    "existing verbatim record evidence snippets."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        graphs_added += 1

    for rel_path in COHORT_H_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = build_cohort_h_graphs(rel_path, doc)
        graph_id = graphs[0]["graph_id"]
        disc = build_cohort_h_discussion(rel_path, doc, graph_id)
        disc_id = disc["discussion_id"]
        existing_disc = doc.get("discussions") or []
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
        existing_graphs = doc.get("causal_graphs") or []
        source_gap_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        open_source_gaps = [
            d
            for d in existing_disc
            if isinstance(d, dict)
            and d.get("discussion_id") == source_gap_id
            and (d.get("status") == "OPEN" or d.get("attaches_to") != [f"causal_graphs#{graph_id}"])
        ]
        if existing_graphs == graphs and matched and matched[0] == disc and not open_source_gaps:
            continue
        if (
            len(existing_graphs) == 1
            and existing_graphs[0].get("graph_id") == graph_id
            and matched
            and matched[0].get("kind") == "CURATION_TODO"
            and matched[0].get("attaches_to") == [f"causal_graphs#{graph_id}"]
            and not open_source_gaps
            and (
                (
                    existing_graphs[0].get("scope_status") == "MECHANISTIC"
                    and matched[0].get("status") == "RESOLVED"
                    and matched[0].get("resolution_note")
                )
                or (
                    existing_graphs == graphs
                    and matched[0].get("status") == "OPEN"
                    and matched[0].get("notes")
                )
            )
        ):
            _verify_graph_invariants(rel_path, doc, existing_graphs)
            continue
        _verify_graph_invariants(rel_path, doc, graphs)
        doc["causal_graphs"] = graphs
        for d in existing_disc:
            if isinstance(d, dict) and d.get("discussion_id") == source_gap_id:
                d["status"] = "RESOLVED"
                d["resolved_date"] = POSED_DATE_C5
                d["attaches_to"] = [f"causal_graphs#{graph_id}"]
                d["resolution_note"] = (
                    f"Added connected NONMECHANISTIC causal_graphs entry ({graph_id}) "
                    "anchored on existing verbatim record evidence snippets, and "
                    "tracked the remaining strain-matched UniProtKB protein-example "
                    f"requirement in {disc_id}."
                )
        if matched:
            for idx, d in enumerate(existing_disc):
                if isinstance(d, dict) and d.get("discussion_id") == disc_id:
                    existing_disc[idx] = disc
            doc["discussions"] = existing_disc
        else:
            existing_disc.append(disc)
            doc["discussions"] = existing_disc
            scope_status = graphs[0]["scope_status"]
            record_curation_event(
                doc,
                action=CURATION_ACTION_GRAPH,
                curator=CURATOR,
                changes=(
                    f"Added {scope_status} causal_graphs entry ({graph_id}) "
                    f"and OPEN CURATION_TODO discussion ({disc_id}) anchored on "
                    "existing verbatim record evidence snippets."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        graphs_added += 1

    for rel_path in COHORT_I_PATHS:
        path = REPO_ROOT / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        graphs = build_cohort_i_graphs(rel_path, doc)
        graph_id = graphs[0]["graph_id"]
        disc = build_cohort_i_discussion(rel_path, doc, graph_id)
        disc_id = disc["discussion_id"]
        existing_disc = doc.get("discussions") or []
        matched = [
            d for d in existing_disc if isinstance(d, dict) and d.get("discussion_id") == disc_id
        ]
        existing_graphs = doc.get("causal_graphs") or []
        source_gap_id = f"{path.stem.replace('_', '-')}-causal-graph-source-gap"
        open_source_gaps = [
            d
            for d in existing_disc
            if isinstance(d, dict)
            and d.get("discussion_id") == source_gap_id
            and (d.get("status") == "OPEN" or d.get("attaches_to") != [f"causal_graphs#{graph_id}"])
        ]
        if existing_graphs == graphs and matched and matched[0] == disc and not open_source_gaps:
            continue
        if (
            len(existing_graphs) == 1
            and existing_graphs[0].get("graph_id") == graph_id
            and matched
            and matched[0].get("kind") == "CURATION_TODO"
            and matched[0].get("attaches_to") == [f"causal_graphs#{graph_id}"]
            and not open_source_gaps
            and (
                (
                    existing_graphs[0].get("scope_status") == "MECHANISTIC"
                    and matched[0].get("status") == "RESOLVED"
                    and matched[0].get("resolution_note")
                )
                or (
                    existing_graphs == graphs
                    and matched[0].get("status") == "OPEN"
                    and matched[0].get("notes")
                )
            )
        ):
            _verify_graph_invariants(rel_path, doc, existing_graphs)
            continue
        _verify_graph_invariants(rel_path, doc, graphs)
        doc["causal_graphs"] = graphs
        for d in existing_disc:
            if isinstance(d, dict) and d.get("discussion_id") == source_gap_id:
                d["status"] = "RESOLVED"
                d["resolved_date"] = POSED_DATE_C6
                d["attaches_to"] = [f"causal_graphs#{graph_id}"]
                d["resolution_note"] = (
                    f"Added connected NONMECHANISTIC causal_graphs entry ({graph_id}) "
                    "anchored on existing verbatim record evidence snippets, and "
                    "tracked the remaining strain-matched UniProtKB protein-example "
                    f"requirement in {disc_id}."
                )
        if matched:
            for idx, d in enumerate(existing_disc):
                if isinstance(d, dict) and d.get("discussion_id") == disc_id:
                    existing_disc[idx] = disc
            doc["discussions"] = existing_disc
        else:
            existing_disc.append(disc)
            doc["discussions"] = existing_disc
            scope_status = graphs[0]["scope_status"]
            record_curation_event(
                doc,
                action=CURATION_ACTION_GRAPH,
                curator=CURATOR,
                changes=(
                    f"Added {scope_status} causal_graphs entry ({graph_id}) "
                    f"and OPEN CURATION_TODO discussion ({disc_id}) anchored on "
                    "existing verbatim record evidence snippets."
                ),
                llm_assisted=True,
            )
        errors = validate_trait(doc)
        if errors:
            raise ValidationFailedError(path, errors)
        if apply:
            write_validated_trait(doc, path)
        graphs_added += 1

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
        f"[{mode}] causal_graphs added: {graphs_added}; "
        f"KNOWLEDGE_GAP discussions added: {gaps_added}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
