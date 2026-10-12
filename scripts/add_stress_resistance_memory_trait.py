"""Add acquired stress-resistance memory through the validated writer."""

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
SLUG = "acquired_stress_resistance_memory"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v588/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000712"
METPO_ID = "METPO:1066500"
DEFINITION_SOURCE = "DOI:10.1534/genetics.112.143016"
BACTERIAL_SOURCE = "DOI:10.1371/journal.pbio.2003853"
TIMESTAMP = "2026-10-12T21:02:06Z"
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
    "label": "memory of acquired stress resistance",
    "definition": (
        "A physiological phenotype in which a microbial cell or lineage retains "
        "elevated resistance to a later stress challenge after a previous inducing "
        "stress has been removed, through persistence of a non-genetic state."
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
                "resistance persisted for four to five generations after cells "
                "were removed from the prior salt treatment"
            ),
            "notes": (
                "Guan et al. 2012, PMID:22851651, PMC3454879; scientific abstract, "
                "directly matched in publisher HTML and source-qualified MED. The "
                "resistance endpoint is H2O2 survival, not faster transcriptional "
                "reactivation. Relevant Methods, Results and actual Figure 1 and "
                "S1/S2 were inspected. BY4741-background cells received 0.7 M NaCl "
                "for 60 minutes, then grew in fresh stress-free YPD. Figure 1 "
                "describes three-to-four doublings over 360 minutes; four-to-five "
                "generations is the abstract statement. Methods specifies 11 "
                "peroxide doses plus control, whereas Figure 1A captions ten "
                "plotted doses. The normalized survival score is not a fraction "
                "of memory-bearing cells. S1 growth-arrest interventions and S2 "
                "engineered UCC8613 daughter marking are separate contexts. "
                "No natural canonical exemplar is asserted. The publisher's "
                "formula rendering differs from MED H(2)O(2); the selected span "
                "matches both without changing either source. Raw data were not "
                "independently reanalyzed."
            ),
        },
        {
            "reference": BACTERIAL_SOURCE,
            "snippet": (
                "the cells inheriting this ancestral PA displayed a significantly "
                "increased heat resistance compared to their isogenic, PA-free siblings."
            ),
            "notes": (
                "Govers et al. 2018, PMID:30153247, PMC6112618; scientific abstract, "
                "not Author Summary, matched in primary XML and source-qualified "
                "MED. Relevant Results and Methods, actual Figure 4 and S6 were "
                "inspected. Engineered MG1655 IbpA-msfGFP reporters received "
                "47 C for 15 minutes, recovered with growth, then faced 51 C for "
                "7 minutes. Figure 4D compares aggregate-bearing and aggregate-free "
                "descendants; Figure 4C detects no improved population-average "
                "survival after pretreatment. Survival requires growth and division "
                "within eight hours. S6 detects no age-bin survival difference "
                "in this assay, not universal age independence. Reporter-induced "
                "clustering was separately tested in actual Figure 1, previously "
                "inspected for traitmech:000711; a monomeric label alone is not "
                "proof against artifacts. Synthetic induction experiments and "
                "their duration are not transferred to these heat-induced lineages. "
                "Raw data and all other memory-related figure images were not "
                "independently assessed."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "stress-resistance-memory-scope-and-hierarchy",
            "prompt": "Preserve persistence after stress removal and the resistance endpoint.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Compare matched genetic backgrounds and challenge conditions "
                "after removal of the inducing stress. Persistent resistance is "
                "not merely faster transcriptional reactivation or faster "
                "reacquisition after a second induction. A marker, aggregate, "
                "gene, ongoing stress response or single survival measurement "
                "alone does not establish this history-dependent phenotype. "
                "Cell-level or lineage-restricted protection need not improve "
                "population-average survival. No fixed duration, number of "
                "divisions, stressor identity or molecular mechanism is required. "
                "Genetic adaptation, carbon-source memory, cue-triggered "
                "anticipation, diversifying bet hedging, persister formation and "
                "unequal aggregate inheritance are not equivalent, though "
                "particular observations can overlap. Unqualified cellular "
                "memory, stress priming and cross-protection are not asserted "
                "as exact synonyms. Stress response (traitmech:000078) concerns "
                "sensing and mounting protection; its research report includes "
                "cross-protection as an output but does not establish persistence "
                "after removal. METPO:1000059 phenotype is the conservative "
                "parent pending hierarchy review; existing records are unchanged."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "stress-resistance-memory-evidence-limits",
            "prompt": "Resolve natural strain provenance and assay-specific mechanisms before extending this draft.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Neither a uniform species-wide phenotype nor a shared molecular "
                "mechanism is established. Laboratory backgrounds and engineered "
                "reporters remain qualified evidence, not natural canonical "
                "taxa. No causal graph, exact synonym or external equivalence "
                "is asserted. MED/Crossref and visible publisher notice checks "
                "on 2026-10-12 exposed no linked correction or retraction for "
                "the retained sources; this bounded check does not prove notice "
                "absence. Guan's Crossref has-review relation is not a correction "
                "or independent experiment. The publisher HTML was directly "
                "retrieved through its public redirect after other endpoints "
                "failed. Source access limits and section-specific assay "
                "descriptions are retained rather than silently harmonized."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "stress-resistance-memory-metpo-identity",
            "prompt": "Retain historical stress-response neighbors without reactivating their identifiers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Pinned and current released METPO contain METPO:1000293 "
                "obsolete stress response and METPO:1000222 obsolete oxidative "
                "stress response, marked deprecated below ObsoleteClass with "
                "an OMO:0001000 reason annotation and no replacement or consider "
                "annotation in the inspected releases. These broader lexical "
                "neighbors do not define persistence after stress removal. "
                "Their historical rationale remains unresolved; neither is "
                "reactivated or used as an exact xref. Ignored/hidden available-"
                "file searches, retained historical trees, normalized trait "
                "semantics, pending PRs and ontology RDF found no exact memory "
                "class in the inspected scope. The pinned ontology is unchanged; "
                "this is not discovery exhaustion or a sequence-feature trait."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added memory of acquired stress resistance with two primary DOI "
            "references and directly checked snippets. Retained post-removal, "
            "resistance-endpoint, cell-versus-population and source-context limits. "
            "Reserved 000712, v588 and 1066500-1066599 after ignored/hidden, "
            "historical-tree, independent-copy and pending-PR checks. Examples "
            "and mechanism graph deferred; existing records unchanged. Timestamp "
            "is the observed UTC curation decision."
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
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Persistent resistance after removal, not faster transcription alone or population-wide benefit.",
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
