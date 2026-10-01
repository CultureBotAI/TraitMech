#!/usr/bin/env python3
"""Add the bacterial ferrosome morphology trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "morphology" / "ferrosome.yaml"

GRANT = "DOI:10.1038/s41586-022-04741-x"
PI = "DOI:10.1038/s41586-023-06719-9"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T22:05:50Z"
IDENTIFIER = "traitmech:000527"
PROPOSAL = "proposals/metpo_traitmech_v404"


def grant_new_class_evidence() -> dict[str, str]:
    return {
        "reference": GRANT,
        "snippet": (
            "Overall, this work establishes ferrosomes as a new class of "
            "iron storage organelles"
        ),
        "notes": (
            "Grant et al. establish ferrosomes as an iron-storage "
            "organelle class."
        ),
    }


def grant_fez_evidence() -> dict[str, str]:
    return {
        "reference": GRANT,
        "snippet": (
            "we identify three ferrosome-associated (Fez) proteins that "
            "are responsible for forming ferrosomes"
        ),
        "notes": (
            "Grant et al. support Fez protein-dependent ferrosome formation "
            "in Desulfovibrio magneticus."
        ),
    }


def grant_fez_operon_evidence() -> dict[str, str]:
    return {
        "reference": GRANT,
        "snippet": "fez operons are sufficient for ferrosome formation in foreign hosts",
        "notes": (
            "Grant et al. support fez operon sufficiency for ferrosome "
            "formation in heterologous bacterial hosts."
        ),
    }


def pi_iron_phosphate_evidence() -> dict[str, str]:
    return {
        "reference": PI,
        "snippet": (
            "Here we report that C. difficile undergoes an intracellular "
            "iron biomineralization process and stores iron in "
            "membrane-bound ferrosome organelles containing non-crystalline "
            "iron phosphate biominerals."
        ),
        "notes": (
            "Pi et al. support membrane-bound ferrosome organelles storing "
            "non-crystalline iron phosphate in Clostridioides difficile."
        ),
    }


def pi_fezab_evidence() -> dict[str, str]:
    return {
        "reference": PI,
        "snippet": (
            "We found that a membrane protein (FezA) and a P1B6-ATPase "
            "transporter (FezB), repressed by both iron and the ferric "
            "uptake regulator Fur, are required for ferrosome formation"
        ),
        "notes": (
            "Pi et al. support FezA- and FezB-dependent ferrosome formation "
            "in C. difficile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "ferrosome",
    "definition": (
        "A morphology trait in which a bacterial cell forms membrane-bound "
        "ferrosome organelles that store intracellular iron as "
        "non-crystalline iron phosphate biomineral."
    ),
    "definition_source": GRANT,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000066"],
    "evidence": [
        grant_new_class_evidence(),
        grant_fez_evidence(),
        grant_fez_operon_evidence(),
        pi_iron_phosphate_evidence(),
        pi_fezab_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1496",
            "taxon_label": "Clostridioides difficile",
            "note": (
                "Pi et al. showed that C. difficile forms membrane-bound "
                "ferrosome organelles containing non-crystalline iron "
                "phosphate biominerals."
            ),
            "reference": PI,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "ferrosome_iron_storage",
            "title": "Fez proteins form iron-storing ferrosomes",
            "description": (
                "Evidence-backed causal sketch linking Fez-dependent "
                "formation to membrane-bound iron-storage organelles."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures broad Fez-dependent formation and "
                "ferrosome iron storage at process and organelle level "
                "without asserting one taxon-universal Fez component "
                "roster, individual Fez-protein activity, accession-level "
                "protein examples, iron-remobilization mechanism, "
                "membrane-localization path, iron-deficiency trigger, or "
                "host-colonization output."
            ),
            "nodes": [
                {
                    "node_id": "ferrosome_trait",
                    "label": "ferrosome",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Membrane-bound organelle storing intracellular "
                        "iron as non-crystalline iron phosphate."
                    ),
                },
                {
                    "node_id": "ferrosome_formation",
                    "label": "ferrosome formation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Fez-dependent biogenesis of membrane-bound "
                        "intracellular ferrosome organelles."
                    ),
                },
                {
                    "node_id": "non_crystalline_iron_phosphate",
                    "label": "non-crystalline iron phosphate biomineral",
                    "node_type": "CHEMICAL",
                    "description": (
                        "Non-crystalline iron phosphate mineral stored "
                        "inside ferrosomes."
                    ),
                },
                {
                    "node_id": "iron_storage",
                    "label": "iron storage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Intracellular storage of iron in a recoverable "
                        "organelle-associated pool."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "ferrosome_formation",
                    "predicate": "has output",
                    "predicate_id": "RO:0002234",
                    "object": "ferrosome_trait",
                    "description": (
                        "Fez-dependent ferrosome formation produces the "
                        "ferrosome intracellular organelle."
                    ),
                    "evidence": [
                        grant_new_class_evidence(),
                        grant_fez_evidence(),
                        grant_fez_operon_evidence(),
                        pi_fezab_evidence(),
                    ],
                },
                {
                    "subject": "non_crystalline_iron_phosphate",
                    "predicate": "located in",
                    "predicate_id": "biolink:located_in",
                    "object": "ferrosome_trait",
                    "description": (
                        "Non-crystalline iron phosphate biominerals are "
                        "stored within ferrosome organelles."
                    ),
                    "evidence": [
                        pi_iron_phosphate_evidence(),
                    ],
                },
                {
                    "subject": "ferrosome_trait",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "iron_storage",
                    "description": (
                        "Ferrosome organelles realize intracellular iron "
                        "storage."
                    ),
                    "evidence": [
                        grant_new_class_evidence(),
                        pi_iron_phosphate_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "ferrosome-xref-gap",
            "prompt": (
                "Resolve exact external ontology xrefs for the bacterial "
                "ferrosome morphology trait."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact active METPO, GO, or OBO class was accepted for "
                "the organism-level ferrosome morphology trait. GO:0110143 "
                "magnetosome, GO:0031411 gas vesicle, GO:0031470 "
                "carboxysome, and GO:0070088 PHA granule are sibling "
                "organelles or inclusions rather than ferrosome equivalents."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
        },
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the YAML file")
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted ferrosome as a DOI-backed MORPHOLOGY TraitRecord "
            "under the intracellular inclusion parent after an "
            "ignored-and-hidden duplicate review found no exact same-scope "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            existing = load_trait(TARGET)
            assert existing["identifier"] == IDENTIFIER
            assert existing["label"] == "ferrosome"
            assert existing["mapping_status"] == "PROPOSED"
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
