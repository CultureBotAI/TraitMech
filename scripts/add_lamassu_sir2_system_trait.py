"""Add the Lamassu-Sir2 system genomics trait."""

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

from traitmech.curate.curation_event import record_curation_event  # noqa: E402, RUF100
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402, RUF100

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "lamassu_sir2_system.yaml"
LAMASSU_PARENT = REPO_ROOT / "data" / "traits" / "genomics" / "lamassu_system.yaml"

HAUDIQUET = "DOI:10.1073/pnas.2519643122"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-03T06:34:00Z"
PARENT_TIMESTAMP = "2026-10-03T06:34:01Z"
CANONICAL_TIMESTAMP = "2026-10-03T06:34:02Z"
REVIEW_TIMESTAMP = "2026-10-03T06:56:28Z"
IDENTIFIER = "traitmech:000566"
LAMASSU_PARENT_ID = "traitmech:000232"
PROPOSAL = "proposals/metpo_traitmech_v443"

LAMASSU_DIVERSITY_SNIPPET = (
    "a bacterial immune system family featuring diverse effectors but a "
    "core conserved SMC-like sensor"
)
ARTICLE_ROW = (
    "| Lamassu-Fam | 10\\.1101/2022\\.05\\.11\\.491447 | An expanding "
    "arsenal of immune systems that protect bacteria from phages | "
)
RULE_ROW = (
    "Lamassu-Fam\tLamassu-Sir2\t2\t2\t"
    "Lamassu-Fam__LmuA_effector_Sir2, "
    "Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II\t"
    "Lamassu-Fam__LmuC_acc_Lipase\t"
    "Lamassu-Fam__LmuA_effector_Amidase, "
    "Lamassu-Fam__LmuA_effector_Cap4_nuclease, "
    "Lamassu-Fam__LmuA_effector_Cap4_nuclease_II, "
    "Lamassu-Fam__LmuA_effector_FMO, "
    "Lamassu-Fam__LmuA_effector_Hydrolase, "
    "Lamassu-Fam__LmuA_effector_Lipase, "
    "Lamassu-Fam__LmuA_effector_Mrr, "
    "Lamassu-Fam__LmuA_effector_PDDEXK, "
    "Lamassu-Fam__LmuA_effector_Protease, "
    "Lamassu-Fam__LmuA_effector_hypothetical\t"
)
RULE_PARENT_SPAN = "Lamassu-Fam\tLamassu-Sir2\t2\t2"

LMUA_HMM_ROW = (
    "| Lamassu-Fam__LmuA_effector_Sir2                  |"
    " Lamassu-Fam__LmuA_effector_Sir2                  |"
    " Lamassu-Fam            | Custom                  | 20     |"
)
LMUB_RULE_HMM_ROW = (
    "| Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II           |"
    " Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II           |"
    " Lamassu-Fam            | Custom                  | 20     |"
)
LMUC_RULE_HMM_ROW = (
    "| Lamassu-Fam__LmuC_acc_Lipase                     |"
    " Lamassu-Fam__LmuC_acc_Lipase                     |"
    " Lamassu-Fam            | Custom                  | 20     |"
)
LMUB_SIR2_HMM_ROW = (
    "| Lamassu-Fam__LmuB_SMC_Sir2                       |"
    " Lamassu-Fam__LmuB_SMC_Sir2                       |"
    " Lamassu-Fam            | Custom                  | 20     |"
)
LMUC_SIR2_HMM_ROW = (
    "| Lamassu-Fam__LmuC_acc_Sir2                       |"
    " Lamassu-Fam__LmuC_acc_Sir2                       |"
    " Lamassu-Fam            | Custom                  | 20     |"
)


def lamassu_diversity_evidence() -> dict[str, str]:
    return {
        "reference": HAUDIQUET,
        "snippet": LAMASSU_DIVERSITY_SNIPPET,
        "notes": (
            "Haudiquet et al. support placing Lamassu subtypes under a "
            "Lamassu family with diverse LmuA effectors and a conserved "
            "SMC-like sensor."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the "
            "Lamassu-Fam model namespace to a bacterial immune-systems "
            "preprint."
        ),
    }


