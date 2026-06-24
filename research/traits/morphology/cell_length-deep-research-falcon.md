---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:39:06.846419'
end_time: '2026-06-18T07:09:33.310433'
duration_seconds: 1826.46
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell length
  trait_identifier: METPO:1000881
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_length
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A phenotype that inheres in a cell by virtue of its longer dimension
    when viewed on a plane.
  parent_traits: METPO:1000059
  synonyms: ''
  evidence_summary: 'DOI:10.1016/j.cub.2014.07.022: cell size is tightly controlled
    (Review establishes cell size as an actively regulated phenotype, supporting length
    as a controlled cellular dimension.) | DOI:10.1016/j.cell.2014.11.022: cells grow
    by a fixed amount between divisions (Adder-model paper supports an inter-divisional
    length increment underlying cell-length distributions.)'
  causal_graph_summary: 'cell_length_division_growth_control: 6 nodes, 5 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 60
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length
- **METPO identifier:** METPO:1000881
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its longer dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.cub.2014.07.022: cell size is tightly controlled (Review establishes cell size as an actively regulated phenotype, supporting length as a controlled cellular dimension.) | DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports an inter-divisional length increment underlying cell-length distributions.)
- **Existing causal graph summary:** cell_length_division_growth_control: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **cell length** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length.yaml`.

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


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length
- **METPO identifier:** METPO:1000881
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A phenotype that inheres in a cell by virtue of its longer dimension when viewed on a plane.
- **Parent traits:** METPO:1000059
- **Synonyms:** 
- **Existing evidence:** DOI:10.1016/j.cub.2014.07.022: cell size is tightly controlled (Review establishes cell size as an actively regulated phenotype, supporting length as a controlled cellular dimension.) | DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports an inter-divisional length increment underlying cell-length distributions.)
- **Existing causal graph summary:** cell_length_division_growth_control: 6 nodes, 5 edges

## Research Objective

Research the microbial trait **cell length** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length.yaml`.

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


# Microbial Trait Causal Graph Research Report: **Cell length** (METPO:1000881)

## 1) Trait scope (what “cell length” represents)

**Trait definition (METPO:1000881)**: cell length is the longer dimension of a microbial cell when viewed in a plane (typically measured pole-to-pole for rods). In practice, cell length is treated as a **morphological readout** that emerges from the balance between **cell elongation** and **cell division/separation**.

### Operational meaning in current microbial physiology
- Cell length is commonly operationalized as a **single-cell pole-to-pole distance** extracted from microscopy images (including time-lapse microfluidics) (chung2024singlecellimagingof pages 7-8).
- Mechanistically, rod-shaped bacteria use (i) an **elongation system** (elongasome/Rod complex) to insert peptidoglycan along the sidewall and lengthen before division, and (ii) a **division system** (divisome) to synthesize septal peptidoglycan and constrict, terminating elongation (harpring2023plasticityinthe pages 1-2, cameron2024insightsintothe pages 1-3, hayashi2024septalwallsynthesis pages 1-2).

### Boundary cases / distinctions for curation
- **Cell length vs cell width/diameter**: width is controlled by overlapping but distinct envelope determinants (often Rod complex geometry); do not infer width changes from length changes without evidence.
- **Cell length vs “cell size”/volume**: many studies report “cell size” but use length as the dominant measurable proxy in rods (vashistha2023bacterialcellsizechanges pages 1-2, thiermann2024toolsandmethods pages 1-3).
- **Filamentation vs chaining** (critical boundary case): apparent long “cells” may be (a) true filamentation (single cell that failed division) or (b) **chains of unseparated daughters** due to septum cleavage failure (e.g., AmiC) (tian2023cellsortingdirectedselection pages 4-7).

## 2) Key concepts and definitions (current understanding)

### Elongasome vs divisome as the main conceptual split
- **Elongasome**: a multiprotein complex driving **sidewall peptidoglycan synthesis** that maintains rod shape and enables **cell lengthening prior to division** (harpring2023plasticityinthe pages 1-2).
- **Divisome**: a multiprotein complex that forms at midcell to enable **septal peptidoglycan synthesis** and cytokinesis (harpring2023plasticityinthe pages 1-2, cameron2024insightsintothe pages 1-3).

### Division timing as a cell-length determinant
- A major mechanistic route to longer cells is **delayed Z-ring formation / delayed division initiation**, allowing more elongation time and greater length at division (vashistha2023bacterialcellsizechanges pages 1-2, cameron2024insightsintothe pages 1-3).

### Envelope mechanics as a length/filamentation determinant
- Defects in coordinating outer membrane constriction with peptidoglycan constriction can generate filamentation/chaining phenotypes (lakey2023theroleof pages 1-2).

## 3) Candidate causal graph entities (nodes) grouped by type

