#!/usr/bin/env python3
"""Add the Bacillus cereus B4264 SduA protein example to the Shedu system record.

Scope: one record (`data/traits/genomics/shedu_system.yaml`,
`traitmech:000220`). The script adds a `GENE_OR_PROTEIN` causal node for the
single-protein Shedu immune nuclease and attaches `UniProtKB:B7HFR2` as a
taxon-paired `protein_examples` entry with primary-literature evidence.

Grounding: InterPro offers only domain-level entries for this protein
(IPR025359 SduA C-terminal, formerly Pfam DUF4263 / PF14082, and IPR048396
SduA N-terminal), so the node is `REVIEWED_LABEL_ONLY` per
docs/GROUNDING_POLICY.md rather than grounded to one domain of a
single-protein system.

Dry run by default; pass --apply to write.
"""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from traitmech.curate.curation_event import record_curation_event  # noqa: E402
from traitmech.validation.write_validated import write_validated_trait  # noqa: E402

TARGET = REPO_ROOT / "data" / "traits" / "genomics" / "shedu_system.yaml"
IDENTIFIER = "traitmech:000220"
GRAPH_ID = "shedu_dna_end_nicking"
NODE_ID = "sdua_immune_nuclease"
ANCHOR_NODE = "shedu_locus"
CURATOR = "claude"
TIMESTAMP = "2026-10-08T04:22:03Z"
RETRIEVED_ON = "2026-10-08"

GU = "DOI:10.1016/j.molcel.2024.12.004"

ACTIVATION_SNIPPET = (
    "we reveal the structural basis for activation of Bacillus cereus Shedu"
)
NTD_CONTROL_SNIPPET = (
    "Two cryoelectron microscopy structures of Shedu show that it switches "
    "between inactive and active states through conformational changes "
    "affecting active-site architecture, which are controlled by the "
    "protein's N-terminal domain (NTD)"
)

PROTEIN_EXAMPLE: dict[str, Any] = {
    "uniprot_id": "UniProtKB:B7HFR2",
    "protein_label": "Shedu protein SduA",
    "gene_symbol": "sduA",
    "taxon_id": "NCBITaxon:405532",
    "taxon_label": "Bacillus cereus (strain B4264)",
    "entry_status": "REVIEWED",
    "retrieved_on": RETRIEVED_ON,
    "entry_version": 58,
    "sequence_version": 1,
    "role": (
        "Bacillus cereus B4264 SduA switches between inactive and active "
        "states through conformational changes affecting active-site "
        "architecture, which Gu et al. report are controlled by its "
        "N-terminal domain. UniProt annotates this entry as the only "
        "component of its Shedu system; the attached snippets do not "
        "establish that single-component architecture."
    ),
    "evidence": [
        {
            "reference": GU,
            "snippet": ACTIVATION_SNIPPET,
            "notes": (
                "Gu et al. determined cryo-EM structures of Bacillus cereus "
                "Shedu; PDBe maps their entries 8TI8, 8TI9 and 8TIA to "
                "UniProtKB:B7HFR2 (Bacillus cereus B4264), so the "
                "structurally characterized protein is this accession. "
                "Snippet verified verbatim in the Europe PMC abstract of "
                "PMID:39742666."
            ),
        },
        {
            "reference": GU,
            "snippet": NTD_CONTROL_SNIPPET,
            "notes": (
                "Gu et al. establish the N-terminal domain as the regulator "
                "of the nuclease active site in this B. cereus protein. The "
                "role statement is scoped to the tested protein; the paper's "
                "survey of 79 N-terminal domain types is explicitly about "
                "homologs, not about this accession. Snippet verified "
                "verbatim in the Europe PMC abstract of PMID:39742666."
            ),
        },
    ],
}

NODE: dict[str, Any] = {
    "node_id": NODE_ID,
    "label": "SduA immune nuclease",
    "node_type": "GENE_OR_PROTEIN",
    "description": (
        "The single-protein Shedu immune nuclease, comprising a conserved "
        "nuclease core and an N-terminal regulatory/sensor domain."
    ),
    "gene_symbols": ["sduA"],
    "grounding_status": "REVIEWED_LABEL_ONLY",
    "grounding_notes": (
        "No family-level term covers SduA. A bounded search of all InterPro "
        "member databases and of GO via OLS4 for 'Shedu' on 2026-10-08 "
        "returned only two domain entries plus their InterPro integrations: "
        "IPR025359 (Shedu protein SduA, C-terminal; Pfam PF14082, whose "
        "InterPro name history is DUF4263 then SduA_C) and IPR048396 (Shedu "
        "protein SduA, N-terminal; Pfam PF21407). Neither denotes the whole "
        "protein: InterPro reports PF14082 in 1304 UniProt proteins across "
        "2464 taxa with 18 domain architectures, so grounding this "
        "whole-protein node to the C-terminal domain would sweep in carriers "
        "whose partner domains differ from SduA's. UniProt lists no NCBIfam "
        "cross-reference for B7HFR2, and OLS4 returns no GO term for Shedu. "
        "The node therefore stays reviewed label-only rather than taking a "
        "domain term as a family grounding."
    ),
    "protein_examples": [PROTEIN_EXAMPLE],
}

