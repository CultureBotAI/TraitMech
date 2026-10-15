"""Add an evidence-backed stalk-contraction phenotype and link its existing parent."""

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
TARGET = ROOT / "data/traits/physiology/stalk_contraction.yaml"
PARENT_PATH = ROOT / "data/traits/physiology/cellular_contraction.yaml"
SOURCE_PROPOSAL = ROOT / "proposals/metpo_traitmech_v605/metpo_proposal_classes_robot.tsv"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v606/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000730"
METPO_ID = "METPO:1068300"
PARENT_ID = "traitmech:000729"
PARENT_METPO = "METPO:1068200"
TIMESTAMP = "2026-10-15T03:51:31Z"
PARENT_DIGEST = "5412dbb2115524bfcb952431f57192a3bd57b13681622ffb771928fc10944be0"
SOURCE_SHA256 = "32cd061487da118a9349366f581f4064486dd0dec771027f4a7eb7f7585c4b25"
KAMIGURI = "DOI:10.2142/biophysics.8.1"
RYU = "DOI:10.1016/j.bpj.2012.07.038"
AMOS = "DOI:10.1038/229127a0"
ANCHOR = "cellular-contraction-scope-and-mappings"
OLD_SENTENCE = "stalk contraction remains a possible future child, not a new allocation here."
NEW_SENTENCE = (
    "stalk contraction traitmech:000730 is now a narrower child, defined by active "
    "reduction of stalk end-to-end extension. This does not require shortening "
    "of the stalk contour or make its sheath cytoplasm."
)
PARENT_CHANGE = (
    "Linked the accepted stalk-contraction child traitmech:000730 in place of "
    "the future-lead sentence. Preserved the parent's definition, evidence, "
    "hierarchy and prior history; independent scope and mechanism questions "
    "remain OPEN. No new parent experiment or universal mechanism is asserted."
)
RECORD = {
    "identifier": IDENTIFIER,
    "label": "stalk contraction",
    "definition": (
        "A physiological phenotype in which a microbial cell actively reduces "
        "the end-to-end extension of its stalk."
    ),
    "definition_source": KAMIGURI,
    "trait_category": "PHYSIOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": KAMIGURI,
            "snippet": "The stalk is straight at the initial stage. Then, it bends and coils into a helix near the zooid.",
            "notes": (
                "Kamiguri et al. 2012, PMID:27857602, PMCID:PMC5070450, printed "
                "page 3, Results and Discussion first paragraph, left column. "
                "Direct contiguous PDF match with whitespace-only line-wrap "
                "normalization and actual typeset passage inspected; native "
                "NOT_IN_ABSTRACT retained. Junko Kamiguri is the first author; "
                "the running header says Hashimoto et al. Living source-named "
                "Vorticella sp. from activated sludge attached to glass rods "
                "was stimulated by hitting the dish; eight cells were observed "
                "at 6000 frames/s. Figures 3 and 5 show coiling and decreased "
                "end-to-end extension. The same paragraph says contour length "
                "does not change. All nine main-paper pages were inspected; "
                "raw videos were not reanalyzed. Model fits are not molecular "
                "proof. The primary PDF came from J-STAGE; an acquisition-helper "
                "failure left no original request timestamp or header receipt. "
                "Those missing fields are not reconstructed. Current taxonomic "
                "and culture identities remain unresolved."
            ),
        },
        {
            "reference": RYU,
            "snippet": "The stalk contraction was stalled more as the fluid viscosity and/or flow rate increased.",
            "notes": (
                "Ryu et al. 2012, PMID:23009835, PMCID:PMC3433611, printed "
                "page 862, Figure 2A caption, sentence beginning The stalk "
                "contraction. Direct contiguous PDF match and actual typeset "
                "passage inspected; native NOT_IN_ABSTRACT retained. The primary "
                "PDF was retrieved from the Vanderbilt Lang Lab mirror. "
                "Source-named Vorticella convallaria contracted in microfluidic "
                "channels under varied flow and viscosity. Four to five "
                "contractions per cell per condition are not independent cells. "
                "Figure 3 uses six cells; Figure 4C uses fifteen in a separate "
                "analysis. Isometric force is extrapolated through a hydrodynamic "
                "model, not directly measured zero-shortening force. All eight "
                "main-paper pages and actual Figures 1-5 were inspected; the "
                "supplement was not. Projection and geometry assumptions remain "
                "relevant. Some extracted micrometre symbols appear as mm; no "
                "such numeric extraction is quoted. Culture/taxonomy correspondence "
                "is unresolved. No universal rate, force, calcium threshold, "
                "ATP independence or protein mechanism follows."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "stalk-contraction-scope-and-parent",
            "prompt": "Review the stalk-extension endpoint and its projection-contraction parent.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "The measured endpoint is reduced end-to-end stalk extension, "
                "not necessarily reduced contour length. Coiling is observed, "
                "not a universal geometric requirement. Require active cellular "
                "contraction; static stalk morphology, reduced developmental "
                "growth, passive bending, detachment and isometric force alone "
                "do not establish it. Stalk-induced body displacement is not "
                "cell-body contraction traitmech:000728, and the endpoint differs "
                "from rapid axopodial contraction traitmech:000682. The direct "
                "parent is cell body or cytoplasmic projection contraction "
                "traitmech:000729, by definition-based inference. Amos's "
                "publisher abstract places the spasmoneme within cytoplasm "
                "and a sheath. The stalk is composite; its whole sheath is not "
                "asserted to be cytoplasm. Neither locomotion nor a universal "
                "ATP-driven motor is required by this parent choice. No exact "
                "synonym or organism-level disjointness is asserted."
            ),
            "evidence": [{
                "reference": AMOS,
                "reference_title": "Reversible Mechanochemical Cycle in the Contraction of Vorticella",
                "supports": "NO_EVIDENCE", "evidence_source": "abstract",
                "snippet": "The coiling is produced by the contraction of an intracytoplasmic thread, the spasmoneme, within a cylindrical sheath.",
                "explanation": (
                    "Anatomical background for interpreting the parent, not an "
                    "additional inspected experimental result or counted trait "
                    "support. The curated hierarchy is an inference, not an "
                    "ontology assertion made by this paper."
                ),
                "notes": (
                    "Amos 1971, publisher Abstract second sentence, #Abs1-content. "
                    "Direct issuing-publisher HTML match; DOI/title/author metadata "
                    "checked. Native UNRESOLVED retained, not relabeled VERIFIED "
                    "or unindexed. Full article and historical experiments were "
                    "not inspected. No comprehensive notice clearance is claimed."
                ),
            }],
        },
        {
            "discussion_id": "stalk-contraction-metpo-assessment",
            "prompt": "Review the proposed stalk-contraction class without reviving obsolete morphology.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Pinned and inspected current METPO release/editor/template "
                "owners contain no active exact contraction class in the bounded "
                "assessment. METPO:1000288 obsolete stalk is deprecated, under "
                "ObsoleteClass, with OMO:0001000 as its recorded reason and no "
                "replacement or consider annotation observed. It is a historical "
                "morphology label, not an active exact contraction phenotype; "
                "neither revive it nor put it in xrefs. The reason code alone "
                "does not invalidate the biology. v606 reserves METPO:1068300 "
                "in block 1068300-1068399 and repeats the unchanged v605 parent "
                "declaration METPO:1068200 so the standalone proposal emits the "
                "actual parent hierarchy. Historical v605 and the ontology pin "
                "remain unchanged. No external equivalence or SSSOM mapping "
                "is accepted; upstream adoption and human sign-off remain open."
            ),
        },
        {
            "discussion_id": "stalk-contraction-provenance-and-mechanism",
            "prompt": "Resolve source isolates and endpoint-specific mechanisms before adding taxa or proteins.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "Keep study organism names as qualified observations until "
                "culture provenance and current taxonomic identities are "
                "independently verified. Two distinct experimental papers "
                "support the endpoint; Part II of the Kamiguri study is not "
                "counted as independent replication. Preserve stimulus, load, "
                "viscosity, cell state, geometry, sampling and temporal resolution "
                "when comparing assays. Do not generalize calcium-wave models, "
                "spasmoneme chemistry, force estimates or energy claims to all "
                "microbial stalks. Protein sequence features alone cannot "
                "establish this phenotype. A protein-resolved causal graph "
                "needs authority-checked taxon-paired accessions and "
                "edge-specific experimental support. Mechanism is deferred, "
                "not asserted absent. MED/Crossref notice-field and limited "
                "publisher checks are not comprehensive correction/retraction "
                "clearance; failed retrievals and uninspected supplements remain "
                "explicit source-access limits."
            ),
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
    for discussion in record["discussions"]:
        discussion.update(posed_by="codex", posed_date=TIMESTAMP[:10])
    event(record, "MINTED_TRAITMECH_ID", (
        "Added stalk contraction as active reduction of end-to-end stalk extension "
        "with two primary DOI sources and directly checked 19/14-word excerpts. "
        "Retained native NOT_IN_ABSTRACT outcomes and separate 17-word anatomy "
        "context with native UNRESOLVED. Reserved 000730, v606 and 1068300-1068399 "
        "after ignored/hidden worktree, retained-history, full proposal-range and "
        "open/draft PR checks. Linked the existing parent's future lead without "
        "closing independent questions. No canonical taxon, exact mapping or "
        "universal protein mechanism inferred. Timestamp records observed acceptance."
    ))
    return record


