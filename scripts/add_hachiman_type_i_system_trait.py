"""Add HamC-lacking Hachiman type I and link existing discovery discussions."""

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
SLUG = "hachiman_type_i_system"
IDENTIFIER = "traitmech:000575"
TARGET = TRAITS / f"{SLUG}.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v452"
TIMESTAMP = "2026-10-03T18:37:00Z"
CLASSIFICATION = "DOI:10.1093/nar/gkab883"
EXPERIMENTS = "DOI:10.1038/s41467-025-57851-1"
DF = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/"
    "Hachiman/Hachiman.xml"
)
PADLOC = (
    "https://raw.githubusercontent.com/padlocbio/padloc-db/"
    "9e380165633a8d6aef93b5a164cea0f3359bd33f/sys/hachiman_type_I.yaml"
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Hachiman type I system",
    "definition": (
        "A Hachiman system in which an organism possesses a HamA/HamB "
        "locus without a HamC component."
    ),
    "definition_source": EXPERIMENTS,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000219"],
    "synonyms": [{
        "synonym_text": "Hachiman type I",
        "synonym_type": "EXACT_SYNONYM",
        "source": CLASSIFICATION,
    }],
    "evidence": [
        {
            "reference": CLASSIFICATION,
            "snippet": (
                "We refer to the new Hachiman systems as type II, and "
                "the original Hachiman systems as type I."
            ),
            "notes": (
                "Results, new-subtype classification: Payne et al. distinguish "
                "the original HamAB architecture from the newly identified "
                "HamC-associated systems. Figure 2C depicts the component "
                "contrast. These names classify system architecture, not "
                "individual proteins or organism-level disjoint classes."
            ),
        },
        {
            "reference": EXPERIMENTS,
            "snippet": (
                "Payne et al. classified the Hachiman systems that contain "
                "only HamA and HamB as type I"
            ),
            "notes": (
                "Introduction: Cui et al. explicitly retain the HamAB-only "
                "classification, citing Payne rather than independently "
                "originating the name. Their own experiments characterize "
                "type I-A and I-B. Methods identify the type-I-B source "
                "as K-12, U00096.3 positions 2761204-2765368. Defense assays "
                "used plasmid-borne HamAB in a hamAB-deleted MG1655 host; "
                "these are not measurements of unmodified native-locus activity. "
                "The subtype results do not establish a universal type-I "
                "effector domain, activation trigger or phage spectrum."
            ),
        },
        {
            "reference": PADLOC,
            "snippet": "prohibited_genes:\n  - HamC2",
            "notes": (
                "Pinned PADLOC rule, retrieved 2026-10-03: the core is "
                "HamA1 plus HamB1, minimum_core and minimum_total are 2, "
                "maximum_separation is 0, and force_strand is FALSE. HamC2 "
                "is prohibited in the detected system. This is a profile "
                "constraint, not proof that a biological locus lacks every "
                "divergent HamC homolog or that the whole genome lacks HamC."
            ),
        },
        {
            "reference": DF,
            "snippet": '<gene name="Hachiman__HamB" presence="mandatory"/>',
            "notes": (
                "Pinned DefenseFinder XML, retrieved 2026-10-03: HamA_1 "
                "(exchangeable with HamA_2) and HamB are mandatory, both "
                "minimum counts are 2, and inter_gene_max_space is 5. The "
                "model has no forbidden HamC component. A raw Hachiman call "
                "therefore does not establish the type-I absence condition; "
                "complete biological locus context must be reviewed. The "
                "model name is not added as a type-I exact synonym."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:511145",
        "taxon_label": "Escherichia coli str. K-12 substr. MG1655",
        "reference": EXPERIMENTS,
        "note": (
            "Cui et al. identify the type-I-B source locus at U00096.3 "
            "positions 2761204-2765368. NCBI independently resolves that "
            "accession to K-12 MG1655, taxon 511145; the source region "
            "contains abpA (HamA) and abpB (HamB). This example denotes "
            "natural source-strain possession, not all E. coli strains or "
            "native-locus protection measured without manipulation. Their "
            "defense assays complemented a hamAB-deleted MG1655 host with "
            "plasmid-borne HamAB, and protein expression used BL21(DE3). "
            "The type-I assignment comes from the paper, not an inference "
            "of HamC absence from the retrieved sequence interval alone."
        ),
    }],
    "discussions": [{
        "discussion_id": "hachiman-type-i-absence-and-subtype-scope",
        "prompt": "Resolve type-I subtype mechanisms without equating missing hits with component absence.",
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": (
            "Type I denotes the literature-defined HamAB architecture without "
            "HamC, not an isolated HamA/HamB hit, an incomplete assembly, "
            "a purified-complex omission or automatic reclassification of a "
            "type-II HamC knockout. A genome may possess both type-I and "
            "type-II loci, so these possession traits are not disjoint. "
            "Cui et al. separate four HamA-domain subtypes within type I; "
            "experimental support for I-A/I-B does not validate every "
            "predicted subtype or establish one universal nuclease domain, "
            "DNA substrate, trigger or antiviral spectrum. Subtype classes "
            "remain discovery leads requiring separate source review. "
            "The broader Hachiman record already retains source-qualified "
            "I-A/I-B mechanism evidence; no duplicate or universal causal "
            "graph is added here. Native-locus activity and broader "
            "accession-resolved functional generalization remain open."
        ),
        "posed_by": "codex",
        "posed_date": "2026-10-03",
    }],
}

