---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-04T07:45:45.335281'
end_time: '2026-08-04T07:53:37.932493'
duration_seconds: 472.6
template_file: templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width large
  trait_identifier: METPO:1000890
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_large
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension exceeds approximately
    0.9 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_>0.9
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan
    synthesis (Supports MreB/Rod-complex activity as the control point governing wide
    rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent
    size law supports widening of cells at fast growth rates or under nutrient-rich
    conditions.)'
  causal_graph_summary: 'cell_width_large_setpoint_increase: 15 nodes, 10 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width large
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000890
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension exceeds approximately 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_>0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports MreB/Rod-complex activity as the control point governing wide rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports widening of cells at fast growth rates or under nutrient-rich conditions.)
- **Existing causal graph summary:** cell_width_large_setpoint_increase: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **cell width large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_large.yaml`.

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
- **Trait label:** cell width large
- **Trait identifier (already a CURIE — quote it verbatim, do not prefix it):** METPO:1000890
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension exceeds approximately 0.9 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_>0.9
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: MreB-directed peptidoglycan synthesis (Supports MreB/Rod-complex activity as the control point governing wide rod radii.) | DOI:10.1126/science.aaa1313: cell size scales with growth rate (Growth-rate-dependent size law supports widening of cells at fast growth rates or under nutrient-rich conditions.)
- **Existing causal graph summary:** cell_width_large_setpoint_increase: 15 nodes, 10 edges

## Research Objective

Research the microbial trait **cell width large** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_large.yaml`.

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


# Curation-focused research report: **cell width large**

## 1. Trait scope

**Trait:** “cell width large”  
**Identifier:** `METPO:1000890`  
**Category:** morphology; **term kind:** class; **mapping:** reviewed  
**Operational definition:** the shorter dimension of a microbial cell exceeds approximately **0.9 μm**.

This is best treated as an **assay-observed morphological state**, not as a pathway or intrinsic taxonomic property. For rods, width should be measured perpendicular to the longitudinal axis, preferably from segmented, exponentially growing single cells under specified medium, temperature, osmolarity, and imaging conditions. A population should instantiate the class only when its representative statistic—ideally median or mean single-cell width—crosses the threshold, rather than merely containing occasional cells wider than 0.9 μm.

### Boundary cases

* **Increased length or volume without increased short-axis dimension** is not `METPO:1000890`.
* **Filamentation** caused by division inhibition is primarily a length phenotype unless width also exceeds 0.9 μm.
* **Local bulges, branches, or septal swelling** are evidence of width dysregulation but do not establish a whole-cell large-width phenotype without a defined measurement rule.
* **Rod-to-sphere conversion** often entails widening, but “spherical,” “rounded,” or “increased volume” should not automatically be mapped to `METPO:1000890`; an actual short-axis measurement is required.
* **Transient osmotic swelling, L-forms, protoplasts, and wall-less cells** should be modeled separately unless the intended graph explicitly covers these assay states.
* The 0.9-μm boundary is not universal biological evidence of abnormality: naturally broad or giant taxa may exceed it as their normal morphology.

The strongest current model is that width emerges from the **relative activities and spatial organization of peptidoglycan synthesis/remodeling systems**, rather than from MreB abundance or growth rate alone. In *Bacillus subtilis*, circumferential Rod-system synthesis narrows cells, whereas class-A penicillin-binding proteins tend to widen them; directional MreB/Rod-complex density, not a unique MreB filament geometry, predicts diameter across perturbations (dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 1-3).

## 2. Candidate graph nodes

### Phenotypes and processes

* **cell width large** — `METPO:1000890`
* regulation of cell shape — candidate `GO:0008360`
* peptidoglycan-based cell wall — candidate `GO:0009274`
* cell-wall/peptidoglycan biosynthesis
* circumferential peptidoglycan insertion
* directional Rod-complex motion
* peptidoglycan mechanical anisotropy
* isotropic peptidoglycan insertion
* peptidoglycan hydrolysis/endopeptidase activity
* local cell widening and bulging
* spherical-cell or rounding phenotype — retain as a separate phenotype node unless width is measured
* outer-membrane load-bearing capacity

### Proteins and complexes

