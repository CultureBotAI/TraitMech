"""Add the short-form Lamassu-HNH architecture and its METPO proposal."""

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

SLUG = "lamassu_hnh_system"
TARGET = ROOT / "data/traits/genomics" / f"{SLUG}.yaml"
PARENT = ROOT / "data/traits/genomics/lamassu_system.yaml"
IDENTIFIER = "traitmech:000568"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v445"
TIMESTAMP = "2026-10-03T10:35:00Z"
HAUDIQUET = "DOI:10.1073/pnas.2519643122"
PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/"
)
MODEL = PREFIX + "definitions/DefenseFinder/Lamassu-Fam/Lamassu_HNH.xml"
DATASET = "https://pmc-oa-opendata.s3.amazonaws.com/PMC12663957.1/pnas.2519643122.sd01.xlsx"
ASSEMBLY = (
    "https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_009892245.1/dataset_report"
)
OLD_PARENT_HASH = "815c9d3ea44701a5f81dccba2110143afb7ab695159a61151dfc485cc1969e2d"
PARENT_ADDITION = (
    " Lamassu-HNH system (traitmech:000568) now captures the literature-supported "
    "short-LmuB architecture with HNH-domain LmuA and LmuC. The published "
    "dataset supplies complete computational genome calls, not HNH-specific "
    "functional validation. The pinned executable HNH model accepts either "
    "long or short LmuB, whereas all HNH calls in that dataset use short LmuB; "
    "its software key is therefore not an exact synonym for this biological "
    "scope. HNH-specific activity, substrates, and activation remain unresolved."
)


def evidence(reference: str, snippet: str, notes: str) -> dict[str, str]:
    return {"reference": reference, "snippet": snippet, "notes": notes}


