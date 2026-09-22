#!/usr/bin/env python3
"""Add the MqsRAC system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mqsrac_system.yaml"

FERNANDEZ = "DOI:10.1128/spectrum.03388-23"
FERNANDEZ_PMID = "PMID:38054715"

MQSRAC_PERSISTER_SNIPPET = (
    "Therefore, our results are important since we show for the first time "
    "that a phage-defense system, the MqsRAC toxin/antitoxin system, allows "
    "the host to survive infection by forming persister cells, rather than "
    "inducing cell suicide."
)
MQSRAC_RM_SNIPPET = (
    "Moreover, we demonstrate that the MqsRAC system works in concert with "
    "restriction/modification systems."
)
MQSRAC_TRIPARTITE_SNIPPET = (
    "the tripartite system MqsR (RNase toxin)/MqsA (antitoxin)/MqsC "
    "(SecB-type chaperone)"
)
MQSRAC_T2_INHIBITION_SNIPPET = (
    "We found there was a 2,100 to a 5,000-fold reduction in the EOP with "
    "phage T2 when the cells produced MqsR/MqsA/MqsC"
)
MQSRAC_MCRBC_SNIPPET = (
    "Therefore, MqsR/MqsA/MqsC works in concert with "
    "restriction/modification systems to inhibit T2 phage."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-22T15:02:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-22T15:03:00Z"
GRAPH_DIRECTION_REVIEW_TIMESTAMP = "2026-09-22T15:15:00Z"
RM_SPECIFICITY_REVIEW_TIMESTAMP = "2026-09-22T15:18:00Z"
IDENTIFIER = "traitmech:000368"
PROPOSAL = "proposals/metpo_traitmech_v245"
SLUG = "mqsrac"

ARTICLE_REGISTRY_SNIPPET = (
    "MqsRAC | 10\\.1101/2022\\.05\\.12\\.491691 | Mapping the landscape "
    "of anti-phage defense mechanisms in the E\\. coli pangenome"
)
RULES_SNIPPET = "MqsRAC\tMqsRAC\t2\t2\tMqsRAC__mqsC, MqsRAC__mqsR\t\t\t"
HMM_ROWS = {
    "MqsRAC__mqsC": (
        "| MqsRAC__mqsC                                     | "
        "MqsRAC__mqsC                                     | "
        "MqsRAC                 | Custom                  | 20     |"
    ),
    "MqsRAC__mqsR": (
        "| MqsRAC__mqsR                                     | "
        "MqsRAC__mqsR                                     | "
        "MqsRAC                 | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named MqsRAC "
            "system to Vassallo et al.'s E. coli pangenome phage-defense "
            "screen."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models MqsRAC as a two-profile "
            "system requiring the MqsRAC__mqsC and MqsRAC__mqsR profiles."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} "
            "under MqsRAC."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "MqsRAC system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "tripartite MqsRAC toxin-antitoxin-chaperone locus represented "
        "by DefenseFinder as a two-profile model requiring MqsRAC__mqsC "
        "and MqsRAC__mqsR."
    ),
    "definition_source": FERNANDEZ,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "MqsRAC",
            "synonym_type": "RELATED_SYNONYM",
            "source": FERNANDEZ,
        },
        {
            "synonym_text": "MqsR/MqsA/MqsC",
            "synonym_type": "RELATED_SYNONYM",
            "source": FERNANDEZ,
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
            "reference": FERNANDEZ_PMID,
            "snippet": MQSRAC_PERSISTER_SNIPPET,
            "notes": (
                "Fernandez-Garcia et al. support MqsRAC as a phage-defense "
                "system whose outcome is host survival through persister-cell "
                "formation rather than cell suicide."
            ),
        },
        {
            "reference": FERNANDEZ_PMID,
            "snippet": MQSRAC_RM_SNIPPET,
            "notes": (
                "Fernandez-Garcia et al. connect the MqsRAC system to "
                "restriction/modification systems during phage inhibition."
            ),
        },
        {
            "reference": FERNANDEZ,
            "snippet": MQSRAC_TRIPARTITE_SNIPPET,
            "notes": (
                "Fernandez-Garcia et al. describe MqsR/MqsA/MqsC as a "
                "tripartite toxin-antitoxin-chaperone phage-exclusion "
                "system from Escherichia coli C496_10."
            ),
        },
        {
            "reference": FERNANDEZ,
            "snippet": MQSRAC_T2_INHIBITION_SNIPPET,
            "notes": (
                "Fernandez-Garcia et al. support MqsRAC-mediated reduction "
                "of T2 efficiency of plating."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "mqsrac_locus_promotes_persister_phage_defense",
            "title": "MqsRAC loci support T2 phage inhibition",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "MqsRAC locus to persister-cell formation and T2 inhibition "
                "without asserting a universal phage trigger, lethal "
                "abortive-infection route, or exact MqsRAC "
                "profile-to-activity mapping."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures MqsRAC as a named DefenseFinder "
                "two-profile phage-defense system while leaving natural "
                "phage breadth, upstream MqsRAC activation logic, the exact "
                "relationship between the two DefenseFinder profiles and "
                "the tripartite MqsR/MqsA/MqsC locus, and cooperating "
                "restriction/modification contexts unresolved."
            ),
            "nodes": [
                {
                    "node_id": "mqsrac_locus",
                    "label": "MqsRAC locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A toxin-antitoxin-chaperone locus represented by "
                        "DefenseFinder MqsRAC__mqsC and MqsRAC__mqsR "
                        "profiles."
                    ),
                },
                {
                    "node_id": "mqsrac_persister_formation",
                    "label": "MqsRAC-dependent persister cell formation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Formation of persister cells during T2 phage "
                        "attack in cells producing MqsR/MqsA/MqsC."
                    ),
                },
                {
                    "node_id": "rm_assisted_t2_inhibition",
                    "label": "restriction/modification-assisted T2 inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Inhibition of T2 phage by MqsR/MqsA/MqsC in "
                        "concert with restriction/modification systems."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "MqsRAC system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded MqsRAC "
                        "toxin-antitoxin-chaperone phage-defense system."
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
                    "subject": "mqsrac_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "mqsrac_persister_formation",
                    "description": (
                        "Fernandez-Garcia et al. show that the "
                        "MqsR/MqsA/MqsC toxin-antitoxin-chaperone system "
                        "can promote persister-cell formation during T2 "
                        "attack, and DefenseFinder models MqsRAC as a "
                        "two-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": FERNANDEZ_PMID,
                            "snippet": MQSRAC_PERSISTER_SNIPPET,
                            "notes": (
                                "Fernandez-Garcia et al. connect the MqsRAC "
                                "system to persister-cell formation."
                            ),
                        },
                        {
                            "reference": FERNANDEZ,
                            "snippet": MQSRAC_TRIPARTITE_SNIPPET,
                            "notes": (
                                "Fernandez-Garcia et al. identify the "
                                "system components as MqsR, MqsA, and MqsC."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "mqsrac_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "rm_assisted_t2_inhibition",
                    "description": (
                        "Fernandez-Garcia et al. report that the "
                        "MqsR/MqsA/MqsC toxin-antitoxin-chaperone system "
                        "works in concert with restriction/modification "
                        "systems during T2 inhibition."
                    ),
                    "evidence": [
                        {
                            "reference": FERNANDEZ,
                            "snippet": MQSRAC_MCRBC_SNIPPET,
                            "notes": (
                                "Fernandez-Garcia et al. connect the MqsRAC "
                                "system to restriction/modification activity "
                                "during T2 inhibition."
                            ),
                        }
                    ],
                },
                {
                    "subject": "mqsrac_persister_formation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "MqsRAC-dependent survival through persister-cell "
                        "formation realizes the MqsRAC system trait."
                    ),
                    "evidence": [
                        {
                            "reference": FERNANDEZ_PMID,
                            "snippet": MQSRAC_PERSISTER_SNIPPET,
                            "notes": (
                                "Fernandez-Garcia et al. report "
                                "MqsRAC-dependent host survival through "
                                "persister-cell formation rather than cell "
                                "suicide."
                            ),
                        }
                    ],
                },
                {
                    "subject": "rm_assisted_t2_inhibition",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "MqsR/MqsA/MqsC-mediated T2 inhibition realizes "
                        "the MqsRAC system trait."
                    ),
                    "evidence": [
                        {
                            "reference": FERNANDEZ,
                            "snippet": MQSRAC_T2_INHIBITION_SNIPPET,
                            "notes": (
                                "Fernandez-Garcia et al. report reduced "
                                "T2 efficiency of plating in cells producing "
                                "MqsR/MqsA/MqsC."
                            ),
                        }
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "MqsRAC system possession is a "
                        "phage-defense-system trait."
                    ),
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
            "discussion_id": "mqsrac-breadth-and-profile-gap",
            "prompt": (
                "Resolve MqsRAC natural phage breadth, phage-activation "
                "signals, the exact DefenseFinder profile-to-MqsR/MqsA/MqsC "
                "relationship, and cooperating restriction/modification "
                "contexts before minting narrower MqsRAC mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Fernandez-Garcia et al. support MqsR/MqsA/MqsC as an "
                "Escherichia coli C496_10 toxin-antitoxin-chaperone system "
                "that inhibits T2 phage through persister-cell formation "
                "and in concert with restriction/modification systems, "
                "while DefenseFinder models MqsRAC through MqsRAC__mqsC "
                "and MqsRAC__mqsR markers. Natural phage breadth, the "
                "phage signal that activates MqsRAC, MqsA coverage in the "
                "DefenseFinder model, and cooperating "
                "restriction/modification contexts remain unresolved."
            ),
            "evidence": [
                {
                    "reference": FERNANDEZ_PMID,
                    "snippet": MQSRAC_RM_SNIPPET,
                    "notes": (
                        "Fernandez-Garcia et al. leave the MqsRAC and "
                        "restriction/modification connection at "
                        "system-level resolution."
                    ),
                }
            ],
            "attaches_to": [
                "causal_graphs#mqsrac_locus_promotes_persister_phage_defense"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-09-22",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted MqsRAC system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement placeholder "
            f"is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed the MqsRAC canonical_examples gap and left "
            "canonical_examples empty: the current evidence supports a "
            "MqsR/MqsA/MqsC system from Escherichia coli C496_10 expressed "
            "from its natural promoter in a K-12 host, but it does not cite "
            "a directly observed natural microbial taxon broad enough for a "
            "canonical example of endogenous MqsRAC system possession. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="GRAPH_EDGE_DIRECTION_REVIEW",
        changes=(
            "Addressed issue #1258 by replacing the unsupported MqsRAC "
            "persister-cell formation to restriction/modification-assisted "
            "T2 inhibition edge with independent MqsRAC locus to "
            "restriction/modification-assisted T2 inhibition and "
            "MqsRAC-dependent persister formation to MqsRAC system trait "
            "edges."
        ),
        llm_assisted=True,
        timestamp=GRAPH_DIRECTION_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_RESTRICTION_MODIFICATION_SPECIFICITY",
        changes=(
            "Addressed issue #1259 by generalizing unsupported "
            "McrBC-specific wording to restriction/modification-assisted "
            "T2 inhibition throughout the MqsRAC graph and discussion."
        ),
        llm_assisted=True,
        timestamp=RM_SPECIFICITY_REVIEW_TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            existing = yaml.safe_load(TARGET.read_text(encoding="utf-8")) or {}
            if existing.get("identifier") != IDENTIFIER:
                raise SystemExit(
                    f"{rel} already exists with identifier "
                    f"{existing.get('identifier')!r}"
                )
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
