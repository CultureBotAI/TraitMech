---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T08:20:07.195353'
end_time: '2026-06-18T08:38:37.015686'
duration_seconds: 1109.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: irregular shaped
  trait_identifier: METPO:1000691
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: irregular_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape lacking a consistent geometric form across individual cells
    of a population.
  parent_traits: METPO:1000666
  synonyms: irregular
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control
    as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x:
    coryneform morphology (Corynebacterineae review supports irregular and coryneform
    morphologies associated with apical polar growth and reduced lateral wall patterning.)'
  causal_graph_summary: 'irregular_shaped_loss_of_patterning: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** irregular shaped
- **METPO identifier:** METPO:1000691
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape lacking a consistent geometric form across individual cells of a population.
- **Parent traits:** METPO:1000666
- **Synonyms:** irregular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x: coryneform morphology (Corynebacterineae review supports irregular and coryneform morphologies associated with apical polar growth and reduced lateral wall patterning.)
- **Existing causal graph summary:** irregular_shaped_loss_of_patterning: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **irregular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/irregular_shaped.yaml`.

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
- **Trait label:** irregular shaped
- **METPO identifier:** METPO:1000691
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape lacking a consistent geometric form across individual cells of a population.
- **Parent traits:** METPO:1000666
- **Synonyms:** irregular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports loss of cytoskeletal/wall-patterning control as the basis for irregular morphology.) | DOI:10.1111/j.1574-6976.2011.00298.x: coryneform morphology (Corynebacterineae review supports irregular and coryneform morphologies associated with apical polar growth and reduced lateral wall patterning.)
- **Existing causal graph summary:** irregular_shaped_loss_of_patterning: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **irregular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/irregular_shaped.yaml`.

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


## Research report: Microbial trait “irregular shaped” (METPO:1000691)

### Scope summary (TraitMech curation)
The METPO trait **irregular shaped** (METPO:1000691) represents a **population-level morphology phenotype** in which single cells **lack a consistent geometric form across individuals** (heterogeneous, misshapen, bulged, amoeboid, or otherwise non-uniform). Mechanistically, current evidence supports irregular morphology as a common endpoint of **loss of spatial control over envelope growth**, including (i) disruption of cytoskeletal guidance of peptidoglycan (PG) insertion (e.g., MreB/RodZ), (ii) imbalance/miscoordination between PG synthases and hydrolases, (iii) defects in polar-growth scaffolds and membrane organization in actinobacteria under stress, and (iv) wall-deficient/L-form states where the canonical wall-based shape constraint is absent and cell division systems can partially re-impose regularity (kale2024mechanicsofe. pages 1-4, zhang2023coordinatedpeptidoglycansynthases pages 2-3, claessen2024thestomatinlikeprotein pages 1-5, hayashi2024septalwallsynthesis pages 1-2).

**Boundary cases / distinctions.** The trait should be distinguished from:
- **Stable alternate shapes** (e.g., coccus, spiral, filament) when a consistent geometry is maintained across the population; some perturbations yield spheres uniformly (loss of rod shape) rather than heterogeneous irregularity (zhang2023coordinatedpeptidoglycansynthases pages 2-3, ojima2024buddingandexplosive pages 1-2).
- **Transient division intermediates** (e.g., constricting septa) that do not imply persistent heterogeneity.
- **Taxon-specific developmental morphologies** (e.g., controlled hyphal branching) unless explicitly described as bulging/irregular branching due to perturbed control (claessen2024thestomatinlikeprotein pages 1-5).

### Key concepts and current mechanistic understanding
1. **Envelope growth patterning as a shape-control system.** Multiple recent studies converge on the idea that regular shape requires **regulated spatial patterning** of wall synthesis and remodeling; loss of this patterning produces heterogeneous morphologies (bulges, dents, irregular branches) (kale2024mechanicsofe. pages 1-4, zhang2023coordinatedpeptidoglycansynthases pages 2-3, claessen2024thestomatinlikeprotein pages 1-5).
2. **Cytoskeletal guidance of PG insertion.** In rod-shaped bacteria, the actin-like cytoskeleton **MreB** is described as sensing curvature and directing localized cell-wall insertion; inhibiting MreB polymerization (A22) causes loss of rod shape and aberrant morphologies (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13).
3. **PG synthase–hydrolase coordination.** PG expansion requires coordinated openings (hydrolases) and insertion (synthases). Disruption of this coordination can collapse rod shape (e.g., moenomycin inhibition of aPBPs activates/mislocalizes DacB-mediated hydrolysis leading to rod-to-sphere conversion) (zhang2023coordinatedpeptidoglycansynthases pages 2-3, zhang2023coordinatedpeptidoglycansynthases pages 6-7).
4. **Actinobacterial polar growth and membrane microdomains.** Filamentous actinobacteria rely on polar-growth scaffolds (DivIVA/Scy/FilP) and, under hyperosmotic stress, **StlP-organized membrane microdomains** that maintain spatially confined tip wall synthesis; perturbations yield hyphal bulging, irregular branching, and extrusion of cell wall–deficient cells (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 27-28).
5. **Wall-less/L-form states as intrinsically heterogeneous.** Wall-less **E. coli L-forms** exhibit heterogeneous “ameba-like” morphology; however, **septal wall synthesis and/or FtsZ-dependent division** can convert amoeboid populations toward more uniform oval shapes, contingent on division-site positioning systems (Min or nucleoid occlusion) (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 2-3).

### Recent developments (prioritizing 2023–2024)
#### (A) Rod-shape determinants and irregular surface phenotypes in *E. coli* (2024)
A 2024 study of a hypervesiculating **ΔrodZ** mutant connected loss of rod-shape determinants to both **shape change** and **microstructural envelope defects**. ΔrodZ cells were spherical and a subset had aberrant surface structures (budding vesicles, dented surfaces, curved patterns) that together constituted ~7% of cells (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive pages 4-5). The same work reports **holes in the PG layer** and increased cell volume in ΔrodZ and an mreB-repressed strain, and links osmotic support (sucrose) to reduced vesicle production, consistent with envelope fragility when wall structure is incomplete (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive pages 7-10). Figure evidence for aberrant surface structures and vesicle quantification is available in the cropped figure retrieval (ojima2024buddingandexplosive media 7c48602b, ojima2024buddingandexplosive media 1a468366).

**Key quantitative statistics:**
- ΔrodZ produced **>50×** more vesicles than WT; mreB-repressed cells produced **~8×** more than WT (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive media 7c48602b).
- Aberrant surface-structure frequencies in ΔrodZ: **3.7% budding**, **2.2% dented**, **1% curved-pattern**, total ~**7%** (ojima2024buddingandexplosive pages 4-5, ojima2024buddingandexplosive media 7c48602b).

