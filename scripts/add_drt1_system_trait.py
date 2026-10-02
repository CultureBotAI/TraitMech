#!/usr/bin/env python3
"""Add the DRT1 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "drt1_system.yaml"

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
TIMESTAMP = "2026-10-02T11:04:00Z"
CANONICAL_TIMESTAMP = "2026-10-02T11:04:01Z"
IDENTIFIER = "traitmech:000543"
DRT_PARENT_ID = "traitmech:000279"
PROPOSAL = "proposals/metpo_traitmech_v420"

ARTICLE_ROW = (
    "| DRT | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
    "activities mediate antiviral immunity in prokaryotes | "
)
RULE_ROW = "DRT\tDRT_1\t2\t2\tDRT_1__drt1a, DRT_1__drt1b\t\t\t"
HMM_ROWS = (
    "| DRT_1__drt1a                                     |"
    " DRT_1__drt1a                                     |"
    " DRT_1                  | Custom                  | 600    |\n"
    "| DRT_1__drt1b                                     |"
    " DRT_1__drt1b                                     |"
    " DRT_1                  | Custom                  | 20     |"
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
        "snippet": HMM_ROWS,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            "DRT_1__drt1a and DRT_1__drt1b under the DRT_1 model "
            "namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models DRT_1 as a DRT "
            "subsystem requiring DRT_1__drt1a and DRT_1__drt1b."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DRT1 system",
    "definition": (
        "A DRT system in which an organism possesses a genome-encoded "
        "DefenseFinder DRT_1 subtype locus represented by the mandatory "
        "DRT_1__drt1a and DRT_1__drt1b profiles."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [DRT_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "DRT_1",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "DRT_1__drt1a",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DRT_1__drt1b",
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
            "graph_id": "drt1_locus_reverse_transcriptase_defense",
            "title": "DRT1 loci support DRT antiphage defense",
            "description": (
                "Conservative system-level sketch linking a DRT1 locus "
                "to reverse-transcriptase-dependent DRT phage defense "
                "and DRT1 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DRT1 at DefenseFinder subtype-locus "
                "level without asserting the exact products of the "
                "DRT_1__drt1a and DRT_1__drt1b profiles, phage trigger, "
                "native host breadth, sensitive phage breadth, partner-"
                "feature requirements, profile-to-activity criteria, or "
                "whether every DefenseFinder DRT_1 prediction is a "
                "complete experimentally active DRT1 locus."
            ),
            "nodes": [
                {
                    "node_id": "drt1_locus",
                    "label": "DRT1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A defense-associated reverse transcriptase "
                        "subtype I locus represented in DefenseFinder "
                        "by DRT_1 profiles."
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
                    "node_id": "drt1_system_trait",
                    "label": "DRT1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DRT1 "
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
                    "subject": "drt1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "drt_rt_active_site_activity",
                    "description": (
                        "DRT1 loci are represented in DefenseFinder by "
                        "custom defense-associated reverse transcriptase "
                        "profiles."
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
                    "object": "drt1_system_trait",
                    "description": (
                        "The first-pass DRT1 system trait is realized by "
                        "a DefenseFinder DRT_1 subtype locus within the "
                        "reverse-transcriptase-dependent DRT family."
                    ),
                    "evidence": [
                        drt_discovery_evidence(),
                        drt_active_site_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "drt1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "drt_system_trait",
                    "description": "DRT1 system possession is a DRT-system trait.",
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
            "discussion_id": "drt1-profile-activity-gap",
            "prompt": (
                "Resolve the DRT1 reverse-transcriptase products, direct "
                "phage trigger, host breadth, partner-feature "
                "requirements, and DRT_1__drt1a/DRT_1__drt1b "
                "profile-to-activity criteria before minting DRT1 "
                "mechanism or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support defense-associated reverse "
                "transcriptases as a broad antiphage-system family, and "
                "the pinned DefenseFinder HMM inventory and rules table "
                "support DRT_1 as a DRT subsystem with two mandatory "
                "profiles. This first-pass record leaves the exact DRT1 "
                "RT products, phage trigger, host breadth, partner-feature "
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
                "causal_graphs#drt1_locus_reverse_transcriptase_defense"
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
            "Minted DRT1 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the DRT system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "DRT1 TraitMech, METPO, history, or prior proposal record; "
            "the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DRT1 system during initial curation and left "
            "canonical_examples empty because Gao et al. and the pinned "
            "DefenseFinder tables support the DRT family and the DRT_1 "
            "model namespace but not an accession-backed native microbial "
            "taxon exemplar tied to DRT_1__drt1a and DRT_1__drt1b and "
            "experimentally verified endogenous DRT1 activity. No paid "
            "research was used."
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
            "DRT1 system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
