#!/usr/bin/env python3
"""Add the DdmDE system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "ddmde_system.yaml"

JASKOLSKA = "DOI:10.1038/s41586-022-04546-y"
BRAVO = "DOI:10.1038/s41586-024-07515-9"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-19T10:17:05Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000275",
    "label": "DdmDE system",
    "definition": (
        "A genomics trait describing possession of a DdmDE anti-plasmid defense "
        "locus encoding the DNA-guided prokaryotic Argonaute DdmE and the "
        "helicase-nuclease DdmD, whose DNA recognition and handoff trigger "
        "processive plasmid destruction."
    ),
    "definition_source": BRAVO,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000188"],
    "synonyms": [
        {
            "synonym_text": "DdmDE",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": JASKOLSKA,
            "snippet": (
                "two plasmid defence systems conserved in the Vibrio cholerae "
                "El Tor strains"
            ),
            "notes": (
                "Jaskolska et al. support discovery of plasmid-defense systems "
                "in V. cholerae El Tor strains."
            ),
        },
        {
            "reference": JASKOLSKA,
            "snippet": "These systems, termed DdmABC and DdmDE",
            "notes": "Jaskolska et al. identify DdmDE as one of those plasmid-defense systems.",
        },
        {
            "reference": BRAVO,
            "snippet": (
                "DNA defence module DdmDE system, which rapidly eliminates "
                "small, multicopy plasmids"
            ),
            "notes": (
                "Bravo et al. support DdmDE as a plasmid-elimination DNA "
                "defense module."
            ),
        },
        {
            "reference": BRAVO,
            "snippet": "DNA recognition triggers processive plasmid destruction",
            "notes": (
                "Bravo et al. connect target DNA recognition in DdmDE to "
                "processive plasmid destruction."
            ),
        },
        {
            "reference": DEFENSEFINDER_ARTICLES,
            "snippet": (
                "DdmDE | 10\\.1038/s41586-022-04546-y | Two defence systems "
                "eliminate plasmids from seventh pandemic Vibrio cholerae"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named DdmDE "
                "system to the Jaskolska et al. Nature paper."
            ),
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": (
                "DdmDE__DdmD                                      | "
                "DdmDE__DdmD                                      | "
                "DdmDE                  | Custom                  | 20"
            ),
            "notes": "The DefenseFinder HMM inventory records the custom DdmD profile for DdmDE.",
        },
        {
            "reference": DEFENSEFINDER_HMMS,
            "snippet": (
                "DdmDE__DdmE                                      | "
                "DdmDE__DdmE                                      | "
                "DdmDE                  | Custom                  | 20"
            ),
            "notes": "The DefenseFinder HMM inventory records the custom DdmE profile for DdmDE.",
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:666",
            "taxon_label": "Vibrio cholerae",
            "note": (
                "The DdmDE system was characterized from V. cholerae seventh "
                "pandemic strains."
            ),
            "reference": JASKOLSKA,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "ddmde_pago_helicase_plasmid_destruction",
            "title": "DdmDE couples DNA recognition to plasmid destruction",
            "description": (
                "Process sketch linking a DdmDE locus to target DNA "
                "recognition, processive plasmid destruction, plasmid "
                "clearance, and the DdmDE system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the DdmDE activation pathway resolved by "
                "Bravo et al. without asserting every guide-maturation route, "
                "native plasmid substrate, DdmABC cooperation mode, or "
                "Vibrio-specific locus boundary as universal for all DdmDE "
                "systems."
            ),
            "nodes": [
                {
                    "node_id": "ddmde_locus",
                    "label": "DdmDE locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An anti-plasmid defense locus encoding DdmD and DdmE "
                        "components."
                    ),
                },
                {
                    "node_id": "ddmde_dna_recognition",
                    "label": "DdmDE target DNA recognition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DdmDE DNA recognition coordinated by the DNA-targeting "
                        "pAgo DdmE and helicase-nuclease DdmD."
                    ),
                },
                {
                    "node_id": "processive_plasmid_destruction",
                    "label": "processive plasmid destruction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Processive destruction of plasmid DNA after DdmDE "
                        "target recognition."
                    ),
                },
                {
                    "node_id": "plasmid_clearance",
                    "label": "plasmid clearance",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": "Elimination of invasive small multicopy plasmids.",
                },
                {
                    "node_id": "ddmde_system_trait",
                    "label": "DdmDE system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000275",
                    "description": (
                        "Possession of a genome-encoded DdmDE anti-plasmid "
                        "defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "ddmde_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "ddmde_dna_recognition",
                    "description": (
                        "The DdmDE locus encodes DdmE and DdmD components that "
                        "support DdmDE target DNA recognition."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": (
                                "DdmE is a catalytically inactive, DNA-guided, "
                                "DNA-targeting pAgo"
                            ),
                            "notes": (
                                "Bravo et al. define DdmE as the DNA-guided "
                                "DdmDE pAgo component."
                            ),
                        },
                        {
                            "reference": BRAVO,
                            "snippet": (
                                "helicase-nuclease DdmD transitions from an "
                                "autoinhibited, dimeric complex to a monomeric "
                                "state upon loading of single-stranded DNA "
                                "targets"
                            ),
                            "notes": (
                                "Bravo et al. connect DdmD to target-DNA "
                                "loading and the monomeric active state."
                            ),
                        },
                    ],
                },
                {
                    "subject": "ddmde_dna_recognition",
                    "predicate": "triggers",
                    "object": "processive_plasmid_destruction",
                    "description": (
                        "DdmDE DNA recognition triggers processive plasmid "
                        "destruction."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": "DNA recognition triggers processive plasmid destruction",
                            "notes": (
                                "Bravo et al. place plasmid destruction "
                                "downstream of DNA recognition by DdmDE."
                            ),
                        }
                    ],
                },
                {
                    "subject": "processive_plasmid_destruction",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "plasmid_clearance",
                    "description": (
                        "Processive DdmDE-mediated plasmid DNA destruction "
                        "clears invasive plasmids."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": "pAgos utilize ancillary factors to achieve plasmid clearance",
                            "notes": (
                                "Bravo et al. frame DdmD as the ancillary "
                                "factor that helps a pAgo clear plasmids."
                            ),
                        }
                    ],
                },
                {
                    "subject": "plasmid_clearance",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "ddmde_system_trait",
                    "description": (
                        "DdmDE-mediated clearance of small multicopy plasmids "
                        "realizes the DdmDE system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": (
                                "DdmDE system, which rapidly eliminates small, "
                                "multicopy plasmids"
                            ),
                            "notes": (
                                "Bravo et al. support plasmid elimination as "
                                "the DdmDE defense output."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ddmde-substrate-and-guide-source-gap",
            "prompt": (
                "Resolve DdmDE natural guide sources, plasmid-substrate breadth, "
                "and DdmABC cooperation before minting narrower DdmDE mechanism "
                "or subtype traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Jaskolska et al. support DdmDE as a V. cholerae plasmid-"
                "defense system and Bravo et al. resolve how DdmE and DdmD "
                "cooperate for plasmid destruction, but this first system-level "
                "record does not assert a universal guide-maturation route, "
                "full natural plasmid substrate range, or whether cooperation "
                "with DdmABC is required in some hosts."
            ),
            "attaches_to": ["causal_graphs#ddmde_pago_helicase_plasmid_destruction"],
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
            "Minted DdmDE system as a DOI-backed GENOMICS TraitRecord under "
            "the quality root after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, or prior proposal record; "
            "the replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v152."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADVERSARIAL_REVIEW_REPAIR",
        changes=(
            "Resolved #1055 by simplifying the DdmDE causal graph to a "
            "source-supported target-DNA-recognition sketch and removing "
            "unsupported guide-target handover input edges."
        ),
        llm_assisted=True,
        timestamp="2026-09-19T10:30:00Z",
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
