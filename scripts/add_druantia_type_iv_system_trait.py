"""Add Druantia IV possession and remove a family-wide mechanism overclaim."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TRAITS = ROOT / "data/traits/genomics"
SLUG = "druantia_type_iv_system"
IDENTIFIER = "traitmech:000577"
TARGET = TRAITS / f"{SLUG}.yaml"
PARENT = TRAITS / "druantia_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v454"
TIMESTAMP = "2026-10-03T19:44:00Z"
DISCOVERY = "DOI:10.1093/nar/gkab883"
FAMILY = "DOI:10.64898/2026.05.12.724681"
DF = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/"
    "Druantia/Druantia_IV.xml"
)
PADLOC = (
    "https://raw.githubusercontent.com/padlocbio/padloc-db/"
    "9e380165633a8d6aef93b5a164cea0f3359bd33f/sys/druantia_type_IV.yaml"
)

DISCOVERY_EVIDENCE = {
    "reference": DISCOVERY,
    "snippet": (
        "the Druantia-like system lacks the type II requisite DruM and DruG "
        "proteins, instead encoding a hypothetical protein"
    ),
    "notes": (
        "Payne et al., Results and Figure 2C: the recurring type-IV "
        "architecture contains DruE and DruF together with the newly named "
        "DruL, instead of the type-II DruM/G components. This is a "
        "literature-defined system-possession class, not an individual "
        "profile. The study tests Zorya III, Hachiman II and Lamassu II, "
        "not Druantia IV. Its computational classification does not "
        "demonstrate type-IV phage resistance or DruL chemistry."
    ),
}

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Druantia type IV system",
    "definition": (
        "A Druantia system in which an organism possesses a locus encoding "
        "DruE and DruF together with DruL, without the type-II DruM and "
        "DruG components."
    ),
    "definition_source": DISCOVERY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000234"],
    "synonyms": [{
        "synonym_text": "Druantia type IV", "synonym_type": "EXACT_SYNONYM",
        "source": DISCOVERY,
    }],
    "evidence": [
        DISCOVERY_EVIDENCE,
        {
            "reference": DF,
            "snippet": '<gene name="Druantia_IV__DruL" presence="mandatory"/>',
            "notes": (
                "Pinned DefenseFinder XML, retrieved 2026-10-03: three "
                "mandatory slots, both minimum counts 3, inter_gene_max_space "
                "1. DruL is mandatory; DruE_1 accepts DruE_2, DruE_3 or "
                "DruE4 exchangeables, and the Druantia-II DruF slot accepts "
                "DruF4. There are no forbidden genes: a call does not "
                "establish absence of DruM/G. Check full locus context "
                "before assigning the literature-defined architecture. "
                "Detection does not establish functional defense."
            ),
        },
        {
            "reference": PADLOC,
            "snippet": (
                "minimum_core: 3\nminimum_total: 3\ncore_genes:\n"
                "  - DruE4\n  - DruF4\n  - DruL4"
            ),
            "notes": (
                "Pinned PADLOC rule, retrieved 2026-10-03: three required "
                "core genes, maximum_separation 3, force_strand FALSE. "
                "DruK is secondary, not a required defining component. "
                "The prohibited list is NA, so the detector does not "
                "test the biological absence of DruM/G. A missing hit "
                "or incomplete assembly cannot establish that absence. "
                "These are computational constraints, not experimental "
                "component essentiality or type-IV mechanism evidence."
            ),
        },
    ],
    "discussions": [{
        "discussion_id": "druantia-type-iv-functional-and-architecture-gap",
        "prompt": "Resolve type-IV defense activity, DruL function and complete locus boundaries.",
        "kind": "KNOWLEDGE_GAP", "status": "OPEN",
        "rationale": (
            "The sources support a recurring organism-level DruE/F/L locus "
            "architecture distinct from type-II DruM/F/G/E, not a measured "
            "resistance phenotype. A complete accession-resolved natural "
            "locus, independently resolved taxon and type-IV-specific "
            "functional assays remain to be curated before adding a "
            "canonical example or causal mechanism graph. DruE helicase/"
            "nuclease activity established for type III is not generalized "
            "to type IV. DruL and optional DruK roles remain unresolved "
            "by this evidence bundle. Neither executable detector forbids "
            "DruM/G; mixed or incomplete calls require biological locus "
            "review, not automatic conversion to this absence-qualified "
            "class. No individual protein, HMM hit, source key, unverified "
            "xref or mutually disjoint organism-level possession is asserted."
        ),
        "posed_by": "codex", "posed_date": "2026-10-03",
    }],
}

PREIMAGE_HASH = "f5a86ddefc42988cedde8d691e01b1ce347cf72ce6d5b349aab040917728381b"
POSTIMAGE_HASH = "7ef30b36d18ec2a0893475d054bb2b8f1a9ee830f80b6fe0aace2e0b6d17ceef"
NEW_DEFINITION = (
    "A phage defense system in which an organism possesses a Druantia "
    "locus encoding a conserved DruE-family core and subtype-specific "
    "partner proteins."
)
ADDITION = (
    " Druantia type IV system (traitmech:000577) now captures the "
    "DruE/F/L architecture described by Payne et al. "
    "(DOI:10.1093/nar/gkab883), without the type-II DruM/G components. "
    "This resolves the architectural child, not type-IV experimental "
    "defense or partner chemistry. The family definition no longer "
    "requires universal helicase-nuclease DNA processing. Wu et al.'s "
    "family-wide conservation claim is a hypothesis in a type-III "
    "preprint. The overgeneralized parent graph is removed; the "
    "characterized III branch remains at traitmech:000560. New proposal "
    "v454 replaces the unminted v111 family row without changing the "
    "local family identifier or historical TSV. Type I and II remain "
    "separate architecture-class discovery leads."
)


def fingerprint(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(record, curator="codex", action=action, changes=changes,
                          llm_assisted=True, timestamp=TIMESTAMP)


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(
        record, "MINTED_TRAITMECH_ID",
        "Added the literature-defined DruE/F/L possession class with a DOI "
        "and two pinned executable models, each with an exact snippet. "
        "Ignored-and-hidden novelty searches found no exact METPO or live "
        "record. Reserved METPO:1053101 in v454, below corrected family "
        "placeholder METPO:1053100. Kept computational architecture and "
        "component absence distinct from detector calls and measured defense.",
    )
    return record


def repair_parent(record: dict) -> dict:
    record = copy.deepcopy(record)
    record["definition"] = NEW_DEFINITION
    for item in record["evidence"]:
        if item["reference"] == FAMILY:
            item["notes"] = "Preprint v1, not peer-reviewed. " + item["notes"]
            if "suggesting" in item.get("snippet", ""):
                item["notes"] = (
                    "Preprint v1, not peer-reviewed. Wu et al. infer a "
                    "possible conserved DruE-family function from their "
                    "type-III results and shared DruE. This is a hypothesis, "
                    "not a demonstrated mechanism for every Druantia subtype."
                )
    record["evidence"].append(copy.deepcopy(DISCOVERY_EVIDENCE))
    record.pop("causal_graphs")
    discussion = record["discussions"][0]
    discussion["prompt"] = (
        "Resolve Druantia subtype mechanisms separately from architecture-based possession classes."
    )
    discussion["rationale"] += ADDITION
    event(
        record, "SCOPE_DRUANTIA_FAMILY_AND_TYPE_IV",
        "Addressed #1635: removed a universal DNA-processing requirement "
        "and the overgeneralized family graph, retaining evidence with "
        "preprint/hypothesis qualifiers. Linked the new type-IV "
        "architecture child traitmech:000577. The existing III record "
        "retains its characterized mechanism; type-IV defense remains "
        "unresolved. Proposal v454 supersedes the v111 family row.",
    )
    return record


def build_parent() -> dict:
    record = yaml.safe_load(PARENT.read_text())
    digest = fingerprint(record)
    if digest == POSTIMAGE_HASH:
        return record
    if digest != PREIMAGE_HASH:
        raise SystemExit("Parent preimage changed; refusing unreviewed drift")
    return repair_parent(record)


def proposal_tsv(child: dict, parent: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "proposed_id", "label", "definition", "definition_source", "parent",
        "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed",
    ])
    writer.writerow([
        "ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
        "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
        "A oboInOwl:inSubset", "", "", "",
    ])
    for record, slug, proposed, broader, note in [
        (parent, "druantia_system", "METPO:1053100", "METPO:1016300",
         "Replaces v111 METPO:1018800; no universal DNA-processing mechanism asserted."),
        (child, SLUG, "METPO:1053101", "METPO:1053100",
         "DruE/F/L architecture without type-II DruM/G; detector calls alone do not prove absence or defense."),
    ]:
        writer.writerow([
            proposed, record["label"], record["definition"],
            "|".join(dict.fromkeys([f"TraitMech:data/traits/genomics/{slug}.yaml",
                                    record["definition_source"], DISCOVERY])),
            broader, "|".join(s["synonym_text"] for s in record["synonyms"]
                              if s["synonym_type"] == "EXACT_SYNONYM"),
            "", "metpo_traitmech_2026_10", "HIGH", note, record["identifier"],
        ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    child, parent = build_record(), build_parent()
    proposal = proposal_tsv(child, parent)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != child:
        raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
    updates = [(TARGET, child), (PARENT, parent)]
    with tempfile.TemporaryDirectory() as tmp:
        for path, record in updates:
            write_validated_trait(record, Path(tmp) / path.name)
    if args.apply:
        for path, record in updates:
            write_validated_trait(record, path)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
