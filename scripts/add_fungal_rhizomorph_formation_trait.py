"""Add fungal rhizomorph formation with source-bounded terminology and examples."""

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
SLUG = "fungal_rhizomorph_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v538/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000662"
METPO_ID = "METPO:1061500"
MECHANICS = "DOI:10.1016/j.fgb.2009.04.005"
DEVELOPMENT = "DOI:10.1016/j.mycres.2005.09.006"
PHYLOGENY = "DOI:10.1186/s12862-017-0877-3"
TERMINOLOGY = "DOI:10.3114/fuse.2024.14.03"
TIMESTAMP = "2026-10-07T09:59:27Z"
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
    "label": "fungal rhizomorph formation",
    "definition": (
        "A morphological phenotype in which a fungus forms root-like, "
        "multihyphal structures through coordinated hyphal growth."
    ),
    "definition_source": MECHANICS,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MECHANICS,
            "snippet": (
                "Rhizomorphs of wood-decay basidiomycetes are root-like structures "
                "produced by the coordinated growth of thousands of hyphae."
            ),
            "notes": (
                "Yafetto, Davis and Money (2009), PMID:19427390; scientific "
                "abstract retrieved directly through Europe PMC. The naming "
                "sentence supports the formation phenotype, not a universal "
                "hyphal-count threshold. Armillaria gallica cultures were "
                "tested in media of different gel strengths. The reported "
                "760 kPa is an osmolality-derived turgor estimate, whereas "
                "40-300 kPa describes pressure corresponding to measured tip "
                "forces. These are distinct readouts, not trait thresholds. "
                "Full text, figures, supplements and isolate provenance were "
                "not inspected; no canonical example is inferred from this abstract."
            ),
        },
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "Air pores develop near the inoculum plug shortly after "
                "inoculation, arising directly from the mycelium, and "
                "rhizomorphs are initiated from them."
            ),
            "notes": (
                "Pareek, Allaway and Ashford (2006), PMID:16376531; scientific "
                "abstract checked against the directly retrieved PDF and Europe "
                "PMC abstract. Methods, Results, Discussion, Table 1 and actual "
                "Figures 9-17 were inspected. Results place first tips on day 6, "
                "but Table 1 reports tips on day 5; no exact onset is asserted. "
                "Table 1 counts tips and air pores on five plates, not organisms. "
                "The main oxygen-conductance assay used cut rhizomorph ends; "
                "it does not establish intact-rind permeability or universal "
                "oxygen adaptation. Air pores and rhizomorphs are distinct "
                "structures. Remaining figure images and supplements were not inspected."
            ),
        },
        {
            "reference": PHYLOGENY,
            "snippet": (
                "All armillarioid species have the capacity to form rhizomorphs "
                "in culture, but only the later diverging lineages have been "
                "observed to form them in nature"
            ),
            "notes": (
                "Koch et al. (2017), PMID:28122504, PMC5264464; directly "
                "retrieved full-text XML, Discussion subsection The rise of "
                "rhizomorphs and Table 2. The quoted clause precedes a "
                "parenthetical figure/table citation. This is the authors' "
                "comparative summary, partly based on earlier literature, "
                "not a new formation experiment on every species. They "
                "explicitly describe unmelanized rhizomorphs in culture. "
                "Field non-observation is not biological absence; the summary "
                "does not establish expression in every strain or condition. "
                "Full Methods, actual figures, supplements and additional "
                "isolate provenance were not inspected."
            ),
        },
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "Many rhizomorph-forming fungi occur in the litter on the forest "
                "floor (ground species), while other species make aerial "
                "rhizomorph networks (epiphytic species)."
            ),
            "notes": (
                "Oliveira et al. (2024), PMID:39830290, PMC11739697; Introduction "
                "read directly in PMC HTML after the Europe PMC XML endpoint "
                "failed. This terminology passage supports not restricting "
                "formation to underground growth. These authors adopt a "
                "narrow melanized, differentiated, organized-tip concept and "
                "contrast Singer's white rhizomorph usage with mycelial cords. "
                "That is their attributed account; the original Singer/Rayner "
                "sources were not retrieved. Abstract, Introduction and selected "
                "taxonomic text/captions were read, but actual figures, "
                "supplements and the full Methods were not inspected. "
                "No additional canonical taxon or exact cord synonym is asserted."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:153913",
            "taxon_label": "Armillaria luteobubalina",
            "reference": DEVELOPMENT,
            "note": (
                "Isolate 930199KGS in Pareek et al. (2006), Fungal material "
                "and culture conditions, Results and Figures 9-17. Primary "
                "Methods at https://doi.org/10.1016/j.mycres.2005.09.006 "
                "identify the University of Western Sydney collection culture "
                "as originating from fruit bodies collected at Gore Hill Park, "
                "North Sydney, in June 1993. Rhizomorph development was "
                "observed on malt-marmite agar in darkness at 23 C. The "
                "Methods provenance and actual images were inspected; natural "
                "origin is not inferred from a wild-type label. NCBI Taxonomy "
                "confirms the species ID, label and rank. This is a qualified "
                "culture observation, not evidence for every strain or condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-rhizomorph-scope-and-hierarchy",
            "prompt": "Resolve rhizomorph/cord terminology and a closer fungal parent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059. Mycelial growth traitmech:000074 "
                "is explicitly bacterial; filament shaped METPO:1000674 is a "
                "cell-shape class; rhizoid colony METPO:1007068 and filamentous "
                "colony METPO:1007066 concern colony outlines. None is an "
                "exact fungal multihyphal formation record. Hyphal anastomosis "
                "traitmech:000605 denotes fusion and fungal sclerotium "
                "formation traitmech:000660 denotes compact resting bodies. "
                "Koch et al. (2017) use rhizomorph for unmelanized culture "
                "structures, whereas Oliveira et al. (2024) adopt the narrower "
                "melanized, organized-tip sense and distinguish mycelial cords. "
                "The broad formation definition does not settle that anatomical "
                "boundary: retain the source attribution and do not assert "
                "exact cord/strand synonyms, a universal pigment requirement "
                "or an underground-only habitat. A closer fungal growth-form "
                "parent and external equivalences require upstream review; "
                "no xrefs or SSSOM mappings are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-rhizomorph-formation-and-function",
            "prompt": "Separate formation from transport, invasion and gene mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Formation does not by itself prove pathogenicity, low-oxygen "
                "adaptation, a fixed invasion force or a universal hollow "
                "canal. Pareek et al. distinguish air pores from rhizomorphs; "
                "oxygen measurements on cut structures do not show intact-rind "
                "permeability. Their Results/Table 1 onset discrepancy remains "
                "unresolved. Culture versus field observations and hyphal/tip "
                "counts require explicit conditions and denominators. "
                "Physical growth and aeration have experimental support, "
                "but a formation-regulatory graph requires further primary "
                "perturbation evidence and authority-verified protein examples. "
                "No complete protein pathway is inferred from expression, "
                "gene possession, osmolyte composition or structure alone. "
                "The graph is deferred, not claimed to be biologically absent."
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
            "Added fungal rhizomorph formation with four directly checked "
            "source snippets, a provenance-qualified 930199KGS example and "
            "explicit terminology, hierarchy and experimental limits. "
            "Ignored-and-hidden searches found no exact existing trait. "
            "Reserved METPO:1061500 in v538; existing records unchanged "
            "and protein-level formation mechanism deferred."
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
         "Formation phenotype; rhizomorph/cord anatomy remains source-qualified.",
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
