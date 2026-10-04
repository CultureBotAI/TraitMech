"""Add electric-field-directed growth with bounded bacterial and fungal evidence."""

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

IDENTIFIER = "traitmech:000595"
TARGET = ROOT / "data/traits/physiology/galvanotropism.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v472"
RAJNICEK = "DOI:10.1128/jb.176.3.702-713.1994"
CROMBIE = "DOI:10.1099/00221287-136-2-311"
BRAND = "DOI:10.1016/j.cub.2006.12.043"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "galvanotropism",
    "definition": (
        "A phenotype in which growth is directionally oriented or reoriented "
        "in response to an electric field."
    ),
    "definition_source": RAJNICEK,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": RAJNICEK,
            "snippet": (
                "Field-treated (but not control) Enterobacter cloacae and "
                "Escherichia coli cells curved rapidly toward the anode."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:8300526; "
                "PMCID:PMC205108); full text not inspected. Curvature depended "
                "on field strength and pH and reversed with field polarity. "
                "The authors report controls excluding passive bending and "
                "field-induced gradients of tropic substances in their assay. "
                "Bacillus subtilis required a higher field threshold. "
                "Spatial wall-growth measurements support growth asymmetry, "
                "not a resolved universal electrical sensor. The historical "
                "actin-absence premise is not adopted as current biology."
            ),
        },
        {
            "reference": CROMBIE,
            "snippet": (
                "germ tubes grew unidirectionally towards the cathode for "
                "extended periods and did not deviate to a perpendicular "
                "orientation."
            ),
            "notes": (
                "Abstract, exact-matched at Europe PMC (PMID:2182770); full "
                "text not inspected. Candida albicans cells were attached to "
                "polylysine-coated slides. Budding and germ-tube emergence "
                "sites, as well as subsequent growth, were biased toward the "
                "cathode. Higher fields delayed emergence and reduced extension "
                "rate; those effects are not themselves directional growth. "
                "Cathodal growth here does not imply one electrode preference "
                "for all microbial galvanotropism."
            ),
        },
        {
            "reference": BRAND,
            "snippet": (
                "extending hyphae grew toward the cathode and reoriented "
                "their direction of growth when the field polarity was reversed"
            ),
            "notes": (
                "Full-text Results, Calcium Ions and CaCch1p Mediate Cathodal "
                "Germ-Tube Emergence (PMID:17275302; PMCID:PMC1885950), "
                "https://pmc.ncbi.nlm.nih.gov/articles/PMC1885950/. Exact "
                "contiguous JATS paragraph span, not an abstract quote. "
                "Main Figs. 1 and 2 and supplemental Table S1 were inspected. "
                "The quoted response occurred even in low-calcium medium. "
                "Calcium depletion, channel blockers and CCH1 deletion "
                "primarily reduced cathodal emergence; after six hours, "
                "tip orientation could recover. Calcineurin perturbations "
                "affected cathodal emergence, not thigmotropism. Localized "
                "channel activation is a proposed model, not direct proof "
                "of a universal sensor. The supplement identifies CAI4/CIp10 "
                "as the isogenic control (NGY152) and lists engineered "
                "derivatives. These are qualified experimental backgrounds, "
                "not verified natural canonical exemplars."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "galvanotropism-growth-and-field-boundaries",
            "prompt": "Keep directional growth separate from movement and passive field effects.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Growth orientation is not whole-cell locomotion; the parent "
                "is phenotype, not motile. The existing galvanotaxis record "
                "(traitmech:000581) denotes active migration, and thigmotropism "
                "(traitmech:000594) denotes contact-directed polarized growth. "
                "Passive displacement, bending, alignment or changes in "
                "growth rate alone are insufficient. Do not conflate "
                "galvanotropism with electron uptake or current production. "
                "The bacterial anodal and fungal cathodal observations do "
                "not support an invariant electrode preference. A QuickGO "
                "galvanotropism search returned no hits on 2026-10-04; "
                "broader electric-field responses are not exact xrefs. "
                "Other external equivalences and electrotropism as a lexical "
                "variant require separate authority and scope checks."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "galvanotropism-stage-and-mechanism-grounding",
            "prompt": "Resolve natural-strain evidence and distinguish emergence from maintenance.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The full fungal study distinguishes establishment of "
                "cathodal growth from maintenance of tip orientation. Do not "
                "turn its aggregate abstract claim into a requirement for "
                "calcium influx at every stage. Its supplemental Table S1 "
                "and methods identify an engineered CAI4/CIp10 control and "
                "mutant or complemented derivatives; a wild-type label alone "
                "does not establish natural provenance. Inspect the older "
                "studies' full methods and resolve natural strains with NCBI "
                "identities before adding canonical examples. Resolve "
                "taxon-paired protein accessions and stage-specific causal "
                "claims before adding a mechanism graph. Do not transfer "
                "fungal channel dependence to bacteria or adopt the 1994 "
                "paper's historical actin-absence premise. A NONMECHANISTIC "
                "graph must not bypass missing protein grounding."
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
            "Added galvanotropism with three primary DOI citations, two "
            "abstract snippets and one full-text snippet. Ignored-and-hidden "
            "novelty searches and structured OWL review found no exact "
            "record or METPO term. Reserved METPO:1054900 in v472. "
            "Distinguished directional growth from galvanotaxis and "
            "thigmotropism without requiring one electrode preference. "
            "Inspected Brand full text, Figs. 1 and 2 and supplement; kept "
            "emergence distinct from later orientation and deferred natural "
            "canonical examples and accession-level mechanism grounding."
        ),
        llm_assisted=True, timestamp="2026-10-04T11:09:43Z",
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
        "METPO:1054900", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/galvanotropism.yaml|{RAJNICEK}|{CROMBIE}|{BRAND}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Electric-field-directed growth; not locomotion, passive bending or an invariant pole preference.",
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
