"""Add the short Lamassu family and refine the existing HNH hierarchy."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

SLUG = "short_lamassu_system"
IDENTIFIER = "traitmech:000570"
TARGET = ROOT / "data/traits/genomics" / f"{SLUG}.yaml"
PARENT = ROOT / "data/traits/genomics/lamassu_system.yaml"
HNH = ROOT / "data/traits/genomics/lamassu_hnh_system.yaml"
PROPOSAL = ROOT / "proposals/metpo_traitmech_v447"
TIMESTAMP = "2026-10-03T12:33:00Z"
PAPER = "DOI:10.1073/pnas.2519643122"
STRUCTURE = "https://data.rcsb.org/rest/v1/core/polymer_entity/9NY5/3"
TAXON = "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=666&mode=Info"
PARENT_HASH = "29a239179478b4ea3adad5a834b59df15ab2877abc3fb68f6c0cfd575e1d217e"
HNH_HASH = "1a4ceacad9681901a3ccde8952dbeb75660209fc2dac9c3c88986e540d02f0df"
HNH_DEFINITION = (
    "A Lamassu system in which an organism possesses a locus encoding an HNH-domain "
    "LmuA effector, a short-form SMC-like LmuB sensor, and LmuC."
)
PARENT_ADDITION = (
    " Short Lamassu system (traitmech:000570) now captures the short-LmuB "
    "phylogenetic and structural family, not a fixed protein-length bin or an "
    "effector-specific detector. Lamassu-HNH is placed below it because its "
    "existing definition explicitly requires short-form LmuB. SMEK remains "
    "directly under the broader Lamassu parent because of its unresolved "
    "long-profile exception. The short family permits the reported LmuC-loss "
    "and effector-domain-loss architectures; type I is not an exact synonym "
    "for the whole short family. The Lamassu-Hypothetical registry label is "
    "not accepted as a separate biological trait here: unknown annotation "
    "does not establish effector-domain loss, and its relationship to the "
    "paper's clade O still needs explicit mapping. The long family and "
    "component-number subtypes remain separate discovery leads."
)
HNH_ADDITION = (
    " The direct parent is now traitmech:000570 short Lamassu system, "
    "matching the short-form LmuB restriction already present in this "
    "record's definition. This hierarchy refinement does not narrow the "
    "executable detector, resolve the functional gaps, or reinterpret "
    "computational calls as measured antiviral phenotypes."
)

RECORD = {
    "identifier": IDENTIFIER,
    "label": "short Lamassu system",
    "definition": (
        "A Lamassu system in which an organism possesses a locus from the "
        "short-LmuB family, characterized by shorter coiled-coil regions "
        "in its SMC-like LmuB sensor than in long Lamassu systems."
    ),
    "definition_source": PAPER,
    "trait_category": "GENOMICS",
    "term_kind": "CLASS",
    "mapping_status": "PROPOSED",
    "parent_traits": ["traitmech:000232"],
    "synonyms": [
        {
            "synonym_text": "short-form Lamassu system",
            "synonym_type": "EXACT_SYNONYM",
            "source": PAPER,
        }
    ],
    "evidence": [
        {
            "reference": PAPER,
            "snippet": (
                "two major clades, which were mainly distinguished by the "
                "length of coiled-coil regions"
            ),
            "notes": (
                "Results, LmuB phylogeny paragraph and Figure 1: the authors "
                "distinguish short and long families using phylogeny and "
                "structure. Their approximate 600-residue short-family "
                "average is not a membership cutoff."
            ),
        },
        {
            "reference": PAPER,
            "snippet": (
                "short Lamassus, selecting the experimentally validated "
                "Cap4 system from V. cholerae"
            ),
            "notes": (
                "Results, paragraph introducing structural work: identifies "
                "Vc-Cap4 as a short-family exemplar. Figure 2A shows its "
                "653-residue LmuB. Antiphage assays here used the natural "
                "operon expressed in E. coli, not a species-wide native-host assay."
            ),
        },
        {
            "reference": STRUCTURE,
            "snippet": '"rcsb_sample_sequence_length":653',
            "notes": (
                "PDB 9NY5, entity 3, entity_poly: deposited LmuB sequence "
                "length, consistent with paper Figure 2A. This is not the "
                "number of modeled residues or a length threshold for the family."
            ),
        },
        {
            "reference": STRUCTURE,
            "snippet": (
                '"pdbx_gene_src_ncbi_taxonomy_id":"666",'
                '"pdbx_gene_src_scientific_name":"Vibrio cholerae"'
            ),
            "notes": (
                "PDB entity_src_gen: source organism of the deposited LmuB, "
                "not the recombinant expression host. No strain or genome "
                "assembly is inferred from the species-level deposition."
            ),
        },
        {
            "reference": STRUCTURE,
            "snippet": (
                '"pdbx_host_org_ncbi_taxonomy_id":"562",'
                '"pdbx_host_org_scientific_name":"Escherichia coli"'
            ),
            "notes": (
                "PDB entity_src_gen explicitly identifies the separate "
                "expression host. This does not establish natural E. coli "
                "possession of the Vc-Cap4 locus."
            ),
        },
        {
            "reference": TAXON,
            "snippet": ("Taxonomy ID: 666 (for references in articles please use ncbitaxon:666)"),
            "notes": (
                "NCBI Taxonomy, verified 2026-10-03: taxon 666 resolves to "
                "Vibrio cholerae. This verifies identity only; the paper "
                "supports the exemplar's short-family classification."
            ),
        },
    ],
    "canonical_examples": [
        {
            "taxon_id": "NCBITaxon:666",
            "taxon_label": "Vibrio cholerae",
            "reference": PAPER,
            "note": (
                "The source organism of the Vc-Cap4 system explicitly selected "
                "as a short-Lamassu exemplar. PDB 9NY5 entity 3 independently "
                "records a 653-residue LmuB from taxon 666, expressed in E. coli. "
                "The cited antiphage assays use a heterologous E. coli host. "
                "This does not assert species-wide possession, a specific "
                "strain or assembly, or native V. cholerae phage resistance."
            ),
        }
    ],
    "discussions": [
        {
            "discussion_id": "short-lamassu-classification-and-mechanism-scope",
            "prompt": "Resolve family-wide mechanisms and classify borderline loci.",
            "kind": "KNOWLEDGE_GAP",
            "status": "OPEN",
            "rationale": (
                "Short denotes the phylogenetic and structural LmuB family, "
                "not an arbitrary amino-acid cutoff or an isolated short "
                "protein. LmuC-loss clade S and effector-domain-loss clade O "
                "preclude requiring one universal three-component effector "
                "architecture. Type I/II component classifications and "
                "effector names are not exact synonyms for this family. "
                "HNH's explicitly short-form definition supports its new "
                "parent; SMEK's unresolved long-profile call prevents the "
                "same inference. Other table-defined subtypes require their "
                "own scope review before reparenting. The Vc-Cap4 mechanism "
                "already described on the Lamassu parent is not assumed "
                "universal across short-family effectors, so no duplicate "
                "or universal mechanism graph is asserted here. A registry "
                "Hypothetical label must not be equated with clade O's "
                "effector-domain loss without explicit evidence."
            ),
            "posed_by": "codex",
            "posed_date": "2026-10-03",
        }
    ],
}


def event(record: dict, action: str, changes: str) -> None:
    record_curation_event(
        record,
        curator="codex",
        action=action,
        changes=changes,
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )


def build_record() -> dict:
    record = copy.deepcopy(RECORD)
    event(
        record,
        "MINTED_TRAITMECH_ID",
        "Added the literature-defined short Lamassu family with exact paper, "
        "PDB and NCBI snippets, a qualified Vc-Cap4 source-organism example, "
        "and no artificial protein-length cutoff. Ignored-and-hidden searches "
        "found no exact record or METPO term. Reserved METPO:1052400 in "
        "proposals/metpo_traitmech_v447 and refined the HNH child's parent.",
    )
    return record


def append_guarded(record: dict, discussion_id: str, old_hash: str, addition: str) -> bool:
    matches = [d for d in record["discussions"] if d["discussion_id"] == discussion_id]
    if len(matches) != 1:
        raise SystemExit("Expected one unchanged discussion")
    discussion = matches[0]
    if (discussion["kind"], discussion["status"]) != ("KNOWLEDGE_GAP", "OPEN"):
        raise SystemExit("Discussion kind or status changed")
    old = discussion["rationale"].removesuffix(addition)
    if hashlib.sha256(old.encode()).hexdigest() != old_hash:
        raise SystemExit("Discussion preimage changed; review before applying")
    if discussion["rationale"] != old:
        return False
    discussion["rationale"] += addition
    return True


def build_parent() -> dict:
    record = yaml.safe_load(PARENT.read_text())
    if (
        record["identifier"] != "traitmech:000232"
        or record["label"] != "Lamassu system"
        or record["mapping_status"] != "PROPOSED"
        or record["parent_traits"] != ["traitmech:000209"]
    ):
        raise SystemExit("Lamassu parent identity or hierarchy changed")
    if append_guarded(record, "lamassu-subtype-and-effector-gap", PARENT_HASH, PARENT_ADDITION):
        event(
            record,
            "TRACK_NARROWER_RECORD",
            "Linked traitmech:000570 short Lamassu system and the HNH parent "
            "refinement; retained the SMEK length exception and rejected "
            "unproven equivalence of a Hypothetical label to effector-domain loss.",
        )
    return record


def build_hnh() -> dict:
    record = yaml.safe_load(HNH.read_text())
    if (
        record["identifier"] != "traitmech:000568"
        or record["label"] != "Lamassu-HNH system"
        or record["mapping_status"] != "PROPOSED"
        or record["definition"] != HNH_DEFINITION
    ):
        raise SystemExit("HNH identity or biological scope changed")
    changed = append_guarded(record, "lamassu-hnh-function-and-model-scope", HNH_HASH, HNH_ADDITION)
    expected = ["traitmech:000232"] if changed else [IDENTIFIER]
    if record["parent_traits"] != expected:
        raise SystemExit("HNH parent changed; review before applying")
    if changed:
        record["parent_traits"] = [IDENTIFIER]
        event(
            record,
            "REPARENT_TO_SHORT_LAMASSU",
            "Placed the existing short-LmuB HNH architecture below "
            "traitmech:000570 short Lamassu system without changing its "
            "definition, evidence, model-scope qualifications or example. "
            "The v445 broader Lamassu proposal axiom remains true; v447 "
            "documents the added immediate-parent relation for upstream minting.",
        )
    return record


def proposal_tsv(record: dict) -> str:
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(
        [
            "proposed_id",
            "label",
            "definition",
            "definition_source",
            "parent",
            "synonyms",
            "xrefs",
            "subset",
            "priority",
            "observations",
            "traits_addressed",
        ]
    )
    writer.writerow(
        [
            "ID",
            "LABEL",
            "A IAO:0000115",
            ">A IAO:0000119",
            "SC %",
            "A oboInOwl:hasExactSynonym SPLIT=|",
            "A oboInOwl:hasDbXref SPLIT=|",
            "A oboInOwl:inSubset",
            "",
            "",
            "",
        ]
    )
    writer.writerow(
        [
            "METPO:1052400",
            record["label"],
            record["definition"],
            "|".join([f"TraitMech:data/traits/genomics/{SLUG}.yaml", PAPER, STRUCTURE]),
            "METPO:1018600",
            "short-form Lamassu system",
            "",
            "metpo_traitmech_2026_10",
            "HIGH",
            "Short-LmuB structural family, not a length bin or a type-I synonym. "
            "Parent of traitmech:000568 (v445 METPO:1052200); carry that "
            "additional subclass relation into the upstream ontology on minting.",
            IDENTIFIER,
        ]
    )
    return stream.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    record, parent, hnh = build_record(), build_parent(), build_hnh()
    proposal = proposal_tsv(record)
    proposal_path = PROPOSAL / "metpo_proposal_classes_robot.tsv"
    if TARGET.exists() and yaml.safe_load(TARGET.read_text()) != record:
        raise SystemExit("Existing target differs from this writer; review before applying")
    if proposal_path.exists() and proposal_path.read_text() != proposal:
        raise SystemExit("Existing proposal differs from this writer; review before applying")
    updates = [(TARGET, record), (PARENT, parent), (HNH, hnh)]
    with tempfile.TemporaryDirectory() as tmp:
        for path, updated in updates:
            write_validated_trait(updated, Path(tmp) / path.name)
    if args.apply:
        for path, updated in updates:
            write_validated_trait(updated, path)
        PROPOSAL.mkdir(parents=True, exist_ok=True)
        proposal_path.write_text(proposal)
    print("Applied" if args.apply else "Validated dry run; pass --apply to write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
