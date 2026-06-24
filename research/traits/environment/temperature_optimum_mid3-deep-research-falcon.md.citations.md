# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** temperature optimum mid3
- **METPO identifier:** METPO:1000445
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A temperature optimum phenotype with the best-growth ambient temperature between approximately 30 and 34 °C, characteristic of mesophilic physiology.
- **Parent traits:** METPO:1000304
- **Synonyms:** Mesophilie, TO_30_to_34
- **Existing evidence:** DOI:10.1146/annurev-micro-091313-103612: more unsaturated fatty acids (Membrane-adaptation review supports the 30–34 °C optimum as a typical mesophile setpoint near common host body temperatures.)
- **Existing causal graph summary:** temperature_optimum_mid3_upper_mesophile: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **temperature optimum mid3** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/temperature_optimum_mid3.yaml`.

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
**Generated:** 2026-06-18T02:16:58.005143

1. lehmann2023adaptivelaboratoryevolution pages 1-2
2. ramon2023ageneraloverview pages 1-2
3. moon2023temperaturemattersbacterial pages 1-3
4. ramon2023ageneraloverview pages 2-4
5. sidarta2024lipidphaseseparation pages 1-2
6. sidarta2024lipidphaseseparation pages 12-14
7. moon2023temperaturemattersbacterial pages 5-6
8. dessenne2024lipidomicanalysesreveal pages 1-2
9. liang2023developmentofheatshock pages 1-2
10. purwar2024adaptationsofpsychrophilic pages 7-8
11. sidarta2024lipidphaseseparation pages 2-5
12. hellequin2023membranelipidadaptation pages 1-2
13. wu2023molecularmechanismsof pages 3-5
14. moon2023temperaturemattersbacterial pages 3-5
15. https://doi.org/10.3389/fmicb.2023.1265216
16. https://doi.org/10.1128/spectrum.03925-23
17. https://doi.org/10.1007/s42770-023-01057-4
18. https://doi.org/10.1111/mmi.15323
19. https://doi.org/10.3389/fmicb.2023.1032032
20. https://doi.org/10.3390/cells12101353
21. https://doi.org/10.37256/amtt.5220244537
22. https://doi.org/10.1007/s12275-023-00031-x
23. https://doi.org/10.1128/aem.00666-23
24. https://doi.org/10.1128/spectrum.00757-24
25. https://doi.org/10.3389/fmicb.2023.1265216,
26. https://doi.org/10.1007/s42770-023-01057-4,
27. https://doi.org/10.1007/s12275-023-00031-x,
28. https://doi.org/10.1128/aem.00666-23,
29. https://doi.org/10.1128/spectrum.03925-23,
30. https://doi.org/10.3389/fmicb.2023.1032032,
31. https://doi.org/10.1128/spectrum.00757-24,
32. https://doi.org/10.1111/mmi.15323,
33. https://doi.org/10.37256/amtt.5220244537,
34. https://doi.org/10.3390/cells12101353,