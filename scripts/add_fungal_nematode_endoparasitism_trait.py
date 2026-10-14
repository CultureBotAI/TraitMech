"""Add fungal nematode endoparasitism through guarded validated writes."""

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
SLUG = "fungal_nematode_endoparasitism"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/ecology/animal_pathogen.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v603/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000727"
METPO_ID = "METPO:1068000"
TIMESTAMP = "2026-10-14T15:19:28Z"
DEFINITION_SOURCE = "DOI:10.1371/journal.pgen.1006017"
INTERNAL_GROWTH_SOURCE = "DOI:10.3390/jof10010068"
INGESTION_SOURCE = "DOI:10.1017/S0953756296002092"
PARENT = {
    "identifier": "METPO:1004002",
    "label": "animal pathogen",
    "definition": "A pathogen that infects organisms in the kingdom Metazoa.",
    "definition_source": "DOI:10.1146/annurev.micro.62.081307.162938",
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1004000"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "fungal nematode endoparasitism",
    "definition": (
        "An animal-pathogenic phenotype in which a fungus uses spores attached "
        "to or ingested by a vermiform nematode to initiate infection and then "
        "grows inside the host."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": (
                "Drechmeria coniospora is an obligate fungal pathogen that infects "
                "nematodes via the adhesion of specialized spores to the host cuticle."
            ),
            "notes": (
                "Lebrigand et al. 2016, PMID:27153332, PMCID:PMC4859500, scientific "
                "Abstract. Direct JATS match and native VERIFIED. Author Summary "
                "and Discussion distinguish spore-initiated endoparasitism from "
                "hyphal traps and egg infection. Actual Figures 8 and 9 show "
                "recombinant fungal growth in C. elegans, not unmodified natural "
                "exemplars. S1 Text was fully read and visually checked: the "
                "laboratory line was serially passaged for about 15 years; its "
                "source isolate and ARSEF 6962 share provenance. Obligate is the "
                "authors' species description, not a universal class requirement "
                "or inability to grow on their artificial medium. Predicted genes "
                "and expression are not a universal mechanism."
            ),
        },
        {
            "reference": INTERNAL_GROWTH_SOURCE,
            "snippet": (
                "Then, the fungal hyphae penetrate into the nematode body cavity "
                "and grow in the nematode body"
            ),
            "notes": (
                "Sun et al. 2024, PMID:38248977, PMCID:PMC10820206, Results 3.2. "
                "Direct JATS match; native NOT_IN_ABSTRACT retained. Methods 2.5 "
                "and actual Figure 2c,d concern GFP-engineered HR-eGFP1 on "
                "Bursaphelenchus xylophilus; Figure 2 distinguishes attachment, "
                "entry, internal growth and emergence. The entire two-page "
                "supplement, including S1-S3, was inspected. Methods 2.6 scores "
                "attached spores or colonization as parasitism; no rate is "
                "imported as an internal-infection rate. Main-text intestinal "
                "infection after swallowing is tentative; do not silently "
                "strengthen it using the supplement caption. No field efficacy "
                "or safety is inferred."
            ),
        },
        {
            "reference": INGESTION_SOURCE,
            "snippet": (
                "The infection method for Harposporium cycloides was shown to "
                "be by spore ingestion."
            ),
            "notes": (
                "Glockling and Shimazu 1997, publisher scientific Abstract. "
                "Direct contiguous HTML match; DOI/title confirmed by Crossref "
                "and Europe PMC AGR:IND20619532. The native abstract resolver "
                "returned UNRESOLVED because it returned no abstract; this is "
                "not a missing-index claim. The primary abstract reports "
                "spore-ingestion infection in Harposporium cycloides and "
                "infectivity testing after pure culture. Full Methods, figures "
                "and host/strain provenance were not accessed; no canonical "
                "taxon, dose, route universality or pure-culture obligacy is inferred."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-nematode-endoparasitism-scope-and-hierarchy",
            "prompt": "Refine the infection-strategy hierarchy without conflating infection, trapping and feeding.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The fungal bearer has the established spore-infection-strategy "
                "phenotype, not merely an anatomical location inside a nematode. "
                "The host-contacting or ingested spore is the infectious unit; "
                "spore germination into an external hyphal trap is not this "
                "route. Adhesion or ingestion alone, killing alone, internal "
                "occupancy without the specified route and sequence annotation "
                "are insufficient. Vermiform stages distinguish the selected "
                "strategy from eggshell penetration in fungal nematode egg "
                "parasitism traitmech:000726. Fungal nematophagy traitmech:000719 "
                "requires feeding and includes dead prey; fungal nematode trap "
                "formation traitmech:000718 concerns hyphal differentiation. "
                "Neither is asserted as a parent. Local parasitism "
                "traitmech:000043 inherits persistent symbiosis, not required "
                "here. Animal pathogen METPO:1004002 is active below pathogenic "
                "to host METPO:1004000 and phenotype METPO:1000059. Current "
                "upstream clarifies its pinned organism-like wording as a "
                "phenotype; the local parent remains unchanged. No organism-level "
                "disjointness, exclusive host stage, universal host range or "
                "obligacy is asserted. Bare endoparasitism does not specify the "
                "fungal actor, host or infection route and is not an exact synonym."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "fungal-nematode-endoparasitism-metpo-assessment",
            "prompt": "Review the proposed infection class without reviving the obsolete parasitism identifier.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact active counterpart was identified in inspected "
                "pinned/current releases, editor and six template owners. "
                "Historical METPO:1000227 obsolete parasitism is broader, "
                "deprecated, under ObsoleteClass with OMO:0001000 reason and "
                "no replacement or consider annotation in those releases. "
                "METPO issue 521 disputes mechanically assigned reasons; the "
                "code neither invalidates the biology nor authorizes reuse. "
                "The historical ID is not revived or placed in xrefs. The "
                "ontology pin remains unchanged; v603 proposes this narrower "
                "infection phenotype with PROPOSED status and no equivalent "
                "external xref. Existing bacterial endoparasitic predation is "
                "not this fungal spore-infection strategy."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "fungal-nematode-endoparasitism-evidence-limits",
            "prompt": "Resolve assay endpoints and strain provenance before adding rates, canonical taxa or causal proteins.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Sun's Methods 2.6 counts attached spores or colonization; "
                "reported parasitism percentages are not curated as internal "
                "infection rates. Its imaged HR-eGFP1 is engineered, and "
                "morphological similarity to the wild type does not establish "
                "unchanged virulence. Its intestinal-route suggestion remains "
                "tentative; the distinct 1997 primary abstract supports ingestion "
                "in Harposporium cycloides. Lebrigand's S1 Text reports long "
                "laboratory passage and related isolate provenance, so these "
                "are not independent natural-strain exemplars. Predicted genes, "
                "expression and disputed assembly or mating-type interpretations "
                "are not required causal effectors. No canonical taxa, proteins "
                "or causal graph are asserted without further authority and "
                "strain-provenance work. Microscopy does not measure nutrient "
                "flux; no quantitative threshold, field efficacy or safety is "
                "inferred. The verification sidecar retains actual source "
                "locators, hashes and native verdicts; direct matching does not "
                "upgrade NOT_IN_ABSTRACT or UNRESOLVED. Full Glockling Methods "
                "and all raw experimental data were not accessed, and bounded "
                "notice checks are not comprehensive correction/retraction clearance."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added fungal nematode endoparasitism with three primary DOI sources "
            "and directly matched 20-, 16- and 13-word excerpts. Retained native "
            "VERIFIED, NOT_IN_ABSTRACT and UNRESOLVED outcomes. Spore-initiated "
            "infection and internal growth are not adhesion alone, hyphal traps "
            "or egg infection. No rates, canonical taxa or sequence-derived "
            "mechanism imported. Reserved 000727, v603 and 1068000-1068099 after "
            "ignored/hidden current-copy, retained-history and open/draft PR "
            "checks, including full-content proposal ranges. A ChemSpider "
            "identifier and broad editor envelopes are not METPO reservations. "
            "Other records unchanged; timestamp records observed acceptance."
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
         "|".join([f"TraitMech:data/traits/ecology/{SLUG}.yaml", DEFINITION_SOURCE]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Spore-initiated infection and internal fungal growth in vermiform nematodes; no universal host range or effector.",
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
