"""Add the AbiL system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abil_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DENG = "DOI:10.1016/S0168-1656(98)00175-8"
FEMS_REVIEW = "DOI:10.1093/femsre/fuag009"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T17:17:22Z"
PARENT_TIMESTAMP = "2026-09-21T17:17:23Z"
IDENTIFIER = "traitmech:000340"
PROPOSAL = "proposals/metpo_traitmech_v217"

HMM_ROW_ABILI = (
    "| AbiL__AbiLi                                      | "
    "AbiL__AbiLi                                      | AbiL                   | "
    "Custom                  | 20     |"
)
HMM_ROW_ABILI2 = (
    "| AbiL__AbiLi2                                     | "
    "AbiL__AbiLi2                                     | AbiL                   | "
    "Custom                  | 20     |"
)
HMM_ROW_ABILII = (
    "| AbiL__AbiLii                                     | "
    "AbiL__AbiLii                                     | AbiL                   | "
    "Custom                  | 20     |"
)
HMM_ROW_ABILII2 = (
    "| AbiL__AbiLii2                                    | "
    "AbiL__AbiLii2                                    | AbiL                   | "
    "Custom                  | 20     |"
)
RULES_ROW = "AbiL\tAbiL\t2\t2\tAbiL__AbiLi, AbiL__AbiLii\t\t\t"

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, SpbK, "
    "CmdTAC, Abi2, and AbiJ are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, "
    "traitmech:000318, traitmech:000319, traitmech:000320, "
    "traitmech:000321, traitmech:000322, traitmech:000323, "
    "traitmech:000324, traitmech:000325, traitmech:000335, "
    "traitmech:000338, and traitmech:000339, respectively. Lopatina et "
    "al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang et al., "
    "Bouchard et al., Haaber et al., Owen et al., Depardieu et al., "
    "Prevots et al., O'Connor et al., Su et al., Twomey et al., "
    "McLandsborough et al., Parreira et al., Durmaz et al., Dai et al., "
    "Lossouarn et al., Cram et al., Parma et al., Johnson et al., "
    "Vassallo et al., Chopin et al., Anba et al., and Deng et al. still "
    "support abortive infection as a genomically encoded phage defense "
    "strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, "
    "two-separated-locus lactococcal AbiR DNA-replication impediment, "
    "pBF61-derived lactococcal AbiD burst-size reduction, lactococcal AbiB "
    "phage-transcript decay, lactococcal AbiC Prf infected-cell death, "
    "lactococcal AbiU phage-transcription delay, enterococcal AbiAlpha "
    "premature lysis, F-plasmid pif-region T7 abortive infection, lambda "
    "Rex two-component phage exclusion, ICEBs1 SpbK abortive SP\u03b2 "
    "defense, CmdTAC mRNA ADP-ribosyltransferase abortive infection, "
    "DefenseFinder Abi2/PF07751 Abi-like loci, single-profile lactococcal "
    "AbiJ loci, and other families. Additional narrower TraitRecords need "
    "separate review to ground each subfamily's trigger, effector, "
    "growth-arrest or cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, SpbK, "
    "CmdTAC, Abi2, AbiJ, and AbiL are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, "
    "traitmech:000318, traitmech:000319, traitmech:000320, "
    "traitmech:000321, traitmech:000322, traitmech:000323, "
    "traitmech:000324, traitmech:000325, traitmech:000335, "
    "traitmech:000338, traitmech:000339, and traitmech:000340, "
    "respectively. Lopatina et al., Fineran et al., Dy et al., Durmaz and "
    "Klaenhammer, Wang et al., Bouchard et al., Haaber et al., Owen et "
    "al., Depardieu et al., Prevots et al., O'Connor et al., Su et al., "
    "Twomey et al., McLandsborough et al., Parreira et al., Durmaz et al., "
    "Dai et al., Lossouarn et al., Cram et al., Parma et al., Johnson et "
    "al., Vassallo et al., Chopin et al., Anba et al., and Deng et al. "
    "still support abortive infection as a genomically encoded phage "
    "defense strategy that spans mechanistically diverse "
    "toxin-antitoxin, premature-lysis, RT-related polymerase, "
    "two-component, translation-inhibition, prophage-encoded "
    "DNA-replication-inhibition, staphylococcal-kinase-triggered cell "
    "death, lactococcal AbiH phage resistance, two-gene lactococcal AbiG "
    "RNA-synthesis interference, single-ORF lactococcal AbiI burst-size "
    "reduction, two-separated-locus lactococcal AbiR DNA-replication "
    "impediment, pBF61-derived lactococcal AbiD burst-size reduction, "
    "lactococcal AbiB phage-transcript decay, lactococcal AbiC Prf "
    "infected-cell death, lactococcal AbiU phage-transcription delay, "
    "enterococcal AbiAlpha premature lysis, F-plasmid pif-region T7 "
    "abortive infection, lambda Rex two-component phage exclusion, ICEBs1 "
    "SpbK abortive SP\u03b2 defense, CmdTAC mRNA ADP-ribosyltransferase "
    "abortive infection, DefenseFinder Abi2/PF07751 Abi-like loci, "
    "single-profile lactococcal AbiJ loci, two-component lactococcal AbiL "
    "ATPase/TOPRIM-family loci, and other families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape "
    "routes."
)
PARENT_CHANGES = (
    "Documented AbiL as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000340 for "
    "the AbiL system; other abortive-infection families remain open."
)


def deng_identity_evidence() -> dict[str, str]:
    return {
        "reference": DENG,
        "snippet": (
            "Genetic organization and functional analysis of a novel phage "
            "abortive infection system, AbiL, from Lactococcus lactis"
        ),
        "notes": (
            "Crossref metadata verifies the Deng et al. 1999 AbiL primary "
            "paper title and DOI."
        ),
    }


def fems_two_component_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "13 are two-component systems (AbiD, AbiD1, AbiD-like, AbiE, "
            "AbiF, AbiG, AbiL, AbiQ, AbiT, AbiV, PARIS, type I CBASS, Septu"
        ),
        "notes": (
            "The FEMS review counts AbiL among the confirmed two-component "
            "lactococcal Abi-like systems."
        ),
    }


def fems_toprim_prediction_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "AbiL has been included among systems such as PARIS, which "
            "feature an ABC ATPase and a TOPRIM nuclease"
        ),
        "notes": (
            "The FEMS review places AbiL among predicted ATPase-plus-TOPRIM "
            "systems but does not resolve the AbiLi and AbiLii molecular "
            "activities."
        ),
    }


def fems_second_component_gap_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "No significant sequence similarity was found between the "
            "second components of AbiL and PARIS"
        ),
        "notes": (
            "The AbiL-to-PARIS comparison remains indirect for the second "
            "component, so this record does not copy the PARIS mechanism "
            "onto AbiL."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiL | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiL model "
            "namespace to the Chopin et al. lactococcal "
            "abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_ROW,
        "notes": (
            "The DefenseFinder rules table models AbiL as a two-component "
            "system requiring the AbiL__AbiLi and AbiL__AbiLii profiles."
        ),
    }


def hmm_abili_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_ABILI,
        "notes": (
            "The DefenseFinder HMM inventory records AbiL__AbiLi under the "
            "AbiL model namespace."
        ),
    }


def hmm_abili2_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_ABILI2,
        "notes": (
            "The DefenseFinder HMM inventory also records AbiL__AbiLi2 under "
            "the AbiL model namespace, but this profile is not listed in "
            "the two mandatory profiles in the pinned AbiL rule."
        ),
    }


def hmm_abilii_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_ABILII,
        "notes": (
            "The DefenseFinder HMM inventory records AbiL__AbiLii under the "
            "AbiL model namespace."
        ),
    }


def hmm_abilii2_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW_ABILII2,
        "notes": (
            "The DefenseFinder HMM inventory also records AbiL__AbiLii2 under "
            "the AbiL model namespace, but this profile is not listed in "
            "the two mandatory profiles in the pinned AbiL rule."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiL system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "two-component AbiL-family locus represented by DefenseFinder as "
        "mandatory AbiL__AbiLi and AbiL__AbiLii profiles."
    ),
    "definition_source": DENG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiL",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "AbiL__AbiLi",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "AbiL__AbiLii",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        deng_identity_evidence(),
        fems_two_component_evidence(),
        fems_toprim_prediction_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_abili_evidence(),
        hmm_abilii_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "abil_locus_restricts_lactococcal_phage",
            "title": "AbiL loci confer abortive-infection phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "DefenseFinder AbiL locus to restricted bacteriophage "
                "propagation without asserting the unresolved phage trigger, "
                "AbiLi or AbiLii molecular activity, or AbiL-to-PARIS "
                "mechanistic correspondence."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiL as a named lactococcal "
                "abortive-infection system with DefenseFinder AbiL__AbiLi "
                "and AbiL__AbiLii HMM profiles while leaving its direct "
                "phage trigger, the exact AbiLi and AbiLii activities, the "
                "relationship between the mandatory and suffixed HMM rows, "
                "and the similarity of its route to PARIS unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abil_locus",
                    "label": "AbiL locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AbiL-family abortive-infection locus represented "
                        "by the DefenseFinder AbiL__AbiLi and AbiL__AbiLii "
                        "profiles."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage propagation in cells carrying "
                        "an AbiL-family abortive-infection system."
                    ),
                },
                {
                    "node_id": "abil_system_trait",
                    "label": "AbiL system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiL "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abil_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The DefenseFinder AbiL namespace is modeled as a "
                        "two-profile AbiL__AbiLi plus AbiL__AbiLii system, "
                        "and AbiL is a confirmed lactococcal Abi-like "
                        "system."
                    ),
                    "evidence": [
                        rules_evidence(),
                        hmm_abili_evidence(),
                        hmm_abilii_evidence(),
                        fems_two_component_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abil_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the AbiL "
                        "abortive-infection system possession trait."
                    ),
                    "evidence": [
                        deng_identity_evidence(),
                        fems_two_component_evidence(),
                    ],
                },
                {
                    "subject": "abil_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiL system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        deng_identity_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abil-trigger-and-effector-gap",
            "prompt": (
                "Resolve the AbiL phage trigger, AbiLi and AbiLii "
                "activities, AbiLi2 and AbiLii2 HMM row relationships, and "
                "ATPase-plus-TOPRIM mechanism before minting narrower AbiL "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Deng et al. support AbiL as a lactococcal phage abortive "
                "infection system, the FEMS review lists AbiL among "
                "confirmed two-component lactococcal Abi-like systems, and "
                "DefenseFinder represents AbiL with mandatory AbiL__AbiLi "
                "and AbiL__AbiLii profiles. The same pinned HMM inventory "
                "also contains AbiL__AbiLi2 and AbiL__AbiLii2 rows that are "
                "not in the pinned two-profile rule, and the FEMS review "
                "summarizes unresolved ATPase and TOPRIM predictions. This "
                "first system-level record therefore leaves the direct phage "
                "trigger, exact AbiLi and AbiLii molecular activities, "
                "accessory-model interpretation, AbiL-to-PARIS similarity, "
                "growth-arrest or cell-death route, and phage escape routes "
                "unresolved."
            ),
            "evidence": [
                hmm_abili2_evidence(),
                hmm_abilii2_evidence(),
                fems_toprim_prediction_evidence(),
                fems_second_component_gap_evidence(),
            ],
            "attaches_to": ["causal_graphs#abil_locus_restricts_lactococcal_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
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

    discussion = next(
        item
        for item in record.get("discussions") or []
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
            "Minted AbiL system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiL system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
