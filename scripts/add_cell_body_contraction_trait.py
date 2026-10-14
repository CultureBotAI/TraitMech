"""Add cell-body contraction through guarded, validated writes."""

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
SLUG = "cell_body_contraction"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v604/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000728"
METPO_ID = "METPO:1068100"
TIMESTAMP = "2026-10-14T17:32:15Z"
DEFINITION_SOURCE = "DOI:10.1126/sciadv.add6550"
KINEMATICS_SOURCE = "DOI:10.1073/pnas.2217737120"
VORTICELLA_SOURCE = "DOI:10.1242/jeb.189.1.163"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": "A quality that differentiates specific instances of a species from other instances of the same species.",
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "cell-body contraction",
    "definition": (
        "A physiological phenotype in which a microbial cell actively shortens "
        "its body by contraction of intracellular structures."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "Ca2+ concentrations from 10\u22126 to 10\u22122 M in the culture medium "
                "could stimulate cell contraction while maintaining the viability of the cell."
            ),
            "notes": (
                "Zhang et al. 2023, PMID:36812318, PMCID:PMC9946354, Results: "
                "functional analysis of giant backbone proteins, second paragraph. "
                "Direct JATS match; native NOT_IN_ABSTRACT retained. The study "
                "identified its East Lake, Wuhan isolate as Spirostomum minus using "
                "morphology, protargol staining and SSU rDNA, then established "
                "clonal cultures at 22 C. Actual Figure 1A shows extended and "
                "contracted cell bodies. The quoted treatment maintained viability; "
                "38-to-16 seconds describes intervals between contractions, not "
                "contraction duration. Selected Results, Methods and Discussion, "
                "actual Figures 1, 6 and 9, and relevant supplement pages were "
                "inspected. Figure 9 is a mechanistic schematic. Supplementary "
                "Figure 7 shows shortening during death, which is insufficient "
                "for this trait. Abnormal-cell counts are in Supplementary Table 2, "
                "not Table S1 as cited in the RNAi Results. Rare twisted RNAi "
                "phenotypes do not establish contraction loss in every treated cell."
            ),
        },
        {
            "reference": KINEMATICS_SOURCE,
            "snippet": (
                "In Fig. 2A, we show five contraction measurements in Spirostomum "
                "along with a model solution fitted to their average"
            ),
            "notes": (
                "Floyd et al. 2023, PMID:37307463, PMCID:PMC10288572, Results A, "
                "first paragraph, contiguous result clause. Direct JATS match; "
                "native NOT_IN_ABSTRACT retained. Actual Figures 1A and 2A-B "
                "show Spirostomum body shortening and experimental trajectories "
                "separately from fitted curves. Methods used commercially sourced "
                "cultures and high-speed imaging without compressing cells; no "
                "species identity is inferred. Supplementary Figure S3 measures "
                "length along the central backbone curve, with increasing width. "
                "Supplementary Figure S6 states that repeated contractions of "
                "the same organism were not distinguished from contractions of "
                "different organisms: five traces are not five established "
                "biological replicates. Vorticella panels measure stalk "
                "contraction, not the body endpoint. Calcium-wave and energy "
                "models are not universal molecular proof. Selected experimental "
                "sections, actual Figures 1-2 and supplementary pages 3 and 5 "
                "were inspected; raw videos and the complete model were not reanalyzed."
            ),
        },
        {
            "reference": VORTICELLA_SOURCE,
            "snippet": (
                "Living Vorticella showed a graded shrinkage of the cell body "
                "when Ca2+ buffer was injected into the cell body"
            ),
            "notes": (
                "Katoh and Naitoh 1994, PMID:9317557, scientific Abstract item 3, "
                "first clause. Direct namespace-qualified Europe PMC MED abstract "
                "match and native VERIFIED. The same sentence contrasts graded "
                "cell-body shrinkage with all-or-nothing stalk coiling. "
                "Triton-extracted preparations in other abstract items are not "
                "the living-cell injection assay. Calcium-release causality is "
                "presented as an assumption, not direct molecular proof. "
                "Publisher HTML and PDF requests returned 403; full Methods, "
                "figures and strain provenance were not accessed. No species-wide "
                "example, quantitative threshold or universal trigger is inferred."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "cell-body-contraction-scope-and-parent",
            "prompt": "Resolve a closer parent while distinguishing body shortening from other contractile endpoints.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Active motility METPO:1000701 "
                "and motile METPO:1000702 concern independent locomotion, not "
                "necessarily body shortening. Body contraction is not displacement "
                "caused only by stalk coiling, rapid axopodial contraction "
                "traitmech:000682, contractile-vacuole cycling, injection-system "
                "contraction, cytokinetic constriction, passive osmotic shrinkage, "
                "death or static short-cell size. Behavioral habituation "
                "traitmech:000714 changes response probability rather than "
                "defining the contraction response. The axopodial record's "
                "broader cellular-contractility parent question is not resolved "
                "by this body-specific class; do not reparent it here. No "
                "universal speed, fractional shortening, trigger or ecological "
                "function is imposed. No organism-level disjointness or exact "
                "synonym for generic contractility is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "cell-body-contraction-metpo-assessment",
            "prompt": "Review the proposed phenotype without treating locomotion as an exact equivalent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Pinned/current METPO releases, editor and inspected template "
                "owners provided no active exact contraction class. Historical "
                "obsolete Motility identifiers METPO:0000006 and METPO:000006 "
                "point to active METPO:1000701; obsolete Motile METPO:0000087 "
                "and METPO:000088 point to active METPO:1000702. These locomotion "
                "leads are related, not exact body-contraction identities. They "
                "are not revived or placed in xrefs. The ontology pin remains "
                "unchanged; v604 proposes this phenotype below METPO:1000059. "
                "No external equivalent or SSSOM mapping has been accepted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "cell-body-contraction-mechanism-and-provenance",
            "prompt": "Resolve study-isolate and protein identities before adding canonical examples or a mechanistic graph.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Keep study-named cultures as qualified evidence pending exact "
                "isolate/current-taxonomy correspondence. No canonical taxa, "
                "protein accessions or causal graph are asserted. Zhang's "
                "localization, RNAi and structural models support source-bounded "
                "mechanistic hypotheses, not a common protein mechanism inferred "
                "from sequence features. Category-E twisted cells were rare; "
                "other abnormal forms also occurred in controls. Figure 9's "
                "calcium-storage and energy-coupling scheme is not wholly "
                "demonstrated. A protein graph needs authority-checked taxon-paired "
                "accessions and edge-specific perturbation evidence; its omission "
                "does not claim that mechanisms are unknown. Do not generalize "
                "ATP independence or calcium concentrations to the whole class. "
                "Floyd's five traces have unresolved organism-level replication. "
                "Katoh's full Methods were not accessed. The verification sidecar "
                "retains actual sections, hashes, source-status checks and native "
                "verdicts; bounded notice checks are not comprehensive clearance."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added cell-body contraction with three primary DOI sources and "
            "directly matched 22-, 19- and 19-word excerpts. Full-text Results "
            "retain NOT_IN_ABSTRACT; the Vorticella abstract is VERIFIED. "
            "Body, stalk, axopodial, division and passive-shrinkage endpoints "
            "remain distinct. No sequence-derived mechanism or unverified "
            "canonical example imported. Reserved 000728, v604 and "
            "1068100-1068199 after ignored/hidden, retained-history, full-content "
            "proposal and open/draft PR checks. Contig lengths, embedding "
            "components and broad editor envelopes are not METPO reservations. "
            "Other records unchanged; timestamp records observed acceptance."
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
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml", DEFINITION_SOURCE]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Active shortening of the microbial cell body; no universal speed or protein mechanism.", IDENTIFIER],
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
