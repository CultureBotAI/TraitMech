"""Add fungal peloton formation with source-qualified mycorrhizal scope."""

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
SLUG = "fungal_peloton_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v542/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000666"
METPO_ID = "METPO:1061900"
ORCHID = "DOI:10.1111/nph.14279"
ERICOID = "DOI:10.1111/1365-2745.70188"
REVIEW = "DOI:10.1111/nph.19338"
MANUSCRIPT_URL = (
    "https://iris.unito.it/retrieve/e27ce429-fbc3-2581-e053-d805fe0acbaa/"
    "N_metabolism_ORM_rev10_4aperto.pdf"
)
ERICOID_URL = "https://freidok.uni-freiburg.de/data/273892"
REVIEW_URL = (
    "https://iris.unito.it/retrieve/b44ea427-adb1-4f5b-a5b6-cc876e060f2f/"
    "New%20Phytologist%20-%202023%20-%20Perotto%20-%20At%20the%20core%20of%20the%20"
    "endomycorrhizal%20symbioses%20intracellular%20fungal%20structures%20in%20orchid.pdf"
)
TIMESTAMP = "2026-10-07T15:40:03Z"
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
    "label": "fungal peloton formation",
    "definition": (
        "A morphological phenotype in which a fungus forms intracellular "
        "coiled hyphal masses, called pelotons, in association with a plant host."
    ),
    "definition_source": ORCHID,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": ORCHID,
            "snippet": (
                "In the colonised protocorm cells, ORM fungi form coiled hyphae, "
                "known as pelotons"
            ),
            "notes": (
                "Fochi et al. (2017), author final manuscript, Discussion, "
                "Nitrogen transfer inside the mycorrhizal orchid protocorm, "
                f"printed p. 15 / physical p. 17, line 465: {MANUSCRIPT_URL} "
                "Contiguous clause matched after removing standalone line "
                "numbers and joining PDF line wraps, and visually checked. "
                "The maintained resolver returned NOT_IN_ABSTRACT; this is a "
                "manual full-text check, not a resolver VERIFIED result. Main "
                "text through Conclusions and actual Figure 5 were inspected. "
                "Figure 5 shows intact and collapsed pelotons in Serapias "
                "vomeracea 30 days after sowing with Tulasnella calospora. "
                "The manuscript's title wording and GEO(XXXX) placeholder "
                "differ from final metadata; no dataset accession is inferred. "
                "Other figure images and supplementary contents were not "
                "inspected. Transcript patterns and heterologous yeast assays "
                "are not causal tests of native peloton formation."
            ),
        },
        {
            "reference": ERICOID,
            "snippet": (
                "Ericoid hyphal coils (also called pelotons) are specific "
                "structures formed by ericoid fungi in root epidermal cells"
            ),
            "notes": (
                "Meyers et al. (2025), Table 1 continued, CCI row, Relevance "
                "column, p. 3681 / physical p. 4. The complete morphology "
                "clause was exact-matched and visually checked in the public "
                f"publisher PDF deposited at {ERICOID_URL}; its SHA256 matches "
                "the repository checksum. This directly read usage supports "
                "ericoid scope, not an orchid-only definition. Methods 2.4 "
                "scores Vaccinium myrtillus root intersects, distinguishing "
                "coils from other intracellular hyphae; CCI is not a fungal "
                "cell fraction or measured nutrient flux. No fungal species "
                "was identified for a canonical example. Actual supplementary "
                "Figure S3 was not inspected. The resolver returned UNRESOLVED; "
                "an exact Europe PMC DOI query returned no hit and Crossref "
                "confirmed the exact DOI/title. Manual PDF verification does "
                "not change that resolver verdict."
            ),
        },
        {
            "reference": REVIEW,
            "snippet": (
                "tightly coiled intracellular fungal hyphae (i.e. pelotons) "
                "are a constant feature of OrM"
            ),
            "notes": (
                "Perotto and Balestrini, Viewpoint, online 2023, institutional "
                f"early-view PDF: {REVIEW_URL} Printed/physical p. 2, The "
                "peloton: a constant feature in orchid mycorrhiza. Main text "
                "and actual Figures 1-3 were read; the contiguous clause was "
                "visually checked. This is review terminology, not independent "
                "experimental replication. The same page describes Paris-type "
                "AM coils as resembling orchid pelotons and discusses a "
                "continuum with arbusculate coils; resemblance is not exact "
                "equivalence. Figure 2 has inconsistent panel/scale labels, "
                "so no panel-specific dimensions are adopted. Its hypothesis "
                "of plant-driven development is not an established formation "
                "mechanism. The orchid discussion does not erase the separate "
                "ericoid usage in Meyers et al."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:156515",
            "taxon_label": "Tulasnella calospora",
            "reference": ORCHID,
            "note": (
                "AL13/4D = MUT4182 in Serapias vomeracea protocorms, oat medium, "
                "20 C in darkness; actual Figure 5 documents pelotons 30 days "
                "after sowing. Fochi Methods, printed p. 4 / physical p. 6, "
                f"{MANUSCRIPT_URL} reports isolation from Anacamptis laxiflora "
                "mycorrhizal roots in northern Italy and deposition as MUT4182 "
                "(citing Girlanda et al. 2011, DOI:10.3732/ajb.1000486; that "
                "original isolation paper was not read). NCBI EFetch confirms "
                "species 156515 and child strain 1051891, Tulasnella calospora "
                "MUT 4182, with equivalent name Tulasnella calospora AL13/4D. "
                "The paper's engineered yeast complementation assay is a "
                "separate experiment, not an engineered fungal exemplar. "
                "This culture-qualified example is not independent taxonomic "
                "reidentification or evidence for every strain and condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-peloton-scope-and-hierarchy",
            "prompt": "Resolve a closer parent without collapsing intracellular architectures.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059. Spiral shaped METPO:1000684, "
                "branched shaped METPO:1000687 and filament shaped "
                "METPO:1000674 concern cell shape. Mycelial growth "
                "traitmech:000074 is explicitly bacterial. Fungal arbuscule "
                "formation traitmech:000664 concerns branched intracellular "
                "structures; hyphal anastomosis traitmech:000605 is fusion, "
                "pseudohyphal growth traitmech:000653 budding-cell chains, and "
                "haustorium formation traitmech:000663 a specialized host "
                "interface. None is an exact duplicate or settled closer "
                "parent. Fochi's orchid usage and Meyers' ericoid usage both "
                "inform the unqualified label. The review's Paris-type AM "
                "comparison does not make every intracellular coil a peloton "
                "or establish disjoint organisms. No exact synonyms, structure "
                "xrefs or SSSOM equivalences are asserted. Liverwort terminology "
                "in DOI:10.1098/rstb.2000.0617 remains an abstract-only analogy "
                "lead; its full text and figures were not inspected."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-peloton-formation-versus-function",
            "prompt": "Separate formation from nutrient transfer and proposed regulation.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The phenotype does not require a measured nutrient flux, "
                "exclusive mutualism, a universal lifespan, or a specific "
                "plant-driven mechanism. Transcript associations and isolated "
                "transporter complementation do not establish the native "
                "formation pathway. Nutrient transfer before or during coil "
                "degeneration is a separate question from morphogenesis. A "
                "protein-resolved causal graph is deferred pending direct "
                "formation perturbations and authority-verified protein "
                "anchors; a mechanism is not claimed biologically absent. "
                "Keep the example's MUT4182 separate from Tulasnella sp. SV6 "
                "(MUT4178) studied in DOI:10.1186/s43008-024-00165-6: that "
                "paper uses AL13/4D as a reference genome, not as its culture."
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
            "Added fungal peloton formation with two primary DOI-backed "
            "sources, a separately identified review, three snippets and a "
            "culture-qualified Tulasnella calospora example. Ignored-and-hidden "
            "novelty and main/worktree/open-PR reservation checks support "
            "000666 and v542 block 1061900-1061999, with BAS #1788 reserved "
            "separately. Kept morphology distinct from nutrient flux and "
            "unproven formation mechanisms."
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
         "Intracellular coil morphology; not orchid-only or a nutrient-flux assertion.",
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
