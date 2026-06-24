---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T10:12:36.874579'
end_time: '2026-06-18T10:35:07.026884'
duration_seconds: 1350.15
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: triangular shaped
  trait_identifier: METPO:1000696
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: triangular_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism forms flat, triangular or wedge-shaped
    cells.
  parent_traits: METPO:1000666
  synonyms: triangular
  evidence_summary: 'DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically
    determined (Cell-shape review supports anisotropic envelope architecture as the
    basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703:
    archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal
    cells in halophilic archaea.)'
  causal_graph_summary: 'triangular_shaped_planar_polygonal_growth: 4 nodes, 3 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** triangular shaped
- **METPO identifier:** METPO:1000696
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, triangular or wedge-shaped cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** triangular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope architecture as the basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703: archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal cells in halophilic archaea.)
- **Existing causal graph summary:** triangular_shaped_planar_polygonal_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **triangular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/triangular_shaped.yaml`.

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
- **Trait label:** triangular shaped
- **METPO identifier:** METPO:1000696
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism forms flat, triangular or wedge-shaped cells.
- **Parent traits:** METPO:1000666
- **Synonyms:** triangular
- **Existing evidence:** DOI:10.1146/annurev-cellbio-101011-155745: cell shape is genetically determined (Cell-shape review supports anisotropic envelope architecture as the basis for non-round cell geometries such as triangles.) | DOI:10.1146/annurev-micro-090816-093703: archaeal cell shape (Archaeal cell-shape review supports unusual flat polygonal cells in halophilic archaea.)
- **Existing causal graph summary:** triangular_shaped_planar_polygonal_growth: 4 nodes, 3 edges

## Research Objective

Research the microbial trait **triangular shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/triangular_shaped.yaml`.

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


## Microbial Trait Causal Graph Curation Report: **Triangular shaped** (METPO:1000696)

### Executive scope summary
**METPO:1000696 (triangular shaped)** denotes a **morphology phenotype** in which cells are **flat, triangular, or wedge-shaped**. In current microbial literature, explicit “triangular cells” are most commonly reported as **conditional sub-phenotypes within broader flat polygonal pleomorphism** in **haloarchaea** (e.g., *Haloferax*, *Haloarcula*), rather than as a single invariant shape class. In addition, mechanistic work on **polygonal/angular envelopes** in some bacteria shows that **rigid S-layers** can impose **angular ridges**; this provides a mechanistic route that can plausibly generate triangular outlines even when papers operationalize the phenotype as “polygonal” rather than “triangular.” (patro2023“influenceofplasmids pages 1-2, du2023evolutionarydevelopmentalbiology pages 7-14, schiller2024identificationofstructural pages 1-2, gambelli2021thepolygonalcell pages 1-2)

**Boundary cases / nearby traits:**
- **Square-shaped** cells (e.g., *Haloquadratum*) are a related but distinct polygonal phenotype and should not be conflated with triangular. (du2023evolutionarydevelopmentalbiology pages 7-14, du2023evolutionarydevelopmentalbiology pages 31-33)
- **Flat polygonal pleomorphic disks/plates** are often quantified via circularity/aspect ratio and may include triangles/squares without being separately annotated. (schiller2024identificationofstructural pages 1-2, patro2023“influenceofplasmids pages 7-9)
- “**Triangular pores**” in S-layer lattices are **not** triangular cell shapes and must be treated as a different concept (S-layer lattice geometry). (gambelli2021thepolygonalcell pages 9-10)

### Key concepts and definitions (current understanding)
1. **Triangular shaped cells in haloarchaea are part of pleomorphism.** *Haloferax volcanii* and other haloarchaea can exhibit “**rods and plates … to triangles, squares, and more exotic forms**,” indicating that triangularity is included in a broader, condition-dependent shape repertoire. (patro2023“influenceofplasmids pages 1-2)
2. **Triangularity can be growth-phase dependent in specific taxa.** A haloarchaeal example explicitly links triangular shapes to stationary phase: *Haloarcula* spp. transition from rods in early exponential phase to a mixture including “**rods, disks, triangles, and squares**” in stationary phase. (du2023evolutionarydevelopmentalbiology pages 7-14)
3. **General archaeal diversity includes triangular morphotypes.** A recent high-authority paper summarizes that archaea range “to **triangular or square-shaped cells**,” providing contemporary framing and a pointer to the primary literature for triangular archaeal morphotypes. (schiller2024identificationofstructural pages 1-2)

### Exemplar taxa / contexts for the triangular phenotype
Evidence-supported exemplars relevant to METPO:1000696 curation include:
- **Archaea (haloarchaea):**
  - *Haloferax volcanii* (pleomorphic; triangles included among shapes; condition-dependent rod↔plate/polygonal states). (patro2023“influenceofplasmids pages 1-2, schiller2024identificationofstructural pages 1-2)
  - *Haloarcula hispanica* and *Haloarcula californiae* (reported to include triangular shapes in stationary phase mixtures). (du2023evolutionarydevelopmentalbiology pages 7-14)
  - *Haloarcula japonica* strain TR‑1 is referenced in the context of “triangular halophilic archaebacterium,” supporting a triangular cell exemplar in *Haloarcula*. (gambelli2021thepolygonalcell pages 13-14)
- **Bacteria (mechanistically adjacent polygonal/angular phenotype):**
  - *Methylomirabilis lanthanidiphila* (polygonal/angular cell envelope; S-layer-determined; important mechanistic anchor for how angular outlines can arise). (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10)

