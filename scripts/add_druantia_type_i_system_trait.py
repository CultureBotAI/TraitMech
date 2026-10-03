"""Add literature-defined Druantia I possession without equating detector thresholds."""

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

TRAITS = ROOT / "data/traits/genomics"
SLUG = "druantia_type_i_system"
IDENTIFIER = "traitmech:000578"
TARGET = TRAITS / f"{SLUG}.yaml"
PARENT = TRAITS / "druantia_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v455"
TIMESTAMP = "2026-10-03T20:24:00Z"
DISCOVERY = "DOI:10.1126/science.aar4120"
ARCHITECTURE = "DOI:10.3389/fmicb.2020.00961"
DF = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/"
    "Druantia/Druantia_I.xml"
)
PADLOC = (
    "https://raw.githubusercontent.com/padlocbio/padloc-db/"
    "9e380165633a8d6aef93b5a164cea0f3359bd33f/sys/druantia_type_I.yaml"
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Druantia type I system",
    "definition": (
        "A Druantia system in which an organism possesses a locus encoding "
        "DruE together with DruB, DruC and DruD, with or without DruA."
    ),
    "definition_source": DISCOVERY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000234"],
    "synonyms": [{
        "synonym_text": "Type I Druantia system",
        "synonym_type": "EXACT_SYNONYM",
        "source": ARCHITECTURE,
    }],
    "evidence": [
        {
            "reference": DISCOVERY,
            "snippet": (
                "In some cases Type I systems are preceded by a gene annotated as DUF4338"
            ),
            "notes": (
                "Doron et al., The Druantia system and Table 1: type I has "
                "three partner genes beside DruE, sometimes with an additional "
                "DUF4338 gene. The table names DruA/B/C/D/E; the prose does "
                "not make DruA universal. The UMEA 4076-1 locus protected "
                "engineered E. coli MG1655 against four of six tested phages. "
                "Deletion of four tested genes abolished protection; this "
                "does not establish universal DruA dependence. Snippet verified "
                "in the accepted manuscript, page 7 (PDF page 9), available "
                "from the Weizmann institutional repository."
            ),
        },
        {
            "reference": ARCHITECTURE,
            "snippet": (
                "druA, encodes a large protein with a domain with unknown function (DUF4338)"
            ),
            "notes": (
                "The Druantia System section maps DUF4338 to DruA and "
                "describes a five-gene DruA/B/C/D/E form as type I in the "
                "Ralstonia solanacearum species complex. This independently "
                "corroborates component names, not a universal five-gene "
                "requirement. UW163 is a genomic prediction here; the "
                "authors' suggested functionality is not an infection assay."
            ),
        },
        {
            "reference": PADLOC,
            "snippet": "core_genes:\n  - DruA1\n  - DruB1\n  - DruC1\n  - DruD1\n  - DruE1",
            "notes": (
                "Pinned executable PADLOC rule, retrieved 2026-10-03: "
                "minimum_core and minimum_total are both 5, "
                "maximum_separation is 3, and force_strand is FALSE. "
                "Secondary, neutral and prohibited lists contain only NA. "
                "This detector requires the five named profiles, including "
                "DruA; that is narrower than the literature's optional-DruA "
                "architecture, not evidence for universal DruA essentiality."
            ),
        },
        {
            "reference": DF,
            "snippet": (
                '<model inter_gene_max_space="5" min_mandatory_genes_required="1" '
                'min_genes_required="3" vers="2.0">'
            ),
            "notes": (
                "Pinned executable DefenseFinder model, retrieved 2026-10-03: "
                "Druantia_I__DruA/B/C/D are accessory slots. The mandatory "
                "Druantia__DruE_1 slot permits Druantia__DruE_2, "
                "Druantia__DruE_3 or Druantia_IV__DruE4 as exchangeables. "
                "The model requires only one mandatory and three total "
                "matches and has no forbidden slots. A call alone does "
                "not establish the complete DruB/C/D/E architecture or "
                "active defense. The raw model key is not an exact synonym."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:562",
        "taxon_label": "Escherichia coli",
        "reference": DISCOVERY,
        "note": (
            "Natural possession is limited to the named source strain UMEA "
            "4076-1, not species-wide possession or demonstrated native-host "
            "resistance. Doron et al. transferred its type-I locus into "
            "E. coli MG1655; protection against four of six tested phages "
            "was measured in that engineered recipient. NCBI independently "
            "resolves taxon 562 to Escherichia coli."
        ),
    }],
    "discussions": [{
        "discussion_id": "druantia-type-i-components-and-mechanism",
        "prompt": "Resolve type-I partner functions and reconcile incomplete detector calls.",
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": (
            "DruB/C/D/E with optional DruA is a literature-based architecture "
            "class. The five-gene Ralstonia description and PADLOC rule do "
            "not override Doron's optional DUF4338 component. Conversely, "
            "DefenseFinder's three-match threshold does not establish a "
            "complete locus. Missing profiles, incomplete assemblies and "
            "engineered deletions do not by themselves establish natural "
            "component absence or a new subtype. Full locus context is "
            "required, and a genome may encode several Druantia subtypes. "
            "The specific functions of type-I partners, the phage trigger, "
            "native-host activity and defense breadth remain open. Do not "
            "transfer the DruH/type-III helicase-nuclease mechanism to "
            "type I, or infer biochemical activity from a DruE profile. "
            "No protein examples or causal graph are added without "
            "component-resolved functional evidence and accession anchors."
        ),
        "posed_by": "codex",
        "posed_date": "2026-10-03",
    }],
}

