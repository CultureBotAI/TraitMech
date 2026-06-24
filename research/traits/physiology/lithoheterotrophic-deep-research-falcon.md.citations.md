# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** lithoheterotrophic
- **METPO identifier:** METPO:1000648
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism obtains energy from the oxidation of inorganic compounds while using organic compounds as the primary carbon source for biosynthesis.
- **Parent traits:** METPO:1000631
- **Synonyms:** lithoheterotroph
- **Existing evidence:** DOI:10.1038/s41598-021-81412-3: engineered lithoheterotrophic strain (Experimental study supports Fe(II)-dependent lithoheterotrophic growth with glucose as carbon source.) | DOI:10.1016/B978-0-12-378630-2.00219-X: oxidize inorganic atoms or molecules (Review supports inorganic compound oxidation as lithotrophic energy metabolism.)
- **Existing causal graph summary:** lithoheterotrophic_inorganic_energy_organic_carbon: 10 nodes, 9 edges

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
**Generated:** 2026-06-18T11:47:41.296437

1. quinn2025characterizingstratifiedmicrobiala pages 20-23
2. jain2021engineeringlithoheterotrophyin pages 1-2
3. zhuang2024electrontransferin pages 5-6
4. zhuang2024electrontransferin pages 1-3
5. cui2024proposedminimalstandards pages 2-3
6. bartholet2023rationaldesignand pages 54-58
7. shao2025versatilenitraterespiringheterotrophs pages 1-2
8. shao2025versatilenitraterespiringheterotrophs pages 4-4
9. quinn2025characterizingstratifiedmicrobiala pages 59-62
10. jain2021engineeringlithoheterotrophyin pages 2-4
11. jain2021engineeringlithoheterotrophyin pages 4-5
12. becker2025evaluationofthiobacillus pages 1-2
13. becker2025evaluationofthiobacillus pages 8-9
14. becker2025evaluationofthiobacillus pages 17-18
15. quinn2025characterizingstratifiedmicrobial pages 20-23
16. quinn2025characterizingstratifiedmicrobial pages 59-62
17. becker2025evaluationofthiobacillus pages 2-4
18. Fe(III)
19. https://doi.org/10.1038/s41598-021-81412-3
20. https://doi.org/10.1038/s41467-025-56588-1
21. https://doi.org/10.3390/life14050591
22. https://doi.org/10.3390/microorganisms12112252
23. https://doi.org/10.1099/ijsem.0.006290
24. https://doi.org/10.3389/fmicb.2023.1182497
25. https://doi.org/10.1007/s00248-023-02239-1
26. https://doi.org/10.1093/femsec/fiaf024
27. https://doi.org/10.1099/ijsem.0.006949
28. https://doi.org/10.3390/life14050591,
29. https://doi.org/10.1099/ijsem.0.006290,
30. https://doi.org/10.1038/s41467-025-56588-1,
31. https://doi.org/10.1093/femsec/fiaf024,
32. https://doi.org/10.3390/microorganisms12112252,
33. https://doi.org/10.1099/ijsem.0.006949,