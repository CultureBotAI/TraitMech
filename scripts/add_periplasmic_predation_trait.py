"""Add periplasmic bacterial predation through the guarded validated writer."""

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
SLUG = "periplasmic_bacterial_predation"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/ecology/predatory_bacterium.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v575/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000699"
METPO_ID = "METPO:1065200"
PARENT_ID = "traitmech:000054"
PARENT_METPO_ID = "METPO:1007653"
IDENTITY = "DOI:10.1038/s42003-025-09010-x"
GROWTH = "DOI:10.1128/JB.00914-10"
STRUCTURE = "DOI:10.1128/jb.96.4.1366-1381.1968"
TIMESTAMP = "2026-10-11T14:16:57Z"
PARENT = {
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
    "label": "periplasmic bacterial predation",
    "definition": (
        "A predatory bacterial phenotype in which a bacterium enters the periplasm "
        "of a bacterial prey cell and grows and reproduces there using nutrients "
        "obtained by killing and consuming the prey."
    ),
    "definition_source": IDENTITY,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": IDENTITY,
            "snippet": (
                "establishes itself in the prey periplasm, feeding on the prey\u2019s "
                "cytoplasmic contents as a main nutrient source."
            ),
            "notes": (
                "Lai et al. 2025, PMID:41125861, PMC12546842, Introduction, second "
                "paragraph; the subject is B. bacteriovorus. Direct publisher HTML "
                "and Europe PMC full-text XML match. Scientific Abstract, Introduction, "
                "selected growth/exit Results and culture, sampling, time-lapse and "
                "statistics Methods, Discussion and actual Figures 1 and 4 read. "
                "Figure 1a is a lifecycle schematic, not direct imaging; Figure 4a "
                "includes WT exit measurements. Other figures and supplements "
                "not fully assessed. Publisher and MED showed no linked notice; "
                "MED linked the earlier preprint, not a correction. Published source: "
                "https://doi.org/10.1038/s42003-025-09010-x."
            ),
        },
        {
            "reference": GROWTH,
            "snippet": (
                "Nutrients for the replication of Bdellovibrio bacteria come "
                "entirely from the digestion of the single invaded bacterium"
            ),
            "notes": (
                "Fenton et al. 2010, PMID:20935099, scientific Abstract retrieved "
                "from source-qualified MED metadata. Supports prey-derived nutrition "
                "during intrabacterial replication; do not generalize its single-prey "
                "wording to a fixed predator occupancy or universal prey dependence. "
                "Full-text delivery failed; Methods, actual figures and supplement "
                "remain unread. MED links a commentary, not a correction/retraction; "
                "publisher notice check was inaccessible. Source: "
                "https://pubmed.ncbi.nlm.nih.gov/20935099/."
            ),
        },
        {
            "reference": STRUCTURE,
            "snippet": (
                "Although partial disruption of the cytoplasmic membrane was always "
                "apparent, the parasite did not appear to actively penetrate through this barrier."
            ),
            "notes": (
                "Burnham et al. 1968, PMID:4879563, scientific Abstract directly "
                "read at PubMed and matched source-qualified MED metadata. Electron "
                "microscopy supports entry without observed active penetration of "
                "the prey cytoplasmic membrane, not an intact membrane throughout "
                "predation or direct nutrient tracing. Full text and actual figures "
                "were unavailable; no strain-level example inferred. MED/PubMed "
                "exposed no linked notice, but publisher notice status was not "
                "verified. Source: https://pubmed.ncbi.nlm.nih.gov/4879563/."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:264462",
            "taxon_label": "Bdellovibrio bacteriovorus HD100",
            "reference": IDENTITY,
            "note": (
                "Qualified to wild-type HD100, not deletion, complemented or "
                "host-independent derivatives. Lai et al. used E. coli laboratory "
                "prey; this is not direct field observation. DSM 50701 is HD100 "
                "and is recorded as a soil isolate at "
                "https://webshop.dsmz.de/en/bacteria/Bdellovibrio-bacteriovorus.html; "
                "this establishes natural provenance, not another predation assay. "
                "NCBI strain identifier, scientific name and DSM 50701 synonym "
                "independently checked on 2026-10-11: "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=264462."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "periplasmic-predation-boundaries-and-mappings",
            "prompt": "Distinguish periplasmic feeding from invasion alone.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Predatory bacterium traitmech:000054 is broader; its "
                "intraperiplasmic_growth node denotes a lifecycle stage, not this "
                "whole feeding phenotype, and must not be equated to it. Epibiotic "
                "bacterial predation traitmech:000697 keeps the predator cell body "
                "external. Generic intracellular predation, endoparasitism and "
                "endosymbiosis are not exact synonyms of periplasmic predation. "
                "Attachment, killing without entry, or residence without nutritional "
                "growth are insufficient. Exact synonyms and xrefs remain unassigned "
                "pending authority and scope reconciliation. No organism-level "
                "disjointness, universal prey range, division pattern, progeny "
                "number or obligate dependence is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "periplasmic-predation-mechanism-grounding",
            "prompt": "Ground model-specific machinery before adding causal edges.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "A protein-resolved graph and protein examples are deferred, not "
                "claimed absent. The 2025 proteome and perturbation experiments "
                "provide leads, but protein abundance, gene presence and predicted "
                "sequence function do not establish the complete feeding mechanism. "
                "Heterologous prey lysis does not establish predator invasion or "
                "nutrient uptake. Verify exact accessions, taxon pairing and relevant "
                "supplements before curating machinery; do not transfer the HD100 "
                "mechanism to every periplasmic predator."
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
            "Added periplasmic bacterial predation beneath predatory bacterium "
            "with three DOI-backed sources, checked snippets and a WT-qualified "
            "HD100 example. Ignored/hidden main/worktree and pending-PR checks "
            "support 000699 and v575 block 1065200-1065299. Existing records "
            "unchanged; exact mappings and mechanism grounding remain open. "
            "Timestamp records the observed UTC curation decision."
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
        [PARENT_METPO_ID, PARENT["label"], PARENT["definition"],
         "TraitMech:data/traits/ecology/predatory_bacterium.yaml|" + PARENT["definition_source"],
         "METPO:1000059", "", "", "metpo_traitmech_2026_10", "",
         "Existing v5 parent ID and meaning; included for standalone hierarchy.", PARENT_ID],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/ecology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "Periplasmic residence with prey-derived growth and reproduction; not entry alone.",
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
