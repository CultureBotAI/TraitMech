"""Add microbial nematode repellence through guarded writes."""

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
SLUG = "nematode_repelling_activity"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v601/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000725"
METPO_ID = "METPO:1067800"
TIMESTAMP = "2026-10-14T09:11:26Z"
DEFINITION_SOURCE = "DOI:10.1073/pnas.0610281104"
SUPPORTING_SOURCE = "DOI:10.15252/embj.2020106938"
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
    "label": "nematode-repelling activity",
    "definition": (
        "A physiological capability of a microorganism to elicit active movement "
        "of nematodes away from itself or substances it produces."
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
                "C. elegans specifically avoids certain strains of Serratia based "
                "on their production of the cyclic lipodepsipentapeptide serrawettin W2."
            ),
            "notes": (
                "Pradel et al. 2007, PMID:17267603, PMCID:PMC1892944, scientific "
                "Abstract; exact normalized PMC match and native VERIFIED. "
                "C. elegans denotes Caenorhabditis elegans. Own Results and actual "
                "Figures 1-4 distinguish initial entry followed by leaving "
                "Serratia marcescens lawns from absence of attraction. A swrA "
                "insertion mutant shows reduced lawn leaving but similar multiday "
                "killing; reduced avoidance is not loss of pathogenicity. Purified "
                "serrawettin W2 on E. coli OP50 lawns and acute drop-induced "
                "reversal are separate assays. The 16-hour bacterial-lawn endpoint, "
                "60-minute supplemented-lawn endpoint and acute reversal are not "
                "one exposure. Chemical recognition versus a mechanical surfactant "
                "cue remains unresolved, and other bacterial cues can contribute. "
                "Serratia swrA is not the similarly named Bacillus motility regulator."
            ),
        },
        {
            "reference": SUPPORTING_SOURCE,
            "snippet": (
                "a specific volatile organic compound, 1\u2010undecene, produced by "
                "the pathogen P. aeruginosa is sensed as an aversive signal by C. elegans."
            ),
            "notes": (
                "Prakash et al. 2021, PMID:34086368, PMCID:PMC8246062, Discussion "
                "first paragraph, own-study result; directly matched JATS, PMC and "
                "publisher text. Native NOT_IN_ABSTRACT is retained, not relabeled "
                "VERIFIED. This is its own experiment, not a citation of Pradel. "
                "P. aeruginosa denotes Pseudomonas aeruginosa. Figure 1A-B measures "
                "PA14 lawn occupancy over 12 hours. Pure 1-undecene gives negative "
                "chemotaxis and omega turns in distinct Figure 2 and Appendix S2 "
                "assays. PA14-versus-undA odor choice establishes relative preference, "
                "not by itself repulsion or complete loss of bacterial repellence. "
                "Peer-review reply page 14 reports reversals but no complete lawn "
                "leaving after 1-undecene on OP50; the alternative adjacent-lawn "
                "crossing assay is not eviction from an occupied lawn. Roaming or "
                "higher mean square displacement alone is not directional avoidance. "
                "Recipient sensory genetics is not a microbial causal pathway."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "nematode-repelling-activity-scope-and-hierarchy",
            "prompt": "Refine the hierarchy without confusing microbial repellence with recipient behavior or microbial taxis.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The bearer is a microorganism capable of eliciting active nematode "
                "movement away. Lack of attraction, relative food preference alone, "
                "paralysis, killing, feeding, trapping or altered egg hatching is "
                "insufficient. Infection, benefit to the microbe and prior ingestion "
                "are not required. No organism-level disjointness from attraction or "
                "lethality is asserted: responses depend on strain, recipient and "
                "conditions. Phenotype METPO:1000059 is the conservative parent. "
                "Pinned/current releases and inspected editor/template owners have "
                "no exact counterpart identified. Deprecated chemotaxis METPO:1000062 "
                "has no replacement or consider annotation in the inspected ontology "
                "and concerns the moving organism, not this microbial capability. "
                "It is not revived or used as a mapping. The v601 proposal retains "
                "PROPOSED status; no exact synonym or external equivalence is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "nematode-repelling-activity-source-and-mechanism-limits",
            "prompt": "Resolve assay conditions, host range and strain provenance before adding canonical examples or causal edges.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Two bacterial studies support the capability, not a shared molecule "
                "or universal nematode response. Gene presence or compound production "
                "alone cannot establish repellence. No canonical taxon, protein, "
                "chemical xref or causal graph is asserted without authority checks. "
                "Prakash Appendix S1A depicts a 22-hour incubation then a 2-hour, "
                "37 C step, whereas main Methods describes 22 hours followed by "
                "one hour at room temperature; these are not harmonized into one "
                "headspace condition. Added recipient alleles and controls in peer "
                "review do not establish a successful AWB ablation or blanket "
                "physiological specificity. Neither study proves universal "
                "nonlethality, field efficacy, environmental safety or therapeutic "
                "use. Own results, methods and selected figures/supplement/replies "
                "were inspected, not all raw data. Source URLs, hashes, direct "
                "snippet checks and bounded correction/retraction searches are "
                "retained in the verification sidecar; no comprehensive notice "
                "clearance is claimed."
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
            "Added microbial nematode-repelling activity with two primary DOI "
            "studies and directly checked 18-word and 21-word snippets. Preserved "
            "native VERIFIED/NOT_IN_ABSTRACT outcomes and distinct lawn-leaving, "
            "reversal, chemotaxis and relative-preference endpoints. Reserved "
            "000725, v601 and 1067800-1067899 after ignored/hidden current-copy, "
            "retained-history and open/draft PR checks. Decimal embedding values "
            "and broad editor ranges are not conflicting reservations. No exact "
            "active METPO counterpart or same-scope node migration identified in "
            "inspected owners; no canonical examples or shared mechanism inferred. "
            "Other records unchanged. Timestamp records observed acceptance."
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
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml", record["definition_source"]]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Microbial induction of active nematode movement away; no shared mechanism, universal host range or nonlethality is entailed.",
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
