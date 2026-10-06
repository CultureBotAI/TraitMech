"""Add hormogonium formation with development- and motility-bounded evidence."""

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
SLUG = "hormogonium_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v527/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000651"
METPO_ID = "METPO:1060400"
DEVELOPMENT = "DOI:10.1099/00221287-111-1-1"
INDUCTION = "DOI:10.1128/aem.55.1.125-131.1989"
GENETICS = "DOI:10.1128/mSphere.00231-19"
TIMESTAMP = "2026-10-06T22:07:10Z"
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
    "label": "hormogonium formation",
    "definition": (
        "A morphological phenotype in which a filamentous cyanobacterium "
        "differentiates short, initially heterocyst-free filaments called "
        "hormogonia that are distinct from mature vegetative trichomes."
    ),
    "definition_source": GENETICS,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "In all three genera, the hormogonia are initially devoid of heterocysts."
            ),
            "notes": (
                "Rippka et al. (1979), Genera of Section IV, printed pages 34-36; "
                "publisher PDF extracted text directly read, not a search-result "
                "snippet. The three genera are Nostoc, Scytonema and Calothrix. "
                "The study distinguishes differentiated hormogonia from random "
                "trichome breakage and reports immotile hormogonia in PCC 6314, "
                "7524 and 6719. Smaller cells or gas vacuoles help identify these "
                "immotile forms; neither feature is required in every strain. "
                "Developing hormogonia can subsequently acquire terminal "
                "heterocysts, so initial absence is not permanent absence. "
                "This is a culture-based systematic study, not a universal "
                "modern taxonomic rule. PDF screenshots were unavailable; "
                "no visual panel verification or numerical table claim is made."
            ),
        },
        {
            "reference": INDUCTION,
            "snippet": (
                "motile (gliding) filaments lacking heterocysts and with "
                "distinctly smaller cells than those of vegetative filaments"
            ),
            "notes": (
                "PMID:16347816, PMC184065. Scientific Abstract directly read "
                "on PubMed and through the Europe PMC core API. Campbell and "
                "Meeks (1989) observed induced hormogonia in symbiotically "
                "competent Nostoc cultures. The quoted morphology describes "
                "those cultures, not every hormogonium. Strain 7801 underwent "
                "conversion in Anthoceros punctatus-conditioned medium under "
                "the tested conditions and later reverted to vegetative growth. "
                "The reported loss and recovery of acetylene reduction are "
                "stage-dependent readouts, not a definition requiring nitrogen "
                "fixation or plant symbiosis. Full text and panels were not read."
            ),
        },
        {
            "reference": GENETICS,
            "snippet": (
                "both sigC and sigJ may be required for an early stage in "
                "hormogonium development, while sigF is late acting."
            ),
            "notes": (
                "PMID:31043519, PMC6495340. Direct Europe PMC full-text XML: "
                "scientific ABSTRACT, first RESULTS subsection, and MATERIALS "
                "AND METHODS subsections Strains and culture conditions and "
                "Plasmid and strain construction were read. The snippet is "
                "from Results, not the separate precis/IMPORTANCE text. "
                "Wild-type Nostoc punctiforme formed shorter, morphologically "
                "distinct filaments after induction. In-frame sigF deletion "
                "abolished motility but retained morphological differentiation "
                "and heterocyst loss; sigC and sigJ deletions lacked those "
                "morphological markers. This separates development from "
                "locomotion experimentally. Complementation restored motility "
                "in the assay, not necessarily wild-type levels. These are "
                "strain- and assay-qualified results, not a universal sigma-factor "
                "rule inferred from sequence. Actual panels, movies and the "
                "strain-table supplement were not inspected; no panel-level "
                "or numerical claim is made."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "hormogonium-formation-scope-and-hierarchy",
            "prompt": "Review the developmental scope independently of motility and mature cell shape.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Motile METPO:1000702 is not "
                "a necessary parent: Rippka et al. explicitly include immotile "
                "hormogonia, and the 2019 sigF deletion retains differentiation "
                "without movement. The 1989 abstract's motile description is "
                "specific to the studied Nostoc cultures. Filament shaped "
                "METPO:1000674 denotes elongated cells or hypha-like structures, "
                "not specifically this differentiated multicellular stage. "
                "Filamentous colony METPO:1007066 denotes colony outline. "
                "Heterocyst traitmech:000073 and akinete traitmech:000185 "
                "describe other differentiated cell types, not this filament "
                "stage; their presence in a life cycle is not organism-level "
                "disjointness. Random fragmentation alone is insufficient. "
                "Do not universally require reduced cell size, gas vacuoles, "
                "permanent heterocyst absence, plant symbiosis or nitrogen "
                "fixation. Exact external equivalence and narrower hierarchy "
                "remain for human review; no xref or unqualified synonym is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "hormogonium-formation-stage-and-mechanism-grounding",
            "prompt": "Resolve strain and protein anchors before adding a causal graph or canonical example.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The cited studies support an observed developmental phenotype "
                "and genetic dependence, not merely sequence-feature possession. "
                "Before adding a mechanistic graph, inspect actual panels and "
                "supplements, resolve accession-level sigma-factor examples, "
                "and distinguish induction, morphological differentiation and "
                "motility readouts. Transcript changes or homologous sig genes "
                "alone do not establish the phenotype or the complete cascade. "
                "Canonical examples are deferred pending strain-table and "
                "taxon verification with natural provenance and explicit "
                "life-stage qualifiers; engineered deletion strains must not "
                "be presented as unqualified natural exemplars. The known "
                "mechanism is not claimed to be absent, and natural transient "
                "stages remain valid trait evidence without a canonical row."
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
            "Added hormogonium formation with three DOI-backed snippets and "
            "explicit developmental-stage, motility and sequence-inference "
            "limits. Ignored-and-hidden novelty searches and the pinned METPO "
            "audit found no exact record. Reserved METPO:1060400 in v527. "
            "Deferred unresolved strain/protein anchors; existing records unchanged."
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
         "Differentiated filament stage; neither motility nor sequence possession alone defines it.",
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
