#!/usr/bin/env python3
"""Add the AbiQ system genomics trait."""
from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abiq_system.yaml"
ABORTIVE = (
    REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"
)

EMOND = "DOI:10.1128/AEM.64.12.4748-4756.1998"
SAMSON = "DOI:10.1128/JB.00296-13"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T18:45:00Z"
PARENT_TIMESTAMP = "2026-09-15T18:45:01Z"

OLD_PARENT_SCOPE_NOTES = (
    "The graph captures the shared Abi strategy without claiming that ToxIN, "
    "AbiQ, AbiE, and other abortive-infection families use one exact sensor, "
    "effector, toxin-antitoxin architecture, or cell-death mechanism."
)
NEW_PARENT_SCOPE_NOTES = (
    "The graph captures the shared Abi strategy without claiming that ToxIN, "
    "AbiE, and other abortive-infection families use one exact sensor, "
    "effector, toxin-antitoxin architecture, or cell-death mechanism."
)

OLD_DISCUSSION_PROMPT = (
    "Resolve ToxIN/AbiQ, AbiE, and other abortive-infection families before "
    "minting narrower children under the broad abortive infection system parent."
)
NEW_DISCUSSION_PROMPT = (
    "Resolve ToxIN, AbiE, and other abortive-infection families before "
    "minting narrower children under the broad abortive infection system parent."
)
OLD_DISCUSSION_RATIONALE = (
    "Lopatina et al., Fineran et al., and Dy et al. support Abi as a "
    "genomically encoded phage defense strategy that spans mechanistically "
    "diverse families, including the ToxIN/AbiQ and AbiE toxin-antitoxin "
    "branches. Narrower TraitRecords will need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
NEW_DISCUSSION_RATIONALE = (
    "AbiQ is split out as traitmech:000225. Lopatina et al., Fineran et al., "
    "and Dy et al. still support Abi as a genomically encoded phage defense "
    "strategy that spans mechanistically diverse ToxIN, AbiE, and other "
    "toxin-antitoxin branches. Additional narrower TraitRecords need separate "
    "review to ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Removed AbiQ from the open abortive-infection subfamily split-gap "
    "discussion after minting traitmech:000225 for the AbiQ system; ToxIN, "
    "AbiE, and other abortive-infection families remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000225",
    "label": "AbiQ system",
    "definition": (
        "An abortive infection system in which an organism possesses an AbiQ "
        "type III toxin-antitoxin locus whose protein endoribonuclease and "
        "cognate RNA antitoxin module alter early phage mRNA profiles and "
        "restrict phage propagation after adsorption."
    ),
    "definition_source": SAMSON,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        {
            "reference": EMOND,
            "snippet": (
                "the system encoded by pSRQ900 was classified as an "
                "abortive infection mechanism and was named AbiQ"
            ),
            "notes": (
                "Emond et al. named AbiQ as a Lactococcus plasmid-encoded "
                "abortive infection system rather than an adsorption-blocking "
                "or restriction-modification defense."
            ),
        },
        {
            "reference": EMOND,
            "snippet": (
                "The frameshift mutation completely abolished host "
                "resistance to phages p2 and c21"
            ),
            "notes": (
                "Emond et al. localized the phage-resistance phenotype to "
                "the abiQ open reading frame on the pSRQ900 fragment."
            ),
        },
        {
            "reference": SAMSON,
            "snippet": (
                "Lactococcus lactis AbiQ system, a type III "
                "toxin-antitoxin with antiviral activities"
            ),
            "notes": (
                "Samson et al. support the type III protein-RNA "
                "toxin-antitoxin architecture of AbiQ."
            ),
        },
        {
            "reference": SAMSON,
            "snippet": "AbiQ modified the early-expressed phage mRNA profiles",
            "notes": (
                "Samson et al. connect AbiQ to altered early phage mRNA "
                "profiles during infection."
            ),
        },
        {
            "reference": SAMSON,
            "snippet": (
                "active against various phage families infecting "
                "Gram-positive and Gram-negative bacteria"
            ),
            "notes": (
                "Samson et al. support AbiQ as an antiphage system whose "
                "activity is not restricted to its native lactococcal host."
            ),
        },
        {
            "reference": SAMSON,
            "snippet": "In the presence of AbiQ, additional small transcripts were observed",
            "notes": (
                "Samson et al. observed altered P008 transcript profiles in "
                "phage-infected AbiQ-containing cells."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Emond et al. isolated the pSRQ900 plasmid from Lactococcus "
                "lactis W-37, named its encoded abortive-infection mechanism "
                "AbiQ, and showed AbiQ-dependent resistance to c2- and "
                "936-like lactococcal phages."
            ),
            "reference": EMOND,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abiq_type_iii_ta_antiphage_activity",
            "title": "AbiQ type III toxin-antitoxin activity disrupts phage mRNA profiles",
            "description": (
                "Evidence-backed process sketch linking an AbiQ locus to "
                "type III toxin-antitoxin activity, altered early phage "
                "mRNA profiles, restricted phage propagation, and "
                "abortive-infection system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiQ at the system level without "
                "asserting a universal phage activator, exact AbiQ RNA "
                "target, or phage-escape path; Samson et al. show that "
                "multiple unrelated phage genes can be involved in the "
                "AbiQ phenotype."
            ),
            "nodes": [
                {
                    "node_id": "abiq_locus",
                    "label": "AbiQ locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A type III toxin-antitoxin abortive-infection "
                        "locus encoding the AbiQ toxin with its cognate "
                        "RNA antitoxin."
                    ),
                },
                {
                    "node_id": "abiq_type_iii_toxin_antitoxin_activity",
                    "label": "AbiQ type III toxin-antitoxin activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protein-RNA toxin-antitoxin activity of AbiQ, in "
                        "which the AbiQ protein acts as an endoribonuclease "
                        "neutralized by a cognate RNA antitoxin."
                    ),
                },
                {
                    "node_id": "early_phage_mrna_profile_modification",
                    "label": "early phage mRNA profile modification",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "AbiQ-associated alteration of early phage mRNA "
                        "profiles in infected host cells."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced production of infectious phage from an "
                        "AbiQ-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abiq_system_trait",
                    "label": "AbiQ system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000225",
                    "description": (
                        "Possession of a genome-encoded AbiQ type III "
                        "toxin-antitoxin abortive-infection system."
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
                    "subject": "abiq_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abiq_type_iii_toxin_antitoxin_activity",
                    "description": (
                        "The AbiQ locus encodes a type III protein-RNA "
                        "toxin-antitoxin antiphage system."
                    ),
                    "evidence": [
                        {
                            "reference": SAMSON,
                            "snippet": (
                                "Lactococcus lactis AbiQ system, a type III "
                                "toxin-antitoxin with antiviral activities"
                            ),
                            "notes": (
                                "Samson et al. define AbiQ as a type III "
                                "toxin-antitoxin system with antiviral "
                                "activity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abiq_type_iii_toxin_antitoxin_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "early_phage_mrna_profile_modification",
                    "description": (
                        "AbiQ activity alters the abundance pattern of "
                        "early-expressed phage transcripts during infection."
                    ),
                    "evidence": [
                        {
                            "reference": SAMSON,
                            "snippet": (
                                "AbiQ modified the early-expressed phage "
                                "mRNA profiles"
                            ),
                            "notes": (
                                "Samson et al. directly assayed phage "
                                "transcription in AbiQ-containing "
                                "Lactococcus cells."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abiq_type_iii_toxin_antitoxin_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "AbiQ type III toxin-antitoxin activity contributes "
                        "to restricted phage propagation in infected host "
                        "cells."
                    ),
                    "evidence": [
                        {
                            "reference": SAMSON,
                            "snippet": (
                                "active against various phage families "
                                "infecting Gram-positive and Gram-negative "
                                "bacteria"
                            ),
                            "notes": (
                                "Samson et al. support AbiQ as an antiphage "
                                "type III toxin-antitoxin system."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abiq_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the "
                        "AbiQ antiphage defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": EMOND,
                            "snippet": (
                                "The frameshift mutation completely "
                                "abolished host resistance to phages p2 "
                                "and c21"
                            ),
                            "notes": (
                                "Emond et al. measured reduced phage "
                                "plaquing on cells carrying the native "
                                "AbiQ plasmid."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abiq_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiQ system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": EMOND,
                            "snippet": (
                                "the system encoded by pSRQ900 was "
                                "classified as an abortive infection "
                                "mechanism and was named AbiQ"
                            ),
                            "notes": (
                                "Emond et al. place AbiQ in the abortive "
                                "infection class of phage defense."
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


def update_abortive_parent(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == "traitmech:000214"
    assert record["label"] == "abortive infection system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    graph = record["causal_graphs"][0]
    assert graph["graph_id"] == "abortive_infection_population_level_defense"
    assert graph["scope_notes"] == OLD_PARENT_SCOPE_NOTES
    graph["scope_notes"] = NEW_PARENT_SCOPE_NOTES

    discussions = record.get("discussions") or []
    discussion = next(
        item
        for item in discussions
        if item.get("discussion_id") == "abortive-infection-subfamily-split-gap"
    )
    assert discussion["prompt"] == OLD_DISCUSSION_PROMPT
    assert discussion["status"] == "OPEN"
    assert discussion["rationale"] == OLD_DISCUSSION_RATIONALE
    discussion["prompt"] = NEW_DISCUSSION_PROMPT
    discussion["rationale"] = NEW_DISCUSSION_RATIONALE

    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=PARENT_CHANGES,
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted AbiQ system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v102."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / ABORTIVE.name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_abortive_parent(load_trait(ABORTIVE))
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "AbiQ system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
