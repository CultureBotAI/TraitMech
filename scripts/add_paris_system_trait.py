#!/usr/bin/env python3
"""Add the PARIS system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "paris_system.yaml"

ROUSSET = "DOI:10.1016/j.chom.2022.02.018"
DEEP = "DOI:10.1038/s41586-024-07772-8"
BURMAN = "DOI:10.1038/s41586-024-07874-3"

CURATOR = "codex"
TIMESTAMP = "2026-09-18T08:27:56Z"
REVIEW_TIMESTAMP = "2026-09-18T09:16:05Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000237",
    "label": "PARIS system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "phage anti-restriction-induced system locus encoding an AriA ABC "
        "ATPase sensor and an AriB TOPRIM-family nuclease whose activation "
        "by phage anti-restriction or other foreign proteins releases AriB "
        "to inhibit translation through lysine tRNA cleavage and block "
        "bacteriophage propagation."
    ),
    "definition_source": ROUSSET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "phage anti-restriction-induced system",
            "synonym_type": "EXACT_SYNONYM",
            "source": ROUSSET,
        },
        {
            "synonym_text": "phage antirestriction induced system",
            "synonym_type": "EXACT_SYNONYM",
            "source": BURMAN,
        },
    ],
    "evidence": [
        {
            "reference": ROUSSET,
            "snippet": (
                "We validate the activity of diverse systems and "
                "describe PARIS, an abortive infection system triggered "
                "by a phage-encoded anti-restriction protein"
            ),
            "notes": (
                "Rousset et al. support PARIS as a named abortive "
                "infection system activated by a phage anti-restriction "
                "protein."
            ),
        },
        {
            "reference": ROUSSET,
            "snippet": (
                "phage anti-restriction-induced system (PARIS), an "
                "abortive infection system that triggers growth arrest "
                "upon sensing an anti-restriction protein"
            ),
            "notes": (
                "Rousset et al. support the PARIS long-form name and the "
                "growth-arrest output of the system."
            ),
        },
        {
            "reference": DEEP,
            "snippet": (
                "operates as a toxin-antitoxin system, in which the "
                "antitoxin AriA sequesters and inactivates the toxin "
                "AriB until triggered by the T7 phage counterdefence "
                "protein Ocr"
            ),
            "notes": (
                "Deep et al. support defining the Ocr-triggered PARIS "
                "mechanism around the AriA antitoxin and AriB toxin."
            ),
        },
        {
            "reference": DEEP,
            "snippet": (
                "AriB is a toprim/OLD-family nuclease, the activation of "
                "which arrests cell growth and inhibits phage propagation "
                "by globally inhibiting protein translation through "
                "specific cleavage of a lysine tRNA"
            ),
            "notes": (
                "Deep et al. support the AriB nuclease, lysine-tRNA "
                "cleavage, translational-inhibition, growth-arrest, and "
                "phage-propagation outputs."
            ),
        },
        {
            "reference": BURMAN,
            "snippet": (
                "The phage antirestriction induced system (PARIS) is a "
                "defence system, often encoded in viral genomes, that is "
                "composed of a 55 kDa ABC ATPase (AriA) and a 35 kDa "
                "TOPRIM nuclease (AriB)"
            ),
            "notes": (
                "Burman et al. independently support the AriA ABC ATPase "
                "and AriB TOPRIM nuclease components."
            ),
        },
        {
            "reference": BURMAN,
            "snippet": (
                "ATP-dependent detection of foreign proteins triggers "
                "the release of AriB, which assembles into a homodimeric "
                "nuclease that blocks infection by cleaving host lysine "
                "transfer RNA"
            ),
            "notes": (
                "Burman et al. support an activation model in which "
                "foreign-protein detection releases AriB to cleave host "
                "lysine tRNA."
            ),
        },
        {
            "reference": BURMAN,
            "snippet": (
                "Phage T5 subverts PARIS immunity through expression of "
                "a lysine transfer RNA variant that is not cleaved by "
                "PARIS, thereby restoring viral infection"
            ),
            "notes": (
                "Burman et al. support recording T5 lysine tRNA "
                "anti-defense as a reviewed counter-defense gap before "
                "minting narrower PARIS subtype children."
            ),
        },
        {
            "reference": ROUSSET,
            "snippet": (
                "While the system from E. coli B185 provided robust "
                "defense when expressed from its natural promoter"
            ),
            "notes": (
                "Rousset et al. support E. coli as a canonical organism "
                "by cloning the E. coli B185 PARIS system with its "
                "native promoter and observing robust antiphage defense."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Rousset et al. cloned the native-promoter PARIS locus "
                "from E. coli B185 and showed that it provided robust "
                "defense."
            ),
            "reference": ROUSSET,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "paris_ariab_trna_cleavage_abortive_defense",
            "title": (
                "PARIS loci couple phage anti-restriction sensing to "
                "AriB tRNA cleavage"
            ),
            "description": (
                "Evidence-backed process sketch linking a complete PARIS "
                "locus to AriA/AriB immune-complex assembly, "
                "foreign-protein sensing, AriB activation, host lysine "
                "tRNA cleavage, translational inhibition, and inhibition "
                "of phage propagation."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph stays at the PARIS-family level and uses "
                "characterized E. coli B185 AriA/AriB examples without "
                "asserting one universal phage trigger, Ocr response, "
                "Ptr1/Ptr2 response, T5 lysine tRNA suppressor, exact "
                "AriA/AriB stoichiometry, or anti-anti-restriction "
                "context across all PARIS loci."
            ),
            "nodes": [
                {
                    "node_id": "paris_locus",
                    "label": "PARIS locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A complete phage anti-restriction-induced system "
                        "locus encoding the AriA ABC ATPase sensor and "
                        "AriB TOPRIM-family nuclease effector."
                    ),
                },
                {
                    "node_id": "aria_arib_complex_assembly",
                    "label": "AriA/AriB immune complex assembly",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Assembly of an AriA scaffold that sequesters "
                        "and inactivates AriB nuclease subunits before "
                        "PARIS activation."
                    ),
                },
                {
                    "node_id": "foreign_protein_sensing",
                    "label": "foreign protein sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "AriA-dependent detection of activating phage "
                        "proteins such as the T7 Ocr anti-restriction "
                        "protein."
                    ),
                },
                {
                    "node_id": "arib_nuclease_activation",
                    "label": "AriB nuclease activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Release and dimerization of the AriB "
                        "TOPRIM-family nuclease effector from the AriA "
                        "scaffold."
                    ),
                },
                {
                    "node_id": "lysine_trna_cleavage",
                    "label": "lysine tRNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "AriB-dependent cleavage of host lysine transfer "
                        "RNA after PARIS activation."
                    ),
                },
                {
                    "node_id": "translation_inhibition",
                    "label": "translation inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Global protein-translation inhibition and "
                        "growth arrest following host lysine tRNA "
                        "cleavage."
                    ),
                },
                {
                    "node_id": "phage_propagation",
                    "label": "phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Completion of bacteriophage replication and "
                        "spread in a susceptible bacterial population."
                    ),
                },
                {
                    "node_id": "paris_system_trait",
                    "label": "PARIS system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000237",
                    "description": (
                        "Possession of a genome-encoded PARIS "
                        "abortive-infection defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded "
                        "abortive-infection phage defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "paris_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "aria_arib_complex_assembly",
                    "description": (
                        "PARIS loci encode AriA and AriB components that "
                        "assemble into an immune complex."
                    ),
                    "evidence": [
                        {
                            "reference": BURMAN,
                            "snippet": (
                                "Here we show that AriA and AriB assemble "
                                "into a 425 kDa supramolecular immune "
                                "complex"
                            ),
                            "notes": (
                                "Burman et al. support AriA/AriB complex "
                                "assembly as a direct PARIS system "
                                "activity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "aria_arib_complex_assembly",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "foreign_protein_sensing",
                    "description": (
                        "The AriA/AriB immune complex detects foreign "
                        "proteins in an ATP-dependent way."
                    ),
                    "evidence": [
                        {
                            "reference": BURMAN,
                            "snippet": (
                                "ATP-dependent detection of foreign "
                                "proteins triggers the release of AriB"
                            ),
                            "notes": (
                                "Burman et al. support AriA-dependent "
                                "foreign protein detection as the "
                                "triggering event for PARIS activation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "foreign_protein_sensing",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "arib_nuclease_activation",
                    "description": (
                        "T7 Ocr or other foreign-protein detection "
                        "releases AriB from AriA and activates the "
                        "AriB nuclease."
                    ),
                    "evidence": [
                        {
                            "reference": DEEP,
                            "snippet": (
                                "After Ocr binding, the AriA hexamer "
                                "undergoes a structural rearrangement, "
                                "releasing AriB and allowing it to "
                                "dimerize and activate"
                            ),
                            "notes": (
                                "Deep et al. support Ocr-triggered AriB "
                                "release and dimerization in the E. coli "
                                "B185 PARIS system."
                            ),
                        }
                    ],
                },
                {
                    "subject": "arib_nuclease_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "lysine_trna_cleavage",
                    "description": (
                        "Activated AriB cleaves host lysine transfer RNA."
                    ),
                    "evidence": [
                        {
                            "reference": BURMAN,
                            "snippet": (
                                "AriB, which assembles into a homodimeric "
                                "nuclease that blocks infection by "
                                "cleaving host lysine transfer RNA"
                            ),
                            "notes": (
                                "Burman et al. support host lysine-tRNA "
                                "cleavage by activated AriB."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lysine_trna_cleavage",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "translation_inhibition",
                    "description": (
                        "AriB-mediated lysine tRNA cleavage inhibits "
                        "host-cell translation."
                    ),
                    "evidence": [
                        {
                            "reference": DEEP,
                            "snippet": (
                                "globally inhibiting protein translation "
                                "through specific cleavage of a lysine "
                                "tRNA"
                            ),
                            "notes": (
                                "Deep et al. connect AriB lysine-tRNA "
                                "cleavage to global inhibition of protein "
                                "translation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "translation_inhibition",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_propagation",
                    "description": (
                        "PARIS-associated translational arrest blocks "
                        "phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": DEEP,
                            "snippet": (
                                "arrests cell growth and inhibits phage "
                                "propagation by globally inhibiting "
                                "protein translation"
                            ),
                            "notes": (
                                "Deep et al. support the growth-arrest and "
                                "phage-inhibition output of AriB "
                                "activation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "translation_inhibition",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "paris_system_trait",
                    "description": (
                        "AriB-dependent translational inhibition realizes "
                        "the PARIS abortive-infection phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": ROUSSET,
                            "snippet": (
                                "Therefore, ariAB seem to halt growth in "
                                "infected cells, preventing the "
                                "completion of the phage cycle, a typical "
                                "feature of abortive infection systems"
                            ),
                            "notes": (
                                "Rousset et al. connect AriA/AriB to "
                                "growth arrest, phage-cycle inhibition, "
                                "and abortive infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "paris_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "PARIS system possession is an "
                        "abortive-infection system trait."
                    ),
                    "evidence": [
                        {
                            "reference": ROUSSET,
                            "snippet": (
                                "describe PARIS, an abortive infection "
                                "system triggered by a phage-encoded "
                                "anti-restriction protein"
                            ),
                            "notes": (
                                "Rousset et al. explicitly describe PARIS "
                                "as an abortive infection system."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "paris-trigger-and-counterdefense-gap",
            "prompt": (
                "Resolve PARIS trigger specificity, AriA/AriB "
                "stoichiometry, phage T5 lysine-tRNA suppression, "
                "and non-Ocr phage triggers before minting narrower "
                "PARIS subtype children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. discovered PARIS as an abortive "
                "infection system triggered by T7 Ocr; Deep et al. "
                "resolved Ocr-dependent AriA release of AriB for the "
                "E. coli B185 system; and Burman et al. showed that "
                "T5 Ptr1 and Ptr2 can activate PARIS while a phage T5 "
                "lysine tRNA variant can evade AriB cleavage. The first "
                "TraitRecord therefore stays at the broad PARIS-system "
                "level until separate subtype review resolves which "
                "foreign-protein triggers, AriB activities, and "
                "anti-defense suppressors apply across each PARIS "
                "family."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-18",
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
            "Minted PARIS system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v114."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADVERSARIAL_REVIEW_REPAIR",
        changes=(
            "Resolved PR #976 review issue #977 by scoping the PARIS "
            "canonical example note to the Rousset et al. E. coli B185 "
            "evidence cited by that example."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
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
