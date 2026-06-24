# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** oxidase activity
- **METPO identifier:** traitmech:000076
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A physiological enzyme-activity phenotype in which a cell produces a terminal respiratory oxidase (notably cytochrome c oxidase); it is the basis of the diagnostic oxidase test.
- **Parent traits:** METPO:1000059
- **Synonyms:** oxidase-positive
- **Existing evidence:** DOI:10.3390/microorganisms10050926:  (Hederstedt reviews bacterial cytochrome c oxidase, the terminal respiratory oxidase detected by the oxidase test.) | DOI:10.1089/ars.2020.8039:  (Borisov et al. review cytochrome bd-family terminal oxidases of prokaryotic respiratory chains.)
- **Existing causal graph summary:** oxidase_activity_terminal_oxidase: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **oxidase activity** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/oxidase_activity.yaml`.

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
**Generated:** 2026-06-18T12:15:35.635688

1. hederstedt2022diversityofcytochrome pages 1-2
2. khalfaouihassani2023theescherichiacoli pages 1-2
3. garg2021geneslinkingcopper pages 1-2
4. nastasi2024membraneboundredoxenzyme pages 2-4
5. saha2024cytochromebdoxidase pages 2-3
6. seitz2024targetingtuberculosisnovel pages 1-3
7. garg2021geneslinkingcopper pages 16-17
8. nastasi2024membraneboundredoxenzyme pages 1-2
9. baldea2023theoxidasetest pages 3-4
10. borisov2025carbonmonoxideand pages 5-7
11. gonzalezmontalvo2024therespiratorychain pages 1-2
12. baldea2023theoxidasetesta pages 3-4
13. garg2021geneslinkingcopper pages 7-8
14. baldea2023theoxidasetesta pages 1-3
15. baldea2023theoxidasetest pages 1-3
16. hederstedt2022diversityofcytochrome pages 2-4
17. nastasi2024membraneboundredoxenzyme pages 18-19
18. O2
19. https://doi.org/10.3390/microorganisms10050926.
20. https://doi.org/10.3389/fmicb.2021.683260.
21. https://doi.org/10.3390/ijms25021277.
22. https://doi.org/10.3390/ijms26062809.
23. https://doi.org/10.1039/d3md00587a.
24. https://doi.org/10.1021/acs.jcim.4c00344.
25. https://doi.org/10.1371/journal.pone.0293015.
26. https://doi.org/10.3390/ijms25021277
27. https://doi.org/10.1021/acs.jcim.4c00344
28. https://doi.org/10.1039/d3md00587a
29. https://doi.org/10.3389/fmicb.2024.1479714
30. https://doi.org/10.1371/journal.pone.0293015
31. https://doi.org/10.3390/microorganisms10050926
32. https://doi.org/10.3389/fmicb.2021.683260
33. https://doi.org/10.3390/ijms26062809
34. https://doi.org/10.3390/microorganisms10050926,
35. https://doi.org/10.3390/ijms26062809,
36. https://doi.org/10.3390/ijms25021277,
37. https://doi.org/10.1371/journal.pone.0293015,
38. https://doi.org/10.3389/fmicb.2021.683260,
39. https://doi.org/10.1039/d3md00587a,
40. https://doi.org/10.1021/acs.jcim.4c00344,
41. https://doi.org/10.3389/fmicb.2024.1479714,