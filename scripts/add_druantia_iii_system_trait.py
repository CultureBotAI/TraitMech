"""Add the Druantia III system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "druantia_iii_system.yaml"
DRUANTIA_PARENT = REPO_ROOT / "data" / "traits" / "genomics" / "druantia_system.yaml"

WU_2026 = "DOI:10.64898/2026.05.12.724681"
BELL_2026 = "https://pmc.ncbi.nlm.nih.gov/articles/PMC12458937/"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"

CURATOR = "codex"
TIMESTAMP = "2026-10-03T00:37:00Z"
PARENT_TIMESTAMP = "2026-10-03T00:37:01Z"
CANONICAL_TIMESTAMP = "2026-10-03T00:37:02Z"
IDENTIFIER = "traitmech:000560"
DRUANTIA_PARENT_ID = "traitmech:000234"
PROPOSAL = "proposals/metpo_traitmech_v437"

DRUANTIA_LATE_SNIPPET = (
    "Druantia III is a late-acting defence where DruH is the likely infection "
    "sensor and DruE is a helicase-nuclease effector that engages "
    "ssDNA-containing replication intermediates"
)
DRUANTIA_COMPLETE_SNIPPET = (
    "we identified 6,885 bacterial genomes encoding complete Druantia III "
    "systems, defined by the presence of both DruE and DruH"
)
DRUANTIA_ATCC_8739_SNIPPET = (
    "Screening 66 phages that could form plaques on the double-deletion "
    "strain showed that the strain carrying only Druantia III exhibited at "
    "least modest protection (<0.01 EOP or <0.5 SFC) against 3 phages, "
    "whereas the strain carrying ARMADA Type II exhibited a much broader "
    "range of immunity, with at least modest protection observed against "
    "30 phages."
)
ARTICLE_ROW = (
    "| Druantia | 10\\.1126/science\\.aar4120 | Systematic discovery of "
    "antiphage defense systems in the microbial pangenome | "
)
DRUE_HMM_ROW = (
    "| Druantia__DruE_1                                 |"
    " Druantia__DruE_1                                 |"
    " Druantia               | Custom                  | 20     |"
)
DRUH_HMM_ROW = (
    "| Druantia_III__DruH                               |"
    " Druantia_III__DruH                               |"
    " Druantia_III           | Custom                  | 20     |"
)
DRUANTIA_IV_HMM_ROWS = (
    "| Druantia_IV__DruE4                               |"
    "                                                  |"
    " Druantia_IV            | Custom                  | 750    |\n"
    "| Druantia_IV__DruF4                               |"
    "                                                  |"
    " Druantia_IV            | Custom                  | 20     |\n"
    "| Druantia_IV__DruL                                |"
    "                                                  |"
    " Druantia_IV            | Custom                  | 100    |"
)
RULE_ROW = "Druantia\tDruantia_III\t2\t2\tDruantia_III__DruH, Druantia__DruE_1\t\t\t"
RULE_PARENT_SPAN = "Druantia\tDruantia_III\t2\t2"


def druantia_late_evidence() -> dict[str, str]:
    return {
        "reference": WU_2026,
        "snippet": DRUANTIA_LATE_SNIPPET,
        "notes": (
            "Wu et al. support the characterized Druantia III arrangement "
            "in which DruH likely senses infection and DruE acts as the "
            "helicase-nuclease effector."
        ),
    }


def druantia_complete_evidence() -> dict[str, str]:
    return {
        "reference": WU_2026,
        "snippet": DRUANTIA_COMPLETE_SNIPPET,
        "notes": (
            "Wu et al. support Druantia III as a recurring bacterial "
            "DruE/DruH system rather than a single engineered locus."
        ),
    }


def druantia_atcc_8739_evidence() -> dict[str, str]:
    return {
        "reference": BELL_2026,
        "snippet": DRUANTIA_ATCC_8739_SNIPPET,
        "notes": (
            "Bell et al. support native E. coli ATCC 8739 Druantia III "
            "protection in a deletion-resolved panel separating Druantia "
            "III from co-located ARMADA Type II activity."
        ),
    }


def article_registry_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps the broad "
            "Druantia model namespace to the Doron et al. microbial "
            "pangenome antiphage-system discovery paper."
        ),
    }


def drue_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": DRUE_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the shared "
            "Druantia__DruE_1 custom profile listed by the Druantia_III "
            "rule row."
        ),
    }


def druh_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": DRUH_HMM_ROW,
        "notes": (
            "The pinned DefenseFinder HMM inventory records the "
            "Druantia_III__DruH custom profile under the Druantia_III "
            "model namespace."
        ),
    }


def druantia_iv_hmm_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": DRUANTIA_IV_HMM_ROWS,
        "notes": (
            "The pinned DefenseFinder HMM inventory records "
            "Druantia_IV__DruE4, Druantia_IV__DruF4, and "
            "Druantia_IV__DruL under the Druantia_IV model namespace."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_ROW,
        "notes": (
            "The pinned DefenseFinder rules table models Druantia_III as a "
            "Druantia subsystem requiring two mandatory matches from "
            "Druantia_III__DruH and Druantia__DruE_1 and two genes overall."
        ),
    }


def rules_parent_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULE_PARENT_SPAN,
        "notes": (
            "The pinned DefenseFinder rules table places the Druantia_III "
            "subsystem under the Druantia system key with two mandatory "
            "matches and two genes required."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "Druantia III system",
    "definition": (
        "A Druantia system in which an organism possesses a genome-encoded "
        "DefenseFinder Druantia_III subtype locus represented by the "
        "Druantia_III rule row requiring both the Druantia_III__DruH and "
        "Druantia__DruE_1 profiles."
    ),
    "definition_source": DEFENSEFINDER_RULES,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [DRUANTIA_PARENT_ID],
    "synonyms": [
        {
            "synonym_text": "Druantia III",
            "synonym_type": "EXACT_SYNONYM",
            "source": WU_2026,
        },
        {
            "synonym_text": "Druantia_III",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "Druantia_III__DruH",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
        {
            "synonym_text": "Druantia__DruE_1",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        druantia_late_evidence(),
        druantia_complete_evidence(),
        druantia_atcc_8739_evidence(),
        article_registry_evidence(),
        drue_hmm_evidence(),
        druh_hmm_evidence(),
        rules_evidence(),
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:562",
            "taxon_label": "Escherichia coli",
            "note": (
                "Bell et al. screened E. coli ATCC 8739 system-deletion "
                "derivatives and observed at least modest phage protection "
                "in the derivative retaining only the native Druantia III "
                "system."
            ),
            "reference": BELL_2026,
        }
    ],
    "causal_graphs": [
        {
            "graph_id": "druantia_iii_locus_subtype_defense",
            "title": "Druantia III loci mark a DruH-dependent Druantia subtype",
            "description": (
                "Conservative subtype-level sketch linking a DefenseFinder "
                "Druantia_III locus to DruE/DruH-dependent Type III "
                "Druantia DNA processing, Druantia III system possession, "
                "and its Druantia parent."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures the Druantia_III subtype at "
                "DefenseFinder rule-row level without resolving the exact "
                "late phage trigger, DruH sensory intermediate, RecBCD "
                "dependence, Zorya II synergy, native host breadth beyond "
                "the E. coli ATCC 8739 observation, Type I, Type II, or "
                "Type IV partner functions, or whether every "
                "DefenseFinder Druantia_III prediction is a complete "
                "experimentally active locus."
            ),
            "nodes": [
                {
                    "node_id": "druantia_iii_locus",
                    "label": "Druantia III locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "A DefenseFinder Druantia_III subtype locus "
                        "represented by Druantia_III__DruH and "
                        "Druantia__DruE_1 profiles."
                    ),
                },
                {
                    "node_id": "druantia_iii_dna_processing",
                    "label": "Druantia III DruE/DruH DNA processing",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "DruE helicase-nuclease DNA processing in a "
                        "DruH-containing Type III Druantia context."
                    ),
                },
                {
                    "node_id": "druantia_iii_system_trait",
                    "label": "Druantia III system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded Druantia III phage-defense system."
                    ),
                },
                {
                    "node_id": "druantia_system_trait",
                    "label": "Druantia system",
                    "node_type": "TRAIT",
                    "grounding": DRUANTIA_PARENT_ID,
                    "description": (
                        "Possession of a genome-encoded Druantia phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "druantia_iii_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "druantia_iii_dna_processing",
                    "description": (
                        "Druantia_III loci are represented in DefenseFinder "
                        "by Druantia_III__DruH and Druantia__DruE_1, and Wu "
                        "et al. define complete Druantia III systems by the "
                        "presence of both DruE and DruH."
                    ),
                    "evidence": [
                        druantia_complete_evidence(),
                        drue_hmm_evidence(),
                        druh_hmm_evidence(),
                        rules_evidence(),
                    ],
                },
                {
                    "subject": "druantia_iii_dna_processing",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "druantia_iii_system_trait",
                    "description": (
                        "The first-pass Druantia III system trait is "
                        "realized by a DruE/DruH locus whose late defense "
                        "uses DruE helicase-nuclease effector activity."
                    ),
                    "evidence": [
                        druantia_late_evidence(),
                    ],
                },
                {
                    "subject": "druantia_iii_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "druantia_system_trait",
                    "description": ("Druantia III system possession is a Druantia-system trait."),
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
            "discussion_id": "druantia-iii-activity-gap",
            "prompt": (
                "Resolve Druantia_III phage triggers, DruH sensory "
                "chemistry, RecBCD and Zorya coupling, native host breadth, "
                "and profile-to-activity criteria before minting enzyme, "
                "trigger, or component children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Wu et al. support Druantia III as a recurring DruE/DruH "
                "system in which DruH is the likely infection sensor and "
                "DruE is a helicase-nuclease effector, and the pinned "
                "DefenseFinder HMM inventory and rules table support "
                "Druantia_III as a subtype whose rule row requires the "
                "Druantia_III__DruH and Druantia__DruE_1 profiles. Bell "
                "et al. support one deletion-resolved native E. coli ATCC "
                "8739 Druantia III protection observation. This first-pass "
                "record leaves exact late phage triggers, DruH sensory "
                "intermediates, RecBCD dependence, Zorya II coupling, "
                "native host breadth beyond ATCC 8739, and "
                "profile-to-activity criteria unresolved."
            ),
            "evidence": [
                druantia_late_evidence(),
                druantia_atcc_8739_evidence(),
                druh_hmm_evidence(),
                rules_evidence(),
            ],
            "attaches_to": [
                "causal_graphs#druantia_iii_locus_subtype_defense",
            ],
            "posed_by": CURATOR,
            "posed_date": "2026-10-03",
        }
    ],
}

OLD_DRUANTIA_DISCUSSION_PROMPT = (
    "Resolve Druantia subtype composition and activation mechanisms before "
    "minting narrower Type I, Type II, or Type III Druantia-system children."
)

UPDATED_DRUANTIA_DISCUSSION_PROMPT = (
    "Resolve Druantia Type I, Type II, Type IV, and cross-system activation "
    "mechanisms before minting additional narrower Druantia-system children."
)

OLD_DRUANTIA_DISCUSSION_RATIONALE = (
    "Doron et al. separated Type I DruABCDE, Type II DruMFGE, and Type III "
    "DruHE architectures and validated one Type I locus, while Wu et al. "
    "define a Type III mechanism in which DruH likely senses infection and "
    "DruE engages ssDNA-containing intermediates. The first TraitRecord "
    "therefore stays at the DruE-core family level until separate review "
    "resolves Type I/II partner functions, Type III-specific DruH "
    "activation, exact phage triggers, and Zorya-coupled versus standalone "
    "outputs across Druantia loci."
)

UPDATED_DRUANTIA_DISCUSSION_RATIONALE = (
    "Doron et al. separated Type I DruABCDE, Type II DruMFGE, and Type III "
    "DruHE architectures and validated one Type I locus, while Wu et al. "
    "define a Type III mechanism in which DruH likely senses infection and "
    "DruE engages ssDNA-containing intermediates. Druantia III system now "
    "captures the DruE/DruH Type III branch from the pinned Druantia_III "
    "DefenseFinder row, but the parent record remains at the DruE-core "
    "family level until separate review resolves Type I, Type II, and Type "
    "IV partner functions, exact phage triggers, native host breadth, and "
    "Zorya-coupled versus standalone outputs across Druantia loci."
)

TYPE_IV_GROUNDED_DRUANTIA_DISCUSSION_RATIONALE = (
    "Doron et al. separated Type I DruABCDE, Type II DruMFGE, and Type III "
    "DruHE architectures and validated one Type I locus, while Wu et al. "
    "define a Type III mechanism in which DruH likely senses infection and "
    "DruE engages ssDNA-containing intermediates. Druantia III system now "
    "captures the DruE/DruH Type III branch from the pinned Druantia_III "
    "DefenseFinder row, but the parent record remains at the DruE-core "
    "family level until separate review resolves Type I and Type II "
    "partner functions, Type IV partner functions represented by the "
    "pinned Druantia_IV HMM rows, exact phage triggers, native host "
    "breadth, and Zorya-coupled versus standalone outputs across Druantia "
    "loci."
)

PARENT_EVENT_CHANGES = (
    "Documented Druantia III as split out in the open Druantia subtype "
    "discussion after minting traitmech:000560 for the DefenseFinder-backed "
    "Druantia_III child; Type I, Type II, the pinned Druantia_IV HMM "
    "context, Zorya-coupled versus standalone activity, and finer Druantia "
    "activation mechanisms remain open."
)


def build_record() -> dict[str, Any]:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record,
        curator=CURATOR,
        action="MINTED_TRAITMECH_ID",
        changes=(
            "Minted Druantia III system as a DOI- and "
            "DefenseFinder-backed GENOMICS TraitRecord under the Druantia "
            "system parent after an ignored-and-hidden duplicate review "
            "found no exact live TraitMech, METPO, history, or prior "
            "proposal record for the target local ID, placeholder METPO "
            "ID, proposal cohort, record slug, human label, DefenseFinder "
            "subsystem, DruH profile, or shared DruE_1 profile; existing "
            "Druantia III mentions were supporting evidence on broad "
            "Druantia or ARMADA records, not an exact child TraitRecord, "
            f"and the replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="REVIEW_CANONICAL_EXAMPLE",
        changes=(
            "Reviewed Druantia III system during initial curation and "
            "added Escherichia coli because Bell et al. reported a "
            "deletion-resolved E. coli ATCC 8739 derivative retaining only "
            "native Druantia III activity with modest protection against "
            "3 of 66 screened phages. Broader native host breadth remains "
            "unresolved, and no paid research was used."
        ),
        llm_assisted=True,
        timestamp=CANONICAL_TIMESTAMP,
    )
    return record


def build_parent() -> dict[str, Any]:
    record = yaml.safe_load(DRUANTIA_PARENT.read_text())
    assert record["identifier"] == DRUANTIA_PARENT_ID
    assert record["label"] == "Druantia system"
    assert record["mapping_status"] == "PROPOSED"

    discussion = next(
        item
        for item in record["discussions"]
        if item["discussion_id"] == "druantia-subtype-mechanism-gap"
    )
    assert discussion["kind"] == "KNOWLEDGE_GAP"
    assert discussion["status"] == "OPEN"
    if discussion["prompt"] == OLD_DRUANTIA_DISCUSSION_PROMPT:
        discussion["prompt"] = UPDATED_DRUANTIA_DISCUSSION_PROMPT
    elif discussion["prompt"] != UPDATED_DRUANTIA_DISCUSSION_PROMPT:
        raise SystemExit("unexpected Druantia subtype discussion prompt")
    if discussion["rationale"] in {
        OLD_DRUANTIA_DISCUSSION_RATIONALE,
        UPDATED_DRUANTIA_DISCUSSION_RATIONALE,
    }:
        discussion["rationale"] = TYPE_IV_GROUNDED_DRUANTIA_DISCUSSION_RATIONALE
    elif discussion["rationale"] != TYPE_IV_GROUNDED_DRUANTIA_DISCUSSION_RATIONALE:
        raise SystemExit("unexpected Druantia subtype discussion rationale")
    discussion["evidence"] = [
        item
        for item in discussion.get("evidence", [])
        if item.get("snippet") != DRUANTIA_IV_HMM_ROWS
    ]
    discussion["evidence"].append(druantia_iv_hmm_evidence())

    parent_event = next(
        (
            event
            for event in record.get("curation_history", [])
            if event["timestamp"] == PARENT_TIMESTAMP and event["action"] == "TRACK_NARROWER_RECORD"
        ),
        None,
    )
    if parent_event is None:
        record_curation_event(
            record,
            curator=CURATOR,
            action="TRACK_NARROWER_RECORD",
            changes=PARENT_EVENT_CHANGES,
            llm_assisted=True,
            timestamp=PARENT_TIMESTAMP,
        )
    else:
        parent_event["changes"] = PARENT_EVENT_CHANGES
    return record


def validate_outputs(record: dict[str, Any], parent: dict[str, Any]) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        write_validated_trait(record, tmp_path / TARGET.name)
        write_validated_trait(parent, tmp_path / DRUANTIA_PARENT.name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build_record()
    parent = build_parent()
    validate_outputs(record, parent)

    if args.apply:
        if TARGET.exists():
            existing = yaml.safe_load(TARGET.read_text())
            if existing.get("identifier") != IDENTIFIER:
                raise SystemExit(f"{TARGET} already exists with another identifier")
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, DRUANTIA_PARENT)
    else:
        print(
            "Druantia III system trait and parent update validate; "
            f"rerun with --apply to write {TARGET.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
