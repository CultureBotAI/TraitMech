"""Add fungal homothallism without equating self-fertility with MAT content."""

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

IDENTIFIER = "traitmech:000609"
TARGET = ROOT / "data/traits/physiology/homothallism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v486"
REVIEW = "DOI:10.5598/imafungus.2015.06.01.13"
YUN = "DOI:10.1371/journal.pgen.1006981"
PASSER = "DOI:10.7554/elife.79114"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "homothallism",
    "definition": (
        "A fungal phenotype enabling a culture founded from a single spore to "
        "reproduce sexually in isolation from a mating partner."
    ),
    "definition_source": REVIEW,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": REVIEW,
            "snippet": (
                "the ability of a single spore to produce a sexually reproducing "
                "colony when propagated in complete isolation."
            ),
            "notes": (
                "2015 terminology review, PMID:26203424. Exact contiguous span "
                "of the historical operational definition in the Introduction "
                "at https://pmc.ncbi.nlm.nih.gov/articles/PMC4500084/. Abstract, "
                "Introduction and Conclusions were read as full-text XML; "
                "mechanism-specific sections and figures remain uninspected. "
                "This is definition authority, not experimental replication. "
                "Homothallism is an umbrella encompassing primary homothallism, "
                "pseudohomothallism, mating-type switching and unisexual "
                "reproduction, not one universal MAT architecture. The snippet "
                "is full text, not an abstract quote."
            ),
        },
        {
            "reference": YUN,
            "snippet": (
                "The filamentous fungus Chromocrea spinulosa (Trichoderma "
                "spinulosum) exhibits both self-fertile (homothallic) and "
                "self-sterile (heterothallic) sexual reproductive behavior."
            ),
            "notes": (
                "Yun et al. (2017), PMID:28892488. Exact sentence of the "
                "directly retrieved Europe PMC scientific abstract, separate "
                "from the author summary. Strain/culture Methods and Conclusions "
                "were read at PMC5608430; most main-text experiments, actual "
                "figures and supplements remain uninspected. Cs23 and Cs27 are "
                "the paper's self-fertile and self-sterile reference strains; "
                "their original natural provenance has not been verified. "
                "MAT manipulation supports direct-repeat-mediated MAT1-2 loss "
                "and recognition between unlike nuclei in a shared cytoplasm. "
                "Both intact MAT1-1-1 and MAT1-2-1 in one nucleus are not "
                "sufficient for self-fertility. The authors describe a "
                "heterothallic strategy at the nuclear level, not primary "
                "homothallism, while retaining organism-level self-fertility. "
                "Unstable Cs27 transformants were tested directly from "
                "transformation plates; do not generalize their stability."
            ),
        },
        {
            "reference": PASSER,
            "snippet": (
                "Our findings support C. depauperatus as an obligately sexual, "
                "homothallic fungus"
            ),
            "notes": (
                "Passer, Clancey et al. (2022), PMID:35713948. Exact independent "
                "clause of the scientific abstract in PMC9296135 full-text XML. "
                "Europe PMC's abstractText instead returns the eLife digest; "
                "a manual scientific-abstract match is not a VERIFIED resolver "
                "verdict. Publisher version 2 assets were retrieved through "
                "https://api.elifesciences.org/articles/79114. Introduction, "
                "strain/culture Methods, deletion-mutant Results and intra-/"
                "interstrain crossing and recombination Results were read. "
                "Actual Figures 5 and 8 and their captions were inspected; "
                "Supplementary file 1 strain rows were read from the publisher's "
                "elife-79114-supp1-v2.xlsx. Other figures, supplements and "
                "unread Methods remain uninspected. Figure 5 separates wild-type "
                "CBS7841 sporulation from pheromone/receptor and DMC1 deletion "
                "phenotypes. Hyphal growth alone does not establish meiosis. "
                "Figure 8 recombination assays use CBS7841-derived marker "
                "strains, including UV-induced and spontaneous mutants, not "
                "the unmodified canonical isolate. Drug resistance alone is "
                "not evidence of sex; genotyping distinguishes recombination "
                "from new mutations. Tested interstrain crosses did not yield "
                "PCR-confirmed recombinant progeny, so universal compatibility "
                "is not asserted. Obligately sexual describes this source's "
                "example, not a requirement for all homothallic fungi."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1295531",
            "taxon_label": "Cryptococcus depauperatus CBS 7841",
            "reference": PASSER,
            "note": (
                "Qualified natural-isolate example: wild-type CBS7841, "
                "distinguished from its laboratory derivatives in Supplementary "
                "file 1. Figure 5A shows basidia and spore chains after one week "
                "on V8 medium at room temperature in the dark; Figure 5B assays "
                "sporulation after ten days on Murashige-Skoog medium. The "
                "paper's composite sexual-cycle evidence includes separate "
                "mutant experiments, not all measurements on wild type. "
                "Natural provenance is independently documented by "
                "https://www.atcc.org/products/36983: B3810 [CBS 7841, TRTC "
                "48044], isolated from a dead spider in Ontario, Canada. This "
                "collection record supports provenance, not independent "
                "trait replication. NCBI taxonomy 1295531 resolves to this "
                "active strain name on 2026-10-04."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "homothallism-trait-scope",
            "prompt": "Preserve organism-level self-fertility across distinct mating mechanisms.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is a reproductive phenotype, not a sequence feature or "
                "MAT-gene inventory. The operational single-spore definition "
                "does not require a uninucleate spore, both MAT idiomorphs in "
                "one nucleus, or one molecular mechanism. It does not exclude "
                "outcrossing or require universal compatibility, obligate "
                "sexuality, or self-fertility of every progeny. Distinguish "
                "self-fertility from asexual cloning, ploidy, heterokaryosis, "
                "hyphal fusion and parasexual reproduction; these are not is-a "
                "parents. PHYSIOLOGY is a filesystem category, not an ontology "
                "parent. Self-fertility and self-compatibility also have uses "
                "outside fungi; resolve their lexical scope and external "
                "phenotype/process mappings before adding synonyms or xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "homothallism-mechanism-and-readouts",
            "prompt": "Resolve native proteins and sexual-cycle readouts before adding causal edges.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Complete unread experiments and supplements before expanding "
                "mechanistic claims. Separate wild-type sporulation, deletion "
                "phenotypes, marker segregation and inter-marker recombination. "
                "MAT homology or expression alone cannot establish a sexual "
                "cycle, and neither independent chromosome assortment nor "
                "drug resistance alone excludes parasexual processes. Resolve "
                "native protein accessions, experimental dependencies and "
                "taxonomic provenance before adding a mechanistic graph; do "
                "not use NONMECHANISTIC to bypass unresolved grounding. Retain "
                "the actual abstract-verifier outcome when an API returns an "
                "editorial digest, and identify manual full-text checks separately."
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
            "Added homothallism with a definition review and two primary "
            "DOI-backed studies, each with an exact source snippet. Separated "
            "self-fertility from mating-locus content and retained strain and "
            "assay qualifiers. Added natural CBS 7841 after primary figure, "
            "strain-table, ATCC provenance and NCBI identity checks. Ignored-"
            "and-hidden novelty searches and structured METPO review found "
            "no exact record. Reserved METPO:1056300 in v486 under released "
            "phenotype. Deferred lexical mappings and protein-resolved graphs."
        ),
        llm_assisted=True, timestamp="2026-10-05T01:23:00Z",
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
        "METPO:1056300", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/homothallism.yaml"
        f"|{REVIEW}|{YUN}|{PASSER}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Fungal self-fertility; not a universal MAT architecture.", IDENTIFIER,
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
