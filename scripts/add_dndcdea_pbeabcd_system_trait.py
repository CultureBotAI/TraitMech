#!/usr/bin/env python3
"""Add the DndCDEA-PbeABCD system genomics trait."""
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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dndcdea_pbeabcd_system.yaml"
PHOSPHOROTHIOATE = (
    REPO_ROOT
    / "data"
    / "traits"
    / "genomics"
    / "phosphorothioate_defense_system.yaml"
)

XIONG = "DOI:10.1038/s41467-019-09390-9"
ISAEV = "DOI:10.1134/S0006297921030081"

CURATOR = "codex"
TIMESTAMP = "2026-09-15T17:36:16Z"
PARENT_TIMESTAMP = "2026-09-15T17:36:17Z"

OLD_PARENT_DEFINITION = (
    "A genomics trait describing possession of a DNA "
    "phosphorothioation-dependent antiphage restriction locus in which "
    "host DNA phosphorothioate modification is paired with Dnd- or "
    "Ssp-family restriction activity to nick unmodified invading DNA and "
    "inhibit bacteriophage replication."
)
NEW_PARENT_DEFINITION = (
    "A genomics trait describing possession of a DNA "
    "phosphorothioation-dependent antiviral locus in which host DNA "
    "phosphorothioate modification is paired with a Dnd-, Ssp-, or "
    "Pbe-family effector module to restrict invading viral DNA."
)

OLD_PARENT_TITLE = "Phosphorothioate restriction modules nick invading phage DNA"
NEW_PARENT_TITLE = "Phosphorothioate restriction modules target invading viral DNA"

OLD_PARENT_GRAPH_DESCRIPTION = (
    "Evidence-backed process sketch linking host DNA phosphorothioate "
    "modification to PT-dependent restriction, foreign-DNA nicking, and "
    "impaired phage DNA replication."
)
NEW_PARENT_GRAPH_DESCRIPTION = (
    "Evidence-backed process sketch linking host DNA phosphorothioate "
    "modification to PT-dependent self/non-self discrimination, "
    "restriction of invading viral DNA, and impaired viral DNA "
    "replication."
)

OLD_PARENT_SCOPE_NOTES = (
    "The graph captures system-level logic shared by "
    "phosphorothioate-based Dnd and Ssp restriction-modification systems "
    "without claiming that the DndFGH and SspE restriction modules sense "
    "or cleave DNA by one exact protein mechanism."
)
NEW_PARENT_SCOPE_NOTES = (
    "The graph captures system-level logic shared by phosphorothioate-"
    "based Dnd, Ssp, and Pbe antiviral systems without claiming that "
    "DndFGH, SspE, SspFGH, and PbeABCD sense PT marks, damage foreign "
    "DNA, or inhibit viral replication by one exact protein mechanism."
)
NEW_PARENT_GRAPH_ID = "phosphorothioate_dna_restriction_antiviral_defense"

