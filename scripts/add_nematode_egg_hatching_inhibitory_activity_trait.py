"""Add microbial nematode egg-hatching inhibition through guarded writes."""

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
SLUG = "nematode_egg_hatching_inhibitory_activity"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v599/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000723"
METPO_ID = "METPO:1067600"
TIMESTAMP = "2026-10-14T03:09:57Z"
DEFINITION_SOURCE = "DOI:10.1163/156854104323072883"
SUPPORTING_SOURCE = "DOI:10.1038/s41598-023-33669-z"
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
    "label": "nematode egg-hatching inhibitory activity",
    "definition": (
        "A physiological capability of a microorganism to reduce nematode egg "
        "hatching over a defined observation interval relative to comparable "
        "unexposed controls."
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
                "The least hatches were recorded in 7-day-old C. globosum (L250) "
                "filtrate, with 85 and 98% hatch reductions for SCN and RKN, respectively."
            ),
            "notes": (
                "Meyer et al. 2004, Results, printed page 28/PDF page 6; all ten "
                "pages and actual Figure 1/Table 1 inspected. C. globosum is "
                "Chaetomium globosum; SCN and RKN are Heterodera glycines and "
                "Meloidogyne incognita. Native UNRESOLVED; Crossref and USDA verify "
                "identity. Typeset span matches; PDF extraction loses the fi ligature. "
                "Seven days is culture age, not egg exposure: hatch was scored "
                "after 14 days, including motile and immotile juveniles. Percent "
                "hatch uses initial eggs, then uninoculated PDB hatch as comparator; "
                "quoted reductions are relative to that control, not egg mortality. "
                "Biomass-free filtrate concentrations differ between hosts (75/90%); "
                "approximately 200 eggs per well, five wells per treatment, water "
                "viability control. Forty isolates were retested, not all 253. "
                "pH was measured, not neutralized; no identified active molecule "
                "or universal potency threshold is inferred."
            ),
        },
        {
            "reference": SUPPORTING_SOURCE,
            "snippet": (
                "T. asperellum FbMi6 inhibited egg hatching in all concentrations "
                "as compared to control."
            ),
            "notes": (
                "Saharan et al. 2023, PMID:37088805, Results; direct publisher HTML "
                "match, native NOT_IN_ABSTRACT. This is its own experiment, not its "
                "background account of Meyer. Five surface-sterilized egg masses "
                "received spore-checked culture filtrates at 20/40/60/80%, with "
                "water and PDB controls; alternate-day counts through ten days, "
                "two repeats at 25 +/- 2 degrees C. Actual Figure 3 inspected. "
                "Results associates maximum inhibition with 120 h, whereas its "
                "legend specifies 2/4/6/8/10 days; no exact maximum/time pairing "
                "is adopted. Egg deformation does not prove death. Juvenile "
                "water-recovery findings are not transferred to eggs."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "nematode-egg-hatching-inhibition-scope-and-hierarchy",
            "prompt": "Refine the hierarchy while preserving the microbial actor and hatching endpoint.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The microorganism has the inhibitory capability; this is not its "
                "own development or the nematode's susceptibility. Reduced hatching "
                "over an observed interval does not establish egg death, irreversible "
                "arrest or subsequent recovery. Juvenile paralysis or killing, "
                "fewer root egg masses, population suppression, trapping, attraction "
                "and sequence annotations alone are insufficient. Feeding and "
                "infection are not required. Related lethal, paralyzing, trapping, "
                "attracting and fungal-nematophagy records are not necessary parents; "
                "no organism-level disjointness is asserted. Phenotype METPO:1000059 "
                "is the conservative parent. Pinned/current METPO screening found "
                "only the unrelated fried-egg-shaped colony, not an exact active "
                "or deprecated counterpart in inspected owners; v599 proposes the "
                "class. Ovicidal terminology and nematicide chemical roles are not "
                "exact synonyms or xrefs. Neither a universal host/stage range nor "
                "a particular secretion mechanism is implied."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "nematode-egg-hatching-inhibition-source-and-mechanism-limits",
            "prompt": "Resolve strain provenance and assay discrepancies before adding taxa or mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Meyer's USDA technical abstract reports six motility-inhibitory "
                "isolates, versus four in the published paper; that separate "
                "endpoint is not silently reconciled. Saharan's claimed FbMi6 "
                "accession resolves to clone SF_570, while its supplement has "
                "SF_561/SF_570 and FbMi-4 inconsistencies documented in the "
                "lethal-nematicidal source assessment. Do not infer a corrected "
                "strain or canonical taxon. No shared active chemical, microbial "
                "protein, causal graph, field efficacy or environmental safety "
                "is asserted. Culture-filtrate effects do not define the entire "
                "class as secretion. Source hashes, direct quote checks and "
                "bounded notice checks are retained in the verification sidecar. "
                "Meyer has no Crossmark data available; no comprehensive notice "
                "clearance or full raw-data/statistical reanalysis is claimed."
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
            "Added microbial nematode egg-hatching inhibitory activity with two "
            "DOI-backed primary studies and directly checked 22-word and 13-word "
            "result excerpts. Retained assay denominators, exposure intervals, "
            "source discrepancies and native UNRESOLVED/NOT_IN_ABSTRACT outcomes. "
            "Distinguished hatch reduction from egg death, paralysis and reduced "
            "reproduction. Reserved 000723, v599 and 1067600-1067699 after "
            "ignored/hidden current-copy, retained-history and open/draft PR "
            "checks; broad editor ranges are not competing reservations. No exact "
            "active METPO counterpart identified in inspected owners. Other "
            "records unchanged. Timestamp records observed acceptance, not the "
            "later file write."
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
         "Microbial inhibition of nematode egg hatching; neither egg death nor recovery is entailed.",
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
