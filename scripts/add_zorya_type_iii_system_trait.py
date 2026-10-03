"""Add the literature-defined ZorA/B/F/G Zorya type III possession class."""

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
SLUG = "zorya_type_iii_system"
IDENTIFIER = "traitmech:000576"
TARGET = TRAITS / f"{SLUG}.yaml"
PARENT = TRAITS / "zorya_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v453"
TIMESTAMP = "2026-10-03T19:16:00Z"
DISCOVERY = "DOI:10.1093/nar/gkab883"
ARCHITECTURE = "DOI:10.1038/s41467-025-57397-2"
DF = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/"
    "Zorya/Zorya_TypeIII.xml"
)
PADLOC = (
    "https://raw.githubusercontent.com/padlocbio/padloc-db/"
    "9e380165633a8d6aef93b5a164cea0f3359bd33f/sys/zorya_type_III.yaml"
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Zorya type III system",
    "definition": (
        "A Zorya system in which an organism possesses a locus encoding "
        "ZorA and ZorB together with ZorF and ZorG."
    ),
    "definition_source": DISCOVERY,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000217"],
    "synonyms": [{
        "synonym_text": "Zorya type III",
        "synonym_type": "EXACT_SYNONYM",
        "source": DISCOVERY,
    }],
    "evidence": [
        {
            "reference": DISCOVERY,
            "snippet": (
                "our data demonstrate activity of the Zorya type III system "
                "comprised of ZorA, ZorB, ZorF and ZorG"
            ),
            "notes": (
                "Payne et al., Discussion and Figure 2C: the four-component "
                "architecture is ZorF/ZorA/ZorB/ZorG. The Results paragraph "
                "instead says zorBC; that wording conflicts with the figure "
                "and Discussion and is not used as the component definition. "
                "Methods identify the natural source as Stenotrophomonas "
                "nitritireducens DSM 12575, NZ_LDJG01000021.1. Figure 3 assays "
                "tested the cloned system in E. coli BL21-AI, not native "
                "defense in DSM 12575. The proposed regulatory roles of "
                "ZorF/ZorG are hypotheses, not demonstrated chemistry."
            ),
        },
        {
            "reference": ARCHITECTURE,
            "snippet": (
                "Zorya III instead encodes a DUF3348 domain protein (ZorF) "
                "and a DUF2894 domain protein (ZorG)"
            ),
            "notes": (
                "Mariano et al., Introduction and Figure 1a/b, independently "
                "retain ZorA/ZorB as the shared core and ZorF/ZorG as the "
                "type-III distinguishing components, citing Payne for the "
                "classification. Their mechanistic experiments concern "
                "types I and II; these do not demonstrate a type-III ion "
                "substrate, nuclease activity, phage trigger or death pathway."
            ),
        },
        {
            "reference": PADLOC,
            "snippet": "core_genes:\n  - ZorA3\n  - ZorB3\n  - ZorF3\n  - ZorG3",
            "notes": (
                "Pinned executable PADLOC rule, retrieved 2026-10-03: "
                "minimum_core and minimum_total are both 4, "
                "maximum_separation is 0, and force_strand is FALSE. "
                "There are no additional secondary, neutral or prohibited "
                "profiles. These are detection constraints, not evidence "
                "for biological essentiality or activity of every predicted locus."
            ),
        },
        {
            "reference": DF,
            "snippet": (
                '<model inter_gene_max_space="5" min_mandatory_genes_required="3" '
                'min_genes_required="3" vers="2.0">'
            ),
            "notes": (
                "Pinned executable DefenseFinder model, retrieved 2026-10-03: "
                "four mandatory slots are Zorya__ZorA2 (exchangeable with "
                "Zorya__ZorA), Zorya__ZorB, Zorya_III__ZorG3 and "
                "Zorya_III__ZorF3, but the minimum counts are only 3. "
                "A detector call therefore does not by itself establish "
                "all four biological components; inspect the complete locus. "
                "The raw detector key is not an exact trait synonym."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:83617",
        "taxon_label": "Stenotrophomonas nitritireducens",
        "reference": DISCOVERY,
        "note": (
            "Payne et al. amplified the type-III system from DSM 12575 "
            "genomic DNA, accession NZ_LDJG01000021.1. NCBI independently "
            "resolves that accession to this species, taxon 83617, and "
            "strain DSM 12575. This example is limited to natural possession "
            "by the named strain, not species-wide possession or a native-host "
            "protection assay. The paper tested a plasmid-borne construct "
            "in E. coli BL21-AI, which naturally lacked the system."
        ),
    }],
    "discussions": [{
        "discussion_id": "zorya-type-iii-component-and-mechanism-scope",
        "prompt": "Resolve type-III component roles without transferring type-I/II mechanisms.",
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": (
            "The accepted architecture follows Payne Figure 2C and Discussion "
            "plus Mariano Figure 1 and Introduction, not Payne's conflicting "
            "Results wording or a detector key alone. ZorF/ZorG regulation "
            "of ZorAB is a proposal; no direct component-resolved mechanism "
            "is asserted here. Neither type-I phage-DNA degradation nor "
            "type-II ZorE nickase activity is assigned to type III. The "
            "ion substrate, activation trigger, native-host activity, "
            "individual component dependence and antiviral breadth remain "
            "open. The four-component definition is not weakened to match "
            "DefenseFinder's three-match threshold, and a missing hit or "
            "incomplete assembly is not proof of biological component "
            "absence. Multiple subtype loci may coexist in a genome; no "
            "organism-level disjointness is asserted. No mechanistic graph "
            "or protein examples are added without accession-resolved "
            "functional evidence."
        ),
        "posed_by": "codex",
        "posed_date": "2026-10-03",
    }],
}

