"""Add ixotrophy through the validated, dry-run-first writer."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import tempfile
from pathlib import Path

import yaml

from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
SLUG = "ixotrophy"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v574/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000698"
METPO_ID = "METPO:1065100"
PARENT_ID = "METPO:1000059"
MECHANISM = "DOI:10.1126/science.adp0614"
CAPTURE = "DOI:10.1007/s002489900052"
ADHESION = "DOI:10.1099/mic.0.000158"
TIMESTAMP = "2026-10-11T12:55:05Z"
PARENT = {
    "identifier": PARENT_ID,
    "label": "phenotype",
    "definition": (
        "A quality that differentiates specific instances of a species from other "
        "instances of the same species."
    ),
    "definition_source": "DOI:10.1186/gb-2010-11-1-r2",
    "trait_category": "UPPER",
    "term_kind": "CLASS",
    "mapping_status": "REVIEWED",
    "parent_traits": ["METPO:1000188"],
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "ixotrophy",
    "definition": (
        "A trophic-ecology phenotype in which filamentous bacteria capture "
        "microbial prey on their cell surface and kill the captured cells to "
        "obtain prey-derived nutrients."
    ),
    "definition_source": MECHANISM,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": MECHANISM,
            "snippet": (
                "Single-cell analyses with stable isotope-labeled prey revealed "
                "that prey components are taken up by the attacker."
            ),
            "notes": (
                "Lien et al. 2024, PMID:39418385, scientific Abstract, not the "
                "separate article summary; directly matched source-qualified MED "
                "text. Introduction and contact/capture Results support the "
                "surface-trapping differentia. Nutrient-uptake Results, culture, "
                "killing, imaging and Raman Methods, Discussion and actual Figures "
                "1, 5 and 6 read. Raman labeling supports uptake from killed prey; "
                "Figure 6 is a model, not independent flux data. On solid surfaces, "
                "gliding can establish contact without flagellar trapping; this "
                "record denotes a capability, not a mandatory sequence for every "
                "feeding event. Other figures, supplements and movies not fully "
                "assessed. Author-hosted published full text: "
                "https://stockerlab.ethz.ch/wp-content/uploads/2024/10/183.Lien-et-al_Science_Kang.pdf. "
                "MED linked a commentary and preprint, not a correction/retraction; "
                "publisher status page was inaccessible, so that check remains limited."
            ),
        },
        {
            "reference": CAPTURE,
            "snippet": (
                "can subsist on other microbes and can even catch motile bacteria "
                "by their flagella before killing and digesting them."
            ),
            "notes": (
                "Lewin 1997, PMID:9337418, directly retrieved publisher Abstract. "
                "The subject is Saprospira grandis; supports prey capture, killing "
                "and nutrition, not universal dependence on flagellated prey. "
                "MED metadata matched title and DOI but exposed no abstract; "
                "do not report an abstract-resolver verification for this quote. "
                "Full text, figures and strain provenance were unavailable. "
                "Publisher page and qualified MED metadata showed no linked "
                "correction/retraction at access, not proof none exists. "
                "Source: https://link.springer.com/article/10.1007/s002489900052."
            ),
        },
        {
            "reference": ADHESION,
            "snippet": (
                "The ability of cells to aggregate or adhere is thought to be "
                "a significant initial step in ixotrophy."
            ),
            "notes": (
                "Furusawa et al. 2015, PMID:26306656, scientific Abstract directly "
                "read at the publisher and matched qualified MED metadata. "
                "CCB-QB1 adhesion/capture assays support an initial interaction, "
                "not by themselves nutrient transfer. Calcium and acidic "
                "polysaccharide interpretations are model-specific, not defining "
                "requirements. Full-text delivery failed; Methods, figures and "
                "supplement remain unread. Publisher page and MED record exposed "
                "no linked correction/retraction. Authors and CCB-QB1 material "
                "overlap with 2024, so these are not independent-group replications. "
                "Source: https://doi.org/10.1099/mic.0.000158."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:1313421",
            "taxon_label": "Aureispira sp. CCB-QB1",
            "reference": MECHANISM,
            "note": (
                "Qualified to the ixotrophy-positive WT studied with Vibrio "
                "campbellii, not all culture derivatives or the entire genus. "
                "The primary scientific Abstract at "
                "https://pubmed.ncbi.nlm.nih.gov/25468060/ "
                "(DOI:10.1016/j.margen.2014.10.006) directly identifies CCB-QB1 "
                "as an isolate from the coastal area of Penang, Malaysia; "
                "this is provenance, not another predation experiment. "
                "NCBI identifier/name independently checked on 2026-10-11: "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1313421. "
                "The 2024 IS-inactivated predator derivatives are not the exemplar."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "ixotrophy-boundaries-and-mappings",
            "prompt": "Keep prey capture and nutrition distinct from attachment alone.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use phenotype METPO:1000059 as parent. Predatory bacterium "
                "traitmech:000054 requires bacterial prey, whereas ixotrophy "
                "literature also includes nonbacterial microbial prey. Epibiotic "
                "bacterial predation traitmech:000697 denotes attached external "
                "growth on bacterial prey and is not an exact synonym or proven "
                "broader parent. Heng et al. 2026 (DOI:10.1007/s00248-026-02864-6), "
                "publisher Abstract only, calls ixotrophy epibiotic in a broader "
                "usage; retain that attribution without equating the scopes. "
                "Gliding, aggregation, adhesive surfaces, antagonism and prey "
                "lysis alone do not establish ixotrophy. No universal prey range, "
                "obligate dependence or organism-level disjointness is asserted. "
                "No exact external xrefs or synonyms assigned pending authority "
                "and scope reconciliation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "ixotrophy-mechanism-grounding",
            "prompt": "Ground taxon-specific machinery before adding causal edges.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "The 2024 CCB-QB1 study provides a mechanism lead, but a "
                "protein-resolved graph and protein examples are deferred, not "
                "claimed absent. Verify exact accession identities, taxon pairing "
                "and all relevant figures/supplements before curating those "
                "edges. Do not infer this feeding phenotype from secretion-system "
                "genes, profile matches or an insertion sequence alone, or "
                "generalize the CCB-QB1 machinery to every ixotrophic lineage. "
                "Environmental sequence covariation is not direct field predation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added ixotrophy beneath phenotype with three DOI-backed sources, "
            "short checked snippets and a WT-qualified CCB-QB1 example. "
            "Ignored/hidden main/worktree and pending-PR checks support 000698 "
            "and v574 block 1065100-1065199. Existing records unchanged; "
            "mechanism grounding and exact mappings remain open. Timestamp "
            "records the observed UTC curation decision."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    rows = [
        ["proposed_id", "label", "definition", "definition_source", "parent",
         "synonyms", "xrefs", "subset", "priority", "observations", "traits_addressed"],
        ["ID", "LABEL", "A IAO:0000115", ">A IAO:0000119", "SC %",
         "A oboInOwl:hasExactSynonym SPLIT=|", "A oboInOwl:hasDbXref SPLIT=|",
         "A oboInOwl:inSubset", "", "", ""],
        [METPO_ID, record["label"], record["definition"],
         "|".join([f"TraitMech:data/traits/ecology/{SLUG}.yaml",
                   *(e["reference"] for e in record["evidence"])]),
         PARENT_ID, "", "", "metpo_traitmech_2026_10", "",
         "Surface capture, prey killing and nutritional uptake; not adhesion alone.",
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
    if not isinstance(parent, dict) or any(parent.get(k) != v for k, v in PARENT.items()):
        raise SystemExit("Parent identity or scope differs from reviewed projection")
    record = build_record()
    proposal = proposal_tsv(record)
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
