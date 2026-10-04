"""Add gyrotaxis with source-bounded physical orientation evidence."""

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

IDENTIFIER = "traitmech:000583"
TARGET = ROOT / "data/traits/physiology/gyrotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v460"
ZENG = "DOI:10.1073/pnas.2206738119"
DURHAM = "DOI:10.1126/science.1167334"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "gyrotaxis",
    "definition": (
        "A motile phenotype in which the balance of gravitational and viscous "
        "torques biases an organism's swimming orientation."
    ),
    "definition_source": ZENG,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": ZENG,
            "snippet": (
                "The orientational response to the gravity-viscous torque balance "
                "is known as gyrotaxis"
            ),
            "notes": (
                "Introduction, page 1; definition checked against the publisher-formatted "
                "article deposited by the authors at "
                "https://api.repository.cam.ac.uk/server/api/core/bitstreams/"
                "ac9ccafe-f229-477c-9d59-b7a56cd506a0/content "
                "(PMID:36219692; PMC9586295). Results, Figures 5-7, and Materials "
                "and Methods distinguish gravitational reorientation from wall-contact "
                "effects in Heterosigma akashiwo GY-H24. Viscous resistance to rotation "
                "does not require an imposed fluid velocity gradient. Shape asymmetry "
                "and density asymmetry are alternatives; bottom-heaviness is not "
                "universal. The full main article was read; supplementary material "
                "and movies were not inspected. No gravity-sensing receptor is asserted."
            ),
        },
        {
            "reference": DURHAM,
            "snippet": (
                "We demonstrated that layers formed when the vertical migration of "
                "phytoplankton was disrupted by hydrodynamic shear."
            ),
            "notes": (
                "Abstract, with torque balance and live-cell experiments on pages "
                "1067-1069 of the full main article at "
                "https://stockerlab.ethz.ch/wp-content/uploads/2013/01/"
                "17.-DurhamKesslerStocker_Science2009.pdf (PMID:19229037). "
                "Chlamydomonas nivalis and Heterosigma akashiwo formed layers in "
                "a depth-varying shear chamber; dead cells did not. Gyrotactic "
                "trapping is a population consequence under suitable shear, not "
                "the definition of the organismal trait or the cause of every "
                "oceanic thin layer. Ocean-scale results are model predictions. "
                "The supplement and exact culture identities were not verified; "
                "no strain or modern C. nivalis taxon identity is inferred."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:2829",
        "taxon_label": "Heterosigma akashiwo",
        "reference": ZENG,
        "note": (
            "GY-H24 culture, examined 3-9 hours into the light phase of a 12-hour "
            "light/12-hour dark cycle. Figures 5-7 show gravitational reorientation "
            "and wall-modified swimming in a sealed, still-fluid microchannel; "
            "upward bias is not asserted for every cell or diurnal phase. The "
            "NCBI identifier is species-level, not a resolved GY-H24 strain accession."
        ),
    }],
    "discussions": [{
        "discussion_id": "gyrotaxis-physical-mechanism-representation",
        "prompt": "Represent physical torque-mediated orientation without inventing a protein sensor.",
        "kind": "CURATION_TODO",
        "status": "OPEN",
        "rationale": (
            "The primary papers describe a physical mechanism, so the absence of "
            "a protein accession is not absence of mechanistic evidence. This "
            "identity/evidence pass omits a graph: the current MECHANISTIC coverage "
            "audit requires a protein node and protein example, whereas "
            "NONMECHANISTIC is reserved for measurement or classification contexts. "
            "Resolve a faithful representation separately instead of relabeling "
            "the physical mechanism or inventing a sensor. Keep gravity-viscous "
            "orientation distinct from wall-contact responses and high-shear "
            "trapping. Gyrotaxis is not an exact synonym of gravitaxis, rheotaxis, "
            "bioconvection or thin-layer formation. QuickGO returned no gyrotaxis "
            "term on 2026-10-04; no exact external xref is asserted."
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
            "Added gyrotaxis with two primary DOI sources, contiguous evidence "
            "snippets and a light-phase-qualified GY-H24 example at verified "
            "species taxon NCBITaxon:2829. Ignored-and-hidden novelty searches "
            "found no exact record or METPO class. Reserved METPO:1053700 in "
            "proposal v460. Recorded the physical-graph representation gap "
            "without asserting an unsupported protein or receptor."
        ),
        llm_assisted=True, timestamp="2026-10-04T01:16:29Z",
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
        "METPO:1053700", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/gyrotaxis.yaml|{ZENG}|{DURHAM}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Gravity-viscous torque balance biases swimming; not passive sedimentation.",
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
