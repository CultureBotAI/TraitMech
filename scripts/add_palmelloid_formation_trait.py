"""Add palmelloid formation with enclosure and strain-provenance boundaries."""

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
SLUG = "palmelloid_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v530/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000654"
METPO_ID = "METPO:1060700"
HIGH_LIGHT = "DOI:10.3390/ijms24098374"
PSYCHROPHILE = "DOI:10.3389/fpls.2022.911035"
BROAD_USAGE = "DOI:10.1038/s41598-019-39558-8"
TIMESTAMP = "2026-10-07T00:44:51Z"
REVISION_TIMESTAMP = "2026-10-07T00:57:34Z"
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
    "label": "palmelloid formation",
    "definition": (
        "A morphological phenotype in which algal daughter cells remain enclosed "
        "together within a common outer envelope after division instead of "
        "dispersing as separate cells."
    ),
    "definition_source": HIGH_LIGHT,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": HIGH_LIGHT,
            "snippet": (
                "the cells continue to divide within the mother cell, i.e., "
                "they are unable to separate and remain encased in a single membrane."
            ),
            "notes": (
                "Suwannachuen et al. (2023), PMID:37176080, PMC10179368, "
                "Discussion 3.3. The quote is the authors' interpretation of "
                "enclosed dividing cells, not an abstract quote or a specific "
                "molecular mechanism. Results 2.5 and actual Figure 10 show "
                "CC-4414 palmelloids after high-light exposure in TAP medium. "
                "Methods 4.2 defines the percentage as palmelloid area divided "
                "by total cell area, not an individual-cell count. Larger "
                "aggregates are distinguished from palmelloids. CC-4414 "
                "provenance remains qualified in the discussion below."
            ),
        },
        {
            "reference": PSYCHROPHILE,
            "snippet": (
                "a morphological state characterized by multiple, single "
                "cells encased in an outer limiting membrane"
            ),
            "notes": (
                "Szyszka-Mroz et al. (2022), PMID:36119589, PMC9470844, "
                "Introduction. The scientific abstract, growth Methods, "
                "morphology Results and actual Figure 1 were inspected. "
                "Palmelloids occur alongside single cells at permissive 8 C; "
                "stress is not a necessary condition. Internal cells may "
                "retain flagella. Shared enclosure does not establish a "
                "particular membrane chemistry or universal cytokinesis defect."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1653778",
            "taxon_label": "Chlamydomonas priscui",
            "reference": PSYCHROPHILE,
            "note": (
                "Lake Bonney Antarctic isolate grown at 8 C in Bold's basal "
                "medium supplemented with 0.7 M NaCl, at 150 micromol photons "
                "m^-2 s^-1. Figure 1A,B and morphology Results show a mixed "
                "population of single cells and palmelloids, not every cell "
                "or growth stage. The Introduction identifies its natural "
                "lake origin. The source uses Chlamydomonas priscuii; NCBI "
                "Taxonomy lists that spelling as a synonym of the current "
                "species label Chlamydomonas priscui."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "palmelloid-formation-scope-and-hierarchy",
            "prompt": "Review a multicellular morphology parent and exact mappings.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Cell shape METPO:1000666 "
                "describes an individual cell and colony morphology "
                "METPO:1007062 is macroscopic. Obsolete cell arrangement "
                "METPO:1000046 and aggregate METPO:1000011 are not active "
                "parents. Biofilm formation traitmech:000053 requires "
                "surface-attached matrix-enclosed communities, while this "
                "trait concerns retained daughter cells in a common envelope. "
                "Rosette cell arrangement traitmech:000652 requires inward "
                "cell-pole orientation, which is not required here. Do not "
                "equate palmelloids with any cell aggregate, capsule, resting "
                "spore or normal transient pre-release sporangium. No exact "
                "synonym or xref is asserted; co-occurrence does not imply "
                "organism-level disjointness."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "palmelloid-formation-mechanism-scope",
            "prompt": "Resolve organism-specific cell-release mechanisms before graphing.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "A causal graph is deferred pending perturbation and protein "
                "accession review. The 2023 proteome associations and proposed "
                "photoprotection do not establish that particular proteins "
                "cause palmelloid formation, nor that palmelloids are necessary "
                "for all high-light tolerance. Gene possession alone does not "
                "establish the phenotype. Four-to-sixteen cells, stress "
                "induction, loss of flagella, photoprotection and a particular "
                "cytokinesis or wall-remodelling defect are not universal "
                "requirements. Distinguish a persistent enclosed growth form "
                "from an ordinary division stage using organism-specific "
                "time courses; no universal persistence cutoff is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "palmelloid-formation-cc4414-provenance",
            "prompt": "Reconcile CC-4414 provenance before canonical-example promotion.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The 2023 paper and Chlamydomonas Resource Center describe "
                "CC-4414/DN2 as a field isolate: "
                "https://www.chlamycollection.org/product/cc-4414-wild-type-mt-dn2/ . "
                "However, Flowers et al. (2015), Results accompanying Figure 2, "
                "reports extensive identity-by-descent with laboratory strains "
                "and raises possible cross-contamination while retaining a "
                "distinct chromosome-16 segment: "
                "https://academic.oup.com/plcell/article/27/9/2353/6206349 . "
                "Both primary passages were directly read. This is a "
                "provenance uncertainty, not proof of engineering or "
                "contamination in the 2023 experimental stock. Preserve the "
                "observed high-light phenotype as qualified evidence, but "
                "omit CC-4414 from canonical examples pending reconciliation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_initial_record() -> dict:
    """Retain the exact pre-review state for guarded migration and history."""
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added palmelloid formation with two DOI-backed snippets, a "
            "condition-qualified Antarctic-isolate example, and explicit "
            "enclosure, mechanism and CC-4414 provenance boundaries. "
            "Ignored-and-hidden searches and structured METPO review found "
            "no exact record. Reserved METPO:1060700 in v530; existing "
            "records unchanged."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def revise_record(record: dict) -> dict:
    if record != build_initial_record():
        raise SystemExit("Initial target differs from reviewed preimage")
    revised = copy.deepcopy(record)
    revised["definition"] = (
        "A morphological phenotype in which algal cells form nonmotile "
        "multicellular groups by retention within a mother-cell wall or by "
        "adhesion through extracellular gelatinous material."
    )
    revised["definition_source"] = BROAD_USAGE
    revised["evidence"].append({
        "reference": BROAD_USAGE,
        "snippet": (
            "the production of a gelatinous material that is secreted "
            "extracellularly, resulting in adhesion among cells and/or colonies"
        ),
        "notes": (
            "Herron et al. (2019), PMID:30787483, PMC6382799, Discussion. "
            "Directly retrieved full text explicitly uses palmelloid for "
            "both mother-wall retention and extracellular-material-mediated "
            "adhesion. This quote supports the second sense. The adjacent "
            "text describes palmelloids as nonmotile. This is terminology "
            "evidence, not a claim that the selected evolved isolates are "
            "natural canonical examples. The narrower enclosed-cell usage "
            "in the 2022/2023 sources is retained with its source attribution."
        ),
    })
    revised["discussions"][0]["rationale"] = (
        "Herron et al. (2019) explicitly includes mother-wall retention and "
        "extracellular-gelatinous-material adhesion in palmelloid usage, "
        "whereas the 2022/2023 sources emphasize enclosed cells. Preserve "
        "both documented senses in the unqualified class; review whether "
        "separate children are warranted. Retain phenotype METPO:1000059: "
        "cell shape METPO:1000666 describes an individual cell and colony "
        "morphology METPO:1007062 is macroscopic. Obsolete cell arrangement "
        "METPO:1000046 and aggregate METPO:1000011 are not active parents. "
        "Biofilm formation traitmech:000053 requires surface attachment; "
        "rosette cell arrangement traitmech:000652 requires inward cell-pole "
        "orientation. Neither is required here. Palmelloid is not an exact "
        "synonym for any microbial aggregate, capsule, resting spore or "
        "normal transient pre-release sporangium. No xref or organism-level "
        "disjointness is asserted."
    )
    revised["discussions"][1]["rationale"] = (
        "A causal graph is deferred pending organism-specific perturbation "
        "and protein accession review. The 2023 proteome associations and "
        "proposed photoprotection do not establish that particular proteins "
        "cause palmelloid formation or that palmelloids are necessary for "
        "all high-light tolerance. Gene possession alone does not establish "
        "the phenotype. Do not transfer a cell-release mechanism to the "
        "extracellular-adhesion form. Four-to-sixteen cells, stress induction, "
        "loss of flagella, photoprotection and a particular cytokinesis or "
        "wall-remodelling defect are not universal requirements. For the "
        "wall-retained form, distinguish sustained enclosure from an ordinary "
        "division stage using organism-specific time courses; no universal "
        "persistence cutoff is asserted."
    )
    record_curation_event(
        revised, curator="codex", action="CORRECTED_DEFINITION_SCOPE",
        changes=(
            "Addressed issue #1767: the unqualified palmelloid label was "
            "narrower than documented usage. Added DOI:10.1038/s41598-019-39558-8 "
            "and its verified snippet, broadened the definition to include "
            "extracellular-material adhesion, and retained source-specific "
            "scope and mechanism distinctions. Canonical example unchanged."
        ),
        llm_assisted=True, timestamp=REVISION_TIMESTAMP,
    )
    return revised


def build_record() -> dict:
    return revise_record(build_initial_record())


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
         ("Retained algal daughter cells in a common envelope; not generic aggregation."
          if record == build_initial_record() else
          "Nonmotile algal groups from mother-wall retention or extracellular-material adhesion."),
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
    if TARGET.exists():
        existing = yaml.safe_load(TARGET.read_text())
        if existing == build_initial_record():
            record = revise_record(existing)
        elif existing != record:
            raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() not in (
        proposal, proposal_tsv(build_initial_record()),
    ):
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
