"""Add behavioral habituation through the validated, fail-closed writer."""

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
SLUG = "behavioral_habituation"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v590/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000714"
METPO_ID = "METPO:1066700"
TIMESTAMP = "2026-10-13T04:41:26Z"
DEFINITION_SOURCE = "DOI:10.1098/rspb.2016.0446"
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
    "label": "behavioral habituation",
    "definition": (
        "A physiological phenotype in which repeated stimulation produces an "
        "experience-dependent decrease in a microbial organism's behavioral "
        "response that is not attributable solely to sensory adaptation or "
        "motor fatigue."
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
                "The Q and CAF slime moulds crossing a bridge containing quinine "
                "or caffeine for the sixth time showed reduced aversive behaviour."
            ),
            "notes": (
                "Boisseau et al. 2016, PMID:27122563, PMC4855389; page 4, "
                "Results (b), Test phase 1. Q and CAF denote cultured Physarum "
                "polycephalum plasmodia repeatedly exposed to quinine or caffeine "
                "bridges. Five daily exposures precede same/alternate-repellent "
                "tests; two plain-agar days precede retesting. Contact latency, "
                "crossing time and shape are different readouts. Caffeine does "
                "not show every quinine effect: initial crossing time was not "
                "slower than control, and recovery was incomplete. Residual "
                "aversiveness remains. Alternate-repellent responses support "
                "stimulus specificity, not universal exclusion of every confound. "
                "Main Methods, Results, Discussion and all five figures were "
                "inspected in a public publisher-formatted PDF bearing a 2016 "
                "download stamp, not verified as the current corrected VoR. "
                "Supplementary statistics and raw data were not assessed. "
                "The contiguous quote crosses PDF columns; direct text and "
                "visual checks agree. Native abstract lookup: NOT_IN_ABSTRACT."
            ),
        },
        {
            "reference": "DOI:10.1016/j.cub.2025.05.071",
            "snippet": (
                "the response to the low force stimuli shows extensive habituation "
                "even though the response to the alternating high force stimuli does not."
            ),
            "notes": (
                "Rajan and Marshall 2025, PMID:40562036, PMC13499368; "
                "Figure 4F caption, concluding result clause in retained PMC "
                "author-manuscript HTML. Figure 4F is an experimental contraction "
                "response in cultured Stentor coeruleus, not the adjacent model "
                "panel. Preserved stronger-stimulus responses argue against "
                "general motor exhaustion. The caption describes identical "
                "control timing, while Methods describes one low-force control "
                "tap per minute versus alternating forces at one total tap per "
                "minute; exact cadence equivalence remains unresolved. Figure "
                "4I uses intervening low-force stimulation, not a stimulus-free "
                "rest; Figure 5 separately tests recovery after training. "
                "Anchored healthy nondividing cells were selected from Ward's "
                "cultures; field-of-view denominators vary. Experimental Results, "
                "relevant Methods and actual Figures 4-7 were inspected. "
                "Receptor internalization is modeled, not an identified molecular "
                "mechanism. Supplements and simulations were not reanalyzed. "
                "Native abstract lookup: NOT_IN_ABSTRACT; the exact full-text "
                "caption match is a separate check."
            ),
        },
        {
            "reference": "DOI:10.1016/j.cub.2026.03.080",
            "snippet": (
                "For cells treated with either cycloheximide or puromycin, the "
                "primary effect on learning was accelerating habituation (Figure 1C, 1E)."
            ),
            "notes": (
                "Rajan et al. 2026, PMID:42025171, PMC13192338; Results S3, "
                "retained PMC author manuscript. Stentor contraction assays "
                "compare drug-treated and vehicle cultures under repeated "
                "mechanical stimulation. Figure 1C uses puromycin with two-hour "
                "pretreatment; Figure 1E describes 12-hour cycloheximide "
                "pretreatment, unlike general short-term Methods prose. Dose, "
                "stimulus strength and cadence differ; conditions are not "
                "interchangeable. Drug effects do not prove universally "
                "protein-synthesis-independent learning. Relevant Results and "
                "Methods and actual Figures 1, 3, 4 and 6 were inspected, not "
                "all omics analyses or supplements. RNAi and pharmacology retain "
                "off-target, anchoring, feeding and subculture limitations. "
                "SteCoe_6763 recovery differences were not significant. Figure "
                "6 follows division during continuing stimuli, not retention "
                "after withdrawal. Results and Methods point to different "
                "supplementary electrical-control panels. This follow-up shares "
                "a laboratory with the 2025 study, not an independent replication. "
                "Native abstract lookup: NOT_IN_ABSTRACT; directly matched Results quote."
            ),
        },
        {
            "reference": "DOI:10.1016/j.nlm.2008.09.012",
            "snippet": (
                "Habituation is defined as a behavioral response decrement that "
                "results from repeated stimulation and that does not involve "
                "sensory adaptation/sensory fatigue or motor fatigue."
            ),
            "notes": (
                "Rankin et al. 2009, PMID:18854219, PMC2754195; section 2, "
                "page 136 (PDF page 2), complete opening definition. This "
                "consensus review supports operational terminology, not a "
                "microbial experiment or independent replication. Its nervous-"
                "system framing is not imposed on non-neural microbes. The "
                "public institutional PDF was directly read and pages 2-4 "
                "visually inspected. PDF ligatures are expanded and whitespace "
                "folded for matching; no paraphrase is substituted. Partial "
                "recovery is allowed. Responding to a novel stimulus is not "
                "itself dishabituation, which restores the original response. "
                "The behavioral criteria are not a demonstrated common "
                "molecular mechanism. Source-qualified MED identity was checked; "
                "its absent commentCorrectionList is not exhaustive notice clearance."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "habituation-scope-and-hierarchy",
            "prompt": "Retain a behavioral endpoint and distinguish neighboring uses of adaptation.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Repeated-stimulus decrement alone is insufficient: evaluate "
                "sensory adaptation, motor fatigue, injury/toxicity, selection "
                "and depletion alternatives in the actual assay. Specificity "
                "and recovery provide operational support without identifying "
                "all underlying mechanisms. Rankin 2009 frames habituation in "
                "neural behavioral terms; Rajan 2025 distinguishes that usage "
                "from cellular adaptation while modeling related receptor "
                "dynamics. This record concerns microbial behavior, not a "
                "categorical ban on shared molecular machinery. No fixed time, "
                "curve, complete recovery, dishabituation or all ten hallmarks "
                "are required in every experiment. Response to a stronger "
                "stimulus is not itself dishabituation. Carbon-source memory "
                "(traitmech:000706), acquired stress-resistance memory "
                "(traitmech:000712), enhanced transcriptional reactivation "
                "memory (traitmech:000713), anticipation, bet hedging and "
                "nutrient adaptation have distinct endpoints. Chemotaxis is "
                "not a parent of every behavioral assay. METPO:1000059 phenotype "
                "is the conservative parent; generic learning, memory and "
                "adaptation are not asserted as exact synonyms."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "habituation-evidence-and-mechanism-limits",
            "prompt": "Resolve source discrepancies and culture provenance before adding taxa or mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Different taxa and assays support the phenotype, not independent "
                "replication of each experiment. Laboratory culture provenance "
                "has not been independently resolved for natural canonical "
                "taxa; no species-wide assignment follows. Unread supplements, "
                "raw data and statistical reanalysis remain gaps. The 2025 "
                "control cadence, 2026 cycloheximide timing and electrical-"
                "control locators remain unresolved source discrepancies. "
                "Retained public PDFs and author manuscripts are not verified "
                "equivalent to current corrected publisher versions. Bounded "
                "MED/Crossref checks are not proof of notice absence. Modeled "
                "receptor internalization, exploratory omics and drug/RNAi "
                "effects do not justify a universal protein-resolved mechanism. "
                "No causal graph, protein examples, canonical taxa or exact "
                "external mappings are asserted. Access failures, source "
                "hashes and actual snippet-verifier results are in the sidecar."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "habituation-historical-identity",
            "prompt": "Reconcile deprecated adaptation neighbors without reviving their identifiers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Pinned and inspected current METPO graphs mark METPO:1000004 "
                "adaptation, METPO:1000005 adaptive trait, METPO:0000248 and "
                "METPO:000249 Microbial Adaptation deprecated below ObsoleteClass, "
                "with OMO:0001000 and no inspected replacement or consider "
                "annotations. METPO issue 521 disputes the mechanically "
                "assigned reasons. Original historical scopes remain unresolved; "
                "labels do not prove equivalence or nonequivalence. This "
                "operational behavioral phenotype is accepted independently "
                "from primary evidence, not by reviving an obsolete term or "
                "inferring biological invalidity. Available ignored/hidden "
                "files, retained tracked history, pending changes, ontology "
                "graphs and live corpus semantics revealed no exact active "
                "record in the inspected scope. No historical exact mapping "
                "is asserted. The pinned ontology and existing records remain "
                "unchanged; discovery is not exhausted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added behavioral habituation with three primary DOI sources and "
            "one terminology review, each with a contiguous snippet. Qualified "
            "assay, version, mechanism and historical-identity limitations. "
            "Reserved 000714, v590 and 1066700-1066799 after scoped ignored/hidden, "
            "retained-history, independent-copy and pending-PR checks, with "
            "numeric false positives explicitly adjudicated. Existing records "
            "unchanged; no canonical taxa or causal graph. Timestamp is the "
            "observed UTC post-audit confirmation, not an estimated write time."
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
         "Behavioral response decrement; assay-specific controls and mechanism limits retained.",
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
