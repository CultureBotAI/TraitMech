"""Add pinocytosis and resolve the macropinocytosis parent gap."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/pinocytosis.yaml"
CHILD_PATH = ROOT / "data/traits/physiology/macropinocytosis.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v511/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000635"
METPO_ID = "METPO:1058800"
FIRST = "DOI:10.1083/jcb.53.3.681"
SECOND = "DOI:10.1099/00221287-92-2-246"
TAXONOMY = "DOI:10.1016/j.ejop.2024.126091"
PROVENANCE = "https://www.atcc.org/products/30010"
TIMESTAMP = "2026-10-06T05:29:34Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
CHILD = {
    "identifier": "traitmech:000634",
    "label": "macropinocytosis",
    "definition": (
        "A physiological phenotype in which a microbial organism internalizes "
        "bulk extracellular fluid by closing actin-driven plasma-membrane "
        "ruffles into large intracellular vesicles."
    ),
    "definition_source": "DOI:10.1242/jcs.213736",
    "mapping_status": "PROPOSED",
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
}
CHILD_DISCUSSION = "macropinocytosis-scope-and-hierarchy"
CHILD_RATIONALE_SHA256 = "1867972ba5fc5869e87a2e74493a4f02ac35a7b9a4b7598b2325da14cab584e5"
CHILD_RESOLUTION = (
    "Added pinocytosis traitmech:000635 as the direct broader phenotype. "
    "The existing ruffle-mediated bulk-fluid definition entails vesicular "
    "fluid uptake; its definition, evidence and DdB example are unchanged. "
    "This resolves the temporary phenotype-parent gap, not the separate "
    "native-mechanism discussion or any ontology equivalence. Preserve the "
    "historical v510 phenotype axiom and add METPO:1058700 SubClassOf "
    "METPO:1058800 on upstream adoption."
)
CHILD_CHANGES = (
    "Refined the direct parent to pinocytosis traitmech:000635 and resolved "
    "the temporary hierarchy discussion by definition-based inference. "
    "Preserved identity, definition, evidence, canonical example, mechanism "
    "gap, earlier history and the true broader historical proposal axiom."
)
RECORD = {
    "identifier": IDENTIFIER,
    "label": "pinocytosis",
    "definition": (
        "A physiological phenotype in which a microbial organism internalizes "
        "surrounding extracellular fluid and dissolved material into "
        "membrane-bound compartments formed from its plasma membrane."
    ),
    "definition_source": FIRST,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": FIRST,
            "snippet": (
                "HRP activity was found exclusively within membrane profiles "
                "within the cytoplasm, confirming the pinocytotic mode of uptake."
            ),
            "notes": (
                "PMID:5028259, PMC2108769. Scientific Abstract directly read "
                "in Europe PMC XML. The full-text OCR, including Introduction, "
                "Methods, Results and Discussion, was read at "
                "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2108769/fullTextXML. "
                "Tracer uptake and author-reported intracellular HRP support "
                "vesicular fluid uptake in Neff cells. OCR is not a visual "
                "figure audit: the PDF/figures were unavailable. The authors "
                "qualify the vesicle sample as nonrandom and membrane turnover "
                "as estimated; no size distribution, numerical rate or "
                "exclusive transport route is generalized here."
            ),
        },
        {
            "reference": SECOND,
            "snippet": (
                "The reduced pinocytotic activity of stationary-phase cells "
                "remains sensitive to respiratory inhibitors."
            ),
            "notes": (
                "PMID:1255130. Scientific Abstract directly read at the "
                "publisher and in NCBI PubMed XML. This independent study "
                "reports reduced inulin uptake in stationary-phase "
                "Acanthamoeba trophozoites while bead phagocytosis essentially "
                "ceases. It supports a condition-dependent fluid-uptake "
                "phenotype, not organismal disjointness or a specific protein "
                "mechanism. Full text and figures were unavailable; no "
                "unread methods or strain accession is inferred."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1257118",
            "taxon_label": "Acanthamoeba castellanii str. Neff",
            "reference": FIRST,
            "note": (
                "Laboratory-maintained Neff cells studied in the 1972 paper, "
                "with fluid tracers and author-reported intracellular HRP. "
                "NCBI EFetch verified this exact strain-rank name on "
                "2026-10-06. ATCC Neff provenance at " + PROVENANCE + " gives "
                "soil from Pacific Grove, California. The paper supplies no "
                "collection accession; this does not establish vial or genome "
                "identity with ATCC 30010 or an unchanged original isolate. "
                "The legacy NCBI name is retained despite the transfer of "
                "Neff to A. terricola in " + TAXONOMY + "; see the open "
                "taxonomy discussion. This is not a species-wide assertion."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "pinocytosis-scope-and-hierarchy",
            "prompt": "Keep vesicular fluid uptake distinct from neighboring traits.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059 pending a broader endocytic "
                "capability hierarchy. This is uptake by a microbe, not "
                "induction of host-cell uptake. Macropinocytosis "
                "traitmech:000634 is a narrower ruffle-mediated mode; its "
                "existing definition supports the direct parent refinement. "
                "Do not equate pinocytosis with particle engulfment "
                "traitmech:000627, nutritional phagotrophy traitmech:000628 "
                "or prey-content aspiration traitmech:000631. These traits "
                "are not declared organismally disjoint. Solute transport "
                "across a membrane, surface adsorption, open invaginations "
                "and membrane recycling alone do not establish fluid "
                "internalization. No fixed vesicle size, ruffle, nutritional "
                "requirement or universal nonconcentrative uptake is imposed. "
                "Process-level ontology mappings and synonyms remain unasserted."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "pinocytosis-neff-taxonomy",
            "prompt": "Reconcile the legacy Neff taxon name with its reassignment.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "The 2024 primary taxonomy paper transfers Neff to A. terricola, "
                "whereas NCBI still labels strain 1257118 Acanthamoeba "
                "castellanii str. Neff and ATCC 30010 retains A. castellanii. "
                "Keep the issuing-authority label with explicit strain scope "
                "rather than silently generalizing to either species. The "
                "taxonomy paper's scientific abstract was directly read; "
                "its full phylogenetic data were not audited. Revisit the "
                "authority mapping when the strain identity is reconciled."
            ),
            "evidence": [{
                "reference": TAXONOMY,
                "evidence_source": "abstract",
                "snippet": (
                    "The Neff strain is therefore transferred to A. terricola "
                    "and should no longer be considered as belonging to A. castellanii."
                ),
                "notes": (
                    "PMID:38772052; exact scientific Abstract span from NCBI "
                    "PubMed XML. Taxonomy evidence, not another pinocytosis "
                    "experiment or independent trait replication."
                ),
            }],
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "pinocytosis-native-mechanism",
            "prompt": "Resolve uptake routes before asserting molecular dependencies.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The two experimental papers concern Acanthamoeba and do "
                "not establish independent taxon replication. The 1972 "
                "nonconcentrative uptake interpretation is study-specific. "
                "Tracer loss, metabolism and static membrane profiles limit "
                "rate and route inference; the actual figures remain "
                "unaudited. Respiratory-inhibitor sensitivity does not "
                "identify a particular uptake protein. HRP is an external "
                "tracer, not a native microbial protein exemplar. No "
                "protein accessions or causal graph are inferred."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(record, curator="codex", action=action, changes=changes,
                         llm_assisted=True, timestamp=TIMESTAMP)


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(record, "MINTED_TRAITMECH_ID", (
        "Added pinocytosis with two primary DOI-backed scientific-abstract "
        "snippets, a strain-qualified Neff example and explicit taxonomy "
        "and source-access limits. Ignored-and-hidden searches and full "
        "pinned METPO review found no exact record. Reserved METPO:1058800 "
        "in v511 and refined macropinocytosis to this broader phenotype."
    ))
    return record


def build_child(record: dict) -> dict:
    record = copy.deepcopy(record)
    if any(record.get(k) != v for k, v in CHILD.items()):
        raise SystemExit("Child identity or scope differs from reviewed preimage")
    matches = [d for d in record.get("discussions", [])
               if d.get("discussion_id") == CHILD_DISCUSSION]
    if len(matches) != 1:
        raise SystemExit("Child discussion identity differs")
    discussion = matches[0]
    if (discussion.get("kind") != "CURATION_TODO"
            or hashlib.sha256(discussion.get("rationale", "").encode()).hexdigest()
            != CHILD_RATIONALE_SHA256):
        raise SystemExit("Child discussion scope differs")
    expected = {}
    event(expected, "REFINE_PINOCYTOSIS_PARENT", CHILD_CHANGES)
    expected_event = expected["curation_history"][0]
    history = record.get("curation_history", [])
    if record.get("parent_traits") == [IDENTIFIER]:
        if (discussion.get("status") != "RESOLVED"
                or discussion.get("resolved_date") != "2026-10-06"
                or discussion.get("resolution_note") != CHILD_RESOLUTION
                or not history or history[-1] != expected_event):
            raise SystemExit("Child replay differs from reviewed result")
        return record
    if (record.get("parent_traits") != [PARENT["identifier"]]
            or discussion.get("status") != "OPEN"
            or "resolved_date" in discussion or "resolution_note" in discussion
            or expected_event in history):
        raise SystemExit("Child hierarchy or discussion state differs")
    record["parent_traits"] = [IDENTIFIER]
    discussion.update(status="RESOLVED", resolved_date="2026-10-06",
                      resolution_note=CHILD_RESOLUTION)
    event(record, "REFINE_PINOCYTOSIS_PARENT", CHILD_CHANGES)
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join(["TraitMech:data/traits/physiology/pinocytosis.yaml", FIRST, SECOND]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Vesicular fluid uptake; add the v510 child refinement documented in proposal.md.",
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
    if any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs")
    record = build_record()
    child = build_child(yaml.safe_load(CHILD_PATH.read_text()))
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(child, Path(tmp) / CHILD_PATH.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(child, CHILD_PATH)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