### Recent developments and latest research (prioritizing 2023–2024)
#### 1) Genetic and cytoskeletal determinants of flat polygonal states in *Haloferax volcanii* (2024)
A 2024 **Nature Communications** study used iterative proteomics, genetics, and imaging to identify specific determinants of archaeal shape states (rod vs disk/plate-like forms). Key findings that are directly curatable as mechanistic entities include:
- **RdfA (HVO_2174)** and **Sph3 (HVO_2175)** are **required for rod formation**; deletions form only disks and lose wild-type-like motility. (schiller2024identificationofstructural pages 3-5)
- **DdfA (HVO_2176)** is implicated as a “**key player in disk formation**.” (schiller2024identificationofstructural pages 6-7)
- **Volactin (VolA; HVO_2015)**, a newly annotated archaeal **actin homolog**, is important for rod-to-disk transitions: mid-log partial deletion (ΔvolA*) yields “**significantly more rods**,” and volactin forms dynamic filaments and membrane patches. (schiller2024identificationofstructural pages 6-7)
- **Quantitative/statistical details:** label-free proteomics quantified **1944 proteins** with **314** differentially abundant; aspect ratio comparisons used **Kolmogorov–Smirnov** tests with large sample sizes (n up to ~2600 per condition) and thresholds (aspect ratio <2). (schiller2024identificationofstructural pages 3-5)

Relevance to triangular trait: these determinants govern the **flat polygonal disk/plate state** in which triangular outlines are observed in haloarchaea; however, the 2024 study does not itself isolate “triangular” as a separately quantified class, so edges to METPO:1000696 should be flagged as **indirect** unless further triangle-specific evidence is obtained. (schiller2024identificationofstructural pages 1-2, patro2023“influenceofplasmids pages 1-2)

#### 2) Spatial organization links morphology to motility in *H. volcanii* (2024)
A 2024 Frontiers in Microbiology study reports that **MinD2 (ParA/MinD ATPase family)** modulates both **cell shape** and **motility** in *H. volcanii*, emphasizing spatial organization over transcription:
- Cells transition “**from rod-shaped to flat, polygonal pleomorphic disks (plate shaped)**.” (patro2024mind2modulatescell pages 10-11)
- **ΔminD2** shows a “**preponderance to form plate-shaped cells**.” (patro2024mind2modulatescell pages 10-11)
- **MinD2/MinD4** influence localization of motility/chemosensory machineries: in a ΔminD2ΔminD4 background, there is an almost complete absence of archaellum (**5%**) or chemosensory (**1%**) machineries; and CheW focus formation drops dramatically (e.g., 5% polar foci with ΔminD2ΔcheW; 2% with ΔminD2ΔminD4ΔcheW at OD600 0.01). (patro2024mind2modulatescell pages 10-11, patro2024mind2modulatescell pages 5-7)

Relevance to triangular trait: triangular morphotypes in haloarchaea are often discussed alongside growth-phase transitions and motility states; MinD2 provides a mechanistic entry point connecting the pleomorphic/polygonal state to functional outcomes (motility/chemotaxis organization). (patro2023“influenceofplasmids pages 1-2, patro2024mind2modulatescell pages 10-11)

#### 3) Reproducible morphology quantification and “experimental factors” affecting haloarchaeal pleomorphism (2023)
A 2023 Frontiers in Microbiology paper provides a practical framework for **quantifying** pleomorphism and highlights how **plasmids/markers** can alter shape—important for curation as **experimental factors** rather than intrinsic mechanism:
- Triangles are explicitly listed among *H. volcanii* shapes: “**rods and plates … to triangles, squares, and more exotic forms**.” (patro2023“influenceofplasmids pages 1-2)
- OD600-series quantification shows strong, reproducible transitions. Example quantitative statements include:
  - rods/intermediates peak at **OD600 = 0.06** (65% and 59% respectively) in one background. (patro2023“influenceofplasmids pages 7-9)
  - transition to plates between **OD600 = 0.1 and 0.2**, attaining **95% plates** in one strain/background. (patro2023“influenceofplasmids pages 7-9)
  - plasmid-specific persistence of rods/intermediates at OD600=0.2 (e.g., **33%** with pTA233; **27%** with pTA1392; **52%** with pTA230 in H98 context). (patro2023“influenceofplasmids pages 7-9)
- Statistical/scale: analyses used **Kruskal–Wallis tests** and >**500–1300** cells from three independent experiments. (patro2023“influenceofplasmids pages 7-9)

### Mechanistic entities for causal-graph curation (candidate nodes)
A structured inventory of nodes supported by the retrieved evidence is provided below.

