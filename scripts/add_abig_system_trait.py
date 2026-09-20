#!/usr/bin/env python3
"""Add the AbiG system genomics trait."""

from __future__ import annotations

import argparse
import copy
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abig_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

OCONNOR_1996 = "DOI:10.1128/aem.62.9.3075-3082.1996"
OCONNOR_1999 = "DOI:10.1128/aem.65.1.330-335.1999"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T09:16:00Z"
PARENT_TIMESTAMP = "2026-09-20T09:16:01Z"
IDENTIFIER = "traitmech:000306"
PROPOSAL = "proposals/metpo_traitmech_v183"

ABIGI_ROW = (
    "| AbiG__AbiGi                                      | "
    "AbiG__AbiGi                                      | AbiG                   | "
    "Custom                  | 20     |"
)
ABIGII_ROW = (
    "| AbiG__AbiGii                                     | "
    "AbiG__AbiGii                                     | AbiG                   | "
    "Custom                  | 20     |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, and AbiH are "
    "split out as traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, traitmech:000301, traitmech:000303, and "
    "traitmech:000304, respectively. Lopatina et al., Fineran et al., Dy "
    "et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., Haaber "
    "et al., Owen et al., Depardieu et al., and Prevots et al. still "
    "support Abi as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, RT-related "
    "polymerase, two-component, translation-inhibition, prophage-encoded "
    "DNA-replication-inhibition, staphylococcal-kinase-triggered cell "
    "death, lactococcal AbiH phage resistance, and other Abi families. "
    "Additional narrower TraitRecords need separate review to ground each "
    "subfamily's trigger, effector, growth-arrest or cell-death mechanism, "
    "and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, Stk2, AbiH, and "
    "AbiG are split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, "
    "traitmech:000303, traitmech:000304, and traitmech:000306, "
    "respectively. Lopatina et al., Fineran et al., Dy et al., Durmaz and "
    "Klaenhammer, Wang et al., Bouchard et al., Haaber et al., Owen et al., "
    "Depardieu et al., Prevots et al., and O'Connor et al. still support "
    "Abi as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, RT-related "
    "polymerase, two-component, translation-inhibition, prophage-encoded "
    "DNA-replication-inhibition, staphylococcal-kinase-triggered cell "
    "death, lactococcal AbiH phage resistance, two-gene lactococcal AbiG "
    "RNA-synthesis interference, and other Abi families. Additional "
    "narrower TraitRecords need separate review to ground each subfamily's "
    "trigger, effector, growth-arrest or cell-death mechanism, and phage "
    "escape routes."
)
PARENT_CHANGES = (
    "Documented AbiG as split out in the open abortive-infection subfamily "
    "split-gap discussion after minting traitmech:000306 for the AbiG "
    "system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "AbiG | 10\\.1016/j\\.mib\\.2005\\.06\\.006 | Phage abortive "
            "infection in lactococci: variations on a theme"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named AbiG model "
            "namespace to a lactococcal abortive-infection review."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "AbiG\tAbiG\t2\t2\tAbiG__AbiGi, AbiG__AbiGii",
        "notes": (
            "The DefenseFinder rules table models AbiG as a two-component "
            "system requiring the AbiG__AbiGi and AbiG__AbiGii profiles."
        ),
    }


def abigi_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ABIGI_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiG__AbiGi under the "
            "AbiG model namespace."
        ),
    }


