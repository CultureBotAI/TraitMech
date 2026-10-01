#!/usr/bin/env python3
"""Add the Dag system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dag_system.yaml"

GETZ = "DOI:10.1038/s41564-026-02441-0"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T05:07:00Z"
CANONICAL_TIMESTAMP = "2026-10-01T05:07:01Z"
IDENTIFIER = "traitmech:000507"
PHAGE_DEFENSE_PARENT_ID = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v384"

ARTICLE_ROW = (
    "| Dag | 10\\.1101/2025\\.10\\.29\\.685425 | Antiviral defence is a "
    "conserved function of diverse DNA glycosylases | "
)


def dag_family_evidence() -> dict[str, str]:
    return {
        "reference": GETZ,
        "snippet": (
            "using structure-guided discovery, we identified two widespread "
            "families of anti-phage DNA glycosylases, Dag1 and Dag2"
        ),
        "notes": (
            "Getz et al. identify Dag1 and Dag2 as widespread anti-phage "
            "DNA-glycosylase families."
        ),
    }


def dag_guanine_target_evidence() -> dict[str, str]:
    return {
        "reference": GETZ,
        "snippet": (
            "Dag1 and Dag2 act as antiviral effectors that selectively target "
            "phages carrying modified guanine bases."
        ),
        "notes": (
            "Getz et al. support the modified-guanine phage targeting scope "
            "of the Dag1 and Dag2 antiviral effectors."
        ),
    }


def dag_glycosylase_immunity_evidence() -> dict[str, str]:
    return {
        "reference": GETZ,
        "snippet": (
            "Together, these findings establish DNA glycosylases as a "
            "versatile class of bacterial immune proteins"
        ),
        "notes": (
            "Getz et al. frame defense-associated DNA glycosylases as "
            "bacterial immune proteins."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the Dag source "
            "key to the Getz et al. DNA-glycosylase antiviral defense paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact Dag row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact Dag system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Dag system",
    "definition": (
        "A phage defense system in which an organism possesses a Dag-family "
        "DNA-glycosylase system whose Dag1 or Dag2 effectors selectively "
        "target phages carrying modified guanine bases."
    ),
    "definition_source": GETZ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Dag",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Dag1",
            "synonym_type": "RELATED_SYNONYM",
            "source": GETZ,
        },
        {
            "synonym_text": "Dag2",
            "synonym_type": "RELATED_SYNONYM",
            "source": GETZ,
        },
    ],
    "evidence": [
        dag_family_evidence(),
        dag_guanine_target_evidence(),
        dag_glycosylase_immunity_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "dag_effectors_target_modified_guanine_phages",
            "title": "Dag effectors target modified-guanine phages",
            "description": (
                "Conservative system-level sketch linking the Dag "
                "DefenseFinder namespace to Dag1 and Dag2 antiviral "
                "effector activity and the Dag phage-defense-system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Dag as a named DefenseFinder "
                "DNA-glycosylase phage-defense system at system level and "
                "deliberately defers a protein-resolved glycosylase "
                "mechanism. Getz et al. support Dag1 and Dag2 as "
                "anti-phage DNA glycosylase families that target "
                "modified-guanine phages, but exact natural host "
                "exemplars, accession-level Dag proteins, relationships "
                "between Dag1 and Dag2 families, and DefenseFinder HMM/rules "
                "profiles are unresolved."
            ),
            "nodes": [
                {
                    "node_id": "dag_locus",
                    "label": "Dag locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Dag-family DNA-glycosylase phage-defense locus "
                        "represented by the DefenseFinder Dag article "
                        "namespace."
                    ),
                },
                {
                    "node_id": "modified_guanine_phage_targeting",
                    "label": "modified-guanine phage targeting",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Selective targeting of phages that carry modified "
                        "guanine bases by Dag1 or Dag2 antiviral effectors."
                    ),
                },
                {
                    "node_id": "dag_system_trait",
                    "label": "Dag system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Dag DNA-glycosylase "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system_trait",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PHAGE_DEFENSE_PARENT_ID,
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "dag_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "modified_guanine_phage_targeting",
                    "description": (
                        "Dag-family DNA-glycosylase systems encode Dag1 or "
                        "Dag2 antiviral effectors that selectively target "
                        "modified-guanine phages."
                    ),
                    "evidence": [
                        dag_family_evidence(),
                        dag_guanine_target_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "modified_guanine_phage_targeting",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "dag_system_trait",
                    "description": (
                        "Modified-guanine phage targeting realizes the "
                        "organism-level Dag system possession trait."
                    ),
                    "evidence": [
                        dag_guanine_target_evidence(),
                        dag_glycosylase_immunity_evidence(),
                    ],
                },
                {
                    "subject": "dag_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system_trait",
                    "description": (
                        "Dag system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        dag_family_evidence(),
                        dag_glycosylase_immunity_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "dag-defensefinder-profile-gap",
            "prompt": (
                "Resolve exact Dag1 and Dag2 family boundaries, natural host "
                "exemplars, modified-guanine phage target breadth, and "
                "DefenseFinder HMM/rules coverage before minting narrower "
                "Dag mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Getz et al. support Dag1 and Dag2 as widespread families of "
                "anti-phage DNA glycosylases that selectively target phages "
                "carrying modified guanine bases, and the pinned "
                "DefenseFinder article registry maps the Dag key to the "
                "Getz et al. preprint DOI. The pinned HMM inventory and "
                "rules table have no exact Dag rows. This first-pass record "
                "therefore does not resolve exact Dag1 versus Dag2 family "
                "boundaries, natural host exemplars, accession-level Dag "
                "proteins, full modified-guanine phage target breadth, or a "
                "reusable DefenseFinder profile model."
            ),
            "evidence": [
                dag_family_evidence(),
                dag_guanine_target_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#dag_effectors_target_modified_guanine_phages"],
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
        }
    ],
}


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Dag system as a DOI- and DefenseFinder-backed GENOMICS "
            "TraitRecord under the phage defense system parent after an "
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
            "Reviewed Dag system during initial curation and left "
            "canonical_examples empty because the accessible Getz et al. "
            "abstract supports Dag1 and Dag2 as widespread anti-phage "
            "DNA-glycosylase families but does not name a stable NCBITaxon "
            "strain exemplar for the organism-level Dag system trait. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    validate_outputs(record)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
    else:
        print(
            "Dag system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
