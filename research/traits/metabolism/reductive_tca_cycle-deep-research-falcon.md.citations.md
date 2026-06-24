# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** reductive tricarboxylic acid cycle
- **METPO identifier:** traitmech:000021
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway (reductive citric acid / Arnon-Buchanan cycle) that runs the tricarboxylic acid cycle in reverse to fix CO2. It operates in anaerobic and microaerophilic bacteria such as green sulfur bacteria (Chlorobium) and Aquificales.
- **Parent traits:** traitmech:000019
- **Synonyms:** reductive citric acid cycle, rTCA cycle, Arnon-Buchanan cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the reductive citric acid cycle as functional in anaerobic/microaerophilic autotrophs.) | DOI:10.1146/annurev-marine-120709-142712:  (Hügler & Sievert document the rTCA cycle in chemolithoautotrophs and green sulfur bacteria in marine systems.)
- **Existing causal graph summary:** rtca_reverse_tricarboxylic_acid_co2_fixation: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **reductive tricarboxylic acid cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/reductive_tca_cycle.yaml`.

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
**Generated:** 2026-06-18T06:02:43.770102

1. power2024agenusin pages 5-6
2. petushkova2024thecompletegenome pages 10-12
3. laux2024livinginmangroves pages 18-19
4. mondal2024aquificaeovercomescompetition pages 17-19
5. faulkner2023chemoautotrophicproductionof pages 7-9
6. mondal2024aquificaeovercomescompetition pages 16-17
7. prioretti2023carbonfixationin pages 6-8
8. sokolskyi2023roleofhorizontal pages 1-6
9. cui2023reconfigurationofthe pages 2-3
10. cui2023reconfigurationofthe pages 1-2
11. mondal2024aquificaeovercomescompetition pages 1-2
12. power2024agenusin pages 1-2
13. heker2025chemoorganoautotrophiclifestyleof pages 1-2
14. faulkner2023chemoautotrophicproductionof pages 9-11
15. heker2025chemoorganoautotrophiclifestyleof pages 2-2
16. prioretti2023carbonfixationin pages 16-17
17. mondal2024aquificaeovercomescompetition pages 26-27
18. cui2023reconfigurationofthe pages 5-6
19. faulkner2023chemoautotrophicproductionof pages 11-13
20. faulkner2023chemoautotrophicproductionof pages 1-2
21. cui2023reconfigurationofthe pages 3-4
22. sokolskyi2023roleofhorizontal pages 18-23
23. 4Fe–4S
24. https://doi.org/10.1038/s41467-023-43960-2
25. https://doi.org/10.1101/2022.10.25.513756
26. https://doi.org/10.3390/life13030627
27. https://doi.org/10.1186/s12866-024-03390-6
28. https://doi.org/10.1038/s42003-025-08172-y
29. https://doi.org/10.1371/journal.pone.0310595
30. https://doi.org/10.1186/s13068-023-02404-1
31. https://doi.org/10.1038/s41467-023-44245-4
32. https://doi.org/10.3390/microorganisms12020391
33. https://doi.org/10.3390/microorganisms12020391,
34. https://doi.org/10.1038/s42003-025-08172-y,
35. https://doi.org/10.1101/2022.10.25.513756,
36. https://doi.org/10.3390/life13030627,
37. https://doi.org/10.1038/s41467-023-43960-2,
38. https://doi.org/10.1371/journal.pone.0310595,
39. https://doi.org/10.1186/s13068-023-02404-1,
40. https://doi.org/10.1038/s41467-023-44245-4,
41. https://doi.org/10.1186/s12866-024-03390-6,