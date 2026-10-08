"""Add source-qualified cord formation and link the existing scope discussion."""

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
SLUG = "fungal_mycelial_cord_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
RHIZOMORPH_PATH = ROOT / "data/traits/morphology/fungal_rhizomorph_formation.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v545/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000669"
METPO_ID = "METPO:1062200"
DEFINITION = "DOI:10.1007/s10267-008-0450-4"
OUTGROWTH = "DOI:10.1099/00221287-132-1-203"
REMODELING = "DOI:10.1016/j.mycres.2006.05.013"
DEFINITION_PDF = (
    "https://markfricker.org/wp-content/uploads/2015/12/"
    "boddy_et_al-2009-mycoscience-50-9.pdf"
)
OUTGROWTH_PDF = (
    "https://www.davidmoore.org.uk/21st_century_guidebook_to_fungi_platinum/"
    "REPRINT_collection/Dowson_etal_mycelia_cord-forming_basidiomycetes.pdf"
)
TIMESTAMP = "2026-10-07T22:14:44Z"
RHIZOMORPH_PREIMAGE = "5caa2f9daf01e3ed9cfb01b9800070584580b59c74e7bb930d14c50a9795bd81"
DISCUSSION_ID = "fungal-rhizomorph-scope-and-hierarchy"
SCOPE_APPEND = (
    " Fungal mycelial cord formation traitmech:000669 now represents the "
    "diffuse-front aggregation sense defined by Boddy et al. (2009), "
    "DOI:10.1007/s10267-008-0450-4, rather than silently equating the two "
    "names. Its experimental examples do not resolve all historical usage. "
    "Keep this terminology/hierarchy question OPEN: neither equivalence, "
    "a parent-child relationship nor organism-level disjointness is asserted."
)
SCOPE_CHANGES = (
    "Linked the rhizomorph/cord scope discussion to new traitmech:000669. "
    "Preserved the attributed conflicting usages, OPEN status and all "
    "existing identity, evidence and example fields; no synonym, hierarchy "
    "or disjointness axiom was introduced."
)
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
    "label": "fungal mycelial cord formation",
    "definition": (
        "A morphological phenotype in which a fungus forms linear multihyphal "
        "cords by aggregation behind an extending margin of diffuse hyphae."
    ),
    "definition_source": DEFINITION,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION,
            "snippet": (
                "the whole organ does not extend apically; rather, it develops "
                "behind a mycelial margin of diffuse hyphae"
            ),
            "notes": (
                "Boddy et al. (2009), Introduction, printed p. 10; contiguous "
                "clause whose antecedent is mature mycelial cords. Directly "
                f"read and visually checked in the author PDF: {DEFINITION_PDF} "
                "This review supplies the operational terminology adopted "
                "here, not independent experimental replication. First three "
                "pages and Figure 1 were inspected; remaining figures and "
                "supplements were not."
            ),
        },
        {
            "reference": OUTGROWTH,
            "snippet": (
                "Both fungi grew out radially from the inoculum blocks in "
                "the form of networks of mycelial cords."
            ),
            "notes": (
                "Dowson, Rayner and Boddy (1986), complete abstract sentence, "
                f"visually verified in the original-paper reprint: {OUTGROWTH_PDF} "
                "All nine pages of text and actual Figures 1 and 3 were "
                "inspected. The Introduction describes predominantly parallel, "
                "longitudinally aligned hyphal aggregates. Underside photocopies "
                "show network development, not microscopic proof of internal "
                "anatomy. Inoculum size and culture age are confounded. Other "
                "figure images were not inspected."
            ),
        },
        {
            "reference": REMODELING,
            "snippet": "After 99 d, all systems had produced distinct mycelial cords",
            "notes": (
                "Wood et al. (2006), PMID:16891104; contiguous scientific-abstract "
                "clause retrieved directly through Europe PMC. The following "
                "clause describes regression of diffuse mycelium and thinner "
                "cords. This soil-microcosm experiment supports formation and "
                "remodeling, not a universal 99-day onset. Full text, figures "
                "and strain provenance were not inspected; no additional "
                "canonical isolate is inferred."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:194680",
            "taxon_label": "Phanerochaete velutina",
            "reference": OUTGROWTH,
            "note": (
                "The unnumbered isolate in Dowson et al. (1986), Methods p. 204 "
                "at https://doi.org/10.1099/00221287-132-1-203, originated "
                "from decayed Fagus sylvatica wood at Farleigh Hungerford "
                "Woods, Wiltshire, UK (ST795563). Colonized beech blocks "
                "produced cords on moist unsterile sandy loam at 20 C in "
                "darkness; actual Figure 1d-f shows controls at 8, 12 and "
                "44 days. NCBI EFetch confirms species 194680. No later "
                "collection number or all-strain claim is inferred."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-mycelial-cord-scope-and-hierarchy",
            "prompt": "Reconcile cord/rhizomorph usage and a closer fungal parent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059. The definition adopts the "
                "developmental cord sense in the cited terminology source; "
                "it does not claim every historical cord, strand or rhizomorph "
                "label has this meaning. The broad root-like formation "
                "record traitmech:000662 retains its Koch (2017) unmelanized "
                "culture usage and Oliveira (2024) narrower organized-tip "
                "usage. Its scope discussion is linked, not declared solved. "
                "No exact synonyms, xrefs, parent-child or disjointness "
                "axioms between these records are asserted. Mycelial growth "
                "000074 is bacterial; hyphal anastomosis 000605 requires "
                "cytoplasmic continuity; filament shaped 1000674 describes "
                "a cell, while filamentous colony 1007066 and rhizoid colony "
                "1007068 describe colony outlines. Those are not this "
                "multihyphal developmental architecture. No universal "
                "pigment, rind, vessel-hypha, diameter or habitat condition "
                "is imposed."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-mycelial-cord-mechanism-and-readout",
            "prompt": "Separate cord formation from network function and total hyphal coverage.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "A formation-regulatory protein graph is deferred pending "
                "primary perturbation evidence and authority-verified "
                "protein anchors, not because mechanisms are absent. "
                "Visible cords alone do not prove transport efficiency, "
                "resource sensing or a universal foraging response. The "
                "1986 authors describe variable curvature and did not "
                "discriminate soluble, volatile and other microenvironmental "
                "causes. Numerical network edges are not molecular causal "
                "edges. Total hyphal image coverage is not a cord-specific "
                "formation count or fraction."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def fingerprint(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal mycelial cord formation with source-attributed "
            "developmental scope, two experimental citations, three short "
            "snippets and a provenance-qualified natural isolate. "
            "Ignored-and-hidden searches included all worktrees and "
            "pending PR artifacts. Reserved 000669/v545/1062200-1062299 "
            "after accounting for pending 000667 and 000668. Kept "
            "terminology and protein mechanisms explicitly unresolved."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def scope_event(record: dict) -> None:
    record_curation_event(
        record, curator="codex", action="LINKED_SCOPE_DISCUSSION",
        changes=SCOPE_CHANGES, llm_assisted=True, timestamp=TIMESTAMP,
    )


def update_rhizomorph(record: dict) -> dict:
    if not isinstance(record, dict):
        raise SystemExit("Rhizomorph preimage differs from reviewed scope")
    before = copy.deepcopy(record)
    expected_event = {}
    scope_event(expected_event)
    # Accept only the reviewed original or its exact, idempotent result.
    if fingerprint(before) != RHIZOMORPH_PREIMAGE:
        if (before.get("curation_history") or [])[-1:] != expected_event["curation_history"]:
            raise SystemExit("Rhizomorph preimage differs from reviewed scope")
        before["curation_history"].pop()
        matches = [d for d in before.get("discussions", []) if d.get("discussion_id") == DISCUSSION_ID]
        if len(matches) != 1 or not matches[0].get("rationale", "").endswith(SCOPE_APPEND):
            raise SystemExit("Rhizomorph preimage differs from reviewed scope")
        matches[0]["rationale"] = matches[0]["rationale"][:-len(SCOPE_APPEND)]
        if fingerprint(before) != RHIZOMORPH_PREIMAGE:
            raise SystemExit("Rhizomorph preimage differs from reviewed scope")
    discussion, = [d for d in before["discussions"] if d["discussion_id"] == DISCUSSION_ID]
    if discussion["status"] != "OPEN":
        raise SystemExit("Rhizomorph discussion differs from reviewed scope")
    discussion["rationale"] += SCOPE_APPEND
    scope_event(before)
    return before


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Diffuse-front cord aggregation; no exact rhizomorph synonym or protein mechanism asserted.",
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
    rhizomorph = update_rhizomorph(yaml.safe_load(RHIZOMORPH_PATH.read_text()))
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(rhizomorph, Path(tmp) / RHIZOMORPH_PATH.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(rhizomorph, RHIZOMORPH_PATH)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
