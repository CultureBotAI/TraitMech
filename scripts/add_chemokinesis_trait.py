"""Add chemokinesis while separating speed responses from directional taxis."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000586"
TARGET = ROOT / "data/traits/physiology/chemokinesis.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v463"
GARREN = "DOI:10.1038/ismej.2013.210"
SON = "DOI:10.1073/pnas.1602307113"
GAO = "DOI:10.1038/s41396-021-01024-7"
STRAIN = "DOI:10.7717/peerj.17126"
INITIAL_DRAFT_SHA256 = "14a703054d337fcf604684192481b002c3b4802310cf3c10b834f792fb9ecbc9"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "chemokinesis",
    "definition": (
        "A motile phenotype in which swimming speed changes in response to "
        "chemical concentration, without requiring directional bias along a "
        "chemical gradient."
    ),
    "definition_source": GARREN,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000702"],
    "evidence": [
        {
            "reference": GARREN,
            "snippet": (
                "chemokinesis is the ability to change swimming speed in response "
                "to a change in chemical concentration."
            ),
            "notes": (
                "Discussion, page 1005, visually checked in the author-hosted "
                "published PDF at https://stockerlab.ethz.ch/wp-content/uploads/"
                "2015/03/49.-Garren_etal_ISME_2014.pdf. This bacterial usage defines "
                "chemokinesis by speed, in contrast to chemotactic directional bias. "
                "The two responses can coexist. This citation supports identity; "
                "no independent reanalysis of its supplementary assays is claimed."
            ),
        },
        {
            "reference": SON,
            "snippet": (
                "Chemokinesis was also observed in the absence of a chemical gradient"
            ),
            "notes": (
                "SI Text, Chemokinesis, page 3 of 9; full article and SI inspected "
                "at https://pmc.ncbi.nlm.nih.gov/articles/PMC4978249/. Figure S5 "
                "and its caption were visually checked in the author PDF at "
                "https://stockerlab.ethz.ch/wp-content/uploads/2017/05/89._Son_atall.pdf "
                "(SI page 7 of 9). The uniform-serine assay supports a speed "
                "response without a gradient. Model block removals are in silico "
                "mutants, not biological gene deletions. YM4 cells were harvested "
                "in late exponential phase and resuspended in TMN motility medium, "
                "pH 7.5; Figure S5 uses uniform 5 micromolar serine at 600 mM sodium. "
                "YM4 is a laboratory mutant deficient in lateral flagella, as "
                "documented separately by DOI:10.7717/peerj.17126; it is retained "
                "as qualified experimental evidence, not a natural canonical example."
            ),
        },
        {
            "reference": GAO,
            "snippet": (
                "Thus, we hypothesize that the metabolism of mucus substrate "
                "stimulates Na+-NQR activity, which in turn enables sustained chemokinesis."
            ),
            "notes": (
                "Discussion, page 3677, visually checked at "
                "https://stockerlab.ethz.ch/wp-content/uploads/2022/03/"
                "141.-Cherry-Gao_Coral-Muscus.pdf. The plus is superscript in "
                "the typeset sodium notation and plain text in extraction. "
                "The following sentence requires experimental testing of this "
                "hypothesis. Transcript associations do not establish a causal "
                "protein pathway; no supplementary gene-level result is curated here."
            ),
        },
        {
            "reference": STRAIN,
            "snippet": (
                "two strains showing defects in the lateral flagellum (VIO5 and YM4)"
            ),
            "notes": (
                "Abstract, PMID:38515459. This primary genomic study identifies "
                "YM4 as a laboratory strain with defective lateral flagellation. "
                "It supplies strain provenance, not a chemokinesis measurement. "
                "The Son observation must not be generalized to unperturbed "
                "Vibrio alginolyticus. Canonical examples are deferred pending "
                "separate verification of a natural exemplar (issue #1653)."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "chemokinesis-speed-and-taxis-boundaries",
            "prompt": "Preserve the source-defined speed response and its distinction from taxis.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This record follows the swimming-speed usage in Garren, Son and "
                "Gao. Chemotaxis (traitmech:000086) concerns directional bias. "
                "No equivalence, disjointness or parent-child relation between "
                "them is asserted. A speed response can occur with or without "
                "chemotaxis and need not always be an increase. Existing research "
                "also uses chemokinesis more broadly for changes in turning "
                "frequency. Reconcile that broader usage, orthokinesis and "
                "klinokinesis before adding synonyms, narrower terms or xrefs; "
                "do not equate a turning-only response with this speed definition."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-04",
        },
        {
            "discussion_id": "chemokinesis-mechanism-grounding",
            "prompt": "Distinguish observed behavior from model ablations and molecular hypotheses.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Son's computational removal of functional blocks is not a "
                "gene-knockout experiment. Gao's Na+-NQR explanation is explicitly "
                "hypothetical, with further experimental work requested. A "
                "mechanistic graph is deferred pending source-backed causal "
                "edges and eligible taxon-paired protein examples. Do not borrow "
                "the enterobacterial Che pathway from chemotaxis, infer causality "
                "from transcript changes, or use NONMECHANISTIC to bypass the "
                "protein-coverage requirement. No universal receptor is asserted."
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
            "Added chemokinesis with three primary DOI citations, contiguous "
            "snippets and a uniform-serine YM4 example at verified species "
            "taxon 663. Ignored-and-hidden searches found only a chemotaxis "
            "boundary mention, not an exact record or METPO class. Reserved "
            "METPO:1054000 in proposal v463. Kept speed, directional bias, "
            "computational ablations and molecular hypotheses separate."
        ),
        llm_assisted=True, timestamp="2026-10-04T04:08:00Z",
    )
    record_curation_event(
        record, curator="codex", action="QUALIFY_EXPERIMENTAL_STRAIN",
        changes=(
            "Addressed adversarial review #1653: added primary YM4 strain "
            "provenance, removed the laboratory-mutant canonical example, and "
            "retained its uniform-serine speed response in qualified evidence. "
            "Natural canonical exemplars remain deferred."
        ),
        llm_assisted=True, timestamp="2026-10-04T04:09:00Z",
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
        "METPO:1054000", record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/chemokinesis.yaml|{GARREN}|{SON}|{GAO}",
        "METPO:1000702", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Chemical-dependent swimming-speed response; directional bias is not required.",
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
    if TARGET.exists():
        existing = yaml.safe_load(TARGET.read_text())
        digest = hashlib.sha256(json.dumps(existing, sort_keys=True).encode()).hexdigest()
        if existing != record and digest != INITIAL_DRAFT_SHA256:
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
