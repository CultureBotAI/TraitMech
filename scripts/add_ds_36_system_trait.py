#!/usr/bin/env python3
"""Add the DS-36 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ds_36_system.yaml"

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
TIMESTAMP = "2026-09-29T21:04:31Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T21:04:32Z"

IDENTIFIER = "traitmech:000474"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v351"

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
    "| DS-36 | 10\\.1101/2025\\.01\\.08\\.631726 | DefensePredictor: A "
    "machine learning model to discover novel prokaryotic immune systems | "
)
HMM_ROW = (
    "| DS-36__DS-36                                     |"
    "                                                  | DS-36"
    "                  | Custom                  | 200    |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the DS-36 "
            "source key to the DeWeirdt et al. DefensePredictor preprint."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records DS-36__DS-36 "
            "as a custom DS-36 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "DS-36 system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "genome-encoded DefensePredictor-discovered system 36 locus "
        "represented in the pinned DefenseFinder model inventory by the "
        "DS-36 custom HMM profile."
    ),
    "definition_source": DEWEIRDT_PREPRINT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "DS-36",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "DS-36__DS-36",
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
                "the first-pass DS-36 record uses this source only for the "
                "DefensePredictor DS naming context, not for an exact DS-36 "
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
                "units; the exact preprint DS-36 row was not recovered in "
                "this curation pass."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "ds_36_locus_profile_model",
            "title": "DS-36 locus profile model",
            "description": (
                "Conservative system-level sketch linking the DS-36 "
                "DefensePredictor-discovered system key to DS-36 system "
                "possession and the broader phage-defense-system trait "
                "without resolving DS-36 component function or a phage "
                "activity readout."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DS-36 as a DefensePredictor-discovered "
                "system with a DS-36 custom HMM row in the pinned "
                "DefenseFinder HMM inventory. It does not assert the "
                "preprint working identifier, preprint Table S5/S6 rows, "
                "final Science supplement rows, native host breadth, "
                "profile-to-protein correspondence, DS-36 molecular "
                "activity, exact phage target breadth, or DefenseFinder "
                "rule-level detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "ds_36_locus",
                    "label": "DS-36 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefensePredictor-discovered system 36 locus "
                        "represented in the pinned DefenseFinder HMM "
                        "inventory by the DS-36 custom profile."
                    ),
                },
                {
                    "node_id": "ds_36_system_trait",
                    "label": "DS-36 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded DS-36 phage-defense "
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
                    "subject": "ds_36_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "ds_36_system_trait",
                    "description": (
                        "DefenseFinder links the DS-36 source key to the "
                        "DefensePredictor preprint and represents DS-36 in "
                        "the HMM inventory with a DS-36 custom profile."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "ds_36_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DS-36 system possession is a phage-defense-system "
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
            "discussion_id": "ds-36-defensefinder-model-gap",
            "prompt": (
                "Resolve DS-36 working-identifier rows, preprint Table S5 "
                "and S6 context, final Science supplement omission, native "
                "host breadth, DS-36 profile-to-protein mapping, "
                "sensitive-phage breadth, molecular output, and rule-level "
                "DefenseFinder criteria before minting narrower DS-36 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The DeWeirdt et al. preprint supports the DefensePredictor "
                "discovered System naming convention, the pinned "
                "DefenseFinder article registry names DS-36 and maps it to "
                "that preprint, and the pinned HMM inventory records a "
                "DS-36 custom profile row. DS-36 is absent from the final "
                "Science Table S6, S7, and S8 files checked during this "
                "curation pass, the exact preprint per-TU row was not "
                "recovered, the pinned DefenseFinder rules table has no "
                "DS-36 row, and the first-pass record does not resolve the "
                "working identifier, assayed phages, phage readout, native "
                "host, profile-to-component mapping, component activities, "
                "or complete detection criteria."
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
                hmm_inventory_evidence(),
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "The pinned DefenseFinder rules table does not list "
                        "DS-36 or DS-36__DS-36, leaving complete component "
                        "coverage and rule-level detection criteria "
                        "unresolved."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#ds_36_locus_profile_model"],
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
            "Minted DS-36 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; kept the "
            "graph at DS-36 source-key and HMM-profile level because "
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
            "Reviewed DS-36 system canonical_examples and left them empty "
            "because the pinned DefenseFinder registries support DS-36 "
            "system identity and custom HMM coverage but not a direct named "
            "native microbial isolate exemplar with experimentally verified "
            "endogenous DS-36 activity. No paid research was used."
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
