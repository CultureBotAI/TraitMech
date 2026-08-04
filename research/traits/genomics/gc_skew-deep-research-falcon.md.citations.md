# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** GC skew
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000097
- **Trait category:** GENOMICS
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A genome-sequence property describing strand asymmetry in guanine versus cytosine content between the leading and lagging replication strands, commonly used to locate the replication origin and terminus.
- **Parent traits:** METPO:1000188
- **Synonyms:** strand compositional asymmetry
- **Existing evidence:** DOI:10.1093/oxfordjournals.molbev.a025626:  (Lobry first described asymmetric substitution patterns between the two DNA strands of bacteria, the basis of GC skew that marks replication boundaries.) | DOI:10.1016/S0378-1119(99)00297-8:  (Frank & Lobry review the mutational and selective mechanisms underlying strand compositional asymmetry.)
- **Existing causal graph summary:** gc_skew_replication_strand_asymmetry: 9 nodes, 8 edges

## Research Objective

Research the microbial trait **GC skew** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/genomics/gc_skew.yaml`.

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
**Generated:** 2026-08-04T04:59:28.615838

1. tillier2000thecontributionsof pages 1-2
2. kono2018acceleratedlaboratoryevolution pages 6-8
3. arakawa2012measuresofcompositional pages 4-5
4. guo2011strandspecificcompositionbias pages 8-11
5. kono2011comprehensivepredictionof pages 1-2
6. tomasch2024ontheevolution pages 1-2
7. sahu2024highnucleotideskew pages 17-18
8. arakawa2012measuresofcompositional pages 1-2
9. arakawa2012measuresofcompositional pages 2-3
10. arakawa2012measuresofcompositional pages 3-4
11. tomasch2024ontheevolution pages 2-5
12. guo2011strandspecificcompositionbias pages 16-18
13. sahu2024highnucleotideskew pages 1-3
14. guo2011strandspecificcompositionbias pages 1-3
15. 10.2174/138920212799034749
16. 10.5772/18554
17. 10.1093/gbe/evy237
18. 10.1007/s002399910029
19. ed
20. 10.1186/1471-2164-12-19
21. 10.1128/mbio.00602-24
22. 10.1007/s00239-024-10202-y
23. 10.1101/gr.5525106
24. 10.1073/pnas.95.7.3720
25. 10.1016/S0378-1119(99)00297-8
26. https://doi.org/10.2174/138920212799034749
27. https://doi.org/10.5772/18554
28. https://doi.org/10.1093/gbe/evy237
29. https://doi.org/10.1007/s002399910029
30. https://doi.org/10.1186/1471-2164-12-19
31. https://doi.org/10.1128/mbio.00602-24
32. https://doi.org/10.1007/s00239-024-10202-y
33. https://doi.org/10.1101/gr.5525106
34. https://doi.org/10.1073/pnas.95.7.3720
35. https://doi.org/10.1016/S0378-1119(99
36. https://doi.org/10.1007/s002399910029,
37. https://doi.org/10.2174/138920212799034749,
38. https://doi.org/10.1128/mbio.00602-24,
39. https://doi.org/10.5772/18554,
40. https://doi.org/10.1007/s00239-024-10202-y,
41. https://doi.org/10.1093/gbe/evy237,
42. https://doi.org/10.1186/1471-2164-12-19,