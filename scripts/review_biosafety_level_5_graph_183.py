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
SOURCE = "https://spacearchitect.org/pubs/SAE-2002-01-2469.pdf"
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
            "Verified against the open SAE 2002 PDF; Cohen reports that the NASA "
            "Office of Planetary Protection draft protocol defined PPL-alpha as "
            "the concrete standard once informally called BSL-5."
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
    "graph_id": "biosafety_level_5_ppl_alpha_containment",
    "title": "BSL-5 as draft PPL-alpha containment",
    "scope_status": "NONMECHANISTIC",
    "scope_notes": (
        "This record names a proposed, planetary-protection-specific containment "
        "standard rather than a microbial phenotype, so its graph is contextual "
        "and intentionally carries no organism or token UniProt examples."
    ),
    "description": (
        "Open SAE 2002 graph grounding BSL-5 to draft Planetary Protection Level "
        "Alpha, a Mars returned sample handling standard that extends BSL-4-class "
        "containment to bidirectional Earth and sample protection."
    ),
    "nodes": [
        {
            "node_id": "bsl5_trait",
            "label": "biosafety level 5",
            "node_type": "TRAIT",
            "grounding": "METPO:1001106",
            "description": (
                "Informal name formerly applied to draft PPL-alpha, a proposed "
                "containment level for Mars returned sample handling."
            ),
        },
        {
            "node_id": "planetary_protection_level_alpha",
            "label": "Planetary Protection Level Alpha",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": (
                "Draft NASA planetary-protection standard requiring demonstrable "
                "bioisolation and containment for returned Mars samples."
            ),
        },
        {
            "node_id": "bsl4_standard",
            "label": "biosafety level 4 standard",
            "node_type": "TRAIT",
            "grounding": "METPO:1001105",
            "description": (
                "CDC maximum-containment biosafety level used as the comparison "
                "point for PPL-alpha."
            ),
        },
        {
            "node_id": "mars_returned_sample_handling",
            "label": "Mars returned sample handling",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": (
                "Receiving, handling, analyzing, storing, and releasing samples "
                "returned from Mars."
            ),
        },
        {
            "node_id": "two_way_contamination_control",
            "label": "two-way contamination control",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": (
                "Coordinated backward-contamination protection for Earth and "
                "forward-contamination protection for pristine samples."
            ),
        },
        {
            "node_id": "earth_backward_contamination_prevention",
            "label": "backward-contamination prevention for Earth",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": (
                "Containment preventing potentially hazardous returned material "
                "from escaping into Earth's biosphere."
            ),
        },
        {
            "node_id": "sample_forward_contamination_prevention",
            "label": "forward-contamination prevention for samples",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": (
                "Clean handling preventing terrestrial organisms or organic "
                "molecules from contaminating returned samples."
            ),
        },
        {
            "node_id": "closed_system_sample_handling",
            "label": "closed-system sample handling",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": "Sample storage and retrieval inside a closed system.",
        },
        {
            "node_id": "automation_remote_manipulation",
            "label": "automation and remote manipulation",
            "node_type": "EXPERIMENTAL_FACTOR",
            "description": (
                "Robotic or remotely manipulated sample handling that avoids "
                "leaky conventional glovebox interfaces."
            ),
        },
    ],
    "edges": [
        {
            "subject": "planetary_protection_level_alpha",
            "predicate": "was informally called",
            "object": "bsl5_trait",
            "description": (
                "Draft PPL-alpha was the concrete planetary-protection standard "
                "once informally called BSL-5."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "informally called BSL-5",
                    "notes": (
                        "Verified against the open SAE 2002 PDF; Cohen links the "
                        "BSL-5 label specifically to the draft PPL-alpha standard."
                    ),
                },
            ],
        },
        {
            "subject": "planetary_protection_level_alpha",
            "predicate": "exceeds",
            "object": "bsl4_standard",
            "description": (
                "PPL-alpha is described as more stringent than BSL-4 because it "
                "adds forward sample-protection requirements to backward "
                "biosphere containment."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": (
                        "order of magnitude more stringent than the Center for "
                        "Disease Control"
                    ),
                    "notes": (
                        "Verified against the open SAE 2002 PDF; PPL-alpha is "
                        "contrasted with the CDC BSL-4 standard and framed as a "
                        "stricter two-way protection regime."
                    ),
                },
            ],
        },
        {
            "subject": "planetary_protection_level_alpha",
            "predicate": "requires",
            "object": "two_way_contamination_control",
            "description": (
                "PPL-alpha requires both returned-sample containment and protection "
                "of the samples from terrestrial contamination."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "bioisolation and containment",
                    "notes": (
                        "Verified against the open SAE 2002 PDF; the draft standard "
                        "requires a high-reliability bioisolation and containment "
                        "system for planetary samples."
                    ),
                },
            ],
        },
        {
            "subject": "two_way_contamination_control",
            "predicate": "includes",
            "object": "sample_forward_contamination_prevention",
            "description": (
                "The draft standard includes forward-contamination control to keep "
                "Earth organisms out of returned Mars samples."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "terrestrial forward contamination",
                    "notes": (
                        "Verified against the open SAE 2002 PDF; Cohen's candidate "
                        "MRSH scenario lists PPL-alpha protection of Mars returned "
                        "samples from terrestrial forward contamination."
                    ),
                },
            ],
            "predicate_id": "biolink:has_part",
        },
        {
            "subject": "two_way_contamination_control",
            "predicate": "includes",
            "object": "earth_backward_contamination_prevention",
            "description": (
                "The draft standard includes backward-contamination control to keep "
                "returned Mars material out of Earth's biosphere."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "backward contamination",
                    "notes": (
                        "Verified against the open SAE 2002 PDF; Cohen's candidate "
                        "MRSH scenario lists PPL-alpha protection of Earth from "
                        "backward contamination by Mars and Mars samples."
                    ),
                },
            ],
            "predicate_id": "biolink:has_part",
        },
        {
            "subject": "planetary_protection_level_alpha",
            "predicate": "applies to",
            "object": "mars_returned_sample_handling",
            "description": (
                "The draft protocol extends PPL-alpha beyond a receiving facility "
                "to the whole Mars Sample Return mission."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "Mars Sample Return mission",
                    "notes": (
                        "Verified against the open SAE 2002 PDF; Cohen reports "
                        "that the draft protocol applied to all portions of Mars "
                        "Sample Return, not only one sample receiving facility."
                    ),
                },
            ],
        },
        {
            "subject": "closed_system_sample_handling",
            "predicate": "contributes to",
            "object": "mars_returned_sample_handling",
            "description": (
                "Closed storage and retrieval are part of the required architecture "
                "for safe handling of returned Mars samples."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "sample storage and retrieval within a closed system",
                    "notes": (
                        "Verified against the open SAE 2002 PDF; closed-system "
                        "sample storage and retrieval is one MRSH architecture "
                        "criterion listed in the abstract."
                    ),
                },
            ],
            "predicate_id": "RO:0002326",
        },
        {
            "subject": "automation_remote_manipulation",
            "predicate": "contributes to",
            "object": "closed_system_sample_handling",
            "description": (
                "Automation and remote manipulation support sample transfer without "
                "the leaky glove interfaces that conventional gloveboxes present."
            ),
            "evidence": [
                {
                    "reference": SOURCE,
                    "snippet": "automation and remote manipulation",
                    "notes": (
                        "Verified against the open SAE 2002 PDF; Cohen names "
                        "automation and remote manipulation as an alternative to "
                        "conventional gloveboxes for sample handling and transfer."
                    ),
                },
            ],
            "predicate_id": "RO:0002326",
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
            "Reviewed the biosafety_level_5_ppl_alpha_containment graph for issue "
            "#183: replaced the unsupported generalized enhanced-pathogen-hazard "
            "graph with an 8-edge Mars returned sample handling graph grounded in "
            "the open Cohen 2002 SAE paper, kept definition_source on the DOI "
            "that backs the proposed pathogen-hazard definition, added exact "
            "snippets to record and edge evidence, and kept BSL-5 scoped as an "
            "explicitly hypothetical nonmechanistic planetary-protection proposal. "
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
