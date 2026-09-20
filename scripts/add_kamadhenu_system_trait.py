#!/usr/bin/env python3
"""Add the Kamadhenu system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "kamadhenu_system.yaml"

GRAFAKOU = "DOI:10.1093/nar/gkae671"
MOSTERD = "DOI:10.1073/pnas.2426508122"

GRAFAKOU_DISCOVERY_SNIPPET = (
    "These systems were named after cheese, cattle or fermentation related "
    "deities (Rhea, Aristaios, Kamadhenu, Fliodhais, Audmula, Rugutis and "
    "Hesat)"
)
MOSTERD_ESCAPE_SNIPPET = (
    "we isolated 66 phage escape mutants which had become insensitive to 13 "
    "distinct, plasmid-encoded lactococcal phage resistance systems (i.e. "
    "Rhea, Kamadhenu, Rugutis, Audmula, PARIS, type II CBASS, Septu, AbiA, "
    "AbiB, AbiD/F, AbiG, AbiJ, AbiP)"
)

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_ARTICLES = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/List_system_article.md"
)

CURATOR = "codex"
TIMESTAMP = "2026-09-20T13:47:53Z"

IDENTIFIER = "traitmech:000310"
PROPOSAL = "proposals/metpo_traitmech_v187"
SYSTEM = "Kamadhenu"
SLUG = "kamadhenu"


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Kamadhenu | 10\\.1093/nar/gkae671 | Discovery of antiphage "
            "systems in the lactococcal plasmidome"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Kamadhenu "
            "system to the Grafakou et al. lactococcal antiphage-system "
            "discovery paper."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Kamadhenu system",
    "definition": (
        "A phage defense system in which an organism possesses a Kamadhenu "
        "locus that can restrict bacteriophage infection."
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
                "Grafakou et al. named Kamadhenu among seven not previously "
                "described lactococcal antiphage systems."
            ),
        },
        {
            "reference": MOSTERD,
            "snippet": MOSTERD_ESCAPE_SNIPPET,
            "notes": (
                "Mosterd et al. later included Kamadhenu among the distinct "
                "plasmid-encoded lactococcal phage-resistance systems "
                "investigated by phage escape-mutant isolation."
            ),
        },
        article_registry_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": f"{SLUG}_locus_restricts_phage",
            "title": "Kamadhenu loci confer bacterial phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Kamadhenu locus to restricted bacteriophage propagation "
                "without asserting the unresolved phage trigger or molecular "
                "output."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Kamadhenu as a named lactococcal "
                "anti-phage system while leaving its direct phage trigger, "
                "molecular substrate, antiviral effector output, natural "
                "locus breadth, and the absence of pinned DefenseFinder HMM "
                "or rule rows unresolved."
            ),
            "nodes": [
                {
                    "node_id": f"{SLUG}_locus",
                    "label": "Kamadhenu locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Kamadhenu anti-phage defense locus described among "
                        "lactococcal plasmid-encoded phage-resistance systems."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced propagation of bacteriophage in cells carrying "
                        "the Kamadhenu system."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "Kamadhenu system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Kamadhenu phage-defense "
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
                        "The lactococcal plasmidome screen discovered "
                        "Kamadhenu as a named antiphage system, and the "
                        "DefenseFinder article registry maps the Kamadhenu "
                        "system to that discovery paper."
                    ),
                    "evidence": [
                        {
                            "reference": GRAFAKOU,
                            "snippet": GRAFAKOU_DISCOVERY_SNIPPET,
                            "notes": (
                                "Grafakou et al. named Kamadhenu as one of "
                                "the novel lactococcal antiphage systems."
                            ),
                        },
                        {
                            "reference": MOSTERD,
                            "snippet": MOSTERD_ESCAPE_SNIPPET,
                            "notes": (
                                "Mosterd et al. treat Kamadhenu as a "
                                "plasmid-encoded lactococcal phage-resistance "
                                "system in their escape-mutant screen."
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
                        "Kamadhenu-mediated phage restriction realizes the "
                        "Kamadhenu system trait."
                    ),
                    "evidence": [
                        {
                            "reference": MOSTERD,
                            "snippet": MOSTERD_ESCAPE_SNIPPET,
                            "notes": (
                                "Mosterd et al. treat Kamadhenu as a "
                                "plasmid-encoded lactococcal phage-resistance "
                                "system in their escape-mutant screen."
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
                        "Kamadhenu system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [article_registry_evidence()],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "kamadhenu-mechanism-gap",
            "prompt": (
                "Resolve Kamadhenu phage triggers and effector outputs before "
                "minting narrower Kamadhenu mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Grafakou et al., Mosterd et al., and DefenseFinder support "
                "Kamadhenu as a named anti-phage system, but the direct "
                "trigger, molecular substrate, antiviral effector output, "
                "natural locus breadth, and profile-to-component model are not "
                "resolved enough here to assert a narrower mechanistic child "
                "trait."
            ),
            "attaches_to": [f"causal_graphs#{SLUG}_locus_restricts_phage"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help=f"write {TARGET.relative_to(REPO_ROOT)}")
    args = parser.parse_args()

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Kamadhenu system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden duplicate "
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
