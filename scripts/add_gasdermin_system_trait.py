#!/usr/bin/env python3
"""Add the GasderMIN system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "gasdermin_system.yaml"

JOHNSON = "DOI:10.1126/science.abj8432"
JOHNSON_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC9134750/"

BGSDM_DISCOVERY_SNIPPET = (
    "We discovered gasdermin homologs encoded in bacteria that defended "
    "against phages and executed cell death."
)
BGSDM_DISTRIBUTION_SNIPPET = (
    "bGSDM-protease systems are found in diverse bacteria and archaea, as "
    "well as in metagenomic samples of prokaryotic origin"
)
LYSOBACTER_DEFENSE_SNIPPET = (
    "a four gene operon from Lysobacter enzymogenes exhibited robust defense "
    "against coliphages T4, T5, and T6"
)
LYSOBACTER_DELETION_SNIPPET = (
    "Deletion of the bGSDM gene from the Lysobacter operon abolished "
    "protection"
)
BGSDM_PROTEASE_SNIPPET = (
    "Bacterial gasdermins were activated by dedicated caspase-like proteases "
    "that catalyzed site-specific cleavage and the removal of an inhibitory "
    "C-terminal peptide."
)
PORE_ASSEMBLY_SNIPPET = (
    "Release of autoinhibition induced the assembly of large and "
    "heterogeneous pores that disrupted membrane integrity."
)
RUNELLA_PROTEASE_SNIPPET = (
    "The Runella bGSDM and protease only induced cellular toxicity when "
    "expressed together"
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
TIMESTAMP = "2026-09-21T13:10:00Z"

IDENTIFIER = "traitmech:000336"
PROPOSAL = "proposals/metpo_traitmech_v213"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "GasderMIN | 10\\.1101/2021\\.06\\.07\\.447441 | "
            "Bacterial gasdermins reveal an ancient mechanism of cell death"
        ),
        "notes": (
            "The DefenseFinder article registry maps the GasderMIN model "
            "namespace to the Johnson et al. bacterial gasdermin preprint, "
            "later published under DOI:10.1126/science.abj8432."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": (
            "| GasderMIN__bGSDM                                 | "
            "GasderMIN__bGSDM___bGSDM                         | "
            "GasderMIN              | Custom                  | 50     |"
        ),
        "notes": (
            "The DefenseFinder HMM inventory records the bGSDM profile "
            "under the GasderMIN model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "GasderMIN\tGasderMIN\t1\t1\tGasderMIN__bGSDM\t\t\t",
        "notes": (
            "The DefenseFinder rules table models GasderMIN as a "
            "one-mandatory-profile system requiring GasderMIN__bGSDM."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "GasderMIN system",
    "definition": (
        "A phage defense system in which an organism possesses a bacterial "
        "gasdermin locus represented by the DefenseFinder GasderMIN__bGSDM "
        "profile, whose bGSDM effectors are associated with bacteriophage "
        "defense and can be proteolytically activated in characterized "
        "bGSDM-protease systems to assemble membrane pores, disrupt membrane "
        "integrity, and execute cell death."
    ),
    "definition_source": JOHNSON,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "GasderMIN",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        {
            "synonym_text": "GasderMIN__bGSDM",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        {
            "reference": JOHNSON,
            "snippet": BGSDM_DISCOVERY_SNIPPET,
            "notes": (
                "Johnson et al. support bacterial gasdermin homologs as "
                "phage-defense proteins that execute cell death."
            ),
        },
        {
            "reference": JOHNSON_PMC,
            "snippet": BGSDM_DISTRIBUTION_SNIPPET,
            "notes": (
                "Johnson et al. report bGSDM-protease systems across "
                "bacteria, archaea, and prokaryotic metagenomic samples, "
                "supporting curation above one engineered locus."
            ),
        },
        {
            "reference": JOHNSON_PMC,
            "snippet": LYSOBACTER_DEFENSE_SNIPPET,
            "notes": (
                "Johnson et al. experimentally tested a Lysobacter "
                "enzymogenes bGSDM-containing operon that defended against "
                "coliphages T4, T5, and T6."
            ),
        },
        {
            "reference": JOHNSON_PMC,
            "snippet": LYSOBACTER_DELETION_SNIPPET,
            "notes": (
                "Deletion of the bGSDM gene from the Lysobacter operon "
                "abolished the observed phage protection."
            ),
        },
        {
            "reference": JOHNSON,
            "snippet": BGSDM_PROTEASE_SNIPPET,
            "notes": (
                "Johnson et al. connect bacterial gasdermin activation to "
                "dedicated caspase-like proteases that remove an inhibitory "
                "C-terminal peptide."
            ),
        },
        {
            "reference": JOHNSON,
            "snippet": PORE_ASSEMBLY_SNIPPET,
            "notes": (
                "Johnson et al. support pore assembly and membrane "
                "disruption as outputs of bacterial gasdermin "
                "autoinhibition release."
            ),
        },
        article_registry_evidence(),
        hmm_inventory_evidence(),
        rules_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:69",
            "taxon_label": "Lysobacter enzymogenes",
            "note": (
                "Johnson et al. showed that a Lysobacter enzymogenes "
                "bGSDM-containing operon provided robust defense against "
                "coliphages T4, T5, and T6 in an Escherichia coli "
                "heterologous assay, and that deleting the bGSDM gene "
                "abolished protection."
            ),
            "reference": JOHNSON,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "gasdermin_proteolysis_triggers_pore_cell_death",
            "title": "GasderMIN activation forms lethal membrane pores",
            "description": (
                "System-level sketch linking a bacterial gasdermin locus to "
                "phage defense-system possession and linking characterized "
                "bGSDM-protease systems to caspase-like proteolytic "
                "activation, gasdermin pore assembly, membrane disruption, "
                "and cell death."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures GasderMIN as a named DefenseFinder "
                "single-mandatory-profile system supported by Johnson et al. "
                "bacterial gasdermin experiments while leaving the natural "
                "phage trigger, the universality of adjacent protease "
                "activation, the full family breadth, and CARD-NLR-associated "
                "gasdermin variants unresolved."
            ),
            "nodes": [
                {
                    "node_id": "gasdermin_locus",
                    "label": "bacterial gasdermin locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A bacterial gasdermin phage-defense locus cataloged "
                        "in DefenseFinder with the GasderMIN__bGSDM profile."
                    ),
                },
                {
                    "node_id": "caspase_like_bgsdm_cleavage",
                    "label": "caspase-like bGSDM cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Site-specific bacterial gasdermin cleavage by a "
                        "dedicated caspase-like protease."
                    ),
                },
                {
                    "node_id": "gasdermin_pore_assembly",
                    "label": "bacterial gasdermin pore assembly",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Assembly of activated bacterial gasdermins into "
                        "large membrane pores."
                    ),
                },
                {
                    "node_id": "membrane_integrity_disruption",
                    "label": "membrane integrity disruption",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Loss of bacterial membrane integrity after "
                        "gasdermin pore formation."
                    ),
                },
                {
                    "node_id": "gasdermin_cell_death",
                    "label": "gasdermin-dependent cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Host cell death executed by activated bacterial "
                        "gasdermin pores."
                    ),
                },
                {
                    "node_id": "gasdermin_system_trait",
                    "label": "GasderMIN system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded GasderMIN "
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
                    "subject": "gasdermin_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "caspase_like_bgsdm_cleavage",
                    "description": (
                        "Characterized bacterial gasdermin-protease loci can "
                        "encode dedicated caspase-like proteases that cleave "
                        "bGSDM effectors and remove their inhibitory "
                        "C-terminal peptide."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON_PMC,
                            "snippet": BGSDM_DISTRIBUTION_SNIPPET,
                            "notes": (
                                "Johnson et al. describe bGSDM-protease "
                                "systems across prokaryotic genomes and "
                                "metagenomes."
                            ),
                        },
                        {
                            "reference": JOHNSON,
                            "snippet": BGSDM_PROTEASE_SNIPPET,
                            "notes": (
                                "Johnson et al. support caspase-like "
                                "proteases as direct activators of "
                                "bacterial gasdermins."
                            ),
                        },
                    ],
                },
                {
                    "subject": "caspase_like_bgsdm_cleavage",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gasdermin_pore_assembly",
                    "description": (
                        "Proteolytic release of the inhibitory bacterial "
                        "gasdermin peptide induces large pore assembly."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON,
                            "snippet": PORE_ASSEMBLY_SNIPPET,
                            "notes": (
                                "Johnson et al. connect release of "
                                "autoinhibition to gasdermin pore assembly."
                            ),
                        },
                        {
                            "reference": JOHNSON_PMC,
                            "snippet": RUNELLA_PROTEASE_SNIPPET,
                            "notes": (
                                "The Runella bGSDM system required both "
                                "bGSDM and its protease to trigger cellular "
                                "toxicity."
                            ),
                        },
                    ],
                },
                {
                    "subject": "gasdermin_pore_assembly",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "membrane_integrity_disruption",
                    "description": (
                        "Activated bacterial gasdermins assemble pores that "
                        "disrupt membrane integrity."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON,
                            "snippet": PORE_ASSEMBLY_SNIPPET,
                            "notes": (
                                "Johnson et al. link bacterial gasdermin "
                                "pore assembly to disrupted membrane "
                                "integrity."
                            ),
                        },
                    ],
                },
                {
                    "subject": "membrane_integrity_disruption",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gasdermin_cell_death",
                    "description": (
                        "Bacterial gasdermin activation can execute cell "
                        "death through loss of membrane integrity."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON,
                            "snippet": BGSDM_DISCOVERY_SNIPPET,
                            "notes": (
                                "Johnson et al. identify bacterial "
                                "gasdermins as phage-defense homologs that "
                                "execute cell death."
                            ),
                        },
                    ],
                },
                {
                    "subject": "gasdermin_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gasdermin_system_trait",
                    "description": (
                        "The GasderMIN DefenseFinder model identifies a "
                        "GasderMIN__bGSDM profile, and Johnson et al. show "
                        "that deleting a bGSDM gene can abolish phage "
                        "protection by a gasdermin operon."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON_PMC,
                            "snippet": LYSOBACTER_DEFENSE_SNIPPET,
                            "notes": (
                                "The tested Lysobacter enzymogenes "
                                "bGSDM-containing operon protected cells "
                                "from coliphage challenge."
                            ),
                        },
                        {
                            "reference": JOHNSON_PMC,
                            "snippet": LYSOBACTER_DELETION_SNIPPET,
                            "notes": (
                                "The bGSDM gene was essential for the "
                                "Lysobacter operon's observed phage "
                                "protection."
                            ),
                        },
                        hmm_inventory_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "gasdermin_cell_death",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "gasdermin_system_trait",
                    "description": (
                        "Bacterial gasdermin-mediated cell death realizes "
                        "the GasderMIN phage-defense-system output in "
                        "tested bGSDM-protease systems."
                    ),
                    "evidence": [
                        {
                            "reference": JOHNSON,
                            "snippet": BGSDM_DISCOVERY_SNIPPET,
                            "notes": (
                                "Johnson et al. connect bacterial gasdermin "
                                "phage defense with cell death."
                            ),
                        },
                    ],
                },
                {
                    "subject": "gasdermin_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "GasderMIN system possession is a bacterial "
                        "gasdermin phage-defense-system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        rules_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "gasdermin-family-breadth-and-card-nlr-scope-gap",
            "prompt": (
                "Resolve natural GasderMIN family breadth and CARD-NLR "
                "gasdermin context before minting narrower gasdermin "
                "subfamily traits."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Johnson et al. experimentally tested a Lysobacter "
                "bGSDM-containing operon and mechanistically dissected "
                "Runella bGSDM protease-triggered toxicity, while some "
                "bacterial gasdermins showed no discernible phage "
                "restriction in Escherichia coli and the GasderMIN__bGSDM "
                "profile is also used in CARD-NLR detector contexts in the "
                "pinned DefenseFinder rules table. This record captures the "
                "standalone GasderMIN detector namespace and leaves "
                "CARD-NLR-associated gasdermins, natural phage triggers, "
                "and broader family boundaries unresolved."
            ),
            "attaches_to": [
                "causal_graphs#gasdermin_proteolysis_triggers_pore_cell_death"
            ],
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
            "Minted GasderMIN system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, history, "
            "or prior proposal record; the replacement placeholder is "
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
