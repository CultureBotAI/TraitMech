# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** obligately alkaphilic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1003004
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH growth preference in which an organism requires alkaline conditions (typically pH above 8.5) for growth and cannot grow at neutral or acidic pH.
- **Parent traits:** METPO:1003000
- **Synonyms:** obligate alkaliphile, obligate alkaphilic, obligately alkaliphilic
- **Existing evidence:** DOI:10.3389/fbioe.2015.00075: grow only at pH values of ~pH 9 and above (Supports the obligate alkaliphile definition.)
- **Existing causal graph summary:** obligately_alkaphilic_sodium_cycle_homeostasis: 14 nodes, 13 edges

## Research Objective

Research the microbial trait **obligately alkaphilic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/obligately_alkaphilic.yaml`.

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
**Generated:** 2026-08-04T02:14:33.815495

1. preiss2015alkaliphilicbacteriawith pages 4-5
2. goto2022differencesinbioenergetic pages 2-3
3. khomyakova2023phenotypicandgenomic pages 2-3
4. khomyakova2023phenotypicandgenomic pages 10-11
5. goto2022differencesinbioenergetic pages 1-2
6. takahashi2018ahydrophobicsmall pages 9-12
7. takahashi2018ahydrophobicsmall pages 7-9
8. jong2024quantitativeproteomicsreveals pages 6-8
9. preiss2015alkaliphilicbacteriawith pages 12-13
10. jong2024quantitativeproteomicsreveals pages 1-2
11. takahashi2018ahydrophobicsmall pages 1-2
12. horikoshi1999alkaliphilessomeapplications pages 4-5
13. takahashi2018ahydrophobicsmall pages 2-4
14. 10.3389/fbioe.2015.00075
15. 10.3389/fmicb.2022.842785
16. s
17. 10.3389/fmicb.2018.01994
18. 10.3389/fmicb.2024.1468929
19. 10.3389/fmicb.2023.1233691
20. 10.1128/MMBR.63.4.735-750.1999
21. https://doi.org/10.3389/fbioe.2015.00075
22. https://doi.org/10.3389/fmicb.2022.842785
23. https://doi.org/10.3389/fmicb.2018.01994
24. https://doi.org/10.3389/fmicb.2024.1468929
25. https://doi.org/10.3389/fmicb.2023.1233691
26. https://doi.org/10.1128/MMBR.63.4.735-750.1999
27. https://doi.org/10.3389/fbioe.2015.00075,
28. https://doi.org/10.3389/fmicb.2022.842785,
29. https://doi.org/10.3389/fmicb.2023.1233691,
30. https://doi.org/10.3389/fmicb.2024.1468929,
31. https://doi.org/10.1128/mmbr.63.4.735-750.1999,
32. https://doi.org/10.3389/fmicb.2018.01994,