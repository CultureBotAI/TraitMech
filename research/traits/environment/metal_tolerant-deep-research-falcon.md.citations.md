# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** metal tolerant
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000012
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An environmental tolerance in which an organism grows in the presence of elevated concentrations of toxic heavy-metal or metalloid ions, typically via efflux-based resistance determinants (RND-family CBA pumps, P-type ATPases, and cation diffusion facilitators).
- **Parent traits:** METPO:1000059
- **Synonyms:** metallophilic, heavy metal resistant
- **Existing evidence:** PMID:12829273: CBA efflux pumps driven by proteins of the resistance-nodulation-cell division superfamily, P-type ATPases, cation diffusion facilitator and chromate proteins (Review of efflux-mediated heavy-metal resistance supports active metal export as the dominant prokaryotic tolerance mechanism.) | DOI:10.3389/fmicb.2020.00047: This metallophilic strain BS1, harbors numerous gene clusters encoding metal-resistance determinants enabling detoxification of transition metal ions and complexes (Organism example: Cupriavidus metallidurans is the model metallophilic bacterium tolerating many toxic metals via dedicated resistance gene clusters.)
- **Existing causal graph summary:** metal_tolerance_efflux_detoxification: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **metal tolerant** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/metal_tolerant.yaml`.

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
**Generated:** 2026-08-04T01:17:15.844463

1. elbeltagi2024draftgenomeanalysis pages 1-2
2. xie2023wholegenomesequence pages 1-2
3. legatzki2003interplayofthe pages 1-2
4. herreracalderon2024metagenomicandgenomic pages 1-2
5. schulz2021behindtheshield pages 1-2
6. hoque2024arsenotrophicachromobacteraegrifaciens pages 1-2
7. shafiq2024mechanismsoftoxicity pages 9-10
8. ramnarine2024earlytranscriptionalchanges pages 1-2
9. nies2024aflowequilibrium pages 1-3
10. nies2024aflowequilibrium pages 20-22
11. galea2024linkingthetranscriptome pages 4-5
12. hovorukha2024metalresistanceof pages 2-3
13. vaccaro2016novelmetalcation pages 1-2
14. nies2024aflowequilibrium pages 15-19
15. galea2024linkingthetranscriptome pages 1-2
16. https://doi.org/10.1128/JB.00052-21
17. https://doi.org/10.1128/JB.00052-21;
18. https://doi.org/10.1128/JB.185.15.4354-4361.2003
19. https://doi.org/10.1128/JB.185.15.4354-4361.2003;
20. https://doi.org/10.1128/JB.00080-24
21. https://doi.org/10.1186/s12866-024-03676-9
22. https://doi.org/10.52700/jmmg.v5i1.155
23. https://doi.org/10.1186/s12866-024-03206-7
24. https://doi.org/10.1186/s12866-024-03676-9;
25. https://doi.org/10.1128/jb.00080-24
26. https://doi.org/10.1093/mtomcs/mfae058
27. https://doi.org/10.3389/fbioe.2023.1335854
28. https://doi.org/10.1007/s11356-023-30253-w
29. https://doi.org/10.3390/microorganisms11061518
30. https://doi.org/10.3390/su16229655
31. https://doi.org/10.1128/AEM.01845-16
32. https://doi.org/10.3390/su16229655,
33. https://doi.org/10.1007/s11356-023-30253-w,
34. https://doi.org/10.3389/fbioe.2023.1335854,
35. https://doi.org/10.3390/microorganisms11061518,
36. https://doi.org/10.1128/jb.00080-24,
37. https://doi.org/10.1128/jb.00052-21,
38. https://doi.org/10.1128/jb.185.15.4354-4361.2003,
39. https://doi.org/10.1186/s12866-024-03676-9,
40. https://doi.org/10.52700/jmmg.v5i1.155,
41. https://doi.org/10.1186/s12866-024-03206-7,
42. https://doi.org/10.1093/mtomcs/mfae058,
43. https://doi.org/10.1128/aem.01845-16,