"""Add diversifying bet hedging through the validated writer."""

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
SLUG = "diversifying_bet_hedging"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v584/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000708"
METPO_ID = "METPO:1066100"
BACTERIAL = "DOI:10.1038/nature08504"
YEAST = "DOI:10.1371/journal.pbio.1001325"
MICROALGAL = "DOI:10.1038/s41467-024-46297-6"
TIMESTAMP = "2026-10-12T06:39:53Z"
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
    "label": "diversifying bet hedging",
    "definition": (
        "A physiological phenotype in which a clonal microbial lineage reversibly "
        "generates alternative cell states before environmental change, spreading "
        "risk across unpredictable environmental changes through state-specific "
        "survival or reproductive trade-offs."
    ),
    "definition_source": YEAST,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": BACTERIAL,
            "snippet": (
                "Here we report the de novo evolution of bet hedging in "
                "experimental bacterial populations."
            ),
            "notes": (
                "Beaumont et al. 2009, PMID:19890329; scientific abstract, directly "
                "checked against publisher and source-qualified MED text, not the "
                "publisher's Editorial Summary. Supports experimentally evolved "
                "risk spreading by rapid phenotype switching under a changing "
                "selection regime. Mutational evolution of a switching genotype "
                "is not the same claim as mutations generating each alternative "
                "cell state. Main figures, supplements and raw data were not "
                "independently assessed; no gene-level mechanism or natural "
                "canonical exemplar is asserted."
            ),
        },
        {
            "reference": YEAST,
            "snippet": (
                "Our results suggest that yeast bet hedging results from multiple "
                "epigenetic growth states determined by a combination of stochastic "
                "and deterministic factors."
            ),
            "notes": (
                "Levy, Ziv and Siegal 2012, PMID:22589700, PMC3348152; scientific "
                "abstract, directly checked against publisher, MED and full-text "
                "XML, separately from the Author Summary. Box 1 supplies the "
                "definition framework and explicitly leaves adaptive origin "
                "untested in this yeast study. The record preserves that limit: "
                "reversible state variation and differential stress survival do "
                "not alone establish evolutionary optimization. Binary states "
                "and a purely stochastic mechanism are not required."
            ),
        },
        {
            "reference": MICROALGAL,
            "snippet": (
                "Mobile cells grow faster but are stress-sensitive, while "
                "non-mobile cells prioritise stress resistance over growth."
            ),
            "notes": (
                "Tang et al. 2024, PMID:38453919; scientific abstract, directly "
                "checked against publisher and source-qualified MED text. The "
                "Introduction and Discussion distinguish early diversification "
                "of Haematococcus pluvialis cultures from later stress-induced "
                "conversion. Growth and survival are fitness proxies, not a "
                "demonstration of optimized long-term geometric mean fitness. "
                "Figures, supplements and raw data were not independently "
                "assessed; proposed transcriptional explanations are not "
                "encoded as causal edges."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "bet-hedging-scope-and-hierarchy",
            "prompt": "Retain lineage-level risk spreading without equating all cellular heterogeneity with bet hedging.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The diversifying qualifier restricts this class to alternative "
                "states within a clonal microbial lineage; it does not cover "
                "every use of unqualified bet hedging. Heterogeneity, noisy gene "
                "expression or switching alone is insufficient: reversible "
                "states must precede the relevant environmental shift and "
                "differ in survival or reproductive performance across conditions. "
                "Generic stress-induced change, carbon-source memory, "
                "cue-triggered environmental anticipation, genetic resistance "
                "and ecological generalist/specialist niche breadth are not "
                "exact synonyms. Particular observations can overlap without "
                "making these classes equivalent or disjoint. Dormancy and "
                "persister formation can participate in risk spreading, but "
                "their presence alone does not establish it, so neither existing "
                "record is reparented. METPO:1000059 phenotype is the conservative "
                "parent pending upstream review of this lineage-level "
                "physiological disposition. This is not a sequence feature, "
                "individual assay result or mixed-species community property."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "bet-hedging-evidence-and-mechanism-limits",
            "prompt": "Assess adaptive origin, natural exemplars and molecular mechanisms separately from the operational phenotype.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "This first-pass class does not assert that every cited system "
                "was selected for diversification or has a measured long-term "
                "fitness advantage. Levy et al. Box 1 distinguishes those "
                "stronger claims from its operational usage; testing arithmetic "
                "and geometric mean fitness requires an explicit environmental "
                "distribution and comparison strategy. No fixed switching rate, "
                "binary state space or universal protein mechanism is asserted. "
                "Canonical taxa await strain-provenance and taxonomy checks; "
                "causal_graphs, xrefs and synonyms are omitted. MED, Crossref "
                "and visible publisher links checked on 2026-10-12 exposed no "
                "correction or retraction for the three retained papers; "
                "commentary, review and preprint links are not independent "
                "experiments. This bounded check does not exclude every possible "
                "notice. Pinned/current METPO RDF and ignored/hidden novelty "
                "searches found no exact active or deprecated term; earlier "
                "research mentions remain leads, not primary records. The "
                "pinned ontology is unchanged."
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
            "Added diversifying bet hedging with three primary DOI-backed "
            "sources and directly checked scientific-abstract snippets. "
            "Reserved 000708, v584 and 1066100-1066199 after ignored/hidden "
            "worktree and pending-PR checks. Operational risk spreading is "
            "distinguished from evolutionary optimization; examples and "
            "mechanisms remain deferred. Existing traits unchanged; timestamp "
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
         "Clonal state diversification with condition-dependent trade-offs; not heterogeneity alone.", IDENTIFIER],
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