def build_parent(original: dict) -> dict:
    record = copy.deepcopy(original)
    if not isinstance(record, dict) or record.get("identifier") != PARENT_ID:
        raise SystemExit("Parent identity differs")
    matches = [d for d in record.get("discussions", []) if d.get("discussion_id") == ANCHOR]
    if len(matches) != 1:
        raise SystemExit("Parent discussion identity differs")
    discussion = matches[0]
    expected_event = event({}, "LINK_STALK_CONTRACTION_CHILD", PARENT_CHANGE)
    replay = NEW_SENTENCE in discussion.get("rationale", "")
    if replay:
        if (discussion["rationale"].count(NEW_SENTENCE) != 1
                or not record.get("curation_history")
                or record["curation_history"].pop() != expected_event):
            raise SystemExit("Parent successor differs")
        discussion["rationale"] = discussion["rationale"].replace(NEW_SENTENCE, OLD_SENTENCE)
    if (digest(record) != PARENT_DIGEST or record.get("mapping_status") != "PROPOSED"
            or discussion.get("status") != "OPEN"
            or discussion["rationale"].count(OLD_SENTENCE) != 1):
        raise SystemExit("Parent differs from reviewed preimage")
    discussion["rationale"] = discussion["rationale"].replace(OLD_SENTENCE, NEW_SENTENCE)
    event(record, "LINK_STALK_CONTRACTION_CHILD", PARENT_CHANGE)
    if replay and record != original:
        raise SystemExit("Parent replay changed content")
    return record


