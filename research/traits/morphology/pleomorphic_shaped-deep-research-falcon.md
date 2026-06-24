---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T09:00:18.353575'
end_time: '2026-06-18T09:19:11.605734'
duration_seconds: 1133.25
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: pleomorphic shaped
  trait_identifier: METPO:1000679
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: pleomorphic_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape characterized by variable and irregular morphology, where
    individual cells within a population exhibit multiple distinct shapes.
  parent_traits: METPO:1000666
  synonyms: S_star_dumbbell_pleomorphic, pleomorphic, pleomorphic-shaped
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review establishes pleomorphism as a phenotype of relaxed
    or absent cytoskeletal/wall shape control.) | DOI:10.1126/science.1170701: cell-wall-deficient
    L-forms (L-form review supports pleomorphism in wall-deficient or wall-less cells.)'
  causal_graph_summary: 'pleomorphic_shaped_relaxed_shape_control: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** pleomorphic shaped
- **METPO identifier:** METPO:1000679
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by variable and irregular morphology, where individual cells within a population exhibit multiple distinct shapes.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, pleomorphic, pleomorphic-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review establishes pleomorphism as a phenotype of relaxed or absent cytoskeletal/wall shape control.) | DOI:10.1126/science.1170701: cell-wall-deficient L-forms (L-form review supports pleomorphism in wall-deficient or wall-less cells.)
- **Existing causal graph summary:** pleomorphic_shaped_relaxed_shape_control: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pleomorphic shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pleomorphic_shaped.yaml`.

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
- **Trait label:** pleomorphic shaped
- **METPO identifier:** METPO:1000679
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape characterized by variable and irregular morphology, where individual cells within a population exhibit multiple distinct shapes.
- **Parent traits:** METPO:1000666
- **Synonyms:** S_star_dumbbell_pleomorphic, pleomorphic, pleomorphic-shaped
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review establishes pleomorphism as a phenotype of relaxed or absent cytoskeletal/wall shape control.) | DOI:10.1126/science.1170701: cell-wall-deficient L-forms (L-form review supports pleomorphism in wall-deficient or wall-less cells.)
- **Existing causal graph summary:** pleomorphic_shaped_relaxed_shape_control: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **pleomorphic shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/pleomorphic_shaped.yaml`.

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


## Microbial trait causal-graph research report: **Pleomorphic shaped** (METPO:1000679)

### 0) Scope summary (curation-ready)
**Trait meaning.** *Pleomorphic shaped* refers to a **cell shape phenotype characterized by variable and irregular morphology within a population**, rather than a single stable geometry (rod/coccus/spirillum). In microbes this is commonly observed when **normal shape-control systems are relaxed or absent**, especially during **cell-wall-deficient (CWD) states** such as **L-forms**, **protoplasts**, and **spheroplasts**. In these states, cells lose the rigid peptidoglycan sacculus and become osmotically sensitive, flexible, and morphologically heterogeneous (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 1-2, claessen2019cellwalldeficiency pages 2-5).

**Boundary cases and near-traits.**
- **Pleomorphism vs filamentation:** filamentous forms are long/elongated but typically maintain a consistent diameter and axis; pleomorphism implies irregular forms (spherical, angular, budding, vesiculating) within the same population (tian2024implementationoffluorescentproteinbased pages 1-2, errington2016lformbacteriachronic pages 1-2).
- **Pleomorphism vs dimorphism:** dimorphism involves regulated switching between **two defined morphotypes** (often life-cycle-linked). Pleomorphism is broader heterogeneity, often reflecting loss/relaxation of morphological constraints.
- **Spheroplasts vs L-forms:** in Gram-negative bacteria, β-lactam exposure can yield **spheroplasts** that remain intact due to a load-bearing **outer membrane**, whereas **L-forms** are typically defined operationally as cells able to **proliferate without the FtsZ division machine and without peptidoglycan synthesis** under osmoprotective conditions (claessen2019cellwalldeficiency pages 2-5, errington2017cellwalldeficientlform pages 1-2).

### 1) Key concepts and definitions (current understanding)
#### 1.1 L-forms as a dominant mechanistic route to pleomorphism
Authoritative synthesis describes **L-forms** as bacterial variants that **grow in the complete absence of cell wall synthesis**, with **loss of regular shape** and **pleomorphic morphology**, and resistance to many wall-targeting antibiotics (errington2016lformbacteriachronic pages 2-3). L-form proliferation is described as a **blebbing/tubulation-and-scission** process that is **independent of the FtsZ-based division machinery** and is driven by **increased membrane synthesis** that raises the surface-area-to-volume ratio (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 1-2).

#### 1.2 Stress-coping view of cell wall deficiency
A broad review frames CWD as a **coping strategy for stress**, triggered by β-lactams, osmotic stress, and host environments, and highlights that CWD survival requires management of **oxidative stress** and altered metabolism (claessen2019cellwalldeficiency pages 1-2, claessen2019cellwalldeficiency pages 2-5).

### 2) Recent developments (prioritizing 2023–2024)
#### 2.1 Quantitative morphology measurement and standardized labeling in L-forms (2024)
A 2024 study developed **fluorescent-protein labeling and quantitative imaging flow cytometry** workflows for L-forms in *Bacillus subtilis* and *Escherichia coli*, explicitly noting that rod-shaped bacteria can become **spherical or pleomorphic due to lack of cell walls** and that L-forms show **morphological complexity and heterogeneity** (tian2024implementationoffluorescentproteinbased pages 1-2). The paper provides figure-level evidence of **spherical and pleomorphic shapes** in *B. subtilis* L-forms and **spherical/enlarged** *E. coli* L-form morphologies with quantitative IFC descriptors (aspect ratio/size metrics) (tian2024implementationoffluorescentproteinbased media 868f7058, tian2024implementationoffluorescentproteinbased media ce88008d).

