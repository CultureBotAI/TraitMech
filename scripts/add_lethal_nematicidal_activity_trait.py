"""Add lethal nematicidal activity through guarded, validated writes."""

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
SLUG = "lethal_nematicidal_activity"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v596/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000720"
METPO_ID = "METPO:1067300"
TIMESTAMP = "2026-10-13T17:31:43Z"
REVISION_TIMESTAMP = "2026-10-13T18:14:01Z"
PRODUCER_TIMESTAMP = "2026-10-13T18:54:48Z"
CONTEXT_REFERENCE = "DOI:10.3725/jjn.45.51"
DEFINITION_SOURCE = "DOI:10.1128/spectrum.02577-21"
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
# Retain the published preimage for guarded migration and append-only history.
INITIAL_RECORD = {
    "identifier": IDENTIFIER,
    "label": "lethal nematicidal activity",
    "definition": "A physiological capability of a microorganism to kill nematodes.",
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "PPA and t-CA displayed potent, concentration-dependent nematicidal "
                "activities against the root-knot nematode (Meloidogyne incognita) "
                "and the citrus nematode (Tylenchulus semipenetrans)"
            ),
            "notes": (
                "Kusakabe et al. 2022, PMID:35138171, scientific Abstract clause; "
                "native verifier VERIFIED and direct XML/PDF match. Methods "
                "connect P. l. sonorensis Caborca culture extracts to isolated "
                "t-CA (trans-cinnamic acid) and PPA ((4E)-5-phenylpent-4-enoic "
                "acid); synthetic standards were equipotent and used for "
                "dose-response assays. Actual Figures 2/3 and Table 4 inspected. "
                "Needle response and morphology distinguished death from "
                "paralysis; recovery used washing and 24 h in water. Table 4 "
                "tests lower-dose indole, not t-CA/PPA survival. No live-culture "
                "lethal concentration is inferred. Some numerical prose conflicts "
                "with tables; no potency, selectivity or significance values "
                "are adopted. Linked supplemental NMR/statistics files were not "
                "audited; figure inspection is not raw-data verification."
            ),
        },
        {
            "reference": "DOI:10.1038/s41598-023-33669-z",
            "snippet": (
                "T. asperellum FbMi6 at 80% concentration had the highest "
                "(90.3%) juvenile mortality compared to control."
            ),
            "notes": (
                "Saharan et al. 2023, PMID:37088805, Results in vitro activity; "
                "native NOT_IN_ABSTRACT, direct publisher HTML match. Actual "
                "Figure 4 inspected. This is culture filtrate, not live fungal "
                "inoculum: 100 newly hatched M. incognita J2, water/PDB controls, "
                "72 h endpoint, 25 +/- 2 degrees C, two repeats. Methods reports "
                "fresh-water recovery confirmation without its duration or "
                "scoring criterion. The quote's percentage is source-reported, "
                "not independently recalculated. Supplement text/tables and its "
                "embedded image were inspected, not rendered document pages. "
                "Strain/accession discrepancies prevent a canonical taxon "
                "assignment; pot/field efficacy is not imported."
            ),
        },
        {
            "reference": "DOI:10.3725/jjn.45.51",
            "snippet": (
                "The J2s inactivated by low temperature showed no reaction to "
                "the NaOH treatment."
            ),
            "notes": (
                "Harada and Yoshiga 2015, scientific abstract, printed page 51. "
                "Direct publisher HTML/PDF match; actual pages 51-54, Table 1 "
                "and Figure 1 inspected. Second-stage M. incognita juveniles "
                "could recover after warming or removal of some chemicals. "
                "This supports condition-dependent viability-assay caution, "
                "not microbial killing or an additional phenotype replication. "
                "Native UNRESOLVED: exact DOI query returned zero results; "
                "publisher and Crossref verify identity."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "lethal-nematicidal-scope-and-mappings",
            "prompt": "Refine the hierarchy while preserving the lethal, microbial-actor endpoint.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Killing susceptible nematodes is required; reversible paralysis, "
                "repellence, reduced egg hatch, host defense induction and a "
                "sequence annotation alone are insufficient. The label is "
                "qualified because nematicidal usage can include nonlethal "
                "readouts. Neither all nematode species/stages nor all producing "
                "strains are implied. Fungal nematophagy (traitmech:000719) "
                "requires feeding, and trap formation (traitmech:000718) is "
                "structural; neither is an exact parent. Predatory bacterium "
                "(traitmech:000054) requires consuming bacterial prey. Animal "
                "pathogen METPO:1004002 requires infection, unnecessary for "
                "culture-derived toxicity. Phenotype METPO:1000059 is the "
                "conservative parent. Pinned/current METPO inspection found no "
                "exact active or deprecated counterpart. CHEBI:25491 denotes "
                "a nematicide chemical, not this microbial capability, and is "
                "not an xref. No exact synonyms or organism-level disjointness "
                "are asserted; v596 proposes the class."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "lethal-nematicidal-provenance-and-mechanisms",
            "prompt": "Reconcile strain provenance and establish taxon-paired mechanisms before expanding the record.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Saharan's claimed FbMi6 accession MT529846.1 resolves in "
                "GenBank to clone SF_570, not FbMi6. Its supplement compares "
                "strain 6 with MT529837.1, clone SF_561, but labels the table "
                "SF_570 and the mortality image FbMi-4. No corrected accession "
                "is inferred. Caborca's primary strain-provenance reference "
                "has not been reconciled either. Retain these qualified "
                "observations without canonical examples. No common molecular "
                "mechanism, natural lethal dose, nutritional benefit or "
                "environmental safety is established; graphs and proteins "
                "remain unset. Culture-derived activity does not restrict "
                "the entire class to secretion. Crossref/publisher/indexing "
                "notice checks are bounded, not comprehensive clearance. "
                "Source hashes, assay limits and native verification outcomes "
                "are retained in the source-verification sidecar."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
    ],
}


