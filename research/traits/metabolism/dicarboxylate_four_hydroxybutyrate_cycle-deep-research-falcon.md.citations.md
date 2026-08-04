# Citations for Research Query

**Query:** # Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** dicarboxylate/4-hydroxybutyrate cycle
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** traitmech:000025
- **Trait category:** METABOLISM
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** An autotrophic carbon-fixation pathway that fixes one molecule of CO2 and one of bicarbonate per turn via a dicarboxylate stage and a 4-hydroxybutyrate stage. It operates in anaerobic and microaerophilic Crenarchaeota such as Ignicoccus and Thermoproteales.
- **Parent traits:** traitmech:000019
- **Synonyms:** DC/4HB cycle
- **Existing evidence:** DOI:10.1128/AEM.02473-10:  (Berg review describes the dicarboxylate/4-hydroxybutyrate cycle as the anaerobic archaeal counterpart of the 3HP/4HB cycle.) | DOI:10.1126/science.1149976:  (Berg et al.'s archaeal carbon-fixation work establishes the 4-hydroxybutyrate chemistry shared by this cycle in Crenarchaeota.)
- **Existing causal graph summary:** dc_four_hb_anaerobic_archaeal_co2_fixation: 14 nodes, 12 edges

## Research Objective

Research the microbial trait **dicarboxylate/4-hydroxybutyrate cycle** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/metabolism/dicarboxylate_four_hydroxybutyrate_cycle.yaml`.

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
**Generated:** 2026-08-04T05:58:55.974162

1. ramosvera2011identificationofmissing pages 1-2
2. ramosvera2009autotrophiccarbondioxide pages 5-7
3. garritano2022carbonfixationpathways pages 1-2
4. ramosvera2009autotrophiccarbondioxide pages 1-2
5. ramosvera2009autotrophiccarbondioxide pages 8-9
6. 4Fe–4S
7. is converted
8. 4Fe-4S
9. 1-¹⁴C
10. 10.1073/pnas.0801043105
11. 10.1128/JB.00145-09
12. 10.1128/JB.01156-10
13. 10.1093/pnasnexus/pgac226
14. https://doi.org/10.1073/pnas.0801043105
15. https://doi.org/10.1073/pnas.0801043105;
16. https://doi.org/10.1128/JB.00145-09
17. https://doi.org/10.1128/JB.00145-09;
18. https://doi.org/10.1128/JB.01156-10
19. https://doi.org/10.1093/pnasnexus/pgac226
20. https://doi.org/10.1073/pnas.0801043105,
21. https://doi.org/10.1128/jb.00145-09,
22. https://doi.org/10.1128/jb.01156-10,
23. https://doi.org/10.1093/pnasnexus/pgac226,