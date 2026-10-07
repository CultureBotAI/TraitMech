"""Add fungal sclerotium formation with explicit developmental and identity limits."""

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
SLUG = "fungal_sclerotium_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v536/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000660"
METPO_ID = "METPO:1061300"
DENSITY = "DOI:10.1128/AEM.00565-08"
DEVELOPMENT = "DOI:10.3390/jof9070737"
MELANIZATION = "DOI:10.1016/j.micres.2019.126326"
TERMINOLOGY = "DOI:10.1128/spectrum.02084-21"
PLASMODIUM = "DOI:10.2478/s11658-007-0047-5"
TIMESTAMP = "2026-10-07T06:42:13Z"
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
    "label": "fungal sclerotium formation",
    "definition": (
        "A morphological phenotype in which a fungus forms compact mycelial "
        "resting bodies called sclerotia."
    ),
    "definition_source": DENSITY,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DENSITY,
            "snippet": (
                "Aspergillus flavus differentiates to produce asexual dispersing "
                "spores (conidia) or overwintering survival structures called sclerotia."
            ),
            "notes": (
                "Horowitz Brown et al. (2008), PMID:18658287, PMC2547031; "
                "scientific abstract retrieved through Europe PMC and checked "
                "against publisher/PMC HTML. The XML endpoint failed; full text "
                "was read as HTML. Introduction, growth/density Methods, first "
                "Results subsection, Table 1 and actual Figure 1 were inspected. "
                "NRRL 3357 was tested at 29 C for seven days in darkness on "
                "glucose minimal medium with sorbitol. Figure 1A reports log10 "
                "sclerotial dry mass per plate, not raw body counts despite "
                "the abstract's number wording. Density association does not "
                "identify the proposed quorum factor. Other figures, supplements "
                "and natural strain provenance were not inspected; no additional "
                "canonical example or universal LOX mechanism is inferred."
            ),
        },
        {
            "reference": DEVELOPMENT,
            "snippet": (
                "WT and \u0394SSA-178C formed black mature sclerotia on the "
                "colonies and at the rim of the Petri dishes"
            ),
            "notes": (
                "Wang et al. (2023), PMID:37504726, PMC10381867; full-text XML, "
                "Results 3.3. Methods 2.1/2.6, Discussion and actual Figures 3-4 "
                "were inspected. WT 1980 was observed on PDA at 20 C after "
                "10/15 days and on autoclaved carrot slices after 20 days. "
                "Colony photographs are Figure 3A; the Results' Figure 3B "
                "pointers for maturation are misplaced because 3B plots growth. "
                "Figure 4C/D report bodies and total air-dried mass per flask, "
                "not mass per body. Delayed maturation is not complete loss of "
                "formation; do not infer rescue of every cortex measurement or "
                "survival duration. Other figures and supplements were not inspected."
            ),
        },
        {
            "reference": MELANIZATION,
            "snippet": (
                "there are no structural differences in the three stages of "
                "formation of melanized and non-melanized sclerotium."
            ),
            "notes": (
                "2019 microscopy study, PMID:31493702; directly retrieved Europe "
                "PMC scientific abstract only. The authors report development "
                "on PDA and compare melanized/non-melanized Sclerotinia "
                "sclerotiorum structures by microscopy and histochemistry. "
                "This supports not requiring melanization in the definition; "
                "the quoted observation is not a claim of identical composition "
                "or preserved function in every respect. Full text, figures, "
                "supplements, the treatment producing non-melanized structures "
                "and strain provenance were not inspected. No canonical "
                "example or transcript-inferred biochemical pathway is asserted."
            ),
        },
        {
            "reference": TERMINOLOGY,
            "snippet": (
                "There are different types of sclerotia-like fungal structures, "
                "such as the true sclerotia, the pseudosclerotia, the small "
                "sclerotia, and the microsclerotia."
            ),
            "notes": (
                "2022 primary study, PMID:35080446, PMC8791194; Introduction "
                "read directly as full-text XML. This passage is a terminology "
                "classification, not a new experimental observation. The "
                "authors distinguish tissue organization, host-material "
                "incorporation and developmental origins across these forms. "
                "Preserve that attributed distinction rather than imposing "
                "one size, three-layer anatomy or pure-fungal composition on "
                "every usage. Detailed equivalence/subclass mapping remains "
                "unresolved. Experimental Results, figures, supplements and "
                "strain provenance were not inspected; no universal ROS "
                "mechanism or additional canonical example is claimed."
            ),
        },
        {
            "reference": PLASMODIUM,
            "snippet": (
                "Sclerotization only took place when the plasmodia were starved "
                "and very slowly dried."
            ),
            "notes": (
                "Krzywda et al. (2008; online 2007), PMID:17965965, PMC6275577; "
                "scientific abstract read directly in full-text XML. Fuligo "
                "septica forms a dormant plasmodial state also called a "
                "sclerotium. This nonfungal usage motivates the explicit fungal "
                "scope; it is not a mycelial exemplar or an exact synonym of "
                "this trait. The reported dehydration conditions and pigment/"
                "viability observations are not transferred to fungi. Methods, "
                "figures and natural-isolate provenance were not inspected."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:5180",
            "taxon_label": "Sclerotinia sclerotiorum",
            "reference": DEVELOPMENT,
            "note": (
                "Wild-type strain 1980 in Wang et al. (2023), Methods 2.1/2.6, "
                "Results 3.3 and actual Figures 3A/4, forms sclerotia under the "
                "tested PDA/carrot conditions. NCBI Taxonomy confirms the "
                "species label and rank. Independent primary Methods at "
                "https://doi.org/10.1128/AEM.67.1.75-81.2001 "
                "(PMID:11133430, PMC92519) explicitly identify isolate 1980 "
                "as originating from dry bean culls in western Nebraska, "
                "supplied by J. R. Steadman. That passage was read directly "
                "in PMC HTML; its cited original 1990 study was not retrieved. "
                "This URL supports provenance, not an extra formation "
                "observation. The example is not an SSA disruption/complementary "
                "mutant and does not assert the phenotype for every strain or condition."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-sclerotium-identity-and-mapping",
            "prompt": "Reconcile legacy labels and the scope of sclerotial structures.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The explicit fungal label excludes the dormant plasmodial "
                "usage in Fuligo. Retain phenotype METPO:1000059 rather than "
                "plant pathogen, black pigmented, fungal conidiation "
                "traitmech:000657 or chlamydospore formation traitmech:000658. "
                "The pinned ontology contains only deprecated bare-label "
                "sclerotia classes METPO:0000117, METPO:000118 and METPO:1000398, "
                "without definitions or replacement links. Their original "
                "scope is unresolved; do not silently reactivate them or "
                "assert equivalence to this organismal formation phenotype. "
                "Upstream review must reconcile that legacy. QuickGO resolves "
                "GO:1990045 as sclerotium development, a biological process "
                "rather than an exact organismal phenotype; no xref or SSSOM "
                "mapping is asserted. The 2022 source distinguishes true, "
                "small, pseudo- and microsclerotial structures. Whether these "
                "need separate subclasses or mappings requires further primary "
                "morphology review; no exact synonyms, universal size threshold, "
                "three-layer requirement or host-material exclusion is imposed."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
        {
            "discussion_id": "fungal-sclerotium-formation-and-function",
            "prompt": "Separate formation from maturation, survival and mechanism.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Initiation, maturation, persistence and germination are "
                "distinct readouts. Formation of a named resting body does "
                "not establish a particular dormancy duration, survival after "
                "stress or later germinability. Size, pigmentation, nutrient "
                "regime and density responses are not universal defining "
                "requirements. Do not infer plant pathogenicity, aflatoxin "
                "production or a sexual/asexual reproductive mode from "
                "formation alone. The SSA study separates delayed maturation "
                "from a complete block, and total mass per flask from body "
                "number. A causal graph awaits taxon-specific perturbation/"
                "complementation assessment, remaining figures/supplements "
                "and authority-verified protein accessions. Candidate gene "
                "possession or expression of ROS, pigmentation or signaling "
                "genes is not itself the formation phenotype."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-07",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal sclerotium formation with five directly checked "
            "source snippets, a provenance-qualified strain 1980 example and "
            "explicit legacy-identity, morphology and functional limits. "
            "Ignored-and-hidden searches found deprecated bare labels but "
            "no live exact formation trait. Reserved METPO:1061300 in v536; "
            "existing records unchanged and protein-level mechanism deferred."
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
         "Fungal formation phenotype; legacy sclerotia identities remain unresolved.",
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
