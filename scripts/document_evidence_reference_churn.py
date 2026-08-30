#!/usr/bin/env python3
"""Document the decision to retain PR #511's edge-reference replacements (#520).

The offline audit compared the retained pre-tranche and tranche trees. It found
38 surviving edges in 10 records whose evidence reference changed. Only three
edges touch a newly added protein exemplar, so the edits exceeded the tranche's
stated scope. However, all 38 old evidence entries lacked snippets, while every
replacement has an edge-specific snippet and explanatory notes. Reverting the
references would therefore discard the only claim-level provenance now attached
to those unchanged edges.

This migration changes no graph or evidence field. It appends the missing
per-record rationale for the keep-and-document decision, guarded against the
exact 38 edge/reference states found by the audit.

Usage:
    python scripts/document_evidence_reference_churn.py          # dry run
    python scripts/document_evidence_reference_churn.py --only SLUG
    python scripts/document_evidence_reference_churn.py --apply
"""

from __future__ import annotations

import argparse
import collections
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TIMESTAMP = "2026-08-30T19:21:37Z"
CURATOR = "codex"
ACTION = "REVIEW_EVIDENCE_REFERENCE_CHURN"


@dataclass(frozen=True)
class EdgeChange:
    subject: str
    predicate: str
    object: str
    old_reference: str
    retained_reference: str


@dataclass(frozen=True)
class RecordReview:
    graph_id: str
    changes: tuple[EdgeChange, ...]


def edge(
    subject: str, predicate: str, object_: str, old_reference: str, retained_reference: str
) -> EdgeChange:
    return EdgeChange(subject, predicate, object_, old_reference, retained_reference)


