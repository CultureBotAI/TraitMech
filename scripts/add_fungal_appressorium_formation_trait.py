"""Add fungal appressorium formation without imposing one pathogenic mechanism."""

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
SLUG = "fungal_appressorium_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v535/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000659"
METPO_ID = "METPO:1061200"
SURVEY = "DOI:10.3390/jof5030072"
GUY11 = "DOI:10.1371/journal.ppat.1002514"
CELL_CYCLE = "DOI:10.1186/1741-7007-6-9"
EXPRESSORIUM = "DOI:10.1111/nph.13931"
TIMESTAMP = "2026-10-07T05:29:43Z"
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
    "label": "fungal appressorium formation",
    "definition": (
        "A morphological phenotype in which a fungus forms specialized "
        "surface-associated penetration structures called appressoria."
    ),
    "definition_source": SURVEY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": SURVEY,
            "snippet": (
                "Here, we report on the ability of many saprotrophs from a large "
                "range of taxa to produce appressoria on cellophane."
            ),
            "notes": (
                "Demoor, Silar and Brun (2019), PMID:31382649, PMC6787622; "
                "scientific abstract retrieved as full-text XML. Introduction, "
                "Methods, Results and the broad-definition Discussion paragraph "
                "were read; actual Figures 2 and 6 and supplementary Table S1 "
                "were inspected. The authors explicitly include structures "
                "previously called appressorium-like under a broad penetration-"
                "structure usage, including unicellular and compound forms. "
                "The principal assay used mycelial implants on cellophane over "
                "M2 medium at 27 C, with observations after 3-15 days. It is "
                "not an in-host assay or a universal fungal prevalence estimate. "
                "Contact and growth reorientation without penetration were "
                "distinguished from appressoria. Negative results apply to the "
                "tested conditions, not to entire clades. Table S1 identifies "
                "strains but does not independently establish natural provenance "
                "for all of them; they are not added as canonical examples."
            ),
        },
        {
            "reference": GUY11,
            "snippet": (
                "an appressorium is already developing in Guy11 strain whereas "
                "no infection cell development occurs in an isogenic "
                "\u0394pmk1 mutant"
            ),
            "notes": (
                "Soanes et al. (2012), PMID:22346750, PMC3276559; Results "
                "describing Figure 1B, not the Author Summary. Actual Figure 1 "
                "and the fungal-strain/growth Methods were inspected. Wild-type "
                "Guy11 and the deletion mutant were compared at four hours; "
                "the Guy11 series also includes 6, 8, 14 and 16 hours. The "
                "inductive in-vitro assay used plastic coverslips and "
                "1,16-hexadecanediol. Natural-isolate provenance is checked "
                "separately in the canonical-example note. The observed "
                "formation phenotype is not inferred from RNA expression. "
                "Neither these transcript profiles nor one deletion establish "
                "a universal protein-resolved mechanism across fungi. Other "
                "figures and transcript-data supplements were not inspected."
            ),
        },
        {
            "reference": CELL_CYCLE,
            "snippet": (
                "blocking of the cell cycle did not prevent spore germination "
                "and appressoria formation."
            ),
            "notes": (
                "Nesher, Barhoom and Sharon (2008), PMID:18275611, PMC2276476; "
                "scientific abstract Results, read directly in full-text XML. "
                "The Methods name Colletotrichum gloeosporioides f. sp. "
                "aeschynomene 3.1.3 wild-type and transgenic strains; germination "
                "and onion-epidermis assays were read. This result separates "
                "formation from a universal mitosis requirement. It does not "
                "show unrestricted post-penetration growth under cell-cycle "
                "inhibition. Full result figures, natural strain provenance "
                "and current species-complex assignment were not inspected "
                "or resolved, so this is qualified evidence, not a canonical "
                "taxon assignment or a universal autophagy/cell-cycle claim."
            ),
        },
        {
            "reference": EXPRESSORIUM,
            "snippet": (
                "Here we identify an appressorium\u2010like structure, which we "
                "call an expressorium"
            ),
            "notes": (
                "Becker et al. (2016), PMID:26991322, PMC5069595; the article's "
                "scientific Summary and the Results paragraph distinguishing "
                "intrinsecus/extrinsecus terminology were read directly in "
                "full-text XML. The internal structure enables Epichloe "
                "festucae to exit a leaf. The authors propose expressorium "
                "to distinguish it from an external appressorium, while "
                "noting an intrinsecus-appressorium convention. This is "
                "terminology-boundary evidence, not an asserted exact synonym "
                "or additional canonical example. Figures, movies, supplements "
                "and strain provenance were not inspected; no Nox mechanism "
                "or turgor measurement is inferred from this quotation."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:318829",
            "taxon_label": "Pyricularia oryzae",
            "reference": GUY11,
            "note": (
                "Wild-type Guy11 in Soanes et al. (2012), Figure 1A-B and "
                "Methods, directly forms appressoria under the tested "
                "in-vitro induction conditions. NCBI Taxonomy resolves "
                "Pyricularia oryzae at species rank and lists the paper's "
                "Magnaporthe oryzae name as a synonym. Independent primary "
                "population-study Methods at "
                "https://doi.org/10.5423/PPJ.NT.04.2013.0042 "
                "(PMID:25288972, PMC4174813) explicitly identify Guy11 as a "
                "rice-pathogenic isolate from French Guiana and distinguish it from "
                "laboratory crossing derivatives. That passage was read "
                "directly; its cited original 1988 isolation study was not "
                "retrieved. This provenance citation is not counted as an "
                "independent appressorium observation. The example concerns "
                "Guy11, not its engineered deletion mutant, strain 70-15, "
                "every strain, or every environmental condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-appressorium-scope-and-mapping",
            "prompt": "Reconcile broad appressorium usage and neighboring structures.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059 rather than plant pathogen "
                "METPO:1004003, black pigmented METPO:1003022 or thigmotropism "
                "traitmech:000594. Formation is neither disease causation nor "
                "generic adhesion or contact-directed growth. Demoor et al. "
                "(2019) explicitly use a broad appressorium umbrella for "
                "saprotrophic penetration structures and compound infection "
                "cushions; preserve this source attribution rather than "
                "silently imposing a single-celled, melanized or germ-tube-only "
                "definition. Becker et al. (2016) distinguish expressoria "
                "from external appressoria despite the intrinsecus convention. "
                "Whether to include that exit structure or propose narrower "
                "subclasses remains unresolved; no exact synonym is asserted. "
                "QuickGO resolves GO:0075016 as a host-associated biological "
                "process, not an exact organismal phenotype covering the "
                "saprotrophic observations, so xrefs and SSSOM are omitted. "
                "Research-report appressorium mentions describe candidate "
                "material structures, not an existing exact formation-trait "
                "node that can simply be regrounded."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-appressorium-function-and-mechanism",
            "prompt": "Separate formation, functional penetration and regulatory mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Formation does not guarantee successful penetration, host "
                "entry, invasion or disease. Do not require one shape, cell "
                "number, pigmentation, turgor level, surface chemistry or "
                "nutritional regime. Cellophane penetration is not evidence "
                "of natural-host infection or of a functional haustorium. "
                "The Colletotrichum cell-cycle results and the Guy11 Pmk1 "
                "comparison do not support a universal mitosis, autophagy "
                "or kinase dependency. A causal graph awaits review of "
                "primary perturbation/complementation experiments, remaining "
                "figures and supplements, and taxon-paired protein accessions. "
                "Transcriptional association or possession of a candidate "
                "gene is not proof of this formation phenotype. Keep the "
                "unresolved 3.1.3 provenance/species assignment and all "
                "unverified survey strains out of canonical examples."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_initial_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal appressorium formation with four primary-source "
            "snippets, a provenance-qualified Guy11 example and explicit "
            "morphology, terminology and mechanism boundaries. Ignored-and-hidden "
            "searches found only research leads, not an exact live trait. "
            "Reserved METPO:1061200 in v535; existing records unchanged and "
            "protein-level causal mechanism deferred."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_record() -> dict:
    record = build_initial_record()
    evidence = record["evidence"][1]
    old = (
        "The inductive in-vitro assay used plastic coverslips and "
        "1,16-hexadecanediol."
    )
    assert evidence["notes"].count(old) == 1
    evidence["notes"] = evidence["notes"].replace(old, (
        "The Methods describe plastic coverslips and 1,16-hexadecanediol, "
        "whereas the Results describing Figure 1A name a hydrophobic glass "
        "slide. This within-article surface discrepancy is unresolved; "
        "neither description is silently substituted for the other or "
        "treated as a universal surface requirement."
    ))
    record_curation_event(
        record, curator="codex", action="EVIDENCE_CORRECTION",
        changes=(
            "Addressed #1774: attributed the Guy11 plastic-coverslip description "
            "to Methods and the conflicting hydrophobic-glass description to "
            "Results. Left the surface discrepancy unresolved; the verbatim "
            "snippet, formation phenotype and qualified canonical example "
            "remain unchanged."
        ),
        llm_assisted=True, timestamp="2026-10-07T05:45:55Z",
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
         "Fungal formation phenotype; no universal pathogenicity or melanization.",
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
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (
        build_initial_record(), record,
    ):
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
