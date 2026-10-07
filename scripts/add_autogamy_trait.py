"""Add autogamy with nuclear-fusion scope and qualified ciliate evidence."""

from __future__ import annotations

import argparse
import copy
import csv
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

IDENTIFIER = "traitmech:000622"
TARGET = ROOT / "data/traits/physiology/autogamy.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v498"
NOBILI_1967 = "DOI:10.1017/S0016672300010740"
BERGER_1986 = "DOI:10.1016/0014-4827(86)90492-1"
THIND_2020 = "DOI:10.1093/gbe/evaa052"

RECORD = {
    "identifier": IDENTIFIER,
    "label": "autogamy",
    "definition": (
        "A sexual-reproduction phenotype in which two meiotically derived gametic "
        "nuclei formed within one unpaired cell fuse with each other."
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
                "the synkaryon, or fertilization nucleus, is formed by the union "
                "of two pronuclei from the same individual."
            ),
            "notes": (
                "Nobili and Luporini (1967), Introduction p.35, contiguous clause "
                "after Thus, checked against the typeset publisher PDF. Main text "
                "and Summary were read; pp.35-39 and Tables 1-2 were visually "
                "inspected. Results 3(i) use serially fixed cells, not live fusion "
                "tracking. Genetic identity of fusing nuclei was inferred, not "
                "resolved cytologically. Results 3(ii) and Summary support retention "
                "of mt-locus heterozygosity in A-25; complete homozygosity therefore "
                "does not define autogamy. This is marker evidence, not whole-genome "
                "heterozygosity measurement or an identified molecular mechanism. "
                "Table 3 was not visually audited; no quantitative reanalysis is claimed."
            ),
        },
        {
            "reference": BERGER_1986,
            "snippet": (
                "Autogamy is a process of meiosis and fertilization which takes "
                "place in unpaired Paramecium cells, and which is triggered by starvation."
            ),
            "notes": (
                "Berger (1986), PMID:3743667, opening scientific-abstract sentence "
                "directly retrieved in Europe PMC core metadata. The complete "
                "abstract supports unpaired-cell meiosis/fertilization and a "
                "two-stage commitment response to nutritional down-shift. Starvation "
                "and cell-cycle timing concern the studied Paramecium system, not "
                "universal definition requirements. Full text, actual figures and "
                "strain provenance remain uninspected; no canonical example or "
                "protein-level causal mechanism is inferred from this abstract."
            ),
        },
        {
            "reference": THIND_2020,
            "snippet": (
                "Autogamy in P. tetraurelia occurs in unpaired cells, is induced "
                "by starvation, and generates fully homozygous individuals"
            ),
            "notes": (
                "Thind et al. (2020), PMID:32163147, PMC7239694, Introduction sec1 "
                "clause before citations, checked in raw full-text XML. The "
                "scientific abstract, Introduction, strain/culture and autogamy-"
                "reactivity Methods, and survival-advantage Results were inspected. "
                "The scored autogamy readout was DAPI-visible macronuclear "
                "fragmentation, not direct gametic-nuclear fusion in every counted "
                "cell. Fully homozygous stock d12 mass cultures do not establish "
                "that every microbial autogamy event yields homozygosity. Survival "
                "associations and proposed heat-shock-protein models are not a "
                "validated causal pathway. Natural provenance of d12 remains "
                "unresolved; it is not a canonical example here. Actual figures, "
                "remaining sections and supplements were not audited."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:74792",
            "taxon_label": "Moneuplotes minuta",
            "reference": NOBILI_1967,
            "note": (
                "Qualified A-25 example, named Euplotes minuta in the paper. "
                "Material and Methods p.36 traces it to coastal sand near Pisa, "
                "subsequently laboratory-maintained; no exact collection year is "
                "inferred from the relative date. Serial fixed-cell cytology "
                "supports the phenotype. Nonautogamic controls 5G/20 and hybrid "
                "offspring are not this example; A-25 also conjugates. NCBI "
                "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=74792 "
                "and EFetch taxonomy XML checked on 2026-10-05 resolve Moneuplotes "
                "minuta with Euplotes minuta as a synonym. This species-name mapping "
                "does not authenticate a modern strain accession or reference genome."
            ),
        },
    ],
    "discussions": [
        {
            "discussion_id": "autogamy-scope-and-hierarchy",
            "prompt": "Keep intracellular nuclear fusion distinct from broad self-fertility.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "Use the unpaired-cell nuclear-fusion sense supported by the cited "
                "ciliate studies, not plant self-pollination or all selfing. The "
                "existing homothallism traitmech:000609, unisexual reproduction "
                "traitmech:000613 and primary homothallism traitmech:000614 "
                "definitions are explicitly fungal-scoped and are not exact parents "
                "or synonyms. Cytogamy involves paired cells without nuclear exchange "
                "in Nobili and Luporini p.39, unlike this unpaired-cell definition. "
                "No universal genetic identity, complete homozygosity, starvation "
                "trigger, nuclear count, inability to outcross or gamete-size "
                "asymmetry is imposed. Use phenotype METPO:1000059 pending a "
                "narrower reproductive-phenotype parent; PHYSIOLOGY is a filesystem "
                "category. Verify external equivalences and broader automixis "
                "terminology before adding synonyms or mappings."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-05",
        },
        {
            "discussion_id": "autogamy-mechanism-and-coverage",
            "prompt": "Resolve molecular mechanisms and broader taxon coverage before extension.",
            "kind": "CURATION_TODO",
            "status": "OPEN",
            "rationale": (
                "This is an organismal reproductive phenotype, not the literal mt "
                "marker locus or a heat-shock expression signature. Nuclear-selection "
                "inference, nutritional commitment and survival associations do not "
                "supply a universal protein-resolved mechanism. No causal graph "
                "bypasses missing accession-level and perturbation evidence. Keep "
                "macronuclear-fragmentation scoring separate from directly observed "
                "fusion. The diatom terminology paper DOI:10.1080/0269249X.2013.791344 "
                "is only a research lead: the author repository at "
                "https://hdl.handle.net/20.500.12594/2237 supplied metadata, not "
                "the full terminology passage. It is not counted as evidence. Read "
                "that passage before asserting equivalence with paedogamy or "
                "automixis. Preserve actual abstract-resolver verdicts separately "
                "from direct full-text checks."
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
            "Added autogamy with three DOI-backed snippets, unpaired-cell nuclear-"
            "fusion scope and a provenance-qualified Moneuplotes minuta A-25 "
            "example. Ignored-and-hidden novelty/allocation searches found no "
            "exact record or collision. Reserved METPO:1057500 in v498 under "
            "phenotype. Deferred unverified mappings, a narrower parent and "
            "protein-level mechanisms; did not impose universal homozygosity."
        ),
        llm_assisted=True, timestamp="2026-10-05T15:16:14Z",
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
        "METPO:1057500", record["label"], record["definition"],
        "|".join(["TraitMech:data/traits/physiology/autogamy.yaml"]
                 + [e["reference"] for e in record["evidence"]]),
        "METPO:1000059", "", "", "metpo_traitmech_2026_10", "HIGH",
        "Unpaired-cell gametic-nuclear fusion; not universal homozygosity or all selfing.",
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
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
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
