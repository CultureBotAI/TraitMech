# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** Disproportionation
- **METPO identifier:** METPO:1000806
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A metabolism in which a single substrate simultaneously undergoes both oxidation and reduction reactions, with part of the substrate serving as the electron donor and another part serving as the electron acceptor.
- **Parent traits:** METPO:1000060
- **Synonyms:** 
- **Existing evidence:** DOI:10.1080/17415990802105770: serve as both electron donor and acceptor (Review supports inorganic sulfur disproportionation as one substrate serving both donor and acceptor roles.) | DOI:10.1016/j.gca.2013.03.013: elemental sulfur disproportionation (Study supports elemental sulfur disproportionation in acidophilic microbial metabolism.)
- **Existing causal graph summary:** sulfur_disproportionation_redox_split: 8 nodes, 7 edges

## Research Objective

Research the microbial trait **Disproportionation** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/disproportionation.yaml`.

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
**Generated:** 2026-06-18T04:55:30.507533

1. diao2023globaldiversityand pages 1-2
2. wang2023disproportionationofinorganic pages 9-12
3. yan2024characterizationofsulfur pages 49-52
4. wang2023disproportionationofinorganic pages 12-13
5. twible2024phandthiosulfate pages 12-14
6. gordon2024microbialsulfurpathways pages 19-21
7. liu2024enrichmentofacidtolerant pages 1-2
8. wang2023disproportionationofinorganic pages 2-4
9. twible2024phandthiosulfate pages 1-2
10. yan2024characterizationofsulfur pages 42-46
11. twible2024phandthiosulfate pages 5-6
12. yan2024characterizationofsulfur pages 59-63
13. wang2023disproportionationofinorganic pages 1-2
14. gordon2024microbialsulfurpathways pages 1-5
15. gordon2024microbialsulfurpathways pages 5-8
16. germe2023giuliadermo pages 21-24
17. petushkova2024thecompletegenome pages 22-23
18. petushkova2024thecompletegenome pages 20-22
19. germe2023giuliadermo pages 24-28
20. petushkova2024thecompletegenome pages 17-19
21. petushkova2024thecompletegenome pages 19-20
22. twible2024phandthiosulfate pages 11-12
23. Fe(III)
24. S2O32-
25. https://doi.org/10.1007/978-3-031-54306-7_15
26. https://doi.org/10.1128/msystems.00954-22
27. https://doi.org/10.3389/fmicb.2024.1426584
28. https://doi.org/10.1038/s41467-023-37426-8
29. https://doi.org/10.1007/s10230-024-01016-x
30. https://doi.org/10.1093/femsre/fuad058
31. https://doi.org/10.3389/fmicb.2024.1475137
32. https://doi.org/10.3390/microorganisms12020391
33. https://doi.org/10.1038/s41579-024-01044-y
34. https://doi.org/10.1007/978-3-031-54306-7\_15,
35. https://doi.org/10.1128/msystems.00954-22,
36. https://doi.org/10.1093/femsre/fuad058,
37. https://doi.org/10.1038/s41467-023-37426-8,
38. https://doi.org/10.3389/fmicb.2024.1426584,
39. https://doi.org/10.1007/s10230-024-01016-x,
40. https://doi.org/10.3389/fmicb.2024.1475137,
41. https://doi.org/10.3390/microorganisms12020391,