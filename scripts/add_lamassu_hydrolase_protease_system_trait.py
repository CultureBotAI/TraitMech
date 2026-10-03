"""Add the paired Lamassu Hydrolase-Protease system and its METPO proposal."""

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

SLUG = "lamassu_hydrolase_protease_system"
TARGET = ROOT / "data/traits/genomics" / f"{SLUG}.yaml"
PARENT = ROOT / "data/traits/genomics/lamassu_system.yaml"
IDENTIFIER = "traitmech:000567"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v444"
TIMESTAMP = "2026-10-03T09:29:00Z"
MILLMAN = "DOI:10.1016/j.chom.2022.09.017"
HAUDIQUET = "DOI:10.1073/pnas.2519643122"
PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268/"
)
MODEL = PREFIX + "definitions/DefenseFinder/Lamassu-Fam/Lamassu_Hydrolase-Protease.xml"
RULES = PREFIX + "DefenseFinder_rules.tsv"
OLD_PARENT_HASH = "84cef03b90575be1afbf4cbeabe44e11e96475abe7eaf817459beac1c279a377"
PARENT_ADDITION = (
    " Lamassu Hydrolase-Protease system (traitmech:000567) now captures the "
    "literature-supported paired architecture with LmuB and LmuC. Its pinned "
    "executable XML requires four components, whereas the summary TSV requires "
    "three matches and calls LmuC accessory. The existing table-defined "
    "Lamassu-Hydrolase and Lamassu-Protease siblings each forbid the other's "
    "effector profile and are not exact matches to this paired architecture. "
    "Reconciling the legacy table-based sibling definitions with executable "
    "models remains open; do not interpret the summary's profile labels as "
    "current executable model requirements."
)


def evidence(reference: str, snippet: str, notes: str) -> dict[str, str]:
    return {"reference": reference, "snippet": snippet, "notes": notes}


