#!/usr/bin/env python3
"""Add the ENDPaCF1 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "endpacf1_system.yaml"

YEE = "DOI:10.1101/2025.03.31.646159"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-30T23:39:24Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-30T23:39:25Z"
COPILOT_REVIEW_FIX_TIMESTAMP = "2026-10-01T00:24:07Z"
IDENTIFIER = "traitmech:000503"
PHAGE_DEFENSE_SYSTEM = "traitmech:000209"
PROPOSAL = "proposals/metpo_traitmech_v380"

ARTICLE_ROW = (
    "| ENDPaCF1 | 10\\.1101/2025\\.03\\.31\\.646159 | END nucleases: "
    "Antiphage defense systems targeting multiple hypermodified phage genomes | "
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the ENDPaCF1 "
            "source key to the Yee et al. bioRxiv preprint."
        ),
    }


def hmm_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder HMM "
            "inventory found no exact ENDPaCF1 row."
        ),
    }


def rules_absence_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "notes": (
            "A structured first-pass search of the pinned DefenseFinder "
            "rules table found no exact ENDPaCF1 system row."
        ),
    }


def yee_system_evidence() -> dict[str, str]:
    return {
        "reference": YEE,
        "snippet": (
            "The causal defense system is a Type IIS restriction "
            "endonuclease-like protein (ENDPaCF1), common in "
            "Pseudomonads, however it lacks an associated methyltransferase "
            "typical Type IIS R-M systems."
        ),
        "notes": (
            "Yee et al. identify ENDPaCF1 as the causal Pseudomonas "
            "antiphage system and distinguish it from canonical Type IIS "
            "restriction-modification systems."
        ),
    }


def yee_hypermodified_dna_evidence() -> dict[str, str]:
    return {
        "reference": YEE,
        "snippet": (
            "ENDPaCF1 protects bacteria against phages with hypermodified "
            "DNA and is surprisingly agnostic to the specific structure of "
            "the modification, which is unlike typical type IV restriction "
            "endonucleases."
        ),
        "notes": (
            "Yee et al. connect ENDPaCF1 to protection against phages with "
            "multiple hypermodified-DNA chemistries."
        ),
    }


def yee_native_deletion_evidence() -> dict[str, str]:
    return {
        "reference": YEE,
        "snippet": (
            "Here, we employed the CRISPR-based Cascade-Cas3 system to "
            "delete defense islands in a Pseudomonas aeruginosa clinical "
            "isolate to identify mechanisms of lytic phage antagonism. "
            "Deletion of one island in a cystic fibrosis-derived clinical "
            "isolate sensitized the strain to phages from the Pbunavirus "
            "family, which are commonly used as therapeutics."
        ),
        "notes": (
            "Yee et al. identified the ENDPaCF1 island as an endogenous "
            "Pseudomonas aeruginosa phage-defense determinant."
        ),
    }


def yee_domain_evidence() -> dict[str, str]:
    return {
        "reference": YEE,
        "snippet": (
            "In ENDPaCF1, the endonuclease domain is fused to a "
            "catalytically inactive Endonuclease III (iEndoIII), a domain "
            "that recognizes non-canonical bases to repair DNA in "
            "prokaryotes and eukaryotes."
        ),
        "notes": (
            "Yee et al. describe the ENDPaCF1 endonuclease plus inactive "
            "Endonuclease III domain architecture."
        ),
    }


def yee_end_nuclease_evidence() -> dict[str, str]:
    return {
        "reference": YEE,
        "snippet": (
            "We therefore propose that nucleases containing an iEndoIII "
            "domain (END nucleases) can sense diverse DNA "
            "hypermodifications."
        ),
        "notes": (
            "Yee et al. propose the END nuclease family around the iEndoIII "
            "domain's ability to sense diverse DNA modifications."
        ),
    }


def yee_sensing_cleavage_modularity_evidence() -> dict[str, str]:
    return {
        "reference": YEE,
        "snippet": (
            "Our findings reveal modularity of the sensing and cleavage "
            "domains, as expected of a modification-dependent "
            "endonucleases."
        ),
        "notes": (
            "Yee et al. frame END nuclease activity as "
            "modification-dependent coupling between sensing and cleavage "
            "domains."
        ),
    }


def yee_inhibitor_evidence() -> dict[str, str]:
    return {
        "reference": YEE,
        "snippet": (
            "We further show that some hypermodified phages, including "
            "Pbunavirus family members and Wrowclawvirus family "
            "(Pa5oct-like) of jumbo phages, encode END nuclease inhibitors "
            "that directly bind to the nuclease, likely via the iEndoIII "
            "domain."
        ),
        "notes": (
            "Yee et al. support direct phage inhibitor binding to END "
            "nucleases while leaving ENDPaCF1 inhibitor breadth unresolved."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "ENDPaCF1 system",
    "definition": (
        "A phage defense system in which an organism possesses an ENDPaCF1 "
        "Type IIS restriction endonuclease-like locus with an inactive "
        "Endonuclease III sensing domain that can recognize diverse DNA "
        "hypermodifications and protect bacteria from hypermodified phages."
    ),
    "definition_source": YEE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PHAGE_DEFENSE_SYSTEM],
    "synonyms": [
        {
            "synonym_text": "ENDPaCF1",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        yee_system_evidence(),
        yee_hypermodified_dna_evidence(),
        yee_native_deletion_evidence(),
        yee_domain_evidence(),
        yee_end_nuclease_evidence(),
        yee_inhibitor_evidence(),
        article_registry_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:287",
            "taxon_label": "Pseudomonas aeruginosa",
            "note": (
                "Yee et al. identified ENDPaCF1 in the cystic-fibrosis-"
                "derived clinical isolate CF040 and showed that deleting "
                "the ENDPaCF1-bearing defense island sensitized the native "
                "Pseudomonas aeruginosa strain to Pbunavirus phages."
            ),
            "reference": YEE,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "endpacf1_targets_hypermodified_phage_dna",
            "title": "ENDPaCF1 targets hypermodified phage DNA",
            "description": (
                "Conservative system-level sketch linking an ENDPaCF1 locus "
                "to iEndoIII-linked sensing of hypermodified phage DNA, "
                "modification-dependent endonuclease targeting, phage "
                "restriction, and ENDPaCF1 system possession."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures ENDPaCF1 as a named single-protein "
                "phage-defense system with Type IIS restriction "
                "endonuclease-like and iEndoIII domains while leaving "
                "Pseudomonas natural host breadth, complete DNA-modification "
                "breadth, direct domain coupling, phage-inhibitor "
                "specificity, and DefenseFinder HMM/rules detection criteria "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "endpacf1_locus",
                    "label": "ENDPaCF1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An ENDPaCF1 anti-phage locus encoding a Type IIS "
                        "restriction endonuclease-like protein fused to an "
                        "inactive Endonuclease III domain."
                    ),
                },
                {
                    "node_id": "hypermodified_phage_dna_sensing",
                    "label": "hypermodified phage DNA sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Recognition of diverse DNA hypermodifications by "
                        "ENDPaCF1-family END nuclease systems."
                    ),
                },
                {
                    "node_id": "modification_dependent_phage_dna_cleavage",
                    "label": "modification-dependent phage DNA cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cleavage of phage DNA by a nuclease after "
                        "hypermodified DNA is detected."
                    ),
                },
                {
                    "node_id": "hypermodified_phage_infection",
                    "label": "hypermodified phage infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Infection by bacteriophages that carry "
                        "hypermodified genomes."
                    ),
                },
                {
                    "node_id": "endpacf1_system_trait",
                    "label": "ENDPaCF1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded ENDPaCF1 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": PHAGE_DEFENSE_SYSTEM,
                    "description": (
                        "Possession of one or more genome-encoded immune "
                        "systems that inhibit bacteriophage infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "endpacf1_locus",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "hypermodified_phage_dna_sensing",
                    "description": (
                        "An ENDPaCF1 locus enables sensing of diverse "
                        "hypermodified phage genomes."
                    ),
                    "evidence": [
                        yee_system_evidence(),
                        yee_domain_evidence(),
                        yee_end_nuclease_evidence(),
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "hypermodified_phage_infection",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "hypermodified_phage_dna_sensing",
                    "description": (
                        "Hypermodified phage genomes provide the substrate "
                        "recognized by ENDPaCF1-family END nucleases."
                    ),
                    "evidence": [yee_hypermodified_dna_evidence()],
                },
                {
                    "subject": "modification_dependent_phage_dna_cleavage",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "hypermodified_phage_infection",
                    "description": (
                        "Modification-dependent phage DNA cleavage protects "
                        "bacteria against phages with hypermodified DNA."
                    ),
                    "evidence": [yee_hypermodified_dna_evidence()],
                },
                {
                    "subject": "modification_dependent_phage_dna_cleavage",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "endpacf1_system_trait",
                    "description": (
                        "ENDPaCF1-family targeting of hypermodified phage "
                        "DNA realizes the ENDPaCF1 system trait."
                    ),
                    "evidence": [yee_sensing_cleavage_modularity_evidence()],
                },
                {
                    "subject": "endpacf1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "ENDPaCF1 system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        yee_system_evidence(),
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "endpacf1-host-modification-and-model-gap",
            "prompt": (
                "Resolve ENDPaCF1 Pseudomonas host breadth, complete "
                "phage-DNA hypermodification breadth, direct iEndoIII "
                "sensing-to-cleavage coupling, phage inhibitor specificity, "
                "and DefenseFinder HMM/rules coverage before minting "
                "narrower END nuclease mechanism or component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Yee et al. support ENDPaCF1 as a Type IIS restriction "
                "endonuclease-like Pseudomonas phage-defense system that "
                "can recognize diverse hypermodified phage genomes, and "
                "the pinned DefenseFinder article registry maps the "
                "ENDPaCF1 source key to the Yee et al. preprint. The "
                "pinned HMM inventory and rules table have no exact "
                "ENDPaCF1 rows. This first-pass record therefore does not "
                "resolve a complete profile model, the direct domain "
                "coupling between iEndoIII sensing and cleavage, or the "
                "full natural host, phage, and inhibitor breadth."
            ),
            "evidence": [
                yee_system_evidence(),
                yee_hypermodified_dna_evidence(),
                yee_domain_evidence(),
                yee_inhibitor_evidence(),
                article_registry_evidence(),
                hmm_absence_evidence(),
                rules_absence_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#endpacf1_targets_hypermodified_phage_dna"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-09-30",
        }
    ],
}


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
            "Minted ENDPaCF1 system as a bioRxiv- and "
            "DefenseFinder-backed GENOMICS TraitRecord under phage defense "
            "system after an ignored-and-hidden duplicate review found no "
            "exact live TraitMech, METPO, history, research, generated, or "
            "prior proposal record; kept the graph at Type IIS "
            "restriction-endonuclease-like system level because the pinned "
            "DefenseFinder article row is not backed by pinned HMM or "
            "rules rows; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed ENDPaCF1 system canonical_examples and left them "
            "empty because public preprint and DefenseFinder evidence "
            "supports the named phage-defense system but not a direct "
            "named native microbial isolate exemplar with experimentally "
            "verified endogenous ENDPaCF1 activity. No paid research was "
            "used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_ENDPACF1_REVIEW_FINDINGS",
        changes=(
            "Addressed Copilot review issues #1501, #1502, and #1503: "
            "added Pseudomonas aeruginosa (NCBITaxon:287) as a DOI-backed "
            "native ENDPaCF1 canonical example, removed the unsupported "
            "direct hypermodified-phage-DNA-sensing to modification-"
            "dependent-phage-DNA-cleavage causal edge, and included the "
            "discussions block in the repository CREATE history sections."
        ),
        llm_assisted=True,
        timestamp=COPILOT_REVIEW_FIX_TIMESTAMP,
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
