"""Add gravitaxis with context-qualified primary swimming evidence."""

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

IDENTIFIER = "traitmech:000584"
TARGET = ROOT / "data/traits/physiology/gravitaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v461"
NASIR = "DOI:10.1038/s41598-018-26046-8"
ROBERTS = "DOI:10.1242/jeb.050666"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "gravitaxis",
    "definition": (
        "A motile phenotype in which the direction of active swimming is biased "
        "relative to gravity."
    ),
    "definition_source": NASIR,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": NASIR,
            "snippet": "Predominantly, E. gracilis shows a negative gravitaxis behavior.",
            "notes": (
                "Introduction, page 1, visually verified at https://d-nb.info/1186379677/34 "
                "(PMID:29765103; PMC5954063). Direction varies with culture age. "
                "Results, Figure 4 and Supplementary Figure 6e-g distinguish upward-biased "
                "controls from EgPCDUF4201/CaM2 knockdowns. Full main text and supplement "
                "41598_2018_26046_MOESM1_ESM.pdf inspected via Europe PMC. "
                "Supplementary Figure 5e, not the main text's 5c, measures flagellar "
                "length; Supplementary Table 1 reports comparable, not identical, "
                "speeds. These controls do not exclude every flagellar defect. "
                "PKA phosphorylation and a direct dynein link remain hypotheses."
            ),
        },
        {
            "reference": ROBERTS,
            "snippet": (
                "the ability to swim preferentially upwards (negative gravitaxis) "
                "is primarily the result of upwardly curving trajectories"
            ),
            "notes": (
                "Summary (PMID:21112996); publisher main-text Methods, Results and "
                "Discussion inspected. Curved trajectories agree with a physical "
                "shape-orientation model, but shape and orientation rate were not "
                "measured simultaneously in the same individual. This is not proof "
                "that all protists lack gravity receptors. Gravikinesis concerns "
                "orientation-dependent swimming speed, not the directional phenotype. "
                "Equation images and supplementary material were not inspected; "
                "no equation-derived or supplement-only claim is asserted."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:3039",
            "taxon_label": "Euglena gracilis",
            "reference": NASIR,
            "note": (
                "Strain Z, axenic organic-medium cultures at 20 C under continuous "
                "light. Figure 4a and Supplementary Figure 6e show upward-biased "
                "wild-type controls; Methods specify buffer-only electroporation. "
                "These are not the RNAi knockdowns. NCBI identifier is species-level, "
                "not a strain accession; no universal age-independent direction is implied."
            ),
        },
        {
            "taxon_id": "NCBITaxon:5885",
            "taxon_label": "Paramecium caudatum",
            "reference": ROBERTS,
            "note": (
                "Wild-type cells from one-week-old boiled-hay-infusion cultures. "
                "After several hours in the observation chamber, rotation of the "
                "chamber revealed upward-curving swimming tracks (Results, Figure 2). "
                "NCBI identifier is species-level; the paper does not supply a "
                "resolved strain accession."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "gravitaxis-direction-and-process-boundaries",
            "prompt": "Keep gravity-relative swimming distinct from settling and neighboring traits.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Positive and negative gravitaxis are directional cases, not a "
                "requirement that all cells always swim upward. Passive settling "
                "alone and speed changes alone do not establish this trait. The "
                "definition does not require an active gravity receptor: powered "
                "swimming and physical orientation can coexist. Gyrotaxis "
                "(traitmech:000583) specifies a gravity-viscous torque mechanism, "
                "not an exact synonym or a disjoint phenotype. No new subsumption "
                "axiom between them is asserted without reviewing both scopes. "
                "QuickGO resolved active GO:0042332 gravitaxis on 2026-10-04, "
                "including geotaxis as an exact lexical synonym. It denotes a "
                "biological process rather than this organismal disposition; "
                "keep it out of equivalent xrefs and resolve any mapping separately."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "gravitaxis-mechanism-grounding",
            "prompt": "Resolve exact protein anchors and a faithful physical-mechanism graph.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The sources provide mechanism evidence, but this first record "
                "does not yet include a graph. Nasir's CaM2 accession EU935858 "
                "resolves to UniProtKB:B5THA2, an unreviewed entry without a "
                "Proteomes cross-reference in the 2026-10-04 REST response. An "
                "exact EgPCDUF4201 name query returned no hit; this does not "
                "establish sequence absence. Resolve eligible exact examples "
                "before adding the molecular branch; a DUF4201 match alone "
                "does not demonstrate gravitaxis. For the physical branch, "
                "the current MECHANISTIC coverage audit requires a protein "
                "node and example. Do not invent a receptor or misclassify "
                "physical causation as NONMECHANISTIC to satisfy that audit."
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
            "Added gravitaxis with two primary DOI sources, contiguous snippets "
            "and source-qualified examples at verified species taxa 3039 and "
            "5885. Ignored-and-hidden searches found only gyrotaxis boundary "
            "mentions, not an exact record or METPO term. Reserved METPO:1053800 "
            "in proposal v461; documented process-grain and mechanism-grounding "
            "gaps without substituting a protein or asserting a universal receptor."
        ),
        llm_assisted=True, timestamp="2026-10-04T02:18:15Z",
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
        "METPO:1053800", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/gravitaxis.yaml|{NASIR}|{ROBERTS}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Gravity-relative directional swimming, not passive sedimentation or speed alone.",
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
