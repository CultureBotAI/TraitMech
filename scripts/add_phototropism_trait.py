"""Add light-directed growth with strain-qualified fungal evidence."""

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

IDENTIFIER = "traitmech:000598"
TARGET = ROOT / "data/traits/physiology/phototropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v475"
IDNURM = "DOI:10.1073/pnas.0600633103"
SANZ = "DOI:10.1073/pnas.0900879106"
SHAKYA = "DOI:10.1128/EC.00203-13"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "phototropism",
    "definition": (
        "A phenotype in which growth is directionally oriented or reoriented "
        "toward or away from a light source in response to illumination."
    ),
    "definition_source": IDNURM,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": IDNURM,
            "snippet": (
                "it exhibits phototropism by bending toward near-UV and blue "
                "wavelengths and away from far-UV wavelengths"
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:16537433; "
                "PMC1450208); it refers to Phycomyces blakesleeanus "
                "sporangiophore growth. The institutional full-text PDF and "
                "Figure 1A were inspected: the wild-type control bends toward "
                "white light, unlike the reduced response of madA mutants. "
                "The abstract's far-UV response is not measured in that panel. "
                "Methods identify NRRL1555 as the wild-type background and "
                "distinguish chemically mutagenized derivatives and isogenic "
                "A56. Genetic cosegregation supports madA involvement, not "
                "a complete growth-polarity pathway."
            ),
        },
        {
            "reference": SANZ,
            "snippet": (
                "Phototropism, growth toward light, shares many features in "
                "fungi and plants but the molecular mechanisms remain to be "
                "fully elucidated."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:19380729; "
                "PMC2678449). This passage describes the positive case; the "
                "Idnurm source establishes the broader directional scope. "
                "The institutional full-text PDF and Figures 2B and 4 were "
                "inspected. Phototropic responses cosegregate with madB "
                "alleles; MADA-MADB interaction assays use yeast and E. coli, "
                "not the native fungus. The Discussion leaves rapid bending "
                "mechanisms unresolved. Transcription measurements are not "
                "themselves directional-growth readouts. The supplementary "
                "strain table and figures were not accessible and were not inspected."
            ),
        },
        {
            "reference": SHAKYA,
            "snippet": "These strains are wild isolates, except for A56.",
            "notes": (
                "Materials and Methods, Strains and growth conditions; exact "
                "contiguous raw PMC HTML text (PMID:24243797; PMC3910969). "
                "The preceding sentence includes NRRL1555 in the named "
                "strains; the following sentence distinguishes backcrossed "
                "A56. This supports natural-isolate provenance for the "
                "NRRL1555 exemplar, not an independent phototropism experiment."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:763407",
            "taxon_label": "Phycomyces blakesleeanus NRRL 1555(-)",
            "reference": IDNURM,
            "note": (
                "Wild-type sporangiophore growth toward white light in Figure "
                "1A, with NRRL1555 background identified in Methods; not the "
                "madA mutants or backcrossed A56. Independent natural-isolate "
                "provenance: DOI:10.1128/EC.00203-13, Materials and Methods "
                "(https://pmc.ncbi.nlm.nih.gov/articles/PMC3910969/). "
                "Strain-level identity and exact name resolved at NCBI "
                "Taxonomy on 2026-10-04. No invariant wavelength or response "
                "direction is asserted."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "phototropism-growth-and-direction-boundaries",
            "prompt": "Preserve growth, locomotion and response-direction distinctions.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The class includes growth toward or away from light without "
                "requiring both responses in one organism or condition. "
                "It is not phototaxis (active locomotion), photokinesis "
                "(locomotion-speed change), phototrophy (energy acquisition), "
                "or light-dependent growth rate or development alone. "
                "Use phenotype rather than motile as the parent. A blue-light "
                "receptor homolog alone does not establish this phenotype. "
                "Resolve phenotype-level external equivalences separately "
                "before adding synonyms or xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "phototropism-native-mechanism-grounding",
            "prompt": "Separate heterologous interaction assays from native growth control.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain genetic and heterologous evidence at its measured "
                "scope. Neither a yeast interaction assay nor copurification "
                "in E. coli proves the native light-dependent interaction "
                "or the full route from photoreception to asymmetric growth. "
                "Inspect the unavailable Sanz supplement and newer primary "
                "work, and resolve eligible taxon-paired protein accessions "
                "before adding a mechanistic graph. Do not transfer plant "
                "phototropin signaling to fungi or use NONMECHANISTIC to "
                "bypass protein-grounding requirements."
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
            "Added phototropism with two primary phenotype studies, a "
            "primary strain-provenance citation and exact snippets. "
            "Ignored-and-hidden novelty searches and structured OWL review "
            "found no exact record or METPO term. Reserved METPO:1055200 "
            "in v475. Retained both growth directions and distinguished "
            "locomotion and energy acquisition. Inspected primary figures; "
            "added NCBI-resolved natural NRRL1555 exemplar and deferred "
            "native protein-level mechanisms and unavailable supplements."
        ),
        llm_assisted=True, timestamp="2026-10-04T14:39:25Z",
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
        "METPO:1055200", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/phototropism.yaml|{IDNURM}|{SANZ}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Light-directed growth; polarity-neutral, not locomotion or phototrophy.",
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
