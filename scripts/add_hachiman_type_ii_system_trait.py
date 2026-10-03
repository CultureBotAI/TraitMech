"""Add HamC-containing Hachiman type II and repair the family-level scope."""

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
SLUG = "hachiman_type_ii_system"
IDENTIFIER = "traitmech:000574"
TARGET = TRAITS / f"{SLUG}.yaml"
PARENT = TRAITS / "hachiman_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v451"
TIMESTAMP = "2026-10-03T18:08:00Z"
CLASSIFICATION = "DOI:10.1093/nar/gkab883"
CORROBORATION = "DOI:10.1038/s41467-025-57851-1"
DF = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/"
    "Hachiman/Hachiman_II.xml"
)
PADLOC = (
    "https://raw.githubusercontent.com/padlocbio/padloc-db/"
    "9e380165633a8d6aef93b5a164cea0f3359bd33f/sys/hachiman_type_II.yaml"
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Hachiman type II system",
    "definition": (
        "A Hachiman system in which an organism possesses a locus encoding "
        "HamA and HamB together with an additional HamC (DUF3223) component."
    ),
    "definition_source": CLASSIFICATION,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000219"],
    "synonyms": [{
        "synonym_text": "Hachiman type II",
        "synonym_type": "EXACT_SYNONYM",
        "source": CLASSIFICATION,
    }],
    "evidence": [
        {
            "reference": CLASSIFICATION,
            "snippet": (
                "a gene encoding a DUF3223 protein (HamC) either upstream "
                "or downstream of hamAB"
            ),
            "notes": (
                "Results, new-subtype classification: Payne et al. name "
                "this HamC-associated Hachiman architecture type II. Methods "
                "and Figure 3 identify the DSM 14551 source locus and show "
                "antiphage activity after expression in E. coli BL21-AI. "
                "The natural source and engineered assay host are distinct. "
                "The paper does not establish native-host resistance, a "
                "universal phage spectrum, HamC essentiality or HamC chemistry."
            ),
        },
        {
            "reference": CORROBORATION,
            "snippet": (
                "Hachiman systems that include HamA, HamB, and HamC "
                "(DUF3223) were referred to as type II"
            ),
            "notes": (
                "Introduction: Cui et al. retain the HamABC classification "
                "and attribute it to Payne et al.; this is corroborating "
                "terminology, not an independent type-II experiment. Their "
                "biochemical experiments on type I-A/I-B do not establish "
                "DNA-damage sensing, DNA cleavage or HamC function in type II."
            ),
        },
        {
            "reference": DF,
            "snippet": '<gene name="Hachiman_II__HamC" presence="mandatory"/>',
            "notes": (
                "Pinned DefenseFinder XML, retrieved 2026-10-03: HamA "
                "(HamA_1 with HamA_2 exchangeable), HamB and HamC are marked "
                "mandatory, but both minimum gene counts are 2 and the "
                "inter-gene maximum space is 5. Thus the model does not "
                "require all three marked components in every accepted call; "
                "a raw Hachiman_II call alone is insufficient to establish "
                "the complete biological architecture. This is a detector "
                "constraint, not an experiment or a trait synonym."
            ),
        },
        {
            "reference": PADLOC,
            "snippet": (
                "minimum_core: 3\nminimum_total: 3\ncore_genes:\n"
                "  - HamA2\n  - HamB2\n  - HamC2"
            ),
            "notes": (
                "Pinned PADLOC rule, retrieved 2026-10-03: all three core "
                "components are required, maximum_separation is 0 and "
                "force_strand is FALSE. This differs from DefenseFinder's "
                "two-gene minimum; neither detector proves functional "
                "defense or experimental necessity of each component."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:173675",
        "taxon_label": "Sphingopyxis witflariensis",
        "reference": CLASSIFICATION,
        "note": (
            "DSM 14551 is the natural source of the type-II locus amplified "
            "from genomic DNA by Payne et al. (NZ_NISJ01000011.1). The NCBI "
            "GenBank source feature independently identifies DSM 14551 and "
            "taxon 173675. This example denotes possession in this source "
            "strain, not all members of the species or native-host resistance. "
            "The reported defense assays used engineered E. coli BL21-AI."
        ),
    }],
    "discussions": [{
        "discussion_id": "hachiman-type-ii-component-and-mechanism-scope",
        "prompt": "Resolve HamC function and type-II mechanisms beyond heterologous defense assays.",
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": (
            "Type II denotes the HamABC locus architecture, not a HamC hit "
            "alone, a source database row or a fixed phage-protection phenotype. "
            "Type-I DNA-damage sensing and DNA-cleavage mechanisms are not "
            "generalized to this class; HamC's biochemical role and necessity "
            "remain unresolved by these sources. No causal mechanism graph "
            "or unverified protein accession is asserted. Native-host assays "
            "and accession-resolved functional evidence remain desirable. "
            "DefenseFinder and PADLOC have different component-count rules; "
            "inspect complete locus context before converting calls into "
            "trait assertions. Component absence cannot be inferred from "
            "a failed hit or incomplete assembly. Type I remains a separate "
            "discovery lead, and coexisting loci would not make organism-level "
            "type-I and type-II possession traits disjoint."
        ),
        "posed_by": "codex",
        "posed_date": "2026-10-03",
    }],
}