REVIEWS: dict[str, RecordReview] = {
    "metabolism/fermentative_hydrogen_production": RecordReview(
        "fermentative_h2_production",
        (
            edge(
                "fefe_hydrogenase",
                "produces",
                "molecular_hydrogen",
                "DOI:10.3390/en16083321",
                "DOI:10.1128/JB.01582-08",
            ),
        ),
    ),
    "metabolism/lactic_acid_fermentation": RecordReview(
        "lactic_acid_fermentation_lactate",
        tuple(
            edge(
                subject,
                predicate,
                object_,
                "DOI:10.3390/fermentation10030168",
                "DOI:10.3390/molecules31020333",
            )
            for subject, predicate, object_ in (
                ("glucose", "is fermented via", "glycolysis_emp"),
                ("phosphoketolase_pathway", "yields", "lactate"),
                ("phosphoketolase_pathway", "yields", "carbon_dioxide"),
                ("phosphoketolase_pathway", "yields", "ethanol"),
                ("lactate", "causes", "decreased_ph"),
                ("decreased_ph", "inhibits", "pathogenic_microbe"),
            )
        ),
    ),
    "metabolism/methanogenesis": RecordReview(
        "methanogenesis_c1_reduction",
        (
            edge(
                "acetate",
                "serves as substrate for",
                "acetoclastic_methanogenesis",
                "DOI:10.1007/s00253-023-12700-3",
                "DOI:10.3389/fmicb.2017.01198",
            ),
            edge(
                "methylated_compounds",
                "serves as substrate for",
                "methyl_based_methanogenesis",
                "DOI:10.1007/s00253-023-12700-3",
                "DOI:10.3389/fmicb.2017.01198",
            ),
            edge(
                "coenzyme_b",
                "is required for",
                "methane",
                "DOI:10.1128/mmbr.00024-22",
                "DOI:10.1021/ja906367h",
            ),
        ),
    ),
    "metabolism/nitrogen_fixation": RecordReview(
        "nitrogen_fixation_nitrogenase",
        (
            edge(
                "nitrogenase",
                "enables",
                "nitrogen_fixation_process",
                "DOI:10.1038/nrmicro954",
                "DOI:10.34133/bdr.0005",
            ),
            edge(
                "nitrogen_fixation_process",
                "consumes",
                "dinitrogen",
                "DOI:10.1038/nrmicro.2018.9",
                "DOI:10.34133/bdr.0005",
            ),
            edge(
                "nitrogen_fixation_process",
                "has output",
                "ammonia",
                "DOI:10.1038/nrmicro954",
                "DOI:10.34133/bdr.0005",
            ),
            edge(
                "nitrogen_fixation_trait",
                "depends on",
                "nitrogenase",
                "DOI:10.1038/nrmicro954",
                "DOI:10.34133/bdr.0005",
            ),
            edge(
                "ferredoxin_flavodoxin",
                "transfers electron to",
                "nifh_fe_protein",
                "DOI:10.1128/aem.00378-23",
                "DOI:10.34133/bdr.0005",
            ),
        ),
    ),
    "metabolism/proteorhodopsin_phototrophy": RecordReview(
        "proteorhodopsin_light_driven_proton_pump",
        (
            edge(
                "proteorhodopsin_trait",
                "contributes to",
                "proton_motive_force",
                "DOI:10.1038/35081051",
                "DOI:10.1073/pnas.0611035104",
            ),
            edge(
                "proton_pumping",
                "generates",
                "proton_motive_force",
                "DOI:10.4014/jmb.2410.10034",
                "DOI:10.1073/pnas.0611035104",
            ),
            edge(
                "proton_motive_force",
                "enables",
                "atp_production",
                "DOI:10.1007/s12275-024-00125-0",
                "DOI:10.1073/pnas.0611035104",
            ),
            edge(
                "beta_carotene",
                "cleaved to produce",
                "all_trans_retinal",
                "DOI:10.34133/2022/9782712",
                "DOI:10.1128/MMBR.69.1.51-78.2005",
            ),
        ),
    ),
    "metabolism/wood_ljungdahl_pathway": RecordReview(
        "wood_ljungdahl_reductive_acetyl_coa",
        (
            edge(
                "carbon_dioxide",
                "fixed by",
                "wood_ljungdahl_trait",
                "DOI:10.1128/AEM.02473-10",
                "DOI:10.3389/fbioe.2024.1395540",
            ),
            edge(
                "tetrahydrofolate",
                "functions as C1 carrier in",
                "methyl_branch",
                "DOI:10.1039/d4cb00099d",
                "DOI:10.3389/fbioe.2024.1395540",
            ),
        ),
    ),
    "physiology/carboxydotrophic": RecordReview(
        "carboxydotrophic_co_oxidation",
        (
            edge(
                "molybdenum_hydroxylase",
                "coupled to reduction of",
                "molecular_oxygen",
                "DOI:10.1101/2023.01.17.524042",
                "DOI:10.1128/aem.00185-23",
            ),
        ),
    ),
    "physiology/catalase_activity": RecordReview(
        "catalase_activity_h2o2_detoxification",
        (
            edge(
                "catalase",
                "enables",
                "catalase_function",
                "DOI:10.1007/s00018-003-3206-5",
                "DOI:10.1021/ja9018572",
            ),
            edge(
                "catalase_function",
                "consumes",
                "hydrogen_peroxide",
                "DOI:10.1038/nrmicro3032",
                "DOI:10.1021/ja9018572",
            ),
            edge(
                "catalase_function",
                "has output",
                "molecular_oxygen",
                "DOI:10.1007/s00018-003-3206-5",
                "DOI:10.1021/ja9018572",
            ),
            edge(
                "catalase_function",
                "has output",
                "water",
                "DOI:10.1007/s00018-003-3206-5",
                "DOI:10.1021/ja9018572",
            ),
            edge(
                "catalase",
                "confers",
                "catalase_activity_trait",
                "DOI:10.1007/s00018-003-3206-5",
                "DOI:10.1021/ja9018572",
            ),
            edge(
                "catalase_activity_trait",
                "decomposes",
                "hydrogen_peroxide",
                "DOI:10.3390/biom14060697",
                "DOI:10.1021/ja9018572",
            ),
            edge(
                "hydrogen_peroxide",
                "activates",
                "oxyr_regulator",
                "DOI:10.1038/nrmicro3032",
                "DOI:10.1073/pnas.96.11.6161",
            ),
        ),
    ),
    "physiology/hydrogenotrophic": RecordReview(
        "hydrogenotrophic_hydrogen_oxidation_fixation",
        (
            edge(
                "h2_oxidation",
                "generates",
                "proton_motive_force",
                "DOI:10.2138/gselements.16.1.39",
                "DOI:10.21775/cimb.006.159",
            ),
            edge(
                "h2_oxidation",
                "coupled to reduction of",
                "molecular_oxygen",
                "DOI:10.2138/gselements.16.1.39",
                "DOI:10.3390/microorganisms7020053",
            ),
            edge(
                "h2_oxidation",
                "coupled to reduction of",
                "nitrate",
                "DOI:10.2138/gselements.16.1.39",
                "DOI:10.3390/microorganisms7020053",
            ),
            edge(
                "h2_oxidation",
                "coupled to reduction of",
                "sulfate",
                "DOI:10.2138/gselements.16.1.39",
                "DOI:10.3390/microorganisms7020053",
            ),
        ),
    ),
    "physiology/quorum_sensing": RecordReview(
        "quorum_sensing_autoinducer",
        (
            edge(
                "autoinducer",
                "participates in",
                "quorum_sensing_process",
                "DOI:10.1146/annurev.cellbio.21.012704.131001",
                "DOI:10.1007/s10867-010-9186-4",
            ),
            edge(
                "quorum_sensing_process",
                "confers",
                "quorum_sensing_trait",
                "DOI:10.1146/annurev.micro.55.1.165",
                "DOI:10.1007/s10867-010-9186-4",
            ),
            edge(
                "signal_receptor",
                "positively regulates",
                "autoinducer",
                "DOI:10.3390/ijms25052655",
                "DOI:10.1128/mbio.01079-17",
            ),
            edge(
                "quorum_quenching_enzyme",
                "inactivates",
                "autoinducer",
                "DOI:10.3390/ijms25052655",
                "DOI:10.1073/pnas.0504996102",
            ),
            edge(
                "qs_inhibitor",
                "inhibits",
                "signal_receptor",
                "DOI:10.3390/ijms25052655",
                "DOI:10.1016/j.molcel.2011.04.003",
            ),
        ),
    ),
}


