"""Add unconventional secretion without equating it with one cargo or route."""

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
TARGET = ROOT / "data/traits/physiology/unconventional_protein_secretion.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v524/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000648"
METPO_ID = "METPO:1060100"
BYPASS = "DOI:10.3389/fcell.2022.852028"
EXPORT = "DOI:10.7554/eLife.16299"
AUTOPHAGOSOME_BOUNDARY = "DOI:10.1083/jcb.201407119"
GOLGI_BOUNDARY = "DOI:10.1083/jcb.202312120"
TIMESTAMP = "2026-10-06T18:32:51Z"
SCOPE_FIX_TIMESTAMP = "2026-10-06T18:43:11Z"
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
    "label": "unconventional protein secretion",
    "definition": (
        "A physiological phenotype in which a eukaryotic microbial cell delivers "
        "protein cargo to the plasma membrane or extracellular space by a route "
        "that bypasses part or all of the conventional endoplasmic-reticulum-"
        "Golgi-plasma-membrane secretory itinerary."
    ),
    "definition_source": BYPASS,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": BYPASS,
            "snippet": (
                "Our results show that neosynthesized PmaA and PalI are "
                "translocated to the PM via Golgi-bypass, similar to nutrient transporters."
            ),
            "notes": (
                "PMID:35465316, PMC9021693. Scientific Abstract and selected "
                "Introduction, Results and Methods directly read in Europe PMC XML. "
                "The paper includes membrane-cargo delivery within unconventional "
                "protein secretion. Aspergillus nidulans fluorescent cargo, "
                "conditional trafficking repression and localization assays "
                "support Golgi bypass after COPII-dependent ER exit, not soluble "
                "extracellular release or universal ER independence. The reporters "
                "and promoter replacements are engineered; no natural canonical "
                "exemplar is inferred. Actual panels, supplements and independent "
                "recipient-strain provenance were not inspected."
            ),
        },
        {
            "reference": EXPORT,
            "snippet": (
                "Under these conditions Acb1, but not Cof1, was detected in the "
                "cell wall extract of starving cells"
            ),
            "notes": (
                "PMID:27115345, PMC4868542. Contiguous full-text Results s2-1 "
                "span, directly read in Europe PMC XML, not an abstract quote. "
                "Mild extraction detects intact Acb1 outside the plasma membrane "
                "of starved Saccharomyces cerevisiae with Cof1 leakage and Bgl2 "
                "extraction controls. This is cell-wall/periplasmic recovery, not "
                "direct detection in culture medium. Harsh extraction, some "
                "mutants, heat and DMSO can invalidate the assay through leakage. "
                "The direct assay differs from earlier SDF-2 bioactivity assays "
                "and does not support a Vps4 requirement. Static CUPS images "
                "do not prove a temporal sequence. Actual panels and strain "
                "provenance remain uninspected."
            ),
        },
        {
            "reference": AUTOPHAGOSOME_BOUNDARY,
            "snippet": (
                "Altogether our findings indicate that CUPS are not specialized "
                "autophagosomes as suggested previously."
            ),
            "notes": (
                "PMID:25512390, PMC4274258. Scientific Abstract abstract2, "
                "distinct from the precis, and Introduction directly read in "
                "Europe PMC XML. The authors revise the earlier autophagosome "
                "interpretation of yeast CUPS. This is compartment-identity "
                "boundary evidence, not proof that every unconventional route "
                "excludes all autophagy-related machinery. Actual panels, full "
                "Methods and strain provenance were not inspected."
            ),
        },
        {
            "reference": GOLGI_BOUNDARY,
            "snippet": (
                "Notably, while CUPS remain stable, the modified TGN undergoes "
                "remodeling during the later stages of unconventional secretion."
            ),
            "notes": (
                "PMID:40015244, PMC11867701. Scientific Abstract, not the teaser, "
                "and selected Results, Discussion and Methods directly read in "
                "Europe PMC XML. Yeast CUPS contact a modified trans-Golgi network; "
                "this argues against defining the phenotype by absence of all "
                "Golgi-derived membranes. Rcy1 and v-SNARE perturbations reduce "
                "cell-wall recovery of Acb1, SOD1 and Trx2 with Cof1 controls. "
                "Drs2-deleted cells could not be assayed because of lysis concerns. "
                "Cargo collection and final delivery through the proposed "
                "CUPS-TGN route remain a model. BY4741 derivatives include "
                "engineered reporters and mutants. Actual panels and supplements "
                "were not visually inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "unconventional-secretion-scope-and-mapping",
            "prompt": "Keep cargo destinations and route-specific meanings distinct.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The broad usage in DOI:10.3389/fcell.2022.852028 includes "
                "plasma-membrane delivery after ER entry; DOI:10.7554/eLife.16299 "
                "describes an ER-bypassing soluble-cargo route. Preserve both, "
                "rather than treating leaderless secretion, Golgi bypass or "
                "secretory autophagy as exact synonyms. This concerns traffic "
                "performed by a eukaryotic microbe, not its animal or plant host. "
                "An absent predicted signal peptide, ATG dependence, CUPS "
                "formation or protein detected after lysis alone is insufficient. "
                "Membrane localization does not establish soluble release. The "
                "degradative autophagy record traitmech:000638 is not a broader "
                "parent; exocytosis traitmech:000637 specifies fusion-pore release "
                "rather than an unconventional itinerary. Overlap is not "
                "disjointness. Obsolete METPO secretion classes do not supply an "
                "active exact term. Keep METPO:1000059 as parent and leave "
                "ontology equivalences and finer route hierarchy for human review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "unconventional-secretion-exemplars-and-mechanisms",
            "prompt": "Resolve natural exemplars and mechanisms separately for each route.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Retain qualified laboratory observations without labeling "
                "engineered fluorescent cargo or conditional trafficking "
                "mutants as natural canonical exemplars. Natural strain "
                "provenance, source figures and accession-level functional "
                "evidence need further review before adding examples or a "
                "protein-resolved graph. The three CUPS papers share investigators "
                "and are not independent-laboratory replications; the Aspergillus "
                "study supports a different route, not replication of CUPS. No "
                "universal starvation trigger, signal-peptide absence, COPII "
                "independence, autophagosome or conserved export apparatus is "
                "asserted. ATG-dependent export remains a possible narrower "
                "research target, not an allocated additional trait."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-06",
        },
    ],
}