PREIMAGE = {
    "identifier": "traitmech:000234",
    "label": "Druantia system",
    "parents": ["traitmech:000209"],
    "definition_hash": "59e521af7974422318b4b8fd17bd5b102d51af5e6a5ba34dd5f6e06b2c732c1c",
    "discussion_id": "druantia-subtype-mechanism-gap",
    "rationale_hash": "f6380a2d917c1631b7f82afed93327f7ab5a1d87de4e6fd64ee947c3b99fb149",
    "old_tail": "Type I and II remain separate architecture-class discovery leads.",
    "new_tail": (
        "Type I architecture is now represented by traitmech:000578 Druantia "
        "type I system: DruB/C/D/E with optional DruA. Doron's optional "
        "DUF4338 component and the Ralstonia study's mapping of that domain "
        "to DruA qualify the earlier five-gene shorthand. The five-profile "
        "PADLOC rule and three-match DefenseFinder threshold are detection "
        "criteria, not identical biological definitions. This resolves the "
        "type-I architecture lead, not its partner functions or native-host "
        "mechanism. Type II remains an architecture-class discovery lead."
    ),
}


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(
        record, curator="codex", action=action, changes=changes,
        llm_assisted=True, timestamp=TIMESTAMP,
    )


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(
        record, "MINTED_TRAITMECH_ID",
        "Added Druantia I organism-level possession with optional DruA, "
        "two DOI sources, four exact snippets and pinned executable "
        "detector rules. Kept natural UMEA 4076-1 possession distinct from "
        "engineered MG1655 defense, with NCBITaxon:562 resolved at NCBI. "
        "Ignored-and-hidden novelty and allocation searches found no exact "
        "record or METPO term; reserved METPO:1053200 in v455. No "
        "type-III mechanism or raw detector threshold defines this class.",
    )
    return record


def build_parent() -> dict:
    record = yaml.safe_load(PARENT.read_text())
    if (
        record.get("identifier") != PREIMAGE["identifier"]
        or record.get("label") != PREIMAGE["label"]
        or record.get("mapping_status") != "PROPOSED"
        or record.get("parent_traits") != PREIMAGE["parents"]
        or hashlib.sha256(record.get("definition", "").encode()).hexdigest() != PREIMAGE["definition_hash"]
    ):
        raise SystemExit("Druantia parent identity, hierarchy or definition changed")
    matches = [d for d in record.get("discussions", [])
               if d.get("discussion_id") == PREIMAGE["discussion_id"]]
    if len(matches) != 1 or (matches[0].get("kind"), matches[0].get("status")) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit("Druantia parent discussion identity or status changed")
    discussion = matches[0]
    before = discussion.get("rationale", "")
    replay = before.endswith(PREIMAGE["new_tail"])
    if replay:
        before = before.removesuffix(PREIMAGE["new_tail"]) + PREIMAGE["old_tail"]
    if hashlib.sha256(before.encode()).hexdigest() != PREIMAGE["rationale_hash"]:
        raise SystemExit("Druantia parent discussion preimage changed")
    if not before.endswith(PREIMAGE["old_tail"]):
        raise SystemExit("Druantia parent discussion tail changed")
    if not replay:
        discussion["rationale"] = before.removesuffix(PREIMAGE["old_tail"]) + PREIMAGE["new_tail"]
        event(
            record, "TRACK_DRUANTIA_TYPE_I_CLASS",
            "Linked traitmech:000578 using DOI:10.1126/science.aar4120 and "
            "DOI:10.3389/fmicb.2020.00961. Resolved the type-I architecture "
            "lead with optional DruA and distinct detector thresholds. "
            "Kept family identity, definition, hierarchy, evidence and "
            "example unchanged; type-I functions and the type-II lead remain open.",
        )
    return record


def proposal_tsv(record: dict) -> str:
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
    writer.writerow([
        "METPO:1053200", record["label"], record["definition"],
        "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", DISCOVERY, ARCHITECTURE]),
        "METPO:1053100", record["synonyms"][0]["synonym_text"], "",
        "metpo_traitmech_2026_10", "HIGH",
        "DruB/C/D/E with optional DruA; detector thresholds are not "
        "biological essentiality or complete-locus evidence.", IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    updates = [(TARGET, record), (PARENT, build_parent())]
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
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
