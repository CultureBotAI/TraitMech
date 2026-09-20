"""Add the AbiU system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abiu_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DAI = "DOI:10.1128/AEM.67.11.5225-5232.2001"
DAI_PMID = "PMID:11679349"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T22:48:12Z"
PARENT_TIMESTAMP = "2026-09-20T22:48:13Z"
IDENTIFIER = "traitmech:000321"
PROPOSAL = "proposals/metpo_traitmech_v198"

HMM_ROW = (
    "| AbiU__AbiU                                       | "
    "AbiU__AbiU                                       | AbiU                   | "
    "Custom                  | 60     |"
)

OLD_PARENT_RATIONALE = (
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
NEW_PARENT_RATIONALE = (
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
PARENT_CHANGES = (
    "Documented AbiU as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000321 for "
    "the AbiU system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiU | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiU model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiU\tAbiU\t1\t1\tAbiU__AbiU",
        "notes": (
            "The DefenseFinder rules table models AbiU as a one-component "
            "system requiring the AbiU__AbiU profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiU__AbiU under the "
            "AbiU model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiU system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "abiU-family locus represented by the DefenseFinder AbiU__AbiU "
        "profile and exemplified by the Lactococcus lactis LL51-1 AbiU "
        "determinant, whose abiU1 open reading frame is responsible for "
        "phage resistance, whose abiU2 region may downregulate 936/P335 "
        "resistance, and whose activity reduces c2, 936, and P335 "
        "lactococcal phage plaquing while delaying transcription of "
        "phages 712 and c2."
    ),
    "definition_source": DAI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiU",
            "synonym_type": "RELATED_SYNONYM",
            "source": DAI,
        }
    ],
    "evidence": [
        {
            "reference": DAI_PMID,
            "snippet": (
                "This study reports on the identification and characterization "
                "of a novel abortive infection system, AbiU, from Lactococcus "
                "lactis."
            ),
            "notes": (
                "Dai et al. identify AbiU as a novel Lactococcus lactis "
                "abortive-infection system."
            ),
        },
        {
            "reference": DAI_PMID,
            "snippet": (
                "AbiU confers resistance to phages from the three main "
                "industrially relevant lactococcal phage species: c2, 936, "
                "and P335."
            ),
            "notes": (
                "Dai et al. measured the AbiU activity spectrum across "
                "representative c2, 936, and P335 lactococcal phages."
            ),
        },
        {
            "reference": DAI_PMID,
            "snippet": (
                "The presence of AbiU reduced the efficiency of plaquing "
                "against specific phage from each species as follows: 3.7 x "
                "10(-1), 1.0 x 10(-2), and 1.0 x 10(-1), respectively."
            ),
            "notes": (
                "Dai et al. quantified phage-specific AbiU reductions in "
                "efficiency of plaquing against c2, 936, and P335 "
                "representatives."
            ),
        },
        {
            "reference": DAI_PMID,
            "snippet": (
                "abiU involves two open reading frames, abiU1 (1,772 bp) and "
                "abiU2 (1,019 bp)."
            ),
            "notes": (
                "Dai et al. reported a two-ORF abiU locus rather than "
                "resolving AbiU as a single isolated protein trait."
            ),
        },
        {
            "reference": DAI_PMID,
            "snippet": (
                "Evidence indicates that AbiU1 is responsible for phage "
                "resistance and that AbiU2 may downregulate phage resistance "
                "against 936 and P335 type phages but not c2 type phage."
            ),
            "notes": (
                "Dai et al. connected AbiU1 to the phage-resistance "
                "phenotype and left AbiU2 as a likely regulator of a "
                "phage-species-specific resistance output."
            ),
        },
        {
            "reference": DAI_PMID,
            "snippet": (
                "AbiU appeared to delay transcription of both phage 712 and "
                "c2, with the effect being more marked on phage c2."
            ),
            "notes": (
                "Dai et al. linked AbiU to delayed phage transcription "
                "without resolving the direct phage trigger or AbiU1 target."
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
                "Dai et al. characterized AbiU from Lactococcus lactis "
                "LL51-1 and showed that AbiU confers resistance to c2, "
                "936, and P335 lactococcal phages."
            ),
            "reference": DAI,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abiu_locus_delays_lactococcal_phage_transcription",
            "title": "AbiU activity delays lactococcal phage transcription",
            "description": (
                "Conservative system-level sketch linking an abiU-family "
                "locus to AbiU antiphage activity, reduced c2/936/P335 "
                "phage plaquing, delayed phage 712 and c2 transcription, "
                "and AbiU-system possession without asserting the unresolved "
                "phage trigger or AbiU1 molecular target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiU as a named DefenseFinder "
                "single-profile abortive-infection system whose LL51-1 "
                "prototype restricts c2, 936, and P335 lactococcal phages. "
                "It leaves the direct phage trigger, AbiU1 molecular "
                "function, AbiU2 downregulation route, natural locus "
                "breadth, and phage escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abiu_locus",
                    "label": "abiU locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abiU-family abortive-infection locus represented "
                        "by the DefenseFinder AbiU__AbiU profile."
                    ),
                },
                {
                    "node_id": "abiu_antiphage_activity",
                    "label": "AbiU antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection phage resistance mediated by the "
                        "AbiU system."
                    ),
                },
                {
                    "node_id": "lactococcal_phage_plaquing_reduction",
                    "label": "lactococcal phage plaquing reduction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced plaquing of c2, 936, and P335 lactococcal "
                        "phages by an AbiU-containing host."
                    ),
                },
                {
                    "node_id": "phage_transcription_delay",
                    "label": "phage transcription delay",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Delayed transcription of phages 712 and c2 in "
                        "AbiU-containing Lactococcus lactis hosts."
                    ),
                },
                {
                    "node_id": "abiu_system_trait",
                    "label": "AbiU system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiU "
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
                    "subject": "abiu_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abiu_antiphage_activity",
                    "description": (
                        "The abiU-family locus encodes AbiU antiphage "
                        "activity, and DefenseFinder models AbiU as a "
                        "one-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "abiU involves two open reading frames, "
                                "abiU1 (1,772 bp) and abiU2 (1,019 bp)."
                            ),
                            "notes": (
                                "Dai et al. identified the two ORFs in the "
                                "AbiU determinant."
                            ),
                        },
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "Evidence indicates that AbiU1 is responsible "
                                "for phage resistance"
                            ),
                            "notes": (
                                "Dai et al. connected AbiU1 to the "
                                "phage-resistance phenotype."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "abiu_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "lactococcal_phage_plaquing_reduction",
                    "description": (
                        "AbiU activity reduces plaquing of c2, 936, and "
                        "P335 lactococcal phages."
                    ),
                    "evidence": [
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "AbiU confers resistance to phages from the "
                                "three main industrially relevant "
                                "lactococcal phage species: c2, 936, and "
                                "P335."
                            ),
                            "notes": (
                                "Dai et al. measured AbiU activity against "
                                "c2, 936, and P335 phages."
                            ),
                        },
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "The presence of AbiU reduced the efficiency "
                                "of plaquing against specific phage from "
                                "each species as follows: 3.7 x 10(-1), 1.0 "
                                "x 10(-2), and 1.0 x 10(-1), respectively."
                            ),
                            "notes": (
                                "Dai et al. quantified phage-specific AbiU "
                                "EOP reductions."
                            ),
                        },
                    ],
                },
                {
                    "subject": "abiu_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_transcription_delay",
                    "description": (
                        "AbiU activity delays transcription of lactococcal "
                        "phages 712 and c2."
                    ),
                    "evidence": [
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "AbiU appeared to delay transcription of "
                                "both phage 712 and c2"
                            ),
                            "notes": (
                                "Dai et al. detected delayed phage 712 and "
                                "c2 transcription in the presence of AbiU."
                            ),
                        }
                    ],
                },
                {
                    "subject": "lactococcal_phage_plaquing_reduction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abiu_system_trait",
                    "description": (
                        "Reduced c2/936/P335 lactococcal phage plaquing "
                        "realizes the AbiU abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "This study reports on the identification "
                                "and characterization of a novel abortive "
                                "infection system, AbiU, from Lactococcus "
                                "lactis."
                            ),
                            "notes": (
                                "Dai et al. place AbiU in the "
                                "abortive-infection class of phage defense."
                            ),
                        },
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "The presence of AbiU reduced the efficiency "
                                "of plaquing against specific phage from "
                                "each species"
                            ),
                            "notes": (
                                "Dai et al. linked AbiU to reduced "
                                "lactococcal phage plaquing."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "phage_transcription_delay",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abiu_system_trait",
                    "description": (
                        "Delayed 712/c2 phage transcription contributes to "
                        "the AbiU abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "AbiU appeared to delay transcription of "
                                "both phage 712 and c2"
                            ),
                            "notes": (
                                "Dai et al. identified delayed phage "
                                "transcription as an AbiU-associated output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abiu_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiU system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DAI_PMID,
                            "snippet": (
                                "This study reports on the identification "
                                "and characterization of a novel abortive "
                                "infection system, AbiU"
                            ),
                            "notes": (
                                "Dai et al. place AbiU in the "
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
            "discussion_id": "abiu-orf-and-transcription-gap",
            "prompt": (
                "Resolve the AbiU phage trigger, direct AbiU1 and AbiU2 "
                "functions, and phage-transcription-delay route before "
                "minting narrower AbiU mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Dai et al. support AbiU as a named lactococcal "
                "abortive-infection system that reduces plaquing of c2, "
                "936, and P335 phages and delays 712 and c2 phage "
                "transcription. DefenseFinder represents AbiU with a "
                "one-profile rule, but this first system-level record "
                "leaves the phage trigger, AbiU1 molecular function, "
                "AbiU2 downregulation route, natural locus breadth, and "
                "phage escape routes unresolved."
            ),
            "attaches_to": ["causal_graphs#abiu_locus_delays_lactococcal_phage_transcription"],
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
            "Minted AbiU system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiU system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
