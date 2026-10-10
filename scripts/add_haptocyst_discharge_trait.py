"""Add source-bounded haptocyst discharge through the validated writer."""

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
SLUG = "haptocyst_discharge"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v562/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000686"
METPO_ID = "METPO:1063900"
PARENT_METPO_ID = "METPO:1000059"
DISCHARGE = "DOI:10.1515/znc-1984-7-821"
IDENTITY = "DOI:10.1007/BF00331480"
TIMESTAMP = "2026-10-10T01:50:07Z"
PARENT = {
    "identifier": PARENT_METPO_ID,
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
    "label": "haptocyst discharge",
    "definition": (
        "A physiological phenotype in which a microbial cell releases material "
        "from haptocysts to the cell exterior."
    ),
    "definition_source": DISCHARGE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_METPO_ID],
    "evidence": [
        {
            "reference": DISCHARGE,
            "snippet": (
                "The fine structure of haptocysts, characteristic organelles of most "
                "suctorians, is described during the resting state and the discharge "
                "after contact with the prey."
            ),
            "notes": (
                "Benwitz 1984, English abstract reproduced at "
                "https://www.nies.go.jp/chiiki1/protoz/refere/id4999/4538.htm, "
                "read directly on 2026-10-10. Crossref confirms the DOI, title, "
                "author and original 1984 publication; later online dates are not "
                "the experiment year. In Ephelota gemmipara the abstract reports "
                "prey-contact discharge, continuity of the haptocyst membrane "
                "with the tentacle plasma membrane, and attachment of internal "
                "haptocyst structures to the perforated prey pellicle. It explicitly "
                "reports no predator-prey plasma-membrane fusion in Ephelota. "
                "These observations support release to the cell exterior, not "
                "cell-cell fusion or merely possession of haptocysts. The publisher "
                "PDF was unavailable; figures and full Methods were not visually "
                "audited. No universal cargo chemistry or trigger is inferred."
            ),
        },
        {
            "reference": IDENTITY,
            "snippet": "By these haptocysts the tentacle is attached to the prey.",
            "notes": (
                "Bardele and Grell 1967, PMID:4971424. Publisher English Summary "
                "points 1-2 at https://link.springer.com/article/10.1007/BF00331480 "
                "read directly on 2026-10-10. The source identifies the tentacular "
                "organelles in Acineta tuberosa as haptocysts and describes prey "
                "attachment. This is independent organelle-identity and attachment "
                "evidence, not a second direct discharge experiment. Its ingestion "
                "tube hypothesis is not a demonstrated haptocyst release mechanism. "
                "Full text is subscription-only and was not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "haptocyst-discharge-scope-and-parent",
            "prompt": "Resolve the exocytosis placement and historical extrusome terminology.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain phenotype METPO:1000059 pending broader hierarchy review. "
                "Benwitz supports organelle-plasma-membrane continuity in Ephelota, "
                "not predator-prey membrane fusion. This supports an exocytotic "
                "interpretation in that system but does not establish the fusion-pore "
                "differentia of exocytosis traitmech:000637 throughout the unqualified "
                "class. That placement is unresolved, not excluded. Mere possession, "
                "docking, prey attachment, ingestion or nonspecific cell lysis alone "
                "does not demonstrate discharge. Do not require prey death, complete "
                "emptying or a universal natural trigger. Toxicyst discharge "
                "traitmech:000685 explicitly leaves haptocyst terminology unresolved; "
                "this organelle-specific record does not settle whether historical "
                "toxicyst umbrellas include haptocysts. Do not equate haptocysts with "
                "kinetocysts, trichocysts or mucocysts, or assert homology or "
                "organism-level disjointness. No exact synonyms or xrefs are assigned."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
        {
            "discussion_id": "haptocyst-discharge-provenance-and-mechanism",
            "prompt": "Verify natural exemplars and separate release from attachment and ingestion.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Experimental culture provenance and current strain-level taxonomy "
                "remain unchecked; no canonical examples are assigned. The two "
                "citations support different claims and are not replicate discharge "
                "assays. Tentacular ultrastructure does not establish a conserved "
                "protein mechanism, toxin composition or signaling pathway. A future "
                "graph needs direct perturbation evidence and taxon-paired accessions, "
                "separating assembly, triggering, extrusion, attachment and ingestion. "
                "Mechanism is deferred, not claimed absent. Sequence features alone "
                "would not establish any of these causal transitions."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-10",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added haptocyst discharge with two primary DOI sources and directly "
            "checked abstract/Summary snippets, distinguishing discharge evidence "
            "from organelle identity and attachment. Ignored-and-hidden "
            "main/worktree/open-PR checks support 000686 and v562 block "
            "1063900-1063999. Exocytosis hierarchy, natural exemplars and protein "
            "mechanisms remain unresolved. Existing records unchanged. Timestamp "
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
         PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
         "Haptocyst material release; exocytosis hierarchy unresolved.", IDENTIFIER],
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
