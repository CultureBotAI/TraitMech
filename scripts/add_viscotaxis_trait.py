"""Add viscotaxis with condition-bounded migration and hydrodynamic evidence."""

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

IDENTIFIER = "traitmech:000593"
TARGET = ROOT / "data/traits/physiology/viscotaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v470"
PETRINO = "DOI:10.1099/00221287-109-1-113"
COPPOLA = "DOI:10.1038/s41598-020-79887-7"
LIEBCHEN = "DOI:10.1103/physrevlett.120.208002"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "viscotaxis",
    "definition": (
        "A motile phenotype in which active locomotion produces net migration "
        "in response to a spatial gradient in surrounding fluid viscosity."
    ),
    "definition_source": PETRINO,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": PETRINO,
            "snippet": (
                "We have designated this positive response to a viscosity "
                "gradient as 'viscotaxis'."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:731206); full "
                "text not inspected. The antecedent is preferential migration "
                "into the more viscous region by the paper's historically "
                "named Leptospira interrogans (biflexa) strain B16. This "
                "supports positive viscotaxis under the reported conditions, "
                "not a universal direction of response. The historical name "
                "has not been reconciled to a modern species or strain taxon; "
                "no modern Leptospira identity or pathogenicity is inferred."
            ),
        },
        {
            "reference": COPPOLA,
            "snippet": (
                "they concentrate in the region of low viscosity or maintain "
                "a uniform concentration profile, depending on the viscosity "
                "ratio between the two regions."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:33432106). "
                "PMC7801662 full text, Fig. 5 and supplement Figs. S1-S3 "
                "were inspected. Wild-type Chlamydomonas reinhardtii showed "
                "net redistribution toward lower viscosity in some tested "
                "conditions but not others. Short-flagella results are not "
                "substituted for the wild type. Measurements followed pump "
                "stoppage; optical filtering limited phototactic bias. "
                "Interface reorientation, speed and angular diffusion jointly "
                "affect transport; a uniform profile is not positive evidence "
                "of net migration. The confined sharp-interface experiment "
                "does not directly validate an unconfined slowly varying "
                "gradient model. Strain accession provenance remains unresolved."
            ),
        },
        {
            "reference": LIEBCHEN,
            "snippet": (
                "suitable body shapes create viscotaxis based on a systematic "
                "asymmetry of viscous forces acting on a microswimmer."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:29864289); full "
                "text not inspected. This is a theoretical framework for "
                "self-propelled swimmers in slowly varying viscosity fields, "
                "not a new biological migration assay or receptor discovery. "
                "It supports a possible hydrodynamic contribution without "
                "requiring a universal sensory pathway. Suggested functions "
                "of microbial body-shape changes are not treated as "
                "experimentally established molecular mechanisms."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "viscotaxis-direction-and-physical-boundaries",
            "prompt": "Retain directional and environmental scope of viscosity-driven migration.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The class permits migration toward higher or lower fluid "
                "viscosity; neither direction nor a preferred viscosity is "
                "universal. Uniform-viscosity speed changes, passive advection "
                "and differential growth alone do not establish this trait. "
                "Keep fluid-viscosity gradients distinct from flow-directed "
                "rheotaxis, osmotic gradients, chemical cues and substrate "
                "stiffness or loss-modulus gradients. Coupled cues require "
                "controls rather than assumed equivalence. Hydrodynamic "
                "turning can bias an actively swimming organism without "
                "requiring a receptor. External equivalents and lexical "
                "variants remain unasserted pending authority and scope checks."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "viscotaxis-canonical-provenance-and-mechanisms",
            "prompt": "Resolve natural strain identities and distinguish models from mechanisms.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Reconcile the historical Leptospira B16 designation with "
                "current taxonomy before adding a canonical example; do not "
                "infer modern L. interrogans membership from the article "
                "title. The algae study distinguishes wild-type and "
                "short-flagella cells, but strain accessions and natural "
                "provenance have not been established in this curation. "
                "Keep their observations separate and resolve NCBI identity "
                "before adding examples. Inspect remaining full texts and "
                "separate proposed shape-dependent hydrodynamics from measured "
                "reorientation or redistribution. No universal receptor or "
                "protein-resolved causal pathway follows from these sources; "
                "taxon-paired accessions and direct evidence are needed "
                "before adding molecular edges. A NONMECHANISTIC graph must "
                "not bypass those requirements."
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
            "Added viscotaxis with three primary DOI citations and exact "
            "abstract snippets. Ignored-and-hidden novelty searches and "
            "structured OWL review found no exact record or METPO term. "
            "Reserved METPO:1054700 in v470. Inspected the algae full text "
            "and supplementary figures to separate conditional spatial "
            "redistribution from speed changes and model interpretations. "
            "Kept positive and negative response scope, deferred historical "
            "strain taxonomy, canonical examples, external equivalents and "
            "protein-resolved mechanisms."
        ),
        llm_assisted=True, timestamp="2026-10-04T09:34:00Z",
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
        "METPO:1054700", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/viscotaxis.yaml|{PETRINO}|{COPPOLA}|{LIEBCHEN}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Fluid-viscosity-gradient migration; no universal direction or receptor.",
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