#### (B) Mechanics of bulging and heterogeneous shapes from cytoskeleton + septation perturbations (2024)
A 2024 preprint quantified heterogeneous morphologies (“rugby,” multi-bulge cells) in **A22 (MreB inhibitor)** and **cephalexin (PBP3/FtsI inhibitor)** treated *E. coli*, linking these shape changes to reduced envelope mechanical parameters and proposing threshold behavior separating regulated from deregulated width control (kale2024mechanicsofe. pages 10-13). This supports a causal path from perturbations of patterning and septal wall synthesis to irregular/bulged shapes.

#### (C) PG synthase–hydrolase coordination as a mechanism for rod collapse (2023)
A 2023 *Nature Communications* study in **Myxococcus xanthus** found that **moenomycin inhibition** of class A PBP glycosyltransferase activity caused rapid collapse of rod shape (after 2 h, **72.7% spherical**, and prolonged treatment drove conversion without mass lysis) (zhang2023coordinatedpeptidoglycansynthases pages 2-3). Mechanistically, moenomycin-inhibited PBP1a2 promoted **DacB binding to PG** and increased DacB-mediated hydrolysis, with DacB overexpression accelerating rod-to-sphere transition (zhang2023coordinatedpeptidoglycansynthases pages 4-5, zhang2023coordinatedpeptidoglycansynthases pages 6-7). This provides a generalizable “loss of coordination” module for irregular-shape curation.

#### (D) Hydrolase/carboxypeptidase balance and irregular morphologies (2024)
A 2024 *PLOS Genetics* study in **Vibrio cholerae** identified a mechanistic chain linking **DacA1 (PBP5) insufficiency** to altered PG remodeling: pentapeptide accumulation “hinders ShyA’s ability to cleave crosslinks,” thereby disrupting the synthesis/degradation balance and producing aberrant shapes (including increased width) (obando2024geneticinteractionmapping pages 15-17). This supports edges where defective PG maturation indirectly drives irregular morphology via impaired endopeptidase function.

#### (E) Polar-growth scaffolds and membrane microdomains under hyperosmotic stress (2024)
A 2024 Research Square preprint proposes that **StlP** organizes tip-localized membrane microdomains with increased fluidity; loss of StlP yields branching, aberrant wall synthesis, wall thinning, and extrusion of cell wall–deficient cells at hyphal tips under hyperosmotic stress (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 27-28). The same source cites that partial depletion of **DivIVA** causes “hyphal bulging and irregular branching,” consistent with a polarity-scaffold failure mode for irregular morphologies (claessen2024thestomatinlikeprotein pages 1-5).

#### (F) Wall-less L-forms: heterogeneity and re-regularization via division/Septal synthesis (2024)
A 2024 *Communications Biology* paper directly states that wall-less *E. coli* L-forms have “heterogeneous” and “ameboid” morphologies, and that they “can be converted to a mostly uniform oval shape solely by FtsZ-dependent division” even without cylindrical wall synthesis (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 2-3). It further links uniformity to division-site positioning: FtsZ-dependent shape control requires at least one of Min or nucleoid occlusion systems, and “cells lacking a cylindrical cell wall cannot maintain a uniform cell size without both the Min system and nucleoid occlusion” (hayashi2024septalwallsynthesis pages 7-8, hayashi2024septalwallsynthesis pages 1-2).

### Current applications and real-world implementations
1. **Antibiotic mechanism and envelope-failure phenotyping.** Shape collapse (rod-to-sphere conversion) and bulging are used as **phenotypic readouts** of antibiotic action on PG synthesis (e.g., moenomycin inhibiting aPBPs; cephalexin inhibiting PBP3/FtsI), supporting real-world implementation in antimicrobial studies and screening pipelines (zhang2023coordinatedpeptidoglycansynthases pages 2-3, kale2024mechanicsofe. pages 10-13).
2. **Outer membrane vesicle (OMV) hyperproduction as an engineering/bioprocess phenotype.** The ΔrodZ study shows dramatic OMV hypervesiculation tied to envelope defects and osmotic sensitivity, illustrating how engineered or selected morphological perturbations can affect OMV yields and cell integrity; this is relevant to biotechnology where vesicles are used for vaccine platforms or delivery systems (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive media 7c48602b).
3. **Stress resilience in filamentous actinobacteria.** StlP-mediated membrane microdomains are proposed as an adaptation supporting polar growth under hyperosmotic stress, suggesting potential targets for engineering stress tolerance or controlling morphogenesis in industrial actinomycetes (claessen2024thestomatinlikeprotein pages 27-28).
4. **L-form biology and division engineering.** Demonstration that septal wall synthesis/FtsZ positioning can regularize L-form morphology provides a mechanistic handle for experiments using wall-deficient states (e.g., synthetic biology, antibiotic tolerance studies), where controlling heterogeneity can improve reproducibility (hayashi2024septalwallsynthesis pages 1-2).

### Expert opinions / authoritative synthesis within the retrieved sources
- The 2023 *Nature Communications* work explicitly frames rod collapse as arising from **disrupted coordination** between synthases and hydrolases, proposing that “disrupting the coordination between PG synthases and hydrolases could be more lethal than eliminating individual enzymes” (concept summarized in the evidence extraction) (zhang2023coordinatedpeptidoglycansynthases pages 1-2).
- The 2024 eLife study on bactofilins emphasizes that beyond canonical elongation/division machineries, bacteria employ accessory cytoskeletal modules (bactofilin + M23 hydrolase) to locally modulate PG biosynthesis, providing a conceptual generalization that **local PG remodeling modules can drive morphogenesis and, if perturbed, produce morphological defects** (pohl2024adynamicbactofilin pages 1-2).

### Candidate nodes for TraitMech curation
The following artifact provides a curation-oriented node inventory (grouped by type with suggested grounding where available):

