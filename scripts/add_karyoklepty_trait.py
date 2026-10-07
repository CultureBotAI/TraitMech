"""Add selective prey-nucleus retention and use as an organismal trait."""

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
TARGET = ROOT / "data/traits/physiology/karyoklepty.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v506/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000630"
METPO_ID = "METPO:1058300"
DEFINITION = "DOI:10.1038/nature05496"
TERMINOLOGY = "DOI:10.1186/s12864-015-2052-9"
RETENTION = "DOI:10.3389/fmicb.2017.00423"
PROVENANCE = "https://doi.org/10.3389/fmicb.2017.00423"
TIMESTAMP = "2026-10-05T23:36:51Z"
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
    "label": "karyoklepty",
    "definition": (
        "A physiological phenotype in which a microbial organism selectively "
        "retains and uses nuclei acquired from prey."
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
                "Cytokinesis, plastid performance and their replication are "
                "dependent on recurrent stealing of cryptophyte nuclei."
            ),
            "notes": (
                "PMID:17251979. Direct scientific abstract from Europe PMC, "
                "cross-checked with the publisher abstract. This naming study "
                "reports retained, transcriptionally active prey nuclei in "
                "Myrionecta rubra, a synonym of Mesodinium rubrum. The "
                "plastid-related dependence is system-specific, not a universal "
                "definition requirement. Main text, figures and supplements "
                "were not accessed; no protein-resolved mechanism is imported."
            ),
        },
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "Rather, the ciliate steals the nucleus from cryptophyte prey, "
                "a process described as karyoklepty"
            ),
            "notes": (
                "PMID:26475598, PMC4609049. Direct Background naming passage, "
                "not an abstract quote or independent terminology experiment. "
                "Scientific Abstract and Background were read. The abstract "
                "reports prey-derived transcription after sequestration; "
                "expression and annotation are not native protein perturbations. "
                "Methods, Results, actual figures and supplements were not "
                "audited, so no additional canonical strain or causal edge "
                "is asserted from this study."
            ),
        },
        {
            "reference": RETENTION,
            "snippet": (
                "Well-fed cells of M. rubrum contained additional nuclei "
                "of cryptophyte origin."
            ),
            "notes": (
                "PMID:28377747, PMC5359308. Direct Results passage. Main text "
                "and actual Figures 2-5 and 9 were inspected; supplements were "
                "not. Fixed-cell microscopy documents retained central and "
                "peripheral prey nuclei during starvation/refeeding. Figure 9 "
                "is an inheritance model with illustrative micrographs, not "
                "continuous lineage tracking. Carbon fixation correlates with "
                "nuclear prevalence; starvation is not an isolated nuclear "
                "perturbation."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:704171",
            "taxon_label": "Mesodinium rubrum",
            "reference": RETENTION,
            "note": (
                "Qualified example: MBL-DK2009 fed Teleaulax amphioxeia "
                "SCCAP K-0434. The Cultures Methods at " + PROVENANCE + " "
                "document single-cell isolation from Helsingor harbor, Denmark, "
                "in 2009. Retention is conditional on feeding history; do not "
                "generalize nuclear inheritance to every strain. NCBI ESearch "
                "and EFetch independently resolved the species and its "
                "Myrionecta rubra synonym on 2026-10-05."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "karyoklepty-organismal-scope-and-parent",
            "prompt": "Keep prey-nucleus use distinct from plastid retention and sequence transfer.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "This physiological trait is not a literal nucleus, nucleomorph "
                "or sequence feature. Whole living prey/endosymbionts, DNA "
                "detection and horizontal transfer alone are insufficient. "
                "Kleptoplasty traitmech:000629 concerns plastids; phagocytosis "
                "traitmech:000627 concerns uptake; phagotrophy traitmech:000628 "
                "concerns nutrient assimilation. Endosymbiosis traitmech:000045 "
                "describes a microorganism living inside its host, not selective "
                "nuclear retention. These overlapping concepts are not exact "
                "equivalents or established universal parents. Retain phenotype "
                "METPO:1000059 pending a closer acquisition hierarchy. No "
                "fixed retention time, nuclear division, fusion, host-genome "
                "integration or universal photosynthetic role is required. "
                "No unverified synonym or ontology xref is asserted."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "karyoklepty-control-and-inheritance-mechanism",
            "prompt": "Resolve functional control and inheritance without promoting models to mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The 2017 study discusses strain-dependent alternatives to "
                "nuclear division and fusion. Its snapshots do not establish "
                "a universal inheritance mechanism. The 2007 abstract supports "
                "transcriptional function, but source-specific retention "
                "intervals and plastid dependencies are not class restrictions. "
                "Protein identities and host-control machinery remain "
                "unresolved here; no causal graph is asserted from transcript "
                "abundance, inferred targeting or nuclear enlargement alone."
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
            "Added karyoklepty with three DOI-backed snippets and a natural, "
            "strain-qualified Mesodinium example. Ignored-and-hidden searches "
            "and pinned METPO review found no exact record. Reserved "
            "METPO:1058300 in v506. Distinguished prey-nucleus retention/use "
            "from plastid retention, intact endosymbionts and sequence transfer; "
            "deferred unresolved control and inheritance mechanisms."
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
         "|".join(["TraitMech:data/traits/physiology/karyoklepty.yaml",
                   DEFINITION, TERMINOLOGY, RETENTION]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Selective prey-nucleus retention/use; no universal inheritance mechanism asserted.",
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
