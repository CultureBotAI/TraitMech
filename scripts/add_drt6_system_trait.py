#!/usr/bin/env python3
"""Add the DRT6 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "drt6_system.yaml"

GAO_2020 = "DOI:10.1126/science.aba0372"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T08:13:19Z"
CANONICAL_TIMESTAMP = "2026-10-02T08:13:20Z"
IDENTIFIER = "traitmech:000539"
DRT_PARENT_ID = "traitmech:000279"
PROPOSAL = "proposals/metpo_traitmech_v416"

ARTICLE_ROW = (
    "| DRT | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
    "activities mediate antiviral immunity in prokaryotes | "
)
RULE_ROW = "DRT\tDRT6\t1\t1\tDRT6__DRT6\t\t\t"
HMM_ROW = (
    "| DRT6__DRT6                                       |"
    " DRT6__DRT6                                       |"
    " DRT6                   | Custom                  | 300    |"
)


def drt_discovery_evidence() -> dict[str, str]:
    return {
        "reference": GAO_2020,
        "snippet": (
            "We discovered that a family of uncharacterized reverse "
            "transcriptases (RTs) are active defense systems"
        ),
        "notes": (
            "Gao et al. experimentally support defense-associated reverse "
            "transcriptases as active antiphage systems."
        ),
    }


def drt_name_evidence() -> dict[str, str]:
    return {
        "reference": GAO_2020,
        "snippet": "We named these genes defense-associated RTs (DRTs)",
        "notes": (
            "Gao et al. coined the defense-associated RT naming that "
            "underlies the DRT system family."
        ),
    }


def drt_active_site_evidence() -> dict[str, str]:
    return {
        "reference": GAO_2020,
        "snippet": (
            "In all cases, mutations in the RT active site [(Y/F)xDD to "
            "(Y/F)xAA, where x is any amino acid] abolished activity"
        ),
        "notes": (
            "Gao et al. connect DRT antiphage activity to conserved "
            "reverse-transcriptase active-site residues."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DRT source "
            "key to the Gao et al. prokaryotic antiviral-immunity paper."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records DRT6__DRT6 "
            "under the DRT6 model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models DRT6 as a DRT "
            "subsystem with a DRT6 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DRT6 system",
    "definition": (
        "A DRT system in which an organism possesses a genome-encoded "
        "DefenseFinder DRT6 subtype locus represented by the DRT6__DRT6 "
        "profile."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [DRT_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "DRT6",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "DRT6__DRT6",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        drt_discovery_evidence(),
        drt_name_evidence(),
        drt_active_site_evidence(),
        article_registry_evidence(),
        hmm_evidence(),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "drt6_locus_reverse_transcriptase_defense",
            "title": "DRT6 loci support DRT antiphage defense",
            "description": (
                "Conservative system-level sketch linking a DRT6 locus "
                "to reverse-transcriptase-dependent DRT phage defense "
                "and DRT6 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DRT6 at DefenseFinder subtype-locus "
                "level without asserting the direct DRT6 reverse-"
                "transcriptase product, phage trigger, native host "
                "breadth, sensitive phage breadth, partner features, or "
                "whether every DefenseFinder DRT6 prediction is a "
                "complete experimentally active DRT6 locus."
            ),
            "nodes": [
                {
                    "node_id": "drt6_locus",
                    "label": "DRT6 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A defense-associated reverse transcriptase "
                        "subtype VI locus represented in DefenseFinder by "
                        "a DRT6 profile."
                    ),
                },
                {
                    "node_id": "drt_rt_active_site_activity",
                    "label": "DRT reverse-transcriptase active-site activity",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "Reverse-transcriptase active-site-dependent "
                        "activity of a defense-associated RT antiphage "
                        "protein."
                    ),
                },
                {
                    "node_id": "drt6_system_trait",
                    "label": "DRT6 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DRT6 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "drt_system_trait",
                    "label": "DRT system",
                    "node_type": "TRAIT",
                    "grounding": DRT_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded "
                        "defense-associated reverse transcriptase "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "drt6_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "drt_rt_active_site_activity",
                    "description": (
                        "DRT6 loci are represented in DefenseFinder by a "
                        "custom defense-associated reverse transcriptase "
                        "profile."
                    ),
                    "evidence": [
                        drt_name_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "drt_rt_active_site_activity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "drt6_system_trait",
                    "description": (
                        "The first-pass DRT6 system trait is realized by a "
                        "DefenseFinder DRT6 subtype locus within the "
                        "reverse-transcriptase-dependent DRT family."
                    ),
                    "evidence": [
                        drt_discovery_evidence(),
                        drt_active_site_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "drt6_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "drt_system_trait",
                    "description": "DRT6 system possession is a DRT-system trait.",
                    "evidence": [
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "drt6-profile-activity-gap",
            "prompt": (
                "Resolve the DRT6 reverse-transcriptase product, direct "
                "phage trigger, host breadth, partner-feature "
                "requirements, and DefenseFinder profile-to-activity "
                "criteria before minting DRT6 mechanism or component "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support defense-associated reverse "
                "transcriptases as a broad antiphage-system family, and "
                "the pinned DefenseFinder HMM inventory and rules table "
                "support DRT6 as a single-profile DRT subsystem. This "
                "first-pass record leaves the exact DRT6 RT product, "
                "phage trigger, host breadth, partner-feature "
                "requirements, and profile-to-activity requirements "
                "unresolved."
            ),
            "evidence": [
                drt_discovery_evidence(),
                drt_active_site_evidence(),
                hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#drt6_locus_reverse_transcriptase_defense"
            ],
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
            "Minted DRT6 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the DRT system parent after an "
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
            "Reviewed DRT6 system during initial curation and left "
            "canonical_examples empty because Gao et al. and the pinned "
            "DefenseFinder tables support the DRT family and the DRT6 "
            "model namespace but not an accession-backed native microbial "
            "taxon exemplar tied to DRT6__DRT6 and experimentally "
            "verified endogenous DRT6 activity. No paid research was "
            "used."
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
            "DRT6 system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