OLD_DEFINITION = (
    "A genomics trait describing possession of a Hachiman antiphage defense "
    "locus encoding a HamA/HamB nuclease-helicase core that restricts "
    "bacteriophage propagation through DNA cleavage."
)
NEW_DEFINITION = (
    "A phage defense system in which an organism possesses a Hachiman "
    "antiphage locus encoding a HamA/HamB core."
)
OLD_LOCUS = (
    "A Hachiman antiphage defense locus encoding a HamA/HamB nuclease-helicase "
    "core and, in some type II systems, an accessory HamC component."
)
NEW_LOCUS = (
    "A Hachiman antiphage locus encoding a HamA/HamB core. This graph "
    "describes characterized type-I systems, not the HamC-containing type-II "
    "architecture represented by traitmech:000574."
)
RATIONALE_HASH = "7e16df7efff70044d3378e06bc120fd55fd375ba8572cc2deca4641ebd007e87"
ADDITION = (
    " Hachiman type II system (traitmech:000574) now resolves the "
    "HamABC architecture defined by Payne et al. (DOI:10.1093/nar/gkab883) "
    "and retained by Cui et al. The DSM 14551 locus has heterologous "
    "antiphage evidence, but HamC function and type-II mechanism remain "
    "open. The family definition no longer requires universal DNA cleavage; "
    "this graph and its evidence remain restricted to characterized type-I "
    "systems. Proposal v451 replaces v96's overgeneralized family "
    "definition while preserving the stable local family identifier. "
    "Type I remains a separate architecture-class discovery lead."
)


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(
        record, curator="codex", action=action, changes=changes,
        llm_assisted=True, timestamp=TIMESTAMP,
    )


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(
        record, "MINTED_TRAITMECH_ID",
        "Added the literature-defined HamABC possession class with two DOI "
        "sources, exact snippets, pinned detector rules and the NCBI-resolved "
        "DSM 14551 example. Searches included ignored and hidden files and "
        "found no exact live record or METPO class. Reserved METPO:1052801 "
        "in v451; METPO:1052800 replaces the broad parent's v96 proposal. "
        "Kept natural source, heterologous activity and type-I chemistry distinct.",
    )
    return record


def build_parent() -> dict:
    record = yaml.safe_load(PARENT.read_text())
    if (
        record.get("identifier") != "traitmech:000219"
        or record.get("label") != "Hachiman system"
        or record.get("mapping_status") != "PROPOSED"
        or record.get("parent_traits") != ["traitmech:000209"]
    ):
        raise SystemExit("Parent identity or hierarchy changed")
    discussions = [d for d in record.get("discussions", [])
                   if d.get("discussion_id") == "hachiman-subtype-and-trigger-gap"]
    graphs = [g for g in record.get("causal_graphs", [])
              if g.get("graph_id") == "hachiman_hamab_dna_cleavage"]
    if len(discussions) != 1 or len(graphs) != 1:
        raise SystemExit("Parent discussion or graph identity changed")
    discussion, graph = discussions[0], graphs[0]
    if (discussion.get("kind"), discussion.get("status")) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit("Parent discussion status changed")
    nodes = [n for n in graph.get("nodes", []) if n.get("node_id") == "hachiman_locus"]
    if len(nodes) != 1 or nodes[0].get("node_type") != "GENETIC_ELEMENT":
        raise SystemExit("Parent locus node changed")
    node = nodes[0]
    rationale = discussion.get("rationale", "")
    before = rationale.removesuffix(ADDITION)
    if hashlib.sha256(before.encode()).hexdigest() != RATIONALE_HASH:
        raise SystemExit("Parent discussion preimage changed")
    applied = before != rationale
    expected = (NEW_DEFINITION, NEW_LOCUS) if applied else (OLD_DEFINITION, OLD_LOCUS)
    if (record.get("definition"), node.get("description")) != expected:
        raise SystemExit("Parent definition or locus preimage changed")
    if not applied:
        record["definition"] = NEW_DEFINITION
        node["description"] = NEW_LOCUS
        discussion["rationale"] += ADDITION
        event(
            record, "SCOPE_HACHIMAN_FAMILY_AND_TYPE_II",
            "Addressed #1630: removed the unsupported universal DNA-cleavage "
            "condition from the family definition while retaining the type-I "
            "mechanism evidence and graph scope. Linked the new HamABC child "
            "traitmech:000574; HamC chemistry remains an open question. "
            "Proposal v451 supersedes v96 without editing the old TSV.",
        )
    return record


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
        (parent, "hachiman_system", "METPO:1052800", "METPO:1016300",
         "Replaces v96 METPO:1017300; family definition does not require universal DNA cleavage."),
        (child, SLUG, "METPO:1052801", "METPO:1052800",
         "HamABC architecture; heterologous defense is not native-host or universal mechanism evidence."),
    ]:
        writer.writerow([
            proposed, record["label"], record["definition"],
            "|".join([f"TraitMech:data/traits/genomics/{slug}.yaml",
                      record["definition_source"], CORROBORATION]),
            broader, "|".join(s["synonym_text"] for s in record["synonyms"]),
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
