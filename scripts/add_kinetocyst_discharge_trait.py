"""Add source-bounded kinetocyst discharge through the validated writer."""

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
SLUG = "kinetocyst_discharge"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v563/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000687"
METPO_ID = "METPO:1064000"
PARENT_METPO_ID = "METPO:1000059"
DISCHARGE = "DOI:10.1078/0932-4739-00847"
INDUCED = "DOI:10.1515/znc-1976-3-418"
CONFERENCE = "https://protistology.jp/journal/congress_ab/53th_kobe/Abstract%20Book%20Kobe2020"
TIMESTAMP = "2026-10-10T04:04:55Z"
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
    "label": "kinetocyst discharge",
    "definition": (
        "A physiological phenotype in which a microbial cell releases material "
        "from kinetocysts to the cell exterior."
    ),
    "definition_source": DISCHARGE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
    "evidence": [
        {
            "reference": DISCHARGE,
            "snippet": (
                "By electron microscopy, we show evidence that the kinetocyst is an "
                "extrusive organelle that discharges its contents upon food capture."
            ),
            "notes": (
                "Sakaguchi et al. 2002, scientific Abstract directly read on "
                "2026-10-10 at https://www.researchgate.net/publication/222864147. "
                "Electron microscopy of Raphidiophrys contractilis supports release "
                "during food capture, with the posterior remaining cell-attached "
                "and the anterior directed toward prey. The proposed scaffold role "
                "is not demonstrated causality. Crossref identifies the 2002 "
                "publication; ResearchGate's date and automatically linked author "
                "profile are not used as authority. Publisher access returned 403; "
                "full Methods and figures were not inspected. No universal toxin, "
                "prey-killing requirement or trigger is inferred."
            ),
        },
        {
            "reference": INDUCED,
            "snippet": (
                "Freeze-fracture studies reveal that extrusive organelles displaying "
                "saltatory particle movements in centrohelidian axopod are attached "
                "to highly ordered domains within the plasma membrane."
            ),
            "notes": (
                "Bardele 1976, PMID:134561. Scientific abstract and primary full-text "
                "OCR directly read on 2026-10-10 at "
                "https://www.researchgate.net/publication/22999924. The snippet "
                "supports organelle identity and membrane attachment, not discharge "
                "alone. Printed pp191-193 describe formaldehyde-fume-induced release "
                "in living whole mounts and negative-stained expelled jacket "
                "material. Methods name Acanthocystis erinaceoides and Raphidiophrys "
                "ambigua; this observation is not assigned here to just one species. "
                "The author interprets kinetocysts as compound motile mucocysts. "
                "Food-trapping and movement models remain hypotheses. PDF images "
                "were unavailable; no visual audit or OCR-normalized quotation is "
                "claimed. The article year is 1976, not the later upload date."
            ),
        },
        {
            "reference": CONFERENCE,
            "snippet": (
                "In this study, we used Tetrahymena thermophila as food and examined "
                "the process of food capturing and kinetocyst discharge by electron "
                "microscopy."
            ),
            "notes": (
                "Wan and Suzaki, JSP/KSOP joint meeting, 22-23 November 2020, "
                "O-BPA06/P-1A01, printed pp11-12 (PDF indices 10-11). Primary "
                "conference abstract, not a peer-reviewed full paper. Both pages "
                "were visually inspected on 2026-10-10. The snippet establishes "
                "assay context in Raphidiophrys contractilis, not the outcome alone. "
                "Following results describe stretched filamentous contents and "
                "expansion of the ring structure after discharge. Immuno-EM MVP "
                "localization suggests a prey-recognition role but does not "
                "establish causal necessity or a conserved release mechanism. "
                "Tetrahymena is prey here, not the kinetocyst-bearing organism."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "kinetocyst-discharge-scope-and-parent",
            "prompt": "Resolve historical mucocyst terminology and exocytosis placement.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059 pending hierarchy review. Bardele "
                "1976 interprets kinetocysts as compound motile mucocysts; preserve "
                "that attribution rather than asserting separation from every "
                "historical mucocyst umbrella. Existing mucocyst discharge "
                "traitmech:000684 uses a membrane-fusion release definition supported "
                "in Tetrahymena and explicitly defers terminology reconciliation. "
                "Neither exact equivalence nor a mucocyst parent is established "
                "here. The fusion-pore differentia of exocytosis traitmech:000637 "
                "also needs class-wide scope review; placement is unresolved, not "
                "excluded. Possession, docking, axopodial movement or contraction, "
                "prey adhesion, ingestion and nonspecific cell lysis alone do not "
                "demonstrate discharge. Complete emptying, prey death and one "
                "universal trigger are not required. Historical conicyst organelle "
                "terminology does not automatically establish an exact phenotype "
                "synonym. No equivalence to haptocyst discharge traitmech:000686, "
                "homology, disjointness, exact synonyms or xrefs are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "kinetocyst-discharge-exemplars-and-mechanism",
            "prompt": "Resolve assay-strain provenance and release-specific molecular evidence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned: full primary assay Methods "
                "and their relation to the deposited natural culture need joint "
                "verification. The evidence items have different scopes, not three "
                "equivalent discharge replications. Organelle ultrastructure and "
                "protein localization alone do not establish a causal release "
                "pathway. Separate assembly, movement, triggering, extrusion, "
                "attachment and ingestion before adding graph edges. A protein "
                "mechanism needs direct functional evidence and taxon-paired "
                "accessions; sequence features alone cannot provide that support. "
                "Mechanism is deferred, not claimed absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added kinetocyst discharge with two primary DOI citations and a "
            "primary conference abstract, source-checked snippets and explicit "
            "access limits. Ignored-and-hidden main/worktree/open-PR reservation "
            "checks support 000687 and v563 block 1064000-1064099. Historical "
            "mucocyst scope, exocytosis placement, canonical exemplars and protein "
            "mechanism remain unresolved. Existing records unchanged. Timestamp "
            "records the observed UTC curation decision."
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
         "Kinetocyst material release; historical mucocyst hierarchy unresolved.", IDENTIFIER],
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
