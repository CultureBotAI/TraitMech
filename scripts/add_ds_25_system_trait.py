#!/usr/bin/env python3
"""Add the DS-25 system genomics trait."""

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
from traitmech.validation.write_validated import (  # noqa: E402
    emit_trait_yaml,
    write_validated_trait,
)

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_25_system.yaml"

DEWEIRDT_PREPRINT = "DOI:10.1101/2025.01.08.631726"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-29T20:21:54Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T20:21:55Z"

IDENTIFIER = "traitmech:000473"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v350"

DS_VALIDATION_SNIPPET = (
    "To test for anti-phage defense, we placed each TU with its native "
    "promoter region on a low-copy number plasmid in E. coli MG1655 and "
    "then challenged these strains with a panel of 24 diverse E. coli "
    "phages (fig. S2). In total, 45 (42% of 106) of the cloned TUs "
    "produced smaller plaque sizes or reduced the efficiency of plating "
    "(EOP) at least ten-fold relative to an empty vector control strain"
)
DS_NAMING_SNIPPET = (
    "We refer to these validated TUs as DefensePredictor discovered "
    "Systems (DSs), with genes in multi-gene TUs denoted by an "
    "alphabetical suffix, e.g., DS-8A is the first gene of DS-8."
)
DS_DOMAIN_SNIPPET = (
    "To begin elucidating the function of the 45 validated TUs, we "
    "further annotated their protein domains (see Methods; table S6)."
)
ARTICLE_ROW = (
    "| DS-25 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_PROFILE_SNIPPETS = {
    "DS-25__DS-25A": (
        "| DS-25__DS-25A                                    |"
        "                                                  | DS-25"
        "                  | Custom                  | 80     |"
    ),
    "DS-25__DS-25B": (
        "| DS-25__DS-25B                                    |"
        "                                                  | DS-25"
        "                  | Custom                  | 40     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-25 "
            "source key to the DeWeirdt et al. DefensePredictor preprint."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_PROFILE_SNIPPETS[profile],
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} as a "
            "custom DS-25 profile."
        ),
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_inventory_evidence(profile) for profile in HMM_PROFILE_SNIPPETS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-25 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "genome-encoded DefensePredictor-discovered system 25 locus "
        "represented in the pinned DefenseFinder model inventory by "
        "DS-25A and DS-25B custom HMM profiles."
    ),
    "definition_source": DEWEIRDT_PREPRINT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "DS-25",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "DS-25__DS-25A",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "DS-25__DS-25B",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": DEWEIRDT_PREPRINT,
            "snippet": DS_VALIDATION_SNIPPET,
            "notes": (
                "DeWeirdt et al. experimentally validated 45 predicted "
                "transcriptional units as phage-defense systems in E. coli; "
                "the first-pass DS-25 record uses this source only for the "
                "DefensePredictor DS naming context, not for an exact DS-25 "
                "phage readout."
            ),
        },
        {
            "reference": DEWEIRDT_PREPRINT,
            "snippet": DS_NAMING_SNIPPET,
            "notes": (
                "DeWeirdt et al. name validated transcriptional units as "
                "DefensePredictor discovered Systems."
            ),
        },
        {
            "reference": DEWEIRDT_PREPRINT,
            "snippet": DS_DOMAIN_SNIPPET,
            "notes": (
                "DeWeirdt et al. describe Table S6 as a protein-domain "
                "annotation table for the validated DS transcriptional "
                "units; the exact preprint DS-25 row was not recovered in "
                "this curation pass."
            ),
        },
        article_registry_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_25_locus_profile_model",
            "title": "DS-25 locus profile model",
            "description": (
                "Conservative system-level sketch linking the DS-25 "
                "DefensePredictor-discovered system key to DS-25 system "
                "possession and the broader phage-defense-system trait "
                "without resolving DS-25 component function or a phage "
                "activity readout."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-25 as a DefensePredictor-discovered "
                "system with DS-25A and DS-25B custom HMM rows in the "
                "pinned DefenseFinder HMM inventory. It does not assert the "
                "preprint working identifier, preprint Table S5/S6 rows, "
                "final Science supplement rows, native host breadth, "
                "profile-to-protein correspondence, DS-25A or DS-25B "
                "molecular activity, exact phage target breadth, or "
                "DefenseFinder rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_25_locus",
                    "label": "DS-25 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefensePredictor-discovered system 25 locus "
                        "represented in the pinned DefenseFinder HMM "
                        "inventory by DS-25A and DS-25B custom profiles."
                    ),
                },
                {
                    "node_id": "ds_25_system_trait",
                    "label": "DS-25 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-25 phage-defense "
                        "system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PHAGE_DEFENSE_SYSTEM,
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "ds_25_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "ds_25_system_trait",
                    "description": (
                        "DefenseFinder links the DS-25 source key to the "
                        "DefensePredictor preprint and represents DS-25 in "
                        "the HMM inventory with DS-25A and DS-25B custom "
                        "profiles."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "ds_25_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-25 system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEWEIRDT_PREPRINT,
                            "snippet": DS_NAMING_SNIPPET,
                            "notes": (
                                "DeWeirdt et al. name validated TUs as "
                                "DefensePredictor discovered Systems."
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
            "discussion_id": "ds-25-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-25 working-identifier rows, preprint Table S5 "
                "and S6 context, final Science supplement omission, native "
                "host breadth, DS-25A/DS-25B profile-to-protein mapping, "
                "sensitive-phage breadth, molecular output, and rule-level "
                "DefenseFinder criteria before minting narrower DS-25 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The DeWeirdt et al. preprint supports the DefensePredictor "
                "discovered System naming convention, the pinned "
                "DefenseFinder article registry names DS-25 and maps it to "
                "that preprint, and the pinned HMM inventory records "
                "DS-25A and DS-25B custom profile rows. DS-25 is absent from "
                "the final Science Table S6, S7, and S8 files checked during "
                "this curation pass, the exact preprint per-TU rows were not "
                "recovered, the pinned DefenseFinder rules table has no "
                "DS-25 row, and the first-pass record does not resolve the "
                "working identifier, assayed phages, phage readout, native "
                "host, profile-to-component mapping, component activities, or "
                "complete detection criteria."
            ),
            "evidence": [
                {
                    "reference": DEWEIRDT_PREPRINT,
                    "snippet": DS_VALIDATION_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. validate predicted transcriptional "
                        "units by measuring plaquing relative to an empty "
                        "vector control strain."
                    ),
                },
                {
                    "reference": DEWEIRDT_PREPRINT,
                    "snippet": DS_NAMING_SNIPPET,
                    "notes": "DeWeirdt et al. name validated TUs as DSs.",
                },
                {
                    "reference": DEWEIRDT_PREPRINT,
                    "snippet": DS_DOMAIN_SNIPPET,
                    "notes": (
                        "DeWeirdt et al. describe Table S6 as further "
                        "protein-domain annotation of validated TUs."
                    ),
                },
                article_registry_evidence(),
                *all_hmm_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-25, DS-25A, or DS-25B, leaving complete "
                        "component coverage and rule-level detection "
                        "criteria unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_25_locus_profile_model"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-29",
        }
    ],
}


def validate_output(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


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
            "Minted DS-25 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; kept the "
            "graph at DS-25 source-key and HMM-profile level because "
            "preprint Table S5/S6 rows, final Science supplement rows, "
            f"and rule rows remain unresolved, and {PROPOSAL} reserves the "
            "replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed DS-25 system canonical_examples and left them empty "
            "because the pinned DefenseFinder registries support DS-25 "
            "system identity and custom HMM coverage but not a direct named "
            "native microbial isolate exemplar with experimentally verified "
            "endogenous DS-25 activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    validate_output(record)

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"Wrote {rel}")
    else:
        sys.stdout.write(emit_trait_yaml(record))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
