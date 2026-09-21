#!/usr/bin/env python3
"""Add the CmdTAC system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "cmdtac_system.yaml"

GOESSWEIN = "DOI:10.1038/s41586-024-08102-8"
GOESSWEIN_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC11618068/"

CMDTAC_DEFENSE_SNIPPET = (
    "Here we characterize the widely distributed anti-phage defence system "
    "CmdTAC, which provides robust defence against infection by the T-even "
    "family of phages"
)
CMDC_CAPSID_SNIPPET = (
    "CmdC detects infection by sensing viral capsid proteins, ultimately "
    "leading to the activation of a toxic ADP-ribosyltransferase effector "
    "protein, CmdT"
)
CAPSID_DISSOCIATION_SNIPPET = (
    "newly synthesized capsid protein triggers dissociation of the chaperone "
    "CmdC from the CmdTAC complex, leading to destabilization and degradation "
    "of the antitoxin CmdA"
)
CMDT_MRNA_SNIPPET = (
    "CmdT modifies the N6 position of adenine in GA dinucleotides within "
    "single-stranded RNAs, leading to arrest of mRNA translation and "
    "inhibition of viral replication"
)
ECOR22_DISCOVERY_SNIPPET = (
    "was discovered in the genome of the wild E. coli isolate ECOR22 "
    "through a functional genetic screen for anti-phage defence systems"
)
ABI_SNIPPET = (
    "These results are consistent with CmdTAC functioning via an Abi mechanism."
)
CMDT_COMPLEX_SNIPPET = "CmdT co-precipitated with both CmdA and CmdC"
TRANSLATION_ARREST_SNIPPET = (
    "CmdT selectively modifies mRNA to block translation and abort the phage "
    "infection"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T12:03:24Z"

IDENTIFIER = "traitmech:000335"
PROPOSAL = "proposals/metpo_traitmech_v212"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "CmdTAC | 10\\.1038/s41586-024-08102-8 | Anti-viral defence "
            "by an mRNA ADP-ribosyltransferase that blocks translation"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named CmdTAC "
            "system to the Goesswein et al. CmdTAC mechanism paper; the "
            "pinned DefenseFinder HMM inventory and rules table do not "
            "list CmdTAC, so this row is name-to-paper evidence rather "
            "than model-component evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "CmdTAC system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "cmdTAC toxin-antitoxin-chaperone locus encoding a CmdT "
        "ADP-ribosyltransferase, a CmdA antitoxin, and a CmdC "
        "SecB-like chaperone that can sense viral capsid proteins, "
        "liberate CmdT, modify messenger RNA, and arrest translation to "
        "inhibit bacteriophage replication."
    ),
    "definition_source": GOESSWEIN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "CmdTAC",
            "synonym_type": "EXACT_SYNONYM",
            "source": GOESSWEIN,
        },
        {
            "synonym_text": "cmdTAC",
            "synonym_type": "EXACT_SYNONYM",
            "source": GOESSWEIN_PMC,
        },
    ],
    "evidence": [
        {
            "reference": GOESSWEIN_PMC,
            "snippet": CMDTAC_DEFENSE_SNIPPET,
            "notes": (
                "Goesswein et al. name CmdTAC as a widely distributed "
                "anti-phage defense system that protects against T-even "
                "phages."
            ),
        },
        {
            "reference": GOESSWEIN_PMC,
            "snippet": ECOR22_DISCOVERY_SNIPPET,
            "notes": (
                "Goesswein et al. trace the CmdTAC system to a functional "
                "anti-phage defense screen of Escherichia coli ECOR22."
            ),
        },
        {
            "reference": GOESSWEIN_PMC,
            "snippet": CMDC_CAPSID_SNIPPET,
            "notes": (
                "CmdC senses phage infection through viral capsid proteins "
                "and activates the CmdT ADP-ribosyltransferase effector."
            ),
        },
        {
            "reference": GOESSWEIN_PMC,
            "snippet": CAPSID_DISSOCIATION_SNIPPET,
            "notes": (
                "Newly synthesized phage capsid protein can dissociate the "
                "CmdC chaperone from the complex and destabilize CmdA."
            ),
        },
        {
            "reference": GOESSWEIN_PMC,
            "snippet": CMDT_MRNA_SNIPPET,
            "notes": (
                "Goesswein et al. support CmdT modification of "
                "single-stranded RNA as the translation-arresting "
                "antiphage effector output."
            ),
        },
        {
            "reference": GOESSWEIN_PMC,
            "snippet": ABI_SNIPPET,
            "notes": (
                "Goesswein et al. interpret the low-MOI protection and "
                "center-of-infection results as consistent with an "
                "abortive-infection mechanism."
            ),
        },
        article_registry_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Goesswein et al. report that cmdTAC was discovered in "
                "wild Escherichia coli isolate ECOR22 through a functional "
                "anti-phage defense screen."
            ),
            "reference": GOESSWEIN,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "cmdtac_mrna_adp_ribosylation_aborts_phage",
            "title": "CmdTAC activation blocks phage translation",
            "description": (
                "Conservative system-level sketch linking a CmdTAC locus "
                "to CmdC capsid sensing, CmdA degradation, CmdT-mediated "
                "mRNA modification, translation arrest, and abortive "
                "phage defense."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures CmdTAC as a named toxin-antitoxin-"
                "chaperone abortive-infection system from Escherichia "
                "coli ECOR22 while leaving phage specificity beyond "
                "Tevenvirinae, escape routes, natural family breadth, and "
                "the absence of pinned DefenseFinder HMM or rule rows "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "cmdtac_locus",
                    "label": "cmdTAC locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A toxin-antitoxin-chaperone locus encoding CmdT, "
                        "CmdA, and CmdC anti-phage defense components."
                    ),
                },
                {
                    "node_id": "cmdc_capsid_sensing",
                    "label": "CmdC viral capsid sensing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Detection of newly synthesized viral capsid "
                        "protein through CmdC."
                    ),
                },
                {
                    "node_id": "cmda_degradation",
                    "label": "CmdA antitoxin degradation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Destabilization and degradation of the CmdA "
                        "antitoxin after phage-triggered chaperone "
                        "dissociation."
                    ),
                },
                {
                    "node_id": "cmdt_mrna_adp_ribosylation",
                    "label": "CmdT mRNA ADP-ribosylation",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "ADP-ribosyltransferase activity by liberated CmdT "
                        "against single-stranded mRNA."
                    ),
                },
                {
                    "node_id": "mrna_translation_arrest",
                    "label": "mRNA translation arrest",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Arrest of mRNA translation after CmdT-mediated "
                        "messenger-RNA modification."
                    ),
                },
                {
                    "node_id": "cmdtac_system_trait",
                    "label": "CmdTAC system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded CmdTAC "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "cmdtac_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "cmdc_capsid_sensing",
                    "description": (
                        "The cmdTAC locus encodes CmdC, which can sense "
                        "viral capsid proteins."
                    ),
                    "evidence": [
                        {
                            "reference": GOESSWEIN_PMC,
                            "snippet": (
                                "CmdC detects infection by sensing viral "
                                "capsid proteins"
                            ),
                            "notes": (
                                "Goesswein et al. connect CmdC to viral "
                                "capsid protein sensing."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "cmdc_capsid_sensing",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "cmda_degradation",
                    "description": (
                        "Newly synthesized capsid protein can trigger "
                        "CmdC dissociation from CmdTAC and destabilize the "
                        "CmdA antitoxin."
                    ),
                    "evidence": [
                        {
                            "reference": GOESSWEIN_PMC,
                            "snippet": (
                                "newly synthesized capsid protein triggers "
                                "dissociation of the chaperone CmdC from "
                                "the CmdTAC complex"
                            ),
                            "notes": (
                                "Goesswein et al. place phage capsid-driven "
                                "CmdC dissociation upstream of antitoxin "
                                "destabilization."
                            ),
                        }
                    ],
                },
                {
                    "subject": "cmda_degradation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "cmdt_mrna_adp_ribosylation",
                    "description": (
                        "CmdC dissociation and CmdA degradation liberate "
                        "the CmdT ADP-ribosyltransferase."
                    ),
                    "evidence": [
                        {
                            "reference": GOESSWEIN_PMC,
                            "snippet": (
                                "destabilization and degradation of the "
                                "antitoxin CmdA, with consequent liberation "
                                "of the CmdT ADP-ribosyltransferase"
                            ),
                            "notes": (
                                "Goesswein et al. place CmdA degradation "
                                "upstream of CmdT liberation."
                            ),
                        },
                        {
                            "reference": GOESSWEIN_PMC,
                            "snippet": CMDT_COMPLEX_SNIPPET,
                            "notes": (
                                "CmdT co-precipitated with both its "
                                "antitoxin and chaperone partners."
                            ),
                        },
                    ],
                },
                {
                    "subject": "cmdt_mrna_adp_ribosylation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "mrna_translation_arrest",
                    "description": (
                        "Liberated CmdT modifies mRNA and blocks "
                        "translation."
                    ),
                    "evidence": [
                        {
                            "reference": GOESSWEIN_PMC,
                            "snippet": TRANSLATION_ARREST_SNIPPET,
                            "notes": (
                                "Goesswein et al. connect CmdT-mediated "
                                "mRNA modification to translation arrest."
                            ),
                        }
                    ],
                },
                {
                    "subject": "mrna_translation_arrest",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "cmdtac_system_trait",
                    "description": (
                        "Translation arrest and viral-replication "
                        "inhibition realize the CmdTAC system trait."
                    ),
                    "evidence": [
                        {
                            "reference": GOESSWEIN_PMC,
                            "snippet": (
                                "arrest of mRNA translation and inhibition "
                                "of viral replication"
                            ),
                            "notes": (
                                "Goesswein et al. connect CmdT-mediated "
                                "mRNA modification to inhibited viral "
                                "replication."
                            ),
                        }
                    ],
                },
                {
                    "subject": "cmdtac_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "CmdTAC system possession is an abortive-infection "
                        "phage-defense-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": GOESSWEIN_PMC,
                            "snippet": ABI_SNIPPET,
                            "notes": (
                                "Goesswein et al. interpret CmdTAC as "
                                "consistent with an abortive-infection "
                                "mechanism."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "cmdtac-family-and-model-coverage-gap",
            "prompt": (
                "Resolve CmdTAC family breadth, phage escape routes, and "
                "DefenseFinder model coverage before minting narrower "
                "CmdTAC mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Goesswein et al. support CmdTAC as a "
                "toxin-antitoxin-chaperone abortive-infection system in "
                "which CmdC senses viral capsid proteins and liberates the "
                "CmdT mRNA ADP-ribosyltransferase. The current "
                "DefenseFinder snapshot lists CmdTAC in the article "
                "registry but not in the pinned HMM inventory or rules "
                "table, so this record leaves model-component coverage, "
                "phage specificity beyond Tevenvirinae, escape routes, and "
                "natural family breadth unresolved."
            ),
            "attaches_to": [
                "causal_graphs#cmdtac_mrna_adp_ribosylation_aborts_phage"
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
            "Minted CmdTAC system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
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
