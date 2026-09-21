"""Add the AbiA system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abia_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DINSMORE_COPY = "DOI:10.1128/aem.60.4.1129-1136.1994"
DINSMORE_COPY_PMID = "PMID:16349225"
DINSMORE_REPEAT_PMID = "PMID:9661658"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T20:16:02Z"
REVIEW_TIMESTAMP = "2026-09-21T20:44:00Z"
PARENT_TIMESTAMP = "2026-09-21T20:16:03Z"
IDENTIFIER = "traitmech:000344"
PROPOSAL = "proposals/metpo_traitmech_v221"

ABI_A_LARGE_ROW = "| AbiA_large__AbiA_large                           | AbiA_large__AbiA_large                           | AbiA_large             | Custom                  | 250    |"
ABI_A_SMALL_SLATT_ROW = "| AbiA_small__AbiA_SLATT                           | AbiA_small__AbiA_SLATT                           | AbiA_small             | Custom                  | 20     |"
ABI_A_SMALL_ROW = "| AbiA_small__AbiA_small                           | AbiA_small__AbiA_small                           | AbiA_small             | Custom                  | 300    |"
ABI_A_SLATT_ROW = "| AbiA_small__SLATT                                |                                                  | AbiA_small             | Custom                  | 40     |"

PARENT_EXPECTED_FRAGMENTS = (
    "AbiL, AbiN, AbiO, and AbiP2 are split out as ",
    (
        "traitmech:000340, traitmech:000341, traitmech:000342, "
        "and traitmech:000343, respectively."
    ),
    "and Odegrip et al. still support abortive infection",
    (
        "single-profile coliphage AbiP2 reverse-transcriptase-like "
        "loci, and other families."
    ),
)
PARENT_REPLACEMENTS = (
    (
        "AbiL, AbiN, AbiO, and AbiP2 are split out as ",
        "AbiL, AbiN, AbiO, AbiP2, and AbiA are split out as ",
    ),
    (
        (
            "traitmech:000340, traitmech:000341, traitmech:000342, "
            "and traitmech:000343, respectively."
        ),
        (
            "traitmech:000340, traitmech:000341, traitmech:000342, "
            "traitmech:000343, and traitmech:000344, respectively."
        ),
    ),
    (
        "and Odegrip et al. still support abortive infection",
        (
            "Odegrip et al., Dinsmore and Klaenhammer, and Dinsmore et "
            "al. still support abortive infection"
        ),
    ),
    (
        (
            "single-profile coliphage AbiP2 reverse-transcriptase-like "
            "loci, and other families."
        ),
        (
            "single-profile coliphage AbiP2 reverse-transcriptase-like "
            "loci, lactococcal AbiA loci represented by DefenseFinder "
            "AbiA-large and AbiA-small subrules, and other families."
        ),
    ),
)
PARENT_APPLIED_FRAGMENTS = (
    "traitmech:000343, and traitmech:000344, respectively.",
    "AbiA-large and AbiA-small subrules",
)
PARENT_CHANGES = (
    "Documented AbiA as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000344 for "
    "the AbiA system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiA | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | "
            "Phage abortive infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiA model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def large_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiA\tAbiA_large\t1\t1\tAbiA_large__AbiA_large",
        "notes": (
            "The DefenseFinder rules table models one AbiA subrule as the "
            "single-profile AbiA_large subsystem."
        ),
    }


def small_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": (
            "AbiA\tAbiA_small\t2\t2\tAbiA_small__AbiA_SLATT, "
            "AbiA_small__AbiA_small"
        ),
        "notes": (
            "The DefenseFinder rules table models one AbiA subrule as a "
            "two-profile AbiA_small subsystem."
        ),
    }


def large_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ABI_A_LARGE_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiA_large__AbiA_large "
            "under the AbiA_large model namespace."
        ),
    }


def small_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ABI_A_SMALL_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiA_small__AbiA_small "
            "under the AbiA_small model namespace."
        ),
    }


def copy_number_evidence() -> dict[str, str]:
    return {
        "reference": DINSMORE_COPY_PMID,
        "snippet": (
            "The abiA gene (formerly hsp) encodes an abortive phage "
            "infection mechanism which inhibits phage DNA replication."
        ),
        "notes": (
            "Dinsmore and Klaenhammer describe abiA as the former hsp "
            "abortive-infection determinant and connect AbiA activity to "
            "inhibition of phage DNA replication."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiA system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "AbiA-family locus whose copy number or expression modulates "
        "Lactococcus lactis resistance to multiple phages and that "
        "DefenseFinder represents with AbiA_large or AbiA_small model "
        "subrules."
    ),
    "definition_source": DINSMORE_COPY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiA",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "AbiA_large",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "AbiA_small",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "hsp",
            "synonym_type": "RELATED_SYNONYM",
            "source": DINSMORE_COPY,
        },
    ],
    "evidence": [
        copy_number_evidence(),
        {
            "reference": DINSMORE_COPY_PMID,
            "snippet": (
                "Three abiA-containing plasmids of various copy numbers "
                "were introduced into both strains, and the recombinants "
                "were evaluated for resistance to phages c2, p2, sk1, "
                "and phi31."
            ),
            "notes": (
                "Dinsmore and Klaenhammer tested AbiA across two "
                "Lactococcus lactis strains and four lactococcal phages."
            ),
        },
        {
            "reference": DINSMORE_COPY_PMID,
            "snippet": (
                "Altering the gene dosage or expression level of abiA "
                "significantly affects the phage resistance levels."
            ),
            "notes": (
                "Dinsmore and Klaenhammer show that AbiA dosage or "
                "expression modulates the strength of lactococcal phage "
                "resistance."
            ),
        },
        {
            "reference": DINSMORE_REPEAT_PMID,
            "snippet": (
                "The abiA gene encodes an abortive bacteriophage "
                "infection mechanism that can protect Lactococcus species "
                "from infection by a variety of bacteriophages including "
                "three unrelated phage species."
            ),
            "notes": (
                "Dinsmore and Klaenhammer support AbiA as a broad "
                "lactococcal abortive-infection mechanism."
            ),
        },
        {
            "reference": DINSMORE_REPEAT_PMID,
            "snippet": (
                "the leucine repeat structure is essential for conferring "
                "phage resistance against three species of lactococcal "
                "bacteriophages."
            ),
            "notes": (
                "Dinsmore and Klaenhammer connect residues in AbiA's "
                "leucine-repeat region to resistance against c2, sk1, and "
                "phi31."
            ),
        },
        article_registry_evidence(),
        large_rules_evidence(),
        small_rules_evidence(),
        large_hmm_evidence(),
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": ABI_A_SMALL_SLATT_ROW,
            "notes": (
                "The DefenseFinder HMM inventory records AbiA_small__AbiA_SLATT "
                "under the AbiA_small model namespace."
            ),
        },
        small_hmm_evidence(),
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": ABI_A_SLATT_ROW,
            "notes": (
                "The DefenseFinder HMM inventory also records AbiA_small__SLATT "
                "under the AbiA_small model namespace."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Dinsmore and Klaenhammer varied abiA copy number in "
                "Lactococcus lactis MG1363 and NCK203 and assayed "
                "resistance to phages c2, p2, sk1, and phi31."
            ),
            "reference": DINSMORE_COPY,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abia_locus_inhibits_phage_dna_replication",
            "title": "AbiA activity inhibits lactococcal phage DNA replication",
            "description": (
                "Conservative system-level sketch linking an AbiA-family "
                "locus to phage-DNA-replication inhibition, reduced "
                "lactococcal phage propagation, and AbiA-system possession "
                "without asserting the unresolved direct phage trigger or "
                "molecular target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiA as a named DefenseFinder "
                "abortive-infection system with AbiA_large and AbiA_small "
                "subrules. It leaves the direct phage trigger, the natural "
                "boundaries of the DefenseFinder subrules, the molecular "
                "effector activity, the DNA-replication target, and phage "
                "escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abia_locus",
                    "label": "AbiA locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AbiA-family abortive-infection locus represented "
                        "by the DefenseFinder AbiA_large or AbiA_small "
                        "subrules."
                    ),
                },
                {
                    "node_id": "phage_dna_replication_inhibition",
                    "label": "phage DNA replication inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Inhibition of bacteriophage DNA replication in "
                        "AbiA-containing Lactococcus lactis."
                    ),
                },
                {
                    "node_id": "reduced_lactococcal_phage_propagation",
                    "label": "reduced lactococcal phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of lactococcal phages in "
                        "cells carrying an AbiA-family abortive-infection "
                        "system."
                    ),
                },
                {
                    "node_id": "abia_system_trait",
                    "label": "AbiA system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiA "
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
                    "subject": "abia_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_dna_replication_inhibition",
                    "description": (
                        "AbiA activity inhibits phage DNA replication, and "
                        "DefenseFinder represents AbiA with AbiA_large and "
                        "AbiA_small model subrules."
                    ),
                    "evidence": [
                        copy_number_evidence(),
                        large_rules_evidence(),
                        small_rules_evidence(),
                        large_hmm_evidence(),
                        small_hmm_evidence(),
                    ],
                },
                {
                    "subject": "abia_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "reduced_lactococcal_phage_propagation",
                    "description": (
                        "Changing abiA dosage or expression changes "
                        "Lactococcus lactis resistance to c2, p2, sk1, "
                        "and phi31."
                    ),
                    "evidence": [
                        {
                            "reference": DINSMORE_COPY_PMID,
                            "snippet": (
                                "Altering the gene dosage or expression "
                                "level of abiA significantly affects the "
                                "phage resistance levels."
                            ),
                            "notes": (
                                "Dinsmore and Klaenhammer connected abiA "
                                "dosage and expression to lactococcal phage "
                                "resistance level."
                            ),
                        }
                    ],
                },
                {
                    "subject": "reduced_lactococcal_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abia_system_trait",
                    "description": (
                        "AbiA-mediated reduction of lactococcal phage "
                        "propagation realizes the AbiA system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DINSMORE_REPEAT_PMID,
                            "snippet": (
                                "can protect Lactococcus species from "
                                "infection by a variety of bacteriophages "
                                "including three unrelated phage species"
                            ),
                            "notes": (
                                "Dinsmore and Klaenhammer describe the "
                                "AbiA system as protecting Lactococcus "
                                "from multiple phage species."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abia_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiA system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        copy_number_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abia-defensefinder-subrule-gap",
            "prompt": (
                "Resolve the AbiA_large and AbiA_small system boundaries, "
                "phage trigger, direct DNA-replication target, and molecular "
                "effector output before minting narrower AbiA mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Dinsmore and Klaenhammer support AbiA as a lactococcal "
                "abortive-infection determinant whose copy number or "
                "expression changes phage resistance and whose leucine-repeat "
                "region is required for activity against multiple phage "
                "species. DefenseFinder models AbiA through AbiA_large and "
                "AbiA_small subrules, but this first system-level record "
                "leaves those subrules' natural locus boundaries, the direct "
                "phage trigger, the molecular effector output, the exact "
                "phage-DNA-replication target, and phage escape routes "
                "unresolved."
            ),
            "evidence": [
                copy_number_evidence(),
                {
                    "reference": DINSMORE_REPEAT_PMID,
                    "snippet": (
                        "the leucine repeat structure is essential for "
                        "conferring phage resistance against three species "
                        "of lactococcal bacteriophages."
                    ),
                    "notes": (
                        "Dinsmore and Klaenhammer identify an AbiA "
                        "leucine-repeat region needed for phage resistance."
                    ),
                },
                large_rules_evidence(),
                small_rules_evidence(),
                large_hmm_evidence(),
                small_hmm_evidence(),
            ],
            "attaches_to": ["causal_graphs#abia_locus_inhibits_phage_dna_replication"],
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
            "Minted AbiA system as a DOI-backed GENOMICS TraitRecord "
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
        action="ADDRESS_PR_REVIEW",
        changes=(
            "Addressed PR #1218 review issues #1219 and #1220 by "
            "aligning the v221 METPO ROBOT TSV definition with this "
            "TraitRecord and moving the AbiA dosage and expression "
            "evidence onto a direct AbiA locus edge."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
    )
    return record


def assert_same_target(record: dict[str, Any]) -> None:
    assert record["identifier"] == IDENTIFIER
    assert record["label"] == "AbiA system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000214"]


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
            assert_same_target(load_trait(TARGET))
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "AbiA system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
