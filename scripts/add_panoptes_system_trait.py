#!/usr/bin/env python3
"""Add the Panoptes system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "panoptes_system.yaml"

SULLIVAN = "DOI:10.1038/s41586-025-09557-z"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-27T09:24:21Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T09:24:22Z"
POSED_DATE = "2026-09-27"
IDENTIFIER = "traitmech:000407"
PROPOSAL = "proposals/metpo_traitmech_v284"
SLUG = "panoptes"

TWO_GENE_OPERON_SNIPPET = (
    "Panoptes is a two-gene operon, optSE, wherein OptS is predicted to "
    "synthesize a nucleotide-derived second messenger and OptE is predicted to "
    "bind that signal and drive effector-mediated defence."
)
OPTSE_NAMING_SNIPPET = (
    "We named OptSE the Panoptes antiphage system for Argus Panoptes, the "
    "all-seeing, many-eyed giant in Greek mythology who was a faithful "
    "watchman to Hera."
)
OPT_ORTHOLOGUES_CYCLIC_DINUCLEOTIDE_SNIPPET = (
    "OptS orthologues from two distinct Panoptes systems generated cyclic "
    "dinucleotide products, including 2′,3′-cyclic diadenosine monophosphate "
    "(2′,3′-c-di-AMP), which we showed were able to bind the soluble domain "
    "of the OptE transmembrane effector."
)
ACB2_ESCAPE_SNIPPET = (
    "Panoptes potently restricted phage replication, but phages that had "
    "loss-of-function mutations in anti-cyclic oligonucleotide-based "
    "antiphage signalling system (CBASS) protein 2 (Acb2) escaped defence."
)
ACB2_MEMBRANE_RELEASE_SNIPPET = (
    "Our data support the idea that cyclic nucleotide sequestration by Acb2 "
    "releases OptE toxicity, thereby initiating inner membrane disruption, "
    "leading to phage defence."
)
OPTS_REPRESSES_OPTE_SNIPPET = (
    "we found that OptS constitutively produced signalling nucleotides to "
    "repress OptE-mediated growth inhibition."
)
VIBRIO_OPERON_SNIPPET = (
    "We investigated a candidate two-gene Panoptes operon from Vibrio "
    "navarrensis."
)
VIBRIO_ECOLI_CHALLENGE_SNIPPET = (
    "We expressed the operon from its endogenous promoter in Escherichia coli "
    "MG1655 and challenged these bacteria with a panel of diverse phages. The "
    "VnOptSE operon specifically defended against phages from the "
    "Straboviridae family"
)
OPTS_HOLDS_OPTE_SNIPPET = (
    "OptS constitutively synthesizes 2′,3′-c-di-AMP and other cyclic "
    "dinucleotides to hold OptE in an inactive state."
)
ACB2_RELEASES_OPTE_MODEL_SNIPPET = (
    "During phage infection, Acb2 or similar immune evasion proteins are "
    "produced that sequester the OptS-derived signalling molecule, leading "
    "to a population of OptE that is no longer bound to cyclic dinucleotide "
    "and is free to become activated, in turn disrupting the bacterial "
    "membrane and resulting in phage defence"
)
REGISTRY_SNIPPET = (
    "| Panoptes | 10\\.1038/s41586-025-09557-z | The Panoptes system uses "
    "decoy cyclic nucleotides to defend against phage |"
)


def evidence(reference: str, snippet: str, notes: str) -> dict[str, str]:
    return {
        "reference": reference,
        "snippet": snippet,
        "notes": notes,
    }


def two_gene_operon_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        TWO_GENE_OPERON_SNIPPET,
        (
            "Sullivan et al. define Panoptes as the two-gene optSE system "
            "encoding OptS and OptE."
        ),
    )


def optse_naming_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        OPTSE_NAMING_SNIPPET,
        "Sullivan et al. name OptSE as the Panoptes antiphage system.",
    )


def opt_signal_binding_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        OPT_ORTHOLOGUES_CYCLIC_DINUCLEOTIDE_SNIPPET,
        (
            "OptS orthologues produce cyclic dinucleotides, including "
            "2′,3′-c-di-AMP, that can bind the soluble domain of the OptE "
            "transmembrane effector."
        ),
    )


def acb2_escape_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        ACB2_ESCAPE_SNIPPET,
        (
            "Phage replication was restricted by Panoptes, while Acb2 "
            "loss-of-function mutations escaped defense."
        ),
    )


def acb2_membrane_release_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        ACB2_MEMBRANE_RELEASE_SNIPPET,
        (
            "Acb2 cyclic-nucleotide sequestration releases OptE toxicity and "
            "leads to inner-membrane disruption."
        ),
    )


def opts_represses_opte_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        OPTS_REPRESSES_OPTE_SNIPPET,
        (
            "OptS constitutive signalling nucleotide production represses "
            "OptE-mediated growth inhibition."
        ),
    )


def vibrio_operon_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        VIBRIO_OPERON_SNIPPET,
        (
            "Sullivan et al. used a Vibrio navarrensis optSE locus for direct "
            "Panoptes defense assays."
        ),
    )


def vibrio_ecoli_challenge_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        VIBRIO_ECOLI_CHALLENGE_SNIPPET,
        (
            "The V. navarrensis operon was expressed from its endogenous "
            "promoter in E. coli MG1655 and protected the heterologous host "
            "against Straboviridae phages."
        ),
    )


def opts_holds_opte_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        OPTS_HOLDS_OPTE_SNIPPET,
        (
            "The Panoptes model places constitutive OptS cyclic "
            "dinucleotide synthesis upstream of OptE inactive-state "
            "repression."
        ),
    )


def acb2_releases_opte_model_evidence() -> dict[str, str]:
    return evidence(
        SULLIVAN,
        ACB2_RELEASES_OPTE_MODEL_SNIPPET,
        (
            "The Panoptes model links Acb2-like signal sequestration to "
            "OptE activation, bacterial membrane disruption, and phage "
            "defense."
        ),
    )


def registry_evidence() -> dict[str, str]:
    return evidence(
        DEFENSEFINDER_ARTICLES,
        REGISTRY_SNIPPET,
        (
            "The pinned DefenseFinder article registry maps the Panoptes key "
            "to Sullivan et al.; the same pinned rules and HMM inventory "
            "omit a Panoptes model."
        ),
    )


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Panoptes system",
    "definition": (
        "A phage defense system in which an organism possesses a two-gene "
        "optSE locus encoding an OptS minimal CRISPR polymerase synthase that "
        "constitutively produces cyclic dinucleotides and an OptE S-2TMβ "
        "transmembrane effector that is released from cyclic-dinucleotide "
        "repression when phage Acb2-like proteins sequester those signals, "
        "leading to inner-membrane disruption."
    ),
    "definition_source": SULLIVAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Panoptes antiphage system",
            "synonym_type": "EXACT_SYNONYM",
            "source": SULLIVAN,
        },
        {
            "synonym_text": "optSE",
            "synonym_type": "RELATED_SYNONYM",
            "source": SULLIVAN,
        },
        {
            "synonym_text": "OptSE",
            "synonym_type": "RELATED_SYNONYM",
            "source": SULLIVAN,
        },
    ],
    "evidence": [
        two_gene_operon_evidence(),
        optse_naming_evidence(),
        opt_signal_binding_evidence(),
        acb2_escape_evidence(),
        acb2_membrane_release_evidence(),
        vibrio_operon_evidence(),
        vibrio_ecoli_challenge_evidence(),
        registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "panoptes_decoy_cyclic_nucleotide_defense",
            "title": (
                "Panoptes loci couple cyclic-nucleotide sequestration to OptE "
                "membrane disruption"
            ),
            "description": (
                "Evidence-backed process sketch linking an optSE locus to "
                "OptS cyclic-dinucleotide synthesis, OptE repression, "
                "Acb2-like sequestration of the OptS-derived signal, "
                "inner-membrane disruption, and phage restriction."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Sullivan et al. Panoptes evidence without "
                "asserting one universal cyclic-dinucleotide product, "
                "anti-defense trigger, phage breadth, or OptE "
                "oligomerization mechanism across all optSE homologs."
            ),
            "nodes": [
                {
                    "node_id": "optse_locus",
                    "label": "optSE locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene Panoptes locus encoding OptS and OptE."
                    ),
                },
                {
                    "node_id": "opts_cyclic_dinucleotide_synthesis",
                    "label": "OptS cyclic dinucleotide synthesis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Constitutive OptS-dependent production of "
                        "2′,3′-c-di-AMP and other cyclic dinucleotides."
                    ),
                },
                {
                    "node_id": "opte_cyclic_dinucleotide_repression",
                    "label": "OptE cyclic dinucleotide repression",
                    "node_type": "STATE",
                    "description": (
                        "Inactive-state repression of OptE by "
                        "OptS-derived cyclic dinucleotides."
                    ),
                },
                {
                    "node_id": "acb2_like_signal_sequestration",
                    "label": "Acb2-like signal sequestration",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Sequestration or depletion of OptS-derived cyclic "
                        "nucleotides by phage Acb2 or similar immune-evasion "
                        "proteins."
                    ),
                },
                {
                    "node_id": "opte_inner_membrane_disruption",
                    "label": "OptE inner membrane disruption",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "OptE effector toxicity that disrupts the bacterial "
                        "inner membrane during Panoptes defense."
                    ),
                },
                {
                    "node_id": "phage_replication",
                    "label": "phage replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication of bacteriophages that would proceed in "
                        "a susceptible host."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Panoptes system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Panoptes "
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
                    "subject": "optse_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "opts_cyclic_dinucleotide_synthesis",
                    "description": (
                        "The optSE locus encodes OptS, a predicted "
                        "nucleotide-derived second-messenger synthase."
                    ),
                    "evidence": [
                        two_gene_operon_evidence(),
                        opt_signal_binding_evidence(),
                    ],
                },
                {
                    "subject": "opts_cyclic_dinucleotide_synthesis",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "opte_cyclic_dinucleotide_repression",
                    "description": (
                        "OptS-derived cyclic dinucleotides bind OptE and "
                        "hold the effector in an inactive state before "
                        "phage counter-defense challenge."
                    ),
                    "evidence": [
                        opt_signal_binding_evidence(),
                        opts_holds_opte_evidence(),
                    ],
                },
                {
                    "subject": "opte_cyclic_dinucleotide_repression",
                    "predicate": "negatively regulates",
                    "predicate_id": "RO:0002212",
                    "object": "opte_inner_membrane_disruption",
                    "description": (
                        "Cyclic-dinucleotide binding restrains "
                        "OptE-mediated toxicity and inner-membrane "
                        "disruption."
                    ),
                    "evidence": [
                        opts_represses_opte_evidence(),
                    ],
                },
                {
                    "subject": "acb2_like_signal_sequestration",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "opte_inner_membrane_disruption",
                    "description": (
                        "Acb2 or similar immune-evasion proteins sequester "
                        "the OptS-derived signal and release OptE-mediated "
                        "membrane disruption."
                    ),
                    "evidence": [
                        acb2_membrane_release_evidence(),
                    ],
                },
                {
                    "subject": "opte_inner_membrane_disruption",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_replication",
                    "description": (
                        "Panoptes-associated OptE membrane disruption "
                        "restricts bacteriophage replication."
                    ),
                    "evidence": [
                        acb2_escape_evidence(),
                    ],
                },
                {
                    "subject": "opte_inner_membrane_disruption",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "OptE-mediated inner-membrane disruption is the "
                        "phage-defense output that realizes the Panoptes "
                        "system trait."
                    ),
                    "evidence": [
                        acb2_releases_opte_model_evidence(),
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Panoptes system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        two_gene_operon_evidence(),
                        optse_naming_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "panoptes-defensefinder-model-gap",
            "prompt": (
                "Recheck DefenseFinder Panoptes rules and HMM profiles before "
                "using DefenseFinder model rows as optSE profile evidence."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned DefenseFinder article registry maps Panoptes to "
                "Sullivan et al. and the Nature article title, but the pinned "
                "DefenseFinder rules and HMM inventories do not include "
                "Panoptes rows. This record therefore cites the DOI-backed "
                "article and treats the article registry as name-to-paper "
                "evidence rather than as profile support."
            ),
            "evidence": [
                registry_evidence(),
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        },
        {
            "discussion_id": "panoptes-natural-host-gap",
            "prompt": (
                "Find a native endogenous microbial isolate with direct "
                "chromosomal Panoptes antiphage validation before adding "
                "canonical_examples."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Sullivan et al. investigated a candidate Vibrio navarrensis "
                "optSE operon and showed that VnOptSE defended against "
                "Straboviridae phages when expressed in E. coli MG1655 from "
                "its endogenous promoter, but that heterologous challenge "
                "assay does not establish an endogenous V. navarrensis or "
                "E. coli chromosomal Panoptes canonical exemplar."
            ),
            "evidence": [
                vibrio_operon_evidence(),
                vibrio_ecoli_challenge_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#panoptes_decoy_cyclic_nucleotide_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": POSED_DATE,
        },
    ],
}


def write_record(*, apply: bool) -> None:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Panoptes system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement placeholder "
            f"is reserved in {PROPOSAL}."
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
            "Reviewed Panoptes system canonical_examples and left them empty "
            "because the current sources support V. navarrensis VnOptSE "
            "activity in heterologous E. coli MG1655 challenge assays and a "
            "pinned DefenseFinder article-registry row, but not a direct "
            "native microbial isolate exemplar with experimentally verified "
            "endogenous Panoptes activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
    )
    if apply:
        if TARGET.exists():
            raise FileExistsError(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        return

    with tempfile.TemporaryDirectory() as tmp:
        check_path = Path(tmp) / TARGET.name
        write_validated_trait(record, check_path)
        if TARGET.exists():
            if check_path.read_bytes() != TARGET.read_bytes():
                raise SystemExit(
                    f"{TARGET.relative_to(REPO_ROOT)} differs from generated output"
                )
            print(f"{TARGET.relative_to(REPO_ROOT)} matches generated output")
        else:
            print(f"Would write {TARGET.relative_to(REPO_ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    write_record(apply=args.apply)


if __name__ == "__main__":
    main()