| Category | Node label | Suggested ontology grounding | Role in length control (1 phrase) | Key supporting source (author year) | DOI | URL | Date |
|---|---|---|---|---|---|---|---|
| Trait/phenotype nodes | cell length | METPO:1000881 | focal longitudinal morphology trait | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 |
| Trait/phenotype nodes | cell size at division | label-only | outcome of division timing and elongation | Vashistha 2023 (vashistha2023bacterialcellsizechanges pages 1-2) | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 |
| Trait/phenotype nodes | filamentation | label-only | increased apparent length from failed division | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Trait/phenotype nodes | chaining | label-only | increased apparent length from failed separation | Tian 2023 (tian2023cellsortingdirectedselection pages 4-7) | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 |
| Trait/phenotype nodes | asymmetric growth | label-only | generates lineage-to-lineage length heterogeneity | Chung 2024 (chung2024singlecellimagingof pages 1-2) | 10.1038/s41564-024-01846-z | https://doi.org/10.1038/s41564-024-01846-z | Nov 2024 |
| Biological processes | sidewall peptidoglycan synthesis | GO:0009252 | lengthens rod before division | Harpring 2023 (harpring2023plasticityinthe pages 1-2) | 10.3389/fcimb.2023.1205488 | https://doi.org/10.3389/fcimb.2023.1205488 | Oct 2023 |
| Biological processes | septal peptidoglycan synthesis | GO:0009252 | drives constriction and limits final length | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Biological processes | cell elongation | GO:0009826 | increases long axis between birth and division | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Biological processes | cytokinetic constriction / cell division | GO:0051301 | terminates elongation cycle | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Biological processes | septum cleavage / daughter cell separation | GO:0000917 | prevents chaining-based length increase | Tian 2023 (tian2023cellsortingdirectedselection pages 4-7) | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 |
| Biological processes | FtsZ ring formation timing | label-only | sets division onset and size threshold | Vashistha 2023 (vashistha2023bacterialcellsizechanges pages 1-2) | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 |
| Biological processes | outer membrane constriction | label-only | coordinates envelope closure with division | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Complexes/modules | elongasome / Rod complex | label-only | sidewall growth machinery controlling lengthening | Harpring 2023 (harpring2023plasticityinthe pages 1-2), Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.3389/fcimb.2023.1205488; 10.1038/s42003-024-07279-y | https://doi.org/10.3389/fcimb.2023.1205488 ; https://doi.org/10.1038/s42003-024-07279-y | Oct 2023; Nov 2024 |
| Complexes/modules | divisome | label-only | septal synthesis machinery determining division completion | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Complexes/modules | proto-ring (FtsZ-FtsA-ZipA) | label-only | anchors and organizes early division site | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Complexes/modules | FtsWI septal synthase complex | label-only | executes septum synthesis during constriction | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Complexes/modules | Tol-Pal system | label-only | couples OM constriction to septal events | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Complexes/modules | CenKR two-component system | label-only | regulatory module shifting elongation/division balance | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Genes/proteins | FtsZ | GO:0003924 | master organizer of division timing | Cameron 2024 (cameron2024insightsintothe pages 1-3), Vashistha 2023 (vashistha2023bacterialcellsizechanges pages 1-2) | 10.1038/s41579-023-00942-x; 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41579-023-00942-x ; https://doi.org/10.1038/s41467-023-41487-0 | Jul 2024; Sep 2023 |
| Genes/proteins | FtsA | label-only | membrane tether for Z-ring assembly | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Genes/proteins | ZipA | label-only | membrane tether for proto-ring stability | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Genes/proteins | FtsW | label-only | septal glycan polymerization component | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Genes/proteins | FtsI / PBP3 | label-only | septal transpeptidase limiting constriction | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Genes/proteins | FtsN | label-only | late divisome factor linked to septation | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Genes/proteins | FtsK | label-only | upstream divisome recruitment factor | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Genes/proteins | MreB | label-only | cytoskeletal scaffold for elongation zones | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2), Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1038/s42003-024-07279-y; 10.1128/mbio.00631-23 | https://doi.org/10.1038/s42003-024-07279-y ; https://doi.org/10.1128/mbio.00631-23 | Nov 2024; Jun 2023 |
| Genes/proteins | RodZ | label-only | links MreB to Rod machinery | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 |
| Genes/proteins | PBP2 / MrdA | label-only | lateral wall transpeptidase for rod elongation | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 |
| Genes/proteins | RodA | label-only | SEDS partner in elongation PG insertion | Harpring 2023 (harpring2023plasticityinthe pages 1-2) | 10.3389/fcimb.2023.1205488 | https://doi.org/10.3389/fcimb.2023.1205488 | Oct 2023 |
| Genes/proteins | MreC | label-only | periplasmic Rod-complex organizer | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 |
| Genes/proteins | MreD | label-only | Rod-complex accessory elongation factor | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 |
| Genes/proteins | MinC | label-only | negative regulator of polar FtsZ assembly | Cameron 2024 (cameron2024insightsintothe pages 1-3) | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 |
| Genes/proteins | MinD | label-only | oscillatory division-site regulator | Vashistha 2023 (vashistha2023bacterialcellsizechanges pages 1-2) | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 |
| Genes/proteins | MinE | label-only | tunes Z-ring timing via Min oscillations | Vashistha 2023 (vashistha2023bacterialcellsizechanges pages 1-2) | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 |
| Genes/proteins | AmiC | label-only | septal amidase preventing chains | Tian 2023 (tian2023cellsortingdirectedselection pages 4-7) | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 |
| Genes/proteins | Pal | label-only | OM lipoprotein coordinating septal constriction | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Genes/proteins | TolQRA | label-only | energizes Tol-Pal-mediated OM remodeling | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Genes/proteins | CenK | label-only | sensor kinase driving filamentation when overexpressed | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Genes/proteins | CenR | label-only | response regulator controlling envelope genes | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Chemicals/perturbations | cephalexin | CHEBI:3495 | division inhibitor causing filamentation | Lakey 2023 (lakey2023theroleof pages 18-19) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Chemicals/perturbations | A22 | label-only | MreB inhibitor probing elongation control | Lakey 2023 (lakey2023theroleof pages 2-4) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Chemicals/perturbations | mecillinam / amdinocillin | CHEBI:6999 | PBP2-targeting perturbation of Rod complex | Lakey 2023 (lakey2023theroleof pages 2-4) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Chemicals/perturbations | fosfomycin | CHEBI:28915 | MurA inhibitor altering wall synthesis state | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 |
| Chemicals/perturbations | arabinose induction of minE | label-only | experimental increase of MinE/MinD ratio | Vashistha 2023 (vashistha2023bacterialcellsizechanges pages 8-9) | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 |
| Chemicals/perturbations | morphology engineering of ftsZ/minC/minD/mreB targets | label-only | applied rewiring of length for PHA accumulation | Kalia 2024 (kalia2024manipulatingmicrobialcell pages 4-5, kalia2024manipulatingmicrobialcell pages 1-2) | 10.3390/polym16030410 | https://doi.org/10.3390/polym16030410 | Feb 2024 |
| Environmental/experimental factors | high osmotic support / L-form conditions | ENVO:01000335 | reveals division control independent of sidewall growth | Hayashi 2024 (hayashi2024septalwallsynthesis pages 1-2) | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 |
| Environmental/experimental factors | acidic pH | ENVO:09200014 | environmental cue selecting alternative growth modules | Chung 2024 (chung2024singlecellimagingof pages 7-8) | 10.1038/s41564-024-01846-z | https://doi.org/10.1038/s41564-024-01846-z | Nov 2024 |
| Environmental/experimental factors | fast-growth conditions | label-only | context where Min-dependent size effects were measured | Vashistha 2023 (vashistha2023bacterialcellsizechanges pages 1-2) | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 |
| Environmental/experimental factors | nutrient/industrial production conditions | label-only | context for morphology engineering in PHA production | Kalia 2024 (kalia2024manipulatingmicrobialcell pages 1-2) | 10.3390/polym16030410 | https://doi.org/10.3390/polym16030410 | Feb 2024 |
| Assays/measurement platforms | mother machine microfluidics | label-only | long-term single-cell length and division tracking | Thiermann 2024 (thiermann2024toolsandmethods pages 1-3) | 10.7554/elife.88463 | https://doi.org/10.7554/elife.88463 | Apr 2024 |
| Assays/measurement platforms | napari-MM3 image analysis pipeline | label-only | segmentation/extraction of size and timing traits | Thiermann 2024 (thiermann2024toolsandmethods pages 1-3) | 10.7554/elife.88463 | https://doi.org/10.7554/elife.88463 | Apr 2024 |
| Assays/measurement platforms | imaging flow cytometry (IFC) | label-only | distinguishes elongation from chaining with images | Tian 2023 (tian2023cellsortingdirectedselection pages 1-2, tian2023cellsortingdirectedselection pages 4-7) | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 |
| Assays/measurement platforms | fluorescence-activated cell sorting (FACS) | label-only | enriches size/shape variants by optical gates | Tian 2023 (tian2023cellsortingdirectedselection pages 1-2) | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 |
| Assays/measurement platforms | widefield fluorescence microscopy + MicrobeJ | label-only | quantifies constriction positions and cell shape parameters | Lakey 2023 (lakey2023theroleof pages 2-4) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Assays/measurement platforms | cryo-EM / cryo-ET | label-only | resolves envelope constriction defects linked to length | Lakey 2023 (lakey2023theroleof pages 1-2) | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 |
| Assays/measurement platforms | time-lapse microfluidic imaging with pole annotation | label-only | direct pole-to-pole cell length measurement | Chung 2024 (chung2024singlecellimagingof pages 7-8) | 10.1038/s41564-024-01846-z | https://doi.org/10.1038/s41564-024-01846-z | Nov 2024 |


