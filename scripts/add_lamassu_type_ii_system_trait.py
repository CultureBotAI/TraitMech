"""Add the LmuC-containing Lamassu class and refine its existing children."""

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
SLUG = "lamassu_type_ii_system"
IDENTIFIER = "traitmech:000572"
TARGET = TRAITS / f"{SLUG}.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v449"
TIMESTAMP = "2026-10-03T15:14:27Z"
CLASSIFICATION = "DOI:10.1093/nar/gkab883"
STRUCTURE = "DOI:10.1038/s41589-025-02102-z"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Lamassu type II system",
    "definition": (
        "A Lamassu system in which an organism possesses a locus with an "
        "additional LmuC component alongside the LmuA effector module and "
        "SMC-like LmuB sensor."
    ),
    "definition_source": CLASSIFICATION,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000232"],
    "synonyms": [
        {
            "synonym_text": "Lamassu type II",
            "synonym_type": "EXACT_SYNONYM",
            "source": CLASSIFICATION,
        }
    ],
    "evidence": [
        {
            "reference": CLASSIFICATION,
            "snippet": (
                "Similarly, an additional hypothetical protein (LmuC) was "
                "identified in about 10.2% of the Lamassu systems detected "
                "(371 systems) (Lamassu type II)."
            ),
            "notes": (
                "Results: Payne et al. name the LmuC-containing subtype. "
                "The quoted frequency belongs to their RefSeq v201 analysis, "
                "not universal prevalence. Methods and Figure 3 identify the "
                "DSM 9628 source locus and its heterologous phage-protection "
                "assays; these do not establish native-host resistance or "
                "universal LmuC essentiality."
            ),
        },
        {
            "reference": STRUCTURE,
            "snippet": (
                "the type-I Lamassu complex from Bacillus cellulasensis and "
                "the type-II Lamassu complex from Vibrio cholerae"
            ),
            "notes": (
                "Abstract: Li et al. report cryo-EM structures for these two "
                "source-qualified complexes. This independently supports the "
                "type-II category, not species-wide possession, equivalence "
                "to a long/short family, or transfer of one nuclease mechanism "
                "to all LmuC-containing effector architectures."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1349767",
            "taxon_label": "Janthinobacterium agaricidamnosum NBRC 102515 = DSM 9628",
            "reference": CLASSIFICATION,
            "note": (
                "Payne et al. amplified the type-II locus from DSM 9628 "
                "genomic DNA (source accession NZ_HG322949.1) and tested it "
                "in Escherichia coli BL21-AI. NCBI independently resolves "
                "that accession and this strain taxon. The example denotes "
                "source-strain possession, not native-host antiviral activity "
                "or possession by every member of the species."
            ),
        }
    ],
    "discussions": [
        {
            "discussion_id": "lamassu-type-ii-component-and-mechanism-scope",
            "prompt": "Resolve type-II effector diversity and LmuC function without conflating axes.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Type II classifies LmuC-containing Lamassu architecture, "
                "not an isolated LmuC hit, a fixed three-gene count, a "
                "long-LmuB clade, or a universal LmuC-dependence phenotype. "
                "The effector module can include more than one gene. Existing "
                "HNH, SMEK and Hydrolase-Protease definitions require LmuC "
                "and therefore fall below this class; HNH also retains its "
                "short-family parent. This is a definition-based hierarchy "
                "inference, not new experimental validation of those children. "
                "Legacy detector-defined effector records and the complete "
                "long/short families are not reparented merely from model "
                "labels or optional LmuC calls. The V. cholerae nuclease "
                "mechanism does not establish chemistry for every effector "
                "module. Native-host activity, protein accessions and broader "
                "mechanistic generalization remain unresolved; no causal "
                "mechanism graph is asserted. Type I remains a separate "
                "discovery lead."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-03",
        }
    ],
}

