"""Add the AbiJ system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abij_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DENG = "DOI:10.1111/j.1574-6968.1997.tb10185.x"
FEMS_REVIEW = "DOI:10.1093/femsre/fuag009"
MOSTERD = "DOI:10.1073/pnas.2426508122"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T16:24:09Z"
PARENT_TIMESTAMP = "2026-09-21T16:24:10Z"
IDENTIFIER = "traitmech:000339"
PROPOSAL = "proposals/metpo_traitmech_v216"

HMM_ROW = (
    "| AbiJ__AbiJ                                       | "
    "AbiJ__AbiJ                                       | AbiJ                   | "
    "Custom                  | 20     |"
)
RULES_ROW = "AbiJ\tAbiJ\t1\t1\tAbiJ__AbiJ\t\t\t"

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, SpbK, "
    "CmdTAC, and Abi2 are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, "
    "traitmech:000318, traitmech:000319, traitmech:000320, "
    "traitmech:000321, traitmech:000322, traitmech:000323, "
    "traitmech:000324, traitmech:000325, traitmech:000335, and "
    "traitmech:000338, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., Depardieu et al., Prevots et al., "
    "O'Connor et al., Su et al., Twomey et al., McLandsborough et al., "
    "Parreira et al., Durmaz et al., Dai et al., Lossouarn et al., "
    "Cram et al., Parma et al., Johnson et al., Vassallo et al., "
    "Chopin et al., and Anba et al. still support abortive infection as a "
    "genomically encoded phage defense strategy that spans mechanistically "
    "diverse toxin-antitoxin, premature-lysis, RT-related polymerase, "
    "two-component, translation-inhibition, prophage-encoded "
    "DNA-replication-inhibition, staphylococcal-kinase-triggered cell death, "
    "lactococcal AbiH phage resistance, two-gene lactococcal AbiG "
    "RNA-synthesis interference, single-ORF lactococcal AbiI burst-size "
    "reduction, two-separated-locus lactococcal AbiR DNA-replication "
    "impediment, pBF61-derived lactococcal AbiD burst-size reduction, "
    "lactococcal AbiB phage-transcript decay, lactococcal AbiC Prf "
    "infected-cell death, lactococcal AbiU phage-transcription delay, "
    "enterococcal AbiAlpha premature lysis, F-plasmid pif-region T7 "
    "abortive infection, lambda Rex two-component phage exclusion, ICEBs1 "
    "SpbK abortive SP\u03b2 defense, CmdTAC mRNA ADP-ribosyltransferase "
    "abortive infection, DefenseFinder Abi2/PF07751 Abi-like loci, and "
    "other families. Additional narrower TraitRecords need separate review "
    "to ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
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
PARENT_CHANGES = (
    "Documented AbiJ as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000339 for "
    "the AbiJ system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiJ | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiJ model "
            "namespace to the Chopin et al. lactococcal "
            "abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_ROW,
        "notes": (
            "The DefenseFinder rules table models AbiJ as a one-component "
            "system requiring the AbiJ__AbiJ profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiJ__AbiJ under the AbiJ model namespace."
        ),
    }


def fems_abij_identity_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": "AbiJ (Also abi-859)",
        "notes": (
            "The 2026 FEMS review lists AbiJ, also named abi-859, among "
            "the experimentally confirmed lactococcal Abi-like systems."
        ),
    }


def mosterd_escape_evidence() -> dict[str, str]:
    return {
        "reference": MOSTERD,
        "snippet": (
            "we isolated 66 phage escape mutants which had become "
            "insensitive to 13 distinct, plasmid-encoded lactococcal "
            "phage resistance systems (i.e. Rhea, Kamadhenu, Rugutis, "
            "Audmula, PARIS, type II CBASS, Septu, AbiA, AbiB, AbiD/F, "
            "AbiG, AbiJ, AbiP)"
        ),
        "notes": (
            "Mosterd et al. include AbiJ in a set of distinct plasmid-encoded "
            "lactococcal phage-resistance systems used for escape-mutant "
            "isolation."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiJ system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "AbiJ-family locus represented by the DefenseFinder AbiJ model "
        "namespace and mandatory AbiJ__AbiJ profile."
    ),
    "definition_source": DENG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiJ",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "AbiJ__AbiJ",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "abi-859",
            "synonym_type": "RELATED_SYNONYM",
            "source": FEMS_REVIEW,
        },
    ],
    "evidence": [
        {
            "reference": DENG,
            "snippet": (
                "A novel plasmid-encoded phage abortive infection system "
                "from Lactococcus lactis biovar. diacetylactis"
            ),
            "notes": (
                "Europe PMC metadata verifies the Deng et al. 1997 AbiJ "
                "primary paper title and PMID:8997719; the DOI landing "
                "page was Cloudflare-blocked and Europe PMC exposed no "
                "abstract or full text, so this record cites Deng et al. "
                "for the primary AbiJ identity and uses later accessible "
                "sources for snippet-backed system details."
            ),
        },
        {
            "reference": FEMS_REVIEW,
            "snippet": (
                "Experimentally confirmed lactococcal Abi-like systems, "
                "as well as information on their antiphage activity range"
            ),
            "notes": (
                "The FEMS review frames Table 1 as a curated set of "
                "experimentally confirmed lactococcal Abi-like systems."
            ),
        },
        fems_abij_identity_evidence(),
        mosterd_escape_evidence(),
        {
            "reference": FEMS_REVIEW,
            "snippet": (
                "AbiA escape mutants also circumvent AbiJ, which was not "
                "observed for other combinations"
            ),
            "notes": (
                "The FEMS review summarizes Mosterd et al.'s escape-mutant "
                "evidence linking AbiA escape mutations to AbiJ bypass while "
                "not yet identifying AbiJ's direct molecular trigger."
            ),
        },
        {
            "reference": FEMS_REVIEW,
            "snippet": (
                "Although no particular mechanistic information is currently available for AbiJ"
            ),
            "notes": (
                "The FEMS review explicitly keeps AbiJ mechanism unresolved; "
                "this record therefore avoids protein-level chemistry and "
                "TA-system mechanism claims."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "abij_locus_restricts_lactococcal_phage",
            "title": "AbiJ loci confer abortive-infection phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "DefenseFinder AbiJ locus to restricted bacteriophage "
                "propagation without asserting the unresolved phage trigger, "
                "molecular activity, or arrest route."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiJ as a named single-profile "
                "lactococcal abortive-infection system with a DefenseFinder "
                "AbiJ__AbiJ HMM profile while leaving its direct phage "
                "trigger, AbiJ molecular function, exact relationship to "
                "AbiA escape routes, natural locus breadth, and cell-arrest "
                "or death route unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abij_locus",
                    "label": "AbiJ locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AbiJ-family abortive-infection locus represented "
                        "by the DefenseFinder AbiJ__AbiJ profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage propagation in cells carrying "
                        "an AbiJ-family abortive-infection system."
                    ),
                },
                {
                    "node_id": "abij_system_trait",
                    "label": "AbiJ system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiJ "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abij_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The DefenseFinder AbiJ namespace is modeled as a "
                        "one-profile AbiJ__AbiJ system, and AbiJ is a "
                        "plasmid-encoded lactococcal phage-resistance system."
                    ),
                    "evidence": [
                        rules_evidence(),
                        hmm_inventory_evidence(),
                        mosterd_escape_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abij_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the AbiJ "
                        "abortive-infection system possession trait."
                    ),
                    "evidence": [
                        fems_abij_identity_evidence(),
                        mosterd_escape_evidence(),
                    ],
                },
                {
                    "subject": "abij_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiJ system possession is an abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": FEMS_REVIEW,
                            "snippet": (
                                "A recent large-scale study of lactococcal "
                                "plasmids revealed 11 novel Abi-like systems"
                            ),
                            "notes": (
                                "The FEMS review places AbiJ within the set "
                                "of lactococcal Abi-like systems."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abij-trigger-and-effector-gap",
            "prompt": (
                "Resolve the AbiJ phage trigger, molecular activity, and "
                "exact AbiA escape-mutant overlap before minting narrower "
                "AbiJ mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Deng et al. support AbiJ as a lactococcal plasmid-encoded "
                "abortive-infection system, and DefenseFinder represents "
                "AbiJ with a one-profile rule. Mosterd et al. show that "
                "AbiJ escape behavior overlaps with AbiA escape mutants, "
                "but the FEMS review notes that AbiJ still lacks a resolved "
                "mechanism. This first system-level record therefore leaves "
                "AbiJ's direct phage trigger, molecular effector activity, "
                "natural locus breadth, exact HEPN-domain interpretation, "
                "growth-arrest or cell-death route, and phage escape routes "
                "unresolved."
            ),
            "evidence": [
                {
                    "reference": FEMS_REVIEW,
                    "snippet": (
                        "While AbiB and AbiJ show only weak predictions "
                        "(HHpred hits for HEPN domain containing-proteins "
                        "with E-values > 0.1) or lack identifiable "
                        "functional domains based on InterPro and HHpred"
                    ),
                    "notes": (
                        "The FEMS review notes that AbiJ HEPN-domain "
                        "evidence remains weak in sequence/domain-prediction "
                        "analyses."
                    ),
                },
                {
                    "reference": FEMS_REVIEW,
                    "snippet": (
                        "Although no particular mechanistic information is "
                        "currently available for AbiJ"
                    ),
                    "notes": ("The FEMS review leaves AbiJ's mechanism unresolved."),
                },
            ],
            "attaches_to": ["causal_graphs#abij_locus_restricts_lactococcal_phage"],
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
            "Minted AbiJ system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiJ system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
