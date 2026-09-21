"""Add the RexAB system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rexab_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

PARMA = "DOI:10.1101/gad.6.3.497"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T02:17:07Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-21T02:17:08Z"
PARENT_TIMESTAMP = "2026-09-21T02:17:08Z"
IDENTIFIER = "traitmech:000324"
PROPOSAL = "proposals/metpo_traitmech_v201"

REXA_HMM_ROW = (
    "| RexAB__RexA                                      | "
    "RexAB__RexA                                      | RexAB                  | "
    "PF15969.7               | 25     |"
)
REXB_HMM_ROW = (
    "| RexAB__RexB                                      | "
    "RexAB__RexB                                      | RexAB                  | "
    "PF15968.7               | 27     |"
)

OLD_PARENT_RATIONALE = (
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
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, and RexAB are "
    "split out as traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, traitmech:000301, traitmech:000303, "
    "traitmech:000304, traitmech:000306, traitmech:000316, "
    "traitmech:000317, traitmech:000318, traitmech:000319, "
    "traitmech:000320, traitmech:000321, traitmech:000322, "
    "traitmech:000323, and traitmech:000324, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang "
    "et al., Bouchard et al., Haaber et al., Owen et al., Depardieu "
    "et al., Prevots et al., O'Connor et al., Su et al., Twomey "
    "et al., McLandsborough et al., Parreira et al., Durmaz et al., "
    "Dai et al., Lossouarn et al., Cram et al., and Parma et al. still "
    "support abortive infection as a genomically encoded phage defense "
    "strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH "
    "phage resistance, two-gene lactococcal AbiG RNA-synthesis "
    "interference, single-ORF lactococcal AbiI burst-size reduction, "
    "two-separated-locus lactococcal AbiR DNA-replication impediment, "
    "pBF61-derived lactococcal AbiD burst-size reduction, lactococcal "
    "AbiB phage-transcript decay, lactococcal AbiC Prf infected-cell "
    "death, lactococcal AbiU phage-transcription delay, enterococcal "
    "AbiAlpha premature lysis, F-plasmid pif-region T7 abortive "
    "infection, lambda Rex two-component phage exclusion, and other "
    "families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented RexAB as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000324 for "
    "the RexAB system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "RexAB | 10\\.1101/gad\\.6\\.3\\.497 | The Rex system of "
            "bacteriophage lambda: tolerance and altruistic cell death"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named RexAB model "
            "namespace to the bacteriophage-lambda Rex system paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "RexAB\tRexAB\t2\t2\tRexAB__RexA, RexAB__RexB",
        "notes": (
            "The DefenseFinder rules table models RexAB as a two-component "
            "system requiring the RexA and RexB profiles."
        ),
    }


def rexa_hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": REXA_HMM_ROW,
        "notes": "The DefenseFinder HMM inventory records RexAB__RexA under RexAB.",
    }


def rexb_hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": REXB_HMM_ROW,
        "notes": "The DefenseFinder HMM inventory records RexAB__RexB under RexAB.",
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "RexAB system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "bacteriophage-lambda Rex-family locus represented by the "
        "DefenseFinder RexAB__RexA and RexAB__RexB profiles and "
        "exemplified by the rexA and rexB two-component system that "
        "aborts lytic growth of bacterial viruses."
    ),
    "definition_source": PARMA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "RexAB",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": PARMA,
            "snippet": (
                "The rexA and rexB genes of bacteriophage lambda encode "
                "a two-component system that aborts lytic growth of "
                "bacterial viruses."
            ),
            "notes": (
                "Parma et al. support RexA and RexB as a two-component "
                "Rex exclusion system."
            ),
        },
        {
            "reference": PARMA,
            "snippet": (
                "Rex exclusion is characterized by termination of "
                "macromolecular synthesis, loss of active transport, the "
                "hydrolysis of ATP, and cell death."
            ),
            "notes": (
                "Parma et al. support Rex exclusion as an "
                "abortive-infection-like output with host-cell death."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        rexa_hmm_inventory_evidence(),
        rexb_hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rexab_locus_mediates_rex_exclusion",
            "title": "RexAB loci mediate abortive Rex exclusion",
            "description": (
                "Conservative system-level sketch linking RexA/RexB "
                "locus possession to Rex exclusion and RexAB-system "
                "possession without asserting the direct phage trigger, "
                "RexA/RexB stoichiometry, membrane target, or "
                "bacteriophage-lambda self-protection route."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures RexAB as a named DefenseFinder "
                "two-profile abortive-infection system whose lambda "
                "prototype aborts lytic growth. It leaves the direct "
                "phage trigger, RexA/RexB molecular coupling, ion-channel "
                "activity, self-exclusion control, and phage escape "
                "routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rexab_locus",
                    "label": "RexAB locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A bacteriophage-lambda Rex-family abortive "
                        "exclusion locus represented by the DefenseFinder "
                        "RexAB__RexA and RexAB__RexB profiles."
                    ),
                },
                {
                    "node_id": "rex_exclusion",
                    "label": "Rex exclusion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive exclusion of sensitive bacteriophages "
                        "in cells carrying RexA and RexB."
                    ),
                },
                {
                    "node_id": "rexab_system_trait",
                    "label": "RexAB system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded RexAB "
                        "abortive-infection phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "rexab_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "rex_exclusion",
                    "description": (
                        "The bacteriophage-lambda RexA/RexB system aborts "
                        "lytic growth of bacterial viruses, and "
                        "DefenseFinder represents RexAB with required "
                        "RexA and RexB profiles."
                    ),
                    "evidence": [
                        {
                            "reference": PARMA,
                            "snippet": (
                                "The rexA and rexB genes of bacteriophage "
                                "lambda encode a two-component system that "
                                "aborts lytic growth of bacterial viruses."
                            ),
                            "notes": (
                                "Parma et al. support RexA and RexB as "
                                "the core genetic components of Rex "
                                "exclusion."
                            ),
                        },
                        rules_evidence(),
                        rexa_hmm_inventory_evidence(),
                        rexb_hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "rex_exclusion",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "rexab_system_trait",
                    "description": (
                        "RexA/RexB-dependent abortive exclusion realizes "
                        "the RexAB system trait."
                    ),
                    "evidence": [
                        {
                            "reference": PARMA,
                            "snippet": (
                                "Rex exclusion is characterized by "
                                "termination of macromolecular synthesis, "
                                "loss of active transport, the hydrolysis "
                                "of ATP, and cell death."
                            ),
                            "notes": (
                                "Parma et al. connect Rex exclusion to "
                                "host-cell shutdown and death."
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
            "discussion_id": "rexab-mechanism-gap",
            "prompt": (
                "Resolve the direct RexAB phage trigger, RexA and RexB "
                "molecular coupling, ion-channel activity, lambda "
                "self-exclusion control, and sensitive-phage escape "
                "routes before minting narrower RexAB mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Parma et al. support bacteriophage-lambda rexA and rexB "
                "as a two-component system that aborts lytic growth of "
                "bacterial viruses, and DefenseFinder maps RexAB to "
                "RexAB__RexA and RexAB__RexB profiles. The direct "
                "phage trigger, RexA/RexB molecular coupling, "
                "ion-channel output, lambda self-exclusion control, and "
                "sensitive-phage escape routes remain unresolved."
            ),
            "attaches_to": ["causal_graphs#rexab_locus_mediates_rex_exclusion"],
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
            "Minted RexAB system as a DOI-backed GENOMICS TraitRecord "
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
            "Reviewed canonical example evidence while minting RexAB "
            "system and left canonical_examples empty: the "
            "bacteriophage-lambda prototype supports a prophage-encoded "
            "rexA and rexB exclusion system and the pinned DefenseFinder "
            "registry maps a two-profile RexAB namespace, but the "
            "available curation sources do not identify a natural "
            "organism instance with a directly observed RexAB locus. No "
            "paid research was used."
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
            "RexAB system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
