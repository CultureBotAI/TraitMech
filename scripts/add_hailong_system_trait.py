#!/usr/bin/env python3
"""Add the Hailong system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "hailong_system.yaml"

TAN = "DOI:10.1038/s41586-025-09058-z"
CHAN = "DOI:10.1016/j.molcel.2025.06.011"

CURATOR = "codex"
TIMESTAMP = "2026-09-18T13:27:00Z"

RECORD: dict[str, Any] = {
    "identifier": "traitmech:000242",
    "label": "Hailong system",
    "definition": (
        "A phage defense system in which an organism possesses a Hailong "
        "locus encoding a HalB NTase DNA-signal enzyme and a HalA membrane "
        "effector complex that can be held inactive by HalB-derived "
        "oligodeoxyadenylate until viral DNA exonucleases release the primed "
        "HalA complex and induce protective host cell growth arrest."
    ),
    "definition_source": TAN,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "Hailong anti-phage system",
            "synonym_type": "EXACT_SYNONYM",
            "source": CHAN,
        }
    ],
    "evidence": [
        {
            "reference": TAN,
            "snippet": (
                "Here we discover a family of bacterial defence systems, "
                "which we name Hailong, that use NTase enzymes to "
                "constitutively synthesize DNA signals and guard against "
                "phage infection"
            ),
            "notes": (
                "Tan et al. support Hailong as a named NTase-linked "
                "bacterial phage-defense family."
            ),
        },
        {
            "reference": TAN,
            "snippet": (
                "Hailong is a two-gene operon that encodes Hailong protein "
                "A (HalA), a transmembrane protein of unknown function, and "
                "Hailong protein B (HalB), the predicted NTase enzyme"
            ),
            "notes": (
                "Tan et al. support curating the two core Hailong genes as a "
                "complete locus rather than as separate HalA or HalB "
                "protein traits."
            ),
        },
        {
            "reference": TAN,
            "snippet": (
                "Hailong operons are widely conserved in defence islands "
                "across >70 genera of gram-positive and gram-negative "
                "bacteria"
            ),
            "notes": (
                "Tan et al. support placing Hailong at a bacterial system "
                "level rather than curating only the assayed plasmid or "
                "species instances."
            ),
        },
        {
            "reference": TAN,
            "snippet": (
                "Hailong protein B (HalB) is an NTase that converts "
                "deoxy-ATP into single-stranded DNA oligomers"
            ),
            "notes": (
                "Tan et al. identify the HalB NTase signal-synthesis "
                "reaction inside the Hailong system."
            ),
        },
        {
            "reference": TAN,
            "snippet": (
                "We show that HalB DNA signals bind to and repress "
                "activation of a partnering Hailong protein A (HalA) "
                "effector complex"
            ),
            "notes": (
                "Tan et al. support repression of the HalA effector complex "
                "by HalB-derived DNA signals."
            ),
        },
        {
            "reference": TAN,
            "snippet": (
                "viral DNA exonucleases required for phage replication "
                "trigger release of the primed HalA complex and induce "
                "protective host cell growth arrest"
            ),
            "notes": (
                "Tan et al. support the phage-exonuclease trigger and "
                "growth-arrest output captured in the Hailong graph."
            ),
        },
        {
            "reference": CHAN,
            "snippet": (
                "the bacterial Hailong anti-phage system, in which "
                "constitutively synthesized DNA oligonucleotides inhibit a "
                "toxic ion channel-a molecular booby trap primed for "
                "activation by phage exonucleases"
            ),
            "notes": (
                "Kuehn and Pinilla-Redondo summarize Hailong as a bacterial "
                "anti-phage system gated by constitutive inhibitory DNA "
                "oligonucleotide signals."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Tan et al. showed that an Escherichia coli STEC 1178 "
                "Hailong system gave more than 10,000-fold protection "
                "against dsDNA phages in E. coli challenge assays."
            ),
            "reference": TAN,
        },
    ],
    "causal_graphs": [
        {
            "graph_id": "hailong_dna_gated_growth_arrest",
            "title": (
                "Hailong DNA-signal gating couples phage exonuclease "
                "challenge to growth arrest"
            ),
            "description": (
                "Evidence-backed process sketch linking a Hailong locus to "
                "HalB oligodeoxyadenylate signal synthesis, HalA effector "
                "repression, viral DNA exonuclease challenge, HalA channel "
                "activation, and host cell growth arrest."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Tan et al. Hailong "
                "oligodeoxyadenylate-gated phage-exonuclease-response "
                "evidence without asserting one universal ODA-transfer "
                "mechanism, phage trigger, HalA ion specificity, ancillary "
                "gene architecture, or host-processing factor across all "
                "Hailong homologs."
            ),
            "nodes": [
                {
                    "node_id": "hailong_locus",
                    "label": "Hailong locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Hailong phage-defense locus encoding a HalA "
                        "membrane effector and a HalB NTase signal enzyme."
                    ),
                },
                {
                    "node_id": "oda_signal_synthesis",
                    "label": "oligodeoxyadenylate signal synthesis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Constitutive synthesis of single-stranded DNA "
                        "oligodeoxyadenylate signals by the Hailong HalB "
                        "NTase."
                    ),
                },
                {
                    "node_id": "hala_oda_repressed_complex",
                    "label": "HalA-oligodeoxyadenylate repressed complex",
                    "node_type": "STATE",
                    "description": (
                        "A primed, repressed HalA effector complex bound to "
                        "HalB-derived oligodeoxyadenylate."
                    ),
                },
                {
                    "node_id": "phage_exonuclease_challenge",
                    "label": "phage exonuclease challenge",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Viral DNA exonuclease activity encountered during "
                        "phage replication that degrades the Hailong "
                        "inhibitory DNA signal."
                    ),
                },
                {
                    "node_id": "hala_channel_activation",
                    "label": "HalA channel activation",
                    "node_type": "MOLECULAR_FUNCTION",
                    "description": (
                        "Release of Hailong HalA ion-channel effector "
                        "function after inhibitory oligodeoxyadenylate is "
                        "removed."
                    ),
                },
                {
                    "node_id": "host_cell_growth_arrest",
                    "label": "host cell growth arrest",
                    "node_type": "STATE",
                    "description": (
                        "Protective arrest of host-cell growth downstream of "
                        "Hailong HalA effector activation."
                    ),
                },
                {
                    "node_id": "hailong_system_trait",
                    "label": "Hailong system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000242",
                    "description": (
                        "Possession of a genome-encoded Hailong "
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
                    "subject": "hailong_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "oda_signal_synthesis",
                    "description": (
                        "The Hailong locus encodes HalB, an NTase that "
                        "constitutively synthesizes oligodeoxyadenylate DNA "
                        "signals."
                    ),
                    "evidence": [
                        {
                            "reference": TAN,
                            "snippet": (
                                "Hailong protein B (HalB) is an NTase that "
                                "converts deoxy-ATP into single-stranded DNA "
                                "oligomers"
                            ),
                            "notes": (
                                "Tan et al. identify HalB as the "
                                "DNA-signal-synthesizing Hailong NTase."
                            ),
                        }
                    ],
                },
                {
                    "subject": "oda_signal_synthesis",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "hala_oda_repressed_complex",
                    "description": (
                        "HalB-derived DNA signals bind the HalA effector "
                        "complex and hold the complex in a primed, repressed "
                        "state before phage infection."
                    ),
                    "evidence": [
                        {
                            "reference": TAN,
                            "snippet": (
                                "We show that HalB DNA signals bind to and "
                                "repress activation of a partnering Hailong "
                                "protein A (HalA) effector complex"
                            ),
                            "notes": (
                                "Tan et al. support formation of a repressed "
                                "HalA effector complex by HalB-derived DNA "
                                "signals."
                            ),
                        }
                    ],
                },
                {
                    "subject": "hala_oda_repressed_complex",
                    "predicate": "negatively regulates",
                    "predicate_id": "RO:0002212",
                    "object": "hala_channel_activation",
                    "description": (
                        "Oligodeoxyadenylate binding negatively regulates "
                        "HalA channel function by locking the membrane "
                        "effector in an inactive state."
                    ),
                    "evidence": [
                        {
                            "reference": TAN,
                            "snippet": (
                                "These results support that ODA-binding "
                                "negatively regulates HalA channel function"
                            ),
                            "notes": (
                                "Tan et al. directly support negative "
                                "regulation of HalA channel function by ODA "
                                "binding."
                            ),
                        }
                    ],
                },
                {
                    "subject": "phage_exonuclease_challenge",
                    "predicate": "activates",
                    "predicate_id": "RO:0002213",
                    "object": "hala_channel_activation",
                    "description": (
                        "Viral DNA exonucleases degrade the inhibitory "
                        "Hailong signal and trigger release of the primed "
                        "HalA effector complex."
                    ),
                    "evidence": [
                        {
                            "reference": TAN,
                            "snippet": (
                                "viral DNA exonucleases required for phage "
                                "replication trigger release of the primed "
                                "HalA complex"
                            ),
                            "notes": (
                                "Tan et al. support viral DNA exonucleases "
                                "as triggers for release of primed HalA."
                            ),
                        }
                    ],
                },
                {
                    "subject": "hala_channel_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "host_cell_growth_arrest",
                    "description": (
                        "Release of HalA channel effector function links "
                        "phage exonuclease sensing to protective host cell "
                        "growth arrest."
                    ),
                    "evidence": [
                        {
                            "reference": TAN,
                            "snippet": (
                                "degrade ODA and trigger release of HalA "
                                "ion channel effector function"
                            ),
                            "notes": (
                                "Tan et al. connect ODA degradation to "
                                "release of HalA ion-channel effector "
                                "function."
                            ),
                        },
                        {
                            "reference": TAN,
                            "snippet": (
                                "induce protective host cell growth arrest"
                            ),
                            "notes": (
                                "Tan et al. support host cell growth arrest "
                                "as a protective Hailong output after "
                                "phage-exonuclease challenge."
                            ),
                        },
                    ],
                },
                {
                    "subject": "host_cell_growth_arrest",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "hailong_system_trait",
                    "description": (
                        "Hailong-mediated host growth arrest is the "
                        "phage-defense output that realizes the Hailong "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": TAN,
                            "snippet": (
                                "Hailong from the bacterium E. coli STEC "
                                "1178 providing >10,000-fold protection "
                                "against dsDNA phages"
                            ),
                            "notes": (
                                "Tan et al. support Hailong-mediated growth "
                                "arrest as part of a plasmid-borne system "
                                "that protects E. coli against phage "
                                "infection."
                            ),
                        }
                    ],
                },
                {
                    "subject": "hailong_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "Hailong system possession is a phage-defense-system "
                        "trait."
                    ),
                    "evidence": [
                        {
                            "reference": TAN,
                            "snippet": (
                                "Here we discover a family of bacterial "
                                "defence systems, which we name Hailong"
                            ),
                            "notes": (
                                "Tan et al. place Hailong in the bacterial "
                                "phage-defense system family."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "hailong-mechanism-and-family-breadth-gap",
            "prompt": (
                "Resolve Hailong ODA transfer, phage-trigger breadth, HalA "
                "ion specificity, and family architecture before minting "
                "narrower Hailong mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Tan et al. support HalB oligodeoxyadenylate synthesis, HalA "
                "repression by inhibitory DNA signals, and viral "
                "DNA-exonuclease-triggered release of HalA effector function, "
                "but Hailong homologs need separate review before TraitMech "
                "asserts one complete ODA-transfer pathway, phage nuclease "
                "trigger, HalA ion selectivity, host-processing factor, or "
                "ancillary-gene architecture across the full Hailong family."
            ),
            "posed_by": CURATOR,
            "posed_date": "2026-09-18",
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

    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Hailong system as a DOI-backed GENOMICS TraitRecord "
            "under the phage defense system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            "placeholder is reserved in proposals/metpo_traitmech_v119."
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
