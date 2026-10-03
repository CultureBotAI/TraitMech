"""Add the literature-defined long Lamassu family without a length cutoff."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "long_lamassu_system"
IDENTIFIER = "traitmech:000571"
TARGET = ROOT / "data/traits/genomics" / f"{SLUG}.yaml"
PARENT = ROOT / "data/traits/genomics/lamassu_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v448"
TIMESTAMP = "2026-10-03T14:29:24Z"
PAPER = "DOI:10.1073/pnas.2519643122"
DATASET = "https://pmc-oa-opendata.s3.amazonaws.com/PMC12663957.1/pnas.2519643122.sd01.xlsx"
PARENT_HASH = "e70f069e401baf705f43927375d45ba41bd55921a39e96c3615d91669bcbcdda"
PARENT_ADDITION = (
    " Long Lamassu system (traitmech:000571) now captures the complementary "
    "long-LmuB phylogenetic and structural family, not an 800-residue cutoff "
    "or a particular effector model. The paper assigns the B. cereus B4077 "
    "Hydrolase-Protease system to this family, but that effector architecture "
    "also occurs in short Lamassu, so the whole Hydrolase-Protease trait is "
    "not reparented. The legacy table-defined FMO trait still needs model "
    "and biological-scope reconciliation before assigning the entire record "
    "to the long family. SMEK's exception remains unresolved. Raw detection "
    "gene_name hits must not be confused with exchangeable hit_gene_ref "
    "model slots, and ambiguous loci need phylogenetic classification. "
    "Component-number type I/II traits remain separate discovery leads."
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "long Lamassu system",
    "definition": (
        "A Lamassu system in which an organism possesses a locus from the "
        "long-LmuB family, characterized by longer coiled-coil regions in "
        "its SMC-like LmuB sensor than in short Lamassu systems."
    ),
    "definition_source": PAPER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000232"],
    "synonyms": [
        {
            "synonym_text": "long Lamassu",
            "synonym_type": "EXACT_SYNONYM",
            "source": PAPER,
        }
    ],
    "evidence": [
        {
            "reference": PAPER,
            "snippet": (
                "two major clades, which were mainly distinguished by the "
                "length of coiled-coil regions"
            ),
            "notes": (
                "Results, LmuB phylogeny paragraph and Figure 1: the long "
                "family is distinguished from short Lamassu by phylogeny "
                "and structure. The approximate 800-residue total LmuB "
                "length is descriptive, not a membership cutoff."
            ),
        },
        {
            "reference": PAPER,
            "snippet": (
                "one system from Bacillus cereus B4077, encoding Hydrolase-Protease effectors"
            ),
            "notes": (
                "The same paragraph explicitly identifies B4077 as the "
                "long-clade exception among previously validated systems. "
                "This supports strain-qualified possession, not species-wide "
                "distribution or a native-host phage-resistance measurement."
            ),
        },
        {
            "reference": DATASET,
            "snippet": (
                "ACCA003.0722.00003.C001\tACCA003.0722.00003.C001_02431\t"
                "Lamassu__LmuB_Long\n"
                "ACCA003.0722.00003.C001\tACCA003.0722.00003.C001_02432\t"
                "Lamassu__LmuC_Clade_VII\n"
                "ACCA003.0722.00003.C001\tACCA003.0722.00003.C001_02433\t"
                "Lamassu__LmuA_Cap4_III"
            ),
            "notes": (
                "Dataset S1, S3_Lamassu_Detection!A58:C60, raw cells in "
                "column order. Column F assigns these rows to one "
                "ACCA003.0722.00003.C001_Lamassu_Cap4_321 call; column I "
                "reports sys_wholeness 1.0. Column C (gene_name) identifies "
                "the actual long-LmuB hit, unlike column L (hit_gene_ref), "
                "which can name the long model slot for short hits. These "
                "are computational locus observations, not an experimental "
                "antiviral phenotype or a family-membership rule."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1396",
            "taxon_label": "Bacillus cereus",
            "reference": PAPER,
            "note": (
                "Strain B4077 is the source of the Hydrolase-Protease "
                "system assigned to the long family by Haudiquet et al. "
                "The species identifier anchors this strain-qualified "
                "example; no genome assembly, universal species possession, "
                "or native-host phage-resistance phenotype is inferred."
            ),
        }
    ],
    "discussions": [
        {
            "discussion_id": "long-lamassu-classification-and-mechanism-scope",
            "prompt": "Resolve borderline loci and long-family activation mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Long denotes a phylogenetic and structural family, not an "
                "isolated protein, a fixed amino-acid threshold, an effector "
                "name, or the component-number type II category. A raw "
                "long-profile hit alone does not settle membership of an "
                "ambiguous locus. The published detection sheet uses "
                "gene_name for actual hits and hit_gene_ref for potentially "
                "exchangeable model slots; these fields must not be conflated. "
                "Hydrolase-Protease spans both length families; the legacy "
                "FMO record's detector-defined scope and SMEK's long-profile "
                "exception need separate reconciliation before reparenting. "
                "No universal effector chemistry, LmuC requirement, zinc-hook "
                "count, or stoichiometry is imposed. The experimentally "
                "resolved short Vc-Cap4 activation mechanism is not transferred "
                "to this family. Native-host activity, accession-level protein "
                "anchors and family-wide activation remain open, so no "
                "causal mechanism graph is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-03",
        }
    ],
}


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(
        record,
        curator="codex",
        action=action,
        changes=changes,
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(
        record,
        "MINTED_TRAITMECH_ID",
        "Added the literature-defined long Lamassu family with exact primary "
        "paper and dataset snippets and a strain-qualified B4077 example. "
        "Distinguished actual profile hits from model slots without adopting "
        "a length cutoff or transferring short-family mechanisms. Ignored-and-"
        "hidden searches found no exact record or METPO term. Reserved "
        "METPO:1052500 in proposals/metpo_traitmech_v448; left sibling "
        "hierarchies unchanged pending their own scope reconciliation.",
    )
    return record


def build_parent() -> dict:
    record = yaml.safe_load(PARENT.read_text())
    if (
        record["identifier"] != "traitmech:000232"
        or record["label"] != "Lamassu system"
        or record["mapping_status"] != "PROPOSED"
        or record["parent_traits"] != ["traitmech:000209"]
    ):
        raise SystemExit("Lamassu parent identity or hierarchy changed")
    matches = [
        d for d in record["discussions"] if d["discussion_id"] == "lamassu-subtype-and-effector-gap"
    ]
    if len(matches) != 1:
        raise SystemExit("Expected one unchanged parent discussion")
    discussion = matches[0]
    if (discussion["kind"], discussion["status"]) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit("Parent discussion kind or status changed")
    old = discussion["rationale"].removesuffix(PARENT_ADDITION)
    if hashlib.sha256(old.encode()).hexdigest() != PARENT_HASH:
        raise SystemExit("Parent discussion preimage changed; review before applying")
    if old == discussion["rationale"]:
        discussion["rationale"] += PARENT_ADDITION
        event(
            record,
            "TRACK_NARROWER_RECORD",
            "Linked traitmech:000571 long Lamassu system and recorded why "
            "Hydrolase-Protease, FMO and SMEK are not automatically reparented. "
            "Retained component-classification and family-mechanism gaps.",
        )
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "proposed_id",
            "label",
            "definition",
            "definition_source",
            "parent",
            "synonyms",
            "xrefs",
            "subset",
            "priority",
            "observations",
            "traits_addressed",
        ]
    )
    writer.writerow(
        [
            "ID",
            "LABEL",
            "A IAO:0000115",
            ">A IAO:0000119",
            "SC %",
            "A oboInOwl:hasExactSynonym SPLIT=|",
            "A oboInOwl:hasDbXref SPLIT=|",
            "A oboInOwl:inSubset",
            "",
            "",
            "",
        ]
    )
    writer.writerow(
        [
            "METPO:1052500",
            record["label"],
            record["definition"],
            "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", PAPER, DATASET]),
            "METPO:1018600",
            record["synonyms"][0]["synonym_text"],
            "",
            "metpo_traitmech_2026_10",
            "HIGH",
            "Long-LmuB structural family, not a length threshold or a type-II synonym. "
            "Existing effector-defined records are not reparented without scope reconciliation.",
            IDENTIFIER,
        ]
    )
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record, parent = build_record(), build_parent()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from this writer; review before applying")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer; review before applying")
    updates = [(TARGET, record), (PARENT, parent)]
    with tempfile.TemporaryDirectory() as tmp:
        for path, updated in updates:
            write_validated_trait(updated, Path(tmp) / path.name)
    if args.apply:
        for path, updated in updates:
            write_validated_trait(updated, path)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
