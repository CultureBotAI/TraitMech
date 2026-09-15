#!/usr/bin/env python3
"""Add the Lamassu system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "lamassu_system.yaml"

DORON = "DOI:10.1126/science.aar4120"
HAUDIQUET = "DOI:10.1073/pnas.2519643122"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T23:14:40Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000232",
    "label": "Lamassu system",
    "definition": (
        "A phage defense system in which an organism possesses a Lamassu "
        "locus built around a conserved SMC-like LmuB sensor paired with a "
        "modular LmuA effector and subfamily-specific partner architecture, "
        "enabling viral-DNA sensing and effector-mediated antiviral activity."
    ),
    "definition_source": HAUDIQUET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Lamassu",
            "synonym_type": "EXACT_SYNONYM",
            "source": HAUDIQUET,
        }
    ],
    "evidence": [
        {
            "reference": DORON,
            "snippet": (
                "Lamassu LmuAB pfam14130, pfam02463 SMC ATPase N-terminal "
                "domain 697 682 (1.3%)"
            ),
            "notes": (
                "Doron et al. reported Lamassu/LmuAB as an SMC-ATPase-linked "
                "system in their pangenome-scale antiphage-system discovery "
                "screen."
            ),
        },
        {
            "reference": HAUDIQUET,
            "snippet": (
                "Lamassu is a widespread antiviral system in bacteria that "
                "uses structural maintenance of chromosomes-like proteins"
            ),
            "notes": (
                "Haudiquet et al. support defining Lamassu as a recurring "
                "bacterial antiviral system with an SMC-like component."
            ),
        },
        {
            "reference": HAUDIQUET,
            "snippet": (
                "a bacterial immune system family featuring diverse effectors "
                "but a core conserved SMC-like sensor"
            ),
            "notes": (
                "Haudiquet et al. support placing Lamassu at the family level "
                "rather than defining a single effector subtype."
            ),
        },
        {
            "reference": HAUDIQUET,
            "snippet": (
                "It comprises LmuB, an SMC-like protein, LmuC, a small protein "
                "with a domain of unknown function, and LmuA"
            ),
            "notes": (
                "Haudiquet et al. support the LmuA/LmuB/LmuC composition of "
                "the structurally characterized Lamassu Vc-Cap4 branch."
            ),
        },
        {
            "reference": HAUDIQUET,
            "snippet": (
                "Lamassu specifically senses dsDNA ends in vitro and phage "
                "replication origins in vivo"
            ),
            "notes": (
                "Haudiquet et al. connect Lamassu to direct DNA-end and phage "
                "replication origin sensing."
            ),
        },
        {
            "reference": HAUDIQUET,
            "snippet": (
                "triggering the formation of LmuA tetramers that activate its "
                "Cap4 nuclease domain"
            ),
            "notes": (
                "Haudiquet et al. connect viral-DNA sensing to LmuA tetramer "
                "formation and Cap4 nuclease-domain activation in Lamassu "
                "Vc-Cap4."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:666",
            "taxon_label": "Vibrio cholerae",
            "note": (
                "Haudiquet et al. structurally characterized the Vibrio "
                "cholerae Lamassu Vc-Cap4 system and connected its LmuABC "
                "complex to dsDNA-end sensing and LmuA Cap4 nuclease-domain "
                "activation."
            ),
            "reference": HAUDIQUET,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "lamassu_smc_dna_sensing_nuclease_activation",
            "title": (
                "Lamassu SMC-like complexes activate LmuA antiviral effectors"
            ),
            "description": (
                "Evidence-backed process sketch linking a Lamassu locus to "
                "LmuABC complex formation, viral DNA sensing, LmuA effector "
                "activation, and inhibition of bacteriophage infection."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the structurally characterized Lamassu "
                "Vc-Cap4 system without asserting one exact effector domain, "
                "LmuC requirement, LmuB clade, zinc-hook architecture, viral "
                "DNA cue, cell-death output, or phage breadth across all "
                "Lamassu loci."
            ),
            "nodes": [
                {
                    "node_id": "lamassu_locus",
                    "label": "Lamassu locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Lamassu antiviral locus built around an SMC-like "
                        "LmuB core and a cognate LmuA effector."
                    ),
                },
                {
                    "node_id": "lmuabc_complex_assembly",
                    "label": "LmuABC complex assembly",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Assembly of LmuA, SMC-like LmuB, and LmuC into a "
                        "Lamassu Vc-Cap4 complex."
                    ),
                },
                {
                    "node_id": "lamassu_viral_dna_sensing",
                    "label": "Lamassu viral DNA sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Lamassu-mediated sensing of viral double-stranded "
                        "DNA ends or phage replication origins."
                    ),
                },
                {
                    "node_id": "lmuA_effector_activation",
                    "label": "LmuA effector activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Oligomerization-dependent activation of a LmuA "
                        "effector nuclease domain."
                    ),
                },
                {
                    "node_id": "phage_infection",
                    "label": "phage infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Bacteriophage infection and propagation inside a "
                        "bacterial host cell."
                    ),
                },
                {
                    "node_id": "lamassu_system_trait",
                    "label": "Lamassu system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000232",
                    "description": (
                        "Possession of a genome-encoded Lamassu phage-defense "
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
                    "subject": "lamassu_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "lmuabc_complex_assembly",
                    "description": (
                        "The characterized Lamassu Vc-Cap4 locus encodes "
                        "LmuA, SMC-like LmuB, and LmuC components."
                    ),
                    "evidence": [
                        {
                            "reference": HAUDIQUET,
                            "snippet": (
                                "It comprises LmuB, an SMC-like protein, "
                                "LmuC, a small protein with a domain of "
                                "unknown function, and LmuA"
                            ),
                            "notes": (
                                "Haudiquet et al. support the LmuABC "
                                "composition of the Lamassu Vc-Cap4 branch."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lmuabc_complex_assembly",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "lamassu_viral_dna_sensing",
                    "description": (
                        "Lamassu complexes bind double-stranded DNA and "
                        "sense DNA ends or phage replication origins."
                    ),
                    "evidence": [
                        {
                            "reference": HAUDIQUET,
                            "snippet": (
                                "Lamassu specifically senses dsDNA ends in "
                                "vitro and phage replication origins in vivo"
                            ),
                            "notes": (
                                "Haudiquet et al. connect Lamassu to direct "
                                "viral-DNA-associated sensing."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lamassu_viral_dna_sensing",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "lmuA_effector_activation",
                    "description": (
                        "Lamassu viral-DNA sensing triggers LmuA tetramer "
                        "formation and Cap4 nuclease-domain activation."
                    ),
                    "evidence": [
                        {
                            "reference": HAUDIQUET,
                            "snippet": (
                                "triggering the formation of LmuA tetramers "
                                "that activate its Cap4 nuclease domain"
                            ),
                            "notes": (
                                "Haudiquet et al. connect Lamassu DNA "
                                "sensing to LmuA Cap4 nuclease-domain "
                                "activation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lmuA_effector_activation",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_infection",
                    "description": (
                        "Lamassu effector activation helps halt phage "
                        "infection in the bacterial host."
                    ),
                    "evidence": [
                        {
                            "reference": HAUDIQUET,
                            "snippet": (
                                "Lamassu is a widespread antiviral system in "
                                "bacteria that uses structural maintenance "
                                "of chromosomes-like proteins, typically "
                                "associated with chromosome maintenance, to "
                                "detect and halt phage infection"
                            ),
                            "notes": (
                                "Haudiquet et al. support coupling Lamassu "
                                "SMC-like detection to inhibition of phage "
                                "infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lmuA_effector_activation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "lamassu_system_trait",
                    "description": (
                        "Viral-DNA-triggered LmuA effector activation "
                        "realizes the Lamassu system trait."
                    ),
                    "evidence": [
                        {
                            "reference": HAUDIQUET,
                            "snippet": (
                                "a bacterial immune system family featuring "
                                "diverse effectors but a core conserved "
                                "SMC-like sensor"
                            ),
                            "notes": (
                                "Haudiquet et al. support the shared "
                                "SMC-like sensor and diverse effector logic "
                                "of Lamassu immunity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lamassu_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Lamassu system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DORON,
                            "snippet": (
                                "Lamassu LmuAB pfam14130, pfam02463 SMC "
                                "ATPase N-terminal domain 697 682 (1.3%)"
                            ),
                            "notes": (
                                "Doron et al. reported Lamassu in a table of "
                                "candidate antiphage defense systems."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "lamassu-subtype-and-effector-gap",
            "prompt": (
                "Resolve Lamassu subtype architecture, effector diversity, "
                "and viral-DNA trigger specificity before minting narrower "
                "Lamassu mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Haudiquet et al. support a structurally characterized "
                "Vibrio cholerae Lamassu Vc-Cap4 system with LmuABC DNA-end "
                "sensing and LmuA Cap4 nuclease activation, but the first "
                "TraitRecord stays at the system level until separate review "
                "resolves long-versus-short LmuB clades, LmuC-independent "
                "subfamilies, effector-domain diversity, viral DNA triggers, "
                "and cell-death outputs across Lamassu loci."
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
            "Minted Lamassu system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v109."
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
