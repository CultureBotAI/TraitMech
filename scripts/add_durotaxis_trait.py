"""Add stiffness-directed microbial migration with bounded primary evidence."""

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

IDENTIFIER = "traitmech:000596"
TARGET = ROOT / "data/traits/physiology/durotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v473"
KANG = "DOI:10.7554/eLife.96821"
FILIPINAS = "DOI:10.1088/1361-6463/adb6b8"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "durotaxis",
    "definition": (
        "A motile phenotype in which migration is biased toward regions of "
        "greater substrate stiffness."
    ),
    "definition_source": KANG,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": KANG,
            "snippet": (
                "Dictyostelium also displayed stiff-side directed motility "
                "when seeded on the gradient gel"
            ),
            "notes": (
                "Kang et al., Version of Record (v4), 2024-12-13, "
                "https://doi.org/10.7554/eLife.96821.4; full text "
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC11643633/ "
                "(PMID:39671466). Exact Results paragraph span in Amoeboid "
                "durotaxis is evolutionarily conserved, not an abstract quote. "
                "Figure 4 was visually inspected: confined Dictyostelium "
                "cells on polyacrylamide stiffness gradients had greater "
                "directional migration than uniform-gel controls, without "
                "a significant velocity difference. Blebbistatin reduced "
                "directionality and speed; Rho activator II increased them. "
                "These pharmacological results do not isolate a dedicated "
                "stiffness sensor. Supplementary file 1 contains simulation "
                "parameters; the MDAR checklist refers to cell-culture "
                "methods but does not resolve the assayed Dictyostelium "
                "strain. Mammalian NMIIA localization and knockdown results "
                "are not direct microbial protein evidence."
            ),
        },
        {
            "reference": FILIPINAS,
            "snippet": (
                "Our findings reveal directional persistence and strong "
                "polarization of the plasmodia towards regions of stiffer "
                "substrates, indicating a guided migration response."
            ),
            "notes": (
                "Filipinas and Confesor, published online 2025-02-27. "
                "Exact abstract span in the publisher-deposited Crossref "
                "record, https://api.crossref.org/works/10.1088/1361-6463/adb6b8. "
                "The authors report tracking Physarum polycephalum "
                "plasmodial nodes on agar stiffness gradients. This is "
                "independent microbial support for stiffness-directed "
                "migration, not merely a simulation prediction. Full "
                "methods, figures and supplements were not inspected; "
                "strain provenance, gradient controls and the distinction "
                "between node migration and growth remain to be assessed "
                "before adding a canonical example or mechanistic graph. "
                "The abstract's simulation-supported gradient-independence "
                "claim is not generalized to all microbes."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "durotaxis-stiffness-and-migration-boundaries",
            "prompt": "Keep stiffness-directed migration distinct from other mechanical responses.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This definition follows the positive, stiff-side migration "
                "usage in both microbial studies; it does not claim all "
                "microbes prefer stiff substrates. Speed changes on uniform "
                "substrates, passive displacement and differential growth "
                "alone are insufficient. Contact-guided polarized growth "
                "in thigmotropism (traitmech:000594) is a different response. "
                "Do not infer durotaxis from a friction gradient, surface "
                "topography or remote substrate deformation without direct "
                "evidence for stiffness-directed migration. Mechanotaxis "
                "is broader, not an exact synonym. QuickGO returned zero "
                "durotaxis hits on 2026-10-04; other external equivalences "
                "remain unverified. No xref or synonym is inferred."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "durotaxis-strain-and-mechanism-grounding",
            "prompt": "Resolve experimental strains and microbial protein evidence before graphing.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Kang's methods cite Li et al. (DOI:10.3389/fcell.2022.835185), "
                "whose cell-culture methods describe Ax2-derived cells and "
                "expression constructs. That citation does not uniquely "
                "identify the cells used for Kang's Figure 4 or establish "
                "natural-strain provenance. Resolve that identity and inspect "
                "the Physarum full methods before adding NCBI-grounded "
                "canonical examples. Dictyostelium inhibitor/activator "
                "responses support a contractility-related interpretation, "
                "not a resolved protein-level sensing pathway. Do not "
                "transfer mammalian NMIIA polarization or knockdown effects "
                "to an unverified microbial accession, or treat the active "
                "gel model as a biological perturbation. Mechanistic graphs "
                "are deferred pending taxon-paired proteins and bounded "
                "causal evidence; NONMECHANISTIC is not a workaround."
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
            "Added durotaxis with two independent microbial DOI citations "
            "and exact full-text/abstract snippets. Ignored-and-hidden "
            "novelty searches and structured OWL review found no exact "
            "record or METPO term. Reserved METPO:1055000 in v473 under "
            "motile. Inspected Kang v4 Figure 4, methods and relevant "
            "supplement documents; kept stiffness-directed migration "
            "distinct from speed changes and contact-guided growth. "
            "Deferred canonical strains and protein-level mechanisms "
            "rather than inferring them from mammalian experiments."
        ),
        llm_assisted=True, timestamp="2026-10-04T12:00:52Z",
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
        "METPO:1055000", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/durotaxis.yaml|{KANG}|{FILIPINAS}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Stiffness-directed migration; not speed alone, contact-guided growth or passive displacement.",
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
