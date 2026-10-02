#!/usr/bin/env python3
"""Add the DRT2 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "drt2_system.yaml"

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
TIMESTAMP = "2026-10-02T11:51:13Z"
CANONICAL_TIMESTAMP = "2026-10-02T11:51:14Z"
IDENTIFIER = "traitmech:000544"
DRT_PARENT_ID = "traitmech:000279"
PROPOSAL = "proposals/metpo_traitmech_v421"

ARTICLE_ROW = (
    "| DRT | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
    "activities mediate antiviral immunity in prokaryotes | "
)
RULE_ROW = "DRT\tDRT_2\t1\t1\tDRT_2__drt2\t\t\t"
HMM_ROW = (
    "| DRT_2__drt2                                      |"
    " DRT_2__drt2                                      |"
    " DRT_2                  | Custom                  | 100    |"
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
            "The pinned DefenseFinder HMM inventory records "
            "DRT_2__drt2 under the DRT_2 model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models DRT_2 as a DRT "
            "subsystem with a DRT_2__drt2 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DRT2 system",
    "definition": (
        "A DRT system in which an organism possesses a genome-encoded "
        "DefenseFinder DRT_2 subtype locus represented by the "
        "DRT_2__drt2 profile."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [DRT_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "DRT_2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "DRT_2__drt2",
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
            "graph_id": "drt2_locus_reverse_transcriptase_defense",
            "title": "DRT2 loci support DRT antiphage defense",
            "description": (
                "Conservative system-level sketch linking a DRT2 locus "
                "to reverse-transcriptase-dependent DRT phage defense "
                "and DRT2 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DRT2 at DefenseFinder subtype-locus "
                "level without asserting the direct DRT2 reverse-"
                "transcriptase product, phage trigger, native host "
                "breadth, sensitive phage breadth, partner-feature "
                "requirements, profile-to-activity criteria, or whether "
                "every DefenseFinder DRT_2 prediction is a complete "
                "experimentally active DRT2 locus."
            ),
            "nodes": [
                {
                    "node_id": "drt2_locus",
                    "label": "DRT2 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A defense-associated reverse transcriptase "
                        "subtype II locus represented in DefenseFinder "
                        "by a DRT_2 profile."
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
                    "node_id": "drt2_system_trait",
                    "label": "DRT2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DRT2 "
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
                    "subject": "drt2_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "drt_rt_active_site_activity",
                    "description": (
                        "DRT2 loci are represented in DefenseFinder by a "
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
                    "object": "drt2_system_trait",
                    "description": (
                        "The first-pass DRT2 system trait is realized by "
                        "a DefenseFinder DRT_2 subtype locus within the "
                        "reverse-transcriptase-dependent DRT family."
                    ),
                    "evidence": [
                        drt_discovery_evidence(),
                        drt_active_site_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "drt2_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "drt_system_trait",
                    "description": "DRT2 system possession is a DRT-system trait.",
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
            "discussion_id": "drt2-profile-activity-gap",
            "prompt": (
                "Resolve the DRT2 reverse-transcriptase product, direct "
                "phage trigger, host breadth, partner-feature "
                "requirements, and DRT_2 profile-to-activity criteria "
                "before minting DRT2 mechanism or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Gao et al. support defense-associated reverse "
                "transcriptases as a broad antiphage-system family, and "
                "the pinned DefenseFinder HMM inventory and rules table "
                "support DRT_2 as a single-profile DRT subsystem. This "
                "first-pass record leaves the exact DRT2 RT product, "
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
                "causal_graphs#drt2_locus_reverse_transcriptase_defense"
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
            "Minted DRT2 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the DRT system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "DRT2 TraitMech, METPO, history, or prior proposal record; "
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
            "Reviewed DRT2 system during initial curation and left "
            "canonical_examples empty because Gao et al. and the pinned "
            "DefenseFinder tables support the DRT family and the DRT_2 "
            "model namespace but not an accession-backed native microbial "
            "taxon exemplar tied to DRT_2__drt2 and experimentally "
            "verified endogenous DRT2 activity. No paid research was "
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
            "DRT2 system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
