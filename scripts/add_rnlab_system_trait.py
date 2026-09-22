#!/usr/bin/env python3
"""Add the RnlAB system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rnlab_system.yaml"

KOGA = "DOI:10.1534/genetics.110.121798"
KOGA_PMID = "PMID:20980243"
OTSUKA_DMD = "DOI:10.1111/j.1365-2958.2012.07975.x"
OTSUKA_DMD_PMID = "PMID:22403819"

RNASE_LS_T4_SNIPPET = (
    "RNase LS was originally identified as a potential antagonist of "
    "bacteriophage T4 infection. When T4 dmd is defective, RNase LS activity "
    "rapidly increases after T4 infection and cleaves T4 mRNAs to antagonize "
    "T4 reproduction."
)
RNLAB_TA_SNIPPET = (
    "Here we show that rnlA, a structural gene of RNase LS, encodes a novel "
    "toxin, and that rnlB (formally yfjO), located immediately downstream of "
    "rnlA, encodes an antitoxin against RnlA."
)
RNLA_RNLB_INTERACTION_SNIPPET = (
    "Pull-down analysis showed a specific interaction between RnlA and RnlB."
)
RNLAB_NEW_TA_SNIPPET = (
    "All of these results suggested that rnlA-rnlB define a new "
    "toxin-antitoxin (TA) system."
)
EC_K12_CHROMOSOME_SNIPPET = (
    "Predicted proteins encoded by these two ORFs were found to share a weak "
    "homology with RnlA and RnlB, respectively, a toxin–antitoxin system "
    "encoded on the E. coli K-12 chromosome."
)
DMD_DIRECT_INTERACTION_SNIPPET = (
    "T4 phage Dmd suppressed the toxicities of both RnlA and LsoA by direct "
    "interaction, the first example of a phage with an antitoxin against "
    "multiple toxins."
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
TIMESTAMP = "2026-09-22T13:54:00Z"
IDENTIFIER = "traitmech:000367"
PROPOSAL = "proposals/metpo_traitmech_v244"
SLUG = "rnlab"

ARTICLE_REGISTRY_SNIPPET = (
    "RnlAB | 10\\.1534/genetics\\.110\\.121798 | Escherichia coli rnlA "
    "and rnlB compose a novel toxin-antitoxin system"
)
RULES_SNIPPET = "RnlAB\tRnlAB\t2\t2\tRnlAB__RnlA, RnlAB__RnlB\t\t\t"
HMM_ROWS = {
    "RnlAB__RnlA": (
        "| RnlAB__RnlA                                      | "
        "RnlAB__RnlA                                      | "
        "RnlAB                  | Custom                  | 20     |"
    ),
    "RnlAB__RnlB": (
        "| RnlAB__RnlB                                      | "
        "RnlAB__RnlB                                      | "
        "RnlAB                  | Custom                  | 20     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named RnlAB "
            "system to Koga et al.'s rnlA-rnlB toxin-antitoxin paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models RnlAB as a two-profile "
            "system requiring the RnlAB__RnlA and RnlAB__RnlB profiles."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": f"The DefenseFinder HMM inventory records {profile} under RnlAB.",
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "RnlAB system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "genome-encoded RnlAB toxin-antitoxin locus represented by "
        "DefenseFinder as a two-profile model requiring RnlAB__RnlA and "
        "RnlAB__RnlB."
    ),
    "definition_source": KOGA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "RnlAB",
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
            "reference": KOGA_PMID,
            "snippet": RNASE_LS_T4_SNIPPET,
            "notes": (
                "Koga et al. frame RnlA-dependent RNase LS activity as a "
                "potential antagonist of bacteriophage T4 dmd mutants."
            ),
        },
        {
            "reference": KOGA_PMID,
            "snippet": RNLAB_TA_SNIPPET,
            "notes": (
                "Koga et al. identify rnlA as the RNase LS toxin gene and "
                "rnlB as the neighboring cognate antitoxin gene."
            ),
        },
        {
            "reference": KOGA_PMID,
            "snippet": RNLA_RNLB_INTERACTION_SNIPPET,
            "notes": (
                "Koga et al. support direct RnlA/RnlB interaction by pull-down "
                "analysis."
            ),
        },
        {
            "reference": KOGA_PMID,
            "snippet": RNLAB_NEW_TA_SNIPPET,
            "notes": "Koga et al. define rnlA-rnlB as a new toxin-antitoxin system.",
        },
        {
            "reference": OTSUKA_DMD_PMID,
            "snippet": EC_K12_CHROMOSOME_SNIPPET,
            "notes": (
                "Otsuka and Yonesaki describe RnlA/RnlB as a toxin-antitoxin "
                "system encoded on the Escherichia coli K-12 chromosome."
            ),
        },
        {
            "reference": OTSUKA_DMD_PMID,
            "snippet": DMD_DIRECT_INTERACTION_SNIPPET,
            "notes": (
                "Otsuka and Yonesaki support T4 Dmd as a phage antitoxin that "
                "suppresses RnlA toxicity by direct interaction."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:83333",
            "taxon_label": "Escherichia coli K-12",
            "note": (
                "Otsuka and Yonesaki describe the RnlA/RnlB "
                "toxin-antitoxin system as encoded on the Escherichia coli "
                "K-12 chromosome."
            ),
            "reference": OTSUKA_DMD,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "rnlab_locus_antagonizes_t4_dmd_mutants",
            "title": "RnlAB loci support RnlA-dependent RNase LS activity",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "RnlAB locus to RnlA-dependent RNase LS activity against "
                "bacteriophage T4 dmd mutants without asserting a "
                "wild-type-phage trigger, broad phage host range, or exact "
                "RnlAB profile-to-activity mapping."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures RnlAB as a named DefenseFinder "
                "two-profile phage-defense system while leaving natural "
                "phage breadth, wild-type T4 evasion through Dmd, induction "
                "or activation routes in non-T4 contexts, and "
                "RnlAB profile-to-activity mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rnlab_locus",
                    "label": "RnlAB locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A toxin-antitoxin locus represented by "
                        "RnlAB__RnlA and RnlAB__RnlB profiles."
                    ),
                },
                {
                    "node_id": "rnla_dependent_rnase_ls_activity",
                    "label": "RnlA-dependent RNase LS activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "RNase LS activity encoded by rnlA and controlled by "
                        "rnlB, with RnlA capable of cleaving T4 mRNAs when "
                        "phage Dmd is absent."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "RnlAB system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded RnlAB "
                        "toxin-antitoxin phage-defense system."
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
                    "subject": "rnlab_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "rnla_dependent_rnase_ls_activity",
                    "description": (
                        "Koga et al. show that rnlA encodes the RNase LS "
                        "toxin and rnlB encodes the cognate antitoxin; "
                        "DefenseFinder models RnlAB as a two-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": KOGA_PMID,
                            "snippet": RNLAB_TA_SNIPPET,
                            "notes": (
                                "Koga et al. identify rnlA as the RNase LS "
                                "toxin gene and rnlB as the antitoxin gene."
                            ),
                        },
                        {
                            "reference": KOGA_PMID,
                            "snippet": RNLA_RNLB_INTERACTION_SNIPPET,
                            "notes": (
                                "Koga et al. show that RnlA and RnlB "
                                "specifically interact."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "rnla_dependent_rnase_ls_activity",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "RnlA-dependent RNase LS activity against T4 "
                        "dmd-mutant mRNAs realizes the RnlAB system trait."
                    ),
                    "evidence": [
                        {
                            "reference": KOGA_PMID,
                            "snippet": RNASE_LS_T4_SNIPPET,
                            "notes": (
                                "Koga et al. support RNase LS antagonism of "
                                "T4 dmd-mutant reproduction."
                            ),
                        },
                        {
                            "reference": OTSUKA_DMD_PMID,
                            "snippet": DMD_DIRECT_INTERACTION_SNIPPET,
                            "notes": (
                                "Otsuka and Yonesaki show phage Dmd can "
                                "suppress RnlA toxicity by direct interaction."
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
                        "RnlAB system possession is a phage-defense-system "
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
            "discussion_id": "rnlab-phage-breadth-evasion-gap",
            "prompt": (
                "Resolve natural RnlAB phage breadth, wild-type T4 evasion "
                "through Dmd, induction or activation routes in non-T4 "
                "contexts, and RnlAB profile-to-activity mapping before "
                "minting narrower RnlAB mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Koga et al. support RnlA/RnlB as an Escherichia coli K-12 "
                "toxin-antitoxin system whose RNase LS activity can "
                "antagonize T4 dmd mutants, Otsuka and Yonesaki show that "
                "T4 phage Dmd suppresses RnlA toxicity, and DefenseFinder "
                "models RnlAB as a two-profile system with RnlAB__RnlA and "
                "RnlAB__RnlB markers. Natural phage breadth, wild-type T4 "
                "evasion, non-T4 activation contexts, and profile-to-activity "
                "mapping remain unresolved."
            ),
            "evidence": [
                {
                    "reference": OTSUKA_DMD_PMID,
                    "snippet": DMD_DIRECT_INTERACTION_SNIPPET,
                    "notes": (
                        "Otsuka and Yonesaki show that T4 Dmd suppresses "
                        "RnlA toxicity, marking phage evasion as a real "
                        "boundary around RnlAB mechanism curation."
                    ),
                }
            ],
            "attaches_to": [
                "causal_graphs#rnlab_locus_antagonizes_t4_dmd_mutants"
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
            "Minted RnlAB system as a DOI-backed GENOMICS TraitRecord under "
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