PREIMAGES = {
    "lamassu_system": {
        "identifier": "traitmech:000232",
        "label": "Lamassu system",
        "definition_hash": "3a54b8d9a0fed9e0a24a76b256b054430b12613c643c51e79689ce6b3ee820f3",
        "old_parents": ["traitmech:000209"],
        "new_parents": ["traitmech:000209"],
        "discussion_id": "lamassu-subtype-and-effector-gap",
        "rationale_hash": "1e6b2cf4f021d907aa3c718dd93addaa021ad8cd661f8a85517d1dac857dde53",
        "addition": (
            " Lamassu type II system (traitmech:000572) now captures the "
            "LmuC-containing component architecture defined by Payne et al. "
            "(DOI:10.1093/nar/gkab883) and independently used by Li et al. "
            "(DOI:10.1038/s41589-025-02102-z). HNH, SMEK and "
            "Hydrolase-Protease already require LmuC in their definitions and "
            "now have this parent; HNH retains its short-family parent too. "
            "This does not assert a three-gene count, universal LmuC "
            "essentiality, or new antiviral validation of those children. "
            "Long/short families and legacy detector rows are not equivalent "
            "to this component class. Type I and family-wide mechanisms "
            "remain open discovery and curation questions."
        ),
    },
    "lamassu_hydrolase_protease_system": {
        "identifier": "traitmech:000567",
        "label": "Lamassu Hydrolase-Protease system",
        "definition_hash": "e2c56c959f13740bc582d2a3c13645301ca52f5355da2e6e6b669c162426eb14",
        "old_parents": ["traitmech:000232"],
        "new_parents": [IDENTIFIER],
        "discussion_id": "lamassu-hydrolase-protease-model-and-mechanism",
        "rationale_hash": "7cc3bae29896caea6f0b295147de1487aa6683a53f9b94f57b06620b9ec58c0c",
        "addition": (
            " The direct parent is now traitmech:000572 Lamassu type II "
            "system because the biological definition already includes "
            "LmuC. The paired effector architecture illustrates why type II "
            "is not restricted to exactly three genes. This refinement "
            "does not resolve the legacy detector-summary drift or assign "
            "the whole trait to one LmuB-length family."
        ),
    },
    "lamassu_hnh_system": {
        "identifier": "traitmech:000568",
        "label": "Lamassu-HNH system",
        "definition_hash": "5881b98b57bbf1dd1cca813f2f49a23fb0ef34529f38a0f0e25f71625f55987d",
        "old_parents": ["traitmech:000570"],
        "new_parents": ["traitmech:000570", IDENTIFIER],
        "discussion_id": "lamassu-hnh-function-and-model-scope",
        "rationale_hash": "264bcb6a576dfcfac59e6ab1bddb8b3cd3b83be92cbf3f8a25255fbb37ce28ab",
        "addition": (
            " A second direct parent, traitmech:000572 Lamassu type II "
            "system, now captures the LmuC component already required by "
            "this definition. The short-family parent is retained because "
            "component presence and LmuB-length family are separate axes. "
            "Neither hierarchy relation experimentally validates HNH "
            "antiviral activity or narrows the detector's broader scope."
        ),
    },
    "lamassu_smek_system": {
        "identifier": "traitmech:000569",
        "label": "Lamassu-SMEK system",
        "definition_hash": "f8beec4fc3a3a3fca7285287fcc310ea0f60c26048a988d548248188e272da27",
        "old_parents": ["traitmech:000232"],
        "new_parents": [IDENTIFIER],
        "discussion_id": "lamassu-smek-function-and-annotation-scope",
        "rationale_hash": "91ba7a910b806f677800fb09b14375c69eecb08e4cbd3724ad4a97f45464135f",
        "addition": (
            " The direct parent is now traitmech:000572 Lamassu type II "
            "system because this definition already includes LmuC. This "
            "component-based refinement neither resolves the long-profile "
            "exception nor restricts the trait to short Lamassu, and does "
            "not confer experimental validation on the computational calls."
        ),
    },
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
        "Added the literature-defined LmuC-containing Lamassu class with "
        "two independent DOI sources, exact snippets and an NCBI-resolved "
        "DSM 9628 possession example. Kept type II distinct from a length "
        "family, fixed gene count and universal biochemical mechanism. "
        "Ignored-and-hidden searches found no exact record or METPO term. "
        "Reserved METPO:1052600 in proposals/metpo_traitmech_v449 and "
        "refined three existing LmuC-containing child definitions' hierarchy.",
    )
    return record


def build_existing(slug: str, expected: dict) -> dict:
    record = yaml.safe_load((TRAITS / f"{slug}.yaml").read_text())
    if (
        record["identifier"] != expected["identifier"]
        or record["label"] != expected["label"]
        or record["mapping_status"] != "PROPOSED"
        or hashlib.sha256(record["definition"].encode()).hexdigest() != expected["definition_hash"]
    ):
        raise SystemExit(f"{slug}: identity or definition changed")
    matches = [d for d in record["discussions"] if d["discussion_id"] == expected["discussion_id"]]
    if len(matches) != 1 or (matches[0]["kind"], matches[0]["status"]) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit(f"{slug}: discussion identity or status changed")
    discussion = matches[0]
    before = discussion["rationale"].removesuffix(expected["addition"])
    if hashlib.sha256(before.encode()).hexdigest() != expected["rationale_hash"]:
        raise SystemExit(f"{slug}: discussion preimage changed")
    already_applied = before != discussion["rationale"]
    parents = expected["new_parents"] if already_applied else expected["old_parents"]
    if record["parent_traits"] != parents:
        raise SystemExit(f"{slug}: hierarchy or application state changed")
    if not already_applied:
        record["parent_traits"] = list(expected["new_parents"])
        discussion["rationale"] += expected["addition"]
        action = "TRACK_TYPE_II_CLASS" if slug == "lamassu_system" else "ADD_TYPE_II_PARENT"
        event(
            record, action,
            "Linked traitmech:000572 Lamassu type II system using the "
            "LmuC-containing classification in DOI:10.1093/nar/gkab883. "
            "Preserved biological definitions, evidence, examples and "
            "length-family distinctions. Historical proposal parent axioms "
            "remain true; v449 documents the additional subclass relations "
            "for upstream minting. This is not new experimental validation.",
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
        "METPO:1052600", record["label"], record["definition"],
        "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", CLASSIFICATION, STRUCTURE]),
        "METPO:1018600", record["synonyms"][0]["synonym_text"], "",
        "metpo_traitmech_2026_10", "HIGH",
        "LmuC-containing component class, not a length clade or fixed gene count. "
        "See proposal.md for HNH, SMEK and Hydrolase-Protease subclass refinements.",
        IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    updates = [(TARGET, record)] + [
        (TRAITS / f"{slug}.yaml", build_existing(slug, expected))
        for slug, expected in PREIMAGES.items()
    ]
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
