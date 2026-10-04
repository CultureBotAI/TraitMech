"""Add gravikinesis with drift-corrected, source-qualified swimming evidence."""

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

IDENTIFIER = "traitmech:000585"
TARGET = ROOT / "data/traits/physiology/gravikinesis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v462"
TAKEDA = "DOI:10.2187/bss.20.44"
GEBAUER = "DOI:10.1007/s001140050634"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "gravikinesis",
    "definition": (
        "A motile phenotype in which the speed of active propulsion is modulated "
        "according to orientation relative to gravity."
    ),
    "definition_source": TAKEDA,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": TAKEDA,
            "snippet": (
                "We confirmed the gravikinesis from the analysis on the swimming "
                "of single cells."
            ),
            "notes": (
                "Abstract; full publisher PDF inspected at "
                "https://www.jstage.jst.go.jp/article/bss/20/2/20_2_44/_pdf. "
                "Methods and Results (pages 45-46, Table 1) distinguish active "
                "propulsion from passive drift using subsequent 10-18 mM NiCl2 "
                "immobilization of the same cell. The drift controls retained "
                "contractile-vacuole activity and lacked visible deformation. "
                "Curved-swimmer responses reverse in 72% Percoll; straight-swimmer "
                "responses were not significant. Results N=55 and Table 1 "
                "straight-swimmer N=57 are unreconciled; no aggregate sample count "
                "is asserted. Table and method pages were visually checked."
            ),
        },
        {
            "reference": GEBAUER,
            "snippet": (
                "The resulting potential-induced modulation of the speed of propulsion "
                "is called gravikinesis because it acts to neutralize, fully or in "
                "part, sedimentation."
            ),
            "notes": (
                "Publisher abstract and Europe PMC PMID:11536922 checked. "
                "Orientation-dependent membrane-potential changes support a "
                "physiological component of propulsion control in Paramecium. "
                "The sedimentation-opposing response described here is not a "
                "universal sign convention or proof of one receptor in all taxa. "
                "The subscription full text was not inspected; no strain, channel "
                "accession or full-text-only measurement is inferred."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:5885",
            "taxon_label": "Paramecium caudatum",
            "reference": TAKEDA,
            "note": (
                "Curved-swimming cells from 14-20-day early-stationary hay-infusion "
                "cultures at 24 C, adapted to KCM (pH 7.2) and selected beneath "
                "the water surface. Table 1 supports gravity-dependent active "
                "propulsion in the control hypo-density medium. Swimming was "
                "recorded before nickel immobilization, which supplied only the "
                "passive-drift correction. This is not a universal cell-state claim. "
                "NCBI identifier is species-level; no strain accession is supplied."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "gravikinesis-speed-and-direction-boundaries",
            "prompt": "Keep propulsion modulation distinct from orientation and passive drift.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Observed upward/downward speed differences alone can arise from "
                "sedimentation or flotation; the trait concerns the active propulsion "
                "component. Gravitaxis (traitmech:000584) denotes directional bias, "
                "and gyrotaxis (traitmech:000583) denotes torque-mediated orientation. "
                "These can coexist with gravikinesis; no equivalence, disjointness "
                "or parent-child relation among them is asserted. The definition "
                "does not require faster upward swimming in every medium. Reconcile "
                "sign conventions and source-qualified response classes before "
                "adding narrower terms or equivalent external mappings."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "gravikinesis-mechanism-grounding",
            "prompt": "Resolve exact protein and taxon anchors for a mechanistic graph.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Mechanism evidence exists: Gebauer's abstract links orientation "
                "to membrane potential and propulsion, while Takeda discusses "
                "mechanosensitive conductances and ciliary control. The inspected "
                "sources do not identify a sequence-resolved gravity receptor. "
                "Takeda treats hydraulic pressure as a candidate stimulus needing "
                "amplification, not a demonstrated complete molecular pathway. "
                "A graph is deferred pending eligible taxon-paired protein examples "
                "and source-bounded causal edges. Do not substitute an unrelated "
                "channel or classify this physiological mechanism as NONMECHANISTIC "
                "to avoid the protein-coverage gate."
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
            "Added gravikinesis with two primary DOI sources, contiguous snippets "
            "and a drift-corrected Paramecium caudatum example at verified species "
            "taxon 5885. Ignored-and-hidden searches found only gravitaxis boundary "
            "mentions, not an exact trait or METPO term. Reserved METPO:1053900 in "
            "proposal v462; kept direction, passive drift, source sample counts "
            "and unresolved protein-level mechanism separate."
        ),
        llm_assisted=True, timestamp="2026-10-04T03:19:30Z",
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
        "METPO:1053900", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/gravikinesis.yaml|{TAKEDA}|{GEBAUER}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Gravity-relative modulation of active propulsion, not passive drift or directional bias.",
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