*Table: This table lists candidate TraitMech nodes for microbial cell length, grouped across phenotype, process, molecular, environmental, chemical, and assay categories. It is designed to support curation of a causal graph by linking each node to a recent supporting source and suggested grounding.*

## 4) Evidence-backed candidate causal edges (triples)

The table below is designed to be directly curatable as candidate edges for `data/traits/morphology/cell_length.yaml`.

| Subject node (grounding) | Predicate (causal) | Object node (grounding) | Direction/Sign | Evidence snippet (verbatim) | Source (first author year) | DOI | URL | Publication date (month/year) | Notes/uncertainty |
|---|---|---|---|---|---|---|---|---|---|
| CenKR two-component system (label-only; CenK/CenR) | decreases | Pal mobility (Tol-Pal outer membrane lipoprotein; Pal) | increase CenKR activity -> decrease | “increased CenKR activity decreases the mobility of Pal, delaying OM constriction” (lakey2023theroleof pages 1-2) | Lakey 2023 | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 | Direct regulatory/mechanistic statement in *Rhodobacter sphaeroides*; taxon-specific but strong. |
| Pal / Tol-Pal system (Pal; TolQRA-TolB-Pal complex) | enables | outer membrane constriction | positive | “TolQRA–TolB–Pal interactions normally release Pal to populate the septum and bind PG, enabling OM constriction via Pal–PG interactions.” (lakey2023theroleof pages 1-2) | Lakey 2023 | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 | Supports envelope-constriction node upstream of division completion/length. |
| Delayed outer membrane constriction | disrupts | midcell positioning of MreB and FtsZ (MreB/FtsZ) | increase delay -> decrease proper positioning | “ultimately disrupt[s] the midcell positioning of MreB and FtsZ and interfer[es] with the spatial regulation of PG synthesis and remodeling.” (lakey2023theroleof pages 1-2) | Lakey 2023 | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 | Good causal bridge from envelope mechanics to cytoskeletal localization. |
| Increased CenKR activity (label-only) | causes | filamentation and chaining | increase | “overexpression of cenK causes cell filamentation and chaining.” (lakey2023theroleof pages 1-2) | Lakey 2023 | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 | Phenotype edge directly relevant to increased apparent cell length. |
| MinE overexpression / increased MinE:MinD ratio (Min system) | delays | initiation of FtsZ ring formation (Z-ring) | increase MinE -> increase delay | “overexpressing minE (increasing MinE/MinD ratio) causes a gradual increase in cell size to a new steady state and delays the initiation of FtsZ ring formation.” (vashistha2023bacterialcellsizechanges pages 1-2) | Vashistha 2023 | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 | Strong single-cell evidence in *E. coli*. |
| Min system ratio/oscillations (MinC/MinD/MinE) | modulates | FtsZ membrane accumulation/localization | altered ratio disrupts accumulation | “The delay is proposed to result from Min oscillations disrupting FtsZ accumulation at the membrane” (vashistha2023bacterialcellsizechanges pages 1-2) | Vashistha 2023 | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 | Mechanistic interpretation from same study; curate as supported but partly model-based. |
| Delayed FtsZ ring formation | increases | cell size/cell length at division | increase | “Changes in the relative concentrations of Min proteins can disrupt FtsZ binding to the membrane, which in turn can delay cell division until a certain cell size is reached” (vashistha2023bacterialcellsizechanges pages 1-2) | Vashistha 2023 | 10.1038/s41467-023-41487-0 | https://doi.org/10.1038/s41467-023-41487-0 | Sep 2023 | Direct link from division timing to resulting size/length. |
| FtsZ (GO: bacterial-type cell division protein) | organizes/recruits | divisome proteins | positive | “FtsZ is described as the master organizer that assembles into a Z ring required for localization of all other divisome proteins” (cameron2024insightsintothe pages 1-3) | Cameron 2024 | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 | Review, authoritative; useful for generic graph backbone. |
| FtsA and ZipA (proto-ring tethers) | attach | FtsZ to membrane | positive | “its membrane attachment depends on tethers FtsA and ZipA (the proto-ring).” (cameron2024insightsintothe pages 1-3) | Cameron 2024 | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 | Good generic divisome assembly edge. |
| Recruitment cascade FtsK→FtsQ/FtsL/FtsB→FtsW→FtsI→FtsN | brings/activates | septal PG synthases FtsW and FtsI (FtsWI) | positive | “a defined recruitment cascade (FtsK→FtsQ/FtsL/FtsB→FtsW→FtsI→FtsN) brings essential septal peptidoglycan synthases FtsW and FtsI (FtsWI) that drive septum synthesis” (cameron2024insightsintothe pages 1-3) | Cameron 2024 | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 | Supports curated process node: divisome assembly -> sPG synthesis. |
| FtsWI septal PG synthesis complex (FtsW/FtsI) | drives | septum synthesis / division constriction | positive | “essential septal peptidoglycan synthases FtsW and FtsI (FtsWI) that drive septum synthesis” (cameron2024insightsintothe pages 1-3) | Cameron 2024 | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 | Central division-to-length edge. |
| Inactivation of essential divisome proteins | blocks | division, altering cell length | decrease division -> increase length | “inactivation of any of these blocks division, altering cell length.” (cameron2024insightsintothe pages 1-3) | Cameron 2024 | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 | Review-level synthesis; suitable for phenotype edge. |
| Min system and nucleoid occlusion | determine | division site placement via localized negative regulation of FtsZ polymerization | positive for correct placement | “Spatial regulators — the Min system and nucleoid occlusion (NO) — act as localized negative regulators of FtsZ polymerization and thus determine division site placement” (cameron2024insightsintothe pages 1-3) | Cameron 2024 | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 | Good generic edge for positioning branch. |
| Min system inactivation | yields | polar divisions and minicells | decrease proper placement | “Min inactivation yields polar divisions and minicells.” (cameron2024insightsintothe pages 1-3) | Cameron 2024 | 10.1038/s41579-023-00942-x | https://doi.org/10.1038/s41579-023-00942-x | Jul 2024 | Boundary-case phenotype; more about position than length, but relevant. |
| Rod complex / elongasome (MreB, RodZ, PBP2) | mediates | elongation | positive | “elongation is mediated by the Rod complex (the elongasome)” (hayashi2024septalwallsynthesis pages 1-2) | Hayashi 2024 | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 | Strong recent summary of elongasome role. |
| MreB, RodZ, and PBP2 | maintain | normal cell shape | positive | “MreB (a scaffold for the Rod complex), RodZ, and PBP2 are causally implicated in maintaining normal cell shape; their perturbation yields abnormal shapes.” (hayashi2024septalwallsynthesis pages 1-2) | Hayashi 2024 | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 | Shape/length link is indirect but useful; recent source. |
| Rod complex / elongasome | performs | sidewall peptidoglycan synthesis | positive | “a multi-protein complex called the elongasome that drives sidewall peptidoglycan synthesis necessary for the maintenance of rod shape and the lengthening of the cell prior to division.” (lakey2023theroleof pages 18-19) | Harpring 2023 | 10.3389/fcimb.2023.1205488 | https://doi.org/10.3389/fcimb.2023.1205488 | Oct 2023 | Good explicit sidewall PG -> lengthening statement. |
| Sidewall peptidoglycan synthesis | promotes | cell lengthening prior to division | positive | “drives sidewall peptidoglycan synthesis necessary for the maintenance of rod shape and the lengthening of the cell prior to division.” (lakey2023theroleof pages 18-19) | Harpring 2023 | 10.3389/fcimb.2023.1205488 | https://doi.org/10.3389/fcimb.2023.1205488 | Oct 2023 | Direct process-to-trait edge. |
| MreB | organizes | lateral PG insertion / elongation | positive | “MreB polymerization into protofilaments organizes lateral PG insertion (MreB is ‘the major protein responsible for elongation’)” (sichangi2023geneticeventsresponsible pages 28-32) | Sichangi 2023 | n/a | n/a | 2023 | **Uncertain**: source journal/status unclear in retrieved context. |
| mreB deletion | causes | spherical cells / loss of elongation | decrease elongation | “deletion of mreB yields spherical cells.” (sichangi2023geneticeventsresponsible pages 28-32) | Sichangi 2023 | n/a | n/a | 2023 | **Uncertain**: useful but from unknown-journal text. |
| RodA–PBP2 complex | acts as core synthase for | elongation peptidoglycan synthesis | positive | “RodA–PBP2 is proposed as the core PG synthase for elongation” (sichangi2023geneticeventsresponsible pages 28-32) | Sichangi 2023 | n/a | n/a | 2023 | **Uncertain**: mark as tentative until confirmed from primary literature. |
| MreC | regulates/links | RodA–PBP2 elongation machinery | positive | “MreC regulates/links these components.” (sichangi2023geneticeventsresponsible pages 28-32) | Sichangi 2023 | n/a | n/a | 2023 | **Uncertain**. |
| AmiC amidase | cleaves | septum during cell division | positive | “amiC encodes an N-acetylmuramyl-L-alanine amidase ‘involved in septum cleavage during cell division,’” (tian2023cellsortingdirectedselection pages 4-7) | Tian 2023 | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 | Strong phenotype-selection paper with direct imaging support. |
| amiC truncation / loss of function | causes | long unseparated chains | increase apparent length | “a truncation (E382*) correlated with long unseparated chains.” (tian2023cellsortingdirectedselection pages 4-7) | Tian 2023 | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 | Important boundary case: chaining vs single-cell elongation. |
| Incomplete septum cleavage / membrane separation defect | causes | increased apparent cell length by chaining | increase | “chained cells were connected without separation of the cell membrane,” (tian2023cellsortingdirectedselection pages 4-7) | Tian 2023 | 10.3390/ijms24043243 | https://doi.org/10.3390/ijms24043243 | Feb 2023 | Useful assay warning: not true single-cell elongation. |
| Cephalexin (CHEBI label-only; β-lactam) | inhibits | division / FtsI-associated septal PG synthesis | decrease division -> increase length | “Antibiotic perturbation (FtsI inhibitor cephalexin) similarly blocks division and causes longitudinal MreB polymerization and filamentation.” (lakey2023theroleof pages 18-19) | Lakey 2023 | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 | Good drug-to-phenotype edge; taxon in source is *R. sphaeroides*. |
| Cephalexin | causes | filamentation | increase | “FtsI inhibitor cephalexin … blocks division and causes longitudinal MreB polymerization and filamentation.” (lakey2023theroleof pages 18-19) | Lakey 2023 | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 | Direct phenotype effect on apparent cell length. |
| Fosfomycin (CHEBI label-only) | inhibits | MurA / peptidoglycan synthesis | decrease PG synthesis | “specific antibiotics act causally (Fos inhibits MurA; PenG and Cef inhibit PBPs/PBP1A/B) to reduce peptidoglycan synthesis.” (hayashi2024septalwallsynthesis pages 1-2) | Hayashi 2024 | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 | Useful chemical-process edge; phenotype effect may be context dependent (L-forms/high osmotic support). |
| Reduced peptidoglycan synthesis | blocks | proliferation and can produce L-forms / abnormal size-shape states | decrease proliferation | “Inhibiting cell-wall synthesis blocks proliferation and can produce L-forms” (hayashi2024septalwallsynthesis pages 1-2) | Hayashi 2024 | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 | Indirect to length; not a clean general edge for routine curation. |
| A22 (MreB inhibitor; CHEBI label-only) | reduces | MreB motion/velocity | decrease | “MreB dynamics depend on PG precursor availability and new PG synthesis … and are sensitive to A22 (reduced MreB velocity)” (sichangi2023geneticeventsresponsible pages 28-32) | Sichangi 2023 | n/a | n/a | 2023 | **Uncertain**: source unclear; pharmacology plausible but confirm with primary paper before curation. |
| Reduced MreB motion | decreases | elongation / proper rod-like growth | decrease | “MreB polymerization into protofilaments organizes lateral PG insertion” (sichangi2023geneticeventsresponsible pages 28-32) | Sichangi 2023 | n/a | n/a | 2023 | **Uncertain** inference chained from same unknown-journal source. |
| Mecillinam / amdinocillin (PBP2-targeting β-lactam; CHEBI label-only) | perturbs | elongasome / PBP2-dependent growth | decrease | “Perturbations used include sub-MIC A22 (MreB inhibitor) and amdinocillin/mecillinam (PBP2-targeting), useful for dissecting elongasome versus divisome contributions.” (lakey2023theroleof pages 2-4) | Lakey 2023 | 10.1128/mbio.00631-23 | https://doi.org/10.1128/mbio.00631-23 | Jun 2023 | Evidence is experimental-usage oriented; phenotype direction on length not explicitly stated here. |
| FtsZ-dependent division with Min or nucleoid occlusion support | produces | more uniform cell shape/size even without cylindrical wall synthesis | positive | “This FtsZ-dependent control of cell shape and size in the absence of a cell wall requires at least either the Min or nucleoid occlusion systems for positioning FtsZ at mid cell division sites.” (hayashi2024septalwallsynthesis pages 1-2) | Hayashi 2024 | 10.1038/s42003-024-07279-y | https://doi.org/10.1038/s42003-024-07279-y | Nov 2024 | Context-specific to L-forms; useful but should be curated cautiously. |