#### 2.2 Archaeal pleomorphism: CetZ cytoskeleton-mediated shape switching (2024 preprint)
In the pleomorphic archaeon *Haloferax volcanii*, a 2024 preprint reports that **tubulin-like cytoskeletal proteins CetZ1 and CetZ2 have opposing effects on cell morphology across growth phases**. **CetZ1 is required for plate→rod transition** in early–mid log phase, while **CetZ2 is upregulated in stationary phase** and supports **maintenance of plate/disk morphology**, counteracting CetZ1-driven rod development (brown2024archaealtubulinlikeproteins pages 1-5, brown2024archaealtubulinlikeproteins pages 5-7). Quantitatively, the authors report a **shift in the CetZ1:CetZ2 ratio from ~41:1 in mid-log to ~5:1 in stationary phase**, consistent with growth-phase-dependent shape control (brown2024archaealtubulinlikeproteins pages 5-7). Genetic perturbations show causal morphology effects (e.g., **cetZ2 deletion increased elongation**, and **CetZ2 overexpression increased circularity**) (brown2024archaealtubulinlikeproteins pages 5-7).

#### 2.3 Membrane-centric thinking in minimal/wall-less contexts (2024)
A 2024 *Nature Communications* paper on tunable minimal membranes in *Mycoplasma mycoides* and minimal cells references pleomorphism/irregular division in wall-less contexts and situates pleomorphism within a growing set of studies linking membrane properties (composition/fluidity/vesiculation) to division and shape control in simplified cells (justice2024atuneableminimala pages 14-15).

### 3) Current applications and real-world implementations
#### 3.1 Clinical relevance: pleomorphic CWD forms as reservoirs during antibiotic treatment
- **Recurrent UTI:** L-form bacteria were reported in **fresh urine from 29/30 older patients** with recurrent UTI; patient *E. coli* isolates could transition to L-form during **cell-wall-targeting antibiotic challenge** and revert after antibiotic withdrawal, supporting a clinically relevant switching model (errington2016lformbacteriachronic pages 3-4).
- **Chronic bacteriuria/pyelonephritis:** an earlier report summarized in a major review found L-forms (*E. coli*, *Klebsiella* spp., *Enterococcus faecalis*) in **11/57 patients** with chronic bacteriuria or pyelonephritis, underscoring the need for osmoprotective culture/detection approaches (errington2016lformbacteriachronic pages 3-4).

These clinical observations motivate causal-graph nodes for **host environment (urine)**, **cell-wall antibiotics**, and **L-form switching** as a contributor to persistence/recurrence (errington2016lformbacteriachronic pages 3-4).

#### 3.2 Experimental platforms and biotechnology
- **Quantitative phenotyping platforms:** Confocal microscopy and imaging flow cytometry (IFC) pipelines enable standardized quantification of L-form pleomorphism and heterogeneity, useful for perturbation screens (tian2024implementationoffluorescentproteinbased media 868f7058, tian2024implementationoffluorescentproteinbased pages 1-2).
- **Origins-of-life / synthetic cell models:** L-forms and wall-less/minimal cells are repeatedly framed as experimentally tractable systems for studying primitive proliferation and minimal requirements for cellular life (errington2017cellwalldeficientlform pages 1-2, tian2024implementationoffluorescentproteinbased pages 1-2).

### 4) Expert opinions / authoritative synthesis (mechanistic interpretation)
Across authoritative reviews, a coherent mechanistic picture emerges:
1. **Primary trigger:** interruption of **peptidoglycan precursor synthesis** (genetically or via antibiotics) plus the ability to escape the sacculus leads to a CWD state (errington2016lformbacteriachronic pages 1-2, claessen2019cellwalldeficiency pages 2-5).
2. **Key enabling condition:** **osmoprotective/high-osmolarity media** are required to avoid osmotic lysis and permit proliferation (errington2017cellwalldeficientlform pages 1-2).
3. **Core proliferative driver:** **excess membrane synthesis** leads to surface-area-to-volume imbalance and blebbing/vesiculation-based proliferation (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 1-2).
4. **Major constraint:** **ROS/oxidative damage** limits wall-free growth; secondary adaptations that reduce respiratory-chain ROS or increase oxidative stress defenses enable stable growth (claessen2019cellwalldeficiency pages 2-5, errington2017cellwalldeficientlform pages 7-8).
5. **Division mechanism change:** proliferation can be **FtsZ-independent** in L-forms (errington2017cellwalldeficientlform pages 1-2).

### 5) Candidate causal-graph nodes (grouped by type)
#### 5.1 Phenotypes / states
- Pleomorphic shaped (METPO:1000679)
- Cell-wall-deficient state / L-form state (label-only node; definition in reviews) (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 2-3)
- Protoplast; spheroplast (label-only nodes; boundary states) (claessen2019cellwalldeficiency pages 2-5, errington2016lformbacteriachronic pages 2-3)

