"""Add fungal heterokaryosis without conflating nuclear identity and ploidy."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000608"
TARGET = ROOT / "data/traits/genomics/heterokaryosis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v485"
EXPRESSION = "DOI:10.1098/rspb.2022.0971"
SAMILS = "DOI:10.1098/rspb.2014.0084"
KESSLER = "DOI:10.1016/j.fgb.2018.01.005"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "heterokaryosis",
    "definition": (
        "A fungal phenotype characterized by the coexistence of genetically "
        "distinct nuclei within a shared cytoplasm."
    ),
    "definition_source": EXPRESSION,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": EXPRESSION,
            "snippet": (
                "Heterokaryosis is a system in which genetically distinct nuclei "
                "coexist within the same cytoplasm."
            ),
            "notes": (
                "2022 primary study, PMID:35946150. Exact span of the directly "
                "retrieved Europe PMC abstract. Introduction, Methods, Results "
                "and Discussion were read in the PMC9363985 full-text XML; "
                "actual figures and supplements were not inspected. Neurospora "
                "tetrasperma lineages L1, L6 and L10 were reconstituted from "
                "homokaryotic components, with DNA-ratio validation. "
                "Developmental stage and lineage affect expression; global "
                "transcription does not diagnose heterokaryosis by itself. "
                "L10 heterokaryons can remain largely sterile despite containing "
                "both mating types. Expression correlations do not establish "
                "a protein-resolved regulatory mechanism."
            ),
        },
        {
            "reference": SAMILS,
            "snippet": (
                "A heterokaryon is a tissue type composed of cells containing "
                "genetically different nuclei."
            ),
            "notes": (
                "Samils et al. (2014), PMID:24850920. Exact span of the directly "
                "retrieved Europe PMC abstract. Main-text Methods, Results "
                "and Discussion were read at PMC4046401; actual figures and "
                "supplements were not visually inspected. The study assays "
                "natural N. tetrasperma heterokaryons from lineages L1, L6 "
                "and L7 with multiple mating-type-linked SNPs. Bulk DNA ratios "
                "and RNA expression are different readouts; they do not count "
                "nuclei in every cell. The snippet names the tissue, whereas "
                "this record denotes the phenotype."
            ),
        },
        {
            "reference": KESSLER,
            "snippet": (
                "Shifts in fungicide sensitivity and microsatellite genotypes "
                "indicated that heterokaryons could adapt to changes in "
                "fungicide pressure."
            ),
            "notes": (
                "Kessler et al. (2018), PMID:29331685. Exact span of the directly "
                "retrieved Europe PMC abstract. Methods and relevant Results "
                "and Discussion were read in the author-hosted PDF at "
                "https://researchmap.jp/umassturfpathology/published_papers/"
                "2317022/attachment_file.pdf; actual Figures 5-6 were inspected, "
                "but other figures and supplements remain uninspected. "
                "Sclerotinia homoeocarpa field isolates were paired in vitro; "
                "fluorescent nuclear imaging used engineered derivatives. "
                "Tagged histones can move through shared cytoplasm into other "
                "nuclei, so dual fluorescence alone does not establish nuclear "
                "fusion or genotype. Microsatellite and SNP assays provide "
                "complementary evidence, with detection-limit qualifications. "
                "Fungicide responses are condition-specific, not defining "
                "properties of every heterokaryon; parasexuality was suspected, "
                "not demonstrated."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:40127",
            "taxon_label": "Neurospora tetrasperma",
            "reference": SAMILS,
            "note": (
                "Qualified example: natural heterokaryon P581 (lineage L6), "
                "Lihue, Hawaii. Primary provenance is Methods 2a and Table 1 "
                "at https://pmc.ncbi.nlm.nih.gov/articles/PMC4046401/. "
                "FGSC 2508 and 2509 are its homokaryotic components, not "
                "identifiers for the heterokaryon. The study measures "
                "cultured mycelial and sexual tissues at 25 C, not an "
                "in-situ nuclear census. This does not assert that all "
                "isolates or life stages are heterokaryotic. NCBI taxonomy "
                "40127 resolves to the active species name on 2026-10-04."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "heterokaryosis-trait-scope",
            "prompt": "Keep nuclear coexistence distinct from copy number and reproductive processes.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is a reusable genomic phenotype, not a locus or sequence "
                "feature. GENOMICS is a filesystem category, not an ontology "
                "parent. Genetically distinct nuclei sharing cytoplasm differ "
                "from genome-copy number, multinucleation alone, hyphal fusion, "
                "postfusion incompatibility and a complete parasexual cycle. "
                "Those traits are not is-a parents. Do not require exactly two "
                "nuclei, diploidy, a fixed nuclear ratio, universal self-fertility "
                "or fungicide resistance. Heterokaryon names a structure, not "
                "an automatically exact phenotype synonym. The fungal scope "
                "reflects the cited studies; broader terminology and external "
                "mappings require authority-level interpretation before adding "
                "synonyms or xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "heterokaryosis-mechanism-and-readouts",
            "prompt": "Resolve molecular mechanisms and nuclear identity with independent readouts.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Complete unread figures and supplements before extending "
                "quantitative or causal claims. Fluorescent protein localization, "
                "DNA genotype and RNA expression are different readouts; label "
                "exchange must not be interpreted as nuclear fusion. Negative "
                "allele detection does not by itself prove biological absence. "
                "Resolve native protein identities and experimentally supported "
                "edges before adding a mechanistic graph; do not use "
                "NONMECHANISTIC to bypass missing grounding. Keep the 2014 "
                "natural P581 example separate from reconstituted 2022 cultures "
                "and engineered 2018 imaging strains. Verify current taxonomic "
                "placement and strain provenance before adding further taxa."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added heterokaryosis with three primary DOI-backed references and "
            "exact abstract snippets. Separated nuclear coexistence from ploidy, "
            "fusion, incompatibility and parasexual reproduction. Added a "
            "qualified natural P581 Neurospora tetrasperma example after primary "
            "strain-provenance and NCBI taxonomy checks. Ignored-and-hidden "
            "repository searches and structured METPO review found no exact "
            "record. Reserved METPO:1056200 in v485 under released phenotype. "
            "Retained source-access and experimental-readout limits; external "
            "mappings and protein-resolved mechanisms remain unresolved."
        ),
        llm_assisted=True, timestamp="2026-10-05T00:29:53Z",
    )
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "proposed_id", "label", "definition", "definition_source", "parent",
        "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed",
    ])
    writer.writerow([
        "ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
        "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
        "A oboInOwl:inSubset", "", "", "",
    ])
    writer.writerow([
        "METPO:1056200", record["label"], record["definition"],
        "TraitMech:data/traits/genomics/heterokaryosis.yaml"
        f"|{EXPRESSION}|{SAMILS}|{KESSLER}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Genetically distinct nuclei sharing cytoplasm; not ploidy or fusion alone.", IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