*Table: This table lists curation-ready candidate causal edges for microbial cell length control, grounded in recent literature where possible and annotated with evidence, dates, and uncertainty. It emphasizes elongation, division, septation, and antibiotic perturbation mechanisms most directly relevant to TraitMech graph construction.*

## 5) Recent developments and latest research (prioritize 2023–2024)

### 5.1 Division-site regulation links spatial dynamics to cell length (Min → FtsZ timing → length)
- In *E. coli*, altering **relative Min protein expression** (e.g., **minE overexpression**) causes a **gradual increase in cell size** to a new steady state and **delays initiation of FtsZ ring formation**, a direct mechanistic route to increased length at division (vashistha2023bacterialcellsizechanges pages 1-2). 
- Supporting visual evidence: the Vashistha et al. paper includes figures showing population-level and single-cell time series of cell size changes and stable Z-ring size thresholds after minE induction (vashistha2023bacterialcellsizechanges media 1315a8c2, vashistha2023bacterialcellsizechanges media 9ba503f6).

### 5.2 Updated divisome assembly view (authoritative 2024 synthesis)
- A 2024 Nature Reviews Microbiology synthesis frames **FtsZ** as the master organizer; membrane tethering by **FtsA/ZipA** and a recruitment cascade that brings **FtsW/FtsI (FtsWI)** for septal synthesis provides a modular scaffold for curating “division completion limits length” edges (cameron2024insightsintothe pages 1-3).

