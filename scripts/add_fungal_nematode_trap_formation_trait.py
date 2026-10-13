"""Add fungal nematode-trap formation and refine five child parents."""

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
SLUG = "fungal_nematode_trap_formation"
TARGET = ROOT / f"data/traits/morphology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v594/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000718"
METPO_ID = "METPO:1067100"
TIMESTAMP = "2026-10-13T13:31:56Z"
DATE = TIMESTAMP[:10]
JI = "DOI:10.1016/j.isci.2020.101057"
YANG = "DOI:10.1371/journal.ppat.1002179"
CHEN = "DOI:10.1038/s41467-023-43235-w"
SAIKAWA = "DOI:10.1007/s102670200061"
PARENT = {
    "identifier": "METPO:1000059", "label": "phenotype",
    "definition": "A quality that differentiates specific instances of a species from other instances of the same species.",
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER", "term_kind": "CLASS", "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
CHILDREN = {
    "fungal_constricting_ring_formation": ("traitmech:000677", "constricting-ring-scope-and-parent", "METPO:1063000"),
    "fungal_adhesive_net_trap_formation": ("traitmech:000678", "adhesive-net-scope-and-parent", "METPO:1063100"),
    "fungal_adhesive_knob_trap_formation": ("traitmech:000679", "adhesive-knob-scope-and-parent", "METPO:1063200"),
    "fungal_nonconstricting_ring_trap_formation": ("traitmech:000680", "nonconstricting-ring-scope-and-parent", "METPO:1063300"),
    "fungal_adhesive_column_trap_formation": ("traitmech:000681", "adhesive-column-scope-and-parent", "METPO:1063400"),
}
CHILD_PATHS = {slug: ROOT / f"data/traits/morphology/{slug}.yaml" for slug in CHILDREN}
PREIMAGE_SHA256 = {
    "fungal_constricting_ring_formation": "5c46c18654feb75758d0f304eb0f044c1f5306351048842bfbeae28f929e4027",
    "fungal_adhesive_net_trap_formation": "18656607eaf17a69720a7402a1fa2bbb2a8263a6e0f2ac232bfe9aa196b3bf0c",
    "fungal_adhesive_knob_trap_formation": "b04157ba210248aaf4e3108af5d3d420a748eb2186f0d4a2d0567acf71a9fab3",
    "fungal_nonconstricting_ring_trap_formation": "c764ba1a37c1200c4befda6b77e6058748ce93cf27b9708cc54b90b267ef8ae1",
    "fungal_adhesive_column_trap_formation": "c2083ff1516ac266ee614e9b27f12405f99441555543e4409eb1cc94864c791b",
}
COLUMN = "fungal_adhesive_column_trap_formation"
COLUMN_GAP = {
    "discussion_id": "adhesive-column-cell-count-scope",
    "prompt": "Reconcile serial-cell column scope with the supplement's broader cell-count description.",
    "kind": "CURATION_TODO", "status": "OPEN",
    "rationale": (
        "The current definition retains serially arranged cells, supported by Ji's "
        "Introduction. The newly inspected 2020 Transparent Methods, Fungal strains, "
        "PDF page 12, describes columns containing one or more cells. Preserve this "
        "source-level difference pending review of single-cell columns versus knobs; "
        "do not silently broaden the child or make cell number the sole discriminator. "
        "Both usages fit fungal nematode-trap formation, so this question does not "
        "reopen the resolved parent gap. The supplement names YMF1.00569 from Deqin "
        "soil, not the 2016 paper's YMF1.01472. That provenance does not establish "
        "identity between the strains or a canonical example. The earlier evidence "
        "notes record limited supplement access at initial curation; this follow-up "
        "adds the inspected page without claiming a complete supplement audit."
    ),
    "evidence": [{"reference": JI, "evidence_source": "full_text",
                  "notes": "Transparent Methods, Fungal strains, PDF page 12; text and rendered page inspected at https://ars.els-cdn.com/content/image/1-s2.0-S258900422030242X-mmc1.pdf. Source-scope assessment, not an additional experiment."}],
    "posed_by": "codex", "posed_date": DATE,
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "fungal nematode-trap formation",
    "definition": "A morphological phenotype in which a fungus differentiates hyphae into specialized nematode-capturing structures.",
    "definition_source": JI,
    "trait_category": "MORPHOLOGY", "term_kind": "CLASS", "mapping_status": "PROPOSED",
    "parent_traits": [PARENT["identifier"]],
    "evidence": [
        {"reference": JI,
         "snippet": "Nematode-trapping fungi (NTF) can switch to pathogens by producing various trapping devices to capture nematodes.",
         "notes": (
             "Ji et al. 2020, scientific Summary; PMID:32339992. Direct primary XML "
             "at https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7186526/fullTextXML "
             "and actual Figure 1 inspected. Introduction and Results group constricting "
             "rings, adhesive networks, columns and knobs as four representative devices, "
             "not an exhaustive taxonomy. Selected Transparent Methods and actual PDF "
             "pages 8, 11, 12, 15 and 16 were inspected; not every supplement figure or "
             "dataset. The main Introduction describes serial column cells while PDF "
             "12 allows one or more; that narrower child-scope question remains open. "
             "Adhesion-gene expansion and expression correlations do not establish "
             "a universal molecular mechanism or sequence-only phenotype prediction. "
             "Native abstract verifier: VERIFIED."
         )},
        {"reference": YANG,
         "snippet": "A. oligospora forms adhesive networks to capture nematodes",
         "notes": (
             "Yang et al. 2011, Author Summary, not the scientific abstract; "
             "PMID:21909256. Direct primary XML at "
             "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3164635/fullTextXML "
             "and actual Figure 1 inspected. Panel I shows interconnected loops; "
             "the caption distinguishes formation, attraction, adhesion, capture, "
             "penetration and digestion. These are separate endpoints, not automatic "
             "consequences of an observed shape. This parent curation did not renew "
             "the full Methods/supplement audit retained by the net child. The old "
             "teleomorph wording is not imported as a current taxonomic equivalence. "
             "Shares authors with Ji 2020, not independent-laboratory replication. "
             "Native verifier: NOT_IN_ABSTRACT; the Author Summary span matches directly."
         )},
        {"reference": CHEN,
         "snippet": "CRs differentiate from hyphae and develop two basal stalk cells (S1 and S2) and three distal ring cells (R1, R2, and R3)",
         "notes": (
             "Chen et al. 2023, Results, Morphogenesis and development of CR; "
             "PMID:37968349. CR means constricting ring. Primary XML at "
             "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10651832/fullTextXML, "
             "relevant formation/inflation Methods and actual Figure 1 inspected. "
             "Strain 29 (CGMCC3.20198) forms morphologically complete rings before "
             "inflation competence; panels l/m contrast immature-ring escape with "
             "mature-ring capture. Water-agar induction with C. elegans, horse-serum "
             "formation and hot-water inflation are distinct assays, not universal "
             "requirements. Later protein-mechanism figures and supplements were "
             "not fully audited; the incomplete supplementary ZIP is not evidence. "
             "No universal SNARE dependency or natural-strain exemplar is inferred. "
             "Native verifier: NOT_IN_ABSTRACT; the Results span matches directly."
         )},
        {"reference": SAIKAWA,
         "snippet": "A nonconstricting ring (arrow) is capturing a nematode (asterisk).",
         "notes": (
             "Saikawa and Takahashi 2002, Figure 8 caption, page 418. All three "
             "pages and actual Figures 1-20 inspected at "
             "https://www.jstage.jst.go.jp/article/mycosci/43/5/43_MYC43417/_pdf. "
             "Figures 8-14 and 15-20 document nonconstricting rings in source-named "
             "Dactylella leptospora and Dactylaria candida; Figures 1-7 show the "
             "constricting comparator. Curved hyphal branches form the traps. "
             "The observations support inclusion of nonconstricting rings, not "
             "universal stalk lengths, culture conditions or adhesion proteins. "
             "Adhesive ultrastructure is attributed to earlier work, not newly "
             "imaged here. DOI/title reconciled against Crossref. Native verifier: "
             "UNRESOLVED with no result for that exact DOI query; the caption "
             "matches directly. This does not assert that the paper is unindexed everywhere."
         )},
    ],
    "discussions": [
        {"discussion_id": "fungal-nematode-trap-scope-and-hierarchy",
         "prompt": "Refine morphological boundaries without equating formation with feeding.",
         "kind": "CURATION_TODO", "status": "OPEN",
         "rationale": (
             "Phenotype METPO:1000059 is broader. Existing trap-formation traits "
             "000677-000681 entail this parent; their five parent gaps are resolved "
             "by definition-based inference, not new child experiments. The five "
             "types do not exhaust the class or partition organism-level possession. "
             "Morphologically complete immature traps are included; formation does "
             "not guarantee immediate capture, killing, penetration, digestion or "
             "assimilation. Generic hyphal growth, fusion, individual-cell ring "
             "shape, prey attraction, fungal taxonomy and nematicidal activity "
             "without trap differentiation are insufficient. Mycelial growth "
             "traitmech:000074 is explicitly bacterial; hyphal anastomosis "
             "traitmech:000605 denotes fusion. Neither is an exact parent. "
             "Nutritional nematophagy is not an exact synonym. The column child's "
             "serial-cell versus single-cell terminology remains separately open; "
             "no organism-level disjointness is asserted. Pinned/current METPO "
             "lexical hits 0000261, 000262 and 1000125 are deprecated fungal-spore "
             "concepts, not trap counterparts; no replacement/consider annotations "
             "were observed. Their OMO:0001000 reasons do not invalidate biology "
             "or license identifier reuse. No exact synonyms or xrefs are asserted."
         ), "posed_by": "codex", "posed_date": DATE},
        {"discussion_id": "fungal-nematode-trap-mechanism-and-source-limits",
         "prompt": "Resolve trap-specific mechanisms and provenance without universalizing correlations.",
         "kind": "KNOWLEDGE_GAP", "status": "OPEN",
         "rationale": (
             "Genomic homology, gene-family expansion and expression changes do "
             "not validate sequence-only phenotype predictions. Formation, "
             "adhesion, ring inflation and subsequent infection require separate "
             "functional evidence. No common protein inventory, inducer or "
             "mechanism is inferred across traps; protein examples and causal "
             "graphs remain unset. Existing narrow children retain their qualified "
             "canonical examples; none is duplicated onto the parent. Ji's ring "
             "isolate is described first as derived from a teleomorph and later "
             "as soil-derived, and Results/caption adhesive-layer measurements "
             "differ. Do not silently reconcile them. Its column strain is not "
             "the 2016 child's strain. Notice checks were bounded: Cell and "
             "Crossmark access failed, while PubMed, Crossref and three publisher "
             "records were inspected. Yang's linked CommentIn is commentary, "
             "not a correction designation or independent experiment. Source "
             "hashes, exact query outcomes and inspection limits are in the sidecar."
         ), "posed_by": "codex", "posed_date": DATE},
    ],
}


def digest(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=True).encode()).hexdigest()


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(record, curator="codex", action=action, changes=changes,
                         llm_assisted=True, timestamp=TIMESTAMP)


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(record, "MINTED_TRAITMECH_ID", (
        "Added fungal nematode-trap formation with four DOI-backed contiguous "
        "excerpts and bounded source/phenotype scope. Reserved 000718, v594 and "
        "1067100-1067199 after ignored/hidden, retained-history and pending-head "
        "checks. Refined five child parents, preserving their definitions and "
        "evidence and recording the unresolved column cell-count usage. No "
        "sequence-derived mechanism or universal capture guarantee asserted. "
        "Timestamp is observed post-audit acceptance, not estimated writing time."
    ))
    return record


