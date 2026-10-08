"""Add evidence-backed fungal constricting-ring formation."""

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
SLUG = "fungal_constricting_ring_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v553/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000677"
METPO_ID = "METPO:1063000"
DEVELOPMENT = "DOI:10.1038/s41467-023-43235-w"
TAXONOMY = "DOI:10.3897/BDJ.10.e96642"
CYTOKINESIS = "DOI:10.1016/j.devcel.2014.04.021"
TIMESTAMP = "2026-10-08T08:53:27Z"
CORRECTION_TIMESTAMP = "2026-10-08T09:13:13Z"
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
    "label": "fungal constricting-ring formation",
    "definition": (
        "A morphological phenotype in which a fungus forms three-celled hyphal "
        "ring traps whose mature ring cells inflate inward to mechanically "
        "capture nematodes."
    ),
    "definition_source": DEVELOPMENT,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "The R3 cell fuses with the S2 and R1 cells to complete CR formation"
            ),
            "notes": (
                "Chen et al. (2023), Results, Morphogenesis and development of CR; "
                "primary XML at https://www.ebi.ac.uk/europepmc/webservices/rest/"
                "PMC10651832/fullTextXML and actual Figure 1 inspected. CR means "
                "constricting ring; R1-R3 are ring cells and S1-S2 stalk cells. "
                "Wild-type Drechslerella dactyloides strain 29 (CGMCC3.20198) "
                "forms complete rings before becoming inflation-competent. "
                "Methods use water agar at 25 degrees C with Caenorhabditis "
                "elegans for induction, and nematodes or 55-degree-C water for "
                "inflation assays; a separate horse-serum protocol is also "
                "described. These are distinct assay conditions, not universal "
                "requirements. Figure 1 separates immature-ring escape from "
                "mature-ring capture. Neither formation alone nor a circular "
                "outline proves immediate capture competence."
            ),
        },
        {
            "reference": TAXONOMY,
            "snippet": "Both of them produce constricting rings to capture nematodes.",
            "notes": (
                "Zhang et al. (2022; published 16 December), scientific abstract, "
                "New information; primary XML at https://www.ebi.ac.uk/europepmc/"
                "webservices/rest/PMC9836436/fullTextXML. The two taxa are "
                "Drechslerella daliensis and D. xiaguanensis. Methods, taxon "
                "descriptions and actual Figure 1e were inspected. Soil isolates "
                "were purified by single-spore transfers; trapping structures "
                "were induced on corn meal agar observation plates at 26 "
                "degrees C using Panagrellus redivivus. Descriptions distinguish "
                "three-celled constricting rings from adhesive trapping devices. "
                "Figure 1e shows an uninflated ring, not time-resolved inflation. "
                "The taxon-name validity caveat is retained in the example."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2743661",
            "taxon_label": "Drechslerella daliensis (nom. inval.)",
            "reference": TAXONOMY,
            "note": (
                "Source-named D. daliensis, holotype culture CGMCC3.20131, "
                "isolated from burned forest soil at Cangshan Mountain, Dali, "
                "Yunnan, China, collected 25 July 2017. The primary taxon "
                "treatment and Figure 1e directly document three-celled "
                "constricting rings. Morphology and ITS, TEF1-alpha and RPB2 "
                "analyses support the study's identification. Live NCBI "
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                "db=taxonomy&id=2743661 resolves rank species but retains "
                "the nomenclatural qualifier nom. inval.; this is not a claim "
                "that the fungal name is validly published. The example is "
                "restricted to the observed culture and induction conditions, "
                "not every isolate or successful field biocontrol."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "constricting-ring-scope-and-parent",
            "prompt": "Resolve a closer trap-morphology parent without conflating cell shape.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Parent phenotype METPO:1000059 is broader than this multicellular "
                "differentiation phenotype. Ring shaped METPO:1000680 denotes "
                "individual cell geometry, not a three-cell trapping apparatus. "
                "Mycelial growth and hyphal anastomosis alone do not define this "
                "trap. Exclude adhesive non-constricting rings, adhesive nets "
                "and generic nematophagy; neither a taxonomic genus nor prey "
                "capture by any mechanism is an exact synonym. Formation includes "
                "morphologically complete immature rings, not only already "
                "inflated traps. Do not infer that every formed ring immediately "
                "inflates. No xrefs, synonyms, SSSOM mappings or organism-level "
                "disjointness are asserted; closer hierarchy remains open."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "constricting-ring-mechanism-and-taxonomy",
            "prompt": "Separate trap formation, inflation mechanism and nomenclatural validity.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Chen et al. investigate membrane reservoirs and SNARE-dependent "
                "inflation, but a protein-resolved causal graph requires review "
                "of the remaining perturbation/complementation figures, "
                "supplements and taxon-paired accessions. No universal SNARE "
                "requirement is inferred from morphology; mechanism is deferred, "
                "not claimed absent. Native provenance of laboratory strain 29 "
                "has not been established here, so it remains qualified evidence "
                "rather than a natural canonical example. NCBI's nom. inval. "
                "qualifier for D. daliensis concerns nomenclature, not absence "
                "of the observed trap; retain it pending nomenclatural review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_initial_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal constricting-ring formation with two primary DOI "
            "sources, source-checked snippets and a nomenclature-qualified "
            "natural-isolate example. Ignored-and-hidden main/worktree/open-PR "
            "checks support 000677 and v553 block 1063000-1063099. Separated "
            "formation from maturation, inflation and capture; existing "
            "records unchanged. Timestamp is observed UTC."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_record() -> dict:
    record = build_initial_record()
    record["label"] = "fungal constricting-ring trap formation"
    record["evidence"].append({
        "reference": CYTOKINESIS,
        "snippet": "Cytokinesis involves constriction of a contractile actomyosin ring.",
        "notes": (
            "Stachowiak et al. (2014), scientific abstract retrieved from Europe "
            "PMC for PMID:24914559, and primary article https://pmc.ncbi.nlm.nih.gov/"
            "articles/PMC4137230/. Results explicitly use constricting-ring "
            "terminology for intracellular actomyosin rings in fission-yeast "
            "protoplasts. This is terminology-boundary evidence, not another "
            "positive nematode-trap observation. The trap qualifier excludes "
            "this unrelated cellular structure; no cytokinesis mechanism, "
            "protein grounding or canonical example is transferred."
        ),
    })
    record["discussions"][0]["rationale"] += (
        " Stachowiak et al. (2014), DOI:10.1016/j.devcel.2014.04.021, also "
        "use constricting-ring terminology for fission-yeast cytokinesis. "
        "The trap-qualified label explicitly excludes those intracellular "
        "actomyosin rings; they are not synonyms or phenotype evidence here."
    )
    record_curation_event(
        record, curator="codex", action="EVIDENCE_AND_SCOPE_CORRECTION",
        changes=(
            "Addressed #1823: qualified the label with trap to distinguish "
            "intracellular cytokinetic rings in fungi. Added a directly "
            "checked primary boundary-source snippet and explicit exclusion; "
            "it is not a third positive trap study. Preserved the initial "
            "event, definition, identifier, natural example and reservation."
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
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Three-cell trap formation; not single-cell shape, adhesive rings or immediate inflation competence.",
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
    initial = build_initial_record()
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (initial, record):
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() not in (proposal_tsv(initial), proposal):
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
