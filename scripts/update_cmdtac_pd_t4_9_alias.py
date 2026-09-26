#!/usr/bin/env python3
"""Connect DefenseFinder PD-T4-9 model evidence to CmdTAC."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "cmdtac_system.yaml"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_WIKI_COMMIT = "ee7647d8"
DEFENSEFINDER_WIKI = (
    "https://gitlab.pasteur.fr/mdm-lab/wiki/-/raw/"
    f"{DEFENSEFINDER_WIKI_COMMIT}/content/3.defense-systems/pd-t4-9.md"
)
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

TIMESTAMP = "2026-09-26T21:51:06Z"

COMPONENT_SNIPPET = (
    "The CmdTAC system operates through a hierarchy of components where "
    "roles are distinctly defined:\n"
    "* Effector: The CmdT protein (formerly PD-T4-9-A) is the Toxin. Its "
    "functional type is Enzymatic, specifically an ADP-ribosyltransferase "
    "(ART). It performs the irreversible defense action by chemically "
    "modifying the target.\n"
    "* Sensor: The CmdC protein (formerly PD-T4-9-C) is the Chaperone. Its "
    "functional type is Binding/Structural. It maintains the inactive state "
    "and serves as the molecular surveillance unit that recognizes the "
    "infection.\n"
    "* Inhibitor/Switch: The CmdA protein (formerly PD-T4-9-B) is the "
    "Antitoxin. Its functional type is Regulatory/Substrate. It neutralizes "
    "the Toxin (CmdT) and its controlled degradation is the essential switch "
    "mechanism for activation."
)
COMPOSITION_SNIPPET = (
    "The PD-T4-9 is composed of 3 proteins: PD-T4-9_A, PD-T4-9_B and "
    "PD-T4-9_C."
)
REFSEQ_SNIPPET = (
    "The PD-T4-9 system in *Vibrio parahaemolyticus* "
    "(GCF_001700835.1, NZ_CP010883) is composed of 3 proteins "
    "PD-T4-9_C (WP_065870458.1) PD-T4-9_B (WP_141106056.1) "
    "PD-T4-9_A (WP_065870460.1)"
)
RULES_SNIPPET = (
    "PD-T4-9\tPD-T4-9\t2\t2\t"
    "PD-T4-9__PD-T4-9_A, PD-T4-9__PD-T4-9_C\t"
    "PD-T4-9__PD-T4-9_B\t\t"
)
HMM_SNIPPET = (
    "| PD-T4-9__PD-T4-9_A                               | "
    "PD-T4-9__PD-T4-9_A                               | "
    "PD-T4-9                | Custom                  | 20     |\n"
    "| PD-T4-9__PD-T4-9_B                               | "
    "PD-T4-9__PD-T4-9_B                               | "
    "PD-T4-9                | Custom                  | 20     |\n"
    "| PD-T4-9__PD-T4-9_C                               | "
    "PD-T4-9__PD-T4-9_C                               | "
    "PD-T4-9                | Custom                  | 20     |"
)

PD_T4_9_SYNONYM = {
    "synonym_text": "PD-T4-9",
    "synonym_type": "RELATED_SYNONYM",
    "source": DEFENSEFINDER_WIKI,
}

PD_T4_9_EVIDENCE = [
    {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": COMPONENT_SNIPPET,
        "notes": (
            "The DefenseFinder PD-T4-9 page aliases the CmdT, CmdC, and "
            "CmdA components to their former PD-T4-9-A, PD-T4-9-C, and "
            "PD-T4-9-B labels."
        ),
    },
    {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": COMPOSITION_SNIPPET,
        "notes": (
            "The DefenseFinder wiki names the three PD-T4-9 profile "
            "components in the CmdTAC system model."
        ),
    },
    {
        "reference": DEFENSEFINDER_WIKI,
        "snippet": REFSEQ_SNIPPET,
        "notes": (
            "The DefenseFinder wiki illustrates a predicted PD-T4-9 locus "
            "in RefSeq assembly GCF_001700835.1 on NZ_CP010883."
        ),
    },
    {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The pinned DefenseFinder rules table models PD-T4-9 with "
            "PD-T4-9__PD-T4-9_A and PD-T4-9__PD-T4-9_C as required "
            "profiles and PD-T4-9__PD-T4-9_B as an exchangeable profile."
        ),
    },
    {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_SNIPPET,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            "PD-T4-9__PD-T4-9_A, PD-T4-9__PD-T4-9_B, and "
            "PD-T4-9__PD-T4-9_C under the PD-T4-9 system namespace."
        ),
    },
]

DISCUSSION_PROMPT = (
    "Resolve CmdTAC family breadth and phage escape routes before minting "
    "narrower CmdTAC mechanism children."
)
DISCUSSION_RATIONALE = (
    "Vassallo et al. support CmdTAC as a toxin-antitoxin-chaperone "
    "abortive-infection system in which CmdC senses viral capsid proteins "
    "and liberates the CmdT mRNA ADP-ribosyltransferase. The DefenseFinder "
    "PD-T4-9 page aliases the same system through former PD-T4-9 component "
    "names, and the pinned DefenseFinder HMM inventory and rules table model "
    "PD-T4-9 with required PD-T4-9__PD-T4-9_A and PD-T4-9__PD-T4-9_C "
    "profiles plus optional PD-T4-9__PD-T4-9_B. Phage specificity beyond "
    "Tevenvirinae, escape routes, and natural family breadth remain "
    "unresolved."
)
SCOPE_NOTES = (
    "The graph captures CmdTAC as a named toxin-antitoxin-chaperone "
    "abortive-infection system from Escherichia coli ECOR22 and links "
    "DefenseFinder's PD-T4-9 model namespace to that same three-component "
    "system, while leaving phage specificity beyond Tevenvirinae, escape "
    "routes, and natural family breadth unresolved."
)
CHANGE_NOTE = (
    "Recorded PD-T4-9 as a DefenseFinder related label for CmdTAC after an "
    "ignored-and-hidden duplicate review found that PD-T4-9 denotes the "
    "existing CmdTAC system; added the pinned PD-T4-9 DefenseFinder rule and "
    "HMM rows and resolved the DefenseFinder model-coverage half of the open "
    "CmdTAC knowledge gap."
)


def evidence_key(item: dict[str, Any]) -> tuple[str | None, str | None]:
    return item.get("reference"), item.get("snippet")


def update_record(doc: dict[str, Any]) -> None:
    if doc.get("identifier") != "traitmech:000335":
        raise ValueError(f"unexpected identifier: {doc.get('identifier')}")
    if doc.get("label") != "CmdTAC system":
        raise ValueError(f"unexpected label: {doc.get('label')}")
    if doc.get("mapping_status") != "PROPOSED":
        raise ValueError(f"unexpected mapping status: {doc.get('mapping_status')}")
    if doc.get("parent_traits") != ["traitmech:000214"]:
        raise ValueError(f"unexpected parents: {doc.get('parent_traits')}")

    synonyms = doc.setdefault("synonyms", [])
    if not any(item.get("synonym_text") == "PD-T4-9" for item in synonyms):
        synonyms.append(copy.deepcopy(PD_T4_9_SYNONYM))

    evidence = doc.setdefault("evidence", [])
    seen = {evidence_key(item) for item in evidence}
    for item in PD_T4_9_EVIDENCE:
        if evidence_key(item) not in seen:
            evidence.append(copy.deepcopy(item))

    graphs = doc.get("causal_graphs") or []
    if len(graphs) != 1 or graphs[0].get("graph_id") != "cmdtac_mrna_adp_ribosylation_aborts_phage":
        raise ValueError("unexpected CmdTAC causal graph layout")
    old_scope = graphs[0].get("scope_notes", "")
    if "absence of pinned DefenseFinder HMM or rule rows unresolved" in old_scope:
        graphs[0]["scope_notes"] = SCOPE_NOTES
    elif old_scope != SCOPE_NOTES:
        raise ValueError("CmdTAC scope note was already edited")

    discussions = doc.get("discussions") or []
    for discussion in discussions:
        if discussion.get("discussion_id") != "cmdtac-family-and-model-coverage-gap":
            continue
        if discussion.get("status") != "OPEN":
            raise ValueError("CmdTAC model-coverage discussion is not open")
        rationale = discussion.get("rationale", "")
        if "HMM inventory or rules table" in rationale:
            discussion["prompt"] = DISCUSSION_PROMPT
            discussion["rationale"] = DISCUSSION_RATIONALE
        elif (
            discussion.get("prompt") != DISCUSSION_PROMPT
            or rationale != DISCUSSION_RATIONALE
        ):
            raise ValueError("CmdTAC model-coverage rationale was already edited")
        discussion["evidence"] = copy.deepcopy(PD_T4_9_EVIDENCE)
        break
    else:
        raise ValueError("CmdTAC model-coverage discussion is missing")

    record_curation_event(
        doc,
        curator="codex",
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=CHANGE_NOTE,
        llm_assisted=True,
        timestamp=TIMESTAMP,
        upsert=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the updated CmdTAC record instead of printing a dry run",
    )
    args = parser.parse_args()

    doc = yaml.safe_load(TARGET.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise TypeError(f"{TARGET} did not parse to a mapping")

    update_record(doc)

    if args.apply:
        write_validated_trait(doc, TARGET)
    else:
        yaml.safe_dump(doc, sys.stdout, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
