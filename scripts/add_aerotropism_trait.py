"""Add oxygen-gradient-directed growth with qualified primary evidence."""

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

IDENTIFIER = "traitmech:000601"
TARGET = ROOT / "data/traits/physiology/aerotropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v478"
AOKI = "DOI:10.1007/BF02464003"
CARLILE = "DOI:10.1016/S0007-1536(88)80071-8"
DAMM = "DOI:10.1016/S0168-6496(03)00161-2"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "aerotropism",
    "definition": (
        "A phenotype in which polarized growth is directionally "
        "biased in response to a spatial oxygen concentration gradient."
    ),
    "definition_source": AOKI,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000597"],
    "evidence": [
        {
            "reference": AOKI,
            "notes": (
                "Aoki et al. (1998), publisher page at "
                "https://www.sciencedirect.com/science/article/abs/pii/S1340354098709003. "
                "Crossref and the Elsevier API confirmed bibliographic metadata "
                "only; direct publisher retrieval returned 403. Interpretation "
                "is search-index-limited: indexed publisher text reports Candida "
                "albicans hyphal reorientation in thin-layer corn-meal agar and "
                "growth toward an oxygen-rich capillary meniscus, interpreted "
                "as positive aerotropism. The source wording, full text and "
                "figures were not directly verified, so no snippet is asserted "
                "(#1678). This citation supports the oxygen-directed growth "
                "interpretation provisionally, not a resolved oxygen receptor. "
                "Reorientation is distinct from growth rate; oxygen-dependent "
                "growth and other local gradients remain confounds."
            ),
        },
        {
            "reference": CARLILE,
            "notes": (
                "Carlile and Tew (1988), publisher page at "
                "https://www.sciencedirect.com/science/article/abs/pii/S0007153688800718. "
                "Crossref and the Elsevier API confirmed bibliographic metadata "
                "only; direct publisher retrieval returned 403. Interpretation "
                "is search-index-limited: indexed publisher text reports "
                "negative aerotropism in Phytophthora citricola germ tubes "
                "and no response to casein hydrolysate. The existence and "
                "wording of an original abstract were not directly verified, "
                "so no snippet is asserted (#1678). Full text, figures, strain "
                "identity and gradient controls remain unverified. This "
                "citation supports retaining avoidance within the proposed "
                "class, not a universal oxygen-attraction rule or an absence "
                "of responses to all other chemical gradients."
            ),
        },
        {
            "reference": DAMM,
            "snippet": (
                "Conidia also germinated close to air-filled Teflon tubes and "
                "exhibited germ-tube tropism, but not as distinctly as on living reed roots."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:19719598). "
                "Publisher HTML methods, results and discussion were read at "
                "https://academic.oup.com/femsec/article/45/3/293/549782. "
                "Section 3.2 reports Microdochium bolleyi germ-tube orientation "
                "toward air-filled Teflon root dummies (60% +/- 12%) and stronger "
                "orientation toward living roots. This is qualified supporting "
                "evidence: oxygen-dependent germination and root-derived "
                "chemicals complicate attribution, and the tube result alone "
                "does not establish significance against random orientation. "
                "Figure 3 measures germination, not orientation. Figures were "
                "not visually verified. No strain accession or molecular "
                "mechanism is asserted."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "aerotropism-direction-and-stimulus-boundaries",
            "prompt": "Keep oxygen-directed growth distinct from oxygen demand, taxis and flow.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The class includes positive or negative directional growth, "
                "without requiring both in one organism. Aerotaxis denotes "
                "locomotion, not growth orientation. Oxygen tolerance, oxygen "
                "requirement, biomass, germination and extension rate alone "
                "are insufficient. This record uses the oxygen-gradient sense "
                "of aerotropism in its primary sources; air-flow-directed "
                "growth belongs to rheotropism, not this class solely because "
                "air supplies oxygen. Resolve external phenotype mappings "
                "and variant-label scopes before adding xrefs or synonyms. "
                "The local parent is chemotropism (traitmech:000597); its "
                "v474 METPO:1055100 proposal is not released. The v478 proposal "
                "therefore uses the existing METPO:1000059 phenotype parent; "
                "reconcile the narrower hierarchy when chemotropism is accepted."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "aerotropism-controls-and-native-mechanism",
            "prompt": "Resolve gradient controls, strain provenance and native causal mechanisms.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Inspect the older full texts and orientation readouts, and "
                "discriminate tip reorientation from preferential growth or "
                "survival in oxygen-rich regions. Resolve natural strain "
                "provenance and NCBI identity before canonical examples. "
                "The current evidence does not establish a universal oxygen "
                "sensor or a taxon-independent protein mechanism. Do not "
                "transfer pheromone chemotropism or aerotaxis mechanisms "
                "without direct evidence. Defer causal graphs until native "
                "causal evidence and taxon-paired protein accessions support "
                "them; NONMECHANISTIC is not a grounding bypass."
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
            "Added polarity-neutral oxygen-gradient-directed growth under "
            "local chemotropism, supported by three primary DOI citations "
            "and source snippets. Ignored-and-hidden novelty searches and "
            "structured OWL review found no exact term. Reserved METPO:1055500 "
            "in v478 under the released phenotype parent. Recorded indexed "
            "abstract access limits, growth confounds and pending narrower "
            "METPO hierarchy; deferred canonical strains and causal graphs."
        ),
        llm_assisted=True, timestamp="2026-10-04T17:35:43Z",
    )
    record_curation_event(
        record, curator="codex", action="EVIDENCE_CORRECTION",
        changes=(
            "Addressed #1676: replaced the margin-reorientation abstract quote "
            "with a contiguous oxygen-gradient passage so the definition "
            "snippet identifies the stimulus. Retained reorientation evidence, "
            "source-access limits and growth confounds in notes."
        ),
        llm_assisted=True, timestamp="2026-10-04T17:43:50Z",
    )
    record_curation_event(
        record, curator="codex", action="REVIEW_CORRECTION",
        changes=(
            "Addressed #1678 and #1679: removed the two snippets obtained "
            "only from indexed publisher text. Prior history describes "
            "those now-withdrawn quotes, not directly verified source wording. "
            "Retained qualified DOI-backed interpretations in notes and the "
            "directly verified Damm snippet. Changed the definition genus "
            "to phenotype to match the released proposal parent, preserving "
            "the local chemotropism parent and pending hierarchy explanation."
        ),
        llm_assisted=True, timestamp="2026-10-04T18:01:14Z",
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
        "METPO:1055500", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/aerotropism.yaml|{AOKI}|{CARLILE}|{DAMM}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Oxygen-gradient-directed growth; local chemotropism parent awaits v474 acceptance.",
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