* **Rod complex/elongasome** — complex node containing taxon-dependent components
* **MreB**, plus *B. subtilis* homologues Mbl and MreBH
* **RodA** — SEDS-family peptidoglycan glycosyltransferase
* **PBP2/MrdA** in *E. coli*; **PBP2A/PbpH** in *B. subtilis* — class-B transpeptidases
* **MreC**, **MreD**, **RodZ** — accessory/activation and coupling components
* **class-A PBPs**, especially PBP1/PonA in *B. subtilis*
* peptidoglycan DL- and DD-endopeptidases
* **PBP5/DacA**, CwlO, FtsE, FtsX — width-related candidates from the *B. subtilis* screen
* metabolic candidates: Rpe, Pyk, PtsH, GuaA, PanD
* MinJ, YaaA, YbzH — secondary candidates requiring gene-specific mechanistic follow-up

Protein nodes should be assigned **taxon-specific UniProt accessions during implementation**. A generic “MreB” node is useful for a high-level graph, but it should not be given a single species-specific accession across *E. coli*, *B. subtilis*, and other taxa.

### Chemicals and environmental/experimental factors

* **magnesium(2+)** — candidate `CHEBI:18420`
* **A22** — MreB-polymerization antagonist; retain label-only until its exact ChEBI record is verified
* **mecillinam/amdinocillin** — PBP2-directed β-lactam; verify the chemical CURIE before curation
* nutrient-rich versus minimal medium
* growth rate
* osmotic support with sucrose
* cell-wall stress and turgor pressure
* lipopolysaccharide synthesis/modification and outer-membrane fortification

### Cellular locations

* cytoplasmic membrane
* periplasm/periplasmic space in diderm bacteria — candidate `GO:0030288`
* peptidoglycan sacculus/cell wall
* Gram-negative outer membrane
* cell sidewall

## 3. Candidate causal edges

The compact graph-ready summary is provided below; “indirect” means that the paper establishes rounding, shape failure, or an upstream mechanism but does not demonstrate that the population crosses 0.9 μm.

