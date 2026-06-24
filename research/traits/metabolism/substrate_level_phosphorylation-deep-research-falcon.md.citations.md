# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Substrate-level phosphorylation
- **METPO identifier:** METPO:1000804
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which ATP is formed directly by transfer of a phosphoryl group from a substrate to ADP.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1111/1751-7915.13746: Substrate-level phosphorylation is one of the main sources (Review supports SLP as microbial energy conservation in fermentative metabolism.) | DOI:10.1128/MMBR.69.1.12-50.2005: phosphotransacetylase [PTA], acetate kinase [ACK] (Review supports acetate kinase and phosphotransacetylase as central acetate-switch enzymes.)
- **Existing causal graph summary:** substrate_level_phosphorylation_direct_atp: 9 nodes, 6 edges

## Research Objective

Research the microbial trait **Substrate-level phosphorylation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/substrate_level_phosphorylation.yaml`.

## Required Findings

### 1. Trait Scope
- Clarify what phenotype, physiological capacity, environmental preference, or assay-observed
  property the trait represents.
- Identify boundary cases and distinguish the trait from nearby traits.

### 2. Causal Graph Entities
- Pathways and metabolic modules.
- Environmental factors and experimental factors.
- Genes, proteins, enzymes, transporters, and complexes.
- Chemicals, electron donors, electron acceptors, nutrients, metabolites, and inhibitors.
- Organelles, cellular localizations, molecular functions, and biological processes.

### 3. Evidence-Backed Edges
- Propose causal edges as subject-predicate-object triples.
- For every proposed edge, provide a reference, a short supporting quote/snippet, and notes
  explaining how the source supports the edge.
- Prefer DOI references. Use PMID only when a DOI is not available.
- Mark weak, taxon-specific, assay-specific, or inferred claims as uncertain.

### 4. Ontology Grounding
- Suggest CURIEs where available: METPO, GO, CHEBI, ENVO, NCBITaxon, EC, UniProt, Rhea,
  KEGG, MetaCyc, or other stable identifiers.
- Do not invent identifiers. Label-only candidate nodes are acceptable when grounding is unclear.

## Output Format

Return a curation-focused report with:
- A short scope summary.
- Candidate nodes grouped by type.
- Candidate causal edges in a table with reference, snippet, and notes.
- DOI-first bibliography.
- Warnings for claims that should not yet be curated into TraitMech.

**Provider:** falcon
**Generated:** 2026-06-18T06:07:38.485732

1. hackmann2024thevastlandscape pages 1-2
2. hackmann2024thevastlandscape pages 2-3
3. chowdhary2023effectofsubstrate pages 17-21
4. hosmer2023bacterialacetatemetabolism pages 1-3
5. hackmann2024thevastlandscape pages 4-5
6. bae2024harnessingacetogenicbacteria pages 7-8
7. zhang2024understandingenergyfluctuation pages 4-6
8. zhang2024understandingenergyfluctuation pages 6-7
9. zhang2024understandingenergyfluctuation pages 10-12
10. PTA
11. ACK
12. ADP-forming
13. https://doi.org/10.1093/femsre/fuae016
14. https://doi.org/10.1042/ETLS20220092
15. https://doi.org/10.1186/s12934-024-02572-1
16. https://doi.org/10.1039/d4cb00099d
17. https://doi.org/10.1042/etls20220092
18. https://doi.org/10.1093/femsre/fuae016,
19. https://doi.org/10.1042/etls20220092,
20. https://doi.org/10.1039/d4cb00099d,
21. https://doi.org/10.1186/s12934-024-02572-1,