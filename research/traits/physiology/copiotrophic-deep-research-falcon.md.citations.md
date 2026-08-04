# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** copiotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000642
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A nutrient adaptation in which an organism thrives in environments with high nutrient concentrations, typically exhibiting rapid growth rates and utilizing diverse carbon sources.
- **Parent traits:** METPO:1000731
- **Synonyms:** copiotroph
- **Existing evidence:** DOI:10.1073/pnas.0903507106: high (copiotrophic) or low (oligotrophic) nutrient concentrations (Comparative genomics paper defines copiotrophic growth strategy by high-nutrient adaptation.) | DOI:10.1002/bies.1091: common in environments with greater nutritional opportunities (Essay contrasts copiotrophs with oligotrophs in nutrient-rich environments.)
- **Existing causal graph summary:** copiotrophic_high_nutrient_fast_growth: 15 nodes, 13 edges

## Research Objective

Research the microbial trait **copiotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/copiotrophic.yaml`.

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
**Generated:** 2026-08-04T11:11:54.146536

1. dragone2024taxonomicandgenomic pages 8-10
2. zhu2024shapingofmicrobial pages 7-8
3. lauro2009thegenomicbasis pages 2-3
4. lauro2009thegenomicbasis pages 1-2
5. ho2017revisitinglifestrategy pages 2-3
6. lauro2009thegenomicbasis pages 3-4
7. zhang2024antarcticsoilsselect pages 1-2
8. dragone2024taxonomicandgenomic pages 3-4
9. evan2021controlsofmicrobially pages 160-164
10. zhang2024antarcticsoilsselect pages 5-9
11. marschmann2024predictionsofrhizosphere pages 11-12
12. zhang2024antarcticsoilsselect pages 4-5
13. ing
14. 10.1038/s41467-024-48591-9
15. 10.1093/ismeco/ycae081
16. 10.1038/s41564-023-01582-w
17. 10.3390/microorganisms12081689
18. 10.1073/pnas.0903507106
19. 10.1093/femsec/fix006
20. 10.7298/h89k-hy10
21. https://doi.org/10.1038/s41467-024-48591-9
22. https://doi.org/10.1093/ismeco/ycae081
23. https://doi.org/10.1038/s41564-023-01582-w
24. https://doi.org/10.3390/microorganisms12081689
25. https://doi.org/10.1073/pnas.0903507106
26. https://doi.org/10.1093/femsec/fix006
27. https://doi.org/10.7298/h89k-hy10
28. https://doi.org/10.1073/pnas.0903507106,
29. https://doi.org/10.1093/femsec/fix006,
30. https://doi.org/10.1038/s41467-024-48591-9,
31. https://doi.org/10.1093/ismeco/ycae081,
32. https://doi.org/10.3390/microorganisms12081689,
33. https://doi.org/10.7298/h89k-hy10,
34. https://doi.org/10.1038/s41564-023-01582-w,