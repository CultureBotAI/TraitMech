"""Add evidence-backed fungal adhesive-knob trap formation."""

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
SLUG = "fungal_adhesive_knob_trap_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v555/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000679"
METPO_ID = "METPO:1063200"
PROTEOME = "DOI:10.1128/AEM.01390-13"
TAXONOMY = "DOI:10.1016/j.femsle.2005.02.027"
TIMESTAMP = "2026-10-08T11:29:45Z"
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
    "label": "fungal adhesive-knob trap formation",
    "definition": (
        "A morphological phenotype in which a fungus forms unicellular knobs "
        "at hyphal apices that serve as adhesive nematode traps."
    ),
    "definition_source": PROTEOME,
    "trait_category": "MORPHOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": PROTEOME,
            "snippet": (
                "The trap of M. haptotylum consists of a unicellular structure "
                "called a knob that develops at the apex of a hypha."
            ),
            "notes": (
                "Andersson et al. (2013), scientific Abstract; primary publisher "
                "HTML https://journals.asm.org/doi/10.1128/AEM.01390-13. "
                "Introduction, Culture Methods, relevant Results/Discussion "
                "and Conclusion, and actual Figure 1 were inspected. CBS 200.50 "
                "formed knobs in aerated liquid culture. Figure 1 shows residual "
                "attached knobs and isolated knobs after filtration, not a "
                "capture time course. Detachment is a culture observation, not "
                "a defining requirement. Proteomic and transcript changes do "
                "not establish causal functions of individual proteins; WSC "
                "adhesion roles remain hypotheses. Supplements were not used "
                "to assert protein mechanisms."
            ),
        },
        {
            "reference": TAXONOMY,
            "snippet": (
                "The adhesive knobs were produced frequently on nutritional "
                "agar plates even in the absence of challenging nematodes."
            ),
            "notes": (
                "Liu, Liu and Zhuang (2005), scientific Abstract, directly "
                "retrieved from the primary publisher https://academic.oup.com/"
                "femsle/article/245/1/99/483775 (minimal-article redirect). "
                "Abstract-only access: full Methods and figures were not "
                "retrieved. Orbilia querci material came from rotten Quercus "
                "wood in Huai-rou County, Beijing, and pure culture from "
                "ascospores. The authors report nematode capture with adhesive "
                "stalked knobs. Formation without added prey under these "
                "conditions excludes an obligatory prey-induction definition; "
                "neither medium nor stalk length is universal. The reported "
                "Dactylellina querci anamorph name is source terminology, not "
                "an independently verified current taxonomic equivalence."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1284197",
            "taxon_label": "Dactylellina haptotyla CBS 200.50",
            "reference": PROTEOME,
            "note": (
                "Source-named Monacrosporium haptotylum CBS 200.50. Live NCBI "
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"
                "db=taxonomy&id=1284197 resolves rank strain, the exact label "
                "Dactylellina haptotyla CBS 200.50 and the historical name. "
                "Zhou et al. (2018), DOI:10.1080/23802359.2018.1507650, body "
                "paragraph 2, directly read primary XML at https://www.ebi.ac.uk/"
                "europepmc/webservices/rest/PMC7801010/fullTextXML, reports "
                "collection from a decaying leaf in a pond at Chelsea Physic "
                "Garden, London, by M.P. Peach in 1948. That genome study is "
                "strain-provenance support, not an independent knob-formation "
                "experiment. The unperturbed natural-origin strain example "
                "is qualified by the 2013 culture conditions, not every isolate "
                "or field biocontrol efficacy."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "adhesive-knob-scope-and-parent",
            "prompt": "Resolve a closer fungal trap-morphology parent.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Phenotype METPO:1000059 is a broad parent. Existing mycelial "
                "growth traitmech:000074 explicitly concerns bacteria; hyphal "
                "anastomosis traitmech:000605 concerns fusion. Distinguish "
                "unicellular adhesive knobs from multicellular adhesive nets, "
                "adhesive columns, nonconstricting rings and mechanically "
                "constricting rings. Auxiliary cells and appressoria have "
                "different biological roles; a generic rounded hyphal tip "
                "or nematophagous genus is not sufficient. Detachment, a "
                "particular stalk length and nematode induction are not "
                "defining requirements. Formation alone does not demonstrate "
                "adhesion or successful capture in every condition. No exact "
                "synonyms, xrefs, SSSOM equivalences or organism-level "
                "disjointness are asserted; closer hierarchy remains open."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-08",
        },
        {
            "discussion_id": "adhesive-knob-mechanism",
            "prompt": "Separate knob morphogenesis from adhesion and infection mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Sequence features and expression correlations alone do not "
                "establish a necessary or sufficient gene effect. A "
                "protein-resolved causal graph requires perturbation and "
                "complementation evidence, relevant remaining figures and "
                "supplements, and taxon-paired accessions. Formation, adhesion, "
                "capture, penetration and digestion remain separate endpoints. "
                "No universal lectin, WSC-domain protein or signaling-gene "
                "requirement is asserted; mechanism is deferred, not claimed "
                "absent. Taxonomic membership alone does not establish this "
                "phenotype."
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
            "Added fungal adhesive-knob trap formation with two independent "
            "primary DOI sources, contiguous snippets and a natural-origin "
            "strain example. Ignored-and-hidden main/worktree/open-PR checks "
            "support 000679 and v555 block 1063200-1063299. Distinguished "
            "abstract-only access and provenance-only support; separated "
            "morphology from sequence-derived mechanism hypotheses. Existing "
            "records unchanged. Timestamp is observed UTC."
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
         "Unicellular adhesive-knob formation; neither detachment nor prey induction is required.",
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
