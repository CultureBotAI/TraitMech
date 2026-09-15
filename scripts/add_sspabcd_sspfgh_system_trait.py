#!/usr/bin/env python3
"""Add the SspABCD-SspFGH system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "sspabcd_sspfgh_system.yaml"
PHOSPHOROTHIOATE = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "phosphorothioate_defense_system.yaml"
)

WANG = "DOI:10.1128/mbio.00613-21"
XIONG = "DOI:10.1038/s41564-020-0700-6"
XU_GU = "DOI:10.3390/ijms252413316"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T17:06:06Z"
PARENT_TIMESTAMP = "2026-09-15T17:06:07Z"

OLD_PARENT_PROMPT = (
    "Resolve SspABCD-sspFGH and archaeal phosphorothioate-based antiviral "
    "systems before minting additional narrower children under the "
    "phosphorothioate defense parent."
)
OLD_PARENT_RATIONALE = (
    "The Dnd system is split out as traitmech:000221, and the "
    "SspABCD-SspE single-restriction-enzyme system is split out as "
    "traitmech:000222. Xiong et al. and Jiang et al. still support "
    "additional bacterial PT-related R-M architectures with SspFGH "
    "restriction modules, and SspFGH systems plus archaeal "
    "phosphorothioate-based antiviral systems need separate primary-source "
    "review before they can be split into narrower TraitRecords with exact "
    "component groundings."
)
NEW_PARENT_PROMPT = (
    "Resolve archaeal phosphorothioate-based antiviral systems before "
    "minting additional narrower children under the phosphorothioate "
    "defense parent."
)
NEW_PARENT_RATIONALE = (
    "The Dnd system is split out as traitmech:000221, the SspABCD-SspE "
    "single-restriction-enzyme system is split out as traitmech:000222, "
    "and the SspABCD-SspFGH system is split out as traitmech:000223. "
    "Archaeal phosphorothioate-based antiviral systems still need "
    "separate primary-source review before they can be split into a "
    "narrower TraitRecord with exact component groundings."
)
PARENT_CHANGES = (
    "Removed SspFGH from the open phosphorothioate subfamily split-gap "
    "discussion after minting traitmech:000223 for the SspABCD-SspFGH "
    "system; archaeal phosphorothioate-based antiviral systems remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000223",
    "label": "SspABCD-SspFGH system",
    "definition": (
        "A phosphorothioate defense system in which an organism possesses "
        "an SspABCD-SspFGH locus that pairs an SspABCD-family "
        "single-stranded DNA phosphorothioation module with an SspFGH "
        "restriction module to damage non-phosphorothioated phage DNA and "
        "suppress phage DNA replication."
    ),
    "definition_source": WANG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000213"],
    "synonyms": [
        {
            "synonym_text": "SspABCD-SspFGH defense system",
            "synonym_type": "EXACT_SYNONYM",
            "source": WANG,
        },
    ],
    "evidence": [
        {
            "reference": WANG,
            "snippet": (
                "new type of ssDNA PT-based SspABCD-SspFGH defense system "
                "capable of providing protection against phages"
            ),
            "notes": (
                "Wang et al. name SspABCD-SspFGH as a single-stranded "
                "DNA phosphorothioation-based bacterial phage-defense "
                "system."
            ),
        },
        {
            "reference": WANG,
            "snippet": (
                "PT-modifying genes sspBCD and iscS in Vibrio anguillarum "
                "strain FF-93 can provide protection against a range of "
                "phages in combination with sspFGH"
            ),
            "notes": (
                "Wang et al. support a native Vibrio anguillarum FF-93 "
                "Ssp system whose IscS-SspBCD phosphorothioation module "
                "works with the sspFGH cassette."
            ),
        },
        {
            "reference": WANG,
            "snippet": (
                "SspFGH coupled with IscS-SspBCD behaves as a new type of "
                "ssDNA PT modification-based defense barrier to fend off "
                "phage invasion"
            ),
            "notes": (
                "Wang et al. support the modification-plus-restriction "
                "architecture and antiphage output."
            ),
        },
        {
            "reference": WANG,
            "snippet": (
                "SspFGH damages non-PT-modified DNA and exerts antiphage "
                "activity by suppressing phage DNA replication"
            ),
            "notes": (
                "Wang et al. connect SspFGH-dependent DNA damage to the "
                "observed block in phage DNA replication."
            ),
        },
        {
            "reference": XIONG,
            "snippet": (
                "SspABCD confers single-stranded and high-frequency PTs "
                "with SspB acting as a nickase"
            ),
            "notes": (
                "Xiong et al. independently support SspABCD-family "
                "single-stranded host-DNA phosphorothioation."
            ),
        },
        {
            "reference": XU_GU,
            "snippet": (
                "could also be coupled to SspFGH for anti-phage activity"
            ),
            "notes": (
                "Xu and Gu summarize SspFGH as an SspABCD-coupled "
                "phosphorothioate antiphage restriction module."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:55601",
            "taxon_label": "Vibrio anguillarum",
            "note": (
                "Wang et al. identified an sspFGH cassette adjacent to the "
                "sspBCD cluster in Vibrio anguillarum FF-93 and showed "
                "that its SspFGH module couples to IscS-SspBCD "
                "phosphorothioation for phage defense."
            ),
            "reference": WANG,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "sspabcd_sspfgh_non_pt_dna_damage",
            "title": "SspABCD-SspFGH systems couple Ssp PT marks to foreign-DNA damage",
            "description": (
                "Evidence-backed process sketch linking an SspABCD-SspFGH "
                "locus to single-stranded host DNA phosphorothioation, "
                "SspFGH-dependent damage of non-phosphorothioated phage "
                "DNA, and reduced phage DNA replication."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures SspABCD-SspFGH restriction at the "
                "system level without asserting one universal host taxon, "
                "PT frequency, a DNA-damage chemistry, a complete SspFGH "
                "subunit cycle, or relationship to SspE and archaeal PT "
                "antiviral systems."
            ),
            "nodes": [
                {
                    "node_id": "sspabcd_sspfgh_locus",
                    "label": "SspABCD-SspFGH locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An Ssp phosphorothioation-dependent restriction "
                        "locus pairing an SspABCD-family DNA modification "
                        "module with SspFGH restriction activity."
                    ),
                },
                {
                    "node_id": "ssp_single_stranded_dna_phosphorothioation",
                    "label": "Ssp single-stranded DNA phosphorothioation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "SspABCD-family installation of single-stranded "
                        "phosphorothioate marks on host DNA."
                    ),
                },
                {
                    "node_id": "ssp_pt_self_nonself_discrimination",
                    "label": "Ssp PT self/nonself discrimination",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Use of Ssp phosphorothioate marks to distinguish "
                        "phosphorothioated host DNA from invading DNA "
                        "that lacks host phosphorothioate marks."
                    ),
                },
                {
                    "node_id": "sspfgh_non_pt_dna_damage",
                    "label": "SspFGH-dependent non-PT DNA damage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "SspFGH-dependent damage of DNA molecules that "
                        "lack host single-stranded phosphorothioate marks."
                    ),
                },
                {
                    "node_id": "phage_dna_replication",
                    "label": "phage DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication of invading bacteriophage DNA after "
                        "host cell entry."
                    ),
                },
                {
                    "node_id": "sspabcd_sspfgh_system_trait",
                    "label": "SspABCD-SspFGH system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000223",
                    "description": (
                        "Possession of a genome-encoded SspABCD-SspFGH "
                        "restriction-modification defense system."
                    ),
                },
                {
                    "node_id": "phosphorothioate_defense_system_trait",
                    "label": "phosphorothioate defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000213",
                    "description": (
                        "Possession of a genome-encoded "
                        "phosphorothioate-based phage defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "sspabcd_sspfgh_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "ssp_single_stranded_dna_phosphorothioation",
                    "description": (
                        "The SspABCD-family modification module installs "
                        "single-stranded PT marks on host DNA."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "IscS and SspBCD in FF-93 also confer DNA "
                                "PT modification at 5'-CPSCA-3' consensus "
                                "sequences"
                            ),
                            "notes": (
                                "Wang et al. support single-stranded "
                                "host-DNA phosphorothioation by the FF-93 "
                                "IscS-SspBCD module."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sspabcd_sspfgh_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "sspfgh_non_pt_dna_damage",
                    "description": (
                        "SspABCD-SspFGH loci pair the Ssp modification "
                        "module with SspFGH-dependent restriction "
                        "activity against DNA lacking PT marks."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "SspFGH coupled with IscS-SspBCD behaves "
                                "as a new type of ssDNA PT "
                                "modification-based defense barrier"
                            ),
                            "notes": (
                                "Wang et al. support the paired Ssp "
                                "phosphorothioation and SspFGH restriction "
                                "architecture."
                            ),
                        }
                    ],
                },
                {
                    "subject": "ssp_single_stranded_dna_phosphorothioation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "ssp_pt_self_nonself_discrimination",
                    "description": (
                        "SspFGH uses Ssp phosphorothioate marks as a "
                        "recognition tag to discriminate self DNA from "
                        "invading non-PT DNA."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "SspFGH employs ssDNA PT modification as a "
                                "recognition tag to introduce damage to "
                                "non-PT-modified phage genomes"
                            ),
                            "notes": (
                                "Wang et al. support PT-dependent "
                                "self/nonself discrimination by the SspFGH "
                                "barrier."
                            ),
                        }
                    ],
                },
                {
                    "subject": "ssp_pt_self_nonself_discrimination",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "sspfgh_non_pt_dna_damage",
                    "description": (
                        "Ssp PT self/nonself discrimination leads to "
                        "SspFGH-dependent damage of non-PT phage DNA."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "SspFGH introduces damage to non-PT DNA "
                                "and consequently impairs phage DNA "
                                "replication"
                            ),
                            "notes": (
                                "Wang et al. connect SspFGH non-PT DNA "
                                "damage to the restriction output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sspfgh_non_pt_dna_damage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_dna_replication",
                    "description": (
                        "SspFGH-dependent damage of phage DNA suppresses "
                        "phage DNA replication."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "its DNA replication was markedly "
                                "suppressed in the presence of "
                                "IscS-SspBCD-SspFGH"
                            ),
                            "notes": (
                                "Wang et al. directly connect the SspFGH "
                                "barrier to impaired phage DNA "
                                "replication."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sspfgh_non_pt_dna_damage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "sspabcd_sspfgh_system_trait",
                    "description": (
                        "SspFGH-dependent non-PT DNA damage realizes the "
                        "SspABCD-SspFGH antiphage defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "SspFGH provided moderate levels of "
                                "protection against phages"
                            ),
                            "notes": (
                                "Wang et al. support phage restriction as "
                                "the SspFGH system output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "sspabcd_sspfgh_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phosphorothioate_defense_system_trait",
                    "description": (
                        "SspABCD-SspFGH possession is a "
                        "phosphorothioate-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": WANG,
                            "snippet": (
                                "new type of ssDNA PT-based "
                                "SspABCD-SspFGH defense system"
                            ),
                            "notes": (
                                "Wang et al. place SspABCD-SspFGH among "
                                "single-stranded DNA phosphorothioation-"
                                "based defense systems."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def update_phosphorothioate_parent(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == "traitmech:000213"
    assert record["label"] == "phosphorothioate defense system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    discussions = {
        item["discussion_id"]: item for item in record.get("discussions") or []
    }
    discussion = discussions["phosphorothioate-subfamily-split-gap"]
    assert discussion["kind"] == "KNOWLEDGE_GAP"
    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] in {OLD_PARENT_PROMPT, NEW_PARENT_PROMPT}
    assert discussion["rationale"] in {OLD_PARENT_RATIONALE, NEW_PARENT_RATIONALE}

    discussion["prompt"] = NEW_PARENT_PROMPT
    discussion["rationale"] = NEW_PARENT_RATIONALE
    record["curation_history"] = [
        event
        for event in record.get("curation_history") or []
        if not (
            event.get("curator") == CURATOR
            and event.get("action") == "RESOLVE_DISCUSSION_SCOPE"
            and event.get("changes") == PARENT_CHANGES
        )
    ]
    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=PARENT_CHANGES,
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the new TraitRecord YAML and update the parent gap",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted SspABCD-SspFGH system as a DOI-backed GENOMICS "
            "TraitRecord under the phosphorothioate defense system parent "
            "after an ignored-and-hidden duplicate review found no exact "
            "live TraitMech, METPO, or prior proposal record; the "
            "replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v100."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    parent = update_phosphorothioate_parent(load_trait(PHOSPHOROTHIOATE))

    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, PHOSPHOROTHIOATE)
        print(f"wrote {TARGET.relative_to(REPO_ROOT)}")
        print(f"wrote {PHOSPHOROTHIOATE.relative_to(REPO_ROOT)}")
    else:
        print(f"would write {TARGET.relative_to(REPO_ROOT)}")
        print(f"would write {PHOSPHOROTHIOATE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