RECORD = {
    "identifier": IDENTIFIER,
    "label": "Lamassu-HNH system",
    "definition": (
        "A Lamassu system in which an organism possesses a locus encoding an "
        "HNH-domain LmuA effector, a short-form SMC-like LmuB sensor, and LmuC."
    ),
    "definition_source": HAUDIQUET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000232"],
    "synonyms": [
        {"synonym_text": "Lamassu_HNH", "synonym_type": "RELATED_SYNONYM", "source": MODEL},
        {
            "synonym_text": "Lamassu/Lamassu/Lamassu_HNH",
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
            "effector types. Figure 1A depicts HNH-domain LmuA with short LmuB "
            "and LmuC. This establishes a recognized architecture, not "
            "HNH-specific biochemical or infection-assay validation.",
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
            '<gene name="Lamassu__LmuA_HNH" presence="mandatory"/>',
            "HNH-bearing LmuA is mandatory. Other named LmuA effector profiles "
            "are forbidden by separate blocks; an isolated HNH-profile hit "
            "does not establish possession of the complete system.",
        ),
        evidence(
            MODEL,
            '<gene name="Lamassu__LmuB_Long" presence="mandatory">\n'
            '<exchangeables>\n<gene name="Lamassu__LmuB_Short"/>\n'
            "</exchangeables>\n</gene>",
            "The detector accepts either long or short LmuB. Its software "
            "scope is broader than this record's literature-supported "
            "short-LmuB architecture, so the model key is only a related synonym.",
        ),
        evidence(
            MODEL,
            '<gene name="Lamassu__LmuC_Clade_I" presence="mandatory">',
            "LmuC is mandatory, with Clade II-VII and MC1-MC8 profiles in the "
            "exchangeables block. There are no accessory components in this XML.",
        ),
        evidence(
            DATASET,
            "ACHA001.0722.00006.C001\tACHA001.0722.00006.C001_03320\tLamassu__LmuB_Short\n"
            "ACHA001.0722.00006.C001\tACHA001.0722.00006.C001_03321\tLamassu__LmuC_MC7\n"
            "ACHA001.0722.00006.C001\tACHA001.0722.00006.C001_03322\tLamassu__LmuA_HNH",
            "Dataset S1, S3_Lamassu_Detection!A121:C123, raw cells in column "
            "order. Columns E, F, I and M identify one Lamassu/Lamassu/Lamassu_HNH "
            "call, ACHA001.0722.00006.C001_Lamassu_HNH_807, with sys_wholeness "
            "1.0 and three mandatory hits. The full sheet has 281 unique HNH "
            "system IDs, each with short LmuB. These are computational genome "
            "annotations, not experimental antiviral phenotypes.",
        ),
        evidence(
            DATASET,
            "ACHA001.0722.00006.C001\tGCF_009892245.1\tBacteria\tProteobacteria\t"
            "Acinetobacter haemolyticus\tNZ_CP031972",
            "Dataset S1, S2_Genomes!A1159:F1159, raw cells linking the HNH-bearing "
            "replicon to assembly GCF_009892245.1 and its species. The historical "
            "phylum label is quoted as source data, not adopted as a taxonomic "
            "assertion. This supports a genome-qualified possession example.",
        ),
        evidence(
            ASSEMBLY,
            '"tax_id":29430,"organism_name":"Acinetobacter haemolyticus",'
            '"infraspecific_names":{"strain":"AN59"}',
            "NCBI Datasets assembly report, verified 2026-10-03: resolves the "
            "study's assembly to species taxon 29430 and strain AN59. This "
            "source verifies identity only; the published dataset supports "
            "the computational system-possession annotation.",
        ),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:29430",
            "taxon_label": "Acinetobacter haemolyticus",
            "note": (
                "Computational genomic example: strain AN59, assembly "
                "GCF_009892245.1, study replicon ACHA001.0722.00006.C001, has "
                "a complete three-component HNH-system call in Dataset S1 "
                "(S3_Lamassu_Detection rows 121-123; S2_Genomes row 1159). "
                "NCBI Datasets resolves the assembly to this species and strain. "
                "This does not establish experimentally measured antiviral "
                "activity in AN59 or species-wide possession."
            ),
            "reference": DATASET,
        }
    ],
    "discussions": [
        {
            "discussion_id": "lamassu-hnh-function-and-model-scope",
            "prompt": "Validate HNH-system function and reconcile detector scope.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The paper identifies HNH as a short-Lamassu effector type, "
                "and all 281 HNH calls in Dataset S1 contain short LmuB. The "
                "pinned executable XML nevertheless permits long LmuB, so "
                "the detector name is not an exact biological equivalence. "
                "At the same commit, the legacy DefenseFinder_rules.tsv and "
                "Liste_hmm_system.md lack an HNH-system entry even though "
                "the executable XML and HNH profile exist. Summary-table "
                "absence is not model absence. HNH-specific experimental "
                "antiviral validation, exact substrates, activation order, "
                "and accession-level protein anchors remain unresolved. "
                "Cap4 and Lipase experiments do not establish HNH chemistry "
                "or its phage spectrum. No protein-resolved causal graph or "
                "functional equivalence to standalone HNH proteins is asserted."
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
            "Added the literature-supported short-Lamassu HNH architecture "
            "with DOI, executable-model, published dataset and NCBI identity "
            "evidence and exact snippets. Restricted the AN59 example to "
            "computational genomic possession. Ignored-and-hidden searches "
            "found no exact record or METPO term. Reserved METPO:1052200 in "
            "proposals/metpo_traitmech_v445; retained the detector-scope and "
            "HNH-specific functional-validation gaps."
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
                "Linked traitmech:000568 Lamassu-HNH system and distinguished "
                "its short-LmuB genomic architecture from the broader executable "
                "detector. Retained HNH-specific functional-validation gaps."
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
            "METPO:1052200",
            record["label"],
            record["definition"],
            "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", HAUDIQUET, MODEL, DATASET]),
            "METPO:1018600",
            "",
            "",
            "metpo_traitmech_2026_10",
            "HIGH",
            "Short-LmuB HNH-bearing Lamassu architecture; computational genomic "
            "example only. The XML also accepts long LmuB; model keys are related, "
            "not exact synonyms. No HNH-specific experimental activity is asserted.",
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
