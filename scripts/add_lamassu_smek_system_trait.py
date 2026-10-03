"""Add the Lamassu-SMEK architecture without inferring SMEK chemistry."""

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

from traitmech.curate.curation_event import record_curation_event  # noqa: E402, RUF100
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402, RUF100

SLUG = "lamassu_smek_system"
TARGET = ROOT / "data/traits/genomics" / f"{SLUG}.yaml"
PARENT = ROOT / "data/traits/genomics/lamassu_system.yaml"
IDENTIFIER = "traitmech:000569"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v446"
TIMESTAMP = "2026-10-03T11:15:00Z"
HAUDIQUET = "DOI:10.1073/pnas.2519643122"
PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/"
)
MODEL = PREFIX + "definitions/DefenseFinder/Lamassu-Fam/Lamassu_SMEK.xml"
DATASET = "https://pmc-oa-opendata.s3.amazonaws.com/PMC12663957.1/pnas.2519643122.sd01.xlsx"
ASSEMBLY = (
    "https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_021491935.1/dataset_report"
)
OLD_PARENT_HASH = "4369c1b0ded1f4b0ba83824d6285b9d34685f8bf998901dd03a80405d22187a0"
PARENT_ADDITION = (
    " Lamassu-SMEK system (traitmech:000569) now captures a locus with "
    "SMEK-domain LmuA, LmuB, and LmuC. The paper describes SMEK as short-specific, "
    "but its dataset contains 124 short-profile system calls and one long-profile "
    "call; the latter requires reconciliation before asserting a biological "
    "long-LmuB subtype. The definition therefore does not impose a LmuB-length "
    "restriction. The three-component architecture is not equivalent to the "
    "single-gene DS-27 system that also uses SMEK as a working label. "
    "SMEK-specific functional validation and chemistry remain unresolved."
)


def evidence(reference: str, snippet: str, notes: str) -> dict[str, str]:
    return {"reference": reference, "snippet": snippet, "notes": notes}


