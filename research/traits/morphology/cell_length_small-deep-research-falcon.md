---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T06:42:24.913242'
end_time: '2026-06-18T07:09:22.988399'
duration_seconds: 1618.08
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell length small
  trait_identifier: METPO:1000884
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_length_small
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-length phenotype in which the longer cell dimension lies approximately
    between 1.3 and 2 micrometers.
  parent_traits: METPO:1000881
  synonyms: L_1.3_2
  evidence_summary: 'DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount
    between divisions (Adder-model paper supports a defined inter-divisional length
    increment that produces a narrow length distribution at standard growth conditions.)'
  causal_graph_summary: 'cell_length_small_size_setpoint: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell length small
- **METPO identifier:** METPO:1000884
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 1.3 and 2 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_1.3_2
- **Existing evidence:** DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports a defined inter-divisional length increment that produces a narrow length distribution at standard growth conditions.)
- **Existing causal graph summary:** cell_length_small_size_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell length small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_small.yaml`.

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
- **Trait label:** cell length small
- **METPO identifier:** METPO:1000884
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-length phenotype in which the longer cell dimension lies approximately between 1.3 and 2 micrometers.
- **Parent traits:** METPO:1000881
- **Synonyms:** L_1.3_2
- **Existing evidence:** DOI:10.1016/j.cell.2014.11.022: cells grow by a fixed amount between divisions (Adder-model paper supports a defined inter-divisional length increment that produces a narrow length distribution at standard growth conditions.)
- **Existing causal graph summary:** cell_length_small_size_setpoint: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell length small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_length_small.yaml`.

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


## Curation-focused research report: Microbial trait “cell length small” (METPO:1000884)

### Scope summary (TraitMech curation)
**Trait definition.** METPO:1000884 (“cell length small”) is a **cell-length phenotype class** defined as having the **longer cell dimension approximately 1.3–2.0 μm** under the relevant assay/growth condition. This is most naturally interpreted for rod-shaped (or rod-capable) microbes where “length” corresponds to the long axis of the cell. 

**Boundary cases and nearby traits.**
- **Below-range short/coccoid states** (e.g., intracellular UPEC cocci) can yield lengths <1.3 μm and represent a different morphological regime (rod→coccus transition) rather than “small rods”; these should be curated only if TraitMech intends to include coccoid morphological transitions as causal routes to “small length”. Intracellular UPEC cocci were reported with average length ~0.88 ± 0.13 μm and intracellular UPEC were shorter than extracellular bacteria (1.3 ± 0.53 μm vs 2.59 ± 0.41 μm). (pokhrel2024e.colidivision pages 1-5)
- **Filamentation/elongation phenotypes** (e.g., Min perturbations leading to very long cells) are the opposite direction and better map to “cell length large/filamentous”. Min perturbation experiments include cell-length axes extending to ~20 μm, indicating extreme elongation under some conditions. (vashistha2023bacterialcellsizechanges pages 2-3)
- **Assay/measurement confounders**: microfluidic confinement, shear, and segmentation choices can bias extracted lengths, especially near channel openings or if models are not retrained on representative data. (thiermann2024toolsandmethods pages 10-11, yokoyama2024capturingofextracellular pages 1-2)

### Key concepts & current understanding (mechanistic framing)
#### 1) Phenomenological size-control models (adder vs sizer-like) and “small length”
**Adder (canonical balanced growth):** Adder control is commonly defined as cells adding a constant size increment between birth and division (added size independent of birth size). (nieto2024bacterialcellsize pages 5-7, nieto2024ageneralizedadder pages 1-2)

**Sider-like behavior under slow growth:** In *E. coli* under poor media/slow growth, the adder can break, and cells can become **smaller** and follow a **sizer-like strategy** in which added size is inversely related to birth size (i.e., small-born cells add more, large-born cells add less). (nieto2024mechanismsofcell pages 1-2)

**Mechanistic hypotheses proposed for sizer-like behavior:** Nieto et al. (2024) propose mechanistic classes in which division is tied to **FtsZ accumulation**, including possibilities such as **FtsZ degradation** and size-dependent accumulation/commitment-size effects that become more visible in **smaller cells**. (nieto2024mechanismsofcell pages 1-2, nieto2024mechanismsofcell pages 6-7, nieto2024mechanismsofcell pages 4-6)

#### 2) Division machinery as causal levers for cell length setpoints
**FtsZ-centered divisome assembly:** A recent authoritative review describes **FtsZ as the central organizer** of the divisome; it polymerizes into a **Z ring** whose assembly is required for localization of downstream divisome proteins, and which provides a dynamic framework for septal synthesis. (cameron2024insightsintothe pages 1-3)

**Rate-limiting factors for constriction onset:** Männik et al. (2024) experimentally upregulated division proteins and concluded that, in *E. coli*, **FtsZ numbers are one rate-limiting factor for cell division**, whereas FtsN and FtsA are not rate-limiting at physiological upregulation ranges (though they can affect division at higher overexpression levels). (mannik2024determiningtheratelimiting pages 1-2)

