"""Add nematode-attracting activity through guarded, validated writes."""

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
SLUG = "nematode_attracting_activity"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v597/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000721"
METPO_ID = "METPO:1067400"
TIMESTAMP = "2026-10-13T23:01:02Z"
DEFINITION_SOURCE = "DOI:10.7554/eLife.20023"
BACTERIAL_SOURCE = "DOI:10.1038/ismej.2015.134"
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
    "label": "nematode-attracting activity",
    "definition": (
        "A physiological capability of a microorganism to elicit directed "
        "movement of nematodes toward itself or substances it produces."
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
                "C. elegans and other nematodes were attracted to volatile "
                "compounds produced by A. oligospora."
            ),
            "notes": (
                "Hsueh et al. 2017, PMID:28098555, scientific abstract; native "
                "VERIFIED and direct original XML match, not an editorial digest. "
                "The producer is Arthrobotrys oligospora CBS 115.81. The 2 h "
                "assay physically separates fungal material from nematodes and "
                "compares fungal volatiles with medium controls. Actual Figure "
                "1B/D inspected: adult responses are stronger than L1/dauer "
                "responses, and not every tested nematode species is attracted. "
                "Figure 1D, not the capture image 1E, supplies the multispecies "
                "behavioral comparison. Sodium azide retains arrivals; it is "
                "not microbial killing evidence. No universal host range, "
                "evolutionary adaptation or exact pheromone mimicry is inferred."
            ),
        },
        {
            "reference": BACTERIAL_SOURCE,
            "snippet": (
                "We showed that C. elegans is attracted to L. paracasei grown "
                "on citrate or yuzu media."
            ),
            "notes": (
                "Choi et al. 2016, online 2015, PMID:26241504, Discussion opening "
                "paragraph; native NOT_IN_ABSTRACT and direct publisher HTML "
                "match. Lactobacillus paracasei YSM0385-bearing plugs on the lid "
                "are compared with matched bacteria-free medium in a 1 h adult "
                "C. elegans N2 assay. Citrate medium includes glucose plus "
                "citrate. Actual Figures 1-4 and HTML Table 1 inspected; the "
                "table's wild co-occurrence observations alone do not establish "
                "attraction. Sodium azide retains arrivals, not bacterial "
                "toxicity. Wild isolate Y091 is only Lactobacillus sp., not "
                "an inferred L. paracasei assignment. Field recruitment, "
                "microbial benefit and nematode fitness benefit are not adopted."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "nematode-attraction-scope-and-hierarchy",
            "prompt": "Refine the hierarchy while preserving the microbial actor and nematode movement endpoint.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is the microorganism's attracting capability, not its own "
                "chemotaxis or a nematode's sensory trait. Passive retention, "
                "co-occurrence, trapping, paralysis, killing or consumption "
                "alone are insufficient; attraction need not imply any of "
                "those outcomes. Neither infection nor predatory intent is "
                "required. Phenotype METPO:1000059 is the conservative parent; "
                "the trap-formation, fungal-nematophagy and lethal-nematicidal "
                "records are related, not equivalents or necessary parents. "
                "Pinned/current METPO annotations and templates yielded no "
                "exact active or deprecated counterpart in the documented "
                "screen. v597 proposes the missing class. No exact synonyms, "
                "xrefs or organism-level disjointness are asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "nematode-attraction-source-and-mechanism-limits",
            "prompt": "Resolve source discrepancies and strain provenance before adding canonical taxa or microbial mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Hsueh's five-compound exclusivity caption conflicts with a "
                "2-methyl-1-butanol medium-control signal in its source workbook; "
                "no exclusive chemical signature is adopted. The published "
                "review exchange questions sex-pheromone mimicry and adaptation; "
                "host neuronal genetics do not establish fungal genes. Choi's "
                "host odr-10 allele is ky32 in Methods/captions but ky10 in "
                "Results; no correction is inferred. Its shared supplement "
                "link yields a colony-count image, not a separately verified "
                "S2 diacetyl calibration. Choi's typeset PDF and complete raw "
                "statistics were not audited. Strain provenance and authority "
                "taxonomy remain unchecked for canonical-example purposes. "
                "No shared microbial mechanism, proteins or causal graph is "
                "asserted. Source hashes, native outcomes, bounded notice "
                "checks and inspection limits are retained in the source "
                "verification sidecar."
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
            "Added a microbial nematode-attracting capability with two "
            "DOI-backed primary studies and directly matched snippets. "
            "Retained host/stage, growth-medium and source discrepancies; "
            "distinguished attraction from microbial taxis, trapping, killing "
            "and feeding. Reserved 000721, v597 and 1067400-1067499 after "
            "ignored/hidden current-copy, retained-history and open/draft "
            "PR checks with numeric false positives adjudicated. No exact "
            "active METPO counterpart was identified in the inspected scope. "
            "Other records remain unchanged. Timestamp is observed acceptance "
            "after source and allocation assessment, not the later file write."
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
         "|".join([f"TraitMech:data/traits/physiology/{SLUG}.yaml", record["definition_source"]]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Microbial attracting capability; nematode movement, not trapping or killing.",
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
