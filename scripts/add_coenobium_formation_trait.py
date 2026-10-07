"""Add coenobium formation with source-bounded developmental scope."""

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
SLUG = "coenobium_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v531/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000655"
METPO_ID = "METPO:1060800"
TERMINOLOGY = "DOI:10.1098/rspb.2023.1882"
MICROSCOPY = "DOI:10.1242/jcs.212233"
PLASTICITY = "DOI:10.1038/s41598-018-28627-z"
TIMESTAMP = "2026-10-07T01:56:55Z"
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
    "label": "coenobium formation",
    "definition": (
        "A morphological phenotype in which an alga forms clonal multicellular "
        "colonies whose cell complement is established during colony formation, "
        "with subsequent colony growth by cell enlargement rather than addition "
        "of cells."
    ),
    "definition_source": TERMINOLOGY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "characteristically form clonal colonies of fixed cell number "
                "known as coenobia."
            ),
            "notes": (
                "Harvey (2023), PMID:37876191, PMC10598416, Comparisons with "
                "extant taxa. Direct full-text terminology passage covers "
                "Volvocales, Scenedesmaceae and Hydrodictyaceae. Growth after "
                "colony formation is by cell expansion; a later reproductive "
                "cycle makes daughter colonies. This comparison supports "
                "terminology, not a new experiment on living algae; the "
                "paper's fossil developmental reconstruction remains an inference."
            ),
        },
        {
            "reference": MICROSCOPY,
            "snippet": (
                "progeny were unicellular in three species and multicellular "
                "(joined in a sheet-like coenobium) in two."
            ),
            "notes": (
                "Cardon et al. (2018), PMID:29487180, scientific abstract. "
                "Primary Results, Methods and actual Figure 1 were inspected. "
                "The coenobial species are Enallax costatus and Tetradesmus "
                "obliquus; multiple fission occurs in all five tested species "
                "and alone does not establish coenobial progeny. Figure 1 "
                "supports joined-cell morphology. Release is author-reported "
                "in the Results, not visible in Figure 3; supplementary "
                "Figure S1 and movies were not directly inspected."
            ),
        },
        {
            "reference": PLASTICITY,
            "snippet": (
                "monocultures of D. opoliensis in the control groups (without "
                "IAA treatment) were dominated by two-celled and four-celled coenobia"
            ),
            "notes": (
                "Chung et al. (2018), PMID:29980731, PMC6035231, Results. "
                "Direct full text reports this morphology after one week; "
                "Methods describes native isolates cultured in CA medium. "
                "Higher indole-3-acetic acid concentrations favor unicells "
                "in the tested monocultures, so IAA is not a universal "
                "coenobium inducer. No percentage, causal protein claim or "
                "direct figure inspection is asserted here."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:113528",
            "taxon_label": "Enallax costatus",
            "reference": MICROSCOPY,
            "note": (
                "CCAP 276/31 (paper: CCAP 276-31), grown at 25 C on a "
                "12:12 light/dark cycle in a 1:1 mixture of Bold's basal "
                "medium with micronutrients and Woods Hole medium. Figure 1 "
                "and Results document coenobial morphology, not an invariant "
                "state for every life stage. Collection provenance at "
                "https://www.ccap.ac.uk/catalogue/strain-276-31 identifies "
                "Hegewald's 1980 Finnish lake isolate and lists GMO: No. "
                "The paper describes unialgal cultures, not axenic cultures."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "coenobium-formation-scope-and-hierarchy",
            "prompt": "Review a multicellular morphology parent and exact mappings.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Cell shape METPO:1000666 "
                "is individual-cell morphology; colony morphology "
                "METPO:1007062 concerns macroscopic colony characteristics. "
                "Obsolete cell arrangement METPO:1000046 and aggregate "
                "METPO:1000011 are not active parents. Palmelloid formation "
                "traitmech:000654 covers mother-wall retention or extracellular "
                "adhesion, not this developmental cell-complement criterion. "
                "Rosette cell arrangement traitmech:000652 requires inward "
                "cell poles, and biofilm formation traitmech:000053 requires "
                "surface attachment; neither is required here. A coenocyte "
                "is a multinucleate cell, not a multicellular coenobium. "
                "No exact synonym, xref or organism-level disjointness is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "coenobium-formation-development-and-mechanism",
            "prompt": "Resolve organism-specific colony development before graphing.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Fixed cell complement describes an individual colony, not "
                "one invariant count across taxa or conditions. Reproduction "
                "can form new daughter colonies. Harvey's extant comparisons "
                "include motile forms and Volvox germ-soma differentiation; "
                "Chung's introductory little-or-no-specialization formulation "
                "is not imposed universally. Neither a sheet shape, common "
                "wall, power-of-two count, lack of flagella nor grazer induction "
                "defines the class. Defer a causal graph pending perturbation "
                "and accession-level evidence: Cardon's observed Golgi "
                "localization and cell rotation do not demonstrate causal "
                "necessity for coenobium formation. Gene possession alone "
                "does not establish this phenotype."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added coenobium formation with three DOI-backed snippets, a "
            "qualified Enallax costatus example and developmental scope "
            "boundaries. Ignored-and-hidden searches and structured METPO "
            "review found no exact record. Reserved METPO:1060800 in v531; "
            "existing records unchanged."
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
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Developmentally established clonal colony cell complement; not generic aggregation.",
         IDENTIFIER],
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