**Self-enhancing feedback between septal PG synthesis and Z-ring condensation:** Gong et al. (2024) report that septal cell wall synthesis can **feed back to promote Z ring condensation and stability**, describing a positive-feedback architecture involving FtsN and septal PG synthesis processing/recruitment loops. (gong2024thedivisomeis pages 1-3)

#### 3) Spatial regulators that modulate division timing and length
**Min system effects on division timing and size:** Vashistha et al. (2023) report that **FtsZ localization depends on membrane-associated Min proteins**, and that changes in Min protein relative concentration can disrupt FtsZ membrane binding, delaying division until a larger size is reached. Their study emphasizes that increasing MinE/MinD ratio can delay FtsZ ring formation and increase cell size to a new steady state. (vashistha2023bacterialcellsizechanges pages 1-2)

**Min and nucleoid occlusion in wall-deficient contexts:** For wall-less *E. coli* L-forms, FtsZ-dependent division producing uniform oval shapes requires division-site placement systems (Min and/or nucleoid occlusion) to position FtsZ at midcell. (hayashi2024septalwallsynthesis pages 7-8)

### Recent developments (2023–2024 prioritized)
1) **Slow-growth size-control mechanisms beyond the adder (2024):** Nieto et al. (NPJ Syst Biol Appl, May 2024) provide a framework to discriminate candidate mechanisms for the **sizer-like behavior** observed in slow-growing *E. coli* and explicitly connect poor media to **smaller cells** and altered division-size regulation. URL: https://doi.org/10.1038/s41540-024-00383-z (published May 2024). (nieto2024mechanismsofcell pages 1-2)

2) **Quantitative perturbation of divisome component abundance (2024):** Männik et al. (Nat Commun, Nov 2024) identify **FtsZ abundance as rate-limiting** for division timing and refine the model in which constriction onset is not simply limited by FtsN arrival. URL: https://doi.org/10.1038/s41467-024-54242-w (published Nov 2024). (mannik2024determiningtheratelimiting pages 1-2)

3) **Divisome positive-feedback architectures (2024):** Gong et al. (Nat Commun, Sep 2024) propose the divisome as a **self-enhancing machine**, where septal synthesis and Z-ring condensation reinforce each other. URL: https://doi.org/10.1038/s41467-024-52217-5 (published Sep 2024). (gong2024thedivisomeis pages 1-3)

4) **Host-associated size reduction via division–growth imbalance (2024):** Pokhrel et al. (bioRxiv, Jul 2024) show intracellular UPEC transitioning to short cocci because **division outpaces growth**, yielding strongly reduced lengths (reported statistics below). URL: https://doi.org/10.1101/2024.04.08.588611 (posted Jul 2024). (pokhrel2024e.colidivision pages 1-5)

5) **Microfluidic single-cell measurements and analysis robustness (2024):** Thiermann et al. (eLife, Apr 2024) benchmark mother-machine image-analysis pipelines and show that **adder correlations and length-derived parameters** can be robust across methods, while also highlighting systematic segmentation error modes and generalization pitfalls. URL: https://doi.org/10.7554/eLife.88463 (published Apr 2024). (thiermann2024toolsandmethods pages 10-11)

6) **Antibiotic-associated small length changes in controlled microfluidics (2024):** Yokoyama et al. (Lab Chip, Feb 2024) report polymyxin-B-associated modest length decreases in single trapped *E. coli*, and discuss confinement/shear as possible confounders. URL: https://doi.org/10.1039/d3lc00707c (published Feb 2024). (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 6-7)

### Current applications and real-world implementations
#### A) Microfluidics + quantitative microscopy as a standard assay for “cell length small”
Mother-machine style devices enable **long-term tracking** of single-cell growth and division under controlled conditions, yielding length-at-birth, length-at-division, and added-length (Δ) distributions used to infer adder/sizer-like behavior. (thiermann2024toolsandmethods pages 10-11)

**Assay implementation detail:** segmentation can be 1D or 2D, with 1D methods adequate under tight confinement, while errors near channel openings can bias measures. These are direct considerations for curating edges involving “assay: microfluidics” and “measurement bias” nodes. (thiermann2024toolsandmethods pages 10-11)

#### B) Antibiotics and envelope stress as practical perturbations that modulate length
Yokoyama et al. use on-chip single-cell culture and show **polymyxin B** produced small but quantifiable decreases in length at tested concentrations, while doubling time was “almost not affected,” suggesting morphological changes can occur without gross growth-rate change in some regimes. (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 6-7)

**Visual evidence:** the length-vs-polymyxin-B relationship and microfluidic assay readouts are presented in the source figure panel (yokoyama2024capturingofextracellular media 0a26e6cd, yokoyama2024capturingofextracellular media 661119d7).

#### C) Infection biology: intracellular niche can drive “small length” states
Pokhrel et al. report that within intracellular bacterial communities, **division frequency outpaces growth**, producing shorter, coccoid cells with lengths overlapping/below the METPO small-length definition. This provides a real-world, host-associated route to “small length” that may be taxon- and context-specific (UPEC in bladder epithelial cells). (pokhrel2024e.colidivision pages 1-5)

