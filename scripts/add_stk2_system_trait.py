#!/usr/bin/env python3
"""Add the Stk2 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "stk2_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

DEPARDIEU = "DOI:10.1016/j.chom.2016.08.010"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    "https://raw.githubusercontent.com/mdmparis/defense-finder-models/"
    f"{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-09-20T07:41:00Z"
PARENT_TIMESTAMP = "2026-09-20T07:41:01Z"
IDENTIFIER = "traitmech:000303"
PROPOSAL = "proposals/metpo_traitmech_v180"

HMM_ROW = (
    "| Stk2__Stk2                                       | "
    "Stk2__Stk2                                       | Stk2                   | "
    "Custom                  | 150    |"
)

OLD_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, and BstA are split out "
    "as traitmech:000226, traitmech:000225, traitmech:000227, "
    "traitmech:000228, traitmech:000229, traitmech:000230, "
    "traitmech:000300, and traitmech:000301, respectively. Lopatina "
    "et al., Fineran et al., Dy et al., Durmaz and Klaenhammer, Wang "
    "et al., Bouchard et al., Haaber et al., and Owen et al. still "
    "support Abi as a genomically encoded phage defense strategy that "
    "spans mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, and other Abi "
    "families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
NEW_PARENT_RATIONALE = (
    "ToxIN, AbiQ, AbiE, AbiZ, AbiK, AbiT, AbiV, BstA, and Stk2 are "
    "split out as traitmech:000226, traitmech:000225, "
    "traitmech:000227, traitmech:000228, traitmech:000229, "
    "traitmech:000230, traitmech:000300, traitmech:000301, and "
    "traitmech:000303, respectively. Lopatina et al., Fineran et al., "
    "Dy et al., Durmaz and Klaenhammer, Wang et al., Bouchard et al., "
    "Haaber et al., Owen et al., and Depardieu et al. still support "
    "Abi as a genomically encoded phage defense strategy that spans "
    "mechanistically diverse toxin-antitoxin, premature-lysis, "
    "RT-related polymerase, two-component, translation-inhibition, "
    "prophage-encoded DNA-replication-inhibition, "
    "staphylococcal-kinase-triggered cell death, and other Abi "
    "families. Additional narrower TraitRecords need separate review to "
    "ground each subfamily's trigger, effector, growth-arrest or "
    "cell-death mechanism, and phage escape routes."
)
PARENT_CHANGES = (
    "Documented Stk2 as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000303 for "
    "the Stk2 system; other abortive-infection families remain open."
)


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": (
            "Stk2 | 10\\.1016/j\\.chom\\.2016\\.08\\.010 | A "
            "eukaryotic-like Serine/threonine kinase protects "
            "staphylococci against phages"
        ),
        "notes": (
            "The DefenseFinder article registry maps the named Stk2 "
            "system to the Depardieu et al. final article."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records the Stk2__Stk2 "
            "profile under the Stk2 model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": "Stk2\tStk2\t1\t1\tStk2__Stk2",
        "notes": (
            "The DefenseFinder rules table models Stk2 as a one-component "
            "system requiring the Stk2__Stk2 profile."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Stk2 system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "phage-defense locus encoding the Stk2 serine/threonine kinase, "
        "which can be activated by a phage protein to phosphorylate host "
        "proteins and induce host-cell death that prevents bacteriophage "
        "propagation."
    ),
    "definition_source": DEPARDIEU,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "Stk2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_ARTICLES,
        }
    ],
    "evidence": [
        {
            "reference": DEPARDIEU,
            "snippet": (
                "Here we identify Stk2, a staphylococcal "
                "serine/threonine kinase that provides efficient immunity "
                "against bacteriophages by inducing abortive infection"
            ),
            "notes": (
                "Depardieu et al. identify Stk2 as a staphylococcal "
                "serine/threonine kinase that provides bacteriophage "
                "immunity through abortive infection."
            ),
        },
        {
            "reference": DEPARDIEU,
            "snippet": "A phage protein of unknown function activates the Stk2 kinase",
            "notes": (
                "Depardieu et al. connect an unidentified phage protein to "
                "Stk2 kinase activation."
            ),
        },
        {
            "reference": DEPARDIEU,
            "snippet": (
                "This leads to the Stk2-dependent phosphorylation of "
                "several proteins involved in translation, global "
                "transcription control, cell-cycle control, stress "
                "response, DNA topology, DNA repair, and central metabolism"
            ),
            "notes": (
                "Depardieu et al. describe Stk2-dependent phosphorylation "
                "of multiple host-protein targets after Stk2 activation."
            ),
        },
        {
            "reference": DEPARDIEU,
            "snippet": (
                "Bacterial host cells die as a consequence of Stk2 "
                "activation, thereby preventing propagation of the phage to "
                "the rest of the bacterial population"
            ),
            "notes": (
                "Depardieu et al. connect Stk2 activation to host-cell "
                "death and the resulting block of phage propagation."
            ),
        },
        article_registry_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "stk2_activation_aborts_phage_infection",
            "title": "Stk2 kinase activation aborts phage infection",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "Stk2 phage-defense locus to phage-protein-triggered "
                "kinase activation, host protein phosphorylation, host-cell "
                "death, and the Stk2 abortive-infection trait without "
                "asserting the unresolved direct phage activator or lethal "
                "phosphorylation target."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Stk2 as a named DefenseFinder "
                "single-profile abortive-infection system with a "
                "phage-activated serine/threonine kinase output while "
                "leaving the activating phage protein, the direct lethal "
                "phosphorylation event, target conservation, and "
                "phage-specific escape routes unresolved."
            ),
            "nodes": [
                {
                    "node_id": "stk2_locus",
                    "label": "Stk2 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A Stk2 abortive-infection phage-defense locus "
                        "represented by the DefenseFinder Stk2__Stk2 "
                        "profile."
                    ),
                },
                {
                    "node_id": "stk2_kinase_activation",
                    "label": "Stk2 kinase activation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Activation of the Stk2 serine/threonine kinase by "
                        "a phage protein of unknown function."
                    ),
                },
                {
                    "node_id": "host_protein_phosphorylation",
                    "label": "host protein phosphorylation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Stk2-dependent phosphorylation of host proteins "
                        "after Stk2 kinase activation."
                    ),
                },
                {
                    "node_id": "host_cell_death",
                    "label": "host cell death",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Stk2-activation-dependent death of infected "
                        "bacterial host cells."
                    ),
                },
                {
                    "node_id": "phage_propagation",
                    "label": "phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Propagation of bacteriophage through a bacterial "
                        "host population."
                    ),
                },
                {
                    "node_id": "stk2_system_trait",
                    "label": "Stk2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Stk2 "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a bacteriophage abortive-infection "
                        "defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "stk2_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "stk2_kinase_activation",
                    "description": (
                        "Depardieu et al. identify the Stk2 "
                        "serine/threonine kinase as a phage-immunity "
                        "factor, and DefenseFinder models Stk2 as a "
                        "single-profile system."
                    ),
                    "evidence": [
                        {
                            "reference": DEPARDIEU,
                            "snippet": (
                                "Here we identify Stk2, a staphylococcal "
                                "serine/threonine kinase that provides "
                                "efficient immunity against bacteriophages"
                            ),
                            "notes": (
                                "Depardieu et al. identify Stk2 as a "
                                "bacteriophage-immunity factor."
                            ),
                        },
                        rules_evidence(),
                        hmm_inventory_evidence(),
                    ],
                },
                {
                    "subject": "stk2_kinase_activation",
                    "predicate": "enables",
                    "predicate_id": "RO:0002327",
                    "object": "host_protein_phosphorylation",
                    "description": (
                        "Phage-protein activation of Stk2 leads to "
                        "Stk2-dependent phosphorylation of several host "
                        "proteins."
                    ),
                    "evidence": [
                        {
                            "reference": DEPARDIEU,
                            "snippet": (
                                "A phage protein of unknown function "
                                "activates the Stk2 kinase"
                            ),
                            "notes": (
                                "Depardieu et al. show phage-protein "
                                "activation of Stk2."
                            ),
                        },
                        {
                            "reference": DEPARDIEU,
                            "snippet": (
                                "This leads to the Stk2-dependent "
                                "phosphorylation of several proteins"
                            ),
                            "notes": (
                                "Depardieu et al. connect Stk2 activation "
                                "to host-protein phosphorylation."
                            ),
                        },
                    ],
                },
                {
                    "subject": "stk2_kinase_activation",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "host_cell_death",
                    "description": (
                        "Stk2 activation is followed by death of infected "
                        "bacterial host cells."
                    ),
                    "evidence": [
                        {
                            "reference": DEPARDIEU,
                            "snippet": (
                                "Bacterial host cells die as a consequence "
                                "of Stk2 activation"
                            ),
                            "notes": (
                                "Depardieu et al. connect Stk2 activation "
                                "to host-cell death."
                            ),
                        }
                    ],
                },
                {
                    "subject": "host_cell_death",
                    "predicate": "mitigates",
                    "predicate_id": "METPO:2007407",
                    "object": "phage_propagation",
                    "description": (
                        "Stk2-triggered host-cell death prevents "
                        "propagation of the phage through the rest of the "
                        "bacterial population."
                    ),
                    "evidence": [
                        {
                            "reference": DEPARDIEU,
                            "snippet": (
                                "Bacterial host cells die as a consequence "
                                "of Stk2 activation, thereby preventing "
                                "propagation of the phage to the rest of "
                                "the bacterial population"
                            ),
                            "notes": (
                                "Depardieu et al. connect Stk2-dependent "
                                "host-cell death to phage-propagation "
                                "prevention."
                            ),
                        }
                    ],
                },
                {
                    "subject": "host_cell_death",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "stk2_system_trait",
                    "description": (
                        "Stk2-triggered host-cell death realizes the Stk2 "
                        "abortive-infection trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEPARDIEU,
                            "snippet": (
                                "provides efficient immunity against "
                                "bacteriophages by inducing abortive "
                                "infection"
                            ),
                            "notes": (
                                "Depardieu et al. classify the "
                                "Stk2-dependent immunity mechanism as "
                                "abortive infection."
                            ),
                        },
                        article_registry_evidence(),
                    ],
                },
                {
                    "subject": "stk2_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system",
                    "description": (
                        "Stk2 system possession is an abortive-infection "
                        "system trait."
                    ),
                    "evidence": [
                        {
                            "reference": DEPARDIEU,
                            "snippet": (
                                "provides efficient immunity against "
                                "bacteriophages by inducing abortive "
                                "infection"
                            ),
                            "notes": (
                                "Depardieu et al. support Stk2 as an "
                                "abortive-infection system."
                            ),
                        }
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "stk2-activator-and-death-target-gap",
            "prompt": (
                "Resolve the Stk2-activating phage protein and lethal "
                "host-phosphorylation target before minting narrower Stk2 "
                "mechanism children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Depardieu et al. support Stk2 as a named "
                "phage-activated serine/threonine kinase system whose "
                "activation causes host-protein phosphorylation, "
                "bacterial host-cell death, and abortive infection, and "
                "DefenseFinder represents Stk2 with a one-profile model. "
                "This system-level record leaves the direct phage "
                "activator, the lethal Stk2 phosphorylation target, "
                "target conservation across Stk2 loci, and phage escape "
                "routes unresolved."
            ),
            "attaches_to": ["causal_graphs#stk2_activation_aborts_phage_infection"],
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
            "Minted Stk2 system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, or prior proposal record; the replacement "
            f"placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def validate_output(record: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = update_abortive_parent(load_trait(ABORTIVE))
    validate_output(record)
    validate_output(parent)

    if args.apply:
        if TARGET.exists():
            raise SystemExit(f"{TARGET} already exists")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "Stk2 system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
