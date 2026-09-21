#!/usr/bin/env python3
"""Add the MazEF system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "mazef_system.yaml"

NIKOLIC_MAZEF = "DOI:10.1098/rsbl.2025.0080"
NIKOLIC_MAZEF_PMID = "PMID:40494395"
NIKOLIC_MAZEF_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12151602/"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T21:03:46Z"
IDENTIFIER = "traitmech:000345"
PROPOSAL = "proposals/metpo_traitmech_v222"

ARTICLE_REGISTRY_SNIPPET = (
    "MazEF | 10\\.1098/rsbl\\.2025\\.0080 | A bacterial "
    "toxin-antitoxin system as a native defence element against RNA phages"
)
RULES_SNIPPET = "MazEF\tMazEF\t2\t2\tMazEF__MazE, MazEF__MazF"
MAZE_HMM_ROW = (
    "| MazEF__MazE                                      | "
    "MazEF__MazE                                      | "
    "MazEF                  | Custom                  | 20     |"
)
MAZF_HMM_ROW = (
    "| MazEF__MazF                                      | "
    "MazEF__MazF                                      | "
    "MazEF                  | Custom                  | 20     |"
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named MazEF system "
            "to the Nikolic et al. RNA-phage defense paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models MazEF as a two-profile "
            "system requiring MazE and MazF profiles."
        ),
    }


def maze_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": MAZE_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records the MazE profile in "
            "the MazEF model namespace."
        ),
    }


def mazf_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": MAZF_HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records the MazF profile in "
            "the MazEF model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "MazEF system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "two-component MazEF toxin-antitoxin locus whose MazE antitoxin "
        "and MazF endoribonuclease can protect Escherichia coli against "
        "RNA phages and that DefenseFinder represents with mandatory "
        "MazEF__MazE and MazEF__MazF profiles."
    ),
    "definition_source": NIKOLIC_MAZEF,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "MazEF",
            "synonym_type": "EXACT_SYNONYM",
            "source": NIKOLIC_MAZEF_PMID,
        },
        {
            "synonym_text": "mazEF",
            "synonym_type": "RELATED_SYNONYM",
            "source": NIKOLIC_MAZEF_PMID,
        },
        {
            "synonym_text": "MazEF__MazE",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "MazEF__MazF",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": NIKOLIC_MAZEF_PMID,
            "snippet": (
                "we investigated the role of a model toxin-antitoxin "
                "system, MazEF, in protecting Escherichia coli against "
                "two RNA phage species"
            ),
            "notes": (
                "Nikolic et al. directly tested MazEF as an Escherichia "
                "coli toxin-antitoxin module protecting against RNA phages."
            ),
        },
        {
            "reference": NIKOLIC_MAZEF_PMID,
            "snippet": (
                "the native presence of mazEF moderately reduced "
                "population susceptibility and increased the survival of "
                "individual E. coli cells"
            ),
            "notes": (
                "Nikolic et al. support native mazEF as a moderate RNA "
                "phage defense determinant in Escherichia coli."
            ),
        },
        {
            "reference": NIKOLIC_MAZEF_PMID,
            "snippet": (
                "Genomic analysis further revealed an underrepresentation "
                "of the MazF cleavage site in genomes of RNA phages "
                "infecting E. coli"
            ),
            "notes": (
                "Nikolic et al. support selection against MazF ACA "
                "cleavage sites in RNA phages that infect E. coli."
            ),
        },
        {
            "reference": NIKOLIC_MAZEF_PMC,
            "snippet": (
                "MazEF interferes with RNA phage replication within "
                "already infected cells"
            ),
            "notes": (
                "Nikolic et al. interpret the mazEF deletion phenotype as "
                "intracellular interference with RNA phage replication, not "
                "an adsorption defect."
            ),
        },
        {
            "reference": NIKOLIC_MAZEF_PMC,
            "snippet": (
                "direct interference, rather than abortive infection, plays "
                "the predominant role in the case of MazEF"
            ),
            "notes": (
                "Nikolic et al. caution that the main MazEF effect in their "
                "RNA phage assays appears to be direct interference rather "
                "than abortive infection."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        maze_hmm_evidence(),
        mazf_hmm_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Nikolic et al. compared Escherichia coli K-12 MG1655 "
                "derivatives carrying or lacking the native mazEF locus and "
                "found moderate but measurable native mazEF protection "
                "against the MS2 and Qbeta RNA phages."
            ),
            "reference": NIKOLIC_MAZEF,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "mazef_rna_phage_defense",
            "title": "MazEF loci reduce RNA phage susceptibility",
            "description": (
                "Conservative system-level sketch linking a MazEF locus to "
                "native RNA phage defense and the MazEF system possession "
                "trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures native MazEF protection against RNA "
                "phages without asserting a phage-triggered MazF activation "
                "route, a resolved direct phage-RNA cleavage event, "
                "MazEF-mediated DNA-phage defense breadth, or a generic "
                "abortive-infection output."
            ),
            "nodes": [
                {
                    "node_id": "mazef_locus",
                    "label": "MazEF locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-component toxin-antitoxin locus represented "
                        "by MazE and MazF profiles."
                    ),
                },
                {
                    "node_id": "rna_phage_replication_interference",
                    "label": "RNA phage replication interference",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced RNA phage replication or survival of RNA "
                        "phage-infected cells associated with native mazEF."
                    ),
                },
                {
                    "node_id": "mazef_system_trait",
                    "label": "MazEF system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded MazEF "
                        "toxin-antitoxin phage-defense system."
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
                    "subject": "mazef_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "rna_phage_replication_interference",
                    "description": (
                        "Native mazEF contributes to reduced Escherichia "
                        "coli susceptibility to the MS2 and Qbeta RNA "
                        "phages."
                    ),
                    "evidence": [
                        {
                            "reference": NIKOLIC_MAZEF_PMID,
                            "snippet": (
                                "the native presence of mazEF moderately "
                                "reduced population susceptibility"
                            ),
                            "notes": (
                                "Nikolic et al. connect native mazEF "
                                "presence to reduced RNA phage "
                                "susceptibility."
                            ),
                        },
                        {
                            "reference": NIKOLIC_MAZEF_PMC,
                            "snippet": (
                                "MazEF interferes with RNA phage "
                                "replication within already infected cells"
                            ),
                            "notes": (
                                "Nikolic et al. distinguish MazEF-mediated "
                                "intracellular interference from blocked "
                                "RNA phage adsorption."
                            ),
                        },
                    ],
                },
                {
                    "subject": "rna_phage_replication_interference",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "mazef_system_trait",
                    "description": (
                        "MazEF-associated reduction of RNA phage "
                        "susceptibility realizes the MazEF system trait."
                    ),
                    "evidence": [
                        {
                            "reference": NIKOLIC_MAZEF_PMID,
                            "snippet": (
                                "RNA-degrading toxin-antitoxin systems may "
                                "also help defend against RNA phages"
                            ),
                            "notes": (
                                "Nikolic et al. frame the MazEF result as "
                                "support for RNA-degrading toxin-antitoxin "
                                "systems as RNA phage defense elements."
                            ),
                        }
                    ],
                },
                {
                    "subject": "mazef_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "MazEF system possession is a "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEFENSEFINDER_ARTICLES,
                            "snippet": ARTICLE_REGISTRY_SNIPPET,
                            "notes": (
                                "DefenseFinder associates MazEF with the "
                                "Nikolic et al. RNA-phage defense paper."
                            ),
                        },
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "mazef-activation-breadth-gap",
            "prompt": (
                "Resolve MazEF activation, direct MazF RNA targets, and "
                "RNA- versus DNA-phage breadth before minting narrower "
                "MazEF mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Nikolic et al. support native MazEF protection against "
                "RNA phages and argue that direct interference "
                "predominates in those assays, but the phage-induced "
                "route to active MazF, the relative contributions of "
                "phage-RNA cleavage and host-RNA degradation, the breadth "
                "of MazEF DNA-phage defense, and the DefenseFinder MazEF "
                "model boundaries remain unresolved."
            ),
            "attaches_to": ["causal_graphs#mazef_rna_phage_defense"],
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
            "Minted MazEF system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is "
            f"reserved in {PROPOSAL}."
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
