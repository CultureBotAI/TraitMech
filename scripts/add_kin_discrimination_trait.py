"""Add kin discrimination with guarded, validated trait and proposal writes."""

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
SLUG = "kin_discrimination"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v592/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000716"
METPO_ID = "METPO:1066900"
TIMESTAMP = "2026-10-13T09:09:53Z"
DEFINITION_SOURCE = "DOI:10.1073/pnas.1512671112"
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
    "label": "kin discrimination",
    "definition": (
        "An ecological phenotype in which microbial cells preferentially "
        "associate with kin or exclude nonkin through differential interactions "
        "according to genetic similarity or relatedness."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": "DOI:10.1371/journal.pbio.0060287",
            "snippet": (
                "Our findings demonstrate that D. discoideum cells co-aggregate "
                "more with genetically similar than dissimilar individuals"
            ),
            "notes": (
                "Ostrowski et al. 2008, PMID:19067487; scientific abstract, "
                "publisher PDF page 1, contiguous span visually checked. "
                "Mixtures with AX4-GFP and natural-isolate dye controls support "
                "partial sorting during aggregation, not complete clonal "
                "exclusion. The measured endpoint is variation in fluorescent "
                "spore proportions among fruiting bodies; genetic distance "
                "uses 12 microsatellite loci, not genome-wide identity. "
                "Main text and all four figures were inspected; Figure 1 is "
                "hypothetical. Supplementary Tables S1 and S2 were read by "
                "text extraction. Main Methods names QS45, absent from the "
                "retrieved S1 strain table; no strain alias is inferred. "
                "Kin-selected benefit is an interpretation, not a measured "
                "fitness endpoint here. Natural provenance of every laboratory "
                "derivative and a molecular recognition mechanism remain "
                "unresolved. Native abstract verifier: VERIFIED."
            ),
        },
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "Overall the swarm interaction phenotype strongly correlated "
                "with phylogenetic relatedness, indicative of kin discrimination."
            ),
            "notes": (
                "Stefanic et al. 2015, PMID:26438858, PMC4653157; directly "
                "retrieved scientific abstract from Europe PMC with the "
                "namespace-qualified query EXT_ID:26438858 AND SRC:MED. "
                "Title, PMID and DOI were checked together. The authors define "
                "a conspecific scope and report relatedness-associated swarm "
                "merging versus boundary formation among sympatric Bacillus "
                "subtilis isolates. The separately reported root-colonization "
                "outcome is not a direct killing measurement. Full text, "
                "figures and supplements were inaccessible and are not "
                "claimed as inspected; indexed search passages were not "
                "used as excerpts or quantitative evidence. Native abstract "
                "verifier: VERIFIED. Linked PMID:26512099 is commentary, "
                "not a correction or experimental replication."
            ),
        },
        {
            "reference": "DOI:10.1128/mBio.00723-17",
            "snippet": (
                "The most closely related species are therefore treated just "
                "like intraspecies nonkin, demonstrating carryover of kin "
                "discrimination behaviors into interspecies dynamics."
            ),
            "notes": (
                "Lyons and Kolter 2017, PMID:28679746, PMC5573675; Results, "
                "Correlation of interaction phenotype with phylogeny, PDF "
                "page 6 / JATS s1.3. The comparison concerns interactions "
                "with B. subtilis NCIB3610: nearby species can be antagonized, "
                "while more distant lineages show varied outcomes. This is "
                "not a universal monotonic relation between distance and "
                "antagonism. Relatedness uses type-strain 16S, not whole-genome "
                "identity of every isolate. Swarm, biofilm and halo assays "
                "differ in medium and endpoint. Figure 2A and 2C assign "
                "WNC032 to different species; Data Set S1 identifies it as "
                "B. megaterium. No silent panel correction or taxon anchor "
                "is inferred. Actual Figures 2 and 4 and selected spreadsheet "
                "rows/totals were inspected, not all figures or raw assays. "
                "NLM version 1 PDF and JATS support the contiguous quote, "
                "also visually checked. Native verdict: NOT_IN_ABSTRACT, "
                "not relabeled VERIFIED. Shares an investigator with 2015; "
                "not an independent-laboratory replication."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "kin-discrimination-scope-and-hierarchy",
            "prompt": "Preserve relational phenotype scope without equating all recognition or cooperation.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Stefanic 2015 defines conspecific discrimination, whereas "
                "Lyons 2017 explicitly extends exclusion to nearby species. "
                "The record retains that attributed extension without a "
                "universal kin threshold, obligate killing, cognition or "
                "monotonic distance-response rule. Kin recognition, "
                "allorecognition and self/nonself discrimination are not "
                "asserted as exact synonyms. An interaction phenotype is "
                "required; a recognition locus, allele match, isolated "
                "pairing or spatial assortment alone is insufficient. "
                "Recognition-allele specificity, measured relatedness proxies "
                "and genome-wide relatedness must not be conflated. "
                "METPO:1000059 phenotype is the conservative parent. Mutualism "
                "(traitmech:000041) requires reciprocal benefit; biofilm "
                "formation (traitmech:000053) is neither necessary nor "
                "sufficient. Contact-dependent outer membrane exchange "
                "(traitmech:000650) is material transfer, and its existing "
                "negative kin-discrimination evidence remains a boundary, "
                "not a parent gap. Heterokaryon incompatibility "
                "(traitmech:000606) concerns postfusion restriction and is "
                "not automatically equivalent or reparented. Predation "
                "requires trophic benefit; DNA self/nonself defense has a "
                "different target and endpoint. No organism-level "
                "disjointness is implied."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "kin-discrimination-evidence-and-mechanism-limits",
            "prompt": "Resolve strain, assay and source gaps before assigning canonical taxa or molecular mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The QS45 strain-table gap and WNC032 figure-label conflict "
                "remain unresolved. The 2015 scientific abstract was read "
                "directly, but full text was not. The 2017 scientific abstract "
                "and IMPORTANCE summary were distinguished; the excerpt is "
                "from Results, not either abstract. Selected supplemental "
                "spreadsheet checks are not raw-image reanalysis or a "
                "statistical replication; supplementary EPS figures remain "
                "unread. Bounded MED, PLOS and NLM metadata checks are not "
                "exhaustive clearance of corrections or retractions; some "
                "publisher routes were inaccessible. No canonical taxa, "
                "exact external mappings, protein examples or causal graph "
                "are asserted. Allele-specific adhesion in engineered "
                "systems requires separate provenance and mechanism review, "
                "not inference of natural species-wide possession. Source "
                "URLs, hashes, access limits and native snippet outcomes "
                "are retained in the source-verification sidecar."
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
            "Added kin discrimination with three DOI-backed contiguous snippets "
            "and bounded assay, source and hierarchy discussions. Reserved "
            "000716, v592 and 1066900-1066999 after ignored/hidden current-file, "
            "retained-history, independent-copy and open/draft PR checks; "
            "numeric false positives were adjudicated. No exact active METPO "
            "counterpart identified in inspected sources. No taxa or causal "
            "graph inferred; prior records unchanged. Timestamp is observed "
            "post-audit acceptance, not an estimated write time."
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
         "|".join([f"TraitMech:data/traits/ecology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Relational interaction phenotype; no universal distance threshold or molecular recognition claim.",
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
