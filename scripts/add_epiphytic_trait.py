#!/usr/bin/env python3
"""Add the plant-epiphytic ecology trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "ecology" / "epiphytic.yaml"
LINDOW = "DOI:10.1128/AEM.69.4.1875-1883.2003"
FONES = "DOI:10.1186/s12915-024-01967-1"
CURATOR = "codex"
TIMESTAMP = "2026-09-28T20:20:16Z"

RECORD = {
    "identifier": "traitmech:000443",
    "label": "epiphytic",
    "definition": (
        "A host-associated trait in which a microbe resides on living aerial "
        "plant surfaces."
    ),
    "definition_source": FONES,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000049"],
    "synonyms": [
        {
            "synonym_text": "epiphyte",
            "synonym_type": "EXACT_SYNONYM",
            "source": FONES,
        },
        {
            "synonym_text": "phyllosphere association",
            "synonym_type": "RELATED_SYNONYM",
            "source": LINDOW,
        },
    ],
    "evidence": [
        {
            "reference": LINDOW,
            "snippet": (
                "The aerial habitat colonized by these microbes is termed the "
                "phyllosphere, and the inhabitants are called epiphytes."
            ),
            "notes": (
                "Lindow and Brandl define epiphytes as microbes inhabiting the "
                "aerial plant-surface phyllosphere."
            ),
        },
        {
            "reference": FONES,
            "snippet": (
                "Epiphytic microbes are those that live for some or all of "
                "their life cycle on the surface of plant leaves."
            ),
            "notes": (
                "Fones et al. support the plant leaf surface-residence scope "
                "of the epiphytic trait."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "epiphytic_plant_surface_colonization",
            "title": "Plant-surface colonization defines epiphytism",
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "This broad plant-host habitat trait spans bacteria, yeasts, "
                "and filamentous fungi on external plant surfaces and does "
                "not assert one universal molecular colonization mechanism."
            ),
            "description": (
                "Evidence-backed ecological sketch connecting exposed living "
                "plant surfaces to epiphytic residence."
            ),
            "nodes": [
                {
                    "node_id": "external_plant_surface",
                    "label": "living external plant surface",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "An aerial external plant host surface occupied by "
                        "epiphytic microbes."
                    ),
                },
                {
                    "node_id": "epiphytic_colonization",
                    "label": "epiphytic colonization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Residence of microbial populations on the surface of "
                        "leaves or other aerial plant parts."
                    ),
                },
                {
                    "node_id": "epiphytic_trait",
                    "label": "epiphytic",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000443",
                    "description": "Residence on living aerial plant surfaces.",
                },
            ],
            "edges": [
                {
                    "subject": "external_plant_surface",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "epiphytic_colonization",
                    "description": (
                        "Living aerial plant surfaces are the host tissue "
                        "habitat where epiphytic populations establish."
                    ),
                    "evidence": [
                        {
                            "reference": LINDOW,
                            "snippet": (
                                "The aerial habitat colonized by these "
                                "microbes is termed the phyllosphere, and the "
                                "inhabitants are called epiphytes."
                            ),
                            "notes": (
                                "Lindow and Brandl define the phyllosphere as "
                                "an aerial plant habitat and its inhabitants "
                                "as epiphytes."
                            ),
                        }
                    ],
                },
                {
                    "subject": "epiphytic_colonization",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "epiphytic_trait",
                    "description": (
                        "Epiphytic colonization realizes the plant-surface "
                        "epiphytic ecological trait."
                    ),
                    "evidence": [
                        {
                            "reference": FONES,
                            "snippet": (
                                "Epiphytic microbes are those that live for "
                                "some or all of their life cycle on the "
                                "surface of plant leaves."
                            ),
                            "notes": (
                                "Fones et al. define epiphytic microbes by "
                                "leaf-surface residence."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted epiphytic as a DOI-backed ECOLOGY TraitRecord below "
            "host-associated after an ignored-and-hidden repository search "
            "found no exact TraitMech, METPO, proposal, or history record; "
            "reserved the upstream placeholder in proposals/metpo_traitmech_v320."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed canonical examples for the first pass and left them empty "
            "rather than promoting a pathogen fitness, biocontrol, or strain-level "
            "plant-growth study into generic epiphytism evidence."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = build_record()
    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
