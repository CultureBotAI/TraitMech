"""Add microbial extracellular vesicle production with route-bounded evidence."""

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
SLUG = "extracellular_membrane_vesicle_production"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v525/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000649"
METPO_ID = "METPO:1060200"
LYSIS = "DOI:10.1038/ncomms11220"
WALL = "DOI:10.1038/s41467-017-00492-w"
YEAST = "DOI:10.1371/journal.pone.0011113"
ARCHAEA = "DOI:10.1038/s41467-025-60272-9"
TIMESTAMP = "2026-10-06T19:52:36Z"
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
    "label": "extracellular membrane vesicle production",
    "definition": (
        "A physiological phenotype in which microbial cells give rise to closed, "
        "cell-derived lipid-membrane vesicles in the extracellular space."
    ),
    "definition_source": LYSIS,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:420247",
        "taxon_label": "Methanobrevibacter smithii ATCC 35061",
        "reference": ARCHAEA,
        "note": (
            "Type strain PS (= ATCC 35061 = DSM 861). Vesicles were purified "
            "from exponentially growing cultures at 37 C in modified DSM 119 "
            "medium under H2/CO2 and examined by TEM. The collection record "
            "https://www.dsmz.de/collection/catalogue/details/culture/DSM-861 "
            "traces PS to a primary sewage digester in Gainesville, not to a "
            "human donor; it supplies provenance, not independent vesicle "
            "evidence. NCBI Taxonomy resolves this strain to species 2173. "
            "This is a culture observation, not direct in-gut vesicle production."
        ),
    }],
    "evidence": [
        {
            "reference": LYSIS,
            "snippet": (
                "Super-resolution microscopy reveals that explosive cell lysis "
                "also produces shattered membrane fragments that rapidly form MVs."
            ),
            "notes": (
                "PMID:27075392, PMC4834629. Scientific Abstract, not the editorial "
                "teaser, directly read in Europe PMC XML; selected Results and "
                "strain/isolation Methods also read. Live super-resolution imaging "
                "in Pseudomonas aeruginosa distinguishes vesicles from fragments "
                "and supports membrane reassembly after lysis. Lys dependence in "
                "biofilms/stress does not extend to ordinary oxic planktonic "
                "cultures, where the lys mutant retains comparable MV levels. "
                "Reporter/deletion/rescue experiments are qualified observations, "
                "not proof of one universal route. Actual panels and supplements "
                "were not visually inspected."
            ),
        },
        {
            "reference": WALL,
            "snippet": (
                "Through these openings, cytoplasmic membrane material protrudes "
                "into the extracellular space and is released as MVs."
            ),
            "notes": (
                "PMID:28883390, PMC5589764. Scientific Abstract, separate from "
                "the appended teaser, and selected Results/Methods directly read "
                "in Europe PMC XML. The openings are endolysin-associated "
                "peptidoglycan holes in Bacillus subtilis. Live imaging and "
                "induced strains support extrusion from cells that ultimately "
                "die; tomography uses an engineered skinny ponA deletion, not "
                "wild-type cells. Static tomographic stages are not a measured "
                "time sequence. This route differs from explosive-fragment "
                "reassembly. This study and the 2016 paper share investigators; "
                "they are not independent-laboratory replications. Actual panels "
                "were not visually inspected."
            ),
        },
        {
            "reference": YEAST,
            "snippet": (
                "Bilayered vesicles with diameters at the 100\u2013300 nm range were "
                "found in extracellular fractions from yeast cultures."
            ),
            "notes": (
                "PMID:20559436, PMC2885426. Scientific Abstract and Methods "
                "s2a-s2c, Results s3a/s3d directly read in Europe PMC XML. "
                "Saccharomyces cerevisiae WT and trafficking mutants yield "
                "vesicles after supernatant fractionation and TEM. Heat-killed "
                "controls yielded no vesicle-like structures; viability controls "
                "were reported without displayed data. SEC/MVB perturbations "
                "alter composition and sterol-based release proxies without "
                "abolishing production. The abstract's concluding requirement "
                "language is not taken as a universal necessity claim. Size is "
                "assay-specific; WT denotes laboratory comparators, not verified "
                "natural isolates. Actual panels were not visually inspected."
            ),
        },
        {
            "reference": ARCHAEA,
            "snippet": (
                "The EVs were isolated from exponentially growing M. smithii "
                "cultures to limit the contamination of the EV preparations "
                "with cell debris."
            ),
            "notes": (
                "PMID:40461479, PMC12134362. Full-text Results Sec3 quote, not "
                "an abstract quote, checked in Europe PMC XML. Sec3/Sec7 and "
                "Methods Sec10-Sec12 describe PS cultures, density-gradient "
                "purification, TEM and particle assays. Instrument detection "
                "limits yield different size distributions. Cryo-ET suggests "
                "budding and wall passage; the large-vesicle lysis route is "
                "hypothesized, not directly demonstrated. DNA/protein cargo "
                "annotations do not demonstrate increased methane production. "
                "Actual panels and supplements were not visually inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "extracellular-vesicle-production-scope-and-mapping",
            "prompt": "Separate vesicle production from particle identity and cargo effects.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Include vesicles produced by non-lytic release or membrane "
                "reassembly after cell lysis; the producer need not survive. "
                "Require evidence for intact extracellular vesicles, not bulk "
                "membrane-dye signal, unclosed debris, intracellular organelles, "
                "whole daughter cells or virions. Vesicle-associated viral DNA "
                "alone does not make a particle a virion. Gas vesicles are "
                "proteinaceous intracellular inclusions. Exocytosis "
                "traitmech:000637 describes fusion-pore discharge, which need "
                "not release an intact vesicle. The yeast source attributes "
                "roles to both conventional and unconventional trafficking, so "
                "unconventional protein secretion traitmech:000648 is not a "
                "universal parent; possible overlap is not disjointness. Outer-"
                "membrane vesicles and exosomes are narrower or route-specific "
                "usages, not exact synonyms. No universal size, cargo, lipid-"
                "bilayer architecture or ecological function is imposed. "
                "Retain phenotype METPO:1000059 pending human hierarchy and "
                "external mapping review; no exact xref is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "extracellular-vesicle-production-route-mechanisms",
            "prompt": "Ground separate biogenesis mechanisms without universalizing them.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The bacterial sources support distinct endolysin-associated "
                "routes; the yeast work supports trafficking contributions; "
                "the methanogen's budding and large-vesicle lysis models remain "
                "qualified. No common protein apparatus follows from these "
                "observations. Before adding route-specific causal graphs, "
                "inspect the remaining panels, supplements and strain provenance "
                "and resolve the relevant protein accessions with taxon-paired "
                "functional evidence. The verified PS exemplar does not ground "
                "bacterial Lys or yeast SEC proteins. Do not infer vesicle "
                "production from a sequence feature, cargo annotation, membrane "
                "blebbing alone or an isolation protocol that mechanically "
                "manufactures particles from cells."
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
            "Added extracellular membrane vesicle production with four DOI-backed "
            "snippets and a provenance-qualified M. smithii PS example. Ignored-"
            "and-hidden duplicate searches and the pinned METPO audit found no "
            "exact record. Reserved METPO:1060200 in v525. Retained route, "
            "particle-identity and mapping limits; existing records are unchanged."
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
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Includes lytic and non-lytic routes; no universal cargo or protein apparatus.",
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
