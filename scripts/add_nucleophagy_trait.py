"""Add microbial nucleophagy and correct autophagy's nuclear-cargo scope."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/nucleophagy.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v514/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v519/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000643"
METPO_ID = "METPO:1059600"
PARENT_METPO_ID = "METPO:1059100"
TIMESTAMP = "2026-10-06T13:33:28Z"
PARENT_HASH = "ca93d09966ac81f73c0e02b59209429851989505381eeec97eb3f1c2eebff4bc"
TEMPLATE_HASH = "87e7687d6255ea0865bcf00968af244b26cb4f9ab3bd2d5dac8797d027ca777b"
PMN = "DOI:10.1091/mbc.e02-08-0483"
FOLLOWUP = "DOI:10.1091/mbc.e08-04-0363"
WHOLE = "DOI:10.1007/s00284-024-03838-y"
NONSELECTIVE = "DOI:10.1371/journal.pone.0033270"
REVIEW = "DOI:10.1242/jcs.133090"
OLD_DEFINITION = (
    "A physiological phenotype in which a microbial cell degrades cytoplasmic "
    "material, including its own constituents or intracellular non-self cargo, "
    "by delivering that material to lysosomal or vacuolar compartments."
)
NEW_DEFINITION = OLD_DEFINITION.replace("cytoplasmic material", "intracellular material")
WHOLE_SNIPPET = (
    "These results indicate that nuclei are engulfed in the autophagosomes as a "
    "whole and transported/released into the vacuolar lumen where they are degraded."
)
PARENT_EVIDENCE = {
    "reference": WHOLE,
    "snippet": WHOLE_SNIPPET,
    "notes": (
        "PMID:39162852, PMC11335778. Scientific Abstract directly read in Europe PMC "
        "with matching DOI. Selected XML Methods, Results and Discussion support "
        "including nuclear cargo within autophagy. The nucleophagy child retains "
        "the assay and access limits. This repairs cytoplasmic to intracellular "
        "in the parent definition (#1754), without imposing this macro route on "
        "all autophagy or changing its stable identity."
    ),
}
PARENT_SCOPE_ADDITION = (
    " Nuclear cargo is included: DOI:10.1007/s00284-024-03838-y supports "
    "whole-nucleus autophagy in Aspergillus oryzae. The former cytoplasmic-only "
    "wording was too narrow (#1754); intracellular corrects that wording, "
    "not the identity of autophagy. Nucleophagy traitmech:000643 is a "
    "cargo-defined child. The original definition source supports the retained "
    "vacuolar catabolic genus; the added evidence supports nuclear cargo."
)
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
RECORD = {
    "identifier": IDENTIFIER,
    "label": "nucleophagy",
    "definition": (
        "An autophagy phenotype in which a microbial cell degrades parts of "
        "its nucleus or an entire nucleus by delivering nuclear material "
        "to lysosomal or vacuolar compartments."
    ),
    "definition_source": WHOLE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000638"],
    "evidence": [
        {
            "reference": PMN,
            "snippet": (
                "During PMN, teardrop-like blebs are pinched from the nucleus, "
                "released into the vacuole lumen, and degraded by soluble hydrolases."
            ),
            "notes": (
                "PMID:12529432, PMC140233. Scientific Abstract directly read in "
                "Europe PMC with matching DOI. Saccharomyces cerevisiae nuclear "
                "portions undergo selective microautophagic turnover; Nvj1 "
                "degradation supports flux, not just bleb formation. The reported "
                "apg7-delta independence was revised by the 2008 follow-up, so "
                "it is not a universal absence-of-ATG requirement. Full-text "
                "retrieval failed; Methods, actual figures and strain provenance "
                "were not inspected."
            ),
        },
        {
            "reference": FOLLOWUP,
            "snippet": (
                "We conclude that a spectrum of ATG genes is required for the "
                "terminal vacuole enclosure and fusion stages of PMN."
            ),
            "notes": (
                "PMID:18701704, PMC2555948. Scientific Abstract directly read in "
                "Europe PMC with matching DOI. Two biochemical assays revise "
                "the older PMN dependence claim: atg mutants form blebs but "
                "rarely release vesicles into the vacuole. Formation, terminal "
                "enclosure and degradation are distinct readouts. This is a "
                "yeast PMN result, not a gene-inventory definition of all "
                "nucleophagy. Full-text retrieval returned HTTP 500; complete "
                "Methods and actual figures were not inspected."
            ),
        },
        {
            "reference": WHOLE,
            "snippet": WHOLE_SNIPPET,
            "notes": (
                "PMID:39162852, PMC11335778. Scientific Abstract directly read "
                "in Europe PMC; matching-DOI XML Methods Sec3/Sec6, Results "
                "Sec11/Sec12 and Discussion Sec13 read. Aspergillus oryzae "
                "H2B-EGFP processing and Atg1/Atg8/Ypt7/Atg15 perturbations "
                "distinguish whole-nucleus uptake, fusion and degradation. "
                "Residual carbon-starvation cleavage and possible "
                "sample-preparation proteolysis limit interpretation; "
                "complementation was incomplete. RIB40 was the DNA donor, "
                "not the assayed NSRku70-derived host; Aspergillus nidulans "
                "supplied the reporter, not the phenotype. Receptor speculation "
                "includes unpublished data. Figure captions, not actual figures "
                "or supplements, were inspected."
            ),
        },
        {
            "reference": NONSELECTIVE,
            "snippet": (
                "infection-associated nuclear degeneration in M. oryzae instead "
                "occurs by non-selective macroautophagy, which is necessary for "
                "rice blast disease."
            ),
            "notes": (
                "PMID:22448240, PMC3308974. Scientific Abstract directly read "
                "in Europe PMC and PLOS. Results on nuclear degeneration and "
                "macroautophagy were read. H1-RFP imaging and Atg1/Atg4 "
                "perturbations support infection-associated nuclear loss; "
                "MoVac8/MoTsc13 are dispensable for it. Some selective-autophagy "
                "mutant comparisons are data not shown. The 2024 study's "
                "Discussion includes this route under nucleophagy; retain "
                "that attributed usage, not a yeast PMN assignment. Actual "
                "figures, full Methods and independent strain provenance "
                "were not inspected."
            ),
        },
        {
            "reference": REVIEW,
            "snippet": (
                "A selective form of autophagy, known as nucleophagy, can be "
                "used to accomplish the degradation of nucleus-derived material."
            ),
            "notes": (
                "PMID:24013549. Scientific Abstract directly read in Europe PMC "
                "with matching DOI. This is a review supporting terminology, "
                "not an independent experiment. Its selective formulation is "
                "narrower than the 2024 Discussion's inclusion of nonselective "
                "Magnaporthe nuclear degradation. Preserve that scope question "
                "explicitly rather than imposing selectivity universally. "
                "Full text and poster were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "nucleophagy-cargo-route-and-selectivity",
            "prompt": "Review nuclear-cargo scope and source-specific selectivity.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Include nuclear portions and entire nuclei, micro and macro "
                "routes. The 2013 review defines nucleophagy as selective, "
                "whereas the 2024 Discussion includes the 2012 nonselective "
                "Magnaporthe route. The present cargo-defined phenotype does "
                "not require universal selectivity; preserve this attributed "
                "difference for human review. GO:0044804, resolved at "
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044804, "
                "is nonobsolete and includes nuclear parts or entire nuclei "
                "without an explicit selectivity restriction. Its biological "
                "process scope is not an exact organismal-phenotype xref. "
                "The autophagy parent traitmech:000638 is corrected to "
                "intracellular cargo in this change (#1754). Nuclear-envelope "
                "overlap with ER-phagy traitmech:000642 does not make the "
                "records equivalent. No exact synonyms or SSSOM mapping are "
                "asserted. Nuclear damage, loss of fluorescence or DNA "
                "degradation alone does not prove autophagic delivery and flux."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "nucleophagy-flux-exemplars-and-mechanism",
            "prompt": "Resolve native exemplars and route-specific mechanisms.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The microbial cell carrying out degradation has the phenotype, "
                "not a bacterium eliciting an animal-host response. Whole-nucleus "
                "turnover in multinucleate cells need not cause cell death. "
                "Do not equate blebs, puncta, inhibited autophagic bodies, "
                "gene presence or partial rate reductions with completed flux "
                "or total absence. The 2003/2008 PMN dependence conflict needs "
                "full-text assay reconciliation before protein-resolved causal "
                "claims. Canonical examples remain unset pending independent "
                "natural-strain provenance; do not infer origin from a mutant "
                "label. Native taxon-paired protein accessions and functional "
                "evidence are required before adding a causal graph."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def fingerprint(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parent_event() -> dict:
    holder = {}
    record_curation_event(
        holder, curator="codex", action="CURATED_WITH_LITERATURE",
        changes=(
            "Corrected cytoplasmic to intracellular cargo using whole-nucleus "
            "autophagy evidence (#1754). Retained autophagy identity, prior "
            "evidence and route/flux limits; added the nucleophagy child and "
            "corrected parent context in proposal v519."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return holder["curation_history"][0]


def prepare_parent(current: dict) -> dict:
    base = copy.deepcopy(current)
    if not isinstance(base, dict):
        raise SystemExit("Parent differs from reviewed preimage")
    if fingerprint(base) != PARENT_HASH:
        # Undo only this exact patch to recognize a replay, then recheck all fields.
        try:
            if not (
                base["definition"] == NEW_DEFINITION
                and base["evidence"][-1] == PARENT_EVIDENCE
                and base["curation_history"][-1] == parent_event()
                and base["discussions"][0]["rationale"].endswith(PARENT_SCOPE_ADDITION)
            ):
                raise ValueError("Not the reviewed result")
            base["evidence"].pop()
            base["curation_history"].pop()
            base["discussions"][0]["rationale"] = base["discussions"][0]["rationale"][:-len(PARENT_SCOPE_ADDITION)]
            base["definition"] = OLD_DEFINITION
        except (ValueError, KeyError, IndexError, TypeError, AttributeError):
            raise SystemExit("Parent differs from reviewed preimage or result") from None
        if fingerprint(base) != PARENT_HASH:
            raise SystemExit("Parent differs from reviewed preimage or result")
    result = copy.deepcopy(base)
    result["definition"] = NEW_DEFINITION
    result["evidence"].append(copy.deepcopy(PARENT_EVIDENCE))
    result["discussions"][0]["rationale"] += PARENT_SCOPE_ADDITION
    record_curation_event(result, **parent_event())
    return result


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added nuclear-cargo autophagy with five DOI-backed snippets, "
            "source-attributed selectivity and flux limits. Corrected its "
            "autophagy parent's cytoplasmic-only wording (#1754). Ignored-and-hidden "
            "novelty checks found no exact record; reserved METPO:1059600 in "
            "v519. Deferred unverified exemplars, mappings and protein graphs."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict, parent: dict, old_rows: list[list[str]]) -> str:
    parent_row = copy.deepcopy(old_rows[2])
    parent_row[2] = parent["definition"]
    parent_row[3] += "|" + WHOLE
    parent_row[9] = "Corrected nuclear-cargo scope (#1754); supersedes v514-v518 parent wording."
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/nucleophagy.yaml",
                  *[e["reference"] for e in record["evidence"]]]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Nuclear portions or whole nuclei; route and selectivity scope remains source-attributed.",
        IDENTIFIER,
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows([*HEADERS, parent_row, child])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = prepare_parent(yaml.safe_load(PARENT_PATH.read_text()))
    template = PARENT_PROPOSAL.read_bytes()
    if hashlib.sha256(template).hexdigest() != TEMPLATE_HASH:
        raise SystemExit("Parent proposal differs from reviewed context")
    old_rows = list(csv.reader(io.StringIO(template.decode()), delimiter="\t"))
    record = build_record()
    proposal = proposal_tsv(record, parent, old_rows)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(parent, Path(tmp) / PARENT_PATH.name)
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(parent, PARENT_PATH)
        write_validated_trait(record, TARGET)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
