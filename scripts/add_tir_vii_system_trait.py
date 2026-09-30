#!/usr/bin/env python3
"""Add the TIR-VII system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "tir_vii_system.yaml"

WANG = "DOI:10.1038/s41467-024-51738-3"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T05:13:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-30T05:13:01Z"
POSED_DATE = "2026-09-30"
IDENTIFIER = "traitmech:000483"
PROPOSAL = "proposals/metpo_traitmech_v360"

WANG_NEW_SYSTEMS_SNIPPET = (
    "Twelve systems have defense activities against a variable number of "
    "phages, and 9 of them are new defense systems and named TIR-I to IX"
)
WANG_PLAQUING_SNIPPET = (
    "The defense activity of the TIR systems against each phage was "
    "determined based on their ability to inhibit plaque formation "
    "compared to the pSEC1 empty vector control"
)
WANG_CONTEXT_SNIPPET = (
    "TIR-I, TIR-III, and TIR-IV systems appear in diverse domains "
    "contexts, whereas the TIR-VII and TIR-VIII systems were found in a "
    "single form"
)
ARTICLE_ROW = (
    "| TIR-VII | 10\\.1038/s41467-024-51738-3 | The role of TIR "
    "domain-containing proteins in bacterial defense against phages |"
)
HMM_PROFILES = (
    "TIR-VII__TIR-VII_A",
    "TIR-VII__TIR-VII_B",
)
HMM_SNIPPET = "\n".join(
    f"| {profile:<49}| {'':<49}| {'TIR-VII':<23}| {'Custom':<24}| {ga_cut:<7}|"
    for profile, ga_cut in (
        ("TIR-VII__TIR-VII_A", "50"),
        ("TIR-VII__TIR-VII_B", "500"),
    )
)


def wang_new_systems_evidence() -> dict[str, str]:
    return {
        "reference": WANG,
        "snippet": WANG_NEW_SYSTEMS_SNIPPET,
        "notes": (
            "Wang et al. report that TIR-VII belongs to nine newly named "
            "TIR-domain anti-phage defense systems with activity against "
            "variable phage subsets."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the named "
            "TIR-VII system to the Wang et al. TIR-domain anti-phage "
            "system paper."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            "TIR-VII__TIR-VII_A and TIR-VII__TIR-VII_B custom profiles "
            "under the TIR-VII system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "TIR-VII system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "TIR-VII locus, represented in the pinned DefenseFinder HMM "
        "inventory by TIR-VII__TIR-VII_A and TIR-VII__TIR-VII_B "
        "custom profiles, that can inhibit bacteriophage plaquing."
    ),
    "definition_source": WANG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "TIR-VII",
            "synonym_type": "EXACT_SYNONYM",
            "source": WANG,
        },
        {
            "synonym_text": HMM_PROFILES[0],
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": HMM_PROFILES[1],
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        wang_new_systems_evidence(),
        {
            "reference": WANG,
            "snippet": WANG_PLAQUING_SNIPPET,
            "notes": (
                "Wang et al. assayed cloned Escherichia coli TIR "
                "systems by efficiency-of-plating reduction against a "
                "phage panel."
            ),
        },
        {
            "reference": WANG,
            "snippet": WANG_CONTEXT_SNIPPET,
            "notes": (
                "Wang et al. found that TIR-VII and TIR-VIII systems "
                "were recovered in a single form, while TIR-I, TIR-III, "
                "and TIR-IV systems occur in diverse domain contexts."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "tir_vii_locus_inhibits_phage_plaquing",
            "title": "TIR-VII loci inhibit bacteriophage plaquing",
            "description": (
                "Conservative system-level sketch linking a TIR-VII "
                "locus to inhibited bacteriophage plaquing and TIR-VII "
                "system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures TIR-VII at TIR-system and "
                "anti-phage assay level without asserting exact native-host "
                "breadth, profile-to-component mapping, a direct phage "
                "trigger, TIR-domain catalytic output, accession-level "
                "components, or a DefenseFinder detection rule absent from "
                "the pinned rules table."
            ),
            "nodes": [
                {
                    "node_id": "tir_vii_locus",
                    "label": "TIR-VII locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A TIR-VII phage-defense locus represented in the "
                        "pinned DefenseFinder HMM inventory by "
                        "TIR-VII__TIR-VII_A and TIR-VII__TIR-VII_B "
                        "custom profiles."
                    ),
                },
                {
                    "node_id": "inhibited_phage_plaquing",
                    "label": "inhibited bacteriophage plaquing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced efficiency of plaquing by bacteriophages "
                        "in cells carrying a complete TIR-VII system."
                    ),
                },
                {
                    "node_id": "tir_vii_system_trait",
                    "label": "TIR-VII system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded TIR-VII "
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
                    "subject": "tir_vii_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "inhibited_phage_plaquing",
                    "description": (
                        "Wang et al. linked TIR-VII to anti-phage "
                        "activity, and DefenseFinder records two custom "
                        "TIR-VII system profiles."
                    ),
                    "evidence": [
                        wang_new_systems_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "inhibited_phage_plaquing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "tir_vii_system_trait",
                    "description": (
                        "TIR-VII-mediated inhibition of bacteriophage "
                        "plaquing realizes the TIR-VII system trait."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": WANG_PLAQUING_SNIPPET,
                            "notes": (
                                "Wang et al. measured cloned TIR-system "
                                "activity by inhibited plaque formation "
                                "relative to an empty-vector control."
                            ),
                        },
                    ],
                },
                {
                    "subject": "tir_vii_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "TIR-VII system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "tir-vii-detection-trigger-gap",
            "prompt": (
                "Resolve TIR-VII native host breadth, the "
                "TIR-VII__TIR-VII_A and TIR-VII__TIR-VII_B "
                "profile-to-component mapping, phage-trigger specificity, "
                "TIR-domain output chemistry, and rule-level "
                "DefenseFinder detection criteria before minting narrower "
                "TIR-VII mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wang et al. support TIR-VII as one of nine newly named "
                "TIR-domain anti-phage defense systems and note that "
                "TIR-VII was recovered in a single form with TIR-VIII. "
                "The pinned DefenseFinder HMM inventory records "
                "TIR-VII__TIR-VII_A and TIR-VII__TIR-VII_B custom profile "
                "rows, but the pinned DefenseFinder rules table has no "
                "TIR-VII row. This first record therefore does not assert "
                "profile requirement logic, accession-level components, a "
                "direct phage trigger, or TIR-domain output chemistry."
            ),
            "evidence": [
                wang_new_systems_evidence(),
                {
                    "reference": WANG,
                    "snippet": WANG_CONTEXT_SNIPPET,
                    "notes": (
                        "Wang et al. report that TIR-VII and TIR-VIII "
                        "were found in a single form."
                    ),
                },
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not "
                        "list TIR-VII, leaving rule-level detection "
                        "criteria unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#tir_vii_locus_inhibits_phage_plaquing"],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
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
            "Minted TIR-VII system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact same-scope live TraitMech, "
            "METPO, history, or prior proposal record; kept the graph at "
            "TIR-system and phage-plaquing level because TIR-VII direct "
            "triggers, profile-to-component mapping, and rule-level "
            "DefenseFinder criteria remain unresolved; the replacement "
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
            "Reviewed TIR-VII system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because Wang "
            "et al. support heterologous E. coli MG1655 plaque assays "
            "and DefenseFinder TIR-VII HMM rows, but the first-pass "
            "curation did not recover a direct named native microbial "
            "isolate exemplar with experimentally verified endogenous "
            "TIR-VII activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
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
