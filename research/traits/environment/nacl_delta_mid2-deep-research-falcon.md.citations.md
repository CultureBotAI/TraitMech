# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** NaCl delta mid2
- **METPO identifier:** METPO:1000481
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A NaCl delta phenotype with a growth-supporting NaCl breadth of approximately 3–8% (w/v), characteristic of organisms with broad salinity tolerance.
- **Parent traits:** METPO:1000335
- **Synonyms:** Nad_3_8
- **Existing evidence:** DOI:10.1093/femsre/fuy009: salinity range (Osmoadaptation review supports broad osmoadaptive breadths as the halotolerant / moderately euryhaline phenotype.)
- **Existing causal graph summary:** nacl_delta_mid2_broad_breadth: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **NaCl delta mid2** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/nacl_delta_mid2.yaml`.

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
**Generated:** 2026-06-17T23:22:45.238619

1. nesrine2020phylogeneticcharacterizationand pages 1-2
2. lichty2024compatiblesolutesare pages 74-78
3. foster2024bacterialcellvolume pages 8-10
4. zou2024metabolicengineeringof pages 1-2
5. khanh2024metabolicpathwayengineering pages 1-2
6. khanh2024metabolicpathwayengineering pages 6-9
7. schiavo2025proposalfornew pages 1-4
8. schiavo2025proposalfornew pages 4-7
9. lichty2024compatiblesolutesare pages 10-14
10. https://doi.org/10.1128/aem.01905-23
11. https://doi.org/10.1128/aem.01195-24
12. https://doi.org/10.1128/mmbr.00181-23
13. https://doi.org/10.1111/mec.16316
14. https://doi.org/10.1093/femsre/fuaf020
15. https://doi.org/10.58088/07hg-r941
16. https://doi.org/10.33865/wjb.005.02.0294
17. https://doi.org/10.33865/wjb.005.02.0294,
18. https://doi.org/10.1111/mec.16316,
19. https://doi.org/10.1128/aem.01905-23,
20. https://doi.org/10.1128/aem.01195-24,
21. https://doi.org/10.1128/mmbr.00181-23,
22. https://doi.org/10.21203/rs.3.rs-8012852/v1,
23. https://doi.org/10.1093/femsre/fuaf020,