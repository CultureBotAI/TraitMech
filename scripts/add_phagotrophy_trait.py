"""Add particulate nutrition without equating uptake with assimilation."""

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
TARGET = ROOT / "data/traits/physiology/phagotrophy.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v504/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000628"
METPO_ID = "METPO:1058100"
ISOTOPES = "DOI:10.1038/ismej.2017.68"
GROWTH = "DOI:10.1007/s00248-001-1024-6"
PROVENANCE = (
    "https://dornsife.usc.edu/caron/wp-content/uploads/sites/263/2023/11/"
    "2001_Sanders_etal_ME.pdf"
)
TIMESTAMP = "2026-10-05T21:49:00Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "phagotrophy",
    "definition": (
        "A physiological phenotype in which a microbial organism ingests "
        "particulate food and assimilates nutrients derived from that food."
    ),
    "definition_source": ISOTOPES,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": ISOTOPES,
            "snippet": (
                "NanoSIMS and bulk IRMS isotope analyses revealed that Ochromonas "
                "obtained 84-99% of its carbon and 88-95% of its nitrogen "
                "from consumed bacteria."
            ),
            "notes": (
                "PMID:28524870, PMC5563956. This contiguous scientific-abstract "
                "quote uses the directly retrieved Europe PMC abstract's ASCII "
                "range hyphens; the full-text XML uses en dashes. The maintained "
                "resolver verifies the API form but flags the en-dash form as "
                "LIKELY_PARAPHRASE solely for that typography difference. Full "
                "Introduction, Methods, Results and Discussion were read, and "
                "actual Figures 1 and 4 were inspected. Axenic Ochromonas sp. "
                "BG-1 cultures received washed heat-killed bacterial prey or "
                "labeled inorganic substrates in triplicate light/dark treatments "
                "with unlabeled controls. Isotope incorporation and prey-dependent "
                "growth support nutritional use, not merely particle uptake. "
                "The percentages describe the nutrient source under these "
                "conditions, not a universal rate or an exclusively direct "
                "organic-carbon assimilation route: bacterial carbon can be "
                "respired and refixed, and uncontrolled pH/atmospheric exchange "
                "may underestimate inorganic carbon fixation. NanoSIMS and bulk "
                "carbon estimates differ. Actual Figures 2, 3 and 5 and "
                "supplements were not visually audited; no unique claims from "
                "those panels are imported. Heat-killed prey do not demonstrate "
                "that the consumer kills living prey."
            ),
        },
        {
            "reference": GROWTH,
            "snippet": (
                "nutrient acquisition for this species in the presence of "
                "bacteria was accomplished primarily via ingestion of bacteria."
            ),
            "notes": (
                "Sanders et al. (2001), PMID:12024234. Scientific Abstract and "
                "full Introduction, Methods, Results, Discussion and Conclusions "
                "were directly read from the author-institution PDF. Actual "
                "PDF pages 2 and 7, including Figure 4, were inspected. The study "
                "compares axenic and bacterized BG-1 cultures with light, "
                "dissolved-organic and nutrient treatments. Live Pasteurella sp. "
                "prey in this experiment are distinct from the 2017 heat-killed "
                "prey treatment. Population abundance and biovolume are separate "
                "readouts; cell division alone need not mean biomass increase. "
                "Authors cannot exclude contributions from bacterial trace "
                "compounds or nutrient recycling. Fluorescent prey added above "
                "ambient prey abundance can inflate grazing estimates, while "
                "prey-disappearance estimates omit bacterial growth. No "
                "unqualified grazing rate, specific MES assimilation or "
                "BG-1 cannibalism claim is imported. This is a separate study "
                "of the same strain, not independent taxon replication."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1616673",
            "taxon_label": "Ochromonas sp. BG-1",
            "reference": ISOTOPES,
            "note": (
                "Strain-qualified BG-1 example: washed heat-killed bacterial "
                "prey supported growth and supplied cellular carbon and nitrogen "
                "in the 2017 isotope experiments; actual Figures 1 and 4 were "
                "inspected. This is not a claim that every Ochromonas isolate "
                "has the same trophic dependence. NCBI ESearch and EFetch "
                "independently resolve the exact name and identifier on "
                "2026-10-05; NCBI assigns species rank despite the BG-1 name. "
                "Natural isolation from a Malaysian freshwater pond after "
                "dark organic enrichment, followed by single-cell transfers "
                "and antibiotic axenization, is documented in the 2001 primary "
                "Methods (DOI:10.1007/s00248-001-1024-6), directly read at "
                + PROVENANCE + ". Antibiotic axenization is not evidence of "
                "genetic engineering. Nutrient-source fractions do not identify "
                "the complete intracellular assimilation pathway."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "phagotrophy-nutrition-and-hierarchy-scope",
            "prompt": "Keep particulate nutrition distinct from uptake and carbon-source axes.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "The class requires nutritional assimilation after ingestion; "
                "particle contact, retention or engulfment alone is insufficient. "
                "Phagocytosis traitmech:000627 describes membrane-mediated "
                "uptake and explicitly leaves nutrition separate. Its existing "
                "discussion is not an unresolved exact phagotrophy node. The "
                "2001 Introduction describes carbon, macronutrient and growth-"
                "factor benefits of phagotrophy as variable, partly speculative "
                "roles across mixotrophs; the 2017 Introduction attributes "
                "growth-factor cases to earlier papers not independently "
                "audited here. Those statements frame terminology, not new "
                "canonical examples. Trophic type METPO:1000631 is locally "
                "defined by carbon, energy and electron-donor sources, "
                "heterotrophic METPO:1000644 by organic carbon, and mixotrophic "
                "METPO:1000652 by dual carbon use. This broader nutrient-"
                "acquisition mode does not prescribe a carbon source or "
                "require photosynthesis, so retain phenotype METPO:1000059 "
                "pending review of a closer nutritional-mode hierarchy. "
                "Nutrient adaptation METPO:1000731 concerns nutrient regimes, "
                "not specifically particle feeding. Do not equate phagotrophy "
                "with phagocytosis, mixotrophy, bacterivory or the bacteria-only "
                "predatory-bacterium class. Extracellular digestion without "
                "particle ingestion is outside this definition. No unverified "
                "synonym or process-level ontology xref is asserted."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "phagotrophy-assimilation-mechanism-evidence",
            "prompt": "Resolve nutrient processing with native functional evidence.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Growth and isotope incorporation establish nutritional use "
                "without identifying a universal phagosomal digestion or "
                "assimilation mechanism. Distinguish prey origin, release of "
                "dissolved metabolites, direct organic assimilation and "
                "respiration followed by carbon refixation. Isotope mass "
                "balance does not by itself separate all these routes. "
                "Sequence annotation or differential expression alone would "
                "not establish native protein function. Obtain taxon-paired "
                "functional evidence and inspect relevant supplements before "
                "adding protein accessions or a causal graph."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added phagotrophy as an organism-level particulate-nutrition "
            "phenotype with two DOI-backed snippets, primary growth/isotope "
            "evidence and a natural BG-1 exemplar. Ignored-and-hidden novelty "
            "searches and pinned METPO review found no exact record. Reserved "
            "METPO:1058100 in v504. Kept uptake, nutrient sources, carbon-source "
            "classification and molecular mechanisms separate; no graph inferred."
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
         "|".join(["TraitMech:data/traits/physiology/phagotrophy.yaml", ISOTOPES, GROWTH]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Particulate nutrition; uptake alone is insufficient; no fixed carbon-source axis.",
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
    if any(parent.get(k) != v for k, v in PARENT.items()):
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
