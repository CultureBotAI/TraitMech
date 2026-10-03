"""Add LmuC-lacking Lamassu type I and resolve its existing discovery links."""

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
SLUG = "lamassu_type_i_system"
IDENTIFIER = "traitmech:000573"
TARGET = TRAITS / f"{SLUG}.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v450"
TIMESTAMP = "2026-10-03T15:57:07Z"
CLASSIFICATION = "DOI:10.1073/pnas.2519643122"
STRUCTURE = "DOI:10.1038/s41589-025-02102-z"
UNIPROT = "https://rest.uniprot.org/uniprotkb/P0DW44.json"
PDB = "https://data.rcsb.org/rest/v1/core/polymer_entity/9UX7/1"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Lamassu type I system",
    "definition": (
        "A Lamassu system in which an organism possesses a locus encoding "
        "the LmuA effector and SMC-like LmuB sensor but no LmuC component."
    ),
    "definition_source": CLASSIFICATION,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000232"],
    "synonyms": [{
        "synonym_text": "type I Lamassu",
        "synonym_type": "EXACT_SYNONYM",
        "source": CLASSIFICATION,
    }],
    "evidence": [
        {
            "reference": CLASSIFICATION,
            "snippet": (
                "We observed loss of LmuC in a specific clade (Clade S, Fig. 1B), "
                "an architecture previously called type I Lamassu shown to be antiphage"
            ),
            "notes": (
                "Results, effector-diversity paragraph: Haudiquet et al. "
                "explicitly identify the LmuC-loss architecture as type I. "
                "Clade S occurs in their short-Lamassu phylogeny, but this "
                "does not make type I equivalent to the whole short family "
                "or establish a universal protein-length cutoff. Clade O's "
                "LmuA effector-domain loss is a different observation."
            ),
        },
        {
            "reference": STRUCTURE,
            "snippet": (
                "the type-I Lamassu complex from Bacillus cellulasensis and "
                "the type-II Lamassu complex from Vibrio cholerae"
            ),
            "notes": (
                "Abstract: Li et al. independently distinguish the two "
                "source-qualified complexes. The associated 9UX7 deposition "
                "identifies the type-I source as Bacillus sp. nio-1130, "
                "NCBITaxon:1761765. Retain the issuing authority's current "
                "label rather than asserting species-name equivalence from "
                "the abstract. One studied nuclease mechanism is not a "
                "universal mechanism for every type-I effector."
            ),
        },
        {
            "reference": UNIPROT,
            "snippet": (
                "Component of antiviral defense system Lamassu type I, "
                "composed of LmuA and LmuB."
            ),
            "notes": (
                "Reviewed P0DW44, entry version 8, retrieved 2026-10-03: "
                "the FUNCTION annotation identifies the LmuA/LmuB system "
                "in the NIO-1130 source strain (taxon 1761765), citing "
                "PMID:29371424. Its protection assays were heterologous "
                "expression in B. subtilis BEST7003, not native-host assays. "
                "The source organism and expression host are not interchangeable."
            ),
        },
        {
            "reference": PDB,
            "snippet": (
                '"pdbx_gene_src_ncbi_taxonomy_id":"1761765",'
                '"pdbx_gene_src_scientific_name":"Bacillus sp. nio-1130"'
            ),
            "notes": (
                "PDB 9UX7 entity 1 independently records the LmuB source "
                "taxon and maps the sequence to P0DW44. The separate "
                "expression host is E. coli. The deposited 562-residue "
                "length is not a type-I membership threshold; absence of "
                "a component from a purified structure alone would not "
                "establish genomic absence."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:1761765",
        "taxon_label": "Bacillus sp. nio-1130",
        "reference": UNIPROT,
        "note": (
            "NIO-1130 is the source strain of the reviewed LmuB entry "
            "P0DW44 explicitly annotated as part of Lamassu type I. PDB "
            "9UX7 entity 1 independently identifies the same source taxon; "
            "NCBI confirms this exact current label. The example denotes "
            "source-strain possession, not native-host resistance. The "
            "cited defense assays used B. subtilis BEST7003 and structural "
            "expression used E. coli. The paper's B. cellulasensis name "
            "is not asserted as a taxonomic synonym or species-wide trait."
        ),
    }],
    "discussions": [{
        "discussion_id": "lamassu-type-i-absence-and-mechanism-scope",
        "prompt": "Resolve type-I architecture and mechanism without inferring absence from missing hits.",
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": (
            "Type I denotes the literature-supported LmuA/LmuB architecture "
            "without LmuC, not an isolated LmuB hit, a failed LmuC detector "
            "call, an incomplete assembly or a knockout of a type-II locus. "
            "Component absence must be established in the biological locus; "
            "absence from a purified complex alone is insufficient. The "
            "reported clade S is in the short family, but the component "
            "definition is not equated with that whole family or a protein "
            "length bin. Keep the broad Lamassu parent until wider "
            "phylogenetic scope is established; no existing detector-defined "
            "effector subtype is reparented from an optional LmuC rule. "
            "Type-II loci can coexist in the same genome, so these organism-level "
            "possession traits are not asserted disjoint. Source-specific "
            "nuclease activity is not generalized to all type-I effectors. "
            "A family-wide mechanism, native-host activity and the paper's "
            "B. cellulasensis nomenclature relative to current NCBI naming "
            "remain unresolved. No causal mechanism graph is asserted."
        ),
        "posed_by": "codex",
        "posed_date": "2026-10-03",
    }],
}

