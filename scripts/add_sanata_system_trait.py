#!/usr/bin/env python3
"""Add the SanaTA system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sanata_system.yaml"

SBERRO = "DOI:10.1016/j.molcel.2013.02.002"
SBERRO_PMID = "PMID:23478446"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-25T06:02:46Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-25T06:20:44Z"
IDENTIFIER = "traitmech:000373"
PROPOSAL = "proposals/metpo_traitmech_v250"
SLUG = "sanata"

TA_VALIDATION_SNIPPET = (
    "In all six tested pairs, induction of toxin expression inhibited "
    "bacterial growth, while co-induction of the toxin and antitoxin "
    "resulted in bacterial survival"
)
T7_RESISTANCE_SNIPPET = (
    "One of the tested systems, sanaTA, was found to provide E. coli "
    "with resistance against T7Δ4.5 and T7Δ4.3Δ4.5Δ4.7, reducing "
    "sensitivity to these phage strains by about 3 orders of magnitude"
)
ANTI_DEFENSE_SNIPPET = (
    "Since the sanaTA system provides resistance to the T7Δ4.5 mutant "
    "phage but not to the WT T7 phage, we hypothesized that the 4.5 "
    "gene codes for an anti-defense mechanism that overcomes the "
    "abortive infection imposed by the TA system."
)
ABSTRACT_RESISTANCE_SNIPPET = (
    "Infection experiments with T7 phage showed that two of the new "
    "modules can provide resistance against phage."
)
ARTICLE_REGISTRY_SNIPPET = (
    "SanaTA | 10\\.1016/j\\.molcel\\.2013\\.02\\.002 | Discovery of "
    "functional toxin/antitoxin systems in bacteria by shotgun cloning"
)
RULES_SNIPPET = "SanaTA\tSanaTA\t2\t2\tSanaTA__SanaA, SanaTA__SanaT\t\t\t"
HMM_ROWS = {
    "SanaTA__SanaA": (
        "| SanaTA__SanaA                                    | "
        "SanaTA__SanaA                                    | "
        "SanaTA                 | Custom                  | 20     |"
    ),
    "SanaTA__SanaT": (
        "| SanaTA__SanaT                                    | "
        "SanaTA__SanaT                                    | "
        "SanaTA                 | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named SanaTA "
            "system to the Sberro et al. toxin/antitoxin shotgun-cloning "
            "paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models SanaTA as a two-profile "
            "system requiring SanaTA__SanaA and SanaTA__SanaT."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under "
            "SanaTA."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "SanaTA system",
    "definition": (
        "A phage defense system in which an organism possesses a sanaTA "
        "toxin-antitoxin locus represented by DefenseFinder as a "
        "SanaA/SanaT two-profile model and experimentally linked to "
        "resistance against T7 phage mutants lacking gene 4.5 "
        "anti-defense activity."
    ),
    "definition_source": SBERRO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "sanaTA",
            "synonym_type": "RELATED_SYNONYM",
            "source": SBERRO,
        },
        {
            "synonym_text": "SanaTA",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_ROWS
        ],
    ],
    "evidence": [
        {
            "reference": SBERRO_PMID,
            "snippet": TA_VALIDATION_SNIPPET,
            "notes": (
                "Sberro et al. experimentally validated the sanaTA family "
                "as one of six new toxin-antitoxin systems."
            ),
        },
        {
            "reference": SBERRO_PMID,
            "snippet": T7_RESISTANCE_SNIPPET,
            "notes": (
                "Sberro et al. connect the sanaTA system to lower "
                "sensitivity to T7 phages lacking gene 4.5."
            ),
        },
        {
            "reference": SBERRO_PMID,
            "snippet": ANTI_DEFENSE_SNIPPET,
            "notes": (
                "Sberro et al. show that SanaTA resists a T7 gene 4.5 "
                "mutant and leave the phage-encoded anti-Abi interaction "
                "as part of the system context."
            ),
        },
        {
            "reference": SBERRO,
            "snippet": ABSTRACT_RESISTANCE_SNIPPET,
            "notes": (
                "Sberro et al. summarize that infection experiments found "
                "phage resistance in two of the newly identified modules."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "sanata_locus_restricts_t7_mutants",
            "title": "SanaTA loci restrict T7 gene 4.5 mutants",
            "description": (
                "Conservative system-level sketch linking a DefenseFinder "
                "SanaTA locus to resistance against T7 phages lacking gene "
                "4.5 anti-defense activity."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SanaTA as a named two-profile "
                "toxin-antitoxin phage-defense system while leaving native "
                "host breadth, SanaA and SanaT molecular activities, the "
                "exact T7 Gp4.5/Lon interaction sequence, and the extra "
                "pinned SanaTA__SanaT_1 HMM row unresolved."
            ),
            "nodes": [
                {
                    "node_id": "sanata_locus",
                    "label": "SanaTA locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A sanaTA toxin-antitoxin phage-defense locus "
                        "represented by the DefenseFinder SanaTA__SanaA "
                        "and SanaTA__SanaT profiles."
                    ),
                },
                {
                    "node_id": "t7_gene_45_mutant_resistance",
                    "label": "T7 gene 4.5 mutant resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of T7 phage mutants that lack the "
                        "gene 4.5 anti-defense activity in a host "
                        "expressing SanaTA."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "SanaTA system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded SanaTA "
                        "phage-defense system."
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
                    "subject": "sanata_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t7_gene_45_mutant_resistance",
                    "description": (
                        "A cloned sanaTA toxin-antitoxin system can reduce "
                        "sensitivity to T7 phages lacking gene 4.5, and "
                        "DefenseFinder models SanaTA as a two-profile "
                        "SanaA/SanaT system."
                    ),
                    "evidence": [
                        {
                            "reference": SBERRO_PMID,
                            "snippet": T7_RESISTANCE_SNIPPET,
                            "notes": (
                                "Sberro et al. show that SanaTA reduced "
                                "sensitivity to T7 mutants lacking gene 4.5."
                            ),
                        },
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "t7_gene_45_mutant_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "SanaTA-mediated resistance to T7 gene 4.5 mutants "
                        "realizes the SanaTA system trait."
                    ),
                    "evidence": [
                        {
                            "reference": SBERRO_PMID,
                            "snippet": ANTI_DEFENSE_SNIPPET,
                            "notes": (
                                "Sberro et al. frame T7 gene 4.5 as the "
                                "anti-defense context for SanaTA-mediated "
                                "abortive infection."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "SanaTA system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": SBERRO,
                            "snippet": ABSTRACT_RESISTANCE_SNIPPET,
                            "notes": (
                                "Sberro et al. connect newly discovered "
                                "toxin-antitoxin modules to phage "
                                "resistance in T7 infection experiments."
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
            "discussion_id": "sanata-host-trigger-profile-gap",
            "prompt": (
                "Resolve SanaTA native host breadth, SanaA/SanaT "
                "molecular activities, T7 Gp4.5/Lon anti-defense logic, "
                "and the SanaTA__SanaT_1 profile before minting narrower "
                "SanaTA mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Sberro et al. support sanaTA as a Shewanella sp. ANA-3 "
                "two-gene toxin-antitoxin family that confers resistance to "
                "T7 phage mutants lacking gene 4.5 when expressed in "
                "Escherichia coli, and DefenseFinder models SanaTA with "
                "SanaTA__SanaA and SanaTA__SanaT. This first system-level "
                "record leaves the natural host range, SanaA/SanaT "
                "activities, T7 Gp4.5/Lon counter-defense sequence, and the "
                "extra non-rule SanaTA__SanaT_1 HMM unresolved."
            ),
            "evidence": [
                {
                    "reference": SBERRO_PMID,
                    "snippet": ANTI_DEFENSE_SNIPPET,
                    "notes": (
                        "Sberro et al. connect T7 gene 4.5 to SanaTA "
                        "anti-Abi escape but leave the locus-level "
                        "SanaTA mechanism only partly resolved."
                    ),
                },
                rules_evidence(),
            ],
            "attaches_to": ["causal_graphs#sanata_locus_restricts_t7_mutants"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-25",
        }
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted SanaTA system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed SanaTA during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "source validates a broad DefenseFinder toxin-antitoxin "
            "family in an Escherichia coli expression assay and does not "
            "establish a direct native host exemplar. No paid research "
            "was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    write_record(apply=args.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
