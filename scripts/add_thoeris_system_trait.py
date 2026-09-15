#!/usr/bin/env python3
"""Add the Thoeris system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "thoeris_system.yaml"

KA = "DOI:10.1038/s41467-020-16703-w"
OFIR = "DOI:10.1038/s41586-021-04098-7"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T13:11:03Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000216",
    "label": "Thoeris system",
    "definition": (
        "A genomics trait describing possession of a Thoeris antiphage "
        "defense locus in which phage-triggered TIR-domain proteins generate "
        "a cyclic-ADP-ribose-like signal that activates a ThsA NADase effector "
        "to deplete NAD and inhibit bacteriophage replication."
    ),
    "definition_source": OFIR,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Thoeris defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": KA,
        },
        {
            "synonym_text": "Thoeris defence system",
            "synonym_type": "EXACT_SYNONYM",
            "source": OFIR,
        },
    ],
    "evidence": [
        {
            "reference": KA,
            "snippet": (
                "One such system is the Thoeris defense system, which "
                "consists of two genes, thsA and thsB"
            ),
            "notes": (
                "Ka et al. support the two-component B. cereus Thoeris "
                "system architecture and its standard US-English name."
            ),
        },
        {
            "reference": KA,
            "snippet": (
                "Mutation analysis suggests that NAD+ cleavage is linked to "
                "the antiphage function of Thoeris"
            ),
            "notes": (
                "Ka et al. support the relationship between ThsA NADase "
                "activity and Thoeris antiphage function."
            ),
        },
        {
            "reference": OFIR,
            "snippet": (
                "phage infection triggers Thoeris TIR-domain proteins to "
                "produce an isomer of cyclic ADP-ribose"
            ),
            "notes": (
                "Ofir et al. support the phage-triggered TIR-domain signal "
                "production that activates the ThsA effector."
            ),
        },
        {
            "reference": OFIR,
            "snippet": (
                "This molecular signal activates a second protein, ThsA, "
                "which then depletes the cell of the essential molecule "
                "nicotinamide adenine dinucleotide (NAD)"
            ),
            "notes": (
                "Ofir et al. connect the Thoeris TIR-domain signal to ThsA "
                "NAD depletion."
            ),
        },
        {
            "reference": KA,
            "snippet": (
                "One is from Bacillus cereus MSX-D12. The thsA gene and its "
                "downstream thsB gene conferred resistance against myophage "
                "infection when engineered into the model bacterium Bacillus "
                "subtilis BEST7003"
            ),
            "notes": (
                "Ka et al. summarize experimental validation of the native "
                "Bacillus cereus MSX-D12 Thoeris thsA-thsB locus."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1396",
            "taxon_label": "Bacillus cereus",
            "note": (
                "Ka et al. describe the Bacillus cereus MSX-D12 thsA-thsB "
                "Thoeris system that conferred resistance to myophage "
                "infection when engineered into a Thoeris-lacking Bacillus "
                "subtilis host."
            ),
            "reference": KA,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "thoeris_tir_signal_nad_depletion_defense",
            "title": "Thoeris TIR signalling activates ThsA NAD depletion",
            "description": (
                "Evidence-backed process sketch linking a Thoeris locus to "
                "phage-triggered TIR-domain signalling, ThsA-dependent NAD "
                "depletion, and inhibition of bacteriophage replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the characterized Thoeris TIR-signal and "
                "ThsA NADase outputs without asserting one universal number "
                "of TIR-domain proteins, exact cADPR isomer structure, ThsA "
                "oligomeric state, cell-death pathway, or phage trigger "
                "across all Thoeris loci."
            ),
            "nodes": [
                {
                    "node_id": "phage_infection",
                    "label": "phage infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Entry and replication attempt by a bacteriophage "
                        "inside a bacterial host."
                    ),
                },
                {
                    "node_id": "thoeris_locus",
                    "label": "Thoeris locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Thoeris antiphage defense locus encoding a ThsA "
                        "NADase effector and one or more Thoeris TIR-domain "
                        "sensor proteins."
                    ),
                },
                {
                    "node_id": "thoeris_tir_signal_production",
                    "label": "Thoeris TIR cADPR-isomer production",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Phage-triggered production of a cyclic-ADP-ribose "
                        "isomer by Thoeris TIR-domain proteins."
                    ),
                },
                {
                    "node_id": "thsa_nad_depletion",
                    "label": "ThsA NAD depletion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Thoeris signal-activated ThsA NADase activity that "
                        "depletes intracellular nicotinamide adenine "
                        "dinucleotide."
                    ),
                },
                {
                    "node_id": "phage_replication",
                    "label": "phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication of invading bacteriophage DNA after "
                        "host-cell entry."
                    ),
                },
                {
                    "node_id": "thoeris_system_trait",
                    "label": "Thoeris system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000216",
                    "description": (
                        "Possession of a genome-encoded Thoeris antiphage "
                        "defense locus."
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
                    "subject": "thoeris_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "thoeris_tir_signal_production",
                    "description": (
                        "The Thoeris locus encodes TIR-domain proteins that "
                        "produce a cADPR-like signal during phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": OFIR,
                            "snippet": (
                                "phage infection triggers Thoeris TIR-domain "
                                "proteins to produce an isomer of cyclic "
                                "ADP-ribose"
                            ),
                            "notes": (
                                "Ofir et al. support Thoeris TIR-domain "
                                "proteins as phage-triggered cADPR-isomer "
                                "producers."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_infection",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "thoeris_tir_signal_production",
                    "description": (
                        "Phage infection activates production of the Thoeris "
                        "TIR-domain cADPR-like signal."
                    ),
                    "evidence": [
                        {
                            "reference": OFIR,
                            "snippet": (
                                "phage infection triggers Thoeris TIR-domain "
                                "proteins to produce an isomer of cyclic "
                                "ADP-ribose"
                            ),
                            "notes": (
                                "Ofir et al. support phage-triggered Thoeris "
                                "signal production."
                            ),
                        }
                    ],
                },
                {
                    "subject": "thoeris_tir_signal_production",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "thsa_nad_depletion",
                    "description": (
                        "The Thoeris cADPR-like signal activates ThsA, which "
                        "then depletes cellular NAD."
                    ),
                    "evidence": [
                        {
                            "reference": OFIR,
                            "snippet": (
                                "This molecular signal activates a second "
                                "protein, ThsA, which then depletes the cell "
                                "of the essential molecule nicotinamide "
                                "adenine dinucleotide (NAD)"
                            ),
                            "notes": (
                                "Ofir et al. connect the TIR-derived signal "
                                "to ThsA-mediated NAD depletion."
                            ),
                        }
                    ],
                },
                {
                    "subject": "thsa_nad_depletion",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "ThsA NAD depletion helps inhibit bacteriophage "
                        "replication."
                    ),
                    "evidence": [
                        {
                            "reference": KA,
                            "snippet": (
                                "highlighting a unique strategy for bacterial "
                                "antiphage resistance via NAD+ degradation"
                            ),
                            "notes": (
                                "Ka et al. place ThsA-linked NAD degradation "
                                "in Thoeris antiphage resistance."
                            ),
                        }
                    ],
                },
                {
                    "subject": "thsa_nad_depletion",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "thoeris_system_trait",
                    "description": (
                        "ThsA NAD depletion is the antiviral output that "
                        "realizes the Thoeris system defense phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": OFIR,
                            "snippet": (
                                "depletes the cell of the essential molecule "
                                "nicotinamide adenine dinucleotide (NAD) and "
                                "leads to abortive infection and cell death"
                            ),
                            "notes": (
                                "Ofir et al. support NAD depletion as the "
                                "Thoeris output that drives abortive infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "thoeris_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Thoeris system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": OFIR,
                            "snippet": (
                                "bacterial anti-phage defence system called "
                                "Thoeris"
                            ),
                            "notes": (
                                "Ofir et al. place Thoeris in the bacterial "
                                "antiphage-defense-system family."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "thoeris-family-signal-and-trigger-gap",
            "prompt": (
                "Resolve Thoeris family architecture, signal chemistry, and "
                "phage triggering before minting narrower Thoeris mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Ka et al. support the B. cereus ThsA/ThsB two-gene system "
                "and Ofir et al. support the TIR-produced cADPR-like signal "
                "that activates ThsA NAD depletion, but Thoeris variants need "
                "separate review before TraitMech asserts one exact number of "
                "TIR-domain proteins, cADPR-isomer chemistry, TIR target, "
                "ThsA activation state, cell-death pathway, or "
                "phage-triggering mechanism."
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
            "Minted Thoeris system as a DOI-backed GENOMICS TraitRecord under "
            "the phage defense system parent after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or prior "
            "proposal record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v93."
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