| subject | predicate | object | taxon/context | confidence | key quantitative evidence | DOI |
|---|---|---|---|---|---|---|
| Rod complex activity | decreases | cell width large (METPO:1000890) | *Bacillus subtilis* elongation; balance of Rod system vs aPBPs | High for width control; indirect for >0.9 µm threshold | Rod system “reduces diameter,” while aPBPs increase it; wild-type diameter maintained only within a PBP1/MreB ratio window of ~0.8–1.5; increased directional MreB/PBP2A activity correlates with thinner cells (dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 1-3) | 10.1101/392837 |
| class A PBP activity | increases | cell width large (METPO:1000890) | *B. subtilis* sidewall synthesis opposing Rod system | High for width control; indirect for >0.9 µm threshold | aPBPs “increase diameter”; aPBP-deficient cells are thinner, supporting causal widening by aPBP activity (dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 10-12) | 10.1101/392837 |
| reduced MreB function | increases | cell width / rounding | *Escherichia coli*; A22 treatment or point mutants | High for shape/width; indirect for trait threshold | Cell diameter varied from **790 ± 30 nm to 1700 ± 20 nm** across A22 and mreB perturbations; A22 causes “cell rounding and eventual lysis” (ouzounov2016mreborientationcorrelates pages 1-2, shi2017deepphenotypicmapping pages 1-3) | 10.1016/j.bpj.2016.07.017; 10.1016/j.cub.2017.09.065 |
| reduced PBP2 function | increases | cell width / rounding | *E. coli*; mecillinam inhibition of PBP2 | High for shape; indirect for width threshold | Mecillinam “causes cell rounding and death”; pathway-directed screening exploits toxic Rod-system malfunction caused by mecillinam (buss2019pathwaydirectedscreenfor pages 1-2, shi2017deepphenotypicmapping pages 1-3) | 10.1128/AAC.01530-18; 10.1016/j.cub.2017.09.065 |
| reduced RodZ function | increases | cell width / spherical morphology | *E. coli* ΔrodZ | Moderate; mostly indirect because shape/volume emphasized | ΔrodZ cells are “spherical”; PG holes and increased cell volume observed; >50-fold higher vesicle production than WT indicates severe envelope/shape defect (ojima2024buddingandexplosive pages 1-2) | 10.3389/fmicb.2024.1400434 |
| directional MreB filament density/orientation | decreases | cell width large (METPO:1000890) | *B. subtilis* and *E. coli* Rod mutants | High for width control; indirect for >0.9 µm threshold | In *B. subtilis*, increased mreBCD induction inversely correlates with rod width; in *E. coli*, directional MreB filament density vs width shows **R² = 0.84–0.99** across datasets (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 1-3) | 10.1101/392837 |
| MreB helical pitch angle | inversely correlates with | cell diameter | *E. coli* A22-treated and mreB mutant cells | Moderate; correlation, not direct intervention edge | Diameter shifted over **790 ± 30 nm to 1700 ± 20 nm**; among measured MreB properties, helical pitch angle significantly inversely correlated with diameter (ouzounov2016mreborientationcorrelates pages 1-2) | 10.1016/j.bpj.2016.07.017 |
| peptidoglycan hydrolase activity | causes local increase in | cell width / bulging | *B. subtilis* ΔmreB | High for local widening; indirect for steady-state trait | Pulse-chase imaging showed anisotropic PG hydrolase activity “at the sites of increased cell width and bulging,” while PG synthesis remained isotropic (tesson2022magnesiumrescuesthe pages 1-2) | 10.1038/s41598-021-04294-5 |
| Mg2+ excess | inhibits | peptidoglycan hydrolase-driven widening | *B. subtilis* ΔmreB rescue medium | High for suppression mechanism; indirect for trait threshold | “Millimolar concentrations of magnesium” rescue viability/morphology; increased DL-endopeptidase activity is mitigated by excess Mg2+ (tesson2022magnesiumrescuesthe pages 1-2) | 10.1038/s41598-021-04294-5 |
| fortified Gram-negative outer membrane | rescues | Rod-complex shape defects | *E. coli* mreC/Rod-complex-defective backgrounds | Moderate; indirect because width not directly quantified | OM-strengthening LPS changes “suppress the growth and shape defects” of Rod-complex mutants and restore proper MreB orientation (fivenson2023arolefor pages 1-2) | 10.1073/pnas.2301987120 |
| MreD–MreC interaction integrity | activates / is required for | Rod complex activity | *Thermus thermophilus* structure with *E. coli* in vivo validation | Moderate for upstream mechanism; indirect to width | Disrupting MreD–MreC contacts “abolishes Rod complex activity in vivo”; supports an upstream activation edge relevant to width control (gilman2024mrecmredstructurereveals pages 1-2) | 10.1101/2024.10.08.617240 |
| RodA cellular level | modulates | elongasome processivity and likely cell shape | *B. subtilis* single-molecule tracking | Moderate; indirect because width not directly measured | RodA levels regulate elongasome processivity, reversal, and pausing; authors state this “likely also regulates the cell shape” (middlemiss2024molecularmotortugofwar pages 1-2) | 10.1038/s41467-024-49785-x |


*Table: This table summarizes the strongest graph-ready causal edges for the large-cell-width trait, emphasizing direct width-control mechanisms and clearly marking evidence that only supports broader rounding or shape defects. It is useful for prioritizing which entities and relations are strong enough for TraitMech curation versus those that should remain indirect or provisional.*

### Additional graph-detail edges

