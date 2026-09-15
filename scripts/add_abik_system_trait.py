#!/usr/bin/env python3
"""Add the AbiK system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abik_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

EMOND = "DOI:10.1128/aem.63.4.1274-1283.1997"
BOUCHER = "DOI:10.1099/00221287-146-2-445"
FORTIER = "DOI:10.1128/JB.187.11.3721-3730.2005"
WANG = "DOI:10.1093/nar/gkr397"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T21:30:00Z"
PARENT_TIMESTAMP = "2026-09-15T21:30:01Z"

OLD_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, AbiE, and AbiZ are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, and traitmech:000228, respectively. "
    "Lopatina et al., Fineran et al., Dy et al., and Durmaz and Klaenhammer "
    "still support Abi as a genomically encoded phage defense strategy that "
    "spans mechanistically diverse toxin-antitoxin, premature-lysis, and other "
    "Abi families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or cell-death "
    "mechanism, and phage escape routes."
)
NEW_DISCUSSION_RATIONALE = (
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
PARENT_CHANGES = (
    "Documented AbiK as split out in the open abortive-infection subfamily "
    "split-gap discussion after minting traitmech:000229 for the AbiK system; "
    "other abortive-infection families remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000229",
    "label": "AbiK system",
    "definition": (
        "An abortive infection system in which an organism possesses an abiK "
        "locus encoding a reverse-transcriptase-related polymerase that uses "
        "conserved RT motifs for phage resistance and restricts 936/P335 "
        "lactococcal phage propagation."
    ),
    "definition_source": EMOND,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        {
            "reference": EMOND,
            "snippet": (
                "The phage resistance mechanism encoded on pSRQ800 is a "
                "temperature-sensitive abortive infection system (Abi)"
            ),
            "notes": (
                "Emond et al. localized a lactococcal plasmid-encoded "
                "abortive-infection mechanism that strongly resists 936 and "
                "P335 phages."
            ),
        },
        {
            "reference": EMOND,
            "snippet": (
                "orf1 (renamed abiK) coded for a predicted protein of 599 "
                "amino acids (AbiK)"
            ),
            "notes": (
                "Emond et al. identified abiK as the open reading frame "
                "needed for the pSRQ800 Abi phenotype."
            ),
        },
        {
            "reference": EMOND,
            "snippet": (
                "No phage DNA replication nor phage structural protein "
                "production was detected in infected AbiK+ L. lactis cells"
            ),
            "notes": (
                "Emond et al. support an AbiK-associated block at or before "
                "DNA replication for the ul36 lactococcal phage."
            ),
        },
        {
            "reference": BOUCHER,
            "snippet": (
                "Only immature forms (concatemeric and circular DNA) of phage "
                "p2 DNA were found, indicating that the presence of AbiK "
                "prevented phage DNA maturation"
            ),
            "notes": (
                "Boucher et al. show that AbiK can block later DNA maturation "
                "rather than DNA replication itself, depending on the "
                "lactococcal phage tested."
            ),
        },
        {
            "reference": FORTIER,
            "snippet": (
                "the antiphage activity depends on the level of expression of "
                "the abiK gene and on the presence of a reverse transcriptase "
                "(RT) motif in AbiK"
            ),
            "notes": (
                "Fortier et al. connect AbiK phage resistance to conserved "
                "reverse-transcriptase motifs in the AbiK protein."
            ),
        },
        {
            "reference": FORTIER,
            "snippet": (
                "Conservative mutations in key positions resulted in the "
                "complete loss of the resistance phenotype"
            ),
            "notes": (
                "Fortier et al. mutated AbiK RT motifs and showed that key "
                "positions are necessary for AbiK-mediated resistance."
            ),
        },
        {
            "reference": WANG,
            "snippet": (
                "AbiK does not exhibit the properties expected for an RT, but "
                "polymerizes long DNAs of ‘random’ sequence, analogous to a "
                "terminal transferase"
            ),
            "notes": (
                "Wang et al. biochemically characterized AbiK as an "
                "RT-related polymerase with template-independent DNA "
                "polymerization activity."
            ),
        },
        {
            "reference": WANG,
            "snippet": (
                "Mutagenesis experiments indicate that the polymerase activity "
                "resides in the RT motifs and is essential for phage "
                "resistance in vivo"
            ),
            "notes": (
                "Wang et al. support AbiK RT-motif polymerase activity as an "
                "essential contributor to phage resistance."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Emond et al. isolated the pSRQ800 abiK determinant from "
                "Lactococcus lactis subsp. lactis W1 and showed that it "
                "confers abortive infection against 936 and P335 lactococcal "
                "phages when introduced into phage-sensitive Lactococcus "
                "lactis strains."
            ),
            "reference": EMOND,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abik_rt_polymerase_antiphage_activity",
            "title": "AbiK RT-related polymerase activity restricts lactococcal phages",
            "description": (
                "Evidence-backed process sketch linking an abiK locus to "
                "AbiK RT-related polymerase activity, phage DNA replication "
                "or maturation blocks, restricted phage propagation, and "
                "abortive-infection system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiK at the system level without "
                "asserting the natural AbiK DNA primer or product, the "
                "endogenous polymerase substrate, or one universal DNA-stage "
                "block for all sensitive phages."
            ),
            "nodes": [
                {
                    "node_id": "abik_locus",
                    "label": "abiK locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abortive-infection locus encoding the AbiK "
                        "RT-related polymerase."
                    ),
                },
                {
                    "node_id": "abik_rt_polymerase_activity",
                    "label": "AbiK RT-related polymerase activity",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "Reverse-transcriptase-motif-dependent DNA "
                        "polymerase activity of AbiK."
                    ),
                },
                {
                    "node_id": "interrupted_phage_dna_replication_or_maturation",
                    "label": "interrupted phage DNA replication or maturation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Phage-specific interruption of DNA replication or "
                        "DNA maturation in AbiK-containing infected "
                        "Lactococcus cells."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of 936 or P335 phage propagation "
                        "in an AbiK-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abik_system_trait",
                    "label": "AbiK system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000229",
                    "description": (
                        "Possession of a genome-encoded AbiK "
                        "RT-related abortive-infection system."
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
                    "subject": "abik_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abik_rt_polymerase_activity",
                    "description": (
                        "The abiK locus encodes an AbiK protein whose "
                        "conserved RT motifs support antiphage activity."
                    ),
                    "evidence": [
                        {
                            "reference": FORTIER,
                            "snippet": (
                                "the antiphage activity depends on the level "
                                "of expression of the abiK gene and on the "
                                "presence of a reverse transcriptase (RT) "
                                "motif in AbiK"
                            ),
                            "notes": (
                                "Fortier et al. connect abiK expression and "
                                "AbiK RT motifs to the phage-resistance "
                                "phenotype."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abik_rt_polymerase_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "AbiK RT-motif polymerase activity is required for "
                        "the in vivo phage-resistance phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "Mutagenesis experiments indicate that the "
                                "polymerase activity resides in the RT motifs "
                                "and is essential for phage resistance in vivo"
                            ),
                            "notes": (
                                "Wang et al. showed that AbiK RT motifs carry "
                                "the in vitro polymerase activity and are "
                                "essential for phage resistance in vivo."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abik_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "interrupted_phage_dna_replication_or_maturation",
                    "description": (
                        "The AbiK determinant produces a phage-specific block "
                        "at DNA replication or DNA maturation."
                    ),
                    "evidence": [
                        {
                            "reference": BOUCHER,
                            "snippet": (
                                "Only immature forms (concatemeric and "
                                "circular DNA) of phage p2 DNA were found, "
                                "indicating that the presence of AbiK "
                                "prevented phage DNA maturation"
                            ),
                            "notes": (
                                "Boucher et al. found immature DNA forms for "
                                "phage p2 and compared that phenotype with "
                                "the earlier ul36 DNA-replication block."
                            ),
                        }
                    ],
                },
                {
                    "subject": "interrupted_phage_dna_replication_or_maturation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Interrupting DNA replication or maturation limits "
                        "completion of the phage lytic cycle."
                    ),
                    "evidence": [
                        {
                            "reference": EMOND,
                            "snippet": (
                                "No phage DNA replication nor phage "
                                "structural protein production was detected "
                                "in infected AbiK+ L. lactis cells"
                            ),
                            "notes": (
                                "Emond et al. show that AbiK prevents ul36 "
                                "DNA replication and structural-protein "
                                "production in infected Lactococcus lactis."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abik_system_trait",
                    "description": (
                        "Restriction of 936/P335 phage propagation realizes "
                        "the AbiK abortive-infection defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": EMOND,
                            "snippet": (
                                "The phage resistance mechanism encoded on "
                                "pSRQ800 is a temperature-sensitive abortive "
                                "infection system (Abi)"
                            ),
                            "notes": (
                                "Emond et al. define the pSRQ800 AbiK "
                                "determinant as an abortive-infection phage "
                                "resistance system."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abik_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiK system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "AbiK, which is required for abortive phage "
                                "infection in the Gram-positive bacterium "
                                "Lactococcus lactis"
                            ),
                            "notes": (
                                "Wang et al. place AbiK in the abortive "
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
            "Minted AbiK system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v106."
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
            "AbiK system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
