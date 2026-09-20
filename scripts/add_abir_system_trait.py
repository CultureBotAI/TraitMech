#!/usr/bin/env python3
"""Add the AbiR system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abir_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

TWOMEY = "DOI:10.1128/AEM.66.6.2647-2651.2000"
TWOMEY_PMID = "PMID:10831451"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T19:30:10Z"
PARENT_TIMESTAMP = "2026-09-20T19:30:11Z"
IDENTIFIER = "traitmech:000317"
PROPOSAL = "proposals/metpo_traitmech_v194"

ABIRA_ROW = (
    "| AbiR__AbiRa                                      | "
    "AbiR__AbiRa                                      | AbiR                   | "
    "Custom                  | 20     |"
)
ABIRB_ROW = (
    "| AbiR__AbiRb                                      | "
    "AbiR__AbiRb                                      | AbiR                   | "
    "Custom                  | 20     |"
)
ABIRC_ROW = (
    "| AbiR__AbiRc                                      | "
    "AbiR__AbiRc                                      | AbiR                   | "
    "Custom                  | 20     |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, and "
    "AbiI are split out as traitmech:000226, traitmech:000225, "
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
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, and AbiR are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, traitmech:000304, traitmech:000306, "
    "traitmech:000316, and traitmech:000317, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang "
    "et al., Bouchard et al., Haaber et al., Owen et al., Depardieu "
    "et al., Prevots et al., O'Connor et al., Su et al., and Twomey "
    "et al. still support Abi as a genomically encoded phage defense "
    "strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, two-separated-locus "
    "lactococcal AbiR DNA-replication impediment, and other Abi families. "
    "Additional narrower TraitRecords need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiR as split out in the open abortive-infection subfamily "
    "split-gap discussion after minting traitmech:000317 for the AbiR "
    "system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiR | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiR model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiR\tAbiR\t3\t3\tAbiR__AbiRa, AbiR__AbiRb, AbiR__AbiRc",
        "notes": (
            "The DefenseFinder rules table models AbiR as a three-component "
            "system requiring the AbiR__AbiRa, AbiR__AbiRb, and "
            "AbiR__AbiRc profiles."
        ),
    }


def abira_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ABIRA_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiR__AbiRa under the "
            "AbiR model namespace."
        ),
    }


def abirb_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ABIRB_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiR__AbiRb under the "
            "AbiR model namespace."
        ),
    }


def abirc_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ABIRC_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiR__AbiRc under the "
            "AbiR model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiR system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "multicomponent AbiR determinant represented by the DefenseFinder "
        "AbiR__AbiRa, AbiR__AbiRb, and AbiR__AbiRc profiles and capable "
        "of restricting lactococcal phage propagation by an early "
        "abortive-infection mechanism that impedes phage DNA replication, "
        "as exemplified by the two pKR223 loci from Lactococcus lactis "
        "subsp. lactis KR2 separated by the LlaKR2I "
        "restriction-modification genes."
    ),
    "definition_source": TWOMEY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiR",
            "synonym_type": "RELATED_SYNONYM",
            "source": TWOMEY,
        }
    ],
    "evidence": [
        {
            "reference": TWOMEY_PMID,
            "snippet": (
                "The native lactococcal plasmid pKR223 encodes two distinct "
                "phage resistance mechanisms, a restriction and modification "
                "(R/M) system designated LlaKR2I and an abortive infection "
                "mechanism (Abi) which affects prolate-headed-phage "
                "proliferation"
            ),
            "notes": (
                "Twomey et al. identify native Lactococcus lactis plasmid "
                "pKR223 as the source of a restriction-modification system "
                "and a separate abortive-infection determinant."
            ),
        },
        {
            "reference": TWOMEY_PMID,
            "snippet": (
                "sequence analysis has validated the novelty of the Abi "
                "system, which has now been designated AbiR"
            ),
            "notes": (
                "Twomey et al. name AbiR as the novel abortive-infection "
                "system from pKR223."
            ),
        },
        {
            "reference": TWOMEY_PMID,
            "snippet": (
                "Analysis of deletion and insertion clones demonstrated "
                "that AbiR was encoded by two genetic loci, separated by "
                "the LlaKR2I R/M genes"
            ),
            "notes": (
                "Twomey et al. show that the AbiR phenotype requires two "
                "pKR223 loci separated by the LlaKR2I "
                "restriction-modification genes."
            ),
        },
        {
            "reference": TWOMEY_PMID,
            "snippet": (
                "Mechanistic studies on the AbiR phenotype indicated that "
                "it was heat sensitive and that it impeded phage DNA "
                "replication"
            ),
            "notes": (
                "Twomey et al. connect AbiR activity to a heat-sensitive "
                "abortive-infection phenotype that impedes phage DNA "
                "replication."
            ),
        },
        {
            "reference": TWOMEY_PMID,
            "snippet": (
                "These data indicated that AbiR is a novel multicomponent, "
                "heat-sensitive, \"early\"-functioning Abi system"
            ),
            "notes": (
                "Twomey et al. classify AbiR as a multicomponent early "
                "abortive-infection system."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        abira_hmm_evidence(),
        abirb_hmm_evidence(),
        abirc_hmm_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Twomey et al. characterized AbiR from native plasmid "
                "pKR223 of Lactococcus lactis subsp. lactis KR2 and showed "
                "a multicomponent, two-locus Abi phenotype that impeded "
                "phage DNA replication."
            ),
            "reference": TWOMEY,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abir_loci_impede_phage_dna_replication",
            "title": "AbiR activity impedes lactococcal phage DNA replication",
            "description": (
                "Conservative system-level sketch linking the separated "
                "pKR223 AbiR loci to AbiR antiphage activity, impeded "
                "phage DNA replication, restricted lactococcal phage "
                "propagation, and abortive-infection system possession "
                "without resolving the phage trigger or individual "
                "component activities."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiR as a named DefenseFinder "
                "three-profile abortive-infection system whose pKR223 "
                "prototype is encoded by two genetic loci and impedes "
                "phage DNA replication. It leaves the direct phage trigger, "
                "the profile-to-locus mapping, AbiRa, AbiRb, and AbiRc "
                "molecular functions, the reason the R/M genes interrupt "
                "the two AbiR loci, and phage escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abir_loci",
                    "label": "AbiR loci",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A multicomponent abortive-infection determinant "
                        "encoded by two separated pKR223 loci and "
                        "represented by the DefenseFinder AbiR rule."
                    ),
                },
                {
                    "node_id": "abir_antiphage_activity",
                    "label": "AbiR antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection phage resistance mediated by "
                        "the AbiR system."
                    ),
                },
                {
                    "node_id": "phage_dna_replication",
                    "label": "phage DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication of lactococcal bacteriophage DNA "
                        "during sensitive-host infection."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of lactococcal phage "
                        "propagation in an AbiR-containing infected host "
                        "cell."
                    ),
                },
                {
                    "node_id": "abir_system_trait",
                    "label": "AbiR system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiR "
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
                    "subject": "abir_loci",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abir_antiphage_activity",
                    "description": (
                        "The pKR223 AbiR determinant is encoded by two "
                        "genetic loci separated by LlaKR2I genes, and "
                        "DefenseFinder models AbiR as a three-profile "
                        "system requiring AbiRa, AbiRb, and AbiRc "
                        "components."
                    ),
                    "evidence": [
                        {
                            "reference": TWOMEY_PMID,
                            "snippet": (
                                "Analysis of deletion and insertion clones "
                                "demonstrated that AbiR was encoded by two "
                                "genetic loci, separated by the LlaKR2I R/M "
                                "genes"
                            ),
                            "notes": (
                                "Twomey et al. show that the AbiR phenotype "
                                "requires two separated pKR223 genetic loci."
                            ),
                        },
                        rules_evidence(),
                        abira_hmm_evidence(),
                        abirb_hmm_evidence(),
                        abirc_hmm_evidence(),
                    ],
                },
                {
                    "subject": "abir_antiphage_activity",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_dna_replication",
                    "description": (
                        "AbiR antiphage activity impedes sensitive phage DNA "
                        "replication as an early abortive-infection output."
                    ),
                    "evidence": [
                        {
                            "reference": TWOMEY_PMID,
                            "snippet": (
                                "Mechanistic studies on the AbiR phenotype "
                                "indicated that it was heat sensitive and "
                                "that it impeded phage DNA replication"
                            ),
                            "notes": (
                                "Twomey et al. classify the AbiR phenotype "
                                "as heat-sensitive and DNA-replication "
                                "impeding."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abir_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "AbiR antiphage activity affects "
                        "prolate-headed-phage proliferation through a "
                        "multicomponent early Abi mechanism."
                    ),
                    "evidence": [
                        {
                            "reference": TWOMEY_PMID,
                            "snippet": (
                                "These data indicated that AbiR is a novel "
                                "multicomponent, heat-sensitive, "
                                "\"early\"-functioning Abi system"
                            ),
                            "notes": (
                                "Twomey et al. summarize the AbiR "
                                "phenotype as multicomponent, heat-sensitive, "
                                "and early functioning."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abir_system_trait",
                    "description": (
                        "Restriction of lactococcal phage propagation "
                        "realizes the AbiR abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": TWOMEY_PMID,
                            "snippet": (
                                "sequence analysis has validated the "
                                "novelty of the Abi system, which has now "
                                "been designated AbiR"
                            ),
                            "notes": (
                                "Twomey et al. name AbiR as the novel "
                                "pKR223 abortive-infection system."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abir_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiR system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": TWOMEY_PMID,
                            "snippet": (
                                "These data indicated that AbiR is a novel "
                                "multicomponent, heat-sensitive, "
                                "\"early\"-functioning Abi system"
                            ),
                            "notes": (
                                "Twomey et al. classify AbiR in the "
                                "abortive-infection class of phage defense."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abir-component-activity-gap",
            "prompt": (
                "Resolve the AbiR phage trigger, profile-to-locus mapping, "
                "and AbiRa, AbiRb, and AbiRc molecular functions before "
                "minting narrower AbiR mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Twomey et al. support AbiR as a multicomponent "
                "abortive-infection system encoded by two separated pKR223 "
                "loci, and DefenseFinder represents AbiR with a "
                "three-profile rule. This first system-level record leaves "
                "the phage trigger, the mapping from the two original "
                "genetic loci to AbiRa, AbiRb, and AbiRc profiles, the "
                "component molecular activities, and the direct reason that "
                "AbiR impedes phage DNA replication unresolved."
            ),
            "evidence": [
                {
                    "reference": TWOMEY_PMID,
                    "snippet": (
                        "Analysis of deletion and insertion clones "
                        "demonstrated that AbiR was encoded by two genetic "
                        "loci, separated by the LlaKR2I R/M genes"
                    ),
                    "notes": (
                        "Twomey et al. localize AbiR to two separated "
                        "pKR223 loci rather than to the three-component "
                        "DefenseFinder profile scheme."
                    ),
                }
            ],
            "attaches_to": ["causal_graphs#abir_loci_impede_phage_dna_replication"],
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
            "Minted AbiR system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
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
            "AbiR system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
