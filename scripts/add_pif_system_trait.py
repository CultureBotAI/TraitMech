"""Add the Pif system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pif_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

CRAM = "DOI:10.1007/BF00327934"
CRAM_PMID = "PMID:6096670"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T01:30:12Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-21T01:30:13Z"
PARENT_TIMESTAMP = "2026-09-21T01:30:13Z"
IDENTIFIER = "traitmech:000323"
PROPOSAL = "proposals/metpo_traitmech_v200"

PIFA_HMM_ROW = (
    "| Pif__PifA                                        | "
    "Pif__PifA                                        | Pif                    | "
    "Custom                  | 20     |"
)
PIFC_HMM_ROW = (
    "| Pif__PifC                                        | "
    "Pif__PifC                                        | Pif                    | "
    "Custom                  | 20     |"
)

OLD_PARENT_RATIONALE = (
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
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, and Pif are split "
    "out as traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, traitmech:000301, traitmech:000303, "
    "traitmech:000304, traitmech:000306, traitmech:000316, "
    "traitmech:000317, traitmech:000318, traitmech:000319, "
    "traitmech:000320, traitmech:000321, traitmech:000322, and "
    "traitmech:000323, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., Depardieu et al., Prevots et al., "
    "O'Connor et al., Su et al., Twomey et al., McLandsborough et al., "
    "Parreira et al., Durmaz et al., Dai et al., Lossouarn et al., and "
    "Cram et al. still support abortive infection as a genomically "
    "encoded phage defense strategy that spans mechanistically diverse "
    "toxin-antitoxin, premature-lysis, RT-related polymerase, "
    "two-component, translation-inhibition, prophage-encoded "
    "DNA-replication-inhibition, staphylococcal-kinase-triggered cell "
    "death, lactococcal AbiH phage resistance, two-gene lactococcal "
    "AbiG RNA-synthesis interference, single-ORF lactococcal AbiI "
    "burst-size reduction, two-separated-locus lactococcal AbiR "
    "DNA-replication impediment, pBF61-derived lactococcal AbiD "
    "burst-size reduction, lactococcal AbiB phage-transcript decay, "
    "lactococcal AbiC Prf infected-cell death, lactococcal AbiU "
    "phage-transcription delay, enterococcal AbiAlpha premature lysis, "
    "F-plasmid pif-region T7 abortive infection, and other families. "
    "Additional narrower TraitRecords need separate review to ground "
    "each subfamily's trigger, effector, growth-arrest or cell-death "
    "mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented Pif as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000323 for "
    "the Pif system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Pif | 10\\.1007/BF00327934 | Molecular analysis of F "
            "plasmid pif region specifying abortive infection of T7 phage"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Pif model "
            "namespace to the F-plasmid pif-region molecular analysis paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "Pif\tPif\t2\t2\tPif__PifA, Pif__PifC",
        "notes": (
            "The DefenseFinder rules table models Pif as a two-component "
            "system requiring both the Pif__PifA and Pif__PifC profiles."
        ),
    }


def pifa_hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": PIFA_HMM_ROW,
        "notes": "The DefenseFinder HMM inventory records Pif__PifA under Pif.",
    }


def pifc_hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": PIFC_HMM_ROW,
        "notes": "The DefenseFinder HMM inventory records Pif__PifC under Pif.",
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Pif system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "F-plasmid pif-family locus represented by the DefenseFinder "
        "Pif__PifA and Pif__PifC profiles and exemplified by the pif "
        "region that specifies abortive infection of T7 phage."
    ),
    "definition_source": CRAM,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "Pif",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": CRAM_PMID,
            "snippet": (
                "Molecular analysis of F plasmid pif region specifying "
                "abortive infection of T7 phage."
            ),
            "notes": (
                "Cram et al. title the paper around F-plasmid pif-region "
                "specification of the T7 abortive-infection phenotype."
            ),
        },
        {
            "reference": CRAM,
            "snippet": (
                "We report the molecular cloning of the pif region of the "
                "F plasmid and its physical dissection by subcloning and "
                "deletion analysis."
            ),
            "notes": (
                "Cram et al. cloned and deletion-mapped the F-plasmid pif "
                "region."
            ),
        },
        {
            "reference": CRAM,
            "snippet": (
                "Examination of the polypeptide products synthesized in "
                "maxicells by plasmids carrying defined pif sequences has "
                "shown that the region specifies at least two proteins of "
                "molecular weights 80,000 and 40,000, the genes for which "
                "appear to lie in the same transcriptional unit."
            ),
            "notes": (
                "Cram et al. support a multigene pif region without "
                "resolving a direct PifA or PifC molecular function."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        pifa_hmm_inventory_evidence(),
        pifc_hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pif_locus_specifies_t7_abortive_infection",
            "title": "Pif locus specifies T7 abortive infection",
            "description": (
                "Conservative system-level sketch linking an F-plasmid "
                "pif-family locus to T7 abortive infection and Pif-system "
                "possession without asserting the direct phage trigger, "
                "host-cell output, or PifA/PifC molecular targets."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Pif as a named DefenseFinder "
                "two-profile abortive-infection system whose F-plasmid "
                "prototype specifies T7 abortive infection. It leaves the "
                "direct T7 trigger, PifA and PifC molecular functions, "
                "host-cell output, and phage escape route unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pif_locus",
                    "label": "pif locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An F-plasmid pif-family abortive-infection locus "
                        "represented by the DefenseFinder Pif__PifA and "
                        "Pif__PifC profiles."
                    ),
                },
                {
                    "node_id": "t7_abortive_infection",
                    "label": "T7 abortive infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive infection of T7 phage specified by an "
                        "F-plasmid pif region."
                    ),
                },
                {
                    "node_id": "pif_system_trait",
                    "label": "Pif system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Pif "
                        "abortive-infection phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "pif_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t7_abortive_infection",
                    "description": (
                        "The F-plasmid pif region specifies T7 abortive "
                        "infection, and DefenseFinder represents Pif with "
                        "required PifA and PifC profiles."
                    ),
                    "evidence": [
                        {
                            "reference": CRAM_PMID,
                            "snippet": (
                                "Molecular analysis of F plasmid pif "
                                "region specifying abortive infection of "
                                "T7 phage."
                            ),
                            "notes": (
                                "Cram et al. frame the F-plasmid pif "
                                "region as specifying T7 abortive infection."
                            ),
                        },
                        {
                            "reference": CRAM,
                            "snippet": (
                                "the region specifies at least two "
                                "proteins of molecular weights 80,000 and "
                                "40,000"
                            ),
                            "notes": (
                                "Cram et al. observed two pif-region "
                                "polypeptides in maxicells."
                            ),
                        },
                        rules_evidence(),
                        pifa_hmm_inventory_evidence(),
                        pifc_hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "t7_abortive_infection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "pif_system_trait",
                    "description": (
                        "F-plasmid-pif-specified T7 abortive infection "
                        "realizes the Pif system trait."
                    ),
                    "evidence": [
                        {
                            "reference": CRAM_PMID,
                            "snippet": (
                                "Molecular analysis of F plasmid pif "
                                "region specifying abortive infection of "
                                "T7 phage."
                            ),
                            "notes": (
                                "Cram et al. support T7 abortive "
                                "infection as the pif-region output."
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
            "discussion_id": "pif-output-gap",
            "prompt": (
                "Resolve the direct T7 trigger, PifA and PifC molecular "
                "functions, host-cell output, and phage escape routes "
                "before minting narrower Pif mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Cram et al. support an F-plasmid pif-region "
                "abortive-infection system that maps to a two-profile "
                "DefenseFinder model, but the direct T7 trigger, the "
                "molecular functions of PifA and PifC, the host-cell "
                "growth-arrest or cell-death output, and phage escape "
                "routes remain unresolved."
            ),
            "attaches_to": ["causal_graphs#pif_locus_specifies_t7_abortive_infection"],
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
            "Minted Pif system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed canonical example evidence while minting Pif system "
            "and left canonical_examples empty: the Cram et al. prototype "
            "supports an F-plasmid pif region that specifies T7 abortive "
            "infection and the pinned DefenseFinder registry maps a "
            "two-profile Pif namespace, but the available curation sources "
            "do not identify a natural organism instance with a directly "
            "observed Pif locus. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
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
            "Pif system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
