"""Add fungal BAS formation without inferring absorption from morphology."""

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
SLUG = "fungal_branched_absorbing_structure_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v541/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000665"
METPO_ID = "METPO:1061800"
MORPHOGENESIS = "DOI:10.1046/j.1469-8137.1998.00199.x"
TRANSCRIPTOME = "DOI:10.1093/pcp/pcz122"
COLLECTION_URL = (
    "https://agriculture.canada.ca/en/agricultural-science-and-innovation/"
    "agriculture-and-agri-food-research-centres-and-collections/"
    "glomeromycota-vitro-collection-ginco/catalogue-arbuscular-mycorrhizal-"
    "fungi-strains-available-glomeromycetes-vitro-collection"
)
TIMESTAMP = "2026-10-07T14:21:36Z"
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
    "label": "fungal branched absorbing structure formation",
    "definition": (
        "A morphological phenotype in which an arbuscular mycorrhizal fungus "
        "forms localized, dichotomously branched groups of progressively finer "
        "hyphae, called branched absorbing structures, on its extraradical "
        "runner hyphae."
    ),
    "definition_source": MORPHOGENESIS,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MORPHOGENESIS,
            "snippet": (
                "small groups of dichotomous hyphae formed by the extraradical "
                "mycelium of arbuscular mycorrhizal (AM) fungi."
            ),
            "notes": (
                "Bago et al. (1998), New Phytologist 139:375-388; contiguous "
                "defining phrase from the Summary, read in the primary publisher "
                "PDF. The publisher's later online date is not the study year. "
                "Methods, Results and selected Discussion passages were read; "
                "actual figures were not inspected after screenshot/download "
                "failures. DAOM197198, named Glomus intraradices in this paper, "
                "formed BAS with non-transformed tomato cv. Vendor roots. "
                "Results distinguish progressively finer dichotomous branches "
                "from aborted short branches. Formation took about seven days "
                "under the tested conditions, not a universal lifespan. "
                "Some spore-associated BAS persisted and produced spores. "
                "Negative axenic and unsuccessful monoxenic cultures constrain "
                "these experiments, not every possible asymbiotic condition. "
                "The proposed absorptive role is not a direct uptake assay."
            ),
        },
        {
            "reference": TRANSCRIPTOME,
            "snippet": (
                "highly branched hyphae called branched absorbing structures "
                "(BAS) differentiate on the runner hyphae"
            ),
            "notes": (
                "Kameoka et al. (2019), PMID:31241164; Introduction clause "
                "before the Figure 1 citation, exact-matched in directly "
                "retrieved publisher HTML. Abstract, Introduction, Results, "
                "Discussion and Methods were read. Actual Figure 1C/G and its "
                "caption were inspected: six-week Rhizophagus irregularis "
                "DAOM197198 carrot hairy-root cocultures supply direct BAS "
                "morphology evidence. The RNA-seq comparison is not a direct "
                "uptake assay or causal perturbation. Runner-hypha and spore "
                "samples contained some BAS; negligible contamination influence "
                "was the authors' inference, not measured absence. Their "
                "historical no-direct-uptake-evidence statement is not a "
                "present-day knowledge claim. Remaining figure images and "
                "supplementary spreadsheet contents were not inspected."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:588596",
            "taxon_label": "Rhizophagus irregularis",
            "reference": TRANSCRIPTOME,
            "note": (
                "DAOM197198 from Premier Tech in six-week carrot hairy-root "
                "coculture, Methods and actual Figure 1C/G. The Canadian "
                f"GINCO catalogue {COLLECTION_URL} lists DAOMC197198, "
                "herbarium DAOM197198/181602, MUCL43194, Pont-Rouge in Quebec, "
                "a tree plantation, and collectors/isolators C. Plenchette and "
                "V. Furlan. These collection fields support field-isolate "
                "origin and are not a synthesized evidence snippet. NCBI "
                "Taxonomy confirms species 588596 and its strain 747089, "
                "Rhizophagus irregularis DAOM 181602=DAOM 197198. The "
                "transformed carrot host does not imply an engineered fungus. "
                "This is a culture-qualified observation, not independent "
                "reidentification or evidence for every strain and condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-bas-scope-and-hierarchy",
            "prompt": "Resolve a closer parent while preserving BAS morphology scope.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059. Branched shaped METPO:1000687 "
                "and filament shaped METPO:1000674 classify cell shape, not "
                "this differentiated extraradical architecture. Mycelial "
                "growth traitmech:000074 is explicitly bacterial. Fungal "
                "arbuscule formation traitmech:000664 concerns structures "
                "within living plant cells; the historical arbuscule-like "
                "structures name does not make BAS intracellular arbuscules. "
                "Appressorium formation traitmech:000659 concerns penetration "
                "structures, hyphal anastomosis traitmech:000605 fusion, and "
                "pseudohyphal growth traitmech:000653 budding-cell chains. "
                "Bago et al. also distinguish pre-infection fan-like structures "
                "and aborted short branches. No exact synonyms, structure "
                "xrefs, SSSOM equivalences or disjoint-organism claims are "
                "asserted. A closer morphology parent needs upstream review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-bas-formation-and-function",
            "prompt": "Separate formation from absorption, host dependence and mechanism.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Absorbing is the established structure name, not a required "
                "flux measurement. Do not infer mineral uptake, obligatory "
                "host contact, universal timing, inevitable degeneration or "
                "sporulation from morphology. Bago et al.'s host-dependence "
                "interpretation describes their tested media; later asymbiotic "
                "growth work DOI:10.1073/pnas.2006948117 remains a BAS-specific "
                "full-text/figure follow-up, not counted BAS evidence here. "
                "Transcriptional associations in Kameoka et al. do not identify "
                "a causal formation pathway. Their in vitro host system also "
                "does not establish expression patterns in soil-grown intact "
                "plants. A protein-resolved graph is deferred pending direct "
                "perturbation evidence and authority-verified protein anchors; "
                "it is not claimed biologically absent."
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
            "Added fungal BAS formation with two primary DOI-backed snippets "
            "and a culture/provenance-qualified DAOM197198 example. Ignored-"
            "and-hidden novelty and main/worktree/open-PR checks support local "
            "ID 000665 and v541 block 1061800-1061899. Kept morphology separate "
            "from uptake, host-dependence extrapolation and causal mechanisms."
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
         "Differentiated extraradical morphology; absorption is not inferred.",
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