#### 5.2 Cellular structures and processes
- Peptidoglycan (PG) cell wall; sacculus; lipid II precursor pathway (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 2-3)
- Penicillin-binding proteins (PBPs), transpeptidases; SEDS (RodA/FtsW) polymerases (errington2017cellwalldeficientlform pages 1-2, errington2017cellwalldeficientlform pages 8-9)
- Membrane synthesis; fatty-acid synthesis; surface area-to-volume ratio changes (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 1-2)
- ROS generation; oxidative stress response; respiratory chain modulation (claessen2019cellwalldeficiency pages 2-5, errington2017cellwalldeficientlform pages 7-8)
- FtsZ-based division machinery (dispensable in L-form proliferation) (errington2017cellwalldeficientlform pages 1-2)

#### 5.3 Genes/proteins/complexes
- **AccDA acetyl-CoA carboxylase** (fatty-acid synthesis activation/overproduction linked to L-form switch) (errington2016lformbacteriachronic pages 2-3)
- **FtsZ** (division machinery; dispensable in L-form proliferation) (errington2017cellwalldeficientlform pages 1-2)
- **MreB** (shape/elongation system referenced as part of walled shape control) (errington2016lformbacteriachronic pages 2-3, errington2017cellwalldeficientlform pages 1-2)
- **CetZ1, CetZ2** (archaeal tubulin-like proteins controlling morphology across growth phases) (brown2024archaealtubulinlikeproteins pages 1-5, brown2024archaealtubulinlikeproteins pages 5-7)

#### 5.4 Chemicals / inhibitors / osmolytes
- β-lactam antibiotics (cell-wall synthesis inhibitors; promote CWD/L-form emergence in permissive contexts) (claessen2019cellwalldeficiency pages 2-5)
- Fosfomycin/phosphomycin (cell wall precursor synthesis inhibitor; induces L-form switch in reviews) (errington2017cellwalldeficientlform pages 1-2)
- D-cycloserine (induces pleomorphic/spherical L-form morphologies in *B. subtilis* in 2024 quantification study) (tian2024implementationoffluorescentproteinbased media 868f7058)
- Lysozyme (promotes emergence of L-forms in host-relevant contexts) (tian2024implementationoffluorescentproteinbased pages 12-13)
- Osmoprotectants (sucrose/NaCl/glycine betaine; serum; soft agar) (purkayastha2024isolation&characterization pages 102-106, errington2017cellwalldeficientlform pages 1-2)

#### 5.5 Environmental/experimental factors
- Osmoprotective/high-osmolarity growth medium (required enabling condition) (errington2017cellwalldeficientlform pages 1-2)
- Host urine environment + antibiotic challenge (clinical switching context) (errington2016lformbacteriachronic pages 3-4)
- Growth phase (stationary vs log phase for archaeal CetZ-dependent switching) (brown2024archaealtubulinlikeproteins pages 5-7)

### 6) Candidate causal edges (evidence-backed)
The table below is intended for direct translation into `pleomorphic_shaped.yaml` edges (subject–predicate–object), with uncertainty flags.

