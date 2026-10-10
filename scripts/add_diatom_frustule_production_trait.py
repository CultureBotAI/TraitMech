"""Add source-bounded diatom frustule production through the validated writer."""

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
SLUG = "diatom_frustule_production"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/biomineralization.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v567/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000691"
METPO_ID = "METPO:1064400"
PARENT_ID = "traitmech:000690"
PARENT_METPO_ID = "METPO:1000059"
MORPHOGENESIS = "DOI:10.1007/s00709-017-1199-4"
TOMOGRAPHY = "DOI:10.1038/s41467-024-52211-x"
TIMESTAMP = "2026-10-10T20:14:43Z"
PARENT = {
    "identifier": PARENT_ID,
    "label": "biomineralization",
    "definition": (
        "A physiological phenotype in which a microbe mediates the formation of mineral phases."
    ),
    "definition_source": "DOI:10.1016/j.crte.2010.09.002",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "diatom frustule production",
    "definition": (
        "A biomineralization phenotype in which a diatom forms the siliceous valve "
        "and girdle-band elements of its cell wall (frustule)."
    ),
    "definition_source": MORPHOGENESIS,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": MORPHOGENESIS,
            "snippet": (
                "The basic stages of frustule morphogenesis characteristic of "
                "raphid pennate diatoms have been traced"
            ),
            "notes": (
                "Bedoshvili et al., journal issue May 2018, online 2017-12-21, "
                "PMID:29270874. Scientific Abstract directly read at "
                "https://pubmed.ncbi.nlm.nih.gov/29270874/ and in Europe PMC CORE "
                "on 2026-10-10 using EXT_ID:29270874 AND SRC:MED; exact ID, source, "
                "title and DOI checked together. The abstract defines frustule "
                "components as silica valves and girdle bands and reports microscopy "
                "of morphogenesis in Encyonema ventricosum under the source name. "
                "This supports formation, not just an isolated shell's presence. "
                "Cytoskeletal proximity is not functional necessity. Full text, "
                "Methods, actual figures and supplements were not inspected; "
                "no canonical taxon or universal membrane-release mechanism is inferred."
            ),
        },
        {
            "reference": TOMOGRAPHY,
            "snippet": (
                "A diatom cell wall consists of two types of building blocks: "
                "two plate-shaped valves and several ring-shaped girdle bands."
            ),
            "notes": (
                "Aram et al. 2024, PMID:39251596, PMC11385223, Introduction. "
                "Scientific Abstract, Introduction, Results, Discussion and Methods "
                "directly read in official Europe PMC full-text XML on 2026-10-10; "
                "actual Figure 2 inspected, other actual figures and supplements "
                "unread. Source-qualified CORE lookup EXT_ID:39251596 AND SRC:MED "
                "confirmed ID, source, title and DOI. Silicon-starved CCMP1335 "
                "cultures were resupplied and imaged during valve formation. "
                "Figure 2 orders different cells by inferred maturation, not a "
                "live-cell time series. The paper retains historical Thalassiosira "
                "pseudonana naming while noting Cyclotella nana; this is not a "
                "current taxonomy assignment. Structural correlations support "
                "a membrane-mold hypothesis, not proven contact-site function or "
                "a universal molecular mechanism. The quote defines wall elements; "
                "the Results provide the production observations."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "diatom-frustule-production-scope-and-mappings",
            "prompt": "Keep frustule-element formation distinct from possession and other silica traits.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use biomineralization traitmech:000690 as the broader phenotype "
                "because this endpoint entails formation of mineral cell-wall "
                "elements. It is not a material frustule, generic silicification, "
                "silica uptake, retention of an inherited valve or adsorption of "
                "preformed silica. Production of new wall elements does not require "
                "both valves to be synthesized anew in one cell cycle or every "
                "element to be formed simultaneously. Keep valve/girdle formation "
                "distinct from silica scales, auxospore coverings and setae; "
                "their observation alone does not establish this endpoint. "
                "The existing scale-production scope note distinguishes these "
                "phenotypes and is not an unresolved exact grounding. Do not "
                "infer organism-level disjointness or a universal geometry, "
                "cell-cycle schedule or fitness effect. Exact synonyms and "
                "external phenotype mappings remain unasserted pending authority "
                "review; process and material terms are not exact equivalents."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "diatom-frustule-production-exemplars-and-mechanisms",
            "prompt": "Resolve assay-strain provenance and production-specific causal evidence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned before reconciling study "
                "strains, collection provenance and current taxonomy. The two "
                "studies support wall-element formation but do not establish a "
                "conserved protein mechanism. The contact-site transport model "
                "and actin-associated expansion in Aram et al. remain proposals; "
                "unobserved vesicle fusion is not proof of its absence. Separate "
                "silica deposition, shaping, exocytosis and wall assembly when "
                "evaluating perturbation evidence. Functional evidence and "
                "taxon-paired accessions are required for protein edges; sequence "
                "features alone are insufficient. Mechanism is deferred, not "
                "claimed absent, and no universal intracellular route is imposed "
                "on all diatom silica structures."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added diatom frustule production beneath biomineralization with two "
            "primary DOI citations and directly checked short snippets. "
            "Ignored-and-hidden main/worktree/open-PR reservation checks support "
            "000691 and v567 block 1064400-1064499. Existing trait records "
            "unchanged; mappings, canonical taxa and mechanisms remain open. "
            "Timestamp records the observed UTC curation decision."
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
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "Local parent biomineralization; request subclass of v566 METPO:1064300 on adoption.",
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
