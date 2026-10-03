"""Add Druantia II possession, separating DruE assays from full-system defense."""

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
SLUG = "druantia_type_ii_system"
IDENTIFIER = "traitmech:000579"
TARGET = TRAITS / f"{SLUG}.yaml"
PARENT = TRAITS / "druantia_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v456"
TIMESTAMP = "2026-10-03T21:24:00Z"
ARCHITECTURE = "DOI:10.1093/nar/gkab883"
MECHANISM = "DOI:10.65215/LTSpreprints.2026.06.18.000273"
DF = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/definitions/DefenseFinder/"
    "Druantia/Druantia_II.xml"
)
PADLOC = (
    "https://raw.githubusercontent.com/padlocbio/padloc-db/"
    "9e380165633a8d6aef93b5a164cea0f3359bd33f/sys/druantia_type_II.yaml"
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "Druantia type II system",
    "definition": (
        "A Druantia system in which an organism possesses a locus encoding "
        "DruE together with DruM, DruF and DruG."
    ),
    "definition_source": ARCHITECTURE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000234"],
    "synonyms": [{
        "synonym_text": "Type II Druantia system",
        "synonym_type": "EXACT_SYNONYM",
        "source": MECHANISM,
    }],
    "evidence": [
        {
            "reference": ARCHITECTURE,
            "snippet": (
                "the Druantia-like system lacks the type II requisite DruM and DruG proteins"
            ),
            "notes": (
                "Payne et al., Results: Identification of new defence system variants, "
                "and Figure 2C: "
                "type II contains DruE/F/M/G; the proposed type IV shares "
                "DruE/F but replaces the type-II M/G architecture with DruL. "
                "This supports locus composition, not experimental dependence "
                "of each component in every host. The type-II distribution "
                "observed in RefSeq v201 is not a universal taxonomic limit."
            ),
        },
        {
            "reference": MECHANISM,
            "snippet": (
                "DruE alone confers limited protection against a subset of "
                "coliphages in heterologous expression"
            ),
            "notes": (
                "Hou et al., version 2 posted 2026-07-08, not peer reviewed; "
                "PDF https://langtaosha.org.cn/lts/en/preprint/download/273/1236, "
                "pages 5-6 and 18, Figure 1 and supplementary Figure S2. "
                "The Pf-5 druMFGE locus is the source. Purified DruE is an "
                "ATP-dependent 3-prime-to-5-prime helicase preferring "
                "3-prime overhangs and forks, with an asymmetric homodimer. "
                "Standalone DruE in E. coli BL21 gave limited T7/T1 protection; "
                "R1241A reduced protection. Insoluble DruF/G prevented full-system "
                "reconstitution. Native-host phage defense and the link from "
                "unwinding to restriction remain untested or unresolved. "
                "Pf-5 deletion assays under mitomycin C suggest accessory "
                "control of toxicity, not a demonstrated defense trigger."
            ),
        },
        {
            "reference": PADLOC,
            "snippet": "core_genes:\n  - DruE2\n  - DruF2\n  - DruG2\n  - DruM2",
            "notes": (
                "Pinned executable PADLOC rule, retrieved 2026-10-03: "
                "minimum_core and minimum_total are both 4, "
                "maximum_separation is 3, and force_strand is FALSE. "
                "DruK is secondary, not a required fifth component; neutral "
                "and prohibited lists contain only NA. These are detection "
                "constraints, not evidence of active defense."
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
                "Druantia_II__DruM/F/G are accessory slots. DruF permits "
                "Druantia_IV__DruF4. Mandatory Druantia__DruE_1 permits "
                "Druantia__DruE_2, Druantia__DruE_3 or Druantia_IV__DruE4. "
                "One mandatory and three total matches are required; no "
                "forbidden slots are declared. A call alone need not establish "
                "the complete DruM/F/G/E architecture. Exchangeable matches "
                "and missing profiles do not establish biological equivalence "
                "or component absence."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:220664",
        "taxon_label": "Pseudomonas protegens Pf-5",
        "reference": MECHANISM,
        "note": (
            "Natural locus possession in Pf-5, assembly GCF_000012265.1 "
            "identified by Hou et al. version 2, Figure 1a and Methods. "
            "Not a native-host phage-resistance example: infection assays "
            "used standalone DruE in engineered E. coli. NCBI resolves "
            "taxon 220664 to Pseudomonas protegens Pf-5."
        ),
    }],
    "discussions": [{
        "discussion_id": "druantia-type-ii-full-system-defense-gap",
        "prompt": "Resolve full-system defense and accessory functions beyond isolated DruE assays.",
        "kind": "KNOWLEDGE_GAP",
        "status": "OPEN",
        "rationale": (
            "DruM/F/G/E possession is an architecture class, not an assay "
            "result or a universal helicase mechanism. Hou et al. version 2 "
            "provides real DruE biochemistry; the remaining gap is not absence "
            "of protein evidence. RCSB entry 9WAE entity 1 maps Pf-5 "
            "PFL_3016 to UniProtKB:Q4KCB1, a live unreviewed entry checked "
            "2026-10-03. No full-system causal graph is asserted because "
            "native-host phage restriction, accessory regulation and the "
            "unwinding-to-restriction transition are unresolved. The "
            "measured isolated-protein results remain in the evidence notes. "
            "Do not transfer type-III nuclease chemistry to type II or "
            "turn mitomycin-C growth effects into an infection trigger. "
            "A missing profile or incomplete assembly cannot establish "
            "component absence; inspect complete locus context. Organism-level "
            "subtype possession classes are not disjoint because a genome "
            "may encode several loci."
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
    "rationale_hash": "a73d36b4a5a7bcacf33cb663bfe7115349d737a4d258955d692915c17d3b3026",
    "old_tail": "Type II remains an architecture-class discovery lead.",
    "new_tail": (
        "Type II architecture is now represented by traitmech:000579 "
        "Druantia type II system, defined by DruM/F/G/E possession using "
        "DOI:10.1093/nar/gkab883. Hou et al. version 2 "
        "(DOI:10.65215/LTSpreprints.2026.06.18.000273, 2026-07-08 preprint) "
        "adds Pf-5 DruE biochemistry and a limited heterologous assay, "
        "not full-system or native-host phage-defense validation. The "
        "architectural lead is resolved; accessory roles and the transition "
        "from DNA unwinding to phage restriction remain open."
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
        "Added literature-defined Druantia II possession with two DOI "
        "sources, four exact snippets, pinned executable detector rules "
        "and NCBI-resolved Pf-5 possession. Kept the version-2 preprint's "
        "isolated DruE assays distinct from full-system and native-host "
        "defense. Ignored-and-hidden novelty and allocation searches found "
        "no exact record or METPO term; reserved METPO:1053300 in v456. "
        "No protein-resolved full-system causal mechanism is asserted.",
    )
    record_curation_event(
        record, curator="codex", action="CORRECT_EVIDENCE_LOCATOR",
        changes=(
            "Corrected the Payne evidence subsection locator to Results: "
            "Identification of new defence system variants after checking "
            "primary PMC8565338 XML; the snippet, architecture claim and "
            "Figure 2C locator are unchanged. Addresses issue #1639."
        ),
        llm_assisted=True, timestamp="2026-10-03T21:32:00Z",
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
            record, "TRACK_NARROWER_RECORD",
            "Linked traitmech:000579 Druantia II possession using "
            "DOI:10.1093/nar/gkab883 and the July 8 version of "
            "DOI:10.65215/LTSpreprints.2026.06.18.000273. Resolved the "
            "architecture lead while preserving full-system mechanism "
            "uncertainty. Family identity, evidence and example are unchanged.",
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
        "METPO:1053300", record["label"], record["definition"],
        "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", ARCHITECTURE, MECHANISM]),
        "METPO:1053100", record["synonyms"][0]["synonym_text"], "",
        "metpo_traitmech_2026_10", "HIGH",
        "DruM/F/G/E possession; standalone DruE assays do not establish "
        "full-system or native-host defense.", IDENTIFIER,
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