| Subject node | Predicate | Object node | Node types (subject/object) | Evidence snippet | Source (DOI, year, URL) | Notes/uncertainty |
|---|---|---|---|---|---|---|
| Inhibition of peptidoglycan / cell-wall precursor synthesis | causes transition to | L-form / wall-deficient pleomorphic state | biological process / cell state | “repression or inhibition of cell wall precursor synthesis can stimulate the L-form transition in a wide range of bacteria” (errington2016lformbacteriachronic pages 1-2) | 10.1098/rstb.2015.0494, 2016, https://doi.org/10.1098/rstb.2015.0494 | Strong general mechanism across Gram+ and Gram− bacteria. |
| β-lactam antibiotics | promote emergence of | L-form bacteria | chemical / cell state | “cell-wall-targeting antibiotics even promote the conversion to a wall-deficient state” and “host lytic enzymes, such as lysozyme” contribute (claessen2019cellwalldeficiency pages 2-5, claessenUnknownyearerrington.(2019) pages 7-8) | 10.1016/j.tim.2019.07.008, 2019, https://doi.org/10.1016/j.tim.2019.07.008 | Strong but context-dependent; usually requires permissive/osmoprotective conditions. |
| Penicillin G (300 µg/ml HG001; 2000 µg/ml JE2) | induces | Staphylococcus aureus L-forms with pleomorphic budding/large-body morphology | chemical / phenotype | “Conversion to wall-defective L-forms was induced experimentally with high-dose penicillin G (300 µg/ml for HG001; 2000 µg/ml for MRSA JE2)… L-forms show hallmarks of pleomorphism — larger cell size, vacuolation, budding” (purkayastha2024isolation&characterization pages 97-102) | 2024 dissertation text, URL not established in gathered snippets | Experimental, taxon-specific; useful as assay edge rather than universal mechanism. |
| Cephalosporin | induces | Staphylococcus aureus L-forms | chemical / cell state | “L-forms were induced experimentally by cell-wall inhibitors (Penicillin G; Cephalosporin)” (purkayastha2024isolation&characterization pages 157-160) | 2024 dissertation text, URL not established in gathered snippets | Taxon- and assay-specific. |
| Lysozyme | promotes emergence of | L-form bacteria | protein/enzyme / cell state | “Lysozyme Counteracts β-Lactam Antibiotics by Promoting the Emergence of L-Form Bacteria” and reviews summarize lysozyme as an inducer (tian2024implementationoffluorescentproteinbased pages 12-13, purkayastha2024isolation&characterization pages 102-106) | 10.1016/j.cell.2018.01.021, 2018, https://doi.org/10.1016/j.cell.2018.01.021 | Strong for host-associated induction; may act with β-lactams. |
| Osmoprotective medium | enables survival/growth of | pleomorphic L-forms | environment / phenotype | “They grow robustly provided that lack of the cell wall is compensated for by an osmoprotective growth medium” (errington2017cellwalldeficientlform pages 1-2) | 10.1042/bst20160435, 2017, https://doi.org/10.1042/bst20160435 | Strong enabling condition; not sufficient alone to cause pleomorphism. |
| Isotonic / osmoprotective media (sucrose, NaCl, glycine betaine; serum; soft agar) | supports induction/propagation of | unstable L-forms / pleomorphic wall-deficient cells | environment / cell state | “unstable forms can be induced by cell-wall inhibitors under appropriate osmotic conditions” and culturing requires “isotonic/osmoprotective media (e.g., sucrose, NaCl, glycine betaine)” (purkayastha2024isolation&characterization pages 102-106) | 2024 dissertation text, URL not established in gathered snippets | Good curation node for experimental factor. |
| Excess membrane synthesis | drives proliferation of | wall-free pleomorphic L-forms | biological process / phenotype | “increasing membrane synthesis… promotes the unusual form of proliferation used by L-forms, involving a range of relatively disorganized membrane blebbing or vesiculation events” (errington2016lformbacteriachronic pages 1-2) | 10.1098/rstb.2015.0494, 2016, https://doi.org/10.1098/rstb.2015.0494 | Strong core mechanistic edge. |
| AccDA acetyl-CoA carboxylase overproduction | increases | fatty-acid membrane synthesis | protein complex / biological process | “activation of fatty acid membrane synthetic pathway (overproduction of AccDA acetyl-CoA carboxylase)” (errington2016lformbacteriachronic pages 2-3) | 10.1098/rstb.2015.0494, 2016, https://doi.org/10.1098/rstb.2015.0494 | Specific genetic example from Bacillus subtilis L-form switch. |
| Increased membrane synthesis / elevated surface area-to-volume ratio | enables | blebbing-tubulation-scission proliferation of pleomorphic L-forms | biological process / biological process | “This proliferation appears to require only an increased rate of membrane synthesis, producing an increased surface area-to-volume ratio” (errington2017cellwalldeficientlform pages 1-2) | 10.1042/bst20160435, 2017, https://doi.org/10.1042/bst20160435 | Strong mechanistic edge; broadly cited in L-form literature. |
| Oxidative stress / ROS from respiratory chain | limits or kills | wall-deficient protoplasts / L-forms | biological process / cell state | “reactive oxygen species (ROS) are formed, causing oxidative stress and ultimately killing the wall-deficient cells” (claessen2019cellwalldeficiency pages 2-5) | 10.1016/j.tim.2019.07.008, 2019, https://doi.org/10.1016/j.tim.2019.07.008 | Strong negative constraint edge. |
| Downregulation of respiratory chain activity / upregulation of oxidative stress response genes | relieves | oxidative stress limiting L-form growth | biological process / biological process | “class 2… ‘counteraction of ROS originating from the respiratory chain’ via ‘down regulation of respiratory chain activity’ and ‘up regulation of oxidative stress response genes’” (errington2016lformbacteriachronic pages 2-3) | 10.1098/rstb.2015.0494, 2016, https://doi.org/10.1098/rstb.2015.0494 | Strong in Bacillus model; broader generality plausible but inferred. |
| FtsZ-based division machinery | dispensable for proliferation of | pleomorphic L-forms | protein / phenotype | “L-forms proliferate by an unusual blebbing/tubulation-and-scission mechanism that is completely independent of the normal FtsZ-based division machinery” (errington2017cellwalldeficientlform pages 1-2) | 10.1042/bst20160435, 2017, https://doi.org/10.1042/bst20160435 | Curate as absence-of-requirement edge rather than positive cause. |
| Loss of cell wall | causes | spherical or pleomorphic morphology from rod-shaped bacteria | cell envelope state / phenotype | “rod-shaped bacteria, e.g., Escherichia coli and Bacillus subtilis, exhibit spherical or pleomorphic shapes due to the lack of cell walls” (tian2024implementationoffluorescentproteinbased pages 1-2) | 10.3390/bioengineering11010081, 2024, https://doi.org/10.3390/bioengineering11010081 | Recent direct summary; good phenotype-level edge. |
| D-cycloserine treatment | induces | spherical and pleomorphic shapes in Bacillus subtilis L-form LR2 | chemical / phenotype | “Figure 3… shows the transition to spherical and pleomorphic shapes upon treatment with D-cycloserine (DCS)” (tian2024implementationoffluorescentproteinbased media 868f7058) | 10.3390/bioengineering11010081, 2024, https://doi.org/10.3390/bioengineering11010081 | Assay-specific but quantitatively supported by IFC morphology metrics in source figure. |
| Outer membrane rigidity / load-bearing function | maintains | pleomorphic/angular shapes in Gram-negative wall-deficient cells | cell component / phenotype | E. coli NC-7 “showed a variety of morphologies including spherical, angular and cylindrical cells… We suggest that the mechanical rigidity of the outer membrane enables the angular shapes” (tian2024implementationoffluorescentproteinbased pages 1-2) | 10.1099/mic.0.000799, 2019, https://doi.org/10.1099/mic.0.000799 | Strong for Gram-negative spheroplast/L-form boundary case; not universal across bacteria. |
| EDTA-mediated reduction of outer-membrane rigidity | induces division before lysis in | elongated E. coli L-forms | chemical / biological process | “cells that had an elongated shape underwent division shortly after addition of EDTA, suggesting that reducing the rigidity of the outer membrane… induces division before lysis occurs” (tian2024implementationoffluorescentproteinbased pages 1-2) | 10.1099/mic.0.000799, 2019, https://doi.org/10.1099/mic.0.000799 | Weaker because exact snippet is from search summary rather than gathered context; curation caution. |
| Lysostaphin resistance in S. aureus L-forms | indicates reduction/alteration of | peptidoglycan cell wall | phenotype / cell component | “L-form variants displayed resistance to Lysostaphin treatment” and FL-vancomycin signal was “notably weaker in L-forms” (purkayastha2024isolation&characterization pages 160-165, purkayastha2024isolation&characterization pages 157-160) | 2024 dissertation text, URL not established in gathered snippets | Supportive evidence for wall loss underpinning pleomorphism; not itself causal. |
| S. aureus L-form state | associated with | larger/variable cell bodies (~0.75 µm L-forms; ~1 µm vesicles vs WT 0.85 µm HG001, 0.50 µm JE2) | cell state / phenotype | “wild-type HG001 ~0.85 µm, JE2 ~0.50 µm, L-forms ~0.75 µm, and large vesicles ≈1 µm” (purkayastha2024isolation&characterization pages 157-160) | 2024 dissertation text, URL not established in gathered snippets | Quantitative phenotype support; descriptive edge, not upstream mechanism. |
| Recurrent UTI urine environment + cell-wall-targeting antibiotic challenge | permits switching to | L-form state in patient E. coli | environment/assay / cell state | “cell-wall deficient (L-form) bacteria in fresh urine from 29 out of 30 older patients with rUTI. In urine, E. coli strains… readily transition from the walled state to L-form during challenge with a cell wall targeting antibiotic” (errington2016lformbacteriachronic pages 3-4) | 10.1038/s41467-019-12359-3, 2019, https://doi.org/10.1038/s41467-019-12359-3 | Strong real-world relevance; environment- and taxon-specific. |
| Chronic bacteriuria / pyelonephritis isolates under osmoprotective culture | reveal presence of | L-forms of E. coli, Klebsiella spp., Enterococcus faecalis | clinical context / phenotype | “L-forms of Escherichia coli, Klebsiella spp. and Enterococcus faecalis from 11 of 57 patients” (errington2016lformbacteriachronic pages 3-4) | 10.1098/rstb.2015.0494, 2016, https://doi.org/10.1098/rstb.2015.0494 | Clinical observation supports prevalence/relevance, not direct mechanism. |
| CetZ1 | required for | plate-to-rod transition in Haloferax volcanii | protein / phenotype | “CetZ1 is required for the plate→rod transition during early–mid log phase” (brown2024archaealtubulinlikeproteins pages 1-5) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Strong but archaeal/taxon-specific; preprint. |
| CetZ1 dynamic GTP-dependent polymerization–depolymerization | enables | rod development / morphogenesis | molecular function / phenotype | “its dynamic, GTP-dependent polymerisation–depolymerisation cycle… [is] linked causally to rod development” and CetZ1.E218A “prevents rod formation” (brown2024archaealtubulinlikeproteins pages 1-5) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Strong in H. volcanii; preprint. |
| CetZ2 upregulation in stationary phase | promotes maintenance of | plate/disk morphology | protein regulation / phenotype | “CetZ2 is upregulated… [and] promotes and maintains the plate/disk morphology” (brown2024archaealtubulinlikeproteins pages 1-5) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Strong but archaeal/taxon-specific; preprint. |
| Increased CetZ2:CetZ1 abundance ratio (CetZ1:CetZ2 shifts ~41:1 mid-log to ~5:1 stationary) | associated with | stationary-phase plate-shape maintenance | quantitative abundance change / phenotype | “shifting the CetZ1:CetZ2 ratio from ~41:1 in mid-log to ~5:1 in stationary” and CetZ2 role is “maintenance of plate-shape in stationary phase” (brown2024archaealtubulinlikeproteins pages 5-7) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Quantitative support for growth-phase mechanism; association stronger than direct causation. |
| CetZ2 | counteracts | CetZ1-based rod-development pathway | protein / biological process | “CetZ2 counteracts the CetZ1-based rod-development pathway to maintain plate shape” (brown2024archaealtubulinlikeproteins pages 1-5) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Strong model from preprint; likely curate as archaeal branch. |
| cetZ2 deletion | increases | cell elongation in H. volcanii stationary phase | gene / phenotype | “deletion of cetZ2 resulted in more elongation of cells (120 h)” (brown2024archaealtubulinlikeproteins pages 5-7) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Direct perturbation evidence; archaeal/taxon-specific. |
| CetZ2 overexpression or GTPase-defective CetZ2.E212A | increases | circularity / distorted cell shapes | gene expression variant / phenotype | “overexpression of cetZ2 or cetZ2.E212A increased cell circularity” and CetZ2.E212A caused “distorted cell shapes” (brown2024archaealtubulinlikeproteins pages 5-7) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Strong perturbation evidence; archaeal/taxon-specific. |
| CetZ1 presence | required for proper localization/dynamics of | CetZ2 structures | protein / protein behavior | “CetZ2 localization and dynamics require CetZ1: in a ΔcetZ1 background CetZ2 mis-localizes as discrete immobile foci” (brown2024archaealtubulinlikeproteins pages 7-9) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Mechanistic interdependency within archaeal cytoskeleton. |
| CetZ2 presence | modulates/stabilizes | CetZ1 filaments and inhibits rod formation | protein / protein behavior | “absence of CetZ2 yields more large CetZ1 filaments” and “CetZ2 can lead to inhibition of CetZ1 filament formation yet can stabilize CetZ1 filaments if they form” (brown2024archaealtubulinlikeproteins pages 7-9) | 10.1101/2024.10.29.620987, 2024, https://doi.org/10.1101/2024.10.29.620987 | Mechanistic but nuanced; curate with note on phase specificity and possible indirect effects. |


