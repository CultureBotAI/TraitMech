"""Add cytogamy and distinguish its paired-cell scope from autogamy."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import tempfile
from pathlib import Path

import yaml

import add_autogamy_trait as neighbor_writer
from traitmech.curate.curation_event import record_curation_event
from traitmech.validation.write_validated import write_validated_trait

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data/traits/physiology/cytogamy.yaml"
NEIGHBOR = ROOT / "data/traits/physiology/autogamy.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v499/metpo_proposal_classes_robot.tsv"
NEIGHBOR_SHA = "d2662ea26435cc14c57fcdcc5c00c7166716b1b0a3493d4cf29ed94cff8b9f85"
IDENTIFIER = "traitmech:000623"
NOBILI_1967 = "DOI:10.1017/S0016672300010740"
DILLER_1958 = "DOI:10.1111/j.1550-7408.1958.tb02567.x"
ORIAS_1979 = "DOI:10.1093/genetics/91.4.657"
OLD_SCOPE = (
    "Cytogamy involves paired cells without nuclear exchange in Nobili and "
    "Luporini p.39, unlike this unpaired-cell definition."
)
NEW_SCOPE = (
    "Cytogamy traitmech:000623 involves paired cells without nuclear exchange "
    "in Nobili and Luporini p.39, unlike this unpaired-cell definition. Diller "
    "(1958), DOI:10.1111/j.1550-7408.1958.tb02567.x, uses double autogamy for "
    "the tentative paired-cell observation. That broader source terminology "
    "does not make cytogamy a child or exact synonym of this operationally "
    "unpaired-cell class."
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "cytogamy",
    "definition": (
        "A sexual-reproduction phenotype in which paired cells undergo "
        "self-fertilization by fusion of gametic nuclei originating within "
        "each cell, without reciprocal gametic-nuclear exchange."
    ),
    "definition_source": NOBILI_1967,
    "trait_category": "PHYSIOLOGY",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["METPO:1000059"],
    "evidence": [
        {
            "reference": NOBILI_1967,
            "snippet": (
                "Cytogamy is a process of internal self-fertilization in animals "
                "which appear to conjugate, but which in fact do not exchange nuclei"
            ),
            "notes": (
                "Nobili and Luporini (1967), PMID:4964874, p.39 parenthetical "
                "before the Wichterman citation, checked in the typeset PDF. "
                "This directly read definition supports paired-cell internal "
                "self-fertilization without nuclear exchange. The surrounding "
                "Results and Table 2 offer cytogamy as an explanation for three "
                "mating-type outlier clones; they do not directly demonstrate "
                "cytogamy in those clones. The paper's primary experiments "
                "concern autogamy in Euplotes minuta. Do not count this terminology "
                "passage as independent experimental replication or turn its "
                "proposed explanation into a canonical taxon example. The cited "
                "1940 original was not read beyond bibliographic metadata."
            ),
        },
        {
            "reference": DILLER_1958,
            "snippet": (
                "In fact, the conjugation process seems to be one of double "
                "autogamy (cytogamy), rather than of reciprocal gametic interchange."
            ),
            "notes": (
                "Diller (1958), scientific abstract directly read on the Wiley "
                "publisher page. The qualifier seems is retained. Paired "
                "Paramecium polycaryum cultures collected at Annamalainagar, "
                "South India, showed nuclear behavior resembling autogamy in "
                "singles. Breakdown of the paroral cones permitting micronuclear "
                "passage was not observed; this is not a genetic exclusion of "
                "exchange. The abstract also describes fertilization and "
                "postzygotic nuclear reorganization. Double autogamy is "
                "source-attributed terminology, not equivalence with our "
                "unpaired-cell autogamy class. Full text, actual figures and "
                "tables were not inspected; the tentative observation is not "
                "an unqualified canonical example."
            ),
        },
        {
            "reference": ORIAS_1979,
            "snippet": (
                "cytogamy generates exconjugant clones that derive their entire "
                "genetic information from a single meiotic product of their "
                "cytoplasmic parent."
            ),
            "notes": (
                "Orias and Hamilton (1979), PMID:17248904, PMC1216858, scientific "
                "abstract clause after By analogy to Paramecium, directly checked "
                "in Europe PMC core metadata and NCBI PMC EFetch front-matter XML. "
                "The abstract reports hyperosmotic-shock-induced cytogamy in "
                "tested Tetrahymena thermophila strains and high fertility in "
                "most progeny. Its whole-genome-homozygote interpretation is "
                "source-specific, not a universal definition requirement or "
                "a genome-sequencing result established here. Other rare "
                "transmission abnormalities were not characterized in that "
                "abstract. The full text, Methods, actual figures and tables "
                "remain unread: PMC EFetch withholds body XML, and attempted "
                "public PDF retrieval did not yield a readable PDF. Strain "
                "provenance is unresolved; no natural canonical example or "
                "protein-level causal mechanism is inferred from this abstract."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "cytogamy-scope-and-hierarchy",
            "prompt": "Distinguish paired-cell self-fertilization from unpaired autogamy.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Pairing with internal gametic-nuclear fusion and no reciprocal "
                "exchange distinguishes this class from ordinary conjugation "
                "with exchange and from operationally unpaired autogamy "
                "traitmech:000622. Diller (1958) calls the tentative observation "
                "double autogamy; preserve that broader source usage without "
                "silently making cytogamy a child or exact synonym of the "
                "unpaired class. This is not all selfing or a literal mating "
                "locus. No universal hyperosmotic trigger, whole-genome "
                "homozygosity, nuclear count or inability to outcross is imposed. "
                "Do not infer species-level disjointness between reproductive "
                "modes. Use phenotype METPO:1000059 pending a narrower "
                "reproductive-phenotype parent; PHYSIOLOGY is a filesystem "
                "category. Verify external equivalences and synonym scope "
                "before adding mappings."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "cytogamy-mechanism-and-provenance",
            "prompt": "Resolve original cytology, strain provenance and molecular mechanisms.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "The 1967 definitional passage is not a direct cytogamy "
                "experiment, the 1958 observation is tentative, and the 1979 "
                "evidence here is limited to its scientific abstract. Retrieve "
                "the original primary study DOI:10.1002/jmor.1050660303 "
                "(Wichterman, 1940) and the remaining experimental material "
                "before stronger cytological or natural-strain claims. That "
                "1940 DOI is a metadata-verified research lead, not counted "
                "trait evidence. No canonical example is assigned from "
                "unresolved provenance or tentative marker explanations. "
                "Induced transmission outcomes do not identify a molecular "
                "causal pathway; graphs and protein accessions remain deferred. "
                "Retain actual snippet-resolver outcomes separately from "
                "direct source checks."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
    ],
}


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    record_curation_event(
        record, curator="codex", action="MINTED_TRAITMECH_ID",
        changes=(
            "Added cytogamy with three DOI-backed snippets and paired-cell "
            "self-fertilization scope. Ignored-and-hidden novelty/allocation "
            "checks found no exact record or collision. Reserved METPO:1057600 "
            "in v499 under phenotype, not operational unpaired autogamy. "
            "Preserved tentative observations, induced-system and source-access "
            "limits; deferred canonical examples, mappings and causal graphs."
        ),
        llm_assisted=True, timestamp="2026-10-05T16:16:00Z",
    )
    return record


def build_neighbor(before: dict) -> dict:
    record = copy.deepcopy(before)
    scope = record["discussions"][0]
    if (record["identifier"] != "traitmech:000622" or record["label"] != "autogamy"
            or record["mapping_status"] != "PROPOSED"
            or record["parent_traits"] != ["METPO:1000059"]
            or scope["discussion_id"] != "autogamy-scope-and-hierarchy"
            or scope["status"] != "OPEN" or scope["rationale"].count(OLD_SCOPE) != 1):
        raise SystemExit("Neighbor scope differs from reviewed preimage")
    scope["rationale"] = scope["rationale"].replace(OLD_SCOPE, NEW_SCOPE)
    record_curation_event(
        record, curator="codex", action="LINKED_RELATED_TRAIT",
        changes=(
            "Linked paired-cell cytogamy traitmech:000623 and attributed Diller's "
            "broader double-autogamy usage. Preserved the unpaired definition, "
            "evidence, example and parent; did not assert subsumption or equivalence."
        ),
        llm_assisted=True, timestamp="2026-10-05T16:16:00Z",
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
        "METPO:1057600", record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/cytogamy.yaml"]
                 + [e["reference"] for e in record["evidence"]]),
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Paired-cell internal self-fertilization without reciprocal nuclear exchange; not unpaired autogamy.",
        IDENTIFIER,
    ])
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not NEIGHBOR.exists():
        raise SystemExit("Missing reviewed neighbor preimage")
    before = yaml.safe_load(NEIGHBOR.read_text())
    expected_neighbor = build_neighbor(neighbor_writer.build_record())
    record = build_record()
    proposal = proposal_tsv(record)
    if before == expected_neighbor:
        neighbor = before
    elif hashlib.sha256(NEIGHBOR.read_bytes()).hexdigest() == NEIGHBOR_SHA:
        neighbor = build_neighbor(before)
    else:
        raise SystemExit("Existing neighbor differs from reviewed preimage or result")
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
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
