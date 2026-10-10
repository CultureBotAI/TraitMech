"""Add source-bounded coccolith production through the validated writer."""

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
SLUG = "coccolith_production"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v565/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000689"
METPO_ID = "METPO:1064200"
PARENT_METPO_ID = "METPO:1000059"
ULTRASTRUCTURE = "DOI:10.1038/ncomms11228"
TIME_LAPSE = "DOI:10.1111/nph.15272"
TIMESTAMP = "2026-10-10T06:31:15Z"
PARENT = {
    "identifier": PARENT_METPO_ID,
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
    "label": "coccolith production",
    "definition": (
        "A physiological phenotype in which a microbial cell produces the calcitic "
        "cell-covering elements known as coccoliths."
    ),
    "definition_source": ULTRASTRUCTURE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
    "evidence": [
        {
            "reference": ULTRASTRUCTURE,
            "snippet": (
                "Coccoliths are calcitic particles produced inside the cells of "
                "unicellular marine algae known as coccolithophores."
            ),
            "notes": (
                "Sviben et al. 2016, PMID:27075521, PMC4834641. Scientific Abstract "
                "and full article text directly read in Europe PMC XML on 2026-10-10; "
                "actual Figures 1 and 3 inspected. Calcium resupply to depleted "
                "AWI1516 cultures supports new calcite formation; imaging distinguishes "
                "forming coccoliths from a separate calcium-rich compartment. Its "
                "necessity, direct precursor identity and transfer route are not "
                "established. Figure 3's detector-panel caption repeats c in two "
                "pairs; no panel-specific detector assignment is imported. Other "
                "figures and supplements were not visually inspected. Historical "
                "Emiliania huxleyi is retained as the source name, not a current "
                "taxonomic or culture-collection phenotype assertion."
            ),
        },
        {
            "reference": TIME_LAPSE,
            "snippet": (
                "The continued production of malformed coccoliths could be observed "
                "on successive days"
            ),
            "notes": (
                "Walker et al. 2018, PMID:29916209, PMC6175242, Results, time-lapse "
                "observations associated with Figure 8. Full article text and actual "
                "Figures 5 and 8 directly inspected on 2026-10-10; supplements and "
                "movies unread. This passage concerns Ge-treated Coccolithus braarudii "
                "PLY182g, not normal morphology. Production persists despite defective "
                "coccosphere integrity. Growth responses differ from the assayed "
                "E. huxleyi CCMP1516; neither growth dependence nor photosynthetic "
                "benefit is generalized. Preserve source discrepancies: Methods "
                "time-lapse stage 17 C versus Figure 5's 16 C; Methods/Results "
                "HEDP 50 micromolar versus Figure 1's 5 micromolar; Results low-Si "
                "threshold below 0.2 micromolar versus Discussion below 0.1. No "
                "unqualified quantitative claim depends on choosing between them."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "coccolith-production-scope-and-parent",
            "prompt": "Resolve broader biomineralization placement without conflating endpoints.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059 pending a source-backed broader "
                "biomineralization phenotype. Coccolith production is not mere "
                "possession, secretion or arrangement of preformed elements into "
                "a coccosphere. Defective elements still count as production; a "
                "complete covering is not required. It is not equivalent to generic "
                "calcification, urease-associated calcium carbonate precipitation, "
                "siliceous scale production, or magnetosome/ferrosome possession. "
                "The physiological trait is distinct from a material coccolith, "
                "its vesicle and a process-level ontology term. No exact synonyms, "
                "xrefs, common molecular pathway or organism-level disjointness "
                "are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "coccolith-production-exemplars-and-mechanism",
            "prompt": "Reconcile assay strains, life stages and production-specific mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned pending joint strain-provenance "
                "and current-taxonomy verification. Skeffington et al., "
                "DOI:10.1111/jpy.12942, p. 239, explicitly derives calcifying "
                "AWI1516 from CCMP1516; this does not make all descendants equivalent. "
                "The current collection https://ncma.bigelow.org/CCMP1516, read "
                "2026-10-10, labels it Gephyrocapsa huxleyi and reports lost coccolith "
                "production. Keep historical assay observations separate from this "
                "current catalog state; loss alone does not establish engineering. "
                "PLY182g provenance remains unresolved here. No universal silicon "
                "requirement, ploidy restriction, growth dependence or protective "
                "function is inferred. Separate mineral deposition, transport, "
                "secretion and covering integrity before adding causal edges. "
                "A protein mechanism needs direct functional evidence and "
                "taxon-paired accessions; sequence features alone are insufficient. "
                "Mechanism is deferred, not claimed absent."
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
            "Added coccolith production with two primary DOI citations and short "
            "directly checked snippets, retaining assay and source-conflict limits. "
            "Ignored-and-hidden main/worktree/open-PR reservation checks support "
            "000689 and v565 block 1064200-1064299. Broader hierarchy, canonical "
            "exemplars and protein mechanism remain unresolved. Existing records "
            "unchanged. Timestamp records the observed UTC curation decision."
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
         "Production, not possession or complete coccosphere maintenance.", IDENTIFIER],
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