*Table: This table compiles candidate subject-predicate-object edges for curating the pleomorphic shaped trait, with evidence snippets, DOI-first sourcing, and notes on uncertainty. It emphasizes core L-form/wall-deficiency mechanisms and an archaeal CetZ-based shape-control branch, while preserving quantitative details useful for TraitMech curation.*

### 7) Ontology grounding suggestions (CURIE recommendations)
Because the evidence excerpts do not provide explicit ontology CURIEs, grounding is given at the **ontology-class level**, suitable for manual lookup during YAML curation.

**GO (process / function / component)**
- Peptidoglycan biosynthetic process (GO term; referenced via lipid II and PG synthesis/insertion pathways) (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 2-3)
- Cell division (GO term), FtsZ-dependent cytokinesis (GO term) (errington2017cellwalldeficientlform pages 1-2)
- Fatty acid biosynthetic process / membrane lipid biosynthesis (GO term; linked to AccDA activation and excess membrane synthesis) (errington2016lformbacteriachronic pages 2-3, errington2017cellwalldeficientlform pages 1-2)
- Response to oxidative stress / reactive oxygen species metabolic process (GO terms; ROS constraint and adaptations) (claessen2019cellwalldeficiency pages 2-5, errington2017cellwalldeficientlform pages 7-8)

