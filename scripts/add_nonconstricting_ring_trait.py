"""Add evidence-backed fungal nonconstricting-ring trap formation."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
SLUG = "fungal_nonconstricting_ring_trap_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v556/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000680"
METPO_ID = "METPO:1063300"
MICROSCOPY = "DOI:10.1007/s102670200061"
TAXONOMY = "DOI:10.1016/j.mycres.2006.04.011"
TIMESTAMP = "2026-10-08T12:40:34Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "fungal nonconstricting-ring trap formation",
    "definition": (
        "A morphological phenotype in which a fungus forms stalked, three-celled "
        "hyphal rings that trap nematodes without inward inflation of the ring cells."
    ),
    "definition_source": MICROSCOPY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": MICROSCOPY,
            "snippet": (
                "A nonconstricting ring (arrow) is capturing a nematode (asterisk)."
            ),
            "notes": (
                "Saikawa and Takahashi (2002), Figure 8 caption, page 418; "
                "all three pages and actual Figures 1-20 directly inspected at "
                "https://www.jstage.jst.go.jp/article/mycosci/43/5/43_MYC43417/_pdf. "
                "Time-lapse microscopy distinguishes noninflating three-cell "
                "rings in Dactylella leptospora and Dactylaria candida from the "
                "inflating Arthrobotrys dactyloides comparator. Figures 8-14 "
                "and 15-20 show the former taxa; Figures 1-7 show the comparator. "
                "Hook-tip fusion lacks the opposing bud seen in that comparator; "
                "stalk lengths vary. Adhesive ultrastructure is attributed to "
                "Saikawa (1985), not newly imaged here. These morphological "
                "observations do not identify causal proteins."
            ),
        },
        {
            "reference": TAXONOMY,
            "snippet": "D. varietas forms both adhesive knobs and non-constricting rings",
            "notes": (
                "Li et al. (2006), scientific Abstract, directly retrieved as "
                "published abstract XML for PMID:16876699 at "
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                "db=pubmed&id=16876699&retmode=xml. Abstract-only access: full "
                "Methods and figures were not retrieved. The independent "
                "description of Dactylellina sichuanensis and D. varietas from "
                "China reports capture with knobs and nonconstricting rings. "
                "The quoted clause contrasts D. varietas with nontrapping "
                "Dactylella oxyspora. Co-occurring trap types are not disjoint "
                "organism categories. The sequence analyses concern taxonomy, "
                "not a sequence-predicted trapping phenotype; no current "
                "taxonomic equivalence for those new taxa is asserted."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:430499",
            "taxon_label": "Dactylellina leptospora",
            "reference": MICROSCOPY,
            "note": (
                "Source-named Dactylella leptospora, natural TGU orchard-soil "
                "isolate collected June 1998. Observed on water agar at "
                "18-22 degrees C with Rhabditis sp.; Figures 8-14 document "
                "capture and ring development. Live NCBI "
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                "db=taxonomy&id=430499 resolves rank species, exact label "
                "Dactylellina leptospora and synonym Dactylella leptospora. "
                "This is not a strain accession or an assertion about every "
                "isolate, universal culture conditions or field biocontrol."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "nonconstricting-ring-scope-and-parent",
            "prompt": "Resolve a closer trap-morphology parent without conflating cell shape.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Phenotype METPO:1000059 is a broad parent. Ring shaped "
                "METPO:1000680 concerns individual-cell geometry, not this "
                "multicellular trapping apparatus. Mycelial growth "
                "traitmech:000074 explicitly concerns bacteria; hyphal "
                "anastomosis traitmech:000605 concerns fusion. Distinguish "
                "nonconstricting traps from an immature constricting ring that "
                "has not yet acquired inflation competence, adhesive-net loops, "
                "unicellular knobs, columns and intracellular cytokinetic "
                "rings. A circular outline or nematophagous genus is not "
                "sufficient. No exact synonyms, xrefs, SSSOM equivalences or "
                "organism-level disjointness are asserted. Neighboring scope "
                "exclusions do not constitute unresolved groundings, and their "
                "closer-parent TODOs remain open."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "nonconstricting-ring-mechanism",
            "prompt": "Separate ring morphogenesis from adhesion and infection mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The observed developmental sequence is not evidence that a "
                "particular protein is necessary or sufficient. Formation, "
                "adhesion, capture, penetration and digestion are separate "
                "endpoints; formation alone does not guarantee capture in "
                "every condition. A protein-resolved causal graph needs "
                "direct perturbation/complementation evidence and taxon-paired "
                "accessions. Do not transfer inflation mechanisms from "
                "constricting rings or adhesion proteins from knobs and nets. "
                "No universal stalk length, detachment, induction medium or "
                "prey requirement is asserted; mechanism is deferred, not "
                "claimed absent."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal nonconstricting-ring trap formation with two primary "
            "DOI sources, contiguous source-checked snippets and a qualified "
            "natural-isolate example. Ignored-and-hidden main/worktree/open-PR "
            "checks support 000680 and v556 block 1063300-1063399. Separated "
            "morphology from molecular mechanism and species rank from strain "
            "identity. Existing records unchanged. Timestamp is observed UTC."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Three-cell noninflating trap formation; not immature constricting rings or cell shape.",
         IDENTIFIER],
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
