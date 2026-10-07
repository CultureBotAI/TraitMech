"""Add prey-content aspiration as an organismal feeding phenotype."""

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
TARGET = ROOT / "data/traits/physiology/myzocytosis.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v507/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000631"
METPO_ID = "METPO:1058400"
DEFINITION = "DOI:10.3390/microorganisms11081945"
FEEDING = "DOI:10.1111/jeu.13050"
PREY_SCOPE = "DOI:10.1038/ismej.2012.29"
PROVENANCE = "https://doi.org/10.1111/jeu.13050"
TIMESTAMP = "2026-10-06T00:46:04Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "myzocytosis",
    "definition": (
        "A physiological phenotype in which a microbial organism feeds by "
        "aspirating prey cell contents through a localized feeding connection "
        "rather than engulfing the prey whole."
    ),
    "definition_source": DEFINITION,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION,
            "snippet": (
                "Colpodella sp. (ATCC 50594) obtain nutrients by preying on "
                "Parabodo caudatus using myzocytosis."
            ),
            "notes": (
                "PMID:37630505, PMC10458597. Direct scientific Abstract quote. "
                "Main text and actual Figures 7-9 were inspected; Figures 1-6 "
                "were not visually audited. Introduction and Conclusions "
                "describe aspiration through a feeding channel. Fixed-cell "
                "TEM supports prey-membrane uptake at the contact, not direct "
                "piercing by the pseudoconoid. Unattached nanoparticle uptake "
                "is separate endocytosis, not proof of myzocytosis. Intact prey "
                "organelles in food vacuoles do not establish functional "
                "organelle retention. Posterior vacuole position and "
                "encystation are not universal requirements. The mixed "
                "culture does not resolve a complete native protein mechanism."
            ),
        },
        {
            "reference": FEEDING,
            "snippet": (
                "cytoplasm contents were transferred through the peduncle "
                "to the dinoflagellate."
            ),
            "notes": (
                "PMID:39019843, PMC11603288. Direct Nutrition and feeding "
                "behavior Results passage, not an abstract quote. Scientific "
                "Abstract, culture and fluorescence Methods, feeding Results "
                "and Discussion, and actual supplementary Figure S6 with its "
                "caption were inspected. S6 identifies imaged SPMC98; the "
                "molecular-data isolate SPMC100 is different. Panel D shows "
                "deformed cryptophyte material passing through the peduncle; "
                "attachment in panel E alone is not ingestion. The organism "
                "can also use conventional phagocytosis. Trichocyst discharge "
                "may be a fixation artifact, not a demonstrated prey-capture "
                "mechanism. Other supplementary figures, molecular datasets "
                "and movies were not audited."
            ),
        },
        {
            "reference": PREY_SCOPE,
            "snippet": (
                "parts are sucked out by a microtubule supported feeding "
                "tube or peduncle (myzocytosis)"
            ),
            "notes": (
                "PMID:22513533, PMC3446796. Direct Introduction terminology "
                "span, not an abstract quote or independent naming experiment. "
                "Main text and actual Figure 2 were inspected; other figures "
                "and supplementary movies were not visually audited. Results "
                "report Karlodinium armiger tube feeding on copepods and "
                "polychaete larvae, so the prey need not be unicellular. "
                "Nematode feeding was not directly observed. Abstract and "
                "later passages call the strain K-0688, whereas initial "
                "Methods and Table 1 say K-0668; no canonical strain is "
                "assigned from this conflicting record. Proposed toxin and "
                "chemotaxis explanations are not molecular demonstrations."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:160603",
            "taxon_label": "Oxytoxum lohmannii",
            "reference": FEEDING,
            "note": (
                "Qualified example: imaged SPMC98 feeding on cryptophyte "
                "prey, not molecular-data isolate SPMC100. Maintenance "
                "cultures Methods at " + PROVENANCE + " document natural "
                "isolation from the Salish Sea near Anacortes, Washington, "
                "in 1993, originally identified as Amphidinium longum. "
                "SPMC98 was lost in 2004. Actual supplementary Figure S6 "
                "names this strain and shows prey material passing through "
                "the peduncle. Feeding mode is prey-dependent; this is not "
                "a claim about all isolates or exclusive myzocytosis. NCBI "
                "ESearch and EFetch resolved the species and its Amphidinium "
                "longum synonym on 2026-10-06."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "myzocytosis-feeding-scope-and-parent",
            "prompt": "Reconcile feeding-mode terminology with operational trait boundaries.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "This is an organismal feeding phenotype, not a peduncle, "
                "pseudoconoid or sequence feature. The 2023 Discussion calls "
                "myzocytosis a form of apical phagotrophy and endocytosis "
                "while arguing against phagocytosis and trogocytosis in its "
                "studied system. The 2012 Introduction uses phagocytise for "
                "feeding-tube uptake; the 2024 study contrasts myzocytosis "
                "with conventional whole-prey phagocytosis. Those usages "
                "are not silently treated as identical. Local phagocytosis "
                "traitmech:000627 requires particle enclosure and "
                "internalization; phagotrophy traitmech:000628 requires "
                "particulate ingestion and nutrient assimilation. Retain "
                "phenotype METPO:1000059 pending a closer feeding-mode "
                "hierarchy rather than assert unsupported universal "
                "subtyping. Mere attachment, free-particle uptake, "
                "extracellular digestion or an apparatus-like sequence "
                "does not establish prey-content aspiration. A microbe may "
                "use several feeding modes; these possession traits are "
                "not declared disjoint. No unverified synonym or xref is "
                "asserted. Prey death, mechanical piercing and a particular "
                "vacuole position are not definition requirements."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "myzocytosis-native-feeding-mechanism",
            "prompt": "Separate observed aspiration from inferred apparatus and protein functions.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Fixed-cell contact ultrastructure does not establish every "
                "step by continuous observation. The 2023 paper cites "
                "earlier cytochalasin experiments; those experiments were "
                "not independently audited here. Its CellMask staining "
                "description alone is not accepted as proof of a specific "
                "actin mechanism. The 2024 molecular data are from a "
                "different isolate than the feeding micrographs, and "
                "trichocyst-mediated capture remains uncertain. The 2012 "
                "study did not measure the proposed toxin. Obtain "
                "taxon-paired functional evidence before adding protein "
                "accessions or a causal graph. Ancestral feeding and "
                "apicomplexan invasion similarities are hypotheses, not "
                "proof of one universal apparatus or molecular mechanism."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added myzocytosis with three DOI-backed snippets and a natural, "
            "strain-qualified Oxytoxum example. Ignored-and-hidden searches "
            "and pinned METPO review found no exact record. Reserved "
            "METPO:1058400 in v507. Distinguished prey-content aspiration "
            "from whole-prey engulfment, free-particle uptake and sequence "
            "interpretation; retained hierarchy and mechanism gaps."
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
         "|".join(["TraitMech:data/traits/physiology/myzocytosis.yaml",
                   DEFINITION, FEEDING, PREY_SCOPE]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Prey-content aspiration; not universal piercing or whole-prey engulfment.",
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
    if any(parent.get(k) != v for k, v in PARENT.items()):
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
