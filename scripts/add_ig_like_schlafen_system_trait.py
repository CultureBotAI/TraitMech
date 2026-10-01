#!/usr/bin/env python3
"""Add the Ig-like Schlafen system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ig_like_schlafen_system.yaml"

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
TIMESTAMP = "2026-10-01T06:21:00Z"
CANONICAL_TIMESTAMP = "2026-10-01T06:21:01Z"
IDENTIFIER = "traitmech:000508"
PHAGE_DEFENSE_PARENT_ID = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v385"

ARTICLE_ROW = (
    "| Shlafen_Ig-like | 10\\.1038/s41564-026-02277-8 | Bacterial "
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


def ig_sensor_evidence() -> dict[str, str]:
    return {
        "reference": PEREZ_TABOADA,
        "snippet": (
            "Schlafen nuclease is fused to a previously unknown "
            "immunoglobulin-like sensor domain and demonstrated that it "
            "recognizes tail assembly chaperones of T5-like phages."
        ),
        "notes": (
            "Perez Taboada et al. support Ig-like domain fusion and "
            "T5-like tail assembly chaperone recognition by an Ig-like "
            "prokaryotic Schlafen system."
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


def trna_cleavage_evidence() -> dict[str, str]:
    return {
        "reference": PEREZ_TABOADA,
        "snippet": (
            "Upon activation, the Schlafen nuclease cleaves both E. coli "
            "and phage-encoded tRNAs and restricts T5 phage by reducing "
            "its burst size."
        ),
        "notes": (
            "Perez Taboada et al. connect activation of an Ig-like "
            "RorSlfn5 nuclease to bacterial and phage tRNA cleavage and "
            "T5 burst-size reduction."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the "
            "Shlafen_Ig-like source key to the Perez Taboada et al. "
            "Schlafen phage-defense paper."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact Shlafen_Ig-like, Schlafen, or "
            "pSlfn5 row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact Shlafen_Ig-like, Schlafen, or "
            "pSlfn5 system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Ig-like Schlafen system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "genome-encoded prokaryotic Schlafen nuclease fused to an "
        "immunoglobulin-like sensor domain that recognizes T5-like phage "
        "tail assembly chaperones and activates Schlafen tRNase defense."
    ),
    "definition_source": PEREZ_TABOADA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Shlafen_Ig-like",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "pSlfn5",
            "synonym_type": "RELATED_SYNONYM",
            "source": PEREZ_TABOADA,
        },
    ],
    "evidence": [
        antiviral_effector_evidence(),
        ig_sensor_evidence(),
        tested_systems_evidence(),
        trna_cleavage_evidence(),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ig_like_schlafen_trna_cleavage",
            "title": "Ig-like Schlafen systems cleave tRNAs after phage sensing",
            "description": (
                "Conservative system-level sketch linking an Ig-like "
                "prokaryotic Schlafen locus to T5-like tail assembly "
                "chaperone sensing, Schlafen nuclease-dependent tRNA "
                "cleavage, and the Ig-like Schlafen phage-defense trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the Ig-like prokaryotic Schlafen "
                "DefenseFinder article namespace at system level and "
                "deliberately defers a protein-resolved RorSlfn5 "
                "mechanism. Perez Taboada et al. support an Ig-like "
                "Schlafen nuclease system that recognizes T5-like phage "
                "tail assembly chaperones and cleaves bacterial and phage "
                "tRNAs, but exact profile boundaries, natural host "
                "exemplars, phage trigger breadth, and DefenseFinder "
                "HMM/rules profiles are unresolved."
            ),
            "nodes": [
                {
                    "node_id": "ig_like_schlafen_locus",
                    "label": "Ig-like Schlafen locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A locus encoding a prokaryotic Schlafen nuclease "
                        "fused to an Ig-like sensor domain."
                    ),
                },
                {
                    "node_id": "t5_like_tail_chaperone_sensing",
                    "label": "T5-like tail chaperone sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Recognition of T5-like phage tail assembly "
                        "chaperones by an Ig-like prokaryotic Schlafen "
                        "sensor domain."
                    ),
                },
                {
                    "node_id": "schlafen_trna_cleavage",
                    "label": "Schlafen tRNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cleavage of bacterial and phage tRNAs by an "
                        "activated Schlafen nuclease."
                    ),
                },
                {
                    "node_id": "ig_like_schlafen_system_trait",
                    "label": "Ig-like Schlafen system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Ig-like "
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
                    "subject": "ig_like_schlafen_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t5_like_tail_chaperone_sensing",
                    "description": (
                        "Ig-like Schlafen loci encode a Schlafen nuclease "
                        "fused to an Ig-like sensor domain that recognizes "
                        "T5-like phage tail assembly chaperones."
                    ),
                    "evidence": [
                        ig_sensor_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "t5_like_tail_chaperone_sensing",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "schlafen_trna_cleavage",
                    "description": (
                        "Phage-triggered activation of the Ig-like "
                        "Schlafen nuclease leads to bacterial and phage "
                        "tRNA cleavage."
                    ),
                    "evidence": [
                        ig_sensor_evidence(),
                        trna_cleavage_evidence(),
                    ],
                },
                {
                    "subject": "schlafen_trna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ig_like_schlafen_system_trait",
                    "description": (
                        "Schlafen tRNase activity restricts T5 phage and "
                        "realizes the organism-level Ig-like Schlafen "
                        "system trait."
                    ),
                    "evidence": [
                        antiviral_effector_evidence(),
                        trna_cleavage_evidence(),
                    ],
                },
                {
                    "subject": "ig_like_schlafen_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system_trait",
                    "description": (
                        "Ig-like Schlafen system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        antiviral_effector_evidence(),
                        tested_systems_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ig-like-schlafen-defensefinder-profile-gap",
            "prompt": (
                "Resolve exact pSlfn5 family boundaries, natural host "
                "exemplars, T5-like tail chaperone trigger breadth, and "
                "DefenseFinder HMM/rules coverage before minting narrower "
                "Ig-like Schlafen mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Perez Taboada et al. support prokaryotic Schlafen "
                "nucleases as widespread antiviral effectors and "
                "experimentally characterize the Ig-like RorSlfn5 nuclease "
                "as a T5-like tail chaperone-triggered tRNase, and the "
                "pinned DefenseFinder article registry maps the "
                "Shlafen_Ig-like key to the same article. The pinned HMM "
                "inventory and rules table have no exact Schlafen rows. "
                "This first-pass record therefore does not resolve exact "
                "pSlfn5 family boundaries, natural host exemplars, "
                "accession-level Schlafen proteins, full phage trigger "
                "breadth, or a reusable DefenseFinder profile model."
            ),
            "evidence": [
                antiviral_effector_evidence(),
                ig_sensor_evidence(),
                trna_cleavage_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#ig_like_schlafen_trna_cleavage"],
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
            "Minted Ig-like Schlafen system as a DOI- and "
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
            "Reviewed Ig-like Schlafen system during initial curation and "
            "left canonical_examples empty because Perez Taboada et al. "
            "support RorSlfn5 from Raoultella ornithinolytica, but an "
            "NCBI Taxonomy lookup for that current name did not resolve "
            "during first-pass curation. No paid research was used."
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
            "Ig-like Schlafen system trait validates; rerun with --apply "
            f"to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