**CHEBI (chemicals)**
- β-lactam antibiotic (CHEBI class) (claessen2019cellwalldeficiency pages 2-5)
- Fosfomycin (CHEBI entry; also called phosphomycin in some texts) (errington2017cellwalldeficientlform pages 1-2)
- D-cycloserine (CHEBI entry) (tian2024implementationoffluorescentproteinbased media 868f7058)
- Lysozyme is a protein (not CHEBI); consider GO molecular function “lysozyme activity” and/or UniProt protein family; mechanistic role supported (tian2024implementationoffluorescentproteinbased pages 12-13)
- Reactive oxygen species (CHEBI class) (claessen2019cellwalldeficiency pages 2-5)
- Glycine betaine, sucrose, NaCl, EDTA (CHEBI entries) as osmolytes/chelators used in induction/propagation media (purkayastha2024isolation&characterization pages 102-106)

**ENVO (environment)**
- Osmoprotective/high-osmolarity medium (ENVO class for culture medium / high osmolarity condition; evidence supports necessity for wall-free growth) (errington2017cellwalldeficientlform pages 1-2)
- Urine (ENVO class for urine / urinary tract environment) (errington2016lformbacteriachronic pages 3-4)

**NCBITaxon (organisms)**
- *Bacillus subtilis* (NCBITaxon) (errington2017cellwalldeficientlform pages 1-2, tian2024implementationoffluorescentproteinbased media 868f7058)
- *Escherichia coli* (NCBITaxon) (errington2017cellwalldeficientlform pages 1-2, errington2016lformbacteriachronic pages 3-4)
- *Staphylococcus aureus* (NCBITaxon) (purkayastha2024isolation&characterization pages 97-102)
- *Haloferax volcanii* (NCBITaxon) (brown2024archaealtubulinlikeproteins pages 1-5)

**UniProt (proteins) / gene-centric identifiers**
- FtsZ; MreB; AccDA (acetyl-CoA carboxylase subunits); CetZ1/CetZ2 (tubulin-like GTPases): recommend grounding to UniProt accessions **per taxon** at curation time, because sequences and accessions are organism-specific even when names are conserved (brown2024archaealtubulinlikeproteins pages 1-5, errington2016lformbacteriachronic pages 2-3).

### 8) Relevant statistics and quantitative data (from evidence)
- L-forms detected in urine from **29/30** older patients with recurrent UTI (errington2016lformbacteriachronic pages 3-4).
- L-forms isolated from **11/57** patients with chronic bacteriuria or pyelonephritis (errington2016lformbacteriachronic pages 3-4).
- Archaeal cytoskeletal abundance ratio shift: **CetZ1:CetZ2 ~41:1 (mid-log) to ~5:1 (stationary)** (brown2024archaealtubulinlikeproteins pages 5-7).
- Experimental induction (taxon-specific, dissertation evidence): *S. aureus* L-forms induced with penicillin G at **300 µg/mL** (HG001) or **2000 µg/mL** (JE2); approximate cell sizes reported (WT HG001 ~0.85 µm; WT JE2 ~0.50 µm; L-forms ~0.75 µm; large vesicles ~1 µm) (purkayastha2024isolation&characterization pages 97-102, purkayastha2024isolation&characterization pages 157-160).

### 9) Warnings / curation cautions
1. **Preprint evidence (archaea):** CetZ1/CetZ2 mechanisms are from a 2024 bioRxiv preprint and should be curated with a “preprint/awaiting peer review” flag (brown2024archaealtubulinlikeproteins pages 1-5).
2. **Dissertation/grey literature:** Multiple *S. aureus* L-form induction details (drug concentrations, sizes, colony morphology) come from a 2024 dissertation-like document with unclear journal status; treat as **supporting but weak** unless confirmed in peer-reviewed primary sources (purkayastha2024isolation&characterization pages 97-102, purkayastha2024isolation&characterization pages 157-160).
3. **Mechanism vs marker:** Observations like lysostaphin resistance or reduced vancomycin staining support **cell wall alteration** but do not by themselves establish upstream causality for pleomorphism; curate them as phenotype markers unless paired with mechanistic interventions (purkayastha2024isolation&characterization pages 160-165).
4. **Trait generality:** Some mechanisms are universal at the conceptual level (wall loss → shape irregularity), but specific genetic routes (e.g., AccDA overproduction) can be taxon- and experimental-context-dependent (errington2016lformbacteriachronic pages 2-3).

