"""Add collective bacterial predation through the guarded validated writer."""

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
SLUG = "collective_bacterial_predation"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/ecology/predatory_bacterium.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v577/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000701"
METPO_ID = "METPO:1065400"
PARENT_ID = "traitmech:000054"
PARENT_METPO_ID = "METPO:1007653"
IDENTITY = "DOI:10.1038/s41467-023-41193-x"
BOUNDARY = "DOI:10.1128/AEM.02286-19"
TIMESTAMP = "2026-10-11T16:59:40Z"
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
    "label": "collective bacterial predation",
    "definition": (
        "A predatory bacterial phenotype in which cells act in coordinated "
        "multicellular groups to kill bacterial prey and obtain nutrients from "
        "the killed cells."
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
                "Myxococcus xanthus forages and moves collectively to prey and "
                "feed on other bacterial species."
            ),
            "notes": (
                "Rombouts et al. 2023, PMID:37696789, PMC10495355, scientific "
                "abstract, not the separate editor summary. Identity checked with "
                "EXT_ID:37696789 AND SRC:MED plus matching title and DOI. Results "
                "on cell-state transitions, A/S motility, trail following and prey "
                "lysis, Discussion and relevant Methods were read directly. "
                "Figure 5 and Supplementary Table 1 (p. 12) were visually inspected. "
                "The table identifies DZ2 laboratory material and engineered "
                "reporters or motility mutants; the paper's wild-type designation "
                "does not establish an untouched natural isolate. The prey is "
                "E. coli MG1655 with HU-mCherry for the lysis readout. Figure 5 "
                "measures prey fluorescence loss relative to an uninvaded zone, "
                "not direct nutrient assimilation or individual fitness benefits. "
                "Motility perturbations support contributions to efficient "
                "predation in this assay, not universal group obligacy. Raw "
                "movies and source data were not independently reanalyzed. MED "
                "and Crossref exposed a preprint relationship, not a linked "
                "correction/retraction; none was identified on the retrieved "
                "publisher page. Source: https://www.nature.com/articles/s41467-023-41193-x."
            ),
        },
        {
            "reference": BOUNDARY,
            "snippet": (
                "In addition to group hunting, individual M. xanthus cells are "
                "able to kill and lyse prey cells"
            ),
            "notes": (
                "Zhang et al. 2020, PMID:31704687, PMC6974655, scientific "
                "ABSTRACT, not the separate IMPORTANCE text. Qualified MED "
                "identity and title/DOI checked. The PMC Results and Discussion "
                "subsections on post-killing behavior and conclusions, Methods "
                "strain table and tracking analysis were also read. This is "
                "primary counterevidence to obligate group-only killing: DK1622 "
                "cells can kill E. coli individually. Prey-fragment consumption "
                "inferences do not constitute a direct assimilation assay. The "
                "delta-aglZ analysis also included individuals in groups of two "
                "or three and is not uniformly a solitary-cell dataset. This "
                "paper is boundary evidence, not independent replication of the "
                "2023 collective-motility experiment. MED and Crossref exposed "
                "no linked correction/retraction; publisher access returned "
                "HTTP 403, leaving publisher notice status unverified. Source: "
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC6974655/."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "collective-predation-scope-and-cooperation",
            "prompt": "Keep coordinated group feeding distinct from claims of obligatory cooperation.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Predatory bacterium traitmech:000054 supplies killing and "
                "nutrition; coordinated multicellular predation supplies the "
                "differentia. Mere cell density, aggregation, motility or prey "
                "lysis without feeding is insufficient. This is a capability "
                "expressed by cells in a group context, not a claim that a lone "
                "cell displays a collective phenotype. It does not require every "
                "cell to attack one prey simultaneously or benefit equally. "
                "Solitary killing and collective feeding can coexist in the same "
                "organism; no obligate group dependence or disjointness is "
                "asserted. Cooperative predation and wolf-pack predation are "
                "not assigned exact synonym status: cooperation in an "
                "evolutionary fitness sense requires separate evidence. The "
                "2023 scout/loner/swarm bins are analysis states, not distinct "
                "primary traits. Swarming motility traitmech:000062 is explicitly "
                "flagella-dependent; gliding METPO:1000706 and twitching "
                "traitmech:000061 do not require predation. Epibiotic, "
                "periplasmic and cytoplasmic predation classify predator location, "
                "not group organization. No exact xrefs or synonyms are assigned."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "collective-predation-examples-and-mechanism",
            "prompt": "Resolve natural examples and mechanism breadth without inferring feeding from sequence.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The directly inspected collective-imaging evidence concerns "
                "DZ2 laboratory material, engineered reporters and motility "
                "perturbations. Canonical examples remain unset pending natural "
                "material provenance and independently checked taxon identity. "
                "A- and S-motility contribute to the studied M. xanthus assay, "
                "but their combination is not imposed on every possible bearer "
                "of this trophic phenotype. A causal graph and protein examples "
                "are deferred until taxon-scoped machinery and mechanism "
                "boundaries are grounded. Motility genes, secretion systems, "
                "hydrolases or other sequence features alone do not establish "
                "coordinated prey consumption. Direct nutrient assimilation "
                "and individual fitness benefits require evidence beyond the "
                "reported fluorescence-loss readout. These limits are not "
                "evidence that collective predation is absent."
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
            "Added collective bacterial predation beneath predatory bacterium "
            "with DOI-backed collective-motility and solitary-killing evidence "
            "and two checked scientific-abstract snippets. Ignored/hidden "
            "main/worktree and pending-PR checks support 000701 and v577 block "
            "1065400-1065499. Existing records unchanged; cooperation, natural "
            "examples and mechanism breadth remain explicitly bounded. "
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
         "Coordinated group feeding; neither motility alone nor obligate cooperative benefit.",
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
