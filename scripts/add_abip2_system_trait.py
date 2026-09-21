"""Add the AbiP2 system genomics trait."""

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

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "abip2_system.yaml"
ABORTIVE = REPO_ROOT / "data" / "traits" / "genomics" / "abortive_infection_system.yaml"

ODEGRIP_ABIP2 = "DOI:10.1128/JB.188.4.1643-1647.2006"
MESTRE_UG_ABI = "DOI:10.1093/nar/gkac467"
FEMS_REVIEW = "DOI:10.1093/femsre/fuag009"
FIGIEL_ABI_POLYMERASES = "DOI:10.1093/nar/gkac772"

DEFENSEFINDER_COMMIT = "afb0e5a8b466be53586b13266f5d38d98c3ac268"
DEFENSEFINDER_PREFIX = (
    f"https://raw.githubusercontent.com/mdmparis/defense-finder-models/{DEFENSEFINDER_COMMIT}/"
)
DEFENSEFINDER_HMMS = f"{DEFENSEFINDER_PREFIX}Liste_hmm_system.md"
DEFENSEFINDER_RULES = f"{DEFENSEFINDER_PREFIX}DefenseFinder_rules.tsv"
DEFENSEFINDER_ARTICLES = f"{DEFENSEFINDER_PREFIX}List_system_article.md"

CURATOR = "codex"
TIMESTAMP = "2026-09-21T19:10:26Z"
PARENT_TIMESTAMP = "2026-09-21T19:10:27Z"
REVIEW_TIMESTAMP = "2026-09-21T19:50:08Z"
IDENTIFIER = "traitmech:000343"
PROPOSAL = "proposals/metpo_traitmech_v220"
GRAPH_ID = "abip2_locus_restricts_phage_propagation"

HMM_ROW = (
    "| AbiP2__AbiP2                                     | "
    "AbiP2__AbiP2                                     | AbiP2                  | "
    "Custom                  | 400    |"
)
RULES_ROW = "AbiP2\tAbiP2\t1\t1\tAbiP2__AbiP2\t\t\t"
ARTICLE_ROW = (
    r"| AbiP2 | 10\.1016/j\.mib\.2005\.06\.006 | "
    "Phage abortive infection in lactococci: variations on a theme |"
)

PARENT_EXPECTED_FRAGMENTS = (
    "AbiJ, AbiL, AbiN, and AbiO are split out as ",
    (
        "traitmech:000339, traitmech:000340, traitmech:000341, "
        "and traitmech:000342, respectively."
    ),
    "Deng et al., Prevots et al., and Prevots and Ritzenthaler still support",
    (
        "single-gene lactococcal AbiN loci, single-profile "
        "lactococcal AbiO loci, and other families."
    ),
)
PARENT_REPLACEMENTS = (
    (
        "AbiJ, AbiL, AbiN, and AbiO are split out as ",
        "AbiJ, AbiL, AbiN, AbiO, and AbiP2 are split out as ",
    ),
    (
        (
            "traitmech:000339, traitmech:000340, traitmech:000341, "
            "and traitmech:000342, respectively."
        ),
        (
            "traitmech:000339, traitmech:000340, traitmech:000341, "
            "traitmech:000342, and traitmech:000343, respectively."
        ),
    ),
    (
        "Deng et al., Prevots et al., and Prevots and Ritzenthaler still support",
        (
            "Deng et al., Prevots et al., Prevots and Ritzenthaler, "
            "and Odegrip et al. still support"
        ),
    ),
    (
        (
            "single-gene lactococcal AbiN loci, single-profile "
            "lactococcal AbiO loci, and other families."
        ),
        (
            "single-gene lactococcal AbiN loci, single-profile "
            "lactococcal AbiO loci, single-profile coliphage AbiP2 "
            "reverse-transcriptase-like loci, and other families."
        ),
    ),
)
PARENT_APPLIED_FRAGMENTS = tuple(new for _, new in PARENT_REPLACEMENTS)
PARENT_CHANGES = (
    "Documented AbiP2 as split out in the open abortive-infection "
    "subfamily split-gap discussion after minting traitmech:000343 for "
    "the AbiP2 system; other abortive-infection families remain open."
)