PREIMAGE = {
    "identifier": "traitmech:000217",
    "label": "Zorya system",
    "parents": ["traitmech:000209"],
    "definition_hash": "83cf218126fdad415897ed1d2ef696962297012c961d7f7f7ff5dd3212e8e27c",
    "discussion_id": "zorya-subtype-effector-and-trigger-gap",
    "rationale_hash": "4f4c6b5395b302d97820364cdc1f406dbb4196f7b5231370ef4c3ff821d074ff",
    "addition": (
        " The type-III architecture is now represented by traitmech:000576 "
        "Zorya type III system for ZorA/ZorB/ZorF/ZorG loci. Payne Figure "
        "2C and Discussion plus Mariano's Introduction support that "
        "composition despite the conflicting zorBC wording in Payne's "
        "Results. DefenseFinder's three-match threshold is not a complete "
        "four-component biological definition. Type-III component roles "
        "and native-host mechanisms remain open; the family definition, "
        "graph and type-I/II records are unchanged."
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
        "Added the literature-defined ZorA/B/F/G possession class with "
        "two DOI sources, four exact snippets, pinned executable detection "
        "rules and the NCBI-resolved DSM 12575 source-strain example. "
        "Ignored-and-hidden novelty and allocation searches found no exact "
        "record or METPO term; reserved METPO:1053000 in v453. Kept "
        "source strain, heterologous assay, predicted regulation and "
        "detector thresholds distinct.",
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
        raise SystemExit("Zorya parent identity, hierarchy or definition changed")
    matches = [d for d in record.get("discussions", [])
               if d.get("discussion_id") == PREIMAGE["discussion_id"]]
    if len(matches) != 1 or (matches[0].get("kind"), matches[0].get("status")) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit("Zorya parent discussion identity or status changed")
    discussion = matches[0]
    before = discussion.get("rationale", "").removesuffix(PREIMAGE["addition"])
    if hashlib.sha256(before.encode()).hexdigest() != PREIMAGE["rationale_hash"]:
        raise SystemExit("Zorya parent discussion preimage changed")
    if before == discussion["rationale"]:
        discussion["rationale"] += PREIMAGE["addition"]
        event(
            record, "TRACK_ZORYA_TYPE_III_CLASS",
            "Linked traitmech:000576 using DOI:10.1093/nar/gkab883 and "
            "DOI:10.1038/s41467-025-57397-2. Kept the family definition, "
            "hierarchy, graph, evidence and example unchanged; type-III "
            "component functions remain open rather than inheriting type-I/II chemistry.",
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
        "METPO:1053000", record["label"], record["definition"],
        "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", DISCOVERY, ARCHITECTURE]),
        "METPO:1017100", record["synonyms"][0]["synonym_text"], "",
        "metpo_traitmech_2026_10", "HIGH",
        "Literature-defined ZorA/B/F/G architecture, not an incomplete "
        "detector call or a universal nuclease mechanism.", IDENTIFIER,
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