PREIMAGES = {
    "lamassu_system": {
        "identifier": "traitmech:000232",
        "label": "Lamassu system",
        "definition_hash": "3a54b8d9a0fed9e0a24a76b256b054430b12613c643c51e79689ce6b3ee820f3",
        "parents": ["traitmech:000209"],
        "discussion_id": "lamassu-subtype-and-effector-gap",
        "rationale_hash": "0ded329dfe3fd472b3e00bb0fac75e61f35a9cb9983531f5d491ca0b0952aa02",
        "addition": (
            " Lamassu type I system (traitmech:000573) now resolves the "
            "component-class discovery lead: Haudiquet et al. explicitly "
            "identify the LmuC-loss architecture as type I, and Li et al. "
            "independently study a type-I LmuA/LmuB complex. This is not "
            "equivalent to all short Lamassu or proof that every failed "
            "LmuC hit is biological absence. No existing effector-defined "
            "child is reparented. Family-wide mechanisms, legacy model "
            "reconciliation and native-host activity remain open."
        ),
    },
    "short_lamassu_system": {
        "identifier": "traitmech:000570",
        "label": "short Lamassu system",
        "definition_hash": "1160fd24312fe04a124fd0209f85933c672fbb8320cb0700d32f16634687d223",
        "parents": ["traitmech:000232"],
        "discussion_id": "short-lamassu-classification-and-mechanism-scope",
        "rationale_hash": "c63b1a36786ec4f3036329eacdb8bc4f03069c8211c6e623cfe2954ee274dcd7",
        "addition": (
            " The LmuC-loss architecture is now represented separately by "
            "traitmech:000573 Lamassu type I system. The paper identifies "
            "clade S as type I; clade O's effector-domain loss remains a "
            "distinct question. The new component class is not treated as "
            "a synonym for this whole length family, and its broader "
            "phylogenetic distribution is left open rather than inferred "
            "from one clade. Existing hierarchy and mechanism scope are unchanged."
        ),
    },
    "lamassu_type_ii_system": {
        "identifier": "traitmech:000572",
        "label": "Lamassu type II system",
        "definition_hash": "09877d201fc919404bb865d2a7090b7d52a178f75764ebb1205ad351beb1a9ea",
        "parents": ["traitmech:000232"],
        "discussion_id": "lamassu-type-ii-component-and-mechanism-scope",
        "rationale_hash": "ec363a4def554a2756e6be31afddda782201ca43deba2d243dd99d53857fba5c",
        "addition": (
            " That discovery lead is now represented by traitmech:000573 "
            "Lamassu type I system for LmuA/LmuB loci without LmuC. The "
            "two component architectures do not establish disjoint "
            "organism-level possession classes: one genome could encode "
            "both. LmuC absence is not inferred from a missing model hit "
            "or a type-II knockout. This record's definition, child "
            "classification and unresolved mechanism questions are unchanged."
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
        "Added the LmuC-lacking Lamassu type-I possession class with two "
        "independent primary DOI sources, exact snippets, reviewed UniProt "
        "and PDB source metadata, and the NCBI-resolved NIO-1130 example. "
        "Ignored-and-hidden searches found no exact record or METPO class. "
        "Reserved METPO:1052700 in proposals/metpo_traitmech_v450. Linked "
        "existing parent, short-family and type-II discussions without "
        "changing their biological definitions or hierarchy.",
    )
    return record


def build_existing(slug: str, expected: dict) -> dict:
    record = yaml.safe_load((TRAITS / f"{slug}.yaml").read_text())
    if (
        record["identifier"] != expected["identifier"]
        or record["label"] != expected["label"]
        or record["mapping_status"] != "PROPOSED"
        or record["parent_traits"] != expected["parents"]
        or hashlib.sha256(record["definition"].encode()).hexdigest() != expected["definition_hash"]
    ):
        raise SystemExit(f"{slug}: identity, hierarchy or definition changed")
    matches = [d for d in record["discussions"] if d["discussion_id"] == expected["discussion_id"]]
    if len(matches) != 1 or (matches[0]["kind"], matches[0]["status"]) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit(f"{slug}: discussion identity or status changed")
    discussion = matches[0]
    before = discussion["rationale"].removesuffix(expected["addition"])
    if hashlib.sha256(before.encode()).hexdigest() != expected["rationale_hash"]:
        raise SystemExit(f"{slug}: discussion preimage changed")
    if before == discussion["rationale"]:
        discussion["rationale"] += expected["addition"]
        event(
            record, "TRACK_TYPE_I_CLASS",
            "Linked traitmech:000573 Lamassu type I system to the existing "
            "component-architecture discussion using DOI:10.1073/pnas.2519643122 "
            "and DOI:10.1038/s41589-025-02102-z. Preserved all definitions, "
            "parents, evidence, examples and prior history. Component absence, "
            "LmuB-length family and experimental activity remain separate claims.",
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
        "METPO:1052700", record["label"], record["definition"],
        "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", CLASSIFICATION, STRUCTURE, UNIPROT, PDB]),
        "METPO:1018600", record["synonyms"][0]["synonym_text"], "",
        "metpo_traitmech_2026_10", "HIGH",
        "LmuA/LmuB component architecture without LmuC; not a missing detector hit "
        "or a synonym for the short family. No organism-level disjointness asserted.",
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