OLD_DISCUSSION_PROMPT = (
    "Resolve archaeal phosphorothioate-based antiviral systems before "
    "minting additional narrower children under the phosphorothioate "
    "defense parent."
)
OLD_DISCUSSION_RATIONALE = (
    "The Dnd system is split out as traitmech:000221, the SspABCD-SspE "
    "single-restriction-enzyme system is split out as traitmech:000222, "
    "and the SspABCD-SspFGH system is split out as traitmech:000223. "
    "Archaeal phosphorothioate-based antiviral systems still need "
    "separate primary-source review before they can be split into a "
    "narrower TraitRecord with exact component groundings."
)
NEW_DISCUSSION_RATIONALE = (
    "Dnd, SspABCD-SspE, SspABCD-SspFGH, and archaeal "
    "DndCDEA-PbeABCD PT antiviral architectures have all been split out "
    "as narrower phosphorothioate defense system children."
)
PARENT_CHANGES = (
    "Minted traitmech:000224 for the archaeal DndCDEA-PbeABCD system, "
    "broadened the phosphorothioate defense system parent from "
    "bacteriophage-only Dnd/Ssp wording to Dnd/Ssp/Pbe viral-DNA "
    "restriction wording, and marked the phosphorothioate subfamily "
    "split-gap discussion resolved."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000224",
    "label": "DndCDEA-PbeABCD system",
    "definition": (
        "A phosphorothioate defense system in which an organism possesses "
        "a DndCDEA-PbeABCD locus that pairs DndCDEA-mediated host-DNA "
        "phosphorothioation with PbeABCD-dependent targeting of "
        "non-phosphorothioated viral DNA to inhibit viral DNA replication."
    ),
    "definition_source": XIONG,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000213"],
    "synonyms": [
        {
            "synonym_text": "PbeABCD-mediated PT defence system",
            "synonym_type": "EXACT_SYNONYM",
            "source": XIONG,
        },
    ],
    "evidence": [
        {
            "reference": XIONG,
            "snippet": (
                "a new archaeal defence system that involves "
                "DndCDEA-specific DNA phosphorothioate (PT) modification "
                "and the PbeABCD-mediated halt of virus propagation via "
                "inhibition of DNA replication"
            ),
            "notes": (
                "Xiong et al. name the DndCDEA-PbeABCD architecture as "
                "an archaeal PT-based antiviral system."
            ),
        },
        {
            "reference": XIONG,
            "snippet": (
                "can defend against viral attack together with pbeABCD, a "
                "conserved 4-gene cassette sharing no sequence homology "
                "with DndFGH"
            ),
            "notes": (
                "Xiong et al. support separating PbeABCD systems from "
                "canonical Dnd systems whose restriction module is DndFGH."
            ),
        },
        {
            "reference": XIONG,
            "snippet": (
                "DndCDEA-PbeABCD confers protection against the "
                "haloarchaeal virus SNJ1"
            ),
            "notes": (
                "Xiong et al. experimentally support the antiviral output "
                "of the Haloterrigena jeotgali A29 DndCDEA-PbeABCD locus "
                "after heterologous expression in CJ7-F cells."
            ),
        },
        {
            "reference": XIONG,
            "snippet": (
                "PbeABCD exerted antiviral activity depending on the "
                "presence of PT modifications"
            ),
            "notes": (
                "Xiong et al. connect PbeABCD antiviral restriction to "
                "phosphorothioation-dependent self/non-self "
                "discrimination."
            ),
        },
        {
            "reference": XIONG,
            "snippet": (
                "the subsequent viral genome replication process is "
                "significantly inhibited by the DndCDEA-PbeABCD system"
            ),
            "notes": (
                "Xiong et al. directly connect DndCDEA-PbeABCD to "
                "inhibition of SNJ1 viral DNA replication after viral DNA "
                "injection."
            ),
        },
        {
            "reference": XIONG,
            "snippet": (
                "does not involve viral DNA degradation or cleavage, "
                "ruling out the involvement of currently known defence "
                "mechanisms"
            ),
            "notes": (
                "Xiong et al. bound the PbeABCD mechanism away from the "
                "DNA-cleavage mechanisms of canonical restriction systems."
            ),
        },
        {
            "reference": ISAEV,
            "snippet": (
                "instead of the dndFGH, the restriction function is "
                "performed by the pbeABCD gene cluster"
            ),
            "notes": (
                "Isaev et al. summarize pbeABCD as the restriction branch "
                "paired with archaeal DndCDEA phosphorothioation."
            ),
        },
        {
            "reference": ISAEV,
            "snippet": (
                "The dndCDEA-pbeABCD from Haloterrigena jeotgali was "
                "shown to provide antiviral defense"
            ),
            "notes": (
                "Isaev et al. independently summarize the Haloterrigena "
                "jeotgali DndCDEA-PbeABCD locus as an antiviral defense "
                "system."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1455609",
            "taxon_label": "Natrinema thermotolerans A29",
            "note": (
                "Xiong et al. identified the dndCDEA-pbeABCD locus in "
                "Haloterrigena jeotgali A29 and showed that the cloned "
                "locus confers DndCDEA- and PbeABCD-dependent resistance "
                "to the haloarchaeal virus SNJ1."
            ),
            "reference": XIONG,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "dndcdea_pbeabcd_pt_viral_replication_inhibition",
            "title": "DndCDEA-PbeABCD systems halt archaeal viral DNA replication",
            "description": (
                "Evidence-backed process sketch linking a DndCDEA-PbeABCD "
                "locus to host DNA phosphorothioation, PT-dependent "
                "PbeABCD antiviral activity, and inhibited replication of "
                "non-phosphorothioated viral DNA."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures DndCDEA-PbeABCD restriction at the "
                "system level without asserting one universal host taxon, "
                "PT motif outside characterized haloarchaeal systems, "
                "PbeABCD subunit cycle, direct viral DNA cleavage, or "
                "relationship to bacterial DndFGH and Ssp-family systems."
            ),
            "nodes": [
                {
                    "node_id": "dndcdea_pbeabcd_locus",
                    "label": "DndCDEA-PbeABCD locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An archaeal phosphorothioation-dependent "
                        "antiviral locus pairing DndCDEA host-DNA "
                        "phosphorothioation with PbeABCD restriction "
                        "activity."
                    ),
                },
                {
                    "node_id": "dndcdea_dna_phosphorothioation",
                    "label": "DndCDEA DNA phosphorothioation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DndCDEA-mediated installation of sequence-"
                        "specific phosphorothioate marks on host DNA."
                    ),
                },
                {
                    "node_id": "pbeabcd_pt_dependent_virus_targeting",
                    "label": "PbeABCD PT-dependent virus targeting",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Phosphorothioate-dependent PbeABCD antiviral "
                        "activity against invading DNA that lacks host PT "
                        "marks."
                    ),
                },
                {
                    "node_id": "viral_dna_replication",
                    "label": "viral DNA replication",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Replication of invading archaeal viral DNA after "
                        "host cell entry."
                    ),
                },
                {
                    "node_id": "dndcdea_pbeabcd_system_trait",
                    "label": "DndCDEA-PbeABCD system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000224",
                    "description": (
                        "Possession of a genome-encoded DndCDEA-PbeABCD "
                        "phosphorothioation-dependent antiviral defense "
                        "system."
                    ),
                },
                {
                    "node_id": "phosphorothioate_defense_system_trait",
                    "label": "phosphorothioate defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000213",
                    "description": (
                        "Possession of a genome-encoded "
                        "phosphorothioate-based antiviral defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "dndcdea_pbeabcd_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dndcdea_dna_phosphorothioation",
                    "description": (
                        "The DndCDEA modification module installs "
                        "phosphorothioate marks on archaeal host DNA."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "involves DndCDEA-specific DNA "
                                "phosphorothioate (PT) modification"
                            ),
                            "notes": (
                                "Xiong et al. support DndCDEA-dependent "
                                "host DNA phosphorothioation in the "
                                "PbeABCD-coupled system."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dndcdea_pbeabcd_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pbeabcd_pt_dependent_virus_targeting",
                    "description": (
                        "DndCDEA-PbeABCD loci pair host-DNA "
                        "phosphorothioation with PbeABCD antiviral "
                        "activity."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "can defend against viral attack together "
                                "with pbeABCD"
                            ),
                            "notes": (
                                "Xiong et al. support the paired DndCDEA "
                                "modification and PbeABCD effector "
                                "architecture."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dndcdea_dna_phosphorothioation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pbeabcd_pt_dependent_virus_targeting",
                    "description": (
                        "PbeABCD antiviral activity depends on the "
                        "presence of PT marks rather than direct "
                        "PbeABCD-DndCDEA protein interactions."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "depending on the presence of PT "
                                "modifications"
                            ),
                            "notes": (
                                "Xiong et al. distinguish PT-dependent "
                                "PbeABCD restriction from direct "
                                "modification-effector protein coupling."
                            ),
                        }
                    ],
                },
                {
                    "subject": "pbeabcd_pt_dependent_virus_targeting",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "viral_dna_replication",
                    "description": (
                        "PbeABCD-dependent targeting inhibits replication "
                        "of non-phosphorothioated viral DNA."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "the subsequent viral genome replication "
                                "process is significantly inhibited"
                            ),
                            "notes": (
                                "Xiong et al. observed impaired SNJ1 "
                                "genome replication in cells expressing "
                                "DndCDEA-PbeABCD."
                            ),
                        }
                    ],
                },
                {
                    "subject": "pbeabcd_pt_dependent_virus_targeting",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "dndcdea_pbeabcd_system_trait",
                    "description": (
                        "PT-dependent PbeABCD antiviral activity realizes "
                        "the DndCDEA-PbeABCD defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": XIONG,
                            "snippet": (
                                "DndCDEA-PbeABCD confers resistance "
                                "against invading viruses"
                            ),
                            "notes": (
                                "Xiong et al. support PbeABCD-mediated "
                                "restriction as the system's antiviral "
                                "output."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dndcdea_pbeabcd_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phosphorothioate_defense_system_trait",
                    "description": (
                        "DndCDEA-PbeABCD possession is a "
                        "phosphorothioate-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": ISAEV,
                            "snippet": (
                                "instead of the dndFGH, the restriction "
                                "function is performed by the pbeABCD gene "
                                "cluster"
                            ),
                            "notes": (
                                "Isaev et al. place PbeABCD in the family "
                                "of PT defense systems while distinguishing "
                                "it from DndFGH."
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
    assert record["definition"] in {OLD_PARENT_DEFINITION, NEW_PARENT_DEFINITION}
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    record["definition"] = NEW_PARENT_DEFINITION

    new_parent_evidence = {
        "reference": XIONG,
        "snippet": (
            "DndCDEA-specific DNA phosphorothioate (PT) modification "
            "and the PbeABCD-mediated halt of virus propagation"
        ),
        "notes": (
            "Xiong et al. support DndCDEA-PbeABCD as an archaeal "
            "phosphorothioation-dependent antiviral branch distinct "
            "from bacterial DndFGH and Ssp systems."
        ),
    }
    evidence = record.setdefault("evidence", [])
    evidence = [
        item
        for item in evidence
        if not (
            item.get("reference") == new_parent_evidence["reference"]
            and item.get("snippet") == new_parent_evidence["snippet"]
        )
    ]
    evidence.append(new_parent_evidence)
    record["evidence"] = evidence

    graph = record["causal_graphs"][0]
    assert graph["graph_id"] in {
        "phosphorothioate_dna_nicking_antiphage_defense",
        NEW_PARENT_GRAPH_ID,
    }
    assert graph["title"] in {OLD_PARENT_TITLE, NEW_PARENT_TITLE}
    assert graph["description"] in {
        OLD_PARENT_GRAPH_DESCRIPTION,
        NEW_PARENT_GRAPH_DESCRIPTION,
    }
    assert graph["scope_notes"] in {OLD_PARENT_SCOPE_NOTES, NEW_PARENT_SCOPE_NOTES}

    graph["graph_id"] = NEW_PARENT_GRAPH_ID
    graph["title"] = NEW_PARENT_TITLE
    graph["description"] = NEW_PARENT_GRAPH_DESCRIPTION
    graph["scope_notes"] = NEW_PARENT_SCOPE_NOTES

    nodes = {node["node_id"]: node for node in graph["nodes"]}
    nodes["phosphorothioate_modification_module"]["description"] = (
        "A Dnd-, Ssp-, or Pbe-paired gene module that installs "
        "sequence-specific phosphorothioate modifications on host DNA."
    )

    if "foreign_dna_nicking" in nodes:
        viral_restriction = nodes.pop("foreign_dna_nicking")
        viral_restriction.update(
            {
                "node_id": "viral_dna_restriction",
                "label": "viral DNA restriction",
                "description": (
                    "Restriction of invading viral DNA by a PT-associated "
                    "Dnd, Ssp, or Pbe effector module."
                ),
            }
        )
        nodes["viral_dna_restriction"] = viral_restriction
    else:
        nodes["viral_dna_restriction"].update(
            {
                "label": "viral DNA restriction",
                "description": (
                    "Restriction of invading viral DNA by a PT-associated "
                    "Dnd, Ssp, or Pbe effector module."
                ),
            }
        )

    if "phage_dna_replication" in nodes:
        viral_replication = nodes.pop("phage_dna_replication")
        viral_replication.update(
            {
                "node_id": "viral_dna_replication",
                "label": "viral DNA replication",
                "description": "Replication of invading viral DNA after host cell entry.",
            }
        )
        nodes["viral_dna_replication"] = viral_replication
    else:
        nodes["viral_dna_replication"].update(
            {
                "label": "viral DNA replication",
                "description": "Replication of invading viral DNA after host cell entry.",
            }
        )

    nodes["phosphorothioate_defense_system_trait"]["description"] = (
        "Possession of a genome-encoded phosphorothioate-based antiviral "
        "defense system."
    )
    nodes["phage_defense_system"]["description"] = (
        "Possession of one or more genome-encoded immune systems that "
        "inhibit viral infection."
    )

    pbe_targeting_evidence = {
        "reference": XIONG,
        "snippet": (
            "PbeABCD exerted antiviral activity depending on the "
            "presence of PT modifications"
        ),
        "notes": "Xiong et al. support PT-dependent PbeABCD antiviral activity.",
    }
    pbe_replication_evidence = {
        "reference": XIONG,
        "snippet": (
            "PbeABCD-mediated halt of virus propagation via "
            "inhibition of DNA replication"
        ),
        "notes": (
            "Xiong et al. connect PbeABCD-dependent PT restriction to "
            "inhibited archaeal viral DNA replication."
        ),
    }
    pbe_family_evidence = {
        "reference": XIONG,
        "snippet": "a new type of PT-based virus resistance system",
        "notes": (
            "Xiong et al. place DndCDEA-PbeABCD in the PT "
            "antiviral defense family."
        ),
    }

    for edge in graph["edges"]:
        if edge["object"] == "foreign_dna_nicking":
            edge["object"] = "viral_dna_restriction"
        if edge["object"] == "phage_dna_replication":
            edge["object"] = "viral_dna_replication"
        if edge["subject"] == "foreign_dna_nicking":
            edge["subject"] = "viral_dna_restriction"

        if (
            edge["subject"] == "dna_phosphorothioation"
            and edge["object"] == "pt_dependent_foreign_dna_targeting"
        ):
            edge["description"] = (
                "Sequence-specific PT marks couple host DNA modification "
                "to PT-dependent self/non-self restriction by Dnd-, Ssp-, "
                "and Pbe-family effector modules."
            )

        if (
            edge["subject"] == "pt_dependent_foreign_dna_targeting"
            and edge["object"] == "viral_dna_restriction"
        ):
            edge["description"] = (
                "Dnd, Ssp, and Pbe phosphorothioation-dependent systems "
                "converge on restriction of viral DNA lacking host PT "
                "marks."
            )
            edge["evidence"] = [
                item
                for item in edge.get("evidence", [])
                if not (
                    item.get("reference") == pbe_targeting_evidence["reference"]
                    and item.get("snippet") == pbe_targeting_evidence["snippet"]
                )
            ]
            edge["evidence"].append(copy.deepcopy(pbe_targeting_evidence))

        if (
            edge["subject"] == "viral_dna_restriction"
            and edge["object"] == "viral_dna_replication"
        ):
            edge["description"] = (
                "PT-dependent effector activity inhibits replication of "
                "invading viral DNA."
            )
            edge["evidence"] = [
                item
                for item in edge.get("evidence", [])
                if not (
                    item.get("reference") == pbe_replication_evidence["reference"]
                    and item.get("snippet") == pbe_replication_evidence["snippet"]
                )
            ]
            edge["evidence"].append(copy.deepcopy(pbe_replication_evidence))

        if (
            edge["subject"] == "viral_dna_restriction"
            and edge["object"] == "phosphorothioate_defense_system_trait"
        ):
            edge["description"] = (
                "Restriction of invading viral DNA realizes "
                "phosphorothioate-based antiviral defense."
            )
            edge["evidence"] = [
                item
                for item in edge.get("evidence", [])
                if not (
                    item.get("reference") == pbe_family_evidence["reference"]
                    and item.get("snippet") == pbe_family_evidence["snippet"]
                )
            ]
            edge["evidence"].append(copy.deepcopy(pbe_family_evidence))

        if (
            edge["subject"] == "phosphorothioate_defense_system_trait"
            and edge["object"] == "phage_defense_system"
        ):
            edge["description"] = (
                "Phosphorothioate restriction-system possession is an "
                "antiviral defense-system trait."
            )
            edge["evidence"] = [
                item
                for item in edge.get("evidence", [])
                if not (
                    item.get("reference") == pbe_family_evidence["reference"]
                    and item.get("snippet") == pbe_family_evidence["snippet"]
                )
            ]
            edge["evidence"].append(copy.deepcopy(pbe_family_evidence))

    discussions = {
        item["discussion_id"]: item for item in record.get("discussions") or []
    }
    discussion = discussions["phosphorothioate-subfamily-split-gap"]
    assert discussion["kind"] == "KNOWLEDGE_GAP"
    assert discussion["status"] in {"OPEN", "RESOLVED"}
    assert discussion["prompt"] == OLD_DISCUSSION_PROMPT
    assert discussion["rationale"] in {
        OLD_DISCUSSION_RATIONALE,
        NEW_DISCUSSION_RATIONALE,
    }
    discussion["status"] = "RESOLVED"
    discussion["rationale"] = NEW_DISCUSSION_RATIONALE

    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=PARENT_CHANGES,
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
        upsert=True,
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
            "Minted DndCDEA-PbeABCD system as a DOI-backed GENOMICS "
            "TraitRecord under the phosphorothioate defense system "
            "parent after an ignored-and-hidden duplicate review found no "
            "exact live TraitMech, METPO, or prior proposal record; the "
            "replacement placeholder is reserved in "
            "proposals/metpo_traitmech_v101."
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