| Subject | Predicate | Object | Evidence snippet and interpretation | Curation status |
|---|---|---|---|---|
| MreB filaments | organizes/orients | Rod-complex peptidoglycan synthesis | The Rod complex contains synthases organized by actin-like MreB; circumferential motion deposits sidewall PG. This supports a mechanistic organization edge, not direct enzymatic catalysis by MreB (buss2019pathwaydirectedscreenfor pages 1-2, middlemiss2024molecularmotortugofwar pages 1-2). | **Curate**, with taxon context. |
| RodA | polymerizes | peptidoglycan glycan strands | Buss et al.: “RodA is a PG polymerase that synthesizes the glycan strands.” (buss2019pathwaydirectedscreenfor pages 1-2) | **Curate**. |
| PBP2 | cross-links | RodA-produced glycan strands into PG matrix | Buss et al.: “PBP2 is a transpeptidase that cross-links the RodA products into the existing matrix.” (buss2019pathwaydirectedscreenfor pages 1-2) | **Curate**. |
| MreD–MreC interaction | promotes | MreC conformation primed for Rod-complex activation | 2024 structural work reports that MreD controls MreC conformation and that disrupting contacts abolishes Rod-complex activity in vivo (gilman2024mrecmredstructurereveals pages 1-2). | **Provisional**: 2024 source is a preprint in the retrieved record. |
| MreC activation state | promotes | PBP2 opening/activation | The 2023 PNAS study summarizes genetic, structural, and cytological evidence that MreC induces a PBP2 conformational change, which activates RodA (fivenson2023arolefor pages 1-2). | **Curate as supported model**, not universal fact. |
| RodZ | couples/interacts with | MreB and PG-synthesis machinery | RodZ is part of the Rod complex; ΔrodZ causes spherical cells, PG holes, and increased volume (ojima2024buddingandexplosive pages 1-2). | **Curate interaction/upstream shape edge**; large-width endpoint remains indirect. |
| increased directional Rod-system synthesis | increases | oriented PG and wall anisotropy | Increased MreBCD activity and directionally moving PBP2A produce more circumferentially oriented material and mechanically anisotropic sacculi (dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 1-3). | **Curate**. |
| oriented PG/mechanical anisotropy | suppresses | large cell width | The supported model is that hoop-like reinforcement limits radial expansion; direct width correlations are strong, but this intermediate-to-trait edge remains partly mechanistic inference (dion2018celldiameterin pages 18-19, dion2018celldiameterin pages 8-10). | **Curate with “model-supported” qualifier**. |
| class-A PBP synthesis relative to Rod synthesis | promotes | increased width | aPBPs widen cells, whereas the Rod system narrows them; diameter is set by their balance (dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 8-10, dion2018celldiameterin pages 10-12). | **Curate**, especially for *B. subtilis*. |
| MreB loss/depletion | increases | PG hydrolase activity and local widening | In ΔmreB *B. subtilis*, PG degradation was enriched at sites of increased width and bulging while synthesis remained isotropic (tesson2022magnesiumrescuesthe pages 1-2). | **Curate taxon-specific chain**. |
| Mg²⁺ excess | inhibits | DL-endopeptidase activity | Excess magnesium mitigated the elevated DL-endopeptidase activity and rescued morphology in ΔmreB cells (tesson2022magnesiumrescuesthe pages 1-2). | **Curate as suppressor**, not a primary cause of large width. |
| strengthened outer membrane | restores | MreB orientation/Rod-mutant shape | LPS changes predicted to fortify the outer membrane suppressed Rod-complex mutant growth and shape defects and restored MreB orientation (fivenson2023arolefor pages 1-2). | **Provisional indirect modifier**, Gram-negative only. |
| A22 | inhibits | MreB-dependent width control | A22 depolymerizes/inhibits MreB, causing rounding and eventual lysis; A22/mreB perturbations covered diameters from 790 ± 30 to 1,700 ± 20 nm (shi2017deepphenotypicmapping pages 1-3, ouzounov2016mreborientationcorrelates pages 1-2). | **Curate experimental perturbation edge**. |
| mecillinam | inhibits | PBP2/Rod-system function | Mecillinam inhibition of PBP2 causes rounding and death; the compound is used as a Rod-pathway probe (buss2019pathwaydirectedscreenfor pages 1-2, shi2017deepphenotypicmapping pages 1-3). | **Curate experimental perturbation edge**; threshold crossing must be dataset-specific. |
| ΔdacA, ΔcwlO, ΔftsE, ΔftsX, or ΔrodZ | increases | *B. subtilis* cell width | A genome-scale microscopy screen found that these cell-wall-homeostasis mutants increased width (juillot2021ahighcontentmicroscopy pages 10-11, juillot2021ahighcontentmicroscopy pages 8-10). | **Candidate edges**, but inspect mutant-level measurements before asserting `METPO:1000890`. |
| Δrpe | increases | *B. subtilis* cell width variability/mean width | Δrpe increased width by about 11% and produced a 0.7–1.4-μm range (juillot2021ahighcontentmicroscopy pages 5-8). | **Provisional**: population mean may not cross 0.9 μm. |

## 4. Quantitative evidence and recent developments

### Direct width evidence

