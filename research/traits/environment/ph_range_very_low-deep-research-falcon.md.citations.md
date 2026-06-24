# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pH range very low
- **METPO identifier:** METPO:1000459
- **Trait category:** ENVIRONMENT
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A pH range phenotype in which growth extends to external pH at or below approximately 4, characteristic of extreme-acidophile physiology.
- **Parent traits:** METPO:1000332
- **Synonyms:** Acid Tolerant, Acidophile, Extreme Acidophile, Facultative acidophile, Obligative acidophile, pHR_0_to_4
- **Existing evidence:** DOI:10.1038/nrmicro2549: growing at pH 1.0-3.0 (pH-homeostasis review supports growth in the pH 1–4 range as the extreme-acidophile growth range.)
- **Existing causal graph summary:** ph_range_very_low_extreme_acidophile: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **pH range very low** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/environment/ph_range_very_low.yaml`.

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
**Generated:** 2026-06-18T01:02:19.172786

1. krulwich2011molecularaspectsof pages 11-12
2. gonzalez2024acidophilicheterotrophsbasic pages 1-2
3. johnson2016themicrobiologyof pages 3-4
4. krulwich2011molecularaspectsof pages 5-6
5. gonzalez2024acidophilicheterotrophsbasic pages 2-3
6. lund2020understandinghowmicroorganisms pages 3-5
7. gonzalez2024acidophilicheterotrophsbasic pages 3-4
8. krulwich2011molecularaspectsof pages 15-17
9. lund2020understandinghowmicroorganisms pages 1-2
10. lehtovirtamorley2016identifyingpotentialmechanisms pages 1-5
11. lehtovirtamorley2016identifyingpotentialmechanisms pages 28-33
12. https://doi.org/10.1128/9781555818821.ch4.3.1
13. https://doi.org/10.1038/nrmicro2549
14. https://doi.org/10.3389/frbis.2023.1338019
15. https://doi.org/10.1111/1758-2229.70019
16. https://doi.org/10.1128/9781555818821.ch4.3.1;
17. https://doi.org/10.3389/fmicb.2020.556140
18. https://doi.org/10.1128/AEM.04031-15;
19. https://doi.org/10.3389/fmicb.2024.1374800
20. https://doi.org/10.1128/AEM.04031-15
21. https://doi.org/10.1038/nrmicro2549,
22. https://doi.org/10.1128/9781555818821.ch4.3.1,
23. https://doi.org/10.3389/fmicb.2024.1374800,
24. https://doi.org/10.3389/fmicb.2020.556140,
25. https://doi.org/10.1111/1758-2229.70019,
26. https://doi.org/10.1128/aem.04031-15,