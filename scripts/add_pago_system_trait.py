#!/usr/bin/env python3
"""Add the prokaryotic Argonaute defense system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pago_system.yaml"
SPARTA = REPO_ROOT / "data" / "traits" / "genomics" / "sparta_system.yaml"
DDMDE = REPO_ROOT / "data" / "traits" / "genomics" / "ddmde_system.yaml"

MAKAROVA = "DOI:10.1186/1745-6150-4-29"
KOOPAL = "DOI:10.1016/j.cell.2022.03.012"
BRAVO = "DOI:10.1038/s41586-024-07515-9"
JASKOLSKA = "DOI:10.1038/s41586-022-04546-y"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-27T22:11:00Z"
IDENTIFIER = "traitmech:000419"
PROPOSAL = "proposals/metpo_traitmech_v296"

ARTICLE_ROW = (
    "| pAgo | 10\\.1186/1745-6150-4-29 | Prokaryotic homologs of "
    "Argonaute proteins are predicted to function as key components of a "
    "novel system of defense against mobile genetic elements |"
)
RULE_ROW = (
    "pAgo\tpAgo\t1\t3\tpAgo__pAgo_LongA, pAgo__pAgo_LongB, "
    "pAgo__pAgo_S1A, pAgo__pAgo_S2B, pAgo__pAgo_SPARTA\t"
    "pAgo__EabAgaM, pAgo__EcAgaN, pAgo__GbbAgaS, "
    "pAgo__SIR2APAZ, pAgo__TIRAPAZ, pAgo__XAPAZ\t\t"
)
PAGO_SPARTA_ROW = (
    "| pAgo__pAgo_SPARTA                                | "
    "pAgo__pAgo_SPARTA                                | pAgo"
    "                   | Custom                  | 20     |"
)
PAGO_TIRAPAZ_ROW = (
    "| pAgo__TIRAPAZ                                    | "
    "pAgo__TIRAPAZ                                    | pAgo"
    "                   | Custom                  | 20     |"
)
SPARTA_COMPLEX_SNIPPET = (
    "short prokaryotic Argonaute and the associated TIR-APAZ (SPARTA) "
    "proteins form heterodimeric complexes"
)
DDMDE_PAGO_SNIPPET = "DdmE is a catalytically inactive, DNA-guided, DNA-targeting pAgo"
DDMDE_SYSTEM_SNIPPET = "These systems, termed DdmABC and DdmDE"
MAKAROVA_PAGO_SNIPPET = (
    "The hypothesis that pAgos are key components of a novel prokaryotic "
    "immune system that employs guide RNA or DNA molecules to degrade "
    "nucleic acids of invading mobile elements"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the pAgo model "
            "namespace to the Makarova et al. prokaryotic Argonaute mobile "
            "genetic element defense paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models pAgo as a system "
            "namespace with long pAgo, SPARTA, and optional APAZ-associated "
            "profile groups."
        ),
    }


def hmm_inventory_evidence(profile: str, snippet: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": snippet,
        "notes": (
            f"The pinned DefenseFinder HMM inventory records {profile} under "
            "the pAgo model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "prokaryotic Argonaute defense system",
    "definition": (
        "A genomics trait describing possession of a prokaryotic "
        "Argonaute-centered defense locus that uses a pAgo protein, alone "
        "or with cognate accessory proteins, to defend against plasmids, "
        "bacteriophages, or other mobile genetic elements."
    ),
    "definition_source": MAKAROVA,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000188"],
    "synonyms": [
        {
            "synonym_text": "pAgo",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": MAKAROVA,
            "snippet": MAKAROVA_PAGO_SNIPPET,
            "notes": (
                "Makarova et al. link prokaryotic Argonaute homologs to a "
                "predicted defense system against mobile genetic elements; "
                "later SPARTA and DdmDE experiments support two branches of "
                "this family."
            ),
        },
        {
            "reference": KOOPAL,
            "snippet": SPARTA_COMPLEX_SNIPPET,
            "notes": (
                "Koopal et al. support SPARTA as one experimentally "
                "resolved short pAgo and TIR-APAZ defense system."
            ),
        },
        {
            "reference": JASKOLSKA,
            "snippet": DDMDE_SYSTEM_SNIPPET,
            "notes": (
                "Jaskolska et al. support DdmDE as another prokaryotic "
                "Argonaute defense system in Vibrio cholerae."
            ),
        },
        {
            "reference": BRAVO,
            "snippet": DDMDE_PAGO_SNIPPET,
            "notes": (
                "Bravo et al. directly identify DdmE as the DNA-targeting "
                "prokaryotic Argonaute component of DdmDE."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence("pAgo__pAgo_SPARTA", PAGO_SPARTA_ROW),
        hmm_inventory_evidence("pAgo__TIRAPAZ", PAGO_TIRAPAZ_ROW),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:666",
            "taxon_label": "Vibrio cholerae",
            "note": (
                "V. cholerae seventh pandemic strains carry the "
                "prokaryotic-Argonaute DdmDE plasmid defense system."
            ),
            "reference": JASKOLSKA,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "pago_system_family_hierarchy",
            "title": (
                "Prokaryotic Argonaute systems include SPARTA and DdmDE "
                "defense loci"
            ),
            "description": (
                "Nonmechanistic family sketch linking the pAgo possession "
                "trait to experimentally curated SPARTA and DdmDE child "
                "systems."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph is deliberately limited to family hierarchy "
                "because long pAgo, SPARTA, DdmDE, SIR2-APAZ, TIR-APAZ, "
                "and other APAZ-associated pAgo systems can differ in "
                "effector chemistry, guide origin, accessory proteins, "
                "and plasmid or phage target breadth."
            ),
            "nodes": [
                {
                    "node_id": "sparta_system",
                    "label": "SPARTA system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000240",
                    "description": (
                        "Possession of a short prokaryotic Argonaute "
                        "TIR-APAZ defense system."
                    ),
                },
                {
                    "node_id": "ddmde_system",
                    "label": "DdmDE system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000275",
                    "description": (
                        "Possession of a DNA-guided prokaryotic "
                        "Argonaute DdmDE defense system."
                    ),
                },
                {
                    "node_id": "pago_system_trait",
                    "label": "prokaryotic Argonaute defense system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded prokaryotic "
                        "Argonaute-centered defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "sparta_system",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "pago_system_trait",
                    "description": (
                        "SPARTA is a short-pAgo TIR-APAZ system within the "
                        "broader prokaryotic Argonaute defense family."
                    ),
                    "evidence": [
                        {
                            "reference": KOOPAL,
                            "snippet": SPARTA_COMPLEX_SNIPPET,
                            "notes": (
                                "Koopal et al. define SPARTA around a "
                                "short pAgo and TIR-APAZ protein pair."
                            ),
                        },
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "ddmde_system",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "pago_system_trait",
                    "description": (
                        "DdmDE is an anti-plasmid defense system with a "
                        "DNA-guided pAgo component."
                    ),
                    "evidence": [
                        {
                            "reference": BRAVO,
                            "snippet": DDMDE_PAGO_SNIPPET,
                            "notes": (
                                "Bravo et al. identify DdmE as the pAgo "
                                "component of DdmDE."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "pago-subfamily-boundary-gap",
            "prompt": (
                "Resolve pAgo subfamily boundaries, accessory-protein "
                "requirements, and substrate breadth before minting "
                "narrower long-pAgo or APAZ-associated defense children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "SPARTA and DdmDE support prokaryotic Argonaute defense "
                "systems as a reusable genomics family, and DefenseFinder "
                "models a pAgo namespace with long pAgo, SPARTA, and "
                "optional APAZ-associated profiles. This parent does not "
                "yet resolve whether every DefenseFinder pAgo submodel "
                "has the same plasmid or phage substrate range, whether "
                "standalone APAZ-associated profiles are exact children, "
                "or which native-host examples support each subfamily."
            ),
            "evidence": [
                {
                    "reference": KOOPAL,
                    "snippet": SPARTA_COMPLEX_SNIPPET,
                    "notes": (
                        "Koopal et al. support one short-pAgo branch as "
                        "a paired SPARTA system."
                    ),
                },
                {
                    "reference": BRAVO,
                    "snippet": DDMDE_PAGO_SNIPPET,
                    "notes": (
                        "Bravo et al. support one DdmDE branch with DdmE "
                        "as a DNA-guided pAgo."
                    ),
                },
                rules_evidence(),
            ],
            "attaches_to": ["causal_graphs#pago_system_family_hierarchy"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-27",
        }
    ],
}


def load_record(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text())


def reparent_child(
    path: Path,
    *,
    expected_identifier: str,
    expected_label: str,
    expected_parents: list[str],
    changes: str,
) -> None:
    record = load_record(path)
    if record["identifier"] != expected_identifier:
        raise SystemExit(f"{path}: unexpected identifier {record['identifier']!r}")
    if record["label"] != expected_label:
        raise SystemExit(f"{path}: unexpected label {record['label']!r}")
    if record.get("mapping_status") != "PROPOSED":
        raise SystemExit(f"{path}: unexpected mapping_status")
    if record.get("parent_traits") != expected_parents:
        raise SystemExit(f"{path}: unexpected parent_traits {record.get('parent_traits')!r}")

    record["parent_traits"] = [IDENTIFIER]
    record_curation_event(
        record,
        curator=CURATOR,
        action="REPAIRED_PARENT_TRAIT",
        changes=changes,
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    write_validated_trait(record, path)
    print(f"updated {path.relative_to(REPO_ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}"
    )
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted prokaryotic Argonaute defense system as a "
            "DOI-backed GENOMICS TraitRecord under the quality root after "
            "an ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; scoped "
            "the graph to SPARTA and DdmDE family hierarchy and reserved "
            f"the replacement placeholder in {PROPOSAL}."
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
        reparent_child(
            SPARTA,
            expected_identifier="traitmech:000240",
            expected_label="SPARTA system",
            expected_parents=["METPO:1000188"],
            changes=(
                "Reparented SPARTA system from the generic quality root "
                "to the newly minted prokaryotic Argonaute defense system "
                "parent without changing SPARTA-specific evidence or "
                "mechanism claims."
            ),
        )
        reparent_child(
            DDMDE,
            expected_identifier="traitmech:000275",
            expected_label="DdmDE system",
            expected_parents=["METPO:1000188"],
            changes=(
                "Reparented DdmDE system from the generic quality root to "
                "the newly minted prokaryotic Argonaute defense system "
                "parent without changing DdmDE-specific evidence or "
                "mechanism claims."
            ),
        )
    else:
        print(f"would write {rel} and reparent SPARTA/DdmDE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