| Node label | Node type | Suggested ontology grounding | Example taxa/context | Key supporting citation IDs |
|---|---|---|---|---|
| S-layer protein mela_00855 | gene/protein | label only | *Methylomirabilis lanthanidiphila* candidate S-layer protein linked to polygonal/angular envelope morphology | (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10) |
| S-layer | structure | label only | Outermost rigid layer determining polygonal shape in *M. lanthanidiphila*; broad haloarchaeal shape-maintenance context | (gambelli2021thepolygonalcell pages 1-2, du2023evolutionarydevelopmentalbiology pages 7-14, gambelli2021thepolygonalcell pages 9-10) |
| Outer membrane | structure | GO:0019867 | *M. lanthanidiphila* outer membrane follows polygonal cell shape | (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10) |
| Peptidoglycan layer | structure | GO:0009273 | *M. lanthanidiphila* peptidoglycan does not follow polygonal shape | (gambelli2021thepolygonalcell pages 1-2) |
| Cytoplasmic membrane | structure | GO:0005886 | *M. lanthanidiphila* cytoplasmic membrane does not follow polygonal shape | (gambelli2021thepolygonalcell pages 1-2) |
| Volactin (VolA, HVO_2015) | gene/protein | label only | *Haloferax volcanii* actin homolog required for disk-shape morphogenesis and rod-to-disk transition | (schiller2024identificationofstructural pages 6-7) |
| rdfA (HVO_2174; rod-determining factor A) | gene/protein | label only | *H. volcanii* rod-determining factor; deletion yields disk-only phenotype | (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 3-5) |
| sph3 (HVO_2175) | gene/protein | label only | *H. volcanii* SMC-like protein required for rod formation | (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 3-5) |
| ddfA (HVO_2176; disk-determining factor A) | gene/protein | label only | *H. volcanii* key player in disk formation | (patro2024mind2modulatescell pages 10-11, schiller2024identificationofstructural pages 6-7) |
| CetZ1 | gene/protein | label only | *H. volcanii* tubulin/FtsZ-family shape determinant; depletion prevents rod formation | (schiller2024identificationofstructural pages 1-2, du2023evolutionarydevelopmentalbiology pages 7-14) |
| MinD2 (HVO_0595) | gene/protein | label only | *H. volcanii* ParA/MinD-family ATPase affecting rod retention, motility, and machinery positioning | (patro2024mind2modulatescell pages 10-11) |
| MinD4 | gene/protein | label only | *H. volcanii* cooperates with MinD2 in positioning motility and chemosensory machinery | (patro2024mind2modulatescell pages 5-7, patro2024mind2modulatescell pages 10-11) |
| ArlD | gene/protein | label only | *H. volcanii* archaellum motor marker used to quantify polar foci and archaellum presence | (patro2024mind2modulatescell pages 5-7, patro2024mind2modulatescell pages 10-11) |
| ArlA1/ArlA2 | gene/protein | label only | *H. volcanii* archaellins enriched in rod-forming cells | (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 6-7) |
| CheW | gene/protein | label only | *H. volcanii* marker for chemosensory array localization; affected by MinD2/MinD4 | (patro2024mind2modulatescell pages 5-7, patro2024mind2modulatescell pages 10-11) |
| Agl11 | gene/protein | label only | *H. volcanii* Agl15-dependent N-glycosylation component enriched in disk-forming conditions | (schiller2024identificationofstructural pages 3-5) |
| Agl12 | gene/protein | label only | *H. volcanii* Agl15-dependent N-glycosylation component enriched in disk-forming conditions | (schiller2024identificationofstructural pages 3-5) |
| Agl15-dependent N-glycosylation pathway | process | GO:0006487 | *H. volcanii* envelope/glycosylation pathway associated with disk-forming conditions | (schiller2024identificationofstructural pages 3-5) |
| ArtA | gene/protein | label only | *H. volcanii* depletion/deletion biases cells toward rods; linked to cytokinetic ring localization in cited context | (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 9-9) |
| LonB | gene/protein | label only | *H. volcanii* membrane protease; depletion yields predominantly rod-shaped cells | (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 9-9) |
| PssA | gene/protein | label only | *H. volcanii* phosphatidylethanolamine biosynthesis enzyme; deletion/depletion biases toward rods | (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 9-9) |
| PssD | gene/protein | label only | *H. volcanii* phosphatidylethanolamine biosynthesis enzyme; deletion/depletion biases toward rods | (schiller2024identificationofstructural pages 1-2, schiller2024identificationofstructural pages 9-9) |
| Growth phase | environmental factor | label only | Early-log rods versus mid/late-log flat polygonal disks in *H. volcanii* and related haloarchaea | (schiller2024identificationofstructural pages 1-2, du2023evolutionarydevelopmentalbiology pages 7-14, patro2023“influenceofplasmids pages 7-9) |
| OD600 | assay/measurement | label only | Operational growth-stage proxy for rod-to-plate/disk transitions in *H. volcanii* studies | (schiller2024identificationofstructural pages 1-2, patro2023“influenceofplasmids pages 7-9) |
| Plasmid presence | environmental factor | label only | Experimental factor favoring early rod development in *H. volcanii* | (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 7-9) |
| auxotrophic mutation / hdrB marker | environmental factor | label only | *H. volcanii* ΔhdrB strains/markers strongly affect morphology metrics | (patro2023“influenceofplasmids pages 1-2) |
| Trace element availability | environmental factor | label only | Haloarchaeal morphology shifts under depletion of Fe, Zn, Cu, Co, Mn, Ni, Mo, B | (du2023evolutionarydevelopmentalbiology pages 7-14) |
| DIC microscopy | assay/measurement | label only | Used for *H. volcanii* mutant shape phenotyping and aspect-ratio quantification | (schiller2024identificationofstructural pages 3-5) |
| Phase-contrast microscopy | assay/measurement | label only | Used for growth-stage morphology analysis in *H. volcanii* plasmid/auxotroph experiments | (patro2023“influenceofplasmids pages 7-9, du2023evolutionarydevelopmentalbiology pages 26-31) |
| Cryo-electron tomography (cryo-ET) | assay/measurement | label only | Used to resolve polygonal envelope and S-layer organization in *M. lanthanidiphila* | (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10) |
| Subtomogram averaging | assay/measurement | label only | Used with cryo-ET to obtain 21 Å S-layer lattice map in *M. lanthanidiphila* | (gambelli2021thepolygonalcell pages 9-10) |
| Immunogold labeling | assay/measurement | label only | Used to localize mela_00855 to S-layer patches and cell envelope in *M. lanthanidiphila* | (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10) |
| Circularity metric | assay/measurement | label only | Used to classify rods/intermediates/plates in *H. volcanii* morphology studies | (patro2023“influenceofplasmids pages 7-9) |
| Aspect ratio metric | assay/measurement | label only | Used for *H. volcanii* shape quantification; aspect ratio <2 counted as disks/short rods in one study | (schiller2024identificationofstructural pages 3-5, patro2023“influenceofplasmids pages 7-9) |
| Cell area metric | assay/measurement | label only | Used to compare shape states across *H. volcanii* genotypes and growth stages | (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 7-9) |
| Cell length metric | assay/measurement | label only | Used to quantify elongation and rod development in *H. volcanii* | (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 7-9) |
| Motility halo assay | assay/measurement | label only | Agar-based assay quantifying motility differences among shape mutants in *H. volcanii* | (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 11-12) |
| Motility | phenotype | GO:0040011 | Rod morphology correlates with motility in *H. volcanii*; reduced in discoid/ΔminD2 contexts | (patro2024mind2modulatescell pages 10-11, schiller2024identificationofstructural pages 6-7) |
| Chemosensory localization | phenotype | label only | Polar CheW focus formation/array localization depends on MinD2 and MinD4 in *H. volcanii* | (patro2024mind2modulatescell pages 5-7, patro2024mind2modulatescell pages 10-11) |
| Rod shape | phenotype | label only | Early-growth and rod-program morphology in *H. volcanii*; contrasted with disks/plates | (schiller2024identificationofstructural pages 1-2, patro2023“influenceofplasmids pages 7-9) |
| Disk / plate / flat polygonal pleomorphic disk shape | phenotype | label only | Flat polygonal state in *H. volcanii* associated with later growth and disk-determining factors | (schiller2024identificationofstructural pages 1-2, patro2024mind2modulatescell pages 10-11, patro2023“influenceofplasmids pages 7-9) |
| Triangular shaped cells | phenotype | METPO:1000696 | Trait target; reported among haloarchaeal pleomorphic forms alongside rods, plates, squares | (patro2023“influenceofplasmids pages 1-2, du2023evolutionarydevelopmentalbiology pages 7-14) |
| Polygonal cell shape | phenotype | label only | Angular envelope morphology in *M. lanthanidiphila* and broader flat polygonal haloarchaeal states | (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10) |


