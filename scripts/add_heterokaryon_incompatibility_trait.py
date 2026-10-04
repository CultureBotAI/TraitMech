"""Add heterokaryon incompatibility with source-bounded postfusion scope."""

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

IDENTIFIER = "traitmech:000606"
TARGET = ROOT / "data/traits/physiology/heterokaryon_incompatibility.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v483"
HUTCHISON = "DOI:10.1099/mic.0.032284-0"
MAREK = "DOI:10.1016/s1087-1845(03)00086-0"
SMITH = "DOI:10.3852/mycologia.98.1.43"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "heterokaryon incompatibility",
    "definition": (
        "A fungal phenotype in which postfusion nonself recognition restricts "
        "the establishment or growth of viable vegetative heterokaryons."
    ),
    "definition_source": HUTCHISON,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": HUTCHISON,
            "snippet": (
                "Incompatible heterokaryons show a macroscopic phenotype of slow "
                "growth and diminished conidiation, and a microscopic phenotype "
                "of hyphal compartmentation and cell death."
            ),
            "notes": (
                "Hutchison et al. (2009), PMID:19696111. The directly retrieved "
                "Europe PMC abstract and publisher abstract identify nonself "
                "recognition during fusion between strains differing at het loci, "
                "with restricted growth and localized cell death. This supports "
                "postfusion heterokaryon incompatibility, not failure to approach "
                "or fuse. The study combines transcriptional profiling with "
                "functional analysis of het-c pin-c incompatibility in Neurospora "
                "crassa. Transcript associations do not establish causal edges; "
                "the abstract reports that tested caspase and AIF homologues "
                "were not required. Full text, figures and supplements were not "
                "retrieved, so no detailed assay or protein-dependency claim "
                "beyond the abstract is asserted."
            ),
        },
        {
            "reference": MAREK,
            "snippet": (
                "Hyphal fusion cells in compatible self-pairings and hyphal "
                "cells in het-c compatible transformants were not compartmentalized "
                "and rarely showed TUNEL-positive nuclei."
            ),
            "notes": (
                "Marek et al. (2003), PMID:14516765; snippet exact-matched to "
                "the directly retrieved Europe PMC abstract. Incompatible "
                "Neurospora crassa pairings differing at mat, het-c and het-6 "
                "were compared with compatible self-pairings; separate "
                "transformant experiments tested incompatible het-c alleles. "
                "The abstract reports septal compartmentation and nuclear DNA "
                "degradation in incompatible cells, contrasted with the quoted "
                "controls. TUNEL and apoptosis-like morphology do not identify "
                "a conserved metazoan apoptosis pathway. Death also occurred "
                "in older hyphae, so death alone is not specific for this trait. "
                "Full text, figures, supplements and original strain provenance "
                "were not inspected; no natural canonical exemplar is inferred "
                "from the transformed assay."
            ),
        },
        {
            "reference": SMITH,
            "snippet": (
                "While clearly forming barrages in mycelial interactions, paired "
                "strains with different alleles at vic4 formed stable heterokaryons."
            ),
            "notes": (
                "2006 primary study, PMID:16800303; snippet exact-matched to the "
                "directly retrieved Europe PMC abstract. Hygromycin B- and "
                "benomyl-resistance forcing markers were used in Cryphonectria "
                "parasitica pairings. Differences at vic1, vic2, vic3, vic6 or "
                "vic7, but not vic4, produced heterokaryon incompatibility "
                "readouts of slow growth or abnormal morphology. The vic4 "
                "counterexample separates barrage formation from this trait; "
                "the abstract treats heterokaryon incompatibility as a component "
                "of a broader vegetative incompatibility system. Vegetative "
                "incompatibility is therefore not asserted as an exact synonym. "
                "Full text, figures, supplements and marker-strain provenance "
                "were not inspected. The DOI and any publisher alias identify "
                "one study, not independent replications."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "heterokaryon-incompatibility-scope",
            "prompt": "Keep postfusion incompatibility distinct from broader vegetative barriers.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This organismal phenotype is not a het/vic locus, protein "
                "domain, sequence feature or individual pairing result. It "
                "requires nonself recognition, not merely slow growth or cell "
                "death. Barrage formation, prefusion avoidance, negative "
                "autotropism, sexual incompatibility and inability to fuse are "
                "not exact equivalents. Hyphal anastomosis can precede this "
                "response and is not an is-a parent. The definition does not "
                "require death of the whole colony, failure of every nonself "
                "pairing or a single conserved death pathway. The 2006 vic4 "
                "result prevents treating vegetative incompatibility as an "
                "unqualified exact synonym. Resolve organismal ontology "
                "equivalences at their issuing authorities before adding xrefs."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "heterokaryon-incompatibility-mechanism-provenance",
            "prompt": "Read experimental details and resolve strain and protein anchors before enrichment.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Three primary abstracts support the phenotype and its boundary; "
                "full texts, figures and supplements remain unread. Separate "
                "natural pairing observations from transformants, forced "
                "heterokaryons and partial-diploid models when assessing "
                "canonical examples. Verify original strain provenance and "
                "current NCBI identities before adding taxon rows. Protein "
                "accessions, taxon pairing and native perturbation/rescue "
                "details must be checked before a causal graph is added. "
                "Transcript changes and TUNEL-positive nuclei are readouts, "
                "not proof of ROS necessity or canonical apoptosis. Do not "
                "use NONMECHANISTIC to hide unresolved protein mechanisms."
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
            "Added heterokaryon incompatibility as a postfusion nonself "
            "recognition phenotype with three directly retrieved primary "
            "DOI-backed abstracts and exact snippets. Distinguished barrage "
            "formation and broader vegetative incompatibility; no exact "
            "synonyms, canonical examples or causal graph are asserted. "
            "Ignored-and-hidden repository searches and structured METPO "
            "review found no exact trait. Reserved METPO:1056000 in proposal "
            "v483 under released phenotype. Deferred unread full texts, "
            "strain provenance, protein grounding and external equivalences."
        ),
        llm_assisted=True, timestamp="2026-10-04T23:02:57Z",
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
        "METPO:1056000", record["label"], record["definition"],
        "TraitMech:data/traits/physiology/heterokaryon_incompatibility.yaml"
        f"|{HUTCHISON}|{MAREK}|{SMITH}",
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Postfusion nonself recognition; barrage formation alone is insufficient.", IDENTIFIER,
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
