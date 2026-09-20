"""Add the AbiB system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abib_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

PARREIRA = "DOI:10.1046/j.1365-2958.1996.371896.x"
PARREIRA_PMID = "PMID:8825768"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T21:21:12Z"
PARENT_TIMESTAMP = "2026-09-20T21:21:13Z"
IDENTIFIER = "traitmech:000319"
PROPOSAL = "proposals/metpo_traitmech_v196"

HMM_ROW = (
    "| AbiB__AbiB                                       | "
    "AbiB__AbiB                                       | AbiB                   | "
    "Custom                  | 20     |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, and AbiD are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, and "
    "traitmech:000318, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., Depardieu et al., Prevots et al., "
    "O'Connor et al., Su et al., Twomey et al., and McLandsborough "
    "et al. still support Abi as a genomically encoded phage defense "
    "strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, two-separated-locus "
    "lactococcal AbiR DNA-replication impediment, pBF61-derived lactococcal "
    "AbiD burst-size reduction, and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
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
PARENT_CHANGES = (
    "Documented AbiB as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000319 for "
    "the AbiB system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiB | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiB model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiB\tAbiB\t1\t1\tAbiB__AbiB",
        "notes": (
            "The DefenseFinder rules table models AbiB as a one-component "
            "system requiring the AbiB__AbiB profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiB__AbiB under the "
            "AbiB model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiB system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "abiB-family locus represented by the DefenseFinder AbiB__AbiB "
        "profile and exemplified by the Lactococcus lactis IL1403 "
        "determinant whose AbiB activity blocks sensitive bIL170 phage "
        "growth and promotes rapid degradation of sensitive phage "
        "transcripts after infection."
    ),
    "definition_source": PARREIRA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiB",
            "synonym_type": "RELATED_SYNONYM",
            "source": PARREIRA,
        }
    ],
    "evidence": [
        {
            "reference": PARREIRA_PMID,
            "snippet": (
                "The abortive infection determinant AbiB prevents growth "
                "of the sensitive phage bIL170, but not of the resistant "
                "phage bIL41, on Lactococcus lactis strain IL1403"
            ),
            "notes": (
                "Parreira et al. place AbiB in the abortive-infection "
                "class and show that it blocks the sensitive lactococcal "
                "phage bIL170 on Lactococcus lactis IL1403."
            ),
        },
        {
            "reference": PARREIRA_PMID,
            "snippet": (
                "AbiB promotes a dramatic degradation of sensitive phage "
                "transcripts, starting 10-15 min after infection"
            ),
            "notes": (
                "Parreira et al. connect AbiB activity to rapid decay of "
                "transcripts from sensitive phages after infection."
            ),
        },
        {
            "reference": PARREIRA_PMID,
            "snippet": (
                "The decay of the transcripts is the probable cause of "
                "the arrest of the sensitive phage development"
            ),
            "notes": (
                "Parreira et al. infer that phage transcript decay causes "
                "arrest of AbiB-sensitive phage development."
            ),
        },
        {
            "reference": PARREIRA_PMID,
            "snippet": (
                "Mapping of the 5' end of degradation products "
                "established that they result from endonucleolytic "
                "cleavage preferentially at U/U, A/U and U/A sites"
            ),
            "notes": (
                "Parreira et al. map AbiB-associated phage transcript "
                "decay products to preferential endonucleolytic cleavage "
                "sites."
            ),
        },
        {
            "reference": PARREIRA_PMID,
            "snippet": (
                "an early product of the sensitive phage either induces "
                "the synthesis or stimulates the activity of an RNase in "
                "an AbiB+ cell"
            ),
            "notes": (
                "Parreira et al. leave the AbiB trigger and nuclease "
                "identity unresolved, favoring an open knowledge gap for "
                "narrower mechanism children."
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
                "Parreira et al. studied AbiB in Lactococcus lactis IL1403 "
                "and showed that it prevented sensitive bIL170 phage "
                "growth while promoting sensitive phage transcript decay."
            ),
            "reference": PARREIRA,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abib_locus_degrades_sensitive_phage_transcripts",
            "title": "AbiB activity degrades sensitive lactococcal phage transcripts",
            "description": (
                "Conservative system-level sketch linking an abiB-family "
                "locus to AbiB antiphage activity, sensitive-phage "
                "transcript degradation, sensitive-phage arrest, and "
                "abortive-infection system possession without asserting "
                "the unresolved phage trigger or nuclease effector."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiB as a named DefenseFinder "
                "single-profile abortive-infection system whose IL1403 "
                "prototype restricts bIL170 phage by promoting rapid "
                "sensitive-phage transcript degradation. It leaves the "
                "direct phage trigger, AbiB molecular function, RNase "
                "effector identity, natural locus breadth, and phage "
                "escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abib_locus",
                    "label": "abiB locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abiB-family abortive-infection locus "
                        "represented by the DefenseFinder AbiB__AbiB "
                        "profile."
                    ),
                },
                {
                    "node_id": "abib_antiphage_activity",
                    "label": "AbiB antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection phage resistance mediated by "
                        "the AbiB system."
                    ),
                },
                {
                    "node_id": "sensitive_phage_transcript_degradation",
                    "label": "sensitive phage transcript degradation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Rapid decay of sensitive lactococcal phage "
                        "transcripts in an AbiB-containing infected host."
                    ),
                },
                {
                    "node_id": "sensitive_phage_development_arrest",
                    "label": "sensitive phage development arrest",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Failure of AbiB-sensitive bIL170 phages to "
                        "complete productive growth on Lactococcus lactis "
                        "IL1403."
                    ),
                },
                {
                    "node_id": "abib_system_trait",
                    "label": "AbiB system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiB "
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
                    "subject": "abib_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abib_antiphage_activity",
                    "description": (
                        "The abiB-family locus encodes an "
                        "abortive-infection phage-resistance determinant, "
                        "and DefenseFinder models AbiB as a one-profile "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": PARREIRA_PMID,
                            "snippet": (
                                "The abortive infection determinant AbiB "
                                "prevents growth of the sensitive phage "
                                "bIL170"
                            ),
                            "notes": (
                                "Parreira et al. identify AbiB as an "
                                "abortive-infection determinant that blocks "
                                "sensitive phage growth."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "abib_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "sensitive_phage_transcript_degradation",
                    "description": (
                        "AbiB activity promotes rapid degradation of "
                        "sensitive phage transcripts after infection."
                    ),
                    "evidence": [
                        {
                            "reference": PARREIRA_PMID,
                            "snippet": (
                                "AbiB promotes a dramatic degradation of "
                                "sensitive phage transcripts, starting "
                                "10-15 min after infection"
                            ),
                            "notes": (
                                "Parreira et al. connect AbiB to rapid "
                                "decay of sensitive phage transcripts."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sensitive_phage_transcript_degradation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "sensitive_phage_development_arrest",
                    "description": (
                        "Transcript decay probably arrests development of "
                        "AbiB-sensitive phages."
                    ),
                    "evidence": [
                        {
                            "reference": PARREIRA_PMID,
                            "snippet": (
                                "The decay of the transcripts is the "
                                "probable cause of the arrest of the "
                                "sensitive phage development"
                            ),
                            "notes": (
                                "Parreira et al. interpret phage transcript "
                                "decay as the likely cause of sensitive "
                                "phage developmental arrest."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sensitive_phage_development_arrest",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abib_system_trait",
                    "description": (
                        "Arrest of sensitive lactococcal phage development "
                        "realizes the AbiB abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": PARREIRA_PMID,
                            "snippet": (
                                "The abortive infection determinant AbiB "
                                "prevents growth of the sensitive phage "
                                "bIL170"
                            ),
                            "notes": (
                                "Parreira et al. show that AbiB prevents "
                                "sensitive lactococcal phage growth."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abib_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiB system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": PARREIRA_PMID,
                            "snippet": "The abortive infection determinant AbiB",
                            "notes": (
                                "Parreira et al. place AbiB in the "
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
            "discussion_id": "abib-trigger-and-rnase-gap",
            "prompt": (
                "Resolve the AbiB phage trigger, AbiB molecular function, "
                "and RNase effector before minting narrower AbiB mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Parreira et al. support AbiB as a named lactococcal "
                "abortive-infection determinant that prevents bIL170 "
                "growth and promotes sensitive phage transcript "
                "degradation. DefenseFinder represents AbiB with a "
                "one-profile rule, but this first system-level record "
                "leaves the phage trigger, AbiB molecular function, RNase "
                "effector identity, natural locus breadth, and phage "
                "escape routes unresolved."
            ),
            "attaches_to": ["causal_graphs#abib_locus_degrades_sensitive_phage_transcripts"],
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
            "Minted AbiB system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiB system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
