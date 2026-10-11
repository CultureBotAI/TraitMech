"""Add epibiotic bacterial predation and qualify its parent graph, dry-run first."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
SLUG = "epibiotic_bacterial_predation"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/ecology/predatory_bacterium.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v573/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000697"
METPO_ID = "METPO:1065000"
PARENT_ID = "traitmech:000054"
PARENT_METPO_ID = "METPO:1007653"
DEFINITION = "DOI:10.1038/ismej.2013.164"
ISOLATE = "DOI:10.1099/ijs.0.039701-0"
LIFECYCLE = "DOI:10.1038/s41467-024-48042-5"
TIMESTAMP = "2026-10-11T11:39:38Z"
PARENT_DIGEST = "0344b54577bbc17ae9f209d5651ef2163b1745509382f94eff359c4a47668694"
OLD_EDGE = "Predatory bacteria invade and lyse prey cells for nutrients."
INTERIM_EDGE = (
    "In the B. bacteriovorus model, prey invasion precedes killing and "
    "digestion of prey cells for nutrients."
)
NEW_EDGE = "B. bacteriovorus invades and digests bacterial prey for nutrients."
OLD_SCOPE = (
    "This broad ecological, host-relationship, habitat, or hazard classification "
    "spans multiple taxa and mechanisms; contextual protein nodes do not receive "
    "token UniProt examples."
)
NEW_SCOPE = OLD_SCOPE + (
    " The invasion and bdelloplast branch illustrates B. bacteriovorus, not a "
    "requirement for every predatory bacterium; epibiotic bacterial predators "
    "feed with their cell bodies outside the prey."
)
PARENT_PROJECTION = {
    "identifier": PARENT_ID,
    "label": "predatory bacterium",
    "definition": (
        "A trophic-ecology lifestyle in which a bacterium actively kills and consumes "
        "other bacteria for nutrients, e.g. the periplasmic predator Bdellovibrio bacteriovorus."
    ),
    "definition_source": "DOI:10.1146/annurev.micro.091208.073346",
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000059"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "epibiotic bacterial predation",
    "definition": (
        "A predatory bacterial phenotype in which a bacterium kills and obtains "
        "nutrients from bacterial prey while attached and growing externally, "
        "without its cell body entering the prey cell."
    ),
    "definition_source": DEFINITION,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": DEFINITION,
            "snippet": "epibiotic, where they attach to the prey from outside.",
            "notes": (
                "Pasternak et al. 2014, PMID:24088628, PMC3930308, Introduction; "
                "contiguous quotation defining the external predation strategy. "
                "Abstract, Introduction, culture/prey-range/electron-microscopy "
                "Methods, growth Results, Discussion and actual Figure 1 read. "
                "JSS and Micavibrio aeruginosavorus EPB observations support "
                "external feeding; genome comparisons are not functional proof. "
                "Do not make the paper's binary-division generalization defining: "
                "the 2024 JSS time-lapse study demonstrates nonbinary division. "
                "Other figures, genomic analyses and supplements not fully assessed. "
                "Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3930308/."
            ),
        },
        {
            "reference": ISOLATE,
            "snippet": "No periplasmic growth stage was observed and no bdelloplast was formed.",
            "notes": (
                "Koval et al. 2013, PMID:22368169, directly read scientific Abstract "
                "on the publisher site and source-qualified MED metadata. JSS "
                "was isolated from sewage in London, Ontario, with Caulobacter "
                "crescentus prey; attached external predation left emptied cells. "
                "This supports natural strain provenance and noninvasive feeding, "
                "not its frequency in undisturbed sewage. Full text, figures and "
                "supplement unavailable to this review; no Methods claim imported. "
                "Publisher: https://doi.org/10.1099/ijs.0.039701-0."
            ),
        },
        {
            "reference": LIFECYCLE,
            "snippet": (
                "Bdellovibrio exovorus is an obligate epibiotic predator that "
                "attaches on the prey cell surface, where it grows and proliferates."
            ),
            "notes": (
                "Santin et al. 2024, PMID:38678033, PMC11055950, scientific "
                "Abstract; direct contiguous match. Abstract, Introduction, "
                "Results, Discussion, selected culture/killing/live-imaging/"
                "cryo-EM/statistics Methods and actual Figures 2-5 read; other "
                "Methods, actual Figures 1/6, supplements and movies not fully "
                "assessed. JSS time-lapse growth and prey-content loss support "
                "feeding, not direct molecular nutrient tracing. The 2025 "
                "correction DOI:10.1038/s41467-025-58758-7 (PMID:40234419, "
                "PMC12000597) was read: retain its qualified prey-range wording "
                "and removal of the S-layer-defense recommendation. It is not "
                "another independent experiment. Full corrected text: "
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC11055950/."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:453816",
            "taxon_label": "Pseudobdellovibrio exovorus",
            "reference": LIFECYCLE,
            "note": (
                "Qualified to JSS (ATCC BAA-2330 = DSM 25223), not every species "
                "member. Studied as Bdellovibrio exovorus on C. crescentus; "
                "the predator's natural sewage-isolate provenance and type-strain "
                "identity are stated in the primary Abstract at "
                "https://doi.org/10.1099/ijs.0.039701-0. Some 2024 prey strains "
                "carry engineered labels or deletions; this natural-provenance "
                "qualification concerns the predator. NCBI species ID/name and "
                "JSS type material independently resolved on 2026-10-11: "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=453816."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "epibiotic-predation-scope-and-mappings",
            "prompt": "Keep external feeding distinct from general surface association.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Predatory bacterium traitmech:000054 supplies killing and "
                "nutrition; external attachment and growth supply the differentia. "
                "The broader METPO:1007093 epibiont phenotype does not require "
                "predation. Epibiosis, ectosymbiosis, ectoparasitism and vampirism "
                "are not asserted exact synonyms. The existing predation research "
                "report also calls wolf-pack Myxococcus feeding epibiotic; this "
                "record follows the attached-feeding sense of Pasternak et al., "
                "not every use of external killing. Attachment, prey lysis or "
                "sequence signatures alone are insufficient. Bacterial cannibalism "
                "traitmech:000626 concerns prey relatedness, an orthogonal axis. "
                "No organism-level disjointness is asserted. No exact xrefs or "
                "synonyms are assigned pending authority and scope reconciliation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "epibiotic-predation-mechanism-limits",
            "prompt": "Resolve feeding machinery without generalizing model-specific observations.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Causal graphs and protein examples are deferred, not claimed "
                "absent. An external predator cell body does not exclude "
                "envelope-crossing feeding structures or secreted effectors. "
                "JSS imaging supports a feeding junction but does not identify "
                "its molecular machinery; fluorescence loss is not direct nutrient "
                "tracing. Comparative gene content is not functional causality. "
                "Do not require polar attachment, binary division, fixed progeny "
                "number, a universal prey range, or obligate dependence merely "
                "because particular models exhibit them. The corrected 2024 "
                "S-layer experiments concern tested prey backgrounds, not all "
                "predators or all S-layers. The 2013/2014 studies share authors "
                "and JSS material; three citations are not three independent "
                "laboratory replications."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added external attached bacterial predation beneath predatory bacterium "
            "with three DOI-backed sources, checked snippets and a JSS-qualified "
            "example. Reserved v573 block 1065000-1065099 after ignored/hidden "
            "main/worktree and pending-PR checks. Corrected-paper scope retained; "
            "mechanisms and mappings remain open. Timestamp is the observed UTC decision."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def digest(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parent_event() -> dict:
    holder = {}
    record_curation_event(
        holder, curator="codex", action="QUALIFY_GRAPH_SCOPE",
        changes=(
            "Qualified invasion wording to the B. bacteriovorus model, not all "
            "predatory bacteria (issue #1865). Epibiotic child traitmech:000697 "
            "retains external predator bodies; parent identity, evidence and "
            "graph topology are unchanged."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return holder["curation_history"][0]


def scope_correction_event() -> dict:
    holder = {}
    record_curation_event(
        holder, curator="codex", action="CLARIFY_EVIDENCE_SCOPE",
        changes=(
            "Removed the interim edge's unnecessary temporal implication about "
            "invasion preceding killing. The final wording only qualifies the "
            "existing invasion/digestion claim to B. bacteriovorus; prior event retained."
        ),
        llm_assisted=True, timestamp="2026-10-11T11:43:59Z",
    )
    return holder["curation_history"][0]


def build_parent(parent: dict) -> dict:
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT_PROJECTION.items()):
        raise SystemExit("Parent identity differs from reviewed preimage")
    original = copy.deepcopy(parent)
    event = parent_event()
    correction = scope_correction_event()
    history = original.get("curation_history", [])
    final_replay = history[-2:] == [event, correction]
    interim_replay = history[-1:] == [event]
    if final_replay or interim_replay:
        graph = original["causal_graphs"][0]
        expected_edge = NEW_EDGE if final_replay else INTERIM_EDGE
        if graph["scope_notes"] != NEW_SCOPE or graph["edges"][0]["description"] != expected_edge:
            raise SystemExit("Parent replay differs from reviewed result")
        del original["curation_history"][-(2 if final_replay else 1):]
        graph["scope_notes"] = OLD_SCOPE
        graph["edges"][0]["description"] = OLD_EDGE
    if digest(original) != PARENT_DIGEST:
        raise SystemExit("Parent content differs from reviewed preimage")
    result = copy.deepcopy(original)
    result["causal_graphs"][0]["scope_notes"] = NEW_SCOPE
    result["causal_graphs"][0]["edges"][0]["description"] = NEW_EDGE
    result["curation_history"].extend([event, correction])
    return result


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [PARENT_METPO_ID, PARENT_PROJECTION["label"], PARENT_PROJECTION["definition"],
         "TraitMech:data/traits/ecology/predatory_bacterium.yaml|" + PARENT_PROJECTION["definition_source"],
         "METPO:1000059", "", "", "metpo_traitmech_2026_10", "",
         "Existing v5 parent ID and meaning; included for standalone hierarchy.", PARENT_ID],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/ecology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "External attached feeding; predator cell body does not enter prey.", IDENTIFIER],
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = build_parent(yaml.safe_load(PARENT_PATH.read_text()))
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(parent, Path(tmp) / PARENT_PATH.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, PARENT_PATH)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
