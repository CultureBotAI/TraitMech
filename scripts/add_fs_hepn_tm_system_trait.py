#!/usr/bin/env python3
"""Add the FS-HEPN-TM system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "fs_hepn_tm_system.yaml"

FILLOL_SALOM = "DOI:10.1016/j.cell.2022.07.014"
FILLOL_SALOM_PMID = "PMID:35985290"
PICI_DEFENSE_SNIPPET = (
    "the phage-inducible chromosomal islands (PICIs), carry an "
    "impressive arsenal of defense mechanisms"
)
PICI_IMMUNITY_SNIPPET = (
    "These defense systems provide broad immunity, blocking not only "
    "phage reproduction, but also plasmid and non-cognate PICI transfer."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T22:22:47Z"
IDENTIFIER = "traitmech:000347"
PROPOSAL = "proposals/metpo_traitmech_v224"
SLUG = "fs_hepn_tm"

ARTICLE_REGISTRY_SNIPPET = (
    "FS_HEPN_TM | 10\\.1016/j\\.cell\\.2022\\.07\\.014 | "
    "Bacteriophages benefit from mobilizing pathogenicity islands "
    "encoding immune systems against competitors"
)
RULES_SNIPPET = "FS_HEPN_TM\tFS_HEPN_TM\t2\t2\tFS_HEPN_TM__HEPN, FS_HEPN_TM__TM"
HEPN_HMM_ROW = (
    "| FS_HEPN_TM__HEPN                                 | "
    "FS_HEPN_TM__HEPN                                 | "
    "FS_HEPN_TM             | PF05168.15              | 20     |"
)
TM_HMM_ROW = (
    "| FS_HEPN_TM__TM                                   | "
    "FS_HEPN_TM__TM                                   | "
    "FS_HEPN_TM             | Custom                  | 20     |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named FS_HEPN_TM "
            "system to the Fillol-Salom et al. PICI defense-system paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models FS_HEPN_TM as a two-profile "
            "system requiring the FS_HEPN_TM__HEPN and FS_HEPN_TM__TM profiles."
        ),
    }


def hepn_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HEPN_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records FS_HEPN_TM__HEPN under "
            "FS_HEPN_TM."
        ),
    }


def tm_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": TM_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records FS_HEPN_TM__TM under "
            "FS_HEPN_TM."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "FS-HEPN-TM system",
    "definition": (
        "A phage defense system in which an organism possesses an "
        "FS_HEPN_TM locus represented by DefenseFinder as a two-profile "
        "model requiring FS_HEPN_TM__HEPN and FS_HEPN_TM__TM."
    ),
    "definition_source": FILLOL_SALOM,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "FS_HEPN_TM",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "FS_HEPN_TM__HEPN",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "FS_HEPN_TM__TM",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": FILLOL_SALOM_PMID,
            "snippet": PICI_DEFENSE_SNIPPET,
            "notes": (
                "Fillol-Salom et al. support phage-inducible chromosomal "
                "islands as carriers of mobile-element defense mechanisms."
            ),
        },
        {
            "reference": FILLOL_SALOM_PMID,
            "snippet": PICI_IMMUNITY_SNIPPET,
            "notes": (
                "Fillol-Salom et al. support PICI-encoded defense systems "
                "as broad immunity determinants against phage reproduction "
                "and other mobile genetic element transfer."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hepn_hmm_evidence(),
        tm_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "fs_hepn_tm_locus_restricts_phage",
            "title": "FS-HEPN-TM loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of an "
                "FS_HEPN_TM locus to broad mobile-element defense without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures FS-HEPN-TM as a named DefenseFinder "
                "two-profile system in the Fillol-Salom PICI defense family "
                "while leaving its natural host breadth, helper-phage trigger, "
                "HEPN-family substrate, and transmembrane partner function "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "fs_hepn_tm_locus",
                    "label": "FS_HEPN_TM locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder FS_HEPN_TM phage-defense locus "
                        "represented by HEPN-family and transmembrane "
                        "profiles."
                    ),
                },
                {
                    "node_id": "pici_encoded_mobile_element_defense",
                    "label": "PICI-encoded mobile-element defense",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Defense by phage-inducible chromosomal island loci "
                        "against phage reproduction, plasmid transfer, or "
                        "non-cognate PICI transfer."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "FS-HEPN-TM system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded FS-HEPN-TM "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "fs_hepn_tm_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pici_encoded_mobile_element_defense",
                    "description": (
                        "DefenseFinder maps FS_HEPN_TM to the Fillol-Salom "
                        "et al. PICI-encoded immunity study and models it "
                        "as a two-profile system requiring HEPN-family and "
                        "transmembrane profiles."
                    ),
                    "evidence": [
                        {
                            "reference": FILLOL_SALOM_PMID,
                            "snippet": PICI_DEFENSE_SNIPPET,
                            "notes": (
                                "Fillol-Salom et al. support PICI loci as "
                                "carriers of phage and mobile-element "
                                "defense mechanisms."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        hepn_hmm_evidence(),
                        tm_hmm_evidence(),
                    ],
                },
                {
                    "subject": "pici_encoded_mobile_element_defense",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "FS_HEPN_TM-associated mobile-element defense "
                        "realizes the FS-HEPN-TM system trait."
                    ),
                    "evidence": [
                        {
                            "reference": FILLOL_SALOM_PMID,
                            "snippet": PICI_IMMUNITY_SNIPPET,
                            "notes": (
                                "Fillol-Salom et al. support PICI-encoded "
                                "defense systems as broad mobile-element "
                                "immunity determinants."
                            ),
                        },
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "FS-HEPN-TM system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [article_registry_evidence(), rules_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "fs-hepn-tm-mechanism-gap",
            "prompt": (
                "Resolve FS_HEPN_TM natural hosts, helper-phage triggers, "
                "HEPN-family substrates, and transmembrane partner activity "
                "before minting narrower FS_HEPN_TM mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Fillol-Salom et al. support phage-inducible chromosomal "
                "islands as carriers of defense systems that provide broad "
                "immunity, and DefenseFinder models FS_HEPN_TM as a "
                "two-profile HEPN/transmembrane system. Its exact natural "
                "host breadth, helper-phage trigger, substrate, and "
                "profile-to-activity mapping remain unresolved."
            ),
            "attaches_to": ["causal_graphs#fs_hepn_tm_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help=f"write {TARGET.relative_to(REPO_ROOT)}",
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted FS-HEPN-TM system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, "
            "history, or prior proposal record; the replacement placeholder "
            f"is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
