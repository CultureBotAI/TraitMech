#!/usr/bin/env python3
"""Add the PrrC system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "prrc_system.yaml"

UZAN = "DOI:10.1186/1743-422X-7-360"
UZAN_PMID = "PMID:21129205"
UZAN_SNIPPET = (
    "phage exclusion systems that involve T4-mediated activation of a latent "
    "endoribonuclease (PrrC) and cofactor-assisted activation of EF-Tu "
    "proteolysis (Gol-Lit)"
)
BLANGA_KANFI_PMID = "PMID:16790566"
PRRC_ASSOCIATION_SNIPPET = (
    "The tRNA(Lys) anticodon nuclease PrrC is associated in latent form with "
    "the type Ic DNA restriction endonuclease EcoprrI and activated by a phage "
    "T4-encoded inhibitor of EcoprrI."
)
PRRC_HOMOLOG_SNIPPET = (
    "This triad exists in all the known PrrC homologs but only some of them "
    "feature residues needed for tRNA(Lys) recognition by the Escherichia "
    "coli prototype."
)
PRRC_RESTRICTION_RNASE_SNIPPET = (
    "The differential conservation and consistent genetic linkage of the PrrC "
    "proteins with EcoprrI homologs portray them as a family of restriction "
    "RNases of diverse substrate specificities that are mobilized when an "
    "associated DNA restriction nuclease is compromised."
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
TIMESTAMP = "2026-09-22T11:25:19Z"
CANONICAL_EXAMPLES_TIMESTAMP = "2026-09-22T11:39:03Z"
PR_REVIEW_TIMESTAMP = "2026-09-22T11:42:52Z"
IDENTIFIER = "traitmech:000364"
PROPOSAL = "proposals/metpo_traitmech_v241"
SLUG = "prrc"

ARTICLE_REGISTRY_SNIPPET = (
    "PrrC | 10\\.1186/1743-422X-7-360 | Post-transcriptional control "
    "by bacteriophage T4: mRNA decay and inhibition of translation initiation"
)
RULES_SNIPPET = (
    "PrrC\tPrrC\t2\t2\tPrrC__EcoprrI, PrrC__PrrC\t"
    "RM__Type_I_REases, RM__Type_I_S"
)
HMM_ROWS = {
    "PrrC__EcoprrI": (
        "| PrrC__EcoprrI                                    | "
        "PrrC__EcoprrI                                    | "
        "PrrC                   | Custom                  | 20     |"
    ),
    "PrrC__PrrC": (
        "| PrrC__PrrC                                       | "
        "PrrC__PrrC                                       | "
        "PrrC                   | Custom                  | 100    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named PrrC system "
            "to the Uzan et al. T4 post-transcriptional-control review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models PrrC as a two-profile "
            "system requiring the PrrC__EcoprrI and PrrC__PrrC profiles, "
            "with type I restriction-modification components as accessory "
            "markers."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": f"The DefenseFinder HMM inventory records {profile} under PrrC.",
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PrrC system",
    "definition": (
        "A phage defense system in which an organism possesses a PrrC "
        "locus represented by DefenseFinder as a two-profile model "
        "requiring PrrC__EcoprrI and PrrC__PrrC, with type I "
        "restriction-modification components accepted as accessory markers."
    ),
    "definition_source": UZAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PrrC",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
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
            "reference": UZAN_PMID,
            "snippet": UZAN_SNIPPET,
            "notes": (
                "Uzan et al. name PrrC as a T4-mediated phage-exclusion "
                "system that activates a latent endoribonuclease."
            ),
        },
        {
            "reference": BLANGA_KANFI_PMID,
            "snippet": PRRC_ASSOCIATION_SNIPPET,
            "notes": (
                "Blanga-Kanfi et al. support latent PrrC association with "
                "the EcoprrI restriction endonuclease and activation by a "
                "T4-encoded EcoprrI inhibitor."
            ),
        },
        {
            "reference": BLANGA_KANFI_PMID,
            "snippet": PRRC_HOMOLOG_SNIPPET,
            "notes": (
                "Blanga-Kanfi et al. support a family of PrrC homologs "
                "whose substrate-recognition residues can differ from the "
                "Escherichia coli prototype."
            ),
        },
        {
            "reference": BLANGA_KANFI_PMID,
            "snippet": PRRC_RESTRICTION_RNASE_SNIPPET,
            "notes": (
                "Blanga-Kanfi et al. support genetic linkage between PrrC "
                "proteins and EcoprrI homologs as a restriction-RNase "
                "family mobilized when an associated restriction nuclease is "
                "compromised."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "prrc_locus_restricts_t4_phage",
            "title": "PrrC loci confer T4 phage exclusion",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "PrrC locus to T4-induced PrrC restriction-RNase defense "
                "without asserting the exact T4 trigger, natural substrate, "
                "or accessory component logic."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PrrC as a named DefenseFinder "
                "two-profile phage-exclusion system while leaving natural "
                "homolog substrate specificity, the exact EcoprrI accessory "
                "composition and profile matching, the phage trigger logic, "
                "and PrrC profile-to-activity mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "prrc_locus",
                    "label": "PrrC locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder PrrC phage-defense locus "
                        "represented by PrrC__EcoprrI and PrrC__PrrC "
                        "profiles."
                    ),
                },
                {
                    "node_id": "t4_induced_prrc_rnase_defense",
                    "label": "T4-induced PrrC RNase defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Mobilization of a PrrC-family restriction RNase "
                        "during bacteriophage T4 interference with the "
                        "associated EcoprrI restriction nuclease."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "PrrC system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PrrC phage-defense "
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
                    "subject": "prrc_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "t4_induced_prrc_rnase_defense",
                    "description": (
                        "PrrC proteins are genetically linked with EcoprrI "
                        "homologs and can be mobilized when associated DNA "
                        "restriction nucleases are compromised, and "
                        "DefenseFinder models PrrC as a two-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": UZAN_PMID,
                            "snippet": UZAN_SNIPPET,
                            "notes": (
                                "Uzan et al. identify PrrC as a latent "
                                "endonuclease participating in T4-mediated "
                                "phage exclusion."
                            ),
                        },
                        {
                            "reference": BLANGA_KANFI_PMID,
                            "snippet": PRRC_ASSOCIATION_SNIPPET,
                            "notes": (
                                "Blanga-Kanfi et al. connect PrrC to "
                                "EcoprrI and T4 inhibitor-triggered "
                                "activation."
                            ),
                        },
                        {
                            "reference": BLANGA_KANFI_PMID,
                            "snippet": PRRC_RESTRICTION_RNASE_SNIPPET,
                            "notes": (
                                "Blanga-Kanfi et al. generalize PrrC "
                                "homologs as EcoprrI-linked restriction "
                                "RNases."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "t4_induced_prrc_rnase_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "T4-induced PrrC RNase defense realizes the PrrC "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BLANGA_KANFI_PMID,
                            "snippet": PRRC_ASSOCIATION_SNIPPET,
                            "notes": (
                                "Blanga-Kanfi et al. support latent PrrC "
                                "activation by a T4-encoded inhibitor of "
                                "EcoprrI."
                            ),
                        },
                        {
                            "reference": BLANGA_KANFI_PMID,
                            "snippet": PRRC_RESTRICTION_RNASE_SNIPPET,
                            "notes": (
                                "Blanga-Kanfi et al. support broader "
                                "mobilization of EcoprrI-linked PrrC-family "
                                "restriction RNases."
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
                        "PrrC system possession is a phage-defense-system "
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
            "discussion_id": "prrc-mechanism-gap",
            "prompt": (
                "Resolve natural PrrC homolog substrate specificity, exact "
                "EcoprrI accessory composition and profile matching, and "
                "phage trigger logic before minting narrower PrrC mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Uzan et al. summarize PrrC as a T4 phage-exclusion system, "
                "Blanga-Kanfi et al. support PrrC and EcoprrI homologs as "
                "genetically linked restriction RNases, and DefenseFinder "
                "models PrrC as a two-profile system with EcoprrI and PrrC "
                "markers plus type I restriction-modification accessories. "
                "The natural substrates, accessory composition, and phage "
                "trigger logic remain unresolved."
            ),
            "attaches_to": ["causal_graphs#prrc_locus_restricts_t4_phage"],
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
            "Minted PrrC system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
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
            "Reviewed the PrrC canonical_examples gap and left "
            "canonical_examples empty: the current evidence supports a named "
            "PrrC phage-exclusion system, the pinned DefenseFinder PrrC "
            "profiles, and EcoprrI-linked PrrC homologs, but does not cite a "
            "directly observed natural microbial taxon with a source-backed "
            "PrrC locus. No paid research was used. Fixes #1247."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLES_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_PR_REVIEW",
        changes=(
            "Resolved PR #1245 review issue #1249 by removing the bare "
            "EcoprrI component name from PrrC system related synonyms while "
            "retaining the DefenseFinder PrrC__EcoprrI profile name and "
            "Blanga-Kanfi evidence for EcoprrI-linked PrrC homologs."
        ),
        llm_assisted=True,
        timestamp=PR_REVIEW_TIMESTAMP,
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
