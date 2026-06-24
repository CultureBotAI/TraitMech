# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature range mid3
- **METPO identifier:** METPO:1000452
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature range phenotype in which the growth-supporting ambient temperature range spans approximately 30–34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000306
- **Synonyms:** Mesophilie, TR_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C range as the upper-mesophile growth range.)
- **Existing causal graph summary:** temperature_range_mid3_upper_mesophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **temperature range mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_range_mid3.yaml`.

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
**Generated:** 2026-06-18T02:55:18.094540

1. ramon2023ageneraloverview pages 1-2
2. engqvist2018correlatingenzymeannotations pages 1-2
3. sidarta2024lipidphaseseparation pages 1-2
4. ramon2023ageneraloverview pages 2-4
5. ramon2023ageneraloverview pages 4-5
6. purwar2024adaptationsofpsychrophilic pages 6-7
7. sidarta2024lipidphaseseparation pages 2-5
8. mansilla2025fattyacidsynthesis pages 15-17
9. lehmann2023adaptivelaboratoryevolution pages 6-7
10. sidarta2024lipidphaseseparation pages 12-14
11. rekadwad2023extremophilesthespecies pages 2-4
12. s
13. https://doi.org/10.1128/spectrum.03925-23;
14. https://doi.org/10.1128/mmbr.00069-23;
15. https://doi.org/10.1007/s42770-023-01057-4;
16. https://doi.org/10.37256/amtt.5220244537;
17. https://doi.org/10.3389/fmicb.2023.1265216;
18. https://doi.org/10.1186/s12866-018-1320-7;
19. https://doi.org/10.1128/spectrum.03925-23
20. https://doi.org/10.1007/s42770-023-01057-4
21. https://doi.org/10.37256/amtt.5220244537
22. https://doi.org/10.3389/fmicb.2023.1265216
23. https://doi.org/10.1186/s12866-018-1320-7
24. https://doi.org/10.1007/s13205-023-03733-6
25. https://doi.org/10.1007/s42770-023-01057-4,
26. https://doi.org/10.1186/s12866-018-1320-7,
27. https://doi.org/10.1007/s13205-023-03733-6,
28. https://doi.org/10.1128/spectrum.03925-23,
29. https://doi.org/10.1128/mmbr.00069-23,
30. https://doi.org/10.37256/amtt.5220244537,
31. https://doi.org/10.3389/fmicb.2023.1265216,