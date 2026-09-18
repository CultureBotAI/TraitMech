#!/usr/bin/env python3
"""Add the DarTG system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "dartg_system.yaml"

LEROUX = "DOI:10.1038/s41564-022-01153-5"
PATEL = "DOI:10.1128/mbio.00111-24"

CURATOR = "codex"
TIMESTAMP = "2026-09-18T14:18:08Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000243",
    "label": "DarTG system",
    "definition": (
        "A phage defense system in which an organism possesses a DarTG "
        "toxin-antitoxin locus whose DarT toxin can be released during "
        "bacteriophage infection to ADP-ribosylate viral DNA, block "
        "phage genome replication, and prevent production of mature virions."
    ),
    "definition_source": LEROUX,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "DarTG toxin-antitoxin system",
            "synonym_type": "EXACT_SYNONYM",
            "source": LEROUX,
        }
    ],
    "evidence": [
        {
            "reference": LEROUX,
            "snippet": (
                "Representatives from two different subfamilies, DarTG1 and "
                "DarTG2, strongly protected E. coli MG1655 against different "
                "phages."
            ),
            "notes": (
                "LeRoux et al. support DarTG as a two-subfamily "
                "phage-defense system with experimental activity in "
                "E. coli MG1655 challenge assays."
            ),
        },
        {
            "reference": LEROUX,
            "snippet": (
                "infection with either RB69 or T5 phage, respectively, "
                "triggers release of the DarT toxin, a DNA "
                "ADP-ribosyltransferase, that then modifies viral DNA and "
                "prevents replication, thereby blocking the production of "
                "mature virions"
            ),
            "notes": (
                "LeRoux et al. support the DarT release, viral-DNA "
                "ADP-ribosylation, phage-genome-replication blockade, and "
                "mature-virion-production blockade captured in the "
                "causal graph."
            ),
        },
        {
            "reference": LEROUX,
            "snippet": (
                "Collectively, our results indicate that phage defence may "
                "be a common function for TA systems and reveal the "
                "mechanism by which DarTG systems inhibit phage infection."
            ),
            "notes": (
                "LeRoux et al. support DarTG as an experimentally resolved "
                "toxin-antitoxin phage-defense system."
            ),
        },
        {
            "reference": PATEL,
            "snippet": (
                "we identify clinical isolates of the global pathogen Vibrio "
                "cholerae harboring a novel genetic element encoding the "
                "bacterial immune system DarTG and reveal the immune "
                "system's impact on the co-circulating lytic phage ICP1."
            ),
            "notes": (
                "Patel and Seed independently support DarTG as a bacterial "
                "immune system in V. cholerae clinical isolates and connect "
                "the system to defense against ICP1 phage."
            ),
        },
        {
            "reference": PATEL,
            "snippet": (
                "We show that DarTG inhibits ICP1 genome replication, thus "
                "preventing ICP1 plaquing."
            ),
            "notes": (
                "Patel and Seed support phage-genome-replication blockade "
                "as an output of the V. cholerae DarTG system."
            ),
        },
        {
            "reference": PATEL,
            "snippet": (
                "we probe clinical V. cholerae isolates for novel anti-phage "
                "immune systems that can inhibit ICP1 and discover the "
                "toxin-antitoxin system DarTG as a potent inhibitor."
            ),
            "notes": (
                "Patel and Seed support the DarTG toxin-antitoxin system "
                "as a potent inhibitor of the co-circulating phage ICP1."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:666",
            "taxon_label": "Vibrio cholerae",
            "note": (
                "Patel and Seed characterized a phage defense element "
                "encoding DarTG in 2008-2009 clinical V. cholerae isolates "
                "and showed DarTG was responsible for ICP1 inhibition."
            ),
            "reference": PATEL,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "dartg_dna_adp_ribosylation_defense",
            "title": (
                "DarTG loci couple phage infection to viral-DNA "
                "ADP-ribosylation"
            ),
            "description": (
                "Evidence-backed process sketch linking sensitive phage "
                "infection to DarT toxin release, viral DNA "
                "ADP-ribosylation, inhibition of phage genome replication, "
                "restricted phage propagation, and the DarTG system trait."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures LeRoux and Patel DarTG phage-defense "
                "evidence without claiming a universal phage trigger, DarT "
                "release mechanism, viral target scope, or phage-encoded "
                "anti-DarT factor across all DarTG systems."
            ),
            "nodes": [
                {
                    "node_id": "sensitive_phage_infection",
                    "label": "sensitive phage infection",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Infection by a phage whose propagation can be "
                        "inhibited by an active DarTG system."
                    ),
                },
                {
                    "node_id": "darT_toxin_release",
                    "label": "DarT toxin release",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Release of the DNA ADP-ribosyltransferase DarT "
                        "toxin from inhibition during phage infection."
                    ),
                },
                {
                    "node_id": "viral_dna_adp_ribosylation",
                    "label": "viral DNA ADP-ribosylation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DarT-mediated ADP-ribosylation of bacteriophage "
                        "DNA after DarT is released from antitoxin control."
                    ),
                },
                {
                    "node_id": "inhibited_phage_genome_replication",
                    "label": "inhibited phage genome replication",
                    "node_type": "STATE",
                    "description": (
                        "Reduced or blocked replication of the infecting "
                        "phage genome downstream of DarT activity."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Blocked mature-virion production or plaquing after "
                        "DarTG inhibits the infecting phage."
                    ),
                },
                {
                    "node_id": "dartg_system_trait",
                    "label": "DarTG system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000243",
                    "description": (
                        "Possession of a genome-encoded DarTG "
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
                    "subject": "sensitive_phage_infection",
                    "predicate": "triggers",
                    "object": "darT_toxin_release",
                    "description": (
                        "Infection by RB69 or T5 phage triggers release of "
                        "the DarT toxin in the tested DarTG subfamily systems."
                    ),
                    "evidence": [
                        {
                            "reference": LEROUX,
                            "snippet": (
                                "infection with either RB69 or T5 phage, "
                                "respectively, triggers release of the DarT "
                                "toxin"
                            ),
                            "notes": (
                                "LeRoux et al. identify phage infection as "
                                "the upstream trigger for DarT toxin release."
                            ),
                        }
                    ],
                },
                {
                    "subject": "darT_toxin_release",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "viral_dna_adp_ribosylation",
                    "description": (
                        "Released DarT ADP-ribosylates viral DNA after phage "
                        "infection."
                    ),
                    "evidence": [
                        {
                            "reference": LEROUX,
                            "snippet": (
                                "triggers release of the DarT toxin, a DNA "
                                "ADP-ribosyltransferase, that then modifies "
                                "viral DNA"
                            ),
                            "notes": (
                                "LeRoux et al. support DarT release leading "
                                "to viral-DNA ADP-ribosylation."
                            ),
                        }
                    ],
                },
                {
                    "subject": "viral_dna_adp_ribosylation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "inhibited_phage_genome_replication",
                    "description": (
                        "DarT-dependent viral-DNA modification blocks "
                        "replication of the infecting phage genome."
                    ),
                    "evidence": [
                        {
                            "reference": LEROUX,
                            "snippet": (
                                "then modifies viral DNA and prevents "
                                "replication, thereby blocking the production "
                                "of mature virions"
                            ),
                            "notes": (
                                "LeRoux et al. directly connect viral-DNA "
                                "modification to blocked phage replication."
                            ),
                        },
                        {
                            "reference": PATEL,
                            "snippet": (
                                "We show that DarTG inhibits ICP1 genome "
                                "replication, thus preventing ICP1 plaquing."
                            ),
                            "notes": (
                                "Patel and Seed show that V. cholerae DarTG "
                                "also blocks ICP1 genome replication."
                            ),
                        },
                    ],
                },
                {
                    "subject": "inhibited_phage_genome_replication",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "Inhibition of genome replication restricts mature "
                        "virion production and phage plaquing."
                    ),
                    "evidence": [
                        {
                            "reference": LEROUX,
                            "snippet": (
                                "prevents replication, thereby blocking the "
                                "production of mature virions"
                            ),
                            "notes": (
                                "LeRoux et al. support mature-virion "
                                "blockade as a downstream effect of blocked "
                                "phage replication."
                            ),
                        },
                        {
                            "reference": PATEL,
                            "snippet": (
                                "DarTG inhibits ICP1 genome replication, thus "
                                "preventing ICP1 plaquing"
                            ),
                            "notes": (
                                "Patel and Seed support plaquing prevention "
                                "as a downstream effect of ICP1 "
                                "genome-replication blockade."
                            ),
                        },
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "dartg_system_trait",
                    "description": (
                        "The DarTG system trait is realized by inhibition of "
                        "phage replication and propagation."
                    ),
                    "evidence": [
                        {
                            "reference": LEROUX,
                            "snippet": (
                                "reveal the mechanism by which DarTG systems "
                                "inhibit phage infection"
                            ),
                            "notes": (
                                "LeRoux et al. place the DNA "
                                "ADP-ribosylation mechanism in the broader "
                                "DarTG phage-infection-inhibition trait."
                            ),
                        }
                    ],
                },
                {
                    "subject": "dartg_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "DarTG system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": PATEL,
                            "snippet": (
                                "we probe clinical V. cholerae isolates for "
                                "novel anti-phage immune systems that can "
                                "inhibit ICP1 and discover the "
                                "toxin-antitoxin system DarTG as a potent "
                                "inhibitor."
                            ),
                            "notes": (
                                "Patel and Seed support DarTG as an "
                                "anti-phage immune system."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the new TraitRecord YAML",
    )
    args = parser.parse_args()

    if TARGET.exists():
        raise SystemExit(f"{TARGET.relative_to(REPO_ROOT)} already exists")

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted DarTG system as a DOI-backed GENOMICS TraitRecord "
            "under phage defense system after an ignored-and-hidden "
            "duplicate review found no exact live TraitMech, METPO, or "
            "prior proposal record; the replacement placeholder is "
            "reserved in proposals/metpo_traitmech_v120."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )

    rel = TARGET.relative_to(REPO_ROOT)
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {rel}")
    else:
        print(f"would write {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
