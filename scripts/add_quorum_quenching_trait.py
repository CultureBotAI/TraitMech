"""Add source-bounded quorum quenching through the validated writer."""

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
SLUG = "quorum_quenching"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v570/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000694"
METPO_ID = "METPO:1064700"
PARENT_ID = "METPO:1000059"
SIGNAL_INTERFERENCE = "DOI:10.1128/AEM.70.2.954-960.2004"
LACTONASES = "DOI:10.1128/AEM.68.4.1754-1759.2002"
AGR_INTERFERENCE = "DOI:10.1126/scitranslmed.aat8329"
TIMESTAMP = "2026-10-11T02:46:16Z"
PARENT = {
    "identifier": PARENT_ID,
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
    "label": "quorum quenching",
    "definition": (
        "A physiological capability of a microorganism to interfere with "
        "quorum-sensing communication."
    ),
    "definition_source": SIGNAL_INTERFERENCE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": SIGNAL_INTERFERENCE,
            "snippet": (
                "However, no AHL was detected in the culture supernatant of SCG1 "
                "cocultured with either COT1 or B1, which produce AHL-lactonase."
            ),
            "notes": (
                "Dong et al. 2004, PMID:14766576, PMC348924, first Results "
                "subsection. Introduction explicitly calls signal interference "
                "quorum quenching. Scientific Abstract, Introduction, Methods, "
                "Results and early Discussion read; actual Figure 1 and Tables "
                "1/2 inspected. Other actual figures unread. COT1/B1 cocultures "
                "support AHL loss with comparable growth in this setting, not "
                "universal growth neutrality. Table 2 retains residual protection "
                "after aiiA disruption. B23 is plasmidless; SCG1-GFP is engineered. "
                "COT1 species assignment partly uses an unshown crystal-protein "
                "observation. EXT_ID:14766576 AND SRC:MED confirmed ID, title and "
                "DOI on 2026-10-11. Native resolver: NOT_IN_ABSTRACT; quotation "
                "separately matched directly retrieved PMC full text."
            ),
        },
        {
            "reference": LACTONASES,
            "snippet": (
                "Here we report identification of more than 20 bacterial isolates "
                "capable of enzymatic inactivation of AHLs from different sources."
            ),
            "notes": (
                "Dong et al. 2002, PMID:11916693, PMC123891, scientific Abstract. "
                "Abstract, Introduction, Methods, Results and selected Discussion "
                "read; actual Figure 2 and Table 1 inspected. Other actual figures "
                "unread. Whole-cell OHHL inactivation and live-versus-boiled "
                "controls support activity, not just aiiA sequence homology. "
                "Activity units use culture OD600, not molecular turnover. "
                "Restricted isolate sampling does not establish universal species "
                "activity. Plasmidless derivatives and recombinant E. coli are "
                "not unqualified natural exemplars. Authors overlap the 2004 "
                "study, not independent-laboratory replication. "
                "EXT_ID:11916693 AND SRC:MED confirmed ID, title and DOI on "
                "2026-10-11; native resolver VERIFIED, also matched directly "
                "retrieved scientific Abstract."
            ),
        },
        {
            "reference": AGR_INTERFERENCE,
            "snippet": (
                "clinical isolates of different coagulase-negative staphylococci "
                "(CoNS) species residing on normal skin produced autoinducing "
                "peptides that inhibited the S. aureus agr system"
            ),
            "notes": (
                "Williams et al. 2019, PMID:31043573, PMC7106486, scientific "
                "Abstract. Direct PMC Abstract, Results S4-S6, Methods "
                "S9-S11/S18 and actual Figures 2-4 with captions inspected. "
                "Other actual figures unread. Natural isolate supernatants and "
                "live S. hominis C5 support non-AHL interference. Figure 4 "
                "separates culture-product identification from synthetic-peptide "
                "assays; synthetic potency is not a whole-cell threshold. "
                "Figure 2A shows modest type-II/III effects despite prose "
                "describing little effect. Growth controls are condition-specific; "
                "nonsignificance is not equivalence. Supplement returned HTML, "
                "not PDF; supplemental figures and Table S1 unread. "
                "EXT_ID:31043573 AND SRC:MED confirmed ID, title and DOI on "
                "2026-10-11; native resolver VERIFIED, also matched directly "
                "retrieved scientific Abstract. A separate author group and "
                "mechanism, not direct replication of the Bacillus experiments."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "quorum-quenching-scope-and-mappings",
            "prompt": "Resolve phenotype mappings without conflating signaling actors and molecules.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is the microbial interference capability, not its enzyme, "
                "peptide, sequence feature, molecular function or treated target's "
                "loss of sensing. Positive quorum sensing traitmech:000084 is "
                "not a parent; a microorganism can both sense and quench, so "
                "organism-level disjointness is not asserted. The existing "
                "AiiA and inhibitor nodes there denote a protein and a chemical, "
                "not unresolved exact trait nodes. Reduced reporter output from "
                "toxicity or impaired growth alone is insufficient. Signal "
                "inactivation and inhibitory products are demonstrated routes, "
                "not an exhaustive mechanism restriction. No requirement for "
                "AHL, aiiA, interspecies interaction, growth neutrality, fitness "
                "benefit or disease prevention is imposed. No exact synonym or "
                "external phenotype equivalence is asserted pending authority "
                "review; molecular-function terms are not phenotype xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "quorum-quenching-exemplars-and-mechanisms",
            "prompt": "Resolve natural study strains and source-specific causal mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No canonical examples are assigned until taxonomic authorities "
                "and exact strain provenance are reconciled, including laboratory "
                "derivatives and the unread 2019 strain supplement. Preserve "
                "native coculture and supernatant evidence apart from isolated "
                "enzymes, recombinant hosts and synthetic peptides. AHL "
                "hydrolysis and agr interference need separate, source-bounded "
                "graphs; reporter inhibition alone does not establish receptor "
                "binding. Protein edges require functional evidence and "
                "taxon-paired accessions, not sequence homology alone. "
                "Mechanism is deferred, not claimed absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added quorum quenching beneath phenotype with three primary DOI "
            "citations and directly checked short snippets. Ignored-and-hidden "
            "main/worktree/open-PR checks support 000694 and v570 block "
            "1064700-1064799. Existing trait records unchanged; mappings, "
            "canonical taxa and source-specific mechanisms remain open. "
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
         PARENT_ID, "", "", "metpo_traitmech_2026_10", "",
         "Microbial interference capability, not positive quorum sensing or an enzyme.",
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
