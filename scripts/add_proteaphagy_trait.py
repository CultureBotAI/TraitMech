"""Add a source-bounded microbial proteasome autophagy phenotype."""

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
TARGET = ROOT / "data/traits/physiology/proteaphagy.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/autophagy.yaml"
PARENT_PROPOSAL = ROOT / "proposals/metpo_traitmech_v520/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v521/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000645"
METPO_ID = "METPO:1059800"
PARENT_METPO_ID = "METPO:1059100"
TIMESTAMP = "2026-10-06T15:30:25Z"
PARENT_HASH = "f97521b02026c370e138bea96d5ed332316678c01d9f2786ead3d9e5df5ff398"
TEMPLATE_HASH = "65b5c24b366b868e3657dd80dfe2bec80375adbf41ca767913c12ac56e776703"
STARVATION = "DOI:10.1074/jbc.M115.699124"
INACTIVATION = "DOI:10.1016/j.celrep.2016.07.015"
REGULATION = "DOI:10.1016/j.jbc.2021.101494"
CORRECTION = "DOI:10.1016/j.celrep.2022.110552"
HEADERS = [
    ["proposed_id", "label", "definition", "definition_source", "parent",
     "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
    ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
     "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
     "A oboInOwl:inSubset", "", "", ""],
]
RECORD = {
    "identifier": IDENTIFIER,
    "label": "proteaphagy",
    "definition": (
        "An autophagy phenotype in which a microbial cell degrades its proteasomes "
        "or proteasome subcomplexes by delivering them to lysosomal or vacuolar compartments."
    ),
    "definition_source": STARVATION,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000638"],
    "evidence": [
        {
            "reference": STARVATION,
            "snippet": (
                "Here we show that in yeast, upon nitrogen starvation, proteasomes "
                "are targeted for vacuolar degradation through autophagy."
            ),
            "notes": (
                "PMID:26670610, PMC4751371. Scientific abstract directly read in "
                "DOI-matched Europe PMC metadata and XML. Yeast-strain and "
                "immunoblot Methods, autophagy-dependence and core/regulatory-particle "
                "Results, Table 1 and relevant captions were read. Saccharomyces "
                "cerevisiae reporter processing and vacuolar localization support "
                "degradation; native gels address incorporation into complexes. "
                "The core and regulatory particles can be targeted separately, "
                "with different Ubp3 dependence; intact 26S uptake is not required "
                "by the definition. Figure 6D's caption conflicts with its title "
                "and body concerning Rpn10, so no Rpn10 requirement is curated. "
                "Actual figures, supplements and independent natural-strain "
                "provenance were not inspected."
            ),
        },
        {
            "reference": INACTIVATION,
            "snippet": (
                "Here, we define two proteaphagy routes in yeast that respond to "
                "either nitrogen starvation or particle inactivation."
            ),
            "notes": (
                "PMID:27477278. Scientific abstract directly read in Europe PMC "
                "with matching DOI. The yeast study distinguishes starvation "
                "from quality-control turnover of inactive proteasomes; Cue5 "
                "and Hsp42 support the latter route, not a universal microbial "
                "gene inventory. Correction " + CORRECTION + " (PMID:35294886) "
                "is linked by the source metadata. Its text was directly read at "
                "https://profiles.wustl.edu/en/publications/erratum-autophagic-turnover-of-inactive-26s-proteasomes-in-yeast-/: "
                "a duplicated anti-histone H3 control blot in Figure S3 was "
                "replaced; the authors state their conclusions are unchanged. "
                "The corrected figure, original full Methods, actual figures "
                "and strain provenance were not inspected. The correction is "
                "not independent trait evidence."
            ),
        },
        {
            "reference": REGULATION,
            "snippet": (
                "Indeed, we found that several conditions that activated general "
                "autophagy did not induce proteaphagy, further distinguishing "
                "proteaphagy from general autophagy."
            ),
            "notes": (
                "PMID:34919962, PMC8732087. Scientific abstract directly read in "
                "DOI-matched Europe PMC metadata and XML; Results sec1.1-sec1.3, "
                "Discussion sec2 and Methods sec3.1-sec3.4 were read. Proteasome "
                "GFP processing, native gels and vacuolar microscopy distinguish "
                "cargo turnover from general autophagy. In sec1.3, ATG11 deletion "
                "abolishes residual nitrogen-starvation turnover in an ATG17 "
                "deletion background, not all proteaphagy in every condition. "
                "Rapamycin yields no detected difference in the ATG11 single "
                "deletion, with a stated detection-limit caveat. Thus the later "
                "result does not establish a blanket contradiction of the 2016 "
                "single-deletion result. Methods identify W303-derived SUB61/SUB62 "
                "reporter and deletion strains. Captions were read; actual "
                "figures, supplements and independent strain provenance were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "proteaphagy-cargo-scope-and-go",
            "prompt": "Review proteasome-cargo scope and qualified GO alignment.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Proteasomes are the autophagic cargo, not the machinery "
                "degrading unrelated substrates. Ordinary proteasome-mediated "
                "proteolysis, proteasome biogenesis, storage granules, free-subunit "
                "loss or gene presence alone does not establish this phenotype. "
                "The 2016 starvation study includes separately targeted core "
                "and regulatory particles, so do not require intact holoenzyme "
                "uptake. GO:0061816, directly resolved at "
                "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0061816, "
                "is a nonobsolete biological process restricted to selective "
                "macroautophagy, not an exact organismal phenotype. The "
                "cargo-defined local term does not impose a universal route, "
                "trigger or selectivity mechanism; retain this scope difference "
                "for human review and omit exact xrefs and synonyms. Ribophagy "
                "traitmech:000641 and nuclear-cargo degradation traitmech:000643 "
                "are distinct: shared machinery or prior nuclear localization "
                "does not equate these cargo phenotypes."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "proteaphagy-context-exemplars-and-mechanisms",
            "prompt": "Resolve route-specific mechanisms, figures and natural exemplars.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Keep starvation and inactive-particle quality-control routes "
                "distinct. The later ATG11 result concerns residual turnover "
                "in an ATG17 deletion background; neither an abstract's general "
                "wording nor a single deletion establishes universal necessity. "
                "Do not turn reduced efficiency, a detection limit or partial "
                "turnover into complete absence. Resolve the 2016 Figure 6D "
                "Rpn10 caption/body discrepancy and inspect the corrected "
                "Figure S3 associated with " + CORRECTION + " before relying "
                "on those panels. Canonical examples remain unset pending "
                "independent natural-strain provenance. The microbial cell "
                "performing degradation carries the phenotype, not a bacterium "
                "eliciting an animal host response. Native taxon-paired protein "
                "accessions and functional evidence are required before a "
                "causal graph is added; ATG presence, puncta or loss of total "
                "proteasome abundance alone is not proof of autophagic flux."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def fingerprint(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added proteasome-cargo autophagy with three DOI-backed scientific-abstract "
            "snippets, subcomplex scope, context-specific ATG11 interpretation and "
            "explicit correction/figure limits. Ignored-and-hidden novelty checks, "
            "fresh seed and pinned METPO review found no exact record. Reserved "
            "METPO:1059800 in v521 using unchanged corrected parent context from "
            "v520. Deferred unverified exemplars, mappings and protein graphs."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict, old_rows: list[list[str]]) -> str:
    parent = next(r for r in old_rows[2:] if r[0] == PARENT_METPO_ID)
    child = [
        METPO_ID, record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/proteaphagy.yaml",
                  *[e["reference"] for e in record["evidence"]]]),
        PARENT_METPO_ID, "", "", "metpo_traitmech_2026_10", "",
        "Proteasomes are cargo, including subcomplexes; retain route and correction limits.",
        IDENTIFIER,
    ]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows([*HEADERS, parent, child])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    parent = yaml.safe_load(PARENT_PATH.read_text())
    if not isinstance(parent, dict) or fingerprint(parent) != PARENT_HASH:
        raise SystemExit("Parent differs from reviewed context")
    template = PARENT_PROPOSAL.read_bytes()
    if hashlib.sha256(template).hexdigest() != TEMPLATE_HASH:
        raise SystemExit("Parent proposal differs from reviewed context")
    old_rows = list(csv.reader(io.StringIO(template.decode()), delimiter="\t"))
    record = build_record()
    proposal = proposal_tsv(record, old_rows)
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
