#!/usr/bin/env python3
"""Add the AbiT system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abit_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

BOUCHARD = "DOI:10.1128/JB.184.22.6325-6332.2002"
LABRIE = "DOI:10.1128/AEM.01755-12"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T22:05:00Z"
PARENT_TIMESTAMP = "2026-09-15T22:05:01Z"

OLD_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, and AbiK are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, and "
    "traitmech:000229, respectively. Lopatina et al., Fineran et al., Dy "
    "et al., Durmaz and Klaenhammer, and Wang et al. still support Abi as a "
    "genomically encoded phage defense strategy that spans mechanistically "
    "diverse toxin-antitoxin, premature-lysis, RT-related polymerase, and "
    "other Abi families. Additional narrower TraitRecords need separate "
    "review to ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
NEW_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, and AbiT are split out as "
    "traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, and traitmech:000230, "
    "respectively. Lopatina et al., Fineran et al., Dy et al., Durmaz and "
    "Klaenhammer, Wang et al., and Bouchard et al. still support Abi as a "
    "genomically encoded phage defense strategy that spans mechanistically "
    "diverse toxin-antitoxin, premature-lysis, RT-related polymerase, "
    "two-component, and other Abi families. Additional narrower TraitRecords "
    "need separate review to ground each subfamily's trigger, effector, "
    "growth-arrest or cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiT as split out in the open abortive-infection subfamily "
    "split-gap discussion after minting traitmech:000230 for the AbiT system; "
    "other abortive-infection families remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000230",
    "label": "AbiT system",
    "definition": (
        "An abortive infection system in which an organism possesses the "
        "two-gene pED1 abiT locus whose constitutively cotranscribed abiTi "
        "and abiTii genes encode an AbiTi-AbiTii phage-resistance module that "
        "acts late in the 936/P335 lactococcal phage lytic cycle."
    ),
    "definition_source": BOUCHARD,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        {
            "reference": BOUCHARD,
            "snippet": (
                "Here, we describe the isolation and characterization of a "
                "novel Abi mechanism encoded by plasmid pED1 from L. lactis"
            ),
            "notes": (
                "Bouchard et al. identified the plasmid pED1-encoded AbiT "
                "abortive-infection mechanism in Lactococcus lactis."
            ),
        },
        {
            "reference": BOUCHARD,
            "snippet": (
                "The system is composed of two constitutively cotranscribed "
                "genes encoding putative proteins of 127 and 213 amino acids, "
                "named AbiTi and AbiTii, respectively"
            ),
            "notes": (
                "Bouchard et al. support defining AbiT around the paired "
                "abiTi and abiTii host genes rather than around a single gene."
            ),
        },
        {
            "reference": BOUCHARD,
            "snippet": (
                "The fact that resistant cells do not survive phage infection "
                "proves that the antiphage system carried by pED1 is an Abi "
                "mechanism. It was therefore named AbiT."
            ),
            "notes": (
                "Bouchard et al. placed the pED1 phage-resistance determinant "
                "in the abortive-infection class and named it AbiT."
            ),
        },
        {
            "reference": BOUCHARD,
            "snippet": "Two genes are responsible for the antiphage activity of AbiT",
            "notes": (
                "Bouchard et al. support a two-gene genetic basis for AbiT "
                "phage resistance."
            ),
        },
        {
            "reference": BOUCHARD,
            "snippet": (
                "It appears that AbiT affects DNA replication and also "
                "prevents effective encapsidation"
            ),
            "notes": (
                "Bouchard et al. connect AbiT to both impaired phage DNA "
                "replication and ineffective phage encapsidation."
            ),
        },
        {
            "reference": LABRIE,
            "snippet": (
                "AbiT-resistant phage mutants derived from the wild-type "
                "AbiT-sensitive lactococcal phages p2, bIL170, and P008 were "
                "isolated and characterized"
            ),
            "notes": (
                "Labrie et al. generated AbiT-resistant mutants from three "
                "sensitive 936-group Lactococcus phages."
            ),
        },
        {
            "reference": LABRIE,
            "snippet": (
                "three distinct phage genes involved in AbiT activity were "
                "identified"
            ),
            "notes": (
                "Labrie et al. found that AbiT sensitivity maps to multiple "
                "nonhomologous phage genes rather than one universal phage "
                "escape determinant."
            ),
        },
        {
            "reference": LABRIE,
            "snippet": (
                "AbiT blocks capsid protein synthesis of the wild-type phage, "
                "while it does not affect the resistant phage p2.t3, mutated "
                "in the capsid gene"
            ),
            "notes": (
                "Labrie et al. connect a p2 major-capsid-protein escape "
                "mutation to restoration of capsid protein synthesis in the "
                "presence of AbiT."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Bouchard et al. isolated pED1 from Lactococcus lactis W51, "
                "localized the AbiT phage-resistance phenotype to abiTi and "
                "abiTii, and showed that the determinant restricts 936 and "
                "P335 Lactococcus phages after transfer into phage-sensitive "
                "Lactococcus lactis strains."
            ),
            "reference": BOUCHARD,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abit_late_phage_development_block",
            "title": "AbiT activity blocks late phage development",
            "description": (
                "Evidence-backed process sketch linking the two-gene abiT "
                "locus to AbiTi-AbiTii antiphage activity, impaired phage DNA "
                "replication or capsid production, restricted phage "
                "propagation, and abortive-infection system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiT at the system level without "
                "asserting a molecular function for AbiTi or AbiTii, the "
                "exact host target, the direct phage activator, or that every "
                "AbiT-insensitive phage mutates the same phage gene."
            ),
            "nodes": [
                {
                    "node_id": "abit_locus",
                    "label": "abiT locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene abortive-infection locus encoding AbiTi "
                        "and AbiTii."
                    ),
                },
                {
                    "node_id": "abiti_abitii_antiphage_activity",
                    "label": "AbiTi-AbiTii antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection antiphage activity mediated by "
                        "the AbiTi and AbiTii host proteins."
                    ),
                },
                {
                    "node_id": "interrupted_late_phage_development",
                    "label": "interrupted late phage development",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "AbiT-associated impairment of phage DNA replication, "
                        "phage DNA encapsidation, or capsid protein "
                        "synthesis after early phage gene expression."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of 936 or P335 phage propagation "
                        "in an AbiT-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abit_system_trait",
                    "label": "AbiT system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000230",
                    "description": (
                        "Possession of a genome-encoded AbiT two-component "
                        "abortive-infection system."
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
                    "subject": "abit_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abiti_abitii_antiphage_activity",
                    "description": (
                        "The abiT locus carries abiTi, abiTii, and the "
                        "promoter required for the complete phage-resistance "
                        "phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": BOUCHARD,
                            "snippet": (
                                "Two genes are responsible for the antiphage "
                                "activity of AbiT"
                            ),
                            "notes": (
                                "Bouchard et al. showed that both abiT genes "
                                "are required for full AbiT activity."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abiti_abitii_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "interrupted_late_phage_development",
                    "description": (
                        "AbiT activity interferes with late phage "
                        "development after early phage gene expression."
                    ),
                    "evidence": [
                        {
                            "reference": BOUCHARD,
                            "snippet": (
                                "It appears that AbiT affects DNA replication "
                                "and also prevents effective encapsidation"
                            ),
                            "notes": (
                                "Bouchard et al. found reduced DNA "
                                "replication and failed encapsidation in "
                                "AbiT-containing infected cells."
                            ),
                        },
                        {
                            "reference": LABRIE,
                            "snippet": (
                                "AbiT blocks capsid protein synthesis of the "
                                "wild-type phage, while it does not affect "
                                "the resistant phage p2.t3, mutated in the "
                                "capsid gene"
                            ),
                            "notes": (
                                "Labrie et al. refine the AbiT phenotype by "
                                "linking wild-type p2 capsid protein "
                                "synthesis blockage to an AbiT-sensitive "
                                "capsid gene."
                            ),
                        },
                    ],
                },
                {
                    "subject": "interrupted_late_phage_development",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Failed phage DNA maturation or capsid production "
                        "limits completion of the phage lytic cycle."
                    ),
                    "evidence": [
                        {
                            "reference": BOUCHARD,
                            "snippet": (
                                "The monitoring of the intracellular phage "
                                "infection process by DNA replication, gene "
                                "expression, and electron microscopy as well "
                                "as the study of phage mutants by genome "
                                "mapping indicated that AbiT is likely to "
                                "act at a later stage of the phage lytic cycle"
                            ),
                            "notes": (
                                "Bouchard et al. support a late-stage block "
                                "in the phage lytic cycle."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abit_system_trait",
                    "description": (
                        "Restriction of 936/P335 phage propagation realizes "
                        "the AbiT abortive-infection defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": BOUCHARD,
                            "snippet": (
                                "The fact that resistant cells do not survive "
                                "phage infection proves that the antiphage "
                                "system carried by pED1 is an Abi mechanism. "
                                "It was therefore named AbiT."
                            ),
                            "notes": (
                                "Bouchard et al. define AbiT as a pED1 "
                                "abortive-infection phage resistance system."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abit_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiT system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BOUCHARD,
                            "snippet": (
                                "Here, we describe the isolation and "
                                "characterization of a novel Abi mechanism "
                                "encoded by plasmid pED1 from L. lactis"
                            ),
                            "notes": (
                                "Bouchard et al. place AbiT in the abortive "
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
            "Minted AbiT system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v107."
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
            "AbiT system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
