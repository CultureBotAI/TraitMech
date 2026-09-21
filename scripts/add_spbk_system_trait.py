"""Add the SpbK system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "spbk_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

JOHNSON = "DOI:10.1371/journal.pgen.1010065"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T03:22:00Z"
PARENT_TIMESTAMP = "2026-09-21T03:22:01Z"
IDENTIFIER = "traitmech:000325"
PROPOSAL = "proposals/metpo_traitmech_v202"

SPBK_HMM_ROW = (
    "| SpbK__SpbK                                       | "
    "SpbK__SpbK                                       | SpbK                   | "
    "Custom                  | 80     |"
)

OLD_PARENT_RATIONALE = (
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
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, AbiD, AbiB, AbiC, AbiU, AbiAlpha, Pif, RexAB, and "
    "SpbK are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, traitmech:000304, traitmech:000306, "
    "traitmech:000316, traitmech:000317, traitmech:000318, "
    "traitmech:000319, traitmech:000320, traitmech:000321, "
    "traitmech:000322, traitmech:000323, traitmech:000324, and "
    "traitmech:000325, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., Depardieu et al., Prevots et al., "
    "O'Connor et al., Su et al., Twomey et al., McLandsborough et al., "
    "Parreira et al., Durmaz et al., Dai et al., Lossouarn et al., "
    "Cram et al., Parma et al., and Johnson et al. still support "
    "abortive infection as a genomically encoded phage defense strategy "
    "that spans mechanistically diverse toxin-antitoxin, premature-lysis, "
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
    "abortive SPß defense, and other families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's "
    "trigger, effector, growth-arrest or cell-death mechanism, and "
    "phage escape routes."
)
PARENT_CHANGES = (
    "Documented SpbK as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000325 for "
    "the SpbK system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "SpbK | 10\\.1371/journal\\.pgen\\.1010065 | "
            "Interactions between mobile genetic elements: An "
            "anti-phage gene in an integrative and conjugative element "
            "protects host cells from predation by a temperate "
            "bacteriophage"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named SpbK model "
            "namespace to the ICEBs1 SpbK anti-phage paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "SpbK\tSpbK\t1\t1\tSpbK__SpbK",
        "notes": (
            "The DefenseFinder rules table models SpbK as a single-profile "
            "system requiring the SpbK__SpbK profile."
        ),
    }


def spbk_hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": SPBK_HMM_ROW,
        "notes": "The DefenseFinder HMM inventory records SpbK__SpbK under SpbK.",
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "SpbK system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "SpbK-family locus represented by the DefenseFinder SpbK__SpbK "
        "profile and exemplified by the ICEBs1 spbK gene whose "
        "SPß-YonE-dependent activity inhibits SPß production and kills "
        "infected cells."
    ),
    "definition_source": JOHNSON,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "SpbK",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": JOHNSON,
            "snippet": (
                "The ICEBs1 gene spbK, although dispensable for conjugation, "
                "was necessary and sufficient for the inhibition of SPß."
            ),
            "notes": (
                "Johnson et al. support spbK as the ICEBs1 locus sufficient "
                "for SPß inhibition."
            ),
        },
        {
            "reference": JOHNSON,
            "snippet": (
                "The anti-SPß phenotype (abortive infection) caused by spbK "
                "was dependent on the SPß gene yonE."
            ),
            "notes": (
                "Johnson et al. support yonE-dependent abortive infection "
                "as the phage-specific SpbK output."
            ),
        },
        {
            "reference": JOHNSON,
            "snippet": (
                "Co-expression of spbK and yonE inhibited host cell growth "
                "and caused a drop in cell viability, even in the absence "
                "of any other ICEBs1 or SPß genes."
            ),
            "notes": (
                "Johnson et al. support SpbK/YonE-associated host growth "
                "inhibition and cell death."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        spbk_hmm_inventory_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1423",
            "taxon_label": "Bacillus subtilis",
            "note": (
                "Johnson et al. showed that ICEBs1 encodes an SpbK-dependent "
                "abortive infection system that protects B. subtilis host "
                "populations from SPß."
            ),
            "reference": JOHNSON,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "spbk_locus_mediates_spb_defense",
            "title": "SpbK loci mediate SPß abortive defense",
            "description": (
                "Conservative system-level sketch linking SpbK-family locus "
                "possession to SPß YonE-dependent abortive infection and the "
                "SpbK system trait without asserting the direct SpbK-YonE "
                "coupling event or TIR-domain effector chemistry."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SpbK as a named DefenseFinder single-profile "
                "abortive-infection system whose Bacillus ICEBs1 prototype "
                "requires the SPß YonE trigger. It leaves the direct SpbK-YonE "
                "coupling, TIR-domain output, essential host target, and "
                "homolog breadth unresolved."
            ),
            "nodes": [
                {
                    "node_id": "spbk_locus",
                    "label": "SpbK locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An ICEBs1-like abortive-infection locus represented by "
                        "the DefenseFinder SpbK__SpbK profile."
                    ),
                },
                {
                    "node_id": "spbk_yone_abortive_infection",
                    "label": "SpbK/YonE-dependent abortive infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive infection in which SpbK activity depends on "
                        "the SPß YonE gene and causes host growth inhibition "
                        "and cell death."
                    ),
                },
                {
                    "node_id": "spbk_system_trait",
                    "label": "SpbK system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded SpbK abortive-infection "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "spbk_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "spbk_yone_abortive_infection",
                    "description": (
                        "The ICEBs1 spbK locus is necessary and sufficient for "
                        "YonE-dependent SPß abortive infection, and DefenseFinder "
                        "represents SpbK with a required SpbK profile."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON,
                            "snippet": (
                                "The ICEBs1 gene spbK, although dispensable for "
                                "conjugation, was necessary and sufficient for "
                                "the inhibition of SPß."
                            ),
                            "notes": (
                                "Johnson et al. connect the ICEBs1 spbK gene to "
                                "SPß inhibition."
                            ),
                        },
                        {
                            "reference": JOHNSON,
                            "snippet": (
                                "The anti-SPß phenotype (abortive infection) "
                                "caused by spbK was dependent on the SPß gene "
                                "yonE."
                            ),
                            "notes": (
                                "Johnson et al. support YonE dependence of "
                                "SpbK-mediated abortive infection."
                            ),
                        },
                        rules_evidence(),
                        spbk_hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "spbk_yone_abortive_infection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "spbk_system_trait",
                    "description": (
                        "SpbK/YonE-dependent abortive infection realizes the "
                        "SpbK system trait."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON,
                            "snippet": (
                                "Whatever the mechanism, we conclude that "
                                "ICEBs1 encodes an abortive infection system "
                                "that protects its host from predation by SPß."
                            ),
                            "notes": (
                                "Johnson et al. classify ICEBs1 spbK activity as "
                                "an abortive infection system that protects its "
                                "host from SPß predation."
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
            "discussion_id": "spbk-mechanism-gap",
            "prompt": (
                "Resolve the direct SPß YonE trigger, SpbK TIR-domain output, "
                "essential host target, and broader SpbK homolog scope before "
                "minting narrower SpbK mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Johnson et al. support ICEBs1 spbK as a YonE-dependent "
                "abortive infection gene that inhibits SPß and causes cell "
                "death, and DefenseFinder maps SpbK to the SpbK__SpbK profile. "
                "The direct SpbK-YonE coupling event, TIR-domain output, "
                "essential host target, and homolog breadth remain unresolved."
            ),
            "attaches_to": ["causal_graphs#spbk_locus_mediates_spb_defense"],
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
            "Minted SpbK system as a DOI-backed GENOMICS TraitRecord "
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
            "SpbK system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
