#!/usr/bin/env python3
"""Add the AbiZ system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abiz_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DURMAZ = "DOI:10.1128/JB.00904-06"
PHILIPPE = "DOI:10.1371/journal.pone.0298680"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T20:35:00Z"
PARENT_TIMESTAMP = "2026-09-15T20:35:01Z"

OLD_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, and AbiE are split out as traitmech:000226, "
    "traitmech:000225, and traitmech:000227, respectively. Lopatina et al., "
    "Fineran et al., and Dy et al. still support Abi as a genomically "
    "encoded phage defense strategy that spans mechanistically diverse "
    "toxin-antitoxin branches and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape "
    "routes."
)
NEW_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, AbiE, and AbiZ are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, and traitmech:000228, respectively. "
    "Lopatina et al., Fineran et al., Dy et al., and Durmaz and Klaenhammer "
    "still support Abi as a genomically encoded phage defense strategy that "
    "spans mechanistically diverse toxin-antitoxin, premature-lysis, and other "
    "Abi families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or cell-death "
    "mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiZ as split out in the open abortive-infection subfamily "
    "split-gap discussion after minting traitmech:000228 for the AbiZ system; "
    "other abortive-infection families remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000228",
    "label": "AbiZ system",
    "definition": (
        "An abortive infection system in which an organism possesses an abiZ "
        "locus encoding a membrane-associated lactococcal phage-resistance "
        "determinant that accelerates infected-cell lysis through "
        "AbiZ-enhanced holin/lysin activity and restricts P335 phage "
        "propagation."
    ),
    "definition_source": DURMAZ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        {
            "reference": DURMAZ,
            "snippet": (
                "A single ORF, designated abiZ, was found to be responsible "
                "for a significant reduction in plaque size and an efficiency "
                "of plaquing (EOP) of 10−6, without affecting phage adsorption"
            ),
            "notes": (
                "Durmaz and Klaenhammer localized the pTR2030 AbiZ phage "
                "resistance determinant to the abiZ open reading frame."
            ),
        },
        {
            "reference": DURMAZ,
            "snippet": (
                "The new phage resistance gene, designated abiZ, encodes an "
                "abortive infection resistance which results in cell death "
                "after infection and appears to limit the production of "
                "progeny phage"
            ),
            "notes": (
                "Durmaz and Klaenhammer place the abiZ determinant in the "
                "abortive-infection class rather than adsorption or "
                "restriction-modification defense."
            ),
        },
        {
            "reference": DURMAZ,
            "snippet": (
                "The average burst size of φ31 on NCK203(pTRKH2) of 316 ± 68 "
                "was reduced by two logs to 3 ± 1.4 for NCK203(pTRKH2:E4)"
            ),
            "notes": (
                "Durmaz and Klaenhammer show that the abiZ-containing subclone "
                "strongly reduces production of infectious phage progeny."
            ),
        },
        {
            "reference": DURMAZ,
            "snippet": (
                "The measures of both optical density and viable cell count "
                "showed that holin- and lysin-induced lysis in the phage-free "
                "system occurred 30 min earlier when AbiZ was present"
            ),
            "notes": (
                "Durmaz and Klaenhammer support AbiZ-associated acceleration "
                "of holin/lysin-driven cell lysis."
            ),
        },
        {
            "reference": DURMAZ,
            "snippet": (
                "AbiZ enhances the permeability of cells in which holin alone "
                "was expressed"
            ),
            "notes": (
                "Durmaz and Klaenhammer connect AbiZ to increased "
                "membrane-permeability in holin-induced cells."
            ),
        },
        {
            "reference": PHILIPPE,
            "snippet": (
                "We focus our investigation on AbiZ, an abortive infection "
                "mechanism discovered and described by Durmaz et al. [18] as "
                "leading to premature cell lysis during phage infection, and "
                "one of the most understood Abi mechanisms on L. lactis"
            ),
            "notes": (
                "Philippe et al. support AbiZ as a named Lactococcus abortive "
                "infection mechanism with phage-induced premature lysis."
            ),
        },
        {
            "reference": PHILIPPE,
            "snippet": (
                "NCK4 and IL6 cells were made electrocompetent and then "
                "electroporated with plasmid pTRK914 (pTRK686:abiZ, Cmr) to "
                "obtain NCK5 and IL7 (AbiZ+) using methods from [31]"
            ),
            "notes": (
                "Philippe et al. reused the abiZ-containing pTRK914 plasmid "
                "to construct independent AbiZ-positive Lactococcus strains."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Durmaz and Klaenhammer localized the pTR2030 abiZ determinant "
                "from Lactococcus lactis ME2 and showed that abiZ expression "
                "in Lactococcus lactis NCK203 produced abortive phage "
                "resistance with premature lysis of phage-infected cells."
            ),
            "reference": DURMAZ,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abiz_premature_lysis_antiphage_activity",
            "title": "AbiZ accelerates premature lysis to restrict P335 phages",
            "description": (
                "Evidence-backed process sketch linking an abiZ locus to "
                "enhanced holin/lysin activity, premature infected-cell lysis, "
                "restricted phage propagation, and abortive-infection system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiZ at the system level without "
                "asserting a direct physical AbiZ-holin interaction, an exact "
                "phage activator, or one known phage-escape mutation."
            ),
            "nodes": [
                {
                    "node_id": "abiz_locus",
                    "label": "abiZ locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abortive-infection locus encoding the "
                        "membrane-associated AbiZ phage resistance determinant."
                    ),
                },
                {
                    "node_id": "abiz_enhanced_holin_lysin_activity",
                    "label": "AbiZ-enhanced holin/lysin activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Phage holin/lysin-associated lysis activity that is "
                        "accelerated in cells carrying AbiZ."
                    ),
                },
                {
                    "node_id": "premature_infected_cell_lysis",
                    "label": "premature infected-cell lysis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Early lysis of a phage-infected host cell before many "
                        "infectious phage particles have been assembled."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of P335 phage propagation in an "
                        "AbiZ-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abiz_system_trait",
                    "label": "AbiZ system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000228",
                    "description": (
                        "Possession of a genome-encoded AbiZ "
                        "premature-lysis abortive-infection system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abiz_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abiz_enhanced_holin_lysin_activity",
                    "description": (
                        "The abiZ locus contributes to accelerated "
                        "holin/lysin-driven lysis."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ,
                            "snippet": (
                                "The measures of both optical density and "
                                "viable cell count showed that holin- and "
                                "lysin-induced lysis in the phage-free system "
                                "occurred 30 min earlier when AbiZ was present"
                            ),
                            "notes": (
                                "Durmaz and Klaenhammer assayed φ31 holin and "
                                "lysin expression in the presence of abiZ."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abiz_enhanced_holin_lysin_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "premature_infected_cell_lysis",
                    "description": (
                        "AbiZ-enhanced lysis activity contributes to "
                        "premature lysis of phage-infected cells."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ,
                            "snippet": (
                                "AbiZ enhances the permeability of cells in "
                                "which holin alone was expressed"
                            ),
                            "notes": (
                                "Durmaz and Klaenhammer connect AbiZ to "
                                "enhanced holin-associated membrane "
                                "permeability."
                            ),
                        }
                    ],
                },
                {
                    "subject": "premature_infected_cell_lysis",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Premature AbiZ-associated lysis limits the yield of "
                        "infectious P335 phage progeny."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ,
                            "snippet": (
                                "The average burst size of φ31 on "
                                "NCK203(pTRKH2) of 316 ± 68 was reduced by "
                                "two logs to 3 ± 1.4 for NCK203(pTRKH2:E4)"
                            ),
                            "notes": (
                                "Durmaz and Klaenhammer measured a lower "
                                "single-step burst size in cells carrying the "
                                "AbiZ-active E4 subclone."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abiz_system_trait",
                    "description": (
                        "Restriction of P335 phage propagation realizes the "
                        "AbiZ abortive-infection defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ,
                            "snippet": (
                                "The new phage resistance gene, designated "
                                "abiZ, encodes an abortive infection "
                                "resistance which results in cell death after "
                                "infection and appears to limit the production "
                                "of progeny phage"
                            ),
                            "notes": (
                                "Durmaz and Klaenhammer classify abiZ as an "
                                "abortive-infection phage resistance gene."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abiz_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiZ system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": PHILIPPE,
                            "snippet": (
                                "AbiZ, an abortive infection mechanism "
                                "discovered and described by Durmaz et al. "
                                "[18] as leading to premature cell lysis "
                                "during phage infection"
                            ),
                            "notes": (
                                "Philippe et al. place AbiZ in the abortive "
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

    discussions = record.get("discussions") or []
    discussion = next(
        item
        for item in discussions
        if item.get("discussion_id") == "abortive-infection-subfamily-split-gap"
    )
    if discussion["rationale"] == NEW_DISCUSSION_RATIONALE:
        assert discussion["status"] == "OPEN"
        return record

    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    assert discussion["rationale"] == OLD_DISCUSSION_RATIONALE
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
            "Minted AbiZ system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v105."
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
            "AbiZ system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
