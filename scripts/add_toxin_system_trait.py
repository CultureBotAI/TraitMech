#!/usr/bin/env python3
"""Add the ToxIN system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "toxin_system.yaml"
ABORTIVE = (
    REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"
)

FINERAN = "DOI:10.1073/pnas.0808832106"
BLOWER = "DOI:10.1128/JB.00720-09"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T19:25:00Z"
PARENT_TIMESTAMP = "2026-09-15T19:25:01Z"

OLD_PARENT_SCOPE_NOTES = (
    "The graph captures the shared Abi strategy without claiming that ToxIN, "
    "AbiE, and other abortive-infection families use one exact sensor, "
    "effector, toxin-antitoxin architecture, or cell-death mechanism."
)
NEW_PARENT_SCOPE_NOTES = (
    "The graph captures the shared Abi strategy without claiming that AbiE "
    "and other abortive-infection families use one exact sensor, effector, "
    "toxin-antitoxin architecture, or cell-death mechanism."
)

OLD_DISCUSSION_PROMPT = (
    "Resolve ToxIN, AbiE, and other abortive-infection families before "
    "minting narrower children under the broad abortive infection system parent."
)
NEW_DISCUSSION_PROMPT = (
    "Resolve AbiE and other abortive-infection families before minting "
    "narrower children under the broad abortive infection system parent."
)
OLD_DISCUSSION_RATIONALE = (
    "AbiQ is split out as traitmech:000225. Lopatina et al., Fineran et al., "
    "and Dy et al. still support Abi as a genomically encoded phage defense "
    "strategy that spans mechanistically diverse ToxIN, AbiE, and other "
    "toxin-antitoxin branches. Additional narrower TraitRecords need separate "
    "review to ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
NEW_DISCUSSION_RATIONALE = (
    "ToxIN and AbiQ are split out as traitmech:000226 and traitmech:000225, "
    "respectively. Lopatina et al., Fineran et al., and Dy et al. still "
    "support Abi as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse AbiE and other toxin-antitoxin branches. "
    "Additional narrower TraitRecords need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
PARENT_CHANGES = (
    "Removed ToxIN from the open abortive-infection subfamily split-gap "
    "discussion after minting traitmech:000226 for the ToxIN system; AbiE "
    "and other abortive-infection families remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000226",
    "label": "ToxIN system",
    "definition": (
        "An abortive infection system in which an organism possesses a toxIN "
        "type III protein-RNA toxin-antitoxin locus whose ToxN toxin and "
        "tandem ToxI RNA antitoxins constitute a two-component Abi module "
        "that inhibits bacterial growth and restricts phage propagation."
    ),
    "definition_source": FINERAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        {
            "reference": FINERAN,
            "snippet": (
                "A highly effective 2-gene Abi system from the phytopathogen "
                "Erwinia carotovora subspecies atroseptica, designated "
                "ToxIN, is described"
            ),
            "notes": (
                "Fineran et al. define ToxIN as a two-gene abortive "
                "infection system from the native pECA1039 plasmid."
            ),
        },
        {
            "reference": FINERAN,
            "snippet": (
                "ToxN inhibiting bacterial growth and the tandemly repeated "
                "ToxI RNA antitoxin counteracting the toxicity"
            ),
            "notes": (
                "Fineran et al. connect the ToxN protein toxin and tandem "
                "ToxI RNA repeats to the toxin-antitoxin behavior of ToxIN."
            ),
        },
        {
            "reference": FINERAN,
            "snippet": (
                "ToxIN defines an entirely new TA class that functions via a "
                "novel protein-RNA mechanism"
            ),
            "notes": (
                "Fineran et al. support ToxIN as the defining member of the "
                "type III protein-RNA toxin-antitoxin class."
            ),
        },
        {
            "reference": FINERAN,
            "snippet": (
                "All of our data are consistent with ToxIN functioning as a "
                "phage Abi system"
            ),
            "notes": (
                "Fineran et al. ruled out adsorption blockade and a "
                "restriction-modification explanation before classifying "
                "ToxIN as abortive infection."
            ),
        },
        {
            "reference": FINERAN,
            "snippet": (
                "ToxN functions through a reversible growth-inhibiting "
                "(bacteriostatic) mechanism"
            ),
            "notes": (
                "Fineran et al. support host growth inhibition as the ToxN "
                "toxin output."
            ),
        },
        {
            "reference": BLOWER,
            "snippet": (
                "Designated ToxIN, this two-component abortive infection "
                "system acts as a toxin-antitoxin module"
            ),
            "notes": (
                "Blower et al. place the two-component ToxIN module in the "
                "abortive infection class."
            ),
        },
        {
            "reference": BLOWER,
            "snippet": (
                "We determined the minimal ToxI RNA sequence in the native "
                "operon that is both necessary and sufficient for abortive "
                "infection and to counteract the toxicity of ToxN"
            ),
            "notes": (
                "Blower et al. connect ToxI RNA repeat dosage to both ToxN "
                "neutralization and the native abortive-infection phenotype."
            ),
        },
        {
            "reference": BLOWER,
            "snippet": (
                "this two-component Abi system operates as a novel "
                "protein-RNA toxin-antitoxin (TA) system to abort phage "
                "infection in multiple gram-negative bacteria"
            ),
            "notes": (
                "Blower et al. support the ToxIN system as an Abi trait "
                "that can operate beyond the source Erwinia strain."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:29471",
            "taxon_label": "Pectobacterium atrosepticum",
            "note": (
                "Fineran et al. isolated pECA1039 from Erwinia carotovora "
                "subsp. atroseptica 1039, designated its two-gene Abi "
                "system ToxIN, and showed that the native toxIN locus "
                "conferred phage resistance in strain SCRI 1043."
            ),
            "reference": FINERAN,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "toxin_type_iii_ta_antiphage_activity",
            "title": "ToxIN type III toxin-antitoxin activity restricts phage propagation",
            "description": (
                "Evidence-backed process sketch linking a toxIN locus to "
                "type III toxin-antitoxin activity, ToxN-dependent growth "
                "inhibition, restricted phage propagation, and "
                "abortive-infection system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures ToxIN at the system level without "
                "asserting a universal phage activator, an exact molecular "
                "target for ToxN, or the stoichiometry of ToxI "
                "neutralization."
            ),
            "nodes": [
                {
                    "node_id": "toxin_locus",
                    "label": "toxIN locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A type III protein-RNA toxin-antitoxin "
                        "abortive-infection locus encoding the ToxN toxin "
                        "and tandem ToxI RNA antitoxins."
                    ),
                },
                {
                    "node_id": "toxin_type_iii_toxin_antitoxin_activity",
                    "label": "ToxIN type III toxin-antitoxin activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protein-RNA toxin-antitoxin activity of ToxIN, in "
                        "which tandem ToxI RNA repeats counteract ToxN "
                        "toxicity."
                    ),
                },
                {
                    "node_id": "toxn_growth_inhibition",
                    "label": "ToxN-dependent growth inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reversible bacterial growth inhibition caused by "
                        "ToxN toxin activity."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of phage propagation in a "
                        "ToxIN-containing infected host cell."
                    ),
                },
                {
                    "node_id": "toxin_system_trait",
                    "label": "ToxIN system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000226",
                    "description": (
                        "Possession of a genome-encoded toxIN type III "
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
                    "subject": "toxin_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "toxin_type_iii_toxin_antitoxin_activity",
                    "description": (
                        "The toxIN locus encodes the defining type III "
                        "protein-RNA toxin-antitoxin module."
                    ),
                    "evidence": [
                        {
                            "reference": FINERAN,
                            "snippet": (
                                "ToxIN defines an entirely new TA class that "
                                "functions via a novel protein-RNA mechanism"
                            ),
                            "notes": (
                                "Fineran et al. show that ToxIN constitutes "
                                "a protein-RNA toxin-antitoxin system."
                            ),
                        }
                    ],
                },
                {
                    "subject": "toxin_type_iii_toxin_antitoxin_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "toxn_growth_inhibition",
                    "description": (
                        "The ToxIN toxin-antitoxin module couples ToxN "
                        "growth inhibition to ToxI RNA antitoxin "
                        "counteraction."
                    ),
                    "evidence": [
                        {
                            "reference": FINERAN,
                            "snippet": (
                                "ToxN inhibiting bacterial growth and the "
                                "tandemly repeated ToxI RNA antitoxin "
                                "counteracting the toxicity"
                            ),
                            "notes": (
                                "Fineran et al. identify ToxN as the toxic "
                                "component and ToxI repeats as RNA "
                                "antitoxins."
                            ),
                        }
                    ],
                },
                {
                    "subject": "toxin_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The native toxIN locus contributes to abortive "
                        "restriction of phage propagation."
                    ),
                    "evidence": [
                        {
                            "reference": FINERAN,
                            "snippet": (
                                "All of our data are consistent with ToxIN "
                                "functioning as a phage Abi system"
                            ),
                            "notes": (
                                "Fineran et al. connect the toxIN locus to "
                                "the abortive-infection phage resistance "
                                "output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "toxin_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the "
                        "ToxIN abortive-infection defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": BLOWER,
                            "snippet": (
                                "this two-component Abi system operates as a "
                                "novel protein-RNA toxin-antitoxin (TA) "
                                "system to abort phage infection in multiple "
                                "gram-negative bacteria"
                            ),
                            "notes": (
                                "Blower et al. describe ToxIN as a "
                                "two-component Abi system that aborts phage "
                                "infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "toxin_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "ToxIN system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BLOWER,
                            "snippet": (
                                "Designated ToxIN, this two-component "
                                "abortive infection system acts as a "
                                "toxin-antitoxin module"
                            ),
                            "notes": (
                                "Blower et al. place ToxIN in the abortive "
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
            "Minted ToxIN system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v103."
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
            "ToxIN system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