### 5.3 Cell length measurement is scaling up; segmentation bias is now a recognized confound (2024 methods)
- High-throughput mother machine imaging can track **thousands of trapped single cells** over **hundreds of generations**, but extracted size/length parameters can be **systematically altered by thresholding choices** and **training-data pixel-level variation** (thiermann2024toolsandmethods pages 1-3).
- Quantitative robustness/sensitivity: reported segmentation accuracy (Jaccard index) ~0.92–1.0 at IoU=0.6 (thiermann2024toolsandmethodsa pages 10-11, thiermann2024toolsandmethods pages 10-11), and a conservative **~10% lower bound** for absolute spatial uncertainty (thiermann2024toolsandmethodsa pages 14-16).

### 5.4 Beyond model rods: lineage-specific length dynamics (2024 Mtb)
- Single-cell microfluidic imaging of *Mycobacterium tuberculosis* shows **linear** growth at the single-cell level and heterogeneous pole usage (old/new/both poles), implying different mechanistic constraints on length control compared with canonical exponential-growth rods (chung2024singlecellimagingof pages 1-2).

## 6) Current applications and real-world implementations

### 6.1 Biotechnology: morphology/length engineering for intracellular polymer production and recovery (2024)
- A 2024 Polymers review synthesizes industrially motivated “morphology engineering” where manipulating division/elongation genes (e.g., **ftsZ**, **minC/minD**, **mreB**, **rodZ**) yields enlarged or filamentous cells to increase intracellular capacity and lower recovery costs (kalia2024manipulatingmicrobialcell pages 4-5, kalia2024manipulatingmicrobialcell pages 1-2).
- Reported quantitative outcomes include:
  - **PHB accumulation showed 100% increase** under filamentation/enlargement strategies (kalia2024manipulatingmicrobialcell pages 7-8).
  - Weakening cell walls via genetic edits is reported to increase PHB accumulation **up to ~4-fold** (kalia2024manipulatingmicrobialcell pages 5-7).
  - PHA granules reported **up to 10 µm** in an engineered *Halomonas bluephagenesis* strain (kalia2024manipulatingmicrobialcell pages 7-8).
  - PHA production levels reaching **~70% DCW** (dry cell weight) in engineered systems used for recovery workflows (kalia2024manipulatingmicrobialcell pages 9-11).

### 6.2 Antimicrobial development: division as a drug target (FtsZ)
- A 2023 review emphasizes FtsZ as a conserved division protein and an attractive antibiotic target, but highlights that species-specific differences in FtsZ function and partners can alter translation of anti-FtsZ strategies and that mechanisms of action need clarification across taxa (battaje2023modelsversuspathogens pages 1-3).

## 7) Relevant statistics and data (selected 2023–2024 quantitative points)

### Cell-size control statistics from recent quantitative/theory papers
- A 2024 Physical Review Research paper modeling microfluidic single-cell size/length data treats division as threshold crossing of log fold change with an approximately Gaussian threshold (mean ≈ ln 2, **σφ = 0.17**), weak inter-cycle dependence (correlation coefficient ≈ **−0.02**), and best-fit negative correlation with birth size (slope **β = 0.65**) (biswas2024universalityofphenotypic pages 1-2).
- A 2023 Physical Review E paper reports distinct correlation timescales in mother-machine vs sister-lineage analysis (birth-size ACF nA ≈ **1 generation**; sister-lineage PCF nP ≈ **3.5 generations**), motivating models with longer-lived inherited components (elgamel2023multigenerationalmemoryin pages 1-2).

