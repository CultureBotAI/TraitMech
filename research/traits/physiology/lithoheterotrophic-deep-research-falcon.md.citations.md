# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithoheterotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000648
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of inorganic compounds while using organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.)
- **Existing causal graph summary:** lithoheterotrophic_inorganic_energy_organic_carbon: 18 nodes, 17 edges

## Research Objective

Research the microbial trait **lithoheterotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/lithoheterotrophic.yaml`.

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
**Generated:** 2026-08-04T11:26:42.916037

1. lappan2023molecularhydrogenin pages 1-2
2. lappan2023molecularhydrogenin pages 6-7
3. gureeva2024wastewatertreatmentwith pages 7-9
4. gureeva2024wastewatertreatmentwith pages 15-16
5. gureeva2024wastewatertreatmentwith pages 9-12
6. lappan2023molecularhydrogenin pages 2-3
7. kublanov2017genomicanalysisof pages 11-12
8. shao2025versatilenitraterespiringheterotrophs pages 1-2
9. gureeva2024wastewatertreatmentwith pages 6-7
10. zeng2021microorganismsfromdeepsea pages 9-11
11. zeng2021microorganismsfromdeepsea pages 12-13
12. lappan2023molecularhydrogenin pages 17-18
13. shao2025versatilenitraterespiringheterotrophs pages 4-4
14. NiFe
15. 10.1038/s41564-023-01322-0
16. 10.1128/AEM.01344-19
17. 10.3390/ijms25169093
18. 10.1038/s41467-025-56588-1
19. 10.1038/s41598-021-81412-3
20. 10.1038/s41396-021-01165-9
21. 10.1007/s42995-020-00086-4
22. 10.3389/fmicb.2017.00195
23. 10.1016/B978-0-12-378630-2.00219-X
24. https://doi.org/10.1038/s41564-023-01322-0
25. https://doi.org/10.1128/AEM.01344-19
26. https://doi.org/10.3390/ijms25169093
27. https://doi.org/10.1038/s41467-025-56588-1
28. https://doi.org/10.1038/s41598-021-81412-3
29. https://doi.org/10.1038/s41396-021-01165-9
30. https://doi.org/10.1007/s42995-020-00086-4
31. https://doi.org/10.3389/fmicb.2017.00195
32. https://doi.org/10.1016/B978-0-12-378630-2.00219-X
33. https://doi.org/10.1128/aem.01344-19,
34. https://doi.org/10.1038/s41564-023-01322-0,
35. https://doi.org/10.1007/s42995-020-00086-4,
36. https://doi.org/10.3390/ijms25169093,
37. https://doi.org/10.3389/fmicb.2017.00195,
38. https://doi.org/10.1038/s41467-025-56588-1,