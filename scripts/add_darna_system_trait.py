#!/usr/bin/env python3
"""Add the DARNA system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "darna_system.yaml"

PUTEIKIENE = "DOI:10.64898/2026.02.22.705581"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-19T08:54:19Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000273",
    "label": "DARNA system",
    "definition": (
        "A phage defense system in which activated DARNA cleaves a subset "
        "of host tRNAs and thereby inhibits phage propagation after "
        "activation by single-stranded DNA presented by phage SSB."
    ),
    "definition_source": PUTEIKIENE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DARNA",
            "synonym_type": "EXACT_SYNONYM",
            "source": PUTEIKIENE,
        }
    ],
    "evidence": [
        {
            "reference": PUTEIKIENE,
            "snippet": (
                "the bacterial immunity protein DARNA, once activated, "
                "cleaves a subset of host tRNAs, thereby inhibiting phage "
                "propagation"
            ),
            "notes": (
                "Puteikiene et al. support DARNA as a bacterial immunity "
                "protein whose activation leads to host tRNA cleavage and "
                "phage-propagation inhibition."
            ),
        },
        {
            "reference": PUTEIKIENE,
            "snippet": (
                "DARNA is activated by single-stranded DNA presented by "
                "phage SSB, but not by the host SSB"
            ),
            "notes": (
                "Puteikiene et al. support phage SSB-presented "
                "single-stranded DNA as an activation input for DARNA."
            ),
        },
        {
            "reference": PUTEIKIENE,
            "snippet": (
                "The recognition of an endogenous nucleic acid signal "
                "promoted by a viral protein ensures that DARNA can detect "
                "and respond to a broad range of viruses while avoiding "
                "auto-immunity"
            ),
            "notes": (
                "Puteikiene et al. connect DARNA activation to viral-protein "
                "promoted self/non-self discrimination."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "DARNA | 10\\.64898/2026\\.02\\.22\\.705581 | Viral "
                "SSB-bound ssDNA activates the bacterial anti-phage defense "
                "system DARNA"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named DARNA "
                "system to the Puteikiene et al. bacterial anti-phage-system "
                "preprint."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "darna_phage_ssb_ssdna_cleaves_trna",
            "title": "DARNA activation restricts phage propagation through host-tRNA cleavage",
            "description": (
                "Process sketch linking phage SSB-presented "
                "single-stranded DNA to DARNA activation, cleavage of a "
                "subset of host tRNAs, restricted phage propagation, and the "
                "DARNA system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the DOI abstract's DARNA activation and "
                "tRNA-cleavage summary without asserting a DefenseFinder "
                "component profile, universal locus architecture, "
                "strain-resolved component accessions, or the full host and "
                "phage breadth of every natural DARNA system."
            ),
            "nodes": [
                {
                    "node_id": "phage_ssb_presented_ssdna",
                    "label": "phage SSB-presented single-stranded DNA",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Presentation of single-stranded DNA by phage "
                        "single-stranded DNA-binding protein rather than by "
                        "host SSB."
                    ),
                },
                {
                    "node_id": "darna_activation",
                    "label": "DARNA activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of the bacterial immunity protein DARNA "
                        "by phage SSB-presented single-stranded DNA."
                    ),
                },
                {
                    "node_id": "host_trna_cleavage",
                    "label": "host tRNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cleavage of a subset of host tRNAs after DARNA is "
                        "activated."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage after DARNA "
                        "activation and host-tRNA cleavage."
                    ),
                },
                {
                    "node_id": "darna_system_trait",
                    "label": "DARNA system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000273",
                    "description": (
                        "Possession of a genome-encoded DARNA phage-defense "
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
                    "subject": "phage_ssb_presented_ssdna",
                    "predicate": "triggers",
                    "object": "darna_activation",
                    "description": (
                        "Single-stranded DNA presented by phage SSB "
                        "activates DARNA."
                    ),
                    "evidence": [
                        {
                            "reference": PUTEIKIENE,
                            "snippet": (
                                "DARNA is activated by single-stranded DNA "
                                "presented by phage SSB, but not by the host "
                                "SSB"
                            ),
                            "notes": (
                                "Puteikiene et al. directly identify phage "
                                "SSB-presented single-stranded DNA as the "
                                "DARNA activation signal."
                            ),
                        }
                    ],
                },
                {
                    "subject": "darna_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "host_trna_cleavage",
                    "description": "Activated DARNA cleaves a subset of host tRNAs.",
                    "evidence": [
                        {
                            "reference": PUTEIKIENE,
                            "snippet": (
                                "the bacterial immunity protein DARNA, once "
                                "activated, cleaves a subset of host tRNAs"
                            ),
                            "notes": (
                                "Puteikiene et al. connect DARNA activation "
                                "to host-tRNA cleavage."
                            ),
                        }
                    ],
                },
                {
                    "subject": "host_trna_cleavage",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "DARNA-dependent host-tRNA cleavage inhibits phage "
                        "propagation."
                    ),
                    "evidence": [
                        {
                            "reference": PUTEIKIENE,
                            "snippet": (
                                "cleaves a subset of host tRNAs, thereby "
                                "inhibiting phage propagation"
                            ),
                            "notes": (
                                "Puteikiene et al. place phage-propagation "
                                "inhibition downstream of DARNA-mediated "
                                "host-tRNA cleavage."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "darna_system_trait",
                    "description": (
                        "DARNA-mediated phage-propagation inhibition "
                        "realizes the DARNA system trait."
                    ),
                    "evidence": [
                        {
                            "reference": PUTEIKIENE,
                            "snippet": (
                                "DARNA can detect and respond to a broad "
                                "range of viruses while avoiding auto-immunity"
                            ),
                            "notes": (
                                "Puteikiene et al. support the detected viral "
                                "signal and antiviral response as the DARNA "
                                "system output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "darna_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DARNA system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": (
                                "DARNA | 10\\.64898/2026\\.02\\.22\\.705581 | "
                                "Viral SSB-bound ssDNA activates the "
                                "bacterial anti-phage defense system DARNA"
                            ),
                            "notes": (
                                "DefenseFinder associates DARNA with the "
                                "Puteikiene et al. bacterial anti-phage "
                                "defense-system preprint."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "darna-model-profile-gap",
            "prompt": (
                "Resolve DARNA component profiles and locus architecture "
                "before minting component-profile synonyms or narrower DARNA "
                "subsystem traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Puteikiene et al. support DARNA as an anti-phage system "
                "with a resolved phage-SSB single-stranded-DNA trigger and "
                "host-tRNA cleavage output, and DefenseFinder lists DARNA in "
                "its article registry. The pinned DefenseFinder snapshot does "
                "not yet expose DARNA HMM or rule rows, so this first record "
                "does not assert a component-profile synonym or universal "
                "locus architecture."
            ),
            "attaches_to": ["causal_graphs#darna_phage_ssb_ssdna_cleaves_trna"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-19",
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
            "Minted DARNA system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, or prior proposal "
            "record; the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v150."
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