*Table: This table inventories candidate nodes for a causal graph of the triangular-shaped microbial trait, limited to entities and measurements directly supported in the provided context. It is useful for selecting grounded nodes before curating causal edges into TraitMech.*

### Evidence-backed candidate causal edges (triples)
The following table lists candidate causal edges in a form suitable for curation into a TraitMech/TraitGraph YAML. Edges are annotated with uncertainty where triangular specificity is not directly demonstrated.

| Subject node (suggested ID) | Predicate | Object node (suggested ID) | Evidence snippet | Taxon/context | Reference | DOI | URL | Publication date | Curation notes incl. uncertainty |
|---|---|---|---|---|---|---|---|---|---|
| S-layer protein mela_00855 (label only) | determines | polygonal cell shape (candidate parent of METPO:1000696) | “the S-layer is the determining factor for their polygonal cell shape” | *Methylomirabilis lanthanidiphila* (NC10 bacterium) | Gambelli et al., 2021, *The Polygonal Cell Shape and Surface Protein Layer of Anaerobic Methane-Oxidizing Methylomirabilis lanthanidiphila Bacteria* | 10.3389/fmicb.2021.766527 | https://doi.org/10.3389/fmicb.2021.766527 | 2021-12 | Strong mechanistic evidence for polygonal/angular morphology, not triangle-specific; curate as broader polygonal/planar-envelope mechanism feeding triangular trait. Uncertainty: medium for direct METPO:1000696 mapping. (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10) |
| S-layer sheet architecture (GO:0098556 cell outer membrane? label-only preferred) | confers rigidity to | polygonal/angular envelope morphology | “these S-layer sheets are very rigid” and “the dense net of protein bridges… establishes the observed rigidity of the S-layer” | *M. lanthanidiphila* | Gambelli et al., 2021, same as above | 10.3389/fmicb.2021.766527 | https://doi.org/10.3389/fmicb.2021.766527 | 2021-12 | Structural edge from rigid overlapping S-layer sheets to stable angular morphology; useful mechanism node: rigid S-layer sheets / protein bridges. Uncertainty: low for polygonal shape, medium for triangular trait. (gambelli2021thepolygonalcell pages 9-10) |
| Outer membrane (GO:0019867) | follows | polygonal cell shape | “the outer membrane followed the polygonal cell shape” | *M. lanthanidiphila* | Gambelli et al., 2021, same as above | 10.3389/fmicb.2021.766527 | https://doi.org/10.3389/fmicb.2021.766527 | 2021-12 | Good localization/structure edge; outer membrane is a participant, not necessarily the upstream determinant. Uncertainty: low. (gambelli2021thepolygonalcell pages 9-10, gambelli2021thepolygonalcell pages 10-11) |
| Peptidoglycan layer (GO:0009273 peptidoglycan-based cell wall) | does not follow | polygonal cell shape | “the S-layer and outer membrane, but not the peptidoglycan layer and the cytoplasmic membrane, exhibited the polygonal shape” | *M. lanthanidiphila* | Gambelli et al., 2021, same as above | 10.3389/fmicb.2021.766527 | https://doi.org/10.3389/fmicb.2021.766527 | 2021-12 | Negative edge helpful for boundary of mechanism: exclude PG layer as direct shaper here. Uncertainty: low. (gambelli2021thepolygonalcell pages 1-2) |
| volactin / VolA / HVO_2015 (label only; actin homolog) | promotes | disk-shape formation / rod-to-disk transition | “volactin is important for rod-to-disk shape transitions” and “Mid-log ΔvolA* cultures contained significantly more rods” | *Haloferax volcanii* (haloarchaeon) | Schiller et al., 2024, *Identification of structural and regulatory cell-shape determinants in Haloferax volcanii* | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Strong genetic evidence for flat disk morphogenesis; triangles likely emerge within broader flat polygonal states, so indirect for METPO:1000696. Uncertainty: medium. (schiller2024identificationofstructural pages 6-7) |
| volactin / VolA / HVO_2015 (label only) | assembles into | dynamic filaments | “Volactin assembles into dynamic filaments in vivo” | *H. volcanii* | Schiller et al., 2024, same as above | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Supports cytoskeletal-structure node for shape mechanism; curate as mechanistic intermediate rather than trait edge. Uncertainty: low. (schiller2024identificationofstructural pages 6-7) |
| rdfA / HVO_2174 (label only; RdfA) | is required for | rod formation | “Δhvo_2174… formed only disks across all growth phases” and authors “annotate HVO_2174 as rod-determining factor A (RdfA)” | *H. volcanii* | Schiller et al., 2024, same as above | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Regulatory edge establishing rod-vs-disk switch. Useful because triangular cells in haloarchaea likely arise from disk/polygonal program when rod program is reduced. Uncertainty: medium for triangular specificity. (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 1-2) |
| sph3 / HVO_2175 (label only; SMC-like protein) | is required for | rod formation | “Δsph3 formed only disks across all growth phases” | *H. volcanii* | Schiller et al., 2024, same as above | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Strong mutant evidence; role may be partly linked to motility-associated rod state. Uncertainty: medium for triangular specificity. (schiller2024identificationofstructural pages 3-5) |
| ddfA / HVO_2176 (label only; DdfA) | promotes | disk formation | “ddfA as a key player in disk formation” | *H. volcanii* | Schiller et al., 2024, same as above | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Strong reverse-genetics evidence; disk formation is proximal to flat polygonal/triangular morphologies. Uncertainty: medium. (schiller2024identificationofstructural pages 6-7, patro2024mind2modulatescell pages 10-11) |
| CetZ1 (label only; tubulin/FtsZ family) | is required for | rod formation | “CetZ1 depletion prevents rod formation” | *H. volcanii* | Du, 2023, *Evolutionary Developmental Biology in Haloarchaea* | 10.48617/etd.674 | https://doi.org/10.48617/etd.674 | 2023-01 | Thesis source summarizing prior literature; acceptable as supporting review-level edge, but direct primary citation would be preferable before final TraitMech curation. Uncertainty: medium. (du2023evolutionarydevelopmentalbiology pages 7-14) |
| growth phase: early log (label only) | is associated with | rod-shaped cells | “development of rods is restricted to the early stages of exponential growth” | *H. volcanii* | Patro et al., 2023, *Influence of plasmids, selection markers and auxotrophic mutations on Haloferax volcanii cell shape plasticity* | 10.3389/fmicb.2023.1270665 | https://doi.org/10.3389/fmicb.2023.1270665 | 2023-09 | Environmental/assay context edge. Important because triangular cells are generally not the early-log rod state. Uncertainty: low. (patro2023“influenceofplasmids pages 7-9, patro2023“influenceofplasmids pages 1-2) |
| increasing OD600 / later growth phase (label only) | shifts cells toward | plates / flat polygonal pleomorphic disks | “transitioned to plate shape between OD600 = 0.1 and OD600 = 0.2 to attain 95% of plates” | *H. volcanii* strain H98 and related backgrounds | Patro et al., 2023, same as above | 10.3389/fmicb.2023.1270665 | https://doi.org/10.3389/fmicb.2023.1270665 | 2023-09 | Quantitative environmental edge; plates/disks are the proximate state from which triangular/square subtypes may be drawn. Uncertainty: medium for direct triangular mapping. (patro2023“influenceofplasmids pages 7-9) |
| plasmid presence (experimental factor) | favors development of | rods in early growth | “plasmid presence is also a factor impacting H. volcanii cell shape, notably by favoring the development of rods in early stages of growth” | *H. volcanii* | Patro et al., 2023, same as above | 10.3389/fmicb.2023.1270665 | https://doi.org/10.3389/fmicb.2023.1270665 | 2023-09 | Assay/genetic background effect; likely should be modeled as experimental factor, not native mechanism. Uncertainty: low as assay effect; high as natural trait mechanism. (patro2023“influenceofplasmids pages 1-2) |
| trace element depletion (Fe, Zn, Cu, Co, Mn, Ni, Mo, B; label only) | causes | elongated rods with polar tails and uneven widths | “trace-element depletion causes Hfx. volcanii to become ‘elongated rods with polar tails and uneven widths’” | *H. volcanii* | Du, 2023, same as above | 10.48617/etd.674 | https://doi.org/10.48617/etd.674 | 2023-01 | Environmental factor shifting cells away from polygonal/triangular states; useful negative regulator/context edge. Thesis summary; confirm with primary study before strict curation. Uncertainty: medium. (du2023evolutionarydevelopmentalbiology pages 7-14) |
| MinD2 / HVO_0595 (label only) | promotes retention of | rod shape | “MinD2 promotes retention of a rod shape especially in early growth/early log phase” | *H. volcanii* | Patro et al., 2024, *MinD2 modulates cell shape and motility in the archaeon Haloferax volcanii* | 10.3389/fmicb.2024.1474570 | https://doi.org/10.3389/fmicb.2024.1474570 | 2024-11 | Regulatory edge from spatial organizer to morphology state. Triangular/polygonal cells may increase when this rod-retention system is lost. Uncertainty: medium. (patro2024mind2modulatescell pages 10-11) |
| ΔminD2 / loss of MinD2 (experimental genotype) | increases tendency to form | plate-shaped cells | “ΔminD2 mutants show a ‘preponderance to form plate-shaped cells’” | *H. volcanii* | Patro et al., 2024, same as above | 10.3389/fmicb.2024.1474570 | https://doi.org/10.3389/fmicb.2024.1474570 | 2024-11 | Strong mutant phenotype for disk/plate state; indirect but relevant for flat polygonal/triangular morphogenesis. Uncertainty: medium. (patro2024mind2modulatescell pages 10-11) |
| MinD2 (label only) | positions | archaellum machinery | “MinD2 impacts the localization of both the motility… machineries” and ΔminD2 cells had reduced polar ArlD-GFP foci | *H. volcanii* | Patro et al., 2024, same as above | 10.3389/fmicb.2024.1474570 | https://doi.org/10.3389/fmicb.2024.1474570 | 2024-11 | Functional consequence edge linking shape regulator to motility apparatus organization. Uncertainty: low. (patro2024mind2modulatescell pages 5-7, patro2024mind2modulatescell pages 10-11) |
| MinD2 (label only) | positions | chemosensory arrays / CheW foci | “MinD2 impacts the localization of both the motility and chemosensory machineries” | *H. volcanii* | Patro et al., 2024, same as above | 10.3389/fmicb.2024.1474570 | https://doi.org/10.3389/fmicb.2024.1474570 | 2024-11 | Functional consequence edge; in ΔminD2ΔcheW, only 5% cells showed polar CheW foci, and in ΔminD2ΔminD4ΔcheW only 2% at OD600 0.01. Uncertainty: low. (patro2024mind2modulatescell pages 5-7, patro2024mind2modulatescell pages 10-11) |
| rod morphology (label only) | correlates with | motility | “motility correlates with rods” | *H. volcanii* | Schiller et al., 2024, same as above | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Useful phenotype-phenotype edge; can support downstream consequence modeling. Uncertainty: low. (schiller2024identificationofstructural pages 6-7) |
| archaellins + chemotaxis proteins + transducers (label only) | are enriched in | rods | “archaellin proteins ArlA1 and ArlA2 were highly abundant in rods as were chemotaxis proteins” | *H. volcanii* | Schiller et al., 2024, same as above | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Proteomics-backed association; may reflect functional coupling rather than direct causation on triangular shape. Uncertainty: medium. (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 6-7) |
| Agl11/Agl12 and Agl15-dependent N-glycosylation pathway (label only) | are enriched in | disk-forming conditions | “Agl11 and Agl12, showed higher abundance in disk-forming conditions and mutants” | *H. volcanii* | Schiller et al., 2024, same as above | 10.1038/s41467-024-45196-0 | https://doi.org/10.1038/s41467-024-45196-0 | 2024-02 | Candidate envelope/glycosylation mechanism for flat polygonal states; not yet direct causal proof. Uncertainty: medium-high. (schiller2024identificationofstructural pages 3-5) |
| S-layer (label only) | contributes to maintenance of | cell shape | “S-layer… contributes to cell shape maintenance” | haloarchaea broadly; includes taxa with triangles/squares | Du, 2023, same as above | 10.48617/etd.674 | https://doi.org/10.48617/etd.674 | 2023-01 | Broad review/thesis statement across haloarchaea; useful high-level edge but not species-specific and not direct experimental proof in triangular cells. Uncertainty: high for strict TraitMech curation. (du2023evolutionarydevelopmentalbiology pages 7-14) |