* A22 treatment and *mreB* point mutations shifted *E. coli* steady-state diameter from **790 ± 30 nm to 1,700 ± 20 nm**, directly spanning the `METPO:1000890` threshold (ouzounov2016mreborientationcorrelates pages 1-2).
* An MreB mutant library covered a **fivefold range in average cell volume** without detectable growth-rate changes; mutations at MreB residue A53 had previously produced widths up to **60% above wild type**. This demonstrates that width can be altered independently of growth rate, arguing against a graph in which rapid growth is the sole proximal cause (shi2017deepphenotypicmapping pages 1-3).
* Across *E. coli* Rod-system mutant datasets, directional MreB-filament density and width had reported **R² values of 0.84–0.99** (dion2018celldiameterin pages 18-19).
* The *B. subtilis* high-content screen examined approximately **3,983 single-gene deletions**, roughly **93% genome coverage**, and identified 13 width-affecting mutations. Seven wider mutants showed approximately **8.9–23.4%** increases (juillot2021ahighcontentmicroscopy pages 4-5, juillot2021ahighcontentmicroscopy pages 2-4).
* Wild-type *B. subtilis* width varied by less than **2%** between conditions in that screen, with cell-to-cell standard deviations of **0.071–0.089 μm**, underscoring that width is normally tightly controlled (juillot2021ahighcontentmicroscopy pages 2-4).

### 2023–2024 mechanistic updates

1. **Outer-membrane mechanics:** A 2023 PNAS study showed that LPS changes predicted to strengthen the *E. coli* outer membrane can rescue growth and shape defects of Rod-complex mutants and restore proper MreB orientation. Thus, the peptidoglycan system is not the only mechanical contributor to shape propagation in Gram-negative organisms (fivenson2023arolefor pages 1-2).
2. **Rod complex and PG architecture:** A 2023 *MicrobiologyOpen* study found that a RodZ transmembrane-domain mutant produced abnormal morphology, slower growth, large holes in purified PG, and altered muropeptide composition. Suppressors mapped mainly to Rod-complex components, supporting the complex as a determinant of PG density and mechanical integrity, although direct width measurements were not the main endpoint (ago2023relationshipbetweenthe pages 1-3).
3. **Elongasome processivity:** Single-molecule work published in 2024 found that *B. subtilis* elongasomes are highly processive but frequently reverse or pause; RodA abundance controls processivity, pausing, and reversal. A likely two-motor tug-of-war along MreB regulates synthesis dynamics, refining the graph below the coarse “Rod complex activity” node (middlemiss2024molecularmotortugofwar pages 1-2).
4. **MreC–MreD activation mechanism:** A 2024 preprint resolved a 3.6-Å *Thermus thermophilus* MreC–MreD structure and used *E. coli* validation to show that disrupting their contacts abolishes Rod activity. This suggests the chain MreD–MreC interaction → activation-compatible MreC conformation → PBP2/RodA activation, but it should remain provisional pending peer-reviewed publication (gilman2024mrecmredstructurereveals pages 1-2).
5. **RodZ depletion and envelope failure:** In 2024, *E. coli* ΔrodZ cells were spherical; MreB CRISPRi reduced expression to **20% of wild type**. ΔrodZ produced **>50-fold** more vesicles, MreB-repressed cells produced **eightfold** more, and about **7%** of ΔrodZ cells had aberrant surface structures. These are strong envelope-failure data, but they do not by themselves prove a steady-state population width above 0.9 μm (ojima2024buddingandexplosive pages 1-2).

## 5. Applications and expert interpretation

### Antibiotic target discovery

The Rod system is a validated morphogenesis vulnerability. A pathway-directed screen of approximately **690,000 compounds** identified 1,300 initially active compounds and eight A22 analogues, illustrating how synthetic interactions with mecillinam can enrich for MreB/Rod-system inhibitors (buss2019pathwaydirectedscreenfor pages 1-2). New MreC–MreD structural information and RodA processivity measurements create additional regulatory targets beyond conventional transpeptidase inhibition (middlemiss2024molecularmotortugofwar pages 1-2, gilman2024mrecmredstructurereveals pages 1-2).

### Morphological profiling

Width and rounding are practical mode-of-action readouts for MreB, PBP2, and envelope-active compounds. However, a TraitMech assertion should preserve the distinction between **a drug causing rounding** and **a measured short-axis width crossing 0.9 μm**. Morphology classifiers can identify candidates, but quantitative segmentation is required for the target trait.

### Cell-factory and envelope engineering

