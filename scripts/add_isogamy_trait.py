"""Add isogamy without conflating similar gamete size with complete symmetry."""

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

IDENTIFIER = "traitmech:000619"
TARGET = ROOT / "data/traits/physiology/isogamy.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v496"
INNAMI_2022 = "DOI:10.1038/s42003-022-04275-y"
SEED_2018 = "DOI:10.1111/evo.13427"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "isogamy",
    "definition": (
        "A sexual-reproduction phenotype in which the fusing gametes are "
        "similar in size."
    ),
    "definition_source": INNAMI_2022,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": INNAMI_2022,
            "snippet": "The gametes of isogamous species are of similar size and appearance.",
            "notes": (
                "Innami et al. (2022), PMID:36473948, PMC9726906. Exact Introduction "
                "Sec1 sentence checked against raw Europe PMC XML and publisher HTML; "
                "not an abstract or web-summary quote. The paper identifies "
                "Chlamydomonas reinhardtii as isogamous while testing mating-structure "
                "positioning, not the maintenance of equal gamete size. Similar "
                "appearance does not exclude mating-type-specific structural or "
                "functional differences. Main text and captions were read; actual "
                "Figure 4 and Supplementary Table 2 were visually inspected. The "
                "latter lists nit1 nit2 in CC-125 and nit1 nit2 agg1 in CC-124 despite "
                "their wild-type names. CC-3712 has a deletion including MID and "
                "lacks FUS1; CC-3947 carries a MID transgene. These are qualified "
                "laboratory observations, not unqualified natural exemplars. Other "
                "actual figures, supplementary figures and the source-data workbook "
                "remain uninspected. Phototactic fitness explanations in Discussion "
                "remain hypotheses, not measured consequences of isogamy."
            ),
        },
        {
            "reference": SEED_2018,
            "snippet": (
                "we explored size-speed distributions in vegetative and gamete cells "
                "of 10 cell lines, and clonal data from within two cell lines."
            ),
            "notes": (
                "Seed and Tomkins (2018), PMID:29345308. Exact scientific-abstract "
                "clause from raw Europe PMC metadata; the author's institutional "
                "repository abstract corroborates the content. Its preceding clause "
                "identifies C. reinhardtii as isogamous. This independently supports "
                "experimental use of an isogamous microalga, not a second direct test "
                "of the definition's size-symmetry criterion. The two cell types are "
                "vegetative cells and gametes, not plus and minus gametes. Positive "
                "size-speed relationships and artificial speed selection do not "
                "establish a universal size threshold, identical gamete behaviour, "
                "or an evolutionary cause of isogamy. Full text, figures, supplements "
                "and strain provenance remain uninspected; the linked author "
                "manuscript returned HTTP 403."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "isogamy-scope-and-hierarchy",
            "prompt": "Keep gamete-size similarity distinct from mating-type identity.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This reproductive phenotype compares gametes participating in sexual "
                "fusion, not arbitrary equal-sized cells or vegetative-versus-gamete "
                "measurements. Similar size is not exact equality and does not imply "
                "identical structure, behaviour, recognition machinery or organelle "
                "inheritance. No numerical boundary with slight anisogamy is imposed. "
                "The fungal compatibility-locus systems traitmech:000615 through "
                "traitmech:000618 and same-mating-type reproduction traitmech:000613 "
                "describe different axes; isogamy does not mean one mating type. "
                "Use released phenotype METPO:1000059 in record and proposal pending "
                "a narrower reproductive-phenotype hierarchy. PHYSIOLOGY is a "
                "filesystem category. Resolve exact lexical and external equivalences "
                "before adding synonyms or xrefs; no disjointness is asserted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "isogamy-examples-and-mechanism",
            "prompt": "Resolve natural strain provenance and mechanisms before extension.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The cited microalgal studies justify the trait, but collection "
                "provenance and unperturbed gamete measurements should be checked "
                "before adding a natural canonical example. A wild-type label alone "
                "does not establish that a reference strain lacks mutations. Do not "
                "turn MID-dependent mating-structure positioning into a demonstrated "
                "cause of gamete-size similarity. Resolve native protein accessions "
                "and experimentally tested size-control dependencies before a causal "
                "graph; no NONMECHANISTIC graph bypasses grounding. Read the remaining "
                "source material before quantitative or evolutionary extensions. "
                "Keep full-text quote checks distinct from abstract-resolver verdicts."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added isogamy with two primary DOI-backed sources and exact full-text "
            "and scientific-abstract snippets. Kept gamete-size similarity distinct "
            "from structural symmetry, mating-type identity and sequence features. "
            "Ignored-and-hidden novelty and allocation searches found no exact "
            "record or collision. Reserved METPO:1057300 in v496 under phenotype. "
            "Deferred natural canonical taxa, lexical mappings and causal graphs, "
            "with strain mutations and source-access limits explicit."
        ),
        llm_assisted=True, timestamp="2026-10-05T11:50:56Z",
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
        "METPO:1057300", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/isogamy.yaml|{INNAMI_2022}|{SEED_2018}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Similar gamete size; not identical structure, one mating type or a sequence feature.",
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
