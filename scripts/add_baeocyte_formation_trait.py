"""Add source-qualified cyanobacterial baeocyte formation."""

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
SLUG = "baeocyte_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v548/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000672"
METPO_ID = "METPO:1062500"
WATERBURYA = "DOI:10.1007/s10482-021-01672-x"
PLEUROCAPSA = "PMID:18365724"
TIMESTAMP = "2026-10-08T03:20:10Z"
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
    "label": "baeocyte formation",
    "definition": (
        "A morphological phenotype in which a cyanobacterium forms small "
        "reproductive cells called baeocytes by multiple fission within a "
        "mother cell."
    ),
    "definition_source": WATERBURYA,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": WATERBURYA,
            "snippet": (
                "Baeocytes formation through multiple fission of the mature "
                "cells, which are much larger than baeocytes."
            ),
            "notes": (
                "Bonthond et al. (2021), Waterburya genus Description, directly "
                "read in publisher full text. Species Description and actual "
                "Figure 4 with its caption were inspected: panel c identifies "
                "formation inside a mother cell; panel b warns that adjacent "
                "growing cells are not products of binary fission. The images "
                "do not establish division timing or protein causality. "
                "Supplements were not inspected."
            ),
        },
        {
            "reference": PLEUROCAPSA,
            "snippet": (
                "Electron microscopy of cyanobacteria Pleurocapsa sp. CALU "
                "1126 revealed that multiple fission proceeds by successive "
                "binary fissions."
            ),
            "notes": (
                "Pinevich et al. (2008), English scientific abstract directly "
                "retrieved at https://pubmed.ncbi.nlm.nih.gov/18365724/. Its "
                "following sentence identifies baeocytes as multiple-fission "
                "products and macrocytes as binary-fission products. This "
                "supports the reported division sequence in CALU 1126, not "
                "a universal simultaneous-cleavage requirement. Juvenile-cell "
                "differences and metabolic uncoupling are source-specific "
                "observations and interpretation, not the class definition. "
                "The Russian full paper, figures and strain provenance were "
                "not inspected; no CALU 1126 canonical example is assigned."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:2874699",
            "taxon_label": "Waterburya agarophytonicola KI4",
            "reference": WATERBURYA,
            "note": (
                "KI4, a non-axenic culture from seaweed apical material collected "
                "at Falckensteiner Strand near Kiel, Germany. Collection "
                "Methods report 15-degree near-dark artificial-seawater "
                "incubation and host-free subculture; the species description "
                "reports low-light liquid BG11 at 20 PSU. These are distinct "
                "culture descriptions, not an asserted Figure 4 acquisition "
                "protocol. C-A-99685 is a lyophilized filter herbarium specimen, "
                "not a living-culture accession. "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=2874699 "
                "confirms the strain-level current name with rank no rank, "
                "not a species-level ID or an independent phenotype assay."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "baeocyte-formation-scope",
            "prompt": "Review a closer parent and historical reproductive-cell terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use active phenotype METPO:1000059 below quality METPO:1000188. "
                "Binary fission METPO:1000033, reproductive process "
                "METPO:1000264 and reproductive structure METPO:1000265 are "
                "obsolete. Sporulation METPO:1000870 denotes dormant resistant "
                "endospores in the local record, not this reproductive-cell "
                "phenotype. Coenobium formation traitmech:000655 requires a "
                "clonal colony with an established cell complement; multiple "
                "fission alone is insufficient. Historical nanocyte and "
                "cyanobacterial endospore usages need source-specific review "
                "before synonym mapping. No exact synonyms, xrefs, SSSOM "
                "equivalents or organism-level disjointness are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "baeocyte-formation-mechanism",
            "prompt": "Resolve developmental mechanisms without inferring them from sequence features.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Formation, release and subsequent growth are distinct stages. "
                "Do not impose an invariant cell count, diameter, release route, "
                "motility, dormancy, sheath state or lack of growth between "
                "divisions on the whole class. Gene predictions and static "
                "morphology do not establish a protein-resolved formation "
                "mechanism. A causal graph is deferred pending direct "
                "perturbation evidence and authority-verified protein examples; "
                "the mechanism is not claimed biologically absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added baeocyte formation with two primary references, two "
            "verbatim snippets and a source-qualified KI4 example. Ignored-and-"
            "hidden novelty and current-main/worktree/complete-open-PR "
            "reservation checks support 000672 and v548 block 1062500-1062599. "
            "Kept reproductive morphology distinct from resistant endospores, "
            "coenobia and inferred protein mechanisms; existing records unchanged."
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
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Cyanobacterial reproductive-cell formation; no invariant count or protein mechanism asserted.",
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
