# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur oxidation
- **METPO identifier:** traitmech:000106
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which an organism oxidizes reduced inorganic sulfur compounds (sulfide, elemental sulfur, thiosulfate) to sulfate, conserving energy and often supporting chemolithotrophic growth.
- **Parent traits:** METPO:1000060
- **Synonyms:** sulfide oxidation
- **Existing evidence:** DOI:10.1111/j.1574-6976.2009.00187.x:  (Ghosh & Dam review the biochemistry and molecular biology of lithotrophic sulfur oxidation across bacteria and archaea.) | DOI:10.1128/AEM.67.7.2873-2882.2001:  (Friedrich et al. describe a common mechanism for bacterial oxidation of reduced inorganic sulfur compounds (the Sox system).)
- **Existing causal graph summary:** sulfur_oxidation_sox: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **sulfur oxidation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/sulfur_oxidation.yaml`.

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
**Generated:** 2026-06-18T06:17:25.365307

1. liu2024determinantsofsulfuroxidizinga pages 17-20
2. yan2024characterizationofsulfur pages 59-63
3. twible2024phandthiosulfate pages 1-2
4. twible2024phandthiosulfate pages 5-6
5. petushkova2024thecompletegenome pages 19-20
6. rudenko2024mechanismofintracellular pages 1-2
7. rudenko2024mechanismofintracellular pages 12-13
8. li2024yeeelikebacterialsoxt pages 1-2
9. li2024yeeelikebacterialsoxt pages 7-8
10. li2024yeeelikebacterialsoxt pages 5-7
11. li2024yeeelikebacterialsoxt pages 2-3
12. sudo2024soxygenefamily pages 1-2
13. twible2024phandthiosulfate pages 10-11
14. gordon2024microbialsulfurpathways pages 1-5
15. gordon2024microbialsulfurpathways pages 5-8
16. sudo2024soxygenefamily pages 4-6
17. sudo2024soxygenefamily pages 8-11
18. sudo2024soxygenefamily pages 15-17
19. twible2024phandthiosulfate pages 9-10
20. liu2024determinantsofsulfuroxidizing pages 17-20
21. https://doi.org/10.3390/ijms252010962
22. https://doi.org/10.1093/ismejo/wrae110
23. https://doi.org/10.3389/fmicb.2024.1426584
24. https://doi.org/10.1007/s10230-024-01016-x
25. https://doi.org/10.1038/s42003-024-07270-7
26. https://doi.org/10.1128/msystems.01135-23
27. https://doi.org/10.3390/microorganisms12020391
28. https://doi.org/10.1038/s41564-024-01704-y
29. https://doi.org/10.3389/fmicb.2024.1426584,
30. https://doi.org/10.3390/ijms252010962,
31. https://doi.org/10.1007/s10230-024-01016-x,
32. https://doi.org/10.3390/microorganisms12020391,
33. https://doi.org/10.1038/s42003-024-07270-7,
34. https://doi.org/10.1128/msystems.01135-23,