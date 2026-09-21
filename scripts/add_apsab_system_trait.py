#!/usr/bin/env python3
"""Add the ApsAB system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "apsab_system.yaml"

ZONGO = "DOI:10.1038/s41467-024-48219-y"

ZONGO_ABSTRACT_SYSTEM_SNIPPET = (
    "a novel antiplasmid system ApsAB actively involved in pOXA-48 "
    "destabilization"
)
ZONGO_TARGETS_SNIPPET = (
    "We show that ApsAB targets high and low-copy number plasmids."
)
ZONGO_COMPOSITION_SNIPPET = (
    "ApsAB combines a nuclease/helicase protein and a novel type of "
    "Argonaute-like protein."
)
ZONGO_RENAMING_SNIPPET = (
    "This confirmed that F3141-F3140 corresponds to a novel antiplasmid "
    "defense system that we renamed apsAB for antiplasmid system AB."
)
ZONGO_ELIMINATION_SNIPPET = (
    "These results indicate that ApsAB actively eliminates the plasmid, "
    "likely by promoting its degradation"
)
ZONGO_FAMILY_SNIPPET = (
    "Both systems were found to destabilize a ColE1 multicopy plasmid"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T05:45:03Z"

IDENTIFIER = "traitmech:000328"
PROPOSAL = "proposals/metpo_traitmech_v205"
SYSTEM = "ApsAB"
SLUG = "apsab"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "ApsAB | 10\\.1038/s41467-024-48219-y | An antiplasmid system "
            "drives antibiotic resistance gene integration in "
            "carbapenemase-producing Escherichia coli lineages"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named ApsAB system "
            "to the Zongo et al. Escherichia coli anti-plasmid-system paper; "
            "the pinned DefenseFinder HMM inventory and rules table do not "
            "list ApsAB, so this row is name-to-paper evidence rather than "
            "model-component evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "ApsAB system",
    "definition": (
        "A genomics trait describing possession of an ApsAB anti-plasmid "
        "defense locus encoding the nuclease/helicase ApsA and Argonaute-like "
        "ApsB proteins that can destabilize high- and low-copy-number "
        "plasmids."
    ),
    "definition_source": ZONGO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000188"],
    "synonyms": [
        {
            "synonym_text": SYSTEM,
            "synonym_type": "EXACT_SYNONYM",
            "source": ZONGO,
        },
        {
            "synonym_text": "apsAB",
            "synonym_type": "EXACT_SYNONYM",
            "source": ZONGO,
        },
    ],
    "evidence": [
        {
            "reference": ZONGO,
            "snippet": ZONGO_ABSTRACT_SYSTEM_SNIPPET,
            "notes": (
                "Zongo et al. support ApsAB as a named anti-plasmid system "
                "involved in pOXA-48 destabilization."
            ),
        },
        {
            "reference": ZONGO,
            "snippet": ZONGO_TARGETS_SNIPPET,
            "notes": (
                "Zongo et al. support anti-plasmid activity against both "
                "high- and low-copy-number plasmids."
            ),
        },
        {
            "reference": ZONGO,
            "snippet": ZONGO_COMPOSITION_SNIPPET,
            "notes": (
                "Zongo et al. support a two-component ApsAB system combining "
                "ApsA nuclease/helicase and Argonaute-like ApsB proteins."
            ),
        },
        {
            "reference": ZONGO,
            "snippet": ZONGO_RENAMING_SNIPPET,
            "notes": (
                "Zongo et al. support apsAB as the expanded name for the "
                "F3141-F3140 anti-plasmid defense locus."
            ),
        },
        article_registry_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Zongo et al. identified ApsAB in ST38 Escherichia coli and "
                "found that homologous E. coli ApsAB-like systems also "
                "destabilized a ColE1 multicopy plasmid."
            ),
            "reference": ZONGO,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_destabilizes_plasmids",
            "title": "ApsAB loci destabilize plasmids",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "ApsAB locus to plasmid destabilization without asserting the "
                "unresolved guide source, recognition rule, or degradation "
                "chemistry."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures ApsAB as a named anti-plasmid defense "
                "system while leaving the direct ApsB guide source, the "
                "target-recognition rule, the exact plasmid-degradation "
                "chemistry, the natural plasmid substrate range, family "
                "breadth, and the absence of pinned DefenseFinder HMM or rule "
                "rows unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "ApsAB locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An anti-plasmid defense locus encoding ApsA "
                        "nuclease/helicase and Argonaute-like ApsB "
                        "components."
                    ),
                },
                {
                    "node_id": "plasmid_destabilization",
                    "label": "plasmid destabilization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced maintenance or active elimination of "
                        "plasmids in cells carrying ApsAB."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "ApsAB system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded ApsAB anti-plasmid "
                        "defense locus."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": f"{SLUG}_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "plasmid_destabilization",
                    "description": (
                        "The F3141-F3140 locus was renamed apsAB and ApsAB "
                        "expression promotes plasmid elimination."
                    ),
                    "evidence": [
                        {
                            "reference": ZONGO,
                            "snippet": ZONGO_RENAMING_SNIPPET,
                            "notes": (
                                "Zongo et al. identify F3141-F3140 as the "
                                "ApsAB anti-plasmid system."
                            ),
                        },
                        {
                            "reference": ZONGO,
                            "snippet": ZONGO_ELIMINATION_SNIPPET,
                            "notes": (
                                "Zongo et al. report active ApsAB-mediated "
                                "plasmid elimination after arabinose "
                                "induction."
                            ),
                        },
                        {
                            "reference": ZONGO,
                            "snippet": ZONGO_FAMILY_SNIPPET,
                            "notes": (
                                "Zongo et al. found that homologous E. coli "
                                "ApsAB-like systems can destabilize a ColE1 "
                                "multicopy plasmid."
                            ),
                        },
                    ],
                },
                {
                    "subject": "plasmid_destabilization",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "ApsAB-mediated plasmid destabilization realizes the "
                        "ApsAB system trait."
                    ),
                    "evidence": [
                        {
                            "reference": ZONGO,
                            "snippet": ZONGO_TARGETS_SNIPPET,
                            "notes": (
                                "Zongo et al. support the ApsAB anti-plasmid "
                                "output against high- and low-copy-number "
                                "plasmids."
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
            "discussion_id": "apsab-substrate-and-guide-source-gap",
            "prompt": (
                "Resolve ApsAB guide sources, plasmid substrates, and model "
                "coverage before minting narrower ApsAB mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Zongo et al. support ApsAB as a two-component E. coli "
                "anti-plasmid system and report activity against high- and "
                "low-copy-number plasmids, but the direct ApsB guide source, "
                "the target-recognition rule, exact plasmid-degradation "
                "chemistry, natural substrate range, family-level breadth, "
                "and profile-to-component model are not resolved enough here "
                "to assert narrower mechanistic or subtype traits."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_destabilizes_plasmids"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
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
            "Minted ApsAB system as a DOI-backed GENOMICS TraitRecord under "
            "the quality root after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior proposal "
            f"record; the replacement placeholder is reserved in {PROPOSAL}."
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
