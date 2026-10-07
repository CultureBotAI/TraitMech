"""Add rosette cell arrangement without imposing one formation mechanism."""

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
SLUG = "rosette_cell_arrangement"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v528/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000652"
METPO_ID = "METPO:1060500"
CHOANOFLAGELLATE = "DOI:10.7554/eLife.41482"
BACTERIAL = "DOI:10.1128/jb.00064-19"
TIMESTAMP = "2026-10-06T23:05:49Z"
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
    "label": "rosette cell arrangement",
    "definition": (
        "A morphological phenotype in which cells form multicellular clusters "
        "organized around a shared central region, with corresponding cell "
        "poles directed inward."
    ),
    "definition_source": CHOANOFLAGELLATE,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": CHOANOFLAGELLATE,
            "snippet": (
                "all cells are oriented with their basal poles toward the "
                "rosette center and their apical flagella extending out from "
                "the rosette surface"
            ),
            "notes": (
                "Wetzel et al. (2018), PMID:30556809, PMC6322860, first Results "
                "subsection; full-text XML and Figure 1 directly inspected. "
                "Wild-type Salpingoeca rosetta rosettes have organized polarity, "
                "unlike disordered clumps in the four Class C mutants. Methods "
                "identify wild type as SrEpac and use Algoriphagus-derived "
                "rosette-inducing factors. The three-cell minimum after "
                "vortexing is this study's scoring rule, not a universal "
                "definition. Clonal development rather than aggregation is "
                "specific to S. rosetta here. The Results quote is not the "
                "scientific abstract or editorial digest."
            ),
        },
        {
            "reference": BACTERIAL,
            "snippet": (
                "form multicellular rosettes by adhering to each other through "
                "the polar polysaccharide, or holdfast."
            ),
            "notes": (
                "Fiebig (2019), PMID:31010900, PMC6707911, Results subsection "
                "Holdfasts are prominent in the pellicle. Publisher HTML, "
                "growth/sampling/microscopy Methods, and Figure 4 were directly "
                "inspected. Static CB15 cultures form rosettes with holdfast-rich "
                "cores. The Results describe both radial and oblong rosettes; "
                "not every core is a single attachment point. Supplemental "
                "Figure S2's text was accessible but its image was not verified. "
                "Pellicle dependence on holdfast is not a universal rosette "
                "mechanism. The Discussion leaves the field relevance of thick "
                "Caulobacter pellicles unresolved; laboratory observations are "
                "not evidence that these structures occur in every habitat."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:946362",
            "taxon_label": "Salpingoeca rosetta",
            "reference": CHOANOFLAGELLATE,
            "note": (
                "Wild-type SrEpac (ATCC PRA-390) in rosette-inducing-factor "
                "cultures, not every life stage. Natural-isolate provenance "
                "was checked in Levin and King's Experimental Procedures: "
                "https://doi.org/10.1016/j.cub.2013.08.061. SrEpac is isolate C, "
                "derived from Px1 by feeder replacement, antibiotic treatment "
                "and clonal isolation; Px1 derives from environmental rosette "
                "isolate ATCC 50818. It is not the EMS-mutagenized isolate B. "
                "The provenance citation is not counted as independent trait "
                "evidence. NCBI Taxonomy resolves the species ID and label."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "rosette-cell-arrangement-scope-and-hierarchy",
            "prompt": "Review a multicellular arrangement parent and exact external mappings.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Cell shape METPO:1000666 "
                "describes an individual cell, while colony morphology "
                "METPO:1007062 and colony shape METPO:1007063 describe "
                "macroscopic colonies on solid medium. Neither is the genus "
                "of this microscopic multicellular arrangement. Obsolete "
                "cell arrangement METPO:1000046 is not a usable active parent. "
                "Star shaped METPO:1000685 is one cell with radiating "
                "projections; staphylococcus arrangement traitmech:000118 "
                "is an irregular coccal cluster. Holdfast traitmech:000184 "
                "is a polar adhesin phenotype, not a rosette, and biofilm "
                "formation traitmech:000053 does not define this arrangement. "
                "Co-occurrence is not organism-level disjointness. No "
                "unqualified synonym, external equivalence, perfect spherical "
                "symmetry, fixed cell count or single central attachment "
                "point is asserted. Irregular clumping alone is insufficient."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "rosette-cell-arrangement-mechanism-scope",
            "prompt": "Keep organism-specific developmental and adhesion mechanisms separate.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The two primary studies support a shared morphological "
                "description, not one homologous developmental program. "
                "Wetzel et al.'s exclusion of aggregation concerns S. rosetta "
                "rosettes, whereas Fiebig describes polar adhesion in "
                "Caulobacter. Do not require clonal division or a bacterial "
                "holdfast for all rosettes. A causal graph is deferred pending "
                "separate organism-scoped perturbation and accession reviews, "
                "not because mechanisms are unknown. Holdfast-associated genes "
                "or predicted glycosyltransferases alone do not establish the "
                "observed arrangement. Quantitative shear, growth and "
                "cell-number thresholds are assay-specific. Additional "
                "bacterial canonical examples require strain-provenance and "
                "taxon verification; the CB15 evidence is retained without "
                "an unverified taxon row."
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
            "Added rosette cell arrangement with two DOI-backed Results "
            "snippets, a provenance-qualified S. rosetta example, and explicit "
            "arrangement/mechanism boundaries. Ignored-and-hidden novelty "
            "searches and structured METPO review found no exact record. "
            "Reserved METPO:1060500 in v528; existing records unchanged."
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
         "Multicellular polar arrangement; formation routes differ across organisms.",
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
