"""Add bacterial mycophagy through the validated, dry-run-first writer."""

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
SLUG = "bacterial_mycophagy"
TARGET = ROOT / f"data/traits/ecology/{SLUG}.yaml"
PARENT_PATH = ROOT / "data/traits/upper/phenotype.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v572/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000696"
METPO_ID = "METPO:1064900"
PARENT_ID = "METPO:1000059"
DEFINITION = "DOI:10.1111/j.1469-8137.2007.02325.x"
ISOLATES = "DOI:10.1099/ijs.0.02920-0"
MICROCOSMS = "DOI:10.1038/ismej.2008.97"
TIMESTAMP = "2026-10-11T10:20:00Z"
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
    "label": "bacterial mycophagy",
    "definition": (
        "A trophic-ecology phenotype in which a bacterium actively obtains "
        "nutrients from living fungi or oomycetes and uses them for its own growth."
    ),
    "definition_source": DEFINITION,
    "trait_category": "ECOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": [PARENT_ID],
    "evidence": [
        {
            "reference": DEFINITION,
            "snippet": (
                "phenotypic behaviours that make available nutrients from living "
                "fungi and allow the conversion of living fungal biomass into "
                "bacterial biomass."
            ),
            "notes": (
                "Leveau and Preston 2008, PMID:18086226, section I, p. 860 "
                "(author PDF page 2), visually checked contiguous quotation. "
                "Definition authority, not experimental replication. Summary, "
                "section I, strategy overview and selected diagnostic passages "
                "in section III read; remaining review and referenced experiments "
                "not comprehensively assessed. Section I explicitly includes "
                "oomycetes while acknowledging they are not true fungi. Section "
                "III requires growth controls and distinguishes inferred nutrient "
                "acquisition from direct flux measurement. Author full text: "
                "https://leveau.faculty.ucdavis.edu/wp-content/uploads/sites/220/2015/05/Leveau2008.pdf. "
                "DOI AND SRC:MED metadata matched PMID, title and DOI on 2026-10-11."
            ),
        },
        {
            "reference": ISOLATES,
            "snippet": (
                "All Ter isolates proliferated in sand when hyphae of the fungi "
                "C. globosum, F. culmorum or M. hiemalis invaded."
            ),
            "notes": (
                "de Boer et al. 2004, PMID:15143036, Results, p. 860 "
                "(PDF page 4), visually checked quotation. Methods tested all "
                "isolates against intact living hyphae, using plate counts at "
                "three weeks corrected for uninoculated controls. Growth is "
                "indirect nutritional evidence, not isotope-traced transfer. "
                "Heat-fixed-hypha adhesion is a separate observation. Abstract, "
                "Introduction, Methods, relevant Results and taxonomic "
                "descriptions read; pages 4/7 visually inspected; supplement "
                "unread. Author full text: "
                "https://leveau.faculty.ucdavis.edu/wp-content/uploads/sites/220/2015/05/deBoer2004.pdf. "
                "EXT_ID:15143036 AND SRC:MED matched source, ID, title and DOI "
                "on 2026-10-11."
            ),
        },
        {
            "reference": MICROCOSMS,
            "snippet": (
                "The growth of collimonads did not cause a significant reduction "
                "in the Absidia biomass."
            ),
            "notes": (
                "Hoppener-Ogawa et al. 2009, PMID:18923455, scientific Abstract, "
                "directly matched. Abstract, Introduction, Methods, Results, "
                "Discussion, Table 1 and actual Figures 1/2 read; Figure 3 and "
                "supplement unread. Indigenous soil populations and a four-strain "
                "sand mixture grew with invading fungus; this is not individual "
                "strain proof or direct nutrient tracing. Nonsignificant biomass "
                "loss does not establish no fitness cost. Methods samples at "
                "three weeks, whereas Figure 2 caption names two and three; no "
                "time-specific quantitative claim adopted. Overlapping authors "
                "with 2004, not independent-group replication. Author full text: "
                "https://leveau.ucdavis.edu/wp-content/uploads/sites/220/2015/05/HoppenerOgawa2009.pdf. "
                "EXT_ID:18923455 AND SRC:MED matched source, ID, title and DOI "
                "on 2026-10-11."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:158899",
            "taxon_label": "Collimonas fungivorans",
            "reference": ISOLATES,
            "note": (
                "Qualified to natural dune-soil isolate Ter6 (type strain, "
                "NCCB 100033 = LMG 21973), not every species member. Primary "
                "Methods establish provenance and hyphal-growth testing; "
                "species description on p. 863 identifies Ter6. Provenance: "
                "https://doi.org/10.1099/ijs.0.02920-0. NCBI species ID/name "
                "and Ter6 type material independently resolved on 2026-10-11: "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=158899. "
                "Do not assign all 22 Ter isolates to this species from the "
                "2004 circumscription."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "bacterial-mycophagy-scope-and-mappings",
            "prompt": "Resolve exact mappings without conflating trophic endpoints.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Follow Leveau and Preston's active nutritional definition and "
                "explicit oomycete scope, without classifying oomycetes as true "
                "fungi or asserting experimentally demonstrated feeding on every "
                "target group. Merely consuming passive leaks or tissue dead "
                "through unrelated causes is excluded. Fungal inhibition, lysis, "
                "chitinase activity or a sequence annotation alone is insufficient. "
                "Killing and obligate fungal dependence are not required. "
                "Predatory bacterium traitmech:000054 requires bacterial prey; "
                "saprotrophy traitmech:000055 concerns dead material; parasitism "
                "traitmech:000043 requires host harm; phagotrophy traitmech:000628 "
                "requires particle ingestion. None is an established broader "
                "parent here. No organism-level disjointness is asserted. "
                "Unqualified mycophagy, fungivory and mycetophagy also cover "
                "nonbacterial organisms and are not exact synonyms. No exact "
                "xref or synonym assigned pending authority/scope reconciliation."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-11",
        },
        {
            "discussion_id": "bacterial-mycophagy-mechanisms-and-assays",
            "prompt": "Resolve active nutrient acquisition and taxon-specific mechanisms.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Causal graphs and protein examples are deferred, not claimed "
                "absent. Separate fungal damage, nutrient release and bacterial "
                "assimilation; require functional evidence and taxon-paired "
                "accessions before encoding protein mechanisms. CommunityMech "
                "CommunityMech:000364 led to DOI:10.1093/ismejo/wrag201 "
                "(PMID:42523014, PMC13615538). Its Abstract, antagonistic-assay "
                "Methods and mycophagy Results/Discussion passages were read: "
                "CFU after five days with sclerotia is compared with glass "
                "beads. This is a follow-up lead, not counted evidence of "
                "active feeding rather than released-nutrient consumption. "
                "Figures and supplement remain unread; no additional canonical "
                "taxon or independent replication is inferred from the assay name."
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
            "Added bacterial mycophagy beneath phenotype with three DOI-backed "
            "sources, checked short snippets and a Ter6-qualified canonical "
            "example. Ignored-and-hidden main/worktree/open-PR checks support "
            "000696 and v572 block 1064900-1064999. Existing records unchanged. "
            "Mechanisms and mappings remain open. Timestamp records observed "
            "UTC curation decision."
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
         "Active nutritional growth; neither killing nor obligate dependence required.",
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
