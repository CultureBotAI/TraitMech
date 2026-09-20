#!/usr/bin/env python3
"""Add the Detocs system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "detocs_system.yaml"

ROUSSET = "DOI:10.1016/j.cell.2023.07.020"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T06:11:22Z"
IDENTIFIER = "traitmech:000302"
PROPOSAL = "proposals/metpo_traitmech_v179"

DEFENSEFINDER_HMM_ROWS = {
    "dtcA": (
        "| Detocs__dtcA                                     | "
        "Detocs__dtcA                                     | Detocs                 | "
        "Custom                  | 30     |"
    ),
    "dtcB": (
        "| Detocs__dtcB                                     | "
        "Detocs__dtcB                                     | Detocs                 | "
        "Custom                  | 40     |"
    ),
    "dtcC": (
        "| Detocs__dtcC                                     | "
        "Detocs__dtcC                                     | Detocs                 | "
        "Custom                  | 40     |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Detocs | 10\\.1101/2023\\.01\\.24\\.525353 | A conserved "
            "family of immune effectors cleaves cellular ATP upon viral "
            "infection"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Detocs "
            "system to the Rousset et al. ATP-cleavage preprint."
        ),
    }


def hmm_inventory_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": DEFENSEFINDER_HMM_ROWS[profile],
        "notes": (
            f"The DefenseFinder HMM inventory records {profile} under "
            "the Detocs model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": (
            "Detocs\tDetocs\t2\t2\tDetocs__dtcA, "
            "Detocs__dtcB\tDetocs__dtcC"
        ),
        "notes": (
            "The DefenseFinder rules table models the core Detocs system "
            "with required dtcA and dtcB profiles and an optional dtcC "
            "profile."
        ),
    }


def atp_degradation_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": (
            "upon phage infection, degrade cellular adenosine "
            "triphosphate (ATP) and deoxyadenosine triphosphate (dATP)"
        ),
        "notes": (
            "Rousset et al. support ATP and dATP degradation as a "
            "phage-triggered bacterial immune output."
        ),
    }


def halted_propagation_evidence() -> dict[str, str]:
    return {
        "reference": ROUSSET,
        "snippet": (
            "ATP and dATP degradation during infection halts phage "
            "propagation"
        ),
        "notes": (
            "Rousset et al. connect ATP and dATP degradation to "
            "inhibition of phage propagation."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Detocs system",
    "definition": (
        "A phage defense system in which an organism possesses a Detocs "
        "locus represented in DefenseFinder by DtcA and DtcB profiles "
        "plus optional DtcC-family profiles, with an ATP nucleosidase "
        "output that can degrade ATP and dATP upon phage infection and "
        "halt phage propagation."
    ),
    "definition_source": ROUSSET,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Detocs",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": ROUSSET,
            "snippet": (
                "By analyzing homologs of the immune ATP nucleosidase domain, "
                "we discover and characterize Detocs, a family of bacterial "
                "defense systems with a two-component "
                "phosphotransfer-signaling architecture"
            ),
            "notes": (
                "Rousset et al. discover Detocs from immune ATP nucleosidase "
                "domain homologs and name it as a bacterial defense-system "
                "family with two-component phosphotransfer-signaling "
                "architecture."
            ),
        },
        atp_degradation_evidence(),
        halted_propagation_evidence(),
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence("dtcA"),
        hmm_inventory_evidence("dtcB"),
        hmm_inventory_evidence("dtcC"),
    ],
    "causal_graphs": [
        {
            "graph_id": "detocs_locus_depletes_atp",
            "title": "Detocs loci connect phage infection to ATP depletion",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Detocs locus to phage-associated ATP and dATP degradation, "
                "halted phage propagation, and the Detocs system trait "
                "without asserting the direct phage trigger or "
                "component-specific activation mechanism."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Detocs as a named ATP-depletion "
                "anti-phage system with DtcA, DtcB, and DtcC-family "
                "DefenseFinder profiles while leaving the direct phage "
                "trigger, component-specific phosphotransfer sequence, "
                "DtcC-variant effects, and universal system boundary "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "detocs_locus",
                    "label": "Detocs locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Detocs anti-phage defense locus represented in "
                        "DefenseFinder by dtcA and dtcB profiles plus an "
                        "optional dtcC-family profile."
                    ),
                },
                {
                    "node_id": "phage_associated_atp_degradation",
                    "label": "phage-associated ATP and dATP degradation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "ATP nucleosidase-mediated degradation of cellular "
                        "ATP and dATP during phage infection."
                    ),
                },
                {
                    "node_id": "halted_phage_propagation",
                    "label": "halted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Blockage of bacteriophage propagation after "
                        "ATP-and-dATP degradation during infection."
                    ),
                },
                {
                    "node_id": "detocs_system_trait",
                    "label": "Detocs system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Detocs "
                        "ATP-depletion phage-defense system."
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
                    "subject": "detocs_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "phage_associated_atp_degradation",
                    "description": (
                        "Rousset et al. connect ATP nucleosidase-domain "
                        "bacterial immune effectors to phage-associated "
                        "ATP and dATP degradation and discovered Detocs "
                        "from ATP nucleosidase domain homologs; "
                        "DefenseFinder catalogs Detocs with dtcA, dtcB, "
                        "and dtcC-family profiles."
                    ),
                    "evidence": [
                        {
                            "reference": ROUSSET,
                            "snippet": (
                                "By analyzing homologs of the immune ATP "
                                "nucleosidase domain, we discover and "
                                "characterize Detocs, a family of bacterial "
                                "defense systems"
                            ),
                            "notes": (
                                "Rousset et al. identify Detocs from "
                                "homologs of immune ATP nucleosidase "
                                "domains."
                            ),
                        },
                        atp_degradation_evidence(),
                        rules_evidence(),
                        hmm_inventory_evidence("dtcA"),
                        hmm_inventory_evidence("dtcB"),
                        hmm_inventory_evidence("dtcC"),
                    ],
                },
                {
                    "subject": "phage_associated_atp_degradation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "halted_phage_propagation",
                    "description": (
                        "ATP and dATP degradation during infection "
                        "contributes to halted phage propagation."
                    ),
                    "evidence": [
                        {
                            "reference": ROUSSET,
                            "snippet": (
                                "ATP and dATP degradation during infection "
                                "halts phage propagation"
                            ),
                            "notes": (
                                "Rousset et al. connect ATP and dATP "
                                "degradation to halted phage propagation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "halted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "detocs_system_trait",
                    "description": (
                        "Detocs-associated ATP and dATP depletion realizes "
                        "the Detocs system trait."
                    ),
                    "evidence": [
                        halted_propagation_evidence(),
                        {
                            "reference": ROUSSET,
                            "snippet": (
                                "we discover and characterize Detocs, a "
                                "family of bacterial defense systems"
                            ),
                            "notes": (
                                "Rousset et al. support Detocs as a named "
                                "bacterial defense-system family."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "detocs_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Detocs system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": ROUSSET,
                            "snippet": (
                                "we discover and characterize Detocs, a "
                                "family of bacterial defense systems"
                            ),
                            "notes": (
                                "Rousset et al. place Detocs in a bacterial "
                                "defense-system family."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "detocs-component-mechanism-gap",
            "prompt": (
                "Resolve Detocs phage triggers, component-specific "
                "phosphotransfer events, and DtcC-family effector outputs "
                "before minting narrower Detocs mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Rousset et al. support Detocs as a named family of "
                "two-component phosphotransfer-signaling bacterial defense "
                "systems, and DefenseFinder represents Detocs with required "
                "dtcA and dtcB profiles plus optional dtcC-family profiles. "
                "This system-level record leaves the direct phage trigger, "
                "component-specific activation route, exact ATP "
                "nucleosidase effector architecture, and DtcC-variant "
                "outputs unresolved."
            ),
            "attaches_to": ["causal_graphs#detocs_locus_depletes_atp"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
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
            "Minted Detocs system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is "
            f"reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_output(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    validate_output(record)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
    else:
        print(
            "Detocs system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
