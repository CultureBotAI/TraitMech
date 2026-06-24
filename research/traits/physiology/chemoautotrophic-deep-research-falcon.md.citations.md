# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautotrophic
- **METPO identifier:** METPO:1000635
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)
- **Existing causal graph summary:** chemoautotrophic_chemical_energy_co2_fixation: 9 nodes, 9 edges

## Research Objective

Research the microbial trait **chemoautotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/chemoautotrophic.yaml`.

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
**Generated:** 2026-06-18T11:10:19.995761

1. wieschollek2024anewtype pages 1-2
2. johnson2024crystalstructureof pages 1-2
3. prioretti2023carbonfixationin pages 1-2
4. harrison2024prevalenceofthe pages 1-5
5. johnson2024crystalstructureof pages 6-8
6. petushkova2024thecompletegenome pages 16-17
7. wieschollek2024anewtype pages 2-5
8. salcedo2026substantialgeneticpotential pages 9-11
9. salcedo2026substantialgeneticpotential pages 1-3
10. wang2025phylogeneticallyandmetabolically pages 2-4
11. salcedo2026substantialgeneticpotential pages 11-14
12. salcedo2026substantialgeneticpotential pages 8-9
13. salcedo2026substantialgeneticpotential pages 14-18
14. johnson2024crystalstructureof pages 2-3
15. johnson2024crystalstructureof pages 5-6
16. wang2025phylogeneticallyandmetabolically pages 1-2
17. was
18. https://doi.org/10.1128/AEM.01075-24
19. https://doi.org/10.3390/microorganisms12020391
20. https://doi.org/10.64898/2026.01.13.699260
21. https://doi.org/10.1101/2024.08.01.606197
22. https://doi.org/10.3390/life13030627
23. https://doi.org/10.1186/s40168-025-02177-9
24. https://doi.org/10.1038/s42003-024-06432-x
25. https://doi.org/10.64898/2026.01.13.699260,
26. https://doi.org/10.1186/s40168-025-02177-9,
27. https://doi.org/10.1128/aem.01075-24,
28. https://doi.org/10.1038/s42003-024-06432-x,
29. https://doi.org/10.3390/life13030627,
30. https://doi.org/10.1101/2024.08.01.606197,
31. https://doi.org/10.3390/microorganisms12020391,