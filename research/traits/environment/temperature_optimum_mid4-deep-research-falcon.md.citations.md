# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid4
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000446
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 34 and 40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 34–40 °C optimum as the warm-mesophile (mammalian-host) setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid4_warm_mesophile: 15 nodes, 11 edges

## Research Objective

Research the microbial trait **temperature optimum mid4** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid4.yaml`.

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
**Generated:** 2026-08-04T04:15:13.223430

1. engqvist2018correlatingenzymeannotations pages 1-2
2. blaby2012experimentalevolutionof pages 1-2
3. berdejo2024evolutionarytradeoffbetween pages 1-2
4. blaby2012experimentalevolutionof pages 7-8
5. murata2011molecularstrategyfor pages 1-2
6. charoensuk2017thermotolerantgenesessential pages 1-2
7. murata2011molecularstrategyfor pages 6-7
8. moon2023temperaturemattersbacterial pages 3-5
9. hoogerland2024atemperaturesensitivemetabolic pages 1-2
10. hoogerland2024atemperaturesensitivemetabolic pages 3-4
11. siliakus2017adaptationsofarchaeal pages 8-10
12. yared2024beyondtheanticodon pages 1-2
13. barnum2024predictingmicrobialgrowth pages 1-3
14. shen2024genomicbasisof pages 1-2
15. mcguire2023wholegenomesequencinganalysis pages 1-2
16. fabA mutant
17. wild type
18. https://doi.org/10.1128/aem.05773-11
19. https://doi.org/10.1038/s41467-024-53677-5
20. https://doi.org/10.1128/mbio.03105-23
21. https://doi.org/10.1007/s12275-023-00031-x
22. https://doi.org/10.1371/journal.pone.0020063
23. https://doi.org/10.1186/s13068-017-0891-0
24. https://doi.org/10.1186/s12866-018-1320-7
25. https://doi.org/10.3390/genes15030374
26. https://doi.org/10.1007/s00792-017-0939-x
27. https://doi.org/10.3389/fmicb.2023.1265216
28. https://doi.org/10.1101/2024.03.22.586313
29. https://doi.org/10.1093/ismejo/wrad020
30. https://doi.org/10.1186/s12864-023-09266-9
31. https://doi.org/10.1186/s12866-018-1320-7,
32. https://doi.org/10.1128/aem.05773-11,
33. https://doi.org/10.1371/journal.pone.0020063,
34. https://doi.org/10.1007/s12275-023-00031-x,
35. https://doi.org/10.1038/s41467-024-53677-5,
36. https://doi.org/10.1007/s00792-017-0939-x,
37. https://doi.org/10.1128/mbio.03105-23,
38. https://doi.org/10.1186/s13068-017-0891-0,
39. https://doi.org/10.3390/genes15030374,
40. https://doi.org/10.1101/2024.03.22.586313,
41. https://doi.org/10.1093/ismejo/wrad020,
42. https://doi.org/10.1186/s12864-023-09266-9,