def lmua_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": LMUA_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "Lamassu-Fam__LmuA_effector_Sir2 custom profile listed as "
            "mandatory by the Lamassu-Sir2 rule row."
        ),
    }


def lmub_rule_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": LMUB_RULE_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II custom profile listed "
            "as mandatory by the Lamassu-Sir2 rule row."
        ),
    }


def lmuc_rule_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": LMUC_RULE_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "Lamassu-Fam__LmuC_acc_Lipase custom profile listed as "
            "accessory by the Lamassu-Sir2 rule row."
        ),
    }


def lmub_sir2_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": LMUB_SIR2_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records a "
            "Lamassu-Fam__LmuB_SMC_Sir2 custom profile that is not the "
            "LmuB SMC profile named by the pinned Lamassu-Sir2 rule row."
        ),
    }


def lmuc_sir2_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": LMUC_SIR2_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records a "
            "Lamassu-Fam__LmuC_acc_Sir2 custom profile that is not the "
            "LmuC accessory profile named by the pinned Lamassu-Sir2 rule "
            "row."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models Lamassu-Sir2 as a "
            "Lamassu-Fam subsystem requiring "
            "Lamassu-Fam__LmuA_effector_Sir2 and "
            "Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II, with "
            "Lamassu-Fam__LmuC_acc_Lipase as an accessory profile."
        ),
    }


