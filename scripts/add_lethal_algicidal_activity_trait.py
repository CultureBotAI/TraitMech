"""Add source-bounded lethal algicidal activity through the validated writer."""

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
SLUG = "lethal_algicidal_activity"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v571/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000695"
METPO_ID = "METPO:1064800"
PARENT_ID = "METPO:1000059"
STRAIN_Y = "DOI:10.1128/AEM.64.8.2806-2813.1998"
STRAIN_A28 = "DOI:10.1128/AEM.66.10.4334-4339.2000"
STRAIN_HY = "DOI:10.3390/toxins15030220"
TIMESTAMP = "2026-10-11T08:50:39Z"
PARENT = {
    "identifier": PARENT_ID,
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
    "label": "lethal algicidal activity",
    "definition": (
        "A physiological capability of a microorganism to kill cells of "
        "eukaryotic algae or cyanobacteria."
    ),
    "definition_source": STRAIN_A28,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": STRAIN_Y,
            "snippet": (
                "All G. catenatum cells in strain Y-treated wells were dead and "
                "most cells had lysed after 2 days."
            ),
            "notes": (
                "Lovejoy et al. 1998, PMID:9687434, PMC106776, Results sec9. "
                "Scientific Abstract, algal-culture/toxicity Methods, activity "
                "and specificity Results, Discussion, Tables 1/2/4/5 and actual "
                "Figure 2 inspected. Other actual figures and remaining Methods "
                "unread. Strain Y and filtrate support killing, unlike reversible "
                "ecdysis or rounding in other targets. Some dinoflagellate "
                "controls also died in separate experiments; raphidophyte "
                "controls remained healthy. P. carrageenovora was not uniformly "
                "harmless. Close affinity to P. peptidysin is not exact species "
                "identification. EXT_ID:9687434 AND SRC:MED matched source, "
                "ID, title and DOI on 2026-10-11. Full-text quotation directly "
                "matched; abstract matching alone cannot verify this passage."
            ),
        },
        {
            "reference": STRAIN_A28,
            "snippet": (
                "The marine bacterium Pseudoalteromonas sp. strain A28 was able "
                "to kill the diatom Skeletonema costatum strain NIES-324."
            ),
            "notes": (
                "Lee et al. 2000, PMID:11010878, PMC92304, scientific Abstract. "
                "Abstract, Introduction, Methods, Results, Discussion, Tables "
                "1/2 and actual Figures 1/2 inspected; actual Figures 3/4 "
                "unread. Parental A28 culture and supernatant support the "
                "capability. Results sec11 reports no regrowth after transfer "
                "from cleared agar, distinguishing algicidal from algistatic, "
                "but that experiment is data not shown. Protease II lacked "
                "algicidal action despite protease activity. Six N-terminal "
                "residues do not establish full AprI identity; NH1/NH2 are "
                "mutagenized derivatives, not natural exemplars. A separate "
                "group from Lovejoy et al., not a replication of strain Y. "
                "EXT_ID:11010878 AND SRC:MED matched source, ID, title and DOI "
                "on 2026-10-11; quotation matched direct scientific Abstract "
                "and qualified API abstract."
            ),
        },
        {
            "reference": STRAIN_HY,
            "snippet": (
                "The cyanobacterial cell walls were severely damaged, leading "
                "to the leakage of intracellular components."
            ),
            "notes": (
                "Zhang et al. 2023, PMID:36977111, PMC10058357, Results 2.4. "
                "Scientific Abstract, Introduction, Results 2.1-2.4, Discussion, "
                "Methods 5.1-5.4/5.8/5.12 and actual Figure 3 with caption "
                "inspected; other figures and supplement unread. Filtrate "
                "damage/lysis supports cyanobacterial target scope. Methods "
                "5.3 calculates relative cell-density reduction versus controls, "
                "not a direct dead-cell fraction; no percentage is adopted. "
                "Results 2.1 calls HY #320 from 411 isolates, versus #332/412 "
                "in Methods 5.2 and #332 in Figure 1 caption; provenance remains "
                "unreconciled. Molecular agents are unidentified; transcription "
                "changes alone do not establish causal protein edges. "
                "EXT_ID:36977111 AND SRC:MED matched source, ID, title and DOI "
                "on 2026-10-11. Quotation directly matched full text."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "lethal-algicidal-scope-and-mappings",
            "prompt": "Resolve mappings while retaining a lethal endpoint and actor-level scope.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The lethal qualifier distinguishes this capability from broader "
                "algicidal usage. Paul and Pohnert 2011, "
                "DOI:10.1371/journal.pone.0021032, Methods Monitoring algicidal "
                "activity and Results, uses fluorescence-based growth inhibition "
                "as an algicidal readout; those directly read passages provide "
                "terminology context, not additional killing evidence. This "
                "record requires killing, not reduced fluorescence, reversible "
                "growth arrest, ecdysis, passive removal or a protease sequence "
                "alone. It denotes the acting microbe's capability, not an "
                "algicide molecule, treated alga's susceptibility or assay row. "
                "Cyanobacteria are included explicitly, not classified as "
                "eukaryotic algae. Activity against some susceptible targets "
                "suffices; universal host range is not asserted. Predatory "
                "bacterium traitmech:000054 requires killing and consuming "
                "bacteria for nutrients, so it is not a parent of this class. "
                "Killing may overlap predation but neither consumption, grazing "
                "nor nutritional benefit is required or inferred; no organismal "
                "disjointness is asserted. No exact synonym or phenotype xref "
                "is assigned pending authority and scope review."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "lethal-algicidal-strains-and-mechanisms",
            "prompt": "Reconcile study strains and build independently supported mechanism graphs.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Canonical examples await authoritative strain/taxon "
                "reconciliation, including HY's conflicting isolate numbers. "
                "Retain source strain names as qualified evidence without "
                "species-wide assignments or promotion of induced mutants. "
                "Secreted activity is demonstrated, not a universal restriction "
                "excluding contact-dependent routes. Neither a common protein "
                "mechanism, a universal lethal threshold, bloom-control "
                "efficacy nor environmental safety is established. Protein "
                "graphs require exact functional evidence and taxon-paired "
                "accessions, not a short sequence match. Mechanisms are "
                "deferred, not claimed absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added lethal algicidal activity beneath phenotype with three "
            "primary DOI citations and directly checked short snippets. "
            "Ignored-and-hidden main/worktree/open-PR checks support 000695 "
            "and v571 block 1064800-1064899. Existing records unchanged; "
            "mappings, canonical taxa and mechanisms remain open. Timestamp "
            "records the observed UTC curation decision."
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
         PARENT_ID, "", "", "metpo_traitmech_2026_10", "",
         "Microbial killing capability; algistatic-only activity is outside scope.",
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
