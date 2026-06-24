# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid4
- **METPO identifier:** METPO:1000446
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 34 and 40 °C, characteristic of warm-mesophilic physiology (including many mammalian host-associated bacteria).
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_34_to_40
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports a 34–40 °C optimum as the warm-mesophile (mammalian-host) setpoint.)
- **Existing causal graph summary:** temperature_optimum_mid4_warm_mesophile: 4 nodes, 3 edges

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
**Generated:** 2026-06-18T02:38:28.445319

1. moon2023temperaturemattersbacterial pages 1-3
2. lehmann2023adaptivelaboratoryevolution pages 1-2
3. takemata2024howdothermophiles pages 1-2
4. mendoza2014temperaturesensingby pages 1-2
5. moon2023temperaturemattersbacterial pages 3-5
6. park2024unveilingthenovel pages 1-2
7. dessenne2024lipidomicanalysesreveal pages 2-4
8. lehmann2023adaptivelaboratoryevolution pages 6-7
9. moon2023temperaturemattersbacterial pages 14-15
10. viuda2025physicalcommunicationpathways pages 5-7
11. park2024unveilingthenovel pages 4-5
12. park2024unveilingthenovel pages 2-4
13. arsh2025effectsofcooling pages 28-32
14. dessenne2024lipidomicanalysesreveal pages 1-2
15. takemata2024howdothermophiles pages 2-3
16. ATP
17. ADP
18. https://doi.org/10.1146/annurev-micro-091313-103612
19. https://doi.org/10.1007/s12275-023-00031-x
20. https://doi.org/10.1128/spectrum.00757-24
21. https://doi.org/10.1007/s12275-023-00031-x;
22. https://doi.org/10.1371/journal.pgen.1011464
23. https://doi.org/10.3389/fmicb.2023.1265216
24. https://doi.org/10.1264/jsme2.me23087
25. https://doi.org/10.1007/s12275-023-00031-x,
26. https://doi.org/10.3389/fmicb.2023.1265216,
27. https://doi.org/10.1264/jsme2.me23087,
28. https://doi.org/10.1146/annurev-micro-091313-103612,
29. https://doi.org/10.1128/spectrum.00757-24,
30. https://doi.org/10.1371/journal.pgen.1011464,
31. https://doi.org/10.1007/s12551-025-01290-1,
32. https://doi.org/10.1128/mmbr.00153-25,