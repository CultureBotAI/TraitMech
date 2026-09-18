#!/usr/bin/env python3
"""Add the CapRel system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "caprel_system.yaml"

ZHANG_2022 = "DOI:10.1038/s41586-022-05444-z"
ZHANG_2024 = "DOI:10.1038/s41586-024-08039-y"

CURATOR = "codex"
TIMESTAMP = "2026-09-18T15:19:24Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000244",
    "label": "CapRel system",
    "definition": (
        "A phage defense system in which an organism possesses a fused "
        "CapRel toxin-antitoxin locus whose C-terminal antitoxin sensor can "
        "directly bind phage trigger proteins, relieve autoinhibition of the "
        "toxSAS toxin domain, promote tRNA pyrophosphorylation, and restrict "
        "phage propagation by blocking translation."
    ),
    "definition_source": ZHANG_2022,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "CapRel toxin-antitoxin system",
            "synonym_type": "EXACT_SYNONYM",
            "source": ZHANG_2022,
        },
        {
            "synonym_text": "fused CapRel system",
            "synonym_type": "EXACT_SYNONYM",
            "source": ZHANG_2022,
        },
    ],
    "evidence": [
        {
            "reference": ZHANG_2022,
            "snippet": (
                "protects Escherichia coli against diverse phages"
            ),
            "notes": (
                "Zhang et al. support CapRelSJ46 as a fused CapRel "
                "toxin-antitoxin antiphage system that protects E. coli "
                "against several phages."
            ),
        },
        {
            "reference": ZHANG_2022,
            "snippet": (
                "newly synthesized major capsid protein binds directly to "
                "the C-terminal domain"
            ),
            "notes": (
                "Zhang et al. support direct sensing of a phage major "
                "capsid protein by the CapRelSJ46 C-terminal antitoxin "
                "domain."
            ),
        },
        {
            "reference": ZHANG_2022,
            "snippet": (
                "enabling the toxin domain to pyrophosphorylate tRNAs, "
                "which blocks translation to restrict viral infection"
            ),
            "notes": (
                "Zhang et al. connect phage-triggered CapRel activation to "
                "tRNA pyrophosphorylation, translation blockade, and "
                "restriction of viral infection."
            ),
        },
        {
            "reference": ZHANG_2022,
            "snippet": (
                "fused CapRels can provide anti-phage defence, with "
                "variable phage specificity"
            ),
            "notes": (
                "Zhang et al. support treating fused CapRel loci as a "
                "family-level phage-defense system rather than only one "
                "CapRelSJ46 instance."
            ),
        },
        {
            "reference": ZHANG_2024,
            "snippet": (
                "can directly bind and sense two completely unrelated and "
                "structurally different proteins using the same sensory domain"
            ),
            "notes": (
                "Zhang et al. independently support CapRelSJ46 as a direct "
                "phage-trigger-sensing immune protein and show that a single "
                "sensory domain can recognize more than one phage trigger."
            ),
        },
        {
            "reference": ZHANG_2024,
            "snippet": (
                "can fully evade CapRelSJ46 defence only when both triggers "
                "are mutated"
            ),
            "notes": (
                "Zhang et al. connect multifactorial trigger sensing to "
                "CapRel-mediated defense during Bas11 phage infection."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "caprel_phage_triggered_translation_blockade",
            "title": (
                "CapRel sensors couple phage trigger binding to translation "
                "blockade"
            ),
            "description": (
                "Evidence-backed process sketch linking a fused CapRel "
                "toxin-antitoxin locus to direct phage-protein sensing, "
                "toxSAS activation, tRNA pyrophosphorylation, translation "
                "inhibition, and restricted phage propagation."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures CapRelSJ46 major-capsid-protein and "
                "Gp54 trigger evidence without claiming one universal "
                "CapRel phage trigger, allosteric route, escape route, or "
                "phage specificity across all fused CapRel homologs."
            ),
            "nodes": [
                {
                    "node_id": "caprel_locus",
                    "label": "CapRel locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A fused CapRel toxin-antitoxin locus encoding an "
                        "N-terminal toxSAS toxin domain and a C-terminal "
                        "antitoxin sensor domain."
                    ),
                },
                {
                    "node_id": "phage_trigger_binding",
                    "label": "phage trigger binding",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Direct binding of a phage-encoded trigger protein "
                        "to the CapRel antitoxin sensor domain."
                    ),
                },
                {
                    "node_id": "caprel_toxin_activation",
                    "label": "CapRel toxSAS activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Relief of autoinhibition that activates the "
                        "N-terminal CapRel toxSAS toxin domain."
                    ),
                },
                {
                    "node_id": "trna_pyrophosphorylation",
                    "label": "tRNA pyrophosphorylation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Pyrophosphorylation of transfer RNAs by activated "
                        "CapRel toxSAS toxin activity."
                    ),
                },
                {
                    "node_id": "translation_blockade",
                    "label": "translation blockade",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Inhibition of cellular translation downstream of "
                        "CapRel-mediated tRNA pyrophosphorylation."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage propagation in cells whose "
                        "CapRel system has blocked translation."
                    ),
                },
                {
                    "node_id": "caprel_system_trait",
                    "label": "CapRel system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000244",
                    "description": (
                        "Possession of a genome-encoded fused CapRel "
                        "toxin-antitoxin phage-defense system."
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
                    "subject": "caprel_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "caprel_toxin_activation",
                    "description": (
                        "Fused CapRel loci encode the N-terminal toxin "
                        "domain and C-terminal antitoxin sensor domain that "
                        "keep CapRel inhibited until phage trigger binding."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG_2022,
                            "snippet": (
                                "regulates the toxic N-terminal region, "
                                "serving as both antitoxin and phage "
                                "infection sensor"
                            ),
                            "notes": (
                                "Zhang et al. support the C-terminal CapRel "
                                "domain as both antitoxin and phage-infection "
                                "sensor."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_trigger_binding",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "caprel_toxin_activation",
                    "description": (
                        "Binding of phage-encoded triggers to the "
                        "C-terminal CapRel sensor relieves autoinhibition of "
                        "the toxSAS domain."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG_2022,
                            "snippet": (
                                "major capsid protein binds directly to the "
                                "C-terminal domain"
                            ),
                            "notes": (
                                "Zhang et al. identify phage major capsid "
                                "protein as a direct CapRelSJ46 trigger."
                            ),
                        },
                        {
                            "reference": ZHANG_2024,
                            "snippet": (
                                "directly binds and senses two completely "
                                "unrelated and structurally different phage "
                                "proteins using the same sensor domain"
                            ),
                            "notes": (
                                "Zhang et al. show that CapRelSJ46 can "
                                "directly sense an alternative Gp54 trigger."
                            ),
                        },
                    ],
                },
                {
                    "subject": "caprel_toxin_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "trna_pyrophosphorylation",
                    "description": (
                        "CapRel trigger binding activates the toxSAS domain "
                        "that pyrophosphorylates tRNAs."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG_2022,
                            "snippet": (
                                "enabling the toxin domain to "
                                "pyrophosphorylate tRNAs"
                            ),
                            "notes": (
                                "Zhang et al. connect relief of "
                                "autoinhibition to CapRel toxSAS-mediated "
                                "tRNA pyrophosphorylation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "trna_pyrophosphorylation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "translation_blockade",
                    "description": (
                        "tRNA pyrophosphorylation blocks cellular "
                        "translation during CapRel antiviral activation."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG_2022,
                            "snippet": (
                                "pyrophosphorylate tRNAs, which blocks "
                                "translation"
                            ),
                            "notes": (
                                "Zhang et al. identify translation blockade "
                                "as the immediate outcome of CapRel-mediated "
                                "tRNA pyrophosphorylation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "translation_blockade",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Translation blockade contributes to restriction of "
                        "the infecting phage."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG_2022,
                            "snippet": (
                                "blocks translation to restrict viral "
                                "infection"
                            ),
                            "notes": (
                                "Zhang et al. connect translation blockade "
                                "to restriction of viral infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "caprel_system_trait",
                    "description": (
                        "CapRel-dependent restriction of phage propagation "
                        "realizes the CapRel system trait."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG_2022,
                            "snippet": (
                                "fused CapRels can provide anti-phage defence"
                            ),
                            "notes": (
                                "Zhang et al. support fused CapRels as "
                                "anti-phage defense systems."
                            ),
                        }
                    ],
                },
                {
                    "subject": "caprel_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "CapRel system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG_2022,
                            "snippet": (
                                "a fused anti-phage toxin-antitoxin system"
                            ),
                            "notes": (
                                "Zhang et al. place CapRelSJ46 in the "
                                "anti-phage toxin-antitoxin-system family."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "caprel-trigger-and-family-breadth-gap",
            "prompt": (
                "Resolve CapRel trigger breadth, phage escape routes, and "
                "family-specific activation before minting narrower CapRel "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Zhang et al. support CapRelSJ46 sensing of a major capsid "
                "protein and an unrelated Gp54 trigger, but fused CapRel "
                "homologs need separate review before TraitMech asserts one "
                "universal phage trigger, CapRel escape route, tRNA target "
                "spectrum, or phage specificity across the family."
            ),
            "posed_by": "codex",
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

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted CapRel system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v121."
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
