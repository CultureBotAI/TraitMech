#!/usr/bin/env python3
"""Add the plant-endophytic ecology trait."""
from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "ecology" / "endophytic.yaml"
HARDOIM = "DOI:10.1128/MMBR.00050-14"
KANDEL = "DOI:10.3390/microorganisms5040077"
CURATOR = "codex"
TIMESTAMP = "2026-09-28T19:37:27Z"

RECORD = {
    "identifier": "traitmech:000442",
    "label": "endophytic",
    "definition": (
        "A host-associated trait in which a microbe resides within living "
        "internal plant tissues without causing apparent disease in the host."
    ),
    "definition_source": KANDEL,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000049"],
    "synonyms": [
        {
            "synonym_text": "endophyte",
            "synonym_type": "EXACT_SYNONYM",
            "source": KANDEL,
        },
        {
            "synonym_text": "endophytism",
            "synonym_type": "RELATED_SYNONYM",
            "source": HARDOIM,
        },
    ],
    "evidence": [
        {
            "reference": HARDOIM,
            "snippet": (
                "All plants are inhabited internally by diverse microbial "
                "communities comprising bacterial, archaeal, fungal, and "
                "protistic taxa."
            ),
            "notes": (
                "Hardoim et al. frame endophytic lifestyles as internal "
                "microbial residence in plants."
            ),
        },
        {
            "reference": KANDEL,
            "snippet": (
                "Endophytes are microbial symbionts residing within the "
                "plant for the majority of their life cycle without any "
                "detrimental impact to the host plant."
            ),
            "notes": (
                "Kandel et al. support the no-apparent-disease clause in the "
                "endophytic definition."
            ),
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "endophytic_internal_plant_colonization",
            "title": "Internal plant colonization defines endophytism",
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "This broad plant-host habitat trait spans bacteria, archaea, "
                "fungi, and protists and does not assert one universal "
                "molecular colonization mechanism."
            ),
            "description": (
                "Evidence-backed ecological sketch connecting living internal "
                "plant tissue to endophytic residence."
            ),
            "nodes": [
                {
                    "node_id": "internal_plant_tissue",
                    "label": "living internal plant tissue",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "A nonexternal plant host tissue occupied by "
                        "endophytic microbes."
                    ),
                },
                {
                    "node_id": "endophytic_colonization",
                    "label": "endophytic colonization",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Entry, growth, and multiplication of an endophyte "
                        "population within a plant host."
                    ),
                },
                {
                    "node_id": "endophytic_trait",
                    "label": "endophytic",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000442",
                    "description": (
                        "Residence inside living internal plant tissue "
                        "without apparent host disease."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "internal_plant_tissue",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "endophytic_colonization",
                    "description": (
                        "Living plant interiors are the host tissue habitat "
                        "where endophyte populations establish."
                    ),
                    "evidence": [
                        {
                            "reference": KANDEL,
                            "snippet": (
                                "Endophytic colonization refers to the entry, "
                                "growth and multiplication of endophyte "
                                "populations within the host plant."
                            ),
                            "notes": (
                                "Kandel et al. define endophytic colonization "
                                "as establishment inside a plant host."
                            ),
                        }
                    ],
                },
                {
                    "subject": "endophytic_colonization",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "endophytic_trait",
                    "description": (
                        "Endophytic colonization realizes the endophytic "
                        "ecological trait."
                    ),
                    "evidence": [
                        {
                            "reference": KANDEL,
                            "snippet": (
                                "Endophytes are microbial symbionts residing "
                                "within the plant for the majority of their "
                                "life cycle without any detrimental impact to "
                                "the host plant."
                            ),
                            "notes": (
                                "Kandel et al. define endophytes by internal "
                                "plant residence without detrimental host "
                                "impact."
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
            "Minted endophytic as a DOI-backed ECOLOGY TraitRecord below "
            "host-associated after an ignored-and-hidden repository search "
            "found no exact TraitMech, METPO, proposal, or history record; "
            "reserved the upstream placeholder in proposals/metpo_traitmech_v319."
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
            "rather than promoting a strain-level growth-promotion or nitrogen-"
            "fixation study into generic endophytism evidence."
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
