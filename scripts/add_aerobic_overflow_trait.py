"""Add aerobic overflow metabolism through the guarded validated writer."""

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
SLUG = "aerobic_overflow_metabolism"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v581/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000705"
METPO_ID = "METPO:1065800"
IDENTITY = "DOI:10.1038/msb.2009.82"
BACTERIAL = "DOI:10.1038/nature15765"
YEAST = "DOI:10.1111/febs.13019"
TIMESTAMP = "2026-10-12T01:03:22Z"
CORRECTION_TIMESTAMP = "2026-10-12T01:08:15Z"
ORIGINAL_RESPIRATION_NOTE = "Figure 2 does not show a first-hour respiratory decrease in those yeasts."
CORRECTED_RESPIRATION_NOTE = (
    "The authors report no first-hour repression of respiration; Figure 2 does "
    "not establish monotonic or unchanged oxygen-consumption rates."
)
PARENT = {
    "identifier": "METPO:1000059",
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
    "label": "aerobic overflow metabolism",
    "definition": (
        "A physiological phenotype in which microbial cells divert part of their "
        "catabolic carbon flux to excreted, incompletely oxidized products with "
        "lower ATP yield per substrate than complete respiration, despite "
        "possessing respiratory capacity and sufficient oxygen for respiration."
    ),
    "definition_source": IDENTITY,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": IDENTITY,
            "snippet": (
                "S. cerevisiae and E. coli fully oxidize glucose at low "
                "concentrations and shift to overflow metabolism at high glucose "
                "concentrations."
            ),
            "notes": (
                "Molenaar et al. 2009, PMID:19888218, PMC2795476; Current growth "
                "models and their limitations, not the abstract. The surrounding "
                "paragraph supplies the fully aerobic, incomplete-oxidation and "
                "retained respiratory-capacity differentia. This Perspective "
                "contains original modeling, not new experimental replication of "
                "the cited organisms. The terminology discussion also includes "
                "mixed-acid-to-lactate shifts; the qualified label here does not "
                "define every use of unqualified overflow metabolism."
            ),
        },
        {
            "reference": BACTERIAL,
            "snippet": (
                "cells use fermentation instead of the more efficient respiration "
                "to generate energy, despite the availability of oxygen."
            ),
            "notes": (
                "Basan et al. 2015, PMID:26632588, PMC4843128; scientific abstract. "
                "Relevant Results, growth Methods, model scope, Extended Data "
                "Table 1, actual Figure 1 and Extended Data Figure 2 were inspected "
                "through public XML and figure assets. Acetate excretion depends "
                "on growth conditions; the fitted threshold is not universal. "
                "The oxidative-fermentation accounting includes oxygen-dependent "
                "NADH oxidation. Net excretion does not exclude acetate reuptake. "
                "Proteome allocation is a tested model in this system, not a "
                "necessary mechanism for every member of the trait. Complete "
                "supplements, equations and referenced batch-culture methods were "
                "not independently reanalyzed. Publisher retrieval failed; the "
                "public full-text XML was accessible."
            ),
        },
        {
            "reference": YEAST,
            "snippet": (
                "We generated an extensive collection of data on glucose and "
                "oxygen consumption, and ethanol and carbon dioxide generation."
            ),
            "notes": (
                "Hagman et al. 2014, PMID:25161062, PMC4240471; scientific "
                "abstract. Introduction, relevant Results, Experimental procedures "
                "and actual Figures 1-2 were inspected. Glucose pulses into "
                "initially respiratory cultures produced ethanol in responsive "
                "yeasts while dissolved oxygen was controlled above 30% air "
                "saturation. Figure 2 does not show a first-hour respiratory "
                "decrease in those yeasts. Replication excludes V. polyspora; "
                "E. coryli received supplementation. This short-term Crabtree "
                "assay is not an exact synonym for the entire microbial phenotype. "
                "Supplemental time series and strain origins were not fully reviewed."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "aerobic-overflow-scope-and-parent",
            "prompt": "Retain oxygen-sufficient overflow as a conditional phenotype with an explicit hierarchy boundary.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The qualifier aerobic is deliberate. Unqualified overflow, "
                "Crabtree effect, respiro-fermentation and industrial aerobic "
                "fermentation are not asserted as exact synonyms. The local "
                "METPO:1002005 fermentation record is donor/acceptor-defined and "
                "excludes external electron acceptors; Basan's oxidative branch "
                "uses different accounting. https://github.com/berkeleybop/metpo/issues/468 discusses fermentation "
                "hierarchy, and the pinned ontology already differs from the "
                "retained local parent/definition. Neither that process nor "
                "METPO:1000060 metabolism is adopted as an is-a parent of this "
                "organismal phenotype. METPO:1000059 phenotype is used pending "
                "upstream hierarchy review. Product-specific ethanol/butanediol "
                "fermentation, aerotolerance, facultative anaerobiosis, copiotrophy "
                "and diauxic growth are not equivalent. Product detection or "
                "oxygen presence alone is insufficient: oxygen limitation must "
                "be excluded. No universal substrate, product, concentration, "
                "growth-rate threshold, complete respiratory shutdown or fixed "
                "molecular mechanism is required."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "aerobic-overflow-examples-and-mechanism",
            "prompt": "Resolve natural strain provenance and taxon-specific mechanisms before adding canonical examples or a graph.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Laboratory reference strains and engineered perturbations are "
                "qualified evidence, not proof that every member of a species "
                "has this phenotype under all conditions. Canonical taxa require "
                "primary strain provenance and authority-resolved identities. "
                "No common protein-resolved causal graph is established here; "
                "bacterial and yeast mechanisms must retain their experimental "
                "scope. Gene presence and predicted flux alone do not demonstrate "
                "overflow. Canonical examples, causal graphs and external xrefs "
                "are therefore unasserted. Qualified MED and Crossref records "
                "for all three citations exposed no linked correction or "
                "retraction on 2026-10-12; this bounded check is not a guarantee "
                "that no notice exists. Basan's publisher access remains unavailable."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
    ],
}


def build_initial_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added aerobic overflow metabolism with three DOI-backed sources "
            "and directly checked snippets. Reserved 000705, v581 and "
            "1065800-1065899 after ignored/hidden worktree and pending-PR checks. "
            "Oxygen-sufficient scope, hierarchy and inference limits are explicit. "
            "Existing traits unchanged; timestamp is the observed UTC curation decision."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_record() -> dict:
    record = build_initial_record()
    notes = record["evidence"][2]["notes"]
    assert notes.count(ORIGINAL_RESPIRATION_NOTE) == 1
    record["evidence"][2]["notes"] = notes.replace(
        ORIGINAL_RESPIRATION_NOTE, CORRECTED_RESPIRATION_NOTE,
    )
    record_curation_event(
        record, curator="codex", action="CLARIFIED_EVIDENCE_SCOPE",
        changes=(
            "Address #1881: distinguish the authors' reported lack of early "
            "respiratory repression from a claim that individual oxygen-consumption "
            "rates never decrease. Retain the original curation event unchanged."
        ),
        llm_assisted=True, timestamp=CORRECTION_TIMESTAMP,
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
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Conditional oxygen-sufficient phenotype; no universal pathway asserted.", IDENTIFIER],
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
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (build_initial_record(), record):
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
