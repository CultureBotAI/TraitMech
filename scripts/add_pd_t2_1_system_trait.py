#!/usr/bin/env python3
"""Add the PD-T2-1 system genomics trait."""

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
from traitmech.validation.write_validated import (  # noqa: E402
    emit_trait_yaml,
    write_validated_trait,
)

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "pd_t2_1_system.yaml"

GOEDECKE = "DOI:10.1038/s41564-025-02239-6"
GOEDECKE_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12875140/"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-29T22:58:06Z"
CANONICAL_EXAMPLE_REVIEW_TIMESTAMP = "2026-09-29T22:58:07Z"
IDENTIFIER = "traitmech:000476"
PROPOSAL = "proposals/metpo_traitmech_v353"

ABSTRACT_SNIPPET = (
    "Two phage proteins were further investigated, revealing T7 gp17 and "
    "additional tail fiber proteins activated the undescribed antiphage "
    "system PD-T2–1 and identifying λ gpE major capsid protein activated "
    "the antiphage system Avs8."
)
ECOR03_OPERON_SNIPPET = (
    "Sequencing the transposon insertion site of mutants that did grow "
    "revealed 28 out of 48 mutants contained transposons that disrupted "
    "a two-gene operon of unknown function"
)
FIGURE_OPERON_SNIPPET = (
    "Operon structure of phage defense against T2 system 1 (PD-T2–1). "
    "Transposon insertions identified in mutant ECOR03 expressing T7 gp17 "
    "are indicated with triangles. A predicted transmembrane domain (TM) "
    "for PD-T2–1A, accession numbers, and the length of each protein in "
    "amino acids (aa) are shown."
)
PHAGE_PROTECTION_SNIPPET = (
    "GeneAB conferred >100-fold protection against phages T2, T6, and "
    "Bas18, and approximately 10-fold protection against phages T4 and T5"
)
RENAME_SNIPPET = (
    "These findings led us to rename the geneAB operon phage defense "
    "against T2 system 1 (PD-T2–1)"
)
TAIL_FIBER_TRIGGER_SNIPPET = (
    "Transformation efficiency assays revealed that PD-T2–1 also "
    "selectively inhibited bacterial growth when T2 gp37, T2 gp34, and "
    "T2 gp12 were co-expressed"
)
TA_GAP_SNIPPET = (
    "These results indicate PD-T2–1 does not function as a canonical "
    "toxin-antitoxin system."
)
ECOR03_ACCESSION_SNIPPET = (
    "ECOR03 PD-T2–1A: RCR47252.1; WP_075861856.1"
)
ECOR03_GENOMIC_COORDINATE_SNIPPET = (
    "Nucleotide coordinates for PD-T2–1 in ECOR03 (accession QOWO01000016): "
    "10,064–11,256"
)
ARTICLE_REGISTRY_SNIPPET = (
    "PD-T2-1 | 10\\.1101/2025\\.07\\.02\\.662641 | Identifying phage "
    "proteins that activate the bacterial innate immune system"
)


