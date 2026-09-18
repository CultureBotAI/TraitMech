#!/usr/bin/env python3
"""Add the Hna system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hna_system.yaml"

SATHER = "DOI:10.1016/j.chom.2023.01.010"
HOOPER = "DOI:10.1038/s41467-026-73157-2"

CURATOR = "codex"
TIMESTAMP = "2026-09-18T12:46:11Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000241",
    "label": "Hna system",
    "definition": (
        "A phage defense system in which an organism possesses an Hna locus "
        "encoding a single SF2 helicase/nuclease effector that protects cells "
        "from bacteriophage infection by responding to phage single-stranded "
        "DNA-binding protein challenge, shifting toward dysregulated nuclease "
        "activation, and triggering abortive infection."
    ),
    "definition_source": SATHER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Hna anti-phage defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": HOOPER,
        }
    ],
    "evidence": [
        {
            "reference": SATHER,
            "snippet": (
                "single phage defense protein, Hna, that provides protection "
                "against diverse phages in Sinorhizobium meliloti"
            ),
            "notes": (
                "Sather et al. support Hna as a single-protein phage-defense "
                "determinant in S. meliloti."
            ),
        },
        {
            "reference": SATHER,
            "snippet": (
                "Homologs of Hna are distributed widely across bacterial "
                "lineages"
            ),
            "notes": (
                "Sather et al. support placing Hna at a bacterial family "
                "level rather than curating only the S. meliloti instance."
            ),
        },
        {
            "reference": SATHER,
            "snippet": (
                "Hna contains superfamily II helicase motifs at its N terminus "
                "and a nuclease motif at its C terminus, with mutagenesis of "
                "these motifs inactivating viral defense"
            ),
            "notes": (
                "Sather et al. connect the predicted helicase/nuclease domain "
                "architecture to Hna antiphage activity."
            ),
        },
        {
            "reference": HOOPER,
            "snippet": (
                "Hna is a broadly distributed anti-phage immune system that "
                "confers resistance against diverse phage by eliciting an "
                "abortive infection response"
            ),
            "notes": (
                "Hooper et al. independently support Hna as a named "
                "anti-phage immune system with abortive-infection output."
            ),
        },
        {
            "reference": HOOPER,
            "snippet": (
                "shifts catalytic partitioning toward dysregulated nuclease "
                "activation"
            ),
            "notes": (
                "Hooper et al. support phage single-stranded DNA-binding "
                "protein as a direct stimulus for Hna nuclease activation."
            ),
        },
        {
            "reference": SATHER,
            "snippet": (
                "Hna limits phage spread by initiating abortive infection in "
                "response to a phage protein"
            ),
            "notes": (
                "Sather et al. support abortive infection in response to a "
                "phage-encoded protein as the Hna phage-defense output."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:382",
            "taxon_label": "Sinorhizobium meliloti",
            "note": (
                "Sather et al. showed that Sinorhizobium meliloti Hna "
                "provides protection against diverse bacteriophages and "
                "triggers abortive infection in phage-infected cells."
            ),
            "reference": SATHER,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "hna_ssb_triggered_abortive_infection",
            "title": (
                "Hna nuclease activation couples phage SSB challenge to "
                "abortive infection"
            ),
            "description": (
                "Evidence-backed process sketch linking an Hna locus to "
                "phage single-stranded DNA-binding protein challenge, "
                "dysregulated helicase/nuclease activity, abortive "
                "infection, and inhibition of phage spread."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Sather et al. and Hooper et al. Hna "
                "phage-SSB-triggered abortive infection evidence without "
                "asserting one universal phage trigger, escape route, DNA "
                "substrate, ATP-concentration gate, or host-cell-death "
                "timing across all Hna homologs."
            ),
            "nodes": [
                {
                    "node_id": "hna_locus",
                    "label": "Hna locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-effector Hna phage-defense locus encoding "
                        "an SF2 helicase/nuclease immune protein."
                    ),
                },
                {
                    "node_id": "phage_ssb_stimulation",
                    "label": "phage SSB stimulation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Stimulation of Hna by a phage-encoded "
                        "single-stranded DNA-binding protein."
                    ),
                },
                {
                    "node_id": "hna_nuclease_activation",
                    "label": "Hna nuclease activation",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "Dysregulated activation of Hna nuclease activity "
                        "after phage single-stranded DNA-binding protein "
                        "challenge."
                    ),
                },
                {
                    "node_id": "abortive_infection_response",
                    "label": "abortive infection response",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Host cell death after infection that prevents "
                        "release of bacteriophage progeny."
                    ),
                },
                {
                    "node_id": "hna_system_trait",
                    "label": "Hna system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000241",
                    "description": (
                        "Possession of a genome-encoded Hna phage-defense "
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
                    "subject": "hna_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "hna_nuclease_activation",
                    "description": (
                        "Hna loci encode SF2 helicase/nuclease proteins "
                        "whose conserved helicase and nuclease motifs are "
                        "required for viral defense."
                    ),
                    "evidence": [
                        {
                            "reference": SATHER,
                            "snippet": (
                                "mutagenesis of these motifs inactivating "
                                "viral defense"
                            ),
                            "notes": (
                                "Sather et al. connect Hna helicase and "
                                "nuclease motifs to antiphage activity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_ssb_stimulation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "hna_nuclease_activation",
                    "description": (
                        "A phage-encoded single-stranded DNA-binding "
                        "protein stimulates Hna and shifts it toward "
                        "dysregulated nuclease activation."
                    ),
                    "evidence": [
                        {
                            "reference": SATHER,
                            "snippet": (
                                "A similar host cell response is triggered in "
                                "cells containing Hna upon expression of a "
                                "phage-encoded single-stranded DNA binding "
                                "protein (SSB)"
                            ),
                            "notes": (
                                "Sather et al. support Hna response to a "
                                "phage SSB independently of whole-phage "
                                "infection."
                            ),
                        },
                        {
                            "reference": HOOPER,
                            "snippet": (
                                "shifts catalytic partitioning toward "
                                "dysregulated nuclease activation"
                            ),
                            "notes": (
                                "Hooper et al. directly connect phage SSB "
                                "stimulation to Hna nuclease activation."
                            ),
                        },
                    ],
                },
                {
                    "subject": "hna_nuclease_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abortive_infection_response",
                    "description": (
                        "Dysregulated Hna nuclease activation damages DNA, "
                        "causes cellular toxicity, and contributes to the "
                        "abortive infection response."
                    ),
                    "evidence": [
                        {
                            "reference": HOOPER,
                            "snippet": (
                                "Disruption of this balance enhances DNA "
                                "cleavage and causes cellular toxicity"
                            ),
                            "notes": (
                                "Hooper et al. support Hna nuclease "
                                "dysregulation as a toxic DNA-cleavage "
                                "output."
                            ),
                        },
                        {
                            "reference": SATHER,
                            "snippet": (
                                "infected cells carrying the system die but "
                                "do not release phage progeny"
                            ),
                            "notes": (
                                "Sather et al. support the abortive "
                                "infection host-cell fate of Hna-containing "
                                "cells."
                            ),
                        },
                    ],
                },
                {
                    "subject": "abortive_infection_response",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hna_system_trait",
                    "description": (
                        "Hna-mediated abortive infection is the "
                        "phage-defense output that realizes the Hna system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": SATHER,
                            "snippet": (
                                "Hna limits phage spread by initiating "
                                "abortive infection in response to a phage "
                                "protein"
                            ),
                            "notes": (
                                "Sather et al. support abortive infection "
                                "as the Hna antiviral output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "hna_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Hna system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": HOOPER,
                            "snippet": (
                                "Hna is a broadly distributed anti-phage "
                                "immune system"
                            ),
                            "notes": (
                                "Hooper et al. place Hna in the "
                                "anti-phage immune-system family."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "hna-trigger-and-family-breadth-gap",
            "prompt": (
                "Resolve Hna trigger breadth, phage escape routes, and "
                "family architecture before minting narrower Hna mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Sather et al. support Sinorhizobium Hna abortive infection "
                "after phage infection or phage SSB expression, and Hooper "
                "et al. support 5A SSB stimulation of nuclease activation, "
                "but Hna homologs need separate review before TraitMech "
                "asserts one universal phage trigger, ATP-dependent "
                "activation gate, DNA substrate, escape route, or host death "
                "timing across the full Hna family."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-18",
        }
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
            "Minted Hna system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v118."
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
