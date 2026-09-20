"""Add the AbiD system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abid_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

MCLANDSBOROUGH = "DOI:10.1128/aem.61.5.2023-2026.1995"
MCLANDSBOROUGH_PMID = "PMID:7646042"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T20:30:20Z"
PARENT_TIMESTAMP = "2026-09-20T20:30:21Z"
IDENTIFIER = "traitmech:000318"
PROPOSAL = "proposals/metpo_traitmech_v195"

HMM_ROW = (
    "| AbiD__AbiD                                       | "
    "AbiD__AbiD                                       | AbiD                   | "
    "Custom                  | 90     |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, and AbiR are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, and traitmech:000317, respectively. "
    "Lopatina et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, "
    "Wang et al., Bouchard et al., Haaber et al., Owen et al., Depardieu "
    "et al., Prevots et al., O'Connor et al., Su et al., and Twomey et al. "
    "still support Abi as a genomically encoded phage defense strategy that "
    "spans mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, staphylococcal-kinase-triggered "
    "cell death, lactococcal AbiH phage resistance, two-gene lactococcal AbiG "
    "RNA-synthesis interference, single-ORF lactococcal AbiI burst-size "
    "reduction, two-separated-locus lactococcal AbiR DNA-replication impediment, "
    "and other Abi families. Additional narrower TraitRecords need separate "
    "review to ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, AbiG, "
    "AbiI, AbiR, and AbiD are split out as traitmech:000226, "
    "traitmech:000225, traitmech:000227, traitmech:000228, "
    "traitmech:000229, traitmech:000230, traitmech:000300, "
    "traitmech:000301, traitmech:000303, traitmech:000304, "
    "traitmech:000306, traitmech:000316, traitmech:000317, and "
    "traitmech:000318, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., Depardieu et al., Prevots et al., "
    "O'Connor et al., Su et al., Twomey et al., and McLandsborough "
    "et al. still support Abi as a genomically encoded phage defense "
    "strategy that spans mechanistically diverse toxin-antitoxin, "
    "premature-lysis, RT-related polymerase, two-component, "
    "translation-inhibition, prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, lactococcal AbiH phage "
    "resistance, two-gene lactococcal AbiG RNA-synthesis interference, "
    "single-ORF lactococcal AbiI burst-size reduction, two-separated-locus "
    "lactococcal AbiR DNA-replication impediment, pBF61-derived lactococcal "
    "AbiD burst-size reduction, and other Abi families. Additional narrower "
    "TraitRecords need separate review to ground each subfamily's trigger, "
    "effector, growth-arrest or cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented AbiD as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000318 for "
    "the AbiD system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiD | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiD model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiD\tAbiD\t1\t1\tAbiD__AbiD",
        "notes": (
            "The DefenseFinder rules table models AbiD as a one-component "
            "system requiring the AbiD__AbiD profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiD__AbiD under the AbiD model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiD system",
    "definition": (
        "An abortive infection system in which an organism possesses an "
        "abiD-family locus represented by the DefenseFinder AbiD__AbiD "
        "profile and exemplified by the Lactococcus lactis subsp. "
        "lactis KR5 pBF61 determinant whose abiD open reading frame "
        "confers an abortive phage infection phenotype with reduced "
        "plating efficiency, plaque size, and c2 phage burst size."
    ),
    "definition_source": MCLANDSBOROUGH,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiD",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": MCLANDSBOROUGH_PMID,
            "snippet": (
                "A 6.3-kb fragment from pBF61 in Lactococcus lactis "
                "subsp. lactis KR5 was cloned and found to confer an "
                "abortive phage infection (Abi+) phenotype"
            ),
            "notes": (
                "McLandsborough et al. cloned the pBF61-derived fragment "
                "from Lactococcus lactis subsp. lactis KR5 and showed "
                "that it conferred an Abi phenotype."
            ),
        },
        {
            "reference": MCLANDSBOROUGH_PMID,
            "snippet": (
                "exhibiting a reduction in efficiency of plating and "
                "plaque size for small isometric- and prolate-headed "
                "bacteriophages sk1 and c2, respectively, and to produce "
                "a 10-fold decrease in c2 phage burst size"
            ),
            "notes": (
                "McLandsborough et al. measured reduced plating "
                "efficiency, plaque size, and c2 phage burst size from "
                "the pBF61 AbiD determinant."
            ),
        },
        {
            "reference": MCLANDSBOROUGH_PMID,
            "snippet": "Phage adsorption was not significantly reduced",
            "notes": (
                "McLandsborough et al. distinguished AbiD activity from a phage-adsorption block."
            ),
        },
        {
            "reference": MCLANDSBOROUGH_PMID,
            "snippet": ("An open reading frame of 1,098 bp was sequenced and designated abiD"),
            "notes": (
                "McLandsborough et al. named the abiD open reading frame "
                "within the pBF61 determinant."
            ),
        },
        {
            "reference": MCLANDSBOROUGH_PMID,
            "snippet": ("Tn5 mutagenesis confirmed that abiD was required for the Abi+ phenotype"),
            "notes": (
                "McLandsborough et al. verified that the abiD open "
                "reading frame is required for the abortive-infection "
                "phenotype."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "McLandsborough et al. cloned the pBF61 AbiD determinant "
                "from Lactococcus lactis subsp. lactis KR5 and showed "
                "that the abiD open reading frame is required for "
                "abortive-infection phage resistance."
            ),
            "reference": MCLANDSBOROUGH,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abid_locus_reduces_lactococcal_phage_burst",
            "title": "AbiD activity restricts lactococcal phages",
            "description": (
                "Conservative system-level sketch linking an abiD-family "
                "locus to AbiD antiphage activity, reduced lactococcal "
                "phage propagation, and abortive-infection system "
                "possession without asserting the unresolved molecular "
                "target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiD as a named DefenseFinder "
                "single-profile abortive-infection system whose pBF61 "
                "prototype restricts sk1 and c2 phages. It leaves the "
                "direct phage trigger, AbiD molecular function, cell-death "
                "or growth-arrest route, natural locus breadth, and phage "
                "escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abid_locus",
                    "label": "abiD locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An abiD-family abortive-infection locus represented "
                        "by the DefenseFinder AbiD__AbiD profile."
                    ),
                },
                {
                    "node_id": "abid_antiphage_activity",
                    "label": "AbiD antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection phage resistance mediated by the AbiD system."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of lactococcal phage propagation "
                        "in an AbiD-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abid_system_trait",
                    "label": "AbiD system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiD "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abid_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abid_antiphage_activity",
                    "description": (
                        "The abiD-family locus encodes an "
                        "abortive-infection phage-resistance determinant, "
                        "and DefenseFinder models AbiD as a one-profile "
                        "system."
                    ),
                    "evidence": [
                        {
                            "reference": MCLANDSBOROUGH_PMID,
                            "snippet": (
                                "Tn5 mutagenesis confirmed that abiD was "
                                "required for the Abi+ phenotype"
                            ),
                            "notes": (
                                "McLandsborough et al. show that the abiD "
                                "open reading frame is required for the Abi "
                                "phenotype."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "abid_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "AbiD activity restricts tested small isometric- "
                        "and prolate-headed lactococcal phages."
                    ),
                    "evidence": [
                        {
                            "reference": MCLANDSBOROUGH_PMID,
                            "snippet": (
                                "exhibiting a reduction in efficiency of "
                                "plating and plaque size for small "
                                "isometric- and prolate-headed bacteriophages "
                                "sk1 and c2, respectively, and to produce a "
                                "10-fold decrease in c2 phage burst size"
                            ),
                            "notes": (
                                "McLandsborough et al. connect the AbiD "
                                "determinant to reduced sk1 and c2 plating "
                                "or plaque size and reduced c2 burst size."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abid_system_trait",
                    "description": (
                        "Restriction of lactococcal phage propagation "
                        "realizes the AbiD abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": MCLANDSBOROUGH_PMID,
                            "snippet": (
                                "A 6.3-kb fragment from pBF61 in "
                                "Lactococcus lactis subsp. lactis KR5 was "
                                "cloned and found to confer an abortive "
                                "phage infection (Abi+) phenotype"
                            ),
                            "notes": (
                                "McLandsborough et al. classify the pBF61 "
                                "AbiD determinant phenotype as abortive "
                                "phage infection."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abid_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiD system possession is an abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MCLANDSBOROUGH_PMID,
                            "snippet": (
                                "A 6.3-kb fragment from pBF61 in "
                                "Lactococcus lactis subsp. lactis KR5 was "
                                "cloned and found to confer an abortive "
                                "phage infection (Abi+) phenotype"
                            ),
                            "notes": (
                                "McLandsborough et al. place AbiD in the "
                                "abortive-infection class of phage defense."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abid-trigger-and-effector-gap",
            "prompt": (
                "Resolve the AbiD phage trigger, molecular activity, and "
                "direct arrest target before minting narrower AbiD "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "McLandsborough et al. support AbiD as a named "
                "lactococcal abortive-infection determinant whose cloned "
                "pBF61 fragment reduces sk1 plating efficiency and c2 "
                "burst size, whose abiD open reading frame is required "
                "for the Abi phenotype, and whose activity does not "
                "primarily block phage adsorption. DefenseFinder "
                "represents AbiD with a one-profile rule, but this first "
                "system-level record leaves the phage trigger, AbiD "
                "molecular function, direct host or phage target, "
                "growth-arrest or cell-death route, and phage escape "
                "routes unresolved."
            ),
            "attaches_to": ["causal_graphs#abid_locus_reduces_lactococcal_phage_burst"],
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

    discussion = next(
        item
        for item in record.get("discussions") or []
        if item.get("discussion_id") == "abortive-infection-subfamily-split-gap"
    )
    if discussion["rationale"] == NEW_PARENT_RATIONALE:
        assert discussion["status"] == "OPEN"
        return record

    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    assert discussion["rationale"] == OLD_PARENT_RATIONALE
    discussion["rationale"] = NEW_PARENT_RATIONALE

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
            "Minted AbiD system as a DOI-backed GENOMICS TraitRecord under "
            "the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
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
    parser = argparse.ArgumentParser(description=__doc__)
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
            "AbiD system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
