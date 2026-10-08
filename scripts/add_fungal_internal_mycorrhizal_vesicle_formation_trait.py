"""Add source-qualified fungal internal mycorrhizal vesicle formation."""

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
SLUG = "fungal_internal_mycorrhizal_vesicle_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v546/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000670"
METPO_ID = "METPO:1062300"
TERMINOLOGY = "https://www.mycorrhizas.info/vam.html"
ULTRASTRUCTURE = "DOI:10.1139/m75-258"
THALLUS = "DOI:10.3390/plants8060142"
TIMESTAMP = "2026-10-07T23:11:33Z"
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
    "label": "fungal internal mycorrhizal vesicle formation",
    "definition": (
        "A morphological phenotype in which a fungus forms lipid-storage "
        "hyphal swellings, called internal vesicles, within plant tissue "
        "during arbuscular mycorrhizal colonization."
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
                "Vesicles are hyphal swellings in the root cortex that contain "
                "lipids and cytoplasm."
            ),
            "notes": (
                "Mark Brundrett, Mycorrhizal Associations, version 2 (2008), "
                "section C.5 and glossary F, directly read. This author resource "
                "supports terminology, not independent experimental replication. "
                "Its root-context definition is broadened here to plant tissue "
                "using Kobae et al.'s primary thallus observations. Internal "
                "vesicles may be within or between host cells. The glossary "
                "separately calls extraradical auxiliary bodies external "
                "vesicles; those are outside this qualified scope. The "
                "resource also notes variable similarity to spores. Its "
                "images were not inspected; historic genus-level statements "
                "are not universal taxonomic absence assertions."
            ),
        },
        {
            "reference": ULTRASTRUCTURE,
            "snippet": (
                "Mature vesicles were engorged with lipid droplets, possessed "
                "a trilaminate wall and were also enclosed by host wall "
                "material and cytoplasm."
            ),
            "notes": (
                "Kinden and Brown (1975), PMID:172206; directly retrieved "
                "scientific abstract from Europe PMC. Electron microscopy "
                "of yellow-poplar mycorrhizal roots supports intracellular "
                "vesicles and lipid accumulation. Full text and actual "
                "micrographs were not inspected; the abstract does not name "
                "the fungus, so no taxon is inferred from historical MeSH. "
                "Trilaminate walls are this observation, not a universal "
                "definition. Nutrient release after degeneration is the "
                "authors' hypothesis, not measured transfer."
            ),
        },
        {
            "reference": THALLUS,
            "snippet": (
                "C. etunicatum and R. intraradices formed vesicles at 25 days "
                "post-sowing (dps)"
            ),
            "notes": (
                "Kobae et al. (2019), PMID:31151150, PMC6631804; Results 2.2 "
                "clause checked against the primary full-text XML and "
                "https://rakuno.repo.nii.ac.jp/record/6472/files/R-2020-321_kobae.pdf. "
                "Methods 3.1-3.3 and actual supplementary Figure S1 were "
                "inspected. The top two S1 panels separately label vesicles "
                "and arbuscules in young Marchantia paleacea thalli for "
                "MAFF520053 and MAFF520059, with 20-micrometer bars. WGA-HRP "
                "and DAB visualize fungal cell walls, not lipid chemistry. "
                "This is direct vesicle morphology, not an independent lipid "
                "assay or universal 25-day onset. The other panels' missing "
                "vesicle labels do not establish absence. The paper's "
                "DAOM197198 arbuscule-timing discrepancy concerns a separate "
                "culture and readout, not a resolved vesicle onset."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:937382",
            "taxon_label": "Entrophospora etunicata",
            "reference": THALLUS,
            "note": (
                "MAFF520053 (H1-1), reported as Claroideoglomus etunicatum, "
                "forms vesicles in Marchantia paleacea thalli (Results 2.2; "
                "actual Figure S1). Methods 3.2 uses 1 g MAFF inoculum below "
                "approximately 100 gemmae per pot, at 26 C with 16 h light/day; "
                "Results reports 25 days post-sowing. The directly checked "
                "NARO collection record "
                "https://www.gene.affrc.go.jp/databases-micro_search_detail_en.php?maff=520053 "
                "lists soybean-field soil, Tokyo, October 1987 and H. Hirata "
                "as separate fields, and deposition as Glomus etunicatum. "
                "These are provenance, not a composite quote or independent "
                "trait evidence. NCBI Taxonomy resolves 937382 to Entrophospora "
                "etunicata with Claroideoglomus etunicatum as a homotypic "
                "synonym. Name correspondence is not reidentification. "
                "The directly read Table 1 and Results of "
                "DOI:10.1264/jsme2.ME25040 retain H1-1/520053; primer-dependent "
                "ASV resolution does not independently prove every culture's "
                "identity or a vesicle phenotype. Its figures and supplements "
                "were not inspected. The example is culture- and condition-"
                "qualified, not an assertion about all strains."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-internal-mycorrhizal-vesicle-scope",
            "prompt": "Resolve the closer parent and vesicle-versus-spore terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use active phenotype METPO:1000059 below quality METPO:1000188; "
                "mycorrhization METPO:1000198 is obsolete. Internal means "
                "within plant tissue, not necessarily within host cells and "
                "not free in host cytoplasm. Root-only scope excludes the "
                "direct thallus observations. Gas vesicles traitmech:000070, "
                "extracellular membrane vesicles and intracellular trafficking "
                "vesicles are not these hyphal swellings. Arbuscule formation "
                "traitmech:000664 is a different architecture. Brundrett's "
                "auxiliary-body usage motivates the internal qualifier; "
                "fine-endophyte vesicle-like swellings are not automatically "
                "equivalent. Fungal chlamydospore formation traitmech:000658 "
                "does not cover every storage swelling. Variable historical "
                "spore terminology remains unresolved; no universal "
                "disjointness, subclass relation, exact synonyms, xrefs or "
                "SSSOM equivalences are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-internal-mycorrhizal-vesicle-readouts",
            "prompt": "Separate vesicle formation, storage and causal mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Require a vesicle-specific morphological observation; pooled "
                "spores-and-vesicles or colonized-root-length percentages "
                "must not become vesicle counts or fungal-cell fractions. "
                "Neither these images nor the lipid-storage terminology "
                "establish universal lifespan, wall layers, infectivity, "
                "nutrient transfer, reciprocal benefit or developmental "
                "timing. Host signaling mutants and lipid-transfer assays "
                "are not fungal gene perturbations. A protein-resolved "
                "formation graph is deferred pending direct causal evidence "
                "and authority-verified fungal protein examples; it is not "
                "claimed biologically absent."
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
            "Added fungal internal mycorrhizal vesicle formation with two "
            "primary DOI-backed sources, attributed terminology, three "
            "verbatim snippets and a culture-qualified example. Ignored-and-"
            "hidden novelty and main/worktree/complete-open-PR reservation "
            "checks support 000670 and v546 block 1062300-1062399. Kept "
            "thallus scope, storage versus formation readouts and mechanism "
            "limits explicit; existing records unchanged."
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
         "Internal to plant tissue, including thalli; not membrane vesicles or auxiliary bodies.",
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
