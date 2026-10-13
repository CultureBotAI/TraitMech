"""Add enhanced transcriptional reactivation memory through the validated writer."""

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
SLUG = "enhanced_transcriptional_reactivation_memory"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v589/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000713"
METPO_ID = "METPO:1066600"
DEFINITION_SOURCE = "DOI:10.7554/eLife.77646"
STRESS_SOURCE = "DOI:10.7554/eLife.16691"
TIMESTAMP = "2026-10-13T00:34:29Z"
RESULT_CORRECTION_TIMESTAMP = "2026-10-13T01:22:19Z"
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
    "label": "enhanced transcriptional reactivation memory",
    "definition": (
        "A physiological phenotype in which a microbial cell or lineage retains "
        "a non-genetic state from prior inducing conditions that enhances the "
        "rate or magnitude of later transcriptional activation after intervening "
        "repression."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": "Upon Anchor Away of Opi1, reactivation was faster than activation",
            "notes": (
                "Sump et al. 2022, PMID:35579426, PMC9129879; Results s2-1, "
                "paragraph 2, contiguous in primary XML and publisher Version of "
                "Record HTML. Figure 1D uses synthetic Opi1 Anchor Away to bypass "
                "upstream induction control; enhancement is lost in mrs and "
                "nup100 mutants. Ordinary-starvation INO1 reactivation in Figure "
                "1B is not clearly faster than activation. Figure 1 supplement "
                "1C separately measures CHO1/ACT1 after three-hour repression; "
                "its generic statistical-comparator caption is ambiguous. "
                "Figure 1 supplement 2E measures 18-hour peripheral localization, "
                "not that duration of enhanced transcription; the main Results "
                "mispoints to supplement 1. Figure 1G competitive fitness is a "
                "different endpoint, not proof of transcriptional causality. "
                "Selected Results, Methods, scientific abstract, actual figures "
                "and strain-table rows were inspected. RT-qPCR mRNA kinetics "
                "are not direct measurements of initiation rate. Native abstract "
                "lookup returns NOT_IN_ABSTRACT; direct full-text matching "
                "supports the quotation, not a native VERIFIED verdict."
            ),
        },
        {
            "reference": STRESS_SOURCE,
            "snippet": (
                "We confirmed this observation for several of these genes "
                "(PGM2, PMT5 and YGP1, Figure 7A; and USV1, not shown; Guan et al., 2012)."
            ),
            "notes": (
                "D'Urso et al. 2016, PMID:27336723, PMC4951200; Results s2-7, "
                "paragraph 1, contiguous in primary XML and publisher Version "
                "of Record HTML. This complete sentence reports the authors' own "
                "confirmation: prior salt exposure enhances later peroxide-induced "
                "mRNA responses. The preceding sentence attributes the gene count "
                "and duration to Guan 2012, not a new measurement here. Figure 7A "
                "directly tests selected mRNA responses after 0.7 M NaCl for "
                "one hour, two-hour rich-medium "
                "recovery, then 0.5 mM H2O2. PGM2, PMT5 and YGP1 differ from "
                "the HSP31 control; USV1 is explicitly not shown. "
                "Four-generation persistence is not measured "
                "in that panel. Actual Figure 7B is wild-type ChIP, C mutant "
                "ChIP, D mutant mRNA and E Ssn3 ChIP; caption B/C/D assignments "
                "conflict with the image. INO1 mutant reactivation defects in "
                "Figure 1E/F alone do not establish faster within-wild-type "
                "reactivation. Relevant Results, Methods, abstract and actual "
                "figures were inspected; raw data were not reanalyzed. Native "
                "abstract lookup returns NOT_IN_ABSTRACT, with the selected "
                "quotation independently matched in full text."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "transcriptional-memory-endpoint-and-hierarchy",
            "prompt": "Preserve enhanced reactivation after repression as the defining endpoint.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Compare induced transcript responses under matched later test "
                "conditions and genetic backgrounds, after intervening repression. "
                "Continued expression, transcript or reporter persistence, a "
                "chromatin mark, peripheral localization or a gene alone does "
                "not establish this phenotype. Transcript abundance does not "
                "by itself distinguish synthesis from degradation. No identical "
                "first and second stimulus, prior production of a particular "
                "transcript, fixed duration, universal mitotic inheritance or "
                "shared chromatin mechanism is required. Carbon-source memory "
                "(traitmech:000706) spans growth and induction endpoints and is "
                "not reparented wholesale. Memory of acquired stress resistance "
                "(traitmech:000712) concerns retained resistance, not faster "
                "transcription. Anticipation and bet hedging are also not exact "
                "equivalents. Unqualified transcriptional memory, epigenetic "
                "memory and priming are not asserted as exact synonyms. "
                "METPO:1000059 phenotype is the conservative parent pending "
                "hierarchy review; existing records are unchanged."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "transcriptional-memory-evidence-limits",
            "prompt": "Resolve strain provenance and assay-specific mechanisms before extending this draft.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The two papers share a research lineage, not independent "
                "laboratory replication. Laboratory and engineered yeast "
                "backgrounds are qualified evidence, not natural canonical "
                "taxa. Sump's retrieved v2 strain table has a CHO1 DBY1428 "
                "figure locator and an HTA1-mCherry versus Methods Pho88 "
                "description discrepancy; no strain-wide extrapolation follows. "
                "Selected publisher and XML text agrees after normalization, "
                "not complete byte-level version equivalence. Publisher figure "
                "images were inspected at limited resolution, without numerical "
                "reanalysis. Bounded publisher, qualified MED and Crossref "
                "checks on 2026-10-12 exposed no linked correction or retraction; "
                "this does not prove notice absence. No causal graph, exact "
                "synonym, external equivalence or species-wide phenotype is "
                "asserted. Source access challenges and caption discrepancies "
                "are retained in the source-verification sidecar."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "transcriptional-memory-historical-identity",
            "prompt": "Reconcile deprecated lexical neighbors without reactivating their identifiers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Pinned and inspected current METPO releases mark METPO:1000108 "
                "epigenetic modification and METPO:1000310 transcription factor "
                "deprecated below ObsoleteClass, with OMO:0001000 and no "
                "replacement or consider annotation in those graphs. OMO means "
                "out of scope, but METPO issue 521 disputes the mechanical reason "
                "assignment. Original historical definitions and parent axioms "
                "remain unassessed; labels alone do not prove historical "
                "nonequivalence. This operational physiological phenotype is "
                "accepted independently from primary experiments, not by "
                "reactivating those terms or assuming a sequence-feature meaning. "
                "Ignored/hidden available files, retained historical trees, "
                "normalized trait semantics, pending changes and ontology "
                "graphs revealed no exact active record in the inspected scope. "
                "No historical exact-equivalence claim is made. The pinned "
                "ontology is unchanged; discovery is not exhausted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added enhanced transcriptional reactivation memory with two DOI "
            "references and contiguous full-text snippets. Preserved synthetic "
            "induction, transcript-endpoint, duration, source-version and "
            "historical-identity limits. Reserved 000713, v589 and "
            "1066600-1066699 after ignored/hidden, retained-tree, independent-copy "
            "and pending-PR checks. No canonical examples or mechanism graph; "
            "existing records unchanged. Timestamp is the observed UTC decision."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    record_curation_event(
        record, curator="codex", action="CORRECTED_EVIDENCE_PROVENANCE",
        changes=(
            "Replaced the D'Urso background-attribution snippet with the authors' "
            "own confirmation sentence for Figure 7A, addressing review issue "
            "1904. Retained selected-gene, two-hour recovery, unshown-USV1, "
            "four-generation and assay limits; no definition or identifiers changed."
        ),
        llm_assisted=True, timestamp=RESULT_CORRECTION_TIMESTAMP,
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
         "Enhanced transcript reactivation after repression; synthetic and assay contexts remain qualified.",
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
