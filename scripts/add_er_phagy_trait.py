"""Add selective microbial ER degradation as an autophagy phenotype."""

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
TARGET = ROOT / "data/traits/physiology/er_phagy.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v514/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v518/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000642"
METPO_ID = "METPO:1059500"
PARENT_METPO_ID = "METPO:1059100"
MICRO = "DOI:10.1242/jcs.154716"
MACRO = "DOI:10.1038/nature14506"
ROUTES = "DOI:10.15252/embj.2019102586"
TIMESTAMP = "2026-10-06T12:48:38Z"
PARENT = {
    "identifier": "traitmech:000638",
    "label": "autophagy",
    "definition": (
        "A physiological phenotype in which a microbial cell degrades cytoplasmic "
        "material, including its own constituents or intracellular non-self cargo, "
        "by delivering that material to lysosomal or vacuolar compartments."
    ),
    "definition_source": "DOI:10.1083/jcb.119.2.301",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
}
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
PARENT_ROW = [
    PARENT_METPO_ID, PARENT["label"], PARENT["definition"],
    "|".join([
        "TraitMech:data/traits/physiology/autophagy.yaml",
        "DOI:10.1083/jcb.119.2.301", "DOI:10.1242/jcs.108.1.25",
        "DOI:10.1073/pnas.0813319106", "DOI:10.1371/journal.ppat.1006344",
    ]),
    "METPO:1000059", "", "", "metpo_traitmech_2026_10", "",
    "Catabolic phenotype; formation markers alone do not establish degradative flux.",
    PARENT["identifier"],
]
RECORD = {
    "identifier": IDENTIFIER,
    "label": "ER-phagy",
    "definition": (
        "An autophagy phenotype in which a microbial cell selectively degrades "
        "portions of its endoplasmic reticulum by delivering them to lysosomal "
        "or vacuolar compartments."
    ),
    "definition_source": ROUTES,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MICRO,
            "snippet": (
                "Finally, we provide evidence that ER-phagy degrades excess ER "
                "membrane, suggesting that it contributes to cell homeostasis "
                "by controlling organelle size."
            ),
            "notes": (
                "PMID:25052096, PMC4163648. Scientific Abstract directly read "
                "in Europe PMC core metadata with matching DOI. XML Results "
                "s2c/s2e and Methods s4b/s4f were read. In Saccharomyces "
                "cerevisiae, ER-targeted Pho8 reporters distinguish selective "
                "turnover from cytosolic and mitochondrial cargo; Atg7 and "
                "vacuolar-protease controls distinguish routes and reporter "
                "activation. ER whorls enter the vacuole by microautophagy. "
                "DTT and tunicamycin interfere with vacuolar proteolysis, so "
                "stress-induced whorl accumulation alone is not completed "
                "degradation. Untreated opi1 mutants show partly disintegrated "
                "vacuolar whorls, unlike opi1 pep4 prb1 mutants; membrane "
                "expansion can elicit this response without misfolded-protein "
                "stress. The strains derive from W303, but independent natural "
                "provenance was not verified. Figure 5/7 captions were read; "
                "actual figures, supplements and complete Methods were not inspected."
            ),
        },
        {
            "reference": MACRO,
            "snippet": (
                "Atg40 is enriched in the cortical and cytoplasmic ER, and "
                "loads these ER subdomains into autophagosomes."
            ),
            "notes": (
                "PMID:26040717. Scientific Abstract directly read in Europe PMC "
                "core metadata with matching DOI. This Saccharomyces cerevisiae "
                "study explicitly restricts its use of autophagy to "
                "macroautophagy. Atg40 targets cortical/cytoplasmic ER, whereas "
                "Atg39 targets perinuclear ER and nuclear material. These "
                "source-specific subdomain assignments do not make ER-phagy "
                "and nucleophagy synonyms or restrict all ER-phagy to the "
                "macro route. The proposed mammalian FAM134B functional "
                "counterpart is qualified as probable, not experimentally "
                "universal. Full text, actual figures, supplements and strain "
                "provenance were not inspected."
            ),
        },
        {
            "reference": ROUTES,
            "snippet": (
                "Third, we demonstrate that macro- and micro-ER-phagy are "
                "parallel pathways with distinct molecular requirements."
            ),
            "notes": (
                "PMID:31802527, PMC6960443. Scientific Abstract directly read "
                "in Europe PMC core metadata with matching DOI. XML Results "
                "embj2019102586-sec-0005 and Methods sec-0011/sec-0018/sec-0019 "
                "were read. This yeast study explicitly includes macro- and "
                "microautophagic ER turnover. Their contributions depend on "
                "the trigger; do not universalize measured proportions. "
                "Nem1-Spo7 and ESCRTs contribute to micro-ER-phagy, but ESCRT "
                "mutants also impair nonselective autophagy and vacuolar "
                "function, so their defects are not micro-ER-phagy-specific "
                "absence tests. Atg40 is dispensable for the Atg7-independent "
                "micro route. Pho8 assays require background correction; the "
                "Sec63-GFP assay quantifies Pep4-dependent, Atg7-independent "
                "cleavage products using unsaturated exposures. Uptake or "
                "membrane scission alone does not prove complete degradation. "
                "Actual figures, supplements, complete Methods and independent "
                "strain provenance were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "er-phagy-route-scope-and-flux",
            "prompt": "Review route-inclusive scope and cargo-selective degradative flux.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Use autophagy traitmech:000638 as parent. The 2014 microautophagy "
                "study and the 2019 online/2020 issue ESCRT paper support a "
                "route-inclusive phenotype, whereas Mochida et al. 2015 use "
                "autophagy specifically for macroautophagy. GO:0061709 "
                "reticulophagy, resolved at "
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061709, "
                "is a nonobsolete biological process whose definition specifies "
                "autophagosomes and whose exact synonyms include ER-phagy. "
                "That route restriction and the process-to-phenotype shift "
                "prevent an exact xref here; retain the source-attributed "
                "difference for human review without silently narrowing the "
                "microbial phenotype. No synonyms or SSSOM mapping are asserted. "
                "ER stress, unfolded-protein responses, ER-associated protein "
                "degradation outside the lysosome/vacuole, bulk cytoplasmic "
                "turnover, gene presence, puncta or accumulated whorls alone "
                "are insufficient. Nuclear-envelope cargo can overlap "
                "nucleophagy without making the two traits equivalent."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "er-phagy-exemplars-and-route-mechanisms",
            "prompt": "Resolve natural exemplars and route-specific protein mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Canonical examples remain unset because natural strain "
                "provenance has not been independently verified for the "
                "laboratory reporter and perturbation strains. Do not infer "
                "natural or engineered origin from a mutant label. The yeast "
                "doing the degradation carries this phenotype; a bacterium "
                "eliciting an animal-host response does not. Resolve native "
                "taxon-paired protein accessions and direct functional evidence "
                "before adding a causal graph. Neither Atg39/Atg40 nor "
                "Nem1-Spo7/ESCRT dependence is an unconditional definition of "
                "ER-phagy across all routes and microbial taxa. Keep reduced "
                "rates, residual turnover and complete absence distinct, and "
                "do not equate impaired vacuolar function with selective loss "
                "of this phenotype."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def tsv(rows: list[list[str]]) -> str:
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added route-inclusive ER-phagy under autophagy with three DOI-backed "
            "scientific-abstract snippets and explicit selectivity, flux and "
            "source-access limits. Ignored-and-hidden searches and pinned METPO "
            "review found no exact record. Reserved METPO:1059500 in v518 with "
            "v514's unchanged parent context. Deferred unverified examples, "
            "mappings and protein graphs."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/er_phagy.yaml", MICRO, MACRO, ROUTES]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Selective ER degradation; macro/micro routes included, uptake alone insufficient.",
        IDENTIFIER,
    ]
    return tsv([*HEADERS, PARENT_ROW, child])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    if PARENT_PROPOSAL.read_text() != tsv([*HEADERS, PARENT_ROW]):
        raise SystemExit("Parent proposal differs from reviewed context")
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
