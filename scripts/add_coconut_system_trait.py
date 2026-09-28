#!/usr/bin/env python3
"""Add the CoCoNuT system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "coconut_system.yaml"

BELL = "DOI:10.7554/eLife.94800.3"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-28T01:05:00Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-28T01:05:01Z"

IDENTIFIER = "traitmech:000422"
PROPOSAL = "proposals/metpo_traitmech_v299"

COCONUT_IDENTITY_SNIPPET = (
    "We focus on a previously uncharacterized branch, which we denote "
    "coiled-coil nuclease tandems (CoCoNuTs) for their salient features: "
    "the presence of extensive coiled-coil structures and tandem nucleases"
)
COCONUT_SUBTYPE_SNIPPET = (
    "We classified the CoCoNuTs into three types and seven subtypes based "
    "on the GTPase domain phylogeny and conserved genomic context"
)
COCONUT_RNA_TARGET_SNIPPET = (
    "all suggesting that the CoCoNuTs target RNA"
)
COCONUT_DNA_TARGET_SNIPPET = (
    "Many CoCoNuTs might additionally target DNA, via McrC nuclease homologs"
)
COCONUT_ANTIPHAGE_SNIPPET = (
    "largely uncharacterized prokaryotic antiphage restriction systems"
)
ARTICLE_ROW = (
    "| CoCoNut | 10\\.7554/eLife\\.94800\\.3 | CoCoNuTs are a diverse "
    "subclass of Type IV restriction systems predicted to target RNA | "
)
HMM_PROFILE_SNIPPETS = {
    "CoCoNut-I-A__I-A_CnuB": (
        "| CoCoNut-I-A__I-A_CnuB                            |"
        "                                                  | CoCoNut-I-A"
        "            | Custom                  | 200    |"
    ),
    "CoCoNut-II__II_CnuH": (
        "| CoCoNut-II__II_CnuH                              |"
        "                                                  | CoCoNut-II"
        "             | Custom                  | 500    |"
    ),
    "CoCoNut-III-B__III-B_CnuHE": (
        "| CoCoNut-III-B__III-B_CnuHE                       |"
        "                                                  | CoCoNut-III-B"
        "          | Custom                  | 750    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the CoCoNut "
            "source key to the Bell et al. versioned eLife article."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom CoCoNut profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "CoCoNuT system",
    "definition": (
        "A phage defense system in which an organism possesses a CoCoNuT "
        "locus from a coiled-coil nuclease tandem branch of McrBC Type IV "
        "restriction systems whose domain and genomic-context architecture "
        "predict RNA targeting and, in many CoCoNuTs, DNA targeting via McrC "
        "nuclease homologs."
    ),
    "definition_source": BELL,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "CoCoNuT",
            "synonym_type": "EXACT_SYNONYM",
            "source": BELL,
        },
        {
            "synonym_text": "CoCoNut",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "CoCoNut-I-A__I-A_CnuB",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "CoCoNut-II__II_CnuH",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "CoCoNut-III-B__III-B_CnuHE",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": BELL,
            "snippet": COCONUT_IDENTITY_SNIPPET,
            "notes": (
                "Bell et al. name CoCoNuTs as coiled-coil nuclease tandem "
                "systems in an uncharacterized McrBC Type IV restriction "
                "branch."
            ),
        },
        {
            "reference": BELL,
            "snippet": COCONUT_SUBTYPE_SNIPPET,
            "notes": (
                "Bell et al. classify CoCoNuTs into multiple types and "
                "subtypes using GTPase phylogeny and conserved genomic "
                "context."
            ),
        },
        {
            "reference": BELL,
            "snippet": COCONUT_RNA_TARGET_SNIPPET,
            "notes": (
                "Bell et al. interpret CoCoNuT domain architecture as "
                "predictive of RNA targeting."
            ),
        },
        {
            "reference": BELL,
            "snippet": COCONUT_DNA_TARGET_SNIPPET,
            "notes": (
                "Bell et al. predict that many CoCoNuTs might also target "
                "DNA via McrC nuclease homologs."
            ),
        },
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "coconut_system_family_hierarchy",
            "title": "CoCoNuT loci are predicted Type IV restriction systems",
            "description": (
                "Conservative system-level sketch linking CoCoNuT system "
                "possession to phage defense without resolving individual "
                "components or a direct molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures CoCoNuT at the named McrBC/Type IV "
                "system-family level with representative CoCoNut-I, "
                "CoCoNut-II, and CoCoNut-III DefenseFinder HMM rows. It "
                "does not assert exact profile-to-protein boundaries, direct "
                "RNA or DNA substrates, native host range, phage range, "
                "subtype boundaries, pseudo-CoCoNuT scope, CARF-regulated "
                "superoperon scope, or rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "coconut_system_trait",
                    "label": "CoCoNuT system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded CoCoNuT Type IV "
                        "restriction-system family locus."
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
                    "subject": "coconut_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "CoCoNuT system possession is treated as a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BELL,
                            "snippet": COCONUT_ANTIPHAGE_SNIPPET,
                            "notes": (
                                "Bell et al. frame EVE/McrB-like Type IV "
                                "restriction-system diversity in the context "
                                "of prokaryotic antiphage restriction."
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
            "discussion_id": "coconut-defensefinder-model-gap",
            "prompt": (
                "Resolve exact CoCoNuT type and subtype boundaries, native "
                "host breadth, direct RNA and DNA substrates, phage range, "
                "pseudo-CoCoNuT scope, CARF-regulated superoperon scope, and "
                "rule-level detection criteria before minting narrower "
                "CoCoNuT mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Bell et al. support CoCoNuTs as a computationally defined "
                "McrBC/Type IV restriction branch predicted to target RNA "
                "and, for many loci, DNA; the pinned DefenseFinder HMM "
                "inventory records custom CoCoNut-I, CoCoNut-II, and "
                "CoCoNut-III profile rows. The pinned rules table has no "
                "CoCoNut row, and the first-pass record leaves exact "
                "profile-to-protein boundaries, pseudo-CoCoNuT inclusion, "
                "natural host breadth, phage range, and substrate-level "
                "mechanism unresolved."
            ),
            "evidence": [
                {
                    "reference": BELL,
                    "snippet": COCONUT_SUBTYPE_SNIPPET,
                    "notes": (
                        "Bell et al. classify CoCoNuTs into type and "
                        "subtype groups using phylogeny and genomic context."
                    ),
                },
                {
                    "reference": BELL,
                    "snippet": COCONUT_RNA_TARGET_SNIPPET,
                    "notes": (
                        "Bell et al. predict RNA targeting from CoCoNuT "
                        "component-domain architectures."
                    ),
                },
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "CoCoNut, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#coconut_system_family_hierarchy"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-28",
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
            "Minted CoCoNuT system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "McrBC/Type IV system-family level because the pinned "
            "DefenseFinder CoCoNut HMM rows are not backed by a rules row; "
            f"{PROPOSAL} reserves the replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed CoCoNuT system canonical_examples and left them empty "
            "because Bell et al. support computationally predicted CoCoNuT "
            "systems and DefenseFinder records CoCoNut HMM profiles, but "
            "the sources do not provide a direct native microbial isolate "
            "exemplar with experimentally verified endogenous CoCoNuT "
            "activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
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
