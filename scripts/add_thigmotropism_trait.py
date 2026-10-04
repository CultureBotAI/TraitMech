"""Add contact-directed polarized growth with source-bounded fungal evidence."""

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

IDENTIFIER = "traitmech:000594"
TARGET = ROOT / "data/traits/physiology/thigmotropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v471"
SHERWOOD = "DOI:10.1080/02681219280000621"
WATTS = "DOI:10.1099/00221287-144-3-689"
BRAND = "DOI:10.1016/j.cub.2006.12.043"
THOMSON = "DOI:10.1111/cmi.12369"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "thigmotropism",
    "definition": (
        "A phenotype in which polarized growth is directionally reoriented "
        "in response to physical contact with surface topography."
    ),
    "definition_source": SHERWOOD,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": SHERWOOD,
            "snippet": (
                "The response was likely to be due to contact guidance "
                "(thigmotropism) and not chemotropism towards the nutrients"
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:1287165); full "
                "text not inspected. Candida albicans hyphae entered membrane "
                "pores after contacting their lips, including from the "
                "underside while growing away from nutrient agar. This "
                "supports the authors' contact-guidance interpretation, "
                "not exclusion of every chemical influence or proof of "
                "tissue invasion in vivo."
            ),
        },
        {
            "reference": WATTS,
            "snippet": (
                "both compounds reduced the percentage of hyphae reorienting "
                "on contact with a ridge without markedly affecting hyphal "
                "extension rate"
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:9534238); full "
                "text not inspected. The compounds are GdCl3 and verapamil "
                "at the tested low concentrations. Reorientation and extension "
                "rate are distinct readouts. Pharmacological attenuation "
                "and membrane channel recordings suggest channel involvement "
                "but do not identify a unique molecular mechanosensor."
            ),
        },
        {
            "reference": BRAND,
            "snippet": (
                "The establishment and maintenance of directional growth "
                "in relation to these environmental cues was Ca(2+) dependent."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:17275302). "
                "PMC1885950 full text distinguishes contact-dependent "
                "thigmotropism from electric-field galvanotropism. In the "
                "reported ridge assays, channel-component mutations reduced "
                "reorientation without reducing hyphal extension rates. "
                "Calcineurin was required for cathodal emergence but not "
                "thigmotropism; do not transfer that pathway requirement "
                "between the two responses. Localized channel activation "
                "and calcium influx remain a proposed model, not a universal "
                "mechanism established in every microbe. Supplement not inspected."
            ),
        },
        {
            "reference": THOMSON,
            "snippet": (
                "In vitro, hyphal tips reorient thigmotropically on contact "
                "with small obstacles."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:25262778). "
                "PMC4371639 full text, Fig. 6 and supplementary Table S1 "
                "were inspected. Adhesion or friction sufficient to oppose "
                "forward growth supported acute tip reorientation; less "
                "constrained hyphae instead bent subapically. Tip contact "
                "alone was insufficient in these assays. Table S1 lists "
                "CAI4/CIp10, BWP17 and engineered derivatives, including "
                "fluorescent reporters and an rsr1 deletion; the paper's "
                "wild-type designation is not proof of natural strain "
                "provenance. Spitzenkorper position correlated with growth "
                "but was not an absolute predictor. Force magnitudes are "
                "not curated because main-text and supplementary Fig. S2 "
                "units disagree. Movies were not inspected."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "thigmotropism-growth-and-contact-boundaries",
            "prompt": "Keep contact-directed growth distinct from locomotion and passive bending.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Polarized growth reorientation is not whole-cell locomotion, "
                "so the parent is phenotype, not motile. Filament shape "
                "alone does not imply contact sensitivity, and the existing "
                "mycelial-growth record is explicitly bacterial. Do not "
                "equate this trait with thigmotaxis, stiffness-gradient "
                "migration, electric-field growth, generic adhesion or "
                "contact-induced differentiation. Passive bending, growth "
                "rate changes and incidental alignment alone are insufficient. "
                "The fungal observations do not demonstrate a universal "
                "mechanosensor or establish tissue invasion in vivo. "
                "External equivalences and lexical variants need separate "
                "authority and scope checks."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "thigmotropism-strain-and-mechanism-grounding",
            "prompt": "Resolve natural strain provenance and protein-level mechanism evidence.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Retain the reported Candida albicans observations as qualified "
                "evidence. The inspected strain table includes engineered "
                "backgrounds and fluorescent reporters; verify direct "
                "measurements in naturally occurring strains and NCBI "
                "identities before adding canonical examples. Resolve "
                "taxon-paired protein accessions and distinguish channel "
                "deletion evidence from inhibitor specificity and proposed "
                "localized calcium signals before adding a causal graph. "
                "Keep calcineurin's galvanotropic role separate from the "
                "reported thigmotropic response. Rsr1-dependent polarity "
                "positioning does not make Spitzenkorper position an "
                "absolute predictor of growth direction. Inspect remaining "
                "full texts and supplements before strengthening these "
                "claims; no NONMECHANISTIC graph should bypass missing "
                "protein or taxon grounding."
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
            "Added thigmotropism with four primary DOI citations and exact "
            "abstract snippets. Ignored-and-hidden novelty searches and "
            "structured OWL review found no exact record or METPO term. "
            "Reserved METPO:1054800 in v471. Distinguished contact-directed "
            "polarized growth from locomotion and passive bending. Inspected "
            "two full texts plus the Thomson Fig. 6 and supplementary strain "
            "table. Deferred natural canonical examples and accession-level "
            "mechanism grounding; did not infer them from engineered strains."
        ),
        llm_assisted=True, timestamp="2026-10-04T10:24:00Z",
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
        "METPO:1054800", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/thigmotropism.yaml|{SHERWOOD}|{WATTS}|{BRAND}|{THOMSON}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Contact-directed polarized growth; not whole-cell locomotion or passive bending.",
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