### Relevant statistics and quantitative data (recent)
1) **Polymyxin B in microfluidic single-cell traps (E. coli):** 
- Length decreased from **4.0 μm → 3.6 μm** comparing **0 vs 250 ng mL−1 polymyxin B**. (yokoyama2024capturingofextracellular pages 1-2)
- Reported as **4.0, 3.9, 3.6 μm** at **0, 50, 250 ng mL−1**, respectively. (yokoyama2024capturingofextracellular pages 6-7)
- On-chip doubling time was **25 min**; authors note higher on-chip susceptibility possibly due to **space limitation and shear forces**. (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 5-6)

2) **Intracellular vs extracellular UPEC length (host-cell environment):**
- Intracellular UPEC length: **1.3 ± 0.53 μm** vs extracellular: **2.59 ± 0.41 μm**. (pokhrel2024e.colidivision pages 1-5)
- Intracellular cocci: average length **~0.88 ± 0.13 μm** and near-unity aspect ratio. (pokhrel2024e.colidivision pages 1-5)
- Intracellular cocci division times: mean **~127 ± 75 min** with broad ranges reported. (pokhrel2024e.colidivision pages 1-5)

3) **Nutrient limitation / stationary entry (division-growth allocation model):**
- A division-growth allocation parameter λ shifts from **~20% toward growth** to **60–70% toward division** when entering stationary phase, consistent with decreasing biomass-per-cell (smaller size). (nieto2024bacterialcellsize pages 5-7)

### Candidate nodes grouped by type (ontology grounding suggestions)
**Trait**
- METPO:1000884: cell length small (given)

**Genes/proteins (label-only unless curated to species-specific IDs)**
- FtsZ (Z-ring tubulin homolog; divisome organizer; rate-limiting factor for division timing in *E. coli*). (mannik2024determiningtheratelimiting pages 1-2, cameron2024insightsintothe pages 1-3)
- FtsA, ZipA (membrane tethers for proto-ring in *E. coli*). (cameron2024insightsintothe pages 1-3)
- FtsN (late divisome; activation of septal synthesis in models and feedback loops). (gong2024thedivisomeis pages 1-3)
- FtsW/FtsI (septal PG synthesis enzymes; “FtsWI”). (cameron2024insightsintothe pages 1-3, gong2024thedivisomeis pages 1-3)
- Zap proteins (FtsZ-associated proteins promoting condensation/stability). (gong2024thedivisomeis pages 1-3)
- MinC/MinD/MinE (division-site placement system). (vashistha2023bacterialcellsizechanges pages 1-2, cameron2024insightsintothe pages 1-3)
- Nucleoid occlusion system (label-only; positions FtsZ, especially relevant in L-form context). (hayashi2024septalwallsynthesis pages 7-8)

**Processes / pathways**
- Adder control; sizer-like division control. (nieto2024bacterialcellsize pages 5-7, nieto2024mechanismsofcell pages 1-2)
- Septal peptidoglycan synthesis; Z ring condensation; divisome assembly checkpoints. (gong2024thedivisomeis pages 1-3, cameron2024insightsintothe pages 1-3)
- Division vs growth allocation (λ). (nieto2024bacterialcellsize pages 5-7)

**Environmental / experimental factors**
- Poor medium / slow growth. (nieto2024mechanismsofcell pages 1-2)
- Intracellular host environment / intracellular bacterial communities. (pokhrel2024e.colidivision pages 1-5)
- Microfluidic confinement and shear forces. (yokoyama2024capturingofextracellular pages 1-2)

**Chemicals / inhibitors**
- Polymyxin B (length decrease in trapped *E. coli*). (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 6-7)

**Assays**
- Mother machine single-cell imaging and segmentation pipelines. (thiermann2024toolsandmethods pages 10-11)

### Candidate causal edges (curation-ready)
The following artifact consolidates candidate nodes and evidence-backed edges with quotes, DOIs/URLs, and curation notes.

