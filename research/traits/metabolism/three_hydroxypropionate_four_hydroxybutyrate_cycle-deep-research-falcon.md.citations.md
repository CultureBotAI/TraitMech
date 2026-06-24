# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** 3-hydroxypropionate/4-hydroxybutyrate cycle
- **METPO identifier:** traitmech:000024
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes two molecules of bicarbonate per turn via 3-hydroxypropionate and 4-hydroxybutyrate intermediates. It operates in aerobic and microaerophilic Crenarchaeota such as Sulfolobus and Metallosphaera.
- **Parent traits:** traitmech:000019
- **Synonyms:** 3HP/4HB cycle
- **Existing evidence:** DOI:10.1126/science.1149976:  (Berg et al. described the 3-hydroxypropionate/4-hydroxybutyrate autotrophic CO2-assimilation pathway in Archaea (Sulfolobales).) | DOI:10.1128/AEM.02473-10:  (Berg review situates the 3HP/4HB cycle among the six recognized autotrophic carbon-fixation pathways.)
- **Existing causal graph summary:** three_hp_four_hb_sulfolobales: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **3-hydroxypropionate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/three_hydroxypropionate_four_hydroxybutyrate_cycle.yaml`.

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
**Generated:** 2026-06-18T06:20:55.611902

1. bahrle2023currentstatusof pages 2-4
2. johnson2024crystalstructureof pages 1-2
3. wang2023microbialconversionand pages 3-5
4. cornell2024genomeencodedmetabolicpotential pages 60-61
5. padalko2024fusionfissionproteinfamily pages 10-12
6. ulas2012genomescalereconstructionand pages 6-9
7. kang2023insightsintoenzyme pages 2-4
8. cornell2024genomeencodedmetabolicpotential pages 59-60
9. johnson2024crystalstructureof pages 6-8
10. is
11. s
12. https://doi.org/10.1186/s40643-023-00705-9
13. https://doi.org/10.1038/s42003-024-06432-x
14. https://doi.org/10.4014/jmb.2306.06005
15. https://doi.org/10.1186/s40168-024-01912-y
16. https://doi.org/10.1371/journal.pone.0043401
17. https://doi.org/10.29328/journal.acee.1001055
18. https://doi.org/10.1038/ismej.2010.197
19. https://doi.org/10.1128/msystems.00948-23
20. https://doi.org/10.1111/1751-7915.14353
21. https://doi.org/10.1186/s40643-023-00705-9,
22. https://doi.org/10.1038/s42003-024-06432-x,
23. https://doi.org/10.1371/journal.pone.0043401,
24. https://doi.org/10.1111/1751-7915.14353,
25. https://doi.org/10.4014/jmb.2306.06005,
26. https://doi.org/10.29328/journal.acee.1001055,
27. https://doi.org/10.1128/msystems.00948-23,