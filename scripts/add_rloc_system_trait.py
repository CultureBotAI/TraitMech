#!/usr/bin/env python3
"""Add the RloC system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "rloc_system.yaml"

DAVIDOV = "DOI:10.1111/j.1365-2958.2008.06387.x"
DAVIDOV_PMID = "PMID:18681940"
RLOC_TRNASE_SNIPPET = (
    "The conserved bacterial protein RloC, a distant homologue of the "
    "tRNA(Lys) anticodon nuclease (ACNase) PrrC, is shown here to act as a "
    "wobble nucleotide-excising and Zn(++)-responsive tRNase."
)
RLOC_WOBBLE_EXCISION_SNIPPET = (
    "Geobacillus kaustophilus RloC expressed in Escherichia coli exhibited "
    "ACNase activity that differed from PrrC's in substrate preference and "
    "ability to excise the wobble nucleotide."
)

BITTON = "DOI:10.1111/mmi.13074"
BITTON_PMID = "PMID:26031711"
DNA_BREAK_SWITCH_SNIPPET = (
    "In contrast, RloC is rarely linked to an RM protein, and its ACNase is "
    "regulated by an internal switch responsive to double-stranded DNA breaks."
)
T4_ACTIVATION_SNIPPET = (
    "Consistent with these predictions we show that Acinetobacter baylyi RloC "
    "expressed in Escherichia coli is activated by wild-type phage T4 but not "
    "by a mutant impaired in host DNA degradation."
)
T4_RESTRICTION_SNIPPET = (
    "Nonetheless, T4's plating efficiency was inefficiently impaired by "
    "AbaRloC, presumably due to a decoy function of the phage encoded tRNA "
    "target, the absence of which exacerbated the restriction."
)
NATURAL_ROLE_GAP_SNIPPET = (
    "The natural role of the conserved bacterial anticodon nuclease (ACNase) "
    "RloC is not known, but traits that set it apart from the homologous phage "
    "T4-excluding ACNase PrrC could provide relevant clues."
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
TIMESTAMP = "2026-09-22T13:03:00Z"
CANONICAL_REVIEW_TIMESTAMP = "2026-09-22T13:03:01Z"
IDENTIFIER = "traitmech:000366"
PROPOSAL = "proposals/metpo_traitmech_v243"
SLUG = "rloc"

ARTICLE_REGISTRY_SNIPPET = (
    "RloC | 10\\.1111/j\\.1365-2958\\.2008\\.06387\\.x | RloC: a wobble "
    "nucleotide-excising and zinc-responsive bacterial tRNase"
)
RULES_SNIPPET = "RloC\tRloC\t1\t1\tRloC__RloC\t\t\t"
HMM_ROWS = {
    "RloC__RloC": (
        "| RloC__RloC                                       | "
        "RloC__RloC                                       | "
        "RloC                   | Custom                  | 120    |"
    ),
}


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_REGISTRY_SNIPPET,
        "notes": (
            "The DefenseFinder article registry maps the named RloC system to "
            "Davidov and Kaufmann's wobble nucleotide-excising tRNase paper."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_SNIPPET,
        "notes": (
            "The DefenseFinder rules table models RloC as a one-profile "
            "system requiring the RloC__RloC profile."
        ),
    }


def hmm_evidence(profile: str) -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROWS[profile],
        "notes": f"The DefenseFinder HMM inventory records {profile} under RloC.",
    }


def all_hmm_evidence() -> list[dict[str, str]]:
    return [hmm_evidence(profile) for profile in HMM_ROWS]


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "RloC system",
    "definition": (
        "A phage defense system in which an organism possesses a "
        "genome-encoded RloC locus represented by DefenseFinder as a "
        "one-profile model requiring RloC__RloC."
    ),
    "definition_source": DAVIDOV,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000209"],
    "synonyms": [
        {
            "synonym_text": "RloC",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        },
        *[
            {
                "synonym_text": profile,
                "synonym_type": "RELATED_SYNONYM",
                "source": DEFENSEFINDER_HMMS,
            }
            for profile in HMM_ROWS
        ],
    ],
    "evidence": [
        {
            "reference": DAVIDOV_PMID,
            "snippet": RLOC_TRNASE_SNIPPET,
            "notes": (
                "Davidov and Kaufmann identify RloC as a conserved bacterial "
                "wobble nucleotide-excising, zinc-responsive tRNase related "
                "to PrrC."
            ),
        },
        {
            "reference": DAVIDOV_PMID,
            "snippet": RLOC_WOBBLE_EXCISION_SNIPPET,
            "notes": (
                "Davidov and Kaufmann support wobble nucleotide excision by "
                "Geobacillus kaustophilus RloC expressed in Escherichia coli."
            ),
        },
        {
            "reference": BITTON_PMID,
            "snippet": DNA_BREAK_SWITCH_SNIPPET,
            "notes": (
                "Bitton et al. describe RloC ACNase regulation by an internal "
                "switch that responds to double-stranded DNA breaks."
            ),
        },
        {
            "reference": BITTON_PMID,
            "snippet": T4_ACTIVATION_SNIPPET,
            "notes": (
                "Bitton et al. show that Acinetobacter baylyi RloC expressed "
                "in Escherichia coli is activated by wild-type phage T4, but "
                "not by a host-DNA-degradation mutant."
            ),
        },
        {
            "reference": BITTON_PMID,
            "snippet": T4_RESTRICTION_SNIPPET,
            "notes": (
                "Bitton et al. report that Acinetobacter baylyi RloC "
                "inefficiently impairs wild-type T4 plating and more strongly "
                "restricts a phage mutant lacking the decoy tRNA target."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        *all_hmm_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "rloc_locus_triggers_dna_break_responsive_activation",
            "title": "RloC loci encode DNA-break-responsive activation",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "DefenseFinder RloC locus to DNA-break-responsive RloC "
                "anticodon nuclease activation without asserting natural host "
                "breadth, the endogenous phage trigger, or exact RloC "
                "profile-to-activity mapping."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures RloC as a named DefenseFinder one-profile "
                "phage-defense system while leaving natural host breadth, the "
                "endogenous DNA-break trigger, phage restriction strength, and "
                "RloC profile-to-activity mapping unresolved."
            ),
            "nodes": [
                {
                    "node_id": "rloc_locus",
                    "label": "RloC locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder RloC phage-defense locus represented "
                        "by the RloC__RloC profile."
                    ),
                },
                {
                    "node_id": "dna_break_responsive_rloc_activation",
                    "label": "DNA-break-responsive RloC activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of RloC anticodon nuclease activity by "
                        "double-stranded DNA breaks, causing wobble "
                        "nucleotide excision from tRNA."
                    ),
                },
                {
                    "node_id": f"{SLUG}_system_trait",
                    "label": "RloC system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded RloC phage-defense "
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
                    "subject": "rloc_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "dna_break_responsive_rloc_activation",
                    "description": (
                        "RloC encodes a wobble nucleotide-excising anticodon "
                        "nuclease, Acinetobacter baylyi RloC responds to T4 "
                        "host DNA degradation when expressed in Escherichia "
                        "coli, and DefenseFinder models RloC as a "
                        "one-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": DAVIDOV_PMID,
                            "snippet": RLOC_TRNASE_SNIPPET,
                            "notes": (
                                "Davidov and Kaufmann identify RloC as a "
                                "wobble nucleotide-excising and "
                                "zinc-responsive tRNase."
                            ),
                        },
                        {
                            "reference": BITTON_PMID,
                            "snippet": DNA_BREAK_SWITCH_SNIPPET,
                            "notes": (
                                "Bitton et al. support RloC ACNase regulation "
                                "by an internal double-stranded-DNA-break "
                                "switch."
                            ),
                        },
                        {
                            "reference": BITTON_PMID,
                            "snippet": T4_ACTIVATION_SNIPPET,
                            "notes": (
                                "Bitton et al. show T4 host DNA degradation "
                                "activates Acinetobacter baylyi RloC expressed "
                                "in Escherichia coli."
                            ),
                        },
                        article_registry_evidence(),
                        rules_evidence(),
                        *all_hmm_evidence(),
                    ],
                },
                {
                    "subject": "dna_break_responsive_rloc_activation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": f"{SLUG}_system_trait",
                    "description": (
                        "DNA-break-responsive RloC anticodon nuclease "
                        "activation realizes the RloC system trait."
                    ),
                    "evidence": [
                        {
                            "reference": BITTON_PMID,
                            "snippet": T4_ACTIVATION_SNIPPET,
                            "notes": (
                                "Bitton et al. show that wild-type phage T4 "
                                "activates Acinetobacter baylyi RloC expressed "
                                "in Escherichia coli."
                            ),
                        },
                        {
                            "reference": BITTON_PMID,
                            "snippet": T4_RESTRICTION_SNIPPET,
                            "notes": (
                                "Bitton et al. report that Acinetobacter "
                                "baylyi RloC inefficiently impairs wild-type "
                                "T4 plating and more strongly restricts a "
                                "phage mutant lacking the decoy tRNA target."
                            ),
                        },
                    ],
                },
                {
                    "subject": f"{SLUG}_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "phage_defense_system",
                    "description": (
                        "RloC system possession is a phage-defense-system "
                        "trait."
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
            "discussion_id": "rloc-mechanism-gap",
            "prompt": (
                "Resolve natural RloC host breadth, endogenous RloC "
                "activation triggers, phage restriction strength, and RloC "
                "profile-to-activity mapping before minting narrower RloC "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Davidov and Kaufmann support RloC as a bacterial wobble "
                "nucleotide-excising tRNase, Bitton et al. show that "
                "Acinetobacter baylyi RloC responds to phage T4 host DNA "
                "degradation in an Escherichia coli expression context, and "
                "DefenseFinder models RloC as a one-profile system with an "
                "RloC__RloC marker. Natural host breadth, native phage "
                "triggers, restriction strength, and profile-to-activity "
                "mapping remain unresolved."
            ),
            "evidence": [
                {
                    "reference": BITTON_PMID,
                    "snippet": NATURAL_ROLE_GAP_SNIPPET,
                    "notes": (
                        "Bitton et al. leave the natural role of conserved "
                        "bacterial RloC unknown while comparing it to the "
                        "phage T4-excluding PrrC ACNase."
                    ),
                }
            ],
            "attaches_to": [
                "causal_graphs#rloc_locus_triggers_dna_break_responsive_activation"
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-09-22",
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
            "Minted RloC system as a DOI-backed GENOMICS TraitRecord under "
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
            "Reviewed the RloC canonical_examples gap and left "
            "canonical_examples empty: the current evidence supports RloC as "
            "a wobble nucleotide-excising tRNase, T4 activation of "
            "Acinetobacter baylyi RloC expressed in Escherichia coli, and the "
            "pinned DefenseFinder RloC profile, but does not cite a directly "
            "observed natural microbial taxon with a source-backed RloC locus "
            "broad enough for a canonical example. No paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_REVIEW_TIMESTAMP,
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