| Node/Edge ID | Subject | Predicate | Object | Node types (gene/protein, process, environment, chemical, assay) | Proposed ontology grounding (CURIEs where available) | Directionality/Effect (increase/decrease) | Evidence snippet (verbatim short quote with numbers if present) | Source (first author, year, venue) | DOI/URL | Citation ID |
|---|---|---|---|---|---|---|---|---|---|---|
| N1 | cell length small | is_a | cell-length phenotype with long axis ~1.3–2 µm | trait | METPO:1000884 | baseline class | "the longer cell dimension lies approximately between 1.3 and 2 micrometers" | User trait metadata | n/a | (pokhrel2024e.colidivision pages 1-5) |
| N2 | slow growth / poor medium | associated_with | smaller E. coli cells | environment, process | label only; ENVO candidate unclear | decrease length/size | "under poor media conditions, E. coli cells exhibit a different size regulation. They are smaller" | Nieto, 2024, NPJ Syst Biol Appl | https://doi.org/10.1038/s41540-024-00383-z | (nieto2024mechanismsofcell pages 1-2) |
| N3 | sizer-like division strategy | associated_with | small-cell state | process | GO candidate unclear | decrease added size for large-born cells / smaller steady size | "follow a sizer-like division strategy where the added size is inversely proportional to the size at birth" | Nieto, 2024, NPJ Syst Biol Appl | https://doi.org/10.1038/s41540-024-00383-z | (nieto2024mechanismsofcell pages 1-2) |
| N4 | FtsZ | rate_limiting_for | cell division timing / constriction onset | gene/protein, process | UniProt/NCBI Gene candidate; GO:0000921-like ring assembly candidate | increase FtsZ -> promotes division | "the FtsZ numbers in the cell are one of the rate-limiting factors for cell divisions" | Männik, 2024, Nat Commun | https://doi.org/10.1038/s41467-024-54242-w | (mannik2024determiningtheratelimiting pages 1-2) |
| N5 | Min system (MinC/MinD/MinE) | regulates | FtsZ ring positioning/initiation | gene/protein, process | UniProt candidates; GO candidate unclear | altered Min ratio delays ring formation, increases size | "FtsZ localization depends on membrane-associated Min proteins" | Vashistha, 2023, Nat Commun | https://doi.org/10.1038/s41467-023-41487-0 | (vashistha2023bacterialcellsizechanges pages 1-2) |
| N6 | polymyxin B | decreases | E. coli cell length in microfluidic traps | chemical, assay | CHEBI candidate unclear | decrease | "decrease from 4.0 μm to 3.6 μm for 0 and 250 ng mL−1 polymyxin B, respectively" | Yokoyama, 2024, Lab Chip | https://doi.org/10.1039/d3lc00707c | (yokoyama2024capturingofextracellular pages 1-2) |
| N7 | microfluidic trap confinement / shear forces | may_increase | apparent antibiotic susceptibility / affect growth and size | assay, environment | label only | uncertain decrease | "may be caused, among other reasons, by the space limitation in the cell trap and shear forces" | Yokoyama, 2024, Lab Chip | https://doi.org/10.1039/d3lc00707c | (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 5-6) |
| N8 | division frequency greater than growth rate | produces | smaller cocci cells | process | label only | decrease length | "the frequency of cell division outpaced the rate of cell growth, resulting in smaller cocci cells" | Pokhrel, 2024, bioRxiv | https://doi.org/10.1101/2024.04.08.588611 | (pokhrel2024e.colidivision pages 1-5) |
| N9 | intracellular host-cell environment / IBC | associated_with | short coccoid UPEC | environment, assay | ENVO candidate unclear | decrease length | "Intracellular UPEC are reported to be significantly shorter than extracellular bacteria (1.3 ± 0.53 µm vs 2.59 ± 0.41 µm)" | Pokhrel, 2024, bioRxiv | https://doi.org/10.1101/2024.04.08.588611 | (pokhrel2024e.colidivision pages 1-5) |
| N10 | mother machine imaging + segmentation pipeline | measures | cell length at birth/division and adder correlations | assay | label only | measurement node | "essentially identical correlations between cell length at birth (SB) ... and ... the length added between birth and division (Δ)" | Thiermann, 2024, eLife | https://doi.org/10.7554/elife.88463 | (thiermann2024toolsandmethods pages 10-11) |
| N11 | segmentation threshold / channel opening errors | biases | extracted cell-length values | assay | label only | uncertain measurement bias | "most segmentation errors … arose from misclassification of cells near the channel opening" | Thiermann, 2024, eLife | https://doi.org/10.7554/elife.88463 | (thiermann2024toolsandmethods pages 10-11) |
| N12 | FtsN | activates | FtsWI septal PG synthase complex | gene/protein, process | UniProt candidates; GO candidate unclear | increase septal synthesis | "Activation of the sPG synthase (FtsWI within the FtsQLBWI complex) depends on FtsN" | Gong, 2024, Nat Commun | https://doi.org/10.1038/s41467-024-52217-5 | (gong2024thedivisomeis pages 1-3) |
| N13 | septal peptidoglycan synthesis (sPG) | feeds_back_to_promote | Z-ring condensation/stability | process | GO candidate unclear | increase division robustness | "septal cell wall synthesis feeds back to promote Z ring condensation and stability" | Gong, 2024, Nat Commun | https://doi.org/10.1038/s41467-024-52217-5 | (gong2024thedivisomeis pages 1-3) |
| N14 | Min system + nucleoid occlusion + FtsZ-dependent division | required_for | uniform cell size in L-forms | gene/protein, process | Min system label; nucleoid occlusion label; FtsZ candidate | increase uniformity / constrain size | "requires at least either the Min or nucleoid occlusion systems for positioning FtsZ at mid cell division sites" | Hayashi, 2024, Commun Biol | https://doi.org/10.1038/s42003-024-07279-y | (hayashi2024septalwallsynthesis pages 7-8) |
| N15 | division-growth allocation parameter λ | shifts_toward | division during nutrient limitation/stationary entry | process | label only | increase division allocation, decrease biomass per cell | "λ shifts from ≈20% toward growth to 60–70% toward division when entering stationary phase" | Nieto, 2024, bioRxiv | https://doi.org/10.1101/2024.09.24.614723 | (nieto2024bacterialcellsize pages 5-7) |
| E1 | slow growth / poor medium | causes | smaller E. coli cells with sizer-like control | environment -> process/phenotype | label only -> METPO:1000884 candidate mapping | decrease | "under poor media conditions... They are smaller and follow a sizer-like division strategy" | Nieto, 2024, NPJ Syst Biol Appl | https://doi.org/10.1038/s41540-024-00383-z | (nieto2024mechanismsofcell pages 1-2) |
| E2 | sizer-like division strategy | contributes_to | small-cell phenotype | process -> trait | label only -> METPO:1000884 candidate mapping | decrease | "cells dividing once they reach, on average, a specified size" | Nieto, 2024, NPJ Syst Biol Appl | https://doi.org/10.1038/s41540-024-00383-z | (nieto2024mechanismsofcell pages 1-2) |
| E3 | increasing MinE/MinD ratio | delays | FtsZ ring formation | gene/protein -> process | MinE/MinD/FtsZ labels | increase delay; indirect increase cell length | "increasing MinE/MinD delays FtsZ ring formation" | Vashistha, 2023, Nat Commun | https://doi.org/10.1038/s41467-023-41487-0 | (vashistha2023bacterialcellsizechanges pages 1-2) |
| E4 | delayed FtsZ ring formation | increases | cell size / cell length | process -> trait | FtsZ process label -> METPO:1000884 opposite direction | increase | "delay cell division until the cell reaches a larger size" | Vashistha, 2023, Nat Commun | https://doi.org/10.1038/s41467-023-41487-0 | (vashistha2023bacterialcellsizechanges pages 1-2) |
| E5 | FtsZ abundance | rate_limiting_for | division timing | gene/protein -> process | FtsZ label | increase FtsZ promotes earlier division | "FtsZ numbers are identified as one of the rate-limiting factors" | Männik, 2024, Nat Commun | https://doi.org/10.1038/s41467-024-54242-w | (mannik2024determiningtheratelimiting pages 1-2) |
| E6 | higher effective division relative to growth | causes | smaller cocci cells | process -> phenotype | label only | decrease length | "the frequency of cell division outpaced the rate of cell growth, resulting in smaller cocci cells" | Pokhrel, 2024, bioRxiv | https://doi.org/10.1101/2024.04.08.588611 | (pokhrel2024e.colidivision pages 1-5) |
| E7 | intracellular host environment | associated_with | UPEC length 1.3 ± 0.53 µm vs extracellular 2.59 ± 0.41 µm | environment -> phenotype | ENVO candidate unclear | decrease | "1.3 ± 0.53 µm vs 2.59 ± 0.41 µm" | Pokhrel, 2024, bioRxiv | https://doi.org/10.1101/2024.04.08.588611 | (pokhrel2024e.colidivision pages 1-5) |
| E8 | intracellular divisome-driven coccoid transition | produces | average cocci length ~0.88 ± 0.13 µm | process -> phenotype | FtsZ/divisome labels | decrease below trait boundary | "average lengths around 0.88 ± 0.13 µm" | Pokhrel, 2024, bioRxiv | https://doi.org/10.1101/2024.04.08.588611 | (pokhrel2024e.colidivision pages 1-5) |
| E9 | polymyxin B treatment | decreases | trapped-cell length from 4.0 to 3.6 µm | chemical -> phenotype | CHEBI candidate unclear | decrease | "4.0, 3.9, and 3.6 μm at 0, 50, and 250 ng mL−1, respectively" | Yokoyama, 2024, Lab Chip | https://doi.org/10.1039/d3lc00707c | (yokoyama2024capturingofextracellular pages 6-7) |
| E10 | trap confinement / shear forces | confounds | on-chip length/susceptibility interpretation | assay/environment -> assay outcome | label only | uncertain | "space limitation in the cell trap and shear forces" | Yokoyama, 2024, Lab Chip | https://doi.org/10.1039/d3lc00707c | (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 5-6) |
| E11 | FtsN | activates | FtsWI complex | gene/protein -> process | FtsN/FtsW/FtsI labels | increase septal PG synthesis | "depends on FtsN, which allosterically activates FtsWI" | Gong, 2024, Nat Commun | https://doi.org/10.1038/s41467-024-52217-5 | (gong2024thedivisomeis pages 1-3) |
| E12 | septal PG synthesis | positively_feedback_on | Z-ring condensation/stability | process -> process | sPG/Z-ring labels | increase | "feedback to promote Z ring condensation and stability" | Gong, 2024, Nat Commun | https://doi.org/10.1038/s41467-024-52217-5 | (gong2024thedivisomeis pages 1-3) |
| E13 | Min system and nucleoid occlusion | position | FtsZ at midcell | process/gene -> process | Min label; FtsZ label | increase proper size uniformity | "for positioning FtsZ at mid cell division sites" | Hayashi, 2024, Commun Biol | https://doi.org/10.1038/s42003-024-07279-y | (hayashi2024septalwallsynthesis pages 7-8) |
| E14 | FtsZ-dependent division with Min/NO support | required_for | uniform cell size in wall-less E. coli | process -> phenotype | FtsZ label | increase uniformity; constrain size | "requires at least either the Min or nucleoid occlusion systems" | Hayashi, 2024, Commun Biol | https://doi.org/10.1038/s42003-024-07279-y | (hayashi2024septalwallsynthesis pages 7-8) |
| E15 | λ shift toward division under nutrient depletion | decreases | biomass per cell / cell volume | process -> phenotype | label only | decrease size | "OD levels off while CFU continues to rise—indicates decreased biomass per cell" | Nieto, 2024, bioRxiv | https://doi.org/10.1101/2024.09.24.614723 | (nieto2024bacterialcellsize pages 5-7) |
| E16 | mother machine 1D segmentation under tight confinement | adequately_measures | cell length | assay -> assay outcome | label only | measurement support | "perform adequately when cells are tightly confined in the growth channels" | Thiermann, 2024, eLife | https://doi.org/10.7554/elife.88463 | (thiermann2024toolsandmethods pages 10-11) |
| E17 | segmentation model/training mismatch | biases | cell-length extraction | assay -> assay outcome | label only | uncertain | "the pre-trained mother machine model provided with DeLTA did not generalize well" | Thiermann, 2024, eLife | https://doi.org/10.7554/elife.88463 | (thiermann2024toolsandmethods pages 10-11) |
| E18 | FtsZ proto-ring with FtsA/ZipA | organizes | divisome assembly and septal synthesis | gene/protein -> process | FtsZ/FtsA/ZipA labels | increase division | "FtsZ ... required for localization of all other divisome proteins" | Cameron & Margolin, 2024, Nat Rev Microbiol | https://doi.org/10.1038/s41579-023-00942-x | (cameron2024insightsintothe pages 1-3) |
| E19 | Min system | negatively_regulates | FtsZ polymerization at incorrect sites | process -> process | Min label; FtsZ label | decrease ectopic division, improve placement | "acting as localized negative regulators of FtsZ polymerization" | Cameron & Margolin, 2024, Nat Rev Microbiol | https://doi.org/10.1038/s41579-023-00942-x | (cameron2024insightsintothe pages 1-3) |


