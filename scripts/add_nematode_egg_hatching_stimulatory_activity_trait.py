"""Add microbial nematode egg-hatching stimulation through guarded writes."""

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
SLUG = "nematode_egg_hatching_stimulatory_activity"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v600/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000724"
METPO_ID = "METPO:1067700"
TIMESTAMP = "2026-10-14T06:04:12Z"
DEFINITION_SOURCE = "DOI:10.1163/156854104323072883"
SUPPORTING_SOURCE = "DOI:10.1186/s13071-015-0986-z"
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
    "label": "nematode egg-hatching stimulatory activity",
    "definition": (
        "A physiological capability of a microorganism to increase nematode egg "
        "hatching over a defined observation interval relative to comparable "
        "controls without that microbial influence."
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
                "Fifteen isolates (5.9%) produced compounds that strongly stimulated "
                "SCN egg hatch compared to PDB controls (Table 1)."
            ),
            "notes": (
                "Meyer et al. 2004, Results, printed page 28/PDF page 6, lower left. "
                "SCN denotes Heterodera glycines; PDB is potato dextrose broth. "
                "Native UNRESOLVED; Crossref and the USDA-hosted article verify "
                "identity. The typeset span was visually checked; PDFKit splits "
                "controls across lines, so plain whitespace normalization does "
                "not match. Hatch counts include motile and immotile juveniles at "
                "14 days, normalized to initial eggs and then uninoculated PDB "
                "hatch. Three or seven days denotes culture age, not egg exposure. "
                "The source-specific strong-effect threshold combines effect size "
                "and statistical significance; it is not a universal trait cutoff. "
                "Forty isolates were retested, not all 253. Nutrient depletion "
                "versus added stimulants remains unresolved despite the quote's "
                "compound wording. pH was measured, not neutralized. Host, isolate "
                "and culture age can change effect direction."
            ),
        },
        {
            "reference": SUPPORTING_SOURCE,
            "snippet": (
                "When incubated with Gram-positive bacteria, only T. muris eggs "
                "showed noticeable hatching after 20 h, although with high variability."
            ),
            "notes": (
                "Vejzagic et al. 2015, PMID:26174801, PMCID:PMC4501204, scientific "
                "Abstract Results; exact normalized publisher/XML match and native "
                "VERIFIED. This is its own bacterial experiment, not a citation of "
                "Meyer. Full Results and actual Figure 2 show Enterococcus caccae "
                "and Lactobacillus reuteri above bacteria-free controls after 20 h "
                "without antimicrobials, with substantial within- and between-run "
                "variability. Hatch is released larvae divided by initial embryonated "
                "eggs. T. muris and T. suis are Trichuris muris and Trichuris suis; "
                "little T. suis hatch in these conditions is not absolute inability. "
                "Antimicrobials and egg storage history affect interpretation. The "
                "E. coli strain/concentration ANOVA excludes near-zero controls; "
                "that analysis is not a statistical contrast against no bacteria. "
                "No direct-contact mechanism is inferred from background citations."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "nematode-egg-hatching-stimulation-scope-and-hierarchy",
            "prompt": "Refine the hierarchy without changing the microbial actor or positive-hatch endpoint.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is a microbial capability to increase hatching, not merely "
                "lack of inhibition, the microorganism's own development or the "
                "nematode's susceptibility. Embryogenesis without emergence, "
                "attraction, trapping, juvenile paralysis or killing alone is "
                "insufficient. Feeding, infection and benefit to the microbe are "
                "not required. No organism-level disjointness from hatch inhibition "
                "is asserted: host and culture conditions can reverse responses. "
                "Phenotype METPO:1000059 is the conservative parent. Pinned/current "
                "METPO screening found only unrelated fried-egg-shaped colony, not "
                "an exact active or deprecated counterpart in inspected owners; "
                "v600 proposes the class. No exact synonym or xref is asserted. "
                "Neither host-generalism nor a secretion/contact mechanism is implied."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "nematode-egg-hatching-stimulation-source-and-mechanism-limits",
            "prompt": "Resolve host range, strain provenance and mechanism before adding canonical examples or causal edges.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Meyer explicitly leaves nutrient depletion versus added compounds "
                "unresolved. Some fungal filtrates stimulate one host while "
                "inhibiting another, and culture age can reverse activity. The "
                "bacterial study reports variable hatch and contrasts two Trichuris "
                "hosts; neither study defines universal potency or host range. "
                "No canonical taxon, shared active molecule, protein or causal graph "
                "is inferred. No field efficacy, environmental safety, infectivity "
                "benefit or therapeutic use is asserted. Methods, own results and "
                "selected figures were inspected, not the full experimental raw "
                "data. Direct snippets and bounded notice checks are retained in "
                "the verification sidecar. Crossmark responses were script shells, "
                "not current-status verdicts; Meyer publisher access returned 403. "
                "No comprehensive correction/retraction clearance is claimed."
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
            "Added microbial nematode egg-hatching stimulatory activity with two "
            "DOI-backed primary studies and directly checked 17-word and 19-word "
            "excerpts. Preserved native UNRESOLVED/VERIFIED outcomes, source-specific "
            "comparators, host dependence and mechanism uncertainty. Positive hatch "
            "enhancement is not merely lack of inhibition. Reserved 000724, v600 "
            "and 1067700-1067799 after ignored/hidden current-copy, retained-history "
            "and open/draft PR checks; decimal measurements, embedding coordinates "
            "and broad editor ranges are not competing reservations. No exact "
            "active METPO counterpart identified in inspected owners. Other records "
            "unchanged. Timestamp records observed acceptance, not later writing."
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
         "Microbial enhancement of nematode egg hatching; no universal host range or secretion mechanism is entailed.",
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
