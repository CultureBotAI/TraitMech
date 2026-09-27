#!/usr/bin/env python3
"""Add the Rst_RT-nitrilase-Tm system genomics trait."""

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

TARGET = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "rst_rt_nitrilase_tm_system.yaml"
)

ROUSSET = "DOI:10.1016/j.chom.2022.02.018"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/"
    "ee7647d8/content/3.defense-systems/rst_rt-nitrilase-tm.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-27T06:35:23Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T06:35:24Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000403"
PROPOSAL = "proposals/metpo_traitmech_v280"
SLUG = "rst_rt_nitrilase_tm"

ROUSSET_RT_SNIPPET = (
    "with a C-terminal nitrilase domain (Table S3) that is associated "
    "with a transmembrane effector"
)
ROUSSET_VALIDATED_DEFENSES_SNIPPET = (
    "Phage resistance heatmap of the validated defense systems shows "
    "the mean fold resistance of three independent replicates against "
    "a panel of eight phages"
)
WIKI_DESCRIPTION_SNIPPET = (
    "RT-nitrilase-Tm (also named UG5-large) is a two-gene defense "
    "system. It was discovered from P4-like satellites in *E. coli* "
    "genomes :ref{doi=10.1016/j.chom.2022.02.018} "
    ":ref{doi=10.1093/nar/gkac467}. Its antiphage activity was "
    "shown in *E. coli* against phage AL505_P2 (Myoviridae)."
)
WIKI_COMPONENT_SNIPPET = (
    "The first protein is a reverse transcriptase (RT) fussed with C-N "
    "hydrolase domain (nitrilase); the second protein is transmembrane "
    "protein :ref{doi=10.1093/nar/gkac467}."
)
WIKI_STRUCTURE_SNIPPET = (
    "The Rst_RT-nitrilase-Tm is composed of 2 proteins: RT and RT-Tm."
)
WIKI_REFSEQ_SNIPPET = (
    "The Rst_RT-Tm system in *Morganella morganii* "
    "(GCF_900478755.1, NZ_LS483498) is composed of 2 proteins RT "
    "(WP_061057569.1) RT-Tm (WP_004234654.1)"
)
WIKI_PROTECTS_SNIPPET = "Expressed_0[Escherichia coli] ----> Al505_P2"
ARTICLE_REGISTRY_SNIPPET = (
    "Rst_RT-nitrilase-Tm | 10\\.1101/2021\\.01\\.21\\.427644 | "
    "Prophage-encoded hotspots of bacterial immune systems"
)
RULES_SNIPPET = (
    "Rst_RT-nitrilase-Tm\tRst_RT-Tm\t2\t2\t"
    "Rst_RT-Tm__RT, Rst_RT-Tm__RT-Tm\t\t\t"
)
HMM_PROFILES = (
    ("Rst_RT-Tm__RT", "Rst_RT-Tm__RT", "500"),
    ("Rst_RT-Tm__RT2", "", "100"),
    ("Rst_RT-Tm__RT-Tm", "Rst_RT-Tm__RT-Tm", "100"),
)
HMM_SNIPPET = "\n".join(
    f"| {gene_name:<49}| {hmm_name:<49}| {'Rst_RT-Tm':<23}| "
    f"{'Custom':<24}| {ga_cut:<7}|"
    for gene_name, hmm_name, ga_cut in HMM_PROFILES
)


def rousset_rt_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_RT_SNIPPET,
        "notes": (
            "Rousset et al. described a validated P4-hotspot system "
            "containing a group-5 reverse transcriptase with a C-terminal "
            "nitrilase domain associated with a transmembrane effector."
        ),
    }


def rousset_validated_defenses_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": ROUSSET_VALIDATED_DEFENSES_SNIPPET,
        "notes": (
            "The Figure 2 legend frames the cloned P4-hotspot hits, "
            "including the RT-nitrilase plus one-TM system, as validated "
            "defense systems in a replicated phage-resistance heatmap."
        ),
    }


def wiki_description_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_DESCRIPTION_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page names RT-nitrilase-Tm, "
            "also called UG5-large, as a two-gene system and records "
            "AL505_P2 antiphage activity in Escherichia coli."
        ),
    }


def wiki_component_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_COMPONENT_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page describes the "
            "reverse-transcriptase/nitrilase plus transmembrane-protein "
            "architecture."
        ),
    }


def wiki_structure_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_STRUCTURE_SNIPPET,
        "notes": (
            "The pinned DefenseFinder wiki page maps the Rst-prefixed "
            "name to a two-component RT/RT-Tm structure."
        ),
    }


def wiki_refseq_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted two-protein "
            "Rst_RT-Tm locus in RefSeq assembly GCF_900478755.1 on "
            "NZ_LS483498."
        ),
    }


def wiki_protects_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": WIKI_PROTECTS_SNIPPET,
        "notes": (
            "The DefenseFinder experimental-validation diagram links "
            "Escherichia coli expression of the Rst_RT-nitrilase-Tm "
            "system to protection against AL505_P2."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named "
            "Rst_RT-nitrilase-Tm system to the Rousset et al. preprint."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table maps Rst_RT-nitrilase-Tm to a "
            "two-profile Rst_RT-Tm model requiring RT and RT-Tm profiles."
        ),
    }


def hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The DefenseFinder HMM inventory records the RT, alternate "
            "RT2, and RT-Tm profiles under the normalized Rst_RT-Tm "
            "system namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Rst_RT-nitrilase-Tm system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "two-protein Rst_RT-nitrilase-Tm locus represented by "
        "DefenseFinder as a two-profile Rst_RT-Tm model requiring "
        "Rst_RT-Tm__RT and Rst_RT-Tm__RT-Tm and experimentally linked "
        "to AL505_P2 protection when expressed in Escherichia coli."
    ),
    "definition_source": DEFENSEFINDER_WIKI,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Rst_RT-nitrilase-Tm",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "RT-nitrilase-Tm",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        {
            "synonym_text": "UG5-large",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
        {
            "synonym_text": "Rst_RT-Tm",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile, _, _ in HMM_PROFILES
        ],
        {
            "synonym_text": "RT-Tm",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_WIKI,
        },
    ],
    "evidence": [
        rousset_rt_evidence(),
        rousset_validated_defenses_evidence(),
        wiki_description_evidence(),
        wiki_component_evidence(),
        wiki_structure_evidence(),
        wiki_refseq_evidence(),
        wiki_protects_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rst_rt_nitrilase_tm_locus_restricts_al505_p2",
            "title": "Rst_RT-nitrilase-Tm loci restrict AL505_P2",
            "description": (
                "Conservative system-level sketch linking a named "
                "Rst_RT-nitrilase-Tm two-gene locus model to AL505_P2 "
                "phage resistance."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Rst_RT-nitrilase-Tm as a named "
                "DefenseFinder two-profile phage-defense system while "
                "leaving native host breadth, the exact "
                "Rst_RT-nitrilase-Tm-to-Rst_RT-Tm naming relationship, "
                "RT and RT-Tm molecular roles, the relationship to "
                "UG5-large systems, and the mechanism of AL505_P2 "
                "restriction unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rst_rt_nitrilase_tm_locus",
                    "label": "Rst_RT-nitrilase-Tm locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene reverse-transcriptase/nitrilase plus "
                        "transmembrane-protein phage-defense locus "
                        "represented by the DefenseFinder Rst_RT-Tm "
                        "profiles."
                    ),
                },
                {
                    "node_id": "al505_p2_phage_resistance",
                    "label": "AL505_P2 phage resistance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Resistance against phage AL505_P2 in a host "
                        "expressing an Rst_RT-nitrilase-Tm locus."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Rst_RT-nitrilase-Tm system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded "
                        "Rst_RT-nitrilase-Tm phage-defense system."
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
                    "subject": "rst_rt_nitrilase_tm_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "al505_p2_phage_resistance",
                    "description": (
                        "Rousset et al. linked a group-5 reverse "
                        "transcriptase/nitrilase plus transmembrane "
                        "effector locus to phage resistance, and "
                        "DefenseFinder models Rst_RT-nitrilase-Tm as a "
                        "two-profile Rst_RT-Tm system."
                    ),
                    "evidence": [
                        rousset_rt_evidence(),
                        wiki_component_evidence(),
                        wiki_structure_evidence(),
                        rules_evidence(),
                        hmm_evidence(),
                    ],
                },
                {
                    "subject": "al505_p2_phage_resistance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Rst_RT-nitrilase-Tm-linked AL505_P2 resistance "
                        "realizes the Rst_RT-nitrilase-Tm system trait."
                    ),
                    "evidence": [
                        rousset_validated_defenses_evidence(),
                        wiki_description_evidence(),
                        wiki_protects_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Rst_RT-nitrilase-Tm system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        rousset_validated_defenses_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "rst-rt-nitrilase-tm-host-mechanism-gap",
            "prompt": (
                "Resolve Rst_RT-nitrilase-Tm native host breadth, the "
                "Rst_RT-nitrilase-Tm and Rst_RT-Tm namespace relationship, "
                "accession-level RT/RT-Tm roles, the relationship to "
                "UG5-large source naming, and the mechanism of AL505_P2 "
                "restriction before minting narrower "
                "Rst_RT-nitrilase-Tm mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support a two-gene P4-hotspot system that "
                "combines a group-5 reverse transcriptase with a "
                "C-terminal nitrilase domain and a transmembrane effector, "
                "and DefenseFinder maps Rst_RT-nitrilase-Tm to a required "
                "two-profile Rst_RT-Tm model. This first system-level "
                "record leaves native host breadth, exact profile-to-gene "
                "mapping, the model-namespace mismatch, the relationship "
                "to UG5-large source naming, the molecular activities of "
                "the RT and RT-Tm components, and the AL505_P2 "
                "restriction mechanism unresolved."
            ),
            "evidence": [
                rousset_rt_evidence(),
                wiki_description_evidence(),
                rules_evidence(),
                hmm_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#rst_rt_nitrilase_tm_locus_restricts_al505_p2"
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        }
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    if TARGET.exists():
        raise FileExistsError(f"{TARGET} already exists")
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Rst_RT-nitrilase-Tm system as a DOI/stable-URL-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        curator=CURATOR,
        timestamp=TIMESTAMP,
        llm_assisted=True,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed Rst_RT-nitrilase-Tm during canonical-example issue "
            "444 enforcement and left canonical_examples empty because "
            "the sources support a cloned P4-hotspot RT/RT-Tm locus "
            "assayed in Escherichia coli and a DefenseFinder RefSeq "
            "model example, but not a direct native microbial host "
            "exemplar with experimentally verified Rst_RT-nitrilase-Tm "
            "activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    if apply:
        write_validated_trait(record, TARGET)
    else:
        print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
