"""Add automixis and resolve three tightly coupled reproductive-parent gaps."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import tempfile
from pathlib import Path

import yaml

import add_autogamy_trait as template_writer
import add_paedogamy_trait as paedogamy_writer
import qualify_autogamy_nuclear_origin as autogamy_writer
import qualify_cytogamy_scope as cytogamy_writer
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TRAITS = ROOT / "data/traits/physiology"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v501/metpo_proposal_classes_robot.tsv"
IDENTIFIER = "traitmech:000625"
METPO_ID = "METPO:1057800"
MOGIE = "DOI:10.1111/j.1095-8312.1986.tb01761.x"
YEAST = "DOI:10.1186/s13059-021-02521-w"
TIMESTAMP = "2026-10-05T18:20:28Z"
SUPPLEMENT_URL = (
    "https://media.springernature.com/original/springer-static/esm/art%3A"
    "10.1186%2Fs13059-021-02521-w/MediaObjects/13059_2021_2521_MOESM1_ESM.pdf"
)
CHILD_IDS = {
    "autogamy": "METPO:1057500",
    "cytogamy": "METPO:1057600",
    "paedogamy": "METPO:1057700",
}
RECORD = {
    "identifier": IDENTIFIER,
    "label": "automixis",
    "definition": (
        "A reproductive phenotype in which the reduction of reproductive nuclear "
        "ploidy is prevented or compensated and progeny derive their reproductive "
        "nuclei solely from products of one meiotically dividing cell or their descendants."
    ),
    "definition_source": MOGIE,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": MOGIE,
            "snippet": (
                "Automixis describes several reproductive processes whereby a new "
                "individual derives from a product or products of a single meiotically dividing cell."
            ),
            "notes": (
                "Mogie (1986), scientific abstract directly read on Wiley. "
                "Terminology authority, not a new microbial experiment. Its scope "
                "includes fusion and non-fusion routes, restitutional meiosis and "
                "endomitosis before or after reductional meiosis. The ploidy clause "
                "distinguishes ordinary reduced meiotic progeny; reproductive "
                "nuclei excludes a universal somatic-ploidy requirement. Do not "
                "classify every route as sexual. The abstract contrasts "
                "botanical/mycological autogamous selfing involving different "
                "meioses, not our operational same-cell autogamy. Full text and "
                "actual figures remain unread."
            ),
        },
        {
            "reference": YEAST,
            "snippet": (
                "Mating of gametes from the same meiotic event represents a "
                "particular type of inbreeding referred to as intratetrad mating or automixis"
            ),
            "notes": (
                "Papaioannou et al. (2021), PMID:34732243, PMC8567612, "
                "Background clause checked in publisher HTML and Europe PMC "
                "full-text XML. Scientific abstract, Results, Discussion and "
                "main Methods read; actual Figure 1 and all Table S1 pages "
                "visually inspected. Figure 1C depicts the automictic life "
                "cycle with NBRC 1722 and its diploid progenitor NBRC 1721. "
                "It is not a measured automixis rate. This fusion-based usage "
                "is narrower than Mogie's scope. Recombination experiments "
                "do not establish universal homozygosity or zero recombination. "
                "Other figures and detailed supplementary methods remain unread."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:36035",
        "taxon_label": "Saccharomycodes ludwigii",
        "reference": YEAST,
        "note": (
            "Qualified NBRC 1721 strain-family example in Figure 1C; not a "
            "strain-specific automixis-frequency measurement. Table S1 p.1 "
            "and p.3 footnote 2 identify NBRC 1721 as a wild diploid isolate "
            "from grape must, Japan, 1964. NBRC 1722 is a single-spore "
            "descendant, not that wild parent or an engineered deletion strain. "
            f"Provenance: {SUPPLEMENT_URL}. NCBI taxonomy EFetch on 2026-10-05 "
            "confirmed the species name at "
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=36035; "
            "no genome accession is authenticated."
        ),
    }],
    "discussions": [
        {
            "discussion_id": "automixis-scope-and-hierarchy",
            "prompt": "Preserve source-specific meanings of self-fertilization terms.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Mogie's broad reproductive class is not exclusively nuclear "
                "fusion or exclusively sexual reproduction. The operational "
                "autogamy traitmech:000622, cytogamy traitmech:000623 and "
                "paedogamy traitmech:000624 fit as narrower same-cell-origin "
                "routes; postmeiotic mitosis is allowed. Kaczmarska et al. "
                "DOI:10.1080/0269249X.2013.791344 section 5.2 directly names "
                "autogamy and paedogamy as automixis in diatoms. This does not "
                "make all botanical autogamy equivalent. Cytogamy's existing "
                "1979 evidence supports same-parent meiotic origin despite "
                "cell pairing; cytoplasmic exchange is not nuclear outcrossing. "
                "Same-clone mating after different meioses is insufficient. "
                "Fungal homothallism, heterothallism and intratetrad mating are "
                "not exact synonyms of this broad class. External equivalences "
                "and narrower non-fusion microbial exemplars remain unresolved."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "automixis-mechanism-and-coverage",
            "prompt": "Resolve route-specific mechanisms without universal genetic claims.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "A reproductive phenotype, not a literal mating locus or "
                "sequence feature. No single protein pathway is established "
                "for all fusion and non-fusion routes, so no causal graph or "
                "protein accessions are asserted. Do not infer universal "
                "homozygosity, central fusion, absence of outcrossing, or "
                "disjoint taxa from event-level distinctions. Retain actual "
                "snippet-resolver outcomes separately from direct source checks."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
    ],
}


def preimages() -> dict[str, dict]:
    return {
        "autogamy": autogamy_writer.build_record(),
        "cytogamy": cytogamy_writer.build_record(),
        "paedogamy": paedogamy_writer.build_record(),
    }


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added automixis with two DOI-backed snippets and a qualified "
            "natural yeast strain-family example. Ignored-and-hidden novelty "
            "and allocation searches found no exact record or collision. "
            "Reserved METPO:1057800 in v501; broadened beyond fusion-only "
            "terminology and deferred universal molecular mechanisms."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_child(slug: str, before: dict) -> dict:
    if before != preimages()[slug]:
        raise SystemExit(f"{slug} differs from reviewed preimage")
    record = copy.deepcopy(before)
    record["parent_traits"] = [IDENTIFIER]
    old = (
        "Use phenotype METPO:1000059 pending a suitable reproductive-phenotype parent."
        if slug == "paedogamy" else
        "Use phenotype METPO:1000059 pending a narrower reproductive-phenotype parent; "
        "PHYSIOLOGY is a filesystem category."
    )
    scope = record["discussions"][0]
    if scope["status"] != "OPEN" or scope["rationale"].count(old) != 1:
        raise SystemExit(f"Unexpected {slug} parent-gap discussion")
    scope["rationale"] = scope["rationale"].replace(old, (
        "The parent gap is resolved by automixis traitmech:000625, whose "
        "single-meiotic-cell nuclear origin includes this operational scope. "
        "The broader terminology and mapping questions keep this discussion OPEN."
    ))
    if slug == "autogamy":
        scope["rationale"] = scope["rationale"].replace(
            "Verify external equivalences and broader automixis terminology before adding synonyms or mappings.",
            "Verify external equivalences and source-specific synonym scope before adding mappings.",
        )
    record_curation_event(
        record, curator="codex", action="RESOLVED_PARENT_GAP",
        changes=(
            "Reparented below automixis traitmech:000625 and documented the "
            "resolved parent gap while retaining other open terminology and "
            "mapping questions. Preserved definition, evidence, examples and "
            "prior history. v501 carries the existing proposed METPO ID with "
            "this hierarchy; earlier standalone templates remain historical."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(records: dict[str, dict]) -> str:
    rows = list(csv.reader(io.StringIO(template_writer.proposal_tsv(records["automixis"])), delimiter="\t"))[:2]
    for slug, record in records.items():
        row = list(csv.reader(io.StringIO(template_writer.proposal_tsv(record)), delimiter="\t"))[2]
        row[0] = METPO_ID if slug == "automixis" else CHILD_IDS[slug]
        row[3] = "|".join([f"TraitMech:data/traits/physiology/{slug}.yaml"]
                          + [e["reference"] for e in record["evidence"]])
        row[4] = "METPO:1000059" if slug == "automixis" else METPO_ID
        row[5] = "pedogamy" if slug == "paedogamy" else ""
        row[9] = "Broad automixis; fusion and non-fusion routes." if slug == "automixis" else "Existing ID; v501 supersedes standalone parent assertion."
        row[10] = record["identifier"]
        rows.append(row)
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    before = preimages()
    records = {"automixis": build_record()}
    records.update({slug: build_child(slug, record) for slug, record in before.items()})
    for slug, record in records.items():
        path = TRAITS / f"{slug}.yaml"
        if slug in before and not path.exists():
            raise SystemExit(f"Missing reviewed preimage: {path}")
        allowed = (record, before[slug]) if slug in before else (record,)
        if path.exists() and yaml.safe_load(path.read_text()) not in allowed:
            raise SystemExit(f"Existing record differs from reviewed preimage or result: {path}")
    proposal = proposal_tsv(records)
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        for slug, record in records.items():
            write_validated_trait(record, Path(tmp) / f"{slug}.yaml")
    if args.apply:
        for slug, record in records.items():
            write_validated_trait(record, TRAITS / f"{slug}.yaml")
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