*Table: This table compiles candidate causal edges relevant to the microbial trait 'triangular shaped' (METPO:1000696), emphasizing experimentally supported structural, cytoskeletal, regulatory, environmental, and functional links from the provided sources. It is designed to help prioritize which edges are strong enough for TraitMech curation and which remain indirect or taxon-specific.*

### Statistics and quantitative data useful for curation
**Haloarchaeal pleomorphism / shape transitions**
- OD600-resolved transitions quantify the rod→plate shift; example: peak rods/intermediates at OD600=0.06 (65% and 59%) and plates reaching 95% by OD600=0.2 in one background. (patro2023“influenceofplasmids pages 7-9)
- Large-n morphology distributions: >1300 cells (H26 analysis) and >500 cells (H53 analysis) across three experiments, analyzed by Kruskal–Wallis tests. (patro2023“influenceofplasmids pages 7-9)
- Aspect ratio-based shape quantification: aspect ratio <2 used as disk/short-rod threshold; early/late log n in the ~800–2600 range per strain, with Kolmogorov–Smirnov tests (p<0.0001) and motility-halo t-tests. (schiller2024identificationofstructural pages 3-5)

**Polygonal bacterial envelope structure (S-layer–driven)**
- Cryo-ET/subtomogram averaging: **8,938 sub-volumes**, **21 Å** resolution. (gambelli2021thepolygonalcell pages 9-10)
- S-layer lattice: p6 symmetry; unit cell **~11.6 × ~11.9 nm** at **60°**; thickness **~7 nm**; pore areas **~12 nm² (hexagonal)** and **~3.9 nm² (triangular)**. (gambelli2021thepolygonalcell pages 9-10, gambelli2021thepolygonalcell media 935aa569)
- Gene expression proxy: mela_00855 transcription reported as **1,539.33 RPKM**. (gambelli2021thepolygonalcell pages 9-10)
- Surface-area/volume advantage estimate: polygonal shape computed as SA:V **~0.2 µm⁻1** higher than an equivalent rod. (gambelli2021thepolygonalcell pages 10-11)

