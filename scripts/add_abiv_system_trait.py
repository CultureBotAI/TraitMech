#!/usr/bin/env python3
"""Add the AbiV system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abiv_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

HAABER = "DOI:10.1128/AEM.00780-08"

DEFENSE_FINDER_RAW = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    "afb0e5a8b466be53586b13266f5d38d98c3ac268"
)
LIST_SYSTEM_ARTICLE = f"{DEFENSE_FINDER_RAW}/List_system_article.md"
LISTE_HMM_SYSTEM = f"{DEFENSE_FINDER_RAW}/Liste_hmm_system.md"
DEFENSE_FINDER_RULES = f"{DEFENSE_FINDER_RAW}/DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T03:07:25Z"
PARENT_TIMESTAMP = "2026-09-20T03:07:26Z"

OLD_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, and AbiT are split out as "
    "traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, and traitmech:000230, "
    "respectively. Lopatina et al., Fineran et al., Dy et al., Durmaz "
    "and Klaenhammer, Wang et al., and Bouchard et al. still support Abi "
    "as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, and other Abi families. "
    "Additional narrower TraitRecords need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
NEW_DISCUSSION_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, and AbiV are split out as "
    "traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, and "
    "traitmech:000300, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "and Haaber et al. still support Abi as a genomically encoded phage "
    "defense strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "phage-DNA-maturation, and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape "
    "routes."
)
PARENT_CHANGES = (
    "Documented AbiV as split out in the open abortive-infection subfamily "
    "split-gap discussion after minting traitmech:000300 for the AbiV system; "
    "other abortive-infection families remain open."
)

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000300",
    "label": "AbiV system",
    "definition": (
        "An abortive infection system in which an organism possesses an abiV "
        "locus whose encoded AbiV protein can restrict 936-like or c2-like "
        "lactococcal phages by interfering with late phage DNA maturation."
    ),
    "definition_source": HAABER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "evidence": [
        {
            "reference": HAABER,
            "snippet": (
                "We report here a novel lactococcal Abi system, designated "
                "AbiV, which is chromosomally encoded and effective against "
                "virulent phages belonging to the 936 and c2 species"
            ),
            "notes": (
                "Haaber et al. name AbiV as a chromosomal lactococcal "
                "abortive-infection system that can defend against 936- and "
                "c2-group virulent phages."
            ),
        },
        {
            "reference": HAABER,
            "snippet": (
                "This gene was also found to confer phage resistance to "
                "L. lactis MG1363 when it was cloned into an expression vector"
            ),
            "notes": (
                "Haaber et al. show that expressing the AbiV open reading "
                "frame is sufficient to confer phage resistance in "
                "Lactococcus lactis MG1363."
            ),
        },
        {
            "reference": HAABER,
            "snippet": (
                "A subsequent frameshift mutation in the ORF completely "
                "eliminated the phage resistance phenotype, confirming that "
                "the ORF was necessary for phage resistance"
            ),
            "notes": (
                "Haaber et al. show that the AbiV open reading frame is "
                "necessary for the cloned resistance phenotype."
            ),
        },
        {
            "reference": HAABER,
            "snippet": (
                "the data show that the phage resistance mechanism encoded "
                "by orf1 is an abortive infection mechanism"
            ),
            "notes": (
                "Haaber et al. classify the orf1/abiV resistance determinant "
                "as an abortive-infection mechanism."
            ),
        },
        {
            "reference": HAABER,
            "snippet": (
                "AbiV prevented cleavage of the replicated phage DNA and "
                "thus that it acts at a later stage of the phage infection "
                "process"
            ),
            "notes": (
                "Haaber et al. localize AbiV activity after phage DNA "
                "replication and connect it to failed DNA cleavage."
            ),
        },
        {
            "reference": HAABER,
            "snippet": (
                "AbiV inhibits proliferation of small isometric phages "
                "belonging to the 936 species and of prolate phages "
                "belonging to the c2 species"
            ),
            "notes": (
                "Haaber et al. support the observed 936- and c2-species phage "
                "sensitivity of the AbiV system."
            ),
        },
        {
            "reference": LIST_SYSTEM_ARTICLE,
            "snippet": (
                "AbiV | 10\\.1128/AEM\\.00780-08 | AbiV, a novel antiphage "
                "abortive infection mechanism on the chromosome of "
                "Lactococcus lactis subsp\\. cremoris MG1363"
            ),
            "notes": (
                "The DefenseFinder article registry maps the named AbiV "
                "system to the Haaber et al. AbiV paper."
            ),
        },
        {
            "reference": LISTE_HMM_SYSTEM,
            "snippet": (
                "| AbiV__AbiV                                       | "
                "AbiV__AbiV                                       | "
                "AbiV                   | Custom                  | 20     |"
            ),
            "notes": (
                "The DefenseFinder HMM inventory records the custom AbiV "
                "profile in the AbiV model namespace."
            ),
        },
        {
            "reference": DEFENSE_FINDER_RULES,
            "snippet": "AbiV\tAbiV\t1\t1\tAbiV__AbiV",
            "notes": (
                "The DefenseFinder rules table models AbiV as a "
                "single-profile system."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "Haaber et al. discovered abiV on the Lactococcus lactis "
                "subsp. cremoris MG1363 chromosome, expressed it in "
                "Lactococcus lactis MG1363, and showed that its expression "
                "conferred abortive-infection phage resistance."
            ),
            "reference": HAABER,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "abiv_late_phage_dna_maturation_block",
            "title": "AbiV activity blocks late phage DNA maturation",
            "description": (
                "Evidence-backed process sketch linking an abiV locus to AbiV "
                "antiphage activity, failed late DNA maturation of replicated "
                "phage DNA, restricted phage propagation, and "
                "abortive-infection system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiV at the system level without asserting "
                "a direct phage trigger, the host substrate, the exact route "
                "to phage-DNA maturation arrest, a c2-specific mechanism, or "
                "why one tested 936 phage and the P335 phages were insensitive."
            ),
            "nodes": [
                {
                    "node_id": "abiv_locus",
                    "label": "abiV locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abortive-infection locus encoding the AbiV phage "
                        "resistance determinant."
                    ),
                },
                {
                    "node_id": "abiv_antiphage_activity",
                    "label": "AbiV antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection antiphage activity mediated by "
                        "the AbiV protein."
                    ),
                },
                {
                    "node_id": "stalled_phage_dna_maturation",
                    "label": "stalled phage DNA maturation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Late phage DNA maturation block in which replicated "
                        "concatemeric 936-like phage DNA is not cleaved into "
                        "mature resolved DNA."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of 936-like or c2-like phage "
                        "propagation in an AbiV-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abiv_system_trait",
                    "label": "AbiV system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000300",
                    "description": (
                        "Possession of a genome-encoded AbiV "
                        "abortive-infection system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abiv_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abiv_antiphage_activity",
                    "description": (
                        "The abiV locus encodes the protein required for the "
                        "cloned phage-resistance phenotype."
                    ),
                    "evidence": [
                        {
                            "reference": HAABER,
                            "snippet": (
                                "A subsequent frameshift mutation in the ORF "
                                "completely eliminated the phage resistance "
                                "phenotype"
                            ),
                            "notes": (
                                "Haaber et al. abolish the phenotype with a "
                                "frameshift in the AbiV open reading frame."
                            ),
                        },
                        {
                            "reference": LISTE_HMM_SYSTEM,
                            "snippet": (
                                "| AbiV__AbiV                                       "
                                "| AbiV__AbiV                                       "
                                "| AbiV                   | Custom                  "
                                "| 20     |"
                            ),
                            "notes": (
                                "The DefenseFinder HMM inventory records the "
                                "custom AbiV profile in the AbiV model "
                                "namespace."
                            ),
                        },
                        {
                            "reference": DEFENSE_FINDER_RULES,
                            "snippet": "AbiV\tAbiV\t1\t1\tAbiV__AbiV",
                            "notes": (
                                "The DefenseFinder rules table models AbiV as "
                                "a single-profile system requiring the AbiV "
                                "profile."
                            ),
                        },
                    ],
                },
                {
                    "subject": "abiv_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "stalled_phage_dna_maturation",
                    "description": (
                        "AbiV activity prevents cleavage of replicated "
                        "936-like phage DNA into mature resolved DNA."
                    ),
                    "evidence": [
                        {
                            "reference": HAABER,
                            "snippet": (
                                "The results described above showed that AbiV "
                                "prevented cleavage of the replicated phage DNA"
                            ),
                            "notes": (
                                "Haaber et al. connect AbiV to failed cleavage "
                                "of replicated phage DNA."
                            ),
                        }
                    ],
                },
                {
                    "subject": "stalled_phage_dna_maturation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Accumulation of nonmature concatemeric phage DNA "
                        "limits completion of AbiV-sensitive phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": HAABER,
                            "snippet": (
                                "indicated that phage DNA accumulated in its "
                                "concatemeric (nonmature) form in the "
                                "resistant L. lactis cells"
                            ),
                            "notes": (
                                "Haaber et al. observed uncleaved "
                                "concatemeric phage DNA in AbiV-containing "
                                "resistant cells."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abiv_system_trait",
                    "description": (
                        "Restriction of 936-like or c2-like phage propagation "
                        "realizes the AbiV abortive-infection defense trait."
                    ),
                    "evidence": [
                        {
                            "reference": HAABER,
                            "snippet": (
                                "This ORF provided resistance against virulent "
                                "lactococcal phages belonging to the 936 and "
                                "c2 species with an efficiency of plaquing of "
                                "10−4"
                            ),
                            "notes": (
                                "Haaber et al. support AbiV-mediated "
                                "resistance to multiple 936- and c2-group "
                                "lactococcal phages."
                            ),
                        },
                        {
                            "reference": LIST_SYSTEM_ARTICLE,
                            "snippet": (
                                "AbiV | 10\\.1128/AEM\\.00780-08 | AbiV, "
                                "a novel antiphage abortive infection "
                                "mechanism on the chromosome of Lactococcus "
                                "lactis subsp\\. cremoris MG1363"
                            ),
                            "notes": (
                                "DefenseFinder records AbiV as a named "
                                "antiphage abortive-infection system from the "
                                "Haaber et al. paper."
                            ),
                        },
                    ],
                },
                {
                    "subject": "abiv_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiV system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": HAABER,
                            "snippet": (
                                "the gene was designated abiV and the Abi "
                                "mechanism was designated AbiV"
                            ),
                            "notes": (
                                "Haaber et al. name the abiV-encoded phage "
                                "resistance determinant as an Abi mechanism."
                            ),
                        }
                    ],
                },
            ],
        },
    ],
    "discussions": [
        {
            "discussion_id": "abiv-mechanism-gap",
            "prompt": (
                "Resolve the AbiV phage trigger, host target, c2-specific "
                "output, and phage-escape routes before minting narrower "
                "AbiV mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Haaber et al. support AbiV as a single-gene Abi system that "
                "acts after phage DNA replication and prevents cleavage of "
                "replicated 936-like phage DNA, but the direct AbiV target, "
                "the trigger that connects infection to activity, the "
                "mechanism restricting c2-like phages, and AbiV-insensitive "
                "escape routes are unresolved."
            ),
            "attaches_to": ["causal_graphs#abiv_late_phage_dna_maturation_block"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
        }
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def update_abortive_parent(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == "traitmech:000214"
    assert record["label"] == "abortive infection system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    discussions = record.get("discussions") or []
    discussion = next(
        item
        for item in discussions
        if item.get("discussion_id") == "abortive-infection-subfamily-split-gap"
    )
    if discussion["rationale"] == NEW_DISCUSSION_RATIONALE:
        assert discussion["status"] == "OPEN"
        return record

    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    assert discussion["rationale"] == OLD_DISCUSSION_RATIONALE
    discussion["rationale"] = NEW_DISCUSSION_RATIONALE

    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=PARENT_CHANGES,
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted AbiV system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v177."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / ABORTIVE.name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_abortive_parent(load_trait(ABORTIVE))
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "AbiV system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
