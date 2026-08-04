# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** genomic island
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000093
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing possession of a genomic island — a horizontally acquired chromosomal region (e.g. a pathogenicity, symbiosis, or metabolic island) that often retains mobility signatures such as flanking repeats and atypical nucleotide composition.
- **Parent traits:** traitmech:000089
- **Synonyms:** pathogenicity island
- **Existing evidence:** DOI:10.1038/nrmicro884:  (Dobrindt et al. review genomic islands in pathogenic and environmental microorganisms.) | DOI:10.1111/j.1574-6976.2008.00136.x:  (Juhas et al. review genomic islands as tools of bacterial horizontal gene transfer and evolution.)
- **Existing causal graph summary:** gi_hgt_accessory_function: 8 nodes, 6 edges

## Research Objective

Research the microbial trait **genomic island** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/genomic_island.yaml`.

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
**Generated:** 2026-08-04T05:14:49.065041

1. watanabe2025theroleof pages 1-2
2. chai2025comprehensiveprofilingof pages 10-13
3. benevides2024genomicfeaturesand pages 1-2
4. vladimirova2024hotspotsof pages 1-2
5. matsumoto2024evolutionofthe pages 9-13
6. watanabe2025theroleof pages 12-13
7. zhu2024thecaddxoperon pages 1-2
8. watanabe2025theroleof pages 13-15
9. watanabe2025theroleof pages 11-12
10. matsumoto2024evolutionofthe pages 1-3
11. lechner2009genomicislandexcisions pages 1-2
12. zhu2024thecaddxoperon pages 9-13
13. elsen2024crossregulationandcrosstalk pages 1-2
14. mageeney2020newcandidatesfor pages 12-13
15. beavogui2024thedefensomeof pages 8-9
16. watanabe2025theroleof pages 15-17
17. lyu2024theintricaterelationship pages 4-6
18. vladimirova2024hotspotsof pages 20-21
19. beavogui2024thedefensomeof pages 1-2
20. elsen2024crossregulationandcrosstalk pages 13-14
21. ramesh2024genomesequencingand pages 1-2
22. https://doi.org/10.3390/microorganisms13081803,
23. https://doi.org/10.1093/nargab/lqaf083,
24. https://doi.org/10.1128/spectrum.00607-24,
25. https://doi.org/10.7554/elife.91985.3,
26. https://doi.org/10.3390/microorganisms12020312,
27. https://doi.org/10.3390/ijms251910421,
28. https://doi.org/10.1038/s41467-024-46489-0,
29. https://doi.org/10.1093/nar/gkaa156,
30. https://doi.org/10.1371/journal.pgen.1011325,
31. https://doi.org/10.1186/s13567-024-01371-1,
32. https://doi.org/10.1186/1471-2180-9-141,
33. https://doi.org/10.1038/s41598-024-80533-9,