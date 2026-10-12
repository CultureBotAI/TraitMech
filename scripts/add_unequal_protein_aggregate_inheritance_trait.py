"""Add a quantity-qualified aggregate-inheritance phenotype through the validated writer."""

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
SLUG = "unequal_protein_aggregate_inheritance"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v587/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000711"
METPO_ID = "METPO:1066400"
DEFINITION_SOURCE = "DOI:10.1371/journal.pbio.1001886"
BACTERIAL_RETENTION = "DOI:10.1073/pnas.0708931105"
SHARED_INHERITANCE = "DOI:10.1111/mmi.14228"
TIMESTAMP = "2026-10-12T14:38:12Z"
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
    "label": "unequal protein aggregate inheritance at cell division",
    "definition": (
        "A physiological phenotype in which microbial cell division recurrently "
        "yields sibling cells with unequal numbers or amounts of inherited protein aggregates."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": BACTERIAL_RETENTION,
            "snippet": (
                "their position in the mother cell determines which offspring "
                "inherits the inclusion body and where it will be located within it"
            ),
            "notes": (
                "Lindner et al. 2008, PMID:18287048, PMC2268587; Results, Inclusion "
                "Bodies Are Formed in Discrete Cellular Positions and Accumulate "
                "in Old Poles Under Nonstressing Conditions. Primary PMC Results "
                "and Methods directly read. The quoted position is that of an "
                "IbpA-YFP focus. MGAY is an engineered MG1655 reporter strain, "
                "grown on LB-agarose at 37 C without imposed stress. Figure 2 is "
                "the inspected localization measurement; Figure 3 is an inspected "
                "lineage schematic, not another experiment. Pole identity changes "
                "across divisions. The observations support inheritance and eventual "
                "older-pole accumulation; they do not establish active transport, "
                "universal aggregate toxicity or a natural canonical exemplar. "
                "Supplements were not inspected. The full-text span retains the "
                "native abstract resolver verdict NOT_IN_ABSTRACT."
            ),
        },
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "We experimentally confirmed that fusion increases segregation "
                "asymmetry, for a range of stresses, and identified Hsp16 as a fusion factor."
            ),
            "notes": (
                "Coelho et al. 2014, PMID:24936793, PMC4061010; scientific abstract, "
                "not Author Summary. Primary XML and actual Figures 3, 4 and S4 "
                "were inspected. Hsp104-GFP fission-yeast imaging supports stress-"
                "associated unequal inheritance without consistent old/new-pole "
                "bias. Figure 3C measures an absolute sibling difference in "
                "aggregate-associated fluorescence, not concentration; S4I measures "
                "count asymmetry. Figure 4B is fusion and 4C is nucleation: the "
                "caption reverses them. A Results pointer to 4C for stress-dependent "
                "asymmetry disagrees with the plotted endpoints. Figure 3C describes "
                "continuous 40 C, whereas Methods describes 40 C for one hour "
                "followed by 37 C; this remains unresolved. Text S1 experimental "
                "methods and strain table were text-extracted, not visually rendered. "
                "No universal transport, death threshold or rejuvenation mechanism "
                "is inferred. The scientific-abstract span matches the native "
                "resolver text (VERIFIED)."
            ),
        },
        {
            "reference": SHARED_INHERITANCE,
            "snippet": (
                "Noticeably, stalked cells always inherited more aggregates (75%) "
                "than swarmer cells (25%)."
            ),
            "notes": (
                "Schramm et al. 2019, PMID:30779464, PMC6850343; Results, The "
                "aggregate load does not sort to swarmer or stalked daughter cells "
                "in C. crescentus. Primary XML Results, Discussion and relevant "
                "Methods were read; actual Figure 6 was inspected. DnaK-mVenus, "
                "delta-clpB cells recovered at 30 C after 10 minutes at 40 C. "
                "Figure 6G reports aggregate allocation across daughter cell types "
                "over successive divisions, not the fraction of all sibling pairs "
                "with unequal counts. Figure 6F measures projected cell area, not "
                "volume. Unequal shared inheritance is compatible with the broad "
                "phenotype; it contradicts neither sharing nor a stable allocation "
                "ratio. The paper limits universal exclusive old-pole retention, "
                "not every form of quantitative inequality. Supplements and "
                "independent strain provenance were not inspected; no natural "
                "canonical example is asserted. The full-text span retains the "
                "native abstract resolver verdict NOT_IN_ABSTRACT."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "unequal-aggregate-inheritance-operational-scope",
            "prompt": "Assess the quantity-qualified definition and the level of inheritance evidence.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Require repeated lineage or population observations under stated "
                "conditions, not a single unequal sibling pair. Retain aggregate "
                "count versus fluorescence-derived amount, the time of measurement, "
                "reporter, strain and detection limits. Amount is not concentration; "
                "cell area is not volume. Within-pair inequality, cell-type allocation "
                "bias and complete aggregate exclusion are distinct readouts. Sharing "
                "between daughters need not be equal, and unequal inheritance need "
                "not favor a fixed pole or cell type. No universal threshold or "
                "programmed asymmetry is specified. Bare asymmetric segregation "
                "has narrower source usages and is not asserted as an exact synonym. "
                "Aggregate presence, aggrephagy, heat-shock response, morphological "
                "division asymmetry, replicative aging and functional rejuvenation "
                "are not equivalent traits or demonstrated narrower parents. "
                "Use METPO:1000059 phenotype without reparenting existing records."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "unequal-aggregate-inheritance-mechanism-and-source-limits",
            "prompt": "Resolve assay discrepancies, strain provenance and mechanisms before extending this first-pass record.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "This phenotype does not imply active transport, toxic damage, "
                "functional decline or rejuvenation. An aggregate-free descendant "
                "alone establishes none of those mechanisms or outcomes. The "
                "engineered reporter and deletion contexts remain qualified evidence, "
                "not natural canonical examples. No shared protein mechanism, graph "
                "or external equivalence is asserted. Coelho Figure 4 panel-label "
                "and Figure 3C versus Methods temperature discrepancies remain open; "
                "actual plotted endpoints are distinguished from text pointers. "
                "Primary source/metadata notice checks on 2026-10-12 were bounded "
                "by access; they do not prove exhaustive notice absence."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-12",
        },
        {
            "discussion_id": "unequal-aggregate-inheritance-historical-metpo-match",
            "prompt": "Retain the deprecated aggregate lexical hit without asserting identity or reusing its ID.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Pinned and current released METPO contain METPO:1000011, obsolete "
                "aggregate, marked deprecated and below ObsoleteClass. It has an "
                "IAO:0000231 annotation to OMO:0001000, but no definition, replacement "
                "or consider annotation in the inspected releases. Its original "
                "scope and reason-code interpretation remain unresolved. A lexical "
                "aggregate hit does not establish equivalence to unequal protein "
                "aggregate inheritance; this literature-defined phenotype was "
                "independently accepted. Do not reactivate 1000011 or include it "
                "as an exact xref. Ignored/hidden available-file and registered "
                "historical-tree searches, pending PRs and released RDF found no "
                "exact trait in the inspected scope; this is not discovery exhaustion."
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
            "Added unequal protein aggregate inheritance at cell division with "
            "three primary DOI references and checked snippets. Retained quantity, "
            "population, assay and historical-METPO scope limits. Reserved 000711, "
            "v587 and 1066400-1066499 after ignored/hidden, registered historical-tree "
            "and pending-PR checks, distinguishing an editor namespace envelope "
            "from narrower reservations. Examples and mechanism graph deferred. "
            "Existing records unchanged; timestamp is the observed UTC curation decision."
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
         "Inherited count or amount, not concentration, fixed pole bias or rejuvenation.", IDENTIFIER],
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
