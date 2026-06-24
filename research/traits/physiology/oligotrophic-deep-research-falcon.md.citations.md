# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oligotrophic
- **METPO identifier:** METPO:1000654
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A nutrient adaptation characterized by the ability to thrive in environments with very low nutrient concentrations, typically possessing efficient nutrient uptake and utilization systems.
- **Parent traits:** METPO:1000731
- **Synonyms:** TT_oligotroph, oligotroph
- **Existing evidence:** DOI:10.1073/pnas.0903507106: high (copiotrophic) or low (oligotrophic) nutrient concentrations (Comparative genomics paper defines oligotrophy by low-nutrient adaptation.) | DOI:10.1038/ismej.2014.60: nutrients limit growth (Streamlining review links nutrient limitation to small-cell/genome adaptation.) | PMID:16109880: Pelagibacter ubique (Organism example: Pelagibacter ubique HTCC1062 (SAR11 clade) is the archetypal oligotrophic marine bacterium with a streamlined genome adapted to nutrient-poor open-ocean conditions (Giovannoni et al. 2005, Science).)
- **Existing causal graph summary:** oligotrophic_low_nutrient_efficiency: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **oligotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/oligotrophic.yaml`.

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
**Generated:** 2026-06-18T12:14:52.966495

1. zhu2024shapingofmicrobial pages 7-8
2. ngugi2023abioticselectionof pages 1-2
3. molinapardines2023phosphaterelatedgenomicislands pages 1-2
4. clifton2024theultrahighaffinity pages 1-2
5. clifton2024theultrahighaffinity pages 6-7
6. molinapardines2023phosphaterelatedgenomicislands pages 9-11
7. huancavalenzuela2024nichedifferentiationin pages 8-10
8. harbeitner2024gradientsofbacteria pages 1-2
9. huancavalenzuela2024nichedifferentiationin pages 15-17
10. huancavalenzuela2024nichedifferentiationin pages 1-2
11. clifton2024theultrahighaffinity pages 7-7
12. todd2024bloomandbust pages 1-8
13. yang2023decipheringfactorsdriving pages 1-2
14. zhang2024antarcticsoilsselect pages 1-2
15. clifton2024theultrahighaffinity pages 5-6
16. harbeitner2024gradientsofbacteria pages 11-12
17. https://doi.org/10.1038/s41467-023-36988-x
18. https://doi.org/10.1038/s41586-024-07924-w
19. https://doi.org/10.1038/s41586-024-07924-w;
20. https://doi.org/10.1128/msystems.00898-23
21. https://doi.org/10.1038/s41467-024-48591-9
22. https://doi.org/10.1038/s41467-024-48591-9;
23. https://doi.org/10.3389/fmars.2024.1386686
24. https://doi.org/10.1371/journal.pone.0298139
25. https://doi.org/10.1002/imt2.66
26. https://doi.org/10.3390/microorganisms12081689
27. https://doi.org/10.1038/s41586-024-07924-w,
28. https://doi.org/10.1038/s41467-024-48591-9,
29. https://doi.org/10.1128/msystems.00898-23,
30. https://doi.org/10.1038/s41467-023-36988-x,
31. https://doi.org/10.3389/fmars.2024.1386686,
32. https://doi.org/10.1371/journal.pone.0298139,
33. https://doi.org/10.1002/imt2.66,
34. https://doi.org/10.3390/microorganisms12081689,