def pmc_evidence(snippet: str, notes: str) -> dict[str, str]:
    return {
        "reference": GOEDECKE_PMC,
        "snippet": snippet,
        "notes": notes,
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The pinned DefenseFinder article registry maps the named "
            "PD-T2-1 system to the Goedecke et al. preprint."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "PD-T2-1 system",
    "definition": (
        "A phage defense system in which an organism possesses a two-gene "
        "PD-T2-1 operon whose expression was experimentally linked to "
        "protection against T2, T6, Bas18, T4, and T5 phages."
    ),
    "definition_source": GOEDECKE,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "PD-T2-1",
            "synonym_type": "EXACT_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "PD-T2–1",
            "synonym_type": "EXACT_SYNONYM",
            "source": GOEDECKE,
        },
        {
            "synonym_text": "geneAB operon",
            "synonym_type": "RELATED_SYNONYM",
            "source": GOEDECKE_PMC,
        },
    ],
    "evidence": [
        {
            "reference": GOEDECKE_PMC,
            "snippet": ABSTRACT_SNIPPET,
            "notes": (
                "Goedecke et al. report that T7 gp17 and additional tail "
                "fiber proteins activated the previously undescribed "
                "PD-T2-1 antiphage system."
            ),
        },
        pmc_evidence(
            ECOR03_OPERON_SNIPPET,
            (
                "ECOR03 transposon mutants that escaped T7 gp17-mediated "
                "growth inhibition were enriched for insertions disrupting "
                "the same unknown two-gene operon."
            ),
        ),
        pmc_evidence(
            FIGURE_OPERON_SNIPPET,
            (
                "The PD-T2-1 operon figure identifies transposon "
                "insertions, the predicted transmembrane domain in "
                "PD-T2-1A, and the protein accessions used in the study."
            ),
        ),
        pmc_evidence(
            PHAGE_PROTECTION_SNIPPET,
            (
                "Expression of the operon in MG1655 protected against T2, "
                "T6, Bas18, T4, and T5 in phage-challenge assays."
            ),
        ),
        pmc_evidence(
            RENAME_SNIPPET,
            (
                "Goedecke et al. renamed the placeholder geneAB operon "
                "phage defense against T2 system 1."
            ),
        ),
        pmc_evidence(
            TAIL_FIBER_TRIGGER_SNIPPET,
            (
                "PD-T2-1 also selectively inhibited growth when the T2 "
                "tail-fiber genes gp37, gp34, and gp12 were expressed."
            ),
        ),
        pmc_evidence(
            TA_GAP_SNIPPET,
            (
                "Single-gene expression experiments argue against "
                "PD-T2-1 as a canonical toxin-antitoxin system."
            ),
        ),
        pmc_evidence(
            ECOR03_ACCESSION_SNIPPET,
            (
                "The Methods section reports the ECOR03 PD-T2-1A "
                "RefSeq and nonredundant protein accessions used in the "
                "article."
            ),
        ),
        pmc_evidence(
            ECOR03_GENOMIC_COORDINATE_SNIPPET,
            (
                "The extended-data figure caption places the ECOR03 "
                "PD-T2-1 locus on nucleotide record QOWO01000016."
            ),
        ),
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "pd_t2_1_locus_phage_protection",
            "title": "PD-T2-1 loci protect against multiple phages",
            "description": (
                "Conservative system-level sketch linking a PD-T2-1 locus "
                "to experimentally measured T2, T6, Bas18, T4, and T5 "
                "protection."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures PD-T2-1 as a named phage-defense "
                "system in the final Goedecke et al. article and pinned "
                "DefenseFinder article registry while leaving the direct "
                "sensor or output mechanism, native host breadth, "
                "accession-level protein examples, profile-to-protein "
                "mapping, and exact DefenseFinder HMM/rules detection "
                "criteria unresolved."
            ),
            "nodes": [
                {
                    "node_id": "pd_t2_1_locus",
                    "label": "PD-T2-1 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene phage-defense locus corresponding to "
                        "the ECOR03 operon renamed PD-T2-1."
                    ),
                },
                {
                    "node_id": "pd_t2_1_listed_phage_protection",
                    "label": "T2, T6, Bas18, T4, and T5 protection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Protection against T2, T6, Bas18, T4, and T5 "
                        "after PD-T2-1 expression in MG1655."
                    ),
                },
                {
                    "node_id": "pd_t2_1_system_trait",
                    "label": "PD-T2-1 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded PD-T2-1 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "phage_defense_system",
                    "label": "phage defense system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000209",
                    "description": (
                        "Possession of one or more genome-encoded "
                        "immune systems that inhibit bacteriophage "
                        "infection."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "pd_t2_1_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "pd_t2_1_listed_phage_protection",
                    "description": (
                        "Expression of the PD-T2-1 operon in MG1655 "
                        "protected against phages T2, T6, Bas18, T4, "
                        "and T5."
                    ),
                    "evidence": [
                        pmc_evidence(
                            PHAGE_PROTECTION_SNIPPET,
                            (
                                "Goedecke et al. challenged MG1655 "
                                "expressing the PD-T2-1 operon with "
                                "diverse phages and measured protection."
                            ),
                        ),
                        pmc_evidence(
                            RENAME_SNIPPET,
                            (
                                "Goedecke et al. renamed the two-gene "
                                "geneAB operon PD-T2-1."
                            ),
                        ),
                    ],
                },
                {
                    "subject": "pd_t2_1_listed_phage_protection",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "pd_t2_1_system_trait",
                    "description": (
                        "Protection against T2, T6, Bas18, T4, and T5 "
                        "realizes the PD-T2-1 phage-defense-system trait."
                    ),
                    "evidence": [
                        pmc_evidence(
                            PHAGE_PROTECTION_SNIPPET,
                            (
                                "The PD-T2-1 operon conferred phage "
                                "protection when expressed in MG1655."
                            ),
                        )
                    ],
                },
                {
                    "subject": "pd_t2_1_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "PD-T2-1 system possession is a phage-defense "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": GOEDECKE_PMC,
                            "snippet": ABSTRACT_SNIPPET,
                            "notes": (
                                "Goedecke et al. identify PD-T2-1 as an "
                                "undescribed antiphage system."
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
            "discussion_id": "pd-t2-1-mechanism-and-model-coverage-gap",
            "prompt": (
                "Resolve the PD-T2-1 direct sensor, effector output, "
                "native host breadth, and DefenseFinder HMM/rules model "
                "coverage before minting narrower PD-T2-1 mechanism or "
                "protein-component traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The final Goedecke et al. article supports PD-T2-1 as a "
                "two-gene operon activated by multiple phage tail-fiber "
                "proteins, links heterologous expression to protection "
                "against T2, T6, Bas18, T4, and T5, and argues that the "
                "system is not a canonical toxin-antitoxin system. The "
                "pinned DefenseFinder article registry names PD-T2-1 and "
                "maps it to the Goedecke et al. preprint, but the pinned "
                "HMM inventory and rules table do not contain PD-T2-1 "
                "rows, leaving profile coverage and detection criteria "
                "unresolved."
            ),
            "evidence": [
                pmc_evidence(
                    TAIL_FIBER_TRIGGER_SNIPPET,
                    (
                        "PD-T2-1 responded to multiple T2 tail-fiber "
                        "proteins in transformation-efficiency assays."
                    ),
                ),
                pmc_evidence(
                    TA_GAP_SNIPPET,
                    (
                        "The PD-T2-1A/PD-T2-1B single-gene assays argue "
                        "against a canonical toxin-antitoxin mechanism."
                    ),
                ),
                article_registry_evidence(),
                {
                    "reference": DEFENSEFINDER_HMMS,
                    "notes": (
                        "No PD-T2-1 or PD-T2-1-prefixed HMM inventory "
                        "row was present in the pinned DefenseFinder "
                        "model file."
                    ),
                },
                {
                    "reference": DEFENSEFINDER_RULES,
                    "notes": (
                        "No PD-T2-1 rule row was present in the pinned "
                        "DefenseFinder rules table."
                    ),
                },
            ],
            "attaches_to": ["causal_graphs#pd_t2_1_locus_phage_protection"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-29",
        }
    ],
}


def validate_output(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


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
            "Minted PD-T2-1 system as a DOI- and DefenseFinder-backed "
            "GENOMICS TraitRecord under phage defense system after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record. The "
            f"{PROPOSAL} cohort reserves the replacement placeholder."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE_EVIDENCE_GAP",
        changes=(
            "Reviewed PD-T2-1 canonical_examples and left them empty "
            "because ECOR03 supports native discovery and locus "
            "coordinates without a verified NCBITaxon strain CURIE, while "
            "heterologous MG1655 phage-challenge assays do not by "
            "themselves support an endogenous named isolate exemplar. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_EXAMPLE_REVIEW_TIMESTAMP,
    )
    validate_output(record)

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{rel} already exists")
        write_validated_trait(record, TARGET)
        print(f"Wrote {rel}")
    else:
        sys.stdout.write(emit_trait_yaml(record))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
