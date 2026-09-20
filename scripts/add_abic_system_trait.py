"""Add the AbiC system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abic_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DURMAZ = "DOI:10.1128/jb.174.22.7463-7469.1992"
DURMAZ_PMID = "PMID:1429469"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T22:01:24Z"
PARENT_TIMESTAMP = "2026-09-20T22:01:25Z"
IDENTIFIER = "traitmech:000320"
PROPOSAL = "proposals/metpo_traitmech_v197"

HMM_ROW = (
    "| AbiC__AbiC                                       | "
    "AbiC__AbiC                                       | AbiC                   | "
    "Custom                  | 20     |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, and AbiB are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, "
    "traitmech:000318, and traitmech:000319, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang "
    "et al., Bouchard et al., Haaber et al., Owen et al., Depardieu "
    "et al., Prevots et al., O'Connor et al., Su et al., Twomey "
    "et al., McLandsborough et al., and Parreira et al. still support "
    "Abi as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, two-separated-locus "
    "lactococcal AbiR DNA-replication impediment, pBF61-derived "
    "lactococcal AbiD burst-size reduction, lactococcal AbiB "
    "phage-transcript decay, and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, and AbiC are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, "
    "traitmech:000318, traitmech:000319, and traitmech:000320, "
    "respectively. Lopatina et al., Fineran et al., Dy et al., Durmaz "
    "and Klaenhammer, Wang et al., Bouchard et al., Haaber et al., "
    "Owen et al., Depardieu et al., Prevots et al., O'Connor et al., "
    "Su et al., Twomey et al., McLandsborough et al., Parreira et al., "
    "and Durmaz et al. still support Abi as a genomically encoded phage "
    "defense strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, two-separated-locus "
    "lactococcal AbiR DNA-replication impediment, pBF61-derived "
    "lactococcal AbiD burst-size reduction, lactococcal AbiB "
    "phage-transcript decay, lactococcal AbiC Prf infected-cell death, "
    "and other Abi families. Additional narrower TraitRecords need separate "
    "review to ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiC as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000320 for "
    "the AbiC system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiC | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiC model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiC\tAbiC\t1\t1\tAbiC__AbiC",
        "notes": (
            "The DefenseFinder rules table models AbiC as a one-component "
            "system requiring the AbiC__AbiC profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiC__AbiC under the "
            "AbiC model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiC system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "abiC-family locus represented by the DefenseFinder AbiC__AbiC "
        "profile and exemplified by the Lactococcus lactis subsp. lactis "
        "ME2 pTN20 determinant whose abiC structural gene confers Prf "
        "abortive resistance to small isometric-headed phage p2, reducing "
        "plaquing, plaque size, and burst size while killing most infected "
        "Prf-positive cells."
    ),
    "definition_source": DURMAZ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiC",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": DURMAZ_PMID,
            "snippet": (
                "The genetic determinant for Prf (phage resistance five) "
                "was subcloned from the conjugative plasmid pTN20"
            ),
            "notes": (
                "Durmaz et al. subcloned the Prf determinant from the "
                "Lactococcus lactis ME2 conjugative plasmid pTN20."
            ),
        },
        {
            "reference": DURMAZ_PMID,
            "snippet": (
                "Prf reduces the efficiency of plaquing to 10(-2) to "
                "10(-3) and decreases the plaque size and burst size of "
                "the small isometric-headed phage p2"
            ),
            "notes": (
                "Durmaz et al. measured Prf-dependent reductions in p2 "
                "phage plating efficiency, plaque size, and burst size."
            ),
        },
        {
            "reference": DURMAZ_PMID,
            "snippet": (
                "Prf does not prevent phage adsorption or promote "
                "restriction and modification activities"
            ),
            "notes": (
                "Durmaz et al. distinguished Prf activity from adsorption "
                "blocking and restriction-modification activities."
            ),
        },
        {
            "reference": DURMAZ_PMID,
            "snippet": (
                "90% of Prf+ cells infected with phage p2 die. Thus, phage "
                "infections in Prf+ cells are aborted."
            ),
            "notes": (
                "Durmaz et al. showed that most Prf-positive cells infected "
                "with phage p2 die and interpreted those p2 infections as "
                "aborted."
            ),
        },
        {
            "reference": DURMAZ_PMID,
            "snippet": "DNA sequencing identified a 1,056-nucleotide structural gene designated abiC",
            "notes": (
                "Durmaz et al. identified the abiC structural gene in the "
                "Prf determinant."
            ),
        },
        {
            "reference": DURMAZ_PMID,
            "snippet": (
                "Prf+ expression was obtained when abiC was subcloned into "
                "the lactococcal expression vector pMG36e"
            ),
            "notes": (
                "Durmaz et al. showed that abiC expression is sufficient "
                "for Prf-positive activity in the pMG36e expression vector."
            ),
        },
        {
            "reference": DURMAZ_PMID,
            "snippet": (
                "Unlike abiA, the action of abiC does not appear to affect "
                "DNA replication"
            ),
            "notes": (
                "Durmaz et al. left AbiC downstream mechanism unresolved "
                "but distinguished it from AbiA-associated DNA-replication "
                "effects."
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
                "Durmaz et al. subcloned the Prf determinant from the "
                "Lactococcus lactis subsp. lactis ME2 conjugative plasmid "
                "pTN20 and showed that the abiC structural gene confers "
                "Prf-positive abortive resistance against small "
                "isometric-headed phage p2."
            ),
            "reference": DURMAZ,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abic_locus_aborts_lactococcal_phage_p2_infection",
            "title": "AbiC Prf activity aborts lactococcal phage p2 infection",
            "description": (
                "Conservative system-level sketch linking an abiC-family "
                "locus to Prf abortive-infection activity, reduced p2 "
                "phage propagation, Prf-positive infected-cell death, and "
                "AbiC-system possession without asserting an unresolved "
                "molecular target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiC as a named DefenseFinder "
                "single-profile abortive-infection system whose ME2 pTN20 "
                "prototype restricts small isometric-headed phage p2. It "
                "leaves the direct phage trigger, AbiC molecular function, "
                "cell-death route, natural locus breadth, and phage escape "
                "routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abic_locus",
                    "label": "abiC locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abiC-family abortive-infection locus represented "
                        "by the DefenseFinder AbiC__AbiC profile."
                    ),
                },
                {
                    "node_id": "abic_prf_activity",
                    "label": "AbiC Prf activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Prf abortive-infection phage resistance mediated by "
                        "the abiC structural gene."
                    ),
                },
                {
                    "node_id": "p2_phage_propagation_reduction",
                    "label": "p2 phage propagation reduction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced small isometric-headed phage p2 plating, "
                        "plaque size, and burst size in an AbiC-containing "
                        "Lactococcus lactis host."
                    ),
                },
                {
                    "node_id": "prf_positive_infected_cell_death",
                    "label": "Prf-positive infected cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Death of most Prf-positive Lactococcus lactis cells "
                        "after infection with phage p2."
                    ),
                },
                {
                    "node_id": "abic_system_trait",
                    "label": "AbiC system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiC "
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
                    "subject": "abic_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abic_prf_activity",
                    "description": (
                        "The abiC-family locus encodes the Prf "
                        "abortive-infection phage-resistance determinant, "
                        "and DefenseFinder models AbiC as a one-profile "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ_PMID,
                            "snippet": (
                                "DNA sequencing identified a 1,056-nucleotide "
                                "structural gene designated abiC"
                            ),
                            "notes": (
                                "Durmaz et al. identified the abiC "
                                "structural gene within the Prf determinant."
                            ),
                        },
                        {
                            "reference": DURMAZ_PMID,
                            "snippet": (
                                "Prf+ expression was obtained when abiC was "
                                "subcloned into the lactococcal expression "
                                "vector pMG36e"
                            ),
                            "notes": (
                                "Durmaz et al. showed that abiC subcloning "
                                "is sufficient for Prf-positive expression."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "abic_prf_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "p2_phage_propagation_reduction",
                    "description": (
                        "AbiC Prf activity reduces phage p2 plating, plaque "
                        "size, and burst size."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ_PMID,
                            "snippet": (
                                "Prf reduces the efficiency of plaquing to "
                                "10(-2) to 10(-3) and decreases the plaque "
                                "size and burst size of the small "
                                "isometric-headed phage p2"
                            ),
                            "notes": (
                                "Durmaz et al. measured reduced p2 plating "
                                "efficiency, plaque size, and burst size in "
                                "Prf-positive cells."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abic_prf_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "prf_positive_infected_cell_death",
                    "description": (
                        "AbiC Prf-positive activity is associated with "
                        "death of most phage p2-infected host cells."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ_PMID,
                            "snippet": (
                                "90% of Prf+ cells infected with phage p2 die. "
                                "Thus, phage infections in Prf+ cells are "
                                "aborted."
                            ),
                            "notes": (
                                "Durmaz et al. connect the Prf-positive "
                                "phenotype to infected-cell death and "
                                "aborted p2 infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "p2_phage_propagation_reduction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abic_system_trait",
                    "description": (
                        "Reduced p2 phage propagation realizes the AbiC "
                        "abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ_PMID,
                            "snippet": (
                                "Prf reduces the efficiency of plaquing to "
                                "10(-2) to 10(-3) and decreases the plaque "
                                "size and burst size of the small "
                                "isometric-headed phage p2"
                            ),
                            "notes": (
                                "Durmaz et al. measured reduced p2 plating "
                                "efficiency, plaque size, and burst size in "
                                "Prf-positive cells."
                            ),
                        },
                        {
                            "reference": DURMAZ_PMID,
                            "snippet": (
                                "Thus, abiC represents a second abortive "
                                "system found in ME2 that acts at a different "
                                "point of the phage lytic cycle."
                            ),
                            "notes": (
                                "Durmaz et al. place abiC in the "
                                "abortive-infection class and distinguish it "
                                "from the AbiA system."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abic_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiC system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DURMAZ_PMID,
                            "snippet": (
                                "Thus, abiC represents a second abortive "
                                "system found in ME2"
                            ),
                            "notes": (
                                "Durmaz et al. place abiC in the "
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
            "discussion_id": "abic-trigger-and-death-route-gap",
            "prompt": (
                "Resolve the AbiC phage trigger, AbiC molecular function, "
                "and infected-cell death route before minting narrower "
                "AbiC mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Durmaz et al. support AbiC as a named lactococcal "
                "abortive-infection determinant that reduces p2 plating, "
                "plaque size, and burst size while killing most "
                "Prf-positive infected cells. DefenseFinder represents "
                "AbiC with a one-profile rule, but this first system-level "
                "record leaves the phage trigger, AbiC molecular function, "
                "cell-death route, natural locus breadth, and phage escape "
                "routes unresolved."
            ),
            "attaches_to": ["causal_graphs#abic_locus_aborts_lactococcal_phage_p2_infection"],
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
            "Minted AbiC system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiC system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
