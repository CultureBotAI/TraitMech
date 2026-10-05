"""Add unisexual reproduction without conflating mating type and clonality."""

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

IDENTIFIER = "traitmech:000613"
TARGET = ROOT / "data/traits/physiology/unisexual_reproduction.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v490"
FERETZAKI = "DOI:10.1371/journal.pgen.1003688"
LIN = "DOI:10.1038/nature03448"
ALBY = "DOI:10.1038/nature08252"
NI = "DOI:10.1371/journal.pbio.1001653"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "unisexual reproduction",
    "definition": (
        "A fungal phenotype enabling sexual or parasexual reproduction with "
        "genetic contribution from only one mating type."
    ),
    "definition_source": FERETZAKI,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": FERETZAKI,
            "snippet": (
                "Sexual reproduction involves cells of either opposite "
                "(bisexual) or one (unisexual) mating type."
            ),
            "notes": (
                "Feretzaki and Heitman (2013), PMID:23966871, PMC3744442. "
                "Exact sentence of the directly retrieved scientific abstract "
                "(abstract1), not the separate Author Summary. Introduction s1 "
                "also includes Candida unisexual reproduction and helper-cell "
                "stimulation. Results s2g/s2h and Methods s4a/s4f were read in "
                "XML: reduced sporulation in Spo11/Ubc5 mutants is distinct "
                "from hyphal growth, and Ubc5's precise role remains unresolved. "
                "Do not universalize one diploidization route or timing. "
                "Actual figures, complete tables, supplements and other "
                "experimental sections remain uninspected; no protein-level "
                "dependency is asserted here. Species names follow the paper."
            ),
        },
        {
            "reference": LIN,
            "snippet": (
                "Furthermore, fusion and meiosis can occur between non-isogenic "
                "alpha strains, enabling genetic exchange."
            ),
            "notes": (
                "Lin, Hull and Heitman (2005), PMID:15846346. Exact sentence "
                "from the scientific abstract directly retrieved through "
                "Europe PMC core metadata. The API uses the word alpha. "
                "Cryptococcus same-type partners need not be genetically "
                "identical: this supports outcrossing within a mating type, "
                "not obligatory clonal selfing. Diploidization and meiosis "
                "distinguish the reported fruiting from purely mitotic growth. "
                "Full text, methods, figures, supplements and natural strain "
                "provenance remain uninspected; no canonical example is inferred."
            ),
        },
        {
            "reference": ALBY,
            "snippet": (
                "could be induced to undergo chromosome loss to produce diploid "
                "cells, thereby completing a parasexual mating cycle"
            ),
            "notes": (
                "Alby et al. (2009), PMID:19675652, PMC2866515. Exact main-text "
                "clause retrieved via NCBI PMC efetch after Europe PMC full-text "
                "failure, not an abstract quote. All main-text paragraphs and "
                "Methods Summary were read; Figures 3/4 and Supplementary "
                "Figure 7 were visually inspected. Marked opaque Candida "
                "a-a partners form tetraploids. Supplement pp. 6-7/15 reports "
                "sorbose-induced ploidy reduction, including near-diploid and "
                "intermediate progeny, not uniform restoration of euploidy. "
                "Bar1-deletion assays and helper-stimulated wild-type mating "
                "are distinct: opposite-type pheromone helpers need not "
                "contribute genomes. Other figures and supplement sections "
                "remain uninspected. Engineered or marked strains are not "
                "promoted to natural canonical examples."
            ),
        },
        {
            "reference": NI,
            "snippet": (
                "generates abundant hyphae, homozygous diploid intermediates, "
                "and haploid meiotic spores when grown on mating-inducing "
                "media all by itself."
            ),
            "notes": (
                "Ni et al. (2013), PMID:24058295, PMC3769227. Exact Results "
                "s2a clause, not an abstract quote; its subject is XL280alpha. "
                "Scientific abstract, author summary, Results s2a and Methods "
                "s4b were read directly in XML. Solo culture on V8 or filament "
                "agar followed by spore isolation supports selfing in this "
                "laboratory F1 derivative of B3501alpha and JEC20a. Natural "
                "ancestral isolates do not make XL280 a natural exemplar. "
                "The paper does not resolve cell fusion versus endoreplication "
                "into one obligatory route. Actual figures, supplements "
                "including Table S4, and other experimental sections remain "
                "uninspected. Aneuploidy and adaptive benefit are not defining "
                "requirements of the whole trait."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "unisexual-reproduction-scope-and-hierarchy",
            "prompt": "Keep mating-type contribution distinct from selfing, helper cells and MAT inventory.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "One mating type does not mean one strain: non-isogenic "
                "same-type partners can exchange genetic material. Solo "
                "selfing overlaps homothallism (traitmech:000609), but the "
                "whole class is not restricted to single-isolate self-fertility. "
                "It is not a subclass of parasexuality (traitmech:000607), "
                "because meiotic cycles are also included. Pheromone-producing "
                "opposite-type helper cells are not necessarily genetic "
                "contributors, so do not require their physical absence. "
                "Use released phenotype METPO:1000059 in both record and "
                "proposal; PHYSIOLOGY is only a filesystem category. MAT "
                "sequence content, population mating-type bias or hyphae "
                "alone do not establish reproductive completion. Do not "
                "require universal meiosis, spores, cell fusion, clonality "
                "or absence of outcrossing. Resolve context-dependent same-sex "
                "mating terminology and external phenotype/process mappings "
                "before adding synonyms or xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "unisexual-reproduction-mechanism-and-examples",
            "prompt": "Resolve native examples and taxon-specific reproductive mechanisms before graphing.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Complete unread primary experiments and supplements before "
                "expanding mechanistic claims. Keep solo meiosis, non-isogenic "
                "same-type fusion and parasexual chromosome loss separate. "
                "Hyphal growth, cell fusion, ploidy change and viable progeny "
                "are different readouts, not interchangeable proof of a "
                "completed cycle. XL280 is a laboratory-cross derivative; "
                "Candida deletion and marked strains also do not establish "
                "natural canonical provenance. Verify natural strains and "
                "current taxonomic authority before adding examples, and "
                "native protein accessions before causal edges. No graph "
                "or unverified taxon/protein CURIE is asserted. Manual "
                "full-text matching is not an abstract-resolver VERIFIED "
                "verdict."
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
            "Added unisexual reproduction with four DOI-backed exact source "
            "snippets after scientific-abstract, full-text and selected "
            "Candida figure/supplement checks. Distinguished mating-type "
            "contribution from selfing and pheromone helpers; included "
            "meiotic and parasexual cycles. Ignored-and-hidden novelty "
            "searches and structured METPO review found no exact record. "
            "Reserved METPO:1056700 in v490 under released phenotype. "
            "Deferred natural canonical examples, lexical mappings and "
            "protein-resolved causal graphs."
        ),
        llm_assisted=True, timestamp="2026-10-05T04:48:00Z",
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
        "METPO:1056700", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/unisexual_reproduction.yaml"
        f"|{FERETZAKI}|{LIN}|{ALBY}|{NI}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "One genetic-contributor mating type; meiotic and parasexual routes, not obligatory clonal selfing.",
        IDENTIFIER,
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
