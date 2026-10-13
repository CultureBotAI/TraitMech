"""Add extracellular-trail-based spatial memory with guarded, validated writes."""

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
SLUG = "extracellular_trail_based_spatial_memory"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v591/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000715"
METPO_ID = "METPO:1066800"
TIMESTAMP = "2026-10-13T06:32:45Z"
DEFINITION_SOURCE = "DOI:10.1073/pnas.1215037109"
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
    "label": "extracellular-trail-based spatial memory",
    "definition": (
        "A physiological phenotype in which a microorganism's subsequent spatial "
        "exploration is guided by persistent extracellular trails deposited "
        "during earlier movement."
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
                "When one arm contained extracellular slime, 39 of 40 plasmodia "
                "chose the blank agar arm"
            ),
            "notes": (
                "Reid et al. 2012, PMID:23045640, PMC3491460; Results opening "
                "paragraph, printed page 17490 / PDF page 1. Cultured Physarum "
                "polycephalum avoided previously deposited slime in a Y maze. "
                "Same-stock coatings do not demonstrate individual recognition "
                "of one's own trace. In the separate U-trap experiment, 23/24 "
                "plasmodia on blank agar versus 8/24 on slime-coated agar reached "
                "the target within 120 hours. Coating masks newly informative "
                "trails; it does not abolish secretion or lesion internal memory. "
                "Success, completion time among successful trials, speed, path "
                "length and revisitation are distinct endpoints. No-trap and "
                "speed controls do not exclude every environmental confound. "
                "Main Methods, Results, Discussion and all four figures were "
                "inspected in an author-hosted publisher-formatted PDF bearing "
                "a 2012 download stamp, not verified as the current corrected "
                "VoR. Supplements and raw data were not assessed. Southern "
                "Biological Supplies culture provenance remains unresolved. "
                "The contiguous result span was text-matched and visually checked."
            ),
        },
        {
            "reference": "DOI:10.1088/1361-6463/aa87df",
            "snippet": (
                "Our results suggest that the external memory has an adaptive "
                "advantage in \u2018open\u2019 and simple bounded environments."
            ),
            "notes": (
                "Smith-Ferguson et al. 2017; scientific abstract, printed page 1 / "
                "PDF page 2. This is the authors' interpretation of maze "
                "performance, not a measured fitness or natural-selection "
                "endpoint. Within 72 hours, blank versus extracellular-slime "
                "conditions yielded success in 24/24 versus 9/24 open trials, "
                "12/15 versus 4/12 simple-maze trials and 11/17 versus 11/13 "
                "complex-maze trials; the last comparison showed no significant "
                "benefit. Completion times conditional on success were not "
                "significantly different. Escaped trials were excluded; split "
                "decisions used the dominant front. Printed page 6 pairs the "
                "same chi-square 0.802 with P=0.004 and P=0.371; this discrepancy "
                "is unresolved. Figure 8 is illustrative, not quantified "
                "trajectory evidence. Main Methods, Results, Discussion, "
                "Conclusion and all eight figures were inspected; supplements "
                "were not. The author-hosted PDF bears a 2017 download stamp, "
                "not verified current VoR equivalence. This study shares authors "
                "with Reid 2012, not an independent-laboratory replication."
            ),
        },
        {
            "reference": "DOI:10.1073/pnas.2312611121",
            "snippet": (
                "In accordance with the literature, we observe that plasmodia "
                "generally avoid previously visited areas marked by their slime trail"
            ),
            "notes": (
                "Troger et al. 2024, PMID:38517977, PMC10990088; Results, "
                "Quantifying Run-and-Tumble and Self-Avoiding Behavior, page 3. "
                "The authors report their own Physarum observations, not only "
                "a background citation. Actual trajectories, including Figure "
                "2A, are distinct from simulated-model panels. Page 5 describes "
                "14 trajectories divided into groups of nine each; Figure 4 "
                "instead gives seven small and seven large. The discrepancy "
                "remains unresolved. The 0.65 square-millimeter median is a "
                "cohort split, not a universal threshold. Small plasmodia can "
                "cross trails; a modeled three-hour forgetting time is not a "
                "measured chemical half-life or internal-memory duration. "
                "Main text, Methods and all four main figures were inspected "
                "in the author-hosted publisher-formatted PDF with a March "
                "2024 download stamp, not verified current corrected VoR "
                "equivalence. Publisher supplements and raw data were not "
                "reanalyzed. This different laboratory's assay is not a "
                "replication of the earlier maze experiments; no universal "
                "molecular receptor is established."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "trail-memory-scope-and-hierarchy",
            "prompt": "Keep external trace-guided exploration distinct from internal memory and universal trail avoidance.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This operational phenotype concerns spatial information "
                "persisting outside the microorganism. It does not require "
                "always avoiding a trail, improved navigation in every setting, "
                "individual self-recognition, or internal recall. Carbon-source "
                "memory (traitmech:000706), acquired stress-resistance memory "
                "(traitmech:000712), enhanced transcriptional reactivation "
                "memory (traitmech:000713) and behavioral habituation "
                "(traitmech:000714) have different endpoints. Negative "
                "autotropism (traitmech:000603) concerns germ-tube or hyphal "
                "orientation. Collective bacterial predation (traitmech:000701) "
                "concerns coordinated killing and feeding, despite a trail "
                "mention. Contact-dependent outer membrane exchange "
                "(traitmech:000650) concerns actual intercellular exchange. "
                "METPO:1000059 phenotype is the conservative parent pending "
                "hierarchy review; local chemotaxis has a flagellar-specific "
                "definition and is not a universal parent. Generic memory, "
                "learning, stigmergy and extracellular polymer production are "
                "not exact synonyms. Psl-biased visitation and community growth "
                "history require separate scope and evidence assessments."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "trail-memory-source-and-mechanism-limits",
            "prompt": "Resolve source versions, assay discrepancies and culture provenance before assigning taxa or mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Coated-versus-blank substrates manipulate spatial trace "
                "information along with the environment, not exclusively a "
                "memory molecule. The 2017 significance-statistic discrepancy "
                "and 2024 group-size discrepancy remain visible source gaps. "
                "The 2024 arXiv v1 was posted after journal publication; its "
                "seven-per-group wording and differing illumination details "
                "do not silently correct the publisher-formatted PDF. "
                "Supplement illustrations do not establish crossing frequencies. "
                "Bounded Crossref/MED and publisher checks do not establish "
                "exhaustive absence of notices or corrected-version equivalence. "
                "The evidence concerns cultured Physarum, not species-wide "
                "possession or all microbes. Natural culture provenance remains "
                "unverified. No canonical taxa, exact external mappings, "
                "protein examples or molecular causal graph are asserted. "
                "Unknown trail components, sensory mechanisms, unread "
                "supplements and raw-data reanalysis remain research gaps. "
                "Source hashes, access limits and actual native snippet-verifier "
                "outcomes are retained in the source-verification sidecar."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "trail-memory-historical-identity",
            "prompt": "Retain unresolved historical adaptation and chemotaxis identity without reviving deprecated identifiers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Pinned and inspected current METPO graphs mark METPO:0000248 "
                "and METPO:000249 Microbial Adaptation, METPO:1000004 adaptation "
                "and METPO:1000062 chemotaxis deprecated. Inspected subjects "
                "have no replacement or consider annotations; OMO:0001000 "
                "reasons are provisional under open METPO issue 521. Original "
                "historical scopes remain unresolved. Neither biological "
                "invalidity nor exact equivalence follows from their labels "
                "or deprecation reasons. This qualified external-trace phenotype "
                "is accepted independently from primary evidence. Ignored and "
                "hidden current files, available tracked history, independent "
                "copies, pending changes and inspected ontology graphs revealed "
                "no exact active record within the documented scope. No "
                "historical exact mapping is asserted. Existing records and "
                "the pinned ontology remain unchanged; discovery is not exhausted."
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
            "Added extracellular-trail-based spatial memory with three primary "
            "DOI sources and contiguous snippets. Retained assay, version, "
            "mechanism and historical-identity limits. Reserved 000715, v591 "
            "and 1066800-1066899 after scoped ignored/hidden, retained-history, "
            "independent-copy and pending-PR checks; numeric false positives "
            "were explicitly adjudicated. No canonical taxa or causal graph; "
            "existing records unchanged. Timestamp is the observed UTC "
            "post-audit confirmation, not an estimated write time."
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
         "External trace-guided exploration; no universal avoidance or internal recall claim.",
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
