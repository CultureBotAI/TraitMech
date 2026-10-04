"""Add phototaxis with versioned primary evidence and a qualified exemplar."""

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

IDENTIFIER = "traitmech:000588"
TARGET = ROOT / "data/traits/physiology/phototaxis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v465"
SCHUERGERS = "DOI:10.7554/eLife.12620"
BERTHOLD = "DOI:10.1105/tpc.108.057919"
TRAUTMANN = "DOI:10.1093/dnares/dss024"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "phototaxis",
    "definition": (
        "A motile phenotype in which active locomotion is directionally biased "
        "toward or away from a light source in response to illumination."
    ),
    "definition_source": BERTHOLD,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": SCHUERGERS,
            "snippet": (
                "the majority of motile cells switched direction within about "
                "1 min, and then moved directly towards the light source"
            ),
            "notes": (
                "Results, first subsection, Figure 1c-d and methods; publisher "
                "version 2, posted 2022-04-22, originally published 2016-02-09 "
                "(PMID:26858197). Version-specific full text: "
                "https://cdn.elifesciences.org/articles/12620/elife-12620-v2.xml. "
                "Figure 1 and both optical figure supplements visually inspected. "
                "Motile Synechocystis sp. PCC 6803 PCC-M cells on agarose move "
                "toward oblique RGB illumination (470/525/625 nm, equal intensity; "
                "10 micromol photons per square metre per second). The projected "
                "white-light intensity gradient does not produce significant "
                "directional bias in this experiment. Cells were sampled from "
                "moving colony fronts; analysis excludes immotile cells. These "
                "observations are separate from torA-gfp optical reporter assays "
                "and from the proposed PixJ1-to-pilus signaling model. They do "
                "not establish one universal directional-sensing mechanism."
            ),
        },
        {
            "reference": BERTHOLD,
            "snippet": (
                "Chlamydomonas cells with low CHR2 content exhibit photophobic "
                "and phototactic responses that strictly depend on the "
                "availability of CHR1."
            ),
            "notes": (
                "Abstract exact-matched at Europe PMC (PMID:18552201). The PMC "
                "introduction distinguishes directional swimming toward or away "
                "from light from transient photophobic reversal; the beginning "
                "of Results identifies the cell-wall-deficient CW2 strain. "
                "Evidence concerns Chlamydomonas reinhardtii under the stated "
                "receptor-content conditions, not every algal strain or a "
                "universal CHR1 requirement. Xenopus ion-conductance assays are "
                "heterologous. Remaining full-text sections and supplements "
                "were not inspected; no natural algal exemplar or complete "
                "protein-resolved pathway is inferred."
            ),
        },
        {
            "reference": TRAUTMANN,
            "snippet": (
                "\u2018PCC-M and PCC-P\u2019 are strains that both exhibit the native "
                "positive phototaxis, whereas \u2018PCC-N\u2019 strain shows negative phototaxis."
            ),
            "notes": (
                "Results, section 3.1, exact-matched to Europe PMC full-text XML "
                "(PMID:23069868). Methods trace PCC-M to the Shestakov laboratory "
                "in 1993 and maintenance of motile colonies, matching the "
                "Schuergers study. The strain descends from the original PCC "
                "isolate but has undergone laboratory microevolution; it is "
                "not asserted genetically identical to the original isolate. "
                "Discussion also reports no blue-light phototaxis for PCC-M. "
                "This supports a substrain-qualified exemplar, not a statement "
                "that every PCC 6803 lineage or illumination gives the same response."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1148",
            "taxon_label": "Synechocystis sp. PCC 6803",
            "reference": SCHUERGERS,
            "note": (
                "Motile wild-type PCC-M substrain, not the torA-gfp reporter. "
                "Figure 1c-d shows positive phototaxis on agarose under oblique "
                "RGB illumination after sampling moving colony fronts. "
                "Independent provenance: DOI:10.1093/dnares/dss024, Methods 2.1 "
                "and Results 3.1; PCC-M retains native positive phototaxis but "
                "has laboratory sequence differences and lacks blue-light "
                "phototaxis in the cited comparison. NCBI:1148 was resolved "
                "at NCBI on 2026-10-04; it is species-level, not a PCC-M-specific "
                "accession. No universal substrain, wavelength or sign claim."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "phototaxis-direction-and-mapping-boundaries",
            "prompt": "Preserve directional scope and resolve phenotype-level mappings.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Positive and negative responses are directional cases, not a "
                "requirement to exhibit both or a permanent sign. Speed changes "
                "alone (photokinesis), light sensing alone and phototrophic energy "
                "conservation do not establish this trait. A photophobic response "
                "can participate in phototaxis but is not an exact synonym. "
                "METPO:1000241 is obsolete with no replacement or definition; "
                "do not revive it or assert a replaces relation without upstream "
                "review. External biological-process terms are not automatically "
                "equivalent to this organismal disposition; verify scope before "
                "adding xrefs or lexical synonyms."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "phototaxis-mechanism-and-optical-provenance",
            "prompt": "Ground causal branches without promoting optical models to facts.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The cyanobacterial PixJ1/response-regulator/pilus branch is a "
                "proposed model in Schuergers Figure 5; causal edges and eligible "
                "taxon-paired protein accessions require additional primary "
                "checks. Native algal signaling must be separated from "
                "heterologous conductance and cell-wall-deficient strains. "
                "Version 2 optical supplement graphics also differ from their "
                "captions: Figure 3 supplement 1 labels a 60x objective versus "
                "100x in text, and Figure 4 supplement 1 labels 633 nm versus "
                "625 nm in text. Do not silently reconcile these parameters or "
                "use them to quantify a mechanistic graph. Figure 1 phenotype "
                "evidence is retained independently. No NONMECHANISTIC graph "
                "is used to bypass protein-grounding requirements."
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
            "Added phototaxis with three primary DOI citations and exact snippets. "
            "Ignored-and-hidden searches found no exact live trait; the obsolete "
            "METPO class is not reused. Reserved METPO:1054200 in v465. Verified "
            "publisher version 2, optical supplements and PCC-M provenance; "
            "added a substrain-qualified NCBI-resolved canonical example. "
            "Deferred ungrounded protein branches and recorded source discrepancies."
        ),
        llm_assisted=True, timestamp="2026-10-04T05:21:00Z",
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
        "METPO:1054200", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/phototaxis.yaml|{BERTHOLD}|{SCHUERGERS}|{TRAUTMANN}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Directional light response; positive and negative cases, not speed modulation alone.",
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