Controlled widening changes surface-to-volume ratio, intracellular volume, wall mechanics, secretion, and lysis susceptibility. The ΔrodZ study links shape disruption to hypervesiculation, while genome-scale *B. subtilis* screening connects width to central metabolism and cell-wall homeostasis (juillot2021ahighcontentmicroscopy pages 4-5, juillot2021ahighcontentmicroscopy pages 5-8, ojima2024buddingandexplosive pages 1-2). Such phenotypes may be useful for extracellular-vesicle production or product recovery, but severe widening commonly brings osmotic fragility and lysis.

### Recommended causal-graph backbone

A conservative graph for `cell_width_large_setpoint_increase` is:

**MreC–MreD/RodZ coupling → PBP2–RodA activation and MreB-guided circumferential synthesis → oriented PG/mechanical anisotropy ┤ radial expansion → decreased probability of `METPO:1000890`.**

Parallel widening branch:

**relative class-A PBP activity and/or inadequately constrained PG hydrolysis → more isotropic or locally excessive wall expansion → increased cell width → `METPO:1000890`.**

Experimental entry points include **A22 → MreB inhibition**, **mecillinam → PBP2 inhibition**, and **Mg²⁺ ┤ PG hydrolase activity**. Nutrient/growth-rate effects should enter upstream only where a study measures width separately from length and volume.

## 6. Warnings: claims not ready for TraitMech curation

1. **Do not equate “larger cell,” increased biomass, or increased volume with large width.** Growth laws often concern volume or mass and may predominantly alter length.
2. **Do not curate rapid growth/nutrient richness → `METPO:1000890` as a universal direct edge.** *B. subtilis* diameter can remain nearly constant across growth conditions, and MreB mutants can vary widely in width without altered growth rate (juillot2021ahighcontentmicroscopy pages 2-4, shi2017deepphenotypicmapping pages 1-3).
3. **Do not treat all MreB filament properties as causal.** Helical pitch angle and directional filament density correlate with diameter, but different studies support different geometric descriptors; retain correlation predicates unless directly manipulated (dion2018celldiameterin pages 18-19, ouzounov2016mreborientationcorrelates pages 1-2).
4. **Do not infer the >0.9-μm class from “round,” “spherical,” “bulged,” or “increased volume” alone.** This applies particularly to ΔrodZ, MreB depletion, mecillinam, and outer-membrane rescue studies.
5. **Keep taxon specificity explicit.** The aPBP-widening/Rod-thinning balance is especially well tested in *B. subtilis* and supported in *E. coli* mutants, but polar-growing Actinobacteria, cocci, wall-less taxa, and organisms lacking canonical MreB require separate models.
6. **Do not assign unverified CURIEs.** Resolve UniProt records against the exact strain and verify chemical ontology records for A22 and mecillinam before YAML insertion.
7. **Treat 2024 preprints as provisional.** The MreC–MreD structural activation edge is compelling but should be marked `uncertain` until peer-reviewed or independently reproduced (gilman2024mrecmredstructurereveals pages 1-2).
8. **Genome-screen hits are associations until mechanistically resolved.** For Rpe, Pyk, PtsH, GuaA, PanD, MinJ, YaaA, and YbzH, avoid direct gene → width causal chains that omit growth impairment, pleiotropy, or cell-wall intermediates (juillot2021ahighcontentmicroscopy pages 8-10, juillot2021ahighcontentmicroscopy pages 5-8).

## DOI-first bibliography

