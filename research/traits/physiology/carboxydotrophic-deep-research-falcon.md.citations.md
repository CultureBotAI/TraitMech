# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** carboxydotrophic
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000633
- **Trait category:** PHYSIOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A trophic type in which an organism derives energy from the oxidation of carbon monoxide.
- **Parent traits:** METPO:1000631
- **Synonyms:** 
- **Existing evidence:** DOI:10.1038/nrmicro1595: Carbon monoxide (CO) supports the growth and metabolism (Review supports aerobic CO oxidation as an energy-supporting metabolism.) | DOI:10.1111/j.1574-6968.1986.tb01858.x: presence of the enzyme CO dehydrogenase (Review supports CODH and CO-insensitive respiratory-chain features in aerobic carboxydotrophs.)
- **Existing causal graph summary:** carboxydotrophic_co_oxidation: 18 nodes, 16 edges

## Research Objective

Research the microbial trait **carboxydotrophic** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/physiology/carboxydotrophic.yaml`.

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
**Generated:** 2026-08-04T10:47:45.838424

1. bahrle2023currentstatusof pages 5-8
2. svetlitchnyi2001twomembraneassociatednifescarbon pages 7-9
3. oelgeschlager2008carbonmonoxidedependentenergy pages 1-2
4. bahrle2023currentstatusof pages 8-9
5. karnachuk2024novelthermophilicgenera pages 8-10
6. wang2024codrivenelectronand pages 7-8
7. robazza2024acetateshockloads pages 11-12
8. svetlitchnyi2001twomembraneassociatednifescarbon pages 1-2
9. robazza2024acetateshockloads pages 1-2
10. karnachuk2024novelthermophilicgenera pages 5-8
11. sobieraj2023biologicaltreatmentof pages 5-6
12. sobieraj2023biologicaltreatmentof pages 3-5
13. and
14. 10.1186/s40643-023-00705-9
15. 10.3389/fmicb.2024.1441865
16. 10.1186/s40168-024-01869-y
17. 10.1111/1751-7915.70063
18. 10.3389/fbioe.2023.1126737
19. 10.1128/JB.183.17.5134-5144.2001
20. 10.1007/s00203-008-0382-6
21. 10.1111/j.1574-6968.1986.tb01858.x
22. https://doi.org/10.1186/s40643-023-00705-9
23. https://doi.org/10.3389/fmicb.2024.1441865
24. https://doi.org/10.1186/s40168-024-01869-y
25. https://doi.org/10.1111/1751-7915.70063
26. https://doi.org/10.3389/fbioe.2023.1126737
27. https://doi.org/10.1128/JB.183.17.5134-5144.2001
28. https://doi.org/10.1007/s00203-008-0382-6
29. https://doi.org/10.1111/j.1574-6968.1986.tb01858.x
30. https://doi.org/10.1186/s40643-023-00705-9,
31. https://doi.org/10.1007/s00203-008-0382-6,
32. https://doi.org/10.1128/jb.183.17.5134-5144.2001,
33. https://doi.org/10.3389/fmicb.2024.1441865,
34. https://doi.org/10.1186/s40168-024-01869-y,
35. https://doi.org/10.1111/1751-7915.70063,
36. https://doi.org/10.3389/fbioe.2023.1126737,