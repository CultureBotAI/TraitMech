#!/usr/bin/env python3
"""Add the abortive infection system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

LOPATINA = "DOI:10.1146/annurev-virology-011620-040628"
FINERAN = "DOI:10.1073/pnas.0808832106"
DY = "DOI:10.1093/nar/gkt1419"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T11:47:52Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000214",
    "label": "abortive infection system",
    "definition": (
        "A genomics trait describing possession of a bacteriophage "
        "abortive-infection defense system in which phage infection activates "
        "a host-encoded growth-arrest or cell-death program that prevents "
        "completion of phage replication and protects nearby bacterial cells."
    ),
    "definition_source": LOPATINA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Abi system",
            "synonym_type": "EXACT_SYNONYM",
            "source": DY,
        },
    ],
    "evidence": [
        {
            "reference": LOPATINA,
            "snippet": (
                "A commonly used phage resistance strategy is abortive "
                "infection (Abi), in which the infected cell commits suicide "
                "before the phage can complete its replication cycle"
            ),
            "notes": (
                "Lopatina et al. support abortive infection as a phage "
                "resistance strategy that blocks completion of the phage "
                "replication cycle."
            ),
        },
        {
            "reference": LOPATINA,
            "snippet": (
                "The Abi strategy is manifested by a plethora of "
                "mechanistically diverse defense systems that are abundant in "
                "bacterial genomes"
            ),
            "notes": (
                "Lopatina et al. support defining the trait at the broad Abi "
                "system level rather than as one toxin-antitoxin family."
            ),
        },
        {
            "reference": FINERAN,
            "snippet": (
                "Resistance strategies include the abortive infection (Abi) "
                "systems, which promote cell death and limit phage "
                "replication within a bacterial population"
            ),
            "notes": (
                "Fineran et al. summarize the cell-death and phage-limitation "
                "outputs of abortive infection systems."
            ),
        },
        {
            "reference": DY,
            "snippet": (
                "AbiE systems are encoded by bicistronic operons and function "
                "via a non-interacting (Type IV) bacteriostatic TA mechanism"
            ),
            "notes": (
                "Dy et al. support AbiE as a bacteriostatic toxin-antitoxin "
                "Abi family, one reason the parent record should cover "
                "growth arrest as well as cell death."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:29471",
            "taxon_label": "Pectobacterium atrosepticum",
            "note": (
                "Fineran et al. identified the native toxIN locus from "
                "Erwinia carotovora subspecies atroseptica 1039 and "
                "demonstrated ToxIN-mediated phage resistance."
            ),
            "reference": FINERAN,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abortive_infection_population_level_defense",
            "title": "Abortive infection halts infected cells to limit phage spread",
            "description": (
                "Evidence-backed process sketch linking phage-triggered Abi "
                "activation to infected-host growth arrest or death, "
                "restricted phage replication, and protection of nearby "
                "bacterial cells."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the shared Abi strategy without claiming "
                "that ToxIN, AbiQ, AbiE, and other abortive-infection "
                "families use one exact sensor, effector, toxin-antitoxin "
                "architecture, or cell-death mechanism."
            ),
            "nodes": [
                {
                    "node_id": "phage_infection",
                    "label": "phage infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Entry and intracellular replication attempt by a "
                        "bacteriophage infecting a host bacterium."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_activation",
                    "label": "abortive infection system activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Phage-infection-triggered activation of a host Abi "
                        "system."
                    ),
                },
                {
                    "node_id": "host_growth_arrest_or_cell_death",
                    "label": "host growth arrest or cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abi-system output in which an infected host cell "
                        "undergoes growth arrest or dies before productive "
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
                    "node_id": "bacterial_population_protection",
                    "label": "bacterial population protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced phage spread that protects nearby bacterial "
                        "cells in the same population."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage defense system."
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
                    "subject": "phage_infection",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "abortive_infection_system_activation",
                    "description": (
                        "Phage infection triggers Abi defense-system "
                        "activation."
                    ),
                    "evidence": [
                        {
                            "reference": DY,
                            "snippet": (
                                "Bacterial abortive infection (Abi) systems "
                                "are ‘altruistic’ cell death systems that are "
                                "activated by phage infection and limit viral "
                                "replication, thereby providing protection to "
                                "the bacterial population"
                            ),
                            "notes": (
                                "Dy et al. support phage-triggered activation "
                                "as a defining Abi-system behavior."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abortive_infection_system_activation",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "host_growth_arrest_or_cell_death",
                    "description": (
                        "Abi activation produces growth-arrest or cell-death "
                        "outputs through family-specific effectors."
                    ),
                    "evidence": [
                        {
                            "reference": FINERAN,
                            "snippet": (
                                "Resistance strategies include the abortive "
                                "infection (Abi) systems, which promote cell "
                                "death and limit phage replication within a "
                                "bacterial population"
                            ),
                            "notes": (
                                "Fineran et al. support cell death as an "
                                "abortive-infection output."
                            ),
                        },
                        {
                            "reference": DY,
                            "snippet": (
                                "AbiE systems are encoded by bicistronic "
                                "operons and function via a non-interacting "
                                "(Type IV) bacteriostatic TA mechanism"
                            ),
                            "notes": (
                                "Dy et al. support bacteriostasis as an AbiE "
                                "output, distinct from obligate cell death."
                            ),
                        },
                    ],
                },
                {
                    "subject": "host_growth_arrest_or_cell_death",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "Arrest or death of the infected host cell limits "
                        "completion of phage replication."
                    ),
                    "evidence": [
                        {
                            "reference": LOPATINA,
                            "snippet": (
                                "A commonly used phage resistance strategy is "
                                "abortive infection (Abi), in which the "
                                "infected cell commits suicide before the "
                                "phage can complete its replication cycle"
                            ),
                            "notes": (
                                "Lopatina et al. connect infected-cell death "
                                "to premature phage-cycle termination."
                            ),
                        }
                    ],
                },
                {
                    "subject": "host_growth_arrest_or_cell_death",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "bacterial_population_protection",
                    "description": (
                        "The local cost of infected-cell arrest or death "
                        "protects neighboring bacteria by limiting onward "
                        "phage spread."
                    ),
                    "evidence": [
                        {
                            "reference": LOPATINA,
                            "snippet": (
                                "Abi prevents the phage epidemic from "
                                "spreading to nearby cells, thus protecting "
                                "the bacterial colony"
                            ),
                            "notes": (
                                "Lopatina et al. support the population-level "
                                "benefit of abortive infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "host_growth_arrest_or_cell_death",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "Phage-triggered infected-host arrest or death "
                        "realizes the abortive-infection defense phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": FINERAN,
                            "snippet": (
                                "abortive infection (Abi) systems, which "
                                "promote cell death and limit phage "
                                "replication within a bacterial population"
                            ),
                            "notes": (
                                "Fineran et al. support cell death coupled to "
                                "limited phage replication as the Abi defense "
                                "output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abortive_infection_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Abortive-infection-system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": LOPATINA,
                            "snippet": (
                                "The Abi strategy is manifested by a plethora "
                                "of mechanistically diverse defense systems "
                                "that are abundant in bacterial genomes"
                            ),
                            "notes": (
                                "Lopatina et al. place abortive infection "
                                "among bacterial antiviral defense systems."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abortive-infection-subfamily-split-gap",
            "prompt": (
                "Resolve ToxIN/AbiQ, AbiE, and other abortive-infection "
                "families before minting narrower children under the broad "
                "abortive infection system parent."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Lopatina et al., Fineran et al., and Dy et al. support Abi "
                "as a genomically encoded phage defense strategy that spans "
                "mechanistically diverse families, including the ToxIN/AbiQ "
                "and AbiE toxin-antitoxin branches. Narrower TraitRecords "
                "will need separate review to ground each subfamily's "
                "trigger, effector, growth-arrest or cell-death mechanism, "
                "and phage escape routes."
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
            "Minted abortive infection system as a DOI-backed GENOMICS "
            "TraitRecord under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v91."
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
