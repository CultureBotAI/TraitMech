#!/usr/bin/env python3
"""Add the CBASS system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "cbass_system.yaml"

COHEN = "DOI:10.1038/s41586-019-1605-5"
MILLMAN = "DOI:10.1038/s41564-020-0777-y"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T10:20:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000212",
    "label": "CBASS system",
    "definition": (
        "A genomics trait describing possession of a "
        "cyclic-oligonucleotide-based antiphage signaling locus in which an "
        "oligonucleotide cyclase produces cyclic oligonucleotide signals "
        "during phage infection that activate an effector to inhibit "
        "bacteriophage replication."
    ),
    "definition_source": COHEN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": (
                "cyclic-oligonucleotide-based anti-phage signalling system"
            ),
            "synonym_type": "EXACT_SYNONYM",
            "source": MILLMAN,
        },
        {
            "synonym_text": (
                "cyclic-oligonucleotide-based anti-phage signaling system"
            ),
            "synonym_type": "EXACT_SYNONYM",
            "source": MILLMAN,
        },
    ],
    "evidence": [
        {
            "reference": COHEN,
            "snippet": (
                "cGAMP signalling is part of an antiphage defence system that "
                "is common in bacteria"
            ),
            "notes": (
                "Cohen et al. experimentally established a bacterial "
                "cGAS-phospholipase system as a common antiphage defense "
                "system."
            ),
        },
        {
            "reference": COHEN,
            "snippet": "Phage infection triggers the production of cGAMP",
            "notes": (
                "Cohen et al. support phage-triggered cyclic "
                "oligonucleotide production in an experimentally "
                "characterized cGAMP-phospholipase CBASS."
            ),
        },
        {
            "reference": MILLMAN,
            "snippet": (
                "CBASS systems are composed of an oligonucleotide cyclase, "
                "which generates signalling cyclic oligonucleotides in "
                "response to phage infection"
            ),
            "notes": (
                "Millman et al. generalized CBASS systems as "
                "oligonucleotide-cyclase-centered antiphage signaling loci."
            ),
        },
        {
            "reference": MILLMAN,
            "snippet": (
                "identified more than 5,000 CBASS systems, which have diverse "
                "architectures"
            ),
            "notes": (
                "Millman et al. support CBASS as a diverse recurring family "
                "across bacterial and archaeal genomes rather than a single "
                "four-gene operon."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:913088",
            "taxon_label": "Escherichia coli TW11681",
            "note": (
                "Cohen et al. cloned the native E. coli TW11681 four-gene "
                "CBASS operon into E. coli MG1655 and measured P1 and "
                "coliphage resistance."
            ),
            "reference": COHEN,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "cbass_cyclic_oligonucleotide_antiphage_defense",
            "title": "CBASS cyclic oligonucleotides activate abortive cell death",
            "description": (
                "Evidence-backed process sketch linking CBASS "
                "oligonucleotide-cyclase activation to effector activation, "
                "abortive cell death, and blocked phage replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the shared system-level CBASS logic of "
                "phage-triggered cyclic oligonucleotide synthesis and "
                "effector activation across multiple effector subtypes. The "
                "subtype-specific protein families carry the exact "
                "mechanistic edges and remain shifted from this first "
                "organism-level trait."
            ),
            "nodes": [
                {
                    "node_id": "cbass_oligonucleotide_cyclase_activation",
                    "label": "CBASS oligonucleotide cyclase activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Phage-infection-associated activation of a CBASS "
                        "oligonucleotide cyclase."
                    ),
                },
                {
                    "node_id": "cyclic_oligonucleotide_synthesis",
                    "label": "CBASS cyclic oligonucleotide synthesis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Production of cyclic oligonucleotide second "
                        "messengers by an activated CBASS oligonucleotide "
                        "cyclase."
                    ),
                },
                {
                    "node_id": "cbass_effector_activation",
                    "label": "CBASS effector activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of a CBASS effector by a cyclic "
                        "oligonucleotide signal."
                    ),
                },
                {
                    "node_id": "abortive_cell_death",
                    "label": "abortive cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Programmed death of an infected host cell before "
                        "phage replication is completed."
                    ),
                },
                {
                    "node_id": "phage_replication",
                    "label": "phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication and completion of a bacteriophage "
                        "infection cycle inside a host cell."
                    ),
                },
                {
                    "node_id": "cbass_system_trait",
                    "label": "CBASS system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000212",
                    "description": (
                        "Possession of a genome-encoded CBASS phage defense "
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
                    "subject": "cbass_oligonucleotide_cyclase_activation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "cyclic_oligonucleotide_synthesis",
                    "description": (
                        "Phage sensing activates a CBASS oligonucleotide "
                        "cyclase to synthesize cyclic oligonucleotide "
                        "signals."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "oligonucleotide cyclase, which generates "
                                "signalling cyclic oligonucleotides in "
                                "response to phage infection"
                            ),
                            "notes": (
                                "Millman et al. summarize phage-triggered "
                                "oligonucleotide cyclase activation in their "
                                "general CBASS model."
                            ),
                        }
                    ],
                },
                {
                    "subject": "cyclic_oligonucleotide_synthesis",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "cbass_effector_activation",
                    "description": (
                        "CBASS cyclic oligonucleotide second messengers "
                        "activate cognate effector proteins."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "an effector that is activated by the cyclic "
                                "oligonucleotides and promotes cell death"
                            ),
                            "notes": (
                                "Millman et al. support effector activation "
                                "as the central output of CBASS cyclic "
                                "oligonucleotide signaling."
                            ),
                        }
                    ],
                },
                {
                    "subject": "cbass_effector_activation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "abortive_cell_death",
                    "description": (
                        "CBASS effector activation induces host cell death "
                        "through subtype-specific nuclease, phospholipase, or "
                        "other toxic activities."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "six effector subtypes that promote cell death "
                                "by membrane impairment, DNA degradation or "
                                "other means"
                            ),
                            "notes": (
                                "Millman et al. classified multiple CBASS "
                                "effector subtypes that converge on host cell "
                                "death."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abortive_cell_death",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "CBASS-induced death of the infected host cell aborts "
                        "infection before phage replication is completed."
                    ),
                    "evidence": [
                        {
                            "reference": COHEN,
                            "snippet": (
                                "to cell death before completion of phage "
                                "reproduction"
                            ),
                            "notes": (
                                "Cohen et al. experimentally tied CBASS "
                                "cGAMP-phospholipase signaling to abortive "
                                "cell death before the phage cycle completed."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abortive_cell_death",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "cbass_system_trait",
                    "description": (
                        "CBASS effector-induced abortive cell death realizes "
                        "CBASS-mediated antiphage defense."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "therefore preventing the spread of phages to "
                                "nearby cells"
                            ),
                            "notes": (
                                "Millman et al. link cell death before phage "
                                "replication completion to the protective "
                                "output of CBASS loci."
                            ),
                        }
                    ],
                },
                {
                    "subject": "cbass_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "CBASS possession is a "
                        "cyclic-oligonucleotide-mediated phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": MILLMAN,
                            "snippet": (
                                "a family of defence systems against "
                                "bacteriophages"
                            ),
                            "notes": (
                                "Millman et al. place CBASS in the phage "
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
            "discussion_id": "cbass-subtype-mechanism-gap",
            "prompt": (
                "Resolve CBASS subtype-specific sensing and effector "
                "mechanisms before splitting cGAMP-phospholipase, "
                "cAAA-nuclease, ancillary-gene, or individual CD-NTase "
                "protein-family edges into reviewed graph groundings."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Cohen et al. resolved a phage-triggered "
                "cGAMP-phospholipase CBASS system and Millman et al. "
                "classified CBASS loci into four major types with multiple "
                "signaling molecules, effectors, and ancillary genes; exact "
                "phage sensors and subtype-specific effector families remain "
                "shifted from this first organism-level trait."
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
            "Minted CBASS system as a DOI-backed GENOMICS TraitRecord under "
            "the phage defense system parent after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or prior "
            "proposal record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v89."
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