def build_record(*, initial: bool = False) -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added unconventional protein secretion with four DOI-backed "
            "snippets and explicit soluble-export, membrane-delivery, route "
            "and assay limits. Ignored-and-hidden searches and pinned METPO "
            "review found no exact record. Reserved METPO:1060100 in v524. "
            "Deferred unverified mappings, natural exemplars and protein "
            "mechanisms; existing records remain unchanged."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    if initial:
        record["definition"] = record["definition"].replace(
            "endoplasmic-reticulum-Golgi-plasma-membrane",
            "endoplasmic-reticulum-to-Golgi",
        )
    else:
        record_curation_event(
            record, curator="codex", action="CURATED_WITH_LITERATURE",
            changes=(
                "Clarified the conventional itinerary through plasma-membrane "
                "delivery (#1760), preserving the definition source's inclusion "
                "of unconventional post-Golgi export. No new route, cargo, taxon "
                "or universal mechanism is inferred."
            ),
            llm_assisted=True, timestamp=SCOPE_FIX_TIMESTAMP,
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
         "|".join(["TraitMech:data/traits/physiology/unconventional_protein_secretion.yaml",
                   BYPASS, EXPORT, AUTOPHAGOSOME_BOUNDARY, GOLGI_BOUNDARY]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Includes soluble export and membrane delivery; not one universal mechanism.",
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
    initial = build_record(initial=True)
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) not in (record, initial):
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() not in (proposal, proposal_tsv(initial)):
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