RECORD = {
    "identifier": IDENTIFIER,
    "label": "Lamassu-SMEK system",
    "definition": (
        "A Lamassu system in which an organism possesses a locus encoding an "
        "LmuA effector with a SMEK domain, an SMC-like LmuB sensor, and LmuC."
    ),
    "definition_source": HAUDIQUET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000232"],
    "synonyms": [
        {"synonym_text": "Lamassu_SMEK", "synonym_type": "RELATED_SYNONYM", "source": MODEL},
        {
            "synonym_text": "Lamassu/Lamassu/Lamassu_SMEK",
            "synonym_type": "RELATED_SYNONYM",
            "source": DATASET,
        },
    ],
    "evidence": [
        evidence(
            HAUDIQUET,
            "others are type-specific like the flavin-containing monooxygenase (FMO) "
            "for long Lamassu, and HNH, SMEK, and Lipase for short Lamassu.",
            "Results, effector-diversity paragraph: 'others' refers to LmuA "
            "effector types. The paper recognizes SMEK-bearing Lamassu and "
            "describes it as short-specific. Dataset S1 nevertheless contains "
            "one long-profile SMEK-system call; that annotation discrepancy "
            "is not resolved by treating the detector as experimental evidence.",
        ),
        evidence(
            MODEL,
            '<model inter_gene_max_space="1" min_mandatory_genes_required="3" '
            'min_genes_required="3" vers="2.0">',
            "The executable model requires three mandatory components and "
            "permits at most one intervening gene between components.",
        ),
        evidence(
            MODEL,
            '<gene name="Lamassu__LmuA_SMEK" presence="mandatory"/>',
            "SMEK-bearing LmuA is mandatory, without an exchangeable effector. "
            "Other named LmuA effector profiles are forbidden by separate blocks. "
            "An isolated SMEK-domain or profile hit does not establish this trait.",
        ),
        evidence(
            MODEL,
            '<gene name="Lamassu__LmuB_Long" presence="mandatory">\n'
            '<exchangeables>\n<gene name="Lamassu__LmuB_Short"/>\n'
            "</exchangeables>\n</gene>",
            "The detector accepts either long or short LmuB. This permissiveness "
            "does not prove biological function in either clade. The trait "
            "definition follows the shared architecture without a length restriction.",
        ),
        evidence(
            MODEL,
            '<gene name="Lamassu__LmuC_Clade_I" presence="mandatory">',
            "LmuC is mandatory, with Clade II-VII and MC1-MC8 exchangeable "
            "profiles. There are no accessory components in this executable XML.",
        ),
        evidence(
            DATASET,
            "ACJU001.0722.00009.C001\tACJU001.0722.00009.C001_01299\tLamassu__LmuB_Short\n"
            "ACJU001.0722.00009.C001\tACJU001.0722.00009.C001_01300\tLamassu__LmuC_Clade_VI\n"
            "ACJU001.0722.00009.C001\tACJU001.0722.00009.C001_01301\tLamassu__LmuA_SMEK",
            "Dataset S1, S3_Lamassu_Detection!A165:C167, raw cells in column "
            "order. Columns E, F, I and M identify one Lamassu/Lamassu/Lamassu_SMEK "
            "call, ACJU001.0722.00009.C001_Lamassu_SMEK_36, with sys_wholeness "
            "1.0 and three mandatory hits. This is computational evidence of "
            "the complete architecture, not experimental antiviral activity.",
        ),
        evidence(
            DATASET,
            "ACJU001.0722.00009.C001\tGCF_021491935.1\tBacteria\tProteobacteria\t"
            "Acinetobacter junii\tNZ_CP090890",
            "Dataset S1, S2_Genomes!A1383:F1383, raw cells linking the "
            "SMEK-system replicon to assembly GCF_021491935.1 and its species. "
            "The historical phylum name is retained only inside this source quote.",
        ),
        evidence(
            DATASET,
            "Lamassu__LmuB_Long\nLamassu__LmuC_Clade_VII\nLamassu__LmuA_SMEK\nLamassu__LmuB_Long",
            "Dataset S1, S3_Lamassu_Detection!C6042:C6045, raw cells for "
            "HAAN001.0722.00001.C001_Lamassu_SMEK_499. Column F assigns these "
            "four rows to one call, including two distinct long-profile LmuB "
            "hits. Across the sheet, 125 unique SMEK system IDs comprise 124 "
            "calls with short LmuB and this one call with long LmuB; these sets "
            "do not overlap. Component-row counts are not system counts. "
            "The long-profile call is an annotation exception needing review, "
            "not a validated biological long-Lamassu SMEK subtype.",
        ),
        evidence(
            ASSEMBLY,
            '"tax_id":40215,"organism_name":"Acinetobacter junii",'
            '"infraspecific_names":{"strain":"WCO-9"}',
            "NCBI Datasets assembly report, verified 2026-10-03: resolves "
            "GCF_021491935.1 to taxon 40215 and strain WCO-9. This source "
            "verifies identity only; Dataset S1 supports system possession.",
        ),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:40215",
            "taxon_label": "Acinetobacter junii",
            "note": (
                "Computational genomic example: strain WCO-9, assembly "
                "GCF_021491935.1, study replicon ACJU001.0722.00009.C001. "
                "Dataset S1 S3_Lamassu_Detection rows 165-167 record a complete "
                "short-LmuB, LmuC and SMEK-LmuA call; S2_Genomes row 1383 "
                "links it to the assembly. NCBI resolves the strain and taxon. "
                "This does not establish experimentally measured antiviral "
                "activity in WCO-9 or species-wide possession."
            ),
            "reference": DATASET,
        }
    ],
    "discussions": [
        {
            "discussion_id": "lamassu-smek-function-and-annotation-scope",
            "prompt": "Resolve the long-profile exception and validate SMEK-system function.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The paper describes SMEK as short-Lamassu-specific, while "
                "Dataset S1 has 124 short-profile calls and one long-profile "
                "call with two distinct LmuB hits. The pinned model accepts "
                "both lengths. Reconcile that exceptional call with phylogeny "
                "and locus context before claiming a biological long-LmuB "
                "subtype or short-only distribution. The definition therefore "
                "captures architecture without a length restriction. The "
                "pinned legacy summary TSV and HMM inventory lack SMEK entries "
                "although the executable model and SMEK profile exist. "
                "This whole-system trait is not equivalent to DS-27 "
                "(traitmech:000451), whose existing definition denotes a "
                "single-gene transcriptional unit with the working label SMEK. "
                "No DS-27 assay phenotype or exact synonym is transferred. "
                "SMEK-specific Lamassu antiviral validation, substrates, "
                "activation order, domain-name expansion and accession-level "
                "protein mechanisms remain unresolved. Cap4 and Lipase "
                "experiments do not establish SMEK chemistry. No causal graph "
                "is asserted from these computational architecture calls alone."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-03",
        }
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator="codex",
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Added the literature-recognized Lamassu-SMEK architecture using "
            "DOI, pinned executable-model, Dataset S1 and NCBI identity evidence "
            "with exact snippets. Distinguished 125 system calls from 377 "
            "component rows and recorded the long-profile exception. Kept the "
            "WCO-9 example computational and rejected equivalence to DS-27. "
            "Ignored-and-hidden searches found no exact record or METPO term. "
            "Reserved METPO:1052300 in proposals/metpo_traitmech_v446."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def build_parent() -> dict:
    parent = yaml.safe_load(PARENT.read_text())
    assert parent["identifier"] == "traitmech:000232"
    assert parent["label"] == "Lamassu system"
    assert parent["mapping_status"] == "PROPOSED"
    assert parent["parent_traits"] == ["traitmech:000209"]
    discussion = next(
        d for d in parent["discussions"] if d["discussion_id"] == "lamassu-subtype-and-effector-gap"
    )
    assert (discussion["kind"], discussion["status"]) == ("KNOWLEDGE_GAP", "OPEN")
    old = discussion["rationale"].removesuffix(PARENT_ADDITION)
    if hashlib.sha256(old.encode()).hexdigest() != OLD_PARENT_HASH:
        raise SystemExit("Lamassu parent discussion changed; review before applying")
    if discussion["rationale"] == old:
        discussion["rationale"] += PARENT_ADDITION
        record_curation_event(
            parent,
            curator="codex",
            action="TRACK_NARROWER_RECORD",
            changes=(
                "Linked traitmech:000569 Lamassu-SMEK system; documented the "
                "long-profile dataset exception and distinction from the "
                "single-gene DS-27 SMEK working label. Retained function gaps."
            ),
            llm_assisted=True,
            timestamp=TIMESTAMP,
        )
    return parent


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
            "exact_synonyms",
            "xrefs",
            "subset",
            "priority",
            "observations",
            "traits_addressed",
            "related_synonyms",
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
            "A oboInOwl:hasRelatedSynonym SPLIT=|",
        ]
    )
    writer.writerow(
        [
            "METPO:1052300",
            record["label"],
            record["definition"],
            "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", HAUDIQUET, MODEL, DATASET]),
            "METPO:1018600",
            "",
            "",
            "metpo_traitmech_2026_10",
            "HIGH",
            "Three-component SMEK-bearing Lamassu architecture, not single-gene "
            "DS-27. No short-only restriction: the dataset has one long-profile "
            "exception requiring review. Genomic example only; no SMEK chemistry asserted.",
            IDENTIFIER,
            "|".join(s["synonym_text"] for s in record["synonyms"]),
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
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(parent, Path(tmp) / PARENT.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, PARENT)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
