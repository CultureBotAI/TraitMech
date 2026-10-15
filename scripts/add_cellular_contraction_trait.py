"""Add a cellular-shortening parent and preserve two narrower child scopes."""

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
SLUG = "cellular_contraction"
TARGET = ROOT / f"data/traits/physiology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v605/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000729"
METPO_ID = "METPO:1068200"
TIMESTAMP = "2026-10-14T22:35:09Z"
DATE = TIMESTAMP[:10]
KATOH = "DOI:10.1242/jeb.189.1.163"
KHAN = "DOI:10.2108/zsj.20.1367"
FEBVRE = "DOI:10.1083/jcb.118.3.585"
PARENT = {
    "identifier": "METPO:1000059", "label": "phenotype",
    "definition": "A quality that differentiates specific instances of a species from other instances of the same species.",
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER", "term_kind": "CLASS", "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
CHILDREN = {
    "cell_body_contraction": ("traitmech:000728", "cell-body-contraction-scope-and-parent"),
    "rapid_axopodial_contraction": ("traitmech:000682", "axopodial-contraction-scope-and-parent"),
}
CHILD_PATHS = {slug: ROOT / f"data/traits/physiology/{slug}.yaml" for slug in CHILDREN}
PREIMAGE_SHA256 = {
    "cell_body_contraction": "7c3603133f82fe3e68b2137c500809955eccfc06951e9457e70d4eaf8dace0e1",
    "rapid_axopodial_contraction": "5dd74cb0e052cebd5a30adb67d2361763599cb48d8a803b219da75f4574d66a5",
}
OLD_KHAN_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14624035&resultType=core&format=json"
NEW_KHAN_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14624035%20AND%20SRC%3AMED&resultType=core&format=json"
RESOLUTION = (
    "Added cellular contraction (body or cytoplasmic projection shortening) "
    "traitmech:000729 as the direct broader phenotype. This is a definition-based "
    "subclass inference, not a new child experiment or evidence of a common "
    "molecular mechanism. Phenotype METPO:1000059 remains an ancestor. Preserved "
    "the historical rationale and endpoint boundaries; the v605 proposal requests "
    "the child axiom without rewriting the historical proposal cohort."
)
AXOPODIAL_RESOLUTION = (
    RESOLUTION + " Only the hierarchy question is resolved here. The independent "
    "time-resolved assay question is retained OPEN in "
    "axopodial-contraction-assay-comparability; provenance and mechanism remain OPEN."
)
ASSAY_DISCUSSION = {
    "discussion_id": "axopodial-contraction-assay-comparability",
    "prompt": "Establish comparable time-resolved assays for rapid axopodial contraction.",
    "kind": "CURATION_TODO", "status": "OPEN",
    "rationale": (
        "Carried forward from axopodial-contraction-scope-and-parent when only its "
        "hierarchy gap was resolved. Preserve stimulus, cell state, projection "
        "identity, length readout and temporal resolution when comparing assays. "
        "The published speed is not a universal cutoff; re-elongation, slow "
        "structural loss and drug-induced microtubule disassembly alone do not "
        "establish the rapid physiological response. No new comparative assay "
        "or biological experiment was performed by this hierarchy repair."
    ),
    "posed_by": "codex", "posed_date": DATE,
}
CHILD_CHANGE = (
    "Refined the direct parent to cellular contraction traitmech:000729 by "
    "definition-based inference. Preserved child definition, supporting excerpts, "
    "prior curation history and independent provenance/mechanism gaps. Resolved "
    "only the parent question. No new experiment, "
    "canonical taxon or molecular mechanism is asserted."
)
AXOPODIAL_CHANGE = (
    CHILD_CHANGE + " Retained the independent assay-comparability question OPEN "
    "and qualified the Khan Europe PMC URL to SRC:MED using the verified identity."
)
RECORD = {
    "identifier": IDENTIFIER,
    "label": "cellular contraction (body or cytoplasmic projection shortening)",
    "definition": (
        "A physiological phenotype in which a microbial cell actively contracts "
        "its body or a cytoplasmic projection, reducing its length or extension."
    ),
    "definition_source": KATOH,
    "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {
            "reference": KATOH,
            "snippet": "Living Vorticella showed a graded shrinkage of the cell body when Ca2+ buffer was injected into the cell body",
            "notes": (
                "Katoh and Naitoh 1994, PMID:9317557, scientific Abstract item 3, "
                "first clause. Direct namespace-qualified Europe PMC MED match; "
                "native VERIFIED. The same sentence contrasts graded cell-body "
                "shrinkage with all-or-nothing stalk coiling. This supports the "
                "curator-synthesized body/projection-shortening parent, not a "
                "universal calcium threshold. Other abstract items use "
                "Triton-extracted preparations, not the living-cell injection "
                "assay. Calcium-induced calcium release is an assumption, not "
                "direct molecular proof. Publisher requests returned 403; full "
                "Methods, figures and strain provenance were not accessed."
            ),
        },
        {
            "reference": KHAN,
            "snippet": "Axopodial contraction of the centrohelid heliozoon Raphidiophrys contractilis was induced by mechanical or electrical stimulation.",
            "notes": (
                "Khan et al. 2003, PMID:14624035, scientific Abstract opening "
                "sentence. Direct namespace-qualified Europe PMC MED match; "
                "native VERIFIED. This supports stimulated shortening of a "
                "cytoplasmic projection rather than whole-cell locomotion. "
                "Reported calcium dependence and speed apply to this assay, "
                "not every member of the parent class. Non-detection of other "
                "filaments after fixation is not proof of their absence. Full "
                "Methods and figures were not accessed; the publisher's HTTP "
                "200 response was an access challenge, not readable article "
                "content. Current taxonomic and culture identities remain unresolved."
            ),
        },
        {
            "reference": FEBVRE,
            "snippet": "Both recording techniques showed that the rapid contraction involves 80% of the total cell length.",
            "notes": (
                "Febvre-Chevalier and Febvre 1992, PMID:1639845, PMCID:PMC2289557, "
                "Results, Kinetics of the Contraction, printed page 588, right "
                "column. Direct extracted-PDF match with the typeset passage "
                "visually checked; native NOT_IN_ABSTRACT retained. The primary "
                "PDF was retrieved from its Semantic Scholar mirror after "
                "official PDF attempts failed. Selected Methods/Results and "
                "actual Figures 1 and 3-6 were inspected. Length was measured "
                "from head top to stalk base, not isolated cell-body length; "
                "graph axes use stalk length. The percentage is study-specific. "
                "Natural-seawater responses differ from artificially slowed "
                "responses. The specimens were collected near Villefranche and "
                "cultured at 14-18 C; current taxonomic identity is not verified. "
                "The n=20 initial-length sample is not asserted as independent "
                "contraction replication. Microtubule disassembly accompanies "
                "shortening, but this study expressly does not establish force "
                "production. Its disassembly half-time is not automatically "
                "contraction duration. The accessible JATS contains an abstract "
                "and PDF pointer, not the complete experimental text."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "cellular-contraction-scope-and-mappings",
            "prompt": "Review the shortening-defined parent without equating all contractility endpoints.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Require active reduction of cell-body length or the extension "
                "of a cytoplasmic projection. Generic force production or "
                "isometric contractility alone is insufficient. Extracellular "
                "pilus retraction, injection-system contraction, contractile-vacuole "
                "cycling and cytokinetic constriction alone do not establish "
                "this endpoint. Neither passive osmotic shrinkage, death-associated "
                "shortening nor static short-cell morphology suffices. The "
                "existing body and rapid axopodial traits are narrower children; "
                "stalk contraction remains a possible future child, not a new "
                "allocation here. Motility METPO:1000701 and motile METPO:1000702 "
                "concern locomotion, not necessarily shortening. Active denotes "
                "the cellular response, not demonstrated ATP-driven motor action. "
                "No universal speed, fractional shortening, trigger, calcium "
                "threshold, ATP dependence, ecological role, exact synonym for "
                "generic contractility or organism-level disjointness is asserted."
            ),
            "posed_by": "codex", "posed_date": DATE,
        },
        {
            "discussion_id": "cellular-contraction-metpo-assessment",
            "prompt": "Review the proposed shortening phenotype and its upstream hierarchy.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Pinned/current METPO releases, editor and inspected template "
                "owners yielded no active exact class in the bounded identity "
                "assessment. Deprecated Motility METPO:0000006 and METPO:000006 "
                "lead to METPO:1000701; deprecated Motile METPO:0000087 and "
                "METPO:000088 lead to METPO:1000702. These are related locomotion "
                "concepts, not exact replacements for shortening. They are not "
                "revived or put in xrefs. Keep phenotype METPO:1000059 as the "
                "direct parent. Proposal v605 reserves METPO:1068200; the ontology "
                "pin and historical child cohorts v558/v604 remain unchanged. "
                "No external equivalence or SSSOM mapping is accepted."
            ),
            "posed_by": "codex", "posed_date": DATE,
        },
        {
            "discussion_id": "cellular-contraction-provenance-and-mechanism",
            "prompt": "Resolve isolate identities and endpoint-specific mechanisms before adding exemplars or causal proteins.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Keep source-named organisms as qualified observations, not "
                "species-wide canonical exemplars. Verify culture provenance and "
                "current taxonomic identity before adding canonical_examples. "
                "Calcium dependence, microtubule breakdown, contractile fibers "
                "and fitted calcium-wave models must not be combined into one "
                "universal mechanism. Protein sequence features alone cannot "
                "establish this phenotype. A protein-resolved graph requires "
                "authority-checked taxon-paired accessions and edge-specific "
                "perturbation evidence. No graph is asserted; mechanisms are "
                "deferred, not claimed absent. Source checks covered identified "
                "metadata fields and selected text/figures, not comprehensive "
                "correction or retraction clearance."
            ),
            "posed_by": "codex", "posed_date": DATE,
        },
    ],
}


