"""Add selective microbial peroxisome turnover as an autophagy phenotype."""

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
TARGET = ROOT / "data/traits/physiology/pexophagy.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v514/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v516/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000640"
METPO_ID = "METPO:1059300"
PARENT_METPO_ID = "METPO:1059100"
ATG36 = "DOI:10.1038/emboj.2012.151"
ATG30 = "DOI:10.1016/j.devcel.2007.12.011"
ROUTES = "DOI:10.1242/jcs.108.1.25"
BOUNDARY = "DOI:10.1080/15548627.2019.1603546"
TIMESTAMP = "2026-10-06T11:04:55Z"
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
    "label": "pexophagy",
    "definition": (
        "An autophagy phenotype in which a microbial cell selectively degrades "
        "its peroxisomes by delivering them to lysosomal or vacuolar compartments."
    ),
    "definition_source": ATG36,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": ATG36,
            "snippet": (
                "Peroxisomes undergo rapid, selective autophagic degradation "
                "(pexophagy) when the metabolic pathways they contain are no "
                "longer required for cellular metabolism."
            ),
            "notes": (
                "PMID:22643220, PMC3395097. Scientific Abstract directly read "
                "in Europe PMC core metadata with matching DOI. Results sec3/sec4 "
                "and Methods sec16/sec20/sec23 were also directly read in "
                "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3395097/fullTextXML. "
                "In Saccharomyces cerevisiae, Pex11-GFP processing and peroxisomal "
                "reporters, with Atg1 and vacuolar-protease controls, support "
                "degradation rather than puncta alone. Atg36 perturbation "
                "distinguishes peroxisome turnover from mitophagy, Cvt and bulk "
                "autophagy in the tested conditions. Post-log turnover also "
                "occurs in glucose, glycerol and oleate media; starvation is "
                "not a universal requirement. Pex14 deletion retains pexophagy "
                "in this species. The abstract's mitochondrial Pex3 redirection "
                "is engineered, not native Atg36 mitophagy evidence. Figure 1/2 "
                "captions were read, but actual figures, supplements, complete "
                "Methods and natural strain provenance were not inspected."
            ),
        },
        {
            "reference": ATG30,
            "snippet": (
                "It is necessary for pexophagy, but not for other selective "
                "and nonselective autophagy-related processes."
            ),
            "notes": (
                "PMID:18331717, PMC3763908. Scientific Abstract directly read "
                "in Europe PMC core metadata with matching DOI. The quoted "
                "protein is PpAtg30 in historically named Pichia pastoris. "
                "The abstract explicitly uses pexophagy for selective peroxisome "
                "turnover through micropexophagy and macropexophagy, and reports "
                "cargo selection and delivery. This supports route-inclusive "
                "terminology and selectivity in the tested yeast, not a universal "
                "Atg30 requirement or a gene-presence trait. The opening "
                "nonselective description of autophagy is not imposed on the "
                "broader local parent, which includes selective turnover. "
                "Full-text retrieval failed; methods, actual figures and "
                "strain-specific modern taxonomy were not inspected."
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
                "core metadata with matching DOI. Methanol-to-ethanol adaptation "
                "elicits individual wrapping and vacuolar fusion; glucose "
                "adaptation elicits vacuolar engulfment of peroxisome clusters "
                "and also turnover of a cytosolic enzyme. Morphology, enzyme "
                "measurements and mutant controls support distinct routes; "
                "vacuolar-proteinase mutants accumulate undegraded peroxisomes. "
                "Enzyme loss or delivery alone is not completed organelle "
                "degradation. These conditions are not universal trait "
                "requirements. Full methods, actual figures and natural "
                "strain provenance were not inspected."
            ),
        },
        {
            "reference": BOUNDARY,
            "snippet": (
                "the cytosolic pools of PTS receptors and their cargoes are "
                "degraded via a pexophagy-independent, selective autophagy "
                "pathway under pexophagy conditions."
            ),
            "notes": (
                "PMID:31007124, PMC6984484. Scientific Abstract directly read "
                "in Europe PMC core metadata with matching DOI. This is "
                "boundary evidence, not a positive whole-peroxisome turnover "
                "experiment: cytosolic Pex5/Pex7 and cargo pools undergo "
                "Atg30-independent selective autophagy in Pichia pastoris. "
                "Peroxisomal-protein turnover outside the organelle must not "
                "be equated with pexophagy. The background's damaged-or-redundant "
                "wording does not make damage obligatory. Full text, actual "
                "figures and strain provenance were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "pexophagy-selectivity-and-route-scope",
            "prompt": "Review route-inclusive phenotype against narrower GO terminology.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Use autophagy traitmech:000638 as the direct broader phenotype. "
                "The 2008 PpAtg30 scientific abstract uses pexophagy for both "
                "micropexophagy and macropexophagy. In contrast, issuing "
                "GO:0000425 names pexophagy specifically for selective "
                "macroautophagy and lists macropexophagy as exact; GO:0000426 "
                "micropexophagy is its sibling under GO:0030242 autophagy of "
                "peroxisome, which lists pexophagy as related. These nonobsolete "
                "biological-process records were resolved at "
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000425,GO%3A0000426,GO%3A0030242. "
                "Retain the source-attributed route-inclusive interpretation "
                "for human review and omit exact phenotype xrefs and synonyms. "
                "Bulk incidental capture, peroxisome presence, import defects, "
                "puncta, protein abundance and delivery without degradation "
                "alone are insufficient. Cytosolic peroxisomal-protein "
                "autophagy is a separate endpoint. The microbial cell doing "
                "the degradation carries the trait, not an organism merely "
                "inducing an animal host response."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "pexophagy-exemplars-and-native-mechanisms",
            "prompt": "Resolve strain provenance and taxon-paired mechanisms before expansion.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The evidence uses reporter and perturbation strains; natural "
                "strain provenance is not independently established. Keep "
                "canonical examples unset rather than presenting deficient "
                "mutants as positive exemplars. Historical Pichia names also "
                "need strain-specific taxonomic review. Atg36 in budding yeast "
                "and PpAtg30 do not define a universal receptor inventory; "
                "putative BLAST orthologues are not functional protein examples. "
                "Require native taxon-paired protein accession checks and "
                "direct functional evidence before a causal graph. Neither "
                "an ATG locus nor a detector profile is the phenotype, and "
                "neither starvation nor damaged cargo is universally required."
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
            "Added pexophagy as selective peroxisome degradation under "
            "autophagy, with four DOI-backed snippets and explicit route, "
            "flux and cytosolic-protein boundaries. Ignored-and-hidden "
            "searches and pinned METPO review found no exact record. Reserved "
            "METPO:1059300 in v516, carrying v514's unchanged parent row as "
            "context. Deferred unverified examples, mappings and protein graphs."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/pexophagy.yaml",
                  ATG36, ATG30, ROUTES, BOUNDARY]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Selective peroxisome turnover; route scope remains under human review.",
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
