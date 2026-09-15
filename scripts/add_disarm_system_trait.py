#!/usr/bin/env python3
"""Add the DISARM system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "disarm_system.yaml"

OFIR = "DOI:10.1038/s41564-017-0051-0"
BRAVO = "DOI:10.1038/s41467-022-30673-1"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T09:40:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000211",
    "label": "DISARM system",
    "definition": (
        "A genomics trait describing possession of a Defense Island System "
        "Associated with Restriction-Modification locus that uses "
        "methyltransferase-associated self/non-self discrimination and DrmAB "
        "activation to inhibit bacteriophage DNA replication."
    ),
    "definition_source": OFIR,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Defense Island System Associated with Restriction-Modification",
            "synonym_type": "EXACT_SYNONYM",
            "source": BRAVO,
        },
        {
            "synonym_text": "Defense Island System Associated with Restriction Modification",
            "synonym_type": "EXACT_SYNONYM",
            "source": BRAVO,
        },
    ],
    "evidence": [
        {
            "reference": OFIR,
            "snippet": (
                "Our results establish DISARM as a new defence system, "
                "providing protection against diverse phages"
            ),
            "notes": (
                "Ofir et al. experimentally established DISARM as a phage "
                "defense system and distinguished its intracellular block from "
                "phage-adsorption phenotypes."
            ),
        },
        {
            "reference": OFIR,
            "snippet": (
                "The DISARM system is widespread in defence islands across "
                "the microbial world"
            ),
            "notes": (
                "Ofir et al. support DISARM as a recurring microbial defense "
                "island system rather than a single source-specific locus."
            ),
        },
        {
            "reference": BRAVO,
            "snippet": (
                "DISARM (Defense Island System Associated with "
                "Restriction-Modification) systems can provide protection "
                "against a wide range of phage"
            ),
            "notes": (
                "Bravo et al. independently expand the DISARM acronym and "
                "frame DISARM as a broad anti-phage system."
            ),
        },
        {
            "reference": BRAVO,
            "snippet": (
                "In vivo studies of structure-guided DrmAB mutants demonstrate "
                "that ATP hydrolysis, DNA binding, and DrmAB heterodimer "
                "formation are essential for phage targeting by DISARM"
            ),
            "notes": (
                "Bravo et al. support the DrmAB activation mechanism recorded "
                "in the first causal graph."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:766760",
            "taxon_label": "Bacillus paralicheniformis ATCC 9945a",
            "note": (
                "Ofir et al. amplified the native B. paralicheniformis ATCC "
                "9945a class 2 DISARM locus and integrated it into B. "
                "subtilis to test phage defense."
            ),
            "reference": OFIR,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "disarm_dna_sensing_antiphage_defense",
            "title": "DISARM senses phage DNA to activate DrmAB defense",
            "description": (
                "Evidence-backed causal sketch linking DISARM methylation and "
                "5-prime-overhang DNA sensing to DrmAB activation and blocked "
                "early phage DNA circularization."
            ),
            "scope_status": "MECHANISTIC",
            "scope_notes": (
                "The graph captures host DNA methylation, 5-prime-overhang "
                "sensing, DrmAB activation, and early phage DNA restriction "
                "without asserting the unresolved downstream nuclease or "
                "replication-block coupling."
            ),
            "nodes": [
                {
                    "node_id": "host_dna_methylation",
                    "label": "DISARM host DNA methylation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DISARM methyltransferase-mediated methylation of host "
                        "DNA at cognate motifs."
                    ),
                },
                {
                    "node_id": "five_prime_overhang_dna_sensing",
                    "label": "DISARM 5-prime-overhang DNA sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DrmAB-associated recognition of foreign DNA "
                        "substrates carrying a 5-prime single-stranded "
                        "overhang."
                    ),
                },
                {
                    "node_id": "drmab_core_complex",
                    "grounding_status": "REVIEWED_LABEL_ONLY",
                    "grounding_notes": (
                        "DrmA and DrmB are distinct DISARM protein families; "
                        "this node denotes the activated heterodimeric core "
                        "complex rather than one component family."
                    ),
                    "label": "DrmAB core complex",
                    "node_type": "GENE_OR_PROTEIN",
                    "description": (
                        "Heterodimeric DISARM DrmA-DrmB core complex that "
                        "binds invading DNA and undergoes long-range "
                        "activation upon 5-prime-overhang substrate loading."
                    ),
                    "gene_symbols": ["drmA", "drmB"],
                    "operon": "DISARM",
                    "protein_examples": [
                        {
                            "uniprot_id": "UniProtKB:P0DW05",
                            "protein_label": "DISARM protein DrmA",
                            "gene_symbol": "drmA",
                            "taxon_id": "NCBITaxon:766760",
                            "taxon_label": (
                                "Bacillus paralicheniformis ATCC 9945a"
                            ),
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 12,
                            "sequence_version": 1,
                            "role": (
                                "B. paralicheniformis ATCC 9945a DrmA is the "
                                "helicase-domain component of the class 2 "
                                "DISARM DrmAB core."
                            ),
                            "evidence": [
                                {
                                    "reference": OFIR,
                                    "snippet": (
                                        "Deletions of drmA (helicase domain), "
                                        "drmB (DUF1998 domain) and drmE "
                                        "(unknown function) abolished DISARM "
                                        "protection against all phages tested"
                                    ),
                                    "notes": (
                                        "Ofir et al. tested scarless deletions "
                                        "in the native B. paralicheniformis "
                                        "ATCC 9945a DISARM locus; UniProt "
                                        "verifies the reviewed DrmA accession."
                                    ),
                                }
                            ],
                        },
                        {
                            "uniprot_id": "UniProtKB:P0DW06",
                            "protein_label": "DISARM protein DrmB",
                            "gene_symbol": "drmB",
                            "taxon_id": "NCBITaxon:766760",
                            "taxon_label": (
                                "Bacillus paralicheniformis ATCC 9945a"
                            ),
                            "entry_status": "REVIEWED",
                            "retrieved_on": "2026-09-15",
                            "entry_version": 9,
                            "sequence_version": 1,
                            "role": (
                                "B. paralicheniformis ATCC 9945a DrmB is the "
                                "DUF1998 component paired with DrmA in the "
                                "class 2 DISARM DrmAB core."
                            ),
                            "evidence": [
                                {
                                    "reference": OFIR,
                                    "snippet": (
                                        "Deletions of drmA (helicase domain), "
                                        "drmB (DUF1998 domain) and drmE "
                                        "(unknown function) abolished DISARM "
                                        "protection against all phages tested"
                                    ),
                                    "notes": (
                                        "Ofir et al. tested scarless deletions "
                                        "in the native B. paralicheniformis "
                                        "ATCC 9945a DISARM locus; UniProt "
                                        "verifies the reviewed DrmB accession."
                                    ),
                                }
                            ],
                        },
                    ],
                },
                {
                    "node_id": "drmab_activation",
                    "label": "DISARM DrmAB activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DNA-triggered activation of the DISARM DrmAB core "
                        "complex."
                    ),
                },
                {
                    "node_id": "phage_dna_circularization",
                    "label": "phage DNA circularization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Circularization of injected bacteriophage genomic DNA "
                        "after adsorption and DNA entry."
                    ),
                },
                {
                    "node_id": "disarm_system_trait",
                    "label": "DISARM system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000211",
                    "description": (
                        "Possession of a genome-encoded DISARM phage defense "
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
                    "subject": "drmab_core_complex",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "drmab_activation",
                    "description": (
                        "DrmA DNA binding, DrmA ATP hydrolysis, and DrmAB "
                        "heterodimer formation are required for DISARM "
                        "activation and phage targeting."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": (
                                "DNA binding, and DrmAB heterodimer formation "
                                "are essential for phage targeting by DISARM"
                            ),
                            "notes": (
                                "Bravo et al. established the structural and "
                                "functional importance of the DrmA-DrmB core "
                                "complex."
                            ),
                        }
                    ],
                },
                {
                    "subject": "host_dna_methylation",
                    "predicate": "negatively regulates",
                    "predicate_id": "RO:0002212",
                    "object": "drmab_activation",
                    "description": (
                        "DISARM host-DNA methylation limits DrmAB activation "
                        "by self DNA."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": (
                                "methylated DNA limits the ATPase activity of "
                                "DrmAB which is essential for anti-phage "
                                "defense"
                            ),
                            "notes": (
                                "Bravo et al. support methylation-sensitive "
                                "DrmAB activation as a self/non-self filter."
                            ),
                        }
                    ],
                },
                {
                    "subject": "five_prime_overhang_dna_sensing",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "drmab_activation",
                    "description": (
                        "Unmethylated 5-prime-overhang DNA dislodges the "
                        "DrmA trigger loop to activate DrmAB."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": (
                                "binding to DNA substrates containing a 5′ "
                                "overhang dislodges the TL, initiating a "
                                "long-range structural rearrangement for DrmAB "
                                "activation"
                            ),
                            "notes": (
                                "Bravo et al. structurally support "
                                "5-prime-overhang-triggered DrmAB activation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "drmab_activation",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_dna_circularization",
                    "description": (
                        "Activated DISARM blocks early phage DNA "
                        "circularization and replication after phage entry."
                    ),
                    "evidence": [
                        {
                            "reference": OFIR,
                            "snippet": (
                                "phi3T was not able to circularize its genome "
                                "or form detectible lysogens in "
                                "DISARM-containing cells"
                            ),
                            "notes": (
                                "Ofir et al. showed that DISARM blocks an "
                                "early intracellular step after phage "
                                "adsorption."
                            ),
                        }
                    ],
                },
                {
                    "subject": "drmab_activation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "disarm_system_trait",
                    "description": (
                        "DrmAB activation realizes DISARM-mediated anti-phage "
                        "defense."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": (
                                "provide the mechanism of targeting a wide "
                                "range of phage by DISARM"
                            ),
                            "notes": (
                                "Bravo et al. linked DNA-interacting DrmA "
                                "residues to DISARM anti-phage protection in "
                                "vivo."
                            ),
                        }
                    ],
                },
                {
                    "subject": "disarm_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DISARM possession is a methyltransferase-associated "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": OFIR,
                            "snippet": (
                                "Our results establish DISARM as a new defence "
                                "system"
                            ),
                            "notes": (
                                "Ofir et al. establish DISARM in the phage "
                                "defense system family."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "disarm-downstream-effector-gap",
            "prompt": (
                "Resolve the downstream nuclease or replication-blocking "
                "effector coupled to activated DrmAB before adding a more "
                "specific DISARM phage-DNA degradation edge."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Ofir et al. inferred phage DNA degradation and showed that "
                "DrmC is partially redundant across phages; Bravo et al. "
                "resolved DrmAB recognition and activation but left the "
                "downstream nuclease or physical replication block as a model."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="replace an existing generated target file",
    )
    args = parser.parse_args()

    if TARGET.exists() and not args.overwrite:
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted DISARM system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent with reviewed "
            "B. paralicheniformis ATCC 9945a DrmA and DrmB protein examples "
            "after an ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v88."
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
