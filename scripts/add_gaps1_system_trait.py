#!/usr/bin/env python3
"""Add the GAPS1 system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gaps1_system.yaml"

MAHATA = "DOI:10.1038/s41564-024-01840-5"
MAHATA_PREPRINT = "DOI:10.1101/2023.03.28.534373"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-25T04:19:09Z"
POSED_DATE = "2026-09-24"
IDENTIFIER = "traitmech:000371"
PROPOSAL = "proposals/metpo_traitmech_v248"

GMT_CARGO_SNIPPET = (
    "GMT islands' cargoes contain various anti-phage defence systems"
)
GAPS1_DORMANCY_SNIPPET = (
    "We reveal four anti-phage defence systems encoded within GMT islands "
    "and further characterize one system, GAPS1, showing it is triggered "
    "by a phage capsid protein to induce cell dormancy"
)
PREPRINT_TITLE_SNIPPET = (
    "Gamma-Mobile-Trio systems define a new class of mobile elements rich "
    "in bacterial defensive and offensive tools"
)
ARTICLE_REGISTRY_SNIPPET = (
    "GAPS1 | 10\\.1101/2023\\.03\\.28\\.534373 | Gamma-Mobile-Trio systems "
    "define a new class of mobile elements rich in bacterial defensive and "
    "offensive tools"
)
RULES_SNIPPET = "GAPS1\tGAPS1\t1\t1\tGAPS1__GAPS1\t\t\t"
GAPS1_HMM_PROFILE = "GAPS1__GAPS1"
GAPS1_HMM_GA_CUT = "100"


def mahata_gmt_cargo_evidence() -> dict[str, str]:
    return {
        "reference": MAHATA,
        "snippet": GMT_CARGO_SNIPPET,
        "notes": (
            "Mahata et al. identify GMT islands as carriers of anti-phage "
            "defense-system cargo."
        ),
    }


def mahata_gaps1_dormancy_evidence() -> dict[str, str]:
    return {
        "reference": MAHATA,
        "snippet": GAPS1_DORMANCY_SNIPPET,
        "notes": (
            "Mahata et al. identify GAPS1 as one of four GMT-island "
            "anti-phage defense systems and connect GAPS1 activation to "
            "phage-capsid-protein-triggered cell dormancy."
        ),
    }


def mahata_preprint_evidence() -> dict[str, str]:
    return {
        "reference": MAHATA_PREPRINT,
        "snippet": PREPRINT_TITLE_SNIPPET,
        "notes": (
            "The bioRxiv version of Mahata et al. is the DOI cited in "
            "DefenseFinder's GAPS1 article-registry row."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named GAPS1 system "
            "to the Mahata et al. preprint."
        ),
    }


def defensefinder_rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models GAPS1 as a single-profile "
            "system requiring GAPS1__GAPS1."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            f"| {GAPS1_HMM_PROFILE:<49}| {GAPS1_HMM_PROFILE:<49}| "
            f"{'GAPS1':<23}| {'Custom':<24}| {GAPS1_HMM_GA_CUT:<7}|"
        ),
        "notes": (
            "The DefenseFinder HMM inventory records GAPS1__GAPS1 under the "
            "GAPS1 model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "GAPS1 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "Gamma-Mobile-Trio island-associated GAPS1 locus that can be "
        "triggered by a phage capsid protein to induce cell dormancy."
    ),
    "definition_source": MAHATA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "GAPS1",
            "synonym_type": "EXACT_SYNONYM",
            "source": MAHATA,
        },
        {
            "synonym_text": GAPS1_HMM_PROFILE,
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        mahata_gmt_cargo_evidence(),
        mahata_gaps1_dormancy_evidence(),
        mahata_preprint_evidence(),
        article_registry_evidence(),
        defensefinder_rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "gaps1_capsid_triggered_dormancy",
            "title": "GAPS1 loci induce cell dormancy during phage defense",
            "description": (
                "Conservative system-level sketch connecting the named "
                "GAPS1 locus model and the phage-capsid-protein-triggered "
                "dormancy phenotype to the GAPS1 system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures GAPS1 as a named GMT-island anti-phage "
                "defense system represented in DefenseFinder by a single "
                "GAPS1__GAPS1 profile while leaving its universal host range, "
                "the molecular activity of the GAPS1 component, the exact "
                "capsid-protein trigger, and sibling GAPS2 or GAPS6 systems "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gaps1_locus",
                    "label": "GAPS1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A GMT-island-associated GAPS1 phage-defense locus "
                        "represented by the custom DefenseFinder "
                        "GAPS1__GAPS1 profile."
                    ),
                },
                {
                    "node_id": "gaps1_cell_dormancy",
                    "label": "GAPS1-induced cell dormancy",
                    "node_type": "STATE",
                    "description": (
                        "Cellular dormancy induced by a GAPS1 system after "
                        "recognition of a phage capsid-protein trigger."
                    ),
                },
                {
                    "node_id": "gaps1_system_trait",
                    "label": "GAPS1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded GAPS1 phage-defense "
                        "system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "gaps1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gaps1_system_trait",
                    "description": (
                        "DefenseFinder records GAPS1 as a named system and "
                        "models it as a single-profile GAPS1__GAPS1 rule."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        defensefinder_rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "gaps1_cell_dormancy",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "gaps1_system_trait",
                    "description": (
                        "Phage-capsid-protein-triggered cell dormancy is the "
                        "characterized output that realizes the GAPS1 system "
                        "trait."
                    ),
                    "evidence": [mahata_gaps1_dormancy_evidence()],
                },
                {
                    "subject": "gaps1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "GAPS1 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        mahata_gaps1_dormancy_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "gaps1-trigger-sibling-gap",
            "prompt": (
                "Resolve GAPS1 component activity, natural-host exemplars, "
                "and GAPS2/GAPS6 boundaries before minting narrower "
                "GAPS traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Mahata et al. support GAPS1 as one GMT-island anti-phage "
                "defense system triggered by a phage capsid protein to induce "
                "cell dormancy, and DefenseFinder represents GAPS1 as one "
                "GAPS1__GAPS1 profile. This first system-level record does "
                "not assert the GAPS1 component's molecular activity, the "
                "capsid trigger identity, a universal GAPS1 host range, or "
                "sibling GAPS2 or GAPS6 system boundaries."
            ),
            "evidence": [
                mahata_gaps1_dormancy_evidence(),
                defensefinder_rules_evidence(),
            ],
            "attaches_to": ["causal_graphs#gaps1_capsid_triggered_dormancy"],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        }
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted GAPS1 system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            f"proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        curator=CURATOR,
        timestamp=TIMESTAMP,
        llm_assisted=True,
    )
    record_curation_event(
        record,
        action="UPDATED_DISCUSSION",
        changes=(
            "Resolved GitHub issue #1274 by narrowing stale GAPS1 "
            "sibling-boundary references to GAPS2/GAPS6 after GAPS4 was "
            "split into its own TraitRecord."
        ),
        curator=CURATOR,
        timestamp="2026-09-26T11:02:35Z",
        llm_assisted=True,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
