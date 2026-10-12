"""Add a source-qualified replicative-aging phenotype through the validated writer."""

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
SLUG = "replicative_aging"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v585/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000709"
METPO_ID = "METPO:1066200"
DEFINITION_SOURCE = "DOI:10.1098/rstb.2018.0442"
CAULOBACTER = "DOI:10.1186/1471-2148-7-126"
FISSION_YEAST = "DOI:10.7554/eLife.20340"
BUDDING_YEAST = "DOI:10.1371/journal.pbio.3002245"
TIMESTAMP = "2026-10-12T10:13:30Z"
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
    "label": "replicative aging",
    "definition": (
        "A physiological phenotype in which microbial cells exhibit declining "
        "growth or reproductive performance, or increasing mortality risk, "
        "with increasing replicative age under specified conditions."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "For both cell types, division time progressively increased "
                "over successive generations"
            ),
            "notes": (
                "Lapinska et al. 2019, PMID:31587633, PMC6792439; Figure 2 "
                "caption, directly checked in primary full-text XML and the "
                "author-hosted PDF. The Introduction defines aging by declining "
                "performance. Figure 2 was visually inspected: the early "
                "division-time trend approaches a plateau in the longer run, "
                "not indefinite deterioration. Methods separate brightfield "
                "aging measurements from fluorescent uptake/aggregation assays. "
                "Methods name BW25113, but the Introduction says BW21113; "
                "that discrepancy is unresolved. Starting-condition effects "
                "remain a limitation. No universal protein mechanism is established."
            ),
        },
        {
            "reference": CAULOBACTER,
            "snippet": "Aging refers to a decline in reproduction and survival with increasing age.",
            "notes": (
                "Ackermann et al. 2007, PMID:17662151, PMC2174458; scientific "
                "abstract Background, directly checked against MED and primary "
                "full-text XML. Caulobacter stalked-cell cohorts showed "
                "age-dependent loss of reproductive function, with both faster "
                "and slower aging among evolved clones. This endpoint combines "
                "survival and reproduction and cannot separate them. UJ590 is "
                "a pilA-deletion derivative, not an unmodified natural exemplar. "
                "Its elapsed-time assay complements, rather than replaces, "
                "the division-indexed evidence above."
            ),
        },
        {
            "reference": FISSION_YEAST,
            "snippet": (
                "Surprisingly, cells die without the classic hallmarks of "
                "cellular aging, such as progressive changes in size, doubling "
                "time, or sibling health."
            ),
            "notes": (
                "Spivey et al. 2017, PMID:28139976, PMC5332158; scientific "
                "abstract, not the eLife digest, directly checked against MED "
                "and primary full-text XML. Boundary evidence: finite "
                "replicative lifespan and its extension do not alone demonstrate "
                "age-dependent deterioration. The reported age-independent "
                "mortality applies to the measured fission-yeast conditions, "
                "not all strains and environments. The abstract and Discussion "
                "were assessed, not all experiments or figure images."
            ),
        },
        {
            "reference": BUDDING_YEAST,
            "snippet": (
                "This occurs without an increase in lifespan, proving that at "
                "least in yeast, lifespan is distinct from senescence and loss "
                "of fitness."
            ),
            "notes": (
                "Horkai et al. 2023, PMID:37643155, PMC10464975; Results, "
                "Suppression of age-linked phenotypic change, directly checked "
                "against publisher text and primary XML. Galactose-aged "
                "diploid MEP cells retained better performance without longer "
                "lifespan. This engineered mother-enrichment system and its "
                "platform-dependent results are not universal natural-taxon "
                "claims. The authors also use replicative ageing for passage "
                "through divisions without senescent decline; that broader "
                "usage is not the operational phenotype defined here."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "replicative-aging-operational-scope",
            "prompt": "Review the decline-based phenotype label separately from lifespan and broader aging terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Replicative age follows a cell or inherited cell lineage across "
                "successive divisions; culture age alone is not that measurement. "
                "Use age-resolved performance or mortality risk, not merely a "
                "finite lifespan, old-pole identity, endpoint death, cumulative "
                "survival loss or an old/new sibling difference. A decline can "
                "approach a plateau; continuous worsening until death is not "
                "required. The record uses the functional-decline sense of "
                "aging, while Horkai et al. 2023 explicitly distinguish senescence "
                "from broader replicative ageing. Upstream review should assess "
                "that label boundary; no exact synonym or external xref is "
                "asserted. Chronological survival in nondividing cultures, "
                "population-wide clonal senescence and irreversible mammalian "
                "cell-cycle arrest are not equated with this phenotype. The "
                "existing gram-variable culture_aging node denotes "
                "stationary-phase conditions and is not an exact grounding "
                "target. METPO:1000059 phenotype is the conservative broader "
                "class; no existing record is reparented."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "replicative-aging-mechanism-and-example-limits",
            "prompt": "Resolve strain provenance and taxon-scoped mechanisms without inferring them from lifespan or markers.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "This is an assayable cellular phenotype, not a locus, protein "
                "profile, numeric lifespan field or claim that all microbes "
                "age under all conditions. No canonical example is asserted "
                "pending strain-provenance and taxonomy checks, including the "
                "2019 strain-name discrepancy. A protein-resolved causal graph "
                "is deferred; non-detection of visible aggregates does not "
                "exclude all damage, and correlations with fluorescent markers "
                "do not establish universal causes. Supplements and raw data "
                "were not independently reanalysed. MED and Crossref notice "
                "fields were checked on 2026-10-12; a linked preprint or "
                "evaluation is not independent experimental support. Publisher "
                "access was incomplete for the 2017 and 2019 papers, so no "
                "exhaustive notice-absence claim is made. Pinned/current METPO "
                "and ignored/hidden repository searches found no exact term "
                "in the inspected sources; the pinned ontology is unchanged."
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
            "Added a decline-based replicative-aging phenotype with four primary "
            "DOIs and directly checked snippets; retained lifespan, terminology "
            "and strain limitations. Reserved 000709, v585 and 1066200-1066299 "
            "after ignored/hidden current-file, registered historical-tree and "
            "pending-PR checks. Examples and mechanism graph are deferred. "
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
         "Functional-decline sense; finite lifespan and old-pole identity alone are insufficient.", IDENTIFIER],
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
