# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** endosymbiosis
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000045
- **Trait category:** ECOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A symbiosis in which the microorganism lives inside the cells or tissues of its host. Obligate intracellular endosymbionts (e.g. of insects) frequently undergo extreme genome reduction.
- **Parent traits:** traitmech:000040
- **Synonyms:** endosymbiont
- **Existing evidence:** DOI:10.1038/nrmicro2670:  (McCutcheon & Moran, "Extreme genome reduction in symbiotic bacteria", characterize intracellular endosymbionts and their diminished genomes.) | DOI:10.1038/nrmicro.2017.171:  (Poole et al. describe rhizobia as plant-cell endosymbionts within root nodules, an example of the endosymbiotic lifestyle.)
- **Existing causal graph summary:** endosymbiosis_intracellular_genome_reduction: 10 nodes, 7 edges

## Research Objective

Research the microbial trait **endosymbiosis** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/ecology/endosymbiosis.yaml`.

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
**Generated:** 2026-08-04T14:55:38.832362

1. wierz2024intracellularsymbiontsymbiodolus pages 1-2
2. boyd2024stochasticitydeterminismand pages 1-2
3. duncan2023cooptionofa pages 8-9
4. cai2024expressionandmutagenesis pages 1-2
5. porter2024hostimposedcontrolmechanisms pages 3-4
6. porter2024hostimposedcontrolmechanisms pages 7-8
7. ferrarini2023coordinationofhost pages 13-14
8. ferrarini2023coordinationofhost pages 8-10
9. ling2024acompletedna pages 9-10
10. wang2024decipheringdeepseachemosynthetic pages 1-2
11. wang2024decipheringdeepseachemosynthetic pages 10-12
12. porter2024hostimposedcontrolmechanisms pages 1-3
13. cai2024expressionandmutagenesis pages 13-15
14. silva2024comparativetranscriptomicsof pages 1-2
15. ferrarini2023coordinationofhost pages 1-3
16. cai2024expressionandmutagenesis pages 8-10
17. silva2024comparativetranscriptomicsof pages 21-22
18. boyd2024stochasticitydeterminismand pages 9-10
19. silva2024comparativetranscriptomicsof pages 14-15
20. porter2024hostimposedcontrolmechanisms pages 5-6
21. 10.1073/pnas.2308448120
22. 10.3389/fpls.2023.1306491
23. 10.1038/s41564-024-01762-2
24. 10.1186/s40168-023-01714-8
25. 10.1073/pnas.2415651121
26. d
27. 10.1038/s41467-024-48784-2
28. 10.1093/ismejo/wrae099
29. 10.7554/eLife.88294
30. 10.3390/ijms25084228
31. 10.1038/nrmicro2670
32. 10.1038/nrmicro.2017.171
33. https://doi.org/10.1073/pnas.2308448120
34. https://doi.org/10.3389/fpls.2023.1306491
35. https://doi.org/10.1038/s41564-024-01762-2
36. https://doi.org/10.1186/s40168-023-01714-8
37. https://doi.org/10.1073/pnas.2415651121
38. https://doi.org/10.1038/s41467-024-48784-2
39. https://doi.org/10.1093/ismejo/wrae099
40. https://doi.org/10.7554/eLife.88294
41. https://doi.org/10.3390/ijms25084228
42. https://doi.org/10.1038/nrmicro2670
43. https://doi.org/10.1038/nrmicro.2017.171
44. https://doi.org/10.1093/ismejo/wrae099,
45. https://doi.org/10.1038/s41467-024-48784-2,
46. https://doi.org/10.1073/pnas.2308448120,
47. https://doi.org/10.3389/fpls.2023.1306491,
48. https://doi.org/10.1038/s41564-024-01762-2,
49. https://doi.org/10.1186/s40168-023-01714-8,
50. https://doi.org/10.1073/pnas.2415651121,
51. https://doi.org/10.7554/elife.88294,
52. https://doi.org/10.3390/ijms25084228,