### Current applications and real-world implementations
**1) Practical assay implementations for morphology curation**
- **Image-based morphometrics** (circularity, aspect ratio, area, length) across OD600 series provide a reproducible operationalization of pleomorphism—useful for standardizing phenotype evidence in curation. (patro2023“influenceofplasmids pages 7-9)
- **Motility halo assays** and fluorescence localization of **ArlD** (archaellum motor) and **CheW** (chemosensory arrays) connect morphology to function and help define downstream phenotypes for causal graphs. (schiller2024identificationofstructural pages 3-5, patro2024mind2modulatescell pages 5-7)

**2) High-resolution structural implementation for angular/polygonal envelopes**
- **Cryo-ET with subtomogram averaging** and **immunogold labeling** provide a template for linking specific envelope structures (S-layer sheets) to polygonal cell geometry in vivo. (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10)
- The same work proposes **AFM** as a follow-on method to quantify S-layer binding forces/elasticity, emphasizing translational relevance to materials/biophysical characterization. (gambelli2021thepolygonalcell pages 9-10)

**3) Methods guidance for motility/flow quantification (relevant for shape-function graphs)**
- A 2023 methods review provides concrete PIV/PTV parameterization (e.g., 1–10 µm tracers; volume fraction ~10⁻5 v/v; window sizes and pixel displacement constraints) and standard tracking metrics (curvature, persistence, MSD), useful for integrating morphology into biophysical assays. (bondocnaumovitz2023methodsandmeasures pages 8-9)

