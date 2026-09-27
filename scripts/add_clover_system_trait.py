#!/usr/bin/env python3
"""Add the Clover system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "clover_system.yaml"

YU = "DOI:10.1038/s41586-026-10135-0"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T19:36:20Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-27T19:36:21Z"
IDENTIFIER = "traitmech:000415"
PROPOSAL = "proposals/metpo_traitmech_v292"

ARTICLE_ROW = (
    "| Clover | 10\\.1038/s41586-026-10135-0 | Nucleotide signals "
    "coordinate activation and inhibition of bacterial immunity |"
)
CLOVER_IDENTITY_SNIPPET = (
    "Here we identify Clover, a bacterial anti-phage defence system "
    "that overcomes this trade-off by encoding a deoxynucleoside "
    "triphosphohydrolase enzyme (CloA) that dynamically responds to "
    "both an activating phage cue and an inhibitory nucleotide immune "
    "signal produced by a partnering regulatory enzyme (CloB)."
)
CLOA_DGTPASE_SNIPPET = (
    "Analysis of phage restriction by Clover in cells and reconstitution "
    "of enzymatic function in vitro demonstrate that CloA is a dGTPase "
    "that responds to viral enzymes that increase cellular levels of dTTP."
)
CLOB_P3DIT_SNIPPET = (
    "To restrain CloA activation in the absence of infection, we show "
    "that CloB synthesizes a dTTP-related inhibitory nucleotide signal, "
    "p3diT"
)
ALLOSTERIC_REGULATION_SNIPPET = (
    "Cryo-electron microscopy structures of CloA in activated and "
    "suppressed states reveal how dTTP and p3diT control distinct "
    "allosteric sites and regulate effector function."
)
COORDINATED_IMMUNITY_SNIPPET = (
    "Our results define how nucleotide signals coordinate both activation "
    "and inhibition of antiviral immunity"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the named "
            "Clover system to the Yu and Kranzusch nucleotide-signal "
            "anti-phage-defense paper. The pinned HMM inventory and "
            "rules table do not list Clover, so this row is name-to-paper "
            "evidence rather than model-component evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Clover system",
    "definition": (
        "A phage defense system in which an organism possesses a Clover "
        "anti-phage system whose CloA deoxynucleoside triphosphohydrolase "
        "dynamically responds to an activating phage cue and to a "
        "CloB-produced inhibitory p3diT nucleotide signal to coordinate "
        "nucleotide-pool disruption during antiviral immunity."
    ),
    "definition_source": YU,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Clover",
            "synonym_type": "EXACT_SYNONYM",
            "source": YU,
        }
    ],
    "evidence": [
        {
            "reference": YU,
            "snippet": CLOVER_IDENTITY_SNIPPET,
            "notes": (
                "Yu and Kranzusch define Clover as a bacterial anti-phage "
                "defence system encoding CloA and CloB."
            ),
        },
        {
            "reference": YU,
            "snippet": CLOA_DGTPASE_SNIPPET,
            "notes": (
                "Yu and Kranzusch support CloA as a Clover dGTPase that "
                "responds to viral enzymes that increase cellular dTTP."
            ),
        },
        {
            "reference": YU,
            "snippet": CLOB_P3DIT_SNIPPET,
            "notes": (
                "Yu and Kranzusch support CloB synthesis of the inhibitory "
                "p3diT nucleotide signal."
            ),
        },
        {
            "reference": YU,
            "snippet": ALLOSTERIC_REGULATION_SNIPPET,
            "notes": (
                "Yu and Kranzusch resolve activated and suppressed CloA "
                "states controlled by dTTP and p3diT."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "clover_dttp_p3dit_regulated_dgtpase",
            "title": "Clover coordinates CloA activation and inhibition",
            "description": (
                "Conservative sketch linking a Clover locus to p3diT-gated "
                "CloA dGTPase activity, regulation of antiviral immunity, "
                "and Clover system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Clover at the experimentally supported "
                "CloA/CloB dGTPase-regulation level without asserting exact "
                "native host breadth, full sensitive-phage breadth, "
                "profile-to-component mappings, or a DefenseFinder detection "
                "rule absent from the pinned model files."
            ),
            "nodes": [
                {
                    "node_id": "clover_locus",
                    "label": "Clover locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Clover anti-phage locus encoding the CloA dGTPase "
                        "and partnering CloB regulatory enzyme."
                    ),
                },
                {
                    "node_id": "cloa_dgtpase_activation",
                    "label": "CloA dGTPase activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of CloA deoxynucleoside "
                        "triphosphohydrolase activity in response to a "
                        "phage cue linked to increased dTTP."
                    ),
                },
                {
                    "node_id": "clob_p3dit_synthesis",
                    "label": "CloB p3diT synthesis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "CloB synthesis of a dTTP-related p3diT inhibitory "
                        "nucleotide signal that suppresses CloA activation "
                        "without infection."
                    ),
                },
                {
                    "node_id": "clover_system_trait",
                    "label": "Clover system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Clover phage-defense "
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
                    "subject": "clover_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "cloa_dgtpase_activation",
                    "description": (
                        "A Clover locus encodes the CloA dGTPase that "
                        "responds to viral enzymes increasing cellular dTTP."
                    ),
                    "evidence": [
                        {
                            "reference": YU,
                            "snippet": CLOVER_IDENTITY_SNIPPET,
                            "notes": (
                                "Yu and Kranzusch identify Clover as the "
                                "system encoding CloA and CloB."
                            ),
                        },
                        {
                            "reference": YU,
                            "snippet": CLOA_DGTPASE_SNIPPET,
                            "notes": (
                                "Yu and Kranzusch connect Clover to "
                                "dTTP-responsive CloA dGTPase activity."
                            ),
                        },
                    ],
                },
                {
                    "subject": "clover_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "clob_p3dit_synthesis",
                    "description": (
                        "A Clover locus encodes CloB, which synthesizes the "
                        "inhibitory p3diT signal."
                    ),
                    "evidence": [
                        {
                            "reference": YU,
                            "snippet": CLOB_P3DIT_SNIPPET,
                            "notes": (
                                "Yu and Kranzusch connect CloB to p3diT "
                                "synthesis."
                            ),
                        },
                    ],
                },
                {
                    "subject": "clob_p3dit_synthesis",
                    "predicate": "negatively regulates",
                    "predicate_id": "RO:0002212",
                    "object": "cloa_dgtpase_activation",
                    "description": (
                        "The CloB-produced p3diT nucleotide signal binds "
                        "CloA and suppresses CloA activation."
                    ),
                    "evidence": [
                        {
                            "reference": YU,
                            "snippet": CLOB_P3DIT_SNIPPET,
                            "notes": (
                                "Yu and Kranzusch support p3diT-dependent "
                                "suppression of CloA activation."
                            ),
                        },
                    ],
                },
                {
                    "subject": "cloa_dgtpase_activation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "clover_system_trait",
                    "description": (
                        "Regulated CloA effector activity realizes Clover "
                        "antiviral immunity."
                    ),
                    "evidence": [
                        {
                            "reference": YU,
                            "snippet": COORDINATED_IMMUNITY_SNIPPET,
                            "notes": (
                                "Yu and Kranzusch frame nucleotide-mediated "
                                "CloA activation and inhibition as "
                                "coordinated antiviral immunity."
                            ),
                        },
                        {
                            "reference": YU,
                            "snippet": ALLOSTERIC_REGULATION_SNIPPET,
                            "notes": (
                                "Yu and Kranzusch show that dTTP and p3diT "
                                "regulate Clover effector function through "
                                "distinct CloA sites."
                            ),
                        },
                    ],
                },
                {
                    "subject": "clover_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Clover system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": YU,
                            "snippet": CLOVER_IDENTITY_SNIPPET,
                            "notes": (
                                "Yu and Kranzusch define Clover as a "
                                "bacterial anti-phage defence system."
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
            "discussion_id": "clover-defensefinder-model-gap",
            "prompt": (
                "Resolve Clover native host breadth, sensitive-phage "
                "breadth, profile-to-component coverage, and "
                "DefenseFinder HMM/rules coverage before minting narrower "
                "Clover mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Yu and Kranzusch support Clover as a bacterial anti-phage "
                "defence system whose CloA dGTPase is activated and "
                "suppressed by nucleotide signals, while the pinned "
                "DefenseFinder article registry names a Clover system. The "
                "pinned DefenseFinder HMM inventory and rules table have no "
                "Clover rows, and the evidence does not yet resolve native "
                "host breadth, full target-phage breadth, or "
                "profile-to-activity modeling."
            ),
            "evidence": [
                {
                    "reference": YU,
                    "snippet": ALLOSTERIC_REGULATION_SNIPPET,
                    "notes": (
                        "Yu and Kranzusch support a CloA/CloB mechanism "
                        "regulated by dTTP and p3diT."
                    ),
                },
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "The pinned DefenseFinder HMM inventory does not "
                        "list Clover, leaving profile-level components "
                        "unresolved."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "Clover, leaving rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": [
                "causal_graphs#clover_dttp_p3dit_regulated_dgtpase"
            ],
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
            "Minted Clover system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; kept the graph at "
            "CloA/CloB dGTPase-regulation level because the pinned "
            "DefenseFinder article row is not backed by pinned HMM or "
            "rules rows; the replacement placeholder is reserved in "
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
            "Reviewed Clover system during canonical-example issue 444 "
            "enforcement and left canonical_examples empty because the "
            "sources support cloned Salmonella enterica and Escherichia "
            "coli operon expression in phage-challenge assays plus a "
            "DefenseFinder article-registry system name, but not a direct "
            "native microbial isolate exemplar with experimentally "
            "verified endogenous Clover activity. No paid research was "
            "used."
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