def odegrip_identity_evidence() -> dict[str, str]:
    return {
        "reference": ODEGRIP_ABIP2,
        "snippet": (
            "Identification of a Gene Encoding a Functional Reverse "
            "Transcriptase within a Highly Variable Locus in the P2-Like "
            "Coliphages"
        ),
        "notes": (
            "Crossref metadata verifies the Odegrip et al. 2006 primary "
            "P2-like-coliphage reverse-transcriptase paper title and DOI."
        ),
    }


def odegrip_t5_evidence() -> dict[str, str]:
    return {
        "reference": ODEGRIP_ABIP2,
        "snippet": (
            "The product of one of them exhibits reverse transcriptase "
            "activity and blocks infection of phage T5"
        ),
        "notes": (
            "The Odegrip et al. abstract supports a reverse-transcriptase "
            "gene in the P2-like-coliphage TO region that blocks phage T5."
        ),
    }


def mestre_family_evidence() -> dict[str, str]:
    return {
        "reference": MESTRE_UG_ABI,
        "snippet": (
            "UG/Abi: a highly diverse family of prokaryotic reverse "
            "transcriptases associated with defense functions"
        ),
        "notes": (
            "Mestre et al. describe the broad UG/Abi reverse-transcriptase "
            "family that the FEMS review places AbiP2 within."
        ),
    }


def fems_abip2_ug_abi_evidence() -> dict[str, str]:
    return {
        "reference": FEMS_REVIEW,
        "snippet": (
            "UG)/Abi RT group, which also includes AbiP2 from E. coli and "
            "other predicted RTs"
        ),
        "notes": (
            "The FEMS review explicitly places AbiP2 among UG/Abi reverse "
            "transcriptases rather than the unrelated lactococcal AbiP "
            "membrane-protein system."
        ),
    }


def figiel_abi_polymerase_evidence() -> dict[str, str]:
    return {
        "reference": FIGIEL_ABI_POLYMERASES,
        "snippet": "two Abi polymerases: AbiK and Abi-P2",
        "notes": (
            "Figiel et al. structurally characterize Abi-P2 as a "
            "template-independent Abi polymerase but do not resolve the "
            "in vivo phage trigger or infected-cell output."
        ),
    }


def rules_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_RULES,
        "snippet": RULES_ROW,
        "notes": (
            "The DefenseFinder rules table models AbiP2 as a one-component "
            "system requiring the AbiP2__AbiP2 profile."
        ),
    }


def hmm_inventory_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_HMMS,
        "snippet": HMM_ROW,
        "notes": (
            "The DefenseFinder HMM inventory records AbiP2__AbiP2 under "
            "the AbiP2 model namespace."
        ),
    }


def article_registry_triage_evidence() -> dict[str, str]:
    return {
        "reference": DEFENSEFINDER_ARTICLES,
        "snippet": ARTICLE_ROW,
        "notes": (
            "The pinned DefenseFinder article registry maps AbiP2 to a "
            "2005 lactococcal Abi review; that row is tracked as unresolved "
            "model-to-publication triage rather than positive AbiP2 primary "
            "literature evidence."
        ),
    }


