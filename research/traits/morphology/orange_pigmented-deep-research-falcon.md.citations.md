# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** orange pigmented
- **METPO identifier:** METPO:1003026
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pigmentation phenotype in which microbial colonies or cells appear orange due to production and accumulation of orange pigments such as carotenoids.
- **Parent traits:** METPO:1003021
- **Synonyms:** Pigment_orange
- **Existing evidence:** DOI:10.1080/1040841X.2025.2526423: orange ... pigmentation in bacteria (Supports orange microbial pigmentation as a bacterial carotenoid-associated color phenotype.)
- **Existing causal graph summary:** orange_pigmented_carotenoid_accumulation: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **orange pigmented** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/orange_pigmented.yaml`.

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
**Generated:** 2026-06-18T09:05:07.207475

1. janisch2023geneticunderpinningsof pages 5-8
2. nirmala2024enhancingstaphyloxanthinsynthesis pages 6-11
3. nirmala2024enhancingstaphyloxanthinsynthesis pages 1-2
4. takatani2024identificationofa pages 1-2
5. stra2023carotenoidmetabolismnew pages 1-2
6. agarwal2023bacterialpigmentsand pages 6-7
7. wang2024insightsintothe pages 6-8
8. ochoavinals2024currentadvancesin pages 1-2
9. ochoavinals2024currentadvancesin pages 2-5
10. nagar2024genomicinsightson pages 5-6
11. hoondee2024comparativegenomicanalysis pages 1-2
12. wang2024insightsintothe pages 11-11
13. mushomba2023inducedantibioticresistance pages 65-71
14. sosafajardo2024genomicexplorationof pages 16-17
15. nirmala2024enhancingstaphyloxanthinsynthesis pages 13-14
16. https://doi.org/10.3390/pathogens12010086
17. https://doi.org/10.3390/microorganisms11030614
18. https://doi.org/10.3389/fpls.2022.1072061
19. https://doi.org/10.7759/cureus.59892
20. https://doi.org/10.1186/s12864-024-10490-0
21. https://doi.org/10.1007/s00253-023-12995-2
22. https://doi.org/10.3389/fmicb.2024.1447785
23. https://doi.org/10.3390/fermentation10040190
24. https://doi.org/10.1371/journal.pone.0304699
25. https://doi.org/10.21203/rs.3.rs-4637278/v1
26. https://doi.org/10.11606/d.97.2024.tde-12122024-113132
27. https://doi.org/10.7759/cureus.59892,
28. https://doi.org/10.1186/s12864-024-10490-0,
29. https://doi.org/10.1007/s00253-023-12995-2,
30. https://doi.org/10.3390/pathogens12010086,
31. https://doi.org/10.3389/fpls.2022.1072061,
32. https://doi.org/10.3390/microorganisms11030614,
33. https://doi.org/10.3390/fermentation10040190,
34. https://doi.org/10.11606/d.97.2024.tde-12122024-113132,
35. https://doi.org/10.3389/fmicb.2024.1447785,
36. https://doi.org/10.21203/rs.3.rs-4637278/v1,
37. https://doi.org/10.1371/journal.pone.0304699,