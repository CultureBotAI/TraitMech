"""Add fungal chlamydospore formation without an assumed dormancy function."""

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
SLUG = "fungal_chlamydospore_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v534/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000658"
METPO_ID = "METPO:1061100"
MORPHOLOGY = "DOI:10.1038/s41467-020-20010-9"
ORIGINAL_ISOLATES = "DOI:10.1099/13500872-141-7-1507"
INDUCTION = "DOI:10.3389/fmicb.2016.01697"
VIABILITY = "DOI:10.1111/j.1567-1364.2009.00533.x"
BOUNDARY = "https://research.fs.usda.gov/treesearch/30277"
CONIDIAL_ROUTE = "DOI:10.1007/s10886-012-0171-1"
TIMESTAMP = "2026-10-07T04:23:14Z"
CORRECTION_TIMESTAMP = "2026-10-07T04:34:28Z"
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
# Preserve the exact pre-fix draft for a guarded, provenance-preserving migration.
INITIAL_RECORD = {
    "identifier": IDENTIFIER,
    "label": "fungal chlamydospore formation",
    "definition": (
        "A morphological phenotype in which a fungus forms enlarged, thick-walled "
        "cells called chlamydospores within hyphae or at their tips."
    ),
    "definition_source": MORPHOLOGY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MORPHOLOGY,
            "snippet": (
                "Chlamydospores are enlarged thick-walled cells produced within "
                "hyphae or at hyphal tips"
            ),
            "notes": (
                "Hernandez-Cervantes et al. (2020), PMID:33277479, PMC7718266, "
                "Introduction; this contiguous clause supplies morphological "
                "terminology, not independent experimental replication across "
                "all fungi. Abstract, Introduction and selected Methods were "
                "read directly. Mechanistic panels and supplementary strain "
                "tables were not inspected, so no universal Rme1 dependence "
                "or protein-resolved causal graph is asserted. The definition "
                "does not impose a survival function."
            ),
        },
        {
            "reference": ORIGINAL_ISOLATES,
            "snippet": (
                "These organisms were germ-tube-positive and produced abundant "
                "chlamydospores which were frequently arranged in triplets or "
                "in contiguous pairs."
            ),
            "notes": (
                "Sullivan et al. (1995), PMID:7551019, original Candida "
                "dubliniensis description; scientific abstract retrieved "
                "directly from Europe PMC. These organisms refers to the "
                "recovered oral clinical isolates. This is primary phenotype "
                "and natural-isolate provenance at cohort level, not evidence "
                "that chlamydospores were observed in patient tissue. Full "
                "Methods and strain tables were not inspected; no named "
                "culture, universal arrangement or response of every strain "
                "is inferred."
            ),
        },
        {
            "reference": INDUCTION,
            "snippet": (
                "Both species produced typically high amounts of chlamydospores "
                "on rice and CM agar (chlamydospore index [CI] 3)."
            ),
            "notes": (
                "Bottcher et al. (2016), PMID:27833594, PMC5081361, Figure 1 "
                "caption. Actual Figure 1 micrographs, Methods and Tables 1-2 "
                "were inspected. The strains are C. albicans SC5314 and "
                "C. dubliniensis Wu284, rendered with an umlaut in the source; "
                "CM means corn meal. Cultures were examined after seven days "
                "at 27 C in darkness. CI is an ordinal 0-3 score, not a cell "
                "percentage. Nutrient effects differ by strain and medium; "
                "no universal starvation or darkness requirement is inferred. "
                "Independent provenance of these laboratory strains was not "
                "checked, so they are not the canonical example."
            ),
        },
        {
            "reference": VIABILITY,
            "snippet": (
                "Mycelium-attached and purified chlamydospores rapidly lost "
                "their viability in water and when subjected to dry stress"
            ),
            "notes": (
                "Citiulo et al. (2009), PMID:19538507, scientific abstract "
                "retrieved directly from Europe PMC and checked against "
                "publisher text. The complete result clause is quoted before "
                "the authors' interpretation about long-term storage. It "
                "argues against assuming durable dormancy for these Candida "
                "cells, not against survival roles in every fungus. The "
                "publisher Introduction and selected Methods were also read; "
                "the Introduction calls Candida budding blastic conidiogenesis "
                "and explains chlamydoconidia terminology. Formation is kept "
                "separate from subsequent germination and viability."
            ),
        },
        {
            "reference": BOUNDARY,
            "snippet": (
                "Cell walls of mature P. ramorum chlamydospores are thicker "
                "than reported for other Phytophthora species, although "
                "thin-walled chlamydospores are also formed."
            ),
            "notes": (
                "Smith and Hansen (2008), USDA proceedings report, pp. 451-454; "
                "directly retrieved repository abstract. The repository labels "
                "it Informally Refereed. NCBI Taxonomy confirms Phytophthora "
                "ramorum is an oomycete in Stramenopiles, not Fungi. This is "
                "terminology-boundary evidence, not a fungal observation: "
                "the fungal qualifier avoids silently including the report's "
                "thin-walled structures in a thick-walled fungal definition. "
                "Full report and figures were not inspected; no canonical "
                "oomycete or universal wall-thickness cutoff is asserted."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:42374",
            "taxon_label": "Candida dubliniensis",
            "reference": ORIGINAL_ISOLATES,
            "note": (
                "Species-level example from naturally recovered oral clinical "
                "isolates in the original 1995 description. The primary "
                "scientific abstract at https://doi.org/10.1099/13500872-141-7-1507 "
                "reports abundant chlamydospore production. This supports "
                "cohort-level isolate provenance, not a particular named "
                "laboratory culture, an inferred wild-type or GMO status, "
                "or chlamydospores in patient tissue. Full strain tables and "
                "Methods were not inspected; the observation is not assigned "
                "to CD36 or to every strain or condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-chlamydospore-scope-and-hierarchy",
            "prompt": "Resolve conidiation, dormancy and process-ontology mappings.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059. Sporulation METPO:1000870 "
                "and spore forming METPO:1000871 explicitly concern endospores. "
                "Citiulo et al. (2009) call Candida chlamydospore budding "
                "blastic conidiogenesis; that source-attributed usage does not "
                "settle whether this broader fungal class should be below "
                "fungal conidiation traitmech:000657. Do not equate it with "
                "ordinary pseudohyphal growth or any hyphal swelling. Closed "
                "upstream issue https://github.com/berkeleybop/metpo/issues/67 "
                "suggested chlamydospores under resting spores; the Candida "
                "viability evidence does not support that as a universal "
                "function. GO:0001410 was resolved through QuickGO: it is a "
                "biological process and its survival/endogenous-formation "
                "wording also needs scope review. Leave exact synonyms and "
                "xrefs unset rather than asserting equivalence. The four "
                "obsolete METPO chlamydospore terms are material classes, "
                "not active organismal phenotypes."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-chlamydospore-function-and-mechanism",
            "prompt": "Separate morphological identification from survival and regulation.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wall thickening alone does not establish long-term survival, "
                "dormancy, infectivity or a dispersal function. Preserve "
                "species-, strain-, age- and medium-specific endpoints. "
                "Do not require one arrangement, nucleus count, nutrient "
                "trigger or illumination regime. The USDA Phytophthora "
                "report documents a nonfungal terminology boundary, not "
                "additional fungal replication. Formation and later "
                "germination are different observations. A causal graph is "
                "deferred pending reconciliation of primary perturbations "
                "and supplementary strain identities with natural-host "
                "provenance and taxon-paired protein accessions. Gene "
                "possession alone is not a chlamydospore phenotype."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_initial_record() -> dict:
    record = copy.deepcopy(INITIAL_RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal chlamydospore formation with five directly checked "
            "snippets, a cohort-qualified Candida dubliniensis example and "
            "explicit terminology, hierarchy and function limits. Ignored-and-hidden "
            "searches found no exact live record. Reserved METPO:1061100 in "
            "v534; existing records unchanged and causal graph deferred."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_record() -> dict:
    record = build_initial_record()
    record["definition"] = (
        "A morphological phenotype in which a fungus forms enlarged, "
        "thick-walled cells called chlamydospores."
    )
    record["evidence"].append({
        "reference": CONIDIAL_ROUTE,
        "snippet": (
            "two species of Fusarium formed chlamydospores from hyphae, "
            "germ tubes, or inside the conidia within 2 days."
        ),
        "notes": (
            "Li et al. (2012), PMID:22932866, scientific abstract retrieved "
            "directly from Europe PMC. This result concerns sub-MIC FA17 "
            "fengycin treatment of two Fusarium species, not untreated "
            "formation in every fungus. It establishes a conidial route "
            "excluded by the initial hypha-only draft definition (#1772). "
            "The abstract separately calls structures in 17 other fungi "
            "chlamydospore-like; those are not promoted to equivalent "
            "phenotypes. Full Methods, figures and strain provenance were "
            "not inspected, so no additional canonical strain or causal "
            "chemical mapping is asserted."
        ),
    })
    record["discussions"][1]["rationale"] += (
        " Li et al. (2012), PMID:22932866, report formation inside conidia "
        "as well as from hyphae and germ tubes under the tested treatment. "
        "Issue #1772 corrected the initial hypha-only restriction; retain "
        "formation-site neutrality and do not promote the separately "
        "reported chlamydospore-like structures to confirmed chlamydospores."
    )
    record_curation_event(
        record, curator="codex", action="REVISED_DEFINITION",
        changes=(
            "Addressed #1772: removed the hypha-only formation-site "
            "restriction, added the primary Fusarium conidial-route "
            "counterexample and retained treatment and source-access "
            "limits. Preserve the initial curation event and canonical example."
        ),
        llm_assisted=True, timestamp=CORRECTION_TIMESTAMP,
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
         "Fungal morphology; no universal dormancy or stress-resistance requirement.",
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
    initial = build_initial_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (initial, record):
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() not in (proposal_tsv(initial), proposal):
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
