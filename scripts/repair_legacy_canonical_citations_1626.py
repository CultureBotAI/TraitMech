#!/usr/bin/env python3
"""Repair three source-qualified canonical examples (#1626); dry run by default."""
from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TRAITS_DIR = ROOT / "data/traits"
TIMESTAMP = "2026-10-03T17:07:26Z"
ACTION = "REPAIR_CANONICAL_CITATION_SCOPE_1626"
REVIEW_ACTION = "REFINE_CANONICAL_ARCHETYPES_1629"
REVIEW_TIMESTAMP = "2026-10-03T17:30:07Z"
SWAN = "DOI:10.1128/jb.150.1.377-380.1982"
LI = "DOI:10.3389/fmicb.2021.705326"
SWAN_EVIDENCE = {
    "reference": SWAN,
    "snippet": "unipolar cells, recently divided, have only one bundle of flagella.",
    "notes": (
        "Swan 1982, p. 377, methods: S. volutans ATCC 19554 was grown at "
        "30 C in ATCC medium 234. Recently divided cells in an actively growing "
        "culture were naturally unipolar; older cells had two flagellar bundles "
        "and were excluded from the measurements. This supports a life-stage-qualified "
        "one-pole example, not unipolar flagellation of every cell or a deflagellation "
        "experiment. The source scan, rather than the abstract alone, establishes "
        "the culture and division-stage context."
    ),
}
LI_EVIDENCE = {
    "reference": LI,
    "snippet": (
        "the number of viable cells in LB broth supplemented with 0% NaCl at "
        "24 h is significantly higher than other tested groups"
    ),
    "notes": (
        "Li et al. 2021, Results, Bacterial Growth, Figure 2B: wild-type "
        "E. coli BW25113 was compared in LB broth supplemented with 0%, 1%, "
        "3.5% and 5% NaCl at 37 C. This is a strain- and medium-qualified "
        "low-salt growth observation, not sodium-free growth, a complete "
        "salinity optimum curve or a universal species-wide requirement. "
        "PMCID:PMC8415458 and PMID:34484145 identify this same paper."
    ),
}
SPECS = {
    "morphology/lophotrichous": {
        "identity": {
            "identifier": "traitmech:000058", "label": "lophotrichous",
            "definition": "A flagellar arrangement with a tuft of multiple flagella at one pole of the cell.",
            "definition_source": "DOI:10.1093/femsre/fuv034",
            "trait_category": "MORPHOLOGY", "parent_traits": ["traitmech:000056"],
        },
        "before": {
            "taxon_id": "NCBITaxon:968", "taxon_label": "Spirillum volutans",
            "note": "bipolar flagellar tufts",
            "reference": "PMID:16561638 (DOI:10.1128/jb.57.1.111-118.1949)",
        },
        "after": {
            "taxon_id": "NCBITaxon:968", "taxon_label": "Spirillum volutans",
            "reference": SWAN,
            "note": (
                "Recently divided, naturally unipolar cells of S. volutans ATCC "
                "19554 have one bundle of flagella. Swan studied an actively growing "
                "culture at 30 C in ATCC medium 234; older bipolar cells had two "
                "bundles and were excluded. This example is restricted to the "
                "unipolar division stage, not all cells of the species."
            ),
        },
        "evidence": SWAN_EVIDENCE,
        "changes": (
            "Resolved issue 1626 by replacing the mismatched bipolar example note "
            "and compound PMID:16561638 (DOI:10.1128/jb.57.1.111-118.1949) citation "
            "with a life-stage-qualified, one-bundle example from Swan 1982 "
            "(DOI:10.1128/jb.150.1.377-380.1982; PMID:7061399; PMC220122). "
            "This is an explicit source and scope correction, not a PMID-to-DOI "
            "normalization: Pijper's original PMID and DOI identify the same 1949 "
            "paper. Source-native scans distinguish recently divided unipolar "
            "ATCC 19554 cells from older bipolar cells. Added the exact methods "
            "snippet and bounded interpretation; retained NCBITaxon:968 and the "
            "independently checked NCBI label. The definition, hierarchy, graph, "
            "other example and existing amphitrichous record are unchanged."
        ),
    },
    "environment/non_halophilic": {
        "identity": {
            "identifier": "METPO:1000624", "label": "non halophilic",
            "definition": "A halophily preference in which an organism does not require or prefer elevated salt concentrations for growth.",
            "definition_source": "DOI:10.1128/AEM.01934-12",
            "trait_category": "ENVIRONMENT", "parent_traits": ["METPO:1000629"],
        },
        "before": {
            "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli",
            "note": "grows without added NaCl", "reference": "PMC8415458",
        },
        "after": {
            "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli",
            "reference": LI,
            "note": (
                "Wild-type E. coli BW25113 grew in LB broth supplemented with "
                "0% NaCl at 37 C; at 24 h its viable count exceeded the 1%, 3.5% "
                "and 5% NaCl groups (Figure 2B). This supports a strain-qualified "
                "non-halophilic example, not sodium-free growth or a universal "
                "claim about every E. coli strain."
            ),
        },
        "evidence": LI_EVIDENCE,
        "changes": (
            "Resolved issue 1626 by normalizing PMC8415458 to its verified DOI "
            "10.3389/fmicb.2021.705326 (PMID:34484145), without replacing the "
            "paper. Qualified the E. coli example to wild-type BW25113 growth "
            "in LB supplemented with 0% NaCl at 37 C and the 24-h comparison "
            "with 1%, 3.5% and 5% NaCl. Added an exact Results snippet and "
            "interpretation; no sodium-free or universal species-wide requirement "
            "is inferred. Retained NCBITaxon:562 and its independently checked "
            "NCBI label. Definition, hierarchy, graph and other example unchanged."
        ),
    },
    "environment/halophily_preference": {
        "identity": {
            "identifier": "METPO:1000629", "label": "halophily preference",
            "definition": "A phenotype that is relating to an organism's salt concentration requirements or tolerance for growth.",
            "definition_source": "DOI:10.1093/femsre/fuy009",
            "trait_category": "ENVIRONMENT", "parent_traits": ["METPO:1000059"],
        },
        "before": {
            "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli",
            "reference": "PMC8415458",
            "note": (
                "Escherichia coli is a non-halophilic comparator that grows without "
                "an elevated-salt requirement; it exemplifies a contrasting branch "
                "of this broad preference class."
            ),
        },
        "after": {
            "taxon_id": "NCBITaxon:562", "taxon_label": "Escherichia coli",
            "reference": LI,
            "note": (
                "The non-halophilic branch is exemplified by wild-type E. coli "
                "BW25113: in LB at 37 C, the 0%-NaCl-supplement group had a "
                "higher viable count at 24 h than the 1%, 3.5% and 5% groups "
                "(Figure 2B). This is a strain- and medium-qualified comparator, "
                "not sodium-free growth or a universal species-wide requirement."
            ),
        },
        "changes": (
            "Resolved issue 1626 by normalizing PMC8415458 to its verified DOI "
            "10.3389/fmicb.2021.705326 (PMID:34484145), preserving the same paper. "
            "Qualified the non-halophilic comparator to BW25113 in LB at 37 C "
            "and the reported 24-h viable-count comparison across 0%, 1%, 3.5% "
            "and 5% NaCl supplementation. Retained NCBITaxon:562 and its "
            "independently checked NCBI label. The broad-class role, Halomonas "
            "example, definition, hierarchy and graph are unchanged; no "
            "species-wide salt requirement or sodium-free growth is asserted."
        ),
    },
}