def proposal_tsv(record: dict, parent: dict) -> str:
    raw = SOURCE_PROPOSAL.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
        raise SystemExit("Historical parent proposal differs")
    rows = list(csv.reader(io.StringIO(raw.decode()), delimiter="\t"))
    parents = [r for r in rows[2:] if r[0] == PARENT_METPO]
    if len(parents) != 1 or any(len(r) != 11 for r in rows):
        raise SystemExit("Historical parent proposal shape differs")
    declaration = parents[0]
    if (declaration[1:3] != [parent["label"], parent["definition"]]
            or declaration[4] != "METPO:1000059" or declaration[-1] != PARENT_ID):
        raise SystemExit("Parent record/proposal scope differs")
    output = rows[:2] + [declaration, [
        METPO_ID, record["label"], record["definition"],
        f"TraitMech:data/traits/physiology/stalk_contraction.yaml|{KAMIGURI}",
        PARENT_METPO, "", "", "metpo_traitmech_2026_10", "",
        "Active end-to-end extension reduction; no universal contour shortening or mechanism.",
        IDENTIFIER,
    ]]
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(output)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    parent = build_parent(yaml.safe_load(PARENT_PATH.read_text()))
    proposal = proposal_tsv(record, parent)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(parent, Path(tmp) / PARENT_PATH.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(parent, PARENT_PATH)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
