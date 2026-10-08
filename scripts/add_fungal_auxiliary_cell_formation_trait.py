"""Add source-qualified fungal auxiliary cell formation."""

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
SLUG = "fungal_auxiliary_cell_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v547/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000671"
METPO_ID = "METPO:1062400"
TERMINOLOGY = "https://www.mycorrhizas.info/vam.html"
GERM_TUBES = "DOI:10.1111/j.1469-8137.2007.02345.x"
ROOT_CULTURE = "DOI:10.1017/S0953756203008761"
TIMESTAMP = "2026-10-08T02:02:02Z"
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
    "label": "fungal auxiliary cell formation",
    "definition": (
        "A morphological phenotype in which an arbuscular mycorrhizal fungus "
        "forms auxiliary cells, typically clustered hyphal swellings, on "
        "mycelium outside plant tissue."
    ),
    "definition_source": TERMINOLOGY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "Hyphae of Scutellospora and Gigaspora species produce clustered "
                "swellings with spines or knobs called auxiliary cells."
            ),
            "notes": (
                "Mark Brundrett, Mycorrhizal Associations, version 2 (2008), "
                "C.1 and glossary F, directly read. Terminology support, not "
                "independent experimental replication. The glossary describes "
                "external hyphae and says ornamentation is frequent, not "
                "obligatory. Its unnamed Scutellospora soil-hyphae micrograph "
                "and separate line illustration were actually viewed; neither "
                "establishes a named culture example. Historical auxiliary-body, "
                "external-vesicle and accessory-body labels name structures, "
                "not automatically exact organismal-trait synonyms."
            ),
        },
        {
            "reference": GERM_TUBES,
            "snippet": "In G.\u00a0margarita, auxiliary cells were formed on germ tubes",
            "notes": (
                "Kuga et al. (2008), PMID:18194149; Results clause before "
                "Elemental analyses, directly read in publisher full text. "
                "Methods identify MAFF520054. The Results point to Figure "
                "3a/i; captions were read but actual paper images and "
                "supplements were not inspected. The HTML temperature glyph "
                "renders as 25\u00d7C and remains unresolved rather than normalized "
                "to degrees. Organelle localization and nonspecific DAPI "
                "fluorescence do not establish a formation mechanism or a "
                "universal storage function."
            ),
        },
        {
            "reference": ROOT_CULTURE,
            "snippet": (
                "Isolated auxiliary cells were shown to exhibit hyphal "
                "re-growth, but not root colonization, either in situ or in vitro."
            ),
            "notes": (
                "Declerck et al. (2004), PMID:15035509; scientific abstract "
                "retrieved directly from Europe PMC. It follows extraradical "
                "mycelium, auxiliary cells and spores of Scutellospora "
                "reticulata in root-organ culture. Ri T-DNA transformation "
                "concerns carrot roots, not an engineered fungus. Regrowth "
                "without root colonization is conditional on the tested "
                "assays, not universal noninfectivity. Resource reallocation "
                "is the authors' interpretation, not a direct flux measurement. "
                "Full paper, images and isolate provenance were not inspected; "
                "no additional canonical culture is assigned."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:4874",
            "taxon_label": "Gigaspora margarita",
            "reference": GERM_TUBES,
            "note": (
                "MAFF520054, Results and Fungal materials of Kuga et al. "
                "(2008): auxiliary cells on germ tubes. Methods describe "
                "white-clover propagation, membranes over 1% soil agar, "
                "10 days in darkness and a separate nutrient-agar staining "
                "treatment; cultivation duration is not formation onset. "
                "The temperature glyph and actual Figure 3 images remain "
                "unverified. The directly retrieved NARO record "
                "https://www.gene.affrc.go.jp/databases-micro_search_detail_en.php?maff=520054 "
                "lists designation C, soybean-field soil, Saitama Japan, "
                "isolator S. Ban and depositor/identifier M. Saito as separate "
                "fields. These establish field-isolate provenance, not a "
                "composite quote or independent trait evidence. NCBI Taxonomy "
                "resolves species 4874, not culture reidentification. Table 1 "
                "of DOI:10.1264/jsme2.ME25040 retains C/520054; primer-dependent "
                "ASVs, including above-genus assignments, are not culture "
                "counts or proof of contamination, identity or this phenotype. "
                "Its figures and supplements were not inspected. This example "
                "does not assert the response of all strains or conditions."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-auxiliary-cell-scope",
            "prompt": "Resolve a closer parent and structure-versus-trait terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use active phenotype METPO:1000059 below quality METPO:1000188; "
                "mycorrhization METPO:1000198 is obsolete. Arbuscular "
                "mycorrhizal identifies the fungal context, not a requirement "
                "for current host contact: the germ-tube observation is "
                "outside plant tissue. Internal mycorrhizal vesicle formation "
                "traitmech:000670, arbuscule formation traitmech:000664 and "
                "branched absorbing structure formation traitmech:000665 "
                "denote different architectures or locations. Not every "
                "hyphal swelling is an auxiliary cell; neither fungal "
                "chlamydospore formation traitmech:000658 nor membrane-vesicle "
                "formation is an exact substitute. External-vesicle and "
                "accessory-body usages remain attributed structure labels; "
                "no exact synonyms, xrefs, SSSOM equivalents or disjoint "
                "organism-level phenotypes are asserted. Typical clustering "
                "does not impose a minimum count on every observation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-auxiliary-cell-function",
            "prompt": "Separate auxiliary-cell morphology, counting and function.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Keep individual compartments, clusters, hyphal biomass and "
                "spore counts distinct. Morphology or lipid content does not "
                "establish universal nutrient transfer, propagule function, "
                "lifespan, wall-layer number or obligate host dependence. "
                "Hyphal regrowth and root colonization are different endpoints. "
                "A protein-resolved formation graph is deferred pending "
                "direct causal perturbations and authority-verified fungal "
                "protein examples; it is not claimed biologically absent. "
                "Host transformation and sequence-profile assignments alone "
                "do not demonstrate the fungal formation mechanism."
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
            "Added fungal auxiliary cell formation with two primary DOI "
            "sources, attributed morphology terminology, three verbatim "
            "snippets and a culture-qualified MAFF520054 example. Ignored-and-"
            "hidden novelty and current-main/worktree/complete-open-PR "
            "reservation checks support 000671 and v547 block 1062400-1062499. "
            "Kept external swellings separate from internal vesicles, BAS, "
            "spores, function and protein mechanism; existing records unchanged."
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
         "External auxiliary swellings; morphology does not establish storage or propagule function.",
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
