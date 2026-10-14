"""Add fungal nematode egg parasitism through guarded validated writes."""

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
SLUG = "fungal_nematode_egg_parasitism"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/ecology/animal_pathogen.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v602/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000726"
METPO_ID = "METPO:1067900"
TIMESTAMP = "2026-10-14T11:46:22Z"
DEFINITION_SOURCE = "DOI:10.3389/fmicb.2021.617710"
SUPPORTING_SOURCE = "DOI:10.3389/fmicb.2016.01084"
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
    "label": "fungal nematode egg parasitism",
    "definition": (
        "An animal-pathogenic phenotype in which a fungus infects nematode eggs "
        "by penetrating their eggshells and colonizing their interiors."
    ),
    "definition_source": DEFINITION_SOURCE,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": DEFINITION_SOURCE,
            "snippet": "The egg-pathogenic fungus Purpureocillium lilacinum parasitizes on nematode eggs",
            "notes": (
                "Xu et al. 2021, PMID:33897634, PMCID:PMC8058359, scientific "
                "Abstract; direct JATS match and native VERIFIED. Own JZD02 "
                "experiment, Methods and actual Figure 1 A-C support infection "
                "of Meloidogyne incognita eggs. Supplementary Table 1 defines "
                "infection by hyphal penetration through an individual egg, "
                "not mere surface contact. Its 30-hour printed mean disagrees "
                "with the replicate counts; no numerical infection rates are "
                "adopted. The 6-hour control and 42-hour infected transcriptomes "
                "differ in time and include mixed infection stages. Expression "
                "associations are not causal protein evidence."
            ),
        },
        {
            "reference": SUPPORTING_SOURCE,
            "snippet": "Infected eggs by P. lilacinum 36-1.",
            "notes": (
                "Xie et al. 2016, PMID:27486440, PMCID:PMC4949223, Figure 5 "
                "caption, panel B; actual panels A-C and Methods/Results inspected. "
                "P. lilacinum denotes Purpureocillium lilacinum. Direct JATS "
                "match; native NOT_IN_ABSTRACT is retained. This is its own "
                "36-1 infection experiment, not a repetition of Xu's citation. "
                "Eggs were supplied as the only nourishment for the reported "
                "24-hour comparison, but microscopy does not quantify nutrient "
                "assimilation. RNA-seq replicates were pooled; gene homology "
                "and expression do not demonstrate a required effector."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "fungal-nematode-egg-parasitism-scope-and-hierarchy",
            "prompt": "Refine the egg-infection hierarchy without conflating infection, feeding and hatching endpoints.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The fungal bearer penetrates eggshells and colonizes egg interiors. "
                "Surface attachment, egg-hatching inhibition, killing, trapping or "
                "a gene annotation alone is insufficient. Animal pathogen "
                "METPO:1004002 is active below pathogenic to host METPO:1004000 "
                "and phenotype METPO:1000059. Its pinned organism-like wording "
                "is clarified as a phenotype in current upstream METPO; the "
                "local parent is not rewritten. Nematode egg infection does not "
                "entail mammalian pathogenicity. Xie describes this fungus as "
                "nematophagous, but the operational infection endpoint does not "
                "quantify feeding: fungal nematophagy traitmech:000719 requires "
                "consumption and also includes dead prey. It is related, not an "
                "asserted parent here. Local parasitism traitmech:000043 inherits "
                "persistent symbiosis, which is not required. No organism-level "
                "disjointness, obligacy, exclusive host stage or universal host "
                "range is asserted. Bare egg parasitism does not specify the "
                "fungal actor and is not an exact synonym."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "fungal-nematode-egg-parasitism-metpo-assessment",
            "prompt": "Review the proposed class without reviving the obsolete parasitism identifier.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "No exact active counterpart was identified in the inspected "
                "pinned/current releases, editor and template owners. Historical "
                "METPO:1000227 obsolete parasitism is broader, deprecated, under "
                "ObsoleteClass with OMO:0001000 reason and no replacement or "
                "consider annotation in those releases. METPO issue 521 disputes "
                "mechanically assigned reasons; the code neither invalidates the "
                "biology nor authorizes reuse. The historical ID is not revived "
                "or placed in xrefs. Fried-egg colony is unrelated. The ontology "
                "pin remains unchanged; v602 proposes this narrower infection "
                "phenotype with PROPOSED status and no equivalent external xref."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-14",
        },
        {
            "discussion_id": "fungal-nematode-egg-parasitism-evidence-limits",
            "prompt": "Resolve source inconsistencies and strain provenance before adding rates, examples or causal mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Xu Supplementary Table 1 reports a 30-hour mean of 38% for "
                "replicates 38%, 33% and 33%, whose arithmetic mean is about "
                "34.7%. This discrepancy is preserved, not silently corrected. "
                "Its main Methods sample-level wording is less precise than the "
                "supplement's individual-egg penetration criterion. No rates or "
                "infection threshold are curated. Xie's conserved appressorium "
                "genes also occur in fungi lacking that structure; neither gene "
                "inventory nor differential expression establishes this trait or "
                "a protein-resolved mechanism. No causal graph, protein example "
                "or canonical taxon is asserted without further authority and "
                "strain-provenance checks. Microscopy and source-designated "
                "infection are not tracer measurements of nutrient flux. No field "
                "efficacy or safety claim follows. Source hashes, inspected "
                "figures/supplement, actual snippet verdicts and bounded notice "
                "checks are retained in the verification sidecar; no comprehensive "
                "correction/retraction clearance is claimed."
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
            "Added fungal nematode egg parasitism with two primary DOI sources "
            "and directly matched nine-word and six-word excerpts. Preserved "
            "native VERIFIED/NOT_IN_ABSTRACT outcomes and the supplement's "
            "inconsistent mean; no rates or sequence-derived mechanism imported. "
            "Reserved 000726, v602 and 1067900-1067999 after ignored/hidden "
            "current-copy, retained-history and open/draft PR checks, including "
            "full-content proposal ranges. Wheel sizes and broad editor envelopes "
            "are not conflicting reservations. Animal-pathogen parent scope "
            "checked against pinned/current ontology. Other records unchanged; "
            "timestamp records observed acceptance."
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
         "Fungal penetration and internal colonization of nematode eggs; no universal host range or shared effector.",
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
