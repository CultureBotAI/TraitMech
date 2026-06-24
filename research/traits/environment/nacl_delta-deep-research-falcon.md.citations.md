# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta
- **METPO identifier:** METPO:1000335
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A salinity phenotype with numerical limits expressing the breadth (maximum minus minimum) of NaCl concentrations supporting growth of an organism.
- **Parent traits:** METPO:1000532, METPO:1000534
- **Synonyms:** 
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports the span of NaCl-tolerance as a halophily descriptor; its breadth (delta) reflects euryhaline versus stenohaline physiology.) | DOI:10.1186/1746-1448-4-2: cope with the high salt concentrations (Saline-Systems review supports broad osmoadaptive capacity as the basis of a wide NaCl-delta phenotype.)
- **Existing causal graph summary:** nacl_delta_euryhaline_breadth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **NaCl delta** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta.yaml`.

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
**Generated:** 2026-06-17T23:07:10.429476

1. van2009productionofpoly pages 13-16
2. najjari2023physiologicalandgenomic pages 1-2
3. bonnaud2024haloarchaeaaspromising pages 2-4
4. foster2024bacterialcellvolume pages 6-8
5. zeaiter2019phenomicsandgenomics pages 1-2
6. fan2024improvementinsalt pages 1-2
7. foster2024bacterialcellvolume pages 1-2
8. thompson2024themicrobiomeof pages 5-6
9. galisteo2024thehypersalinesoils pages 19-20
10. fan2024improvementinsalt pages 12-14
11. fan2024improvementinsalt pages 2-3
12. fan2024improvementinsalt pages 8-10
13. fan2024improvementinsalt pages 10-12
14. https://doi.org/10.1128/MMBR.00181-23
15. https://doi.org/10.3390/biology13060404
16. https://doi.org/10.1007/s10709-023-00182-0;
17. https://doi.org/10.3390/microorganisms12071473
18. https://doi.org/10.3389/fmicb.2023.1192059;
19. https://doi.org/10.3389/fmicb.2019.02811;
20. https://doi.org/10.3390/microorganisms12081738;
21. https://doi.org/10.1007/s10709-023-00182-0
22. https://doi.org/10.3389/fmicb.2019.01304
23. https://doi.org/10.3389/frmbi.2023.1329925
24. https://doi.org/10.3389/fmicb.2023.1192059
25. https://doi.org/10.1111/mec.16316
26. https://doi.org/10.1128/mmbr.00181-23
27. https://doi.org/10.3390/microorganisms12081738
28. https://doi.org/10.3390/microorganisms12020375
29. https://doi.org/10.3389/fmicb.2019.02811
30. https://doi.org/10.1111/mec.16316,
31. https://doi.org/10.1007/s10709-023-00182-0,
32. https://doi.org/10.3390/microorganisms12081738,
33. https://doi.org/10.3389/fmicb.2019.01304,
34. https://doi.org/10.1128/mmbr.00181-23,
35. https://doi.org/10.3390/biology13060404,
36. https://doi.org/10.3390/microorganisms12071473,
37. https://doi.org/10.3390/microorganisms12020375,