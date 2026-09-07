#!/usr/bin/env python3
"""Review biosafety_level_5 graph evidence for issue #183.

The migration is dry-run by default, validates rendered records before writing,
rejects partial replay and metadata drift, and is exactly idempotent.

Usage:
    python scripts/review_biosafety_level_5_graph_183.py
    python scripts/review_biosafety_level_5_graph_183.py --apply
"""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "ecology/biosafety_level_5"
ACTION = "REVIEW_CAUSAL_EVIDENCE"
TIMESTAMP = "2026-09-04T10:00:00Z"
SOURCE = "DOI:10.4271/2002-01-2469"
BEFORE_DEFINITION_SOURCE = "DOI:10.1146/annurev.micro.62.081307.162938"
AFTER_DEFINITION_SOURCE = BEFORE_DEFINITION_SOURCE

BEFORE_RECORD_EVIDENCE: list[dict[str, Any]] = [
    {
        "reference": "DOI:10.1146/annurev.micro.62.081307.162938",
        "snippet": "virulence factors",
        "notes": (
            "Virulence-factor review supports the framing of pathogen hazard above "
            "existing BSL-4 thresholds (the rationale underlying the proposed "
            "BSL-5 classification)."
        ),
    },
]

AFTER_RECORD_EVIDENCE: list[dict[str, Any]] = [
    {
        "reference": "DOI:10.1146/annurev.micro.62.081307.162938",
        "snippet": "virulence factors",
        "notes": (
            "Virulence-factor review supports the framing of pathogen hazard above "
            "existing BSL-4 thresholds (the rationale underlying the proposed "
            "BSL-5 classification)."
        ),
    },
    {
        "reference": SOURCE,
        "snippet": "Planetary Protection Level Alpha",
        "notes": (
            "Verified against the open Cohen 2002 SAE paper; PPL-alpha is retained "
            "as historical BSL-5 name-use evidence, not as the scope of the "
            "generic METPO class."
        ),
    },
]

BEFORE_GRAPH: dict[str, Any] = {
    "graph_id": "biosafety_level_5_proposed_enhanced_hazard",
    "title": "BSL-5 proposed enhanced-hazard classification",
    "scope_status": "NONMECHANISTIC",
    "scope_notes": (
        "This broad ecological, host-relationship, habitat, or hazard classification "
        "spans multiple taxa and mechanisms; contextual protein nodes do not receive "
        "token UniProt examples."
    ),
    "description": (
        "DOI-backed graph linking hypothetical pathogen hazards exceeding BSL-4 "
        "thresholds to the proposed BSL-5 enhanced-containment classification."
    ),
    "nodes": [
        {
            "node_id": "bsl5_trait",
            "label": "biosafety level 5",
            "node_type": "TRAIT",
            "grounding": "METPO:1001106",
            "description": (
                "Proposed enhanced-containment classification beyond BSL-4 for "
                "hypothetical extreme-hazard agents."
            ),
        },
        {
            "node_id": "biosafety_level",
            "label": "biosafety level",
            "node_type": "TRAIT",
            "grounding": "METPO:1001101",
            "description": "Hazard-classification axis for biological agents.",
        },
        {
            "node_id": "enhanced_pathogen_hazard",
            "label": "enhanced pathogen hazard",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Hypothetical pathogen hazards judged to exceed the transmissibility, "
                "severity, or treatability thresholds covered by BSL-4."
            ),
        },
    ],
    "edges": [
        {
            "subject": "enhanced_pathogen_hazard",
            "predicate": "motivates",
            "object": "bsl5_trait",
            "description": (
                "Hazards exceeding BSL-4 thresholds motivate the proposed BSL-5 "
                "enhanced-containment classification."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev.micro.62.081307.162938",
                    "snippet": "virulence factors",
                    "notes": (
                        "Supports increasingly severe virulence-factor combinations "
                        "as the rationale for hazard classes above BSL-4."
                    ),
                },
            ],
        },
        {
            "subject": "bsl5_trait",
            "predicate": "is a",
            "object": "biosafety_level",
            "description": (
                "BSL-5 is a proposed member of the biosafety-level classification."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev.micro.62.081307.162938",
                    "snippet": "virulence factors",
                    "notes": (
                        "Supports BSL-5 as a proposed extension of the "
                        "biosafety-level classification axis."
                    ),
                },
            ],
            "predicate_id": "rdfs:subClassOf",
        },
    ],
}