def abigii_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": ABIGII_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiG__AbiGii under the "
            "AbiG model namespace."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiG system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "two-gene abiG locus with abiGi and abiGii open reading frames, "
        "exemplified by the Lactococcus lactis subsp. cremoris UC653 "
        "plasmid pCI750 locus that restricts lactococcal phages without "
        "blocking phage DNA replication and is represented by the "
        "DefenseFinder AbiG__AbiGi and AbiG__AbiGii profiles."
    ),
    "definition_source": OCONNOR_1996,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiG",
            "synonym_type": "RELATED_SYNONYM",
            "source": OCONNOR_1996,
        }
    ],
    "evidence": [
        {
            "reference": OCONNOR_1996,
            "snippet": (
                "AbiG is an abortive infection (Abi) mechanism encoded by "
                "the conjugative plasmid pCI750 originally isolated from "
                "Lactococcus lactis subsp. cremoris UC653"
            ),
            "notes": (
                "O'Connor et al. identify AbiG as an abortive-infection "
                "mechanism encoded by the UC653 pCI750 plasmid."
            ),
        },
        {
            "reference": OCONNOR_1996,
            "snippet": (
                "Insensitivity conferred by this Abi manifested itself as "
                "complete resistance to phi 712 (936 phage species) with "
                "only partial resistance to phi c2 (c2 species)"
            ),
            "notes": (
                "O'Connor et al. show that AbiG restricts tested "
                "lactococcal phages with species-dependent strength."
            ),
        },
        {
            "reference": OCONNOR_1996,
            "snippet": (
                "The smallest subclone of pCI750 which expressed the Abi "
                "phenotype contained a 3.5-kb insert which encoded two "
                "potential open reading frames"
            ),
            "notes": (
                "O'Connor et al. localize AbiG activity to a pCI750 "
                "subclone carrying two predicted coding sequences."
            ),
        },
        {
            "reference": OCONNOR_1996,
            "snippet": (
                "abiGi (750 bp) and abiGii (1,194 bp) were separated by 2 "
                "bp and appeared to share a single promoter upstream of "
                "abiGi"
            ),
            "notes": (
                "O'Connor et al. support abiGi and abiGii as the paired "
                "open reading frames of the AbiG locus."
            ),
        },
        {
            "reference": OCONNOR_1996,
            "snippet": "The mechanism did not inhibit phage DNA replication",
            "notes": (
                "O'Connor et al. rule out phage DNA replication as the "
                "blocked step in the original AbiG characterization."
            ),
        },
        {
            "reference": OCONNOR_1999,
            "snippet": (
                "The abortive infection system AbiG is encoded by the "
                "lactococcal plasmid pCI750"
            ),
            "notes": (
                "The follow-up O'Connor et al. study reiterates AbiG as a "
                "pCI750-encoded lactococcal abortive-infection system."
            ),
        },
        {
            "reference": OCONNOR_1999,
            "snippet": (
                "The abiG locus (consisting of two genes, abiGi and abiGii) "
                "was examined by Northern blot analysis, revealing two "
                "transcripts of approximately 2.8 and 1.5 kb which were "
                "homologous to the two gene-specific probes"
            ),
            "notes": (
                "O'Connor et al. confirm the abiGi/abiGii two-gene locus at "
                "the transcript level."
            ),
        },
        {
            "reference": OCONNOR_1999,
            "snippet": (
                "Examination of phage sk1 RNA synthesis demonstrated that "
                "both the subcloned AbiG and, to a greater extent, pCI750 "
                "inhibited this process"
            ),
            "notes": (
                "O'Connor et al. connect the AbiG subclone to inhibited "
                "sk1 phage RNA synthesis."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        abigi_hmm_evidence(),
        abigii_hmm_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1358",
            "taxon_label": "Lactococcus lactis",
            "note": (
                "O'Connor et al. characterized AbiG from conjugative "
                "plasmid pCI750, originally isolated from Lactococcus "
                "lactis subsp. cremoris UC653, and localized the "
                "abortive-infection phenotype to the abiGi/abiGii locus."
            ),
            "reference": OCONNOR_1996,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "abig_inhibits_lactococcal_phage_rna_synthesis",
            "title": "AbiG inhibits lactococcal phage RNA synthesis",
            "description": (
                "Conservative system-level sketch linking an abiGi/abiGii "
                "locus to AbiG antiphage activity, inhibited phage RNA "
                "synthesis, restricted lactococcal phage propagation, and "
                "abortive-infection system possession without asserting "
                "AbiG's unresolved primary target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiG as a named DefenseFinder two-profile "
                "abortive-infection system whose pCI750 prototype restricts "
                "phi 712, partially restricts phi c2, and inhibits phage sk1 "
                "and late c2 RNA synthesis while leaving the phage trigger, "
                "AbiGi and AbiGii molecular functions, cellular target, "
                "growth-arrest or cell-death route, and phage escape routes "
                "unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abig_locus",
                    "label": "abiG locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A two-gene abiGi/abiGii abortive-infection locus "
                        "represented by the DefenseFinder AbiG rule."
                    ),
                },
                {
                    "node_id": "abig_antiphage_activity",
                    "label": "AbiG antiphage activity",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Abortive-infection phage resistance mediated by the "
                        "AbiG system."
                    ),
                },
                {
                    "node_id": "phage_rna_synthesis",
                    "label": "phage RNA synthesis",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Synthesis of sensitive lactococcal phage RNA during "
                        "infection."
                    ),
                },
                {
                    "node_id": "restricted_lactococcal_phage_propagation",
                    "label": "restricted lactococcal phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced completion of lactococcal phage propagation "
                        "in an AbiG-containing infected host cell."
                    ),
                },
                {
                    "node_id": "abig_system_trait",
                    "label": "AbiG system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiG "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded "
                        "abortive-infection phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abig_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "abig_antiphage_activity",
                    "description": (
                        "The pCI750 abiG locus carries abiGi and abiGii open "
                        "reading frames, and DefenseFinder models AbiG as a "
                        "two-profile system requiring both AbiG components."
                    ),
                    "evidence": [
                        {
                            "reference": OCONNOR_1996,
                            "snippet": (
                                "The smallest subclone of pCI750 which "
                                "expressed the Abi phenotype contained a "
                                "3.5-kb insert which encoded two potential "
                                "open reading frames"
                            ),
                            "notes": (
                                "O'Connor et al. localize the AbiG phenotype "
                                "to a two-ORF pCI750 subclone."
                            ),
                        },
                        rules_evidence(),
                        abigi_hmm_evidence(),
                        abigii_hmm_evidence(),
                    ],
                },
                {
                    "subject": "abig_antiphage_activity",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_rna_synthesis",
                    "description": (
                        "AbiG antiphage activity inhibits RNA synthesis by "
                        "tested sensitive lactococcal phages."
                    ),
                    "evidence": [
                        {
                            "reference": OCONNOR_1999,
                            "snippet": (
                                "Examination of phage sk1 RNA synthesis "
                                "demonstrated that both the subcloned AbiG "
                                "and, to a greater extent, pCI750 inhibited "
                                "this process"
                            ),
                            "notes": (
                                "O'Connor et al. show that the AbiG subclone "
                                "inhibits phage sk1 RNA synthesis."
                            ),
                        }
                    ],
                },
                {
                    "subject": "abig_antiphage_activity",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_lactococcal_phage_propagation",
                    "description": (
                        "AbiG activity restricts propagation by phi 712 "
                        "and partially restricts phi c2."
                    ),
                    "evidence": [
                        {
                            "reference": OCONNOR_1996,
                            "snippet": (
                                "Insensitivity conferred by this Abi "
                                "manifested itself as complete resistance to "
                                "phi 712 (936 phage species) with only "
                                "partial resistance to phi c2 (c2 species)"
                            ),
                            "notes": (
                                "O'Connor et al. measure complete or partial "
                                "resistance from the AbiG mechanism for "
                                "tested lactococcal phages."
                            ),
                        }
                    ],
                },
                {
                    "subject": "restricted_lactococcal_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abig_system_trait",
                    "description": (
                        "Restriction of lactococcal phage propagation "
                        "realizes the AbiG abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": OCONNOR_1996,
                            "snippet": (
                                "AbiG is an abortive infection (Abi) "
                                "mechanism encoded by the conjugative plasmid "
                                "pCI750"
                            ),
                            "notes": (
                                "O'Connor et al. classify AbiG as a pCI750 "
                                "abortive-infection mechanism."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "abig_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiG system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        {
                            "reference": OCONNOR_1999,
                            "snippet": (
                                "The abortive infection system AbiG is "
                                "encoded by the lactococcal plasmid pCI750"
                            ),
                            "notes": (
                                "O'Connor et al. explicitly place AbiG in "
                                "the abortive-infection class of phage "
                                "defense."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abig-primary-target-gap",
            "prompt": (
                "Resolve the AbiG phage trigger, AbiGi and AbiGii molecular "
                "functions, and primary arrest target before minting "
                "narrower AbiG mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "O'Connor et al. support AbiG as a named lactococcal "
                "abortive-infection system encoded by two adjacent pCI750 "
                "open reading frames, and DefenseFinder represents AbiG "
                "with a two-profile rule. The 1999 transcription study "
                "connects AbiG to inhibited phage sk1 and late c2 RNA "
                "synthesis, but it explicitly leaves unresolved whether "
                "transcription is the system's primary target or a "
                "secondary effect."
            ),
            "evidence": [
                {
                    "reference": OCONNOR_1999,
                    "snippet": (
                        "AbiG inhibits phage sk1 and late c2 RNA synthesis; "
                        "however, whether this process of transcription is "
                        "the primary target of the system or a secondary "
                        "effect remains to be determined"
                    ),
                    "notes": (
                        "O'Connor et al. identify phage RNA-synthesis "
                        "inhibition as a downstream AbiG effect while "
                        "leaving the direct target unresolved."
                    ),
                }
            ],
            "attaches_to": ["causal_graphs#abig_inhibits_lactococcal_phage_rna_synthesis"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-20",
        }
    ],
}


def load_trait(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def update_abortive_parent(record: dict[str, Any]) -> dict[str, Any]:
    assert record["identifier"] == "traitmech:000214"
    assert record["label"] == "abortive infection system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    discussions = record.get("discussions") or []
    discussion = next(
        item
        for item in discussions
        if item.get("discussion_id") == "abortive-infection-subfamily-split-gap"
    )
    if discussion["rationale"] == NEW_PARENT_RATIONALE:
        assert discussion["status"] == "OPEN"
        return record

    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    assert discussion["rationale"] == OLD_PARENT_RATIONALE
    discussion["rationale"] = NEW_PARENT_RATIONALE

    record_curation_event(
        record,
        curator=CURATOR,
        action="RESOLVE_DISCUSSION_SCOPE",
        changes=PARENT_CHANGES,
        llm_assisted=True,
        timestamp=PARENT_TIMESTAMP,
    )
    return record


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted AbiG system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / ABORTIVE.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_abortive_parent(load_trait(ABORTIVE))
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "AbiG system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