| Node group | Candidate node | Suggested grounding | Evidence support |
|---|---|---|---|
| Phenotype/trait nodes | irregular shaped | METPO:1000691 | Heterogeneous/aberrant morphologies arise when envelope patterning is disrupted; examples include “multiple shapes,” “budding vesicles and dented surfaces,” and “ameba-like” cells (kale2024mechanicsofe. pages 10-13, ojima2024buddingandexplosive pages 4-5, hayashi2024septalwallsynthesis pages 1-2) |
| Phenotype/trait nodes | loss of rod shape | label-only | A22-induced MreB inhibition causes “loss of rod-shape”; moenomycin treatment caused 72.7% of cells to become spherical (kale2024mechanicsofe. pages 10-13, zhang2023coordinatedpeptidoglycansynthases pages 2-3) |
| Phenotype/trait nodes | spherical cell morphology | label-only | “ΔrodZ cells were spherical (WT cells are rod-shaped)” and moenomycin-treated cells “became spherical” (ojima2024buddingandexplosive pages 1-2, zhang2023coordinatedpeptidoglycansynthases pages 2-3) |
| Phenotype/trait nodes | bulging morphology | label-only | Co-perturbation of MreB and septation produced “central symmetric bulges” and “multiple shapes” (kale2024mechanicsofe. pages 20-24, kale2024mechanicsofe. pages 10-13) |
| Phenotype/trait nodes | amoeboid / heterogeneous L-form morphology | label-only | “wall-less E. coli L-form cells… have a heterogeneous cell morphology” and “the L-form is ameboid” (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 2-3) |
| Phenotype/trait nodes | irregular branching / hyphal bulging | label-only | “Partial depletion of DivIVA causes hyphal bulging and irregular branching” (claessen2024thestomatinlikeprotein pages 1-5) |
| Phenotype/trait nodes | cell wall-deficient (CWD) extrusion | label-only | Loss of StlP causes “extrusion of cell wall-deficient cells at hyphal tips” under hyperosmotic stress (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 27-28) |
| Cellular structures | peptidoglycan cell wall | GO:0009273 | Cell shape is set by PG; holes in the PG layer were observed in ΔrodZ and mreB-repressed cells (pohl2024adynamicbactofilin pages 1-2, ojima2024buddingandexplosive pages 1-2) |
| Cellular structures | septal cell wall | label-only | “the formation of the septal cell wall only, without the side wall, is sufficient to confer uniform cell shape” (hayashi2024septalwallsynthesis pages 2-3) |
| Cellular structures | lateral/side wall | label-only | ΔmreB1 showed a “profound decrease in side wall labelling,” linking lateral wall growth to shape maintenance (zambri2024bacteriacombinepolar pages 13-18) |
| Cellular structures | cell poles / hyphal tips | GO:0046658 | DacB-mediated degradation is enriched at poles; DivIVA and StlP act at growing hyphal tips (zhang2023coordinatedpeptidoglycansynthases pages 3-4, claessen2024thestomatinlikeprotein pages 1-5) |
| Cellular structures | membrane microdomain | label-only | StlP “organizes membrane microdomains” that “locally fluidize the membrane” for coordinated wall synthesis (claessen2024thestomatinlikeprotein pages 27-28) |
| Cellular structures | Z ring | GO:0097527 | Uniform ovalization of L-forms depends on “FtsZ-dependent division” and Z-ring positioning by Min/nucleoid occlusion (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 7-8) |
| Cellular structures | outer membrane vesicle | GO:0097428 | ΔrodZ cells displayed budding vesicles and hypervesiculation linked to incomplete PG structure (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive pages 4-5) |
| Biological processes (GO labels) | peptidoglycan biosynthetic process | GO:0009252 | Perturbing PG synthesis via PBP3, aPBPs, or polar-growth machinery leads to irregular shapes (kale2024mechanicsofe. pages 10-13, zhang2023coordinatedpeptidoglycansynthases pages 2-3, claessen2024thestomatinlikeprotein pages 1-5) |
| Biological processes (GO labels) | peptidoglycan catabolic process | GO:0009253 | Moenomycin “promotes PG hydrolysis by DacB,” driving rod-to-sphere transition (zhang2023coordinatedpeptidoglycansynthases pages 2-3, zhang2023coordinatedpeptidoglycansynthases pages 4-5) |
| Biological processes (GO labels) | cell wall organization or biogenesis | GO:0071555 | StlP loss causes “aberrant cell wall synthesis” and “cell wall thinning” (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 27-28) |
| Biological processes (GO labels) | cell shape determination | GO:0008360 | MreB, RodZ, DivIVA, and associated modules are repeatedly linked to shape maintenance and morphogenesis (kale2024mechanicsofe. pages 1-4, ojima2024buddingandexplosive pages 1-2, sen2024adispensablesepiva pages 1-2) |
| Biological processes (GO labels) | cytokinesis / cell division | GO:0000910 | PBP3 inhibition causes filamentation; FtsZ-dependent division can restore uniform oval shape in L-forms (kale2024mechanicsofe. pages 10-13, hayashi2024septalwallsynthesis pages 1-2) |
| Biological processes (GO labels) | establishment of cell polarity / polar growth | GO:0030010 | DivIVA, Scy, FilP, SepIVA, and StlP are linked to apical/polar growth organization (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 17-20, sen2024adispensablesepiva pages 1-2) |
| Biological processes (GO labels) | response to osmotic stress | GO:0006970 | Hyperosmotic stress reveals StlP-dependent protection against CWD extrusion and irregular growth (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 27-28) |
| Genes/proteins/complexes | MreB | UniProt/label-only by taxon | “MreB filaments both sense curvature and direct localized cell-wall insertion”; inhibition causes rounding/loss of rod shape (kale2024mechanicsofe. pages 1-4) |
| Genes/proteins/complexes | RodZ | label-only | RodZ is required for proper MreB/PG synthase organization; deletion yields spherical, hypervesiculating cells (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive pages 4-5) |
| Genes/proteins/complexes | FtsI / PBP3 | label-only | Cephalexin inhibits FtsI/PBP3 and causes filamentation; PBP3 activation helps regularize SWD/L-form cells (kale2024mechanicsofe. pages 10-13, hayashi2024septalwallsynthesis pages 7-8) |
| Genes/proteins/complexes | class A PBPs / aPBPs | label-only | Moenomycin inhibition of aPBPs collapses rod shape despite their individual dispensability for rod morphology (zhang2023coordinatedpeptidoglycansynthases pages 2-3, zhang2023coordinatedpeptidoglycansynthases pages 1-2) |
| Genes/proteins/complexes | PBP1a2 | label-only | “moenomycin-inhibited PBP1a2 promotes PG-binding by DacB” and associated morphological defects (zhang2023coordinatedpeptidoglycansynthases pages 5-6, zhang2023coordinatedpeptidoglycansynthases pages 6-7) |
| Genes/proteins/complexes | DacB | label-only | DacB overexpression “significantly accelerated the rod-to-sphere transition” (zhang2023coordinatedpeptidoglycansynthases pages 4-5) |
| Genes/proteins/complexes | DacA1 / PBP5 | label-only | DacA1 insufficiency yields “aberrant shapes” and increased width by disturbing PG synthesis/degradation balance (obando2024geneticinteractionmapping pages 15-17) |
| Genes/proteins/complexes | ShyA endopeptidase | label-only | Pentapeptide accumulation “hinders ShyA’s ability to cleave crosslinks,” impairing wall remodeling (obando2024geneticinteractionmapping pages 15-17) |
| Genes/proteins/complexes | DivIVA / Wag31 | label-only | Essential polarity determinant; partial depletion causes “hyphal bulging and irregular branching” (claessen2024thestomatinlikeprotein pages 1-5, sen2024adispensablesepiva pages 1-2) |
| Genes/proteins/complexes | Scy | label-only | Scy is “a key component of a multiprotein assembly controlling polarized growth” (claessen2024thestomatinlikeprotein pages 17-20) |
| Genes/proteins/complexes | FilP | label-only | FilP assemblies “affect polar growth determinant DivIVA” and are linked to extreme morphological transitions (claessen2024thestomatinlikeprotein pages 17-20, claessen2024thestomatinlikeprotein pages 15-17) |
| Genes/proteins/complexes | StlP | label-only | StlP “organizes membrane microdomains” required for normal tip growth under hyperosmotic stress (claessen2024thestomatinlikeprotein pages 27-28) |
| Genes/proteins/complexes | SepIVA | label-only | SepIVA is “associated with polar growth rather than septum formation” in S. venezuelae; mycobacterial mutants can show perturbed morphology (sen2024adispensablesepiva pages 1-2) |
| Genes/proteins/complexes | MinC / Min system | label-only | Required, with nucleoid occlusion, for uniform cell size/shape in wall-less states (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 6-7) |
| Genes/proteins/complexes | SlmA / nucleoid occlusion system | label-only | At least one of Min or nucleoid occlusion is required for FtsZ-dependent regularization of L-forms (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 7-8) |
| Genes/proteins/complexes | FtsZ | UniProt/label-only by taxon | L-forms “can be converted to a mostly uniform oval shape solely by FtsZ-dependent division” (hayashi2024septalwallsynthesis pages 1-2) |
| Chemicals/inhibitors | A22 | label-only | “A22-induced MreB inhibition results in loss of rod-shape” and bulging/aberrant shapes (kale2024mechanicsofe. pages 10-13, kale2024mechanicsofe. pages 1-4) |
| Chemicals/inhibitors | cephalexin | CHEBI:3495 | Inhibits septum assembly via FtsI/PBP3, causing filamentation and, with A22, bulging (kale2024mechanicsofe. pages 10-13) |
| Chemicals/inhibitors | moenomycin | CHEBI:6888 | “Moenomycin specifically inhibits aPBP GTase activity” and drives rod collapse/sphericity (zhang2023coordinatedpeptidoglycansynthases pages 2-3) |
| Chemicals/inhibitors | fosfomycin | CHEBI:28915 | Used to induce wall-deficient/L-form states that are amoeboid/heterogeneous (hayashi2024septalwallsynthesis pages 2-3) |
| Chemicals/inhibitors | aztreonam / Azt | CHEBI:29007 | Removal of Fos and Azt allowed cells to deform into oval shape and divide FtsZ-dependently (hayashi2024septalwallsynthesis pages 7-8) |
| Chemicals/inhibitors | sucrose | CHEBI:17992 | Osmotic support reduced vesicle production and rescued ΔrodZ growth defects, consistent with osmotic fragility (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive pages 7-10) |
| Environmental/experimental factors | hyperosmotic stress | label-only | Under hyperosmotic conditions, loss of StlP weakens the wall and causes CWD extrusion (claessen2024thestomatinlikeprotein pages 27-28) |
| Environmental/experimental factors | osmotic support | label-only | “In conditions of osmotic support using sucrose… vesicle production decreased drastically” in ΔrodZ (ojima2024buddingandexplosive pages 1-2) |
| Environmental/experimental factors | wall-less / L-form induction | label-only | L-forms are generated by inhibiting wall synthesis and show amoeboid morphology (hayashi2024septalwallsynthesis pages 2-3, hayashi2024septalwallsynthesis pages 1-2) |
| Environmental/experimental factors | co-treatment A22 + cephalexin | label-only | Produces rugby, scaled-bacilli, two-bulge, and three-bulge morphologies (kale2024mechanicsofe. pages 20-24) |
| Environmental/experimental factors | mreB repression (CRISPRi) | label-only | Reduced mreB expression to 20% of WT and caused a rodZ-like abnormal morphology (ojima2024buddingandexplosive pages 1-2) |
| Assays/observations | fluorescent D-amino acid side-wall labeling | label-only | ΔmreB1 showed “profound decrease in side wall labelling,” supporting loss of lateral wall patterning (zambri2024bacteriacombinepolar pages 13-18) |
| Assays/observations | quick-freeze replica electron microscopy (QFDE-EM) | label-only | Revealed spherical ΔrodZ cells, budding vesicles, dented surfaces, and curved patterns (ojima2024buddingandexplosive pages 5-7, ojima2024buddingandexplosive pages 4-5) |
| Assays/observations | peptidoglycan imaging / isolated PG analysis | label-only | ΔrodZ PG was “circular with many holes”; holes also seen in mreB-repressed cells (ojima2024buddingandexplosive pages 5-7, ojima2024buddingandexplosive pages 7-10) |
| Assays/observations | Laurdan membrane fluidity measurements | label-only | Used to show StlP-dependent membrane microdomains at tips (claessen2024thestomatinlikeprotein pages 27-28) |
| Assays/observations | cryo-electron tomography / wall-thickness measurement | label-only | Used to support “cell wall thinning” and altered tip-wall organization in stlP mutants (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 15-17) |
| Assays/observations | morphology frequency / OMV quantification | label-only | ΔrodZ produced >50× OMVs; aberrant surface structures accounted for ~7% of cells (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive media 7c48602b) |
| Assays/observations | FtsZ/Z-ring fluorescence microscopy | label-only | Showed mesh-like or mislocalized FtsZ structures in L-forms and uniform-oval restoration with FtsZ-dependent division (hayashi2024septalwallsynthesis pages 6-7, hayashi2024septalwallsynthesis pages 1-2) |


