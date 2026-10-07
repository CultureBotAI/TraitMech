"""Add pseudohyphal growth with source-specific induction boundaries."""

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
SLUG = "pseudohyphal_growth"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v529/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000653"
METPO_ID = "METPO:1060600"
MICROSCOPY = "DOI:10.1590/S1517-83822013005000056"
YEAST = "DOI:10.1016/0092-8674(92)90079-r"
TIMESTAMP = "2026-10-06T23:54:28Z"
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
    "label": "pseudohyphal growth",
    "definition": (
        "A morphological phenotype in which elongated budding yeast cells remain "
        "attached in chains with constrictions at the junctions between cells."
    ),
    "definition_source": MICROSCOPY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MICROSCOPY,
            "snippet": (
                "pseudohyphae formed branched chains of elongated blastoconidial "
                "cells retaining constrictions at the septal junctions"
            ),
            "notes": (
                "Staniszewska et al. (2013), PMID:24516422, PMC3910194, Results "
                "subsection Pseudohyphae. Full-text XML, strain/culture Methods, "
                "Table 1 and actual Figure 4 were inspected. Clinical isolate "
                "82 forms pseudohyphae mixed with true hyphae after six hours "
                "in serum; later hyphal predominance is not a contradictory "
                "same-time observation. The quote is from Results, not the "
                "abstract. Numerical morphology indices and serum induction "
                "conditions are study-specific, not universal trait thresholds."
            ),
        },
        {
            "reference": YEAST,
            "snippet": (
                "Cells become long and thin and form pseudohyphae that grow "
                "away from the colony and invade the agar medium."
            ),
            "notes": (
                "Gimeno et al. (1992), PMID:1547504, scientific abstract directly "
                "retrieved through Europe PMC. Diploid Saccharomyces cerevisiae "
                "under nitrogen starvation changes morphology and budding "
                "pattern. The abstract also reports RAS2, SHR3 and RSR1/BUD1 "
                "perturbations. Full text and figures were not verified. "
                "Diploidy, nitrogen starvation and agar invasion describe this "
                "study, not necessary conditions for every pseudohyphal yeast."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:5476",
            "taxon_label": "Candida albicans",
            "reference": MICROSCOPY,
            "note": (
                "Wild-type clinical bloodstream isolate 82, cultured in "
                "undiluted human serum for six hours at 37 C. Results and "
                "Figure 4A,C show pseudohyphae in a mixed population, not "
                "every cell or culture stage. Table 1 and Methods identify "
                "its clinical origin separately from the engineered comparison "
                "strains. This is an in-vitro morphology observation, not proof "
                "of pseudohyphae in the patient's bloodstream. NCBI Taxonomy "
                "resolves the species identifier and label."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "pseudohyphal-growth-scope-and-hierarchy",
            "prompt": "Review a yeast growth-form parent and exact external mappings.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Mycelial growth "
                "traitmech:000074 is explicitly bacterial. Filament shaped "
                "METPO:1000674 has a broad hypha-like description but is "
                "classified under individual cell shape METPO:1000666; this "
                "record denotes attached budding-cell chains, not merely an "
                "elongated cell. Colony morphology METPO:1007062 concerns "
                "macroscopic colonies, not this microscopic growth form. "
                "Obsolete cell arrangement METPO:1000046 is not an active "
                "parent. Do not equate pseudohyphae with uninterrupted true "
                "hyphae, disordered aggregation, or every filamentous form. "
                "No exact synonym or xref is asserted. Different forms may "
                "coexist in one culture; this is not organism-level disjointness."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "pseudohyphal-growth-mechanism-scope",
            "prompt": "Resolve organism-specific morphogenesis mechanisms before graphing.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "A causal graph is deferred pending full perturbation and "
                "protein-accession review, not because mechanisms are unknown. "
                "Do not transfer the 1992 budding-pattern or ploidy constraints "
                "to all yeasts, or treat the Candida comparison mutants as "
                "natural canonical examples. Gene possession alone does not "
                "establish pseudohyphal growth. Serum exposure, branching, "
                "agar invasion, numerical aspect-ratio cutoffs and virulence "
                "are not universal requirements. The 2013 study's bloodstream "
                "pathogenesis discussion does not directly demonstrate a "
                "pseudohypha-specific virulence mechanism. Additional "
                "Saccharomyces examples need direct strain-provenance review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added pseudohyphal growth with two DOI-backed snippets, a "
            "condition-qualified clinical-isolate example, and explicit "
            "growth-form and mechanism limits. Ignored-and-hidden novelty "
            "searches and structured METPO review found no exact record. "
            "Reserved METPO:1060600 in v529; existing records unchanged."
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
         "Attached elongated budding cells with constricted junctions; induction varies.",
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
