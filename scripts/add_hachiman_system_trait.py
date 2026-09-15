#!/usr/bin/env python3
"""Add the Hachiman system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hachiman_system.yaml"

TUCK = "DOI:10.1016/j.cell.2024.09.020"
CUI = "DOI:10.1038/s41467-025-57851-1"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T14:47:54Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000219",
    "label": "Hachiman system",
    "definition": (
        "A genomics trait describing possession of a Hachiman antiphage "
        "defense locus encoding a HamA/HamB nuclease-helicase core that "
        "restricts bacteriophage propagation through DNA cleavage."
    ),
    "definition_source": TUCK,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Hachiman antiphage defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": TUCK,
        },
        {
            "synonym_text": "Hachiman defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": CUI,
        },
    ],
    "evidence": [
        {
            "reference": TUCK,
            "snippet": (
                "Hachiman is a broad-spectrum antiphage defense system of "
                "unknown function"
            ),
            "notes": (
                "Tuck et al. support Hachiman as a named broad-spectrum "
                "antiphage system."
            ),
        },
        {
            "reference": TUCK,
            "snippet": (
                "Hachiman is a heterodimeric nuclease-helicase complex, "
                "HamAB"
            ),
            "notes": (
                "Tuck et al. support the HamA/HamB nuclease-helicase core "
                "of characterized Hachiman systems."
            ),
        },
        {
            "reference": TUCK,
            "snippet": (
                "When the HamAB complex detects DNA damage, HamB helicase "
                "activity activates HamA, unleashing nuclease activity"
            ),
            "notes": (
                "Tuck et al. connect HamB helicase activity with HamA "
                "nuclease activation after DNA-damage detection."
            ),
        },
        {
            "reference": TUCK,
            "snippet": (
                "Hachiman activation degrades all DNA in the cell, creating "
                '"phantom" cells devoid of both phage and host DNA'
            ),
            "notes": (
                "Tuck et al. support nonspecific DNA degradation as the "
                "type I-A Hachiman antiviral output."
            ),
        },
        {
            "reference": CUI,
            "snippet": (
                "The Hachiman system is a novel prokaryotic antiphage "
                "defense system comprising HamA and HamB proteins"
            ),
            "notes": (
                "Cui et al. support the recurring Hachiman system name and "
                "its HamA/HamB composition."
            ),
        },
        {
            "reference": CUI,
            "snippet": (
                "HamA interacts with HamB to form a heterodimer HamAB to "
                "mediate ATP hydrolysis and execute DNA cleavage, thus "
                "implementing antiphage defense"
            ),
            "notes": (
                "Cui et al. support a type I-B HamAB heterodimer that "
                "couples ATP hydrolysis to antiphage DNA cleavage."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Tuck et al. identified Hachiman loci in E. coli ECOR04, "
                "ECOR28, and ECOR31, and showed that ECOR31 HamAB reduced "
                "plaquing by diverse double-stranded DNA phages."
            ),
            "reference": TUCK,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "hachiman_hamab_dna_cleavage",
            "title": "Hachiman HamAB complexes cleave DNA during antiphage defense",
            "description": (
                "Evidence-backed process sketch linking a Hachiman locus to "
                "HamAB nuclease-helicase activity, cellular DNA degradation, "
                "and inhibition of bacteriophage progeny production."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures characterized type I-A and type I-B "
                "Hachiman nuclease-helicase outputs without asserting one "
                "universal DNA-damage trigger, DNA substrate, active "
                "nuclease domain, HamC accessory role, Cap4 architecture, "
                "phage breadth, or abortive-infection pathway across all "
                "Hachiman loci."
            ),
            "nodes": [
                {
                    "node_id": "hachiman_locus",
                    "label": "Hachiman locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Hachiman antiphage defense locus encoding a "
                        "HamA/HamB nuclease-helicase core and, in some type "
                        "II systems, an accessory HamC component."
                    ),
                },
                {
                    "node_id": "hamab_complex_assembly",
                    "label": "HamAB complex assembly",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Formation of a Hachiman HamA/HamB "
                        "nuclease-helicase complex capable of ATP-dependent "
                        "DNA processing."
                    ),
                },
                {
                    "node_id": "hachiman_dna_cleavage",
                    "label": "Hachiman DNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "HamAB-mediated cleavage or degradation of DNA "
                        "during Hachiman activation."
                    ),
                },
                {
                    "node_id": "phage_particle_production",
                    "label": "phage particle production",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Production of new infectious bacteriophage particles "
                        "inside an infected bacterial host."
                    ),
                },
                {
                    "node_id": "hachiman_system_trait",
                    "label": "Hachiman system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000219",
                    "description": (
                        "Possession of a genome-encoded Hachiman antiphage "
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
                    "subject": "hachiman_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "hamab_complex_assembly",
                    "description": (
                        "Hachiman loci encode HamA and HamB components that "
                        "assemble into HamAB nuclease-helicase complexes."
                    ),
                    "evidence": [
                        {
                            "reference": TUCK,
                            "snippet": (
                                "One such system is Hachiman, a two-gene "
                                "locus encoding HamA"
                            ),
                            "notes": (
                                "Tuck et al. support HamA/HamB as the "
                                "two-gene Hachiman locus core."
                            ),
                        },
                        {
                            "reference": CUI,
                            "snippet": (
                                "The Hachiman system is a novel prokaryotic "
                                "antiphage defense system comprising HamA "
                                "and HamB proteins"
                            ),
                            "notes": (
                                "Cui et al. also support HamA/HamB as the "
                                "core Hachiman components."
                            ),
                        },
                    ],
                },
                {
                    "subject": "hamab_complex_assembly",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "hachiman_dna_cleavage",
                    "description": (
                        "HamA/HamB complexation enables ATP-dependent DNA "
                        "cleavage by Hachiman systems."
                    ),
                    "evidence": [
                        {
                            "reference": TUCK,
                            "snippet": (
                                "When the HamAB complex detects DNA damage, "
                                "HamB helicase activity activates HamA, "
                                "unleashing nuclease activity"
                            ),
                            "notes": (
                                "Tuck et al. connect HamAB activation with "
                                "HamA nuclease activity."
                            ),
                        },
                        {
                            "reference": CUI,
                            "snippet": (
                                "HamA interacts with HamB to form a "
                                "heterodimer HamAB to mediate ATP "
                                "hydrolysis and execute DNA cleavage"
                            ),
                            "notes": (
                                "Cui et al. support ATP-hydrolysis-coupled "
                                "DNA cleavage by a type I-B HamAB "
                                "heterodimer."
                            ),
                        },
                    ],
                },
                {
                    "subject": "hachiman_dna_cleavage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_particle_production",
                    "description": (
                        "Hachiman-mediated DNA degradation inhibits the "
                        "generation of new phage particles."
                    ),
                    "evidence": [
                        {
                            "reference": TUCK,
                            "snippet": (
                                "Hachiman activation degrades all DNA in "
                                "the cell"
                            ),
                            "notes": (
                                "Tuck et al. support DNA degradation as the "
                                "activated Hachiman output."
                            ),
                        },
                        {
                            "reference": TUCK,
                            "snippet": (
                                "We confirmed that Hachiman limits the "
                                "production of new phage particles"
                            ),
                            "notes": (
                                "Tuck et al. connect Hachiman activity to "
                                "restriction of phage progeny production."
                            ),
                        },
                    ],
                },
                {
                    "subject": "hachiman_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hachiman_system_trait",
                    "description": (
                        "HamAB-mediated DNA cleavage is the antiviral output "
                        "that realizes the Hachiman system trait."
                    ),
                    "evidence": [
                        {
                            "reference": CUI,
                            "snippet": (
                                "execute DNA cleavage, thus implementing "
                                "antiphage defense"
                            ),
                            "notes": (
                                "Cui et al. support DNA cleavage as an "
                                "antiphage output of the Hachiman complex."
                            ),
                        }
                    ],
                },
                {
                    "subject": "hachiman_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Hachiman system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": CUI,
                            "snippet": (
                                "The Hachiman system is a novel prokaryotic "
                                "antiphage defense system"
                            ),
                            "notes": (
                                "Cui et al. place Hachiman in the "
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
            "discussion_id": "hachiman-subtype-and-trigger-gap",
            "prompt": (
                "Resolve Hachiman subtype effectors, DNA substrates, and "
                "activation triggers before minting narrower Hachiman "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Tuck et al. support DNA-damage-triggered type I-A HamAB "
                "activation and Cui et al. support type I-B HamAB ATPase "
                "and DNA-cleavage activity, but Hachiman variants need "
                "separate review before TraitMech asserts one universal "
                "triggering DNA substrate, HamA catalytic domain, HamC "
                "accessory role, Cap4 fusion architecture, phage range, or "
                "abortive-infection output."
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
            "Minted Hachiman system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v96."
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