PREIMAGES = {
    "hachiman_system": {
        "identifier": "traitmech:000219",
        "label": "Hachiman system",
        "parents": ["traitmech:000209"],
        "definition_hash": "6c8c6595406813646c5c81f457933a29c9120af1525629ca098993d4cd7593f3",
        "discussion_id": "hachiman-subtype-and-trigger-gap",
        "rationale_hash": "9d9b02f6bc894a8b6f5e5ccf69731d7a953646817699fb4e7db0c51da1b7925f",
        "addition": (
            " That architecture-class lead is now represented by "
            "traitmech:000575 Hachiman type I system for HamAB loci without "
            "HamC. The component definition follows Payne and Cui, not a "
            "failed detector hit or a type-II knockout. The existing graph "
            "still describes characterized I-A/I-B mechanisms, not all "
            "type-I subtypes. Subtype-specific mechanisms and native-locus "
            "activity remain open; no graph, example or hierarchy is changed."
        ),
    },
    "hachiman_type_ii_system": {
        "identifier": "traitmech:000574",
        "label": "Hachiman type II system",
        "parents": ["traitmech:000219"],
        "definition_hash": "f9f440256e7e7fd7947d638edb6fe9b7e3e7e794c88930c06690804956402c1e",
        "discussion_id": "hachiman-type-ii-component-and-mechanism-scope",
        "rationale_hash": "a2d18ab292880b52d4ba89d2020e47aa857e51025e4ac676a2036e5e761bee71",
        "addition": (
            " The type-I lead is now represented by traitmech:000575 "
            "Hachiman type I system for the literature-defined HamC-lacking "
            "HamAB architecture. This does not imply organism-level "
            "disjointness, turn missing detector hits into absence evidence, "
            "or transfer type-I chemistry to type II. HamC function and "
            "type-II mechanisms remain unresolved."
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
        "Added the literature-defined HamC-lacking HamAB possession class "
        "with two DOI sources, exact snippets, pinned detector constraints "
        "and an NCBI-resolved MG1655 source-locus example. Novelty and "
        "allocation searches included ignored and hidden files; the fresh "
        "METPO seed has no exact class. Reserved METPO:1052900 in v452. "
        "Kept natural source, engineered assays and subtype chemistry distinct.",
    )
    return record


def build_existing(slug: str, expected: dict) -> dict:
    record = yaml.safe_load((TRAITS / f"{slug}.yaml").read_text())
    if (
        record.get("identifier") != expected["identifier"]
        or record.get("label") != expected["label"]
        or record.get("mapping_status") != "PROPOSED"
        or record.get("parent_traits") != expected["parents"]
        or hashlib.sha256(record.get("definition", "").encode()).hexdigest() != expected["definition_hash"]
    ):
        raise SystemExit(f"{slug}: identity, hierarchy or definition changed")
    matches = [d for d in record.get("discussions", [])
               if d.get("discussion_id") == expected["discussion_id"]]
    if len(matches) != 1 or (matches[0].get("kind"), matches[0].get("status")) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit(f"{slug}: discussion identity or status changed")
    discussion = matches[0]
    before = discussion.get("rationale", "").removesuffix(expected["addition"])
    if hashlib.sha256(before.encode()).hexdigest() != expected["rationale_hash"]:
        raise SystemExit(f"{slug}: discussion preimage changed")
    if before == discussion["rationale"]:
        discussion["rationale"] += expected["addition"]
        event(
            record, "TRACK_HACHIMAN_TYPE_I_CLASS",
            "Linked traitmech:000575 Hachiman type I system using the "
            "component classification in DOI:10.1093/nar/gkab883 and "
            "DOI:10.1038/s41467-025-57851-1. Kept definitions, hierarchy, "
            "examples, evidence and graphs unchanged; mechanism questions "
            "remain open. No absence assertion is inferred from detector output.",
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
        "METPO:1052900", record["label"], record["definition"],
        "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", EXPERIMENTS, CLASSIFICATION]),
        "METPO:1052800", record["synonyms"][0]["synonym_text"], "",
        "metpo_traitmech_2026_10", "HIGH",
        "HamAB architecture without HamC; not a missing-hit label or universal "
        "mechanism. Parent uses v451 replacement, not superseded v96.",
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
