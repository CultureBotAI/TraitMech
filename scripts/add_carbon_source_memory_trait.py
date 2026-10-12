"""Add carbon-source memory through the guarded validated writer."""

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
SLUG = "carbon_source_memory"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v582/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000706"
METPO_ID = "METPO:1065900"
BACTERIAL = "DOI:10.1371/journal.pgen.1004556"
YEAST_GROWTH = "DOI:10.7554/eLife.39234"
YEAST_INDUCTION = "DOI:10.1016/j.cub.2007.10.044"
TIMESTAMP = "2026-10-12T03:30:18Z"
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
    "label": "carbon-source memory",
    "definition": (
        "A physiological phenotype in which a non-genetic cellular state established "
        "by prior carbon-source conditions persists after those conditions change "
        "and alters subsequent induction or growth responses to carbon sources."
    ),
    "definition_source": BACTERIAL,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": BACTERIAL,
            "snippet": (
                "Cells grown under cyclical glucose/lactose conditions thus displayed "
                "phenotypic memory of their previous metabolic adaptation."
            ),
            "notes": (
                "Lambert and Kussell 2014, PMID:25255314, PMC4177670; Results / "
                "Phenotypic memory in response to sudden environmental changes, "
                "not the abstract. Primary text, actual Figure 2 and Text S1 were "
                "inspected. Repeated glucose/lactose switches demonstrate "
                "history-dependent growth; the paper distinguishes inherited "
                "protein persistence from continuing induction after stimulus "
                "removal. F3 is an engineered W3110 derivative, not an unmodified "
                "natural exemplar. Growth is a chamber-level relative elongation "
                "readout. DOI:10.1371/journal.pgen.1004793 corrects author-name "
                "typesetting, not the biological claims; the correction was read. "
                "Model predictions are not additional experimental replication. "
                "Other figures, raw data and equations were not independently reanalyzed."
            ),
        },
        {
            "reference": YEAST_GROWTH,
            "snippet": (
                "past exposure to an environmental condition can shorten the time "
                "needed to adapt when the condition re-occurs"
            ),
            "notes": (
                "Cerulus et al. 2018, PMID:30299256, PMC6211830; scientific "
                "abstract, confirmed against NCBI full-text XML. Relevant Results, "
                "Methods, Discussion, actual Figures 1, 2, 6 and Figure 1 supplement "
                "4 were inspected. Carbon-shift assays separate population lag "
                "from single-cell growth resumption; cells not resuming within "
                "the observation window are not thereby proved dead. Cross-sugar "
                "effects and respiratory perturbations oppose an obligatory "
                "same-sugar or sugar-specific protein-inheritance mechanism. "
                "The main AN63 series is engineered; the separately reported "
                "non-laboratory strains have unreviewed primary provenance here. "
                "Publisher article access was challenged; public figure assets "
                "were accessible. Raw data and all other supplements were not reanalyzed."
            ),
        },
        {
            "reference": YEAST_INDUCTION,
            "snippet": 'This "galactose memory" persists for several generations',
            "notes": (
                "Zacharioudakis et al. 2007, PMID:17997309; directly retrieved, "
                "source-qualified MED scientific abstract only. The preceding "
                "sentence compares initial GAL activation with rapid reactivation "
                "in progeny after intervening glucose growth. This supports the "
                "induction endpoint, not a measured growth-rate benefit. Its "
                "Gal1 and cytoplasmic-factor interpretation remains assay-specific; "
                "the abstract's chromatin conclusion is not universalized. Full "
                "text, figures and strain provenance were not inspected. The "
                "index links a Comment in, not a correction or independent replication."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "carbon-memory-scope-and-hierarchy",
            "prompt": "Retain carbon-source history dependence without conflating its endpoints or neighboring traits.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The qualifier carbon-source bounds this curator-defined class. "
                "Unqualified cellular, metabolic, phenotypic and transcriptional "
                "memory, bistability and hysteresis are not asserted as exact "
                "synonyms. Demonstrating the phenotype requires comparing prior "
                "histories under matched test conditions and genetic background; "
                "a single diauxic transition, persistent reporter fluorescence, "
                "gene presence or a different current medium alone is insufficient. "
                "Induction kinetics and growth recovery are distinct endpoints, "
                "and one must not be substituted for the other. No fixed duration, "
                "number of divisions, benefit, particular sugar, or molecular "
                "mechanism is required. Genetic adaptation, immune memory, "
                "chemotactic temporal sensing, stress priming and stochastic "
                "bet hedging are not equivalent. METPO:1000731 nutrient adaptation "
                "is a trophic-type class locally framed as the chronic "
                "copiotroph/oligotroph axis; diauxic growth denotes sequential "
                "nutrient use, and generalist/specialist describe niche breadth. "
                "METPO:1000059 phenotype is the conservative parent pending "
                "upstream hierarchy review. This is not a sequence-feature record "
                "or a precomposed uses-carbon-source assertion."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "carbon-memory-examples-and-mechanisms",
            "prompt": "Resolve natural strain provenance and assay-specific causal branches before adding exemplars or a graph.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The retained observations do not establish a uniform species-wide "
                "phenotype or a common protein-resolved mechanism. Canonical taxa "
                "require primary provenance and authority-resolved taxon identity; "
                "no canonical_examples, causal_graphs or external xrefs are "
                "asserted. Source-qualified MED and Crossref records were checked "
                "on 2026-10-12. Lambert's linked correction was read and retained "
                "in evidence notes; no other linked correction or retraction was "
                "exposed by these bounded records. Publisher/full-text access "
                "limits are recorded per source, not treated as absence of notices. "
                "The pinned and current upstream METPO releases contain no exact "
                "memory class found by the ignored/hidden lexical and RDF "
                "assessment; the ontology baseline remains unchanged."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added carbon-source memory with three primary DOI-backed sources "
            "and directly checked snippets. Reserved 000706, v582 and "
            "1065900-1065999 after ignored/hidden worktree and pending-PR checks. "
            "Endpoint, strain-provenance, mechanism and notice limits are explicit. "
            "Existing traits unchanged; timestamp is the observed UTC curation decision."
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
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Non-genetic history-dependent phenotype; distinguish induction and growth endpoints.", IDENTIFIER],
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
