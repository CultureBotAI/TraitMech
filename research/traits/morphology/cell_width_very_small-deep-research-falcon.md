---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:09:33.800139'
end_time: '2026-06-18T07:25:27.586678'
duration_seconds: 953.79
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: cell width very small
  trait_identifier: METPO:1000887
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: cell_width_very_small
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell-width phenotype in which the shorter cell dimension is at most
    approximately 0.5 micrometers.
  parent_traits: METPO:1000882
  synonyms: W_<=0.5
  evidence_summary: 'DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining
    review links very narrow cell widths to oligotrophic and streamlined lineages.)'
  causal_graph_summary: 'cell_width_very_small_streamlining: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** cell width very small
- **METPO identifier:** METPO:1000887
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension is at most approximately 0.5 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_<=0.5
- **Existing evidence:** DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining review links very narrow cell widths to oligotrophic and streamlined lineages.)
- **Existing causal graph summary:** cell_width_very_small_streamlining: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width very small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_very_small.yaml`.

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
- **Trait label:** cell width very small
- **METPO identifier:** METPO:1000887
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell-width phenotype in which the shorter cell dimension is at most approximately 0.5 micrometers.
- **Parent traits:** METPO:1000882
- **Synonyms:** W_<=0.5
- **Existing evidence:** DOI:10.1038/ismej.2014.60: small cells and genomes (Streamlining review links very narrow cell widths to oligotrophic and streamlined lineages.)
- **Existing causal graph summary:** cell_width_very_small_streamlining: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **cell width very small** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/cell_width_very_small.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **cell width very small** (METPO:1000887)

### Scope summary (TraitMech curation intent)
**Trait definition (given):** a morphology-class phenotype in which the shorter cell dimension (“cell width”) is **≤ ~0.5 µm**.

**What the trait represents.** In curation terms, this trait should capture organisms whose characteristic cell diameter/width is in the submicron regime, at or below ~0.5 µm, regardless of cell length or overall volume.

**Boundary cases / nearby traits to distinguish.**
1. **Ultramicrobacteria (UMB) is a stricter concept than METPO:1000887.** A recent synthesis cites classical UMB criteria: **“diameter of proliferating cells less than 0.3 µm, cell volume less than 0.1 µm³”** (plus a genome-size range) (belykh2024ultramicrobacteriaandfilterable pages 1-2). Thus, UMB ⊂ “very small width (≤0.5 µm)”.
2. **Filterability / femtoplankton is an assay-defined fraction, not a synonym of width ≤0.5 µm.** “Femtoplankton” is operationally defined as **bacteria passing through 0.2 µm filters** (belykh2024ultramicrobacteriaandfilterable pages 1-2), and the same review notes that **pleomorphic bacteria with genomes >3.2 Mb can still pass into the <0.2 µm fraction** due to “cell wall structure and morphology” (belykh2024ultramicrobacteriaandfilterable pages 2-3). Therefore, filtration-based membership should be modeled as an *experimental/collection* node (assay), not a direct assertion of very small width.
3. **Near-threshold empirical example (supports plausibility of ≤0.5 µm widths in planktonic lineages).** In Lake Baikal’s ultrafine actinobacterial discussion, a candidate genus isolate is described with **“C-shaped cells of 0.4–0.5 µm in diameter”** (belykh2024ultramicrobacteriaandfilterable pages 3-5), which lies at the METPO cutoff but is not necessarily representative of all femtoplankton.

### Key concepts & current understanding
#### 1) Ecological “small-cell/streamlining/oligotrophy” syndrome
- **Streamlining theory** explicitly links natural selection in nutrient-poor environments with small cells and genomes: it “attributes small cells and genomes” to streamlining/oligotrophic selection (giovannoni2014implicationsofstreamlining pages 3-4) and frames streamlining as selection favoring minimization of cell size/complexity in nutrient-poor environments (giovannoni2014implicationsofstreamlining pages 1-2).
- A freshwater-focused review on ultramicrobacteria emphasizes a functional advantage: **“Thanks to their high surface-to-volume ratio, small-cell bacteria absorb nutrients most efficiently”**, especially under **“oligotrophic water bodies with low organic matter concentrations”** (belykh2024ultramicrobacteriaandfilterable pages 1-2).
- A 2023 Microbiology and Molecular Biology Reviews article defines oligotrophs as **“microbial cells that are adapted to thrive under low-nutrient concentrations in oceans, lakes, and other aquatic ecosystems”** and notes oligotrophs “use less transcriptional regulation” (noell2023areductionof pages 1-2), framing a broader suite of streamlining-aligned traits.

#### 2) Mechanistic control of cell width in rod-shaped bacteria (model systems)
For TraitMech, these mechanistic entities can act as **candidate mechanistic modules** (even if the organismal trait of ≤0.5 µm width is not directly engineered/assayed in these papers).

- In *Bacillus subtilis*, Juillot et al. summarize a prevailing mechanism: **diameter results from a balance between two peptidoglycan (PG) insertion systems**: (i) the **Rod complex** (organized circumferential insertion) and (ii) **class A PBPs (aPBPs)** (more isotropic/unoriented insertion) (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4).
  - Their mechanistic statements are explicit: **aPBP-mediated isotropic insertion “enlarges the cell cylinder”** while **Rod complex-mediated circumferential insertion “reduces it”** (juillot2021ahighcontentmicroscopy pages 2-4).
  - Genetic directionality is also described: “thinner… cells in the absence of aPBPs” and “reduced activity of the Rod complex… increased cell diameter” (juillot2021ahighcontentmicroscopy pages 2-4).
- In *E. coli*, a 2024 preprint frames width control as coupled to cytoskeletal and envelope mechanics:
  - “MreB cytoskeletal filaments act to sense and mechanically determine the cell curvature and therefore width” (kale2024mechanicsofe. pages 1-4).
  - Width can be perturbed by chemical inhibitors: **A22** (MreB polymerization inhibitor) and **cephalexin** (PBP3 inhibitor) (kale2024mechanicsofe. pages 1-4).

### Recent developments & latest research emphasis (2023–2024 prioritized)
- **2024 (Lake Baikal femtoplankton study):** provides operational thresholds and quantitative statistics for the ultrafine fraction, enabling assay/trait separation during curation.
  - Femtoplankton are defined as bacteria “passing through filters with a **0.2 µm** pore size” (belykh2024ultramicrobacteriaandfilterable pages 1-2).
  - Quantitative abundance: femtoplankton fraction **7×10^4 cells/mL** (0–50 m layer) and **4.4%** average contribution to total bacterial number (belykh2024ultramicrobacteriaandfilterable pages 1-2).
  - Additional quantitative context: total bacterioplankton abundance (TBA) in the pelagic zone “0.5 to 2.5×10^6 cells/mL” (belykh2024ultramicrobacteriaandfilterable pages 2-3).
  - Provides a near-threshold morphology example: “0.4–0.5 µm in diameter” (belykh2024ultramicrobacteriaandfilterable pages 3-5).
- **2023 (oligotroph regulation review):** ties oligotroph life history to reduced genome size and altered regulatory strategies (noell2023areductionof pages 1-2).
- **2024 (E. coli width mechanics preprint):** proposes envelope bending rigidity as a primary mechanical parameter for width dynamics and provides mechanical-pressure estimates (e.g., untreated growing cells turgor ≈0.15 MPa; growth pressure ≈0.4 MPa), while focusing on perturbations via A22/cephalexin (kale2024mechanicsofe. pages 1-4). (Preprint; curate as uncertain.)

### Current applications & real-world implementations
1. **Environmental fractionation and microbial community ecology:** Operational collection/quantification of ultra-small microbes via filtration (0.2 µm cutoff and smaller capture filters) is a standard approach and is explicitly positioned as relevant to ecology and monitoring (belykh2024ultramicrobacteriaandfilterable pages 1-2, belykh2024ultramicrobacteriaandfilterable pages 2-3).
2. **Water treatment/sterilization considerations:** The Baikal review notes that passage through 0.45 and 0.2 µm filters “is also important to take into account during sterilization of solutions and water treatment” (belykh2024ultramicrobacteriaandfilterable pages 2-3). This is an applied implication of ultra-small/filterable forms.
3. **Antibiotic mechanism/phenotyping:** Width/shape perturbation by β-lactams (e.g., cephalexin) and cytoskeletal inhibitors (A22) is used to probe cell-envelope mechanics and width homeostasis (kale2024mechanicsofe. pages 1-4). This supports applications in antibiotic mode-of-action studies and microfluidic/mechanical phenotyping contexts (within the constraints of the evidence).

### Expert opinions & authoritative synthesis statements
- **Streamlining theory (highly cited):** defines streamlining as selection favoring minimization of resources required for replication, producing small cells/genomes in nutrient-poor environments (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3).
- **Width-control mechanistic synthesis (cell biology):** Juillot et al. explicitly frame width as a genomic/physiological parameter requiring monitoring and highlight the Rod vs aPBP balance model (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4).

### Relevant statistics and data points (recent studies)
- **Lake Baikal femtoplankton abundance:** 7×10^4 cells/mL (0–50 m layer); ~4.4% of total bacterial number (belykh2024ultramicrobacteriaandfilterable pages 1-2).
- **Pelagic total bacterioplankton abundance:** 0.5–2.5×10^6 cells/mL (belykh2024ultramicrobacteriaandfilterable pages 2-3).
- **Near-threshold cell diameter example:** 0.4–0.5 µm diameter for an ultrafine actinobacterial lineage in the discussion (belykh2024ultramicrobacteriaandfilterable pages 3-5).
- **B. subtilis width control tightness (measurement context):** width variability “below 2%” across replicates/conditions, with SD ~0.071–0.089 µm in their assay (juillot2021ahighcontentmicroscopy pages 2-4).

---

## Candidate nodes grouped by type (ontology grounding suggestions)

| Node type | Label | Suggested CURIE(s) | Short evidence note |
|---|---|---|---|
| **Phenotype/assay** |  |  |  |
| Phenotype/assay | cell width very small | METPO:1000887 | Target trait: shorter cell dimension at most ~0.5 µm; nearby literature includes ultrafine freshwater actinobacteria with “0.4–0.5 µm in diameter,” supporting relevance of this magnitude in planktonic lineages (belykh2024ultramicrobacteriaandfilterable pages 3-5). |
| Phenotype/assay | femtoplankton / filterable bacteria fraction | label-only | Defined operationally as “bacteria passing through filters with a 0.2 μm pore size,” useful assay/collection node but not equivalent to the morphology trait itself (belykh2024ultramicrobacteriaandfilterable pages 1-2). |
| Phenotype/assay | ultramicrobacteria (UMB) | label-only | Explicit classical definition: proliferating cell diameter “less than 0.3 µm,” volume “less than 0.1 µm3,” with small genomes; narrower than the METPO ≤0.5 µm class and therefore a useful boundary case (belykh2024ultramicrobacteriaandfilterable pages 1-2). |
| Phenotype/assay | <0.2 µm fraction | label-only | Lake Baikal study separates bacterioplankton into fractions “larger and smaller than 0.2 µm”; supports an operational node for assay context (belykh2024ultramicrobacteriaandfilterable pages 1-2, belykh2024ultramicrobacteriaandfilterable pages 2-3). |
| Phenotype/assay | cell diameter / cell width | PATO:0000921 candidate, label-only | Juillot et al. frame B. subtilis width/diameter as a tightly controlled parameter with variability below 2%, making width a suitable mechanistic phenotype node (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4). |
| **Environmental factors (ENVO)** |  |  |  |
| Environmental factors (ENVO) | oligotrophic aquatic environment | ENVO:00000223 candidate, label-only | Small-cell bacteria are described as advantageous “especially… in oligotrophic water bodies with low organic matter concentrations” because of efficient uptake and predator protection (belykh2024ultramicrobacteriaandfilterable pages 1-2). |
| Environmental factors (ENVO) | low nutrient concentration | label-only | Oligotrophs are defined as cells “adapted to thrive under low-nutrient concentrations in oceans, lakes, and other aquatic ecosystems” (noell2023areductionof pages 1-2). |
| Environmental factors (ENVO) | low organic matter concentration | label-only | The Baikal review explicitly ties the advantage of small cells to waters with “low organic matter concentrations” (belykh2024ultramicrobacteriaandfilterable pages 1-2). |
| Environmental factors (ENVO) | pelagic freshwater zone | ENVO:00000301 candidate, label-only | The deep-water/pelagic Baikal zone is enriched for ultra-small actinobacterial lineages and femtoplankton fractions, making pelagic freshwater a candidate habitat node (belykh2024ultramicrobacteriaandfilterable pages 3-5). |
| Environmental factors (ENVO) | nutrient-poor environment | label-only | Streamlining theory is described as advantageous in “nutrient-poor (oligotrophic) environments,” linking environment to small cells/genomes (giovannoni2014implicationsofstreamlining pages 1-2). |
| **Cellular processes (GO)** |  |  |  |
| Cellular processes (GO) | peptidoglycan biosynthetic process | GO:0009252 | Bacterial morphogenesis is described as depending on coordinated proteins assembling/degrading the peptidoglycan shell; width determinants heavily map to cell-wall homeostasis (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4). |
| Cellular processes (GO) | peptidoglycan hydrolysis / cell wall expansion | GO:0009253 candidate, label-only | Width-affecting genes include those involved in “PG hydrolysis (required to allow PG expansion),” indicating a process node relevant to width control (juillot2021ahighcontentmicroscopy pages 2-4). |
| Cellular processes (GO) | cell wall organization / cell morphogenesis | GO:0071555, GO:0000902 | The papers explicitly discuss rod-shape maintenance and width control as consequences of cell-wall morphogenesis and organization (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4). |
| Cellular processes (GO) | circumferential peptidoglycan insertion | label-only | The Rod complex “processively and directionally inserts glycan strands around the cell circumference,” a key mechanistic process for narrowing diameter (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4). |
| Cellular processes (GO) | isotropic peptidoglycan insertion | label-only | aPBP-mediated “isotropic insertion of unoriented strands” is proposed to enlarge the cylinder, so this is a useful opposing process node (juillot2021ahighcontentmicroscopy pages 2-4). |
| Cellular processes (GO) | cell division / septation | GO:0051301, GO:0000917 | Kale 2024 highlights FtsZ and PBP3/FtsI in septation and width-associated bulging phenotypes, linking division processes to shape homeostasis (kale2024mechanicsofe. pages 1-4). |
| Cellular processes (GO) | transcriptional regulation reduced in oligotrophs | GO:0006355 candidate, label-only | Noell 2023 reports that oligotrophs “use less transcriptional regulation” and may rely on lower-cost regulatory mechanisms; useful for streamlining context (noell2023areductionof pages 1-2). |
| **Molecular complexes/genes/proteins** |  |  |  |
| Molecular complexes/genes/proteins | Rod complex / elongasome sidewall module | label-only | Proposed to reduce diameter via organized circumferential PG insertion; central mechanistic node for thin-cell phenotypes (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4). |
| Molecular complexes/genes/proteins | class A penicillin-binding proteins (aPBPs) | label-only | aPBPs mediate localized, unoriented insertion and are proposed to enlarge the cell cylinder; loss can yield thinner cells (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4). |
| Molecular complexes/genes/proteins | RodA | UniProt label-only, EC label-only | RodA is listed as an essential Rod-complex transglycosylase and width-control determinant in B. subtilis (juillot2021ahighcontentmicroscopy pages 1-2). |
| Molecular complexes/genes/proteins | PBP2A / PbpH | label-only | Class B PBPs acting with RodA in the Rod complex; depletion/reduced activity is linked to increased diameter or spherical cells (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4). |
| Molecular complexes/genes/proteins | MreB | UniProt label-only | Actin-like MreB proteins orient circumferential motion of the Rod complex; Kale notes MreB determines curvature and therefore width (juillot2021ahighcontentmicroscopy pages 1-2, kale2024mechanicsofe. pages 1-4). |
| Molecular complexes/genes/proteins | Mbl | label-only | Essential MreB paralog in B. subtilis width-control circuitry; included with MreB/MreBH in Rod-complex-associated shape control (juillot2021ahighcontentmicroscopy pages 1-2). |
| Molecular complexes/genes/proteins | MreBH | label-only | Third B. subtilis MreB paralog, relevant under stress and low Mg2+, implicating it in conditional width homeostasis (juillot2021ahighcontentmicroscopy pages 1-2). |
| Molecular complexes/genes/proteins | MreC | label-only | Essential morphogenetic Rod-complex component and presumed regulator of complex activity (juillot2021ahighcontentmicroscopy pages 1-2). |
| Molecular complexes/genes/proteins | MreD | label-only | Essential morphogenetic Rod-complex component and presumed regulator of complex activity (juillot2021ahighcontentmicroscopy pages 1-2). |
| Molecular complexes/genes/proteins | RodZ | label-only | Rod-complex-associated width/shape determinant recovered in B. subtilis width-control literature; useful mechanistic node with medium-dependent effects (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 10-11). |
| Molecular complexes/genes/proteins | peptidoglycan hydrolases | label-only | Mg2+ is reported to reduce PG hydrolase activity; hydrolase modulation affects morphology and width assays (juillot2021ahighcontentmicroscopy pages 2-4). |
| Molecular complexes/genes/proteins | teichoic acid synthesis machinery | label-only | Juillot 2021 notes many width genes affect TA synthesis, making this a broader cell-envelope determinant node (juillot2021ahighcontentmicroscopy pages 2-4). |
| Molecular complexes/genes/proteins | FtsZ | UniProt label-only | Tubulin homolog forming the Z-ring; included because width perturbations intersect with septation/homeostasis mechanisms in E. coli (kale2024mechanicsofe. pages 1-4). |
| Molecular complexes/genes/proteins | PBP3 / FtsI | label-only | Septal transpeptidase targeted by cephalexin; perturbation produces bulging/width defects, useful as a shape-homeostasis node (kale2024mechanicsofe. pages 1-4). |
| Molecular complexes/genes/proteins | envelope bending rigidity | label-only | Kale 2024 identifies envelope bending rigidity as the main mechanical parameter governing width increase/saturation and bulge expansion (kale2024mechanicsofe. pages 1-4). |
| Molecular complexes/genes/proteins | turgor pressure | GO context label-only | Reported as a mechanical driver of bulging and part of width/homeostasis mechanics in E. coli (kale2024mechanicsofe. pages 1-4). |
| **Chemicals (CHEBI)** |  |  |  |
| Chemicals (CHEBI) | magnesium ion | CHEBI:18420 | Growth in millimolar MgSO4 reduces PG hydrolase activity and “slightly reduced the average width” of wild-type B. subtilis, making Mg2+ a useful experimental factor node (juillot2021ahighcontentmicroscopy pages 2-4). |
| Chemicals (CHEBI) | magnesium sulfate | CHEBI:32599 candidate | Used experimentally at 20 mM in the B. subtilis screen to suppress lysis/shape artifacts and modulate width-related phenotypes (juillot2021ahighcontentmicroscopy pages 2-4). |
| Chemicals (CHEBI) | A22 (MreB polymerization inhibitor) | label-only | Kale 2024 identifies A22 as an “inhibitor of MreB polymerization,” directly relevant to width-control perturbation (kale2024mechanicsofe. pages 1-4). |
| Chemicals (CHEBI) | cephalexin | CHEBI:3478 candidate | Used as a PBP3 inhibitor producing bulges and altered width dynamics in E. coli (kale2024mechanicsofe. pages 1-4). |
| Chemicals (CHEBI) | nutrients / dissolved organic matter | CHEBI:33287 candidate, label-only | Streamlining and small-cell ecology are repeatedly framed around competition for limiting nutrients and low concentrations of dissolved organics (belykh2024ultramicrobacteriaandfilterable pages 1-2, giovannoni2014implicationsofstreamlining pages 1-2). |
| **Ecological strategies** |  |  |  |
| Ecological strategies | streamlining | label-only | Giovannoni 2014 explicitly states that streamlining theory “attributes small cells and genomes” to selection for efficient resource use in oligotrophic systems (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3). |
| Ecological strategies | reduced genome size | label-only | Small/reduced genomes are highlighted in oligotrophs and ultramicrobacteria, including explicit UMB genome ranges and streamlined freshwater lineages (belykh2024ultramicrobacteriaandfilterable pages 1-2, belykh2024ultramicrobacteriaandfilterable pages 3-5, noell2023areductionof pages 1-2). |
| Ecological strategies | high surface-to-volume ratio | label-only | The Baikal review directly links high surface-to-volume ratio to efficient nutrient absorption by small cells (belykh2024ultramicrobacteriaandfilterable pages 1-2). |
| Ecological strategies | predator avoidance / reduced predation | label-only | Small cells are noted to be “better protected from predation by predators,” making this a plausible ecological consequence node (belykh2024ultramicrobacteriaandfilterable pages 1-2). |
| Ecological strategies | photoheterotrophy via actinorhodopsins | label-only | Ultra-small freshwater actinobacterial lineages in the femtoplankton are described as often containing actinorhodopsins and leading a photoheterotrophic lifestyle (belykh2024ultramicrobacteriaandfilterable pages 3-5). |
| Ecological strategies | obligate oligotrophy | label-only | Streamlining/oligotrophy literature frames successful small-genome taxa as obligately adapted to low nutrient concentrations (noell2023areductionof pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3). |
| Ecological strategies | filterability not equivalent to ultrasmall width | label-only | Pleomorphic bacteria with genomes “>3.2 Mb” can still enter the <0.2 µm fraction, so filtration should be modeled as an assay/context node rather than a synonym of the trait (belykh2024ultramicrobacteriaandfilterable pages 2-3). |


*Table: This table lists candidate nodes for a TraitMech graph for METPO:1000887, grouped by phenotype, environment, process, molecular components, chemicals, and ecological strategies. It is useful for curating grounded graph nodes while separating true morphology mechanisms from assay-defined or contextual nodes.*

---

## Candidate causal edges (evidence-backed triples)

| Subject node (CURIE if known) | Predicate | Object node (CURIE if known) | Evidence snippet | Source | DOI | URL | Publication date | Uncertainty/notes for curation |
|---|---|---|---|---|---|---|---|---|
| oligotrophic aquatic environment (ENVO:00000223 candidate) | selects_for | small cell size / very small width (label-only) | “streamlining… is especially advantageous in nutrient-poor (oligotrophic) environments… Cell size reduction offers selective advantages including… higher surface-to-volume ratios” (giovannoni2014implicationsofstreamlining pages 1-2) | Giovannoni 2014, *Implications of streamlining theory* | 10.1038/ismej.2014.60 | https://doi.org/10.1038/ismej.2014.60 | Apr 2014 | Broad ecological edge; supports association more than direct width threshold. Good high-level parent edge. |
| low nutrient concentration (label-only) | enables_fitness_of | oligotrophs with reduced transcriptional regulation (label-only) | “oligotrophs… are adapted to thrive under low-nutrient concentrations… [and] use less transcriptional regulation” (noell2023areductionof pages 1-2) | Noell 2023, *Reduction of transcriptional regulation* | 10.1128/mmbr.00124-22 | https://doi.org/10.1128/mmbr.00124-22 | Mar 2023 | Indirect streamlining edge; relevant for oligotrophic syndrome, not specific to width. Mark as contextual. |
| reduced genome size (label-only) | associated_with | oligotrophic microbial lineages (label-only) | “many microbial cell lineages in nature… share with oligotrophs the property of reduced genome size” (noell2023areductionof pages 1-2) | Noell 2023, *Reduction of transcriptional regulation* | 10.1128/mmbr.00124-22 | https://doi.org/10.1128/mmbr.00124-22 | Mar 2023 | Indirect to morphology; useful background node for existing streamlining graph. |
| streamlining selection (label-only) | associated_with | small cells and genomes (label-only) | “streamlining theory attributes small cells and genomes to…” (giovannoni2014implicationsofstreamlining pages 3-4) | Giovannoni 2014, *Implications of streamlining theory* | 10.1038/ismej.2014.60 | https://doi.org/10.1038/ismej.2014.60 | Apr 2014 | Strong review-level support for ecology→small-cell edge; not a direct molecular mechanism. |
| high surface-to-volume ratio (label-only) | increases | nutrient uptake efficiency (label-only) | “Thanks to their high surface-to-volume ratio, small-cell bacteria absorb nutrients most efficiently” (belykh2024ultramicrobacteriaandfilterable pages 1-2) | Belykh 2024, *Ultramicrobacteria and filterable bacteria* | 10.31951/2658-3518-2024-a-4-795 | https://doi.org/10.31951/2658-3518-2024-a-4-795 | Jan 2024 | Supports adaptive rationale for narrow/small cells in oligotrophy. |
| small-cell bacteria / ultramicrobacteria (label-only) | adapted_to | oligotrophic waters (ENVO:00000023 candidate) | “especially important in oligotrophic water bodies with low organic matter concentrations” (belykh2024ultramicrobacteriaandfilterable pages 1-2) | Belykh 2024, *Ultramicrobacteria and filterable bacteria* | 10.31951/2658-3518-2024-a-4-795 | https://doi.org/10.31951/2658-3518-2024-a-4-795 | Jan 2024 | Ecological edge; supports trait scope and candidate parent mechanism. |
| 0.2 µm filtration assay (label-only) | operationally_defines | femtoplankton / filterable bacteria fraction (label-only) | “femtoplankton – bacteria passing through filters with a 0.2 μm pore size” (belykh2024ultramicrobacteriaandfilterable pages 1-2) | Belykh 2024, *Ultramicrobacteria and filterable bacteria* | 10.31951/2658-3518-2024-a-4-795 | https://doi.org/10.31951/2658-3518-2024-a-4-795 | Jan 2024 | Assay edge, not phenotype-mechanism. Important boundary case: filterability ≠ width ≤0.5 µm. |
| ultramicrobacteria (label-only) | has_definition | diameter of proliferating cells <0.3 µm; volume <0.1 µm3; genome 0.58–3.2 Mb (label-only) | “Ultramicrobacteria have a diameter of proliferating cells less than 0.3 µm, cell volume less than 0.1 µm3” (belykh2024ultramicrobacteriaandfilterable pages 1-2) | Belykh 2024, *Ultramicrobacteria and filterable bacteria* | 10.31951/2658-3518-2024-a-4-795 | https://doi.org/10.31951/2658-3518-2024-a-4-795 | Jan 2024 | Very useful boundary/nearby-trait edge. UMB is narrower than the METPO ≤0.5 µm class. |
| pleomorphic bacteria with genome >3.2 Mb (label-only) | can_pass_into | <0.2 µm filter fraction (label-only) | “pleomorphic bacteria with genome sizes >3.2 Mb still pass into the fraction <0.2 µm” (belykh2024ultramicrobacteriaandfilterable pages 2-3) | Belykh 2024, *Ultramicrobacteria and filterable bacteria* | 10.31951/2658-3518-2024-a-4-795 | https://doi.org/10.31951/2658-3518-2024-a-4-795 | Jan 2024 | Important warning edge: filterability should not be curated as equivalent to very small width. |
| class A penicillin-binding proteins / aPBPs (label-only) | increases | cell diameter / width (PATO:0000921 candidate) | “aPBP-mediated isotropic insertion… enlarges the cell cylinder” (juillot2021ahighcontentmicroscopy pages 2-4) | Juillot 2021, *HCS screening identifies width genes* | 10.1128/msystems.01017-21 | https://doi.org/10.1128/msystems.01017-21 | Nov 2021 | Mechanistic width-control edge from B. subtilis model; opposite of narrow-width direction. |
| Rod complex (label-only) | decreases | cell diameter / width (PATO:0000921 candidate) | “Rod complex-mediated organized circumferential insertion of PG strands reduces it” (juillot2021ahighcontentmicroscopy pages 2-4) | Juillot 2021, *HCS screening identifies width genes* | 10.1128/msystems.01017-21 | https://doi.org/10.1128/msystems.01017-21 | Nov 2021 | Strong candidate mechanistic edge for thinner cells; may generalize to rod-shaped bacteria. |
| loss of aPBPs (label-only) | causes | thinner cells / reduced width (label-only) | “observation of thinner B. subtilis cells in the absence of aPBPs” (juillot2021ahighcontentmicroscopy pages 2-4) | Juillot 2021, *HCS screening identifies width genes* | 10.1128/msystems.01017-21 | https://doi.org/10.1128/msystems.01017-21 | Nov 2021 | Useful positive edge toward narrow width; taxon/model-specific. |
| reduced Rod complex activity (label-only) | causes | increased cell diameter / width (PATO:0000921 candidate) | “reduced activity of the Rod complex leads to… an increased cell diameter” (juillot2021ahighcontentmicroscopy pages 2-4) | Juillot 2021, *HCS screening identifies width genes* | 10.1128/msystems.01017-21 | https://doi.org/10.1128/msystems.01017-21 | Nov 2021 | Negative edge for the target trait; helps define opposite regulation. |
| magnesium ion (CHEBI:18420) | reduces_activity_of | peptidoglycan hydrolases (GO:0009253 process context) | “millimolar concentrations of magnesium… reduce the activity of PG hydrolases” (juillot2021ahighcontentmicroscopy pages 2-4) | Juillot 2021, *HCS screening identifies width genes* | 10.1128/msystems.01017-21 | https://doi.org/10.1128/msystems.01017-21 | Nov 2021 | Environmental/experimental factor; may affect width indirectly. Assay-context caution. |
| magnesium ion (CHEBI:18420) supplementation | slightly_decreases | average cell width (PATO:0000921 candidate) | “Addition of Mg2+ to the growth medium slightly reduced the average width of wild-type cells” (juillot2021ahighcontentmicroscopy pages 2-4) | Juillot 2021, *HCS screening identifies width genes* | 10.1128/msystems.01017-21 | https://doi.org/10.1128/msystems.01017-21 | Nov 2021 | Direct but small effect; likely experimental-condition edge rather than natural ecology. |
| MreB (gene/protein; UniProt/COG label-only) | determines | cell curvature and width (label-only) | “MreB cytoskeletal filaments act to sense and mechanically determine the cell curvature and therefore width” (kale2024mechanicsofe. pages 1-4) | Kale 2024, *Mechanics of E. coli cell width homeostasis* | 10.1101/2024.11.22.624946 | https://doi.org/10.1101/2024.11.22.624946 | Nov 2024 | Preprint; strong mechanistic relevance, but not peer-reviewed in this form. |
| A22 (CHEBI:?) | inhibits | MreB polymerization (label-only) | “A22, an inhibitor of MreB polymerization” (kale2024mechanicsofe. pages 1-4) | Kale 2024, *Mechanics of E. coli cell width homeostasis* | 10.1101/2024.11.22.624946 | https://doi.org/10.1101/2024.11.22.624946 | Nov 2024 | Chemical perturbation edge; useful assay/mechanism node. |
| A22-mediated MreB inhibition (label-only) | causes | loss of width control / cell shape change (label-only) | “A22… resulting in loss of width control and cell shape change” (kale2024mechanicsofe. pages 1-4) | Kale 2024, *Mechanics of E. coli cell width homeostasis* | 10.1101/2024.11.22.624946 | https://doi.org/10.1101/2024.11.22.624946 | Nov 2024 | Negative edge for stable narrow-width phenotype; preprint and perturbational. |
| PBP3/FtsI inhibition by cephalexin (label-only) | causes | bulge formation / altered width dynamics (label-only) | “cephalexin, a PBP3 inhibitor… low concentrations… result in bulge formation” (kale2024mechanicsofe. pages 1-4) | Kale 2024, *Mechanics of E. coli cell width homeostasis* | 10.1101/2024.11.22.624946 | https://doi.org/10.1101/2024.11.22.624946 | Nov 2024 | Perturbational antibiotic edge; informative for width homeostasis, not native trait causation. |


*Table: This table compiles candidate subject-predicate-object edges for the trait 'cell width very small (≤0.5 µm)' using only the provided source context. It spans ecological, operational, and molecular mechanisms and flags where evidence is indirect, assay-specific, taxon-specific, or preprint-only.*

---

## Curation warnings (do-not-curate yet / uncertain)
1. **Do not equate filterable fraction (<0.2 µm) with cell width ≤0.5 µm.** Filter passage is explicitly confounded by pleomorphy/cell envelope properties; pleomorphic bacteria with large genomes can enter <0.2 µm fraction (belykh2024ultramicrobacteriaandfilterable pages 2-3). Model filtration as an assay node.
2. **Mechanistic width-control edges from B. subtilis and E. coli are mechanistically relevant but not direct evidence of achieving ≤0.5 µm width.** They support *regulatory modules controlling width*, not necessarily that these modules alone produce the METPO extreme.
3. **E. coli mechanics paper is a preprint (bioRxiv).** Treat all specific quantitative/mechanical claims as provisional (kale2024mechanicsofe. pages 1-4).
4. **Streamlining theory is a review-level ecological theory.** It robustly supports an ecology→small-cell association but is indirect for specific width thresholds and should be curated with an ‘inferred/ecological’ qualifier (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3).

---

## DOI-first bibliography (with URLs and publication dates where available)
1. **Belykh OI, et al.** *Ultramicrobacteria and filterable bacteria in the plankton of Lake Baikal.* **Limnology and Freshwater Biology** (Jan 2024). DOI: **10.31951/2658-3518-2024-a-4-795**. https://doi.org/10.31951/2658-3518-2024-a-4-795 (belykh2024ultramicrobacteriaandfilterable pages 1-2, belykh2024ultramicrobacteriaandfilterable pages 2-3, belykh2024ultramicrobacteriaandfilterable pages 3-5)
2. **Noell SE, et al.** *A Reduction of Transcriptional Regulation in Aquatic Oligotrophic Microorganisms Enhances Fitness in Nutrient-Poor Environments.* **Microbiology and Molecular Biology Reviews** (Published 30 Mar 2023; Jun 2023 issue). DOI: **10.1128/mmbr.00124-22**. https://doi.org/10.1128/mmbr.00124-22 (noell2023areductionof pages 1-2)
3. **Giovannoni SJ, Thrash JC, Temperton B.** *Implications of streamlining theory for microbial ecology.* **The ISME Journal** (Apr 2014). DOI: **10.1038/ismej.2014.60**. https://doi.org/10.1038/ismej.2014.60 (giovannoni2014implicationsofstreamlining pages 1-2, giovannoni2014implicationsofstreamlining pages 2-3, giovannoni2014implicationsofstreamlining pages 3-4)
4. **Juillot D, et al.** *A High-Content Microscopy Screening Identifies New Genes Involved in Cell Width Control in Bacillus subtilis.* **mSystems** (Published 30 Nov 2021). DOI: **10.1128/msystems.01017-21**. https://doi.org/10.1128/msystems.01017-21 (juillot2021ahighcontentmicroscopy pages 1-2, juillot2021ahighcontentmicroscopy pages 2-4)
5. **Kale T, et al.** *Mechanics of E. coli cell width homeostasis and bulging dynamics from MreB and septum inhibition.* **bioRxiv** (Nov 2024). DOI: **10.1101/2024.11.22.624946**. https://doi.org/10.1101/2024.11.22.624946 (kale2024mechanicsofe. pages 1-4)


References

1. (belykh2024ultramicrobacteriaandfilterable pages 1-2): O.I. Belykh, A.Yu. Krasnopeev, S.A. Potapov, D.I. Gutnik, E.G. Sorokovikova, T.V. Butina, and I.V. Tikhonova. Ultramicrobacteria and filterable bacteria in the plankton of lake baikal. Limnology and Freshwater Biology, pages 795-820, Jan 2024. URL: https://doi.org/10.31951/2658-3518-2024-a-4-795, doi:10.31951/2658-3518-2024-a-4-795. This article has 2 citations.

2. (belykh2024ultramicrobacteriaandfilterable pages 2-3): O.I. Belykh, A.Yu. Krasnopeev, S.A. Potapov, D.I. Gutnik, E.G. Sorokovikova, T.V. Butina, and I.V. Tikhonova. Ultramicrobacteria and filterable bacteria in the plankton of lake baikal. Limnology and Freshwater Biology, pages 795-820, Jan 2024. URL: https://doi.org/10.31951/2658-3518-2024-a-4-795, doi:10.31951/2658-3518-2024-a-4-795. This article has 2 citations.

3. (belykh2024ultramicrobacteriaandfilterable pages 3-5): O.I. Belykh, A.Yu. Krasnopeev, S.A. Potapov, D.I. Gutnik, E.G. Sorokovikova, T.V. Butina, and I.V. Tikhonova. Ultramicrobacteria and filterable bacteria in the plankton of lake baikal. Limnology and Freshwater Biology, pages 795-820, Jan 2024. URL: https://doi.org/10.31951/2658-3518-2024-a-4-795, doi:10.31951/2658-3518-2024-a-4-795. This article has 2 citations.

4. (giovannoni2014implicationsofstreamlining pages 3-4): Stephen J Giovannoni, J Cameron Thrash, and Ben Temperton. Implications of streamlining theory for microbial ecology. The ISME Journal, 8:1553-1565, Apr 2014. URL: https://doi.org/10.1038/ismej.2014.60, doi:10.1038/ismej.2014.60. This article has 936 citations.

5. (giovannoni2014implicationsofstreamlining pages 1-2): Stephen J Giovannoni, J Cameron Thrash, and Ben Temperton. Implications of streamlining theory for microbial ecology. The ISME Journal, 8:1553-1565, Apr 2014. URL: https://doi.org/10.1038/ismej.2014.60, doi:10.1038/ismej.2014.60. This article has 936 citations.

6. (noell2023areductionof pages 1-2): Stephen E. Noell, Ferdi L. Hellweger, Ben Temperton, and Stephen J. Giovannoni. A reduction of transcriptional regulation in aquatic oligotrophic microorganisms enhances fitness in nutrient-poor environments. Microbiology and Molecular Biology Reviews, Jun 2023. URL: https://doi.org/10.1128/mmbr.00124-22, doi:10.1128/mmbr.00124-22. This article has 25 citations and is from a domain leading peer-reviewed journal.

7. (juillot2021ahighcontentmicroscopy pages 1-2): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 15 citations and is from a peer-reviewed journal.

8. (juillot2021ahighcontentmicroscopy pages 2-4): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 15 citations and is from a peer-reviewed journal.

9. (kale2024mechanicsofe. pages 1-4): Tanvi Kale, Ryth Dasgupta, Mandar M. Inamdar, and Chaitanya A. Athale. Mechanics of e. coli cell width homeostasis and bulging dynamics from mreb and septum inhibition. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.22.624946, doi:10.1101/2024.11.22.624946. This article has 0 citations.

10. (giovannoni2014implicationsofstreamlining pages 2-3): Stephen J Giovannoni, J Cameron Thrash, and Ben Temperton. Implications of streamlining theory for microbial ecology. The ISME Journal, 8:1553-1565, Apr 2014. URL: https://doi.org/10.1038/ismej.2014.60, doi:10.1038/ismej.2014.60. This article has 936 citations.

11. (juillot2021ahighcontentmicroscopy pages 10-11): Dimitri Juillot, Charlène Cornilleau, Nathalie Deboosere, Cyrille Billaudeau, Parfait Evouna-Mengue, Véronique Lejard, Priscille Brodin, Rut Carballido-López, and Arnaud Chastanet. A high-content microscopy screening identifies new genes involved in cell width control in bacillus subtilis. Dec 2021. URL: https://doi.org/10.1128/msystems.01017-21, doi:10.1128/msystems.01017-21. This article has 15 citations and is from a peer-reviewed journal.