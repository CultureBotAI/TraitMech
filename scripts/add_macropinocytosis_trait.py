"""Add the microbial bulk-fluid uptake phenotype with guarded provenance."""

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
TARGET = ROOT / "data/traits/physiology/macropinocytosis.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v510/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000634"
METPO_ID = "METPO:1058700"
DEFINITION = "DOI:10.1242/jcs.213736"
WILDTYPE = "DOI:10.7554/eLife.04940"
PROVENANCE = "https://link.springer.com/article/10.1186/gb-2008-9-4-r75"
TIMESTAMP = "2026-10-06T04:39:00Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "macropinocytosis",
    "definition": (
        "A physiological phenotype in which a microbial organism internalizes "
        "bulk extracellular fluid by closing actin-driven plasma-membrane "
        "ruffles into large intracellular vesicles."
    ),
    "definition_source": DEFINITION,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION,
            "snippet": (
                "Macropinocytosis is a conserved endocytic process used by "
                "Dictyostelium amoebae for feeding on liquid medium."
            ),
            "notes": (
                "PMID:29440238, PMC5897714. Scientific ABSTRACT quote. "
                "Introduction supports the ruffle-closure definition. Relevant "
                "uptake Results, Methods, Discussion and actual Figure 2 were "
                "read at https://pmc.ncbi.nlm.nih.gov/articles/PMC5897714/. "
                "Figure 2E reports P=0.057 for DdB formation-rate upregulation; "
                "do not call this significant. Diameter measurements use a "
                "transgenic reporter, unlike the dextran formation assay. "
                "Other figures and supplements were not visually audited."
            ),
        },
        {
            "reference": WILDTYPE,
            "snippet": (
                "These cells can also internalise bulk fluid without the "
                "guidance of a particle using a closely related process, "
                "macropinocytosis"
            ),
            "notes": (
                "PMID:25815683, PMC4374526. Contiguous Introduction quote, "
                "not the scientific Abstract or eLife digest. Relevant Results, "
                "confocal Methods, Discussion, Table 2 and actual Figure 3 "
                "were read at https://pmc.ncbi.nlm.nih.gov/articles/PMC4374526/. "
                "Figure 3C measures formation events; Figure 3B single sections "
                "cannot quantify cumulative uptake. Other figures and movies "
                "were not visually audited."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:44689",
            "taxon_label": "Dictyostelium discoideum",
            "reference": WILDTYPE,
            "note": (
                "Wild-type parental DdB cells freshly harvested from bacterial "
                "growth, observed by dextran imaging in Figure 3C; not Ax2, "
                "AX4, NF1 knockouts or reporter transformants. Table 2 links "
                "DdB to DdB(Wel). Strain genealogy at " + PROVENANCE + " identifies "
                "a laboratory-selected NC4 clone with copy-number differences, "
                "not an unchanged original wild isolate. NCBI EFetch verified "
                "the name and species rank on 2026-10-06; this ID does not "
                "identify the strain."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "macropinocytosis-scope-and-hierarchy",
            "prompt": "Keep bulk-fluid uptake distinct from neighboring uptake traits.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059 pending a closer endocytic "
                "capability hierarchy. This is uptake by a microbe, not "
                "microbial induction of uptake by a host cell. Phagocytosis "
                "traitmech:000627 is particle engulfment, phagotrophy "
                "traitmech:000628 requires nutritional assimilation, and "
                "trogocytosis traitmech:000633 removes portions of living "
                "cells. These are neither equivalents nor disjoint organismal "
                "capabilities. Generic pinocytosis is broader; its existing "
                "phagocytosis discussion mention is not an exact unresolved "
                "macropinocytosis node. Membrane ruffling without closure, "
                "solute transport alone and uptake into small endocytic "
                "vesicles are insufficient. No fixed diameter cutoff, "
                "enhanced uptake rate, axenic growth or nutrition is required. "
                "No unverified synonym or process-level ontology xref is asserted."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "macropinocytosis-native-mechanism",
            "prompt": "Separate native capability from mutant and reporter mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The papers share a research group and organism; they are "
                "not independent taxon replication. NF1 loss enhances uptake "
                "but is not required for the phenotype. Do not equate a "
                "drug response, localization or sequence similarity with a "
                "universal causal dependency. Protein accessions, native "
                "functional scope and remaining figures require review before "
                "adding protein examples or a causal graph."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added macropinocytosis with two DOI-backed source snippets and "
            "a parental DdB-qualified example. Ignored-and-hidden searches "
            "and pinned METPO review found no exact record. Reserved "
            "METPO:1058700 in v510. Distinguished native uptake from "
            "axenic mutants, reporter measurements and universal mechanisms."
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
         "|".join(["TraitMech:data/traits/physiology/macropinocytosis.yaml",
                   DEFINITION, WILDTYPE]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Bulk-fluid uptake, not an axenic-mutant or nutritional requirement.",
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
