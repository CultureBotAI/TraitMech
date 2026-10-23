#!/usr/bin/env python3
"""Curate Stage 3 verified UniProt protein_examples and refresh stale entry_version values.

1. Adds 11 verified, source-backed UniProtKB `protein_examples` across 8 previously
   unexemplified `GENE_OR_PROTEIN` causal nodes in 5 `MECHANISTIC` records whose
   edge/record primary-literature evidence explicitly names the organism and
   experimental protein role:
   - `data/traits/genomics/crispr_cas_system.yaml` (`cas1_cas2_complex`: E. coli K-12
     Cas1 `UniProtKB:Q46896` and Cas2 `UniProtKB:P45956`, `DOI:10.1038/nsmb.2820`)
   - `data/traits/physiology/catalase_activity.yaml` (`oxyr_regulator`: E. coli K-12
     OxyR `UniProtKB:P0ACQ4`, `DOI:10.1073/pnas.96.11.6161`)
   - `data/traits/physiology/quorum_sensing.yaml` (`signal_receptor`: P. aeruginosa
     PAO1 LasR `UniProtKB:P25084` and RhlR `UniProtKB:P54292`, `DOI:10.1128/mbio.01079-17`;
     C. violaceum ATCC 12472 CviR `UniProtKB:Q7NQP7`, `DOI:10.1016/j.molcel.2011.04.003`)
   - `data/traits/physiology/lithotrophic.yaml` (`hydroxylamine_oxidoreductase`:
     N. europaea ATCC 19718 HAO `UniProtKB:Q50925`, `DOI:10.1128/jb.185.9.2759-2773.2003`)
   - `data/traits/morphology/sporulation.yaml` (`sigma_f` `UniProtKB:P07860`,
     `sigma_e` `UniProtKB:P06222`, `sigma_g` `UniProtKB:P19940`, `sigma_k`
     `UniProtKB:P12254` in B. subtilis 168, `DOI:10.1038/s41467-024-51654-6`)
2. Refreshes all 110 `ENTRY_VERSION_MISMATCH` `protein_examples` entries across
   104 `TraitRecord` YAML files to match current live UniProtKB `entry_version`
   values as of `2026-10-22`.
3. In Cycle 2 Stage 3 (`C2S3_COHORT_C_PROMOTIONS` and `C2S3_COHORT_C_BLOCKERS`),
   promotes 8 Cohort C `NONMECHANISTIC` records to `MECHANISTIC` by adding 8
   `InterPro`-grounded `GENE_OR_PROTEIN` nodes with 16 verified UniProtKB
   `protein_examples`, 8 distinct verbatim record-level `evidence` items, 2
   `canonical_examples` entries, and `RESOLVED` `CURATION_TODO` discussions, and
   records Cycle 2 Stage 3 UniProtKB audit blocker notes on the 2 remaining
   `NONMECHANISTIC` Cohort C records (`fumarate_respiration.yaml`,
   `siderophore_production.yaml`).
4. In Cycle 3 Stage 3 (`C3S3_COHORT_E_PROMOTIONS` and `C3S3_COHORT_E_BLOCKERS`),
   promotes 2 Cohort E `NONMECHANISTIC` records (`coagulase_positive.yaml`,
   `pyrazinamidase_activity.yaml`) to `MECHANISTIC` by adding 2
   `InterPro`-grounded `GENE_OR_PROTEIN` nodes with 2 verified reviewed UniProtKB
   `protein_examples` (`UniProtKB:P07767` and `UniProtKB:I6XD65`), 1 distinct
   verbatim record-level `evidence` item, 1 `canonical_examples` entry, and
   `RESOLVED` `CURATION_TODO` discussions, and records a Cycle 3 Stage 3
   UniProtKB audit blocker note on the remaining `NONMECHANISTIC` Cohort E
   record (`indole_test_positive.yaml`).

Default is dry-run; pass `--apply` to write changes via `write_validated_trait`
and `record_curation_event`.

Usage:
    python scripts/curate_stage3_protein_examples.py
    python scripts/curate_stage3_protein_examples.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
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

DO_NOT_WORK_PATH = REPO_ROOT / "DO_NOT_WORK.md"
CURATOR = "claude"
TIMESTAMP = "2026-10-22T01:35:00Z"
RETRIEVED_ON = "2026-10-22"
ACTION_EXAMPLE = "CURATE_PROTEIN_TAXON_EXAMPLE"
ACTION_REFRESH = "REFRESH_UNIPROT_ENTRY_VERSION"

NEW_PROTEIN_EXAMPLES: dict[str, dict[str, Any]] = {
    "data/traits/genomics/crispr_cas_system.yaml": {
        "identifier": "traitmech:000094",
        "graph_id": "crispr_adaptive_immunity",
        "scope_notes": (
            "The protein examples anchor the experimentally resolved S. pyogenes "
            "type II Cas9 interference branch (Q99ZW2) and the E. coli K-12 type I-E "
            "Cas1-Cas2 adaptation complex subunits (Q46896 and P45956). RNA nodes "
            "remain distinct and the subunit examples are not presented as universal "
            "across every CRISPR-Cas type."
        ),
        "nodes": {
            "cas1_cas2_complex": [
                {
                    "uniprot_id": "UniProtKB:Q46896",
                    "protein_label": "CRISPR-associated endonuclease Cas1",
                    "gene_symbol": "ygbT",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000000625",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 154,
                    "sequence_version": 1,
                    "role": (
                        "Cas1 integrase subunit of the E. coli K-12 Cas1-Cas2 "
                        "adaptation complex that captures and integrates new spacers; "
                        "this accession represents the Cas1 subunit, not the complete "
                        "heterohexameric complex."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1038/nsmb.2820",
                            "snippet": (
                                "Cas1 and Cas2 from Escherichia coli form a stable "
                                "complex that is essential for spacer acquisition"
                            ),
                            "notes": (
                                "Nuñez et al. 2014 characterize the E. coli K-12 Cas1-Cas2 "
                                "adaptation complex required for spacer acquisition."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:P45956",
                    "protein_label": "CRISPR-associated endoribonuclease Cas2",
                    "gene_symbol": "ygbF",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000000625",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 145,
                    "sequence_version": 2,
                    "role": (
                        "Cas2 central dimer subunit of the E. coli K-12 Cas1-Cas2 "
                        "adaptation complex required for spacer acquisition; this "
                        "accession represents the Cas2 subunit, not the complete complex."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1038/nsmb.2820",
                            "snippet": (
                                "Cas1 and Cas2 from Escherichia coli form a stable "
                                "complex that is essential for spacer acquisition"
                            ),
                            "notes": (
                                "Nuñez et al. 2014 establish that E. coli K-12 Cas2 forms "
                                "a stable adaptation complex with Cas1 essential for spacer "
                                "acquisition."
                            ),
                        }
                    ],
                },
            ]
        },
        "changes_summary": (
            "Added reviewed E. coli K-12 subunit protein_examples UniProtKB:Q46896 "
            "(Cas1/ygbT, v154) and UniProtKB:P45956 (Cas2/ygbF, v145) on "
            "cas1_cas2_complex (DOI:10.1038/nsmb.2820), updated scope_notes for "
            "component-level subunit scope, and refreshed UniProtKB:Q99ZW2 "
            "entry_version 147 -> 148 on cas9_effector."
        ),
    },
    "data/traits/physiology/catalase_activity.yaml": {
        "identifier": "traitmech:000075",
        "graph_id": "catalase_activity_h2o2_detoxification",
        "scope_notes": (
            "Represents a monofunctional heme-catalase reaction and two alternative "
            "bacterial peroxide-sensing regulators. The S. aureus NCTC 8325 PerR "
            "(Q2G282) and E. coli K-12 OxyR (P0ACQ4) examples support their respective "
            "taxon-specific regulatory branches and are not generalized across all "
            "catalase-positive taxa."
        ),
        "nodes": {
            "oxyr_regulator": [
                {
                    "uniprot_id": "UniProtKB:P0ACQ4",
                    "protein_label": "DNA-binding transcriptional dual regulator OxyR",
                    "gene_symbol": "oxyR",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000000625",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 144,
                    "sequence_version": 1,
                    "role": (
                        "Peroxide-sensing transcriptional dual regulator that is "
                        "directly oxidized and activated by hydrogen peroxide to "
                        "induce katG and peroxide-defense genes in E. coli K-12; "
                        "this example supports the OxyR regulatory branch only, not "
                        "PerR-regulated taxa."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1073/pnas.96.11.6161",
                            "snippet": "In wild-type cells, OxyR is activated by hydrogen peroxide.",
                            "notes": (
                                "Åslund et al. 1999 characterize hydrogen peroxide "
                                "activation of E. coli K-12 OxyR."
                            ),
                        }
                    ],
                }
            ]
        },
        "changes_summary": (
            "Added reviewed E. coli K-12 OxyR protein_example UniProtKB:P0ACQ4 "
            "(v144) on oxyr_regulator (DOI:10.1073/pnas.96.11.6161), updated "
            "scope_notes, and refreshed UniProtKB:Q2G282 entry_version 109 -> 110 "
            "on perr_regulator."
        ),
    },
    "data/traits/physiology/quorum_sensing.yaml": {
        "identifier": "traitmech:000084",
        "graph_id": "quorum_sensing_autoinducer",
        "scope_notes": (
            "This graph is reviewed as the AHL/LuxR branch of quorum sensing "
            "(including P. aeruginosa PAO1 LasR/RhlR positive autoregulation and "
            "C. violaceum CviR receptor antagonism) plus a specific B. thuringiensis "
            "AiiA lactonase interruption mechanism; it does not generalize AiiA or "
            "CviR antagonism to peptide or AI-2 signaling systems."
        ),
        "nodes": {
            "signal_receptor": [
                {
                    "uniprot_id": "UniProtKB:P25084",
                    "protein_label": "Transcriptional activator protein LasR",
                    "gene_symbol": "lasR",
                    "taxon_id": "NCBITaxon:208964",
                    "taxon_label": "Pseudomonas aeruginosa PAO1",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000002438",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 177,
                    "sequence_version": 1,
                    "role": (
                        "LuxR-family 3-oxo-C12-HSL receptor that positively "
                        "autoregulates lasI and downstream quorum-sensing genes in "
                        "P. aeruginosa PAO1."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/mbio.01079-17",
                            "snippet": (
                                "the P. aeruginosa lasI and rhlI genes are positively "
                                "autoregulated by their cognate AHLs and LuxR homologs"
                            ),
                            "notes": (
                                "Supports P. aeruginosa PAO1 LasR as the cognate LuxR "
                                "homolog mediating positive autoregulation of lasI."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:P54292",
                    "protein_label": "Transcriptional regulator RhlR",
                    "gene_symbol": "rhlR",
                    "taxon_id": "NCBITaxon:208964",
                    "taxon_label": "Pseudomonas aeruginosa PAO1",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000002438",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 151,
                    "sequence_version": 1,
                    "role": (
                        "LuxR-family C4-HSL receptor that positively autoregulates "
                        "rhlI and quorum-sensing target genes in P. aeruginosa PAO1."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/mbio.01079-17",
                            "snippet": (
                                "the P. aeruginosa lasI and rhlI genes are positively "
                                "autoregulated by their cognate AHLs and LuxR homologs"
                            ),
                            "notes": (
                                "Supports P. aeruginosa PAO1 RhlR as the cognate LuxR "
                                "homolog mediating positive autoregulation of rhlI."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:Q7NQP7",
                    "protein_label": "Transcriptional activator, LuxR/UhpA family of regulators",
                    "gene_symbol": "cviR",
                    "taxon_id": "NCBITaxon:243365",
                    "taxon_label": "Chromobacterium violaceum ATCC 12472",
                    "entry_status": "UNREVIEWED",
                    "proteome_id": "UP000001424",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 143,
                    "sequence_version": 1,
                    "role": (
                        "LuxR-family AHL receptor CviR that is competitively "
                        "antagonized by small-molecule quorum-sensing inhibitors "
                        "occupying the native autoinducer-binding pocket in "
                        "C. violaceum."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1016/j.molcel.2011.04.003",
                            "snippet": (
                                "CviR from Chromobacterium violaceum is potently "
                                "antagonized by molecules that bind in place of the "
                                "native acylated homoserine lactone autoinducer"
                            ),
                            "notes": (
                                "Chen et al. 2011 characterize small-molecule antagonism "
                                "of Chromobacterium violaceum CviR."
                            ),
                        }
                    ],
                },
            ]
        },
        "changes_summary": (
            "Added LuxR-family receptor protein_examples UniProtKB:P25084 (LasR, v177), "
            "UniProtKB:P54292 (RhlR, v151) in P. aeruginosa PAO1 "
            "(DOI:10.1128/mbio.01079-17) and UniProtKB:Q7NQP7 (CviR, v143) in "
            "C. violaceum ATCC 12472 (DOI:10.1016/j.molcel.2011.04.003) on "
            "signal_receptor, updated scope_notes, and refreshed entry_version on "
            "UniProtKB:P12747 (97 -> 98 on autoinducer_synthase) and "
            "UniProtKB:P0CJ63 (47 -> 48 on quorum_quenching_enzyme)."
        ),
    },
    "data/traits/physiology/lithotrophic.yaml": {
        "identifier": "METPO:1000649",
        "graph_id": "lithotrophic_inorganic_donor_energy",
        "scope_notes": (
            "This cross-donor graph combines hydrogen, sulfur, ammonia, and nitrite "
            "oxidation. The N. europaea ATCC 19718 AmoA (Q04507) and HAO (Q50925) "
            "examples anchor only the bacterial ammonia-to-hydroxylamine-to-nitrite "
            "branch; Q04507 is an alpha-subunit component of a multisubunit ammonia "
            "monooxygenase and neither example represents sulfur, hydrogen, or "
            "nitrite oxidizer systems."
        ),
        "nodes": {
            "hydroxylamine_oxidoreductase": [
                {
                    "uniprot_id": "UniProtKB:Q50925",
                    "protein_label": "Hydroxylamine oxidoreductase",
                    "gene_symbol": "hao1",
                    "taxon_id": "NCBITaxon:228410",
                    "taxon_label": "Nitrosomonas europaea ATCC 19718",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001416",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 155,
                    "sequence_version": 2,
                    "role": (
                        "Multiheme hydroxylamine oxidoreductase (encoded by three "
                        "identical hao gene copies in N. europaea ATCC 19718) that "
                        "oxidizes hydroxylamine to nitrite and feeds electrons into "
                        "the respiratory chain via cytochrome c554."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/jb.185.9.2759-2773.2003",
                            "snippet": (
                                "Electrons from hydroxylamine oxidation flow through "
                                "cytochrome c554 and cytochrome cm552 into the electron "
                                "transport chain at the level of ubiquinone"
                            ),
                            "notes": (
                                "Chain et al. 2003 (complete N. europaea ATCC 19718 "
                                "genome analysis) describe hydroxylamine oxidation to "
                                "nitrite and electron transfer into the ubiquinone pool."
                            ),
                        }
                    ],
                }
            ]
        },
        "changes_summary": (
            "Added reviewed N. europaea ATCC 19718 HAO protein_example "
            "UniProtKB:Q50925 (hao1, v155) on hydroxylamine_oxidoreductase "
            "(DOI:10.1128/jb.185.9.2759-2773.2003), updated scope_notes, and "
            "refreshed UniProtKB:Q04507 entry_version 126 -> 127 on "
            "ammonia_monooxygenase."
        ),
    },
    "data/traits/morphology/sporulation.yaml": {
        "identifier": "METPO:1000870",
        "graph_id": "sporulation_spo0a_sigma_morphogenesis",
        "scope_notes": (
            "The B. subtilis 168 protein examples (SpoIIIE P21458 and "
            "compartment-specific sporulation sigma factors SigF P07860, SigE P06222, "
            "SigG P19940, and SigK P12254) anchor the experimentally resolved Bacillus "
            "endospore morphogenesis cascade; they are not presented as universal "
            "across all endospore-forming Firmicutes."
        ),
        "nodes": {
            "sigma_f": [
                {
                    "uniprot_id": "UniProtKB:P07860",
                    "protein_label": "RNA polymerase sigma-F factor",
                    "gene_symbol": "sigF",
                    "taxon_id": "NCBITaxon:224308",
                    "taxon_label": "Bacillus subtilis 168",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001570",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 175,
                    "sequence_version": 1,
                    "role": (
                        "Early forespore-specific RNA polymerase sigma factor "
                        "(sigma F) activated after asymmetric septation in "
                        "B. subtilis 168."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1038/s41467-024-51654-6",
                            "snippet": (
                                "compartment specific RNA polymerase sigma factors – "
                                "σF and σE – responsible for further activation of "
                                "sporulation genes in the forespore and mother cell "
                                "respectively"
                            ),
                            "notes": (
                                "Supports forespore-specific sigma factor SigF in the "
                                "B. subtilis sporulation cascade."
                            ),
                        }
                    ],
                }
            ],
            "sigma_e": [
                {
                    "uniprot_id": "UniProtKB:P06222",
                    "protein_label": "RNA polymerase sigma-E factor",
                    "gene_symbol": "sigE",
                    "taxon_id": "NCBITaxon:224308",
                    "taxon_label": "Bacillus subtilis 168",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001570",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 173,
                    "sequence_version": 1,
                    "role": (
                        "Early mother-cell-specific RNA polymerase sigma factor "
                        "(sigma E) activated downstream of forespore sigma F in "
                        "B. subtilis 168."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1038/s41467-024-51654-6",
                            "snippet": (
                                "compartment specific RNA polymerase sigma factors – "
                                "σF and σE – responsible for further activation of "
                                "sporulation genes in the forespore and mother cell "
                                "respectively"
                            ),
                            "notes": (
                                "Supports mother-cell-specific sigma factor SigE in the "
                                "B. subtilis sporulation cascade."
                            ),
                        }
                    ],
                }
            ],
            "sigma_g": [
                {
                    "uniprot_id": "UniProtKB:P19940",
                    "protein_label": "RNA polymerase sigma-G factor",
                    "gene_symbol": "sigG",
                    "taxon_id": "NCBITaxon:224308",
                    "taxon_label": "Bacillus subtilis 168",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001570",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 166,
                    "sequence_version": 1,
                    "role": (
                        "Late forespore-specific RNA polymerase sigma factor "
                        "(sigma G) activated after forespore engulfment to drive "
                        "spore maturation and Ssp-mediated DNA protection in "
                        "B. subtilis 168."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1038/s41467-024-51654-6",
                            "snippet": (
                                "the late sporulation spore specific sigma factor σG "
                                "responsible for spore maturation, spore DNA protection "
                                "via Ssp proteins and preparation for germination"
                            ),
                            "notes": (
                                "Supports late forespore sigma factor SigG driving "
                                "spore maturation and DNA protection."
                            ),
                        }
                    ],
                }
            ],
            "sigma_k": [
                {
                    "uniprot_id": "UniProtKB:P12254",
                    "protein_label": "RNA polymerase sigma-K factor",
                    "gene_symbol": "sigK",
                    "taxon_id": "NCBITaxon:224308",
                    "taxon_label": "Bacillus subtilis 168",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001570",
                    "retrieved_on": RETRIEVED_ON,
                    "entry_version": 158,
                    "sequence_version": 2,
                    "role": (
                        "Late mother-cell-specific RNA polymerase sigma factor "
                        "(sigma K) controlling spore coat and cortex maturation in "
                        "B. subtilis 168."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1038/s41467-024-51654-6",
                            "snippet": (
                                "Finally, the late mother cell σK activation, regulated "
                                "by σG, results in spore coat and cortex maturation, "
                                "preparation for germination and eventually, mother "
                                "cell lysis"
                            ),
                            "notes": (
                                "Supports late mother-cell sigma factor SigK driving "
                                "spore coat and cortex maturation."
                            ),
                        }
                    ],
                }
            ],
        },
        "changes_summary": (
            "Added reviewed B. subtilis 168 sporulation sigma-factor protein_examples "
            "UniProtKB:P07860 (SigF, v175), UniProtKB:P06222 (SigE, v173), "
            "UniProtKB:P19940 (SigG, v166), and UniProtKB:P12254 (SigK, v158) across "
            "sigma_f, sigma_e, sigma_g, and sigma_k (DOI:10.1038/s41467-024-51654-6), "
            "updated scope_notes, and refreshed UniProtKB:P21458 entry_version "
            "156 -> 157 on spoiiie_translocase."
        ),
    },
}

ENTRY_VERSION_REFRESHES: list[tuple[str, str, str, str, int | None, int]] = [
    (
        "data/traits/ecology/biofilm_formation.yaml",
        "biofilm_eps_matrix_community",
        "wspR_diguanylate_cyclase",
        "UniProtKB:Q9HXT9",
        152,
        153,
    ),
    (
        "data/traits/ecology/nitrogen_fixing_symbiosis.yaml",
        "rhizobia_legume_n2_fixation",
        "nitrogenase_complex",
        "UniProtKB:P00460",
        158,
        159,
    ),
    (
        "data/traits/environment/arsenic_tolerant.yaml",
        "arsenic_tolerance_ars_efflux",
        "arsC_reductase",
        "UniProtKB:Q1LRL1",
        99,
        100,
    ),
    (
        "data/traits/environment/cadmium_tolerant.yaml",
        "cadmium_tolerance_czc_efflux",
        "czc_efflux_system",
        "UniProtKB:P13511",
        153,
        154,
    ),
    (
        "data/traits/environment/cobalt_tolerant.yaml",
        "cobalt_tolerance_czc_cnr_efflux",
        "czcCBA_complex",
        "UniProtKB:P13511",
        153,
        154,
    ),
    (
        "data/traits/environment/copper_tolerant.yaml",
        "copper_tolerance_cop_efflux",
        "multicopper_oxidase",
        "UniProtKB:Q1LBE6",
        99,
        100,
    ),
    (
        "data/traits/environment/radiotolerant.yaml",
        "radiotolerance_repair_antioxidant",
        "reca_protein",
        "UniProtKB:P42443",
        161,
        162,
    ),
    (
        "data/traits/environment/zinc_tolerant.yaml",
        "zinc_tolerance_czc_efflux",
        "znta_atpase",
        "UniProtKB:Q1LEH0",
        135,
        136,
    ),
    (
        "data/traits/genomics/crispr_cas_system.yaml",
        "crispr_adaptive_immunity",
        "cas9_effector",
        "UniProtKB:Q99ZW2",
        147,
        148,
    ),
    (
        "data/traits/genomics/restriction_modification_system.yaml",
        "rm_self_nonself_defense",
        "restriction_endonuclease",
        "UniProtKB:P44413",
        124,
        125,
    ),
    (
        "data/traits/metabolism/acetogenesis.yaml",
        "acetogenesis_wood_ljungdahl",
        "acetyl_coa_synthase",
        "UniProtKB:P27988",
        125,
        126,
    ),
    (
        "data/traits/metabolism/aerobic_respiration.yaml",
        "aerobic_respiration_terminal_oxidase",
        "cytochrome_c_oxidase",
        "UniProtKB:P08306",
        167,
        168,
    ),
    (
        "data/traits/metabolism/anaerobic_oxidation_of_methane.yaml",
        "aom_anme_sulfate_consortium",
        "mcr",
        "UniProtKB:A0A284VQI9",
        21,
        22,
    ),
    (
        "data/traits/metabolism/anoxygenic_photosynthesis.yaml",
        "anoxygenic_photosynthesis_sulfide_donor",
        "type_ii_reaction_center_m",
        "UniProtKB:P0C0Y9",
        108,
        109,
    ),
    (
        "data/traits/metabolism/biopolymer_degradation.yaml",
        "biopolymer_degradation_extracellular_hydrolysis",
        "endoglucanase",
        "UniProtKB:P07984",
        122,
        123,
    ),
    (
        "data/traits/metabolism/cable_bacteria_metabolism.yaml",
        "cable_bacteria_long_distance_electron_transport",
        "dsrab_complex",
        "UniProtKB:A0A521G566",
        24,
        25,
    ),
    (
        "data/traits/metabolism/cable_bacteria_metabolism.yaml",
        "cable_bacteria_long_distance_electron_transport",
        "dsrab_complex",
        "UniProtKB:A0A521G5H7",
        24,
        25,
    ),
    (
        "data/traits/metabolism/calvin_benson_bassham_cycle.yaml",
        "cbb_rubisco_co2_fixation",
        "rubisco",
        "UniProtKB:P42721",
        153,
        154,
    ),
    (
        "data/traits/metabolism/carbon_fixation.yaml",
        "carbon_fixation_co2_assimilation",
        "rubisco",
        "UniProtKB:P42721",
        153,
        154,
    ),
    (
        "data/traits/metabolism/cellulolysis.yaml",
        "cellulolysis_cellulase_systems",
        "cellobiohydrolase",
        "UniProtKB:P0C2S5",
        80,
        81,
    ),
    (
        "data/traits/metabolism/chitinolysis.yaml",
        "chitinolysis_chitinase",
        "chitinase",
        "UniProtKB:P07254",
        158,
        159,
    ),
    (
        "data/traits/metabolism/chitinolysis.yaml",
        "chitinolysis_chitinase",
        "lpmo",
        "UniProtKB:P9WEM3",
        8,
        9,
    ),
    (
        "data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml",
        "dc_four_hb_anaerobic_archaeal_co2_fixation",
        "pep_carboxylase",
        "UniProtKB:A8A9C2",
        70,
        71,
    ),
    (
        "data/traits/metabolism/disproportionation.yaml",
        "sulfur_disproportionation_redox_split",
        "sor_sulfur_oxygenase_reductase",
        "UniProtKB:P29082",
        101,
        102,
    ),
    (
        "data/traits/metabolism/dissimilatory_iron_reduction.yaml",
        "dir_ferric_iron_respiration",
        "mtrc",
        "UniProtKB:Q8EG34",
        125,
        126,
    ),
    (
        "data/traits/metabolism/dissimilatory_manganese_reduction.yaml",
        "dmr_mn_oxide_respiration",
        "mtrc",
        "UniProtKB:Q8EG34",
        125,
        126,
    ),
    (
        "data/traits/metabolism/dissimilatory_metal_reduction.yaml",
        "metal_reduction_anaerobic_respiration",
        "mtrcab_complex",
        "UniProtKB:Q8EG34",
        125,
        126,
    ),
    (
        "data/traits/metabolism/dissimilatory_nitrate_reduction_to_ammonium.yaml",
        "dnra_nitrate_to_ammonium",
        "nrfa",
        "UniProtKB:Q9S1E5",
        163,
        164,
    ),
    (
        "data/traits/metabolism/dissimilatory_sulfate_reduction.yaml",
        "sulfate_reduction_to_sulfide",
        "dsrab_dsrc",
        "UniProtKB:P45574",
        146,
        147,
    ),
    (
        "data/traits/metabolism/electron_transfer.yaml",
        "electron_transfer_redox_carriers",
        "cytochrome",
        "UniProtKB:Q8EG34",
        125,
        126,
    ),
    (
        "data/traits/metabolism/ethanol_fermentation.yaml",
        "ethanol_fermentation_pyruvate_to_ethanol",
        "pyruvate_decarboxylase",
        "UniProtKB:P06672",
        173,
        174,
    ),
    (
        "data/traits/metabolism/fermentation.yaml",
        "fermentation_redox_energy",
        "pfor",
        "UniProtKB:Q97GY6",
        152,
        153,
    ),
    (
        "data/traits/metabolism/fermentative_hydrogen_production.yaml",
        "fermentative_h2_production",
        "fefe_hydrogenase",
        "UniProtKB:O52683",
        157,
        158,
    ),
    (
        "data/traits/metabolism/homoacetogenesis.yaml",
        "homoacetogenesis_wood_ljungdahl_acetate",
        "acs_codh_complex",
        "UniProtKB:P27988",
        125,
        126,
    ),
    (
        "data/traits/metabolism/lignin_degradation.yaml",
        "lignin_degradation_peroxidase_laccase",
        "laccase",
        "UniProtKB:Q9XAL8",
        131,
        132,
    ),
    (
        "data/traits/metabolism/manganese_oxidation.yaml",
        "manganese_oxidation_multicopper_oxidase",
        "manganese_peroxidase",
        "UniProtKB:Q02567",
        150,
        151,
    ),
    (
        "data/traits/metabolism/metabolism.yaml",
        "metabolism_substrate_to_growth",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/metabolism/methanogenesis.yaml",
        "methanogenesis_c1_reduction",
        "methyl_coenzyme_m_reductase",
        "UniProtKB:Q58256",
        146,
        147,
    ),
    (
        "data/traits/metabolism/mixed_acid_fermentation.yaml",
        "mixed_acid_fermentation_enterobacterial",
        "pyruvate_formate_lyase",
        "UniProtKB:P09373",
        217,
        218,
    ),
    (
        "data/traits/metabolism/nitrogen_fixation.yaml",
        "nitrogen_fixation_nitrogenase",
        "nifh_fe_protein",
        "UniProtKB:P00459",
        167,
        168,
    ),
    (
        "data/traits/metabolism/oxidative_phosphorylation.yaml",
        "oxidative_phosphorylation_chemiosmotic_coupling",
        "heme_copper_oxidase",
        "UniProtKB:P08306",
        167,
        168,
    ),
    (
        "data/traits/metabolism/oxygenic_photosynthesis.yaml",
        "oxygenic_photosynthesis_water_splitting",
        "photosystem_ii",
        "UniProtKB:P16033",
        186,
        187,
    ),
    (
        "data/traits/metabolism/photosynthesis.yaml",
        "photosynthesis_chlorophyll_reaction_center",
        "photosystem_ii",
        "UniProtKB:P16033",
        186,
        187,
    ),
    (
        "data/traits/metabolism/phototrophy.yaml",
        "phototrophy_light_energy_capture",
        "photosystem_ii",
        "UniProtKB:P16033",
        186,
        187,
    ),
    (
        "data/traits/metabolism/propionic_acid_fermentation.yaml",
        "propionic_acid_fermentation_propionate",
        "mmc_carboxytransferase",
        "UniProtKB:Q8GBW6",
        97,
        98,
    ),
    (
        "data/traits/metabolism/proteolysis.yaml",
        "proteolysis_extracellular_protease",
        "extracellular_protease",
        "UniProtKB:P04189",
        189,
        190,
    ),
    (
        "data/traits/metabolism/proteorhodopsin_phototrophy.yaml",
        "proteorhodopsin_light_driven_proton_pump",
        "proteorhodopsin",
        "UniProtKB:Q9F7P4",
        97,
        98,
    ),
    (
        "data/traits/metabolism/reductive_tca_cycle.yaml",
        "rtca_reverse_tricarboxylic_acid_co2_fixation",
        "atp_citrate_lyase",
        "UniProtKB:Q8KDG1",
        117,
        118,
    ),
    (
        "data/traits/metabolism/reductive_tca_cycle.yaml",
        "rtca_reverse_tricarboxylic_acid_co2_fixation",
        "atp_citrate_lyase",
        "UniProtKB:Q8KDG2",
        117,
        118,
    ),
    (
        "data/traits/metabolism/respiration.yaml",
        "respiration_electron_acceptor_energy_conservation",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/metabolism/starch_degradation.yaml",
        "starch_degradation_amylase",
        "amylase",
        "UniProtKB:P06278",
        173,
        174,
    ),
    (
        "data/traits/metabolism/substrate_level_phosphorylation.yaml",
        "substrate_level_phosphorylation_direct_atp",
        "carbamate_kinase_arginine_deiminase",
        "UniProtKB:Q99YT9",
        146,
        147,
    ),
    (
        "data/traits/metabolism/syntrophy.yaml",
        "syntrophy_interspecies_electron_transfer",
        "butyryl_coa_dehydrogenase",
        "UniProtKB:Q0AVM4",
        94,
        95,
    ),
    (
        "data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml",
        "three_hp_four_hb_sulfolobales",
        "acetyl_propionyl_coa_carboxylase",
        "UniProtKB:A4YGI1",
        85,
        86,
    ),
    (
        "data/traits/metabolism/wood_ljungdahl_pathway.yaml",
        "wood_ljungdahl_reductive_acetyl_coa",
        "acetyl_coa_synthase",
        "UniProtKB:P27988",
        125,
        126,
    ),
    (
        "data/traits/metabolism/xylan_degradation.yaml",
        "xylan_degradation_xylanase",
        "xylanase",
        "UniProtKB:P23556",
        101,
        102,
    ),
    (
        "data/traits/morphology/brown_pigmented.yaml",
        "brown_pigmented_pyomelanin_pathway",
        "hppD",
        "UniProtKB:A0AAE7AGQ2",
        8,
        9,
    ),
    (
        "data/traits/morphology/carboxysome.yaml",
        "carboxysome_co2_concentrating",
        "bmc_shell_proteins",
        "UniProtKB:Q03511",
        110,
        111,
    ),
    (
        "data/traits/morphology/ellipsoidal.yaml",
        "ellipsoidal_ovococcal_elongation",
        "pbp2b",
        "UniProtKB:P0A3M6",
        110,
        111,
    ),
    (
        "data/traits/morphology/gas_vesicle.yaml",
        "gas_vesicle_buoyancy",
        "gvpa_protein",
        "UniProtKB:B0JPK6",
        76,
        77,
    ),
    (
        "data/traits/morphology/heterocyst.yaml",
        "heterocyst_microoxic_nitrogen_fixation",
        "hetr_regulator",
        "UniProtKB:P27709",
        120,
        121,
    ),
    (
        "data/traits/morphology/magnetosome.yaml",
        "magnetosome_magnetotaxis",
        "mamk_protein",
        "UniProtKB:Q6NE59",
        86,
        87,
    ),
    (
        "data/traits/morphology/motile.yaml",
        "motile_energy_dependent_locomotion",
        "chey_response_regulator",
        "UniProtKB:P0AE67",
        160,
        161,
    ),
    (
        "data/traits/morphology/oval_shaped.yaml",
        "oval_shaped_ovococcal_pg_synthesis",
        "pbp2b",
        "UniProtKB:P0A3M6",
        110,
        111,
    ),
    (
        "data/traits/morphology/ovoid_shaped.yaml",
        "ovoid_shaped_midcell_pg_assembly",
        "roda_pbp2b",
        "UniProtKB:P0A3M6",
        110,
        111,
    ),
    (
        "data/traits/morphology/polyhydroxyalkanoate_granule.yaml",
        "pha_granule_carbon_energy_storage",
        "pha_synthase_phac",
        "UniProtKB:P23608",
        137,
        138,
    ),
    (
        "data/traits/morphology/polyphosphate_granule.yaml",
        "polyphosphate_granule_storage",
        "ppk",
        "UniProtKB:F5XF46",
        69,
        70,
    ),
    (
        "data/traits/morphology/spore_forming.yaml",
        "spore_forming_endospore_assembly",
        "spo0a_phosphorylated",
        "UniProtKB:P06534",
        188,
        189,
    ),
    (
        "data/traits/morphology/spore_shaped.yaml",
        "spore_shaped_endospore_layers",
        "spoiva_protein",
        "UniProtKB:P35149",
        134,
        135,
    ),
    (
        "data/traits/morphology/sporulation.yaml",
        "sporulation_spo0a_sigma_morphogenesis",
        "spoiiie_translocase",
        "UniProtKB:P21458",
        156,
        157,
    ),
    (
        "data/traits/morphology/tailed_shaped.yaml",
        "tailed_shaped_polar_stalk_growth",
        "mreb",
        "UniProtKB:A0A0H3C7V4",
        42,
        43,
    ),
    (
        "data/traits/morphology/twitching_motility.yaml",
        "twitching_type_iv_pilus_retraction",
        "pilt_retraction_atpase",
        "UniProtKB:P24559",
        147,
        148,
    ),
    (
        "data/traits/physiology/antibiotic_resistance.yaml",
        "antibiotic_resistance_mechanisms",
        "beta_lactamase",
        "UniProtKB:P00807",
        171,
        172,
    ),
    (
        "data/traits/physiology/autotrophic.yaml",
        "autotrophic_inorganic_carbon_fixation",
        "rubisco",
        "UniProtKB:P42721",
        153,
        154,
    ),
    (
        "data/traits/physiology/bioluminescence.yaml",
        "bioluminescence_luciferase",
        "lux_i",
        "UniProtKB:P12747",
        97,
        98,
    ),
    (
        "data/traits/physiology/carboxydotrophic.yaml",
        "carboxydotrophic_co_oxidation",
        "nife_codh",
        "UniProtKB:P31896",
        None,
        134,
    ),
    (
        "data/traits/physiology/catalase_activity.yaml",
        "catalase_activity_h2o2_detoxification",
        "perr_regulator",
        "UniProtKB:Q2G282",
        109,
        110,
    ),
    (
        "data/traits/physiology/chemoautolithotrophic.yaml",
        "chemoautolithotrophic_inorganic_energy_co2_fixation",
        "ammonia_monooxygenase",
        "UniProtKB:Q04507",
        126,
        127,
    ),
    (
        "data/traits/physiology/chemoautotrophic.yaml",
        "chemoautotrophic_chemical_energy_co2_fixation",
        "rubisco",
        "UniProtKB:Q82TG6",
        120,
        121,
    ),
    (
        "data/traits/physiology/chemolithoautotrophic.yaml",
        "chemolithoautotrophic_energy_and_fixation",
        "rubisco",
        "UniProtKB:P0C916",
        57,
        58,
    ),
    (
        "data/traits/physiology/chemolithotrophic.yaml",
        "chemolithotrophic_inorganic_oxidation",
        "ammonia_monooxygenase",
        "UniProtKB:Q04507",
        126,
        127,
    ),
    (
        "data/traits/physiology/chemoorganoheterotrophic.yaml",
        "chemoorganoheterotrophic_organic_energy_carbon",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/physiology/chemoorganotrophic.yaml",
        "chemoorganotrophic_organic_oxidation_energy",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/physiology/chemotaxis.yaml",
        "chemotaxis_gradient_response",
        "chey",
        "UniProtKB:P0AE67",
        160,
        161,
    ),
    (
        "data/traits/physiology/chemotrophic.yaml",
        "chemotrophic_chemical_redox_energy",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/physiology/dormancy.yaml",
        "dormancy_seed_bank",
        "rpf_proteins",
        "UniProtKB:P9WG29",
        53,
        54,
    ),
    (
        "data/traits/physiology/heterotrophic.yaml",
        "heterotrophic_organic_carbon_assimilation",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/physiology/hydrogenotrophic.yaml",
        "hydrogenotrophic_hydrogen_oxidation_fixation",
        "hydrogenase",
        "UniProtKB:P31891",
        None,
        156,
    ),
    (
        "data/traits/physiology/lithoautotrophic.yaml",
        "lithoautotrophic_inorganic_donor_co2_fixation",
        "rubisco",
        "UniProtKB:Q82TG6",
        120,
        121,
    ),
    (
        "data/traits/physiology/lithotrophic.yaml",
        "lithotrophic_inorganic_donor_energy",
        "ammonia_monooxygenase",
        "UniProtKB:Q04507",
        126,
        127,
    ),
    (
        "data/traits/physiology/methanotrophic.yaml",
        "methanotrophic_methane_oxidation",
        "particulate_methane_monooxygenase",
        "UniProtKB:G1UBD1",
        76,
        77,
    ),
    (
        "data/traits/physiology/methylotrophic.yaml",
        "methylotrophic_methanol_assimilation",
        "mxa_methanol_dehydrogenase",
        "UniProtKB:P16027",
        179,
        180,
    ),
    (
        "data/traits/physiology/mixotrophic.yaml",
        "mixotrophic_dual_carbon_energy_use",
        "rubisco",
        "UniProtKB:A1B2Q2",
        98,
        99,
    ),
    (
        "data/traits/physiology/natural_competence.yaml",
        "natural_competence_dna_uptake",
        "reca",
        "UniProtKB:P0A452",
        116,
        117,
    ),
    (
        "data/traits/physiology/organoheterotrophic.yaml",
        "organoheterotrophic_organic_donor_carbon",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/physiology/organotrophic.yaml",
        "organotrophic_organic_compound_oxidation",
        "atp_synthase",
        "UniProtKB:P0ABB4",
        155,
        156,
    ),
    (
        "data/traits/physiology/oxidase_activity.yaml",
        "oxidase_activity_terminal_oxidase",
        "family_a_cytochrome_c_oxidase",
        "UniProtKB:P08305",
        132,
        133,
    ),
    (
        "data/traits/physiology/oxidative_stress_response.yaml",
        "oxidative_stress_response_ros_defense",
        "oxyr_regulator",
        "UniProtKB:P0ACQ4",
        143,
        144,
    ),
    (
        "data/traits/physiology/persister_cell_formation.yaml",
        "persister_dormancy_tolerance",
        "hipa_toxin",
        "UniProtKB:P23874",
        176,
        177,
    ),
    (
        "data/traits/physiology/photoautotrophic.yaml",
        "photoautotrophic_cyanobacterial_carbon_fixation",
        "photosystem_ii",
        "UniProtKB:P16033",
        186,
        187,
    ),
    (
        "data/traits/physiology/photoheterotrophic.yaml",
        "photoheterotrophic_light_organic_carbon",
        "photosynthetic_reaction_center",
        "UniProtKB:P10717",
        119,
        120,
    ),
    (
        "data/traits/physiology/photolithoautotrophic.yaml",
        "photolithoautotrophic_light_inorganic_donor_fixation",
        "rubisco",
        "UniProtKB:Q31NB3",
        112,
        113,
    ),
    (
        "data/traits/physiology/photolithotrophic.yaml",
        "photolithotrophic_inorganic_electron_donors",
        "photosynthetic_reaction_center",
        "UniProtKB:Q8KEP5",
        84,
        85,
    ),
    (
        "data/traits/physiology/photoorganoheterotrophic.yaml",
        "photoorganoheterotrophic_light_organic_electrons",
        "photosynthetic_reaction_center",
        "UniProtKB:P10717",
        119,
        120,
    ),
    (
        "data/traits/physiology/phototrophic.yaml",
        "phototrophic_light_energy_capture",
        "photosynthetic_reaction_center",
        "UniProtKB:P10717",
        119,
        120,
    ),
    (
        "data/traits/physiology/quorum_sensing.yaml",
        "quorum_sensing_autoinducer",
        "autoinducer_synthase",
        "UniProtKB:P12747",
        97,
        98,
    ),
    (
        "data/traits/physiology/quorum_sensing.yaml",
        "quorum_sensing_autoinducer",
        "quorum_quenching_enzyme",
        "UniProtKB:P0CJ63",
        47,
        48,
    ),
    (
        "data/traits/physiology/stress_response.yaml",
        "stress_response_induction",
        "rpos",
        "UniProtKB:P13445",
        207,
        208,
    ),
    (
        "data/traits/physiology/urease_activity.yaml",
        "urease_activity_urea_hydrolysis",
        "urease",
        "UniProtKB:P41020",
        152,
        153,
    ),
    (
        "data/traits/physiology/urease_activity.yaml",
        "urease_activity_urea_hydrolysis",
        "urease",
        "UniProtKB:P41021",
        127,
        128,
    ),
    (
        "data/traits/physiology/urease_activity.yaml",
        "urease_activity_urea_hydrolysis",
        "urease",
        "UniProtKB:P41022",
        129,
        130,
    ),
    (
        "data/traits/physiology/viable_but_nonculturable_state.yaml",
        "vbnc_stress_induced_dormancy",
        "rpos",
        "UniProtKB:P13445",
        207,
        208,
    ),
]

C2S3_TIMESTAMP = "2026-10-23T11:45:00Z"
C2S3_RETRIEVED_ON = "2026-10-23"
ACTION_DISCUSSION = "RECORD_CURATION_DISCUSSION"

C2S3_COHORT_C_PROMOTIONS: dict[str, dict[str, Any]] = {
    "data/traits/metabolism/arsenate_respiration.yaml": {
        "identifier": "traitmech:000195",
        "graph_id": "arsenate_respiration_arr_pathway_sketch",
        "discussion_id": "arsenate-respiration-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1073/pnas.1834303100, "
            "DOI:10.1128/AEM.69.5.2800-2809.2003, and DOI:10.1128/JB.01110-07; "
            "exemplified on arsenate_respiration_arr_complex with Shewanella sp. "
            "ANA-3 (NCBITaxon:94122) respiratory arsenate reductase subunits ArrA "
            "(UniProtKB:Q7WTU0) and ArrB (UniProtKB:Q7WTT9)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1128/JB.01110-07",
            "snippet": (
                "ARR is a heterodimer of approximately 131 kDa, composed of one "
                "ArrA subunit (approximately 95 kDa) and one ArrB subunit "
                "(approximately 27 kDa)."
            ),
            "notes": (
                "Malasarn et al. show that Shewanella sp. strain ANA-3 arsenate "
                "respiratory reductase (ARR) is a heterodimer composed of one "
                "ArrA subunit and one ArrB subunit."
            ),
        },
        "new_node": {
            "node_id": "arsenate_respiration_arr_complex",
            "label": "arsenate respiratory reductase ArrAB",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR053686",
            "gene_symbols": ["arrA", "arrB"],
            "operon": "arrAB",
            "description": (
                "Heterodimeric respiratory arsenate reductase complex (ArrAB) "
                "catalyzing dissimilatory As(V) reduction in Shewanella sp. ANA-3."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:Q7WTU0",
                    "protein_label": "Arsenate respiratory reductase molybdopterin-containing subunit ArrA",
                    "gene_symbol": "arrA",
                    "taxon_id": "NCBITaxon:94122",
                    "taxon_label": "Shewanella sp. ANA-3",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 148,
                    "sequence_version": 1,
                    "role": (
                        "ArrA is the catalytic molybdopterin-containing subunit of "
                        "the heterodimeric ArrAB respiratory arsenate reductase "
                        "complex in Shewanella sp. ANA-3; this accession represents "
                        "the ArrA subunit rather than the full heterodimer."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/JB.01110-07",
                            "snippet": (
                                "ARR is a heterodimer of approximately 131 kDa, composed "
                                "of one ArrA subunit (approximately 95 kDa) and one ArrB "
                                "subunit (approximately 27 kDa)."
                            ),
                            "notes": (
                                "Malasarn et al. purify and characterize the Shewanella "
                                "sp. strain ANA-3 heterodimeric arsenate respiratory "
                                "reductase composed of ArrA and ArrB."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:Q7WTT9",
                    "protein_label": "Arsenate respiratory reductase iron-sulfur subunit ArrB",
                    "gene_symbol": "arrB",
                    "taxon_id": "NCBITaxon:94122",
                    "taxon_label": "Shewanella sp. ANA-3",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 141,
                    "sequence_version": 1,
                    "role": (
                        "ArrB is the iron-sulfur electron-transfer subunit of the "
                        "heterodimeric ArrAB respiratory arsenate reductase complex "
                        "in Shewanella sp. ANA-3; this accession represents the ArrB "
                        "subunit rather than the full heterodimer."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/JB.01110-07",
                            "snippet": (
                                "ARR is a heterodimer of approximately 131 kDa, composed "
                                "of one ArrA subunit (approximately 95 kDa) and one ArrB "
                                "subunit (approximately 27 kDa)."
                            ),
                            "notes": (
                                "Malasarn et al. purify and characterize the Shewanella "
                                "sp. strain ANA-3 heterodimeric arsenate respiratory "
                                "reductase composed of ArrA and ArrB."
                            ),
                        }
                    ],
                },
            ],
        },
        "new_edge": {
            "subject": "arsenate_respiration_arr_complex",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "arsenate_respiration_reductase_activity",
            "description": (
                "The heterodimeric ArrAB respiratory arsenate reductase complex "
                "enables dissimilatory arsenate reductase activity in Shewanella sp. ANA-3."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/JB.01110-07",
                    "snippet": (
                        "ARR is a heterodimer of approximately 131 kDa, composed "
                        "of one ArrA subunit (approximately 95 kDa) and one ArrB "
                        "subunit (approximately 27 kDa)."
                    ),
                    "notes": (
                        "Malasarn et al. show that Shewanella sp. strain ANA-3 "
                        "arsenate respiratory reductase (ARR) is a heterodimer "
                        "of ArrA and ArrB."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Promoted arsenate_respiration_arr_pathway_sketch to MECHANISTIC by "
                "adding InterPro:IPR053686-grounded GENE_OR_PROTEIN node "
                "arsenate_respiration_arr_complex with reviewed Shewanella sp. ANA-3 "
                "(NCBITaxon:94122) protein_examples UniProtKB:Q7WTU0 (ArrA) and "
                "UniProtKB:Q7WTT9 (ArrB) backed by DOI:10.1128/JB.01110-07."
            ),
        },
        "changes_summary": (
            "Promoted arsenate_respiration_arr_pathway_sketch to MECHANISTIC; added "
            "InterPro:IPR053686-grounded GENE_OR_PROTEIN node arsenate_respiration_arr_complex "
            "with reviewed Shewanella sp. ANA-3 (NCBITaxon:94122) protein_examples "
            "UniProtKB:Q7WTU0 (ArrA) and UniProtKB:Q7WTT9 (ArrB) backed by "
            "DOI:10.1128/JB.01110-07; resolved arsenate-respiration-protein-example-gap."
        ),
    },
    "data/traits/metabolism/chlorate_respiration.yaml": {
        "identifier": "traitmech:000198",
        "graph_id": "chlorate_respiration_pathway_sketch",
        "discussion_id": "chlorate-respiration-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1128/AEM.69.9.5585-5592.2003 and "
            "DOI:10.1128/AEM.07303-11; exemplified on chlorate_respiration_clr_complex "
            "with Ideonella dechloratans (NCBITaxon:36863) chlorate reductase "
            "subunits ClrA (UniProtKB:P60068) and ClrB (UniProtKB:P60069)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1128/AEM.69.9.5585-5592.2003",
            "snippet": (
                "The genes (clr) encoding chlorate reductase are arranged as "
                "clrABDC, where clrA, clrB, and clrC encode the subunits and clrD "
                "encodes a specific chaperone."
            ),
            "notes": (
                "Danielsson Thorell et al. characterize the Ideonella dechloratans "
                "clrABDC operon encoding the ClrA, ClrB, and ClrC subunits of "
                "chlorate reductase."
            ),
        },
        "new_node": {
            "node_id": "chlorate_respiration_clr_complex",
            "label": "chlorate reductase ClrABC",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR017840",
            "gene_symbols": ["clrA", "clrB", "clrC"],
            "operon": "clrABDC",
            "description": (
                "Periplasmic heterotrimeric chlorate reductase complex (ClrABC) "
                "catalyzing the reduction of chlorate to chlorite."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:P60068",
                    "protein_label": "Chlorate reductase subunit alpha",
                    "gene_symbol": "clrA",
                    "taxon_id": "NCBITaxon:36863",
                    "taxon_label": "Ideonella dechloratans",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 85,
                    "sequence_version": 1,
                    "role": (
                        "ClrA is the catalytic molybdopterin-containing alpha "
                        "subunit of the heterotrimeric ClrABC chlorate reductase "
                        "complex in Ideonella dechloratans; this accession represents "
                        "the alpha subunit rather than the full heterotrimer."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/AEM.69.9.5585-5592.2003",
                            "snippet": (
                                "The genes (clr) encoding chlorate reductase are "
                                "arranged as clrABDC, where clrA, clrB, and clrC "
                                "encode the subunits and clrD encodes a specific "
                                "chaperone."
                            ),
                            "notes": (
                                "Danielsson Thorell et al. clone and sequence the "
                                "Ideonella dechloratans clrABDC operon encoding "
                                "chlorate reductase subunits ClrA, ClrB, and ClrC."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:P60069",
                    "protein_label": "Chlorate reductase subunit beta",
                    "gene_symbol": "clrB",
                    "taxon_id": "NCBITaxon:36863",
                    "taxon_label": "Ideonella dechloratans",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 77,
                    "sequence_version": 1,
                    "role": (
                        "ClrB is the iron-sulfur beta subunit of the heterotrimeric "
                        "ClrABC chlorate reductase complex in Ideonella dechloratans; "
                        "this accession represents the beta subunit rather than the "
                        "full heterotrimer."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/AEM.69.9.5585-5592.2003",
                            "snippet": (
                                "The genes (clr) encoding chlorate reductase are "
                                "arranged as clrABDC, where clrA, clrB, and clrC "
                                "encode the subunits and clrD encodes a specific "
                                "chaperone."
                            ),
                            "notes": (
                                "Danielsson Thorell et al. clone and sequence the "
                                "Ideonella dechloratans clrABDC operon encoding "
                                "chlorate reductase subunits ClrA, ClrB, and ClrC."
                            ),
                        }
                    ],
                },
            ],
        },
        "new_edge": {
            "subject": "chlorate_respiration_clr_complex",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "chlorate_respiration_dissimilatory_pathway",
            "description": (
                "The clrABDC-encoded ClrABC chlorate reductase complex enables "
                "the dissimilatory chlorate reduction pathway in Ideonella dechloratans."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/AEM.69.9.5585-5592.2003",
                    "snippet": (
                        "The genes (clr) encoding chlorate reductase are arranged "
                        "as clrABDC, where clrA, clrB, and clrC encode the subunits "
                        "and clrD encodes a specific chaperone."
                    ),
                    "notes": (
                        "Danielsson Thorell et al. identify the Ideonella "
                        "dechloratans clrABDC gene cluster encoding the ClrABC "
                        "chlorate reductase subunits."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Promoted chlorate_respiration_pathway_sketch to MECHANISTIC by "
                "adding InterPro:IPR017840-grounded GENE_OR_PROTEIN node "
                "chlorate_respiration_clr_complex with reviewed Ideonella "
                "dechloratans (NCBITaxon:36863) protein_examples UniProtKB:P60068 "
                "(ClrA) and UniProtKB:P60069 (ClrB) backed by "
                "DOI:10.1128/AEM.69.9.5585-5592.2003."
            ),
        },
        "changes_summary": (
            "Promoted chlorate_respiration_pathway_sketch to MECHANISTIC; added "
            "InterPro:IPR017840-grounded GENE_OR_PROTEIN node chlorate_respiration_clr_complex "
            "with reviewed Ideonella dechloratans (NCBITaxon:36863) protein_examples "
            "UniProtKB:P60068 (ClrA) and UniProtKB:P60069 (ClrB) backed by "
            "DOI:10.1128/AEM.69.9.5585-5592.2003; resolved chlorate-respiration-protein-example-gap."
        ),
    },
    "data/traits/metabolism/dimethyl_sulfoxide_respiration.yaml": {
        "identifier": "traitmech:000201",
        "graph_id": "dmso_respiration_reductase_sketch",
        "discussion_id": "dimethyl-sulfoxide-respiration-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1073/pnas.0505959103 and "
            "DOI:10.1111/1462-2920.15971; exemplified on dmso_respiration_dms_complex "
            "with Shewanella oneidensis MR-1 (NCBITaxon:211586; UP000008186) "
            "extracellular DMSO reductase subunits DmsA (UniProtKB:Q8EH03) and "
            "DmsB (UniProtKB:Q8EH02)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1073/pnas.0505959103",
            "snippet": (
                "Here, we identify two gene clusters in Shewanella oneidensis "
                "strain MR-1 that each contain homologs of genes required for "
                "metal reduction and genes that are predicted to encode dimethyl "
                "sulfoxide (DMSO) reductase subunits."
            ),
            "notes": (
                "Gralnick et al. identify the Shewanella oneidensis MR-1 gene "
                "clusters encoding the extracellular dimethyl sulfoxide reductase "
                "subunits."
            ),
        },
        "new_node": {
            "node_id": "dmso_respiration_dms_complex",
            "label": "extracellular DMSO reductase DmsEFAB",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR011888",
            "gene_symbols": ["dmsE", "dmsF", "dmsA", "dmsB"],
            "description": (
                "Extracellular dimethyl sulfoxide reductase complex encoded within "
                "the SO1427-SO1432 gene cluster."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:Q8EH03",
                    "protein_label": (
                        "Extracellular dimethyl sulfoxide/manganese oxide reductase "
                        "molybdopterin-binding subunit DmsA"
                    ),
                    "gene_symbol": "dmsA",
                    "taxon_id": "NCBITaxon:211586",
                    "taxon_label": "Shewanella oneidensis MR-1",
                    "entry_status": "UNREVIEWED",
                    "proteome_id": "UP000008186",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 148,
                    "sequence_version": 1,
                    "role": (
                        "DmsA (SO_1429) is the catalytic molybdopterin-binding "
                        "subunit encoded within the SO1427-SO1432 extracellular "
                        "DMSO reductase gene cluster in Shewanella oneidensis MR-1; "
                        "this accession represents the DmsA subunit rather than the "
                        "full multi-subunit complex."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1073/pnas.0505959103",
                            "snippet": "one (SO1427-SO1432) is required for anaerobic respiration of DMSO",
                            "notes": (
                                "Gralnick et al. show that the Shewanella oneidensis "
                                "MR-1 SO1427-SO1432 gene cluster encoding DmsEFAB "
                                "is required for anaerobic respiration of DMSO."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:Q8EH02",
                    "protein_label": (
                        "Extracellular dimethyl sulfoxide/manganese oxide reductase "
                        "ferredoxin subunit DmsB"
                    ),
                    "gene_symbol": "dmsB",
                    "taxon_id": "NCBITaxon:211586",
                    "taxon_label": "Shewanella oneidensis MR-1",
                    "entry_status": "UNREVIEWED",
                    "proteome_id": "UP000008186",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 136,
                    "sequence_version": 1,
                    "role": (
                        "DmsB (SO_1430) is the iron-sulfur ferredoxin subunit "
                        "encoded within the SO1427-SO1432 extracellular DMSO "
                        "reductase gene cluster in Shewanella oneidensis MR-1; this "
                        "accession represents the DmsB subunit rather than the full "
                        "multi-subunit complex."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1073/pnas.0505959103",
                            "snippet": "one (SO1427-SO1432) is required for anaerobic respiration of DMSO",
                            "notes": (
                                "Gralnick et al. show that the Shewanella oneidensis "
                                "MR-1 SO1427-SO1432 gene cluster encoding DmsEFAB "
                                "is required for anaerobic respiration of DMSO."
                            ),
                        }
                    ],
                },
            ],
        },
        "new_edge": {
            "subject": "dmso_respiration_dms_complex",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "dmso_respiration_reductase_activity",
            "description": (
                "The extracellular DmsEFAB DMSO reductase complex enables "
                "dimethyl-sulfoxide reductase activity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1073/pnas.0505959103",
                    "snippet": (
                        "Here, we identify two gene clusters in Shewanella "
                        "oneidensis strain MR-1 that each contain homologs of "
                        "genes required for metal reduction and genes that are "
                        "predicted to encode dimethyl sulfoxide (DMSO) reductase "
                        "subunits."
                    ),
                    "notes": (
                        "Gralnick et al. identify the Shewanella oneidensis MR-1 "
                        "gene clusters encoding the DMSO reductase subunits."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Promoted dmso_respiration_reductase_sketch to MECHANISTIC by "
                "adding InterPro:IPR011888-grounded GENE_OR_PROTEIN node "
                "dmso_respiration_dms_complex with Shewanella oneidensis MR-1 "
                "(NCBITaxon:211586; UP000008186) protein_examples UniProtKB:Q8EH03 "
                "(DmsA) and UniProtKB:Q8EH02 (DmsB) backed by DOI:10.1073/pnas.0505959103."
            ),
        },
        "changes_summary": (
            "Promoted dmso_respiration_reductase_sketch to MECHANISTIC; added "
            "InterPro:IPR011888-grounded GENE_OR_PROTEIN node dmso_respiration_dms_complex "
            "with Shewanella oneidensis MR-1 (NCBITaxon:211586; UP000008186) "
            "protein_examples UniProtKB:Q8EH03 (DmsA) and UniProtKB:Q8EH02 (DmsB) "
            "backed by DOI:10.1073/pnas.0505959103; resolved "
            "dimethyl-sulfoxide-respiration-protein-example-gap."
        ),
    },
    "data/traits/metabolism/perchlorate_respiration.yaml": {
        "identifier": "traitmech:000197",
        "graph_id": "perchlorate_respiration_reduction_sketch",
        "discussion_id": "perchlorate-respiration-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1186/s12864-015-2011-5, "
            "DOI:10.1128/AEM.05758-11, and DOI:10.1128/jb.187.15.5090-5096.2005; "
            "exemplified on perchlorate_respiration_pcr_reductase with Dechloromonas "
            "aromatica RCB (NCBITaxon:159087) perchlorate reductase subunit alpha "
            "PcrA (UniProtKB:Q47CW6)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1128/jb.187.15.5090-5096.2005",
            "snippet": (
                "Deletion of the pcrA gene in Dechloromonas aromatica abolished "
                "growth in both perchlorate and chlorate but not growth in nitrate, "
                "indicating that the pcrABCD genes play a functional role in "
                "perchlorate reduction separate from nitrate reduction."
            ),
            "notes": (
                "Bender et al. demonstrate that the pcrABCD perchlorate reductase "
                "genes are required for anaerobic growth on perchlorate in "
                "Dechloromonas aromatica RCB."
            ),
        },
        "new_canonical_example": {
            "taxon_id": "NCBITaxon:159087",
            "taxon_label": "Dechloromonas aromatica RCB",
            "note": (
                "Bender et al. characterized the pcrABCD perchlorate reductase "
                "genes in Dechloromonas aromatica RCB and showed that pcrA deletion "
                "abolishes anaerobic growth on perchlorate and chlorate."
            ),
            "reference": "DOI:10.1128/jb.187.15.5090-5096.2005",
        },
        "new_node": {
            "node_id": "perchlorate_respiration_pcr_reductase",
            "label": "perchlorate reductase PcrABCD",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR017840",
            "gene_symbols": ["pcrA", "pcrB", "pcrC", "pcrD"],
            "description": (
                "Periplasmic perchlorate reductase enzyme complex (PcrABCD) "
                "required for respiratory perchlorate reduction."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:Q47CW6",
                    "protein_label": "Perchlorate reductase subunit alpha",
                    "gene_symbol": "pcrA",
                    "taxon_id": "NCBITaxon:159087",
                    "taxon_label": "Dechloromonas aromatica RCB",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 106,
                    "sequence_version": 1,
                    "role": (
                        "PcrA is the catalytic molybdopterin-containing alpha "
                        "subunit of perchlorate reductase required for anaerobic "
                        "growth on perchlorate in Dechloromonas aromatica RCB; this "
                        "accession represents the PcrA subunit of the PcrABCD complex."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/jb.187.15.5090-5096.2005",
                            "snippet": (
                                "Deletion of the pcrA gene in Dechloromonas aromatica "
                                "abolished growth in both perchlorate and chlorate but "
                                "not growth in nitrate, indicating that the pcrABCD "
                                "genes play a functional role in perchlorate reduction "
                                "separate from nitrate reduction."
                            ),
                            "notes": (
                                "Bender et al. show that deleting pcrA in Dechloromonas "
                                "aromatica RCB abolishes anaerobic growth on perchlorate."
                            ),
                        }
                    ],
                }
            ],
        },
        "new_edge": {
            "subject": "perchlorate_respiration_pcr_reductase",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "perchlorate_respiration_perchlorate_reduction",
            "description": (
                "The pcrABCD-encoded perchlorate reductase complex enables "
                "anaerobic respiratory perchlorate reduction."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.187.15.5090-5096.2005",
                    "snippet": (
                        "Deletion of the pcrA gene in Dechloromonas aromatica "
                        "abolished growth in both perchlorate and chlorate but not "
                        "growth in nitrate, indicating that the pcrABCD genes play "
                        "a functional role in perchlorate reduction separate from "
                        "nitrate reduction."
                    ),
                    "notes": (
                        "Bender et al. demonstrate that pcrABCD is required for "
                        "perchlorate reduction in Dechloromonas aromatica RCB."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Added canonical_examples entry Dechloromonas aromatica RCB "
                "(NCBITaxon:159087) and promoted perchlorate_respiration_reduction_sketch "
                "to MECHANISTIC by adding InterPro:IPR017840-grounded GENE_OR_PROTEIN "
                "node perchlorate_respiration_pcr_reductase with reviewed "
                "UniProtKB:Q47CW6 (PcrA) backed by DOI:10.1128/jb.187.15.5090-5096.2005."
            ),
        },
        "changes_summary": (
            "Added Dechloromonas aromatica RCB (NCBITaxon:159087; "
            "DOI:10.1128/jb.187.15.5090-5096.2005) canonical example; promoted "
            "perchlorate_respiration_reduction_sketch to MECHANISTIC with "
            "InterPro:IPR017840-grounded GENE_OR_PROTEIN node "
            "perchlorate_respiration_pcr_reductase and reviewed UniProtKB:Q47CW6 "
            "(PcrA); resolved perchlorate-respiration-protein-example-gap."
        ),
    },
    "data/traits/metabolism/tetrathionate_respiration.yaml": {
        "identifier": "traitmech:000200",
        "graph_id": "tetrathionate_respiration_ttr_pathway_sketch",
        "discussion_id": "tetrathionate-respiration-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1046/j.1365-2958.1999.01345.x and "
            "DOI:10.1128/JB.183.8.2463-2475.2001; exemplified on "
            "tetrathionate_respiration_ttr_complex with Salmonella enterica subsp. "
            "enterica serovar Typhimurium str. LT2 (NCBITaxon:99287; UP000001014) "
            "tetrathionate reductase subunits TtrA (UniProtKB:Q9Z4S6) and TtrB "
            "(UniProtKB:Q7CQM9)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1046/j.1365-2958.1999.01345.x",
            "snippet": (
                "Sequence analysis suggests that TtrA contains a molybdopterin "
                "guanine dinucleotide cofactor and a [4Fe-4S] cluster, that TtrB "
                "binds four [4Fe-4S] clusters, and that TtrC is an integral membrane "
                "protein containing a quinol oxidation site."
            ),
            "notes": (
                "Hensel et al. characterize the subunit composition of Salmonella "
                "enterica serovar Typhimurium LT2 tetrathionate reductase (TtrA, "
                "TtrB, and TtrC)."
            ),
        },
        "new_node": {
            "node_id": "tetrathionate_respiration_ttr_complex",
            "label": "tetrathionate reductase TtrABC",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR037946",
            "gene_symbols": ["ttrA", "ttrB", "ttrC"],
            "operon": "ttrBCA",
            "description": (
                "Membrane-bound heterotrimeric tetrathionate reductase complex "
                "encoded by ttrA, ttrB, and ttrC."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:Q9Z4S6",
                    "protein_label": "Tetrathionate reductase subunit A",
                    "gene_symbol": "ttrA",
                    "taxon_id": "NCBITaxon:99287",
                    "taxon_label": "Salmonella enterica subsp. enterica serovar Typhimurium str. LT2",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001014",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 125,
                    "sequence_version": 1,
                    "role": (
                        "TtrA is the catalytic molybdopterin-containing subunit A "
                        "of the heterotrimeric TtrABC tetrathionate reductase "
                        "complex in Salmonella enterica serovar Typhimurium LT2; "
                        "this accession represents the TtrA subunit rather than "
                        "the full heterotrimer."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1046/j.1365-2958.1999.01345.x",
                            "snippet": "ttrA, ttrB and ttrC are the tetrathionate reductase structural genes",
                            "notes": (
                                "Hensel et al. identify ttrA, ttrB, and ttrC as the "
                                "structural genes encoding tetrathionate reductase in "
                                "Salmonella enterica serovar Typhimurium."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:Q7CQM9",
                    "protein_label": "Tetrathionate reductase subunit B",
                    "gene_symbol": "ttrB",
                    "taxon_id": "NCBITaxon:99287",
                    "taxon_label": "Salmonella enterica subsp. enterica serovar Typhimurium str. LT2",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001014",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 121,
                    "sequence_version": 1,
                    "role": (
                        "TtrB is the iron-sulfur electron-transfer subunit B of the "
                        "heterotrimeric TtrABC tetrathionate reductase complex in "
                        "Salmonella enterica serovar Typhimurium LT2; this accession "
                        "represents the TtrB subunit rather than the full heterotrimer."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1046/j.1365-2958.1999.01345.x",
                            "snippet": "ttrA, ttrB and ttrC are the tetrathionate reductase structural genes",
                            "notes": (
                                "Hensel et al. identify ttrA, ttrB, and ttrC as the "
                                "structural genes encoding tetrathionate reductase in "
                                "Salmonella enterica serovar Typhimurium."
                            ),
                        }
                    ],
                },
            ],
        },
        "new_edge": {
            "subject": "tetrathionate_respiration_ttr_complex",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "tetrathionate_respiration_ttr_activity",
            "description": (
                "The heterotrimeric TtrABC tetrathionate reductase complex enables "
                "respiratory tetrathionate reductase activity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1046/j.1365-2958.1999.01345.x",
                    "snippet": (
                        "Sequence analysis suggests that TtrA contains a "
                        "molybdopterin guanine dinucleotide cofactor and a [4Fe-4S] "
                        "cluster, that TtrB binds four [4Fe-4S] clusters, and that "
                        "TtrC is an integral membrane protein containing a quinol "
                        "oxidation site."
                    ),
                    "notes": (
                        "Hensel et al. characterize the TtrA, TtrB, and TtrC "
                        "subunits of the Salmonella enterica serovar Typhimurium "
                        "tetrathionate reductase complex."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Promoted tetrathionate_respiration_ttr_pathway_sketch to MECHANISTIC "
                "by adding InterPro:IPR037946-grounded GENE_OR_PROTEIN node "
                "tetrathionate_respiration_ttr_complex with reviewed Salmonella "
                "enterica serovar Typhimurium LT2 (NCBITaxon:99287; UP000001014) "
                "protein_examples UniProtKB:Q9Z4S6 (TtrA) and UniProtKB:Q7CQM9 "
                "(TtrB) backed by DOI:10.1046/j.1365-2958.1999.01345.x."
            ),
        },
        "changes_summary": (
            "Promoted tetrathionate_respiration_ttr_pathway_sketch to MECHANISTIC; "
            "added InterPro:IPR037946-grounded GENE_OR_PROTEIN node "
            "tetrathionate_respiration_ttr_complex with reviewed Salmonella enterica "
            "serovar Typhimurium LT2 (NCBITaxon:99287; UP000001014) protein_examples "
            "UniProtKB:Q9Z4S6 (TtrA) and UniProtKB:Q7CQM9 (TtrB) backed by "
            "DOI:10.1046/j.1365-2958.1999.01345.x; resolved "
            "tetrathionate-respiration-protein-example-gap."
        ),
    },
    "data/traits/metabolism/trimethylamine_n_oxide_respiration.yaml": {
        "identifier": "traitmech:000199",
        "graph_id": "tmao_respiration_tor_pathway_sketch",
        "discussion_id": "trimethylamine-n-oxide-respiration-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1111/1462-2920.12726 and "
            "DOI:10.3389/fmicb.2024.1467153; exemplified on tmao_respiration_tor_system "
            "with Escherichia coli K-12 (NCBITaxon:83333; UP000000625) TMAO "
            "reductase subunits TorA (UniProtKB:P33225) and TorC (UniProtKB:P33226)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1111/1462-2920.12726",
            "snippet": "the induction of torCAD, but not genes encoding alternative TMAO reductases",
            "notes": (
                "Denby et al. show that adaptation of Escherichia coli K-12 to "
                "anaerobic respiratory growth on TMAO specifically induces the "
                "torCAD operon encoding the TorCA TMAO reductase system."
            ),
        },
        "new_node": {
            "node_id": "tmao_respiration_tor_system",
            "label": "TMAO reductase TorCA",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR041954",
            "gene_symbols": ["torC", "torA"],
            "operon": "torCAD",
            "description": (
                "Periplasmic TMAO reductase (TorA) and membrane-anchored pentaheme "
                "c-type cytochrome (TorC) encoded by the torCAD operon."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:P33225",
                    "protein_label": "Trimethylamine-N-oxide reductase 1",
                    "gene_symbol": "torA",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000000625",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 195,
                    "sequence_version": 2,
                    "role": (
                        "TorA is the periplasmic terminal molybdoenzyme subunit "
                        "encoded by the torCAD operon that reduces TMAO to TMA in "
                        "Escherichia coli K-12; this accession represents the TorA "
                        "catalytic subunit."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1111/1462-2920.12726",
                            "snippet": "TMAO is reduced to TMA by the enzyme TMAO reductase, encoded by the torCAD operon",
                            "notes": (
                                "Denby et al. characterize the Escherichia coli K-12 "
                                "torCAD-encoded TMAO reductase that reduces TMAO to TMA."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:P33226",
                    "protein_label": "Cytochrome c-type protein TorC",
                    "gene_symbol": "torC",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000000625",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 196,
                    "sequence_version": 3,
                    "role": (
                        "TorC is the membrane-anchored pentaheme c-type cytochrome "
                        "electron-transfer subunit encoded by the torCAD operon in "
                        "Escherichia coli K-12; this accession represents the TorC "
                        "cytochrome subunit."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1111/1462-2920.12726",
                            "snippet": "TMAO is reduced to TMA by the enzyme TMAO reductase, encoded by the torCAD operon",
                            "notes": (
                                "Denby et al. characterize the Escherichia coli K-12 "
                                "torCAD operon encoding the TorCA TMAO reductase system."
                            ),
                        }
                    ],
                },
            ],
        },
        "new_edge": {
            "subject": "tmao_respiration_tor_system",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "tmao_respiration_reductase_activity",
            "description": (
                "The torCAD-encoded TorCA TMAO reductase system enables respiratory "
                "TMAO reductase activity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1111/1462-2920.12726",
                    "snippet": "the induction of torCAD, but not genes encoding alternative TMAO reductases",
                    "notes": (
                        "Denby et al. show that anaerobic respiratory growth on "
                        "TMAO specifically induces the torCAD operon encoding the "
                        "TorCA TMAO reductase system."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Promoted tmao_respiration_tor_pathway_sketch to MECHANISTIC by "
                "adding InterPro:IPR041954-grounded GENE_OR_PROTEIN node "
                "tmao_respiration_tor_system with reviewed Escherichia coli K-12 "
                "(NCBITaxon:83333; UP000000625) protein_examples UniProtKB:P33225 "
                "(TorA) and UniProtKB:P33226 (TorC) backed by DOI:10.1111/1462-2920.12726."
            ),
        },
        "changes_summary": (
            "Promoted tmao_respiration_tor_pathway_sketch to MECHANISTIC; added "
            "InterPro:IPR041954-grounded GENE_OR_PROTEIN node tmao_respiration_tor_system "
            "with reviewed Escherichia coli K-12 (NCBITaxon:83333; UP000000625) "
            "protein_examples UniProtKB:P33225 (TorA) and UniProtKB:P33226 (TorC) "
            "backed by DOI:10.1111/1462-2920.12726; resolved "
            "trimethylamine-n-oxide-respiration-protein-example-gap."
        ),
    },
    "data/traits/physiology/arginine_dihydrolase_activity.yaml": {
        "identifier": "traitmech:000164",
        "graph_id": "arginine_dihydrolase_adi_pathway_sketch",
        "discussion_id": "arginine-dihydrolase-activity-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by EC 3.5.3.6, DOI:10.1016/j.fm.2010.11.016, "
            "DOI:10.1128/aem.07724-11, and DOI:10.1016/j.resmic.2012.11.004; "
            "exemplified on arginine_dihydrolase_arc_system with Latilactobacillus "
            "sakei (NCBITaxon:1599) arc operon enzymes ArcA (UniProtKB:O53088), "
            "ArcB (UniProtKB:O53089), and ArcC (UniProtKB:O53090)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1128/aem.07724-11",
            "snippet": (
                "Furthermore, a differential relative expression of the individual "
                "genes of the arc operon was found, with the highest relative gene "
                "expression occurring for the first two genes of the arc operon "
                "(arcA and arcB)."
            ),
            "notes": (
                "Rimaux et al. characterize differential expression of the arc "
                "operon genes (including arcA and arcB) during ADI pathway activity "
                "in Latilactobacillus sakei."
            ),
        },
        "new_node": {
            "node_id": "arginine_dihydrolase_arc_system",
            "label": "arginine deiminase ArcABC",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR003876",
            "gene_symbols": ["arcA", "arcB", "arcC"],
            "operon": "arcABCTD",
            "description": (
                "Arginine deiminase (ArcA), catabolic ornithine carbamoyltransferase "
                "(ArcB), and carbamate kinase (ArcC) enzymes encoded by the arc operon."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:O53088",
                    "protein_label": "Arginine deiminase",
                    "gene_symbol": "arcA",
                    "taxon_id": "NCBITaxon:1599",
                    "taxon_label": "Latilactobacillus sakei",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 106,
                    "sequence_version": 1,
                    "role": (
                        "ArcA is the arginine deiminase enzyme of the arc operon "
                        "that hydrolyzes L-arginine to L-citrulline and ammonia in "
                        "Latilactobacillus sakei; this accession represents the "
                        "ArcA enzyme component."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1016/j.resmic.2012.11.004",
                            "snippet": (
                                "Arginine conversion through the arginine deiminase "
                                "(ADI) pathway is a common metabolic trait of "
                                "Lactobacillus sakei which is ascribed to an arc "
                                "operon and which inquisitively involves citrulline "
                                "excretion and re-uptake."
                            ),
                            "notes": (
                                "Rimaux et al. characterize the Lactobacillus "
                                "(Latilactobacillus) sakei arc-operon-encoded "
                                "arginine deiminase (ADI) pathway."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:O53089",
                    "protein_label": "Ornithine carbamoyltransferase, catabolic",
                    "gene_symbol": "arcB",
                    "taxon_id": "NCBITaxon:1599",
                    "taxon_label": "Latilactobacillus sakei",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 103,
                    "sequence_version": 1,
                    "role": (
                        "ArcB is the catabolic ornithine carbamoyltransferase of "
                        "the arc operon that converts L-citrulline to L-ornithine "
                        "and carbamoyl phosphate in Latilactobacillus sakei; this "
                        "accession represents the ArcB enzyme component."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1016/j.resmic.2012.11.004",
                            "snippet": (
                                "Arginine conversion through the arginine deiminase "
                                "(ADI) pathway is a common metabolic trait of "
                                "Lactobacillus sakei which is ascribed to an arc "
                                "operon and which inquisitively involves citrulline "
                                "excretion and re-uptake."
                            ),
                            "notes": (
                                "Rimaux et al. characterize the Lactobacillus "
                                "(Latilactobacillus) sakei arc-operon-encoded "
                                "arginine deiminase (ADI) pathway."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:O53090",
                    "protein_label": "Carbamate kinase",
                    "gene_symbol": "arcC",
                    "taxon_id": "NCBITaxon:1599",
                    "taxon_label": "Latilactobacillus sakei",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 107,
                    "sequence_version": 1,
                    "role": (
                        "ArcC is the carbamate kinase of the arc operon that "
                        "transfers phosphate from carbamoyl phosphate to ADP to "
                        "generate ATP in Latilactobacillus sakei; this accession "
                        "represents the ArcC enzyme component."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1016/j.resmic.2012.11.004",
                            "snippet": (
                                "Arginine conversion through the arginine deiminase "
                                "(ADI) pathway is a common metabolic trait of "
                                "Lactobacillus sakei which is ascribed to an arc "
                                "operon and which inquisitively involves citrulline "
                                "excretion and re-uptake."
                            ),
                            "notes": (
                                "Rimaux et al. characterize the Lactobacillus "
                                "(Latilactobacillus) sakei arc-operon-encoded "
                                "arginine deiminase (ADI) pathway."
                            ),
                        }
                    ],
                },
            ],
        },
        "new_edge": {
            "subject": "arginine_dihydrolase_arc_system",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "arginine_dihydrolase_deiminase_activity",
            "description": (
                "The arc-operon-encoded ArcABC system enables arginine deiminase "
                "activity and ADI pathway flux."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/aem.07724-11",
                    "snippet": (
                        "Furthermore, a differential relative expression of the "
                        "individual genes of the arc operon was found, with the "
                        "highest relative gene expression occurring for the first "
                        "two genes of the arc operon (arcA and arcB)."
                    ),
                    "notes": (
                        "Rimaux et al. show expression of the arc operon genes "
                        "(including arcA and arcB) during ADI pathway activity in "
                        "Latilactobacillus sakei."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Promoted arginine_dihydrolase_adi_pathway_sketch to MECHANISTIC "
                "by adding InterPro:IPR003876-grounded GENE_OR_PROTEIN node "
                "arginine_dihydrolase_arc_system with reviewed Latilactobacillus "
                "sakei (NCBITaxon:1599) protein_examples UniProtKB:O53088 (ArcA), "
                "UniProtKB:O53089 (ArcB), and UniProtKB:O53090 (ArcC) backed by "
                "DOI:10.1016/j.resmic.2012.11.004 and DOI:10.1128/aem.07724-11."
            ),
        },
        "changes_summary": (
            "Promoted arginine_dihydrolase_adi_pathway_sketch to MECHANISTIC; added "
            "InterPro:IPR003876-grounded GENE_OR_PROTEIN node arginine_dihydrolase_arc_system "
            "with reviewed Latilactobacillus sakei (NCBITaxon:1599) protein_examples "
            "UniProtKB:O53088 (ArcA), UniProtKB:O53089 (ArcB), and UniProtKB:O53090 "
            "(ArcC) backed by DOI:10.1016/j.resmic.2012.11.004 and "
            "DOI:10.1128/aem.07724-11; resolved arginine-dihydrolase-activity-protein-example-gap."
        ),
    },
    "data/traits/physiology/lysine_decarboxylase_activity.yaml": {
        "identifier": "traitmech:000153",
        "graph_id": "lysine_decarboxylase_cadba_sketch",
        "discussion_id": "lysine-decarboxylase-activity-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by EC 4.1.1.18 and DOI:10.1128/jb.01306-06; "
            "exemplified on lysine_decarboxylase_cada with Escherichia coli K-12 "
            "(NCBITaxon:83333; UP000000625) inducible lysine decarboxylase CadA "
            "(UniProtKB:P0A9H3) and cadaverine/lysine antiporter CadB (UniProtKB:P0AAE8)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1128/jb.01306-06",
            "snippet": (
                "CadA activity was favored in P(i)-starved cells probably because "
                "weak organic acids slowly reenter cells fermenting glucose."
            ),
            "notes": (
                "Moreau demonstrates that inducible lysine decarboxylase CadA "
                "activity protects phosphate-starved Escherichia coli K-12 MG1655 "
                "cells fermenting glucose."
            ),
        },
        "new_canonical_example": {
            "taxon_id": "NCBITaxon:83333",
            "taxon_label": "Escherichia coli K-12",
            "note": (
                "Moreau characterized inducible CadBA lysine-dependent acid "
                "resistance and cadaverine production in phosphate-starved "
                "Escherichia coli K-12 strain MG1655."
            ),
            "reference": "DOI:10.1128/jb.01306-06",
        },
        "new_node": {
            "node_id": "lysine_decarboxylase_cada",
            "label": "inducible lysine decarboxylase CadA",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR011193",
            "gene_symbols": ["cadB", "cadA"],
            "operon": "cadBA",
            "description": (
                "Inducible lysine decarboxylase (CadA) and cadaverine/lysine "
                "antiporter (CadB) acid-resistance system."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:P0A9H3",
                    "protein_label": "Inducible lysine decarboxylase",
                    "gene_symbol": "cadA",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000000625",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 145,
                    "sequence_version": 1,
                    "role": (
                        "CadA is the inducible PLP-dependent lysine decarboxylase "
                        "component of the CadBA acid-resistance system in Escherichia "
                        "coli K-12; this accession represents the CadA decarboxylase "
                        "subunit."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/jb.01306-06",
                            "snippet": (
                                "Unexpectedly, the tolerance of P(i)-starved cells to "
                                "fermentation acids was markedly increased as a result "
                                "of the activity of the inducible CadBA lysine-dependent "
                                "acid resistance system that consumes one proton and "
                                "produces the diamine cadaverine."
                            ),
                            "notes": (
                                "Moreau demonstrates that the inducible CadBA "
                                "system in Escherichia coli K-12 MG1655 decarboxylates "
                                "lysine to cadaverine while consuming a proton."
                            ),
                        }
                    ],
                },
                {
                    "uniprot_id": "UniProtKB:P0AAE8",
                    "protein_label": "Cadaverine/lysine antiporter",
                    "gene_symbol": "cadB",
                    "taxon_id": "NCBITaxon:83333",
                    "taxon_label": "Escherichia coli K-12",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000000625",
                    "retrieved_on": C2S3_RETRIEVED_ON,
                    "entry_version": 141,
                    "sequence_version": 1,
                    "role": (
                        "CadB is the inner-membrane cadaverine/lysine antiporter "
                        "component of the CadBA acid-resistance system in Escherichia "
                        "coli K-12; this accession represents the CadB antiporter "
                        "subunit."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1128/jb.01306-06",
                            "snippet": (
                                "Unexpectedly, the tolerance of P(i)-starved cells to "
                                "fermentation acids was markedly increased as a result "
                                "of the activity of the inducible CadBA lysine-dependent "
                                "acid resistance system that consumes one proton and "
                                "produces the diamine cadaverine."
                            ),
                            "notes": (
                                "Moreau demonstrates that the inducible CadBA "
                                "system in Escherichia coli K-12 MG1655 mediates "
                                "lysine-dependent acid resistance and cadaverine export."
                            ),
                        }
                    ],
                },
            ],
        },
        "new_edge": {
            "subject": "lysine_decarboxylase_cada",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "lysine_decarboxylase_catalytic_activity",
            "description": (
                "Inducible lysine decarboxylase CadA enables catalytic lysine "
                "decarboxylation in phosphate-starved Escherichia coli K-12 cells."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1128/jb.01306-06",
                    "snippet": (
                        "CadA activity was favored in P(i)-starved cells probably "
                        "because weak organic acids slowly reenter cells fermenting "
                        "glucose."
                    ),
                    "notes": (
                        "Moreau shows that inducible CadA lysine decarboxylase "
                        "activity is favored in phosphate-starved Escherichia "
                        "coli K-12 cells fermenting glucose."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Added canonical_examples entry Escherichia coli K-12 "
                "(NCBITaxon:83333; DOI:10.1128/jb.01306-06) and promoted "
                "lysine_decarboxylase_cadba_sketch to MECHANISTIC by adding "
                "InterPro:IPR011193-grounded GENE_OR_PROTEIN node "
                "lysine_decarboxylase_cada with reviewed protein_examples "
                "UniProtKB:P0A9H3 (CadA) and UniProtKB:P0AAE8 (CadB)."
            ),
        },
        "changes_summary": (
            "Added Escherichia coli K-12 (NCBITaxon:83333; DOI:10.1128/jb.01306-06) "
            "canonical example; promoted lysine_decarboxylase_cadba_sketch to "
            "MECHANISTIC with InterPro:IPR011193-grounded GENE_OR_PROTEIN node "
            "lysine_decarboxylase_cada and reviewed protein_examples UniProtKB:P0A9H3 "
            "(CadA) and UniProtKB:P0AAE8 (CadB); resolved "
            "lysine-decarboxylase-activity-protein-example-gap."
        ),
    },
}

C2S3_COHORT_C_BLOCKERS: dict[str, dict[str, Any]] = {
    "data/traits/metabolism/fumarate_respiration.yaml": {
        "identifier": "traitmech:000196",
        "graph_id": "fumarate_respiration_frd_pathway_sketch",
        "discussion_id": "fumarate-respiration-protein-example-gap",
        "blocker_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Cycle 2 Stage 3 UniProt audit: species-level Bacteroides fragilis "
                "(NCBITaxon:817) TrEMBL fumarate reductase entries UniProtKB:Q7X479 "
                "(frdA), UniProtKB:Q7X478 (frdB), and UniProtKB:Q7X480 (frdC) lack "
                "a UniProt proteome_id (triggering UNREVIEWED_NO_PROTEOME in "
                "audit_uniprot_grounding.py), whereas reference-proteome entries in "
                "B. fragilis NCTC 9343 (NCBITaxon:272559; UP000006731: Q5L7E5, Q5L7E6, "
                "Q5L7E7) carry only BF4126/BF4125/BF4124 orderedLocusNames without "
                "frdA/frdB/frdC gene symbols. Keeping graph NONMECHANISTIC and "
                "discussion OPEN until Swiss-Prot curation or strain-aligned "
                "canonical_examples resolves the proteome/gene-symbol gap."
            ),
        },
        "changes_summary": (
            "Recorded Cycle 2 Stage 3 UniProtKB audit note on "
            "fumarate-respiration-protein-example-gap documenting the "
            "UNREVIEWED_NO_PROTEOME / locus-tag blocker for Bacteroides fragilis "
            "FrdCAB (Q7X479/Q7X478/Q7X480 vs NCTC 9343 Q5L7E5/Q5L7E6/Q5L7E7)."
        ),
    },
    "data/traits/physiology/siderophore_production.yaml": {
        "identifier": "traitmech:000186",
        "graph_id": "siderophore_production_iron_scavenging_sketch",
        "discussion_id": "siderophore-production-protein-example-gap",
        "blocker_message": {
            "author": CURATOR,
            "timestamp": C2S3_TIMESTAMP,
            "body": (
                "Cycle 2 Stage 3 UniProt audit: canonical_examples cites species-level "
                "Pseudomonas aeruginosa (NCBITaxon:287; DOI:10.1073/pnas.0908760106) "
                "and Pseudomonas fluorescens (NCBITaxon:294; DOI:10.15698/mic2018.10.649), "
                "whereas reviewed Swiss-Prot pyoverdine biosynthesis/transport proteins "
                "(e.g., PvdA UniProtKB:Q51548, FpvA UniProtKB:P48632) are annotated on "
                "strain Pseudomonas aeruginosa PAO1 (NCBITaxon:208964; UP000002438) and "
                "current record evidence snippets do not name individual pvd/fpv gene "
                "products. Keeping graph NONMECHANISTIC and discussion OPEN until a "
                "PAO1-specific primary source snippet and canonical_examples entry are added."
            ),
        },
        "changes_summary": (
            "Recorded Cycle 2 Stage 3 UniProtKB audit note on "
            "siderophore-production-protein-example-gap documenting the taxon-rank "
            "and gene-snippet blocker between species-level canonical_examples "
            "(NCBITaxon:287) and PAO1 Swiss-Prot entries (NCBITaxon:208964)."
        ),
    },
}

C3S3_TIMESTAMP = "2026-10-23T22:45:00Z"
C3S3_RETRIEVED_ON = "2026-10-23"

C3S3_COHORT_E_PROMOTIONS: dict[str, dict[str, Any]] = {
    "data/traits/other/coagulase_positive.yaml": {
        "identifier": "METPO:1007090",
        "graph_id": "coagulase_positive_prothrombin_clotting_sketch",
        "discussion_id": "coagulase-positive-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1371/journal.ppat.1001036; "
            "exemplified on coagulase_positive_coa with Staphylococcus aureus "
            "(NCBITaxon:1280) secreted staphylocoagulase Coa (UniProtKB:P07767)."
        ),
        "new_evidence": {
            "reference": "DOI:10.1371/journal.ppat.1001036",
            "snippet": (
                "Coa and vWbp promote the non-proteolytic activation of "
                "prothrombin and cleavage of fibrinogen, reactions that are "
                "inhibited with specific antibody against each of these molecules."
            ),
            "notes": (
                "Cheng et al. demonstrate that Staphylococcus aureus "
                "staphylocoagulase (Coa) and von Willebrand factor-binding "
                "protein (vWbp) promote non-proteolytic activation of "
                "prothrombin and cleavage of fibrinogen."
            ),
        },
        "new_node": {
            "node_id": "coagulase_positive_coa",
            "label": "staphylocoagulase Coa",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR001443",
            "gene_symbols": ["coa"],
            "description": (
                "Secreted staphylocoagulase (Coa) that binds and "
                "non-proteolytically activates host prothrombin to cleave "
                "fibrinogen into fibrin."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:P07767",
                    "protein_label": "Staphylocoagulase",
                    "gene_symbol": "coa",
                    "taxon_id": "NCBITaxon:1280",
                    "taxon_label": "Staphylococcus aureus",
                    "entry_status": "REVIEWED",
                    "retrieved_on": C3S3_RETRIEVED_ON,
                    "entry_version": 82,
                    "sequence_version": 2,
                    "role": (
                        "Secreted staphylocoagulase (Coa) polypeptide that "
                        "binds and non-proteolytically activates host "
                        "prothrombin to convert fibrinogen into fibrin in "
                        "Staphylococcus aureus."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1371/journal.ppat.1001036",
                            "snippet": (
                                "All natural isolates of S. aureus secrete "
                                "coagulase (Coa), a polypeptide that binds and "
                                "activates prothrombin, thereby converting "
                                "fibrinogen to fibrin and promoting the clotting "
                                "of plasma or blood."
                            ),
                            "notes": (
                                "Cheng et al. show that Staphylococcus aureus "
                                "secretes staphylocoagulase (Coa), which binds "
                                "and activates prothrombin to convert fibrinogen "
                                "to fibrin."
                            ),
                        }
                    ],
                }
            ],
        },
        "new_edge": {
            "subject": "coagulase_positive_coa",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "coagulase_positive_prothrombin_activation",
            "description": (
                "Secreted staphylocoagulase Coa enables non-proteolytic "
                "activation of prothrombin."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.ppat.1001036",
                    "snippet": (
                        "Coa and vWbp promote the non-proteolytic activation of "
                        "prothrombin and cleavage of fibrinogen, reactions that "
                        "are inhibited with specific antibody against each of "
                        "these molecules."
                    ),
                    "notes": (
                        "Cheng et al. show that Staphylococcus aureus "
                        "staphylocoagulase Coa promotes non-proteolytic "
                        "activation of prothrombin and subsequent fibrinogen "
                        "cleavage."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C3S3_TIMESTAMP,
            "body": (
                "Promoted coagulase_positive_prothrombin_clotting_sketch to "
                "MECHANISTIC by adding InterPro:IPR001443-grounded "
                "GENE_OR_PROTEIN node coagulase_positive_coa with reviewed "
                "Staphylococcus aureus (NCBITaxon:1280) protein_examples "
                "UniProtKB:P07767 (Coa) backed by DOI:10.1371/journal.ppat.1001036."
            ),
        },
        "changes_summary": (
            "Promoted coagulase_positive_prothrombin_clotting_sketch to "
            "MECHANISTIC; added InterPro:IPR001443-grounded GENE_OR_PROTEIN "
            "node coagulase_positive_coa with reviewed Staphylococcus aureus "
            "(NCBITaxon:1280) protein_examples UniProtKB:P07767 (Coa) backed "
            "by DOI:10.1371/journal.ppat.1001036; resolved "
            "coagulase-positive-protein-example-gap."
        ),
    },
    "data/traits/physiology/pyrazinamidase_activity.yaml": {
        "identifier": "traitmech:000163",
        "graph_id": "pyrazinamidase_activity_pnca_sketch",
        "discussion_id": "pyrazinamidase-activity-protein-example-gap",
        "scope_notes": (
            "Mechanistic graph backed by DOI:10.1111/j.1742-4658.2007.06241.x "
            "and DOI:10.1371/journal.pone.0015785; exemplified on "
            "pyrazinamidase_pnca with Mycobacterium tuberculosis H37Rv "
            "(NCBITaxon:83332; UP000001584) nicotinamidase/pyrazinamidase PncA "
            "(UniProtKB:I6XD65)."
        ),
        "new_canonical_example": {
            "taxon_id": "NCBITaxon:83332",
            "taxon_label": "Mycobacterium tuberculosis H37Rv",
            "note": (
                "Petrella et al. determined the crystal structure and catalytic "
                "mechanism of Mycobacterium tuberculosis H37Rv pyrazinamidase "
                "(PncA; Rv2043c) in pyrazinamide activation to pyrazinoic acid."
            ),
            "reference": "DOI:10.1371/journal.pone.0015785",
        },
        "new_node": {
            "node_id": "pyrazinamidase_pnca",
            "label": "nicotinamidase/pyrazinamidase PncA",
            "node_type": "GENE_OR_PROTEIN",
            "grounding": "InterPro:IPR000868",
            "gene_symbols": ["pncA"],
            "description": (
                "Isochorismatase-like nicotinamidase/pyrazinamidase (PncA) that "
                "hydrolyzes pyrazinamide and nicotinamide."
            ),
            "protein_examples": [
                {
                    "uniprot_id": "UniProtKB:I6XD65",
                    "protein_label": "Nicotinamidase/pyrazinamidase",
                    "gene_symbol": "pncA",
                    "taxon_id": "NCBITaxon:83332",
                    "taxon_label": "Mycobacterium tuberculosis H37Rv",
                    "entry_status": "REVIEWED",
                    "proteome_id": "UP000001584",
                    "retrieved_on": C3S3_RETRIEVED_ON,
                    "entry_version": 79,
                    "sequence_version": 1,
                    "role": (
                        "PncA (Rv2043c) is the nicotinamidase/pyrazinamidase "
                        "enzyme that hydrolyzes pyrazinamide into pyrazinoic "
                        "acid and ammonia in Mycobacterium tuberculosis H37Rv."
                    ),
                    "evidence": [
                        {
                            "reference": "DOI:10.1371/journal.pone.0015785",
                            "snippet": (
                                "Pyrazinamidase (PncA) activates the first-line "
                                "antituberculous drug pyrazinamide into "
                                "pyrazinoic acid."
                            ),
                            "notes": (
                                "Petrella et al. determined the crystal "
                                "structure of Mycobacterium tuberculosis H37Rv "
                                "pyrazinamidase PncA (UniProtKB:I6XD65) and "
                                "characterized its catalytic mechanism."
                            ),
                        }
                    ],
                }
            ],
        },
        "new_edge": {
            "subject": "pyrazinamidase_pnca",
            "predicate": "enables",
            "predicate_id": "RO:0002327",
            "object": "pyrazinamidase_catalytic_activity",
            "description": (
                "Nicotinamidase/pyrazinamidase PncA enables pyrazinamidase "
                "catalytic activity."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1371/journal.pone.0015785",
                    "snippet": (
                        "Pyrazinamidase (PncA) activates the first-line "
                        "antituberculous drug pyrazinamide into pyrazinoic acid."
                    ),
                    "notes": (
                        "Petrella et al. characterize Mycobacterium tuberculosis "
                        "H37Rv PncA catalyzing the conversion of pyrazinamide "
                        "into pyrazinoic acid."
                    ),
                }
            ],
        },
        "resolution_message": {
            "author": CURATOR,
            "timestamp": C3S3_TIMESTAMP,
            "body": (
                "Added canonical_examples entry Mycobacterium tuberculosis H37Rv "
                "(NCBITaxon:83332; DOI:10.1371/journal.pone.0015785) and promoted "
                "pyrazinamidase_activity_pnca_sketch to MECHANISTIC by adding "
                "InterPro:IPR000868-grounded GENE_OR_PROTEIN node "
                "pyrazinamidase_pnca with reviewed protein_examples "
                "UniProtKB:I6XD65 (PncA)."
            ),
        },
        "changes_summary": (
            "Added Mycobacterium tuberculosis H37Rv (NCBITaxon:83332; "
            "DOI:10.1371/journal.pone.0015785) canonical example; promoted "
            "pyrazinamidase_activity_pnca_sketch to MECHANISTIC with "
            "InterPro:IPR000868-grounded GENE_OR_PROTEIN node pyrazinamidase_pnca "
            "and reviewed protein_examples UniProtKB:I6XD65 (PncA); resolved "
            "pyrazinamidase-activity-protein-example-gap."
        ),
    },
}

C3S3_COHORT_E_BLOCKERS: dict[str, dict[str, Any]] = {
    "data/traits/other/indole_test_positive.yaml": {
        "identifier": "METPO:1005011",
        "graph_id": "indole_test_positive_tryptophan_sketch",
        "discussion_id": "indole-test-positive-protein-example-gap",
        "blocker_message": {
            "author": CURATOR,
            "timestamp": C3S3_TIMESTAMP,
            "body": (
                "Cycle 3 Stage 3 UniProt audit: canonical_examples cites "
                "enterotoxigenic Escherichia coli strain H10407 "
                "(NCBITaxon:316401; DOI:10.1128/AEM.02787-15), an analytical "
                "indole-assay study whose text does not mention tnaA or "
                "tryptophanase and for which UniProtKB lacks a strain H10407 "
                "tnaA entry, whereas reviewed Swiss-Prot tryptophanase TnaA "
                "(UniProtKB:P0A853) is annotated on Escherichia coli K-12 "
                "(NCBITaxon:83333; UP000000625). Keeping graph NONMECHANISTIC "
                "and discussion OPEN until a K-12 tnaA primary source snippet "
                "and canonical_examples entry are added."
            ),
        },
        "changes_summary": (
            "Recorded Cycle 3 Stage 3 UniProtKB audit note on "
            "indole-test-positive-protein-example-gap documenting the "
            "source-snippet and strain-taxon blocker between Escherichia coli "
            "H10407 (NCBITaxon:316401; DOI:10.1128/AEM.02787-15) and Escherichia "
            "coli K-12 Swiss-Prot TnaA (UniProtKB:P0A853; NCBITaxon:83333)."
        ),
    },
}


def _protected_paths(repo_root: Path = REPO_ROOT) -> set[str]:
    dnw = repo_root / "DO_NOT_WORK.md"
    if not dnw.exists():
        return set()
    protected: set[str] = set()
    for line in dnw.read_text(encoding="utf-8").splitlines():
        if "data/traits/" in line and ".yaml" in line:
            for token in line.replace("`", " ").split():
                if token.startswith("data/traits/") and token.endswith(".yaml"):
                    protected.add(token)
    return protected


def process_all(apply: bool = False, repo_root: Path = REPO_ROOT) -> tuple[int, int, int]:
    """Apply Stage 3 new protein_examples and entry_version refreshes.

    Returns:
        (new_examples_added, versions_refreshed, files_updated)
    """
    protected = _protected_paths(repo_root)
    refreshes_by_file: dict[str, list[tuple[str, str, str, int | None, int]]] = {}
    for rel_path, graph_id, node_id, curie, old_v, new_v in ENTRY_VERSION_REFRESHES:
        refreshes_by_file.setdefault(rel_path, []).append((graph_id, node_id, curie, old_v, new_v))

    promotions_by_file = {**C2S3_COHORT_C_PROMOTIONS, **C3S3_COHORT_E_PROMOTIONS}
    blockers_by_file = {**C2S3_COHORT_C_BLOCKERS, **C3S3_COHORT_E_BLOCKERS}
    all_rel_paths = sorted(
        set(refreshes_by_file)
        | set(NEW_PROTEIN_EXAMPLES)
        | set(promotions_by_file)
        | set(blockers_by_file)
    )
    for rel_path in all_rel_paths:
        if rel_path in protected:
            raise ValueError(f"Refusing to touch DO_NOT_WORK protected trait: {rel_path}")

    new_examples_added = 0
    versions_refreshed = 0
    files_updated = 0

    for rel_path in all_rel_paths:
        path = repo_root / rel_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        changed = False
        refresh_descriptions: list[str] = []

        # 1. Apply entry_version refreshes on existing protein_examples
        for graph_id, node_id, curie, old_v, new_v in refreshes_by_file.get(rel_path, []):
            matched_pe = None
            for g in doc.get("causal_graphs") or []:
                if g.get("graph_id") == graph_id:
                    for n in g.get("nodes") or []:
                        if n.get("node_id") == node_id:
                            for pe in n.get("protein_examples") or []:
                                if pe.get("uniprot_id") == curie:
                                    matched_pe = pe
                                    break
            if matched_pe is None:
                raise ValueError(
                    f"Missing expected protein_example {curie} on {graph_id}/{node_id} in {rel_path}"
                )
            cur_v = matched_pe.get("entry_version")
            if cur_v not in (old_v, new_v):
                raise ValueError(
                    f"Unexpected entry_version={cur_v} for {curie} in {rel_path} "
                    f"(expected {old_v} or {new_v})"
                )
            if cur_v != new_v or matched_pe.get("retrieved_on") != RETRIEVED_ON:
                matched_pe["entry_version"] = new_v
                matched_pe["retrieved_on"] = RETRIEVED_ON
                changed = True
                versions_refreshed += 1
            old_label = old_v if old_v is not None else "unset"
            refresh_descriptions.append(f"{curie} ({old_label} -> {new_v} on {node_id})")

        # 2. Apply new verified protein_examples if this file is in NEW_PROTEIN_EXAMPLES
        if rel_path in NEW_PROTEIN_EXAMPLES:
            spec = NEW_PROTEIN_EXAMPLES[rel_path]
            if doc.get("identifier") != spec["identifier"]:
                raise ValueError(
                    f"Identifier mismatch for {rel_path}: {doc.get('identifier')} != {spec['identifier']}"
                )
            graphs = [
                g for g in (doc.get("causal_graphs") or []) if g.get("graph_id") == spec["graph_id"]
            ]
            if len(graphs) != 1:
                raise ValueError(f"Expected graph {spec['graph_id']} in {rel_path}")
            graph = graphs[0]
            if graph.get("scope_notes") != spec["scope_notes"]:
                graph["scope_notes"] = spec["scope_notes"]
                changed = True

            for node_id, desired_examples in spec["nodes"].items():
                nodes = [n for n in (graph.get("nodes") or []) if n.get("node_id") == node_id]
                if len(nodes) != 1:
                    raise ValueError(f"Expected node {node_id} in {rel_path}")
                node = nodes[0]
                desired_copy = copy.deepcopy(desired_examples)
                if node.get("protein_examples") != desired_copy:
                    node["protein_examples"] = desired_copy
                    changed = True
                    new_examples_added += len(desired_copy)

            existing_events = [
                ev
                for ev in (doc.get("curation_history") or [])
                if ev.get("timestamp") == TIMESTAMP and ev.get("curator") == CURATOR
            ]
            if not existing_events or existing_events[-1].get("changes") != spec["changes_summary"]:
                changed = True

            if changed:
                record_curation_event(
                    doc,
                    curator=CURATOR,
                    action=ACTION_EXAMPLE,
                    changes=spec["changes_summary"],
                    llm_assisted=True,
                    timestamp=TIMESTAMP,
                    upsert=True,
                )
        elif rel_path in promotions_by_file:
            spec = promotions_by_file[rel_path]
            promo_ts = spec["resolution_message"]["timestamp"]
            promo_date = promo_ts[:10]
            if doc.get("identifier") != spec["identifier"]:
                raise ValueError(
                    f"Identifier mismatch for {rel_path}: {doc.get('identifier')} != {spec['identifier']}"
                )
            new_ev = spec.get("new_evidence")
            if new_ev is not None:
                ev_list = doc.setdefault("evidence", [])
                if not any(
                    e.get("reference") == new_ev["reference"]
                    and e.get("snippet") == new_ev["snippet"]
                    for e in ev_list
                ):
                    ev_list.append(copy.deepcopy(new_ev))
                    changed = True

            new_ce = spec.get("new_canonical_example")
            if new_ce is not None:
                ce_list = doc.setdefault("canonical_examples", [])
                if not any(c.get("taxon_id") == new_ce["taxon_id"] for c in ce_list):
                    ce_list.append(copy.deepcopy(new_ce))
                    changed = True

            graphs = [
                g for g in (doc.get("causal_graphs") or []) if g.get("graph_id") == spec["graph_id"]
            ]
            if len(graphs) != 1:
                raise ValueError(f"Expected graph {spec['graph_id']} in {rel_path}")
            graph = graphs[0]
            if graph.get("scope_status") != "MECHANISTIC":
                graph["scope_status"] = "MECHANISTIC"
                changed = True
            if graph.get("scope_notes") != spec["scope_notes"]:
                graph["scope_notes"] = spec["scope_notes"]
                changed = True

            new_node = copy.deepcopy(spec["new_node"])
            nodes_list = graph.setdefault("nodes", [])
            existing_nodes = [
                (idx, n)
                for idx, n in enumerate(nodes_list)
                if n.get("node_id") == new_node["node_id"]
            ]
            if not existing_nodes:
                nodes_list.append(new_node)
                changed = True
                new_examples_added += len(new_node.get("protein_examples") or [])
            else:
                idx, cur_node = existing_nodes[0]
                if cur_node != new_node:
                    nodes_list[idx] = new_node
                    changed = True
                    new_examples_added += len(new_node.get("protein_examples") or [])

            new_edge = copy.deepcopy(spec["new_edge"])
            edges_list = graph.setdefault("edges", [])
            existing_edges = [
                (idx, e)
                for idx, e in enumerate(edges_list)
                if e.get("subject") == new_edge["subject"]
                and e.get("object") == new_edge["object"]
                and e.get("predicate_id") == new_edge["predicate_id"]
            ]
            if not existing_edges:
                edges_list.append(new_edge)
                changed = True
            else:
                idx, cur_edge = existing_edges[0]
                if cur_edge != new_edge:
                    edges_list[idx] = new_edge
                    changed = True

            discussions = [
                d
                for d in (doc.get("discussions") or [])
                if d.get("discussion_id") == spec["discussion_id"]
            ]
            if len(discussions) != 1:
                raise ValueError(f"Expected discussion {spec['discussion_id']} in {rel_path}")
            disc = discussions[0]
            res_body = spec["resolution_message"]["body"]
            if (
                disc.get("status") != "RESOLVED"
                or disc.get("resolved_date") != promo_date
                or disc.get("resolution_note") != res_body
            ):
                disc["status"] = "RESOLVED"
                disc["resolved_date"] = promo_date
                disc["resolution_note"] = res_body
                changed = True

            existing_promo_events = [
                ev
                for ev in (doc.get("curation_history") or [])
                if ev.get("timestamp") == promo_ts and ev.get("curator") == CURATOR
            ]
            if (
                not existing_promo_events
                or existing_promo_events[-1].get("changes") != spec["changes_summary"]
            ):
                changed = True

            if changed:
                record_curation_event(
                    doc,
                    curator=CURATOR,
                    action=ACTION_EXAMPLE,
                    changes=spec["changes_summary"],
                    llm_assisted=True,
                    timestamp=promo_ts,
                    upsert=True,
                )
        elif rel_path in blockers_by_file:
            spec = blockers_by_file[rel_path]
            blocker_ts = spec["blocker_message"]["timestamp"]
            if doc.get("identifier") != spec["identifier"]:
                raise ValueError(
                    f"Identifier mismatch for {rel_path}: {doc.get('identifier')} != {spec['identifier']}"
                )
            discussions = [
                d
                for d in (doc.get("discussions") or [])
                if d.get("discussion_id") == spec["discussion_id"]
            ]
            if len(discussions) != 1:
                raise ValueError(f"Expected discussion {spec['discussion_id']} in {rel_path}")
            disc = discussions[0]
            blocker_body = spec["blocker_message"]["body"]
            if disc.get("notes") != blocker_body:
                disc["notes"] = blocker_body
                changed = True

            existing_blocker_events = [
                ev
                for ev in (doc.get("curation_history") or [])
                if ev.get("timestamp") == blocker_ts and ev.get("curator") == CURATOR
            ]
            if (
                not existing_blocker_events
                or existing_blocker_events[-1].get("changes") != spec["changes_summary"]
            ):
                changed = True

            if changed:
                record_curation_event(
                    doc,
                    curator=CURATOR,
                    action=ACTION_DISCUSSION,
                    changes=spec["changes_summary"],
                    llm_assisted=True,
                    timestamp=blocker_ts,
                    upsert=True,
                )
        else:
            if changed:
                summary = (
                    "Refreshed UniProtKB entry_version against live UniProt REST on "
                    f"{RETRIEVED_ON}: " + ", ".join(refresh_descriptions) + "."
                )
                record_curation_event(
                    doc,
                    curator=CURATOR,
                    action=ACTION_REFRESH,
                    changes=summary,
                    llm_assisted=True,
                    timestamp=TIMESTAMP,
                    upsert=True,
                )

        if changed:
            errors = validate_trait(doc)
            if errors:
                raise ValidationFailedError(path, errors)
            if apply:
                write_validated_trait(doc, path)
            files_updated += 1

    return new_examples_added, versions_refreshed, files_updated


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to data/traits/ via write_validated_trait (default: dry-run).",
    )
    args = parser.parse_args(argv)
    new_ex, refreshed, updated = process_all(apply=args.apply)
    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(
        f"[{mode}] New protein_examples added: {new_ex}; "
        f"entry_versions refreshed: {refreshed}; "
        f"TraitRecord files updated: {updated}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