### Measurement/analysis robustness statistics (2024 mother-machine methods)
- Segmentation evaluation: Jaccard index values **0.98, 0.98, 1.0** on three datasets and **0.92** on another (IoU threshold 0.6) (thiermann2024toolsandmethodsa pages 10-11, thiermann2024toolsandmethods pages 10-11).
- Practical uncertainty bounds: typical pixel scale ~0.065 µm at 100× and a conservative **~10%** lower bound on absolute spatial uncertainty for size/length measurements (thiermann2024toolsandmethodsa pages 14-16).

## 8) Expert synthesis: mechanistic “levers” most suitable for TraitMech curation

Based on the strongest 2023–2024 evidence assembled here, the most **curation-ready** mechanistic levers for microbial cell length are:
1. **Division timing lever**: Min system → FtsZ ring initiation delay → increased length at division (vashistha2023bacterialcellsizechanges pages 1-2).
2. **Division machinery lever**: divisome recruitment cascade → FtsWI septal PG synthesis → division completion (limits length) (cameron2024insightsintothe pages 1-3).
3. **Elongation lever**: elongasome/sidewall PG synthesis → lengthening prior to division (harpring2023plasticityinthe pages 1-2, hayashi2024septalwallsynthesis pages 1-2).
4. **Separation lever**: amidase-mediated septum cleavage (AmiC) → prevents chaining-based apparent length increases (tian2023cellsortingdirectedselection pages 4-7).
5. **Envelope coupling lever (taxon-specific)**: Tol-Pal/Pal dynamics and CenKR regulation → OM/PG constriction defects → filamentation/chaining (lakey2023theroleof pages 1-2).

## 9) Curation warnings (claims to qualify or avoid)

> - Do not equate **chaining** with true single-cell elongation: long apparent “cells” may be unseparated daughter chains caused by septum-cleavage defects (for example, **amiC** truncation), so chaining-derived length phenotypes should be curated separately from bona fide filamentation or pole-to-pole cell elongation. (tian2023cellsortingdirectedselection pages 4-7, tian2023cellsortingdirectedselection pages 1-2)
> - Treat morphology values from image analysis as **assay-sensitive**: mother-machine analyses are robust at the level of major correlations, but small thresholding changes can systematically shift extracted size parameters, and a conservative lower bound of about **~10% absolute spatial uncertainty** is recommended for typical imaging setups. (thiermann2024toolsandmethods pages 1-3, thiermann2024toolsandmethodsa pages 14-16, thiermann2024toolsandmethodsa pages 10-11)
> - Mark **Tol-Pal / CenKR / Pal mobility -> filamentation** edges as **taxon-specific** unless generalized by additional evidence; the strongest support here is from *Rhodobacter sphaeroides* and related α-proteobacterial envelope biology rather than a universal bacterial mechanism. (lakey2023theroleof pages 1-2)
> - Mark **Mycobacterium tuberculosis** growth-mode claims as **lineage-specific**: recent single-cell work reports **linear**, heterogeneous, and pole-variable growth in Mtb, which should not be directly projected onto canonical rod models such as *E. coli* or *B. subtilis*. (chung2024singlecellimagingof pages 7-8, chung2024singlecellimagingof pages 1-2)
> - Use caution when curating **adder/sizer** statements into mechanistic graphs: recent 2024 modeling argues that no single mechanism explains all slow-growth *E. coli* data, and different regimes may be better explained by degradation, size-dependent accumulation, or commitment-size models. (nieto2024mechanismsofcell pages 6-7, nieto2024mechanismsofcell pages 1-2)
> - Treat claims sourced from **Sichangi 2023** as **low-confidence / uncertain** until independently confirmed in primary literature, because the retrieved source metadata indicates an unknown journal/publication context despite biologically plausible content on MreB, RodA-PBP2, MraZ, RapZ, and BolA. (sichangi2023geneticeventsresponsible pages 28-32, sichangi2023geneticeventsresponsible pages 45-49)


*Blockquote: This blockquote lists the main issues that should limit or qualify TraitMech curation of microbial cell length. It highlights phenotype misclassification risks, measurement bias, lineage-specific mechanisms, and low-confidence literature that should be flagged as uncertain.*

## 10) DOI-first bibliography (recent, authoritative; with URLs and dates)

1. Cameron TA, Margolin W. **Insights into the assembly and regulation of the bacterial divisome.** *Nature Reviews Microbiology* (Jul 2024). DOI: **10.1038/s41579-023-00942-x**. https://doi.org/10.1038/s41579-023-00942-x (cameron2024insightsintothe pages 1-3)
2. Thiermann R, et al. **Tools and methods for high-throughput single-cell imaging with the mother machine.** *eLife* (Apr 2024). DOI: **10.7554/eLife.88463**. https://doi.org/10.7554/elife.88463 (thiermann2024toolsandmethods pages 1-3)
3. Vashistha H, et al. **Bacterial cell-size changes resulting from altering the relative expression of Min proteins.** *Nature Communications* (Sep 2023). DOI: **10.1038/s41467-023-41487-0**. https://doi.org/10.1038/s41467-023-41487-0 (vashistha2023bacterialcellsizechanges pages 1-2)
4. Lakey BD, et al. **The role of CenKR in the coordination of Rhodobacter sphaeroides cell elongation and division.** *mBio* (Jun 2023). DOI: **10.1128/mbio.00631-23**. https://doi.org/10.1128/mbio.00631-23 (lakey2023theroleof pages 1-2)
5. Hayashi M, et al. **Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in Escherichia coli L-forms.** *Communications Biology* (Nov 2024). DOI: **10.1038/s42003-024-07279-y**. https://doi.org/10.1038/s42003-024-07279-y (hayashi2024septalwallsynthesis pages 1-2)
6. Harpring M, Cox JV. **Plasticity in the cell division processes of obligate intracellular bacteria.** *Frontiers in Cellular and Infection Microbiology* (Oct 2023). DOI: **10.3389/fcimb.2023.1205488**. https://doi.org/10.3389/fcimb.2023.1205488 (harpring2023plasticityinthe pages 1-2)
7. Castanheira S, García-del Portillo F. **Evidence of two differentially regulated elongasomes in Salmonella.** *Communications Biology* (Sep 2023). DOI: **10.1038/s42003-023-05308-w**. https://doi.org/10.1038/s42003-023-05308-w (castanheira2023evidenceoftwo pages 1-2)
8. Chung ES, et al. **Single-cell imaging of the Mycobacterium tuberculosis cell cycle reveals linear and heterogenous growth.** *Nature Microbiology* (Nov 2024). DOI: **10.1038/s41564-024-01846-z**. https://doi.org/10.1038/s41564-024-01846-z (chung2024singlecellimagingof pages 1-2)
9. Nieto C, et al. **Mechanisms of cell size regulation in slow-growing Escherichia coli cells: discriminating models beyond the adder.** *npj Systems Biology and Applications* (May 2024). DOI: **10.1038/s41540-024-00383-z**. https://doi.org/10.1038/s41540-024-00383-z (nieto2024mechanismsofcell pages 1-2)
10. Biswas K, Brenner N. **Universality of phenotypic distributions in bacteria.** *Physical Review Research* (May 2024). DOI: **10.1103/PhysRevResearch.6.L022043**. https://doi.org/10.1103/physrevresearch.6.l022043 (biswas2024universalityofphenotypic pages 1-2)
11. ElGamel M, et al. **Multigenerational memory in bacterial size control.** *Physical Review E* (Sep 2023). DOI: **10.1103/PhysRevE.108.L032401**. https://doi.org/10.1103/physreve.108.l032401 (elgamel2023multigenerationalmemoryin pages 1-2)
12. Tian D, et al. **Cell Sorting-Directed Selection of Bacterial Cells in Bigger Sizes Analyzed by Imaging Flow Cytometry during Experimental Evolution.** *International Journal of Molecular Sciences* (Feb 2023). DOI: **10.3390/ijms24043243**. https://doi.org/10.3390/ijms24043243 (tian2023cellsortingdirectedselection pages 1-2)
13. Kalia VC, et al. **Manipulating Microbial Cell Morphology for the Sustainable Production of Biopolymers.** *Polymers* (Feb 2024). DOI: **10.3390/polym16030410**. https://doi.org/10.3390/polym16030410 (kalia2024manipulatingmicrobialcell pages 1-2)
14. Battaje RR, et al. **Models versus pathogens: how conserved is the FtsZ in bacteria?** *Bioscience Reports* (Feb 2023). DOI: **10.1042/BSR20221664**. https://doi.org/10.1042/bsr20221664 (battaje2023modelsversuspathogens pages 1-3)

