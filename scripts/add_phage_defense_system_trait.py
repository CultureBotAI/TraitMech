#!/usr/bin/env python3
"""Add the phage defense system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "phage_defense_system.yaml"
CRISPR_CAS = REPO_ROOT / "data" / "traits" / "genomics" / "crispr_cas_system.yaml"
RESTRICTION_MODIFICATION = (
    REPO_ROOT / "data" / "traits" / "genomics" / "restriction_modification_system.yaml"
)

BERNHEIM = "DOI:10.1038/s41579-019-0278-2"
HAMPTON = "DOI:10.1038/s41586-019-1894-8"
DORON = "DOI:10.1126/science.aar4120"
BARRANGOU = "DOI:10.1126/science.1138140"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T07:55:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000209",
    "label": "phage defense system",
    "definition": (
        "A genomics trait describing possession of one or more bacterial or "
        "archaeal immune systems that inhibit bacteriophage infection."
    ),
    "definition_source": BERNHEIM,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000188"],
    "synonyms": [
        {
            "synonym_text": "antiphage defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": DORON,
        },
        {
            "synonym_text": "anti-phage system",
            "synonym_type": "EXACT_SYNONYM",
            "source": HAMPTON,
        },
        {
            "synonym_text": "pan-immune system",
            "synonym_type": "RELATED_SYNONYM",
            "source": BERNHEIM,
        },
    ],
    "evidence": [
        {
            "reference": BERNHEIM,
            "snippet": (
                "Viruses and their hosts are engaged in a constant arms race "
                "leading to the evolution of antiviral defence mechanisms"
            ),
            "notes": (
                "Bernheim and Sorek define the bacterial bacteriophage-defense "
                "context and review the pan-genomic diversity and cost of "
                "antiviral defense systems."
            ),
        },
        {
            "reference": BERNHEIM,
            "snippet": (
                "individual microorganisms often encode multiple distinct "
                "defence systems"
            ),
            "notes": (
                "The pan-immune-system model supports treating possession of "
                "one or more defense systems as a strain-level genomics trait "
                "rather than a single protein, locus, or pathway."
            ),
        },
        {
            "reference": HAMPTON,
            "snippet": (
                "Bacteria have evolved numerous immune mechanisms, both innate "
                "and adaptive"
            ),
            "notes": (
                "Hampton et al. review innate and adaptive anti-phage systems "
                "and the phage counter-defense mechanisms that evade them."
            ),
        },
        {
            "reference": HAMPTON,
            "snippet": (
                "Here we review the spectrum of anti-phage systems and "
                "highlight their evasion by bacteriophages"
            ),
            "notes": (
                "This supports the umbrella scope spanning diverse CRISPR-Cas, "
                "restriction-modification, BREX, DISARM, abortive-infection, "
                "and related anti-phage defenses."
            ),
        },
        {
            "reference": DORON,
            "snippet": (
                "Candidate immune systems were then experimentally validated "
                "for their activities"
            ),
            "notes": (
                "The Science article summary for Doron et al. supports genomic "
                "discovery and experimental validation of antiphage defense "
                "systems from microbial pangenomes."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1308",
            "taxon_label": "Streptococcus thermophilus",
            "note": (
                "S. thermophilus is the organism in which CRISPR-Cas adaptive "
                "immunity was experimentally shown to provide phage resistance."
            ),
            "reference": BARRANGOU,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "phage_defense_system_hierarchy",
            "title": "Antiphage defense systems resist viral challenge",
            "description": (
                "Evidence-backed ontology sketch linking phage pressure to the "
                "umbrella phage-defense-system trait and its reviewed "
                "CRISPR-Cas and restriction-modification children."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "This parent trait groups independently reviewed genome-level "
                "anti-phage defense systems without claiming that CRISPR-Cas, "
                "restriction-modification, BREX, DISARM, abortive infection, or "
                "other defense families share one universal molecular mechanism."
            ),
            "nodes": [
                {
                    "node_id": "bacteriophage_pressure",
                    "label": "bacteriophage pressure",
                    "node_type": "ENVIRONMENTAL_FACTOR",
                    "description": (
                        "Selective pressure imposed by bacteriophage infection."
                    ),
                },
                {
                    "node_id": "phage_defense_system_trait",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
                {
                    "node_id": "crispr_cas_system",
                    "label": "CRISPR-Cas system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000094",
                    "description": (
                        "Adaptive immune system using CRISPR arrays and Cas "
                        "proteins to recognize invading nucleic acids."
                    ),
                },
                {
                    "node_id": "restriction_modification_system",
                    "label": "restriction-modification system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000095",
                    "description": (
                        "Paired methyltransferase and restriction-endonuclease "
                        "system for self/non-self DNA discrimination."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "bacteriophage_pressure",
                    "predicate": "selects for",
                    "predicate_id": "METPO:2007401",
                    "object": "phage_defense_system_trait",
                    "description": (
                        "Virus-host arms races select for microbial antiviral "
                        "defense mechanisms."
                    ),
                    "evidence": [
                        {
                            "reference": BERNHEIM,
                            "snippet": (
                                "constant arms race leading to the evolution of "
                                "antiviral defence mechanisms"
                            ),
                            "notes": (
                                "Bernheim and Sorek frame bacteriophages and "
                                "bacterial hosts as engaged in an evolutionary "
                                "arms race."
                            ),
                        }
                    ],
                },
                {
                    "subject": "crispr_cas_system",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system_trait",
                    "description": (
                        "CRISPR-Cas possession is an adaptive phage-defense "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": DORON,
                            "snippet": (
                                "well-known defense arsenals such as "
                                "restriction-modification and CRISPR systems"
                            ),
                            "notes": (
                                "The Science article summary for Doron et al. "
                                "places CRISPR systems among the recognized "
                                "microbial defense arsenals."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restriction_modification_system",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system_trait",
                    "description": (
                        "Restriction-modification possession is an innate "
                        "phage-defense system."
                    ),
                    "evidence": [
                        {
                            "reference": DORON,
                            "snippet": (
                                "well-known defense arsenals such as "
                                "restriction-modification and CRISPR systems"
                            ),
                            "notes": (
                                "The Science article summary for Doron et al. "
                                "places restriction-modification systems among "
                                "the recognized microbial defense arsenals."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "phage-defense-system-xref-gap",
            "prompt": (
                "Resolve exact ontology xrefs for organism-level phage defense "
                "system possession before adding TraitRecord xrefs."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned METPO snapshot retains only obsolete phage defense, "
                "and GO:0051607 defense response to virus is a biological "
                "process rather than this GENOMICS possession trait. "
                "CRISPR-Cas, restriction-modification, BREX, DISARM, "
                "abortive-infection, and other mechanism terms are narrower "
                "than the umbrella parent curated here."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-15",
        }
    ],
}


def _load_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _reparent_child(
    doc: dict[str, Any],
    *,
    identifier: str,
    label: str,
    target_label: str,
) -> dict[str, Any]:
    if (
        doc.get("identifier") != identifier
        or doc.get("label") != label
        or doc.get("mapping_status") != "REVIEWED"
        or doc.get("parent_traits") != ["METPO:1000188"]
    ):
        raise SystemExit(f"unexpected preimage for {label}")

    updated = copy.deepcopy(doc)
    updated["parent_traits"] = ["traitmech:000209"]
    record_curation_event(
        updated,
        curator=CURATOR,
        action="REFINED_PARENT_TRAITS",
        changes=(
            f"Reparented {target_label} from the broad genomics parent to the "
            "newly minted phage defense system parent."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write YAML files")
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted phage defense system as a DOI-backed GENOMICS TraitRecord "
            "after an ignored-and-hidden duplicate review found only obsolete "
            "METPO phage defense and future-gap mentions; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v86."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    crispr_cas = _reparent_child(
        _load_record(CRISPR_CAS),
        identifier="traitmech:000094",
        label="CRISPR-Cas system",
        target_label="CRISPR-Cas system",
    )
    restriction_modification = _reparent_child(
        _load_record(RESTRICTION_MODIFICATION),
        identifier="traitmech:000095",
        label="restriction-modification system",
        target_label="restriction-modification system",
    )

    outputs = [
        (TARGET, record),
        (CRISPR_CAS, crispr_cas),
        (RESTRICTION_MODIFICATION, restriction_modification),
    ]
    for path, doc in outputs:
        rel = path.relative_to(REPO_ROOT)
        if args.apply:
            write_validated_trait(doc, path)
            print(f"wrote {rel}")
        else:
            print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
