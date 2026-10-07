"""Add a source-bounded fungal intercellular root-network phenotype."""

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
SLUG = "fungal_hartig_net_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v543/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000667"
METPO_ID = "METPO:1062000"
MORPHOLOGY = "DOI:10.1111/nph.15113"
DEFINITION = "DOI:10.1111/nph.17940"
ARBUTOID = "DOI:10.1007/s00572-014-0590-7"
MORPHOLOGY_PDF = (
    "https://ri.conicet.gov.ar/bitstream/handle/11336/117651/"
    "CONICET_Digital_Nro.2f10e756-314d-4409-8829-81a4798588b0_A.pdf"
    "?isAllowed=y&sequence=2"
)
ARBUTOID_PDF = "https://d-nb.info/1192098684/34"
ORIGIN_URL = "https://mycor.iam.inrae.fr/IAM/?page_id=4555"
TIMESTAMP = "2026-10-07T18:15:22Z"
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
    "label": "fungal Hartig net formation",
    "definition": (
        "A morphological phenotype in which a fungus forms an intercellular "
        "hyphal network, called a Hartig net, within a plant root."
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
                "hyphae grow between rhizodermal cells, forming an intraradical, "
                "apoplastic hyphal network, the so-called Hartig net"
            ),
            "notes": (
                "Zhang et al. (2022; online 23 December 2021), Introduction, "
                "second paragraph, directly read publisher HTML. The contiguous "
                "clause defines the intercellular architecture, separately from "
                "the external mantle. Main text and captions were read; actual "
                "figure images and supplements were not inspected. RNAi "
                "reductions in network depth or colonized lateral-root frequency "
                "are not complete formation loss. The corrected LbGH28A cDNA "
                "must be compared with the reported reference sequence before "
                "protein grounding; no accession-level equivalence is asserted."
            ),
        },
        {
            "reference": MORPHOLOGY,
            "snippet": (
                "a loose hyphal weft has been formed between two rhizodermal "
                "cells to differentiate an intraradicular hyphal network, "
                "the so-called Hartig net"
            ),
            "notes": (
                "Zhang et al. (2018), Introduction, printed/physical p. 1, "
                f"early-view author PDF: {MORPHOLOGY_PDF} The contiguous clause "
                "was exact-matched after joining PDF line wraps and hyphenated "
                "line breaks, and visually checked. Main text and actual "
                "Figure 2 on p. 7 were inspected. Panel d shows wild-type "
                "S238N root sections; panel c retains a thinner RNAi A4 "
                "network, not its absence. Other images and supplementary "
                "contents were not inspected."
            ),
        },
        {
            "reference": ARBUTOID,
            "snippet": (
                "Hartig net around epidermal cells para-epidermal in one row; "
                "hyphal cells roundish to cylindrical."
            ),
            "notes": (
                "Kuehdorf et al. (2015; online 2014), Results, Anatomical "
                "characters of longitudinal section, printed p. 112 / physical "
                f"p. 4: {ARBUTOID_PDF} Complete contiguous descriptive sentence, "
                "exact-matched and visually checked. Main text through "
                "Discussion and actual Figure 3 on p. 114 were read. Panels "
                "e-f distinguish the Hartig net from intracellular hyphae in "
                "field-collected Leotia cf. lubrica-Comarostaphylis arbutoides "
                "roots. Anatomy was restricted to subgroup e; it does not "
                "identify every Leotia sample or the separately observed "
                "fruit bodies. No species-level canonical example or nutrient "
                "flux is inferred. Other figure images were not inspected."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:29883",
            "taxon_label": "Laccaria bicolor",
            "reference": MORPHOLOGY,
            "note": (
                "Wild-type S238N, not an RNAi line or its haploid S238N-H82 "
                "progeny. Zhang (2018) Figure 2d documents the Hartig net in "
                "hybrid poplar INRA 717-1-B4 roots three weeks after contact; "
                "Methods specifies low-glucose Pachlewski medium. The laboratory "
                f"provenance page {ORIGIN_URL} traces S238N to a 1976 Crater "
                "Lake, Oregon fruitbody collection under Tsuga mertensiana. "
                "NCBI EFetch confirms species 29883 and child strain 486041 "
                "S238N-H82; the child is not substituted for the experimental "
                "culture. This qualified example is not independent "
                "reidentification or evidence for all strains and conditions."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-hartig-net-scope-and-hierarchy",
            "prompt": "Resolve a closer morphology parent without collapsing root interfaces.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use active phenotype METPO:1000059 under quality METPO:1000188. "
                "METPO:1000198 mycorrhization is obsolete. Branched shaped "
                "METPO:1000687 concerns cell shape; mycelial growth "
                "traitmech:000074 is explicitly bacterial. Arbuscule formation "
                "000664 and peloton formation 000666 concern intracellular "
                "architectures; BAS formation 000665 is extraradical. "
                "Haustorium formation 000663 is not asserted exact, broader "
                "or disjoint. Ecological symbiosis, mutualism and "
                "endosymbiosis are not this network morphology. Arbutoid "
                "usage is directly supported above. The directly retrieved "
                "PubMed abstract for DOI:10.1007/s00572-004-0305-6 "
                "(PMID:15490255) also describes paraepidermal Hartig nets in "
                "field-collected Monotropa uniflora and Pterospora andromedea "
                "roots; its full text and figures remain unread, and no fungal "
                "taxon is inferred. The label is not restricted to one "
                "mycorrhizal category, root cell layer or host species. No "
                "exact synonyms, structure xrefs or SSSOM equivalences are "
                "asserted; a bare Hartig net names a structure, not its formation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-hartig-net-mechanism-and-culture-identity",
            "prompt": "Keep morphogenesis, symbiotic function and sequence identity separate.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "No universal nutrient-transfer rate, mutualistic outcome or "
                "cell-wall mechanism is part of the definition. Native RNAi "
                "perturbations are evidence leads, not proof that the entire "
                "network is absent; heterologous and purified-protein assays "
                "are separate. DOI:10.1111/nph.18358, directly read main text "
                "and actual Figures 3 and 8, reports shallower RNAi networks "
                "and deeper overexpression networks despite lower overall "
                "ectomycorrhizal frequency. Its T89 host is not INRA 717-1-B4, "
                "and Figure 8a/c are schematics. A causal graph is deferred "
                "pending authority-verified proteins and sequence-to-culture "
                "links, not because mechanisms are biologically absent. "
                "Keep S238N distinct from H82 reference/progeny material. "
                "The laboratory history calls an Oregon-derived antecedent "
                "S238-O, whereas DOI:10.7150/jgen.130158 assigns S238O to "
                "Quebec; those source-specific aliases are not silently equated."
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
            "Added fungal Hartig net formation with three DOI-backed snippets "
            "and a qualified wild-type S238N example. Ignored-and-hidden "
            "novelty and main/worktree/pending-PR checks support 000667, "
            "v543 and block 1062000-1062099; BAS #1788 and peloton #1791 "
            "retain their separate reservations. Kept intercellular "
            "architecture separate from nutrient transfer, intracellular "
            "structures and unverified protein mechanisms."
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
         "Intercellular root-network morphology; no nutrient-flux or universal mechanism claim.",
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