### Expert opinions / authoritative analysis (within retrieved sources)
- A high-authority 2024 paper frames triangular/square morphologies as part of archaeal diversity, and positions archaeal shape determination as poorly understood but tractable via genetics, proteomics, and live-cell imaging. (schiller2024identificationofstructural pages 1-2)
- The 2021 polygonal-bacteria study interprets strong S-layer rigidity (“very rigid”; dense bridges; potentially unusually strong interactions) as explanatory for stable angular morphology and suggests AFM to further test mechanical hypotheses. (gambelli2021thepolygonalcell pages 9-10)

### Ontology grounding suggestions (non-exhaustive)
- **Trait:** METPO:1000696 (triangular shaped)
- **Structures:** outer membrane GO:0019867; peptidoglycan-based cell wall GO:0009273; cytoplasmic membrane GO:0005886 (artifact-01)
- **Process/phenotypes:** motility GO:0040011; N-glycosylation GO:0006487 (artifact-01)
- **Genes/proteins:** use **label-only** placeholders for RdfA/DdfA/Volactin/MinD2/CetZ1/ArtA/LonB/PssA/PssD unless UniProt IDs are added during curation.

### Warnings / claims not yet ready for TraitMech curation
1. **Triangle-specific mechanisms are not directly mapped** in the strongest 2023–2024 mechanistic studies; they primarily resolve **rod vs disk/plate/polygonal** states and list triangles as part of pleomorphism rather than quantifying triangular frequency or dedicated genetic determinants. Curate triangle edges as **uncertain/indirect** unless supplemented with primary “triangular cell” ultrastructure/perturbation papers for a named taxon (e.g., *Haloarcula japonica* TR‑1) that directly connect a mechanism to triangular geometry. (patro2023“influenceofplasmids pages 1-2, schiller2024identificationofstructural pages 1-2, gambelli2021thepolygonalcell pages 13-14)
2. **Plasmid/marker effects** (e.g., hdrB selection markers) are strong determinants of measured morphology in *H. volcanii* but represent **experimental confounders**; these should typically be modeled as **experimental factors** rather than biological mechanisms of the native trait. (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 7-9)
3. Several broad statements about S-layer flexibility and CetZ effects are from a **2023 thesis**; they can guide hypotheses but should be corroborated with primary peer-reviewed sources before “strong” curation. (du2023evolutionarydevelopmentalbiology pages 7-14)

---

## DOI-first bibliography (with URLs and publication dates)
1. **Schiller H. et al. (2024-02).** *Identification of structural and regulatory cell-shape determinants in Haloferax volcanii.* **Nature Communications** 15:1414. DOI: **10.1038/s41467-024-45196-0**. URL: https://doi.org/10.1038/s41467-024-45196-0 (schiller2024identificationofstructural pages 3-5, schiller2024identificationofstructural pages 6-7, schiller2024identificationofstructural pages 1-2)
2. **Patro M. et al. (2024-11).** *MinD2 modulates cell shape and motility in the archaeon Haloferax volcanii.* **Frontiers in Microbiology** 15. DOI: **10.3389/fmicb.2024.1474570**. URL: https://doi.org/10.3389/fmicb.2024.1474570 (patro2024mind2modulatescell pages 10-11, patro2024mind2modulatescell pages 5-7)
3. **Patro M. et al. (2023-09).** *Influence of plasmids, selection markers and auxotrophic mutations on Haloferax volcanii cell shape plasticity.* **Frontiers in Microbiology** 14. DOI: **10.3389/fmicb.2023.1270665**. URL: https://doi.org/10.3389/fmicb.2023.1270665 (patro2023“influenceofplasmids pages 1-2, patro2023“influenceofplasmids pages 7-9)
4. **Gambelli L. et al. (2021-12).** *The Polygonal Cell Shape and Surface Protein Layer of Anaerobic Methane-Oxidizing Methylomirabilis lanthanidiphila Bacteria.* **Frontiers in Microbiology** 12:766527. DOI: **10.3389/fmicb.2021.766527**. URL: https://doi.org/10.3389/fmicb.2021.766527 (gambelli2021thepolygonalcell pages 1-2, gambelli2021thepolygonalcell pages 9-10, gambelli2021thepolygonalcell pages 10-11, gambelli2021thepolygonalcell media 935aa569)
5. **Du Z. (2023-01).** *Evolutionary Developmental Biology in Haloarchaea.* Brandeis University thesis. DOI: **10.48617/etd.674**. URL: https://doi.org/10.48617/etd.674 (du2023evolutionarydevelopmentalbiology pages 7-14, du2023evolutionarydevelopmentalbiology pages 26-31)
6. **Bondoc-Naumovitz K.G. et al. (2023-02).** *Methods and Measures for Investigating Microscale Motility.* **Integrative and Comparative Biology** 63:1485–1508 (arXiv-linked). DOI: **10.48550/arxiv.2303.00068**. URL: https://doi.org/10.48550/arxiv.2303.00068 (bondocnaumovitz2023methodsandmeasures pages 8-9)


References

1. (patro2023“influenceofplasmids pages 1-2): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

2. (du2023evolutionarydevelopmentalbiology pages 7-14): Zhantao Du. Evolutionary developmental biology in haloarchaea. Text, Jan 2023. URL: https://doi.org/10.48617/etd.674, doi:10.48617/etd.674. This article has 0 citations and is from a peer-reviewed journal.

3. (schiller2024identificationofstructural pages 1-2): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

4. (gambelli2021thepolygonalcell pages 1-2): Lavinia Gambelli, Rob Mesman, Wouter Versantvoort, Christoph A. Diebolder, Andreas Engel, Wiel Evers, Mike S. M. Jetten, Martin Pabst, Bertram Daum, and Laura van Niftrik. The polygonal cell shape and surface protein layer of anaerobic methane-oxidizing methylomirabilis lanthanidiphila bacteria. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.766527, doi:10.3389/fmicb.2021.766527. This article has 3 citations and is from a peer-reviewed journal.

