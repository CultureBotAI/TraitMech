# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** halophily preference
- **METPO identifier:** METPO:1000629
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that is relating to an organism's salt concentration requirements or tolerance for growth.
- **Parent traits:** METPO:1000059
- **Synonyms:** Physiology and metabolism.halophily.halophily level, range_salinity
- **Existing evidence:** DOI:10.1093/femsre/fuy009: life at high salt concentrations (Supports salinity and salt concentration as a growth-relevant microbial trait axis.)
- **Existing causal graph summary:** halophily_preference_osmoadaptation: 7 nodes, 6 edges

## Research Objective

Research the microbial trait **halophily preference** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/halophily_preference.yaml`.

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
**Generated:** 2026-06-17T23:02:25.164795

1. bonnaud2024haloarchaeaaspromising pages 1-2
2. oren2024novelinsightsinto pages 1-2
3. yu2024temporaldynamicsof pages 1-2
4. oren2024novelinsightsinto pages 4-5
5. bonnaud2024haloarchaeaaspromising pages 2-4
6. xing2024thepolyextremophilenatranaerobius pages 14-17
7. xing2024thepolyextremophilenatranaerobius pages 24-25
8. xing2024thepolyextremophilenatranaerobius pages 17-19
9. xing2024thepolyextremophilenatranaerobius pages 10-14
10. chen2024elucidatingthesalttolerant pages 1-2
11. shu2023metabolicengineeringof pages 6-10
12. chen2024elucidatingthesalttolerant pages 10-11
13. yu2024temporaldynamicsof pages 2-5
14. ionescu2024extremefluctuationsin pages 1-2
15. shu2023metabolicengineeringof pages 3-4
16. thompson2024themicrobiomeof pages 5-6
17. lichty2024compatiblesolutesare pages 19-23
18. https://doi.org/10.1186/s12934-024-02358-5
19. https://doi.org/10.3390/microorganisms12081738
20. https://doi.org/10.1128/aem.00145-24
21. https://doi.org/10.1186/s12934-024-02515-w
22. https://doi.org/10.1038/s41598-023-36975-8
23. https://doi.org/10.1038/s44185-024-00050-w
24. https://doi.org/10.3390/microorganisms12081738,
25. https://doi.org/10.1038/s44185-024-00050-w,
26. https://doi.org/10.3389/frmbi.2023.1329925,
27. https://doi.org/10.1186/s12934-024-02358-5,
28. https://doi.org/10.1128/aem.00145-24,
29. https://doi.org/10.1038/s41598-023-36975-8,
30. https://doi.org/10.3390/microorganisms12071473,
31. https://doi.org/10.1186/s12934-024-02515-w,