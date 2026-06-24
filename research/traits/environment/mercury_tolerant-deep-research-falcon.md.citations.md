# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** mercury tolerant
- **METPO identifier:** traitmech:000016
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metal tolerance in which an organism grows in the presence of toxic inorganic or organic mercury compounds, typically via the mer operon, whose mercuric reductase (MerA) reduces reactive Hg(II) to volatile Hg(0).
- **Parent traits:** traitmech:000012
- **Synonyms:** mercury resistant
- **Existing evidence:** DOI:10.1016/S0168-6445(03)00046-9: Bacterial resistance to inorganic and organic mercury compounds (HgR) is one of the most widely observed phenotypes in eubacteria (Review supports mercury resistance as a widespread bacterial phenotype mediated by MerA, "that reduces reactive ionic Hg(II) to volatile, relatively inert, monoatomic Hg(0) vapor".) | PMID:12829273: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins (Heavy-metal resistance review situates mercury detoxification within the broader prokaryotic metal-resistance machinery.)
- **Existing causal graph summary:** mercury_tolerance_mer_reduction: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **mercury tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/mercury_tolerant.yaml`.

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
**Generated:** 2026-06-17T22:44:27.250757

1. kumar2023aretrospectionon pages 9-11
2. bhat2024horizontalgenetransfer pages 1-2
3. paape2024adaptationtomercury pages 1-3
4. gonzalezreguero2023bioremediationofenvironments pages 3-4
5. paape2024adaptationtomercury pages 9-11
6. tiodar2024plantcolonizersof pages 11-13
7. thai2023syntheticbacteriafor pages 5-6
8. tiodar2024plantcolonizersof pages 1-2
9. bhat2023localadaptationto pages 6-9
10. gonzalezreguero2023bioremediationofenvironments pages 1-3
11. gonzalezreguero2023bioremediationofenvironments pages 4-6
12. gonzalezreguero2023bioremediationofenvironments pages 6-8
13. https://doi.org/10.1186/s12866-024-03391-5
14. https://doi.org/10.21203/rs.3.rs-3854515/v1
15. https://doi.org/10.1007/s11104-024-06552-7
16. https://doi.org/10.1128/spectrum.00553-23
17. https://doi.org/10.1007/s11274-023-03686-1
18. https://doi.org/10.3389/fbioe.2023.1178680
19. https://doi.org/10.1101/2023.12.27.573466
20. https://doi.org/10.3390/su151813292
21. https://doi.org/10.21203/rs.3.rs-3854515/v1,
22. https://doi.org/10.1186/s12866-024-03391-5,
23. https://doi.org/10.3390/su151813292,
24. https://doi.org/10.1101/2023.12.27.573466,
25. https://doi.org/10.1128/spectrum.00553-23,
26. https://doi.org/10.1007/s11274-023-03686-1,
27. https://doi.org/10.1007/s11104-024-06552-7,
28. https://doi.org/10.3389/fbioe.2023.1178680,