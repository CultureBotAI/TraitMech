#!/usr/bin/env python3
"""Add the Hma system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hma_system.yaml"

PAYNE_PADLOC = "DOI:10.1093/nar/gkab883"
LIU = "DOI:10.1111/1751-7915.14524"
PADLOC_WEBSERVER = "DOI:10.1093/nar/gkac400"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-02T03:38:00Z"
CANONICAL_TIMESTAMP = "2026-10-02T03:38:01Z"
IDENTIFIER = "traitmech:000533"
PHAGE_DEFENSE_PARENT_ID = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v410"

ARTICLE_ROW = (
    "| Hma | 10\\.1093/nar/gkac400 | PADLOC: a web server for the "
    "identification of antiviral defence systems in microbial genomes | "
)

HMA_HMM_ROWS = [
    (
        "| Hma__HmaA                                        |"
        "                                                  | Hma                    |"
        " Custom                  | 400    |"
    ),
    (
        "| Hma__HmaB                                        |"
        "                                                  | Hma                    |"
        " Custom                  | 20     |"
    ),
    (
        "| Hma__HmaC                                        |"
        "                                                  | Hma                    |"
        " Custom                  | 20     |"
    ),
]


def payne_hma_discovery_evidence() -> dict[str, str]:
    return {
        "reference": PAYNE_PADLOC,
        "snippet": (
            "We designated this as a new candidate defence system named Hma, "
            "as it encodes three proteins with predicted helicase (HmaA), "
            "m5c methyltransferase (HmaB) and ATPase (HmaC) domains."
        ),
        "notes": (
            "Payne et al. define Hma as a predicted three-gene antiviral "
            "defense system with HmaA, HmaB, and HmaC components."
        ),
    }


def payne_distribution_evidence() -> dict[str, str]:
    return {
        "reference": PAYNE_PADLOC,
        "snippet": (
            "The putative Hma system was very widespread, present in 26 "
            "phyla, surpassed only by CBASS type I, Gabija and Septu type I."
        ),
        "notes": (
            "Payne et al. report that the predicted Hma system occurs across "
            "many bacterial and archaeal phyla."
        ),
    }


def liu_hma_evidence() -> dict[str, str]:
    return {
        "reference": LIU,
        "snippet": "we characterized a new defence system, Hma",
        "notes": (
            "Liu et al. experimentally studied Hma in coral-associated "
            "Halomonas meridiana."
        ),
    }


def liu_nickase_evidence() -> dict[str, str]:
    return {
        "reference": LIU,
        "snippet": (
            "Mutation analysis revealed the nickase activity of the nuclease "
            "domain (belonging to PDD/EXK superfamily) of HmaA is essential "
            "in phage defence."
        ),
        "notes": (
            "Liu et al. connect HmaA nuclease activity to anti-phage defense "
            "against Escherichia phage T4."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the Hma source "
            "key to the PADLOC web-server paper."
        ),
    }


def hma_hmm_evidence(row: str, profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": row,
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} under "
            "the Hma model namespace."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact Hma system row."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Hma system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "genome-encoded Hma locus with predicted HmaA helicase, HmaB m5c "
        "methyltransferase, and HmaC ATPase components."
    ),
    "definition_source": PAYNE_PADLOC,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Hma",
            "synonym_type": "EXACT_SYNONYM",
            "source": PAYNE_PADLOC,
        },
        {
            "synonym_text": "Hma__HmaA",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Hma__HmaB",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Hma__HmaC",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        payne_hma_discovery_evidence(),
        payne_distribution_evidence(),
        liu_hma_evidence(),
        liu_nickase_evidence(),
        article_registry_evidence(),
        hma_hmm_evidence(HMA_HMM_ROWS[0], "Hma__HmaA"),
        hma_hmm_evidence(HMA_HMM_ROWS[1], "Hma__HmaB"),
        hma_hmm_evidence(HMA_HMM_ROWS[2], "Hma__HmaC"),
    ],
    "causal_graphs": [
        {
            "graph_id": "hma_locus_phage_defense",
            "title": "Hma loci support helicase-associated phage defense",
            "description": (
                "Conservative system-level sketch linking a three-gene Hma "
                "locus to HmaA-dependent phage defense and Hma system "
                "possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Hma at locus and HmaA antiviral-output "
                "level without asserting HmaB or HmaC regulation, HmaB/HmaC "
                "effector activity, complete HmaABC phage breadth, natural "
                "host activity, accessory systems inserted in the hma "
                "region, or rule-level DefenseFinder detection criteria."
            ),
            "nodes": [
                {
                    "node_id": "hma_locus",
                    "label": "Hma locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A candidate antiviral Hma locus encoding HmaA, "
                        "HmaB, and HmaC components."
                    ),
                },
                {
                    "node_id": "hmaA_phage_defense",
                    "label": "HmaA phage defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "HmaA helicase/nickase-associated inhibition of "
                        "bacteriophage infection."
                    ),
                },
                {
                    "node_id": "hma_system_trait",
                    "label": "Hma system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Hma phage-defense "
                        "system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PHAGE_DEFENSE_PARENT_ID,
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "hma_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "hmaA_phage_defense",
                    "description": (
                        "Hma loci encode HmaA, and HmaA nickase activity is "
                        "required for the characterized anti-phage activity."
                    ),
                    "evidence": [
                        payne_hma_discovery_evidence(),
                        liu_nickase_evidence(),
                        hma_hmm_evidence(HMA_HMM_ROWS[0], "Hma__HmaA"),
                    ],
                },
                {
                    "subject": "hmaA_phage_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hma_system_trait",
                    "description": (
                        "HmaA-dependent anti-phage activity realizes the "
                        "first-pass organism-level Hma system trait."
                    ),
                    "evidence": [
                        liu_hma_evidence(),
                        liu_nickase_evidence(),
                    ],
                },
                {
                    "subject": "hma_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Hma system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        payne_hma_discovery_evidence(),
                        payne_distribution_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "hma-defensefinder-rule-and-component-gap",
            "prompt": (
                "Resolve HmaB/HmaC contributions, complete HmaABC system "
                "requirements, hma-region accessory systems, sensitive-phage "
                "breadth, native host breadth, and DefenseFinder rule-level "
                "criteria before minting Hma mechanism or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Payne et al. predicted Hma as a three-gene candidate "
                "defense system, Liu et al. showed that the HmaA nuclease "
                "domain is essential for T4 phage defense, and the pinned "
                "DefenseFinder HMM inventory records HmaA, HmaB, and HmaC "
                "profiles. However, Liu et al. state that HmaB/HmaC "
                "regulation of HmaA was not known, and the pinned "
                "DefenseFinder rules table lacks an Hma row. This "
                "first-pass record therefore does not resolve exact HmaB "
                "or HmaC activities, complete-system genetic requirements, "
                "accessory defense systems inserted near hma, full "
                "sensitive-phage breadth, endogenous native-host activity, "
                "or reusable rule-level detection criteria."
            ),
            "evidence": [
                payne_hma_discovery_evidence(),
                liu_hma_evidence(),
                liu_nickase_evidence(),
                hma_hmm_evidence(HMA_HMM_ROWS[0], "Hma__HmaA"),
                hma_hmm_evidence(HMA_HMM_ROWS[1], "Hma__HmaB"),
                hma_hmm_evidence(HMA_HMM_ROWS[2], "Hma__HmaC"),
                rules_absence_evidence(),
            ],
            "attaches_to": ["causal_graphs#hma_locus_phage_defense"],
            "posed_by": CURATOR,
            "posed_date": "2026-10-02",
        }
    ],
}


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Hma system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under the phage defense system parent "
            "after an ignored-and-hidden duplicate review found no exact "
            "live TraitMech, METPO, history, or prior proposal record; "
            f"the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed Hma system during initial curation and left "
            "canonical_examples empty because the sources support the "
            "three-gene Hma system namespace, Hma HMM profiles, and "
            "HmaA-dependent activity but not an accession-backed native "
            "microbial taxon exemplar with experimentally verified "
            "endogenous HmaABC activity. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    validate_outputs(record)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
    else:
        print(
            "Hma system trait validates; rerun with "
            f"--apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
