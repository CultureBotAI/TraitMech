#!/usr/bin/env python3
"""Add the RADAR system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "radar_system.yaml"

DUNCAN_LOWEY = "DOI:10.1016/j.cell.2023.01.012"
GAO = "DOI:10.1016/j.cell.2023.01.026"
CURATOR = "codex"
TIMESTAMP = "2026-09-18T09:55:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000238",
    "label": "RADAR system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "restriction by an adenosine deaminase acting on RNA locus "
        "encoding an RdrA AAA+ ATPase and an RdrB adenosine deaminase "
        "that assemble into a supramolecular defense complex to modify "
        "adenosine-containing substrates and inhibit bacteriophage "
        "replication."
    ),
    "definition_source": DUNCAN_LOWEY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "restriction by an adenosine deaminase acting on RNA",
            "synonym_type": "EXACT_SYNONYM",
            "source": DUNCAN_LOWEY,
        }
    ],
    "evidence": [
        {
            "reference": DUNCAN_LOWEY,
            "snippet": (
                "RADAR is a two-protein bacterial defense system that "
                "was reported to defend against phage"
            ),
            "notes": (
                "Duncan-Lowey et al. support RADAR as a named bacterial "
                "phage-defense system."
            ),
        },
        {
            "reference": DUNCAN_LOWEY,
            "snippet": (
                "revealing RdrA as a heptameric, two-layered AAA+ "
                "ATPase and RdrB as a dodecameric, hollow complex with "
                "twelve surface-exposed deaminase active sites"
            ),
            "notes": (
                "Duncan-Lowey et al. support the RdrA AAA+ ATPase and "
                "RdrB adenosine-deaminase complex components."
            ),
        },
        {
            "reference": DUNCAN_LOWEY,
            "snippet": (
                "RdrB catalyzes ATP-to-ITP conversion in vitro and "
                "induces the massive accumulation of inosine "
                "mononucleotides during phage infection in vivo, "
                "limiting phage replication"
            ),
            "notes": (
                "Duncan-Lowey et al. support ATP-to-ITP deamination "
                "and inosine-mononucleotide accumulation as RADAR "
                "antiphage outputs."
            ),
        },
        {
            "reference": DUNCAN_LOWEY,
            "snippet": (
                "When heterologously expressed in E. coli MG1655, all "
                "RADAR systems conferred defense against the closely "
                "related T-even phages T2, T4, and T6"
            ),
            "notes": (
                "Duncan-Lowey et al. support the E. coli P0304799.3 "
                "RADAR locus as experimentally investigated and "
                "antiphage-active when cloned into E. coli MG1655."
            ),
        },
        {
            "reference": GAO,
            "snippet": (
                "RADAR contains an adenosine triphosphatase (RdrA) and "
                "an adenosine deaminase (RdrB)"
            ),
            "notes": (
                "Gao et al. independently support defining RADAR "
                "around the RdrA ATPase and RdrB deaminase components."
            ),
        },
        {
            "reference": GAO,
            "snippet": (
                "up to twelve RdrA rings can dock one RdrB cage with "
                "precise alignments between deaminase catalytic pockets "
                "and RNA-translocation channels"
            ),
            "notes": (
                "Gao et al. independently resolve RADAR RdrA/RdrB "
                "supramolecular assemblies while supporting an "
                "RNA-translocation interpretation of the deaminase "
                "substrate."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Duncan-Lowey et al. selected the RADAR system from "
                "E. coli P0304799.3 for experimental investigation and "
                "reported that it conferred defense against T-even "
                "phages when heterologously expressed in E. coli "
                "MG1655."
            ),
            "reference": DUNCAN_LOWEY,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "radar_rdrab_deamination_antiphage_defense",
            "title": (
                "RADAR RdrA/RdrB complexes couple deamination to phage "
                "defense"
            ),
            "description": (
                "Evidence-backed process sketch linking a complete "
                "RADAR locus to RdrA/RdrB supramolecular complex "
                "assembly, infection-associated adenosine-substrate "
                "deamination, inosine nucleotide accumulation, and "
                "inhibition of phage replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph stays at the RADAR-family level and uses the "
                "mononucleotide-deamination mechanism from "
                "Duncan-Lowey et al. without asserting that the exact "
                "RdrA activation trigger, ATP-versus-RNA substrate, "
                "inosine toxicity route, or abortive-infection output is "
                "resolved across all RADAR loci."
            ),
            "nodes": [
                {
                    "node_id": "radar_locus",
                    "label": "RADAR locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A complete restriction by an adenosine "
                        "deaminase acting on RNA locus encoding RdrA and "
                        "RdrB components."
                    ),
                },
                {
                    "node_id": "rdra_rdrb_complex_assembly",
                    "label": "RdrA/RdrB supramolecular complex assembly",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Assembly of the RdrA AAA+ ATPase and RdrB "
                        "adenosine deaminase into a supramolecular RADAR "
                        "defense complex."
                    ),
                },
                {
                    "node_id": "adenosine_substrate_deamination",
                    "label": "RADAR adenosine-substrate deamination",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "RdrB-associated deamination of "
                        "adenosine-containing substrates during RADAR "
                        "activation."
                    ),
                },
                {
                    "node_id": "inosine_nucleotide_accumulation",
                    "label": "inosine nucleotide accumulation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Accumulation of inosine nucleotides such as ITP "
                        "and dITP in infected cells."
                    ),
                },
                {
                    "node_id": "phage_replication",
                    "label": "phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Bacteriophage genome replication and production "
                        "inside an infected bacterial host."
                    ),
                },
                {
                    "node_id": "radar_system_trait",
                    "label": "RADAR system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000238",
                    "description": (
                        "Possession of a genome-encoded RADAR "
                        "phage-defense system."
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
                    "subject": "radar_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "rdra_rdrb_complex_assembly",
                    "description": (
                        "RADAR loci encode RdrA and RdrB proteins that "
                        "assemble into a supramolecular defense complex."
                    ),
                    "evidence": [
                        {
                            "reference": DUNCAN_LOWEY,
                            "snippet": (
                                "RdrA and RdrB join to form a giant "
                                "assembly up to 10 MDa"
                            ),
                            "notes": (
                                "Duncan-Lowey et al. support RdrA/RdrB "
                                "RADAR complex assembly."
                            ),
                        }
                    ],
                },
                {
                    "subject": "radar_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "adenosine_substrate_deamination",
                    "description": (
                        "RADAR loci encode RdrB, which catalyzes "
                        "ATP-to-ITP deamination."
                    ),
                    "evidence": [
                        {
                            "reference": DUNCAN_LOWEY,
                            "snippet": (
                                "RdrB catalyzes ATP-to-ITP conversion in "
                                "vitro"
                            ),
                            "notes": (
                                "Duncan-Lowey et al. support RdrB as the "
                                "ATP-to-ITP deaminase encoded by RADAR "
                                "loci."
                            ),
                        }
                    ],
                },
                {
                    "subject": "adenosine_substrate_deamination",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "inosine_nucleotide_accumulation",
                    "description": (
                        "RADAR-associated ATP-to-ITP deamination "
                        "drives inosine-mononucleotide accumulation "
                        "during phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": DUNCAN_LOWEY,
                            "snippet": (
                                "RdrB catalyzes ATP-to-ITP conversion in "
                                "vitro and induces the massive "
                                "accumulation of inosine mononucleotides "
                                "during phage infection in vivo"
                            ),
                            "notes": (
                                "Duncan-Lowey et al. connect RdrB "
                                "ATP-to-ITP catalysis to "
                                "phage-infection-associated inosine "
                                "mononucleotide accumulation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "inosine_nucleotide_accumulation",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "RADAR-induced inosine nucleotide accumulation "
                        "limits phage replication."
                    ),
                    "evidence": [
                        {
                            "reference": DUNCAN_LOWEY,
                            "snippet": (
                                "RdrB catalyzes ATP-to-ITP conversion in "
                                "vitro and induces the massive "
                                "accumulation of inosine mononucleotides "
                                "during phage infection in vivo, "
                                "limiting phage replication"
                            ),
                            "notes": (
                                "Duncan-Lowey et al. support inosine "
                                "mononucleotide accumulation as a "
                                "phage-limiting RADAR output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "adenosine_substrate_deamination",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "radar_system_trait",
                    "description": (
                        "RADAR-mediated adenosine-nucleotide "
                        "deamination realizes the RADAR antiphage "
                        "phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": DUNCAN_LOWEY,
                            "snippet": (
                                "rapid deamination of adenosine "
                                "nucleotides is a key mediator of RADAR "
                                "anti-phage defense"
                            ),
                            "notes": (
                                "Duncan-Lowey et al. connect rapid "
                                "adenosine-nucleotide deamination, "
                                "rather than downstream inosine "
                                "accumulation alone, to RADAR antiphage "
                                "defense."
                            ),
                        }
                    ],
                },
                {
                    "subject": "radar_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "RADAR system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DUNCAN_LOWEY,
                            "snippet": (
                                "RADAR is a two-protein bacterial defense "
                                "system that was reported to defend "
                                "against phage"
                            ),
                            "notes": (
                                "Duncan-Lowey et al. support RADAR as a "
                                "bacterial phage-defense system."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "radar-trigger-and-substrate-gap",
            "prompt": (
                "Resolve RADAR phage triggers, RdrA activation, "
                "ATP-versus-RNA deamination, and inosine nucleotide "
                "toxicity before minting narrower RADAR mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support an RNA translocation and "
                "deamination model for RdrA/RdrB RADAR assemblies, "
                "whereas Duncan-Lowey et al. found that ATP and dATP "
                "mononucleotide deamination rather than robust RNA "
                "editing mediates RADAR immunity. The first TraitRecord "
                "therefore stays at the RADAR-system level until "
                "separate review resolves which activating phage cues, "
                "RdrA sensor states, deaminase substrates, and inosine "
                "toxicity routes generalize across RADAR loci."
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
            "Minted RADAR system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v115."
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
