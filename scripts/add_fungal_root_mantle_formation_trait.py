"""Add an evidence-bounded fungal root-sheath morphology phenotype."""

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
SLUG = "fungal_root_mantle_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v544/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000668"
METPO_ID = "METPO:1062100"
DEFINITION = "DOI:10.1128/AEM.01991-15"
FIELD = "DOI:10.3389/fpls.2014.00229"
ATLAS = "DOI:10.3390/microorganisms9122612"
ORIGIN_URL = "https://mycor.iam.inrae.fr/IAM/?page_id=4555"
ATLAS_PDF = "https://pure.mpg.de/rest/items/item_3375108_1/component/file_3400121/content"
TIMESTAMP = "2026-10-07T19:40:30Z"
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
    "label": "fungal root mantle formation",
    "definition": (
        "A morphological phenotype in which a fungus forms an external sheath "
        "of aggregated hyphae, called a mantle, around a plant root."
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
                "the fungus initially grows around the roots to form a mass "
                "of mycelium called the fungal mantle."
            ),
            "notes": (
                "Krause et al. (2015), Introduction, first paragraph, directly "
                "read publisher HTML. This contiguous clause describes the "
                "root-external mantle separately from the intraradical Hartig "
                "net. Main text and captions were read; actual figure images "
                "and supplementary contents were not inspected. The "
                "ald1-overexpressing T. vaccinum 1.16 is an engineered "
                "perturbation, not a natural canonical exemplar."
            ),
        },
        {
            "reference": FIELD,
            "snippet": (
                "The fungus enwraps the root tip with a hyphal mantle [M] "
                "composed of several layers."
            ),
            "notes": (
                "Pena et al. (2014), Figure 1 caption, complete sentence, "
                "exact-matched in primary full-text XML and visually checked "
                "in the publisher PDF on p. 3. The actual composite figure "
                "contains a root photograph and section image with schematic "
                "infrared arrows; it is not an experimental image of radiation "
                "penetration. Main Results separately describe multilayered "
                "mantles in field-collected roots. Other figure images and "
                "Table S1 were not inspected; no numerical thickness, "
                "spectral function or additional taxon exemplar is inferred."
            ),
        },
        {
            "reference": ATLAS,
            "snippet": (
                "Three weeks post-inoculation, fungal hyphae formed a "
                "thinner but denser mantle."
            ),
            "notes": (
                "Ruytinx et al. (2021), Results 3.3, complete sentence, "
                "exact-matched in primary full-text XML. Main text and actual "
                f"Figure 2 on PDF p. 8 were inspected: {ATLAS_PDF} The "
                "21-day state follows the reported thick, dense 14-day "
                "mantle, not loss of the sheath. Methods 2.6 names "
                "WGA-Alexa 488 whereas the Figure 2 caption names "
                "WGA-oregon green; the discrepancy is retained, not resolved "
                "by inference. Other figure images and supplements were "
                "not inspected."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:29883",
            "taxon_label": "Laccaria bicolor",
            "reference": ATLAS,
            "note": (
                "Reference culture S238N, not haploid S238N-H82. Ruytinx "
                "(2021), Methods 2.1/2.3 and Results 3.3 with Figure 2B-C, "
                "documents a mantle around Populus tremula x alba 717-1B4 "
                "lateral roots in P20 sandwich coculture, including the "
                "14- and 21-day states. The laboratory history at "
                f"{ORIGIN_URL} traces S238N to a 1976 Crater Lake, Oregon "
                "fruitbody collection under Tsuga mertensiana. NCBI EFetch "
                "confirms species 29883 and separate child strain 486041 "
                "S238N-H82; the genome strain is not substituted for the "
                "experimental culture. This is culture-qualified evidence, "
                "not independent reidentification or a claim for all strains."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-root-mantle-scope-and-hierarchy",
            "prompt": "Resolve a closer morphology parent without conflating root interfaces.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use active phenotype METPO:1000059 under quality METPO:1000188; "
                "METPO:1000198 mycorrhization is obsolete. The root qualifier "
                "excludes other senses of mantle or sheath. Hartig net "
                "formation traitmech:000667 is intercellular within roots; "
                "arbuscules 000664 and pelotons 000666 are intracellular, "
                "while BAS 000665 are branching groups on extraradical "
                "runner hyphae. Mycelial growth 000074 is explicitly bacterial "
                "and capsule 000063 is a polymer layer around a cell, not "
                "hyphae around a plant root. Colony outline, cell shape, "
                "rhizosphere association and ecological symbiosis outcomes "
                "are not this architecture. The existing Hartig-net mantle "
                "mention is an evidence boundary, not an ungrounded node, "
                "synonym or parent-gap TODO requiring repair. Bare mantle "
                "and fungal sheath name structures, not formation phenotypes; "
                "no exact synonyms, xrefs or SSSOM equivalences are asserted. "
                "No organism-level disjointness or fixed thickness, color, "
                "host range or nutrient-transfer outcome is implied."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-root-mantle-mechanism-and-readout",
            "prompt": "Separate mantle morphogenesis from bulk expression and perturbation effects.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "A protein-resolved causal graph is deferred pending "
                "authority-verified proteins, sequence-to-culture links "
                "and inspection of the relevant perturbation images, not "
                "because mechanisms are absent. DOI:10.1128/AEM.01991-15 "
                "reports a thicker mantle in native ald1 overexpression; "
                "it does not establish an obligatory universal pathway. "
                "Its mte1 evidence is heterologous yeast growth rescue, "
                "not a native mantle-formation knockout. Keep increased "
                "thickness, first sheath formation, branching and plant "
                "responses separate. DOI:10.3390/microorganisms9122612 "
                "uses an EcM transcriptomic sample containing all fungal "
                "and mixed plant-fungal material within 0.5 cm of a root. "
                "Coexpression in that bulk sample is not mantle-specific "
                "localization or functional validation. The paper explicitly "
                "presents working models for future experimental tests."
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
            "Added fungal root mantle formation with three DOI-backed snippets "
            "and a culture-qualified S238N example. Ignored-and-hidden "
            "novelty and main/worktree/pending-PR checks support 000668, "
            "v544 and block 1062100-1062199; pending 000665-000667 "
            "reservations remain occupied. Kept root-external sheath "
            "architecture separate from Hartig nets, ecological outcomes "
            "and unverified protein mechanisms."
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
         "Root-external hyphal sheath; distinct from Hartig net and nutrient-transfer outcome.",
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
