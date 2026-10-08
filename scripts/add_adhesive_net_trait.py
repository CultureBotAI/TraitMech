"""Add evidence-backed fungal adhesive-net trap formation."""

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
SLUG = "fungal_adhesive_net_trap_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v554/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000678"
METPO_ID = "METPO:1063100"
DEVELOPMENT = "DOI:10.1371/journal.ppat.1002179"
TAXONOMY = "DOI:10.3390/jof8070671"
TIMESTAMP = "2026-10-08T10:25:48Z"
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
    "label": "fungal adhesive-net trap formation",
    "definition": (
        "A morphological phenotype in which a fungus forms three-dimensional "
        "networks of interconnected hyphal loops that serve as adhesive "
        "nematode traps."
    ),
    "definition_source": DEVELOPMENT,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEVELOPMENT,
            "snippet": "A. oligospora forms adhesive networks to capture nematodes",
            "notes": (
                "Yang et al. (2011), Author Summary, not the scientific abstract; "
                "primary XML at https://www.ebi.ac.uk/europepmc/webservices/rest/"
                "PMC3164635/fullTextXML. Introduction, trap-formation Results, "
                "strain/proteomics Methods, actual Figure 1 and relevant Text S1 "
                "supplemental Methods were inspected. Figure 1I shows connected "
                "hyphal loops; the paper describes complex three-dimensional "
                "networks. ATCC 24927 is the reference strain. Supplemental "
                "Methods distinguish nematode-extract induction on vegetative "
                "hyphae from subsequent live-nematode interaction assays. "
                "Formation, adhesion, capture, penetration and digestion are "
                "separate observations. No universal induction medium, prey "
                "species or capture efficacy is inferred. Proteomic correlations "
                "are not treated as a causal gene requirement."
            ),
        },
        {
            "reference": TAXONOMY,
            "snippet": "Captures nematodes with adhesive networks.",
            "notes": (
                "Zhang et al. (2022; published 26 June), Results 3.2 Taxonomy, "
                "Arthrobotrys eryuanensis description; primary XML at "
                "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9317614/"
                "fullTextXML. Isolation/observation Methods, all six species "
                "descriptions and actual Figure 2 were inspected. Figure 2i "
                "shows the adhesive network, not time-resolved capture or "
                "adhesion kinetics. Holotype CGMCC3.19715 (Figure 2) and "
                "ex-type culture DLUCC 14-1 are distinguished by the authors. "
                "The material originated "
                "from freshwater sediment at Xihu Lake, Eryuan, Yunnan, China, "
                "collected 20 June 2014. Repeated spore transfers established "
                "pure cultures; corn meal agar observation at 26 degrees C "
                "with Panagrellus redivivus induced traps. These are study "
                "conditions, not universal requirements. The other newly "
                "described soil/sediment taxa provide context, not a universal "
                "genus-level phenotype assertion."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:756982",
            "taxon_label": "Orbilia oligospora ATCC 24927",
            "reference": DEVELOPMENT,
            "note": (
                "Source-named Arthrobotrys oligospora ATCC 24927. Yang et al. "
                "Methods identify the purchased ATCC strain as originally "
                "isolated from soil in Sweden. Live https://www.atcc.org/"
                "products/24927 independently confirms environmental soil "
                "origin and Sweden; it lists Arthrobotrys oligospora as the "
                "former name. Live NCBI https://eutils.ncbi.nlm.nih.gov/entrez/"
                "eutils/efetch.fcgi?db=taxonomy&id=756982 resolves rank strain "
                "with the exact label Orbilia oligospora ATCC 24927. This "
                "unperturbed natural-origin reference strain is qualified by "
                "the reported induction conditions, not every isolate or "
                "field biocontrol efficacy. The 2011 paper's O. auricolor "
                "teleomorph wording is not imported as a current taxonomic "
                "equivalence or synonym."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "adhesive-net-scope-and-parent",
            "prompt": "Resolve a closer fungal trap-morphology parent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Phenotype METPO:1000059 is a broad parent. Existing mycelial "
                "growth traitmech:000074 explicitly concerns bacteria; hyphal "
                "anastomosis traitmech:000605 concerns cytoplasmic fusion, not "
                "trap identity. A Hartig net is a plant-root interface, not a "
                "prey trap. Exclude generic mycelial networks, biofilms, "
                "standalone adhesive rings, knobs and columns, mechanically "
                "constricting rings, and individual-cell ring shape. Adhesive "
                "nets are multicellular loop networks; generic nematophagy or "
                "a fungal genus is not an exact synonym. Network formation "
                "does not alone demonstrate adhesion or successful capture "
                "under all conditions. No exact synonyms, xrefs, SSSOM "
                "equivalences or organism-level disjointness are asserted; "
                "closer hierarchy remains open."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "adhesive-net-mechanism",
            "prompt": "Separate network morphogenesis from adhesion and predation mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The 2011 genomic/proteomic study contains mechanistic leads, "
                "but expression changes alone do not establish necessary or "
                "sufficient gene effects. Protein-resolved causal graphs "
                "require perturbation/complementation evidence, relevant "
                "remaining figures/supplements and taxon-paired accessions. "
                "Formation, adhesion, capture, penetration and digestion "
                "must remain separate endpoints. No universal lectin, "
                "signaling or fusion-gene requirement is asserted; mechanism "
                "is deferred, not claimed absent. Sequence annotation or "
                "taxonomic membership alone does not establish this phenotype."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal adhesive-net trap formation with two primary DOI "
            "sources, source-checked snippets and a natural-origin strain "
            "example. Ignored-and-hidden main/worktree/open-PR checks support "
            "000678 and v554 block 1063100-1063199. Separated morphology from "
            "adhesion/capture and sequence-derived mechanism hypotheses; "
            "existing records unchanged. Corrected draft holotype/ex-type "
            "provenance before generation (#1825). Timestamp is observed UTC."
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
         "Adhesive loop-network formation, not generic hyphal growth or mechanical ring trapping.",
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
