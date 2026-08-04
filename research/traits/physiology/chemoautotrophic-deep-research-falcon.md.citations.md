# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** chemoautotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000635
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from oxidation of inorganic compounds and carbon from carbon dioxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** chemoautotroph
- **Existing evidence:** DOI:10.1146/annurev.micro.52.1.191: Carbon Dioxide Fixation in Chemoautotrophs (Review supports CO2 fixation as central to chemoautotrophic bacteria.) | DOI:10.1128/AEM.02473-10: Calvin-Benson reductive pentose phosphate cycle (Review supports Calvin-Benson and other microbial autotrophic CO2-fixation pathways.)
- **Existing causal graph summary:** chemoautotrophic_chemical_energy_co2_fixation: 16 nodes, 17 edges

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
**Generated:** 2026-08-04T10:54:26.013790

1. shively1998somethingfromalmost pages 3-5
2. marc2023physiologicalandgenetic pages 98-103
3. atencio2024metabolicadaptationsunderpin pages 6-8
4. deng2023strategiesofchemolithoautotrophs pages 1-2
5. yang2024metagenomicsandstable pages 1-2
6. tu2023engineeringartificialphotosynthesis pages 10-11
7. li2024productionofsuccinate pages 10-11
8. li2024productionofsuccinate pages 1-2
9. li2024productionofsuccinate pages 7-10
10. 10.1186/s40168-023-01712-w
11. 10.1038/s41467-023-43524-4
12. 10.1021/acs.est.4c00248
13. 10.1038/s41598-024-68868-9
14. 10.1186/s12934-024-02470-6
15. 10.7939/r3-3c5n-dn16
16. 10.1146/annurev.micro.52.1.191
17. https://doi.org/10.1186/s40168-023-01712-w
18. https://doi.org/10.1038/s41467-023-43524-4
19. https://doi.org/10.1021/acs.est.4c00248
20. https://doi.org/10.1038/s41598-024-68868-9
21. https://doi.org/10.1186/s12934-024-02470-6
22. https://doi.org/10.7939/r3-3c5n-dn16
23. https://doi.org/10.1146/annurev.micro.52.1.191
24. https://doi.org/10.1146/annurev.micro.52.1.191,
25. https://doi.org/10.7939/r3-3c5n-dn16,
26. https://doi.org/10.1038/s41598-024-68868-9,
27. https://doi.org/10.1186/s40168-023-01712-w,
28. https://doi.org/10.1021/acs.est.4c00248,
29. https://doi.org/10.1038/s41467-023-43524-4,
30. https://doi.org/10.1186/s12934-024-02470-6,