REVIEW_SPECS = {
    "traitmech:000058": {
        "before_examples": [
            {"taxon_id": "NCBITaxon:210", "taxon_label": "Helicobacter pylori",
             "note": "polar tuft of flagella", "reference": "PMID:30258065"},
            copy.deepcopy(SPECS["morphology/lophotrichous"]["after"]),
        ],
        "changes": (
            "Addressed independent PR 1628 review and issue 1629 by removing the "
            "S. volutans canonical-example row while retaining the Swan 1982 "
            "evidence and verbatim snippet. Recently divided unipolar cells are "
            "directly observed, but a selected division-stage observation is not "
            "used here as the schema's archetypal taxon exemplar. H. pylori remains "
            "the canonical example. This does not deny naturally unipolar "
            "S. volutans cells, assert disjoint organism-level traits or generalize "
            "the division sequence to every amphitrichous taxon. The amphitrichous "
            "record, trait identity, definition, hierarchy and graph are unchanged; "
            "the initial repair event is preserved."
        ),
    },
    "METPO:1000629": {
        "before_examples": [
            {"taxon_id": "NCBITaxon:2746", "taxon_label": "Halomonas elongata",
             "reference": "PMID:20849449",
             "note": "Halomonas elongata DSM 2581T is a source-backed moderate-halophile model; "
                     "this exemplifies the halophilic branch of the broad salt-preference class."},
            copy.deepcopy(SPECS["environment/halophily_preference"]["after"]),
        ],
        "changes": (
            "Addressed independent PR 1628 review and issue 1629 by retaining the "
            "verified Li 2021 DOI and BW25113/LB strain-medium context as a "
            "non-halophilic branch comparator, without repeating the child's "
            "24-hour numerical growth comparison. The quantitative comparison "
            "and exact snippet remain on non_halophilic. No sodium-free or "
            "universal species-wide growth claim is introduced. Other examples, "
            "identity, definition, hierarchy, graph, evidence and prior history "
            "are unchanged."
        ),
    },
}
REVIEW_SPECS["traitmech:000058"]["after_examples"] = copy.deepcopy(
    REVIEW_SPECS["traitmech:000058"]["before_examples"][:1]
)
REVIEW_SPECS["METPO:1000629"]["after_examples"] = copy.deepcopy(
    REVIEW_SPECS["METPO:1000629"]["before_examples"]
)
REVIEW_SPECS["METPO:1000629"]["after_examples"][1]["note"] = (
    "Wild-type E. coli BW25113 in LB broth serves as the non-halophilic branch "
    "comparator, contrasting with the Halomonas halophile example. This is a "
    "strain- and medium-qualified illustration, not sodium-free growth or a "
    "universal species-wide requirement; the measured comparison is retained "
    "on the non_halophilic child."
)


