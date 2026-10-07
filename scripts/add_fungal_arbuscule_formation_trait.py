"""Add fungal arbuscule formation and link its unresolved haustorium boundary."""

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
SLUG = "fungal_arbuscule_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
HAUSTORIUM_PATH = ROOT / "data/traits/morphology/microbial_haustorium_formation.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v540/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000664"
METPO_ID = "METPO:1061700"
ROOT_STUDY = "DOI:10.1104/pp.109.141879"
THALLUS_STUDY = "DOI:10.3390/plants8060142"
TIMESTAMP = "2026-10-07T13:21:20Z"
HAUSTORIUM_PREIMAGE = "8910bf33ed3491f501a14277fccbc308242e436ae03739049ea135249dce8d8e"
BOUNDARY_ID = "microbial-haustorium-scope-and-hierarchy"
BOUNDARY_LINK = (
    " Fungal arbuscule formation now has its own source-bounded phenotype "
    "record, traitmech:000664. This resolves the missing record reference, "
    "not the umbrella hierarchy question; no subclass or disjointness "
    "relationship between these two phenotypes is asserted."
)
LINK_CHANGES = (
    "Linked the existing arbuscule boundary discussion to traitmech:000664; "
    "retained OPEN status and deferred subclass, equivalence and disjointness. "
    "No haustorium identity, evidence, examples or parent changed."
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
    "label": "fungal arbuscule formation",
    "definition": (
        "A morphological phenotype in which a fungus forms highly branched "
        "hyphal structures, called arbuscules, within living plant cells "
        "during arbuscular mycorrhizal symbiosis."
    ),
    "definition_source": THALLUS_STUDY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": ROOT_STUDY,
            "snippet": (
                "In the arbuscular mycorrhizal symbiosis, the fungal symbiont "
                "colonizes root cortical cells, where it establishes "
                "differentiated hyphae called arbuscules."
            ),
            "notes": (
                "Pumplin and Harrison (2009), PMID:19692536, PMC2754618; "
                "scientific-abstract sentence checked against Europe PMC and "
                "https://academic.oup.com/plphys/article/151/2/809/6108581. "
                "Main text, Figures 1-7 and supplementary Figures S1-S9 were "
                "inspected; Figure 7 is a model. The supplementary movie was "
                "not viewed. Glomus versiforme colonized transgenic Medicago "
                "truncatula A17 roots. Host fluorescent markers distinguish "
                "periarbuscular membrane domains; they are not fungal protein "
                "anchors or nutrient-flux measurements. The host-derived "
                "membrane separates fungal branches from host cytoplasm. "
                "Fungal isolate provenance was not established, so this "
                "experiment is not a natural canonical example."
            ),
        },
        {
            "reference": THALLUS_STUDY,
            "snippet": (
                "All AMF strains formed arbuscules in the parenchyma cells "
                "of the mycothalli"
            ),
            "notes": (
                "Kobae et al. (2019), PMID:31151150, PMC6631804; Results 2.2 "
                "clause. Primary text and Figures 1-4 on pages 1-11 of "
                "https://rakuno.repo.nii.ac.jp/record/6472/files/R-2020-321_kobae.pdf "
                "and all four supplementary pages were inspected. Liverwort "
                "Marchantia paleacea thallus observations support plant-cell, "
                "not root-only, scope. Methods 3.2 and Figure S1 identify "
                "cultures separately from unidentified field-root trapping. "
                "For DAOM197198, Results 2.2 reports arbuscules at 18 dps "
                "and none until 14 dps; S2A instead describes rhizoid-only "
                "hyphae at 18 dps and S2B arbuscules at 28 dps. Onset remains "
                "unresolved. Pigmentation alone is insufficient. Figure 4C "
                "shows root arbuscules, although Results points to 4B and "
                "uses dps instead of the caption's dpi. Figure 3 and Methods "
                "3.6 disagree on phylogenetic method; no independent fungal "
                "species assignment from mixed rDNA is asserted."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:937382",
            "taxon_label": "Entrophospora etunicata",
            "reference": THALLUS_STUDY,
            "note": (
                "MAFF520053 (H1-1), reported as Claroideoglomus etunicatum "
                "in Methods 3.2 and actual Figure S1, forms arbuscules in "
                "Marchantia paleacea thallus cells. NARO's collection record "
                "https://www.gene.affrc.go.jp/databases-micro_search_detail_en.php?maff=520053 "
                "lists soybean-field soil, Tokyo, October 1987, H. Hirata; "
                "it was deposited as Glomus etunicatum. These separate fields "
                "support this culture's field-isolate origin, not a trait "
                "evidence snippet. NCBI Taxonomy resolves species 937382 to "
                "Entrophospora etunicata, with Claroideoglomus etunicatum as "
                "a homotypic synonym; name correspondence is not independent "
                "reidentification of the culture."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-arbuscule-scope-and-hierarchy",
            "prompt": "Resolve the phenotype parent and attributed haustorium umbrella.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use active phenotype METPO:1000059; METPO:1000198 "
                "mycorrhization is obsolete. Mutualism traitmech:000041 "
                "requires reciprocal benefit, which formation alone does "
                "not establish. Direct QuickGO checks identify GO:0085041 "
                "arbuscule as a cellular component below GO:0085035 "
                "haustorium. This attributed umbrella classification is "
                "not silently rejected: microbial haustorium formation "
                "traitmech:000663 and this formation phenotype are not "
                "asserted equivalent, disjoint or in a subclass relation. "
                "GO's root-cortex wording is narrower than the liverwort "
                "observations, and a structure is not an organism-level "
                "phenotype. No exact xrefs, synonyms or SSSOM mappings are "
                "asserted. Plant cells includes thallus cells; within-cell "
                "location does not mean free in host cytoplasm."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-arbuscule-formation-and-function",
            "prompt": "Separate formation, timing and nutrient-exchange mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Do not infer nutrient flux, obligatory benefit, universal "
                "onset or lifespan from these morphology observations. "
                "Keep the 2019 main-text/supplement timing discrepancy open. "
                "The 2009 host membrane markers do not identify a fungal "
                "formation pathway. A protein-resolved causal graph needs "
                "direct perturbation evidence and authority-verified "
                "protein examples; it is deferred, not claimed absent. "
                "Extraradical branching alone does not satisfy this "
                "intracellular morphology definition."
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
            "Added fungal arbuscule formation with two primary DOI citations, "
            "verbatim snippets and a culture-qualified fungal example. "
            "Ignored-and-hidden novelty and main/worktree/open-PR reservation "
            "checks support local ID 000664 and v540 block 1061700-1061799. "
            "Kept host markers, timing disagreements and ontology scope "
            "explicit; protein-level mechanism deferred."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def digest(record: dict) -> str:
    data = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(data.encode()).hexdigest()


def link_event() -> dict:
    return record_curation_event(
        {}, curator="codex", action="LINK_ARBUSCULE_DISCUSSION",
        changes=LINK_CHANGES, llm_assisted=True, timestamp=TIMESTAMP,
    )


def build_haustorium(existing: dict) -> dict:
    # Strip only the exact replay suffix/event, then check the entire preimage.
    before = copy.deepcopy(existing)
    if isinstance(before, dict) and before.get("curation_history", [])[-1:] == [link_event()]:
        before["curation_history"].pop()
        for discussion in before.get("discussions", []):
            if discussion.get("discussion_id") == BOUNDARY_ID:
                rationale = discussion.get("rationale", "")
                if not rationale.endswith(BOUNDARY_LINK):
                    raise SystemExit("Existing haustorium differs from reviewed result")
                discussion["rationale"] = rationale[:-len(BOUNDARY_LINK)]
    if not isinstance(before, dict) or digest(before) != HAUSTORIUM_PREIMAGE:
        raise SystemExit("Existing haustorium differs from reviewed preimage")
    record = copy.deepcopy(before)
    discussion, = [d for d in record["discussions"] if d["discussion_id"] == BOUNDARY_ID]
    discussion["rationale"] += BOUNDARY_LINK
    record_curation_event(
        record, curator="codex", action="LINK_ARBUSCULE_DISCUSSION",
        changes=LINK_CHANGES, llm_assisted=True, timestamp=TIMESTAMP,
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
         "Fungal formation phenotype in living plant cells, including liverwort thalli.",
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
    haustorium = build_haustorium(yaml.safe_load(HAUSTORIUM_PATH.read_text()))
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(haustorium, Path(tmp) / HAUSTORIUM_PATH.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(haustorium, HAUSTORIUM_PATH)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