*Table: This table lists curation-ready candidate nodes for an 'irregular shaped' causal graph, grouped by biological type and grounded where possible. It highlights the main structures, processes, genes, perturbagens, and observational readouts supported by the retrieved evidence.*

### Evidence-backed candidate causal edges (triples)
The following artifact compiles candidate causal edges with DOI-first references, dates, and direct supporting snippets suitable for translation into `irregular_shaped.yaml`:

| Subject | Predicate | Object | Mechanism summary | Strength / uncertainty | Primary citation | Publication date | Direct quote / snippet |
|---|---|---|---|---|---|---|---|
| A22 (MreB inhibitor; CHEBI candidate) | inhibits | MreB polymerization / MreB function | In *E. coli*, chemical inhibition of the actin-like cytoskeleton disrupts lateral wall patterning and width control, producing loss of rod shape, ellipsoidal cells, and bulging when envelope mechanics fail. | Strong for *E. coli*; chemical-perturbation evidence, not universal across taxa. | Kale et al., bioRxiv, DOI: 10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11 | “A22-induced MreB inhibition results in loss of rod-shape” and cells “undergo bulging and show multiple shapes.” (kale2024mechanicsofe. pages 10-13, kale2024mechanicsofe. pages 1-4) |
| MreB inhibition / depletion | causes | irregular shaped phenotype | Loss of MreB-mediated curvature sensing and localized PG insertion removes rod-shape maintenance, yielding rounding and heterogeneous morphologies. | Strong in model bacteria; some taxon variation. | Kale et al., bioRxiv, DOI: 10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11 | “MreB filaments both sense curvature and direct localized cell-wall insertion… inhibition of MreB polymerization (A22) alters width and causes rounding/loss of rod shape.” (kale2024mechanicsofe. pages 1-4) |
| cephalexin (CHEBI candidate) | inhibits | FtsI / PBP3-dependent septal peptidoglycan synthesis | Septal transpeptidase inhibition blocks division-associated wall synthesis, causing filamentation; together with MreB inhibition it promotes central bulging and heterogeneous shapes. | Strong for *E. coli*; antibiotic-specific. | Kale et al., bioRxiv, DOI: 10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11 | “cephalexin inhibits septum assembly via FtsI and causes filamentation; co-treatment with A22 and cephalexin produces diverse, non-lytic aberrant shapes and bulging.” (kale2024mechanicsofe. pages 10-13) |
| Co-treatment: A22 + cephalexin | causes | central bulges / heterogeneous aberrant morphologies | Simultaneous disruption of cytoskeletal patterning and septal wall synthesis weakens local envelope rigidity, generating rugby-shaped, two-bulge, and three-bulge cells. | Strong but assay-specific; preprint. | Kale et al., bioRxiv, DOI: 10.1101/2024.11.22.624946, https://doi.org/10.1101/2024.11.22.624946 | 2024-11 | Combined treatment produced “central symmetric bulges,” with morphologies classified as “Rugby, Scaled-bacilli, Two bulge, Three bulge.” (kale2024mechanicsofe. pages 20-24, kale2024mechanicsofe. pages 1-4) |
| rodZ deletion | causes | spherical cells with aberrant surface structures | RodZ is needed for proper MreB/PG elongation complex organization; deletion causes spherical morphology, incomplete PG structure, budding vesicles, dents, and osmotically sensitive envelopes. | Strong for *E. coli*; genotype-specific. | Ojima et al., Front. Microbiol., DOI: 10.3389/fmicb.2024.1400434, https://doi.org/10.3389/fmicb.2024.1400434 | 2024-06 | “ΔrodZ cells were spherical (WT cells are rod-shaped)” and “around 7%” had “budding vesicles and dented surfaces, or curved patterns.” (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive pages 4-5) |
| rodZ deletion | increases | outer membrane vesicle production | Envelope/PG defects from rod-shape loss promote budding and explosive vesiculation, a readout of incomplete PG structure and osmotic fragility. | Strong for this strain/assay. | Ojima et al., Front. Microbiol., DOI: 10.3389/fmicb.2024.1400434, https://doi.org/10.3389/fmicb.2024.1400434 | 2024-06 | “the ΔrodZ strain produced >50 times more vesicles than the WT” and under imaging “approximately 7% of the total cells” showed aberrant structures. (ojima2024buddingandexplosive pages 1-2, ojima2024buddingandexplosive media 7c48602b) |
| rodZ deletion | leads to | holes in peptidoglycan layer | PG discontinuities support a mechanism in which rod-shape determinants preserve envelope integrity; their loss yields local wall failure and irregular surfaces. | Strong in this study; structural interpretation specific to assay. | Ojima et al., Front. Microbiol., DOI: 10.3389/fmicb.2024.1400434, https://doi.org/10.3389/fmicb.2024.1400434 | 2024-06 | “holes in the PG layer and an increased cell volume were observed for ΔrodZ and mreBR3 cells compared with the WT.” (ojima2024buddingandexplosive pages 1-2) |
| mreB repression | causes | enlarged spherical / aberrant cells | Genetic reduction of MreB phenocopies rodZ loss, supporting the RodZ–MreB axis as a shape-maintenance module. | Strong for *E. coli* CRISPRi system. | Ojima et al., Front. Microbiol., DOI: 10.3389/fmicb.2024.1400434, https://doi.org/10.3389/fmicb.2024.1400434 | 2024-06 | “repression of mreB expression led to a similar phenotype to deletion of rodZ” and the strain showed “eightfold higher vesicle production than the WT.” (ojima2024buddingandexplosive pages 4-5, ojima2024buddingandexplosive pages 1-2) |
| moenomycin (CHEBI candidate) | inhibits | class A PBPs / aPBP glycosyltransferase activity | Inhibition of aPBPs perturbs synthase–hydrolase coordination, collapsing rod shape even where aPBPs are individually non-essential for rod morphology. | Strong for *Myxococcus xanthus*; not direct evidence for all taxa. | Zhang et al., Nat. Commun., DOI: 10.1038/s41467-023-41082-3, https://doi.org/10.1038/s41467-023-41082-3 | 2023-09 | “Moenomycin specifically inhibits aPBP GTase activity” and after 2 h “72.7% of cells became spherical.” (zhang2023coordinatedpeptidoglycansynthases pages 2-3) |
| moenomycin-inhibited PBP1a2 | promotes | DacB binding to peptidoglycan | Drug-bound synthase dysregulates the hydrolase, increasing pole-localized PG degradation and destabilizing shape. | Strong in *M. xanthus*; mechanistically specific. | Zhang et al., Nat. Commun., DOI: 10.1038/s41467-023-41082-3, https://doi.org/10.1038/s41467-023-41082-3 | 2023-09 | “moenomycin promotes PG hydrolysis by DacB” and “promotes PG-binding by DacB.” (zhang2023coordinatedpeptidoglycansynthases pages 2-3, zhang2023coordinatedpeptidoglycansynthases pages 4-5) |
| DacB overactivity / DacB-mediated polar PG hydrolysis | accelerates | rod-to-sphere transition / shape collapse | Excess hydrolase activity at poles causes localized PG loss and sudden rod-shape failure, illustrating a general loss-of-patterning mechanism. | Strong in *M. xanthus*; hydrolase-specific. | Zhang et al., Nat. Commun., DOI: 10.1038/s41467-023-41082-3, https://doi.org/10.1038/s41467-023-41082-3 | 2023-09 | DacB overexpression “significantly accelerated the rod-to-sphere transition,” and activation of hydrolases causes “sudden loss of rod shape.” (zhang2023coordinatedpeptidoglycansynthases pages 4-5, zhang2023coordinatedpeptidoglycansynthases pages 6-7) |
| DacA1 / PBP5 insufficiency | hinders | ShyA endopeptidase crosslink cleavage | Loss of carboxypeptidase activity causes pentapeptide accumulation, reducing EP-mediated opening of PG for insertion and disrupting the synthesis/degradation balance. | Strong for *Vibrio cholerae*; taxon-specific. | Obando et al., PLoS Genet., DOI: 10.1371/journal.pgen.1011234, https://doi.org/10.1371/journal.pgen.1011234 | 2024-04 | Pentapeptide accumulation “hinders ShyA’s ability to cleave crosslinks,” thereby “disrupt[ing] the balance between PG synthesis and degradation.” (obando2024geneticinteractionmapping pages 15-17) |
| DacA1 / PBP5 insufficiency | causes | aberrant / irregular morphology including increased width | Impaired carboxypeptidase–endopeptidase coordination reduces local PG insertion during elongation, producing widened and irregular cells. | Strong for *V. cholerae*; likely transferable only cautiously. | Obando et al., PLoS Genet., DOI: 10.1371/journal.pgen.1011234, https://doi.org/10.1371/journal.pgen.1011234 | 2024-04 | Reduced EP cleavage can produce “aberrant shapes that are typically associated with lack of carboxypeptidases,” including “increased cell width.” (obando2024geneticinteractionmapping pages 15-17) |
| DivIVA partial depletion | causes | hyphal bulging and irregular branching | In filamentous actinobacteria, DivIVA scaffolds polar wall synthesis; reduced function disrupts focused tip growth, producing irregular branched/bulged morphology. | Strong from cited actinobacterial work; partly review-like in this source. | Claessen et al., Research Square preprint, DOI: 10.21203/rs.3.rs-3811693/v1, https://doi.org/10.21203/rs.3.rs-3811693/v1 | 2024-01 | “Partial depletion of DivIVA causes hyphal bulging and irregular branching.” (claessen2024thestomatinlikeprotein pages 1-5) |
| Scy / FilP / DivIVA polar growth complex perturbation | disrupts | polarized growth organization | These apical determinants stabilize the tip-organizing center; perturbation is associated with abnormal branching and mispatterned wall synthesis. | Moderate; mechanism assembled from actinobacterial evidence, not one direct perturbation here. | Claessen et al., Research Square preprint, DOI: 10.21203/rs.3.rs-3811693/v1, https://doi.org/10.21203/rs.3.rs-3811693/v1 | 2024-01 | Scy is “a key component of a multiprotein assembly controlling polarized growth,” and FilP assemblies “affect polar growth determinant DivIVA.” (claessen2024thestomatinlikeprotein pages 17-20, claessen2024thestomatinlikeprotein pages 15-17) |
| StlP | organizes | membrane microdomains with increased fluidity at hyphal tips | StlP creates a fluidized membrane platform that spatially confines apical cell wall synthesis during polar growth, especially under osmotic stress. | Strong in filamentous actinobacteria; preprint. | Claessen et al., Research Square preprint, DOI: 10.21203/rs.3.rs-3811693/v1, https://doi.org/10.21203/rs.3.rs-3811693/v1 | 2024-01 | “StlP oligomerizes on the membrane to form microdomains that locally fluidize the membrane and act as platforms for coordinated cell wall synthesis.” (claessen2024thestomatinlikeprotein pages 27-28) |
| loss of StlP | causes | branching, aberrant wall synthesis, wall thinning, and CWD-cell extrusion | Without the membrane microdomain, apical synthesis becomes diffuse and the weakened wall yields irregular branching and extrusion of cell wall-deficient cells under hyperosmotic stress. | Strong in this system; stress- and taxon-specific. | Claessen et al., Research Square preprint, DOI: 10.21203/rs.3.rs-3811693/v1, https://doi.org/10.21203/rs.3.rs-3811693/v1 | 2024-01 | “Loss of StlP leads to branching, aberrant cell wall synthesis, cell wall thinning, and extrusion of cell wall-deficient cells at hyphal tips.” (claessen2024thestomatinlikeprotein pages 1-5) |
| hyperosmotic stress | promotes | cell wall-deficient extrusion when polar growth control is weak | Environmental stress amplifies irregular-shape phenotypes by challenging tip-wall integrity; StlP-dependent microdomains are protective. | Strong in this actinobacterial model; environmental-context specific. | Claessen et al., Research Square preprint, DOI: 10.21203/rs.3.rs-3811693/v1, https://doi.org/10.21203/rs.3.rs-3811693/v1 | 2024-01 | Under hyperosmotic conditions, loss of StlP “weakens the cell wall and results in extrusion of cells with deficient walls.” (claessen2024thestomatinlikeprotein pages 27-28) |
| wall-less / L-form state | associated with | heterogeneous amoeba-like morphology | Absence of a cylindrical wall removes canonical shape constraints, yielding irregular, amoeboid, multinucleoid cells. | Strong in *E. coli* L-forms. | Hayashi et al., Commun. Biol., DOI: 10.1038/s42003-024-07279-y, https://doi.org/10.1038/s42003-024-07279-y | 2024-11 | “wall-less E. coli L-form cells… have a heterogeneous cell morphology” and “the L-form is ameboid.” (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 2-3) |
| FtsZ-dependent division | converts | amoeba-like L-forms into mostly uniform oval cells | Even without cylindrical wall synthesis, septation can impose more regular morphology if FtsZ is positioned properly. | Strong in *E. coli* L-forms; specific experimental condition. | Hayashi et al., Commun. Biol., DOI: 10.1038/s42003-024-07279-y, https://doi.org/10.1038/s42003-024-07279-y | 2024-11 | L-forms “can be converted to a mostly uniform oval shape solely by FtsZ-dependent division.” (hayashi2024septalwallsynthesis pages 1-2) |
| Min system or nucleoid occlusion | required for | uniform cell shape in wall-less / septal-wall-deficient cells | Spatial regulators position FtsZ in wall-deficient states; without them, Z-rings are mislocalized and cells remain amoeboid/irregular. | Strong in *E. coli* L-form/SWD experiments. | Hayashi et al., Commun. Biol., DOI: 10.1038/s42003-024-07279-y, https://doi.org/10.1038/s42003-024-07279-y | 2024-11 | “this FtsZ-dependent control… requires at least either the Min or nucleoid occlusion systems” and “cells lacking a cylindrical cell wall cannot maintain a uniform cell size without both the Min system and nucleoid occlusion.” (hayashi2024septalwallsynthesis pages 1-2, hayashi2024septalwallsynthesis pages 7-8) |
| septal wall synthesis / PBP3 activation | restores | uniform oval shape from amoeboid wall-deficient cells | Re-establishing septal PG synthesis is sufficient to regularize morphology even in the absence of sidewall synthesis. | Strong in *E. coli* SWD/L-form system. | Hayashi et al., Commun. Biol., DOI: 10.1038/s42003-024-07279-y, https://doi.org/10.1038/s42003-024-07279-y | 2024-11 | “the formation of the septal cell wall only, without the side wall, is sufficient to confer uniform cell shape” and WT SWD cells “are divided into uniform oval cells using Z-ring by the activation of PBP3.” (hayashi2024septalwallsynthesis pages 2-3, hayashi2024septalwallsynthesis pages 7-8) |


