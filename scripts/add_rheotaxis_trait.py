"""Add source-bounded rheotaxis evidence and its companion METPO proposal."""

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

SLUG = "rheotaxis"
IDENTIFIER = "traitmech:000582"
TARGET = ROOT / "data/traits/physiology/rheotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v459"
MARCOS = "DOI:10.1073/pnas.1120955109"
KAYA = "DOI:10.1016/j.bpj.2012.03.001"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "rheotaxis",
    "definition": (
        "A motile phenotype in which fluid velocity gradients bias an "
        "organism's self-propelled movement."
    ),
    "definition_source": MARCOS,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": MARCOS,
            "snippet": "Rheotaxis is the directed movement resulting from fluid velocity gradients",
            "notes": (
                "Abstract and Results, https://pmc.ncbi.nlm.nih.gov/articles/PMC3324032/ "
                "(PMID:22411815). Smooth-swimming Bacillus subtilis OI4139 exhibits "
                "transverse swimming in bulk shear flow. Physical reorientation "
                "couples to active propulsion; passive advection alone is insufficient. "
                "This is not restricted to upstream migration or receptor-mediated sensing. "
                "OI4139 is a mutant that almost never tumbles, not a wild-type "
                "canonical exemplar; no strain accession is inferred."
            ),
        },
        {
            "reference": KAYA,
            "snippet": (
                "positive rheotaxis (rapid and continuous upstream motility) in "
                "wild-type Escherichia coli freely swimming over a surface"
            ),
            "notes": (
                "Abstract, with strain and preparation in Materials and Methods, "
                "Bacteria preparation; behavioral regimes in Results and Figures 3-6. "
                "The publisher-formatted article was read at "
                "https://sacredheart.elsevierpure.com/ws/portalfiles/portal/39998836/Kaya_BJ12_Bacteria.pdf "
                "(PMID:22500751). K12 cells underwent 3-5 rounds of motility "
                "selection. Moderate shear supported upstream swimming near the "
                "channel ceiling; higher shear produced sideways swimming and "
                "downstream drag. The study does not establish universal upstream "
                "motion, a universal shear threshold, or in-vivo infection. "
                "Supplementary movies were not viewed."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:83333",
        "taxon_label": "Escherichia coli K-12",
        "reference": KAYA,
        "note": (
            "Kaya and Koser's wild-type K12 population after 3-5 motility-selection "
            "rounds, swimming near a PDMS channel ceiling under moderate shear. "
            "This condition-qualified example does not cover every K-12 cell or "
            "flow regime. No more specific K-12 substrain is inferred."
        ),
    }],
    "discussions": [{
        "discussion_id": "rheotaxis-context-specific-mechanism-grounding",
        "prompt": "Ground separate surface and bulk-flow mechanisms without inventing a shear-sensing protein.",
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "rationale": (
            "The cited studies support hydrodynamic reorientation coupled to "
            "powered swimming, but surface-associated upstream motion and bulk "
            "transverse motion must not be collapsed into one universal mechanism. "
            "A protein-resolved causal graph is deferred pending a verified link "
            "between a primary mechanistic experiment, its precise strain and "
            "an accession-level protein example. OI4139 must not be silently "
            "identified as strain 168. No graph or protein accession is asserted "
            "in this first-pass identity record. QuickGO search for rheotaxis "
            "returned no term on 2026-10-04; no exact external xref is asserted."
        ),
        "posed_by": "codex",
        "posed_date": "2026-10-04",
    }],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added rheotaxis with two primary DOI citations, contiguous snippets "
            "and a condition-qualified K-12 example resolved at NCBI. "
            "Ignored-and-hidden searches found no exact trait or METPO class. "
            "Reserved METPO:1053600 in proposal v459; deferred a protein-resolved "
            "graph rather than infer strain/protein identity."
        ),
        llm_assisted=True, timestamp="2026-10-04T00:17:45Z",
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
        "METPO:1053600", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/{SLUG}.yaml|{MARCOS}|{KAYA}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Self-propelled movement biased by fluid velocity gradients; not passive advection.",
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
