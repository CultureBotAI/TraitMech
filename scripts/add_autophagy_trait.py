"""Add microbial autophagy while separating degradative flux from marker accumulation."""

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
TARGET = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v514/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000638"
METPO_ID = "METPO:1059100"
YEAST = "DOI:10.1083/jcb.119.2.301"
ROUTES = "DOI:10.1242/jcs.108.1.25"
HOST_DEFENSE = "DOI:10.1073/pnas.0813319106"
FLUX = "DOI:10.1371/journal.ppat.1006344"
TIMESTAMP = "2026-10-06T09:02:37Z"
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
    "label": "autophagy",
    "definition": (
        "A physiological phenotype in which a microbial cell degrades cytoplasmic "
        "material, including its own constituents or intracellular non-self cargo, "
        "by delivering that material to lysosomal or vacuolar compartments."
    ),
    "definition_source": YEAST,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": YEAST,
            "snippet": (
                "This is the first report that nutrient-deficient conditions induce "
                "extensive autophagic degradation of cytosolic components in the "
                "vacuoles of yeast cells."
            ),
            "notes": (
                "PMID:1400575, PMC2289660. Scientific Abstract directly read in "
                "Europe PMC XML. Saccharomyces cerevisiae protease-deficient "
                "mutants and PMSF-treated reference cells accumulate bodies "
                "containing cytosol and organelles; bodies disappear after "
                "inhibitor removal. Sequestration and subsequent degradation, "
                "not inhibited-body accumulation alone, support the phenotype. "
                "The study's starvation conditions are not a universal trigger "
                "requirement. The XML body is sparse; full methods, actual "
                "figures and natural strain provenance were not inspected."
            ),
        },
        {
            "reference": ROUTES,
            "snippet": (
                "there exist in P. pastoris at least two pathways for the "
                "sequestration of peroxisomes into the vacuole for degradation."
            ),
            "notes": (
                "PMID:7738102. Scientific Abstract directly read in Europe PMC "
                "metadata and publisher HTML. In historically named Pichia "
                "pastoris, carbon-source adaptation elicits peroxisome turnover "
                "through macroautophagy-like wrapping or microautophagy-like "
                "vacuolar engulfment. Enzyme activities, morphology and mutants "
                "support route diversity; proteinase-deficient cells accumulate "
                "undegraded cargo. This supports selective organelle turnover "
                "without requiring starvation or a double-membrane intermediate "
                "for every route. Publisher full text requires access; methods, "
                "actual figures and strain-specific modern taxonomy were not "
                "inspected."
            ),
        },
        {
            "reference": HOST_DEFENSE,
            "snippet": (
                "In both organisms, genetic inactivation of the autophagy pathway "
                "increases bacterial intracellular replication, decreases animal "
                "lifespan, and results in apoptotic-independent death."
            ),
            "notes": (
                "PMID:19667176, PMC2731839. Scientific Abstract directly read "
                "in Europe PMC core metadata with matching DOI. The two models "
                "are Dictyostelium discoideum and Caenorhabditis elegans. Only "
                "the microbial amoeba's intracellular-infection phenotype is "
                "relevant here; the abstract's combined animal-lifespan wording "
                "and nematode insulin-signaling results are not transferred to "
                "the amoeba. Genetic perturbation supports an autophagy-associated "
                "host-defense role, not direct proof of completed cargo "
                "degradation by itself. Full text, actual figures and strain "
                "provenance were not accessible in this review."
            ),
        },
        {
            "reference": FLUX,
            "snippet": (
                "Antagonistically, ESX-1 is also essential to block the autophagic "
                "flux and deplete the MCV of proteolytic activity."
            ),
            "notes": (
                "PMID:28414774, PMC5407849. Scientific Abstract, distinct from "
                "the Author summary, directly read in Europe PMC XML and PLOS. "
                "The flux Results, flux-assay Methods and Discussion were read; "
                "Figure 6 and supplemental S6 Figure were visually inspected. "
                "Dictyostelium discoideum is the autophagic cell, not the "
                "infecting Mycobacterium marinum. Protease-inhibitor comparisons "
                "and GFP-Atg8 processing distinguish formation from degradation; "
                "the infection-associated block is partial, not a complete "
                "absence of flux. Free GFP reduction alone is ambiguous in "
                "this assay. The paper frames intracellular-pathogen digestion "
                "as xenophagy, but its blockade result is boundary evidence, "
                "not a positive completed-clearance observation. Other actual "
                "figures and supplements were not visually audited."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "autophagy-scope-and-flux",
            "prompt": "Retain catabolic scope without equating markers with completed flux.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The phenotype belongs to the microbial cell doing the "
                "degradation, not to a bacterium merely eliciting an animal "
                "host response. Selective and bulk turnover, macro- and "
                "microautophagic routes, and intracellular non-self cargo "
                "are within scope; no universal starvation trigger, "
                "double-membrane intermediate or ATG gene inventory is asserted. "
                "ATG genes, puncta, autophagic-body accumulation, cell death "
                "or reduced pathogen replication alone do not establish "
                "completed degradative flux. Nondegradative membrane repair "
                "or ejection using autophagy machinery is not sufficient. "
                "Extracellular uptake and ordinary phagolysosomal digestion "
                "alone do not distinguish autophagy. Existing endocytosis, "
                "phagocytosis, phagotrophy and extracellular proteolysis records "
                "are not equivalent or broader parents; their co-occurrence "
                "is not prohibited. GO:0006914 was resolved at "
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006914 "
                "and includes self and non-self material, but denotes a "
                "biological process rather than an equivalent organismal "
                "phenotype. Keep METPO:1000059 as parent and omit exact xrefs "
                "and synonyms pending human scope review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "autophagy-exemplar-and-mechanism",
            "prompt": "Resolve strain provenance and cargo-specific mechanism evidence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Canonical examples remain unset because reference-strain "
                "provenance and historical yeast taxonomy have not been "
                "independently verified. Do not infer natural or engineered "
                "origin from a mutant label. Retain the qualified experimental "
                "evidence without treating inhibited or knockout cells as "
                "positive completed-flux exemplars. Route-specific proteins, "
                "their accessions and taxon-paired functional evidence need "
                "review before adding a causal graph. The amoeba infection "
                "studies do not establish one universal microbial host-defense "
                "mechanism or prove that autophagy always eliminates an "
                "intracellular pathogen."
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
            "Added autophagy with four DOI-backed scientific-abstract snippets "
            "and explicit route, cargo, flux and source-access limits. "
            "Ignored-and-hidden searches and pinned METPO review found no exact "
            "record. Reserved METPO:1059100 in v514. Deferred unverified "
            "examples, mappings and protein mechanisms; existing traits unchanged."
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
         "|".join(["TraitMech:data/traits/physiology/autophagy.yaml",
                   YEAST, ROUTES, HOST_DEFENSE, FLUX]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Catabolic phenotype; formation markers alone do not establish degradative flux.",
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
