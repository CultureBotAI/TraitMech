#!/usr/bin/env python3
"""Add the Dnd system genomics trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dnd_system.yaml"
PHOSPHOROTHIOATE = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "phosphorothioate_defense_system.yaml"
)

XIONG = "DOI:10.1038/s41564-020-0700-6"
JIANG = "DOI:10.1128/mbio.00933-23"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T16:03:58Z"
PARENT_TIMESTAMP = "2026-09-15T16:03:59Z"

OLD_PARENT_PROMPT = (
    "Resolve Dnd, SspBCD-E, SspABCD-sspFGH, and archaeal "
    "phosphorothioate-based antiviral systems before minting narrower "
    "children under the phosphorothioate defense parent."
)
OLD_PARENT_RATIONALE = (
    "Xiong et al. and Jiang et al. support at least two bacterial PT-related "
    "R-M architectures with distinct restriction modules. The DndFGH "
    "macromolecular machine, SspE single restriction enzyme, SspFGH systems, "
    "and archaeal phosphorothioate-based antiviral systems need separate "
    "primary-source review before they can be split into narrower TraitRecords "
    "with exact component groundings."
)
NEW_PARENT_PROMPT = (
    "Resolve SspBCD-E, SspABCD-sspFGH, and archaeal "
    "phosphorothioate-based antiviral systems before minting additional "
    "narrower children under the phosphorothioate defense parent."
)
NEW_PARENT_RATIONALE = (
    "The Dnd system is now split out as traitmech:000221. Xiong et al. "
    "and Jiang et al. still support additional bacterial PT-related "
    "R-M architectures with distinct restriction modules, and the SspE "
    "single restriction enzyme, SspFGH systems, and archaeal "
    "phosphorothioate-based antiviral systems need separate "
    "primary-source review before they can be split into narrower "
    "TraitRecords with exact component groundings."
)
PARENT_CHANGES = (
    "Removed Dnd from the open phosphorothioate subfamily "
    "split-gap discussion after minting traitmech:000221 for the "
    "Dnd system; SspE, SspFGH, and archaeal "
    "phosphorothioate-based antiviral systems remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000221",
    "label": "Dnd system",
    "definition": (
        "A phosphorothioate defense system in which an organism possesses "
        "a Dnd restriction-modification locus that pairs a Dnd-family DNA "
        "phosphorothioation module with a DndFGH restriction module to nick "
        "invading DNA that lacks phosphorothioate modification."
    ),
    "definition_source": XIONG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000213"],
    "synonyms": [
        {
            "synonym_text": "Dnd R-M system",
            "synonym_type": "EXACT_SYNONYM",
            "source": JIANG,
        },
        {
            "synonym_text": "Dnd-related R-M system",
            "synonym_type": "EXACT_SYNONYM",
            "source": JIANG,
        },
        {
            "synonym_text": "Dnd-related restriction and modification system",
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
                "Xiong et al. summarize Dnd as a named PT-dependent "
                "restriction system with DNA-modification and restriction "
                "modules."
            ),
        },
        {
            "reference": JIANG,
            "snippet": (
                "Usually, this modification gene cluster is paired with a "
                "restriction module consisting of DndF, DndG, and DndH"
            ),
            "notes": (
                "Jiang et al. support DndFGH as the restriction module "
                "paired with Dnd DNA phosphorothioation."
            ),
        },
        {
            "reference": JIANG,
            "snippet": (
                "In general, some dnd or ssp clusters lack dndA or sspA; "
                "DndA or SspA is instead functionally replaced by other "
                "cysteine desulfurases, such as IscS, in bacteria"
            ),
            "notes": (
                "Jiang et al. support defining the Dnd system by a "
                "Dnd-family modification module without requiring a "
                "contiguous dndA gene in every locus."
            ),
        },
        {
            "reference": JIANG,
            "snippet": (
                "In the presence of exogenous DNA that lacks PT, the "
                "macromolecular machine consisting of DndF, DndG, and "
                "DndH undergoes conformational changes to perform DNA "
                "binding, translocation, and DNA nicking activities and "
                "scavenge the foreign DNA"
            ),
            "notes": (
                "Jiang et al. connect DndFGH to detection and nicking of "
                "foreign DNA lacking PT modification."
            ),
        },
        {
            "reference": JIANG,
            "snippet": (
                "we discussed the action of Dnd-related R-M systems "
                "against phages and demonstrated that the host could "
                "benefit from the protection provided by Dnd-related R-M "
                "systems against infection by various lytic phages as well "
                "as temperate phages"
            ),
            "notes": (
                "Jiang et al. support the phage-resistance output of Dnd "
                "restriction-modification systems."
            ),
        },
        {
            "reference": JIANG,
            "snippet": (
                "the 8,286-bp and 8,321-bp fragments containing the whole "
                "dndBCDEFGH gene cluster were amplified from the genomic "
                "DNA of E. coli B7A"
            ),
            "notes": (
                "Jiang et al. support Escherichia coli B7A as a direct "
                "source of the cloned dndBCDEFGH Dnd system."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:340184",
            "taxon_label": "Escherichia coli B7A",
            "note": (
                "Jiang et al. amplified the whole dndBCDEFGH gene cluster "
                "from E. coli B7A and assayed the cloned DndB7A R-M system "
                "for resistance against lytic and temperate phages."
            ),
            "reference": JIANG,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "dnd_dna_phosphorothioation_foreign_dna_nicking",
            "title": "Dnd systems use DNA phosphorothioation to restrict foreign DNA",
            "description": (
                "Evidence-backed process sketch linking a Dnd "
                "restriction-modification locus to host DNA "
                "phosphorothioation, PT-guided DndFGH foreign-DNA "
                "nicking, and Dnd-mediated phage defense."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Dnd-family modification and DndFGH "
                "restriction outputs without asserting one universal DndA "
                "cysteine-desulfurase source, PT motif, DndFGH "
                "conformational pathway, exogenous substrate class, phage "
                "spectrum, methylation interaction, or relationship to Ssp "
                "systems across all Dnd loci."
            ),
            "nodes": [
                {
                    "node_id": "dnd_restriction_modification_locus",
                    "label": "Dnd restriction-modification locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Dnd phosphorothioation-dependent restriction "
                        "locus pairing a Dnd-family DNA modification "
                        "module with a DndFGH restriction module."
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
                    "node_id": "dndfgh_foreign_dna_targeting",
                    "label": "DndFGH foreign DNA targeting",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DndFGH-mediated binding and translocation on "
                        "unmodified exogenous DNA before restriction."
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
                    "node_id": "phage_infection",
                    "label": "phage infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Entry and intracellular replication attempt by a "
                        "bacteriophage infecting a host bacterium."
                    ),
                },
                {
                    "node_id": "dnd_system_trait",
                    "label": "Dnd system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000221",
                    "description": (
                        "Possession of a genome-encoded Dnd "
                        "restriction-modification defense system."
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
            ],
            "edges": [
                {
                    "subject": "dnd_restriction_modification_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dna_phosphorothioation",
                    "description": (
                        "Dnd-family modification modules install "
                        "sequence-specific phosphorothioate marks on host "
                        "DNA."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "uses DndABCDE to insert sulfur into the "
                                "DNA backbone as a double-stranded "
                                "phosphorothioate (PT) modification"
                            ),
                            "notes": (
                                "Xiong et al. support Dnd-mediated host DNA "
                                "phosphorothioation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dnd_restriction_modification_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dndfgh_foreign_dna_targeting",
                    "description": (
                        "Dnd restriction-modification loci pair host DNA "
                        "phosphorothioation genes with the DndFGH "
                        "restriction module."
                    ),
                    "evidence": [
                        {
                            "reference": JIANG,
                            "snippet": (
                                "To build up a line of defense, the "
                                "dndABCDE gene cluster is usually paired "
                                "with dndFGH, which acts as a restriction "
                                "module"
                            ),
                            "notes": (
                                "Jiang et al. support the paired "
                                "modification-plus-restriction architecture "
                                "of Dnd systems."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dna_phosphorothioation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dndfgh_foreign_dna_targeting",
                    "description": (
                        "DNA phosphorothioation marks host DNA as self and "
                        "leaves unmodified exogenous DNA susceptible to "
                        "DndFGH targeting."
                    ),
                    "evidence": [
                        {
                            "reference": JIANG,
                            "snippet": (
                                "In the presence of exogenous DNA that lacks "
                                "PT, the macromolecular machine consisting "
                                "of DndF, DndG, and DndH undergoes "
                                "conformational changes"
                            ),
                            "notes": (
                                "Jiang et al. connect absence of PT on "
                                "exogenous DNA to DndFGH restriction-complex "
                                "activation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dndfgh_foreign_dna_targeting",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "foreign_dna_nicking",
                    "description": (
                        "DndFGH targeting leads to DNA binding, "
                        "translocation, and nicking of invading DNA."
                    ),
                    "evidence": [
                        {
                            "reference": JIANG,
                            "snippet": (
                                "DndFGH exerts DNA binding, translocation, "
                                "and nicking activities to initiate the "
                                "destructive DNA-shredding program to "
                                "eliminate genetic parasites"
                            ),
                            "notes": (
                                "Jiang et al. summarize the nicking output "
                                "of DndFGH foreign-DNA targeting."
                            ),
                        }
                    ],
                },
                {
                    "subject": "foreign_dna_nicking",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_infection",
                    "description": (
                        "DndFGH-mediated nicking restricts lytic phages and "
                        "blocks lysogenization by temperate phages."
                    ),
                    "evidence": [
                        {
                            "reference": JIANG,
                            "snippet": (
                                "Dnd R-M systems protect the host from "
                                "various lytic phages as well as the "
                                "lysogenization of temperate phages"
                            ),
                            "notes": (
                                "Jiang et al. summarize Dnd-mediated "
                                "protection against lytic phages and "
                                "temperate phage lysogenization."
                            ),
                        }
                    ],
                },
                {
                    "subject": "foreign_dna_nicking",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "dnd_system_trait",
                    "description": (
                        "PT-guided foreign-DNA nicking realizes the Dnd "
                        "restriction-modification system trait."
                    ),
                    "evidence": [
                        {
                            "reference": JIANG,
                            "snippet": (
                                "the host could benefit from Dnd-related "
                                "R-M systems for a broad range of "
                                "antiphage activities"
                            ),
                            "notes": (
                                "Jiang et al. support DndFGH restriction as "
                                "the Dnd antiphage defense output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dnd_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phosphorothioate_defense_system_trait",
                    "description": (
                        "Dnd system possession is a "
                        "phosphorothioate-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "We previously identified the Dnd system, "
                                "which uses DndABCDE to insert sulfur into "
                                "the DNA backbone as a double-stranded "
                                "phosphorothioate (PT) modification, and "
                                "DndFGH, a restriction component"
                            ),
                            "notes": (
                                "Xiong et al. place Dnd within "
                                "phosphorothioation-dependent restriction "
                                "systems."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def update_phosphorothioate_parent(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == "traitmech:000213"
    assert record["label"] == "phosphorothioate defense system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    discussions = {
        item["discussion_id"]: item for item in record.get("discussions") or []
    }
    discussion = discussions["phosphorothioate-subfamily-split-gap"]
    assert discussion["kind"] == "KNOWLEDGE_GAP"
    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] in {OLD_PARENT_PROMPT, NEW_PARENT_PROMPT}
    assert discussion["rationale"] in {OLD_PARENT_RATIONALE, NEW_PARENT_RATIONALE}

    discussion["prompt"] = NEW_PARENT_PROMPT
    discussion["rationale"] = NEW_PARENT_RATIONALE
    record["curation_history"] = [
        event
        for event in record.get("curation_history") or []
        if not (
            event.get("curator") == CURATOR
            and event.get("action") == "RESOLVE_DISCUSSION_SCOPE"
            and event.get("changes") == PARENT_CHANGES
        )
    ]
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=PARENT_CHANGES,
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the new TraitRecord YAML and update the parent gap",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Dnd system as a DOI-backed GENOMICS TraitRecord under "
            "the phosphorothioate defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v98."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    parent = update_phosphorothioate_parent(load_trait(PHOSPHOROTHIOATE))

    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, PHOSPHOROTHIOATE)
        print(f"wrote {TARGET.relative_to(REPO_ROOT)}")
        print(f"wrote {PHOSPHOROTHIOATE.relative_to(REPO_ROOT)}")
    else:
        print(f"would write {TARGET.relative_to(REPO_ROOT)}")
        print(f"would write {PHOSPHOROTHIOATE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