AFTER_GRAPH: dict[str, Any] = {
    "graph_id": "biosafety_level_5_proposed_enhanced_hazard",
    "title": "BSL-5 proposed enhanced-hazard classification",
    "scope_status": "NONMECHANISTIC",
    "scope_notes": (
        "This broad ecological, host-relationship, habitat, or hazard classification "
        "spans multiple taxa and mechanisms; contextual protein nodes do not receive "
        "token UniProt examples."
    ),
    "description": (
        "DOI-backed graph linking hypothetical pathogen hazards exceeding BSL-4 "
        "thresholds to the proposed BSL-5 enhanced-containment classification, with "
        "PPL-alpha retained only as historical BSL-5 name-use evidence."
    ),
    "nodes": [
        {
            "node_id": "bsl5_trait",
            "label": "biosafety level 5",
            "node_type": "TRAIT",
            "grounding": "METPO:1001106",
            "description": (
                "Proposed enhanced-containment classification beyond BSL-4 for "
                "hypothetical extreme-hazard agents."
            ),
        },
        {
            "node_id": "biosafety_level",
            "label": "biosafety level",
            "node_type": "TRAIT",
            "grounding": "METPO:1001101",
            "description": "Hazard-classification axis for biological agents.",
        },
        {
            "node_id": "enhanced_pathogen_hazard",
            "label": "enhanced pathogen hazard",
            "node_type": "BIOLOGICAL_PROCESS",
            "description": (
                "Hypothetical pathogen hazards judged to exceed the transmissibility, "
                "severity, or treatability thresholds covered by BSL-4."
            ),
        },
        {
            "node_id": "planetary_protection_level_alpha",
            "label": "Planetary Protection Level Alpha",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": (
                "Draft planetary-protection standard historically associated "
                "with the BSL-5 label by Cohen."
            ),
        },
    ],
    "edges": [
        {
            "subject": "enhanced_pathogen_hazard",
            "predicate": "motivates",
            "object": "bsl5_trait",
            "description": (
                "Hazards exceeding BSL-4 thresholds motivate the proposed BSL-5 "
                "enhanced-containment classification."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev.micro.62.081307.162938",
                    "snippet": "virulence factors",
                    "notes": (
                        "Supports increasingly severe virulence-factor combinations "
                        "as the rationale for hazard classes above BSL-4."
                    ),
                },
            ],
        },
        {
            "subject": "bsl5_trait",
            "predicate": "is a",
            "object": "biosafety_level",
            "description": (
                "BSL-5 is a proposed member of the biosafety-level classification."
            ),
            "evidence": [
                {
                    "reference": "DOI:10.1146/annurev.micro.62.081307.162938",
                    "snippet": "virulence factors",
                    "notes": (
                        "Supports BSL-5 as a proposed extension of the "
                        "biosafety-level classification axis."
                    ),
                },
            ],
            "predicate_id": "rdfs:subClassOf",
        },
        {
            "subject": "planetary_protection_level_alpha",
            "predicate": "is informally called",
            "object": "bsl5_trait",
            "description": (
                "PPL-alpha has been informally called BSL-5, providing historical "
                "name-use evidence without narrowing the BSL-5 class to Mars "
                "sample handling."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "informally called BSL-5",
                    "notes": (
                        "Verified against the open Cohen 2002 SAE paper; the "
                        "PPL-alpha source supports a historical naming "
                        "association only."
                    ),
                },
            ],
        },
    ],
}


def _has_after_record_evidence(doc: dict[str, Any]) -> bool:
    return doc.get("evidence") == AFTER_RECORD_EVIDENCE


def _has_after_graph(doc: dict[str, Any]) -> bool:
    return doc.get("causal_graphs") == [AFTER_GRAPH]


def transform(slug: str, doc: dict[str, Any]) -> bool:
    if slug != SLUG:
        raise ValueError(f"expected {SLUG}, got {slug}")

    if doc.get("definition_source") != AFTER_DEFINITION_SOURCE:
        raise ValueError(f"{SLUG}: source definition_source drifted")

    has_after_record_evidence = _has_after_record_evidence(doc)
    has_after_graph = _has_after_graph(doc)
    if has_after_record_evidence and has_after_graph:
        return False
    if has_after_record_evidence or has_after_graph:
        raise ValueError(
            f"{SLUG}: partial evidence replay: "
            f"record_evidence={has_after_record_evidence} "
            f"graph={has_after_graph}"
        )

    if doc.get("evidence") != BEFORE_RECORD_EVIDENCE:
        raise ValueError(f"{SLUG}: source record evidence drifted")
    if doc.get("causal_graphs") != [BEFORE_GRAPH]:
        raise ValueError(f"{SLUG}: source graph drifted")

    doc["definition_source"] = AFTER_DEFINITION_SOURCE
    doc["evidence"] = copy.deepcopy(AFTER_RECORD_EVIDENCE)
    doc["causal_graphs"] = [copy.deepcopy(AFTER_GRAPH)]

    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        changes=(
            "Reviewed the biosafety_level_5_proposed_enhanced_hazard graph for issue "
            "#183: kept the generic proposed enhanced-hazard BSL-5 graph grounded "
            "in the pathogen-hazard definition DOI, added DOI-backed historical "
            "PPL-alpha name-use evidence from the Cohen 2002 SAE paper, added "
            "exact snippets to record and edge evidence, and kept BSL-5 scoped as "
            "an explicitly hypothetical nonmechanistic containment proposal. "
            "No paid research service was called."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )
    return True


def apply(write: bool = False) -> int:
    changed = 0
    path = REPO_ROOT / "data" / "traits" / f"{SLUG}.yaml"
    doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if transform(SLUG, doc):
        changed = 1
        if write:
            write_validated_trait(doc, path)
        else:
            with tempfile.TemporaryDirectory() as tmp:
                write_validated_trait(doc, Path(tmp) / path.name)
    print(f"{'applied' if write else 'dry run'}: reviewed {changed} graph(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    return apply(parser.parse_args().apply)


if __name__ == "__main__":
    raise SystemExit(main())
