"""Add oogamy and extend the anisogamy proposal without changing its original row."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

import qualify_anisogamy_scope as parent_writer
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/oogamy.yaml"
PARENT = ROOT / "data/traits/physiology/anisogamy.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v497/metpo_proposal_classes_robot.tsv"
PARENT_SHA = "6f1ac7675c99f0e9475531b5432f046a653541e75a7579110dd6b2997c73f520"
PROPOSAL_SHA = "6c8cf24e123738a38e2df3bb2e4ba4b9520d0700aea03bfb5aa1c00c86690ff6"
IDENTIFIER = "traitmech:000621"
VRANKEN_2023 = "DOI:10.5194/essd-15-2711-2023"
LINDSEY_2024 = "DOI:10.1186/s12915-024-01878-1"
NOZAKI_2018 = "DOI:10.1186/s40529-018-0227-9"
GENG_2014 = "DOI:10.1371/journal.pbio.1001904"
OLD_SCOPE = "Verify any future oogamy child and lexical/external mappings before adding them."
NEW_SCOPE = (
    "Oogamy traitmech:000621 now supplies the size-dimorphic child with large "
    "nonmotile female gametes. Its evidence explicitly preserves nonmotile male "
    "exceptions rather than imposing a universal motility convention. Verify "
    "lexical/external mappings and a narrower reproductive parent before adding them."
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "oogamy",
    "definition": (
        "A sexual-reproduction phenotype in which large nonmotile female gametes "
        "fuse with smaller male gametes."
    ),
    "definition_source": VRANKEN_2023,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000620"],
    "evidence": [
        {
            "reference": VRANKEN_2023,
            "snippet": (
                "smaller motile male gametes with flagella (oogamous), except for "
                "red algae in which the male gamete is also non-motile."
            ),
            "notes": (
                "Vranken et al. (2023), Figure 2 caption, directly checked in "
                "publisher HTML and the actual figure. The full caption defines "
                "oogamy with a larger nonmotile female gamete and explicitly allows "
                "nonmotile red-algal male gametes. Thus male motility is not a "
                "universal requirement. This seaweed trait compilation supports "
                "terminology, not an independent microbial experiment or a canonical "
                "macroalgal example. The gamete-type paragraph and inheritance "
                "policy were also read: some species fields inherit genus data. "
                "Other actual figures, the data release and survey sheets remain "
                "uninspected. The figure is a life-cycle diagram, not measured "
                "gamete sizes; no numerical ratio is inferred."
            ),
        },
        {
            "reference": LINDSEY_2024,
            "snippet": (
                "Oogamy constitutes a specialized form of anisogamy wherein small "
                "male gametes are motile and large female gametes are not"
            ),
            "notes": (
                "Lindsey et al. (2024), PMID:38600528, PMC11007952, Background "
                "Sec1 clause before the parenthetical, verified in raw XML and "
                "publisher HTML. Supports the anisogamy parent and usual motile-"
                "male formulation, not a universal rule in view of Vranken et al. "
                "The scientific abstract and scope paragraph were read; remaining "
                "analyses, actual figures and supplements were not audited. This "
                "terminology passage is not independent experimental replication."
            ),
        },
        {
            "reference": NOZAKI_2018,
            "snippet": (
                "Volvox carteri f. nagariensis is an oogamous species that has "
                "heterothallic sexuality"
            ),
            "notes": (
                "Nozaki et al. (2018), PMID:29616358, PMC5882469, exact Background "
                "clause checked in raw XML. Scientific abstract, Background, Methods, "
                "Results, Discussion, Table 1 with row spans, captions and actual "
                "Figure 2 were inspected. Panels a-d show male spheroids/sperm "
                "packets, e female eggs, f-g mature zygotes. The Results qualify "
                "zygote formation as after possible fertilization; individual "
                "gamete fusion was not directly tracked. Do not compare packet "
                "size with egg size as a gamete-size ratio. Reference strains "
                "were induced in VTAC at 25 C with a 14:10 light-dark cycle; "
                "sexual spheroids formed after 2-4 days. Table 1's sex column is "
                "PCR-based, not 33 independent phenotype experiments. Failure to "
                "amplify HMG1f in another strain does not demonstrate deletion: "
                "primer polymorphism remains an explicit alternative. Other actual "
                "figures, Table 2 and supplements remain uninspected. Heterothallism "
                "describes this example, not all oogamy."
            ),
        },
        {
            "reference": GENG_2014,
            "snippet": (
                "Transgenic female V. carteri expressing male MID produced "
                "functional sperm packets during sexual development."
            ),
            "notes": (
                "Geng et al. (2014), PMID:25003332, PMC4086717, scientific-abstract "
                "sentence checked in raw XML. The scientific abstract, selected "
                "Introduction/Results/Methods passages, actual Figure 2 with its "
                "caption and all extracted Table S3 text were inspected. Figure "
                "2B/C/F/H show wild-type egg/sperm controls; D/E/G/I are engineered "
                "pseudo-males. Table S3 distinguishes Eve (UTEX 1885) and AichiM "
                "(NIES-398) from nitA- derivatives E15 and A18 used to generate "
                "transgenics. Table S3 was text-extracted, not visually rendered; "
                "remaining source material was not fully audited. MID gain/loss "
                "supports gamete-development causality in the tested backgrounds, "
                "not a universal oogamy mechanism or a natural canonical exemplar "
                "for the engineered strains. Resolve native protein accessions "
                "before a protein-grounded causal graph."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:3068",
            "taxon_label": "Volvox carteri f. nagariensis",
            "reference": NOZAKI_2018,
            "note": (
                "Source-observed reference example, not every strain. Natural "
                "Taiwan isolates female 2016-0609-v-1 (NIES-4206) and male "
                "2016-tw-nuk-6-1 (NIES-4208) were examined after sex-inducer "
                "treatment; see Figure 2, Table 1 and Methods. The Results describe "
                "zygotes after possible fertilization, not directly tracked fusion "
                "of each pair. Primary collection records at "
                "https://mcc.nbrp.jp/strainList.do?strainNumber=NIES-4206 and "
                "https://mcc.nbrp.jp/strainList.do?strainNumber=NIES-4208 confirm "
                "strain aliases, sex and ITS2 accessions LC376032/LC376034. Both "
                "list collection on 2016-05-25, whereas Table 1 lists 2016-06-09 "
                "and 2016-06-10 respectively (the collection records' isolation "
                "dates). This collection-date conflict remains unresolved; no "
                "date is silently corrected. Their March 2022 axenic status is "
                "not projected onto 2018. Collection fields establish provenance, "
                "not independent phenotype replication or an unmutated genome. "
                "The forma-level name and NCBITaxon:3068 were checked at "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3068 "
                "on 2026-10-05; no reference genome is assigned to these isolates."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "oogamy-scope-and-motility",
            "prompt": "Keep gamete-size asymmetry distinct from universal male motility.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use anisogamy traitmech:000620 in its explicit broad size-based "
                "sense, as in Lindsey et al. (2024), even though some sources "
                "separate motile-both anisogamy from oogamy. Vranken et al. (2023) "
                "explicitly include nonmotile male red-algal gametes. Large and "
                "small compare gamete types, not vegetative cells or sperm packets; "
                "no numerical size cutoff, fixed gamete count, fertilization "
                "location, monoecy/dioecy or mating-system requirement is imposed. "
                "Physiological anisogamy without size dimorphism is not equivalent. "
                "No organism-level disjointness is asserted. Verify external "
                "equivalences and lexical synonyms before adding mappings."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "oogamy-mechanism-and-provenance",
            "prompt": "Resolve protein groundings and strain metadata before mechanism expansion.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Oogamy is a gamete phenotype, not a MID/MAT sequence feature. "
                "The 2014 MID perturbations support sex-development causality "
                "in particular engineered backgrounds; they do not by themselves "
                "supply a universal mechanism for size asymmetry and female "
                "immotility. Resolve accessions and remaining source material "
                "before graph construction; no NONMECHANISTIC graph bypasses "
                "this gap. Do not turn 2018 PCR absence into demonstrated deletion "
                "or transfer the separate strain's failed crosses to all reference "
                "crosses. Preserve the collection-date discrepancy and later "
                "axenic status explicitly. Retain actual abstract-resolver "
                "verdicts separately from manual full-text source checks."
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
            "Added oogamy with four DOI-backed verbatim snippets, a qualified "
            "natural Volvox example and explicit male-motility exceptions. "
            "Ignored-and-hidden novelty/allocation searches found no exact record "
            "or collision. Extended v497 with METPO:1057410 under anisogamy "
            "METPO:1057400; deferred unverified mappings and causal mechanisms."
        ),
        llm_assisted=True, timestamp="2026-10-05T14:12:03Z",
    )
    return record


def build_parent(before: dict) -> dict:
    record = copy.deepcopy(before)
    scope = record["discussions"][0]
    if (record["identifier"] != "traitmech:000620" or record["label"] != "anisogamy"
            or record["mapping_status"] != "PROPOSED"
            or record["parent_traits"] != ["METPO:1000059"]
            or scope["discussion_id"] != "anisogamy-scope-and-hierarchy"
            or scope["status"] != "OPEN" or scope["rationale"].count(OLD_SCOPE) != 1):
        raise SystemExit("Parent scope differs from reviewed preimage")
    scope["rationale"] = scope["rationale"].replace(OLD_SCOPE, NEW_SCOPE)
    record_curation_event(
        record, curator="codex", action="LINKED_NARROWER_TRAIT",
        changes=(
            "Replaced the future oogamy-child TODO with traitmech:000621 and its "
            "qualified motility scope. Preserved the broad size-based definition, "
            "evidence, canonical example, parent and remaining open mapping questions."
        ),
        llm_assisted=True, timestamp="2026-10-05T14:12:03Z",
    )
    return record


def proposal_tsv(record: dict) -> str:
    original = parent_writer.proposal_tsv()
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerow([
        "METPO:1057410", record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/oogamy.yaml"]
                 + [e["reference"] for e in record["evidence"]]),
        "METPO:1057400", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Large nonmotile female gametes and smaller male gametes; male motility is not universal.",
        IDENTIFIER,
    ])
    return original + stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not PARENT.exists() or not PROPOSAL.exists():
        raise SystemExit("Missing reviewed parent or proposal preimage")
    before = yaml.safe_load(PARENT.read_text())
    expected_parent = build_parent(parent_writer.build_record())
    record = build_record()
    proposal = proposal_tsv(record)
    if before == expected_parent:
        parent = before
    elif hashlib.sha256(PARENT.read_bytes()).hexdigest() == PARENT_SHA:
        parent = build_parent(before)
    else:
        raise SystemExit("Existing parent differs from reviewed preimage or result")
    if (PROPOSAL.read_text() != proposal
            and hashlib.sha256(PROPOSAL.read_bytes()).hexdigest() != PROPOSAL_SHA):
        raise SystemExit("Existing proposal differs from reviewed preimage or result")
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(parent, Path(tmp) / PARENT.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, PARENT)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
