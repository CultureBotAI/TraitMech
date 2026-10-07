"""Add endocytosis and refine the pinocytosis/phagocytosis hierarchy."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/endocytosis.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v512/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000636"
METPO_ID = "METPO:1058900"
FIRST = "DOI:10.1083/jcb.128.5.779"
SECOND = "DOI:10.1128/mcb.14.11.7245-7255.1994"
TIMESTAMP = "2026-10-06T06:47:04Z"
PARENT = {
    "identifier": "METPO:1000059",
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
CHILD_PATHS = {
    slug: ROOT / f"data/traits/physiology/{slug}.yaml"
    for slug in ("pinocytosis", "phagocytosis")
}
CHILDREN = {
    "pinocytosis": {
        "identifier": "traitmech:000635",
        "label": "pinocytosis",
        "definition": (
            "A physiological phenotype in which a microbial organism internalizes "
            "surrounding extracellular fluid and dissolved material into "
            "membrane-bound compartments formed from its plasma membrane."
        ),
        "definition_source": "DOI:10.1083/jcb.53.3.681",
        "mapping_status": "PROPOSED", "trait_category": "PHYSIOLOGY", "term_kind": "CLASS",
    },
    "phagocytosis": {
        "identifier": "traitmech:000627",
        "label": "phagocytosis",
        "definition": (
            "A physiological phenotype in which a microbial cell engulfs "
            "extracellular particles by enclosing them within its membrane "
            "and internalizes them into membrane-bound compartments."
        ),
        "definition_source": "DOI:10.1371/journal.pone.0095577",
        "mapping_status": "PROPOSED", "trait_category": "PHYSIOLOGY", "term_kind": "CLASS",
    },
}
DISCUSSIONS = {
    "pinocytosis": "pinocytosis-scope-and-hierarchy",
    "phagocytosis": "phagocytosis-trait-and-process-scope",
}
RATIONALE_SHA256 = {
    "pinocytosis": "cffa12edb67265fddfaebc408f12c9dea02e155d9db64a16f467a87b34b4bfca",
    "phagocytosis": "d03877f5d649652a09768e914393a25ad43ef8c6953c378913d6d5969aafaab7",
}
PINOCYTOSIS_RESOLUTION = (
    "Added endocytosis traitmech:000636 as the direct broader phenotype. "
    "The existing fluid-internalization definition entails this membrane-bound "
    "uptake scope. This resolves the temporary parent gap, not the separate "
    "Neff taxonomy or native-mechanism discussions; the historical scope "
    "contrasts and unasserted mappings remain applicable. Preserve the v511 "
    "phenotype axiom and add METPO:1058800 SubClassOf METPO:1058900 upstream."
)
OLD_PHAGOCYTOSIS_PARENT = "Phenotype METPO:1000059 is the supported broader trait."
NEW_PHAGOCYTOSIS_PARENT = (
    "Endocytosis traitmech:000636 is the direct broader trait because the "
    "existing particle-enclosure definition entails membrane-bound "
    "internalization; phenotype METPO:1000059 remains an ancestor."
)
CHANGES = {
    "pinocytosis": (
        "Refined the direct parent to endocytosis traitmech:000636 and resolved "
        "the temporary parent gap by definition-based inference. Preserved "
        "the historical rationale, definition, evidence, Neff example, "
        "independent taxonomy/mechanism discussions and prior history."
    ),
    "phagocytosis": (
        "Refined the direct parent to endocytosis traitmech:000636 by "
        "definition-based inference. Updated only the parent statement in "
        "the scope discussion, which remains OPEN for process-mapping "
        "review. Preserved definition, evidence, example and prior history."
    ),
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "endocytosis",
    "definition": (
        "A physiological phenotype in which a microbial cell takes up "
        "extracellular material or plasma-membrane components into "
        "intracellular membrane-bound compartments by remodeling and "
        "internalizing its plasma membrane."
    ),
    "definition_source": FIRST,
    "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": FIRST,
            "snippet": (
                "After an additional 20-40 min, the PM and cytoplasmic punctate "
                "staining disappeared concomitant with staining of the vacuolar membrane."
            ),
            "notes": (
                "PMID:7533169, PMC2120394. Scientific Abstract quote verified "
                "in Europe PMC XML; full-text OCR, including Introduction, "
                "Methods, Results and Discussion, was read at "
                "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2120394/fullTextXML. "
                "FM 4-64 tracks plasma-membrane-to-vacuole transport in "
                "Saccharomyces cerevisiae. Early experiments used BHY10.5, "
                "a CPY-invertase reporter background, not the SEY6210 control "
                "in later mutant comparisons. Endosome identity is qualified "
                "as likely. Mutant effects on vacuolar delivery are not "
                "necessarily initial-internalization defects; in vitro "
                "ATP/cytosol dependence concerns later transport. Marker-specific "
                "results do not establish a universal route. PDF/figures "
                "were unavailable and were not visually audited."
            ),
        },
        {
            "reference": SECOND,
            "snippet": (
                "This report presents direct evidence for alpha-factor-induced "
                "internalization of cell surface receptors."
            ),
            "notes": (
                "PMID:7935439, PMC359259. Scientific Abstract directly read "
                "in NCBI PubMed XML and Europe PMC metadata, which agree on "
                "this DOI. Density fractionation and extracellular-protease "
                "protection support receptor internalization in "
                "Saccharomyces cerevisiae. The abstract distinguishes receptor "
                "signaling, internalization and subsequent vacuolar degradation. "
                "No fixed transit time or universal receptor requirement is "
                "imposed. Full text and figures were unavailable: the "
                "Europe PMC full-text endpoint returned HTTP 500 and the "
                "indexed PDF mirror returned 404. Strain provenance and "
                "unread assay details are not inferred."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "endocytosis-scope-and-hierarchy",
            "prompt": "Distinguish membrane-bound uptake from neighboring capabilities.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "This is the microbial cell's uptake phenotype, not a host "
                "response, a sequence feature or intracellular trafficking "
                "alone. Surface adsorption, passive diffusion, transporter "
                "entry, open membrane invaginations and autophagy alone are "
                "insufficient. Pinocytosis traitmech:000635 and phagocytosis "
                "traitmech:000627 entail this scope; macropinocytosis "
                "traitmech:000634 remains below pinocytosis. No fixed size, "
                "clathrin/actin dependence, nutritional assimilation or "
                "degradation is required. Trogocytosis traitmech:000633 "
                "describes removal and uptake of living-cell portions without "
                "universally specifying membrane-bound enclosure. Myzocytosis "
                "traitmech:000631 describes prey-content aspiration. Its cited "
                "2023 Discussion (DOI:10.3390/microorganisms11081945) calls "
                "myzocytosis a form of endocytosis in the studied Colpodella "
                "system; that source-attributed umbrella usage is retained, "
                "not treated as proof that every aspiration phenotype meets "
                "this operational membrane-bound scope. Their broader parent "
                "decisions remain unresolved, not exclusions or disjointness "
                "claims. Nutritional phagotrophy is not an equivalent. "
                "Review process-level ontology mappings separately; no "
                "unverified synonyms or xrefs are asserted."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
        {
            "discussion_id": "endocytosis-exemplar-and-mechanism",
            "prompt": "Resolve strain provenance and route-specific molecular evidence.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "The two independent studies both concern laboratory "
                "Saccharomyces cerevisiae, not independent taxon replication. "
                "BHY10.5's reporter background is not a natural isolate; the "
                "1994 full methods and strain provenance remain unread. "
                "Canonical examples are left unset rather than generalize "
                "these assays to every strain or claim a wild-type provenance. "
                "Membrane-tracer transport, receptor uptake and fluid uptake "
                "need not report identical routes. The 1995 authors discuss "
                "nonvesicular alternatives and qualify endosome identity. "
                "No complete molecular mechanism, protein accessions or "
                "causal graph are inferred from tracer behavior or abstracts. "
                "Obtain taxon-paired functional and strain-provenance evidence "
                "before adding those fields."
            ),
            "posed_by": "codex", "posed_date": "2026-10-06",
        },
    ],
}


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(record, curator="codex", action=action, changes=changes,
                         llm_assisted=True, timestamp=TIMESTAMP)


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(record, "MINTED_TRAITMECH_ID", (
        "Added endocytosis with two DOI-backed scientific-abstract snippets "
        "and explicit strain, assay and access limits. Ignored-and-hidden "
        "searches and pinned METPO review found no exact record. Reserved "
        "METPO:1058900 in v512; refined pinocytosis and phagocytosis parents "
        "without asserting unverified mappings or a molecular mechanism."
    ))
    return record


def build_child(slug: str, record: dict) -> dict:
    record = copy.deepcopy(record)
    if any(record.get(k) != v for k, v in CHILDREN[slug].items()):
        raise SystemExit(f"{slug} identity or scope differs from reviewed preimage")
    matches = [d for d in record.get("discussions", [])
               if d.get("discussion_id") == DISCUSSIONS[slug]]
    if len(matches) != 1:
        raise SystemExit(f"{slug} discussion identity differs")
    discussion = matches[0]
    rationale = discussion.get("rationale", "")
    replay = record.get("parent_traits") == [IDENTIFIER]
    if replay and slug == "phagocytosis":
        if rationale.count(NEW_PHAGOCYTOSIS_PARENT) != 1:
            raise SystemExit(f"{slug} replay differs from reviewed result")
        rationale = rationale.replace(NEW_PHAGOCYTOSIS_PARENT, OLD_PHAGOCYTOSIS_PARENT)
    if (discussion.get("kind") != "CURATION_TODO"
            or hashlib.sha256(rationale.encode()).hexdigest() != RATIONALE_SHA256[slug]):
        raise SystemExit(f"{slug} discussion scope differs")
    expected = {}
    event(expected, "REFINE_ENDOCYTOSIS_PARENT", CHANGES[slug])
    expected_event = expected["curation_history"][0]
    history = record.get("curation_history", [])
    resolved = slug == "pinocytosis"
    if replay:
        if (discussion.get("status") != ("RESOLVED" if resolved else "OPEN")
                or (resolved and (discussion.get("resolved_date") != "2026-10-06"
                                  or discussion.get("resolution_note") != PINOCYTOSIS_RESOLUTION))
                or (not resolved and ("resolved_date" in discussion or "resolution_note" in discussion))
                or not history or history[-1] != expected_event):
            raise SystemExit(f"{slug} replay differs from reviewed result")
        return record
    if (record.get("parent_traits") != [PARENT["identifier"]]
            or discussion.get("status") != "OPEN"
            or "resolved_date" in discussion or "resolution_note" in discussion
            or expected_event in history):
        raise SystemExit(f"{slug} hierarchy or discussion state differs")
    record["parent_traits"] = [IDENTIFIER]
    if resolved:
        discussion.update(status="RESOLVED", resolved_date="2026-10-06",
                          resolution_note=PINOCYTOSIS_RESOLUTION)
    else:
        if rationale.count(OLD_PHAGOCYTOSIS_PARENT) != 1:
            raise SystemExit(f"{slug} parent statement differs")
        discussion["rationale"] = rationale.replace(OLD_PHAGOCYTOSIS_PARENT,
                                                    NEW_PHAGOCYTOSIS_PARENT)
    event(record, "REFINE_ENDOCYTOSIS_PARENT", CHANGES[slug])
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join(["TraitMech:data/traits/physiology/endocytosis.yaml", FIRST, SECOND]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Membrane-bound uptake; add the v503/v511 child axioms documented in proposal.md.",
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
    if any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs")
    record = build_record()
    children = {slug: build_child(slug, yaml.safe_load(path.read_text()))
                for slug, path in CHILD_PATHS.items()}
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        for slug, child in children.items():
            write_validated_trait(child, Path(tmp) / CHILD_PATHS[slug].name)
    if args.apply:
        write_validated_trait(record, TARGET)
        for slug, child in children.items():
            write_validated_trait(child, CHILD_PATHS[slug])
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
