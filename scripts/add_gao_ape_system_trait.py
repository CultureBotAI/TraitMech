#!/usr/bin/env python3
"""Add the ApeA system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gao_ape_system.yaml"

APE_BIORXIV = "DOI:10.64898/2026.01.26.701840"
DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

APE_IMMUNITY_SNIPPET = (
    "Here, we focus on ApeA, a HEPN-domain antiviral protein that confers "
    "immunity through cleavage of host tRNAs within their anticodon loops."
)
APE_LOW_MOI_SNIPPET = (
    "Both ApeA homologs confer protection at low MOI but not at high MOI, "
    "when most cells are infected"
)
APE_HEPN_SNIPPET = (
    "activity of Ec1ApeA and Ec2ApeA proteins was abrogated by HEPN active "
    "site R521A and R502A mutations respectively"
)
APE_TRNA_SNIPPET = (
    "Together, these results demonstrate that Ec1ApeA exhibits "
    "endoribonuclease activity targeting the tRNA anticodon loop, which is "
    "specifically activated during bacteriophage infection."
)
APE_DINUCLEOTIDE_SNIPPET = (
    "In vitro ribonuclease assays showed that under our experimental "
    "conditions tRNA cleavage by wild-type Ec2ApeA was activated by dpCG"
)
APE_DISCUSSION_SNIPPET = (
    "We further demonstrate that ApeA functions as an abortive infection "
    "system by cleaving host tRNAs within their anticodon loops to arrest "
    "translation"
)

HMM_ROW = (
    "| Gao_Ape__ApeA                                    | "
    "Gao_Ape__ApeA                                    | Gao_Ape                | "
    "Custom                  | 18     |"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T11:03:58Z"

IDENTIFIER = "traitmech:000334"
PROPOSAL = "proposals/metpo_traitmech_v211"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Gao_Ape | 10\\.1126/science\\.aba0372 | Diverse enzymatic "
            "activities mediate antiviral immunity in prokaryotes"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Gao_Ape "
            "system to the Gao et al. prokaryotic antiviral-immunity paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "Gao_Ape\tGao_Ape\t1\t1\tGao_Ape__ApeA\t\t\t",
        "notes": (
            "The DefenseFinder rules table models Gao_Ape as a "
            "single-mandatory-profile system with the Gao_Ape__ApeA profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records ApeA under the Gao_Ape "
            "model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "ApeA system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "single-component ApeA locus represented by the DefenseFinder "
        "Gao_Ape__ApeA profile, encoding an oligomeric HEPN-domain antiviral "
        "ribonuclease whose activation can cleave host tRNAs within their "
        "anticodon loops and drive abortive bacteriophage infection."
    ),
    "definition_source": APE_BIORXIV,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "ApeA",
            "synonym_type": "RELATED_SYNONYM",
            "source": APE_BIORXIV,
        },
        {
            "synonym_text": "Gao_Ape",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
    ],
    "evidence": [
        {
            "reference": APE_BIORXIV,
            "snippet": APE_IMMUNITY_SNIPPET,
            "notes": (
                "Juozapaitis et al. describe ApeA as a HEPN-domain "
                "antiviral protein that cleaves host tRNAs within their "
                "anticodon loops."
            ),
        },
        {
            "reference": APE_BIORXIV,
            "snippet": APE_LOW_MOI_SNIPPET,
            "notes": (
                "Juozapaitis et al. show that Ec1ApeA and Ec2ApeA protect "
                "at low multiplicity of infection but not high multiplicity, "
                "supporting abortive-infection behavior."
            ),
        },
        {
            "reference": APE_BIORXIV,
            "snippet": APE_HEPN_SNIPPET,
            "notes": (
                "HEPN active-site mutations abrogated antiviral activity in "
                "the tested Ec1ApeA and Ec2ApeA proteins."
            ),
        },
        {
            "reference": APE_BIORXIV,
            "snippet": APE_TRNA_SNIPPET,
            "notes": (
                "Ec1ApeA exhibits infection-activated endoribonuclease "
                "activity targeting the tRNA anticodon loop."
            ),
        },
        {
            "reference": APE_BIORXIV,
            "snippet": APE_DINUCLEOTIDE_SNIPPET,
            "notes": (
                "Ec2ApeA tRNA cleavage can be activated by "
                "deoxydinucleotides in vitro, supporting ligand-stimulated "
                "ApeA RNase activity for one ApeA variant."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "gao_ape_hepn_rnase_aborts_phage",
            "title": "ApeA loci activate HEPN RNase phage defense",
            "description": (
                "Conservative system-level sketch linking a Gao_Ape/ApeA "
                "locus to HEPN RNase activation, tRNA anticodon-loop "
                "cleavage, abortive phage restriction, and the ApeA system "
                "trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures ApeA as a named DefenseFinder "
                "single-component system with a HEPN RNase output while "
                "leaving the natural-host accession breadth, Ec1ApeA versus "
                "Ec2ApeA trigger differences, the exact phage nuclease "
                "inputs to deoxydinucleotide signaling, and activity of "
                "additional homologs unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gao_ape_locus",
                    "label": "Gao_Ape locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-component ApeA antiphage locus represented "
                        "by the DefenseFinder Gao_Ape__ApeA profile."
                    ),
                },
                {
                    "node_id": "apea_hepn_rnase_activity",
                    "label": "ApeA HEPN RNase activity",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "Ligand-triggered ApeA ribonuclease activity "
                        "dependent on HEPN active-site residues."
                    ),
                },
                {
                    "node_id": "trna_anticodon_loop_cleavage",
                    "label": "tRNA anticodon-loop cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Cleavage of host tRNAs within their anticodon "
                        "loops by activated ApeA HEPN RNase."
                    ),
                },
                {
                    "node_id": "abortive_phage_restriction",
                    "label": "abortive phage restriction",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection defense in which ApeA-mediated "
                        "translation arrest restricts bacteriophage "
                        "propagation."
                    ),
                },
                {
                    "node_id": "apea_system_trait",
                    "label": "ApeA system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded ApeA phage-defense "
                        "system."
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
                    "subject": "gao_ape_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "apea_hepn_rnase_activity",
                    "description": (
                        "ApeA loci encode a HEPN-domain antiviral RNase, and "
                        "DefenseFinder models Gao_Ape as a single-profile "
                        "ApeA system."
                    ),
                    "evidence": [
                        {
                            "reference": APE_BIORXIV,
                            "snippet": APE_IMMUNITY_SNIPPET,
                            "notes": (
                                "Juozapaitis et al. connect ApeA to "
                                "HEPN-domain antiviral RNase activity."
                            ),
                        },
                        {
                            "reference": APE_BIORXIV,
                            "snippet": APE_HEPN_SNIPPET,
                            "notes": (
                                "HEPN active-site mutations eliminated "
                                "activity in Ec1ApeA and Ec2ApeA."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "apea_hepn_rnase_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "trna_anticodon_loop_cleavage",
                    "description": (
                        "Activated ApeA HEPN RNase cleaves host tRNAs "
                        "within their anticodon loops."
                    ),
                    "evidence": [
                        {
                            "reference": APE_BIORXIV,
                            "snippet": APE_TRNA_SNIPPET,
                            "notes": (
                                "Ec1ApeA endoribonuclease activity targets "
                                "the tRNA anticodon loop during phage "
                                "infection."
                            ),
                        },
                        {
                            "reference": APE_BIORXIV,
                            "snippet": APE_DINUCLEOTIDE_SNIPPET,
                            "notes": (
                                "Ec2ApeA tRNA-cleavage activity can be "
                                "reconstituted in vitro with "
                                "deoxydinucleotide ligands."
                            ),
                        },
                    ],
                },
                {
                    "subject": "trna_anticodon_loop_cleavage",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abortive_phage_restriction",
                    "description": (
                        "ApeA-mediated host tRNA cleavage arrests "
                        "translation during abortive phage defense."
                    ),
                    "evidence": [
                        {
                            "reference": APE_BIORXIV,
                            "snippet": APE_DISCUSSION_SNIPPET,
                            "notes": (
                                "Juozapaitis et al. link ApeA tRNA "
                                "anticodon-loop cleavage to translation "
                                "arrest during abortive infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abortive_phage_restriction",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "apea_system_trait",
                    "description": (
                        "ApeA low-MOI protection and abortive infection "
                        "realize the ApeA system possession trait."
                    ),
                    "evidence": [
                        {
                            "reference": APE_BIORXIV,
                            "snippet": APE_LOW_MOI_SNIPPET,
                            "notes": (
                                "Ec1ApeA and Ec2ApeA low-MOI protection "
                                "supports ApeA as an abortive infection "
                                "system."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "apea_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "ApeA system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "apea-trigger-and-homolog-scope-gap",
            "prompt": (
                "Resolve ApeA natural-host loci, homolog-specific "
                "small-molecule triggers, phage nuclease inputs, and "
                "subtype activity before minting narrower ApeA mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Juozapaitis et al. support ApeA as an abortive infection "
                "system whose HEPN RNase can cleave host tRNAs within their "
                "anticodon loops, and DefenseFinder models Gao_Ape with the "
                "Gao_Ape__ApeA profile. This first record stays at system "
                "level because the curated evidence resolves "
                "deoxydinucleotide activation for Ec2ApeA, leaves the "
                "Ec1ApeA activator unidentified, assays several homologs "
                "heterologously, and does not yet define accession-level "
                "natural-host breadth."
            ),
            "attaches_to": ["causal_graphs#gao_ape_hepn_rnase_aborts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
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
            "Minted ApeA system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
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
            "Reviewed the ApeA canonical_examples gap and left "
            "canonical_examples empty: the current evidence supports a "
            "named single-component phage-defense system, DefenseFinder "
            "Gao_Ape/ApeA profiles, and heterologously assayed ApeA "
            "homologs, but does not yet cite a directly observed natural "
            "microbial taxon with a source-backed Gao_Ape/ApeA locus. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp="2026-09-21T11:04:58Z",
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