1. **Middlemiss S, et al.** “Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in *Bacillus subtilis*.” *Nature Communications* 15, 5411. Published June 2024. https://doi.org/10.1038/s41467-024-49785-x (middlemiss2024molecularmotortugofwar pages 1-2)
2. **Ojima Y, et al.** “Budding and explosive membrane vesicle production by hypervesiculating *Escherichia coli* strain ΔrodZ.” *Frontiers in Microbiology* 15:1400434. Published June 20, 2024. https://doi.org/10.3389/fmicb.2024.1400434 (ojima2024buddingandexplosive pages 1-2)
3. **Gilman MSA, et al.** “MreC-MreD structure reveals a multifaceted interface that controls MreC conformation.” bioRxiv. Posted October 2024. https://doi.org/10.1101/2024.10.08.617240 (gilman2024mrecmredstructurereveals pages 1-2)
4. **Ago R, et al.** “Relationship between the Rod complex and peptidoglycan structure in *Escherichia coli*.” *MicrobiologyOpen* 12. Published October 2023. https://doi.org/10.1002/mbo3.1385 (ago2023relationshipbetweenthe pages 1-3)
5. **Fivenson EM, et al.** “A role for the Gram-negative outer membrane in bacterial shape determination.” *PNAS* 120:e2301987120. Published August 22, 2023. https://doi.org/10.1073/pnas.2301987120 (fivenson2023arolefor pages 1-2)
6. **Tesson B, et al.** “Magnesium rescues the morphology of *Bacillus subtilis mreB* mutants through its inhibitory effect on peptidoglycan hydrolases.” *Scientific Reports* 12:1137. Published January 2022. https://doi.org/10.1038/s41598-021-04294-5 (tesson2022magnesiumrescuesthe pages 1-2)
7. **Juillot D, et al.** “A High-Content Microscopy Screening Identifies New Genes Involved in Cell Width Control in *Bacillus subtilis*.” *mSystems* 6. Published December 2021. https://doi.org/10.1128/msystems.01017-21 (juillot2021ahighcontentmicroscopy pages 4-5, juillot2021ahighcontentmicroscopy pages 2-4)
8. **Dion MF, et al.** “*Bacillus subtilis* cell diameter is determined by the opposing actions of two distinct cell wall synthetic systems.” *Nature Microbiology* 4:1294–1305. Published May 2019. https://doi.org/10.1038/s41564-019-0439-0. Retrieved mechanistic evidence was from its 2018 preprint, https://doi.org/10.1101/392837 (dion2018celldiameterin pages 3-6, dion2018celldiameterin pages 1-3)
9. **Buss JA, et al.** “Pathway-Directed Screen for Inhibitors of the Bacterial Cell Elongation Machinery.” *Antimicrobial Agents and Chemotherapy* 63:e01530-18. Published December 21, 2018/January 2019 issue. https://doi.org/10.1128/AAC.01530-18 (buss2019pathwaydirectedscreenfor pages 1-2)
10. **Shi H, et al.** “Deep Phenotypic Mapping of Bacterial Cytoskeletal Mutants Reveals Physiological Robustness to Cell Size.” *Current Biology* 27:3419–3429.e4. Published November 20, 2017. https://doi.org/10.1016/j.cub.2017.09.065 (shi2017deepphenotypicmapping pages 1-3)
11. **Ouzounov N, et al.** “MreB Orientation Correlates with Cell Diameter in *Escherichia coli*.” *Biophysical Journal* 111:1035–1043. Published September 6, 2016. https://doi.org/10.1016/j.bpj.2016.07.017 (ouzounov2016mreborientationcorrelates pages 1-2)

References

1. (dion2018celldiameterin pages 3-6): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

2. (dion2018celldiameterin pages 18-19): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

3. (dion2018celldiameterin pages 8-10): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

4. (dion2018celldiameterin pages 1-3): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

5. (dion2018celldiameterin pages 10-12): Michael F. Dion, Mrinal Kapoor, Yingjie Sun, Sean Wilson, Joel Ryan, Antoine Vigouroux, Sven van Teeffelen, Rudolf Oldenbourg, and Ethan C. Garner. Cell diameter in bacillus subtilis is determined by the opposing actions of two distinct cell wall synthetic systems. bioRxiv, Aug 2018. URL: https://doi.org/10.1101/392837, doi:10.1101/392837. This article has 6 citations.

6. (ouzounov2016mreborientationcorrelates pages 1-2): Nikolay Ouzounov, Jeffrey P. Nguyen, Benjamin P. Bratton, David Jacobowitz, Zemer Gitai, and Joshua W. Shaevitz. Mreb orientation correlates with cell diameter in escherichia coli. Biophysical journal, 111 5:1035-43, Sep 2016. URL: https://doi.org/10.1016/j.bpj.2016.07.017, doi:10.1016/j.bpj.2016.07.017. This article has 118 citations and is from a domain leading peer-reviewed journal.

7. (shi2017deepphenotypicmapping pages 1-3): Handuo Shi, Alexandre Colavin, Marty Bigos, Carolina Tropini, Russell D. Monds, and Kerwyn Casey Huang. Deep phenotypic mapping of bacterial cytoskeletal mutants reveals physiological robustness to cell size. Current Biology, 27:3419-3429.e4, Nov 2017. URL: https://doi.org/10.1016/j.cub.2017.09.065, doi:10.1016/j.cub.2017.09.065. This article has 83 citations and is from a highest quality peer-reviewed journal.