5. (du2023evolutionarydevelopmentalbiology pages 31-33): Zhantao Du. Evolutionary developmental biology in haloarchaea. Text, Jan 2023. URL: https://doi.org/10.48617/etd.674, doi:10.48617/etd.674. This article has 0 citations and is from a peer-reviewed journal.

6. (patro2023“influenceofplasmids pages 7-9): Megha Patro, Iain G. Duggin, Sonja-Verena Albers, and Solenne Ithurbide. “influence of plasmids, selection markers and auxotrophic mutations on haloferax volcanii cell shape plasticity”. Frontiers in Microbiology, Sep 2023. URL: https://doi.org/10.3389/fmicb.2023.1270665, doi:10.3389/fmicb.2023.1270665. This article has 8 citations and is from a peer-reviewed journal.

7. (gambelli2021thepolygonalcell pages 9-10): Lavinia Gambelli, Rob Mesman, Wouter Versantvoort, Christoph A. Diebolder, Andreas Engel, Wiel Evers, Mike S. M. Jetten, Martin Pabst, Bertram Daum, and Laura van Niftrik. The polygonal cell shape and surface protein layer of anaerobic methane-oxidizing methylomirabilis lanthanidiphila bacteria. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.766527, doi:10.3389/fmicb.2021.766527. This article has 3 citations and is from a peer-reviewed journal.

8. (gambelli2021thepolygonalcell pages 13-14): Lavinia Gambelli, Rob Mesman, Wouter Versantvoort, Christoph A. Diebolder, Andreas Engel, Wiel Evers, Mike S. M. Jetten, Martin Pabst, Bertram Daum, and Laura van Niftrik. The polygonal cell shape and surface protein layer of anaerobic methane-oxidizing methylomirabilis lanthanidiphila bacteria. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.766527, doi:10.3389/fmicb.2021.766527. This article has 3 citations and is from a peer-reviewed journal.

9. (schiller2024identificationofstructural pages 3-5): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

10. (schiller2024identificationofstructural pages 6-7): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

11. (patro2024mind2modulatescell pages 10-11): Megha Patro, Felix Grünberger, Shamphavi Sivabalasarma, Sabrina Gfrerer, Marta Rodriguez-Franco, Phillip Nußbaum, Dina Grohmann, Solenne Ithurbide, and Sonja-Verena Albers. Mind2 modulates cell shape and motility in the archaeon haloferax volcanii. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1474570, doi:10.3389/fmicb.2024.1474570. This article has 7 citations and is from a peer-reviewed journal.

12. (patro2024mind2modulatescell pages 5-7): Megha Patro, Felix Grünberger, Shamphavi Sivabalasarma, Sabrina Gfrerer, Marta Rodriguez-Franco, Phillip Nußbaum, Dina Grohmann, Solenne Ithurbide, and Sonja-Verena Albers. Mind2 modulates cell shape and motility in the archaeon haloferax volcanii. Frontiers in Microbiology, Nov 2024. URL: https://doi.org/10.3389/fmicb.2024.1474570, doi:10.3389/fmicb.2024.1474570. This article has 7 citations and is from a peer-reviewed journal.

13. (schiller2024identificationofstructural pages 9-9): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

14. (du2023evolutionarydevelopmentalbiology pages 26-31): Zhantao Du. Evolutionary developmental biology in haloarchaea. Text, Jan 2023. URL: https://doi.org/10.48617/etd.674, doi:10.48617/etd.674. This article has 0 citations and is from a peer-reviewed journal.

15. (schiller2024identificationofstructural pages 11-12): Heather Schiller, Yirui Hong, Joshua Kouassi, Theopi Rados, Jasmin Kwak, Anthony DiLucido, Daniel Safer, Anita Marchfelder, Friedhelm Pfeiffer, Alexandre Bisson, Stefan Schulze, and Mechthild Pohlschroder. Identification of structural and regulatory cell-shape determinants in haloferax volcanii. Nature Communications, Feb 2024. URL: https://doi.org/10.1038/s41467-024-45196-0, doi:10.1038/s41467-024-45196-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

16. (gambelli2021thepolygonalcell pages 10-11): Lavinia Gambelli, Rob Mesman, Wouter Versantvoort, Christoph A. Diebolder, Andreas Engel, Wiel Evers, Mike S. M. Jetten, Martin Pabst, Bertram Daum, and Laura van Niftrik. The polygonal cell shape and surface protein layer of anaerobic methane-oxidizing methylomirabilis lanthanidiphila bacteria. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.766527, doi:10.3389/fmicb.2021.766527. This article has 3 citations and is from a peer-reviewed journal.

17. (gambelli2021thepolygonalcell media 935aa569): Lavinia Gambelli, Rob Mesman, Wouter Versantvoort, Christoph A. Diebolder, Andreas Engel, Wiel Evers, Mike S. M. Jetten, Martin Pabst, Bertram Daum, and Laura van Niftrik. The polygonal cell shape and surface protein layer of anaerobic methane-oxidizing methylomirabilis lanthanidiphila bacteria. Frontiers in Microbiology, Dec 2021. URL: https://doi.org/10.3389/fmicb.2021.766527, doi:10.3389/fmicb.2021.766527. This article has 3 citations and is from a peer-reviewed journal.

18. (bondocnaumovitz2023methodsandmeasures pages 8-9): Karen Grace Bondoc-Naumovitz, Hannah Laeverenz-Schlogelhofer, Rebecca N. Poon, Alexander K. Boggon, Samuel A. Bentley, Dario Cortese, and Kirsty Y. Wan. Methods and measures for investigating microscale motility. Integrative and Comparative Biology, 63:1485-1508, Feb 2023. URL: https://doi.org/10.48550/arxiv.2303.00068, doi:10.48550/arxiv.2303.00068. This article has 17 citations and is from a peer-reviewed journal.