---

## Notes for TraitMech YAML curation
- The artifacts above provide a **node list** (artifact-01) and an **edge list** with supporting snippets (artifact-00) suitable for porting into `cell_length.yaml` with uncertainty flags.
- Consider splitting the trait graph into two linked subgraphs: (i) **elongation/sidewall insertion** and (ii) **division/septation/separation**, with explicit assay nodes for mother-machine vs IFC/FACS vs agar-pad microscopy.


References

1. (chung2024singlecellimagingof pages 7-8): Eun Seon Chung, Prathitha Kar, Maliwan Kamkaew, Ariel Amir, and Bree B. Aldridge. Single-cell imaging of the mycobacterium tuberculosis cell cycle reveals linear and heterogenous growth. Nature Microbiology, 9:3332-3344, Nov 2024. URL: https://doi.org/10.1038/s41564-024-01846-z, doi:10.1038/s41564-024-01846-z. This article has 26 citations and is from a highest quality peer-reviewed journal.

2. (harpring2023plasticityinthe pages 1-2): McKenna Harpring and John V. Cox. Plasticity in the cell division processes of obligate intracellular bacteria. Frontiers in Cellular and Infection Microbiology, Oct 2023. URL: https://doi.org/10.3389/fcimb.2023.1205488, doi:10.3389/fcimb.2023.1205488. This article has 10 citations.

3. (cameron2024insightsintothe pages 1-3): Todd A. Cameron and William Margolin. Insights into the assembly and regulation of the bacterial divisome. Nature Reviews Microbiology, 22:33-45, Jul 2024. URL: https://doi.org/10.1038/s41579-023-00942-x, doi:10.1038/s41579-023-00942-x. This article has 134 citations and is from a highest quality peer-reviewed journal.

4. (hayashi2024septalwallsynthesis pages 1-2): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

5. (vashistha2023bacterialcellsizechanges pages 1-2): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

6. (thiermann2024toolsandmethods pages 1-3): Ryan Thiermann, Michael Sandler, Gursharan Ahir, John T. Sauls, Jeremy W. Schroeder, Steven D. Brown, Guillaume Le Treut, Fangwei Si, Dongyang Li, Jue D. Wang, and Suckjoon Jun. Tools and methods for high-throughput single-cell imaging with the mother machine. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.88463, doi:10.7554/elife.88463. This article has 32 citations and is from a domain leading peer-reviewed journal.

7. (tian2023cellsortingdirectedselection pages 4-7): Di Tian, Caiyan Wang, Yunfei Liu, Yueyue Zhang, Adriano Caliari, Hui Lu, Yang Xia, Boying Xu, Jian Xu, and Tetsuya Yomo. Cell sorting-directed selection of bacterial cells in bigger sizes analyzed by imaging flow cytometry during experimental evolution. International Journal of Molecular Sciences, 24:3243, Feb 2023. URL: https://doi.org/10.3390/ijms24043243, doi:10.3390/ijms24043243. This article has 6 citations.

8. (lakey2023theroleof pages 1-2): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

9. (chung2024singlecellimagingof pages 1-2): Eun Seon Chung, Prathitha Kar, Maliwan Kamkaew, Ariel Amir, and Bree B. Aldridge. Single-cell imaging of the mycobacterium tuberculosis cell cycle reveals linear and heterogenous growth. Nature Microbiology, 9:3332-3344, Nov 2024. URL: https://doi.org/10.1038/s41564-024-01846-z, doi:10.1038/s41564-024-01846-z. This article has 26 citations and is from a highest quality peer-reviewed journal.

10. (lakey2023theroleof pages 18-19): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (lakey2023theroleof pages 2-4): Bryan D. Lakey, François Alberge, Daniel Parrell, Elizabeth R. Wright, Daniel R. Noguera, and Timothy J. Donohue. The role of cenkr in the coordination of rhodobacter sphaeroides cell elongation and division. mBio, Jun 2023. URL: https://doi.org/10.1128/mbio.00631-23, doi:10.1128/mbio.00631-23. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (vashistha2023bacterialcellsizechanges pages 8-9): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

13. (kalia2024manipulatingmicrobialcell pages 4-5): Vipin C. Kalia, Sanjay K. S. Patel, Kugalur K. Karthikeyan, Marimuthu Jeya, In-Won Kim, and Jung-Kul Lee. Manipulating microbial cell morphology for the sustainable production of biopolymers. Polymers, 16:410, Feb 2024. URL: https://doi.org/10.3390/polym16030410, doi:10.3390/polym16030410. This article has 25 citations.

14. (kalia2024manipulatingmicrobialcell pages 1-2): Vipin C. Kalia, Sanjay K. S. Patel, Kugalur K. Karthikeyan, Marimuthu Jeya, In-Won Kim, and Jung-Kul Lee. Manipulating microbial cell morphology for the sustainable production of biopolymers. Polymers, 16:410, Feb 2024. URL: https://doi.org/10.3390/polym16030410, doi:10.3390/polym16030410. This article has 25 citations.