---

## DOI-first bibliography (with dates/URLs)
- Tian D, et al. **Implementation of Fluorescent-Protein-Based Quantification Analysis in L-Form Bacteria.** *Bioengineering* (Jan 2024). DOI: **10.3390/bioengineering11010081**. https://doi.org/10.3390/bioengineering11010081 (tian2024implementationoffluorescentproteinbased pages 1-2)
- Brown HJ, Duggin IG. **Archaeal tubulin-like proteins CetZ1 and CetZ2 have opposing effects on cell morphology during the growth cycle of Haloferax volcanii.** *bioRxiv* (Dec 2024). DOI: **10.1101/2024.10.29.620987**. https://doi.org/10.1101/2024.10.29.620987 (brown2024archaealtubulinlikeproteins pages 1-5)
- Justice I, et al. **A tuneable minimal cell membrane reveals that two lipid species suffice for life.** *Nature Communications* (Nov 2024). DOI: **10.1038/s41467-024-53975-y**. https://doi.org/10.1038/s41467-024-53975-y (justice2024atuneableminimala pages 14-15)
- Errington J, Mickiewicz KM, Kawai Y, Wu LJ. **L-form bacteria, chronic diseases and the origins of life.** *Phil. Trans. R. Soc. B* (Nov 2016). DOI: **10.1098/rstb.2015.0494**. https://doi.org/10.1098/rstb.2015.0494 (errington2016lformbacteriachronic pages 1-2)
- Errington J. **Cell wall-deficient, L-form bacteria in the 21st century: a personal perspective.** *Biochemical Society Transactions* (Apr 2017). DOI: **10.1042/bst20160435**. https://doi.org/10.1042/bst20160435 (errington2017cellwalldeficientlform pages 1-2)
- Claessen D, Errington J. **Cell wall deficiency as a coping strategy for stress.** *Trends in Microbiology* (Dec 2019). DOI: **10.1016/j.tim.2019.07.008**. https://doi.org/10.1016/j.tim.2019.07.008 (claessen2019cellwalldeficiency pages 1-2)
- Mickiewicz KM, et al. **Possible role of L-form switching in recurrent urinary tract infection.** *Nature Communications* (Sep 2019). DOI: **10.1038/s41467-019-12359-3**. https://doi.org/10.1038/s41467-019-12359-3 (errington2016lformbacteriachronic pages 3-4)
- Kawai Y, Mickiewicz K, Errington J. **Lysozyme Counteracts β-Lactam Antibiotics by Promoting the Emergence of L-Form Bacteria.** *Cell* (Feb 2018). DOI: **10.1016/j.cell.2018.01.021**. https://doi.org/10.1016/j.cell.2018.01.021 (tian2024implementationoffluorescentproteinbased pages 12-13)


References

1. (errington2017cellwalldeficientlform pages 1-2): Jeff Errington. Cell wall-deficient, l-form bacteria in the 21st century: a personal perspective. Biochemical Society Transactions, 45:287-295, Apr 2017. URL: https://doi.org/10.1042/bst20160435, doi:10.1042/bst20160435. This article has 75 citations and is from a peer-reviewed journal.

2. (errington2016lformbacteriachronic pages 1-2): Jeff Errington, Katarzyna Mickiewicz, Yoshikazu Kawai, and Ling Juan Wu. L-form bacteria, chronic diseases and the origins of life. Philosophical Transactions of the Royal Society B: Biological Sciences, 371:20150494, Nov 2016. URL: https://doi.org/10.1098/rstb.2015.0494, doi:10.1098/rstb.2015.0494. This article has 169 citations and is from a domain leading peer-reviewed journal.

3. (claessen2019cellwalldeficiency pages 2-5): Dennis Claessen and Jeff Errington. Cell wall deficiency as a coping strategy for stress. Trends in microbiology, 27:1025-1033, Dec 2019. URL: https://doi.org/10.1016/j.tim.2019.07.008, doi:10.1016/j.tim.2019.07.008. This article has 101 citations and is from a domain leading peer-reviewed journal.

4. (tian2024implementationoffluorescentproteinbased pages 1-2): Di Tian, Yiyuan Liu, Yueyue Zhang, Yunfei Liu, Yang Xia, Boying Xu, Jian Xu, and Tetsuya Yomo. Implementation of fluorescent-protein-based quantification analysis in l-form bacteria. Bioengineering, 11:81, Jan 2024. URL: https://doi.org/10.3390/bioengineering11010081, doi:10.3390/bioengineering11010081. This article has 2 citations.

5. (errington2016lformbacteriachronic pages 2-3): Jeff Errington, Katarzyna Mickiewicz, Yoshikazu Kawai, and Ling Juan Wu. L-form bacteria, chronic diseases and the origins of life. Philosophical Transactions of the Royal Society B: Biological Sciences, 371:20150494, Nov 2016. URL: https://doi.org/10.1098/rstb.2015.0494, doi:10.1098/rstb.2015.0494. This article has 169 citations and is from a domain leading peer-reviewed journal.

