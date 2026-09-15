#!/usr/bin/env python3
"""Add the phosphorothioate defense system genomics trait."""
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

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "phosphorothioate_defense_system.yaml"
)

XIONG = "DOI:10.1038/s41564-020-0700-6"
JIANG = "DOI:10.1128/mbio.00933-23"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T10:54:22Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000213",
    "label": "phosphorothioate defense system",
    "definition": (
        "A genomics trait describing possession of a DNA "
        "phosphorothioation-dependent antiphage restriction locus in which "
        "host DNA phosphorothioate modification is paired with Dnd- or "
        "Ssp-family restriction activity to nick unmodified invading DNA and "
        "inhibit bacteriophage replication."
    ),
    "definition_source": XIONG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PT-associated R-M system",
            "synonym_type": "EXACT_SYNONYM",
            "source": JIANG,
        },
        {
            "synonym_text": "PT-related R-M system",
            "synonym_type": "EXACT_SYNONYM",
            "source": JIANG,
        },
    ],
    "evidence": [
        {
            "reference": XIONG,
            "snippet": (
                "We previously identified the Dnd system, which uses "
                "DndABCDE to insert sulfur into the DNA backbone as a "
                "double-stranded phosphorothioate (PT) modification, and "
                "DndFGH, a restriction component"
            ),
            "notes": (
                "Xiong et al. summarize the Dnd modification and restriction "
                "modules as a DNA phosphorothioation defense system."
            ),
        },
        {
            "reference": XIONG,
            "snippet": "SspABCD coupled with SspE provides protection against phages",
            "notes": (
                "Xiong et al. support SspABCD-SspE as a bacterial "
                "phosphorothioation-sensing antiphage defense system."
            ),
        },
        {
            "reference": JIANG,
            "snippet": (
                "Usually, this modification gene cluster is paired with a "
                "restriction module consisting of DndF, DndG, and DndH"
            ),
            "notes": (
                "Jiang et al. support the paired modification-plus-restriction "
                "architecture of Dnd-related phosphorothioate R-M systems."
            ),
        },
        {
            "reference": JIANG,
            "snippet": (
                "the host could benefit from the protection provided by "
                "Dnd-related R-M systems against infection by various lytic "
                "phages as well as temperate phages"
            ),
            "notes": (
                "Jiang et al. experimentally demonstrated broad antiphage "
                "protection by Dnd-related phosphorothioate R-M systems."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:340184",
            "taxon_label": "Escherichia coli B7A",
            "note": (
                "Jiang et al. cloned the native E. coli B7A dndBCDE-FGH "
                "module into E. coli DH10B and measured strong DndB7A R-M "
                "protection against multiple lytic phages."
            ),
            "reference": JIANG,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "phosphorothioate_dna_nicking_antiphage_defense",
            "title": (
                "Phosphorothioate restriction modules nick invading phage DNA"
            ),
            "description": (
                "Evidence-backed process sketch linking host DNA "
                "phosphorothioate modification to PT-dependent restriction, "
                "foreign-DNA nicking, and impaired phage DNA replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures system-level logic shared by "
                "phosphorothioate-based Dnd and Ssp restriction-modification "
                "systems without claiming that the DndFGH and SspE "
                "restriction modules sense or cleave DNA by one exact protein "
                "mechanism."
            ),
            "nodes": [
                {
                    "node_id": "phosphorothioate_modification_module",
                    "label": "phosphorothioate modification module",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Dnd- or Ssp-family gene module that installs "
                        "sequence-specific phosphorothioate modifications on "
                        "host DNA."
                    ),
                },
                {
                    "node_id": "dna_phosphorothioation",
                    "label": "DNA phosphorothioation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replacement of a nonbridging oxygen in the DNA "
                        "phosphate backbone with sulfur."
                    ),
                },
                {
                    "node_id": "pt_dependent_foreign_dna_targeting",
                    "label": "PT-dependent foreign DNA targeting",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Phosphorothioate-dependent self/non-self "
                        "discrimination that targets invading DNA for "
                        "restriction."
                    ),
                },
                {
                    "node_id": "foreign_dna_nicking",
                    "label": "foreign DNA nicking",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Introduction of nicks into unmodified invading DNA "
                        "by a PT-associated restriction module."
                    ),
                },
                {
                    "node_id": "phage_dna_replication",
                    "label": "phage DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication of invading bacteriophage DNA after host "
                        "cell entry."
                    ),
                },
                {
                    "node_id": "phosphorothioate_defense_system_trait",
                    "label": "phosphorothioate defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000213",
                    "description": (
                        "Possession of a genome-encoded "
                        "phosphorothioate-based phage defense system."
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
                    "subject": "phosphorothioate_modification_module",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dna_phosphorothioation",
                    "description": (
                        "DndABCDE or SspABCD modification modules install "
                        "sequence-specific phosphorothioate marks on host DNA."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "uses DndABCDE to insert sulfur into the DNA "
                                "backbone as a double-stranded "
                                "phosphorothioate (PT) modification"
                            ),
                            "notes": (
                                "Xiong et al. support DndABCDE-dependent "
                                "host DNA phosphorothioation."
                            ),
                        },
                        {
                            "reference": XIONG,
                            "snippet": (
                                "SspABCD confers single-stranded and "
                                "high-frequency PTs with SspB acting as a "
                                "nickase"
                            ),
                            "notes": (
                                "Xiong et al. support SspABCD-dependent host "
                                "DNA phosphorothioation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dna_phosphorothioation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pt_dependent_foreign_dna_targeting",
                    "description": (
                        "Sequence-specific PT marks couple host DNA "
                        "modification to self/non-self restriction by Dnd- "
                        "and Ssp-family restriction modules."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "SspE senses sequence-specific PTs by virtue "
                                "of its PT-stimulated NTPase activity to exert "
                                "its anti-phage activity"
                            ),
                            "notes": (
                                "Xiong et al. support direct coupling between "
                                "sequence-specific PT marks and SspE "
                                "restriction activity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "pt_dependent_foreign_dna_targeting",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "foreign_dna_nicking",
                    "description": (
                        "DndFGH and SspE systems converge on nicking "
                        "unmodified invading DNA."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "SspE inhibits phage propagation by "
                                "introducing nicking damage to impair phage "
                                "DNA replication"
                            ),
                            "notes": (
                                "Xiong et al. support SspE-linked nicking "
                                "damage as a second PT-dependent route to "
                                "restricted phage replication."
                            ),
                        },
                        {
                            "reference": JIANG,
                            "snippet": (
                                "DndF, DndG, and DndH undergoes "
                                "conformational changes to perform DNA "
                                "binding, translocation, and DNA nicking "
                                "activities and scavenge the foreign DNA"
                            ),
                            "notes": (
                                "Jiang et al. summarize DndFGH-mediated DNA "
                                "binding, translocation, and nicking of "
                                "foreign DNA that lacks PT modification."
                            ),
                        }
                    ],
                },
                {
                    "subject": "foreign_dna_nicking",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_dna_replication",
                    "description": (
                        "PT-dependent nicking of invading DNA impairs "
                        "bacteriophage DNA replication."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "SspE inhibits phage propagation by "
                                "introducing nicking damage to impair phage "
                                "DNA replication"
                            ),
                            "notes": (
                                "Xiong et al. directly connect SspE DNA "
                                "nicking to impaired phage replication."
                            ),
                        }
                    ],
                },
                {
                    "subject": "foreign_dna_nicking",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "phosphorothioate_defense_system_trait",
                    "description": (
                        "Foreign-DNA nicking realizes phosphorothioate-based "
                        "restriction of infecting bacteriophages."
                    ),
                    "evidence": [
                        {
                            "reference": JIANG,
                            "snippet": (
                                "the host could benefit from Dnd-related R-M "
                                "systems for a broad range of antiphage "
                                "activities"
                            ),
                            "notes": (
                                "Jiang et al. support Dnd-mediated "
                                "phosphorothioate restriction as an "
                                "antiphage defense output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phosphorothioate_defense_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Phosphorothioate restriction-system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": "provides protection against phages",
                            "notes": (
                                "Xiong et al. place PT-dependent SspABCD-SspE "
                                "in the antiphage defense family."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "phosphorothioate-subfamily-split-gap",
            "prompt": (
                "Resolve Dnd, SspBCD-E, SspABCD-sspFGH, and archaeal "
                "phosphorothioate-based antiviral systems before minting "
                "narrower children under the phosphorothioate defense parent."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Xiong et al. and Jiang et al. support at least two bacterial "
                "PT-related R-M architectures with distinct restriction "
                "modules. The DndFGH macromolecular machine, SspE single "
                "restriction enzyme, SspFGH systems, and archaeal "
                "phosphorothioate-based antiviral systems need separate "
                "primary-source review before they can be split into narrower "
                "TraitRecords with exact component groundings."
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
            "Minted phosphorothioate defense system as a DOI-backed GENOMICS "
            "TraitRecord under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v90."
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
