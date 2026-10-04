"""Add photokinesis with condition-qualified primary swimming evidence."""

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

IDENTIFIER = "traitmech:000587"
TARGET = ROOT / "data/traits/physiology/photokinesis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v464"
THAR = "DOI:10.1128/AEM.67.12.5410-5419.2001"
SINESHCHEKOV = "DOI:10.1016/S0176-1617(00)80045-0"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "photokinesis",
    "definition": (
        "A motile phenotype in which the speed of active locomotion changes in "
        "response to illumination intensity, without requiring orientation toward "
        "or away from the light source."
    ),
    "definition_source": THAR,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": THAR,
            "snippet": "swimming velocities are correlated to the illumination intensity.",
            "notes": (
                "Introduction's photokinesis definition; publisher full text at "
                "https://journals.asm.org/doi/10.1128/AEM.67.12.5410-5419.2001 "
                "and Figure 2A-B with caption inspected. In Marichromatium gracile "
                "CE2205, the anoxic 1 mM total-sulfide preparation shows lower speed "
                "at low irradiance; oxic controls (>100 micromolar oxygen, no free "
                "sulfide) show no significant irradiance dependence. Reported "
                "irradiance is visible-region scalar irradiance (400-700 nm), "
                "with a fixed visible:near-infrared photon ratio of 1:8.3. "
                "Measurements use two-dimensional cell tracks after 60 s at each "
                "irradiance. Exponential-phase cells with sulfur globules were "
                "sampled above bottom aggregates. The collection-supplied strain "
                "is not assigned an independently verified natural lineage here. "
                "The separate gradient-migration results are attributed to phobic "
                "responses, not used to infer directional photokinesis."
            ),
        },
        {
            "reference": SINESHCHEKOV,
            "snippet": (
                "Photosynthetically active continuous red light reversibly enhances "
                "the swimming velocity and increases or decreases the precision "
                "of gravitaxis, depending on its initial level."
            ),
            "notes": (
                "Abstract, PMID:12090268, exact-matched at Europe PMC. This primary "
                "study of Chlamydomonas reinhardtii supports light-dependent speed "
                "modulation alongside a distinct orientation response. Its blue-light "
                "responses have different kinetics; proposed chlamy-rhodopsin "
                "participation is explicitly inferential. Subscription full text "
                "was not inspected; no strain lineage, protein accession or "
                "full-text-only result is inferred."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "photokinesis-speed-and-direction-boundaries",
            "prompt": "Preserve the speed-response scope when mapping light responses.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This definition follows the speed usage in the cited experiments. "
                "It does not require increasing speed, a photosynthetic energy "
                "mechanism, or an isolated response without concurrent taxis. "
                "Phototaxis concerns orientation; photophobic responses concern "
                "avoidance or reversals. They may coexist with photokinesis, but "
                "no equivalence, disjointness or parent-child relation is asserted. "
                "The obsolete METPO:1000241 phototaxis class is not an exact match "
                "or a replacement target. Reconcile broader kinesis terminology "
                "before adding turning-frequency synonyms or external xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "photokinesis-strain-and-mechanism-grounding",
            "prompt": "Verify natural exemplars and protein-resolved causal branches.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Qualified experimental observations are retained without canonical "
                "taxa pending independent CE2205 lineage verification or a fully "
                "inspected algal strain source. Collection provenance alone does "
                "not establish unperturbed natural ancestry. Mechanism discussion "
                "in the sources does not establish one universal receptor, and "
                "the algal abstract only suggests rhodopsin participation. A "
                "mechanistic graph is deferred pending source-backed causal edges "
                "and eligible taxon-paired protein examples. Do not borrow the "
                "generic motile graph or use NONMECHANISTIC to bypass this gap."
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
            "Added photokinesis with two primary DOI citations and contiguous "
            "snippets. Ignored-and-hidden searches found no exact record or METPO "
            "term; nearby obsolete phototaxis is distinct. Reserved METPO:1054100 "
            "in proposal v464. Preserved oxygen, spectral and experimental-state "
            "qualifiers; deferred natural canonical taxa and protein-level graphs."
        ),
        llm_assisted=True, timestamp="2026-10-04T04:46:00Z",
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
        "METPO:1054100", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/photokinesis.yaml|{THAR}|{SINESHCHEKOV}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Light-dependent speed modulation, distinct from directional and phobic responses.",
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