*Table: This table compiles curation-oriented candidate entities and causal edges for the microbial trait “cell length small,” using only the cited context sources. It is designed to help TraitMech curation by linking mechanistic claims, measurements, and assay caveats to proposed grounded nodes and edge directions.*

### Warnings / claims to treat as uncertain before curating into TraitMech
1) **Assay-confounded antibiotic effects:** Yokoyama et al. explicitly caution that on-chip susceptibility (and potentially size effects) may be influenced by **space limitation and shear forces**, so edges attributing length decreases solely to polymyxin B should be curated with an **assay context qualifier** (microfluidic trap, flow) rather than generalized. (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 5-6)

2) **Coccoid intracellular states may fall outside METPO range:** Intracellular cocci lengths (~0.88 μm) are **below** the 1.3–2.0 μm “small length” definition; curating these as direct evidence for METPO:1000884 may require either (i) treating them as boundary-case evidence for “small or very small” length, or (ii) mapping them to a different morphology trait (coccoid/spherical) while retaining length as a measured attribute. (pokhrel2024e.colidivision pages 1-5)

3) **Mechanistic hypotheses vs direct causal proof:** The Nieto et al. (2024) slow-growth work includes model discrimination and proposed mechanisms (e.g., FtsZ degradation/commitment size). These are plausible mechanistic entities but should be flagged as **model-supported** unless independently validated by direct perturbation evidence in the same system/condition. (nieto2024mechanismsofcell pages 1-2, nieto2024mechanismsofcell pages 6-7)

