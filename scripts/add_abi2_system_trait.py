"""Add the Abi2 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abi2_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

CHOPIN = "DOI:10.1016/j.mib.2005.06.006"
ANBA = "DOI:10.1128/jb.177.13.3818-3823.1995"
BIDNENKO = "DOI:10.1128/jb.177.13.3824-3829.1995"
INTERPRO_PF07751 = "https://www.ebi.ac.uk/interpro/entry/pfam/PF07751/"
UNIPROT_Q48717 = (
    "https://rest.uniprot.org/uniprotkb/Q48717.tsv?"
    "fields=accession,id,gene_names,protein_name,xref_pfam,organism_name"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T14:52:53Z"
PARENT_TIMESTAMP = "2026-09-21T14:52:54Z"
IDENTIFIER = "traitmech:000338"
PROPOSAL = "proposals/metpo_traitmech_v215"

HMM_ROW = (
    "| Abi2__Abi_2                                      | "
    "Abi2__Abi_2                                      | Abi2                   | "
    "PF07751.12              | 60     |"
)
RULES_ROW = "Abi2\tAbi2\t1\t1\tAbi2__Abi_2\t\t\t"

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, SpbK, and "
    "CmdTAC are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, traitmech:000304, traitmech:000306, "
    "traitmech:000316, traitmech:000317, traitmech:000318, "
    "traitmech:000319, traitmech:000320, traitmech:000321, "
    "traitmech:000322, traitmech:000323, traitmech:000324, "
    "traitmech:000325, and traitmech:000335, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, "
    "Wang et al., Bouchard et al., Haaber et al., Owen et al., "
    "Depardieu et al., Prevots et al., O'Connor et al., Su et al., "
    "Twomey et al., McLandsborough et al., Parreira et al., Durmaz "
    "et al., Dai et al., Lossouarn et al., Cram et al., Parma et al., "
    "Johnson et al., and Vassallo et al. still support abortive infection "
    "as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, staphylococcal-kinase-triggered "
    "cell death, lactococcal AbiH phage resistance, two-gene lactococcal AbiG "
    "RNA-synthesis interference, single-ORF lactococcal AbiI burst-size "
    "reduction, two-separated-locus lactococcal AbiR DNA-replication "
    "impediment, pBF61-derived lactococcal AbiD burst-size reduction, "
    "lactococcal AbiB phage-transcript decay, lactococcal AbiC Prf infected-cell "
    "death, lactococcal AbiU phage-transcription delay, enterococcal AbiAlpha "
    "premature lysis, F-plasmid pif-region T7 abortive infection, lambda Rex "
    "two-component phage exclusion, ICEBs1 SpbK abortive SP\u03b2 defense, "
    "CmdTAC mRNA ADP-ribosyltransferase abortive infection, and other "
    "families. Additional narrower TraitRecords need separate review to ground "
    "each subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
NEW_PARENT_RATIONALE = (
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
PARENT_CHANGES = (
    "Documented Abi2 as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000338 for "
    "the Abi2 system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Abi2 | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | "
            "Phage abortive infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Abi2 model "
            "namespace to the Chopin et al. lactococcal "
            "abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_ROW,
        "notes": (
            "The DefenseFinder rules table models Abi2 as a "
            "one-component system requiring the Abi2__Abi_2 profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records Abi2__Abi_2 under "
            "the Abi2 model namespace, backed by the Pfam PF07751.12 "
            "Abi_2 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Abi2 system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "single-component Abi-like locus represented by the DefenseFinder "
        "Abi2 model namespace and mandatory Abi2__Abi_2/PF07751 profile."
    ),
    "definition_source": CHOPIN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "Abi2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Abi2__Abi_2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Abi_2",
            "synonym_type": "RELATED_SYNONYM",
            "source": INTERPRO_PF07751,
        },
    ],
    "evidence": [
        {
            "reference": CHOPIN,
            "snippet": (
                "Abortive infection (Abi) systems, also called phage exclusion, "
                "block phage multiplication and cause premature bacterial cell "
                "death upon phage infection."
            ),
            "notes": (
                "Chopin et al. define the abortive-infection class of phage "
                "exclusion systems used by the DefenseFinder Abi2 registry row."
            ),
        },
        {
            "reference": ANBA,
            "snippet": (
                "Lactococcal phage abortive infection (AbiD1) determined by "
                "plasmid pIL105 is active on both prolate- and "
                "small-isometric-head phages"
            ),
            "notes": (
                "Anba et al. characterize AbiD1 as a plasmid-encoded "
                "lactococcal abortive-infection determinant active on "
                "multiple phage morphotypes."
            ),
        },
        {
            "reference": ANBA,
            "snippet": (
                "The Abi phenotype was found to be encoded by a single gene, "
                "designated abiD1."
            ),
            "notes": (
                "Anba et al. support a single-gene AbiD1 locus used as "
                "family-level background for Abi-like abortive-infection "
                "systems."
            ),
        },
        {
            "reference": BIDNENKO,
            "snippet": (
                "Phage bIL66 is unable to grow on Lactococcus lactis cells "
                "harboring the abortive infection gene abiD1."
            ),
            "notes": (
                "Bidnenko et al. connect abiD1 carriage to restriction of "
                "bIL66 phage growth in Lactococcus lactis."
            ),
        },
        {
            "reference": INTERPRO_PF07751,
            "snippet": (
                "This family, found in various bacterial species, contains "
                "sequences that are similar to the Abi group of proteins"
            ),
            "notes": (
                "EBI InterPro resolves PF07751 as the reviewed Pfam "
                "Abi-like protein family with short name Abi_2."
            ),
        },
        {
            "reference": UNIPROT_Q48717,
            "snippet": (
                "Q48717\tQ48717_9LACT\tabiD1\tAbiD1\tPF07751;"
                "\tLactococcus lactis"
            ),
            "notes": (
                "UniProt maps the Lactococcus lactis abiD1/AbiD1 entry "
                "to Pfam PF07751, bridging primary AbiD1 papers to the "
                "Abi_2 HMM family without making DefenseFinder Abi2 "
                "exactly equivalent to AbiD1."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "abi2_locus_restricts_phage",
            "title": "Abi2 loci confer abortive-infection phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "DefenseFinder Abi2 locus to restricted bacteriophage "
                "propagation without asserting the unresolved phage trigger, "
                "small-RNA component, or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Abi2 as a named DefenseFinder "
                "single-profile abortive-infection system with an "
                "Abi2__Abi_2/PF07751 HMM profile while leaving its natural "
                "locus boundaries, AbiD/F-group breadth, upstream regulatory "
                "RNA relationships, phage trigger, and direct effector "
                "activity unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abi2_locus",
                    "label": "Abi2 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-component Abi2 abortive-infection locus "
                        "represented by the DefenseFinder Abi2__Abi_2 profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying an Abi2-family abortive-infection system."
                    ),
                },
                {
                    "node_id": "abi2_system_trait",
                    "label": "Abi2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Abi2 "
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
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abi2_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DefenseFinder represents Abi2 with the Abi2__Abi_2 "
                        "Pfam profile, and Abi-like loci mediate "
                        "abortive-infection phage restriction."
                    ),
                    "evidence": [
                        rules_evidence(),
                        hmm_inventory_evidence(),
                        {
                            "reference": ANBA,
                            "snippet": (
                                "Lactococcal phage abortive infection (AbiD1) "
                                "determined by plasmid pIL105 is active on both "
                                "prolate- and small-isometric-head phages"
                            ),
                            "notes": (
                                "Anba et al. support abortive-infection "
                                "antiphage activity in the Abi-like family."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abi2_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the Abi2 "
                        "abortive-infection system possession trait."
                    ),
                    "evidence": [
                        {
                            "reference": BIDNENKO,
                            "snippet": (
                                "Phage bIL66 is unable to grow on Lactococcus "
                                "lactis cells harboring the abortive infection "
                                "gene abiD1."
                            ),
                            "notes": (
                                "Bidnenko et al. connect AbiD1-family carriage "
                                "to blocked phage growth."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abi2_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "Abi2 system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": CHOPIN,
                            "snippet": (
                                "Abortive infection (Abi) systems, also called "
                                "phage exclusion, block phage multiplication "
                                "and cause premature bacterial cell death upon "
                                "phage infection."
                            ),
                            "notes": (
                                "Chopin et al. place Abi systems in the "
                                "abortive-infection class of phage defense."
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
            "discussion_id": "abi2-family-boundary-gap",
            "prompt": (
                "Resolve the natural Abi2 locus breadth, phage trigger, and "
                "AbiD/F-group mapping before minting narrower Abi2 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The DefenseFinder Abi2 model namespace requires the "
                "Abi2__Abi_2 PF07751 profile; InterPro treats PF07751 as "
                "an Abi-like family, and UniProt maps the AbiD1 protein "
                "onto the same Pfam family. This first record leaves "
                "unresolved whether DefenseFinder Abi2 exactly corresponds "
                "to AbiD1, the broader AbiD/F group, or a different subset "
                "of Abi-like loci; it therefore avoids protein-level "
                "chemistry and records only the genome-level model "
                "namespace."
            ),
            "attaches_to": ["causal_graphs#abi2_locus_restricts_phage"],
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
            "Minted Abi2 system as a DOI-backed GENOMICS TraitRecord "
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
            "Abi2 system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
