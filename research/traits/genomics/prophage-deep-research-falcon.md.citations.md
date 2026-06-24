# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** prophage
- **METPO identifier:** traitmech:000091
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of an integrated (or extrachromosomal) temperate bacteriophage genome (a prophage) maintained in the host during lysogeny, often contributing genes that alter host phenotype.
- **Parent traits:** traitmech:000089
- **Synonyms:** lysogen
- **Existing evidence:** DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.) | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature, the maintenance of temperate phage genomes within hosts.)
- **Existing causal graph summary:** prophage_lysogeny: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **prophage** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/prophage.yaml`.

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
**Generated:** 2026-06-18T03:52:33.751363

1. silpe2023smallproteinmodules pages 1-2
2. sass2024thednadamage pages 2-3
3. sweet2023exposureofshewanella pages 2-4
4. herediaponce2023genotoxicstressstimulates pages 1-2
5. liao2024prophageencodedantibioticresistance pages 1-2
6. pfeifer2024phageplasmidspromoterecombination pages 1-2
7. tenoriocarnalla2024hostpopulationstructure pages 2-5
8. sass2024thednadamage pages 6-7
9. thabet2023theclpxprotease pages 1-2
10. thabet2023theclpxprotease pages 10-11
11. thabet2023theclpxprotease pages 5-6
12. mahmud2024roleofbacteriophages pages 4-5
13. tenoriocarnalla2024hostpopulationstructure pages 7-11
14. bucher2024subtherapeuticconcentrationsof pages 9-11
15. nair2024presenceofphageplasmids pages 1-2
16. tenoriocarnalla2024hostpopulationstructure pages 5-7
17. thabet2023theclpxprotease pages 2-3
18. pfeifer2024phageplasmidspromoterecombination pages 9-10
19. tenoriocarnalla2024hostpopulationstructure pages 1-2
20. https://doi.org/10.1038/s41586-023-06376-y
21. https://doi.org/10.1038/s41522-023-00464-7
22. https://doi.org/10.1073/pnas.2407832121
23. https://doi.org/10.1038/s41467-024-45757-3
24. https://doi.org/10.1128/aem.01716-22
25. https://doi.org/10.1038/s41467-023-42413-0
26. https://doi.org/10.1128/jb.00191-23
27. https://doi.org/10.1080/19490976.2024.2390720
28. https://doi.org/10.3389/fmicb.2024.1374708
29. https://doi.org/10.1101/2024.11.20.624585
30. https://doi.org/10.1038/s41467-024-52450-y
31. https://doi.org/10.3390/v16091348
32. https://doi.org/10.1128/mbio.02377-24
33. https://doi.org/10.1099/mgen.0.001247
34. https://doi.org/10.1038/s41586-023-06376-y,
35. https://doi.org/10.1038/s41467-024-45757-3,
36. https://doi.org/10.1099/mgen.0.001247,
37. https://doi.org/10.1073/pnas.2407832121,
38. https://doi.org/10.1128/aem.01716-22,
39. https://doi.org/10.1038/s41522-023-00464-7,
40. https://doi.org/10.1038/s41467-023-42413-0,
41. https://doi.org/10.1128/jb.00191-23,
42. https://doi.org/10.1038/s41467-024-52450-y,
43. https://doi.org/10.1128/mbio.02377-24,
44. https://doi.org/10.1080/19490976.2024.2390720,
45. https://doi.org/10.1101/2024.11.20.624585,