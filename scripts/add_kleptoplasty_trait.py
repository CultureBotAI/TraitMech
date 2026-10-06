"""Add prey-plastid retention without requiring photosynthetic function."""

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
TARGET = ROOT / "data/traits/physiology/kleptoplasty.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v505/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000629"
METPO_ID = "METPO:1058200"
DEFINITION = "DOI:10.1038/s41598-018-28455-1"
RAPAZA = "DOI:10.1073/pnas.2220100120"
FUNCTION = "DOI:10.1038/s41467-026-70516-x"
APHOTIC = "DOI:10.1111/1462-2920.14433"
PROVENANCE = "https://doi.org/10.1186/1471-2148-12-29"
COLLECTION = "https://mcc.nbrp.jp/strainList.do?strainId=4475&strainNumberEn=NIES-4477"
TIMESTAMP = "2026-10-05T22:48:00Z"
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
    "label": "kleptoplasty",
    "definition": (
        "A physiological phenotype in which a microbial organism selectively "
        "retains plastids acquired from algal prey after discarding or digesting "
        "other prey components."
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
                "Kleptoplasty is defined as the process in which a cell sequesters "
                "algal chloroplasts while discarding or digesting other algal components"
            ),
            "notes": (
                "PMID:29973634, PMC6031614. Direct Introduction definition, not "
                "an abstract quote or experimental replication. The Introduction "
                "also includes aphotic cases. Only the scientific Abstract and "
                "Introduction were read for this terminology claim; no canonical "
                "example or mechanism is imported from the paper's experiments."
            ),
        },
        {
            "reference": RAPAZA,
            "snippet": (
                "Rapaza viridis has only kleptoplasts derived from a specific "
                "strain of green alga, Tetraselmis sp., but no canonical plastids"
            ),
            "notes": (
                "PMID:36927158, PMC10041101. Contiguous scientific-abstract span, "
                "not the separate Significance section. Main text and actual "
                "Figures 1 and 3 were inspected: prey plastids persist after "
                "other material is expelled, and bicarbonate labeling supports "
                "photosynthetic carbon use. Plastid subdivision and partition "
                "do not establish plastid growth or biogenesis. Supplements were "
                "not visually audited. Predicted targeting sequences and "
                "transporters are not native protein-function validation."
            ),
        },
        {
            "reference": FUNCTION,
            "snippet": (
                "In the flagellate, Rapaza viridis, nuclear-encoded proteins "
                "support photosynthesis in transient, xenogeneic chloroplasts "
                "(kleptoplasts) acquired from the green alga Tetraselmis sp."
            ),
            "notes": (
                "PMID:41876518, PMC13013580. Scientific Abstract (Abs1), not "
                "the editorial summary (Abs2). Results, Discussion, relevant "
                "culture/perturbation/imaging/physiology Methods, actual Figures "
                "3-5 and Supplementary Figure 4 were inspected. Knockout and "
                "knockdown support host-protein contributions in this system. "
                "RbcS-like localization uses engineered HA tagging; Rca-like "
                "localization uses native-protein antibodies. This is a separate "
                "study of the same strain, not independent taxon replication."
            ),
        },
        {
            "reference": APHOTIC,
            "snippet": (
                "These results indicate that the photosynthetic pathways in "
                "N. labradorica are not functional."
            ),
            "notes": (
                "PMID:30277305. Direct Europe PMC scientific abstract, published "
                "online in 2018 and in the 2019 print issue. The authors call "
                "Nonionellina labradorica kleptoplastidic despite absent carbon "
                "fixation and oxygen production under their assayed conditions. "
                "This supports retaining a photosynthesis-independent definition, "
                "not universal functional absence. Full text and figures were "
                "not accessed; no canonical example or nitrogen/sulfur mechanism "
                "is imported. Host versus plastid assimilation remains unresolved."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1112050",
            "taxon_label": "Rapaza viridis",
            "reference": RAPAZA,
            "note": (
                "NIES-4477, fed Tetraselmis sp. NIES-4478, is the qualified "
                "example; do not generalize prey compatibility to every isolate. "
                "NCBI ESearch and EFetch resolve the species name and identifier "
                "on 2026-10-05. Natural tide-pool isolation at Pachena Beach "
                "in 2010 is documented in the original Methods at " + PROVENANCE + ". "
                "That paper's canonical-plastid interpretation was superseded "
                "by the 2023 study. Collection provenance at " + COLLECTION + " "
                "conflicts with the primary papers on the ATCC alias; retain "
                "NIES-4477 without silently equating the conflicting aliases."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "kleptoplasty-retention-and-hierarchy-scope",
            "prompt": "Keep plastid retention distinct from uptake and acquired photosynthesis.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "This is an organism-level physiological trait, not an organelle "
                "or sequence feature. Whole living algal endosymbionts are not "
                "equivalent to extracted plastids. Phagocytosis traitmech:000627 "
                "describes uptake; phagotrophy traitmech:000628 requires nutrient "
                "assimilation. Neither is exact. Phototrophic METPO:1000660 and "
                "mixotrophic METPO:1000652 prescribe energy/carbon use that the "
                "generic retention definition does not require. The trophic_type "
                "Falcon report attributes an acquired-photosynthesis framing to "
                "Schenone 2024; that narrower usage is preserved as research "
                "provenance, not generalized to all kleptoplasty. Retain phenotype "
                "METPO:1000059 pending a closer organelle-acquisition hierarchy. "
                "No fixed retention duration, plastid replication, complete "
                "nutritional dependence or loss of every other prey organelle is "
                "asserted. No unverified synonym or ontology xref is added."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "kleptoplasty-rapaza-strain-alias-conflict",
            "prompt": "Resolve the discordant ATCC alias with the collection.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "The NIES-4477 collection entry lists ATCC PRA-361, whereas "
                "the 2012 and 2023 primary Methods assign PRA-360 to Rapaza "
                "and PRA-361 to its Tetraselmis prey. The 2023 Methods document "
                "redeposition as NIES-4477 and NIES-4478. Use the NIES host "
                "identifier and primary provenance; do not silently reconcile "
                "the conflict or treat collection metadata as independent trait "
                "evidence. Collection URL is preserved in the canonical note."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "kleptoplasty-protein-import-mechanism",
            "prompt": "Ground native protein contributions without inventing an import apparatus.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The 2026 study supplies native functional perturbations beyond "
                "the 2023 sequence predictions, but this curation has not resolved "
                "taxon-paired protein accessions or a complete import mechanism. "
                "Predicted complexes, phase separation and pyrenoid remodeling "
                "must remain distinct from demonstrated localization and "
                "physiology. A targeting reporter does not identify a universal "
                "translocon. No protein-resolved causal graph is asserted."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added kleptoplasty with four DOI-backed snippets and a natural, "
            "strain-qualified Rapaza example. Ignored-and-hidden searches and "
            "pinned METPO review found no exact record. Reserved METPO:1058200 "
            "in v505. Kept plastid retention independent of photosynthesis, "
            "preserved the collection alias conflict and deferred unresolved "
            "protein groundings without inferring a causal graph."
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
         "|".join(["TraitMech:data/traits/physiology/kleptoplasty.yaml",
                   DEFINITION, RAPAZA, FUNCTION, APHOTIC]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Prey-plastid retention; photosynthesis and plastid replication are not required.",
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
