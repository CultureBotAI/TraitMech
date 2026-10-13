"""Add nutritional fungal mycoparasitism through guarded, validated writes."""

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
SLUG = "nutritional_fungal_mycoparasitism"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v593/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000717"
METPO_ID = "METPO:1067000"
TIMESTAMP = "2026-10-13T11:20:51Z"
DEFINITION_SOURCE = "DOI:10.1139/b95-389"
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
    "label": "nutritional fungal mycoparasitism",
    "definition": (
        "An ecological phenotype in which a fungus obtains nutrients at the "
        "expense of another fungus, either from the living host or after killing it."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "The term mycoparasitism applies strictly to those relationships "
                "in which one living fungus acts as a nutrient source for another"
            ),
            "notes": (
                "Jeffries 1995 review; scientific abstract directly retrieved "
                "from https://kar.kent.ac.uk/19621/. This strict sense contrasts "
                "with broader fungicolous usage in the same abstract. Selected "
                "main text and actual PDF pages 1 and 3 support detrimental "
                "nutrition with either a living host or killing before use. "
                "The record restricts actor and host to fungi, excluding "
                "historically grouped oomycetes. The review supplies terminology, "
                "not an independent experiment. Not every figure or table was "
                "inspected. Native abstract verifier: UNRESOLVED; the direct "
                "institutional excerpt was separately matched, not relabeled VERIFIED."
            ),
        },
        {
            "reference": "DOI:10.1002/rcm.6131",
            "snippet": (
                "In dual-culture the mycelia of T. atroviride which remained in "
                "direct contact with labeled A. mellea showed an increased \u03b4(13)C value"
            ),
            "notes": (
                "Pellegrini et al. 2012, PMID:22302490; directly retrieved "
                "scientific abstract, Results, using DOI and SRC:MED together. "
                "Title, DOI and PMID agree. After 29 days in contact, the "
                "reported carbon isotope value was 66.4 per mille versus "
                "-26.6 per mille with unlabeled host. This supports host-derived "
                "carbon assimilation, not by itself host killing, a penetration "
                "mechanism or exclusion of all alternative transfer routes. "
                "The journal full text was not retrieved; the restricted "
                "institutional deposit was not bypassed. The bacterial "
                "comparator is not an example of this fungal-actor trait. "
                "Native abstract verifier: VERIFIED."
            ),
        },
        {
            "reference": "DOI:10.1016/j.apsoil.2012.12.005",
            "snippet": "Only T. harzianum maintained mycoparasitic activity in the soil microcosm",
            "notes": (
                "Pellegrini et al. 2013; scientific abstract directly read at "
                "https://iris.unipv.it/handle/11571/604013?mode=complete. Native "
                "verifier: VERIFIED via AGR:IND500606635, not PubMed. The "
                "author-deposited Corneo thesis chapter identifies this DOI; "
                "its version is not presumed identical to the unread journal "
                "full text. Its experiment selects three microorganisms: "
                "the positive soil result concerns a sterile microcosm at "
                "20 C after 29 days, followed by three-day culture-out before "
                "isotope measurement, not direct field flux or all 158 isolates. "
                "Dual-culture enrichment accompanies growth inhibition; the "
                "host viability endpoint comes from a separate broth assay. "
                "Washing and host-specific PCR address contamination without "
                "excluding every route of carbon transfer. Leakage versus "
                "direct parasitism remains partly interpretive. Shares all "
                "six authors with 2012, not independent-laboratory replication."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "nutritional-fungal-mycoparasitism-scope-and-hierarchy",
            "prompt": "Resolve the broader hierarchy without importing persistent association or broad fungicolous usage.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Nutrition at host expense is required; mere co-occurrence, "
                "fungicolous association, antagonism or utilization of already "
                "dead material does not establish it. Killing, penetration, "
                "obligacy and a single mechanism are not universal requirements. "
                "The unqualified mycoparasitism label is not an exact synonym. "
                "Local parasitism (traitmech:000043) inherits persistent physical "
                "association from symbiosis (traitmech:000040); that narrower "
                "local umbrella is not automatically applicable to destructive "
                "encounters included by Jeffries. METPO:1000059 phenotype "
                "is retained pending hierarchy review. Bacterial mycophagy "
                "(traitmech:000696) has a bacterial actor; microbial haustorium "
                "formation (traitmech:000663) is a structural phenotype, neither "
                "necessary nor sufficient for this nutrition. Saprotrophy "
                "(traitmech:000055) alone does not establish attack on a living "
                "host; no organism-level disjointness is implied. Pinned and "
                "current METPO broad lexical matches (0000261, 000262, 1000125, "
                "1000197, 1000198, 1000227) are deprecated, with no replacement "
                "or consider annotation observed. Their OMO:0001000 reason "
                "does not disprove the biology or license identifier reuse. "
                "None is an exact active counterpart; historical IDs are not xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-13",
        },
        {
            "discussion_id": "nutritional-fungal-mycoparasitism-source-and-mechanism-limits",
            "prompt": "Resolve source discrepancies and isolate provenance before assigning canonical taxa or a causal mechanism.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The 2013 abstract reports inhibition of 80 +/- 0.19%; thesis "
                "Results gives 88 +/- 0.24% and Table 1 gives 80 +/- 0.29%. "
                "Fluorogenic-assay sampling days differ between Methods and "
                "Figure 2; soil-control isotope values differ between Results "
                "and Table 3. A no-difference statement is paired with P < 0.05, "
                "and abstract versus Results pathogen exclusions differ. These "
                "are unresolved, not silently harmonized. Selected thesis "
                "Methods, Results, Discussion and actual pages 69, 73, 75, 86 "
                "and 89 were inspected, not all figures, tables or raw data. "
                "Ground inoculum may include nonviable material; no killed-host "
                "control was inspected, which is not proof none exists. Table "
                "accessions identify BLAST reference strains, not experimental "
                "isolate deposits. No canonical taxa, exact external mappings, "
                "protein examples or causal graph are asserted. The measured "
                "enzyme activity is not a molecular effector identification. "
                "Metadata and notice checks were bounded; some publisher "
                "endpoints failed. Source URLs, hashes, version distinctions "
                "and native verification results are retained in the sidecar."
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
            "Added nutritional fungal mycoparasitism with three DOI-backed "
            "contiguous excerpts and bounded scope, hierarchy and source "
            "discussions. Reserved 000717, v593 and 1067000-1067099 after "
            "ignored/hidden current-file, retained-history, independent-copy "
            "and open/draft PR checks; numeric false positives adjudicated. "
            "No exact active METPO counterpart identified in inspected "
            "sources. No canonical taxa or causal graph inferred; previous "
            "records unchanged. Timestamp is observed post-audit acceptance, "
            "not an estimated write time."
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
         "Fungal nutrition at host expense; not mere association or obligatory killing.",
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
