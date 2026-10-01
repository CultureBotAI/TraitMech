#!/usr/bin/env python3
"""Add the AbiF system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abif_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

GARVEY = "DOI:10.1128/AEM.61.12.4321-4328.1995"
FEMS_REVIEW = "DOI:10.1093/femsre/fuag009"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T01:32:44Z"
PARENT_TIMESTAMP = "2026-10-01T01:32:45Z"
IDENTIFIER = "traitmech:000504"
PROPOSAL = "proposals/metpo_traitmech_v381"

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, SpbK, "
    "CmdTAC, Abi2, AbiJ, AbiL, AbiN, AbiO, AbiP2, AbiA, and PD-T4-10 "
    "are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, traitmech:000304, traitmech:000306, "
    "traitmech:000316, traitmech:000317, traitmech:000318, "
    "traitmech:000319, traitmech:000320, traitmech:000321, "
    "traitmech:000322, traitmech:000323, traitmech:000324, "
    "traitmech:000325, traitmech:000335, traitmech:000338, "
    "traitmech:000339, traitmech:000340, traitmech:000341, "
    "traitmech:000342, traitmech:000343, traitmech:000344, and "
    "traitmech:000394, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., Depardieu et al., Prevots et al., "
    "O'Connor et al., Su et al., Twomey et al., McLandsborough et al., "
    "Parreira et al., Durmaz et al., Dai et al., Lossouarn et al., "
    "Cram et al., Parma et al., Johnson et al., Vassallo et al., "
    "Chopin et al., Anba et al., Deng et al., Prevots et al., Prevots "
    "and Ritzenthaler, Odegrip et al., Dinsmore and Klaenhammer, and "
    "Dinsmore et al. still support abortive infection as a genomically "
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
    "abortive infection, lambda Rex two-component phage exclusion, "
    "ICEBs1 SpbK abortive SP\u03b2 defense, CmdTAC mRNA "
    "ADP-ribosyltransferase abortive infection, DefenseFinder "
    "Abi2/PF07751 Abi-like loci, single-profile lactococcal AbiJ loci, "
    "two-component lactococcal AbiL ATPase/TOPRIM-family loci, "
    "single-gene lactococcal AbiN loci, single-profile lactococcal AbiO "
    "loci, single-profile coliphage AbiP2 reverse-transcriptase-like "
    "loci, lactococcal AbiA loci represented by DefenseFinder AbiA-large "
    "and AbiA-small subrules, DefenseFinder PD-T4-10 two-profile loci, "
    "and other families. Additional narrower TraitRecords need separate "
    "review to ground each subfamily's trigger, effector, growth-arrest "
    "or cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiF, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, "
    "AbiG, AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, "
    "SpbK, CmdTAC, Abi2, AbiJ, AbiL, AbiN, AbiO, AbiP2, AbiA, and "
    "PD-T4-10 are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000504, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, "
    "traitmech:000318, traitmech:000319, traitmech:000320, "
    "traitmech:000321, traitmech:000322, traitmech:000323, "
    "traitmech:000324, traitmech:000325, traitmech:000335, "
    "traitmech:000338, traitmech:000339, traitmech:000340, "
    "traitmech:000341, traitmech:000342, traitmech:000343, "
    "traitmech:000344, and traitmech:000394, respectively. Lopatina et "
    "al., Fineran et al., Dy et al., Garvey et al., Durmaz and "
    "Klaenhammer, Wang et al., Bouchard et al., Haaber et al., Owen et "
    "al., Depardieu et al., Prevots et al., O'Connor et al., Su et al., "
    "Twomey et al., McLandsborough et al., Parreira et al., Durmaz et "
    "al., Dai et al., Lossouarn et al., Cram et al., Parma et al., "
    "Johnson et al., Vassallo et al., Chopin et al., Anba et al., Deng "
    "et al., Prevots et al., Prevots and Ritzenthaler, Odegrip et al., "
    "Dinsmore and Klaenhammer, and Dinsmore et al. still support "
    "abortive infection as a genomically encoded phage defense strategy "
    "that spans mechanistically diverse toxin-antitoxin, pCG1-derived "
    "lactococcal AbiF DNA-replication-inhibition, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, "
    "two-separated-locus lactococcal AbiR DNA-replication impediment, "
    "pBF61-derived lactococcal AbiD burst-size reduction, lactococcal "
    "AbiB phage-transcript decay, lactococcal AbiC Prf infected-cell "
    "death, lactococcal AbiU phage-transcription delay, enterococcal "
    "AbiAlpha premature lysis, F-plasmid pif-region T7 abortive "
    "infection, lambda Rex two-component phage exclusion, ICEBs1 SpbK "
    "abortive SP\u03b2 defense, CmdTAC mRNA ADP-ribosyltransferase "
    "abortive infection, DefenseFinder Abi2/PF07751 Abi-like loci, "
    "single-profile lactococcal AbiJ loci, two-component lactococcal "
    "AbiL ATPase/TOPRIM-family loci, single-gene lactococcal AbiN loci, "
    "single-profile lactococcal AbiO loci, single-profile coliphage "
    "AbiP2 reverse-transcriptase-like loci, lactococcal AbiA loci "
    "represented by DefenseFinder AbiA-large and AbiA-small subrules, "
    "DefenseFinder PD-T4-10 two-profile loci, and other families. "
    "Additional narrower TraitRecords need separate review to ground "
    "each subfamily's trigger, effector, growth-arrest or cell-death "
    "mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiF as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000504 for "
    "the AbiF system; other abortive-infection families remain open."
)


def garvey_pcg1_fragment_evidence() -> dict[str, str]:
    return {
        "reference": GARVEY,
        "snippet": (
            "Subcloning and deletion analysis of the recombinant plasmid "
            "pCG1 defined a 3.7-kb EcoRV-XbaI fragment as encoding phage "
            "insensitivity"
        ),
        "notes": (
            "Garvey et al. localized the pNP40 AbiF determinant to the "
            "pCG1-derived EcoRV-XbaI fragment."
        ),
    }


def garvey_abif_orf_evidence() -> dict[str, str]:
    return {
        "reference": GARVEY,
        "snippet": (
            "The introduction of a frameshift mutation at the unique BglII "
            "site within this ORF disrupted the phage resistance phenotype, "
            "confirming that this ORF is responsible for the observed phage "
            "insensitivity"
        ),
        "notes": (
            "Garvey et al. showed that the single complete ORF in the "
            "pCG1-derived fragment is required for AbiF-associated phage "
            "resistance."
        ),
    }


def garvey_designation_evidence() -> dict[str, str]:
    return {
        "reference": GARVEY,
        "snippet": (
            "The mechanisms encoded by pPG01 and pCG1 in L. lactis subsp. "
            "lactis MG1614 conformed to the criteria defining abortive "
            "infection and were designated AbiE and AbiF, respectively"
        ),
        "notes": (
            "Garvey et al. designated the pCG1-encoded pNP40 "
            "phage-insensitivity determinant as AbiF."
        ),
    }


def garvey_dna_replication_evidence() -> dict[str, str]:
    return {
        "reference": GARVEY,
        "snippet": (
            "Analysis of the phage DNA content of phi 712-infected hosts "
            "containing AbiF demonstrated that it inhibited the rate of "
            "phage DNA replication"
        ),
        "notes": (
            "Garvey et al. measured reduced phage phi 712 DNA-replication "
            "rate in infected hosts carrying AbiF."
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
            "The FEMS review counts AbiF among the confirmed two-component "
            "lactococcal Abi-like systems."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiF system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "plasmid pCG1-derived abiF locus whose single complete open reading "
        "frame encodes a phage-insensitivity determinant that inhibits "
        "bacteriophage phi 712 DNA replication."
    ),
    "definition_source": GARVEY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        garvey_pcg1_fragment_evidence(),
        garvey_abif_orf_evidence(),
        garvey_designation_evidence(),
        garvey_dna_replication_evidence(),
        fems_two_component_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Garvey et al. cloned the pNP40 pCG1 AbiF determinant and "
                "showed that the pCG1-encoded region conferred "
                "abortive-infection phage insensitivity in Lactococcus "
                "lactis subsp. lactis MG1614."
            ),
            "reference": GARVEY,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abif_locus_inhibits_lactococcal_phage_dna_replication",
            "title": "AbiF inhibits lactococcal phage DNA replication",
            "description": (
                "Conservative system-level sketch linking a pCG1-derived "
                "abiF locus to inhibited phage phi 712 DNA replication, "
                "restricted phage propagation, and AbiF "
                "abortive-infection system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the original AbiF determinant as a "
                "pNP40 pCG1-derived abortive-infection locus that inhibits "
                "the rate of phage phi 712 DNA replication while leaving "
                "the exact AbiF protein function, phage trigger, host "
                "target, possible AbiD/AbiD1 homology-derived family "
                "boundary, natural locus breadth, and phage escape routes "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abif_locus",
                    "label": "abiF locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A pCG1-derived abortive-infection locus containing "
                        "the open reading frame required for AbiF phage "
                        "resistance."
                    ),
                },
                {
                    "node_id": "restricted_phage_dna_replication",
                    "label": "restricted phage DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage phi 712 DNA-replication rate "
                        "in an infected host carrying AbiF."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of phage propagation in an "
                        "AbiF-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abif_system_trait",
                    "label": "AbiF system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiF "
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
                    "subject": "abif_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_dna_replication",
                    "description": (
                        "The pCG1 AbiF open reading frame is responsible for "
                        "the phage-insensitivity phenotype and inhibits the "
                        "rate of phage phi 712 DNA replication."
                    ),
                    "evidence": [
                        garvey_abif_orf_evidence(),
                        garvey_dna_replication_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_dna_replication",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Inhibition of phage phi 712 DNA replication "
                        "contributes to AbiF phage insensitivity."
                    ),
                    "evidence": [
                        garvey_pcg1_fragment_evidence(),
                        garvey_dna_replication_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abif_system_trait",
                    "description": (
                        "Restricted phage propagation realizes the AbiF "
                        "abortive-infection system possession trait."
                    ),
                    "evidence": [
                        garvey_designation_evidence(),
                        fems_two_component_evidence(),
                    ],
                },
                {
                    "subject": "abif_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiF system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        garvey_designation_evidence(),
                        fems_two_component_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abif-function-and-host-breadth-gap",
            "prompt": (
                "Resolve the exact AbiF protein function, phage trigger, "
                "host target, AbiD/AbiD1 homology-derived family boundary, "
                "and natural locus breadth before minting narrower AbiF "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Garvey et al. support AbiF as a pCG1-encoded pNP40 "
                "determinant that conforms to abortive-infection criteria, "
                "depends on a single complete open reading frame, and "
                "inhibits the rate of phage phi 712 DNA replication; the "
                "FEMS review retains AbiF among confirmed two-component "
                "lactococcal Abi-like systems. This first system-level "
                "record therefore leaves the direct phage trigger, exact "
                "AbiF molecular activity, relevant host target, "
                "AbiD/AbiD1-related family boundary, natural locus breadth, "
                "cell-death or growth-arrest route, and phage escape routes "
                "unresolved."
            ),
            "evidence": [
                garvey_abif_orf_evidence(),
                garvey_dna_replication_evidence(),
                fems_two_component_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#abif_locus_inhibits_lactococcal_phage_dna_replication"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
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

    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    assert discussion["status"] == "OPEN"
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
            "Minted AbiF system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiF system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
