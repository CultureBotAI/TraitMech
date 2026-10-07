"""Add microbial particle engulfment without inferring nutritional assimilation."""

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
TARGET = ROOT / "data/traits/physiology/phagocytosis.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v503/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000627"
METPO_ID = "METPO:1058000"
CHOANOFLAGELLATE = "DOI:10.1371/journal.pone.0095577"
COCCOLITHOPHORE = "DOI:10.1111/nph.20388"
PROVENANCE = "https://www.roscoff-culture-collection.org/rcc-strain-details/1456"
TIMESTAMP = "2026-10-05T20:40:00Z"
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
    "label": "phagocytosis",
    "definition": (
        "A physiological phenotype in which a microbial cell engulfs extracellular "
        "particles by enclosing them within its membrane and internalizes them "
        "into membrane-bound compartments."
    ),
    "definition_source": CHOANOFLAGELLATE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": CHOANOFLAGELLATE,
            "snippet": (
                "remodeling of the collar membrane to engulf the prey, "
                "and transport of engulfed bacteria into the cell."
            ),
            "notes": (
                "Dayel and King (2014), PMID:24806026, PMC4012994, scientific "
                "Abstract directly checked in Europe PMC XML and the PLOS article. "
                "Results, Discussion and Methods were read; actual Figures 1 "
                "and 4 were inspected. Live-cell images and SEM/TEM support "
                "collar-associated engulfment and internalization in Salpingoeca "
                "rosetta. Mere contact or retention on the collar is not ingestion. "
                "Nutrient assimilation and the molecular identity of collar "
                "links are not established by these images. Actual supplements "
                "and movies were not inspected. The culture-provenance papers "
                "cited by the Methods were not followed, so this study is retained "
                "as trait evidence without a canonical strain assignment."
            ),
        },
        {
            "reference": COCCOLITHOPHORE,
            "snippet": (
                "We found cells ingested proxy (up to 2 \u03bcm diameter) "
                "and natural (bacteria and cyanobacteria) prey particles"
            ),
            "notes": (
                "Scientific Summary directly checked in Europe PMC full-text XML "
                "and PMC11982794; PMID:40035416. Results, Discussion and Methods "
                "were read, and actual Figures 5, 6, 9 and 10 were inspected. "
                "Scyphosphaera apsteinii RCC1456 cultures internalized particles "
                "and labeled bacteria into a prominent vacuole. Distinguish "
                "pHrodo Escherichia coli BioParticles from Acridine Orange-labeled "
                "marine bacteria and from inert beads. Acidic-organelle staining "
                "alone is not prey uptake; some imaging used EGTA decalcification. "
                "The paper uses phagotrophy for the nutritional interpretation; "
                "this record asserts particle engulfment, not a measured carbon "
                "assimilation rate. Figure 10 is a conceptual sequence-based "
                "model, not native protein validation: its S. apsteinii transcripts "
                "come from RCC1455, not the assayed RCC1456, and some candidates "
                "are from Gephyrocapsa huxleyi. Actual supplements and movies "
                "were not inspected. No negative comparator-species claim, "
                "bead-degrading enzyme assignment or inferred nutrient quota "
                "is imported."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:418940",
            "taxon_label": "Scyphosphaera apsteinii",
            "reference": COCCOLITHOPHORE,
            "note": (
                "Strain-qualified example: diploid RCC1456, also AC504, TW15 "
                "and NIES-3344. Mid- to late-exponential nonaxenic cultures "
                "ingested labeled marine bacteria and particles under the "
                "reported incubation conditions; Figures 5 and 6 were inspected. "
                "The species taxon ID and scientific name were independently "
                "verified at NCBI on 2026-10-05; this is not a strain-level taxon ID "
                "or a claim about every isolate. Natural isolation from the "
                "Spanish coast of the Balearic Sea by single-cell micropipetting "
                "on 2001-02-01 was checked directly in the collection record "
                + PROVENANCE + ". The transcript-source strain RCC1455 "
                "(AC505/TW16) is distinct and is not substituted for this exemplar."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "phagocytosis-trait-and-process-scope",
            "prompt": "Keep particle uptake distinct from nutrition and process-level mappings.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "This class denotes the microbial organism's particle-engulfment "
                "phenotype, not a host immune cell's response to the microbe. "
                "Existing capsule and pathogenic-to-host descriptions concern "
                "host immune evasion and are not same-scope unresolved trait nodes. "
                "Phagotrophy denotes a nutritional strategy; the coccolithophore "
                "paper uses that interpretation, but ingestion of inert particles "
                "does not by itself establish carbon assimilation. Trophic type "
                "METPO:1000631 and heterotrophic METPO:1000644 require nutritional "
                "source use, while predatory bacterium traitmech:000054 is "
                "bacteria-specific. Phenotype METPO:1000059 is the supported "
                "broader trait. Do not equate phagocytosis with all endocytosis, "
                "pinocytosis, bacterial predation or phagotrophy. Review external "
                "process terms separately before asserting any trait-level xref; "
                "no synonym or ontology equivalence is proposed here."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "phagocytosis-native-mechanism-evidence",
            "prompt": "Require native functional evidence before assigning molecular mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The observed cellular uptake phenotypes do not identify a "
                "universal microbial protein mechanism. Collar-link composition "
                "in S. rosetta remains unresolved. The coccolithophore study's "
                "KEGG and Swiss-Prot sequence annotations concern RCC1455 "
                "transcripts and G. huxleyi gene models, not direct validation "
                "of the RCC1456 uptake mechanism. Keep strain provenance, "
                "homology, localization, experimental dependence and nutrient "
                "assimilation as separate evidence requirements. Inspect "
                "supplements and obtain taxon-paired native protein evidence "
                "before adding a causal graph or protein accessions."
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
            "Added phagocytosis as an organism-level particle-engulfment phenotype "
            "with two DOI-backed snippets, inspected primary figures and a "
            "strain-qualified natural RCC1456 example. Ignored-and-hidden novelty "
            "searches and pinned METPO review found no exact record. Reserved "
            "METPO:1058000 in v503. Kept nutritional, mapping and sequence-based "
            "mechanism interpretations separate; no protein graph was inferred."
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
         "|".join(["TraitMech:data/traits/physiology/phagocytosis.yaml",
                   CHOANOFLAGELLATE, COCCOLITHOPHORE]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Organism-level particle uptake; no inferred assimilation or process equivalence.",
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
