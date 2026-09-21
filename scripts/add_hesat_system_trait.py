#!/usr/bin/env python3
"""Add the Hesat system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hesat_system.yaml"

GRAFAKOU = "DOI:10.1093/nar/gkae671"

GRAFAKOU_DISCOVERY_SNIPPET = (
    "Based on comparative sequence analysis (BLASTN and BLASTP) and on "
    "functional and structural analysis (HHpred and InterPro) the remaining "
    "seven antiphage systems (out of the twenty identified) did not display "
    "significant homology to any previously described antiphage system, thus "
    "rendering them novel antiphage systems (Table 1). These systems were "
    "named after cheese, cattle or fermentation related deities (Rhea, "
    "Aristaios, Kamadhenu, Fliodhais, Audmula, Rugutis and Hesat)"
)
GRAFAKOU_SINGLE_GENE_SNIPPET = (
    "Except for Hesat, which was cloned in pPTPi with the addition of its "
    "native signals, all novel systems were cloned in the high-copy number "
    "vector pNZ44 (Supplementary Table S2). All discovered systems, except "
    "Fliodhais, are single gene antiphage systems."
)
GRAFAKOU_STRUCTURE_SNIPPET = (
    "For Hesat, no domain was predicted by HHpred and InterPro. Dali analysis "
    "reports significant hits with the colicin-D toxic domain (PDB ID 1V74; "
    "Figure 4N, O), which specifically cleaves the anticodon loop of all four "
    "tRNA(Arg) iso-acceptors, thereby resulting in cell death (68). Therefore, "
    "it is proposed that Hesat upon phage infection is activated to block "
    "translation, which is in accordance with its abortive infection phenotype."
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-21T04:55:54Z"

IDENTIFIER = "traitmech:000327"
PROPOSAL = "proposals/metpo_traitmech_v204"
SYSTEM = "Hesat"
SLUG = "hesat"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Hesat | 10\\.1093/nar/gkae671 | Discovery of antiphage "
            "systems in the lactococcal plasmidome"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Hesat "
            "system to the Grafakou et al. lactococcal antiphage-system "
            "discovery paper."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Hesat system",
    "definition": (
        "A phage defense system in which an organism possesses a Hesat locus "
        "that can restrict bacteriophage infection."
    ),
    "definition_source": GRAFAKOU,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": SYSTEM,
            "synonym_type": "EXACT_SYNONYM",
            "source": GRAFAKOU,
        }
    ],
    "evidence": [
        {
            "reference": GRAFAKOU,
            "snippet": GRAFAKOU_DISCOVERY_SNIPPET,
            "notes": (
                "Grafakou et al. named Hesat among seven not previously "
                "described lactococcal antiphage systems."
            ),
        },
        {
            "reference": GRAFAKOU,
            "snippet": GRAFAKOU_SINGLE_GENE_SNIPPET,
            "notes": (
                "Grafakou et al. identify Hesat as a single-gene novel "
                "antiphage system cloned with native signals in pPTPi."
            ),
        },
        {
            "reference": GRAFAKOU,
            "snippet": GRAFAKOU_STRUCTURE_SNIPPET,
            "notes": (
                "Grafakou et al. report that Hesat had no HHpred or InterPro "
                "domain prediction, and they propose a colicin-D-like "
                "translation-blocking activity upon phage infection."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Hesat loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Hesat locus to restricted bacteriophage propagation without "
                "asserting the unresolved phage trigger or molecular output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Hesat as a named single-gene lactococcal "
                "anti-phage system while leaving its direct phage trigger, "
                "molecular substrate, experimentally validated antiviral "
                "effector output, natural locus breadth, and the absence of "
                "pinned DefenseFinder HMM or rule rows unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Hesat locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A single-gene Hesat anti-phage defense locus "
                        "described among lactococcal plasmid-encoded "
                        "phage-resistance systems."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells "
                        "carrying the Hesat system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Hesat system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Hesat phage-defense "
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
                    "subject": f"{SLUG}_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The lactococcal plasmidome screen discovered Hesat "
                        "as a named single-gene antiphage system, and the "
                        "DefenseFinder article registry maps the Hesat system "
                        "to that discovery paper."
                    ),
                    "evidence": [
                        {
                            "reference": GRAFAKOU,
                            "snippet": GRAFAKOU_DISCOVERY_SNIPPET,
                            "notes": (
                                "Grafakou et al. named Hesat as one of the "
                                "novel lactococcal antiphage systems."
                            ),
                        },
                        {
                            "reference": GRAFAKOU,
                            "snippet": GRAFAKOU_SINGLE_GENE_SNIPPET,
                            "notes": (
                                "Grafakou et al. identify Hesat as a "
                                "single-gene antiphage system."
                            ),
                        },
                        {
                            "reference": GRAFAKOU,
                            "snippet": GRAFAKOU_STRUCTURE_SNIPPET,
                            "notes": (
                                "Grafakou et al. propose that Hesat blocks "
                                "translation after phage infection while "
                                "leaving that molecular output unresolved."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "Hesat-mediated phage restriction realizes the Hesat "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": GRAFAKOU,
                            "snippet": GRAFAKOU_STRUCTURE_SNIPPET,
                            "notes": (
                                "Grafakou et al. treat Hesat as having an "
                                "abortive infection phenotype and propose a "
                                "translation-blocking mechanism upon phage "
                                "infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Hesat system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [article_registry_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "hesat-mechanism-gap",
            "prompt": (
                "Resolve Hesat phage triggers and effector outputs before "
                "minting narrower Hesat mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Grafakou et al. and DefenseFinder support Hesat as a named "
                "single-gene anti-phage system, but the direct trigger, "
                "experimentally validated molecular substrate, antiviral "
                "effector output, natural locus breadth, and "
                "profile-to-component model are not resolved enough here to "
                "assert a narrower mechanistic child trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
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
            "Minted Hesat system as a DOI-backed GENOMICS TraitRecord under "
            "phage defense system after an ignored-and-hidden duplicate "
            "review found no exact live TraitMech, METPO, history, or prior "
            f"proposal record; the replacement placeholder is reserved in {PROPOSAL}."
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
