#!/usr/bin/env python3
"""Add the AbiE system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abie_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DY = "DOI:10.1093/nar/gkt1419"
GARVEY = "DOI:10.1128/AEM.61.12.4321-4328.1995"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T19:46:30Z"
PARENT_TIMESTAMP = "2026-09-15T19:46:31Z"

OLD_PARENT_SCOPE_NOTES = (
    "The graph captures the shared Abi strategy without claiming that AbiE "
    "and other abortive-infection families use one exact sensor, effector, "
    "toxin-antitoxin architecture, or cell-death mechanism."
)
NEW_PARENT_SCOPE_NOTES = (
    "The graph captures the shared Abi strategy without claiming that other "
    "abortive-infection families use one exact sensor, effector, "
    "toxin-antitoxin architecture, or cell-death mechanism."
)

OLD_DISCUSSION_PROMPT = (
    "Resolve AbiE and other abortive-infection families before minting "
    "narrower children under the broad abortive infection system parent."
)
NEW_DISCUSSION_PROMPT = (
    "Resolve other abortive-infection families before minting narrower "
    "children under the broad abortive infection system parent."
)
OLD_DISCUSSION_RATIONALE = (
    "ToxIN and AbiQ are split out as traitmech:000226 and traitmech:000225, "
    "respectively. Lopatina et al., Fineran et al., and Dy et al. still "
    "support Abi as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse AbiE and other toxin-antitoxin branches. "
    "Additional narrower TraitRecords need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
NEW_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, and AbiE are split out as traitmech:000226, "
    "traitmech:000225, and traitmech:000227, respectively. Lopatina et al., "
    "Fineran et al., and Dy et al. still support Abi as a genomically "
    "encoded phage defense strategy that spans mechanistically diverse "
    "toxin-antitoxin branches and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape "
    "routes."
)
PARENT_CHANGES = (
    "Removed AbiE from the open abortive-infection subfamily split-gap "
    "discussion after minting traitmech:000227 for the AbiE system; other "
    "abortive-infection families remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000227",
    "label": "AbiE system",
    "definition": (
        "An abortive infection system in which an organism possesses an abiE "
        "bicistronic locus whose AbiEii DUF1814-family bacteriostatic toxin "
        "and AbiEi COG5340-family antitoxin constitute a non-interacting "
        "type IV toxin-antitoxin module that supports phage resistance."
    ),
    "definition_source": DY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        {
            "reference": GARVEY,
            "snippet": (
                "Subcloning and deletion analysis of the recombinant plasmid "
                "pPG01 defined a 2.5-kb ScaIHpaI fragment as conferring "
                "phage insensitivity"
            ),
            "notes": ("Garvey et al. localized the pNP40 AbiE determinant to the pPG01 subclone."),
        },
        {
            "reference": GARVEY,
            "snippet": (
                "The mechanisms encoded by pPG01 and pCG1 in L. lactis "
                "subsp. lactis MG1614 conformed to the criteria defining "
                "abortive infection and were designated AbiE and AbiF, "
                "respectively"
            ),
            "notes": (
                "Garvey et al. designated the pPG01-encoded pNP40 "
                "phage-insensitivity determinant as AbiE."
            ),
        },
        {
            "reference": DY,
            "snippet": (
                "AbiE systems are encoded by bicistronic operons and "
                "function via a non-interacting (Type IV) bacteriostatic TA "
                "mechanism"
            ),
            "notes": ("Dy et al. support defining AbiE as a type IV toxin-antitoxin Abi family."),
        },
        {
            "reference": DY,
            "snippet": (
                "We demonstrate that the AbiE phage resistance systems "
                "function as novel Type IV TAs and are widespread in "
                "bacteria and archaea"
            ),
            "notes": (
                "Dy et al. support a reusable AbiE-system trait beyond the "
                "original Lactococcus pNP40 determinant."
            ),
        },
        {
            "reference": DY,
            "snippet": (
                "AbiEii was toxic by acting as a GTP-binding NTase and was "
                "neutralized by expression of AbiEi"
            ),
            "notes": (
                "Dy et al. connect the AbiEii nucleotidyltransferase toxin "
                "and AbiEi antitoxin to the AbiE type IV toxin-antitoxin "
                "module."
            ),
        },
        {
            "reference": DY,
            "snippet": (
                "AbiEii was shown to specifically bind GTP, the first step in a NTase activity"
            ),
            "notes": (
                "Dy et al. support the GTP-binding nucleotidyltransferase "
                "activity of AbiEii while leaving the exact toxic target "
                "unresolved."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Garvey et al. cloned the pNP40 AbiE determinant and showed "
                "that the pPG01-encoded region conferred abortive-infection "
                "phage insensitivity in Lactococcus lactis subsp. lactis "
                "MG1614."
            ),
            "reference": GARVEY,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abie_type_iv_ta_antiphage_activity",
            "title": "AbiE type IV toxin-antitoxin activity supports phage resistance",
            "description": (
                "Evidence-backed process sketch linking an abiE locus to "
                "type IV toxin-antitoxin activity, AbiEii GTP-dependent "
                "toxicity, restricted phage propagation, and "
                "abortive-infection system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiE at the system level without "
                "asserting a universal phage activator, the exact cellular "
                "target of AbiEii, or that every COG5340-DUF1814 pair "
                "functions in abortive infection."
            ),
            "nodes": [
                {
                    "node_id": "abie_locus",
                    "label": "abiE locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A bicistronic type IV toxin-antitoxin "
                        "abortive-infection locus encoding AbiEi and AbiEii."
                    ),
                },
                {
                    "node_id": "abie_type_iv_toxin_antitoxin_activity",
                    "label": "AbiE type IV toxin-antitoxin activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Non-interacting type IV toxin-antitoxin activity "
                        "mediated by the AbiEi antitoxin and AbiEii toxin."
                    ),
                },
                {
                    "node_id": "abieii_ntase_toxicity",
                    "label": "AbiEii GTP-binding nucleotidyltransferase toxicity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Growth-inhibitory toxicity that depends on "
                        "conserved AbiEii nucleotidyltransferase motifs and "
                        "GTP binding."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of phage propagation in an "
                        "AbiE-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abie_system_trait",
                    "label": "AbiE system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000227",
                    "description": (
                        "Possession of a genome-encoded abiE type IV "
                        "toxin-antitoxin abortive-infection system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection phage defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abie_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abie_type_iv_toxin_antitoxin_activity",
                    "description": (
                        "The abiE locus encodes the defining type IV toxin-antitoxin module."
                    ),
                    "evidence": [
                        {
                            "reference": DY,
                            "snippet": (
                                "AbiE systems are encoded by bicistronic "
                                "operons and function via a "
                                "non-interacting (Type IV) bacteriostatic TA "
                                "mechanism"
                            ),
                            "notes": (
                                "Dy et al. show that AbiE is a bicistronic "
                                "type IV toxin-antitoxin system."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abie_type_iv_toxin_antitoxin_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abieii_ntase_toxicity",
                    "description": (
                        "The AbiE type IV module couples AbiEii "
                        "GTP-dependent nucleotidyltransferase toxicity to "
                        "AbiEi antitoxicity."
                    ),
                    "evidence": [
                        {
                            "reference": DY,
                            "snippet": (
                                "AbiEii was toxic by acting as a GTP-binding "
                                "NTase and was neutralized by expression of "
                                "AbiEi"
                            ),
                            "notes": (
                                "Dy et al. identify AbiEii as the toxin and "
                                "AbiEi as its cognate antitoxin."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abie_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The AbiE determinant contributes to abortive phage-resistance phenotypes."
                    ),
                    "evidence": [
                        {
                            "reference": GARVEY,
                            "snippet": (
                                "The mechanisms encoded by pPG01 and pCG1 in "
                                "L. lactis subsp. lactis MG1614 conformed to "
                                "the criteria defining abortive infection and "
                                "were designated AbiE and AbiF, respectively"
                            ),
                            "notes": (
                                "Garvey et al. show that the pPG01 AbiE "
                                "determinant produces an "
                                "abortive-infection phage-insensitivity "
                                "mechanism."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abie_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the AbiE "
                        "abortive-infection defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": DY,
                            "snippet": (
                                "We demonstrate that the AbiE phage "
                                "resistance systems function as novel Type "
                                "IV TAs and are widespread in bacteria and "
                                "archaea"
                            ),
                            "notes": (
                                "Dy et al. describe AbiE systems as type IV "
                                "toxin-antitoxin phage-resistance systems."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abie_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiE system possession is an abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": GARVEY,
                            "snippet": (
                                "The mechanisms encoded by pPG01 and pCG1 in "
                                "L. lactis subsp. lactis MG1614 conformed to "
                                "the criteria defining abortive infection and "
                                "were designated AbiE and AbiF, respectively"
                            ),
                            "notes": (
                                "Garvey et al. place AbiE in the abortive "
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
    discussions = record.get("discussions") or []
    discussion = next(
        item
        for item in discussions
        if item.get("discussion_id") == "abortive-infection-subfamily-split-gap"
    )
    if graph["scope_notes"] == NEW_PARENT_SCOPE_NOTES:
        assert discussion["prompt"] == NEW_DISCUSSION_PROMPT
        assert discussion["status"] == "OPEN"
        assert discussion["rationale"] == NEW_DISCUSSION_RATIONALE
        return record

    assert graph["scope_notes"] == OLD_PARENT_SCOPE_NOTES
    graph["scope_notes"] = NEW_PARENT_SCOPE_NOTES

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
            "Minted AbiE system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v104."
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
            "AbiE system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