6. (claessen2019cellwalldeficiency pages 1-2): Dennis Claessen and Jeff Errington. Cell wall deficiency as a coping strategy for stress. Trends in microbiology, 27:1025-1033, Dec 2019. URL: https://doi.org/10.1016/j.tim.2019.07.008, doi:10.1016/j.tim.2019.07.008. This article has 101 citations and is from a domain leading peer-reviewed journal.

7. (tian2024implementationoffluorescentproteinbased media 868f7058): Di Tian, Yiyuan Liu, Yueyue Zhang, Yunfei Liu, Yang Xia, Boying Xu, Jian Xu, and Tetsuya Yomo. Implementation of fluorescent-protein-based quantification analysis in l-form bacteria. Bioengineering, 11:81, Jan 2024. URL: https://doi.org/10.3390/bioengineering11010081, doi:10.3390/bioengineering11010081. This article has 2 citations.

8. (tian2024implementationoffluorescentproteinbased media ce88008d): Di Tian, Yiyuan Liu, Yueyue Zhang, Yunfei Liu, Yang Xia, Boying Xu, Jian Xu, and Tetsuya Yomo. Implementation of fluorescent-protein-based quantification analysis in l-form bacteria. Bioengineering, 11:81, Jan 2024. URL: https://doi.org/10.3390/bioengineering11010081, doi:10.3390/bioengineering11010081. This article has 2 citations.

9. (brown2024archaealtubulinlikeproteins pages 1-5): Hannah J. Brown and Iain G. Duggin. Archaeal tubulin-like proteins cetz1 and cetz2 have opposing effects on cell morphology during the growth cycle of haloferax volcanii. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.10.29.620987, doi:10.1101/2024.10.29.620987. This article has 1 citations.

10. (brown2024archaealtubulinlikeproteins pages 5-7): Hannah J. Brown and Iain G. Duggin. Archaeal tubulin-like proteins cetz1 and cetz2 have opposing effects on cell morphology during the growth cycle of haloferax volcanii. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.10.29.620987, doi:10.1101/2024.10.29.620987. This article has 1 citations.

11. (justice2024atuneableminimala pages 14-15): Isaac Justice, Petra Kiesel, Nataliya Safronova, Alexander von Appen, and James P. Saenz. A tuneable minimal cell membrane reveals that two lipid species suffice for life. Nature Communications, Nov 2024. URL: https://doi.org/10.1038/s41467-024-53975-y, doi:10.1038/s41467-024-53975-y. This article has 33 citations and is from a highest quality peer-reviewed journal.

12. (errington2016lformbacteriachronic pages 3-4): Jeff Errington, Katarzyna Mickiewicz, Yoshikazu Kawai, and Ling Juan Wu. L-form bacteria, chronic diseases and the origins of life. Philosophical Transactions of the Royal Society B: Biological Sciences, 371:20150494, Nov 2016. URL: https://doi.org/10.1098/rstb.2015.0494, doi:10.1098/rstb.2015.0494. This article has 169 citations and is from a domain leading peer-reviewed journal.

13. (errington2017cellwalldeficientlform pages 7-8): Jeff Errington. Cell wall-deficient, l-form bacteria in the 21st century: a personal perspective. Biochemical Society Transactions, 45:287-295, Apr 2017. URL: https://doi.org/10.1042/bst20160435, doi:10.1042/bst20160435. This article has 75 citations and is from a peer-reviewed journal.

14. (errington2017cellwalldeficientlform pages 8-9): Jeff Errington. Cell wall-deficient, l-form bacteria in the 21st century: a personal perspective. Biochemical Society Transactions, 45:287-295, Apr 2017. URL: https://doi.org/10.1042/bst20160435, doi:10.1042/bst20160435. This article has 75 citations and is from a peer-reviewed journal.

15. (tian2024implementationoffluorescentproteinbased pages 12-13): Di Tian, Yiyuan Liu, Yueyue Zhang, Yunfei Liu, Yang Xia, Boying Xu, Jian Xu, and Tetsuya Yomo. Implementation of fluorescent-protein-based quantification analysis in l-form bacteria. Bioengineering, 11:81, Jan 2024. URL: https://doi.org/10.3390/bioengineering11010081, doi:10.3390/bioengineering11010081. This article has 2 citations.

16. (purkayastha2024isolation&characterization pages 102-106): M Purkayastha. Isolation & characterization of trace amines (tas) producing human skin commensals and isolation and characterization of l-forms in staphylococcus aureus …. Unknown journal, 2024.

17. (claessenUnknownyearerrington.(2019) pages 7-8): D Claessen. Errington,.(2019). Unknown journal, Unknown year.

18. (purkayastha2024isolation&characterization pages 97-102): M Purkayastha. Isolation & characterization of trace amines (tas) producing human skin commensals and isolation and characterization of l-forms in staphylococcus aureus …. Unknown journal, 2024.

19. (purkayastha2024isolation&characterization pages 157-160): M Purkayastha. Isolation & characterization of trace amines (tas) producing human skin commensals and isolation and characterization of l-forms in staphylococcus aureus …. Unknown journal, 2024.

20. (purkayastha2024isolation&characterization pages 160-165): M Purkayastha. Isolation & characterization of trace amines (tas) producing human skin commensals and isolation and characterization of l-forms in staphylococcus aureus …. Unknown journal, 2024.

21. (brown2024archaealtubulinlikeproteins pages 7-9): Hannah J. Brown and Iain G. Duggin. Archaeal tubulin-like proteins cetz1 and cetz2 have opposing effects on cell morphology during the growth cycle of haloferax volcanii. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.10.29.620987, doi:10.1101/2024.10.29.620987. This article has 1 citations.