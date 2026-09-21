#!/usr/bin/env python3
"""Add the NixI system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "nixi_system.yaml"

LEGAULT = "DOI:10.1093/nar/gkac002"
DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

NIXI_BLOCKS_SNIPPET = (
    "Here, we characterize a PLE-encoded nuclease, NixI, that blocks phage "
    "development likely by nicking ICP1’s genome as it transitions to RCR"
)
NIXI_CLEAVAGE_SNIPPET = (
    "Together, these data show that PLE encodes a nicking endonuclease, "
    "NixI, that is necessary for cleavage of ICP1’s genome in vivo and "
    "that shows in vitro specificity for sequences found in ICP1’s genome"
)
NIXI_PROGENY_SNIPPET = (
    "NixI, however, is sufficient to limit ICP1 progeny production in a "
    "single round of infection"
)
NIXI_REPLICATION_SNIPPET = (
    "Together, these data demonstrate that nixI is a potent inhibitor of "
    "ICP1 replication, resulting in decreased virion production."
)
NIXI_HOST_DEFENSE_SNIPPET = (
    "Phage parasites can be considered host defense systems, as the "
    "parasite inhibits production of its viral host, benefiting the "
    "bacterial population"
)

HMM_ROW = (
    "| NixI__NixI                                       | "
    "NixI__NixI                                       | NixI                   | "
    "Custom                  | 20     |"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T10:01:24Z"

IDENTIFIER = "traitmech:000333"
PROPOSAL = "proposals/metpo_traitmech_v210"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "NixI | 10\\.1101/2021\\.07\\.12\\.452122 | A phage parasite "
            "deploys a nicking nuclease effector to inhibit replication of "
            "its viral host"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named NixI model "
            "namespace to the LeGault et al. PLE-encoded nicking-nuclease "
            "preprint, later published under DOI:10.1093/nar/gkac002."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "NixI\tNixI\t1\t1\tNixI__NixI\tNixI__Stix\t\t",
        "notes": (
            "The DefenseFinder rules table models NixI with the NixI__NixI "
            "profile as its mandatory component and an optional NixI__Stix "
            "profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records NixI__NixI under the "
            "NixI model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "NixI system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "NixI-family phage-satellite locus represented by the DefenseFinder "
        "NixI__NixI profile and exemplified by a PLE-encoded nicking "
        "endonuclease that cleaves ICP1 bacteriophage DNA, inhibits ICP1 "
        "genome replication, and reduces progeny production in Vibrio "
        "cholerae."
    ),
    "definition_source": LEGAULT,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "NixI",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": LEGAULT,
            "snippet": NIXI_BLOCKS_SNIPPET,
            "notes": (
                "LeGault et al. characterize NixI as a PLE-encoded nuclease "
                "that likely blocks ICP1 development by nicking the ICP1 "
                "genome as it transitions to rolling-circle replication."
            ),
        },
        {
            "reference": LEGAULT,
            "snippet": NIXI_CLEAVAGE_SNIPPET,
            "notes": (
                "LeGault et al. show that NixI is a PLE-encoded nicking "
                "endonuclease necessary for in vivo ICP1 cleavage and "
                "specific for ICP1-derived sequences in vitro."
            ),
        },
        {
            "reference": LEGAULT,
            "snippet": NIXI_PROGENY_SNIPPET,
            "notes": (
                "LeGault et al. support NixI as a PLE-encoded product "
                "sufficient to limit ICP1 progeny production in a single "
                "infection round."
            ),
        },
        {
            "reference": LEGAULT,
            "snippet": NIXI_REPLICATION_SNIPPET,
            "notes": (
                "LeGault et al. support NixI as a potent inhibitor of ICP1 "
                "genome replication, resulting in decreased virion "
                "production."
            ),
        },
        {
            "reference": LEGAULT,
            "snippet": NIXI_HOST_DEFENSE_SNIPPET,
            "notes": (
                "LeGault et al. explicitly frame PLE-like phage parasites "
                "as host defense systems because they inhibit production of "
                "their viral hosts."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:666",
            "taxon_label": "Vibrio cholerae",
            "note": (
                "LeGault et al. used PLE-positive Vibrio cholerae to show "
                "that NixI-dependent cleavage sites appear in ICP1 during "
                "infection and that nixI inhibits ICP1 replication and "
                "progeny production."
            ),
            "reference": LEGAULT,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "nixi_locus_inhibits_icp1_replication",
            "title": "NixI loci inhibit ICP1 replication",
            "description": (
                "Conservative system-level sketch linking a NixI-family "
                "phage-satellite locus to ICP1 genome cleavage, ICP1 "
                "replication inhibition, and the NixI system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures NixI as a named DefenseFinder "
                "single-mandatory-profile system without asserting the "
                "exact satellite self-protection mechanism, the complete "
                "set of PLE-encoded anti-ICP1 mechanisms, the "
                "accession-level natural-host protein, the full functional "
                "breadth of divergent NixI homologs, or the experimental "
                "scope of the optional NixI__Stix profile."
            ),
            "nodes": [
                {
                    "node_id": "nixi_locus",
                    "label": "NixI locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A NixI-family phage-satellite locus represented by "
                        "the DefenseFinder NixI__NixI profile."
                    ),
                },
                {
                    "node_id": "icp1_genome_cleavage",
                    "label": "ICP1 genome cleavage",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "NixI-dependent cleavage of the ICP1 bacteriophage "
                        "genome in PLE-positive Vibrio cholerae."
                    ),
                },
                {
                    "node_id": "icp1_replication_inhibition",
                    "label": "ICP1 replication inhibition",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Inhibition of ICP1 genome replication and progeny "
                        "production by NixI."
                    ),
                },
                {
                    "node_id": "nixi_system_trait",
                    "label": "NixI system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded NixI phage-defense "
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
                    "subject": "nixi_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "icp1_genome_cleavage",
                    "description": (
                        "The PLE-encoded NixI nicking endonuclease is "
                        "necessary for cleavage of ICP1 DNA in vivo, and "
                        "DefenseFinder models NixI with the mandatory "
                        "NixI__NixI profile."
                    ),
                    "evidence": [
                        {
                            "reference": LEGAULT,
                            "snippet": NIXI_CLEAVAGE_SNIPPET,
                            "notes": (
                                "LeGault et al. support NixI as the "
                                "PLE-encoded nicking endonuclease "
                                "responsible for ICP1 genome cleavage."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "nixi_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "icp1_replication_inhibition",
                    "description": (
                        "NixI inhibits ICP1 replication and decreases ICP1 "
                        "virion production."
                    ),
                    "evidence": [
                        {
                            "reference": LEGAULT,
                            "snippet": NIXI_REPLICATION_SNIPPET,
                            "notes": (
                                "LeGault et al. show that NixI is a potent "
                                "inhibitor of ICP1 replication."
                            ),
                        },
                        {
                            "reference": LEGAULT,
                            "snippet": NIXI_PROGENY_SNIPPET,
                            "notes": (
                                "LeGault et al. show that NixI is "
                                "sufficient to limit ICP1 progeny production."
                            ),
                        },
                    ],
                },
                {
                    "subject": "icp1_replication_inhibition",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "nixi_system_trait",
                    "description": (
                        "NixI-dependent ICP1 replication inhibition "
                        "realizes the NixI system trait."
                    ),
                    "evidence": [
                        {
                            "reference": LEGAULT,
                            "snippet": NIXI_BLOCKS_SNIPPET,
                            "notes": (
                                "LeGault et al. characterize NixI as a "
                                "PLE-encoded nuclease blocking ICP1 phage "
                                "development."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "nixi_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "NixI system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": LEGAULT,
                            "snippet": NIXI_HOST_DEFENSE_SNIPPET,
                            "notes": (
                                "LeGault et al. place phage parasites such "
                                "as NixI-encoding PLE among host defense "
                                "systems because they inhibit their viral "
                                "hosts."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "nixi-stix-and-satellite-scope-gap",
            "prompt": (
                "Resolve NixI satellite self-protection, optional Stix "
                "profile scope, natural-host protein accessions, and "
                "divergent-homolog activity before minting narrower NixI "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "LeGault et al. support NixI as a PLE-encoded nicking "
                "endonuclease that cleaves ICP1 DNA and inhibits ICP1 "
                "genome replication, and DefenseFinder models NixI with a "
                "required NixI__NixI profile plus optional NixI__Stix. This "
                "first system-level record leaves the exact PLE "
                "self-protection mechanism, the optional Stix profile's "
                "experimental scope, the accession-level PLE1 NixI protein, "
                "the breadth of divergent homolog activity, and additional "
                "PLE anti-ICP1 mechanisms unresolved."
            ),
            "attaches_to": ["causal_graphs#nixi_locus_inhibits_icp1_replication"],
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
            "Minted NixI system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            "proposal record; the replacement placeholder is reserved in "
            f"{PROPOSAL}."
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
