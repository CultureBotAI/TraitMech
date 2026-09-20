#!/usr/bin/env python3
"""Add the AbiH system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abih_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

PREVOTS = "DOI:10.1111/j.1574-6968.1996.tb08446.x"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T08:12:00Z"
PARENT_TIMESTAMP = "2026-09-20T08:12:01Z"
IDENTIFIER = "traitmech:000304"
PROPOSAL = "proposals/metpo_traitmech_v181"

HMM_ROW = (
    "| AbiH__AbiH                                       | "
    "AbiH__AbiH                                       | AbiH                   | "
    "PF14253.7               | 30.9   |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, and Stk2 are "
    "split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, and "
    "traitmech:000303, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., and Depardieu et al. still support "
    "Abi as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, and other Abi "
    "families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, and AbiH "
    "are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, and traitmech:000304, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang "
    "et al., Bouchard et al., Haaber et al., Owen et al., Depardieu "
    "et al., and Prevots et al. still support Abi as a genomically "
    "encoded phage defense strategy that spans mechanistically diverse "
    "toxin-antitoxin, premature-lysis, RT-related polymerase, "
    "two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH "
    "phage resistance, and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's "
    "trigger, effector, growth-arrest or cell-death mechanism, and "
    "phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiH as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000304 for "
    "the AbiH system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiH | 10\\.1111/j\\.1574-6968\\.1996\\.tb08446\\.x | "
            "Cloning and sequencing of the novel abortive infection gene "
            "abiH of Lactococcus lactis ssp\\. lactis biovar\\. "
            "diacetylactis S94"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiH system "
            "to the Prevots et al. abiH cloning paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records the PF14253.7-backed "
            "AbiH__AbiH profile under the AbiH model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiH\tAbiH\t1\t1\tAbiH__AbiH",
        "notes": (
            "The DefenseFinder rules table models AbiH as a one-component "
            "system requiring the AbiH__AbiH profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiH system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "abiH-family locus represented by the DefenseFinder AbiH__AbiH "
        "profile and exemplified by the Lactococcus lactis S94 abiH gene "
        "that encodes lactococcal phage abortive-infection resistance."
    ),
    "definition_source": PREVOTS,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiH",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": PREVOTS,
            "snippet": (
                "A gene which encodes resistance by abortive infection "
                "(Abi+) to bacteriophage was cloned from Lactococcus "
                "lactis ssp. lactis biovar. diacetylactis S94"
            ),
            "notes": (
                "Prevots et al. cloned abiH from Lactococcus lactis S94 "
                "and connected the locus to bacteriophage resistance by "
                "abortive infection."
            ),
        },
        {
            "reference": PREVOTS,
            "snippet": (
                "This gene was found to confer a reduction in efficiency "
                "of plating and plaque size for prolate-headed "
                "bacteriophage phi 53 (group I of homology) and total "
                "resistance to the small isometric-headed bacteriophage "
                "phi 59 (group III of homology)"
            ),
            "notes": (
                "Prevots et al. show that the cloned abiH gene restricts "
                "multiple lactococcal phages with distinct plating "
                "phenotypes."
            ),
        },
        {
            "reference": PREVOTS,
            "snippet": (
                "The cloned gene is predicted to encode a polypeptide of "
                "346 amino acid residues with a deduced molecular mass of "
                "41 455 Da"
            ),
            "notes": (
                "Prevots et al. support abiH as an encoded phage-resistance "
                "protein rather than a noncoding marker."
            ),
        },
        {
            "reference": PREVOTS,
            "snippet": "No homology with any previously described genes was found",
            "notes": (
                "Prevots et al. leave the molecular class and effector "
                "mechanism of AbiH unresolved."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Prevots et al. cloned abiH from Lactococcus lactis ssp. "
                "lactis biovar. diacetylactis S94 and showed that the "
                "cloned locus confers abortive-infection phage resistance."
            ),
            "reference": PREVOTS,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abih_locus_restricts_lactococcal_phages",
            "title": "AbiH activity restricts lactococcal phages",
            "description": (
                "Conservative system-level sketch linking an abiH-family "
                "locus to AbiH antiphage activity, reduced lactococcal "
                "phage plaque formation, restricted phage propagation, and "
                "abortive-infection system possession without asserting "
                "the unresolved phage trigger or molecular target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiH as a named DefenseFinder "
                "single-profile abortive-infection system whose prototype "
                "abiH gene reduces or abolishes plating by tested "
                "lactococcal phages while leaving the direct phage trigger, "
                "AbiH molecular function, host or phage target, arrest "
                "route, and phage escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abih_locus",
                    "label": "abiH locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abiH-family abortive-infection locus "
                        "represented by the DefenseFinder AbiH__AbiH "
                        "profile."
                    ),
                },
                {
                    "node_id": "abih_antiphage_activity",
                    "label": "AbiH antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection phage resistance mediated by "
                        "the AbiH protein."
                    ),
                },
                {
                    "node_id": "lactococcal_phage_plaque_formation",
                    "label": "lactococcal phage plaque formation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Formation of plaques by AbiH-sensitive phi 53 and "
                        "phi 59 phages on a Lactococcus lactis indicator "
                        "lawn."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of AbiH-sensitive lactococcal "
                        "phage propagation in an AbiH-containing infected "
                        "host cell."
                    ),
                },
                {
                    "node_id": "abih_system_trait",
                    "label": "AbiH system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiH "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded "
                        "abortive-infection phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abih_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abih_antiphage_activity",
                    "description": (
                        "The abiH-family locus encodes an "
                        "abortive-infection phage-resistance determinant, "
                        "and DefenseFinder models AbiH as a one-profile "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": PREVOTS,
                            "snippet": (
                                "A gene which encodes resistance by "
                                "abortive infection (Abi+) to bacteriophage"
                            ),
                            "notes": (
                                "Prevots et al. identify the cloned abiH "
                                "gene as the abortive-infection "
                                "phage-resistance determinant."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "abih_antiphage_activity",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "lactococcal_phage_plaque_formation",
                    "description": (
                        "AbiH activity reduces phi 53 plating and plaque "
                        "size and confers total resistance to phi 59."
                    ),
                    "evidence": [
                        {
                            "reference": PREVOTS,
                            "snippet": (
                                "This gene was found to confer a reduction "
                                "in efficiency of plating and plaque size "
                                "for prolate-headed bacteriophage phi 53 "
                                "(group I of homology) and total resistance "
                                "to the small isometric-headed "
                                "bacteriophage phi 59"
                            ),
                            "notes": (
                                "Prevots et al. directly measure reduced "
                                "or abolished plaque formation for tested "
                                "lactococcal phages."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abih_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Reduced plating and total phi 59 resistance "
                        "indicate that AbiH limits completion of tested "
                        "lactococcal phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": PREVOTS,
                            "snippet": (
                                "reduction in efficiency of plating and "
                                "plaque size for prolate-headed "
                                "bacteriophage phi 53 (group I of "
                                "homology) and total resistance to the "
                                "small isometric-headed bacteriophage phi "
                                "59 (group III of homology)"
                            ),
                            "notes": (
                                "Prevots et al. support both a partial phi "
                                "53 block and total phi 59 resistance from "
                                "the cloned abiH gene."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abih_system_trait",
                    "description": (
                        "Restriction of lactococcal phage propagation "
                        "realizes the AbiH abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": PREVOTS,
                            "snippet": (
                                "encodes resistance by abortive infection "
                                "(Abi+) to bacteriophage"
                            ),
                            "notes": (
                                "Prevots et al. classify the cloned abiH "
                                "resistance determinant as abortive "
                                "infection."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abih_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiH system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": PREVOTS,
                            "snippet": (
                                "encodes resistance by abortive infection "
                                "(Abi+) to bacteriophage"
                            ),
                            "notes": (
                                "Prevots et al. support AbiH as an "
                                "abortive-infection system."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abih-trigger-and-effector-gap",
            "prompt": (
                "Resolve the AbiH phage trigger, molecular activity, and "
                "direct arrest target before minting narrower AbiH "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Prevots et al. support AbiH as a named lactococcal "
                "abortive-infection gene whose cloned S94 locus reduces or "
                "blocks plating by tested lactococcal phages, and "
                "DefenseFinder represents AbiH with a one-profile rule. "
                "This system-level record leaves the phage trigger, AbiH "
                "molecular function, direct cellular target, "
                "growth-arrest or cell-death route, and phage escape "
                "routes unresolved."
            ),
            "attaches_to": ["causal_graphs#abih_locus_restricts_lactococcal_phages"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
        }
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
    if discussion["rationale"] == NEW_PARENT_RATIONALE:
        assert discussion["status"] == "OPEN"
        return record

    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    assert discussion["rationale"] == OLD_PARENT_RATIONALE
    discussion["rationale"] = NEW_PARENT_RATIONALE

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
            "Minted AbiH system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_output(record: dict[str, Any], filename: str) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / filename)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_abortive_parent(load_trait(ABORTIVE))
    validate_output(record, TARGET.name)
    validate_output(parent, ABORTIVE.name)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "AbiH system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
