"""Add the AbiO system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abio_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

PREVOTS_ABIO = "DOI:10.3168/jds.S0022-0302(98)75713-3"
FEMS_REVIEW = "DOI:10.1093/femsre/fuag009"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T18:34:41Z"
PARENT_TIMESTAMP = "2026-09-21T18:34:42Z"
IDENTIFIER = "traitmech:000342"
PROPOSAL = "proposals/metpo_traitmech_v219"

HMM_ROW = (
    "| AbiO__AbiO                                       | "
    "AbiO__AbiO                                       | AbiO                   | "
    "Custom                  | 50     |"
)
RULES_ROW = "AbiO\tAbiO\t1\t1\tAbiO__AbiO\t\t\t"

PARENT_EXPECTED_FRAGMENTS = (
    "AbiJ, AbiL, and AbiN are split out as ",
    "traitmech:000339, traitmech:000340, and traitmech:000341, respectively.",
    "Deng et al., and Prevots et al. still support",
    "single-gene lactococcal AbiN loci, and other families.",
)
PARENT_REPLACEMENTS = (
    (
        "AbiJ, AbiL, and AbiN are split out as ",
        "AbiJ, AbiL, AbiN, and AbiO are split out as ",
    ),
    (
        "traitmech:000339, traitmech:000340, and traitmech:000341, respectively.",
        (
            "traitmech:000339, traitmech:000340, traitmech:000341, "
            "and traitmech:000342, respectively."
        ),
    ),
    (
        "Deng et al., and Prevots et al. still support",
        "Deng et al., Prevots et al., and Prevots and Ritzenthaler still support",
    ),
    (
        "single-gene lactococcal AbiN loci, and other families.",
        (
            "single-gene lactococcal AbiN loci, single-profile "
            "lactococcal AbiO loci, and other families."
        ),
    ),
)
PARENT_APPLIED_FRAGMENTS = tuple(new for _, new in PARENT_REPLACEMENTS)
PARENT_CHANGES = (
    "Documented AbiO as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000342 for "
    "the AbiO system; other abortive-infection families remain open."
)


def prevots_abio_identity_evidence() -> dict[str, str]:
    return {
        "reference": PREVOTS_ABIO,
        "snippet": (
            "Complete Sequence of the New Lactococcal Abortive Phage "
            "Resistance Gene abiO"
        ),
        "notes": (
            "Crossref metadata verifies the Prevots and Ritzenthaler 1998 "
            "AbiO primary paper title and DOI."
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
            "The FEMS review lists AbiO among the confirmed lactococcal "
            "Abi-like systems in Table 1 and omits AbiO from the named two- "
            "and three-component exception lists."
        ),
    }


def fems_nuclease_prediction_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "the AbiO N-terminal domain resembles a restriction endonuclease "
            "type II-like domain-containing protein"
        ),
        "notes": (
            "The FEMS review summarizes a predicted nuclease-like AbiO "
            "N-terminal domain but does not establish the exact AbiO "
            "trigger or effector activity."
        ),
    }


def fems_helicase_prediction_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "Its C-terminal domain is predicted to encompass a superfamily "
            "1B (SF1B) helicase"
        ),
        "notes": (
            "The FEMS review summarizes a predicted SF1B helicase-like AbiO "
            "C-terminal domain without resolving how AbiO arrests infected "
            "cells."
        ),
    }


def fems_toxicity_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "AbiO was previously shown to be toxic in Lactococcus when its "
            "encoding gene was cloned in a high-copy number vector"
        ),
        "notes": (
            "The FEMS review treats AbiO overexpression toxicity as support "
            "for its abortive-infection phenotype."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiO | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiO model "
            "namespace to the Chopin et al. lactococcal "
            "abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_ROW,
        "notes": (
            "The DefenseFinder rules table models AbiO as a one-component "
            "system requiring the AbiO__AbiO profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiO__AbiO under the "
            "AbiO model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiO system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "single-component AbiO-family locus represented by DefenseFinder as "
        "a mandatory AbiO__AbiO profile."
    ),
    "definition_source": PREVOTS_ABIO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiO",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "AbiO__AbiO",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        prevots_abio_identity_evidence(),
        fems_single_gene_evidence(),
        fems_nuclease_prediction_evidence(),
        fems_helicase_prediction_evidence(),
        fems_toxicity_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "abio_locus_restricts_lactococcal_phage",
            "title": "AbiO loci confer abortive-infection phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "DefenseFinder AbiO locus to restricted bacteriophage "
                "propagation without asserting the unresolved phage trigger, "
                "predicted nuclease activity, or predicted helicase activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiO as a named single-profile "
                "lactococcal Abi-like system with the DefenseFinder "
                "AbiO__AbiO HMM while leaving its direct phage trigger, "
                "restriction-endonuclease interpretation, helicase "
                "interpretation, exact molecular activity, phage escape "
                "routes, and growth-arrest or cell-death route unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abio_locus",
                    "label": "AbiO locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AbiO-family abortive-infection locus represented "
                        "by the DefenseFinder AbiO__AbiO profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage propagation in cells carrying "
                        "an AbiO-family abortive-infection system."
                    ),
                },
                {
                    "node_id": "abio_system_trait",
                    "label": "AbiO system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiO "
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
                    "subject": "abio_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The DefenseFinder AbiO namespace is modeled as a "
                        "one-profile AbiO__AbiO system."
                    ),
                    "evidence": [rules_evidence(), hmm_inventory_evidence()],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abio_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the AbiO "
                        "abortive-infection system possession trait."
                    ),
                    "evidence": [
                        prevots_abio_identity_evidence(),
                        fems_toxicity_evidence(),
                    ],
                },
                {
                    "subject": "abio_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiO system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        prevots_abio_identity_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abio-trigger-and-effector-gap",
            "prompt": (
                "Resolve the AbiO phage trigger, restriction-endonuclease "
                "and helicase activity, and growth-arrest or cell-death "
                "route before minting narrower AbiO mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Prevots and Ritzenthaler support AbiO as a lactococcal "
                "abortive phage resistance gene, the FEMS review retains "
                "AbiO among confirmed lactococcal Abi-like systems, and "
                "DefenseFinder represents AbiO with a mandatory AbiO__AbiO "
                "profile. The FEMS table leaves the AbiO effect on the "
                "cell and phage escape proteins unknown for the tested "
                "phages, and the FEMS structural discussion predicts "
                "restriction-endonuclease-like and SF1B-helicase-like "
                "domains while not resolving the molecular trigger or "
                "effector activity. This first system-level record "
                "therefore leaves the direct phage trigger, exact "
                "molecular activity, growth-arrest or cell-death route, "
                "and phage escape routes unresolved."
            ),
            "evidence": [
                fems_nuclease_prediction_evidence(),
                fems_helicase_prediction_evidence(),
                fems_toxicity_evidence(),
                rules_evidence(),
                hmm_inventory_evidence(),
            ],
            "attaches_to": ["causal_graphs#abio_locus_restricts_lactococcal_phage"],
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
    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    if all(applied in discussion["rationale"] for applied in PARENT_APPLIED_FRAGMENTS):
        return record

    for expected in PARENT_EXPECTED_FRAGMENTS:
        assert expected in discussion["rationale"]
    assert IDENTIFIER not in discussion["rationale"]

    for old, new in PARENT_REPLACEMENTS:
        discussion["rationale"] = discussion["rationale"].replace(old, new, 1)

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
            "Minted AbiO system as a DOI-backed GENOMICS TraitRecord "
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
            "AbiO system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
