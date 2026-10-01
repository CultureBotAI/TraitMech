#!/usr/bin/env python3
"""Add the MksBEFG system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mksbefg_system.yaml"
WADJET_PARENT = REPO_ROOT / "data" / "traits" / "genomics" / "wadjet_system.yaml"

LIU = "DOI:10.1016/j.molcel.2022.11.015"
WEISS = "DOI:10.1093/nar/gkad130"

CURATOR = "codex"
TIMESTAMP = "2026-10-01T21:15:00Z"
PARENT_TIMESTAMP = "2026-10-01T21:15:01Z"
IDENTIFIER = "traitmech:000526"
WADJET_ID = "traitmech:000218"
PROPOSAL = "proposals/metpo_traitmech_v403"

OLD_WADJET_PROMPT = (
    "Resolve Wadjet subfamily architecture, plasmid substrate specificity, "
    "and activation cues before minting narrower Wadjet mechanism children."
)
NEW_WADJET_PROMPT = (
    "Resolve JetABCD, EptABCD, DefenseFinder Wadjet subtype boundaries, "
    "plasmid substrate specificity, and activation cues before minting "
    "additional narrower Wadjet mechanism children."
)
OLD_WADJET_RATIONALE = (
    "Deep et al. and Liu et al. support JetABCD-mediated topology- or "
    "shape-biased circular plasmid cleavage, and Weiss et al. support "
    "MksG-mediated plasmid degradation in the MksBEFG subfamily, but "
    "Wadjet variants need separate review before TraitMech asserts one "
    "exact target size threshold, linear-plasmid escape rule, "
    "loop-extrusion endpoint, polar localization pattern, or nuclease "
    "activation model."
)
NEW_WADJET_RATIONALE = (
    "Deep et al. and Liu et al. support JetABCD-mediated topology- or "
    "shape-biased circular plasmid cleavage and the broad "
    "JetABCD/MksBEFG/EptABCD Wadjet family, while the MksBEFG child now "
    "captures the Weiss et al. plasmid-degradation branch. The parent "
    "still leaves JetABCD, EptABCD, DefenseFinder Wadjet I-III "
    "boundaries, exact target size threshold, linear-plasmid escape rule, "
    "loop-extrusion endpoint, polar localization pattern, and nuclease "
    "activation models for additional Wadjet variants unresolved."
)


def liu_family_evidence() -> dict[str, str]:
    return {
        "reference": LIU,
        "snippet": (
            "Wadjet systems (JetABCD/MksBEFG/EptABCD) are derivative SMC "
            "complexes with roles in bacterial immunity against selfish DNA"
        ),
        "notes": (
            "Liu et al. support MksBEFG as a Wadjet-family derivative SMC "
            "complex related to JetABCD and EptABCD."
        ),
    }


def weiss_title_evidence() -> dict[str, str]:
    return {
        "reference": WEISS,
        "snippet": (
            "The MksG nuclease is the executing part of the bacterial "
            "plasmid defense system MksBEFG"
        ),
        "notes": (
            "Weiss et al. describe MksBEFG as a bacterial plasmid-defense "
            "system and identify MksG as its executing nuclease component."
        ),
    }


def mksg_nuclease_evidence() -> dict[str, str]:
    return {
        "reference": WEISS,
        "snippet": "MksG is a nuclease that degrades plasmid DNA",
        "notes": (
            "Weiss et al. support plasmid-DNA degradation by the MksG "
            "nuclease of the MksBEFG system."
        ),
    }


def mksg_in_vivo_evidence() -> dict[str, str]:
    return {
        "reference": WEISS,
        "snippet": (
            "Introduction of plasmids results in an increase in DNA bound "
            "MksG, indicating an activation of the system in vivo"
        ),
        "notes": (
            "Weiss et al. support plasmid-responsive activation of the "
            "Corynebacterium glutamicum MksBEFG system in vivo."
        ),
    }


def mksbef_atpase_evidence() -> dict[str, str]:
    return {
        "reference": WEISS,
        "snippet": "The MksBEF subunits exhibit an ATPase cycle in vitro",
        "notes": (
            "Weiss et al. support ATPase cycling by the C. glutamicum "
            "MksBEF core."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "MksBEFG system",
    "definition": (
        "A Wadjet system in which an organism possesses an MksBEFG "
        "derivative SMC locus encoding an MksBEF ATPase core and an MksG "
        "nuclease that degrades plasmid DNA."
    ),
    "definition_source": WEISS,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [WADJET_ID],
    "synonyms": [
        {
            "synonym_text": "MksBEFG",
            "synonym_type": "RELATED_SYNONYM",
            "source": WEISS,
        },
    ],
    "evidence": [
        weiss_title_evidence(),
        mksg_nuclease_evidence(),
        mksg_in_vivo_evidence(),
        mksbef_atpase_evidence(),
        liu_family_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1718",
            "taxon_label": "Corynebacterium glutamicum",
            "note": (
                "Weiss et al. investigated the Corynebacterium glutamicum "
                "MksBEFG complex and showed that plasmid introduction "
                "increased DNA-bound MksG in vivo."
            ),
            "reference": WEISS,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "mksbefg_degrades_plasmid_dna",
            "title": "MksBEFG systems degrade plasmid DNA",
            "description": (
                "Conservative system-level sketch linking MksBEFG loci to "
                "MksG-dependent plasmid DNA degradation and Wadjet system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the MksBEFG subfamily at locus and "
                "plasmid-degradation-output level without asserting the "
                "exact MksBEF ATPase-to-MksG coupling step, plasmid "
                "substrate breadth, cellular MksG loading path, or "
                "accession-level protein examples."
            ),
            "nodes": [
                {
                    "node_id": "mksbefg_locus",
                    "label": "MksBEFG locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Wadjet-family plasmid-defense locus encoding "
                        "MksB, MksE, MksF, and MksG components."
                    ),
                },
                {
                    "node_id": "mksbef_atpase_cycle",
                    "label": "MksBEF ATPase cycle",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "ATPase cycling by the MksB, MksE, and MksF "
                        "subunits of the MksBEFG complex."
                    ),
                },
                {
                    "node_id": "mksg_plasmid_dna_degradation",
                    "label": "MksG plasmid DNA degradation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Degradation of plasmid DNA by the MksG nuclease "
                        "component of the MksBEFG system."
                    ),
                },
                {
                    "node_id": "plasmid_transformation",
                    "label": "plasmid transformation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Introduction and establishment of exogenous "
                        "plasmid DNA in a bacterial cell."
                    ),
                },
                {
                    "node_id": "mksbefg_system_trait",
                    "label": "MksBEFG system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded MksBEFG "
                        "anti-plasmid defense system."
                    ),
                },
                {
                    "node_id": "wadjet_system_trait",
                    "label": "Wadjet system",
                    "node_type": "TRAIT",
                    "grounding": WADJET_ID,
                    "description": (
                        "Possession of a genome-encoded Wadjet "
                        "anti-plasmid defense locus."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "mksbefg_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "mksbef_atpase_cycle",
                    "description": (
                        "MksBEFG loci encode the MksBEF ATPase core."
                    ),
                    "evidence": [
                        mksbef_atpase_evidence(),
                    ],
                },
                {
                    "subject": "mksbefg_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "mksg_plasmid_dna_degradation",
                    "description": (
                        "MksBEFG loci encode the MksG nuclease that "
                        "degrades plasmid DNA."
                    ),
                    "evidence": [
                        weiss_title_evidence(),
                        mksg_nuclease_evidence(),
                    ],
                },
                {
                    "subject": "mksg_plasmid_dna_degradation",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "plasmid_transformation",
                    "description": (
                        "MksG-dependent plasmid DNA degradation restricts "
                        "incoming plasmid DNA."
                    ),
                    "evidence": [
                        mksg_nuclease_evidence(),
                        mksg_in_vivo_evidence(),
                    ],
                },
                {
                    "subject": "mksg_plasmid_dna_degradation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "mksbefg_system_trait",
                    "description": (
                        "Plasmid DNA degradation realizes the MksBEFG "
                        "anti-plasmid defense trait."
                    ),
                    "evidence": [
                        weiss_title_evidence(),
                    ],
                },
                {
                    "subject": "mksbefg_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "wadjet_system_trait",
                    "description": (
                        "MksBEFG system possession is a Wadjet system trait."
                    ),
                    "evidence": [
                        liu_family_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "mksbefg-activation-and-substrate-gap",
            "prompt": (
                "Resolve MksBEFG plasmid substrate breadth, MksBEF "
                "ATPase-to-MksG coupling, MksG activation state, and "
                "accession-level protein examples before minting narrower "
                "MksBEFG mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Weiss et al. support MksBEFG as a bacterial "
                "plasmid-defense system with an MksBEF ATPase core and "
                "MksG plasmid-DNA-degradation nuclease, and Liu et al. "
                "place MksBEFG in the broader Wadjet derivative-SMC "
                "family. This first-pass record leaves exact plasmid "
                "substrate breadth, MksBEF-to-MksG coupling, cellular MksG "
                "loading, and accession-level component examples "
                "unresolved."
            ),
            "evidence": [
                weiss_title_evidence(),
                mksg_nuclease_evidence(),
                mksg_in_vivo_evidence(),
                mksbef_atpase_evidence(),
                liu_family_evidence(),
            ],
            "attaches_to": ["causal_graphs#mksbefg_degrades_plasmid_dna"],
            "posed_by": CURATOR,
            "posed_date": "2026-10-01",
        }
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def update_wadjet_parent(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == WADJET_ID
    assert record["label"] == "Wadjet system"
    assert record["mapping_status"] == "PROPOSED"

    discussion = next(
        item
        for item in record.get("discussions") or []
        if item.get("discussion_id") == "wadjet-subfamily-and-substrate-gap"
    )
    if (
        discussion["prompt"] == NEW_WADJET_PROMPT
        and discussion["rationale"] == NEW_WADJET_RATIONALE
    ):
        assert discussion["status"] == "OPEN"
        return record

    assert discussion["prompt"] == OLD_WADJET_PROMPT
    assert discussion["status"] == "OPEN"
    assert discussion["rationale"] == OLD_WADJET_RATIONALE

    discussion["prompt"] = NEW_WADJET_PROMPT
    discussion["rationale"] = NEW_WADJET_RATIONALE
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=(
            "Documented MksBEFG as split out in the open Wadjet "
            "subfamily and substrate discussion after minting "
            "traitmech:000526 for the MksBEFG system; JetABCD, EptABCD, "
            "and DefenseFinder Wadjet subtype boundaries remain open."
        ),
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted MksBEFG system as a DOI-backed GENOMICS "
            "TraitRecord under the Wadjet system parent after an "
            "ignored-and-hidden duplicate review found no exact same-scope "
            "live TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / WADJET_PARENT.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_wadjet_parent(load_trait(WADJET_PARENT))
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            existing = load_trait(TARGET)
            assert existing["identifier"] == IDENTIFIER
            assert existing["label"] == "MksBEFG system"
            assert existing["mapping_status"] == "PROPOSED"
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, WADJET_PARENT)
    else:
        print(
            "MksBEFG system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{WADJET_PARENT.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
