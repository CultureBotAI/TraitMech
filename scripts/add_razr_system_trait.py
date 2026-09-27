#!/usr/bin/env python3
"""Add the RAZR system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "razr_system.yaml"

ZHANG = "DOI:10.1038/s41586-025-10060-8"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T15:45:19Z"

IDENTIFIER = "traitmech:000411"
PROPOSAL = "proposals/metpo_traitmech_v288"

ARTICLE_ROW = (
    "| RAZR | 10\\.1038/s41586-025-10060-8 | Bacterial immune activation "
    "via supramolecular assembly with phage triggers |"
)
ACTIVE_RING_SNIPPET = "assembles into an active, 24-meric ring"
RING_TRIGGER_SNIPPET = "formed by two unrelated phage proteins"
RNA_OUTPUT_SNIPPET = (
    "cleave RNA nonspecifically to inhibit translation and restrict phage "
    "propagation"
)
RNA_CLEAVAGE_SNIPPET = "enables RAZR to cleave RNA nonspecifically"
TRANSLATION_SNIPPET = "inhibit translation"
PHAGE_RESTRICTION_SNIPPET = "restrict phage propagation"
TRANSLATION_RESTRICTION_SNIPPET = (
    "to inhibit translation and restrict phage propagation"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the named RAZR "
            "system to the Zhang et al. Nature article; the pinned "
            f"DefenseFinder HMM inventory ({DEFENSEFINDER_HMMS}) and rules "
            f"table ({DEFENSEFINDER_RULES}) do not list RAZR, so this row is "
            "name-to-paper evidence rather than model-component evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "RAZR system",
    "definition": (
        "A phage defense system in which an organism possesses a locus "
        "encoding a RAZR zinc-finger HEPN RNase that can form a "
        "phage-triggered higher-order ring complex, cleave RNA broadly, "
        "inhibit translation, and restrict phage propagation."
    ),
    "definition_source": ZHANG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "RAZR",
            "synonym_type": "RELATED_SYNONYM",
            "source": ZHANG,
        }
    ],
    "evidence": [
        {
            "reference": ZHANG,
            "snippet": ACTIVE_RING_SNIPPET,
            "notes": (
                "Zhang et al. define RAZR as a ring-activated zinc-finger "
                "RNase whose phage-triggered higher-order assembly generates "
                "an active 24-subunit ring."
            ),
        },
        {
            "reference": ZHANG,
            "snippet": RNA_OUTPUT_SNIPPET,
            "notes": (
                "Zhang et al. connect activated RAZR complexes to broad RNA "
                "cleavage, translational shutdown, and restriction of phage "
                "growth."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "razr_ring_trigger_restricts_phage",
            "title": "RAZR ring assembly activates RNase defense",
            "description": (
                "Conservative system-level sketch linking a RAZR locus and a "
                "phage ring trigger to RAZR oligomerization, nonspecific RNA "
                "cleavage, translation inhibition, phage-propagation "
                "restriction, and RAZR system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures RAZR as a named phage-defense RNase "
                "activated by phage protein ring scaffolds while leaving "
                "natural hosts, the complete phage-trigger set, exact "
                "RNA-substrate preference, and profile-to-component "
                "DefenseFinder modeling unresolved."
            ),
            "nodes": [
                {
                    "node_id": "razr_locus",
                    "label": "RAZR locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A bacterial locus encoding a ring-activated "
                        "zinc-finger HEPN RNase."
                    ),
                },
                {
                    "node_id": "phage_ring_trigger",
                    "label": "phage ring trigger",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Formation of a phage-encoded protein ring scaffold "
                        "whose geometry can promote RAZR assembly."
                    ),
                },
                {
                    "node_id": "razr_oligomerization",
                    "label": "RAZR oligomerization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Assembly of RAZR into a higher-order active RNase "
                        "ring around a phage protein ring scaffold."
                    ),
                },
                {
                    "node_id": "nonspecific_rna_cleavage",
                    "label": "nonspecific RNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Broad RNA cleavage by activated RAZR ribonuclease "
                        "complexes."
                    ),
                },
                {
                    "node_id": "translation_inhibition",
                    "label": "translation inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Suppression of translation downstream of activated "
                        "RAZR-mediated RNA cleavage."
                    ),
                },
                {
                    "node_id": "phage_propagation",
                    "label": "phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Productive bacteriophage propagation.",
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Restriction of productive phage propagation in "
                        "bacteria carrying activated RAZR defense."
                    ),
                },
                {
                    "node_id": "razr_system_trait",
                    "label": "RAZR system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded RAZR phage-defense "
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
                    "subject": "razr_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "razr_oligomerization",
                    "description": (
                        "A RAZR locus encodes the RNase that assembles into "
                        "an active phage-triggered ring complex."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": ACTIVE_RING_SNIPPET,
                            "notes": (
                                "Zhang et al. connect the RAZR bacterial "
                                "immunity protein to phage-triggered active "
                                "ring assembly."
                            ),
                        },
                    ],
                },
                {
                    "subject": "phage_ring_trigger",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "razr_oligomerization",
                    "description": (
                        "Phage-encoded ring scaffolds provide the geometry "
                        "that activates RAZR assembly."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": RING_TRIGGER_SNIPPET,
                            "notes": (
                                "Zhang et al. show that RAZR activation can "
                                "be triggered by ring scaffolds from "
                                "unrelated phage proteins."
                            ),
                        },
                    ],
                },
                {
                    "subject": "razr_oligomerization",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "nonspecific_rna_cleavage",
                    "description": (
                        "RAZR ring assembly activates broad RNase activity."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": RNA_CLEAVAGE_SNIPPET,
                            "notes": (
                                "Zhang et al. place nonspecific RNA cleavage "
                                "downstream of RAZR complex formation."
                            ),
                        },
                    ],
                },
                {
                    "subject": "nonspecific_rna_cleavage",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "translation_inhibition",
                    "description": (
                        "Broad RAZR-mediated RNA cleavage inhibits cellular "
                        "translation during phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": TRANSLATION_SNIPPET,
                            "notes": (
                                "Zhang et al. identify translation inhibition "
                                "as an output of activated RAZR-mediated RNA "
                                "cleavage."
                            ),
                        },
                    ],
                },
                {
                    "subject": "translation_inhibition",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_propagation",
                    "description": (
                        "Translation inhibition caused by RAZR activation "
                        "restricts phage propagation."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": PHAGE_RESTRICTION_SNIPPET,
                            "notes": (
                                "Zhang et al. connect RAZR-dependent "
                                "translation inhibition to restricted phage "
                                "propagation."
                            ),
                        },
                    ],
                },
                {
                    "subject": "translation_inhibition",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "RAZR-associated translation inhibition realizes "
                        "restriction of phage propagation."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": TRANSLATION_RESTRICTION_SNIPPET,
                            "notes": (
                                "Zhang et al. report that the same activated "
                                "RAZR RNase output inhibits translation and "
                                "restricts phage propagation."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "razr_system_trait",
                    "description": (
                        "RAZR-mediated phage restriction realizes the RAZR "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": RNA_OUTPUT_SNIPPET,
                            "notes": (
                                "Zhang et al. support restricted phage "
                                "propagation as an output of active RAZR "
                                "defense complexes."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "razr_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "RAZR system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": ZHANG,
                            "snippet": ACTIVE_RING_SNIPPET,
                            "notes": (
                                "Zhang et al. frame RAZR as a bacterial "
                                "immune RNase whose activated state restricts "
                                "phage propagation."
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
            "discussion_id": "razr-trigger-model-gap",
            "prompt": (
                "Resolve RAZR natural hosts, phage ring triggers, "
                "RNA-substrate breadth, and model coverage before minting "
                "narrower RAZR mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Zhang et al. support RAZR as a ring-activated zinc-finger "
                "HEPN RNase that can oligomerize around unrelated phage ring "
                "scaffolds, but natural locus breadth, the full phage-trigger "
                "set, exact RNA-substrate preference, and absence from the "
                "pinned DefenseFinder HMM/rules rows need further review."
            ),
            "attaches_to": ["causal_graphs#razr_ring_trigger_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}"
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted RAZR system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; left canonical_examples empty until direct "
            "native-locus evidence supports a microbial exemplar; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
