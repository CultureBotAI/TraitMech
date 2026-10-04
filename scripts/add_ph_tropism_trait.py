"""Add external-pH-directed polarized growth with qualified primary evidence."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000602"
TARGET = ROOT / "data/traits/physiology/ph_tropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v479"
FERNANDES = "DOI:10.1128/mbio.00285-23"
YAMAMOTO = "DOI:10.1371/journal.pbio.3002726"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "pH tropism",
    "definition": (
        "A phenotype in which polarized growth is directionally biased "
        "in response to a spatial gradient of external pH."
    ),
    "definition_source": FERNANDES,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000597"],
    "evidence": [
        {
            "reference": FERNANDES,
            "snippet": (
                "F. oxysporum hyphae exposed to a pH gradient displayed "
                "robust tropism toward acid."
            ),
            "notes": (
                "Fernandes et al. (2023), Discussion; exact span in directly "
                "retrieved Europe PMC JATS, PMC10128062 (PMID:36861989). "
                "Results and Methods were read; Figure 1B and Table S1 "
                "(10.1128/mbio.00285-23.7) were visually inspected. Opposing "
                "25 mM HCl/NaOH wells tested germ-tube direction after 8 h, "
                "with at least three experiments and 500 germ tubes per "
                "experiment. Mpk1 deletion reversed direction; complementation "
                "restored acidward growth, not necessarily wild-type magnitude. "
                "Panel A measures invasion, not tropism. The assay does not "
                "by itself resolve the local pH profile or exclude every "
                "co-varying ionic effect. The higher-pH response is an "
                "engineered-mutant observation, not a natural exemplar."
            ),
        },
        {
            "reference": YAMAMOTO,
            "snippet": (
                "These outcomes indicate that the hyphae exhibit chemotropism "
                "towards pH 4 within the pH range of 3 to 8."
            ),
            "notes": (
                "Yamamoto et al. (2024), Results, Chemotropism to low pH; "
                "exact span in directly retrieved Europe PMC JATS, "
                "PMC11288418 (PMID:39078817). Figure 3 and Table S1 "
                "(10.1371/journal.pbio.3002726.s002) were visually inspected. "
                "Aspergillus nidulans tip trajectories near the pH 6.5/8 "
                "interface support reorientation. Figure 3D reports n=1 "
                "experiment with 40-50 hyphae; hypha counts are not independent "
                "experimental replication. Growth inhibition at pH 3 confounds "
                "the 3/4 comparison. The separate summary abstract's "
                "acidic-pH avoidance wording conflicts with the main Results. "
                "This is not a universal pH-4 setpoint. Strains are engineered; "
                "movies and remaining supplements were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "ph-tropism-growth-direction-and-assay-boundaries",
            "prompt": "Keep pH-directed growth distinct from taxis, tolerance and growth rate.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is a pH-specific child of chemotropism, not another "
                "name for all chemical-gradient growth. It includes growth "
                "toward lower or higher pH without requiring both in one "
                "organism; mutant direction reversal does not establish a "
                "natural higher-pH-seeking strain. pH taxis denotes active "
                "locomotion. pH optimum, acid tolerance, intracellular pH "
                "homeostasis, biomass and extension rate alone are "
                "insufficient. Retain the source-specific replication and "
                "growth-inhibition limitations; resolve external equivalents "
                "and alternative labels before adding synonyms or xrefs. "
                "The local chemotropism parent (traitmech:000597) has a "
                "pending v474 proposal, METPO:1055100, not a released term. "
                "The v479 proposal uses released METPO:1000059 phenotype; "
                "reconcile the narrower hierarchy when v474 is accepted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "ph-tropism-strain-provenance-and-spatial-mechanism",
            "prompt": "Resolve strain identity and the spatial-sensing mechanism before enrichment.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Fernandes Methods identify Fol4287 (FGSC 9935), whereas "
                "Table S1 labels its wild type FGSC 4287. Reconcile the "
                "collection label and verify natural provenance and NCBI "
                "identity before canonical examples. Yamamoto Table S1 "
                "lists engineered backgrounds including TH122. Keep "
                "spatial-gradient orientation separate from uniform pH "
                "shifts, cytosolic-pH regulation and invasion assays. "
                "Kinase perturbations support context-specific contributions, "
                "not a universal receptor or a complete spatial-sensing "
                "chain. Resolve native, taxon-paired protein accessions and "
                "direct causal links before adding a mechanism graph; "
                "NONMECHANISTIC is not a grounding bypass."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added pH tropism under local chemotropism with two primary DOI "
            "citations and exact raw-JATS snippets. Ignored-and-hidden "
            "novelty searches and structured OWL review found no exact term; "
            "the parent's pH example has broader class scope. Reserved "
            "METPO:1055600 in v479 under released phenotype. Visually "
            "inspected both key figures and strain tables. Recorded assay "
            "replication, growth confounds, mutant direction scope, source "
            "discrepancies and pending hierarchy; deferred canonical strains "
            "and accession-level causal mechanisms."
        ),
        llm_assisted=True, timestamp="2026-10-04T19:11:26Z",
    )
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "proposed_id", "label", "definition", "definition_source", "parent",
        "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed",
    ])
    writer.writerow([
        "ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
        "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
        "A oboInOwl:inSubset", "", "", "",
    ])
    writer.writerow([
        "METPO:1055600", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/ph_tropism.yaml|{FERNANDES}|{YAMAMOTO}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "External-pH-directed growth; local chemotropism parent awaits v474 acceptance.",
        IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
