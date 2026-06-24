---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-18T07:20:47.233930'
end_time: '2026-06-18T07:33:36.057362'
duration_seconds: 768.82
template_file: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/TraitMech/templates/trait_causal_graph_research.md
template_variables:
  trait_label: crescent shaped
  trait_identifier: METPO:1000669
  trait_category: MORPHOLOGY
  trait_category_slug: morphology
  trait_slug: crescent_shaped
  term_kind: CLASS
  mapping_status: REVIEWED
  definition: A cell shape in which an organism has a curved crescent-like morphology
    with a concave inner side and a convex outer side.
  parent_traits: METPO:1000666
  synonyms: crescent-shaped
  evidence_summary: 'DOI:10.1016/S0092-8674(03)00935-8: required for the vibrioid
    and helical shapes of Caulobacter (Supports crescentin as a bacterial cytoskeletal
    determinant of curved Caulobacter cell shape.)'
  causal_graph_summary: 'crescent_shaped_crescentin_curvature: 5 nodes, 4 edges'
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Microbial Trait Causal Graph Research Template

## Target Trait
- **Trait label:** crescent shaped
- **METPO identifier:** METPO:1000669
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved crescent-like morphology with a concave inner side and a convex outer side.
- **Parent traits:** METPO:1000666
- **Synonyms:** crescent-shaped
- **Existing evidence:** DOI:10.1016/S0092-8674(03)00935-8: required for the vibrioid and helical shapes of Caulobacter (Supports crescentin as a bacterial cytoskeletal determinant of curved Caulobacter cell shape.)
- **Existing causal graph summary:** crescent_shaped_crescentin_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **crescent shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/crescent_shaped.yaml`.

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
- **Trait label:** crescent shaped
- **METPO identifier:** METPO:1000669
- **Trait category:** MORPHOLOGY
- **Term kind:** CLASS
- **Mapping status:** REVIEWED
- **Definition:** A cell shape in which an organism has a curved crescent-like morphology with a concave inner side and a convex outer side.
- **Parent traits:** METPO:1000666
- **Synonyms:** crescent-shaped
- **Existing evidence:** DOI:10.1016/S0092-8674(03)00935-8: required for the vibrioid and helical shapes of Caulobacter (Supports crescentin as a bacterial cytoskeletal determinant of curved Caulobacter cell shape.)
- **Existing causal graph summary:** crescent_shaped_crescentin_curvature: 5 nodes, 4 edges

## Research Objective

Research the microbial trait **crescent shaped** as a candidate TraitMech causal graph.
Focus on source-backed mechanistic entities and causal edges that can be curated into
`data/traits/morphology/crescent_shaped.yaml`.

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


## Research Report: Microbial Trait “crescent shaped” (METPO:1000669)

### Executive scope summary
The METPO trait **crescent shaped** (METPO:1000669) denotes a **curved, crescent/comma (vibrioid) cell body** with a **concave inner side** and **convex outer side**, typically quantified as curvature of the medial axis in single cells. Mechanistically, this phenotype is produced by **asymmetric envelope growth/remodeling**: one lateral side of the cell wall (peptidoglycan) elongates or is remodeled differently than the opposite side, leading to bending rather than straight rod elongation. Multiple, evolutionarily distinct modules can generate this same geometric outcome: (i) an **intermediate-filament–like cytoskeleton** (crescentin/CreS) that mechanically biases peptidoglycan insertion (Caulobacter), (ii) a **periplasmic curvature polymer module** (CrvAB) (Vibrio), (iii) **asymmetric peptidoglycan-editing enzymes** (e.g., Bd1075 LD-carboxypeptidase) (Bdellovibrio), and (iv) **outer-membrane patterning modules** that cage/retard elongasome motion and bias growth (Por39/Por41–PapS) (Rhodospirillum). (cabeen2009bacterialcellcurvature pages 6-7, fernandez2020vibriocholeraeadapts pages 1-2, banks2022asymmetricpeptidoglycanediting pages 1-2, pohl2024anoutermembrane pages 1-2)

**Boundary cases / nearby traits:**
* **Straight rods** are the immediate contrasting phenotype, frequently produced by deleting key curvature determinants (e.g., ΔcreS, ΔcrvA, Δbd1075, ΔpapS) (cabeen2009bacterialcellcurvature pages 6-7, fernandez2020vibriocholeraeadapts pages 5-6, banks2022asymmetricpeptidoglycanediting pages 1-2, pohl2024anoutermembrane pages 1-2).
* **Helical/spiral morphologies** involve twisting and multiple curvature inflections along the cell length; they can share peptidoglycan-remodeling principles but should generally be curated as distinct traits.
* **Transient mechanically imposed bending** (e.g., confinement) can produce temporary curvature without genetic determinants and should be marked as **environment/assay-imposed** rather than intrinsic morphology (banks2022asymmetricpeptidoglycanediting pages 10-11).

---

## 1) Key concepts and definitions (current understanding)

### Definition and operationalization
* **Crescent-shaped morphology** is best conceptualized as a **non-zero intrinsic curvature** of the rod-like cell body, with stable concave/convex sides across the cell length (METPO:1000669).
* The unifying biophysical mechanism is **differential growth/remodeling of the cell envelope around the circumference**, which creates a **length differential** between the two sides of the cell wall during elongation, causing bending (cabeen2009bacterialcellcurvature pages 6-7, pohl2024anoutermembrane pages 12-13).

### Core mechanistic principle: asymmetric peptidoglycan insertion/remodeling
Caulobacter work provides a canonical statement linking the cytoskeleton to growth asymmetry: “**These results show that the crescentin structure caused differential peptidoglycan insertion rates around the cell circumference to produce cell curvature**.” (cabeen2009bacterialcellcurvature pages 6-7)

---

## 2) Recent developments and latest research (prioritize 2023–2024)

### 2.1 Crescentin structural biology (2024)
A major 2024 advance is direct structural characterization of crescentin filaments:
* Crescentin is “**required for the crescent shape**” and “**forms a filamentous structure on the inner, concave side**” of Caulobacter cells, with cryo-ET showing filaments “**close to the inner membrane, where they form a band**.” (liu2024filamentstructureand pages 1-2)

**Implication for curation:** enables more precise nodes/edges for “crescentin filament/band”, “inner curvature localization”, and “inner membrane–proximal cytoskeletal band” as spatially grounded entities.

### 2.2 A new curvature mechanism: outer-membrane patterning that cages the elongasome (Nature Communications 2024)
Pöhl et al. (2024) identified an outer-membrane module in *Rhodospirillum rubrum*:
* “**Por39 and Por41 form a helical ribbon-like structure at the outer curve of the cell that recruits … PapS**,” and “**PapS inactivation … result[s] in cell straightening**.” (pohl2024anoutermembrane pages 1-2)
* Mechanistically, porin–PapS assemblies “**physically entrap elongasome complexes**” and drive “**localized elevated longitudinal peptidoglycan insertion** … thereby inducing bending.” (pohl2024anoutermembrane pages 12-13)

**Why this is important:** it expands curvature causality beyond cytoskeletal/periplasmic polymers to **outer-membrane spatial patterning** as a driver of asymmetric growth.

### 2.3 Conserved bactofilin–M23 peptidase modules modulate curvature (eLife 2024)
Pöhl et al. (2024, eLife) frame a conserved module:
* “**BacA (a bactofilin) recruits the M23 endopeptidase LmdC**” and “**LmdC’s hydrolytic activity stimulates insertion of new peptidoglycan at the inner curve**,” “**increasing local elongation and straightening the cell**.” (pohl2024adynamicbactofilin pages 19-21)

**Curation note:** This edge set is valuable for representing **curvature modulation** (increase vs straightening) as distinct from curvature generation.

### 2.4 Bacterial mechanosensing of envelope stress (Scientific Reports 2023)
While not a curvature determinant per se, mechanical regulation of envelope homeostasis is relevant to the broader causal context:
* In *V. cholerae*, “**changes in mechanical stress within the cell envelope are sufficient to stimulate VxrAB signaling in the absence of antibiotics**.” (harper2023mechanicalstimuliactivate pages 1-2)
* “**Removal of the endopeptidase ShyA led to large increases in cell envelope deformation** and substantially increased VxrAB response.” (harper2023mechanicalstimuliactivate pages 1-2)

**Curation note:** Treat as a **contextual/regulatory subgraph** (mechanical load → VxrAB) unless a direct edge to curvature is evidenced.

---

## 3) Current applications and real-world implementations

### 3.1 Lifestyle switching and biofilm formation in *Vibrio cholerae*
Curvature is not always fixed; it can be regulated to fit ecological state:
* Elevated c-di-GMP is reported to straighten cells: “**high c-di-GMP concentrations decrease cell curvature to generate straight rods**.” (fernandez2020vibriocholeraeadapts pages 4-5)
* Mechanistically: “**C-di-GMP Decreases CrvA Expression to Inhibit Curvature**.” (fernandez2020vibriocholeraeadapts pages 2-3)
* Curvature retention can impair biofilm architecture: “**curvature retention caused defects in microcolony formation and mature biofilm production**.” (fernandez2020vibriocholeraeadapts pages 4-5)

These findings support a real-world implementation in which *V. cholerae* uses morphology as an adaptive parameter coupling signaling (c-di-GMP) to biofilm growth.

### 3.2 Predation and invasion fitness in *Bdellovibrio bacteriovorus*
Curvature can be directly tied to ecological performance:
* The LD-carboxypeptidase Bd1075 “**generates cell curvature**” via asymmetric peptidoglycan editing, and **Δbd1075 yields straight rods** (banks2022asymmetricpeptidoglycanediting pages 1-2).
* Environmental geometry can transiently impose curvature even on mutants: Δbd1075 rods “become curved inside spherical prey but revert to rods upon release,” indicating a mechanical/assay-imposed curvature component (banks2022asymmetricpeptidoglycanediting pages 10-11).

---

## 4) Expert opinions and analysis (authoritative sources)

### 4.1 Mechanical control model as an interpretive framework
The Caulobacter crescentin literature explicitly advances a mechanical-growth interpretation: crescentin is “required” and biases growth by a rate gradient around the circumference, with differential PG insertion rates being sufficient to “produce cell curvature” (cabeen2009bacterialcellcurvature pages 6-7, cabeen2009bacterialcellcurvature pages 1-2). This provides a generalizable causal abstraction: **spatially patterned envelope synthesis/remodeling → curvature**.

### 4.2 Outer-membrane patterning expands the repertoire of morphogenetic control
The 2024 *R. rubrum* porin–PapS module suggests a distinct “roadblock/caging” control of elongasome mobility and processivity at the outer curve (pohl2024anoutermembrane pages 12-13). This is an expert-level conceptual expansion: curvature can arise not only from force-bearing cytoskeletons or asymmetric enzymes, but also from **spatiotemporal regulation of enzyme movement**.

---

## 5) Relevant statistics and data from recent studies

Quantitative/statistical statements extractable from retrieved sources include:
* *V. cholerae* **c-di-GMP does not measurably alter crvA transcription** (reporter slope difference 95% credible interval [−0.11, 0.10]) (fernandez2020vibriocholeraeadapts pages 2-3).
* Under high c-di-GMP conditions, “**crvA mRNA was ∼1.5-fold less abundant**” (fernandez2020vibriocholeraeadapts pages 2-3).
* ΔcrvA exhibits a “**fourfold change in curvature**” relative to wild type (fernandez2020vibriocholeraeadapts pages 5-6).
* Inducing c-di-GMP synthesis (via active DGC) decreased curvature with **P < 1e−3**, supporting a strong statistical association between elevated c-di-GMP and straightening (fernandez2020vibriocholeraeadapts pages 1-2).

---

# Curation-focused outputs

## Candidate nodes (grouped) 
The following artifact lists candidate nodes for a TraitMech causal graph, with suggested grounding where clear.

| Group | Suggested label | Type | Suggested grounding | Brief supporting evidence reference |
|---|---|---|---|---|
| Trait/phenotype | crescent shaped | trait/phenotype | METPO:1000669 | Defined by curved crescent-like morphology; mechanistically exemplified by Caulobacter crescentus crescentin-dependent curvature and related curved-rod systems (liu2024filamentstructureand pages 1-2, cabeen2009bacterialcellcurvature pages 6-7) |
| Trait/phenotype | straight rod morphology | trait/phenotype |  | Loss of curvature after deleting creS, crvA, bd1075, or papS/porin function supports straight rod as the relevant contrasting phenotype (cabeen2009bacterialcellcurvature pages 6-7, fernandez2020vibriocholeraeadapts pages 1-2, banks2022asymmetricpeptidoglycanediting pages 2-4, pohl2024anoutermembrane pages 12-13) |
| Taxa | Caulobacter crescentus | taxon | NCBITaxon:155892 | Model crescent-shaped alphaproteobacterium; crescentin/CreS required for curvature (liu2024filamentstructureand pages 1-2, cabeen2009bacterialcellcurvature pages 6-7) |
| Taxa | Vibrio cholerae | taxon | NCBITaxon:666 | Curvature generated by CrvA/CrvB and modulated by c-di-GMP signaling (fernandez2020vibriocholeraeadapts pages 1-2, fernandez2020vibriocholeraeadapts pages 2-3) |
| Taxa | Rhodospirillum rubrum | taxon | NCBITaxon:1085 | 2024 work identified Por39/Por41–PapS outer-membrane module and BacA/LmdC curvature mechanisms (pohl2024anoutermembrane pages 1-2, pohl2024adynamicbactofilin pages 19-21, pohl2024anoutermembrane pages 12-13) |
| Taxa | Bdellovibrio bacteriovorus | taxon | NCBITaxon:959 | Bd1075 LD-carboxypeptidase generates vibrioid/crescent curvature (banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 1-2) |
| Genes/Proteins/Complexes | crescentin (CreS) | protein |  | Intermediate filament-like protein required for Caulobacter curvature; localizes on inner concave side near inner membrane (liu2024filamentstructureand pages 1-2, cabeen2009bacterialcellcurvature pages 6-7) |
| Genes/Proteins/Complexes | CrvA | protein |  | Periplasmic curvature determinant in V. cholerae; required for normal curvature and downregulated when cells straighten (fernandez2020vibriocholeraeadapts pages 2-3, fernandez2020vibriocholeraeadapts pages 1-2) |
| Genes/Proteins/Complexes | CrvB | protein |  | Works with CrvA; CrvAB together sufficient to produce curvature in normally straight cells (fernandez2020vibriocholeraeadapts pages 1-2, martin2020theevolutionof pages 5-9) |
| Genes/Proteins/Complexes | CrvAB complex/module | protein complex/module |  | Periplasmic curvature-inducing module sufficient for curvature in V. cholerae and heterologous systems (fernandez2020vibriocholeraeadapts pages 1-2, martin2020theevolutionof pages 5-9) |
| Genes/Proteins/Complexes | Por39 | outer-membrane porin |  | One of two porins forming outer-curve helical ribbon that recruits PapS and promotes curvature in R. rubrum (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13) |
| Genes/Proteins/Complexes | Por41 | outer-membrane porin |  | Partner porin in Por39/Por41 asymmetric assemblies at outer curve (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13) |
| Genes/Proteins/Complexes | PapS | lipoprotein |  | Peptidoglycan-binding lipoprotein recruited by porins; loss causes cell straightening (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13) |
| Genes/Proteins/Complexes | BacA | bactofilin cytoskeletal protein |  | Bactofilin that recruits/works with LmdC to modulate curvature in R. rubrum; curvature determinant in related systems (pohl2024adynamicbactofilin pages 19-21, pohl2024adynamicbactofilin pages 27-28) |
| Genes/Proteins/Complexes | LmdC | M23 endopeptidase |  | Cooperates with BacA; localized PG remodeling modulates degree of curvature (pohl2024adynamicbactofilin pages 19-21) |
| Genes/Proteins/Complexes | Bd1075 | LD-carboxypeptidase |  | Asymmetrically localized PG-editing enzyme required for curved Bdellovibrio shape (banks2022asymmetricpeptidoglycanediting pages 2-4, banks2022asymmetricpeptidoglycanediting pages 10-11) |
| Genes/Proteins/Complexes | MreB | actin-like cytoskeletal protein |  | Linked to crescentin attachment and elongasome-guided wall insertion that influences curvature (cabeen2009bacterialcellcurvature pages 1-2, pohl2024adynamicbactofilin pages 27-28) |
| Genes/Proteins/Complexes | RodZ | elongasome component |  | Used as elongasome marker; outer-curve PapS assemblies reduce RodZ mobility to bias growth and produce curvature (pohl2024anoutermembrane pages 12-13) |
| Genes/Proteins/Complexes | VxrAB | two-component system |  | Envelope-stress/mechanosensitive regulatory system in V. cholerae responding to deformation; relevant upstream regulator of curvature-associated envelope responses (harper2023mechanicalstimuliactivate pages 1-2, herzog2020smallregulatoryrnas pages 37-43) |
| Genes/Proteins/Complexes | ShyA | endopeptidase |  | Removal reduces cell-envelope stiffness and increases VxrAB mechanosensitive response (harper2023mechanicalstimuliactivate pages 1-2) |
| Genes/Proteins/Complexes | VpsR | transcription factor |  | Required for c-di-GMP-mediated reduction of V. cholerae curvature via crvA regulation (fernandez2020vibriocholeraeadapts pages 2-3, fernandez2020vibriocholeraeadapts pages 1-2) |
| Genes/Proteins/Complexes | VpsT | transcription factor |  | c-di-GMP-dependent factor sufficient to inhibit curvature under permissive signaling conditions (fernandez2020vibriocholeraeadapts pages 4-5, fernandez2020vibriocholeraeadapts pages 2-3) |
| Genes/Proteins/Complexes | WbqL / LPS biosynthesis pathway | enzyme/pathway component |  | LPS biosynthesis defects interfere with crescentin envelope attachment and abolish curvature in Caulobacter (cabeen2010mutationsinthe pages 1-2, sundararajan2017cytoskeletalproteinsin pages 16-17) |
| Processes/Functions | peptidoglycan insertion | biological process | GO:0009252 | Differential/localized PG insertion around sidewall produces curvature in Caulobacter and R. rubrum (cabeen2009bacterialcellcurvature pages 6-7, pohl2024anoutermembrane pages 12-13) |
| Processes/Functions | peptidoglycan hydrolysis/remodeling | biological process | GO:0009253 | Local wall hydrolysis/remodeling by LmdC and Bd1075 changes local growth/compliance to modulate curvature (pohl2024adynamicbactofilin pages 19-21, banks2022asymmetricpeptidoglycanediting pages 10-11) |
| Processes/Functions | cell wall organization or biogenesis | biological process | GO:0071555 | Broad process repeatedly implicated in curvature generation across taxa (cabeen2009bacterialcellcurvature pages 1-2, pohl2024anoutermembrane pages 1-2) |
| Processes/Functions | elongasome movement/processivity | biological process |  | Porin–PapS assemblies entrap elongasome complexes and bias their mobility to the outer curve (pohl2024anoutermembrane pages 12-13) |
| Processes/Functions | mechanical control of cell growth | biological process |  | Crescentin imposes strain causing anisotropic wall growth in Caulobacter; external force can also bias growth (cabeen2009bacterialcellcurvature pages 1-2, cabeen2009bacterialcellcurvature pages 6-7) |
| Processes/Functions | regulation of crvA expression | regulatory process |  | c-di-GMP decreases CrvA expression to inhibit curvature in V. cholerae (fernandez2020vibriocholeraeadapts pages 2-3, fernandez2020vibriocholeraeadapts pages 1-2) |
| Cellular locations | inner/concave cell curvature | cellular location | GO:0030420 | Crescentin and CrvAB localize along inner concave side where they promote curvature or constrain growth (liu2024filamentstructureand pages 1-2, martin2020theevolutionof pages 5-9) |
| Cellular locations | outer/convex cell face | cellular location |  | Bd1075 localizes to outer convex face; Por39/Por41–PapS assemblies occupy outer curve in R. rubrum (banks2022asymmetricpeptidoglycanediting pages 2-4, pohl2024anoutermembrane pages 12-13) |
| Cellular locations | inner membrane proximal band | cellular location | GO:0005886 | Crescentin forms a membrane-proximal band near the inner membrane (liu2024filamentstructureand pages 1-2, sundararajan2017cytoskeletalproteinsin pages 16-17) |
| Cellular locations | periplasm | cellular location | GO:0042597 | CrvA/CrvB function as periplasmic curvature module; PapS is periplasmic lipoprotein (fernandez2020vibriocholeraeadapts pages 1-2, pohl2024anoutermembrane pages 1-2) |
| Cellular locations | outer membrane | cellular location | GO:0019867 | Por39/Por41 patterning in outer membrane regulates intracellular growth machinery (pohl2024anoutermembrane pages 1-2, pohl2024anoutermembrane pages 12-13) |
| Chemicals/signals | cyclic di-GMP | chemical/signal | CHEBI:49537 | Elevated c-di-GMP straightens V. cholerae by decreasing CrvA expression (fernandez2020vibriocholeraeadapts pages 2-3, fernandez2020vibriocholeraeadapts pages 1-2) |
| Chemicals/signals | peptidoglycan | chemical/polymer |  | Growth/remodeling substrate whose asymmetric insertion/editing generates curvature (cabeen2009bacterialcellcurvature pages 6-7, banks2022asymmetricpeptidoglycanediting pages 2-4) |
| Chemicals/signals | lipopolysaccharide (LPS) | chemical/polymer | CHEBI:16412 | Proper LPS biosynthesis supports crescentin-mediated curvature in Caulobacter (cabeen2010mutationsinthe pages 1-2, sundararajan2017cytoskeletalproteinsin pages 16-17) |
| Environmental/mechanical factors | mechanical loading / envelope stress | environmental/mechanical factor |  | Extrusion, compression, and hydrostatic pressure activate VxrAB in V. cholerae (harper2023mechanicalstimuliactivate pages 1-2) |
| Environmental/mechanical factors | reduced cell-envelope stiffness | environmental/mechanical factor |  | ShyA loss increases deformation and VxrAB signaling; supports role of mechanics in envelope homeostasis relevant to shape control (harper2023mechanicalstimuliactivate pages 1-2) |
| Environmental/mechanical factors | physical confinement / prey bdelloplast geometry | environmental/mechanical factor |  | Δbd1075 rods can transiently curve inside spherical prey, indicating geometry/mechanics can modulate curvature (banks2022asymmetricpeptidoglycanediting pages 10-11) |
| Environmental/mechanical factors | external physical force on growing cells | environmental/mechanical factor |  | Chamber-wall force biases growth and induces curvature in Caulobacter mechanical model experiments (cabeen2009bacterialcellcurvature pages 6-7) |


*Table: This table lists candidate nodes for a TraitMech-style causal graph for the microbial trait 'crescent shaped' (METPO:1000669). It groups taxa, determinants, processes, locations, signals, and mechanical factors with suggested ontology grounding and supporting evidence citations.*

## Candidate evidence-backed causal edges (triples)
The following artifact provides curated subject–predicate–object candidates with verbatim evidence snippets, DOI-first references, and curation notes.

| Edge (S–P–O) | Evidence snippet (verbatim from sources) | Reference (DOI + URL + year/month) | Notes for curation (taxon specificity, uncertainty, mechanism) | Suggested node groundings (CURIEs where possible) |
|---|---|---|---|---|
| crescentin (CreS) — required_for — crescent shaped morphology | “the intermediate filament-like protein crescentin is required for the crescent shape of *Caulobacter crescentus*” (cabeen2009bacterialcellcurvature pages 6-7, liu2024filamentstructureand pages 1-2) | Cabeen et al. 2009, doi:10.1038/emboj.2009.61, https://doi.org/10.1038/emboj.2009.61, 2009-05; Liu et al. 2024, doi:10.1073/pnas.2309984121, https://doi.org/10.1073/pnas.2309984121, 2024-02 | Strong, direct genetic evidence in *Caulobacter crescentus*; suitable core edge for a taxon-specific subgraph. Mechanism is cytoskeletal constraint. | CreS/crescentin [label]; NCBITaxon:155892; METPO:1000669 |
| crescentin filament/band — located_at — inner/concave cell curvature | “Crescentin forms a filamentous structure on the inner, concave side of the curved cells.” (liu2024filamentstructureand pages 1-2) | Liu et al. 2024, doi:10.1073/pnas.2309984121, https://doi.org/10.1073/pnas.2309984121, 2024-02 | Strong localization edge; supports spatial mechanism. | crescentin [label]; inner cell curvature [label] |
| crescentin filament/band — adjacent_to — inner membrane | “Electron cryotomography (cryo-ET) of cells expressing crescentin showed filaments on the concave side of the curved cells, close to the inner membrane, where they form a band.” (liu2024filamentstructureand pages 1-2) | Liu et al. 2024, doi:10.1073/pnas.2309984121, https://doi.org/10.1073/pnas.2309984121, 2024-02 | Strong structural/localization evidence; may support membrane-proximal node. | crescentin [label]; GO:0005886 |
| crescentin — decreases_rate_of — peptidoglycan insertion at inner curvature | “the crescentin structure would not only reduce peptidoglycan insertion at the side where crescentin is located but would also generate a gradient of increasing peptidoglycan growth rates” (cabeen2009bacterialcellcurvature pages 6-7) | Cabeen et al. 2009, doi:10.1038/emboj.2009.61, https://doi.org/10.1038/emboj.2009.61, 2009-05 | Mechanistic growth-bias model with experimental sacculus support; appropriate but still model-framed. Mark as moderate confidence if requiring purely direct biochemical causality. | crescentin [label]; GO:0009252 |
| differential peptidoglycan insertion rates — produces — crescent shaped morphology | “These results show that the crescentin structure caused differential peptidoglycan insertion rates around the cell circumference to produce cell curvature.” (cabeen2009bacterialcellcurvature pages 6-7) | Cabeen et al. 2009, doi:10.1038/emboj.2009.61, https://doi.org/10.1038/emboj.2009.61, 2009-05 | Strong process-to-phenotype edge in *Caulobacter*; broadly useful mechanistic abstraction. | GO:0009252; METPO:1000669 |
| LPS biosynthesis / wbqL — enables — crescentin envelope association | “Mutations in the LPS biosynthesis pathway (wbqL) disrupt envelope components ... and can abolish curvature by interfering with crescentin’s ability to associate with the envelope” (cabeen2010mutationsinthe pages 1-2) | Cabeen et al. 2010, doi:10.1128/jb.01371-09, https://doi.org/10.1128/jb.01371-09, 2010-07 | Good upstream envelope-dependence edge; taxon-specific to *Caulobacter*. | wbqL [label]; CHEBI:16412; crescentin [label] |
| crescentin envelope association — required_for — crescent shaped morphology | “Envelope association is required for crescentin function (attachment-defective mutants fail to produce curvature)” (cabeen2010mutationsinthe pages 1-2) | Cabeen et al. 2010, doi:10.1128/jb.01371-09, https://doi.org/10.1128/jb.01371-09, 2010-07 | Strong mechanistic edge connecting localization/attachment to phenotype. | crescentin envelope association [label]; METPO:1000669 |
| CrvAB module — sufficient_for — cell curvature | “the adjacent ORF to crvA, annotated as crvB, functions with CrvA and, together, CrvAB are sufficient to produce curvature in normally straight cells” (fernandez2020vibriocholeraeadapts pages 1-2) | Fernandez et al. 2020, doi:10.1073/pnas.2010199117, https://doi.org/10.1073/pnas.2010199117, 2020-11 | Strong sufficiency statement for *Vibrio cholerae* module; suitable taxon-specific edge. | CrvA [label]; CrvB [label]; CrvAB complex [label] |
| CrvA — required_for — curved/vibrioid morphology | “the primary morphological difference of the ΔcrvA mutant is a fourfold change in curvature” (fernandez2020vibriocholeraeadapts pages 5-6) | Fernandez et al. 2020, doi:10.1073/pnas.2010199117, https://doi.org/10.1073/pnas.2010199117, 2020-11 | Strong deletion phenotype in *V. cholerae*; direct and curatable. | CrvA [label]; NCBITaxon:666; METPO:1000669 |
| cyclic di-GMP — decreases_expression_of — crvA | “C-di-GMP Decreases CrvA Expression to Inhibit Curvature.” (fernandez2020vibriocholeraeadapts pages 2-3) | Fernandez et al. 2020, doi:10.1073/pnas.2010199117, https://doi.org/10.1073/pnas.2010199117, 2020-11 | Strong regulatory edge; useful if c-di-GMP included as upstream signal node. | CHEBI:49537; crvA [label] |
| elevated cyclic di-GMP — decreases — cell curvature / straightens cells | “high c-di-GMP concentrations decrease cell curvature to generate straight rods” (fernandez2020vibriocholeraeadapts pages 4-5) | Fernandez et al. 2020, doi:10.1073/pnas.2010199117, https://doi.org/10.1073/pnas.2010199117, 2020-11 | Strong phenotype-regulation edge in *V. cholerae*; opposite of target trait but highly informative. | CHEBI:49537; straight rod morphology [label] |
| VpsR — required_for — c-di-GMP-mediated reduction of curvature | “The c-di-GMP-mediated decrease in curvature… was lost in the ΔvpsR mutant” (fernandez2020vibriocholeraeadapts pages 2-3) | Fernandez et al. 2020, doi:10.1073/pnas.2010199117, https://doi.org/10.1073/pnas.2010199117, 2020-11 | Regulatory edge; mechanism is indirect through c-di-GMP-responsive transcription. | VpsR [label]; CHEBI:49537 |
| VpsT — inhibits — cell curvature | “VpsT (a c-di-GMP-dependent transcription factor) is sufficient to inhibit curvature” (fernandez2020vibriocholeraeadapts pages 5-6) | Fernandez et al. 2020, doi:10.1073/pnas.2010199117, https://doi.org/10.1073/pnas.2010199117, 2020-11 | Good regulatory edge; note dependence on c-di-GMP context. | VpsT [label]; METPO:1000669 |
| mechanical loading — activates — VxrAB signaling | “changes in mechanical stress within the cell envelope are sufficient to stimulate VxrAB signaling in the absence of antibiotics” (harper2023mechanicalstimuliactivate pages 1-2) | Harper et al. 2023, doi:10.1038/s41598-023-40897-w, https://doi.org/10.1038/s41598-023-40897-w, 2023-08 | Strong mechanical-response edge in *V. cholerae*; not direct curvature generation, so better curated as contextual/modulatory rather than core trait edge. | mechanical loading [label]; VxrAB [label] |
| loss of ShyA — increases — cell envelope deformation | “Removal of the endopeptidase ShyA led to large increases in cell envelope deformation” (harper2023mechanicalstimuliactivate pages 1-2) | Harper et al. 2023, doi:10.1038/s41598-023-40897-w, https://doi.org/10.1038/s41598-023-40897-w, 2023-08 | Strong envelope mechanics edge; indirect relevance to curvature/mechanosensing. | ShyA [label]; cell envelope deformation [label] |
| loss of ShyA — activates — VxrAB signaling | “Removal of the endopeptidase ShyA led to large increases in cell envelope deformation and substantially increased VxrAB response” (harper2023mechanicalstimuliactivate pages 1-2) | Harper et al. 2023, doi:10.1038/s41598-023-40897-w, https://doi.org/10.1038/s41598-023-40897-w, 2023-08 | Strong mechanosensory edge; likely contextual rather than core curvature determinant. | ShyA [label]; VxrAB [label] |
| Por39/Por41 helical ribbon — recruits — PapS | “the R. rubrum porins Por39 and Por41 form a helical ribbon-like structure at the outer curve of the cell that recruits the peptidoglycan-binding lipoprotein PapS” (pohl2024anoutermembrane pages 1-2) | Pöhl et al. 2024, doi:10.1038/s41467-024-51790-z, https://doi.org/10.1038/s41467-024-51790-z, 2024-09 | Strong outer-membrane patterning edge in *Rhodospirillum rubrum*. | Por39 [label]; Por41 [label]; PapS [label] |
| PapS inactivation — causes — cell straightening | “with PapS inactivation ... resulting in cell straightening” (pohl2024anoutermembrane pages 1-2) | Pöhl et al. 2024, doi:10.1038/s41467-024-51790-z, https://doi.org/10.1038/s41467-024-51790-z, 2024-09 | Strong negative evidence linking loss of module to loss of curvature. | PapS [label]; straight rod morphology [label] |
| porin–PapS assemblies — entrap — elongasome complexes | “The porin–PapS assemblies form high-density, membrane-associated structures that physically entrap elongasome complexes” (pohl2024anoutermembrane pages 12-13) | Pöhl et al. 2024, doi:10.1038/s41467-024-51790-z, https://doi.org/10.1038/s41467-024-51790-z, 2024-09 | Strong mechanism edge for outer-membrane control of wall synthesis dynamics. | Por39/Por41–PapS assembly [label]; elongasome [label] |
| porin–PapS assemblies — bias — peptidoglycan insertion toward outer curve | “thereby inducing bending” and “causing localized elevated longitudinal peptidoglycan insertion where assemblies reside” (pohl2024anoutermembrane pages 12-13) | Pöhl et al. 2024, doi:10.1038/s41467-024-51790-z, https://doi.org/10.1038/s41467-024-51790-z, 2024-09 | Strong mechanistic edge; directly relevant to curvature generation. | Por39/Por41–PapS assembly [label]; GO:0009252 |
| BacA — recruits — LmdC | “In R. rubrum, BacA (a bactofilin) recruits the M23 endopeptidase LmdC” (pohl2024adynamicbactofilin pages 19-21) | Pöhl et al. 2024, doi:10.7554/elife.86577.2, https://doi.org/10.7554/elife.86577.2, 2024-01 | Strong but from eLife/ArXiv-linked version; acceptable with note. | BacA [label]; LmdC [label] |
| LmdC hydrolytic activity — stimulates — peptidoglycan insertion at inner curve | “LmdC’s hydrolytic activity stimulates insertion of new peptidoglycan at the inner curve” (pohl2024adynamicbactofilin pages 19-21) | Pöhl et al. 2024, doi:10.7554/elife.86577.2, https://doi.org/10.7554/elife.86577.2, 2024-01 | Strong mechanistic edge in *R. rubrum*; links PG remodeling to curvature modulation. | LmdC [label]; GO:0009252 |
| localized inner-curve peptidoglycan insertion — straightens/modulates — cell curvature | “increasing local elongation and straightening the cell” (pohl2024adynamicbactofilin pages 19-21) | Pöhl et al. 2024, doi:10.7554/elife.86577.2, https://doi.org/10.7554/elife.86577.2, 2024-01 | Useful for representing directionality of curvature modulation; taxon-specific. | GO:0009252; cell curvature [label] |
| Bd1075 — localizes_to — outer convex face | “Bd1075 localizes asymmetrically to the outer convex face via a C-terminal NTF2-like domain” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Banks et al. 2022, doi:10.1038/s41467-022-29007-y, https://doi.org/10.1038/s41467-022-29007-y, 2022-03 | Strong localization edge in *Bdellovibrio bacteriovorus*. | Bd1075 [label]; outer convex cell face [label] |
| Bd1075 LD-carboxypeptidase activity — generates — cell curvature | “Bd1075 ... acts as an LD-carboxypeptidase on the predator cell wall ... this asymmetric PG editing produces cell curvature” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Banks et al. 2022, doi:10.1038/s41467-022-29007-y, https://doi.org/10.1038/s41467-022-29007-y, 2022-03 | Strong enzyme-to-phenotype edge; distinct PG-editing mechanism. | Bd1075 [label]; EC/LD-carboxypeptidase [label]; METPO:1000669 |
| deletion of bd1075 — causes — straight rod morphology | “deletion of bd1075 yields straight rod-shaped cells” (banks2022asymmetricpeptidoglycanediting pages 1-2) | Banks et al. 2022, doi:10.1038/s41467-022-29007-y, https://doi.org/10.1038/s41467-022-29007-y, 2022-03 | Strong loss-of-function evidence; direct contrast phenotype. | bd1075 [label]; straight rod morphology [label] |


*Table: This table compiles evidence-backed subject–predicate–object edges for curation of a crescent-shaped microbial trait causal graph. It spans multiple taxa and mechanism classes, with verbatim snippets, DOI-first references, curation notes, and suggested node groundings.*

---

## Warnings / claims not yet suitable for curation
1. **Mechanosensing → curvature**: While VxrAB is mechanosensitive and responds to envelope deformation (harper2023mechanicalstimuliactivate pages 1-2), the retrieved evidence does not directly demonstrate that VxrAB activation *causes* crescent-shaped morphology; this should be curated only as a stress-response subgraph unless direct curvature effects are sourced.
2. **Broad generalizations across taxa**: Several mechanisms are explicitly taxon-specific (e.g., crescentin/CreS in Caulobacter; Bd1075 in Bdellovibrio; Por39/Por41–PapS in R. rubrum). Cross-taxon edges should be marked **inferred** unless heterologous sufficiency is directly shown (CrvAB has explicit sufficiency evidence across hosts in some literature, but not all such primary sources were obtainable here).
3. **Edges phrased as models**: Some crescentin→PG insertion edges are partially mechanistic models supported by sacculus labeling and growth experiments; if the curation standard requires only direct biochemical causality, mark these edges **moderate confidence/model-supported** (cabeen2009bacterialcellcurvature pages 6-7).

---

# DOI-first bibliography (with URLs and publication dates)

* Liu Y, van den Ent F, Löwe J. **Filament structure and subcellular organization of the bacterial intermediate filament–like protein crescentin.** *PNAS* (2024-02). DOI: **10.1073/pnas.2309984121**. https://doi.org/10.1073/pnas.2309984121 (liu2024filamentstructureand pages 1-2)
* Pöhl S et al. **An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in Rhodospirillum rubrum.** *Nature Communications* (2024-09). DOI: **10.1038/s41467-024-51790-z**. https://doi.org/10.1038/s41467-024-51790-z (pohl2024anoutermembrane pages 1-2)
* Pöhl S et al. **A dynamic bactofilin cytoskeleton cooperates with an M23 endopeptidase to control bacterial morphogenesis.** (eLife version) (2024-01). DOI: **10.7554/elife.86577.2**. https://doi.org/10.7554/elife.86577.2 (pohl2024adynamicbactofilin pages 19-21)
* Harper CE et al. **Mechanical stimuli activate gene expression via a cell envelope stress sensing pathway.** *Scientific Reports* (2023-08). DOI: **10.1038/s41598-023-40897-w**. https://doi.org/10.1038/s41598-023-40897-w (harper2023mechanicalstimuliactivate pages 1-2)
* Fernandez NL et al. **Vibrio cholerae adapts to sessile and motile lifestyles by cyclic di-GMP regulation of cell shape.** *PNAS* (2020-11). DOI: **10.1073/pnas.2010199117**. https://doi.org/10.1073/pnas.2010199117 (fernandez2020vibriocholeraeadapts pages 2-3)
* Banks EJ et al. **Asymmetric peptidoglycan editing generates cell curvature in Bdellovibrio predatory bacteria.** *Nature Communications* (2022-03). DOI: **10.1038/s41467-022-29007-y**. https://doi.org/10.1038/s41467-022-29007-y (banks2022asymmetricpeptidoglycanediting pages 1-2)
* Cabeen MT et al. **Bacterial cell curvature through mechanical control of cell growth.** *The EMBO Journal* (2009-05). DOI: **10.1038/emboj.2009.61**. https://doi.org/10.1038/emboj.2009.61 (cabeen2009bacterialcellcurvature pages 6-7)
* Cabeen MT et al. **Mutations in the Lipopolysaccharide Biosynthesis Pathway Interfere with Crescentin-Mediated Cell Curvature in Caulobacter crescentus.** *Journal of Bacteriology* (2010-07). DOI: **10.1128/jb.01371-09**. https://doi.org/10.1128/jb.01371-09 (cabeen2010mutationsinthe pages 1-2)



References

1. (cabeen2009bacterialcellcurvature pages 6-7): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 208 citations.

2. (fernandez2020vibriocholeraeadapts pages 1-2): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 51 citations and is from a highest quality peer-reviewed journal.

3. (banks2022asymmetricpeptidoglycanediting pages 1-2): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 31 citations and is from a highest quality peer-reviewed journal.

4. (pohl2024anoutermembrane pages 1-2): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

5. (fernandez2020vibriocholeraeadapts pages 5-6): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 51 citations and is from a highest quality peer-reviewed journal.

6. (banks2022asymmetricpeptidoglycanediting pages 10-11): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 31 citations and is from a highest quality peer-reviewed journal.

7. (pohl2024anoutermembrane pages 12-13): Sebastian Pöhl, Giacomo Giacomelli, Fabian M. Meyer, Volker Kleeberg, Eli J. Cohen, Jacob Biboy, Julia Rosum, Timo Glatter, Waldemar Vollmer, Muriel C. F. van Teeseling, Johann Heider, Marc Bramkamp, and Martin Thanbichler. An outer membrane porin-lipoprotein complex modulates elongasome movement to establish cell curvature in rhodospirillum rubrum. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-51790-z, doi:10.1038/s41467-024-51790-z. This article has 7 citations and is from a highest quality peer-reviewed journal.

8. (liu2024filamentstructureand pages 1-2): Yue Liu, Fusinita van den Ent, and Jan Löwe. Filament structure and subcellular organization of the bacterial intermediate filament–like protein crescentin. Proceedings of the National Academy of Sciences, Feb 2024. URL: https://doi.org/10.1073/pnas.2309984121, doi:10.1073/pnas.2309984121. This article has 7 citations and is from a highest quality peer-reviewed journal.

9. (pohl2024adynamicbactofilin pages 19-21): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

10. (harper2023mechanicalstimuliactivate pages 1-2): Christine E. Harper, Wenyao Zhang, Junsung Lee, Jung-Ho Shin, Megan R. Keller, Ellen van Wijngaarden, Emily Chou, Zhaohong Wang, Tobias Dörr, Peng Chen, and Christopher J. Hernandez. Mechanical stimuli activate gene expression via a cell envelope stress sensing pathway. Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-40897-w, doi:10.1038/s41598-023-40897-w. This article has 26 citations and is from a peer-reviewed journal.

11. (fernandez2020vibriocholeraeadapts pages 4-5): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 51 citations and is from a highest quality peer-reviewed journal.

12. (fernandez2020vibriocholeraeadapts pages 2-3): Nicolas L. Fernandez, Brian Y. Hsueh, Nguyen T. Q. Nhu, Joshua L. Franklin, Yann S. Dufour, and Christopher M. Waters. <i>vibrio cholerae</i> adapts to sessile and motile lifestyles by cyclic di-gmp regulation of cell shape. Nov 2020. URL: https://doi.org/10.1073/pnas.2010199117, doi:10.1073/pnas.2010199117. This article has 51 citations and is from a highest quality peer-reviewed journal.

13. (cabeen2009bacterialcellcurvature pages 1-2): Matthew T Cabeen, Godefroid Charbon, Waldemar Vollmer, Petra Born, Nora Ausmees, Douglas B Weibel, and Christine Jacobs-Wagner. Bacterial cell curvature through mechanical control of cell growth. The EMBO Journal, 28:1208-1219, May 2009. URL: https://doi.org/10.1038/emboj.2009.61, doi:10.1038/emboj.2009.61. This article has 208 citations.

14. (banks2022asymmetricpeptidoglycanediting pages 2-4): Emma J. Banks, Mauricio Valdivia-Delgado, Jacob Biboy, Amber Wilson, Ian T. Cadby, Waldemar Vollmer, Carey Lambert, Andrew L. Lovering, and R. Elizabeth Sockett. Asymmetric peptidoglycan editing generates cell curvature in bdellovibrio predatory bacteria. Nature Communications, Mar 2022. URL: https://doi.org/10.1038/s41467-022-29007-y, doi:10.1038/s41467-022-29007-y. This article has 31 citations and is from a highest quality peer-reviewed journal.

15. (martin2020theevolutionof pages 5-9): Nicholas R. Martin, Edith Blackman, Benjamin P. Bratton, Thomas M. Bartlett, and Zemer Gitai. The evolution of bacterial shape complexity by a curvature-inducing module. bioRxiv, Feb 2020. URL: https://doi.org/10.1101/2020.02.20.954503, doi:10.1101/2020.02.20.954503. This article has 4 citations.

16. (pohl2024adynamicbactofilin pages 27-28): Sebastian Pöhl, Manuel Osorio-Valeriano, Emöke Cserti, Jannik Harberding, Rogelio Hernández-Tamayo, Jacob Biboy, Patrick Sobetzko, Waldemar Vollmer, Peter L. Graumann, and Martin Thanbichler. A dynamic bactofilin cytoskeleton cooperates with an m23 endopeptidase to control bacterial morphogenesis. ArXiv, Jan 2024. URL: https://doi.org/10.7554/elife.86577.2, doi:10.7554/elife.86577.2. This article has 8 citations.

17. (herzog2020smallregulatoryrnas pages 37-43): Roman Herzog. Small regulatory rnas controlling complex phenotypes in vibrio cholerae. Dissertation, Jan 2020. URL: https://doi.org/10.5282/edoc.27302, doi:10.5282/edoc.27302. This article has 0 citations.

18. (cabeen2010mutationsinthe pages 1-2): Matthew T. Cabeen, Michelle A. Murolo, Ariane Briegel, N. Khai Bui, Waldemar Vollmer, Nora Ausmees, Grant J. Jensen, and Christine Jacobs-Wagner. Mutations in the lipopolysaccharide biosynthesis pathway interfere with crescentin-mediated cell curvature in <i>caulobacter crescentus</i>. Journal of Bacteriology, 192:3368-3378, Jul 2010. URL: https://doi.org/10.1128/jb.01371-09, doi:10.1128/jb.01371-09. This article has 35 citations and is from a peer-reviewed journal.

19. (sundararajan2017cytoskeletalproteinsin pages 16-17): Kousik Sundararajan and Erin D. Goley. Cytoskeletal proteins in caulobacter crescentus: spatial orchestrators of cell cycle progression, development, and cell shape. Sub-cellular biochemistry, 84:103-137, Jan 2017. URL: https://doi.org/10.1007/978-3-319-53047-5\_4, doi:10.1007/978-3-319-53047-5\_4. This article has 26 citations.