---

## DOI-first bibliography (with dates and URLs)
- Nieto C, Vargas-García CA, Pedraza JM, Singh A. **Mechanisms of cell size regulation in slow-growing Escherichia coli cells: discriminating models beyond the adder.** *NPJ Systems Biology and Applications* (May 2024). DOI: 10.1038/s41540-024-00383-z. https://doi.org/10.1038/s41540-024-00383-z (nieto2024mechanismsofcell pages 1-2, nieto2024mechanismsofcell pages 6-7, nieto2024mechanismsofcell pages 4-6)
- Vashistha H, Jammal-Touma J, Singh K, Rabin Y, Salman H. **Bacterial cell-size changes resulting from altering the relative expression of Min proteins.** *Nature Communications* (Sep 2023). DOI: 10.1038/s41467-023-41487-0. https://doi.org/10.1038/s41467-023-41487-0 (vashistha2023bacterialcellsizechanges pages 1-2, vashistha2023bacterialcellsizechanges pages 2-3)
- Yokoyama F, Kling A, Dittrich PS. **Capturing of extracellular vesicles derived from single cells of Escherichia coli.** *Lab on a Chip* (Feb 2024). DOI: 10.1039/d3lc00707c. https://doi.org/10.1039/d3lc00707c (yokoyama2024capturingofextracellular pages 1-2, yokoyama2024capturingofextracellular pages 6-7, yokoyama2024capturingofextracellular pages 5-6, yokoyama2024capturingofextracellular media 0a26e6cd, yokoyama2024capturingofextracellular media 661119d7)
- Pokhrel A, Costas A, Pittorino MJ, Duggin I, Söderström B. **E. coli division machinery drives cocci development inside host cells.** *bioRxiv* (posted Jul 2024). DOI: 10.1101/2024.04.08.588611. https://doi.org/10.1101/2024.04.08.588611 (pokhrel2024e.colidivision pages 1-5)
- Männik J, Kar P, Amarasinghe CI, Amir A. **Determining the rate-limiting processes for cell division in Escherichia coli.** *Nature Communications* (Nov 2024). DOI: 10.1038/s41467-024-54242-w. https://doi.org/10.1038/s41467-024-54242-w (mannik2024determiningtheratelimiting pages 1-2)
- Cameron TA, Margolin W. **Insights into the assembly and regulation of the bacterial divisome.** *Nature Reviews Microbiology* (Jul 2024). DOI: 10.1038/s41579-023-00942-x. https://doi.org/10.1038/s41579-023-00942-x (cameron2024insightsintothe pages 1-3, cameron2024insightsintothe pages 10-12, cameron2024insightsintothe pages 20-22)
- Gong H, Yan D, Cui Y, et al. **The divisome is a self-enhancing machine in Escherichia coli and Caulobacter crescentus.** *Nature Communications* (Sep 2024). DOI: 10.1038/s41467-024-52217-5. https://doi.org/10.1038/s41467-024-52217-5 (gong2024thedivisomeis pages 1-3)
- Thiermann R, Sandler M, Ahir G, et al. **Tools and methods for high-throughput single-cell imaging with the mother machine.** *eLife* (Apr 2024). DOI: 10.7554/eLife.88463. https://doi.org/10.7554/elife.88463 (thiermann2024toolsandmethods pages 10-11)
- Hayashi M, Takaoka C, Higashi K, et al. **Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in Escherichia coli L-forms.** *Communications Biology* (Nov 2024). DOI: 10.1038/s42003-024-07279-y. https://doi.org/10.1038/s42003-024-07279-y (hayashi2024septalwallsynthesis pages 7-8)
- Nieto C, Igler C, Singh A. **Bacterial cell size modulation along the growth curve across nutrient conditions.** *bioRxiv* (Sep 2024). DOI: 10.1101/2024.09.24.614723. https://doi.org/10.1101/2024.09.24.614723 (nieto2024bacterialcellsize pages 5-7, nieto2024bacterialcellsize pages 7-9)