15. (tian2023cellsortingdirectedselection pages 1-2): Di Tian, Caiyan Wang, Yunfei Liu, Yueyue Zhang, Adriano Caliari, Hui Lu, Yang Xia, Boying Xu, Jian Xu, and Tetsuya Yomo. Cell sorting-directed selection of bacterial cells in bigger sizes analyzed by imaging flow cytometry during experimental evolution. International Journal of Molecular Sciences, 24:3243, Feb 2023. URL: https://doi.org/10.3390/ijms24043243, doi:10.3390/ijms24043243. This article has 6 citations.

16. (sichangi2023geneticeventsresponsible pages 28-32): SN Sichangi. Genetic events responsible for cell shape evolution in multicellular longitudinally dividing (muldi) oral cavity neisseriaceae. Unknown journal, 2023.

17. (vashistha2023bacterialcellsizechanges media 1315a8c2): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

18. (vashistha2023bacterialcellsizechanges media 9ba503f6): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

19. (thiermann2024toolsandmethodsa pages 10-11): Ryan Thiermann, Michael Sandler, Gursharan Ahir, John T Sauls, Jeremy Schroeder, Steven Brown, Guillaume Le Treut, Fangwei Si, Dongyang Li, Jue D Wang, and Suckjoon Jun. Tools and methods for high-throughput single-cell imaging with the mother machine. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.88463.4, doi:10.7554/elife.88463.4. This article has 1 citations and is from a domain leading peer-reviewed journal.

20. (thiermann2024toolsandmethods pages 10-11): Ryan Thiermann, Michael Sandler, Gursharan Ahir, John T. Sauls, Jeremy W. Schroeder, Steven D. Brown, Guillaume Le Treut, Fangwei Si, Dongyang Li, Jue D. Wang, and Suckjoon Jun. Tools and methods for high-throughput single-cell imaging with the mother machine. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.88463, doi:10.7554/elife.88463. This article has 32 citations and is from a domain leading peer-reviewed journal.

21. (thiermann2024toolsandmethodsa pages 14-16): Ryan Thiermann, Michael Sandler, Gursharan Ahir, John T Sauls, Jeremy Schroeder, Steven Brown, Guillaume Le Treut, Fangwei Si, Dongyang Li, Jue D Wang, and Suckjoon Jun. Tools and methods for high-throughput single-cell imaging with the mother machine. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.88463.4, doi:10.7554/elife.88463.4. This article has 1 citations and is from a domain leading peer-reviewed journal.

22. (kalia2024manipulatingmicrobialcell pages 7-8): Vipin C. Kalia, Sanjay K. S. Patel, Kugalur K. Karthikeyan, Marimuthu Jeya, In-Won Kim, and Jung-Kul Lee. Manipulating microbial cell morphology for the sustainable production of biopolymers. Polymers, 16:410, Feb 2024. URL: https://doi.org/10.3390/polym16030410, doi:10.3390/polym16030410. This article has 25 citations.

23. (kalia2024manipulatingmicrobialcell pages 5-7): Vipin C. Kalia, Sanjay K. S. Patel, Kugalur K. Karthikeyan, Marimuthu Jeya, In-Won Kim, and Jung-Kul Lee. Manipulating microbial cell morphology for the sustainable production of biopolymers. Polymers, 16:410, Feb 2024. URL: https://doi.org/10.3390/polym16030410, doi:10.3390/polym16030410. This article has 25 citations.

24. (kalia2024manipulatingmicrobialcell pages 9-11): Vipin C. Kalia, Sanjay K. S. Patel, Kugalur K. Karthikeyan, Marimuthu Jeya, In-Won Kim, and Jung-Kul Lee. Manipulating microbial cell morphology for the sustainable production of biopolymers. Polymers, 16:410, Feb 2024. URL: https://doi.org/10.3390/polym16030410, doi:10.3390/polym16030410. This article has 25 citations.

25. (battaje2023modelsversuspathogens pages 1-3): Rachana Rao Battaje, Ravikant Piyush, Vidyadhar Pratap, and Dulal Panda. Models versus pathogens: how conserved is the ftsz in bacteria? Bioscience Reports, Feb 2023. URL: https://doi.org/10.1042/bsr20221664, doi:10.1042/bsr20221664. This article has 27 citations and is from a peer-reviewed journal.

26. (biswas2024universalityofphenotypic pages 1-2): Kuheli Biswas and Naama Brenner. Universality of phenotypic distributions in bacteria. Physical Review Research, May 2024. URL: https://doi.org/10.1103/physrevresearch.6.l022043, doi:10.1103/physrevresearch.6.l022043. This article has 8 citations and is from a peer-reviewed journal.

27. (elgamel2023multigenerationalmemoryin pages 1-2): Motasem ElGamel, Harsh Vashistha, Hanna Salman, and Andrew Mugler. Multigenerational memory in bacterial size control. Sep 2023. URL: https://doi.org/10.1103/physreve.108.l032401, doi:10.1103/physreve.108.l032401. This article has 13 citations and is from a domain leading peer-reviewed journal.

28. (nieto2024mechanismsofcell pages 6-7): César Nieto, César Augusto Vargas-García, Juan Manuel Pedraza, and Abhyudai Singh. Mechanisms of cell size regulation in slow-growing escherichia coli cells: discriminating models beyond the adder. NPJ Systems Biology and Applications, May 2024. URL: https://doi.org/10.1038/s41540-024-00383-z, doi:10.1038/s41540-024-00383-z. This article has 12 citations.

29. (nieto2024mechanismsofcell pages 1-2): César Nieto, César Augusto Vargas-García, Juan Manuel Pedraza, and Abhyudai Singh. Mechanisms of cell size regulation in slow-growing escherichia coli cells: discriminating models beyond the adder. NPJ Systems Biology and Applications, May 2024. URL: https://doi.org/10.1038/s41540-024-00383-z, doi:10.1038/s41540-024-00383-z. This article has 12 citations.

30. (sichangi2023geneticeventsresponsible pages 45-49): SN Sichangi. Genetic events responsible for cell shape evolution in multicellular longitudinally dividing (muldi) oral cavity neisseriaceae. Unknown journal, 2023.

31. (castanheira2023evidenceoftwo pages 1-2): Sónia Castanheira and Francisco García-del Portillo. Evidence of two differentially regulated elongasomes in salmonella. Communications Biology, Sep 2023. URL: https://doi.org/10.1038/s42003-023-05308-w, doi:10.1038/s42003-023-05308-w. This article has 15 citations and is from a peer-reviewed journal.