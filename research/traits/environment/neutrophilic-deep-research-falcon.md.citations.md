# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** neutrophilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003001
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference characterized by optimal growth at near-neutral pH values, typically between pH 6.5 and 7.5.
- **Parent traits:** METPO:1003000
- **Synonyms:** neutralophile, neutralophilic, neutrophile
- **Existing evidence:** DOI:10.1038/nrmicro2549: cytoplasmic pH ... must maintain for growth (Supports pH growth preference as tied to cytoplasmic pH requirements.)
- **Existing causal graph summary:** neutrophilic_neutral_ph_homeostasis: 11 nodes, 9 edges

## Research Objective

Research the microbial trait **neutrophilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/neutrophilic.yaml`.

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
**Generated:** 2026-08-04T02:08:12.157983

1. krulwich2011molecularaspectsof pages 1-3
2. maksimova2024metabolicandmorphological pages 1-2
3. krulwich2011molecularaspectsof pages 5-6
4. guan2020microbialresponseto pages 2-4
5. guo2019recentadvancesof pages 3-4
6. beetham2024histidinetransportis pages 1-2
7. beetham2024histidinetransportis pages 7-8
8. maksimova2024metabolicandmorphological pages 5-6
9. 10.1038/nrmicro2549
10. 10.1371/journal.ppat.1011927
11. 10.1155/2024/3087296
12. 10.1007/s00253-019-10226-1
13. 10.1007/s11274-019-2770-2
14. https://doi.org/10.1038/nrmicro2549
15. https://doi.org/10.1371/journal.ppat.1011927
16. https://doi.org/10.1155/2024/3087296
17. https://doi.org/10.1007/s00253-019-10226-1
18. https://doi.org/10.1007/s11274-019-2770-2
19. https://doi.org/10.1038/nrmicro2549,
20. https://doi.org/10.1371/journal.ppat.1011927,
21. https://doi.org/10.1155/2024/3087296,
22. https://doi.org/10.1007/s11274-019-2770-2,
23. https://doi.org/10.1007/s00253-019-10226-1,