"""Add evidence-backed toxicyst discharge with a conservative phenotype parent."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
SLUG = "toxicyst_discharge"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v561/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000685"
METPO_ID = "METPO:1063800"
PARENT_METPO_ID = "METPO:1000059"
CALCIUM = "DOI:10.1007/BF01279249"
COLEPS = "DOI:10.1111/jeu.12106"
GENOMICS = "DOI:10.1186/s12915-024-01904-2"
TIMESTAMP = "2026-10-08T18:21:12Z"
PARENT = {
    "identifier": PARENT_METPO_ID,
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "toxicyst discharge",
    "definition": (
        "A physiological phenotype in which a microbial cell releases material "
        "from toxicysts, its offensive extrusomes, to the cell exterior."
    ),
    "definition_source": COLEPS,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
    "evidence": [
        {
            "reference": COLEPS,
            "snippet": "we isolated the discharge of the toxicysts from living cells",
            "notes": (
                "PMID:24512001. Scientific Abstract read directly in PubMed and "
                "Europe PMC (EXT_ID:24512001 AND SRC:MED); source, title and DOI "
                "agree. Coleps hirtus discharge was collected and tested against "
                "other ciliates. This supports extracellular release from living "
                "cells, not merely possession of an organelle or toxicity of a "
                "whole-cell extract. Abstract-only access: full Methods and "
                "figures were not inspected; the institutional postprint at "
                "https://hdl.handle.net/11393/192287 is access-restricted. "
                "The reported chemical mixture is not a universal toxicyst cargo."
            ),
        },
        {
            "reference": CALCIUM,
            "snippet": (
                "Injection of Ca2+ evoked discharge of toxicysts, if the site of "
                "the injection was the periphery region of the proboscis."
            ),
            "notes": (
                "Scientific Summary read directly on the publisher page; Ca2+ "
                "represents its rendered superscript charge. Methods, Results "
                "and captions also read in the author-upload full-text transcript "
                "at https://www.researchgate.net/publication/227062328_Ca2_triggers_toxicyst_discharge_in_Didinium_nasutum. "
                "Figures were not visually inspected. Didinium nasutum pressure "
                "injection near the proboscis periphery produced discharge in "
                "8/11 cells versus 1/11 calcium-free controls; cell-body and "
                "central-proboscis injections did not. Iontophoretic injection "
                "caused damage and cytoplasm outflow, motivating pressure "
                "injection. These are assay-specific observations, not a "
                "universal calcium requirement or proof of a particular fusion "
                "protein. No PMID was resolved by the exact DOI query."
            ),
        },
        {
            "reference": GENOMICS,
            "snippet": (
                "However, our understanding of the genetic processes and specific "
                "toxins involved in toxicyst formation and discharge is still limited."
            ),
            "notes": (
                "PMID:38715037, PMC11077807. Scientific Abstract, Background, "
                "morphology Results, Discussion and collection/TEM Methods read "
                "in primary HTML/fullTextXML. Figure 1 was visually inspected: "
                "A-C are drawings, whereas D-F are TEM images of fixed Litonotus. "
                "The drawing of discharge is not direct imaging of release. "
                "Sequence and expression associations motivate toxin/transport "
                "hypotheses, not experimentally resolved discharge mechanisms. "
                "Genomics supplements were not inspected and are not used for "
                "accessions, prevalence or functional assignments."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "toxicyst-discharge-scope-and-parent",
            "prompt": "Resolve the exocytosis hierarchy without equating all extrusome types.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Parent phenotype METPO:1000059 is conservative. The 2024 "
                "Background describes telescopic discharge and/or membrane "
                "fusion; its Discussion reports fusion observations. These "
                "statements do not establish that every toxicyst-discharge "
                "phenotype satisfies the fusion-pore definition of exocytosis "
                "traitmech:000637. That placement remains unresolved, not "
                "excluded. Mere toxicyst possession, docking, predation, prey "
                "injury or cell lysis does not alone establish this trait. "
                "Preserve the organelle-specific scope rather than equating "
                "mucocyst discharge traitmech:000684, trichocyst discharge "
                "traitmech:000683, pexicysts or haptocysts. Historical type-I/II "
                "terminology needs reconciliation before synonym or hierarchy "
                "expansion. No exact synonyms, xrefs or organism-level "
                "disjointness are asserted. Prey killing and complete emptying "
                "are not universal defining requirements."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "toxicyst-discharge-provenance-and-mechanism",
            "prompt": "Resolve experimental culture provenance and protein-level mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Natural provenance and strain-level taxonomy of the positive "
                "experimental cultures remain unchecked; no canonical examples "
                "are assigned. Wild-collected genomic material is not by itself "
                "a positive discharge assay for that isolate. Gene-family "
                "expansion, expression and predicted toxin annotations alone "
                "do not establish toxicyst discharge or a causal protein. "
                "A future graph needs source-specific perturbations and "
                "taxon-paired accessions, distinguishing assembly, triggering, "
                "extrusion and toxin action. Mechanism is deferred, not claimed "
                "absent. Do not transfer a calcium threshold, cargo chemistry "
                "or ecological function between species without evidence."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added toxicyst discharge with three primary DOI sources and "
            "directly checked abstract/Summary snippets. Ignored-and-hidden "
            "main/worktree/open-PR checks support 000685 and v561 block "
            "1063800-1063899. Retained phenotype parent while making the "
            "exocytosis placement explicit and unresolved. Distinguished "
            "discharge from damage, organelle possession and sequence-based "
            "predictions. Existing records unchanged. Timestamp is observed UTC."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "Toxicyst material release; exocytosis hierarchy unresolved.", IDENTIFIER],
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