8. (buss2019pathwaydirectedscreenfor pages 1-2): Jackson A. Buss, Vadim Baidin, Michael A. Welsh, Josué Flores-Kim, Hongbaek Cho, B. McKay Wood, Tsuyoshi Uehara, Suzanne Walker, Daniel Kahne, and Thomas G. Bernhardt. Pathway-directed screen for inhibitors of the bacterial cell elongation machinery. Antimicrobial Agents and Chemotherapy, Jan 2019. URL: https://doi.org/10.1128/aac.01530-18, doi:10.1128/aac.01530-18. This article has 32 citations and is from a highest quality peer-reviewed journal.

9. (ojima2024buddingandexplosive pages 1-2): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 9 citations and is from a peer-reviewed journal.

10. (tesson2022magnesiumrescuesthe pages 1-2): Benoit Tesson, Alex Dajkovic, Ruth Keary, Christian Marlière, Christine C. Dupont-Gillain, and Rut Carballido-López. Magnesium rescues the morphology of bacillus subtilis mreb mutants through its inhibitory effect on peptidoglycan hydrolases. Scientific Reports, Jan 2022. URL: https://doi.org/10.1038/s41598-021-04294-5, doi:10.1038/s41598-021-04294-5. This article has 37 citations and is from a peer-reviewed journal.

11. (fivenson2023arolefor pages 1-2): Elayne M. Fivenson, Patricia D. A. Rohs, Andrea Vettiger, Marios F. Sardis, Grasiela Torres, Alison Forchoh, and Thomas G. Bernhardt. A role for the gram-negative outer membrane in bacterial shape determination. Proceedings of the National Academy of Sciences of the United States of America, Aug 2023. URL: https://doi.org/10.1073/pnas.2301987120, doi:10.1073/pnas.2301987120. This article has 98 citations and is from a highest quality peer-reviewed journal.

12. (gilman2024mrecmredstructurereveals pages 1-2): Morgan S.A. Gilman, Irina Shlosman, Daniel D. Samé Guerra, Masy Domecillo, Elayne M. Fivenson, Claire Bourett, Thomas G. Bernhardt, Nicholas F. Polizzi, Joseph J. Loparo, and Andrew C. Kruse. Mrec-mred structure reveals a multifaceted interface that controls mrec conformation. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.08.617240, doi:10.1101/2024.10.08.617240. This article has 2 citations.

13. (middlemiss2024molecularmotortugofwar pages 1-2): Stuart Middlemiss, Matthieu Blandenet, David M. Roberts, Andrew McMahon, James Grimshaw, Joshua M. Edwards, Zikai Sun, Kevin D. Whitley, Thierry Blu, Henrik Strahl, and Séamus Holden. Molecular motor tug-of-war regulates elongasome cell wall synthesis dynamics in bacillus subtilis. Nature Communications, Jun 2024. URL: https://doi.org/10.1038/s41467-024-49785-x, doi:10.1038/s41467-024-49785-x. This article has 22 citations and is from a highest quality peer-reviewed journal.

14. (juillot2021ahighcontentmicroscopy pages 10-11): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 16 citations and is from a peer-reviewed journal.

15. (juillot2021ahighcontentmicroscopy pages 8-10): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 16 citations and is from a peer-reviewed journal.

16. (juillot2021ahighcontentmicroscopy pages 5-8): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 16 citations and is from a peer-reviewed journal.

17. (juillot2021ahighcontentmicroscopy pages 4-5): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 16 citations and is from a peer-reviewed journal.

18. (juillot2021ahighcontentmicroscopy pages 2-4): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 16 citations and is from a peer-reviewed journal.

19. (ago2023relationshipbetweenthe pages 1-3): Risa Ago, Yuhei O. Tahara, Honoka Yamaguchi, Motoya Saito, Wakana Ito, Kaito Yamasaki, Taishi Kasai, Sho Okamoto, Taiki Chikada, Taku Oshima, Issey Osaka, Makoto Miyata, Hironori Niki, and Daisuke Shiomi. Relationship between the rod complex and peptidoglycan structure in escherichia coli. MicrobiologyOpen, Oct 2023. URL: https://doi.org/10.1002/mbo3.1385, doi:10.1002/mbo3.1385. This article has 17 citations and is from a peer-reviewed journal.