*Table: This table lists candidate causal edges for the microbial trait ‘irregular shaped’ (METPO:1000691), linking perturbations in cytoskeletal patterning, peptidoglycan synthesis/remodeling, polar growth control, osmotic stress, and wall-deficient states to irregular morphology. It is useful as a curation-ready starting point for TraitMech edge selection, with citations, dates, and supporting snippets.*

### Visual evidence (figures)
Cropped figures from the ΔrodZ *E. coli* study show representative **aberrant surface structures** and **quantified OMV production** differences between WT, ΔrodZ, and mreB-repressed strains (ojima2024buddingandexplosive media 7c48602b, ojima2024buddingandexplosive media 1a468366). These visuals are useful for curators as direct phenotype documentation supporting edges linking RodZ/MreB perturbation to irregular surfaces and envelope instability.

### DOI-first bibliography (with dates and URLs)

> DOI: [10.1038/s42003-024-07279-y](https://doi.org/10.1038/s42003-024-07279-y) — Hayashi M, Takaoka C, Higashi K, Kurokawa K, Margolin W, Oshima T, Shiomi D. *Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in Escherichia coli L-forms*. **Communications Biology**. November 2024. (hayashi2024septalwallsynthesis pages 7-8, hayashi2024septalwallsynthesis pages 1-2)
>
> DOI: [10.3389/fmicb.2024.1400434](https://doi.org/10.3389/fmicb.2024.1400434) — Ojima Y, Toda K, Sawabe T, Kumazoe Y, Tahara YO, Miyata M, Azuma M. *Budding and explosive membrane vesicle production by hypervesiculating Escherichia coli strain ΔrodZ*. **Frontiers in Microbiology**. June 2024. (ojima2024buddingandexplosive pages 5-7, ojima2024buddingandexplosive pages 1-2)
>
> DOI: [10.1038/s41467-023-41082-3](https://doi.org/10.1038/s41467-023-41082-3) — Zhang H, Venkatesan S, Ng E, Nan B. *Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall*. **Nature Communications**. September 2023. (zhang2023coordinatedpeptidoglycansynthases pages 2-3, zhang2023coordinatedpeptidoglycansynthases pages 1-2)
>
> DOI: [10.1371/journal.pgen.1011234](https://doi.org/10.1371/journal.pgen.1011234) — Obando MA, Rey-Varela D, Cava F, Dörr T. *Genetic interaction mapping reveals functional relationships between peptidoglycan endopeptidases and carboxypeptidases*. **PLOS Genetics**. April 2024. (obando2024geneticinteractionmapping pages 15-17)
>
> DOI: [10.21203/rs.3.rs-3811693/v1](https://doi.org/10.21203/rs.3.rs-3811693/v1) — Claessen D, Zhong X, Baur S, Ongenae V, Egido GG, Shitut S, Du C, Vijgenboom E, van Wezel G, Brava VC, Briegel A, Bramkamp M. *The stomatin-like protein StlP organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress*. **Research Square preprint**. January 2024. (claessen2024thestomatinlikeprotein pages 1-5, claessen2024thestomatinlikeprotein pages 27-28)
>
> DOI: [10.1101/2024.11.22.624946](https://doi.org/10.1101/2024.11.22.624946) — Kale T, Dasgupta R, Inamdar MM, Athale CA. *Mechanics of E. coli cell width homeostasis and bulging dynamics from MreB and septum inhibition*. **bioRxiv preprint**. November 2024. (kale2024mechanicsofe. pages 1-4, kale2024mechanicsofe. pages 10-13)
>
> DOI: [10.1101/2024.07.30.605496](https://doi.org/10.1101/2024.07.30.605496) — Zambri MP, Baglio CR, Irazoki O, Jones SE, Garner EC, Cava F, Elliot MA. *Bacteria combine polar- and dispersed-growth to power cell elongation and wall width dynamics*. **bioRxiv preprint**. July 2024. (zambri2024bacteriacombinepolar pages 13-18)
>
> DOI: [10.1186/s12866-024-03625-6](https://doi.org/10.1186/s12866-024-03625-6) — Sen BC, Mavi PS, Irazoki O, Datta S, Kaiser S, Cava F, Flärdh K. *A dispensable SepIVA orthologue in Streptomyces venezuelae is associated with polar growth and not cell division*. **BMC Microbiology**. November 2024. (sen2024adispensablesepiva pages 1-2)
>
> DOI: [10.7554/elife.86577.2](https://doi.org/10.7554/elife.86577.2) — Pöhl S, Osorio-Valeriano M, Cserti E, Harberding J, Hernández-Tamayo R, Biboy J, Sobetzko P, Vollmer W, Graumann PL, Thanbichler M. *A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis*. **eLife**. January 2024. (pohl2024adynamicbactofilin pages 1-2)


*Blockquote: This blockquote lists the principal 2023–2024 sources used to support the irregular-shaped microbial trait causal graph. It provides DOI-first citations with venues and dates for rapid curation and reference checking.*

### Warnings / claims not ready for curation
1. **User-provided older DOIs appear mismatched to the trait context.** DOI:10.1146/annurev-cellbio-101011-155745 retrieved here is an inflammasome review (not bacterial cell shape), so it should not be curated as evidence for microbial irregular morphology without correction to the intended citation (kale2024mechanicsofe. pages 20-24).
2. **Protein identifiers are taxon-specific.** UniProt IDs should be assigned per species/strain during curation; this report leaves many proteins as label-only to avoid inventing identifiers.
3. **Preprint evidence should be flagged.** Kale 2024 (bioRxiv), Claessen 2024 (Research Square), and Zambri 2024 (bioRxiv) are preprints; edges relying primarily on these should be marked **uncertain** until peer-reviewed versions are available (kale2024mechanicsofe. pages 10-13, claessen2024thestomatinlikeprotein pages 1-5, zambri2024bacteriacombinepolar pages 13-18).
4. **Sphericity vs. irregularity.** Some perturbations yield largely uniform spheres (rod-to-sphere conversion) rather than heterogeneous irregularity; curation should decide whether “spherical” is a separate trait endpoint or a subcase contributing to “irregular shaped,” depending on METPO trait modeling conventions (zhang2023coordinatedpeptidoglycansynthases pages 2-3).


References

1. (kale2024mechanicsofe. pages 1-4): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

2. (zhang2023coordinatedpeptidoglycansynthases pages 2-3): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

3. (claessen2024thestomatinlikeprotein pages 1-5): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

4. (hayashi2024septalwallsynthesis pages 1-2): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

5. (ojima2024buddingandexplosive pages 1-2): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 7 citations and is from a peer-reviewed journal.

6. (kale2024mechanicsofe. pages 10-13): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

7. (zhang2023coordinatedpeptidoglycansynthases pages 6-7): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

8. (claessen2024thestomatinlikeprotein pages 27-28): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

9. (hayashi2024septalwallsynthesis pages 2-3): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

10. (ojima2024buddingandexplosive pages 4-5): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 7 citations and is from a peer-reviewed journal.

11. (ojima2024buddingandexplosive pages 7-10): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 7 citations and is from a peer-reviewed journal.

12. (ojima2024buddingandexplosive media 7c48602b): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 7 citations and is from a peer-reviewed journal.

13. (ojima2024buddingandexplosive media 1a468366): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 7 citations and is from a peer-reviewed journal.

14. (zhang2023coordinatedpeptidoglycansynthases pages 4-5): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

15. (obando2024geneticinteractionmapping pages 15-17): Manuela Alvarado Obando, Diego Rey-Varela, Felipe Cava, and Tobias Dörr. Genetic interaction mapping reveals functional relationships between peptidoglycan endopeptidases and carboxypeptidases. PLOS Genetics, 20:e1011234, Apr 2024. URL: https://doi.org/10.1371/journal.pgen.1011234, doi:10.1371/journal.pgen.1011234. This article has 8 citations and is from a domain leading peer-reviewed journal.

16. (hayashi2024septalwallsynthesis pages 7-8): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

17. (zhang2023coordinatedpeptidoglycansynthases pages 1-2): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

18. (pohl2024adynamicbactofilin pages 1-2): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

19. (kale2024mechanicsofe. pages 20-24): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

20. (zambri2024bacteriacombinepolar pages 13-18): Matthew P. Zambri, Christine R. Baglio, Oihane Irazoki, Stephanie E. Jones, Ethan C. Garner, Felipe Cava, and Marie A. Elliot. Bacteria combine polar- and dispersed-growth to power cell elongation and wall width dynamics. bioRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.30.605496, doi:10.1101/2024.07.30.605496. This article has 2 citations.

21. (zhang2023coordinatedpeptidoglycansynthases pages 3-4): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

22. (sen2024adispensablesepiva pages 1-2): Beer Chakra Sen, Parminder Singh Mavi, Oihane Irazoki, Susmita Datta, Sebastian Kaiser, Felipe Cava, and Klas Flärdh. A dispensable sepiva orthologue in streptomyces venezuelae is associated with polar growth and not cell division. BMC Microbiology, Nov 2024. URL: https://doi.org/10.1186/s12866-024-03625-6, doi:10.1186/s12866-024-03625-6. This article has 6 citations and is from a peer-reviewed journal.

23. (claessen2024thestomatinlikeprotein pages 17-20): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

24. (zhang2023coordinatedpeptidoglycansynthases pages 5-6): Huan Zhang, Srutha Venkatesan, Emily Ng, and Beiyan Nan. Coordinated peptidoglycan synthases and hydrolases stabilize the bacterial cell wall. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41082-3, doi:10.1038/s41467-023-41082-3. This article has 29 citations and is from a highest quality peer-reviewed journal.

25. (claessen2024thestomatinlikeprotein pages 15-17): Dennis Claessen, Xiaobo Zhong, Sarah Baur, Veronique Ongenae, Guillermo Guerrero Egido, Shraddha Shitut, Chao Du, Erik Vijgenboom, Gilles van Wezel, Victor Carrion Brava, Ariane Briegel, and Marc Bramkamp. The stomatin-like protein stlp organizes membrane microdomains to govern polar growth in filamentous actinobacteria under hyperosmotic stress. Unknown journal, Jan 2024. URL: https://doi.org/10.21203/rs.3.rs-3811693/v1, doi:10.21203/rs.3.rs-3811693/v1.

26. (hayashi2024septalwallsynthesis pages 6-7): Masafumi Hayashi, Chigusa Takaoka, Koichi Higashi, Ken Kurokawa, William Margolin, Taku Oshima, and Daisuke Shiomi. Septal wall synthesis is sufficient to change ameba-like cells into uniform oval-shaped cells in escherichia coli l-forms. Communications Biology, Nov 2024. URL: https://doi.org/10.1038/s42003-024-07279-y, doi:10.1038/s42003-024-07279-y. This article has 2 citations and is from a peer-reviewed journal.

27. (ojima2024buddingandexplosive pages 5-7): Yoshihiro Ojima, Kaho Toda, Tomomi Sawabe, Yuki Kumazoe, Yuhei O. Tahara, Makoto Miyata, and Masayuki Azuma. Budding and explosive membrane vesicle production by hypervesiculating escherichia coli strain δrodz. Frontiers in Microbiology, Jun 2024. URL: https://doi.org/10.3389/fmicb.2024.1400434, doi:10.3389/fmicb.2024.1400434. This article has 7 citations and is from a peer-reviewed journal.