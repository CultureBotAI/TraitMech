"""Add diauxic growth through the guarded validated writer."""

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
SLUG = "diauxic_growth"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v580/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000704"
METPO_ID = "METPO:1065700"
IDENTITY = "DOI:10.1371/journal.pone.0061686"
ACETATE = "DOI:10.1128/jb.164.2.866-871.1985"
NITROGEN = "DOI:10.1128/jb.01571-06"
LAG = "DOI:10.1371/journal.pbio.1002041"
ETHANOL = "DOI:10.1038/msb.2013.11"
TIMESTAMP = "2026-10-11T23:42:36Z"
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
    "label": "diauxic growth",
    "definition": (
        "A physiological phenotype in which a microbial population exhibits two "
        "successive growth phases associated with a switch from preferential use "
        "of one nutrient source to use of another as the first becomes limiting."
    ),
    "definition_source": IDENTITY,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "synonyms": [
        {"synonym_text": "diauxie", "synonym_type": "EXACT_SYNONYM", "source": ACETATE},
    ],
    "evidence": [
        {
            "reference": IDENTITY,
            "snippet": (
                "However, a significant fraction of cells maintains a high rate of "
                "elongation and displays no detectable growth lag during the shift."
            ),
            "notes": (
                "Boulineau et al. 2013, PMID:23637881, PMC3640066; scientific abstract. "
                "Introduction defines diauxic growth by sequential carbon-source use, "
                "supporting the definition's nutrient-switching differentia. Relevant "
                "Results, Discussion, Methods, actual Figure 2 and Text S1 prose were "
                "inspected. AB460 is an engineered MG1655 derivative; single-cell "
                "medium exchange is not the same assay as mixed-substrate batch "
                "growth. Population lag does not imply arrest of every cell. "
                "Contaminant-supported growth and model assumptions remain relevant. "
                "Text S1 DOC extraction loses embedded equations; no equation was "
                "visually verified or used as a curated mechanistic claim."
            ),
        },
        {
            "reference": ACETATE,
            "snippet": (
                "Azotobacter vinelandii exhibited diauxie when grown in a medium "
                "containing both acetate and glucose as carbon sources."
            ),
            "notes": (
                "George et al. 1985, PMID:3863813, PMC214331; directly retrieved "
                "source-qualified MED abstract only. Acetate preference in this "
                "experiment contradicts a universal glucose-first requirement and "
                "supports the lexical name diauxie. Full paper and figures were not "
                "inspected; a full-text XML endpoint returned HTTP 500. This access "
                "failure is not evidence that full text does not exist."
            ),
        },
        {
            "reference": NITROGEN,
            "snippet": (
                "Following recovery of growth on the alternative carbon or nitrogen "
                "source, RpoS protein concentrations declined rapidly to a basal level."
            ),
            "notes": (
                "Sandercock and Page 2008, PMID:18055600, PMC2223558; scientific "
                "abstract. Relevant Methods/Results and actual Figure 3 support UW "
                "batch-culture acetate/glucose and ammonium/N2 transitions. This "
                "supports nutrient-source scope rather than sugars or carbon alone. "
                "Ammonium augmentation addresses an oxygen-limitation alternative "
                "for the stress response. RpoS dynamics are not a universal causal "
                "mechanism of diauxie; later PHB consumption was explicitly "
                "unmeasured. Publisher text and Figure 3 were accessible despite "
                "requests HTML 403 and Europe PMC XML 500 responses."
            ),
        },
        {
            "reference": LAG,
            "snippet": (
                "many natural isolates of Saccharomyces cerevisiae display short or "
                "nonexistent diauxic lags when grown in mixtures of glucose "
                "(preferred) and galactose."
            ),
            "notes": (
                "Wang et al. 2015, PMID:25626068, PMC4308108; scientific abstract, "
                "not the XML's preceding TOC teaser or separate Author Summary. "
                "Relevant Results, growth-curve Methods, actual Figure 1 and S1 EPS "
                "were inspected. Operational zero lag means the smoothed growth-rate "
                "curve has no local minimum, not simultaneous equal use of both "
                "substrates. Natural-origin growth panels and engineered reporter "
                "derivatives require separate provenance. Figure 1 caption says "
                "eleven strains but the image has twelve labels; no strain count "
                "is inferred here. The observations oppose mandatory positive lag."
            ),
        },
        {
            "reference": ETHANOL,
            "snippet": "Once glucose is depleted, the cells consume the earlier produced ethanol",
            "notes": (
                "Zampar et al. 2013, PMID:23549479, PMC3693829; Introduction, second "
                "paragraph, not an abstract quote. Relevant Results, culture and "
                "measurement Methods and actual Figure 1 were inspected. FY4 was "
                "initially supplied glucose and later consumed produced ethanol; "
                "the definition therefore does not require both nutrients to be "
                "supplied initially. Figure 1 distinguishes concentration "
                "observations from fitted rates. Intracellular flux ranges are "
                "model-constrained, not direct flux measurements; raw supplemental "
                "data and the full mechanistic analysis were not reanalyzed."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "diauxie-scope-and-hierarchy",
            "prompt": "Retain sequential nutrient use without imposing a universal lag or regulatory mechanism.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Boulineau's Introduction defines sequential carbon use, while "
                "lag-emphasizing accounts operationalize a narrower growth-curve "
                "pattern. Wang reports short or nonexistent lags; Sandercock and "
                "Page extend the observed scope to nitrogen-source transitions. "
                "The present definition uses the nutrient-switching sense and does "
                "not require glucose preference, a positive minimum lag, complete "
                "arrest of every cell or strictly zero secondary-substrate use. "
                "An arbitrary biphasic growth curve without nutrient-switching "
                "evidence is insufficient. Diauxic shift denotes the transition; "
                "polyauxie and unqualified diphasic growth are not exact synonyms. "
                "METPO:1000731 nutrient adaptation is a trophic-type class whose "
                "local record operationalizes chronic copiotroph/oligotroph nutrient "
                "regimes, not this temporal pattern. Phenotype is the conservative "
                "parent pending upstream hierarchy review. Generalist and specialist "
                "denote niche breadth; dormancy, carbon catabolite repression and "
                "generic resource-use predicates are not exact equivalents."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "diauxie-provenance-and-mechanism",
            "prompt": "Ground conditional examples and taxon-specific mechanisms before adding canonical taxa or a graph.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The studies include laboratory strains and engineered reporter "
                "derivatives. No natural canonical example is asserted without "
                "primary strain provenance and authority-resolved taxon identity. "
                "No shared universal molecular mechanism or taxon-paired protein "
                "branch is established here. Gene presence, lac-locus annotation, "
                "RpoS expression or predicted flux alone cannot establish observed "
                "diauxic growth. It is conditional on culture and nutrients, not a "
                "fixed species identity or sequence-feature trait. Qualified MED "
                "and Crossref metadata for all five sources exposed no linked "
                "correction or retraction at the 2026-10-11 check; available primary "
                "pages were also inspected. This bounded check does not guarantee "
                "absence of notices; Wang's preprint link is not a correction. "
                "Canonical examples, causal graphs and external equivalences remain "
                "unasserted rather than being inferred from these observations."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added diauxic growth with five primary DOI-backed sources and directly "
            "checked snippets. Reserved 000704, v580 and 1065700-1065799 after "
            "ignored/hidden worktree and pending-PR checks. Sequential nutrient-use "
            "scope, variable lag, population-versus-cell distinctions and provenance "
            "limits are explicit. Existing traits unchanged; timestamp is the "
            "observed UTC curation decision."
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
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "diauxie", "", "metpo_traitmech_2026_10", "",
         "Sequential nutrient-use phenotype; a positive minimum lag is not required.", IDENTIFIER],
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
