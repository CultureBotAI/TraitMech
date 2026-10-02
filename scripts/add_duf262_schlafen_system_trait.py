#!/usr/bin/env python3
"""Add the DUF262 Schlafen system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "duf262_schlafen_system.yaml"

PEREZ_TABOADA = "DOI:10.1038/s41564-026-02277-8"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T01:00:00Z"
CANONICAL_TIMESTAMP = "2026-10-02T01:00:01Z"
IDENTIFIER = "traitmech:000530"
PHAGE_DEFENSE_PARENT_ID = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v407"

ARTICLE_ROW = (
    "| DUF262_Shlafen | 10\\.1038/s41564-026-02277-8 | Bacterial "
    "Schlafen proteins mediate phage defence | "
)


def antiviral_effector_evidence() -> dict[str, str]:
    return {
        "reference": PEREZ_TABOADA,
        "snippet": (
            "prokaryotic Schlafen nucleases are widespread antiviral "
            "effectors that protect bacteria from bacteriophages and are "
            "fused to a diverse array of phage-sensing domains."
        ),
        "notes": (
            "Perez Taboada et al. support bacterial prokaryotic Schlafen "
            "nucleases as antiviral effectors fused to phage-sensing "
            "domains."
        ),
    }


def tested_systems_evidence() -> dict[str, str]:
    return {
        "reference": PEREZ_TABOADA,
        "snippet": (
            "We expressed seven Enterobacterales Schlafen systems in "
            "Escherichia coli, identifying two that confer defence against "
            "coliphages."
        ),
        "notes": (
            "Perez Taboada et al. cloned candidate Enterobacterales "
            "Schlafen systems into E. coli and observed coliphage defense "
            "for two of them."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the "
            "DUF262_Shlafen source key to the Perez Taboada et al. "
            "Schlafen phage-defense paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact DUF262_Shlafen, Schlafen, or DUF262 "
            "row for this system."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact DUF262_Shlafen, Schlafen, or "
            "DUF262 system row for this system."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DUF262 Schlafen system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "genome-encoded, DUF262-associated prokaryotic Schlafen nuclease "
        "locus."
    ),
    "definition_source": PEREZ_TABOADA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "DUF262_Shlafen",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        antiviral_effector_evidence(),
        tested_systems_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "duf262_schlafen_phage_defense",
            "title": "DUF262 Schlafen loci support Schlafen phage defense",
            "description": (
                "Conservative system-level sketch linking a "
                "DUF262_Schlafen locus to prokaryotic Schlafen nuclease "
                "antiviral activity and the phage-defense parent."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the DefenseFinder DUF262_Shlafen "
                "article namespace at system level and deliberately leaves "
                "the exact locus architecture, the DUF262-associated "
                "domain boundary, accession-level protein examples, native "
                "host exemplars, phage trigger breadth, and DefenseFinder "
                "HMM/rules profiles unresolved."
            ),
            "nodes": [
                {
                    "node_id": "duf262_schlafen_locus",
                    "label": "DUF262 Schlafen locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding a prokaryotic Schlafen nuclease "
                        "in a DUF262-associated anti-phage system."
                    ),
                },
                {
                    "node_id": "schlafen_antiviral_activity",
                    "label": "Schlafen antiviral activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Anti-phage activity mediated by a prokaryotic "
                        "Schlafen nuclease."
                    ),
                },
                {
                    "node_id": "duf262_schlafen_system_trait",
                    "label": "DUF262 Schlafen system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DUF262-associated "
                        "prokaryotic Schlafen phage-defense system."
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
                    "subject": "duf262_schlafen_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "schlafen_antiviral_activity",
                    "description": (
                        "DUF262_Schlafen loci are part of the bacterial "
                        "prokaryotic Schlafen nuclease phage-defense family."
                    ),
                    "evidence": [
                        antiviral_effector_evidence(),
                    ],
                },
                {
                    "subject": "schlafen_antiviral_activity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "duf262_schlafen_system_trait",
                    "description": (
                        "Prokaryotic Schlafen antiviral effector activity "
                        "realizes the organism-level DUF262 Schlafen system "
                        "trait."
                    ),
                    "evidence": [
                        antiviral_effector_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "duf262_schlafen_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system_trait",
                    "description": (
                        "DUF262 Schlafen system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        tested_systems_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "duf262-schlafen-defensefinder-profile-gap",
            "prompt": (
                "Resolve exact DUF262_Schlafen locus architecture, "
                "DUF262-associated domain boundaries, natural host "
                "exemplars, phage trigger breadth, and DefenseFinder "
                "HMM/rules coverage before minting narrower DUF262 "
                "Schlafen mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Perez Taboada et al. support prokaryotic Schlafen "
                "nucleases as widespread antiviral effectors fused to "
                "phage-sensing domains, and the pinned DefenseFinder "
                "article registry maps the DUF262_Shlafen key to the same "
                "article. The pinned HMM inventory and rules table have no "
                "exact DUF262_Schlafen or DUF262 rows for this source key. "
                "This first-pass record therefore does not resolve whether "
                "the exact DUF262_Schlafen architecture is a single-protein "
                "fusion or multi-gene locus, its exact DUF262-associated "
                "domain boundaries, natural host exemplars, "
                "accession-level Schlafen proteins, full phage trigger "
                "breadth, or a reusable DefenseFinder profile model."
            ),
            "evidence": [
                antiviral_effector_evidence(),
                tested_systems_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#duf262_schlafen_phage_defense"],
            "posed_by": CURATOR,
            "posed_date": "2026-10-02",
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
            "Minted DUF262 Schlafen system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under the phage "
            "defense system parent after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or "
            "prior proposal record; the replacement placeholder is "
            f"reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DUF262 Schlafen system during initial curation and "
            "left canonical_examples empty because Perez Taboada et al. "
            "and the pinned DefenseFinder article registry support the "
            "DUF262_Schlafen system namespace, but not an "
            "accession-backed native microbial taxon exemplar for the "
            "exact DUF262_Schlafen source key. No paid research was used."
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
            "DUF262 Schlafen system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
