"""Add positive autotropism with directional emergence and extension evidence."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000604"
TARGET = ROOT / "data/traits/physiology/positive_autotropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v481"
ROBINSON = "DOI:10.1093/jxb/19.1.125"
RICHTER = "DOI:10.1039/d3lc00859b"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "positive autotropism",
    "definition": (
        "A phenotype in which germ-tube emergence or hyphal extension is "
        "directionally biased toward neighboring cells or hyphae of the same species."
    ),
    "definition_source": ROBINSON,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": ROBINSON,
            "snippet": (
                "the positive germ-tube, i.e. one beginning more nearly towards its neighbour"
            ),
            "notes": (
                "Robinson, Park and Graham (1968), original publisher abstract "
                "directly retrieved from "
                "https://oup.silverchair-cdn.com/article-minimal/447341. The "
                "abstract reports positive autotropism in Botrytis cinerea on "
                "Cellophane over agar and neutrality on agar alone. The quoted "
                "orientation definition occurs in the mixed-orientation spore-pair "
                "timing comparison for Rhizopus stolonifer and Mucor plumbeus, "
                "both described as exhibiting marked negative autotropism. "
                "Earlier emergence of the positive germ-tube in those pairs "
                "does not establish a net positive response in either species. "
                "The abstract defines positive germ-tube orientation relative "
                "to the neighboring spore. This supports "
                "the terminology and emergence component, not later tip bending "
                "or completed fusion. Germination timing and cis-ness are "
                "separate readouts. The full paper, strain provenance and "
                "sample sizes were not retrieved. No universal chemical "
                "mechanism is inferred from the abstract's proposed explanations."
            ),
        },
        {
            "reference": RICHTER,
            "snippet": (
                "The hyphae approach each other from opposing directions with "
                "occasional arrestation of growth and readjustment of the growth direction."
            ),
            "notes": (
                "Richter et al. (2024), Results section on stop-and-go growth "
                "before anastomosis; directly retrieved Europe PMC full-text "
                "JATS, PMC10964749 (PMID:38416560). Culture and image-analysis "
                "methods, corresponding Discussion and actual Figure 5 were "
                "inspected. Figure 5a-c shows Rhizophagus irregularis MUCL 43194 "
                "approaching before fusion; the 21-hour trace is a representative "
                "pair, not a replication count. This is independent extension "
                "evidence interpreted within the directional definition, not "
                "an assertion that this paper uses the autotropism label. "
                "Supplementary methods and movies were not retrieved; attachment "
                "requests returned access-check HTML or HTTP errors."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "positive-autotropism-direction-and-fusion-scope",
            "prompt": "Retain the distinction between directional approach and fusion.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Initial germ-tube orientation and later hyphal redirection are "
                "distinct readouts; the definition does not require both in "
                "one organism. Hyphal fusion/anastomosis is a separate endpoint, "
                "not an exact synonym or a prerequisite. Same-species neighbors "
                "can include branches of one mycelium or separate spores; "
                "genetic identity is not required by this definition. Do not "
                "infer whole-cell taxis, chemotropism, mating or a particular "
                "self-recognition mechanism. Passive alignment, faster growth "
                "and contact alone are insufficient. Negative autotropism has "
                "the opposite direction, not the same phenotype. Resolve "
                "external equivalences before adding xrefs or synonyms."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "positive-autotropism-provenance-and-mechanism",
            "prompt": "Verify strain origins, supplements and native signaling mechanisms.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Canonical examples await original strain-provenance and NCBI "
                "identity checks. The 2024 culture method uses transformed "
                "chicory roots; this does not establish engineering of the "
                "fungi. Inspect the original supplements and the 1968 full "
                "paper before quantitative or strain-level enrichment. No "
                "universal ligand/receptor chain is established by these "
                "observations. A causal graph requires directly supported "
                "native perturbations and taxon-paired protein accessions; "
                "NONMECHANISTIC is not a grounding bypass."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added positive autotropism with two directly retrieved DOI-backed "
            "sources and exact snippets. Distinguished orientation and extension "
            "from completed fusion. Ignored-and-hidden searches and structured "
            "OWL review found no exact term; the negative sibling's boundary "
            "mention is not a duplicate. Reserved METPO:1055800 in v481 under "
            "released phenotype. Inspected Figure 5 and retained abstract-only, "
            "representative-pair and unread-supplement limitations. Deferred "
            "canonical strains, synonyms, external equivalents and causal graphs."
        ),
        llm_assisted=True, timestamp="2026-10-04T21:04:32Z",
    )
    record_curation_event(
        record, curator="codex", action="REFINE_EVIDENCE_SNIPPET",
        changes=(
            "Addressed #1687 by replacing the anaphoric label-only 1968 quote "
            "with its exact germ-tube orientation definition. Qualified the "
            "mixed-orientation timing comparison without inferring net positive "
            "autotropism in its two negative-response species. Retained the "
            "separate Botrytis cinerea substrate-dependent observation."
        ),
        llm_assisted=True, timestamp="2026-10-04T21:35:35Z",
    )
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow([
        "proposed_id", "label", "definition", "definition_source", "parent",
        "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed",
    ])
    writer.writerow([
        "ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
        "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
        "A oboInOwl:inSubset", "", "", "",
    ])
    writer.writerow([
        "METPO:1055800", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/positive_autotropism.yaml|{ROBINSON}|{RICHTER}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Directional approach; emergence and extension are distinct from fusion.",
        IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from this writer")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
