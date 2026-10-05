"""Add paedogamy and clarify the coupled autogamy boundary (#1719)."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

import add_autogamy_trait as autogamy_writer
import add_cytogamy_trait as cytogamy_writer
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/paedogamy.yaml"
NEIGHBOR = ROOT / "data/traits/physiology/autogamy.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v500/metpo_proposal_classes_robot.tsv"
NEIGHBOR_PROPOSAL = ROOT / "proposals/metpo_traitmech_v498/metpo_proposal_classes_robot.tsv"
NEIGHBOR_SHA = "7bbbedabda93dcd4da5f8e9dc8d2153d2b87853e66f543f75904e1c14f3445fe"
NEIGHBOR_PROPOSAL_SHA = "f1092aebbdae08ddd75f716a81aef850f4c90ce7102cd3ed39f4646e4ba2859d"
IDENTIFIER = "traitmech:000624"
TERMINOLOGY = "DOI:10.1080/0269249X.2013.791344"
BAGMET = "DOI:10.3390/d14121133"
POULICKOVA = "DOI:10.1007/s12223-008-0018-x"
TIMESTAMP = "2026-10-05T17:13:00Z"
TERMINOLOGY_URL = (
    "https://www.researchgate.net/publication/259079699_Proposals_for_a_"
    "terminology_for_diatom_sexual_reproduction_auxospores_and_resting_stages"
)
SUPPLEMENT_URL = (
    "https://mdpi-res.com/d_attachment/diversity/diversity-14-01133/"
    "article_deploy/diversity-14-01133-s001.zip"
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "paedogamy",
    "definition": (
        "A sexual-reproduction phenotype in which two gametes produced by "
        "division within a single gametangium fuse with each other."
    ),
    "definition_source": TERMINOLOGY,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "synonyms": [{
        "synonym_text": "pedogamy", "synonym_type": "EXACT_SYNONYM", "source": BAGMET,
    }],
    "evidence": [
        {
            "reference": TERMINOLOGY,
            "snippet": "fusion of two gametes within a single gametangium",
            "notes": (
                "Kaczmarska et al. (2013), p.271, section 5.2.1, contiguous "
                "definition phrase in the directly read author-posted full text "
                f"at {TERMINOLOGY_URL}. Cytokinesis distinguishes gametes from "
                "the undivided-cell nuclear fusion of section 5.2.2. Section "
                "5.2 treats both as automixis, not equivalent names. This is "
                "terminology synthesis, not independent experimental replication "
                "of its cited Neidium study. Actual diagrams were not visually "
                "inspected. Do not make meiosis-I cytokinesis or immediate "
                "gametic-nuclear fusion universal requirements."
            ),
        },
        {
            "reference": BAGMET,
            "snippet": (
                "Afterwards, the protoplasts (gametes) fused to form a zygote (auxospore)"
            ),
            "notes": (
                "Bagmet et al. (2022), Results 3.3, p.9, clause before the "
                "Figure 3J,K citation, checked in publisher XML and typeset PDF. "
                "Abstract, Methods 2.1-2.5, Results 3.3, Discussion 4.1 and "
                "Table S1 were read; actual Figure 3 and pp.8-9 were inspected. "
                "Four clones were active: VCA-7, VCA-48, VCA-49 and VCA-51; "
                "VCA-50 and VCA-52 showed no mating. The authors call this "
                "pedogamy. Preserve their apparently-qualified interpretation "
                "of earlier Figure 3G,H; do not infer tracked nuclear fusion "
                "from chloroplast images. Seasonal observations and unsuccessful "
                "salt stimulation are study-specific. Plastid rbcL comparisons "
                "do not establish absence of genomic recombination."
            ),
        },
        {
            "reference": POULICKOVA,
            "snippet": "The gametic nuclei fused after auxospore expansion had begun.",
            "notes": (
                "Poulickova (2008), PMID:18500631, scientific abstract directly "
                "retrieved from Europe PMC and PubMed. Unpaired Neidium cf. "
                "ampliatum cells differentiated into gametangia and underwent "
                "pedogamy. The quoted timing cautions against conflating gamete "
                "fusion with immediate nuclear fusion. Full text, actual figures "
                "and strain provenance remain unread. Preserve cf.; no exact "
                "species mapping or canonical Neidium example is asserted."
            ),
        },
    ],
    "canonical_examples": [{
        "taxon_id": "NCBITaxon:1302829",
        "taxon_label": "Nitzschia acidoclinata",
        "reference": BAGMET,
        "note": (
            "Qualified VCA-7 example, one of the four sexually active clones in "
            "Results 3.3, not every tested clone. Table S1 traces VCA-7 to wet "
            "ground in Gonduras Cave, Krasnoyarsk Territory, collected 2011-02-19; "
            "Methods 2.1 describes single-cell isolation and subsequent culture. "
            f"Provenance table directly inspected in {SUPPLEMENT_URL}. NCBI "
            "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1302829 "
            "and taxonomy EFetch checked on 2026-10-05 resolve this species "
            "name; this does not authenticate a genome or current culture accession."
        ),
    }],
    "discussions": [
        {
            "discussion_id": "paedogamy-scope-and-hierarchy",
            "prompt": "Separate gamete-cell fusion from autogamy and broader selfing.",
            "kind": "CURATION_TODO", "status": "OPEN",
            "rationale": (
                "Use the single-gametangium gamete-fusion sense established in "
                "the cited diatom literature. Autogamy traitmech:000622 denotes "
                "gametic-nuclear fusion in an unpaired undivided cell, without "
                "fusion of separate gametes; cytogamy traitmech:000623 concerns "
                "paired cells without nuclear exchange. Automixis is broader "
                "in Kaczmarska et al. section 5.2 and is not an exact synonym. "
                "Bagmet et al. calls automixis homothallic, whereas our existing "
                "homothallism traitmech:000609 is fungal-scoped; this usage "
                "does not make that record a parent. Use phenotype METPO:1000059 "
                "pending a suitable reproductive-phenotype parent. Do not "
                "infer species-level disjointness or universal homozygosity, "
                "recombination rate, seasonal trigger or inability to outcross. "
                "Broader non-diatom usage and external equivalences need primary "
                "source review before expanding this operational scope."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "paedogamy-mechanism-and-coverage",
            "prompt": "Resolve nuclear cytology and molecular mechanisms beyond morphology.",
            "kind": "KNOWLEDGE_GAP", "status": "OPEN",
            "rationale": (
                "This is a reproductive phenotype, not a literal locus or a "
                "plastid-marker sequence feature. The directly inspected "
                "microscopy supports a gamete-fusion interpretation but does "
                "not identify a protein-resolved causal pathway. No causal "
                "graph or accession-level protein claim is inferred from "
                "chloroplast shape, sequence similarity or terminology. "
                "Full Neidium methods and provenance, and stronger nuclear "
                "observations in the Nitzschia system, remain coverage gaps. "
                "Retain actual snippet-resolver outcomes separately from "
                "direct PDF, XML and abstract checks."
            ),
            "posed_by": "codex", "posed_date": "2026-10-05",
        },
    ],
}


def neighbor_preimage() -> dict:
    return cytogamy_writer.build_neighbor(autogamy_writer.build_record())


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added paedogamy with three DOI-backed snippets, a pedogamy spelling "
            "synonym and qualified natural VCA-7 example. Ignored-and-hidden "
            "novelty/allocation searches found no exact record or collision. "
            "Reserved METPO:1057700 in v500. Distinguished gamete fusion from "
            "autogamy and broader automixis; deferred molecular graphs and mappings."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def build_neighbor(before: dict) -> dict:
    if before != neighbor_preimage():
        raise SystemExit("Neighbor differs from reviewed preimage")
    record = copy.deepcopy(before)
    record["definition"] = (
        "A sexual-reproduction phenotype in which two meiotically derived "
        "gametic nuclei fuse within one unpaired, undivided cell, without "
        "fusion of separate gametes."
    )
    record["evidence"].append({
        "reference": TERMINOLOGY,
        "snippet": (
            "Autogamy is a fusion of two gametic (haploid) nuclei within an undivided cell"
        ),
        "notes": (
            "Kaczmarska et al. (2013), p.271, section 5.2.2, opening clause "
            f"directly read in the author-posted full text at {TERMINOLOGY_URL}. "
            "Sections 5.2.1-5.2.2 distinguish separate gamete fusion from "
            "undivided-cell nuclear fusion. This resolves the prior unread "
            "terminology lead; it is synthesis, not new ciliate replication. "
            "The following diatom-specific meiotic timing is not imposed on "
            "the ciliate definition, which allows postmeiotic mitosis as in "
            "Nobili and Luporini pp.35-37. Actual 2013 diagrams were not inspected."
        ),
    })
    record["discussions"][0]["rationale"] += (
        " Paedogamy traitmech:000624 instead involves separate gametes formed "
        "within one gametangium. The clarified definition excludes their "
        "fusion, without forbidding later cell division or postmeiotic nuclear "
        "mitosis. These are event-level distinctions, not disjoint species."
    )
    record["discussions"][1]["rationale"] = (
        "This is an organismal reproductive phenotype, not the literal mt "
        "marker locus or a heat-shock expression signature. Nuclear-selection "
        "inference, nutritional commitment and survival associations do not "
        "supply a universal protein-resolved mechanism. No causal graph "
        "bypasses missing accession-level and perturbation evidence. Keep "
        "macronuclear-fragmentation scoring separate from directly observed "
        "fusion. The earlier metadata-only lead DOI:10.1080/0269249X.2013.791344 "
        "is now resolved by direct reading of sections 5.2.1-5.2.2: paedogamy "
        "traitmech:000624 is distinct and automixis broader. Molecular "
        "mechanisms, wider taxon coverage and external equivalences remain "
        "open; the terminology source alone does not establish them. Preserve "
        "actual abstract-resolver verdicts separately from direct full-text checks."
    )
    record_curation_event(
        record, curator="codex", action="QUALIFIED_TRAIT_SCOPE",
        changes=(
            "Addressed #1719: made the undivided-cell/no-separate-gamete-fusion "
            "boundary explicit, added directly read 2013 terminology evidence "
            "and linked paedogamy traitmech:000624. Resolved the unread-source "
            "lead while retaining other open gaps. Preserved ciliate evidence, "
            "canonical example, parent and compatibility with postmeiotic mitosis."
        ),
        llm_assisted=True, timestamp=TIMESTAMP,
    )
    return record


def proposal_tsv(record: dict) -> str:
    rows = list(csv.reader(io.StringIO(autogamy_writer.proposal_tsv(record)), delimiter="\t"))
    rows[2][0] = "METPO:1057700"
    rows[2][3] = "|".join(["TraitMech:data/traits/physiology/paedogamy.yaml"]
                          + [e["reference"] for e in record["evidence"]])
    rows[2][5] = "pedogamy"
    rows[2][9] = "Fusion of separate gametes from one gametangium; not undivided-cell autogamy."
    rows[2][10] = IDENTIFIER
    stream = io.StringIO(newline="")
    csv.writer(stream, delimiter="\t", lineterminator="\n").writerows(rows)
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record = build_record()
    neighbor = build_neighbor(neighbor_preimage())
    proposal = proposal_tsv(record)
    neighbor_proposal = autogamy_writer.proposal_tsv(neighbor)
    for path, expected, digest in [
        (NEIGHBOR, neighbor, NEIGHBOR_SHA),
        (NEIGHBOR_PROPOSAL, neighbor_proposal, NEIGHBOR_PROPOSAL_SHA),
    ]:
        if not path.exists():
            raise SystemExit(f"Missing reviewed preimage: {path}")
        content = yaml.safe_load(path.read_text()) if path.suffix == ".yaml" else path.read_text()
        if content != expected and hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise SystemExit(f"Existing neighbor differs from reviewed preimage or result: {path}")
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from reviewed result")
    if PROPOSAL.exists() and PROPOSAL.read_text() != proposal:
        raise SystemExit("Existing proposal differs from reviewed result")
    with tempfile.TemporaryDirectory() as tmp:
        write_validated_trait(record, Path(tmp) / TARGET.name)
        write_validated_trait(neighbor, Path(tmp) / NEIGHBOR.name)
    if args.apply:
        write_validated_trait(record, TARGET)
        write_validated_trait(neighbor, NEIGHBOR)
        PROPOSAL.parent.mkdir(parents=True, exist_ok=True)
        PROPOSAL.write_text(proposal)
        NEIGHBOR_PROPOSAL.write_text(neighbor_proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
