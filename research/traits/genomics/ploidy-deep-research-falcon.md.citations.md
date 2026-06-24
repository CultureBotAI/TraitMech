# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** ploidy
- **METPO identifier:** traitmech:000100
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genomics trait describing the number of complete genome copies per cell; many bacteria and archaea are polyploid, maintaining many chromosome copies that support survival, repair, and large cell size.
- **Parent traits:** METPO:1000188
- **Synonyms:** polyploidy
- **Existing evidence:** DOI:10.1159/000368855:  (Soppa reviews polyploidy in archaea and bacteria and its links to desiccation resistance, giant cell size, and long-term survival.) | DOI:10.1073/pnas.0707522105:  (Mendell et al. document extreme polyploidy (tens of thousands of genome copies) in the large bacterium Epulopiscium.)
- **Existing causal graph summary:** ploidy_repair_survival: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **ploidy** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/ploidy.yaml`.

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
**Generated:** 2026-06-18T03:49:11.092833

1. bruck2023ploidyinvibrio pages 1-2
2. garona2023segregationaldrifthinders pages 2-3
3. bruck2023oneadvantageof pages 15-16
4. mendell2008extremepolyploidyin pages 2-4
5. bruck2023oneadvantageof pages 13-15
6. ozer2024intermoleculargeneconversion pages 1-2
7. garona2023segregationaldrifthinders pages 1-2
8. sakamaki2023characterizationofa pages 1-2
9. kamoku2024deliveryofnovel pages 1-5
10. misra2023effectivegenesilencing pages 1-2
11. bruck2023oneadvantageof pages 10-13
12. ozer2024intermoleculargeneconversion pages 16-17
13. bruck2023oneadvantageof pages 1-2
14. ionescu2023genomicmysteriesof pages 6-7
15. ionescu2023genomicmysteriesof pages 8-8
16. ozer2024intermoleculargeneconversion pages 17-18
17. bruck2023oneadvantageof pages 16-18
18. https://doi.org/10.3390/microorganisms11092267
19. https://doi.org/10.3390/genes15070861
20. https://doi.org/10.1371/journal.pgen.1010829
21. https://doi.org/10.3389/fmicb.2023.1111979;
22. https://doi.org/10.1101/2024.07.31.606084
23. https://doi.org/10.1101/2024.07.31.606084;
24. https://doi.org/10.3389/fmicb.2023.1111979
25. https://doi.org/10.1093/gbe/evad163;
26. https://doi.org/10.1073/pnas.0707522105
27. https://doi.org/10.3390/genes14071437
28. https://doi.org/10.1128/spectrum.05204-22
29. https://doi.org/10.1093/gbe/evad163
30. https://doi.org/10.3390/microorganisms11092267,
31. https://doi.org/10.3390/genes14071437,
32. https://doi.org/10.1371/journal.pgen.1010829,
33. https://doi.org/10.1073/pnas.0707522105,
34. https://doi.org/10.3390/genes15070861,
35. https://doi.org/10.3389/fmicb.2023.1111979,
36. https://doi.org/10.1101/2024.07.31.606084,
37. https://doi.org/10.1093/gbe/evad163,
38. https://doi.org/10.1128/spectrum.05204-22,