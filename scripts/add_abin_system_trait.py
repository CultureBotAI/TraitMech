"""Add the AbiN system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abin_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

PREVOTS_ABIN = "DOI:10.1111/j.1574-6968.1998.tb12879.x"
FEMS_REVIEW = "DOI:10.1093/femsre/fuag009"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T17:52:22Z"
PARENT_TIMESTAMP = "2026-09-21T17:52:23Z"
IDENTIFIER = "traitmech:000341"
PROPOSAL = "proposals/metpo_traitmech_v218"

HMM_ROW = (
    "| AbiN__AbiN                                       | "
    "AbiN__AbiN                                       | AbiN                   | "
    "Custom                  | 20     |"
)
RULES_ROW = "AbiN\tAbiN\t1\t1\tAbiN__AbiN\t\t\t"

OLD_PARENT_RATIONALE = (
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
    "SpbK abortive SPβ defense, CmdTAC mRNA ADP-ribosyltransferase "
    "abortive infection, DefenseFinder Abi2/PF07751 Abi-like loci, "
    "single-profile lactococcal AbiJ loci, two-component lactococcal AbiL "
    "ATPase/TOPRIM-family loci, and other families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape "
    "routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, SpbK, "
    "CmdTAC, Abi2, AbiJ, AbiL, and AbiN are split out as "
    "traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, traitmech:000301, traitmech:000303, "
    "traitmech:000304, traitmech:000306, traitmech:000316, "
    "traitmech:000317, traitmech:000318, traitmech:000319, "
    "traitmech:000320, traitmech:000321, traitmech:000322, "
    "traitmech:000323, traitmech:000324, traitmech:000325, "
    "traitmech:000335, traitmech:000338, traitmech:000339, "
    "traitmech:000340, and traitmech:000341, respectively. Lopatina et "
    "al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang et al., "
    "Bouchard et al., Haaber et al., Owen et al., Depardieu et al., "
    "Prevots et al., O'Connor et al., Su et al., Twomey et al., "
    "McLandsborough et al., Parreira et al., Durmaz et al., Dai et al., "
    "Lossouarn et al., Cram et al., Parma et al., Johnson et al., "
    "Vassallo et al., Chopin et al., Anba et al., Deng et al., and "
    "Prevots et al. still support abortive infection as a genomically "
    "encoded phage defense strategy that spans mechanistically diverse "
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
    "SpbK abortive SPβ defense, CmdTAC mRNA ADP-ribosyltransferase "
    "abortive infection, DefenseFinder Abi2/PF07751 Abi-like loci, "
    "single-profile lactococcal AbiJ loci, two-component lactococcal AbiL "
    "ATPase/TOPRIM-family loci, single-gene lactococcal AbiN loci, and "
    "other families. Additional narrower TraitRecords need separate review "
    "to ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiN as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000341 for "
    "the AbiN system; other abortive-infection families remain open."
)


def prevots_abin_identity_evidence() -> dict[str, str]:
    return {
        "reference": PREVOTS_ABIN,
        "snippet": (
            "Nucleotide sequence and analysis of the new chromosomal abortive "
            "infection gene abiN of Lactococcus lactis subsp. cremoris S114"
        ),
        "notes": (
            "Crossref metadata verifies the Prevots et al. 1998 AbiN primary "
            "paper title and DOI."
        ),
    }


def fems_single_gene_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "the majority (18 systems) are each represented by single "
            "protein-coding genes"
        ),
        "notes": (
            "The FEMS review lists AbiN among the 34 confirmed lactococcal "
            "Abi-like systems in Table 1 and omits AbiN from the named two- "
            "and three-component exception lists."
        ),
    }


def fems_sensor_prediction_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "The structure of AbiN is predicted with high confidence by "
            "AlphaFold and resembles a putative periplasmic ligand-binding "
            "sensor domain protein"
        ),
        "notes": (
            "The FEMS review summarizes a predicted AbiN sensor-like fold but "
            "does not establish a molecular trigger or effector activity."
        ),
    }


def fems_mechanism_gap_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "further research is needed to clarify the mechanism of AbiN "
            "and if it functions via abortive infection"
        ),
        "notes": (
            "The FEMS review explicitly leaves the AbiN mechanism unresolved, "
            "so this record does not mint a more specific sensor or effector "
            "trait."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiN | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiN model "
            "namespace to the Chopin et al. lactococcal "
            "abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_ROW,
        "notes": (
            "The DefenseFinder rules table models AbiN as a one-component "
            "system requiring the AbiN__AbiN profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiN__AbiN under the "
            "AbiN model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiN system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "single-component AbiN-family locus represented by DefenseFinder as "
        "a mandatory AbiN__AbiN profile."
    ),
    "definition_source": PREVOTS_ABIN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiN",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "AbiN__AbiN",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        prevots_abin_identity_evidence(),
        fems_single_gene_evidence(),
        fems_sensor_prediction_evidence(),
        fems_mechanism_gap_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "abin_locus_restricts_lactococcal_phage",
            "title": "AbiN loci confer abortive-infection phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "DefenseFinder AbiN locus to restricted bacteriophage "
                "propagation without asserting the unresolved phage trigger, "
                "predicted ligand-binding sensor role, or molecular "
                "effector activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiN as a named single-profile "
                "lactococcal Abi-like system with the DefenseFinder "
                "AbiN__AbiN HMM while leaving its direct phage trigger, "
                "ligand-sensor interpretation, exact molecular activity, "
                "phage-cycle step, phage escape routes, and growth-arrest or "
                "cell-death route unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abin_locus",
                    "label": "AbiN locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AbiN-family abortive-infection locus represented "
                        "by the DefenseFinder AbiN__AbiN profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage propagation in cells carrying "
                        "an AbiN-family abortive-infection system."
                    ),
                },
                {
                    "node_id": "abin_system_trait",
                    "label": "AbiN system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiN "
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
                    "subject": "abin_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The DefenseFinder AbiN namespace is modeled as a "
                        "one-profile AbiN__AbiN system."
                    ),
                    "evidence": [rules_evidence(), hmm_inventory_evidence()],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abin_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the AbiN "
                        "abortive-infection system possession trait."
                    ),
                    "evidence": [
                        prevots_abin_identity_evidence(),
                        fems_single_gene_evidence(),
                    ],
                },
                {
                    "subject": "abin_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiN system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        prevots_abin_identity_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abin-trigger-and-effector-gap",
            "prompt": (
                "Resolve the AbiN phage trigger, molecular activity, "
                "predicted ligand-binding sensor interpretation, and "
                "growth-arrest or cell-death route before minting narrower "
                "AbiN mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Prevots et al. support AbiN as a chromosomal "
                "lactococcal abortive infection gene, the FEMS review "
                "retains AbiN among confirmed lactococcal Abi-like systems, "
                "and DefenseFinder represents AbiN with a mandatory "
                "AbiN__AbiN profile. The FEMS table leaves the affected "
                "phage lytic-cycle step, phage escape mutants, and "
                "mechanism of cell arrest or death unknown, and the FEMS "
                "structural discussion predicts a putative ligand-binding "
                "sensor fold while explicitly calling for further research "
                "on the AbiN mechanism. This first system-level record "
                "therefore leaves the direct phage trigger, sensor ligand, "
                "exact molecular activity, growth-arrest or cell-death "
                "route, and phage escape routes unresolved."
            ),
            "evidence": [
                fems_sensor_prediction_evidence(),
                fems_mechanism_gap_evidence(),
                rules_evidence(),
                hmm_inventory_evidence(),
            ],
            "attaches_to": ["causal_graphs#abin_locus_restricts_lactococcal_phage"],
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
            "Minted AbiN system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiN system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
