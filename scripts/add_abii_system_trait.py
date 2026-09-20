#!/usr/bin/env python3
"""Add the AbiI system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abii_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

SU = "DOI:10.1016/S0168-1656(97)01692-1"
SU_PMID = "PMID:9195753"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T18:33:34Z"
PARENT_TIMESTAMP = "2026-09-20T18:33:35Z"
IDENTIFIER = "traitmech:000316"
PROPOSAL = "proposals/metpo_traitmech_v193"

HMM_ROW = (
    "| AbiI__AbiI                                       | "
    "AbiI__AbiI                                       | AbiI                   | "
    "Custom                  | 20     |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, and "
    "AbiG are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, traitmech:000304, and traitmech:000306, "
    "respectively. Lopatina et al., Fineran et al., Dy et al., Durmaz "
    "and Klaenhammer, Wang et al., Bouchard et al., Haaber et al., Owen "
    "et al., Depardieu et al., Prevots et al., and O'Connor et al. still "
    "support Abi as a genomically encoded phage defense strategy that "
    "spans mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "and other Abi families. Additional narrower TraitRecords need "
    "separate review to ground each subfamily's trigger, effector, "
    "growth-arrest or cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "and AbiI are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, traitmech:000304, traitmech:000306, and "
    "traitmech:000316, respectively. Lopatina et al., Fineran et al., Dy "
    "et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., Depardieu et al., Prevots et al., "
    "O'Connor et al., and Su et al. still support Abi as a genomically "
    "encoded phage defense strategy that spans mechanistically diverse "
    "toxin-antitoxin, premature-lysis, RT-related polymerase, "
    "two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, and other Abi "
    "families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiI as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000316 for "
    "the AbiI system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiI | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiI model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiI\tAbiI\t1\t1\tAbiI__AbiI",
        "notes": (
            "The DefenseFinder rules table models AbiI as a one-component "
            "system requiring the AbiI__AbiI profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiI__AbiI under the "
            "AbiI model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiI system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "abiI-family locus represented by the DefenseFinder AbiI__AbiI "
        "profile and exemplified by the Lactococcus lactis M138 pND852 "
        "locus whose single abiI open reading frame restricts "
        "lactococcal phage propagation by an abortive-infection "
        "mechanism."
    ),
    "definition_source": SU,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiI",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": SU_PMID,
            "snippet": (
                "Plasmid pND852 (56 kb) encodes nisin resistance and was "
                "isolated from Lactococcus lactis ssp lactis (L. lactis) "
                "M138 by conjugation to L. lactis LM0230"
            ),
            "notes": (
                "Su et al. identified plasmid pND852 from Lactococcus "
                "lactis M138 as the source of the abiI-associated phage "
                "resistance locus."
            ),
        },
        {
            "reference": SU_PMID,
            "snippet": (
                "It conferred strong resistance to the isometric-headed "
                "phage phi 712 and partial resistance to the prolate-headed "
                "phage phi c2"
            ),
            "notes": (
                "Su et al. show that pND852 confers resistance to tested "
                "lactococcal phages."
            ),
        },
        {
            "reference": SU_PMID,
            "snippet": (
                "A 2.6 kb HpaII fragment encoding phage resistance was "
                "cloned into the streptococcal/Bacillus hybrid vector "
                "pGB301 to generate pND817"
            ),
            "notes": (
                "Su et al. localized phage resistance from pND852 to the "
                "2.6 kb fragment in pND817."
            ),
        },
        {
            "reference": SU_PMID,
            "snippet": (
                "The mechanism of phage resistance encoded by pND817 "
                "involved abortive infection"
            ),
            "notes": (
                "Su et al. classified the pND817 phage-resistance "
                "mechanism as abortive infection."
            ),
        },
        {
            "reference": SU_PMID,
            "snippet": (
                "reduction in burst size from 166 to 6 at 30 degrees C "
                "and from 160 to 90 at 37 degrees C"
            ),
            "notes": (
                "Su et al. measured reduced phage burst size from the "
                "cloned pND817 abortive-infection locus."
            ),
        },
        {
            "reference": SU_PMID,
            "snippet": (
                "DNA sequencing revealed that the abortive infection was "
                "encoded by a single open reading frame (ORF), designated "
                "abiI, encoding a 332 amino acid protein"
            ),
            "notes": (
                "Su et al. support a single abiI open reading frame as the "
                "coding sequence for the pND817 abortive-infection locus."
            ),
        },
        {
            "reference": SU_PMID,
            "snippet": (
                "Frame shift mutation at the unique EcoRI site within the "
                "ORF resulted in loss of the Abi+ phenotype"
            ),
            "notes": (
                "Su et al. verified that the abiI open reading frame is "
                "required for the phage-resistance phenotype."
            ),
        },
        {
            "reference": SU_PMID,
            "snippet": (
                "Neither abiI nor the predicted product showed significant "
                "homology to any existing sequence in the GenBank database"
            ),
            "notes": (
                "Su et al. did not resolve AbiI molecular activity or "
                "homology during the original characterization."
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
                "Su et al. cloned the abiI determinant from Lactococcus "
                "lactis M138 plasmid pND852 into pND817 and showed "
                "abortive-infection phage resistance from a single abiI "
                "open reading frame."
            ),
            "reference": SU,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abii_locus_reduces_lactococcal_phage_burst",
            "title": "AbiI activity restricts lactococcal phage burst size",
            "description": (
                "Conservative system-level sketch linking an abiI-family "
                "locus to AbiI antiphage activity, reduced lactococcal "
                "phage burst size, restricted phage propagation, and "
                "abortive-infection system possession without asserting "
                "the unresolved molecular target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiI as a named DefenseFinder "
                "single-profile abortive-infection system whose pND852 "
                "prototype restricts phi 712 and partially restricts phi "
                "c2. It leaves the direct phage trigger, AbiI molecular "
                "function, cell-death or packaging route, natural locus "
                "breadth, and phage escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abii_locus",
                    "label": "abiI locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abiI-family abortive-infection locus "
                        "represented by the DefenseFinder AbiI__AbiI "
                        "profile."
                    ),
                },
                {
                    "node_id": "abii_antiphage_activity",
                    "label": "AbiI antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection phage resistance mediated by "
                        "the AbiI system."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of lactococcal phage "
                        "propagation in an AbiI-containing infected host "
                        "cell."
                    ),
                },
                {
                    "node_id": "abii_system_trait",
                    "label": "AbiI system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiI "
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
                    "subject": "abii_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abii_antiphage_activity",
                    "description": (
                        "The abiI-family locus encodes an "
                        "abortive-infection phage-resistance determinant, "
                        "and DefenseFinder models AbiI as a one-profile "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": SU_PMID,
                            "snippet": (
                                "DNA sequencing revealed that the abortive "
                                "infection was encoded by a single open "
                                "reading frame (ORF), designated abiI, "
                                "encoding a 332 amino acid protein"
                            ),
                            "notes": (
                                "Su et al. identify abiI as the single ORF "
                                "encoding the pND817 abortive-infection "
                                "phenotype."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "abii_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "AbiI activity strongly restricts phi 712 and "
                        "partially restricts phi c2 propagation in "
                        "Lactococcus lactis."
                    ),
                    "evidence": [
                        {
                            "reference": SU_PMID,
                            "snippet": (
                                "It conferred strong resistance to the "
                                "isometric-headed phage phi 712 and partial "
                                "resistance to the prolate-headed phage "
                                "phi c2"
                            ),
                            "notes": (
                                "Su et al. measured strong or partial "
                                "resistance from the AbiI-containing pND852 "
                                "plasmid for two tested lactococcal phages."
                            ),
                        },
                        {
                            "reference": SU_PMID,
                            "snippet": (
                                "reduction in burst size from 166 to 6 at "
                                "30 degrees C and from 160 to 90 at 37 "
                                "degrees C"
                            ),
                            "notes": (
                                "Su et al. connect pND817 to sharply "
                                "reduced phi 712 burst size."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abii_system_trait",
                    "description": (
                        "Restriction of lactococcal phage propagation "
                        "realizes the AbiI abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": SU_PMID,
                            "snippet": (
                                "The mechanism of phage resistance encoded "
                                "by pND817 involved abortive infection"
                            ),
                            "notes": (
                                "Su et al. classify the pND817 mechanism as "
                                "abortive infection."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abii_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiI system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": SU_PMID,
                            "snippet": (
                                "The mechanism of phage resistance encoded "
                                "by pND817 involved abortive infection"
                            ),
                            "notes": (
                                "Su et al. place AbiI in the abortive "
                                "infection class of phage defense."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abii-trigger-and-effector-gap",
            "prompt": (
                "Resolve the AbiI phage trigger, molecular activity, and "
                "direct arrest target before minting narrower AbiI "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Su et al. support AbiI as a named lactococcal "
                "abortive-infection locus whose cloned pND852 fragment "
                "reduces phi 712 burst size and whose abiI frameshift "
                "abolishes phage resistance. DefenseFinder represents AbiI "
                "with a one-profile rule, but this first system-level "
                "record leaves the phage trigger, AbiI molecular function, "
                "direct host or phage target, growth-arrest or cell-death "
                "route, and phage escape routes unresolved."
            ),
            "evidence": [
                {
                    "reference": SU_PMID,
                    "snippet": (
                        "Neither abiI nor the predicted product showed "
                        "significant homology to any existing sequence in "
                        "the GenBank database"
                    ),
                    "notes": (
                        "Su et al. report no informative sequence "
                        "homology for AbiI in the original "
                        "characterization."
                    ),
                }
            ],
            "attaches_to": ["causal_graphs#abii_locus_reduces_lactococcal_phage_burst"],
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
            "Minted AbiI system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
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
    parser = argparse.ArgumentParser(description=__doc__)
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
            "AbiI system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