References

1. (pokhrel2024e.colidivision pages 1-5): Alaska Pokhrel, Ariana Costas, Matthew J. Pittorino, I. Duggin, and Bill Söderström. E. coli division machinery drives cocci development inside host cells. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.04.08.588611, doi:10.1101/2024.04.08.588611. This article has 4 citations.

2. (vashistha2023bacterialcellsizechanges pages 2-3): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

3. (thiermann2024toolsandmethods pages 10-11): Ryan Thiermann, Michael Sandler, Gursharan Ahir, John T. Sauls, Jeremy W. Schroeder, Steven D. Brown, Guillaume Le Treut, Fangwei Si, Dongyang Li, Jue D. Wang, and Suckjoon Jun. Tools and methods for high-throughput single-cell imaging with the mother machine. eLife, Apr 2024. URL: https://doi.org/10.7554/elife.88463, doi:10.7554/elife.88463. This article has 32 citations and is from a domain leading peer-reviewed journal.

4. (yokoyama2024capturingofextracellular pages 1-2): Fumiaki Yokoyama, André Kling, and Petra S. Dittrich. Capturing of extracellular vesicles derived from single cells of escherichia coli. Lab on a Chip, 24:2049-2057, Feb 2024. URL: https://doi.org/10.1039/d3lc00707c, doi:10.1039/d3lc00707c. This article has 7 citations and is from a domain leading peer-reviewed journal.

5. (nieto2024bacterialcellsize pages 5-7): César Nieto, Claudia Igler, and Abhyudai Singh. Bacterial cell size modulation along the growth curve across nutrient conditions. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.24.614723, doi:10.1101/2024.09.24.614723. This article has 2 citations.

6. (nieto2024ageneralizedadder pages 1-2): César Nieto, César Augusto Vargas-García, and Abhyudai Singh. A generalized adder mechanism for cell size homeostasis: implications for stochastic dynamics of clonal proliferation. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.13.612972, doi:10.1101/2024.09.13.612972. This article has 4 citations.

7. (nieto2024mechanismsofcell pages 1-2): César Nieto, César Augusto Vargas-García, Juan Manuel Pedraza, and Abhyudai Singh. Mechanisms of cell size regulation in slow-growing escherichia coli cells: discriminating models beyond the adder. NPJ Systems Biology and Applications, May 2024. URL: https://doi.org/10.1038/s41540-024-00383-z, doi:10.1038/s41540-024-00383-z. This article has 12 citations.

8. (nieto2024mechanismsofcell pages 6-7): César Nieto, César Augusto Vargas-García, Juan Manuel Pedraza, and Abhyudai Singh. Mechanisms of cell size regulation in slow-growing escherichia coli cells: discriminating models beyond the adder. NPJ Systems Biology and Applications, May 2024. URL: https://doi.org/10.1038/s41540-024-00383-z, doi:10.1038/s41540-024-00383-z. This article has 12 citations.

