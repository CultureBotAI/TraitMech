# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carboxydotrophic
- **METPO identifier:** METPO:1000633
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism derives energy from the oxidation of carbon monoxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.) | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase (Review supports CODH and CO-insensitive respiratory-chain features in aerobic carboxydotrophs.)
- **Existing causal graph summary:** carboxydotrophic_co_oxidation: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **carboxydotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/carboxydotrophic.yaml`.

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
**Generated:** 2026-06-18T10:44:07.783244

1. dent2023carbonmonoxidesensingtranscription pages 1-3
2. dent2023carbonmonoxidesensingtranscription pages 3-5
3. katayama2024phylogeneticdiversityofa pages 1-2
4. dent2023carbonmonoxidesensingtranscription pages 7-9
5. williams2024novelendolithicbacteria pages 1-2
6. bahrle2023currentstatusof pages 4-5
7. bahrle2023currentstatusof pages 5-8
8. leung2024tracegasoxidation pages 1-2
9. imaura2023isolationgenomicsequence pages 2-4
10. bahrle2023currentstatusof pages 8-9
11. imaura2023isolationgenomicsequence pages 9-11
12. imaura2023isolationgenomicsequence pages 7-9
13. imaura2023isolationandgenomic pages 1-4
14. dent2023carbonmonoxidesensingtranscription pages 11-13
15. katayama2024phylogeneticdiversityof pages 1-7
16. dent2023carbonmonoxidesensingtranscription pages 9-11
17. leung2024tracegasoxidation pages 2-3
18. https://doi.org/10.1128/jb.00332-22
19. https://doi.org/10.1186/s40643-023-00705-9
20. https://doi.org/10.1101/2023.01.17.524042
21. https://doi.org/10.1128/aem.00185-23
22. https://doi.org/10.1038/s41467-024-47324-2
23. https://doi.org/10.1128/aem.02264-23
24. https://doi.org/10.1099/mgen.0.001285
25. https://doi.org/10.1101/2023.10.23.563559
26. https://doi.org/10.1128/jb.00332-22,
27. https://doi.org/10.1038/s41467-024-47324-2,
28. https://doi.org/10.1101/2023.01.17.524042,
29. https://doi.org/10.1186/s40643-023-00705-9,
30. https://doi.org/10.1128/aem.00185-23,
31. https://doi.org/10.1099/mgen.0.001285,
32. https://doi.org/10.1128/aem.02264-23,
33. https://doi.org/10.1101/2023.10.23.563559,