def resolution(slug: str) -> str:
    return (
        f"Added fungal nematode-trap formation {IDENTIFIER} as the direct broader "
        "phenotype. The existing child definition entails specialized hyphal "
        "trap differentiation. This resolves only the parent gap; the historical "
        "scope contrasts, unasserted mappings, examples and separate mechanism "
        "questions remain applicable. Formation does not guarantee immediate "
        "capture. The column cell-count question is separately OPEN. Preserve "
        f"the historical phenotype axiom and add {CHILDREN[slug][2]} SubClassOf "
        f"{METPO_ID} on upstream adoption."
    )


def child_event(slug: str) -> dict:
    record = {}
    event(record, "REFINE_FUNGAL_TRAP_PARENT", (
        f"Refined {CHILDREN[slug][0]} below fungal nematode-trap formation "
        f"{IDENTIFIER} and resolved its temporary parent discussion by "
        "definition-based inference. Preserved child identity, definition, "
        "evidence, examples, mechanism gaps and earlier history."
        + (" Added a separate source-backed cell-count scope question after "
           "inspecting the 2020 supplement; no identity broadening." if slug == COLUMN else "")
    ))
    return record["curation_history"][0]


def build_child(slug: str, original: dict) -> dict:
    record = copy.deepcopy(original)
    matches = [d for d in record.get("discussions", [])
               if d.get("discussion_id") == CHILDREN[slug][1]]
    if len(matches) != 1:
        raise SystemExit(f"{slug}: parent discussion differs")
    discussion = matches[0]
    replay = record.get("parent_traits") == [IDENTIFIER]
    expected = child_event(slug)
    if replay:
        if (discussion.get("status") != "RESOLVED"
                or discussion.get("resolved_date") != DATE
                or discussion.get("resolution_note") != resolution(slug)
                or not record.get("curation_history")
                or record["curation_history"][-1] != expected):
            raise SystemExit(f"{slug}: replay differs")
        record["parent_traits"] = [PARENT["identifier"]]
        discussion["status"] = "OPEN"
        del discussion["resolved_date"], discussion["resolution_note"]
        record["curation_history"].pop()
        if slug == COLUMN:
            if record["discussions"][-1] != COLUMN_GAP:
                raise SystemExit(f"{slug}: column discussion replay differs")
            record["discussions"].pop()
    if digest(record) != PREIMAGE_SHA256[slug]:
        raise SystemExit(f"{slug}: reviewed preimage differs")
    if replay:
        return copy.deepcopy(original)
    record["parent_traits"] = [IDENTIFIER]
    discussion.update(status="RESOLVED", resolved_date=DATE, resolution_note=resolution(slug))
    if slug == COLUMN:
        record["discussions"].append(copy.deepcopy(COLUMN_GAP))
    record.setdefault("curation_history", []).append(expected)
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/morphology/{SLUG}.yaml", JI, YANG, CHEN, SAIKAWA]),
         PARENT["identifier"], "", "", "metpo_traitmech_2026_10", "",
         "Morphological differentiation, not guaranteed capture; five child refinements requested in proposal.md.",
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