def build_initial_record() -> dict:
    record = copy.deepcopy(INITIAL_RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added lethal nematicidal activity with two primary microbial-product "
            "studies and one viability-method citation, each with a directly "
            "matched snippet. Distinguished death from reversible paralysis "
            "and feeding; retained strain and assay caveats. Reserved 000720, "
            "v596 and 1067300-1067399 after ignored/hidden current-file, retained "
            "history and open/draft PR checks, with numeric false positives "
            "adjudicated. No exact active METPO counterpart identified. Other "
            "records unchanged. Timestamp records observed post-audit acceptance."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_role_corrected_record() -> dict:
    record = build_initial_record()
    context = record["evidence"].pop()
    assert context["reference"] == CONTEXT_REFERENCE
    record["discussions"][0]["rationale"] += (
        f' Methodological context, {context["reference"]}: "{context["snippet"]}". '
        f'{context["notes"]} This citation is discussion-only context, not '
        "supporting evidence for the trait or its definition."
    )
    record_curation_event(
        record, curator="codex", action="CORRECTED_EVIDENCE_ROLE",
        changes=(
            "Addressed review issue #1916: moved the Harada viability-method "
            "citation and exact excerpt from supporting evidence into the scope "
            "discussion. Retained its source/resolver provenance as context. "
            "The two microbial-killing studies remain supporting evidence; the "
            "context-only DOI no longer enters proposal definition annotations. "
            "Preserved original history, identity, hierarchy and other records."
        ),
        llm_assisted=True, timestamp=REVISION_TIMESTAMP,
    )
    return record


def build_record() -> dict:
    record = build_role_corrected_record()
    record["evidence"][0].update(
        snippet=(
            "In this study, three secondary metabolites (SMs) with nematicidal "
            "activities were isolated from in vitro cultures of P. luminescens "
            "sonorensis strain Caborca"
        ),
        notes=(
            "Kusakabe et al. 2022, PMID:35138171, Discussion opening clause, "
            "printed/PDF page 12; native NOT_IN_ABSTRACT and direct XML/typeset "
            "PDF match. The producer is Photorhabdus. Culture-supernatant "
            "fractionation links the isolated metabolites to this microorganism. "
            "t-CA and PPA caused mortality; indole mainly caused reversible "
            "paralysis at lower doses, with killing only at high concentrations. "
            "Equipotent synthetic standards were used for dose-response assays. "
            "Actual Figures 2/3 and Table 4 inspected. Needle response and "
            "morphology distinguished death from paralysis; recovery used washing "
            "and 24 h in water. Table 4 tests lower-dose indole, not t-CA/PPA "
            "survival. No live-culture lethal concentration is inferred. Some "
            "numerical prose conflicts with tables; no potency, selectivity or "
            "significance values are adopted. Linked supplemental NMR/statistics "
            "files were not audited; figure inspection is not raw-data verification."
        ),
    )
    context = INITIAL_RECORD["evidence"][2]
    discussion = record["discussions"][0]
    discussion["rationale"] = INITIAL_RECORD["discussions"][0]["rationale"] + (
        " The methodological context below cautions against equating "
        "immobility or a negative NaOH response with death under all conditions. "
        "It is not evidence of microbial killing or definition support."
    )
    discussion["evidence"] = [{
        "reference": context["reference"],
        "supports": "NO_EVIDENCE",
        "evidence_source": "scientific abstract; publisher HTML and PDF",
        "snippet": context["snippet"],
        "explanation": context["notes"] + (
            " This citation is discussion-only context, not supporting evidence "
            "for the trait or its definition."
        ),
    }]
    record_curation_event(
        record, curator="codex", action="CORRECTED_PRODUCER_EXCERPT",
        changes=(
            "Addressed review issue #1917: replaced the compound-only excerpt "
            "with a directly matched producer-linked Discussion result and "
            "retained the actual NOT_IN_ABSTRACT outcome and assay limits. "
            "Moved the unchanged Harada excerpt into structured discussion "
            "evidence with NO_EVIDENCE role for native verification. Preserved "
            "#1916's two-source definition support, prior events, identity, "
            "hierarchy and other records."
        ),
        llm_assisted=True, timestamp=PRODUCER_TIMESTAMP,
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
                   *dict.fromkeys(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Microbial killing capability, not paralysis, feeding or a chemical role.",
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
    previous = [build_initial_record(), build_role_corrected_record()]
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (*previous, record):
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() not in (*map(proposal_tsv, previous), proposal):
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
