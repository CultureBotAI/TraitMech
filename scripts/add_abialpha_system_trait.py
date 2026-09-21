"""Add the AbiAlpha system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abialpha_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

LOSSOUARN = "DOI:10.3390/v11010048"
LOSSOUARN_PMID = "PMID:30634666"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T23:47:17Z"
PARENT_TIMESTAMP = "2026-09-20T23:47:18Z"
IDENTIFIER = "traitmech:000322"
PROPOSAL = "proposals/metpo_traitmech_v199"

HMM_ROW = (
    "| AbiAlpha__AbiAlpha                               | "
    "                                                  | AbiAlpha               | "
    "PF14337.11              | 27.1   |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, and AbiU are split out as "
    "traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, traitmech:000301, traitmech:000303, "
    "traitmech:000304, traitmech:000306, traitmech:000316, "
    "traitmech:000317, traitmech:000318, traitmech:000319, "
    "traitmech:000320, and traitmech:000321, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang "
    "et al., Bouchard et al., Haaber et al., Owen et al., Depardieu "
    "et al., Prevots et al., O'Connor et al., Su et al., Twomey "
    "et al., McLandsborough et al., Parreira et al., Durmaz et al., "
    "and Dai et al. still support Abi as a genomically encoded phage "
    "defense strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, two-separated-locus "
    "lactococcal AbiR DNA-replication impediment, pBF61-derived "
    "lactococcal AbiD burst-size reduction, lactococcal AbiB "
    "phage-transcript decay, lactococcal AbiC Prf infected-cell death, "
    "lactococcal AbiU phage-transcription delay, and other Abi families. "
    "Additional narrower TraitRecords need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, and AbiAlpha are split out as "
    "traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, traitmech:000301, traitmech:000303, "
    "traitmech:000304, traitmech:000306, traitmech:000316, "
    "traitmech:000317, traitmech:000318, traitmech:000319, "
    "traitmech:000320, traitmech:000321, and traitmech:000322, "
    "respectively. Lopatina et al., Fineran et al., Dy et al., Durmaz "
    "and Klaenhammer, Wang et al., Bouchard et al., Haaber et al., "
    "Owen et al., Depardieu et al., Prevots et al., O'Connor et al., "
    "Su et al., Twomey et al., McLandsborough et al., Parreira et al., "
    "Durmaz et al., Dai et al., and Lossouarn et al. still support Abi "
    "as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, staphylococcal-"
    "kinase-triggered cell death, lactococcal AbiH phage resistance, "
    "two-gene lactococcal AbiG RNA-synthesis interference, single-ORF "
    "lactococcal AbiI burst-size reduction, two-separated-locus "
    "lactococcal AbiR DNA-replication impediment, pBF61-derived "
    "lactococcal AbiD burst-size reduction, lactococcal AbiB "
    "phage-transcript decay, lactococcal AbiC Prf infected-cell death, "
    "lactococcal AbiU phage-transcription delay, enterococcal "
    "AbiAlpha premature lysis, and other Abi families. Additional "
    "narrower TraitRecords need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death "
    "mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiAlpha as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000322 for "
    "the AbiAlpha system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiAlpha | 10\\.3390/v11010048 | Enterococcus faecalis "
            "countermeasures defeat a virulent Picovirinae bacteriophage"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiAlpha "
            "model namespace to the enterococcal AbiAlpha discovery paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiAlpha__AbiAlpha "
            "under the AbiAlpha model namespace with Pfam PF14337.11."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiAlpha system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "abi-alpha-family locus represented by the DefenseFinder "
        "AbiAlpha__AbiAlpha profile and exemplified by the Enterococcus "
        "faecalis V583 prophage 6 abi-alpha determinant, whose encoded "
        "DUF4393/PF14337-family activity perturbs the Idefix lytic cycle "
        "and causes premature lysis of infected Enterococcus faecalis."
    ),
    "definition_source": LOSSOUARN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiAlpha",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": LOSSOUARN_PMID,
            "snippet": (
                "We found that E. faecalis V583 prophage 6 was "
                "particularly efficient in resisting Idefix infection "
                "thanks to a new abortive infection (Abi) mechanism, "
                "which we designated Abiα."
            ),
            "notes": (
                "Lossouarn et al. named a new Abi mechanism from "
                "Enterococcus faecalis V583 prophage 6."
            ),
        },
        {
            "reference": LOSSOUARN_PMID,
            "snippet": (
                "It corresponded to the Pfam domain family with unknown "
                "function DUF4393 and conferred a typical Abi phenotype by "
                "causing a premature lysis"
            ),
            "notes": (
                "Lossouarn et al. connected AbiAlpha to DUF4393 and an "
                "infected-cell premature-lysis phenotype."
            ),
        },
        {
            "reference": LOSSOUARN_PMID,
            "snippet": (
                "The abiα gene is widespread among prophages of "
                "enterococci and other Gram-positive bacteria."
            ),
            "notes": (
                "Lossouarn et al. describe AbiAlpha homologs as prophage "
                "features rather than a single V583-only gene."
            ),
        },
        {
            "reference": LOSSOUARN,
            "snippet": (
                "These results confirmed that ef2833 is responsible for "
                "the abortive mechanism."
            ),
            "notes": (
                "Lossouarn et al. experimentally connected ef2833 to the "
                "V583 prophage 6 Abi phenotype."
            ),
        },
        {
            "reference": LOSSOUARN,
            "snippet": "We concluded that Abiα provokes a lysis asynchrony.",
            "notes": (
                "Lossouarn et al. linked the AbiAlpha mechanism to altered "
                "Idefix lysis timing."
            ),
        },
        {
            "reference": LOSSOUARN,
            "snippet": (
                "Upon Idefix infection, cells are dying while the Idefix "
                "lytic cycle is perturbed"
            ),
            "notes": (
                "Lossouarn et al. summarized the system as infected-cell "
                "death with perturbed Idefix lytic-cycle progression."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1351",
            "taxon_label": "Enterococcus faecalis",
            "note": (
                "Lossouarn et al. characterized AbiAlpha from Enterococcus "
                "faecalis V583 prophage 6 and showed that it causes "
                "premature lysis during Idefix infection."
            ),
            "reference": LOSSOUARN,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abialpha_locus_causes_enterococcal_premature_lysis",
            "title": "AbiAlpha perturbs Idefix lysis in Enterococcus faecalis",
            "description": (
                "Conservative system-level sketch linking an "
                "abi-alpha-family locus to AbiAlpha antiphage "
                "activity, Idefix lytic-cycle perturbation, premature "
                "lysis of infected Enterococcus faecalis, and "
                "AbiAlpha-system possession without asserting the direct "
                "DUF4393-family molecular target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiAlpha as a named DefenseFinder "
                "single-profile abortive-infection system whose V583 "
                "prophage 6 prototype restricts Idefix by perturbing "
                "lysis timing. It leaves the direct phage trigger, "
                "DUF4393-family molecular function, direct Idefix target, "
                "natural host range, and phage escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abialpha_locus",
                    "label": "abi-alpha locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abi-alpha-family abortive-infection locus "
                        "represented by the DefenseFinder "
                        "AbiAlpha__AbiAlpha profile."
                    ),
                },
                {
                    "node_id": "abialpha_antiphage_activity",
                    "label": "AbiAlpha antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Enterococcal abortive-infection activity mediated "
                        "by the AbiAlpha system."
                    ),
                },
                {
                    "node_id": "idefix_lytic_cycle_perturbation",
                    "label": "Idefix lytic-cycle perturbation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Perturbation of the Idefix lytic cycle in "
                        "AbiAlpha-containing Enterococcus faecalis."
                    ),
                },
                {
                    "node_id": "infected_cell_premature_lysis",
                    "label": "infected-cell premature lysis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Premature lysis of Idefix-infected Enterococcus "
                        "faecalis cells that express AbiAlpha."
                    ),
                },
                {
                    "node_id": "abialpha_system_trait",
                    "label": "AbiAlpha system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiAlpha "
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
                    "subject": "abialpha_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abialpha_antiphage_activity",
                    "description": (
                        "The abi-alpha-family locus encoded by V583 "
                        "prophage 6 is responsible for AbiAlpha antiphage "
                        "activity, and DefenseFinder models AbiAlpha as a "
                        "single PF14337-family HMM profile."
                    ),
                    "evidence": [
                        {
                            "reference": LOSSOUARN_PMID,
                            "snippet": (
                                "We found that E. faecalis V583 prophage 6 "
                                "was particularly efficient in resisting "
                                "Idefix infection thanks to a new abortive "
                                "infection (Abi) mechanism, which we "
                                "designated Abiα."
                            ),
                            "notes": (
                                "Lossouarn et al. localized AbiAlpha to "
                                "Enterococcus faecalis V583 prophage 6."
                            ),
                        },
                        {
                            "reference": LOSSOUARN,
                            "snippet": (
                                "These results confirmed that ef2833 is "
                                "responsible for the abortive mechanism."
                            ),
                            "notes": (
                                "Lossouarn et al. connected ef2833 with "
                                "the V583 prophage 6 Abi phenotype."
                            ),
                        },
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "abialpha_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "idefix_lytic_cycle_perturbation",
                    "description": (
                        "AbiAlpha activity perturbs the Idefix lytic cycle "
                        "in infected Enterococcus faecalis cells."
                    ),
                    "evidence": [
                        {
                            "reference": LOSSOUARN,
                            "snippet": (
                                "Upon Idefix infection, cells are dying "
                                "while the Idefix lytic cycle is perturbed"
                            ),
                            "notes": (
                                "Lossouarn et al. summarized the AbiAlpha "
                                "output as death of infected cells while "
                                "the Idefix lytic cycle is perturbed."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abialpha_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "infected_cell_premature_lysis",
                    "description": (
                        "AbiAlpha activity causes premature lysis of "
                        "Idefix-infected Enterococcus faecalis."
                    ),
                    "evidence": [
                        {
                            "reference": LOSSOUARN_PMID,
                            "snippet": (
                                "conferred a typical Abi phenotype by "
                                "causing a premature lysis"
                            ),
                            "notes": (
                                "Lossouarn et al. reported premature lysis "
                                "as the AbiAlpha-infected-cell output."
                            ),
                        },
                        {
                            "reference": LOSSOUARN,
                            "snippet": (
                                "Based on our results, we can only "
                                "speculate that Abiα interferes with lysis"
                            ),
                            "notes": (
                                "Lossouarn et al. framed the direct "
                                "AbiAlpha lysis target as unresolved."
                            ),
                        },
                    ],
                },
                {
                    "subject": "idefix_lytic_cycle_perturbation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abialpha_system_trait",
                    "description": (
                        "Perturbation of Idefix lytic-cycle progression "
                        "contributes to the AbiAlpha system trait."
                    ),
                    "evidence": [
                        {
                            "reference": LOSSOUARN,
                            "snippet": (
                                "Upon Idefix infection, cells are dying "
                                "while the Idefix lytic cycle is perturbed"
                            ),
                            "notes": (
                                "Lossouarn et al. connected AbiAlpha with "
                                "Idefix lytic-cycle perturbation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "infected_cell_premature_lysis",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abialpha_system_trait",
                    "description": (
                        "Premature lysis of Idefix-infected Enterococcus "
                        "faecalis realizes the AbiAlpha "
                        "abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": LOSSOUARN_PMID,
                            "snippet": (
                                "It corresponded to the Pfam domain family "
                                "with unknown function DUF4393 and "
                                "conferred a typical Abi phenotype by "
                                "causing a premature lysis"
                            ),
                            "notes": (
                                "Lossouarn et al. identified premature "
                                "lysis as an AbiAlpha Abi phenotype."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abialpha_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiAlpha system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": LOSSOUARN_PMID,
                            "snippet": (
                                "a new abortive infection (Abi) mechanism, "
                                "which we designated Abiα"
                            ),
                            "notes": (
                                "Lossouarn et al. place AbiAlpha in the "
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
            "discussion_id": "abialpha-lysis-route-gap",
            "prompt": (
                "Resolve the AbiAlpha direct molecular target, Idefix "
                "trigger, lysis route, natural host range, and phage escape "
                "routes before minting narrower AbiAlpha mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Lossouarn et al. support AbiAlpha as a prophage-encoded "
                "Enterococcus faecalis abortive-infection system that maps "
                "to DUF4393/PF14337 and perturbs Idefix lysis timing. "
                "DefenseFinder represents AbiAlpha with a one-profile HMM "
                "inventory row but does not resolve the direct phage "
                "trigger, DUF4393-family molecular function, Idefix lysis "
                "target, natural host range, or escape routes."
            ),
            "attaches_to": ["causal_graphs#abialpha_locus_causes_enterococcal_premature_lysis"],
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
            "Minted AbiAlpha system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiAlpha system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
