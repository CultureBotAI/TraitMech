#!/usr/bin/env python3
"""Add the Gabija system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gabija_system.yaml"

OH = "DOI:10.1093/nar/gkad951"
CHENG = "DOI:10.1016/j.chom.2023.06.014"
ANTINE = "DOI:10.1038/s41586-023-06855-2"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T12:36:55Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000215",
    "label": "Gabija system",
    "definition": (
        "A genomics trait describing possession of a Gabija antiphage "
        "defense locus whose GajA and GajB proteins assemble into a complex "
        "that inhibits bacteriophage replication."
    ),
    "definition_source": OH,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Gabija anti-phage defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": OH,
        },
        {
            "synonym_text": "Gabija anti-phage defence system",
            "synonym_type": "EXACT_SYNONYM",
            "source": ANTINE,
        },
    ],
    "evidence": [
        {
            "reference": OH,
            "snippet": (
                "Gabija is one of the most abundant prokaryotic antiviral "
                "systems and consists of two proteins, GajA and GajB"
            ),
            "notes": (
                "Oh et al. support defining Gabija at the two-component "
                "antiviral-system level."
            ),
        },
        {
            "reference": OH,
            "snippet": (
                "The Gabija anti-phage defense system was first identified "
                "in Bacillus cereus and is present in >4000 prokaryotic "
                "genomes"
            ),
            "notes": (
                "Oh et al. support B. cereus as the source organism for the "
                "Gabija system and support broad prokaryotic distribution."
            ),
        },
        {
            "reference": CHENG,
            "snippet": (
                "synergy between GajA-mediated DNA cleavage and nucleotide "
                "hydrolysis by GajB initiates efficient abortive infection "
                "defense against virulent bacteriophages"
            ),
            "notes": (
                "Cheng et al. support the combined DNA-cleavage and "
                "nucleotide-depletion output of the Gabija complex."
            ),
        },
        {
            "reference": ANTINE,
            "snippet": (
                "Two sets of Gabija protein B (GajB) dimers dock at opposite "
                "sides of the complex and create a 4:4 GajA-GajB assembly "
                "(hereafter, GajAB) that is essential for phage resistance in "
                "vivo"
            ),
            "notes": (
                "Antine et al. support the GajAB complex as essential for "
                "Gabija-mediated phage resistance."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1396",
            "taxon_label": "Bacillus cereus",
            "note": (
                "Oh et al. report that the Gabija anti-phage defense system "
                "was first identified in Bacillus cereus and characterize "
                "GajB from the B. cereus VD045 Gabija system."
            ),
            "reference": OH,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "gabija_gajab_complex_antiphage_defense",
            "title": "Gabija GajAB complexes deplete nucleotides and cleave DNA",
            "description": (
                "Evidence-backed process sketch linking a Gabija gajA-gajB "
                "operon to GajAB complex assembly, nucleotide depletion, DNA "
                "cleavage, and inhibition of bacteriophage replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the characterized Gabija GajA/GajB "
                "outputs without asserting one universal phage sensor, DNA "
                "substrate, GajA:GajB stoichiometry, host death trigger, or "
                "anti-Gabija evasion mechanism across all Gabija loci."
            ),
            "nodes": [
                {
                    "node_id": "gabija_operon",
                    "label": "Gabija gajA-gajB operon",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Gabija defense locus encoding GajA and GajB "
                        "proteins."
                    ),
                },
                {
                    "node_id": "gajab_complex_assembly",
                    "label": "GajAB complex assembly",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Assembly of GajA and GajB proteins into the "
                        "antiphage Gabija complex."
                    ),
                },
                {
                    "node_id": "gabija_nucleotide_depletion",
                    "label": "Gabija nucleotide depletion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "GajB-dependent hydrolysis of host dATP, dGTP, ATP, "
                        "or GTP nucleotide pools."
                    ),
                },
                {
                    "node_id": "gabija_dna_cleavage",
                    "label": "Gabija DNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "GajA-dependent cleavage of DNA during Gabija "
                        "antiviral defense."
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
                    "node_id": "gabija_system_trait",
                    "label": "Gabija system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000215",
                    "description": (
                        "Possession of a genome-encoded Gabija antiphage "
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
                    "subject": "gabija_operon",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gajab_complex_assembly",
                    "description": (
                        "The gajA and gajB genes encode proteins that "
                        "assemble into the Gabija GajAB antiphage complex."
                    ),
                    "evidence": [
                        {
                            "reference": OH,
                            "snippet": (
                                "GajB interacts with GajA to form a "
                                "heterooctameric Gabija complex"
                            ),
                            "notes": (
                                "Oh et al. support assembly of B. cereus "
                                "VD045 GajA and GajB into a stable complex."
                            ),
                        },
                        {
                            "reference": ANTINE,
                            "snippet": (
                                "create a 4:4 GajA-GajB assembly (hereafter, "
                                "GajAB) that is essential for phage "
                                "resistance in vivo"
                            ),
                            "notes": (
                                "Antine et al. support the GajAB assembly as "
                                "required for phage resistance."
                            ),
                        },
                    ],
                },
                {
                    "subject": "gajab_complex_assembly",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gabija_nucleotide_depletion",
                    "description": (
                        "The Gabija complex enables GajB-mediated nucleotide "
                        "hydrolysis and nucleotide-pool depletion."
                    ),
                    "evidence": [
                        {
                            "reference": CHENG,
                            "snippet": (
                                "GajA requires GajB, which senses DNA termini "
                                "produced by GajA to hydrolyze (d)A/(d)GTP, "
                                "depleting essential nucleotides"
                            ),
                            "notes": (
                                "Cheng et al. connect the GajA/GajB complex "
                                "with depletion of adenine and guanine "
                                "nucleotide pools."
                            ),
                        }
                    ],
                },
                {
                    "subject": "gajab_complex_assembly",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gabija_dna_cleavage",
                    "description": (
                        "The Gabija GajAB complex catalyzes GajA-mediated DNA "
                        "cleavage during antiviral defense."
                    ),
                    "evidence": [
                        {
                            "reference": CHENG,
                            "snippet": (
                                "synergy between GajA-mediated DNA cleavage "
                                "and nucleotide hydrolysis by GajB initiates "
                                "efficient abortive infection defense"
                            ),
                            "notes": (
                                "Cheng et al. support DNA cleavage as a "
                                "GajA-dependent component of Gabija defense."
                            ),
                        }
                    ],
                },
                {
                    "subject": "gabija_nucleotide_depletion",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "Gabija nucleotide depletion helps inhibit "
                        "bacteriophage replication."
                    ),
                    "evidence": [
                        {
                            "reference": CHENG,
                            "snippet": (
                                "depleting essential nucleotides. This ATPase "
                                "activity of Gabija complex is only activated "
                                "upon DNA binding"
                            ),
                            "notes": (
                                "Cheng et al. connect GajB ATPase activity to "
                                "depletion of nucleotide pools required for "
                                "phage replication."
                            ),
                        }
                    ],
                },
                {
                    "subject": "gabija_dna_cleavage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "Gabija DNA cleavage helps inhibit bacteriophage "
                        "replication."
                    ),
                    "evidence": [
                        {
                            "reference": ANTINE,
                            "snippet": (
                                "Gabija proteins assemble into a "
                                "supramolecular complex of around 500 kDa "
                                "that degrades phage DNA"
                            ),
                            "notes": (
                                "Antine et al. support phage-DNA degradation "
                                "as an output of the GajAB complex."
                            ),
                        }
                    ],
                },
                {
                    "subject": "gabija_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "gabija_system_trait",
                    "description": (
                        "GajAB DNA cleavage is part of the antiviral output "
                        "that realizes the Gabija system defense phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": CHENG,
                            "snippet": (
                                "synergy between GajA-mediated DNA cleavage "
                                "and nucleotide hydrolysis by GajB initiates "
                                "efficient abortive infection defense"
                            ),
                            "notes": (
                                "Cheng et al. support GajA-mediated DNA "
                                "cleavage as part of the Gabija defense "
                                "phenotype."
                            ),
                        }
                    ],
                },
                {
                    "subject": "gabija_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Gabija system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": OH,
                            "snippet": (
                                "Gabija is one of the most abundant "
                                "prokaryotic antiviral systems"
                            ),
                            "notes": (
                                "Oh et al. place Gabija among prokaryotic "
                                "antiviral systems."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "gabija-activation-and-antidefense-gap",
            "prompt": (
                "Resolve Gabija activation, stoichiometry, cell-outcome, and "
                "phage anti-defense breadth before minting narrower Gabija "
                "mechanistic children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Cheng et al. support nucleotide depletion and DNA cleavage "
                "as Gabija outputs, and Antine et al. support GajAB complex "
                "assembly plus Gad1-mediated inhibition, but Gabija family "
                "members need separate review before TraitMech asserts one "
                "universal trigger, exact GajA:GajB stoichiometry, host death "
                "program, DNA substrate, or anti-Gabija phage inhibitor."
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
            "Minted Gabija system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v92."
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