RECORD: dict[str, Any] = {
    "identifier": IDENTIFIER,
    "label": "AbiP2 system",
    "definition": (
        "An abortive infection system in which an organism possesses a "
        "single-component AbiP2-family reverse-transcriptase-like locus "
        "represented by DefenseFinder as a mandatory AbiP2__AbiP2 profile."
    ),
    "definition_source": ODEGRIP_ABIP2,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000214"],
    "synonyms": [
        {
            "synonym_text": "AbiP2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_RULES,
        },
        {
            "synonym_text": "AbiP2__AbiP2",
            "synonym_type": "RELATED_SYNONYM",
            "source": DEFENSEFINDER_HMMS,
        },
    ],
    "evidence": [
        odegrip_identity_evidence(),
        odegrip_t5_evidence(),
        mestre_family_evidence(),
        fems_abip2_ug_abi_evidence(),
        figiel_abi_polymerase_evidence(),
        rules_evidence(),
        hmm_inventory_evidence(),
    ],
    "causal_graphs": [
        {
            "graph_id": GRAPH_ID,
            "title": "AbiP2 loci confer reverse-transcriptase-associated phage defense",
            "description": (
                "Conservative system-level sketch linking possession of a "
                "DefenseFinder AbiP2 locus to restricted bacteriophage "
                "propagation without asserting the unresolved phage trigger, "
                "protein-primed polymerase product, or host-arrest route."
            ),
            "scope_status": "NONMECHANISTIC",
            "scope_notes": (
                "The graph captures AbiP2 as a named single-profile "
                "reverse-transcriptase-like abortive-infection system with "
                "the DefenseFinder AbiP2__AbiP2 HMM while leaving its direct "
                "phage trigger, in vivo Abi-P2 polymerase product, UG/Abi "
                "family boundary, prophage host range, and cell-arrest or "
                "death route unresolved."
            ),
            "nodes": [
                {
                    "node_id": "abip2_locus",
                    "label": "AbiP2 locus",
                    "node_type": "GENETIC_ELEMENT",
                    "description": (
                        "An AbiP2-family abortive-infection locus "
                        "represented by the DefenseFinder AbiP2__AbiP2 "
                        "profile."
                    ),
                },
                {
                    "node_id": "restricted_phage_propagation",
                    "label": "restricted phage propagation",
                    "node_type": "BIOLOGICAL_PROCESS",
                    "description": (
                        "Reduced bacteriophage propagation in cells carrying "
                        "an AbiP2-family abortive-infection system."
                    ),
                },
                {
                    "node_id": "abip2_system_trait",
                    "label": "AbiP2 system",
                    "node_type": "TRAIT",
                    "grounding": IDENTIFIER,
                    "description": (
                        "Possession of a genome-encoded AbiP2 "
                        "abortive-infection phage-defense system."
                    ),
                },
                {
                    "node_id": "abortive_infection_system_trait",
                    "label": "abortive infection system",
                    "node_type": "TRAIT",
                    "grounding": "traitmech:000214",
                    "description": (
                        "Possession of a genome-encoded abortive-infection "
                        "phage-defense system."
                    ),
                },
            ],
            "edges": [
                {
                    "subject": "abip2_locus",
                    "predicate": "contributes to",
                    "predicate_id": "RO:0002326",
                    "object": "restricted_phage_propagation",
                    "description": (
                        "The DefenseFinder AbiP2 namespace is modeled as a "
                        "one-profile AbiP2__AbiP2 system, matching the "
                        "one-gene reverse-transcriptase-associated P2-like "
                        "coliphage defense architecture."
                    ),
                    "evidence": [
                        rules_evidence(),
                        hmm_inventory_evidence(),
                        odegrip_t5_evidence(),
                    ],
                },
                {
                    "subject": "restricted_phage_propagation",
                    "predicate": "confers",
                    "predicate_id": "METPO:2007700",
                    "object": "abip2_system_trait",
                    "description": (
                        "Restriction of phage propagation realizes the "
                        "AbiP2 abortive-infection system possession trait."
                    ),
                    "evidence": [odegrip_t5_evidence()],
                },
                {
                    "subject": "abip2_system_trait",
                    "predicate": "is a",
                    "predicate_id": "rdfs:subClassOf",
                    "object": "abortive_infection_system_trait",
                    "description": (
                        "AbiP2 system possession is an "
                        "abortive-infection-system trait."
                    ),
                    "evidence": [
                        odegrip_identity_evidence(),
                        fems_abip2_ug_abi_evidence(),
                    ],
                },
            ],
        }
    ],
    "discussions": [
        {
            "discussion_id": "abip2-ug-abi-mechanism-gap",
            "prompt": (
                "Resolve the AbiP2 natural locus breadth, phage trigger, "
                "protein-primed polymerase output, and growth-arrest or "
                "cell-death route before minting narrower AbiP2 mechanism "
                "children."
            ),
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Odegrip et al. support a P2-like-coliphage reverse "
                "transcriptase gene that blocks phage T5 infection, "
                "Mestre et al. describe the UG/Abi reverse-transcriptase "
                "family, the FEMS review places AbiP2 in that family "
                "rather than the unrelated lactococcal AbiP family, Figiel "
                "et al. structurally characterize Abi-P2 as a "
                "template-independent Abi polymerase, and DefenseFinder "
                "represents AbiP2 with a mandatory AbiP2__AbiP2 profile. "
                "This first system-level "
                "record therefore leaves the direct phage trigger, in vivo "
                "DNA product, exact relationship to broader UG/Abi systems, "
                "prophage host breadth, and growth-arrest or cell-death "
                "route unresolved."
            ),
            "evidence": [
                odegrip_t5_evidence(),
                mestre_family_evidence(),
                fems_abip2_ug_abi_evidence(),
                figiel_abi_polymerase_evidence(),
                rules_evidence(),
                hmm_inventory_evidence(),
            ],
            "attaches_to": [f"causal_graphs#{GRAPH_ID}"],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
        },
        {
            "discussion_id": "abip2-defensefinder-article-registry-gap",
            "prompt": (
                "Resolve the DefenseFinder AbiP2 article-registry mapping "
                "before using List_system_article.md as positive system "
                "literature evidence."
            ),
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The pinned DefenseFinder HMM inventory and rules table "
                "support AbiP2 as a one-profile model namespace, but its "
                "article registry row maps AbiP2 to a 2005 lactococcal "
                "abortive-infection review that predates Odegrip et al. "
                "2006. This record therefore leaves the registry-to-primary "
                "link unresolved and relies on Odegrip et al., Mestre et "
                "al., the FEMS review, Figiel et al., and pinned "
                "DefenseFinder HMM/rule rows for AbiP2 identity and system "
                "coverage."
            ),
            "evidence": [article_registry_triage_evidence()],
            "posed_by": CURATOR,
            "posed_date": "2026-09-21",
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

    discussion = next(
        item
        for item in record.get("discussions") or []
        if item.get("discussion_id") == "abortive-infection-subfamily-split-gap"
    )
    assert discussion["status"] == "OPEN"
    assert discussion["prompt"] == (
        "Resolve other abortive-infection families before minting narrower "
        "children under the broad abortive infection system parent."
    )
    if all(applied in discussion["rationale"] for applied in PARENT_APPLIED_FRAGMENTS):
        return record

    for expected in PARENT_EXPECTED_FRAGMENTS:
        assert expected in discussion["rationale"]
    assert IDENTIFIER not in discussion["rationale"]

    for old, new in PARENT_REPLACEMENTS:
        discussion["rationale"] = discussion["rationale"].replace(old, new, 1)

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
            "Minted AbiP2 system as a DOI-backed GENOMICS TraitRecord "
            "under the abortive infection system parent after an "
            "ignored-and-hidden duplicate review found no exact live "
            "TraitMech, METPO, history, or prior proposal record; the "
            f"replacement placeholder is reserved in {PROPOSAL}."
        ),
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADDRESS_PR_REVIEW",
        changes=(
            "Addressed review issues #1215 and #1216 by renaming the "
            "NONMECHANISTIC AbiP2 graph id to omit T5 specificity and by "
            "documenting the unresolved DefenseFinder article-registry row "
            "that maps AbiP2 to a 2005 lactococcal review."
        ),
        llm_assisted=True,
        timestamp=REVIEW_TIMESTAMP,
    )
    return record


def assert_same_target(record: dict[str, Any]) -> None:
    assert record["identifier"] == IDENTIFIER
    assert record["label"] == "AbiP2 system"
    assert record["mapping_status"] == "PROPOSED"
    assert record["parent_traits"] == ["traitmech:000214"]


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
            assert_same_target(load_trait(TARGET))
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, ABORTIVE)
    else:
        print(
            "AbiP2 system trait validates; rerun with --apply to write "
            f"{TARGET.relative_to(REPO_ROOT)} and update "
            f"{ABORTIVE.relative_to(REPO_ROOT)}."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
