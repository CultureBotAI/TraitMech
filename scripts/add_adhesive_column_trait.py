"""Add evidence-backed fungal adhesive-column trap formation."""

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
SLUG = "fungal_adhesive_column_trap_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v557/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000681"
METPO_ID = "METPO:1063400"
MORPHOLOGY = "DOI:10.1016/j.isci.2020.101057"
INDUCTION = "DOI:10.1111/lam.12557"
TIMESTAMP = "2026-10-08T13:53:29Z"
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
    "label": "fungal adhesive-column trap formation",
    "definition": (
        "A morphological phenotype in which a fungus forms columns of serially "
        "arranged hyphal cells with adhesive surfaces that serve as nematode traps."
    ),
    "definition_source": MORPHOLOGY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MORPHOLOGY,
            "snippet": (
                "Fungi with the AC device form a string of cells with adhesive surfaces"
            ),
            "notes": (
                "Ji et al. (2020), Introduction, third paragraph; AC means adhesive "
                "column. Primary full-text XML at https://www.ebi.ac.uk/europepmc/"
                "webservices/rest/PMC7186526/fullTextXML and actual Figure 1 "
                "inspected. Figure 1C shows a column attributed to source-named "
                "Dactylellina cionopagum; Figure 1G shows nematode capture by "
                "multiple columns. This morphology differs from the network, "
                "knob and constricting-ring comparators. Gene-family expansion "
                "and expression correlations do not establish a causal protein "
                "requirement for column formation. The cited adhesion-gene "
                "disruption experiment concerns Arthrobotrys oligospora, not "
                "this column-forming organism. Supplemental Methods were not "
                "retrieved completely; no strain identity or universal culture "
                "condition is inferred from this paper."
            ),
        },
        {
            "reference": INDUCTION,
            "snippet": (
                "Dactylellina cionopaga YMF1\u00b701472, producing adhesive columns"
            ),
            "notes": (
                "Su et al. (2016), scientific Abstract, final sentence, directly "
                "retrieved from NCBI XML for PMID:26928264 at https://eutils.ncbi."
                "nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=26928264&retmode=xml. "
                "Abstract-only access: full Methods and figures were not retrieved. "
                "The abstract reports ammonia-associated trap induction in several "
                "fungi and names this culture as column-producing. The initial "
                "11-bacterium assay and its detailed volatile-compound analysis "
                "concern A. oligospora, not eleven independent column-forming "
                "isolates. No universal ammonia requirement, dosage, effect size "
                "or molecular induction pathway is asserted. Strain provenance "
                "remains unresolved; this is qualified phenotype evidence, not "
                "a natural canonical exemplar."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "adhesive-column-scope-and-parent",
            "prompt": "Resolve a closer fungal trap-morphology parent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Phenotype METPO:1000059 is a broad parent. Existing mycelial "
                "growth traitmech:000074 explicitly concerns bacteria; hyphal "
                "anastomosis traitmech:000605 denotes fusion. Distinguish "
                "multicellular adhesive columns from unicellular knobs, "
                "interconnected net loops, nonconstricting rings and mechanically "
                "constricting rings. A generic hyphal branch, branched-shaped "
                "cell or nematophagous genus is not sufficient. Adhesive branch "
                "is not asserted as an exact synonym without resolving its "
                "usage boundaries. No exact synonyms, xrefs, SSSOM equivalences "
                "or organism-level disjointness are asserted. Neighboring scope "
                "exclusions are not unresolved exact groundings; their "
                "closer-parent questions remain open."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "adhesive-column-strains-and-mechanism",
            "prompt": "Resolve natural strain provenance and column-specific mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Live NCBI https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                "db=taxonomy&id=47266 resolves Dactylellina cionopaga at species "
                "rank, with Monacrosporium cionopagum and Dactylella cionopaga "
                "synonyms. It does not identify YMF1.01472 as a strain accession "
                "or establish its origin. The 2020 paper's cionopagum spelling "
                "and experimental strain must be reconciled before a canonical "
                "example is added; do not conflate strains across these papers. "
                "Formation, adhesion, capture, penetration and digestion are "
                "separate endpoints; formation alone does not guarantee capture "
                "in every condition. Protein-resolved causal graphs require "
                "column-specific perturbation/complementation evidence and "
                "taxon-paired accessions. Sequence features and expression "
                "correlations are not validated phenotype predictors. No "
                "mechanism is transferred from nets, knobs or rings; mechanism "
                "is deferred, not claimed absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal adhesive-column trap formation with two primary DOI "
            "sources and contiguous source-checked snippets. Ignored-and-hidden "
            "main/worktree/open-PR checks support 000681 and v557 block "
            "1063400-1063499. Kept strain provenance and protein mechanism "
            "unresolved, distinguishing morphology from sequence correlations "
            "and induction observations. Existing records unchanged. Timestamp "
            "is observed UTC."
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
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Adhesive multicellular columns; no universal inducer or sequence-derived mechanism.",
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