def rules_parent_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_PARENT_SPAN,
        "notes": (
            "The pinned DefenseFinder rules table places the Lamassu-Sir2 "
            "subsystem under the Lamassu-Fam system key with 2 mandatory "
            "matches and 2 genes required."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Lamassu-Sir2 system",
    "definition": (
        "A Lamassu system in which an organism possesses a genome-encoded "
        "DefenseFinder Lamassu-Sir2 subtype locus represented by the "
        "Lamassu-Sir2 rule row requiring the "
        "Lamassu-Fam__LmuA_effector_Sir2 and "
        "Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II profiles."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [LAMASSU_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Lamassu-Sir2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Lamassu-Fam__LmuA_effector_Sir2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        lamassu_diversity_evidence(),
        article_registry_evidence(),
        lmua_hmm_evidence(),
        lmub_rule_hmm_evidence(),
        lmuc_rule_hmm_evidence(),
        lmub_sir2_hmm_evidence(),
        lmuc_sir2_hmm_evidence(),
        rules_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": "lamassu_sir2_locus_subtype_defense",
            "title": "Lamassu-Sir2 is a DefenseFinder Lamassu subtype",
            "description": (
                "Conservative subtype-level classification linking the "
                "DefenseFinder Lamassu-Sir2 rule-row definition to "
                "Lamassu-Sir2 system possession and its Lamassu parent."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures Lamassu-Sir2 as a DefenseFinder "
                "rule-row subtype of Lamassu system possession without "
                "asserting a Lamassu-Sir2-specific antiphage process, "
                "exact phage-triggered Sir2 effector activity, viral-DNA "
                "trigger, LmuC requirement, native host breadth, cell-death "
                "output, or whether every DefenseFinder Lamassu-Sir2 "
                "prediction is a complete experimentally active locus."
            ),
            "nodes": [
                {
                    "node_id": "lamassu_sir2_system_trait",
                    "label": "Lamassu-Sir2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Lamassu-Sir2 "
                        "phage-defense system."
                    ),
                },
                {
                    "node_id": "lamassu_system_trait",
                    "label": "Lamassu system",
                    "node_type": "TRAIT",
                    "grounding": LAMASSU_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded Lamassu phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "lamassu_sir2_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "lamassu_system_trait",
                    "description": (
                        "Lamassu-Sir2 system possession is a Lamassu-system trait."
                    ),
                    "evidence": [
                        article_registry_evidence(),
                        rules_parent_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "lamassu-sir2-activity-gap",
            "prompt": (
                "Resolve Lamassu-Sir2 phage triggers, native hosts, Sir2 "
                "effector activity, LmuC usage, and profile-to-activity "
                "criteria before minting enzyme, trigger, or component "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Haudiquet et al. support a Lamassu family with diverse "
                "LmuA effectors and a conserved SMC-like sensor, and the "
                "pinned DefenseFinder HMM inventory and rules table support "
                "Lamassu-Sir2 as a Lamassu-Fam subtype whose rule row "
                "requires Lamassu-Fam__LmuA_effector_Sir2 and "
                "Lamassu-Fam__LmuB_SMC_Cap4_nuclease_II. This first-pass "
                "record follows the rule row but leaves exact Sir2 effector "
                "activity, the rule row's relationship to Sir2-scoped "
                "LmuB/LmuC HMM rows, LmuC requirement, native hosts, phage "
                "triggers, cell-death output, and profile-to-activity "
                "criteria unresolved."
            ),
            "evidence": [
                lamassu_diversity_evidence(),
                lmua_hmm_evidence(),
                lmub_sir2_hmm_evidence(),
                lmuc_sir2_hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#lamassu_sir2_locus_subtype_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-03",
        }
    ],
}

OLD_LAMASSU_DISCUSSION_RATIONALE = (
    "Haudiquet et al. support a structurally characterized Vibrio cholerae "
    "Lamassu Vc-Cap4 system with LmuABC DNA-end sensing and LmuA Cap4 "
    "nuclease activation, and the pinned DefenseFinder tables model "
    "Lamassu-Amidase, Lamassu-Cap4_nuclease, Lamassu-FMO, "
    "Lamassu-Hydrolase, Lamassu-Lipase, Lamassu-Mrr, Lamassu-PDDEXK, "
    "Lamassu-Protease, and other Lamassu-Fam subtypes as rule-row "
    "variants. Lamassu-Amidase, Lamassu-Cap4 nuclease, Lamassu-FMO, "
    "Lamassu-Hydrolase, Lamassu-Lipase, Lamassu-Mrr, Lamassu-PDDEXK, and "
    "Lamassu-Protease now capture eight DefenseFinder rule-row subtypes, "
    "but long-versus-short LmuB clades, LmuC-independent subfamilies, the "
    "Lamassu-Fam base, Lamassu-Hydrolase_Protease, Lamassu-Sir2, and "
    "Lamassu-Hypothetical rule rows, viral-DNA triggers, exact LmuA "
    "effector substrates, FMO acronym expansion, the Lamassu-FMO rule row's "
    "relationship to FMO-scoped LmuB/LmuC HMM rows, the Lamassu-Lipase "
    "rule row's relationship to its Lipase-scoped LmuB HMM row, the "
    "Lamassu-Mrr rule row's relationship to Mrr-scoped LmuB/LmuC HMM "
    "rows, the Lamassu-PDDEXK rule row's relationship to PDDEXK-scoped "
    "LmuB/LmuC HMM rows, and cell-death outputs across Lamassu loci remain "
    "unresolved."
)

LAMASSU_DISCUSSION_RATIONALE = (
    "Haudiquet et al. support a structurally characterized Vibrio cholerae "
    "Lamassu Vc-Cap4 system with LmuABC DNA-end sensing and LmuA Cap4 "
    "nuclease activation, and the pinned DefenseFinder tables model "
    "Lamassu-Amidase, Lamassu-Cap4_nuclease, Lamassu-FMO, "
    "Lamassu-Hydrolase, Lamassu-Lipase, Lamassu-Mrr, Lamassu-PDDEXK, "
    "Lamassu-Protease, Lamassu-Sir2, and other Lamassu-Fam subtypes as "
    "rule-row variants. Lamassu-Amidase, Lamassu-Cap4 nuclease, "
    "Lamassu-FMO, Lamassu-Hydrolase, Lamassu-Lipase, Lamassu-Mrr, "
    "Lamassu-PDDEXK, Lamassu-Protease, and Lamassu-Sir2 now capture nine "
    "DefenseFinder rule-row subtypes, but long-versus-short LmuB clades, "
    "LmuC-independent subfamilies, the Lamassu-Fam base, "
    "Lamassu-Hydrolase_Protease, and Lamassu-Hypothetical rule rows, "
    "viral-DNA triggers, exact LmuA effector substrates, FMO acronym "
    "expansion, the Lamassu-FMO rule row's relationship to FMO-scoped "
    "LmuB/LmuC HMM rows, the Lamassu-Lipase rule row's relationship to "
    "its Lipase-scoped LmuB HMM row, the Lamassu-Mrr rule row's "
    "relationship to Mrr-scoped LmuB/LmuC HMM rows, the Lamassu-PDDEXK "
    "rule row's relationship to PDDEXK-scoped LmuB/LmuC HMM rows, the "
    "Lamassu-Sir2 rule row's relationship to Sir2-scoped LmuB/LmuC HMM "
    "rows, and cell-death outputs across Lamassu loci remain unresolved."
)

PARENT_EVENT_CHANGES = (
    "Documented Lamassu-Sir2 as split out in the open Lamassu "
    "subtype-effector discussion after minting traitmech:000566 for "
    "the DefenseFinder-backed Lamassu-Sir2 child; remaining "
    "Lamassu-Fam rule rows and finer Lamassu activation mechanisms "
    "remain open."
)


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Lamassu-Sir2 system as a DefenseFinder-backed "
            "GENOMICS TraitRecord under the Lamassu system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record for the "
            "target local ID, placeholder METPO ID, proposal cohort, "
            "record slug, human label, or DefenseFinder subsystem; existing "
            "Lamassu-Fam__LmuA_effector_Sir2 mentions were limited to "
            "forbidden-profile evidence on neighboring Lamassu-Fam "
            "subtypes, their earlier writer scripts, and rendered pages, "
            "and the replacement placeholder is reserved in "
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
            "Reviewed Lamassu-Sir2 system during initial curation and left "
            "canonical_examples empty because the pinned DefenseFinder "
            "tables support a rule-row subtype but not an accession-backed "
            "native microbial taxon exemplar tied to the Lamassu-Sir2 "
            "profiles and experimentally verified endogenous activity. No "
            "paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="EXPANDED_EVIDENCE",
        changes=(
            "Addressed adversarial review issue #1604 by adding exact "
            "evidence for the Sir2-scoped Lamassu-Fam__LmuB_SMC_Sir2 and "
            "Lamassu-Fam__LmuC_acc_Sir2 HMM rows so the unresolved "
            "relationship between those rows and the generic LmuB/LmuC "
            "rows named by the Lamassu-Sir2 rule is auditable on the "
            "Lamassu-Sir2 record itself."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
    )
    return record


def build_lamassu_parent() -> dict[str, Any]:
    record = yaml.safe_load(LAMASSU_PARENT.read_text())
    assert record["identifier"] == LAMASSU_PARENT_ID
    assert record["label"] == "Lamassu system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000209"]

    discussion = next(
        item
        for item in record["discussions"]
        if item["discussion_id"] == "lamassu-subtype-and-effector-gap"
    )
    assert discussion["kind"] == "KNOWLEDGE_GAP"
    assert discussion["status"] == "OPEN"
    if discussion["rationale"] == OLD_LAMASSU_DISCUSSION_RATIONALE:
        discussion["rationale"] = LAMASSU_DISCUSSION_RATIONALE
    elif discussion["rationale"] != LAMASSU_DISCUSSION_RATIONALE:
        raise SystemExit("unexpected Lamassu subtype discussion rationale")

    existing_event = next(
        (
            event
            for event in record.get("curation_history", [])
            if event.get("action") == "TRACK_NARROWER_RECORD"
            and event.get("timestamp") == PARENT_TIMESTAMP
        ),
        None,
    )
    if existing_event is not None:
        if existing_event.get("changes") != PARENT_EVENT_CHANGES:
            raise SystemExit("unexpected Lamassu-Sir2 parent curation event")
    else:
        record_curation_event(
            record,
            curator=CURATOR,
            action="TRACK_NARROWER_RECORD",
            changes=PARENT_EVENT_CHANGES,
            llm_assisted=True,
            timestamp=PARENT_TIMESTAMP,
        )
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / LAMASSU_PARENT.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = build_lamassu_parent()
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            existing = yaml.safe_load(TARGET.read_text())
            if existing.get("identifier") != IDENTIFIER:
                raise SystemExit(f"{TARGET} already exists with another identifier")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, LAMASSU_PARENT)
    else:
        print(
            "Lamassu-Sir2 system trait and parent update validate; "
            f"rerun with --apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
