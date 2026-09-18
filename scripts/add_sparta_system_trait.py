#!/usr/bin/env python3
"""Add the SPARTA system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sparta_system.yaml"

KOOPAL = "DOI:10.1016/j.cell.2022.03.012"
KOTTUR = "DOI:10.1038/s41467-024-49271-4"

CURATOR = "codex"
TIMESTAMP = "2026-09-18T11:59:02Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000240",
    "label": "SPARTA system",
    "definition": (
        "A genomics trait describing possession of a short prokaryotic "
        "Argonaute TIR-APAZ (SPARTA) locus whose short pAgo and TIR-APAZ "
        "proteins form heterodimeric complexes that oligomerize after "
        "guide RNA-mediated target DNA binding and unleash TIR "
        "domain-mediated NAD(P)ase activity that depletes NAD(P)+ to "
        "remove plasmid-invaded cells."
    ),
    "definition_source": KOOPAL,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000188"],
    "synonyms": [
        {
            "synonym_text": "short prokaryotic Argonaute TIR-APAZ system",
            "synonym_type": "EXACT_SYNONYM",
            "source": KOOPAL,
        }
    ],
    "evidence": [
        {
            "reference": KOOPAL,
            "snippet": (
                "short prokaryotic Argonaute and the associated "
                "TIR-APAZ (SPARTA) proteins form heterodimeric "
                "complexes"
            ),
            "notes": (
                "Koopal et al. define SPARTA as a short pAgo plus "
                "TIR-APAZ system rather than an individual gene or "
                "single protein."
            ),
        },
        {
            "reference": KOOPAL,
            "snippet": (
                "Upon guide RNA-mediated target DNA binding, four SPARTA "
                "heterodimers form oligomers in which TIR "
                "domain-mediated NAD(P)ase activity is unleashed"
            ),
            "notes": (
                "Koopal et al. support the guide RNA and target "
                "DNA-triggered oligomerization mechanism that activates "
                "SPARTA NAD(P)ase activity."
            ),
        },
        {
            "reference": KOOPAL,
            "snippet": (
                "SPARTA is activated in the presence of highly transcribed "
                "multicopy plasmid DNA, which causes cell death through "
                "NAD(P)+ depletion"
            ),
            "notes": (
                "Koopal et al. support plasmid-challenge activation and "
                "NAD(P)+ depletion as experimentally demonstrated SPARTA "
                "outcomes."
            ),
        },
        {
            "reference": KOTTUR,
            "snippet": (
                "cryo-EM structure of the SPARTA oligomer (tetramer of "
                "heterodimers) bound to guide-RNA/target-ssDNA"
            ),
            "notes": (
                "Kottur et al. independently support the RNA/target-DNA "
                "activated oligomeric state of a SPARTA complex."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "sparta_pago_tir_apaz_nadase_cell_death",
            "title": (
                "SPARTA complexes couple guide RNA target binding to "
                "NAD(P)ase-triggered cell death"
            ),
            "description": (
                "Evidence-backed process sketch linking a SPARTA locus to "
                "short-pAgo/TIR-APAZ heterodimer assembly, guide "
                "RNA-target DNA activation, oligomerization, TIR-domain "
                "NAD(P)ase activity, NAD(P)+ depletion, and removal of "
                "plasmid-invaded cells."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph stays at the SPARTA-family level and models the "
                "high-copy plasmid activation route from Koopal et al. "
                "without asserting that phage defense, SIR2-APAZ systems, "
                "nuclease-APAZ systems, or every other short-pAgo family "
                "uses the same enzymatic output."
            ),
            "nodes": [
                {
                    "node_id": "sparta_locus",
                    "label": "SPARTA locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A short prokaryotic Argonaute TIR-APAZ locus "
                        "encoding short pAgo and TIR-APAZ proteins."
                    ),
                },
                {
                    "node_id": "sparta_heterodimer_assembly",
                    "label": "SPARTA heterodimer assembly",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Assembly of short pAgo and TIR-APAZ proteins into "
                        "SPARTA heterodimeric complexes."
                    ),
                },
                {
                    "node_id": "guide_target_binding",
                    "label": "guide RNA-mediated target DNA binding",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Recognition of target DNA by a SPARTA complex "
                        "through a bound guide RNA."
                    ),
                },
                {
                    "node_id": "sparta_oligomerization",
                    "label": "SPARTA oligomerization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Formation of a target-DNA-bound SPARTA oligomer "
                        "from four guide-loaded heterodimers."
                    ),
                },
                {
                    "node_id": "tir_nadpase_activity",
                    "label": "SPARTA TIR-domain NAD(P)ase activity",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "NAD(P)+ hydrolysis by TIR domains assembled in an "
                        "active SPARTA oligomer."
                    ),
                },
                {
                    "node_id": "nadp_depletion",
                    "label": "NAD(P)+ depletion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Loss of cellular NAD(P)+ downstream of activated "
                        "SPARTA TIR-domain NAD(P)ase activity."
                    ),
                },
                {
                    "node_id": "invaded_cell_death",
                    "label": "plasmid-invaded cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cell death triggered in host cells carrying "
                        "highly transcribed multicopy plasmid DNA detected "
                        "by SPARTA."
                    ),
                },
                {
                    "node_id": "sparta_system_trait",
                    "label": "SPARTA system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000240",
                    "description": (
                        "Possession of a genome-encoded short "
                        "prokaryotic Argonaute TIR-APAZ defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "sparta_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "sparta_heterodimer_assembly",
                    "description": (
                        "SPARTA loci encode short pAgo and TIR-APAZ "
                        "proteins that assemble into heterodimeric "
                        "complexes."
                    ),
                    "evidence": [
                        {
                            "reference": KOOPAL,
                            "snippet": (
                                "SPARTA proteins form heterodimeric "
                                "complexes"
                            ),
                            "notes": (
                                "Koopal et al. support the paired-protein "
                                "complex architecture of SPARTA."
                            ),
                        }
                    ],
                },
                {
                    "subject": "guide_target_binding",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "sparta_oligomerization",
                    "description": (
                        "Guide RNA-mediated target DNA binding triggers "
                        "SPARTA tetramer-of-heterodimers oligomerization."
                    ),
                    "evidence": [
                        {
                            "reference": KOOPAL,
                            "snippet": (
                                "Upon guide RNA-mediated target DNA binding, "
                                "four SPARTA heterodimers form oligomers"
                            ),
                            "notes": (
                                "Koopal et al. connect target recognition "
                                "to SPARTA oligomer formation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sparta_oligomerization",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "tir_nadpase_activity",
                    "description": (
                        "SPARTA oligomerization aligns TIR domains and "
                        "activates NAD(P)+ hydrolysis."
                    ),
                    "evidence": [
                        {
                            "reference": KOOPAL,
                            "snippet": (
                                "oligomers in which TIR domain-mediated "
                                "NAD(P)ase activity is unleashed"
                            ),
                            "notes": (
                                "Koopal et al. link oligomer formation to "
                                "activation of TIR-domain NAD(P)ase "
                                "activity."
                            ),
                        },
                        {
                            "reference": KOTTUR,
                            "snippet": (
                                "The TIR domains amass in a "
                                "parallel-strands arrangement for catalysis"
                            ),
                            "notes": (
                                "Kottur et al. structurally support "
                                "TIR-domain arrangement in the active "
                                "SPARTA assembly."
                            ),
                        },
                    ],
                },
                {
                    "subject": "tir_nadpase_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "nadp_depletion",
                    "description": (
                        "Activated SPARTA TIR domains hydrolyze NAD(P)+, "
                        "depleting the cellular NAD(P)+ pool."
                    ),
                    "evidence": [
                        {
                            "reference": KOTTUR,
                            "snippet": (
                                "activated by invading DNA to unleash its "
                                "TIR domain for NAD(P)+ hydrolysis"
                            ),
                            "notes": (
                                "Kottur et al. describe DNA-triggered "
                                "release of SPARTA TIR-domain NAD(P)+ "
                                "hydrolysis."
                            ),
                        }
                    ],
                },
                {
                    "subject": "nadp_depletion",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "invaded_cell_death",
                    "description": (
                        "SPARTA-associated NAD(P)+ depletion contributes "
                        "to death of plasmid-invaded host cells."
                    ),
                    "evidence": [
                        {
                            "reference": KOOPAL,
                            "snippet": (
                                "causes cell death through NAD(P)+ "
                                "depletion"
                            ),
                            "notes": (
                                "Koopal et al. connect SPARTA-driven "
                                "NAD(P)+ depletion to cell death."
                            ),
                        }
                    ],
                },
                {
                    "subject": "invaded_cell_death",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sparta_system_trait",
                    "description": (
                        "Removal of plasmid-invaded cells is the cellular "
                        "outcome of the SPARTA possession trait."
                    ),
                    "evidence": [
                        {
                            "reference": KOOPAL,
                            "snippet": (
                                "This results in the removal of "
                                "plasmid-invaded cells from bacterial "
                                "cultures"
                            ),
                            "notes": (
                                "Koopal et al. support SPARTA-mediated "
                                "removal of plasmid-invaded cells."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "sparta-native-host-and-substrate-gap",
            "prompt": (
                "Resolve SPARTA natural-host substrates before adding "
                "canonical examples or narrower short-pAgo defense "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Koopal et al. support strong high-copy plasmid activation "
                "and only limited, NADase-independent phage effects; Kottur "
                "et al. support C. thermophila SPARTA structural activation. "
                "This first record therefore stays broad until natural-host "
                "activity, phage scope, and whether SIR2-APAZ or "
                "nuclease-APAZ relatives should be separate children are "
                "resolved."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-18",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the new TraitRecord YAML",
    )
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted SPARTA system as a DOI-backed GENOMICS TraitRecord "
            "under the quality root after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior "
            "proposal record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v117."
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