def graph_edges(doc: dict[str, Any], graph_id: str) -> dict[tuple[str, str, str], dict]:
    graphs = [
        graph
        for graph in doc.get("causal_graphs") or []
        if isinstance(graph, dict) and graph.get("graph_id") == graph_id
    ]
    if len(graphs) != 1:
        raise ValueError(f"expected one graph {graph_id}, found {len(graphs)}")
    return {
        (str(item.get("subject")), str(item.get("predicate")), str(item.get("object"))): item
        for item in graphs[0].get("edges") or []
        if isinstance(item, dict)
    }


def verify_review(doc: dict[str, Any], review: RecordReview) -> None:
    indexed = graph_edges(doc, review.graph_id)
    for change in review.changes:
        key = (change.subject, change.predicate, change.object)
        if key not in indexed:
            raise ValueError(f"missing reviewed edge {review.graph_id}:{'|'.join(key)}")
        items = [item for item in indexed[key].get("evidence") or [] if isinstance(item, dict)]
        old_hits = [item for item in items if item.get("reference") == change.old_reference]
        retained_hits = [
            item for item in items if item.get("reference") == change.retained_reference
        ]
        if old_hits or len(retained_hits) != 1:
            raise ValueError(
                f"{review.graph_id}:{'|'.join(key)} expected no {change.old_reference} "
                f"and one {change.retained_reference}; found {len(old_hits)} and "
                f"{len(retained_hits)}"
            )
        retained = retained_hits[0]
        if not retained.get("snippet") or not retained.get("notes"):
            raise ValueError(
                f"{review.graph_id}:{'|'.join(key)} retained evidence lacks snippet/notes"
            )


def decision_text(review: RecordReview) -> str:
    counts = collections.Counter(
        (item.old_reference, item.retained_reference) for item in review.changes
    )
    replacements = "; ".join(
        f"{old} -> {new} ({count} edge{'s' if count != 1 else ''})"
        for (old, new), count in sorted(counts.items())
    )
    return (
        f"Offline review for issue 520 retained {len(review.changes)} evidence-reference "
        "replacement(s) that PR 511 made on surviving causal edges outside its stated "
        "protein-taxon scope. The pre-tranche evidence entries had references but no "
        "snippets; the retained entries supply edge-specific snippets and explanatory "
        "notes. Reverting would discard that claim-level provenance, so the scope defect "
        "is resolved by documenting the decision instead. This audit changed no causal "
        f"claim or evidence field. Reviewed replacements: {replacements}."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--apply", action="store_true", help="write (default: dry run)")
    parser.add_argument("--only", metavar="SLUG", help="restrict to one record slug")
    args = parser.parse_args()

    selected = {
        slug: review
        for slug, review in REVIEWS.items()
        if args.only is None or Path(slug).name == args.only
    }
    if args.only is not None and not selected:
        parser.error(f"unknown review record: {args.only}")

    failures = 0
    for slug, review in selected.items():
        path = REPO_ROOT / "data" / "traits" / f"{slug}.yaml"
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        try:
            verify_review(doc, review)
        except ValueError as error:
            print(f"  {path}: {error}; not writing", file=sys.stderr)
            failures += 1
            continue
        changes = decision_text(review)
        record_curation_event(
            doc,
            curator=CURATOR,
            action=ACTION,
            llm_assisted=True,
            timestamp=TIMESTAMP,
            upsert=True,
            changes=changes,
        )
        print(f"  {path.relative_to(REPO_ROOT)}: {len(review.changes)} edge(s) documented")
        if args.apply:
            write_validated_trait(doc, path)

    mode = "" if args.apply else " (dry run)"
    print(
        f"{len(selected) - failures} record(s) documented{mode}; {failures} failure(s)",
        file=sys.stderr,
    )
    return int(failures > 0)


if __name__ == "__main__":
    sys.exit(main())
