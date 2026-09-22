#!/usr/bin/env python3
"""Add the Lit system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "lit_system.yaml"

COPELAND = "DOI:10.1021/bi0495026"
COPELAND_PMID = "PMID:15196039"
COPELAND_SNIPPET = (
    "Bacteriophage exclusion is a suicide response to viral infection. In "
    "strains of Escherichia coli K-12 infected with T4 phage this process "
    "is mediated by the host-encoded Lit peptidase. Lit is activated by a "
    "unique sequence in the major head protein of the T4 phage (the Gol "
    "sequence) which then cleaves site-specifically the host translation "
    "factor EF-Tu, ultimately leading to cell death."
)
UZAN_PMID = "PMID:21129205"
UZAN_SNIPPET = (
    "phage exclusion systems that involve T4-mediated activation of a latent "
    "endoribonuclease (PrrC) and cofactor-assisted activation of EF-Tu "
    "proteolysis (Gol-Lit)"
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
TIMESTAMP = "2026-09-22T10:38:17Z"
IDENTIFIER = "traitmech:000363"
PROPOSAL = "proposals/metpo_traitmech_v240"
SLUG = "lit"

ARTICLE_REGISTRY_SNIPPET = (
    "Lit | 10\\.1186/1743-422X-7-360 | Post-transcriptional control "
    "by bacteriophage T4: mRNA decay and inhibition of translation initiation"
)
RULES_SNIPPET = "Lit\tLit\t1\t1\tLit__Lit"
HMM_ROWS = {
    "Lit__Lit": (
        "| Lit__Lit                                         | "
        "Lit__Lit                                         | "
        "Lit                    | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named Lit system "
            "to the Uzan et al. T4 post-transcriptional-control review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models Lit as a "
            "single-mandatory-profile system with the Lit__Lit profile."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": f"The DefenseFinder HMM inventory records {profile} under Lit.",
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Lit system",
    "definition": (
        "A phage defense system in which an organism possesses a Lit locus "
        "represented by DefenseFinder as a single-profile model requiring "
        "Lit__Lit."
    ),
    "definition_source": COPELAND,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Lit",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "Gol-Lit",
            "synonym_type": "RELATED_SYNONYM",
            "source": UZAN_PMID,
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
            "reference": COPELAND_PMID,
            "snippet": COPELAND_SNIPPET,
            "notes": (
                "Copeland et al. support host Lit as a T4-activated "
                "bacteriophage-exclusion peptidase that cleaves EF-Tu and "
                "leads to cell death."
            ),
        },
        {
            "reference": UZAN_PMID,
            "snippet": UZAN_SNIPPET,
            "notes": (
                "Uzan et al. name Gol-Lit as a T4 phage-exclusion system "
                "whose output is cofactor-assisted activation of EF-Tu "
                "proteolysis."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "lit_locus_restricts_t4_phage",
            "title": "Lit loci confer T4 phage exclusion",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Lit locus to T4 Gol-Lit phage exclusion without asserting "
                "a protein-resolved Lit mechanism node."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Lit as a named DefenseFinder "
                "single-profile phage-exclusion system while leaving "
                "natural host breadth, non-e14 Lit loci, and the exact "
                "DefenseFinder profile-to-activity mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "lit_locus",
                    "label": "Lit locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder Lit phage-defense locus represented "
                        "by the Lit__Lit profile."
                    ),
                },
                {
                    "node_id": "t4_gol_lit_phage_exclusion",
                    "label": "T4 Gol-Lit phage exclusion",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Bacteriophage T4 exclusion mediated by Gol-activated "
                        "Lit proteolysis of the host translation factor EF-Tu."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Lit system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Lit phage-defense "
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
                    "subject": "lit_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t4_gol_lit_phage_exclusion",
                    "description": (
                        "Lit phage-defense loci can mediate T4 "
                        "bacteriophage exclusion through Gol-activated "
                        "EF-Tu proteolysis, and DefenseFinder models Lit as "
                        "a single-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": COPELAND_PMID,
                            "snippet": COPELAND_SNIPPET,
                            "notes": (
                                "Copeland et al. support Lit-mediated "
                                "bacteriophage exclusion and EF-Tu cleavage."
                            ),
                        },
                        {
                            "reference": UZAN_PMID,
                            "snippet": UZAN_SNIPPET,
                            "notes": (
                                "Uzan et al. identify Gol-Lit as a "
                                "phage-exclusion system mediated by EF-Tu "
                                "proteolysis."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "t4_gol_lit_phage_exclusion",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "T4 Gol-Lit phage exclusion realizes the Lit system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": COPELAND_PMID,
                            "snippet": COPELAND_SNIPPET,
                            "notes": (
                                "Copeland et al. connect host-encoded Lit to "
                                "T4 bacteriophage exclusion."
                            ),
                        },
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Lit system possession is a phage-defense-system "
                        "trait."
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
            "discussion_id": "lit-mechanism-gap",
            "prompt": (
                "Resolve natural Lit loci, host breadth beyond Escherichia "
                "coli K-12 e14, Gol-activation contexts, and Lit__Lit "
                "profile-to-activity mapping before minting narrower Lit "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Copeland et al. support the T4-triggered e14 Lit peptidase "
                "as a bacteriophage-exclusion determinant, Uzan et al. "
                "summarize Gol-Lit as a T4 phage-exclusion system, and "
                "DefenseFinder models Lit as a single-profile system. The "
                "natural host breadth and profile-to-activity mapping remain "
                "unresolved."
            ),
            "attaches_to": ["causal_graphs#lit_locus_restricts_t4_phage"],
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
            "Minted Lit system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
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
