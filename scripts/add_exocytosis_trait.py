"""Add the microbial secretion phenotype without conflating fusion and discharge."""

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
TARGET = ROOT / "data/traits/physiology/exocytosis.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v513/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000637"
METPO_ID = "METPO:1059000"
FUSION = "DOI:10.1083/jcb.56.1.153"
CONSTITUTIVE = "DOI:10.1007/BF01870409"
STEP_BOUNDARY = "DOI:10.1016/s0143-4160(98)90030-6"
TIMESTAMP = "2026-10-06T08:06:46Z"
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
    "label": "exocytosis",
    "definition": (
        "A physiological phenotype in which a microbial cell releases material "
        "from an intracellular membrane-bounded compartment to the cell exterior "
        "through a fusion pore between the compartment membrane and the plasma "
        "membrane."
    ),
    "definition_source": FUSION,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": FUSION,
            "snippet": (
                "The cytoplasm between the two matching membrane sites is "
                "squeezed away and the membranes fuse"
            ),
            "notes": (
                "PMID:4629881, PMC2108847. Scientific Abstract directly read in "
                "Europe PMC XML and PubMed. The quote retains the source's "
                "missing terminal punctuation. Freeze-fracture/etch observations "
                "in the historically named Tetrahymena pyriformis system connect "
                "mucocyst-plasma-membrane fusion, opening enlargement and contents "
                "release. Fixation triggers some discharge. Abstract-level "
                "evidence does not establish a universal pore size or fusion "
                "machinery. The XML has sparse body content and the PDF endpoint "
                "returned HTML; full methods, figures and strain provenance "
                "were not inspected."
            ),
        },
        {
            "reference": CONSTITUTIVE,
            "snippet": (
                "Upon returning the cells to the permissive temperature the "
                "contents of the accumulated vesicles were secreted."
            ),
            "notes": (
                "PMID:1744905. Scientific Abstract directly read in NCBI PubMed "
                "XML and Europe PMC metadata, which agree on the DOI. "
                "Constitutive secretion in Saccharomyces cerevisiae is examined "
                "using temperature-sensitive sec mutants, accumulated vesicles "
                "and blocked protein synthesis. Calcium perturbations did not "
                "affect the measured release under these conditions; this does "
                "not establish calcium irrelevance in every yeast context. "
                "No universal rate or requirement for extracellular stimulation "
                "is inferred. Full methods, figures and strain provenance "
                "remain unread."
            ),
        },
        {
            "reference": STEP_BOUNDARY,
            "snippet": (
                "This is a detailed characterization of a secretory mutant "
                "incapable of releasing secretory contents despite normal "
                "exocytotic membrane fusion performance."
            ),
            "notes": (
                "PMID:9681197. Scientific Abstract verified in PubMed XML and "
                "Europe PMC metadata. Relevant Methods, Results and Discussion "
                "were read in the primary PDF at https://d-nb.info/1107191386/34; "
                "pages 349-350 and 354-356, including Figures 6-9, were visually "
                "inspected. Paramecium caudatum tnd1 retains condensed cargo "
                "despite fusion and extracellular fluorochrome access. Figure 9 "
                "shows untriggered mutant cells, not a wildtype experiment. "
                "This supports separation of fusion and discharge, not tnd1 "
                "as a positive example of completed secretion. Reduced calcium "
                "binding is a proposed explanation, not a proven molecular "
                "lesion. Other figures and tables were not visually audited."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "exocytosis-scope-and-mapping",
            "prompt": "Separate the secretion phenotype from its component steps.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This concerns secretion by the microbe, not a host-cell "
                "response. Docking, intracellular trafficking or fusion alone "
                "does not demonstrate cargo release. Transporter-mediated "
                "export, membrane budding, lysis, cell-cell fusion and "
                "endocytosis are not equivalents. Constitutive and "
                "stimulus-regulated secretion are included; total emptying, "
                "permanent vesicle collapse and a shared calcium response are "
                "not required. GO:0006887 was resolved at "
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006887 "
                "and includes partial secretion through transient pores, but "
                "denotes a biological process rather than an equivalent "
                "organismal phenotype. No xref or synonym is inferred. The "
                "obsolete METPO secretion classes are broader, not exact "
                "replacements or usable parents. Retain phenotype METPO:1000059 "
                "pending human mapping review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "exocytosis-exemplar-and-mechanism",
            "prompt": "Resolve natural strain provenance and route-specific mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Canonical examples remain unset: the historical Tetrahymena "
                "strain needs modern taxonomy and provenance review, the yeast "
                "experiment uses conditional sec mutants, and the origin of "
                "the Paramecium tnd1 mutant has not been independently checked. "
                "Do not infer natural or engineered provenance from a mutant "
                "label. The fusion-only mutant is boundary evidence, not a "
                "positive secretion exemplar. These studies support phenotype "
                "scope across experimental systems, not one conserved "
                "protein mechanism. Obtain taxon-paired functional evidence "
                "and verified accessions before adding protein examples or "
                "a causal graph."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added exocytosis with three DOI-backed scientific-abstract "
            "snippets and explicit secretion-versus-fusion, strain and "
            "source-access limits. Ignored-and-hidden searches and pinned "
            "METPO review found no exact record. Reserved METPO:1059000 "
            "in v513. Deferred unverified examples, mappings and protein "
            "mechanisms; no existing trait was reparented."
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
         "|".join(["TraitMech:data/traits/physiology/exocytosis.yaml",
                   FUSION, CONSTITUTIVE, STEP_BOUNDARY]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Secretion through a fusion pore; fusion without discharge is a distinct readout.",
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