EDGE: dict[str, Any] = {
    "subject": NODE_ID,
    "predicate": "contributes to",
    "predicate_id": "RO:0002326",
    "object": "shedu_nuclease_activation",
    "description": (
        "In Bacillus cereus SduA, the N-terminal domain controls switching "
        "of the nuclease core between inactive and active states. Scoped to "
        "that protein: the graph's scope_notes leave the sensor class open "
        "across Shedu homologs, and the Loeff edge gives the N-terminal "
        "domain a DNA-end clamp role in a different homolog."
    ),
    "evidence": [
        {
            "reference": GU,
            "snippet": NTD_CONTROL_SNIPPET,
            "notes": (
                "Gu et al. support N-terminal-domain-controlled activation of "
                "the B. cereus Shedu nuclease active site."
            ),
        },
    ],
}

EVENT_CHANGES = (
    "Added a GENE_OR_PROTEIN node for the single-protein Shedu immune "
    "nuclease with UniProtKB:B7HFR2 (Shedu protein SduA, Bacillus cereus "
    "B4264, NCBITaxon:405532) as a taxon-paired protein example, plus one "
    "contributes-to edge to Shedu nuclease activation. UniProt REST verified "
    "the accession anonymously on 2026-10-08 as a current reviewed "
    "(Swiss-Prot) primary accession with no secondary accessions, entry "
    "version 58 and sequence version 1, organism Bacillus cereus strain "
    "B4264 (taxon 405532), cross-referenced to Pfam PF14082 (SduA_C, whose "
    "InterPro name history is DUF4263 then SduA_C) and PF21407. Evidence is "
    "Gu et al. 2024 Mol Cell "
    "(PMID:39742666, DOI:10.1016/j.molcel.2024.12.004), whose cryo-EM "
    "entries 8TI8/8TI9/8TIA PDBe maps to this exact accession; both snippets "
    "were verified verbatim against the Europe PMC abstract. The node is "
    "REVIEWED_LABEL_ONLY because no family-level InterPro, NCBIfam or GO "
    "term covers SduA: only the two domain entries IPR025359 and IPR048396 "
    "exist, and PF14082 spans 1304 UniProt proteins with 18 domain "
    "architectures. Graph scope_status, mapping_status, definition, "
    "hierarchy and existing evidence are unchanged."
)


def build(record: dict[str, Any]) -> dict[str, Any]:
    if record.get("identifier") != IDENTIFIER:
        raise SystemExit(f"{TARGET} is not {IDENTIFIER}")
    graphs = [g for g in record.get("causal_graphs") or [] if g.get("graph_id") == GRAPH_ID]
    if len(graphs) != 1:
        raise SystemExit(f"expected exactly one {GRAPH_ID} graph in {TARGET}")
    graph = graphs[0]
    nodes = graph["nodes"]
    if any(n.get("node_id") == NODE_ID for n in nodes):
        raise SystemExit(f"{NODE_ID} already present in {GRAPH_ID}")
    if not any(n.get("node_id") == EDGE["object"] for n in nodes):
        raise SystemExit(f"{EDGE['object']} missing from {GRAPH_ID}")
    anchor = next(i for i, n in enumerate(nodes) if n.get("node_id") == ANCHOR_NODE)
    nodes.insert(anchor + 1, NODE)
    graph["edges"].insert(0, EDGE)
    record_curation_event(
        record,
        curator=CURATOR,
        action="ADD_SDUA_PROTEIN_EXAMPLE",
        changes=EVENT_CHANGES,
        llm_assisted=True,
        timestamp=TIMESTAMP,
    )
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    record = build(yaml.safe_load(TARGET.read_text()))
    if args.apply:
        write_validated_trait(record, TARGET)
        print(f"wrote {TARGET.relative_to(REPO_ROOT)}")
        return
    with tempfile.TemporaryDirectory() as tmp:
        check_path = Path(tmp) / TARGET.name
        write_validated_trait(record, check_path)
        print(f"would write {TARGET.relative_to(REPO_ROOT)} (validated)")


if __name__ == "__main__":
    main()