def event(changes: str, *, action: str = ACTION, timestamp: str = TIMESTAMP) -> dict:
    holder: dict = {}
    return record_curation_event(
        holder, curator="codex", action=action, changes=changes,
        llm_assisted=True, timestamp=timestamp,
    )


def build_initial_update(doc: dict, spec: dict) -> dict:
    expected = {**spec["identity"], "term_kind": "CLASS", "mapping_status": "REVIEWED"}
    for key, value in expected.items():
        if doc.get(key) != value:
            raise ValueError(f"{spec['identity']['label']}: {key} drifted")
    examples = doc.get("canonical_examples") or []
    hits = [i for i, row in enumerate(examples) if row.get("taxon_id") == spec["before"]["taxon_id"]]
    if len(hits) != 1:
        raise ValueError("expected exactly one target canonical example")
    index = hits[0]
    expected_event = event(spec["changes"])
    prior_events = [row for row in doc.get("curation_history", []) if row.get("action") == ACTION]
    evidence = spec.get("evidence")
    matching_evidence = [row for row in doc.get("evidence", [])
                         if evidence and row.get("reference") == evidence["reference"]]
    if examples[index] == spec["after"]:
        if prior_events != [expected_event] or (evidence and matching_evidence != [evidence]):
            raise ValueError("postimage evidence or history drifted")
        return copy.deepcopy(doc)
    if examples[index] != spec["before"]:
        raise ValueError("target canonical example drifted")
    if prior_events or matching_evidence:
        raise ValueError("partial update or pre-existing replacement evidence")
    updated = copy.deepcopy(doc)
    updated["canonical_examples"][index] = copy.deepcopy(spec["after"])
    if evidence:
        updated.setdefault("evidence", []).append(copy.deepcopy(evidence))
    record_curation_event(
        updated, curator="codex", action=ACTION, changes=spec["changes"],
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return updated


def build_update(doc: dict, spec: dict) -> dict:
    review = REVIEW_SPECS.get(spec["identity"]["identifier"])
    if not review:
        return build_initial_update(doc, spec)
    expected_event = event(review["changes"], action=REVIEW_ACTION, timestamp=REVIEW_TIMESTAMP)
    prior = [row for row in doc.get("curation_history", []) if row.get("action") == REVIEW_ACTION]
    if prior:
        if prior != [expected_event] or doc.get("canonical_examples") != review["after_examples"]:
            raise ValueError("review postimage or history drifted")
        # Reconstruct the initial postimage to validate both stages without rewriting history.
        restored = copy.deepcopy(doc)
        restored["canonical_examples"] = copy.deepcopy(review["before_examples"])
        restored["curation_history"].remove(expected_event)
        if build_initial_update(restored, spec) != restored:
            raise ValueError("review postimage lacks completed initial repair")
        return copy.deepcopy(doc)
    updated = build_initial_update(doc, spec)
    if updated["canonical_examples"] != review["before_examples"]:
        raise ValueError("review preimage canonical examples drifted")
    updated["canonical_examples"] = copy.deepcopy(review["after_examples"])
    record_curation_event(
        updated, curator="codex", action=REVIEW_ACTION, changes=review["changes"],
        llm_assisted=True, timestamp=REVIEW_TIMESTAMP,
    )
    return updated


def run(*, apply: bool = False) -> int:
    pending = []
    for slug, spec in SPECS.items():
        path = TRAITS_DIR / f"{slug}.yaml"
        original = yaml.safe_load(path.read_text())
        updated = build_update(original, spec)
        if updated != original:
            pending.append((path, updated))
    # Validate every planned record before the first live write.
    with tempfile.TemporaryDirectory() as tmp:
        for path, updated in pending:
            write_validated_trait(updated, Path(tmp) / path.name)
        if apply:
            for path, updated in pending:
                write_validated_trait(updated, path)
    print(f"{'Updated' if apply else 'Would update'} {len(pending)} canonical-example records")
    return len(pending)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true", help="write validated changes")
    modes.add_argument("--dry-run", action="store_true", help="validate only (default)")
    args = parser.parse_args()
    run(apply=args.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
