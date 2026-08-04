# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** prophage
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000091
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of an integrated (or extrachromosomal) temperate bacteriophage genome (a prophage) maintained in the host during lysogeny, often contributing genes that alter host phenotype.
- **Parent traits:** traitmech:000089
- **Synonyms:** lysogen
- **Existing evidence:** DOI:10.1128/MMBR.67.2.238-276.2003:  (Canchaya et al. review prophage genomics, showing most sequenced bacterial genomes carry prophage sequences.) | DOI:10.1038/ismej.2017.16:  (Howard-Varona et al. review lysogeny in nature, the maintenance of temperate phage genomes within hosts.)
- **Existing causal graph summary:** prophage_lysogeny: 13 nodes, 9 edges

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
**Generated:** 2026-08-04T05:23:39.190794

1. vale2024genecontentphage pages 1-2
2. tommasini2023helperembeddedsatellitesfrom pages 1-2
3. kang2017prophagegenomicsreveals pages 4-7
4. owen2020awindowinto pages 1-2
5. wang2010crypticprophageshelp pages 1-2
6. pei2024auniverseof pages 13-15
7. thabet2023theclpxprotease pages 10-11
8. thabet2023theclpxprotease pages 11-12
9. vale2024genecontentphage pages 8-9
10. thabet2023theclpxprotease pages 6-8
11. thabet2023theclpxprotease pages 3-4
12. tenoriocarnalla2024hostpopulationstructure pages 1-2
13. pei2024auniverseof pages 1-2
14. bobay2014pervasivedomesticationof pages 1-2
15. thabet2023theclpxprotease pages 8-8
16. owen2020awindowinto pages 9-11
17. wang2010crypticprophageshelp pages 2-3
18. kang2017prophagegenomicsreveals pages 1-4
19. kang2017prophagegenomicsreveals pages 7-10
20. relatives
21. 10.1038/s41467-023-42413-0
22. 10.1080/19490976.2024.2379440
23. 10.1080/19490976.2024.2309684
24. 10.1128/mbio.02377-24
25. 10.1093/nargab/lqad036
26. 10.1099/mgen.0.000330
27. 10.1038/ncomms1146
28. 10.1073/pnas.1405336111
29. 10.1101/114819
30. https://doi.org/10.1038/s41467-023-42413-0
31. https://doi.org/10.1080/19490976.2024.2379440
32. https://doi.org/10.1080/19490976.2024.2309684
33. https://doi.org/10.1128/mbio.02377-24
34. https://doi.org/10.1093/nargab/lqad036
35. https://doi.org/10.1099/mgen.0.000330
36. https://doi.org/10.1038/ncomms1146
37. https://doi.org/10.1073/pnas.1405336111
38. https://doi.org/10.1101/114819
39. https://doi.org/10.1038/s41467-023-42413-0,
40. https://doi.org/10.1080/19490976.2024.2309684,
41. https://doi.org/10.1080/19490976.2024.2379440,
42. https://doi.org/10.1099/mgen.0.000330,
43. https://doi.org/10.1073/pnas.1405336111,
44. https://doi.org/10.1093/nargab/lqad036,
45. https://doi.org/10.1101/114819,
46. https://doi.org/10.1038/ncomms1146,
47. https://doi.org/10.1128/mbio.02377-24,