9. (nieto2024mechanismsofcell pages 4-6): César Nieto, César Augusto Vargas-García, Juan Manuel Pedraza, and Abhyudai Singh. Mechanisms of cell size regulation in slow-growing escherichia coli cells: discriminating models beyond the adder. NPJ Systems Biology and Applications, May 2024. URL: https://doi.org/10.1038/s41540-024-00383-z, doi:10.1038/s41540-024-00383-z. This article has 12 citations.

10. (cameron2024insightsintothe pages 1-3): Todd A. Cameron and William Margolin. Insights into the assembly and regulation of the bacterial divisome. Nature Reviews Microbiology, 22:33-45, Jul 2024. URL: https://doi.org/10.1038/s41579-023-00942-x, doi:10.1038/s41579-023-00942-x. This article has 134 citations and is from a highest quality peer-reviewed journal.

11. (mannik2024determiningtheratelimiting pages 1-2): Jaan Männik, Prathitha Kar, Chathuddasie I. Amarasinghe, Ariel Amir, and Jaan Männik. Determining the rate-limiting processes for cell division in escherichia coli. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-54242-w, doi:10.1038/s41467-024-54242-w. This article has 10 citations and is from a highest quality peer-reviewed journal.

12. (gong2024thedivisomeis pages 1-3): Han Gong, Di Yan, Yuanyuan Cui, Ying Li, Jize Yang, Wenjie Yang, Rui Zhan, Qianqian Wan, Xinci Wang, Haofeng He, Xiangdong Chen, Joe Lutkenhaus, Xinxing Yang, and Shishen Du. The divisome is a self-enhancing machine in escherichia coli and caulobacter crescentus. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52217-5, doi:10.1038/s41467-024-52217-5. This article has 15 citations and is from a highest quality peer-reviewed journal.

13. (vashistha2023bacterialcellsizechanges pages 1-2): Harsh Vashistha, Joanna Jammal-Touma, Kulveer Singh, Yitzhak Rabin, and Hanna Salman. Bacterial cell-size changes resulting from altering the relative expression of min proteins. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41487-0, doi:10.1038/s41467-023-41487-0. This article has 16 citations and is from a highest quality peer-reviewed journal.

14. (hayashi2024septalwallsynthesis pages 7-8): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

15. (yokoyama2024capturingofextracellular pages 6-7): Fumiaki Yokoyama, André Kling, and Petra S. Dittrich. Capturing of extracellular vesicles derived from single cells of escherichia coli. Lab on a Chip, 24:2049-2057, Feb 2024. URL: https://doi.org/10.1039/d3lc00707c, doi:10.1039/d3lc00707c. This article has 7 citations and is from a domain leading peer-reviewed journal.

16. (yokoyama2024capturingofextracellular media 0a26e6cd): Fumiaki Yokoyama, André Kling, and Petra S. Dittrich. Capturing of extracellular vesicles derived from single cells of escherichia coli. Lab on a Chip, 24:2049-2057, Feb 2024. URL: https://doi.org/10.1039/d3lc00707c, doi:10.1039/d3lc00707c. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (yokoyama2024capturingofextracellular media 661119d7): Fumiaki Yokoyama, André Kling, and Petra S. Dittrich. Capturing of extracellular vesicles derived from single cells of escherichia coli. Lab on a Chip, 24:2049-2057, Feb 2024. URL: https://doi.org/10.1039/d3lc00707c, doi:10.1039/d3lc00707c. This article has 7 citations and is from a domain leading peer-reviewed journal.

18. (yokoyama2024capturingofextracellular pages 5-6): Fumiaki Yokoyama, André Kling, and Petra S. Dittrich. Capturing of extracellular vesicles derived from single cells of escherichia coli. Lab on a Chip, 24:2049-2057, Feb 2024. URL: https://doi.org/10.1039/d3lc00707c, doi:10.1039/d3lc00707c. This article has 7 citations and is from a domain leading peer-reviewed journal.

19. (cameron2024insightsintothe pages 10-12): Todd A. Cameron and William Margolin. Insights into the assembly and regulation of the bacterial divisome. Nature Reviews Microbiology, 22:33-45, Jul 2024. URL: https://doi.org/10.1038/s41579-023-00942-x, doi:10.1038/s41579-023-00942-x. This article has 134 citations and is from a highest quality peer-reviewed journal.

20. (cameron2024insightsintothe pages 20-22): Todd A. Cameron and William Margolin. Insights into the assembly and regulation of the bacterial divisome. Nature Reviews Microbiology, 22:33-45, Jul 2024. URL: https://doi.org/10.1038/s41579-023-00942-x, doi:10.1038/s41579-023-00942-x. This article has 134 citations and is from a highest quality peer-reviewed journal.

21. (nieto2024bacterialcellsize pages 7-9): César Nieto, Claudia Igler, and Abhyudai Singh. Bacterial cell size modulation along the growth curve across nutrient conditions. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.24.614723, doi:10.1101/2024.09.24.614723. This article has 2 citations.