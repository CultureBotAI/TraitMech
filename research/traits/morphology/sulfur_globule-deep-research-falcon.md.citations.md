# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** sulfur globule
- **METPO identifier:** traitmech:000069
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An intracellular (or periplasmic) inclusion of elemental sulfur formed as an intermediate during the oxidation of reduced sulfur compounds, characteristic of many sulfur-oxidizing and phototrophic sulfur bacteria.
- **Parent traits:** traitmech:000066
- **Synonyms:** sulfur inclusion
- **Existing evidence:** DOI:10.1016/S0065-2911(08)00002-7:  (Frigaard & Dahl describe sulfur globules as sulfur-storage inclusions formed during oxidative sulfur metabolism in phototrophic sulfur bacteria.) | DOI:10.1038/s41579-020-0413-0:  (Greening & Lithgow include sulfur globules among bacterial intracellular storage inclusions/organelles.)
- **Existing causal graph summary:** sulfur_globule_sulfur_oxidation_intermediate: 3 nodes, 2 edges

## Research Objective

Research the microbial trait **sulfur globule** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/sulfur_globule.yaml`.

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
**Generated:** 2026-06-18T10:10:05.680761

1. dahl2017sulfurmetabolismin pages 14-17
2. petushkova2024thecompletegenome pages 20-22
3. rudenko2024mechanismofintracellular pages 1-2
4. kumpel2023cellbiologyof pages 1-3
5. kumpel2023cellbiologyof pages 10-11
6. rudenko2024mechanismofintracellular pages 10-12
7. alarcon2024evidenceforautotrophic pages 1-2
8. alarcon2024evidenceforautotrophic pages 18-20
9. dahl2017sulfurmetabolismin pages 1-4
10. https://doi.org/10.20944/preprints202306.1429.v1;
11. https://doi.org/10.1007/978-3-319-51365-2_2;
12. https://doi.org/10.3390/microorganisms12020391;
13. https://doi.org/10.3390/ijms252010962;
14. https://doi.org/10.1128/aem.01941-21;
15. https://doi.org/10.1128/aem.00863-24;
16. https://doi.org/10.1126/sciadv.adk9345;
17. https://doi.org/10.3390/ijms252010962
18. https://doi.org/10.3390/microorganisms12020391
19. https://doi.org/10.1128/aem.00863-24
20. https://doi.org/10.1126/sciadv.adk9345
21. https://doi.org/10.20944/preprints202306.1429.v1
22. https://doi.org/10.1007/978-3-319-51365-2_2
23. https://doi.org/10.1128/aem.01941-21
24. https://doi.org/10.20944/preprints202306.1429.v1,
25. https://doi.org/10.3390/microorganisms12020391,
26. https://doi.org/10.1007/978-3-319-51365-2\_2,
27. https://doi.org/10.3390/ijms252010962,
28. https://doi.org/10.1126/sciadv.adk9345,
29. https://doi.org/10.1128/aem.00863-24,