RECORD = {
    "identifier": IDENTIFIER,
    "label": "Lamassu Hydrolase-Protease system",
    "definition": (
        "A Lamassu system in which an organism possesses a defense locus "
        "encoding a protease-domain LmuA effector together with a hydrolase-like "
        "protein, an SMC-like LmuB sensor, and LmuC."
    ),
    "definition_source": HAUDIQUET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000232"],
    "synonyms": [
        {
            "synonym_text": "Lamassu-Hydrolase_Protease",
            "synonym_type": "RELATED_SYNONYM",
            "source": RULES,
        },
        {
            "synonym_text": "Lamassu_Hydrolase-Protease",
            "synonym_type": "RELATED_SYNONYM",
            "source": MODEL,
        },
    ],
    "evidence": [
        evidence(
            HAUDIQUET,
            "Protease (accompanied by a hydrolase-like protein)",
            "Results, effector-diversity paragraph: the protease branch is "
            "paired with a hydrolase-like protein in both long and short "
            "Lamassu. Figure 1A shows the paired architecture with LmuB and "
            "LmuC. These annotations do not establish exact effector substrates.",
        ),
        evidence(
            HAUDIQUET,
            "one system from Bacillus cereus B4077, encoding Hydrolase-Protease effectors",
            "Results, LmuB phylogeny paragraph: identifies B4077 as the source "
            "of a previously validated long-Lamassu system, citing Millman "
            "et al. (2022). This supports a strain-qualified possession example, "
            "not species-wide prevalence or a native-host infection assay.",
        ),
        evidence(
            MILLMAN,
            "Mutation in the effector domains of these systems also abolished "
            "defense, as well as the deletion of lmuC",
            "Figure 2C and its Results paragraph report loss of defense after "
            "effector mutations or lmuC deletion in tested Lamassu systems, "
            "including the hydrolase/protease construct. The functional tests "
            "used heterologous hosts. This does not establish a substrate or "
            "the biochemical order of activation for the paired proteins.",
        ),
        evidence(
            MODEL,
            '<model inter_gene_max_space="1" min_mandatory_genes_required="4" '
            'min_genes_required="4" vers="2.0">',
            "The executable model requires four mandatory components, "
            "with at most one intervening gene between components.",
        ),
        evidence(
            MODEL,
            '<gene name="Lamassu__LmuA_Protease" presence="mandatory">\n'
            '<exchangeables>\n<gene name="Lamassu__LmuA_Protease_II"/>\n'
            "</exchangeables>\n</gene>\n\n"
            '<gene name="Lamassu__LmuA_Hydrolase" presence="mandatory"/>',
            "The model requires both protease and hydrolase components; "
            "Protease_II can substitute for the primary protease profile. "
            "Separate mandatory blocks also require LmuB_Long (exchangeable "
            "with LmuB_Short) and LmuC_Clade_I (with listed alternatives).",
        ),
        evidence(
            MODEL,
            '<gene name="Lamassu__LmuC_Clade_I" presence="mandatory">',
            "LmuC is mandatory in this executable model, with alternative "
            "LmuC profiles listed in its exchangeables block.",
        ),
        evidence(
            RULES,
            "Lamassu-Fam\tLamassu-Hydrolase_Protease\t3\t3",
            "The summary TSV places the paired subtype within Lamassu-Fam "
            "but gives three mandatory matches and three genes. Its mandatory "
            "column lists the legacy Hydrolase, Protease and Cap4_nuclease_II "
            "SMC profiles, and its accessory column lists the Lipase LmuC "
            "profile. This summary disagrees with the executable XML at the "
            "same commit and is retained only as provenance for the older label.",
        ),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1396",
            "taxon_label": "Bacillus cereus",
            "note": (
                "Strain B4077 is the source of the experimentally validated "
                "long-Lamassu Hydrolase-Protease system identified by "
                "Haudiquet et al. with reference to Millman et al. (2022). "
                "The species identifier anchors this strain-qualified example; "
                "it does not imply that all B. cereus strains possess it."
            ),
            "reference": HAUDIQUET,
        }
    ],
    "discussions": [
        {
            "discussion_id": "lamassu-hydrolase-protease-model-and-mechanism",
            "prompt": "Reconcile model-summary drift and resolve paired effector chemistry.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The pinned XML uses four mandatory components and newer "
                "Lamassu__ profile names, but its companion TSV uses three "
                "mandatory legacy profiles and accessory LmuC. The inventory's "
                "Hydrolase_protease LmuB and hydrolase_protease LmuC rows also "
                "differ from both representations. Model-summary reconciliation "
                "is required before using that TSV for genotype calls. The "
                "definition follows the biological paired architecture and "
                "executable model, not the table's thresholds. Exact substrates, "
                "activation order, native-host activity, and accession-level "
                "protein examples remain unresolved. No causal mechanism graph "
                "is asserted without those molecular anchors. The single-effector "
                "table-defined siblings are not asserted to be parents or "
                "equivalents of this paired system."
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
            "Added the literature-supported paired Lamassu architecture with "
            "DOI and pinned executable-model evidence, exact snippets, and a "
            "B4077 canonical example. Ignored-and-hidden searches found only "
            "pending parent mentions, not an exact existing record or METPO "
            "term. Reserved METPO:1052100 in proposals/metpo_traitmech_v444. "
            "Recorded summary-table drift rather than adopting its constraints."
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
                "Linked traitmech:000567 Lamassu Hydrolase-Protease system "
                "and documented disagreement between executable models and "
                "legacy tables; retained remaining subtype and mechanism gaps."
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
            "METPO:1052100",
            record["label"],
            record["definition"],
            "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", HAUDIQUET, MILLMAN, MODEL]),
            "METPO:1018600",
            "",
            "",
            "metpo_traitmech_2026_10",
            "HIGH",
            (
                "Paired hydrolase/protease Lamassu architecture; XML requires LmuC, "
                "whereas the legacy TSV calls it accessory. No exact enzyme, "
                "single-effector sibling, or genotype-call equivalence is proposed."
            ),
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