def digest(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


def event(record: dict, action: str, changes: str) -> dict:
    return record_curation_event(record, curator="codex", action=action, changes=changes,
                                 llm_assisted=True, timestamp=TIMESTAMP)


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(record, "MINTED_TRAITMECH_ID", (
        "Added a shortening-defined cellular contraction parent with three primary "
        "DOI sources and directly checked 19/15/15-word excerpts. Retained native "
        "VERIFIED, VERIFIED and NOT_IN_ABSTRACT outcomes. Reserved 000729, v605 "
        "and 1068200-1068299 after ignored/hidden known-copy, retained-history and "
        "open/draft PR checks with full proposal-range inspection. Resolved the "
        "body and axopodial parent gaps while keeping assay and mechanism questions "
        "open. No universal molecular mechanism or canonical taxon inferred. "
        "Timestamp records observed allocation and curation acceptance."
    ))
    return record


def build_child(slug: str, original: dict) -> dict:
    record = copy.deepcopy(original)
    identifier, anchor = CHILDREN[slug]
    if not isinstance(record, dict) or record.get("identifier") != identifier:
        raise SystemExit(f"{slug} identity differs from reviewed preimage")
    matches = [d for d in record.get("discussions", []) if d.get("discussion_id") == anchor]
    if len(matches) != 1:
        raise SystemExit(f"{slug} discussion identity differs")
    discussion = matches[0]
    axopodial = slug == "rapid_axopodial_contraction"
    resolution = AXOPODIAL_RESOLUTION if axopodial else RESOLUTION
    changes = AXOPODIAL_CHANGE if axopodial else CHILD_CHANGE
    expected_event = event({}, "REFINE_CELLULAR_CONTRACTION_PARENT", changes)
    # Reconstruct the exact preimage for replay, then compare the whole result.
    replay = record.get("parent_traits") == [IDENTIFIER]
    if replay:
        if (discussion.get("status") != "RESOLVED"
                or discussion.pop("resolved_date", None) != DATE
                or discussion.pop("resolution_note", None) != resolution
                or not record.get("curation_history")
                or record["curation_history"].pop() != expected_event):
            raise SystemExit(f"{slug} replay differs from reviewed result")
        record["parent_traits"] = [PARENT["identifier"]]
        discussion["status"] = "OPEN"
        if axopodial:
            if record["discussions"].pop() != ASSAY_DISCUSSION:
                raise SystemExit("Axopodial assay follow-up changed")
            notes = record["evidence"][0]["notes"]
            if notes.count(NEW_KHAN_URL) != 1:
                raise SystemExit("Qualified Khan source URL changed")
            record["evidence"][0]["notes"] = notes.replace(NEW_KHAN_URL, OLD_KHAN_URL)
    if digest(record) != PREIMAGE_SHA256[slug]:
        raise SystemExit(f"{slug} content differs from reviewed preimage")
    if (record.get("parent_traits") != [PARENT["identifier"]]
            or record.get("mapping_status") != "PROPOSED"
            or discussion.get("kind") != "CURATION_TODO"
            or discussion.get("status") != "OPEN"):
        raise SystemExit(f"{slug} hierarchy or discussion state differs")
    record["parent_traits"] = [IDENTIFIER]
    discussion.update(status="RESOLVED", resolved_date=DATE, resolution_note=resolution)
    if axopodial:
        notes = record["evidence"][0]["notes"]
        if notes.count(OLD_KHAN_URL) != 1 or record["evidence"][0]["reference"] != KHAN:
            raise SystemExit("Historical Khan source context differs")
        record["evidence"][0]["notes"] = notes.replace(OLD_KHAN_URL, NEW_KHAN_URL)
        record["discussions"].append(copy.deepcopy(ASSAY_DISCUSSION))
    event(record, "REFINE_CELLULAR_CONTRACTION_PARENT", changes)
    if replay and record != original:
        raise SystemExit(f"{slug} replay changed content")
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         f"TraitMech:data/traits/physiology/{SLUG}.yaml|{KATOH}", PARENT["identifier"],
         "", "", "metpo_traitmech_2026_10", "",
         "Shortening phenotype; v558/v604 child axioms requested in proposal.md.", IDENTIFIER],
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
